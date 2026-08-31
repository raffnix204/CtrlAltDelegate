#!/usr/bin/env python3
"""CtrlAltDelegate Graphify bootstrap and invocation wrapper.

Host installation is never implicit. `prepare` reports ASK_USER when Graphify is
missing and no persisted host preference exists. `install --scope host` requires
`--consent` and writes only a user-scoped CtrlAltDelegate preference after a
successful smoke test. Project scope uses an isolated venv under the local
CtrlAltDelegate control/runtime root.
"""
from __future__ import annotations
from pathlib import Path
import argparse, hashlib, json, os, platform, shutil, subprocess, sys, venv

ROOT = Path(__file__).resolve().parents[1]
PINNED = "0.9.53"
PACKAGE = f"graphifyy=={PINNED}"

def control_root() -> Path:
    if ROOT.name == ".ctrlaltdelegate":
        return ROOT
    return ROOT / ".ctrlaltdelegate-runtime"

def host_pref_path() -> Path:
    override = os.environ.get("CTRLALTDELEGATE_HOST_CONFIG")
    if override:
        return Path(override).expanduser()
    if platform.system() == "Windows":
        base = Path(os.environ.get("APPDATA") or (Path.home()/"AppData"/"Roaming"))
    else:
        base = Path(os.environ.get("XDG_CONFIG_HOME") or (Path.home()/".config"))
    return base / "ctrlaltdelegate" / "host-tools.json"

def load_pref() -> dict:
    p = host_pref_path()
    if not p.exists():
        return {"version":"5.9.3","tools":{}}
    try:
        d=json.loads(p.read_text(encoding="utf-8"))
        if not isinstance(d,dict): raise ValueError
        d.setdefault("tools",{})
        return d
    except Exception:
        return {"version":"5.9.3","tools":{},"warning":"preference_file_unreadable"}

def save_pref(choice: str) -> None:
    p=host_pref_path(); d=load_pref(); d["version"]="5.9.3"
    d.setdefault("tools",{})["graphify"]={"choice":choice,"pinned_version":PINNED}
    p.parent.mkdir(parents=True,exist_ok=True)
    tmp=p.with_suffix(p.suffix+".tmp"); tmp.write_text(json.dumps(d,indent=2)+"\n",encoding="utf-8"); os.replace(tmp,p)

def project_bin() -> Path:
    base=control_root()/"tools"/"graphify"/"venv"
    return base/("Scripts" if platform.system()=="Windows" else "bin")/("graphify.exe" if platform.system()=="Windows" else "graphify")

def resolve_bin() -> tuple[str|None,str|None]:
    host=shutil.which("graphify")
    if host: return host,"host"
    pb=project_bin()
    if pb.exists(): return str(pb),"project"
    return None,None

def run(cmd:list[str], **kw):
    return subprocess.run(cmd, text=True, **kw)

def version_of(binary:str) -> str|None:
    for args in ([binary,"--version"],[binary,"version"]):
        try:
            r=run(list(args),capture_output=True,timeout=15)
            out=(r.stdout or r.stderr or "").strip()
            if r.returncode==0 and out: return out.splitlines()[0]
        except Exception: pass
    return None

def state_payload() -> dict:
    b,scope=resolve_bin(); pref=load_pref().get("tools",{}).get("graphify",{}).get("choice","UNKNOWN")
    graph=Path.cwd()/"graphify-out"/"graph.json"
    return {"version":"5.9.3","binary":b,"install_scope":scope,"detected_version":version_of(b) if b else None,"pinned_version":PINNED,"host_preference":pref,"graph_exists":graph.exists(),"graph_path":str(graph) if graph.exists() else None}

def install_host() -> str:
    uv=shutil.which("uv"); pipx=shutil.which("pipx")
    if uv:
        run([uv,"tool","install","--upgrade",PACKAGE],check=True)
    elif pipx:
        run([pipx,"install","--force",PACKAGE],check=True)
    else:
        raise RuntimeError("Host install requires uv or pipx; CtrlAltDelegate will not use sudo/system pip.")
    b=shutil.which("graphify")
    if not b: raise RuntimeError("graphify not found on PATH after host install; refresh shell PATH and retry")
    # Generic Agent Skills registration is preferred because OMP and CtrlAltDelegate
    # both discover ~/.agents/skills. Older Graphify builds may only expose `install`.
    registered=False
    for cmd in ([b,"agents","install"],[b,"install"]):
        r=run(list(cmd),capture_output=True)
        if r.returncode==0:
            registered=True; break
    if not registered: raise RuntimeError("Graphify installed but Agent Skills registration failed")
    return b

def install_project() -> str:
    target=project_bin().parent.parent
    target.parent.mkdir(parents=True,exist_ok=True)
    if not target.exists(): venv.EnvBuilder(with_pip=True,clear=False).create(target)
    py=target/("Scripts/python.exe" if platform.system()=="Windows" else "bin/python")
    run([str(py),"-m","pip","install","--upgrade",PACKAGE],check=True)
    b=project_bin()
    if not b.exists(): raise RuntimeError("project-local graphify install did not create CLI")
    return str(b)

def smoke(binary:str) -> dict:
    r=run([binary,"--help"],capture_output=True,timeout=30)
    if r.returncode!=0: raise RuntimeError("graphify --help smoke test failed")
    return {"binary":binary,"version":version_of(binary),"help_sha256":hashlib.sha256((r.stdout+r.stderr).encode()).hexdigest()}

def persist_runtime_state(extra:dict) -> None:
    p=ROOT/"planning/execution/CODE-INTELLIGENCE-STATE.yaml"
    if not p.exists(): return
    # Keep this wrapper dependency-free; append machine-readable JSON note rather
    # than parsing YAML just to record a bootstrap fact.
    note=ROOT/"planning/execution/CODE-INTELLIGENCE-RUNTIME.json"
    payload=state_payload(); payload.update(extra); note.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")

def main() -> int:
    ap=argparse.ArgumentParser()
    sub=ap.add_subparsers(dest="cmd",required=True)
    sub.add_parser("status")
    sub.add_parser("prepare")
    ins=sub.add_parser("install"); ins.add_argument("--scope",choices=["host","project"],required=True); ins.add_argument("--consent",action="store_true")
    pref=sub.add_parser("preference"); pref.add_argument("choice",choices=["HOST_ALWAYS","PROJECT_ONLY","NEVER","ASK"]); pref.add_argument("--consent",action="store_true")
    for name in ["build","update","watch"]:
        p=sub.add_parser(name); p.add_argument("path",nargs="?",default=".")
    q=sub.add_parser("query"); q.add_argument("question",nargs="+")
    pth=sub.add_parser("path"); pth.add_argument("source"); pth.add_argument("target")
    exp=sub.add_parser("explain"); exp.add_argument("node")
    a=ap.parse_args()
    if a.cmd=="status": print(json.dumps(state_payload(),indent=2)); return 0
    if a.cmd=="prepare":
        s=state_payload()
        if s["binary"]: s["action"]="REUSE_AND_VERIFY"
        elif s["host_preference"]=="HOST_ALWAYS": s["action"]="INSTALL_HOST_WITH_RECORDED_CONSENT"
        elif s["host_preference"]=="PROJECT_ONLY": s["action"]="INSTALL_PROJECT_LOCAL"
        elif s["host_preference"]=="NEVER": s["action"]="USE_FALLBACK"
        else: s["action"]="ASK_USER"; s["choices"]=["HOST_ALWAYS","PROJECT_ONLY","NEVER"]
        print(json.dumps(s,indent=2)); return 0
    if a.cmd=="preference":
        if not a.consent: raise SystemExit("--consent is required to persist a host preference")
        save_pref(a.choice); print(json.dumps({"status":"PREFERENCE_SAVED","choice":a.choice,"path":str(host_pref_path())},indent=2)); return 0
    if a.cmd=="install":
        if not a.consent: raise SystemExit("--consent is required for installation")
        b=install_host() if a.scope=="host" else install_project(); evidence=smoke(b)
        if a.scope=="host": save_pref("HOST_ALWAYS")
        persist_runtime_state({"status":"READY","smoke":evidence})
        print(json.dumps({"status":"GRAPHIFY_READY","scope":a.scope,**evidence},indent=2)); return 0
    b,_=resolve_bin()
    if not b: raise SystemExit("Graphify is not installed. Run `graphify_ctl.py prepare` and follow the consent result.")
    if a.cmd=="build": cmd=[b,a.path]
    elif a.cmd=="update": cmd=[b,a.path,"--update"]
    elif a.cmd=="watch": cmd=[b,a.path,"--watch"]
    elif a.cmd=="query": cmd=[b,"query"," ".join(a.question)]
    elif a.cmd=="path": cmd=[b,"path",a.source,a.target]
    else: cmd=[b,"explain",a.node]
    return run(cmd).returncode

if __name__=="__main__": raise SystemExit(main())
