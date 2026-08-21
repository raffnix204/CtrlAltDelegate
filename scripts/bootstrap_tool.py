#!/usr/bin/env python3
from pathlib import Path
import argparse, json, os, platform, shutil, subprocess, tempfile, urllib.request, tarfile, zipfile, hashlib, re
R=Path(__file__).resolve().parents[1]
TOOLS=(R/'tools') if R.name=='.ctrlaltdelegate' else (R/'.ctrlaltdelegate-runtime/tools')
GITHUB={'crw':'us/crw','obscura':'h4ckf0r0day/obscura'}

def arch_tokens():
    m=platform.machine().lower(); s=platform.system().lower()
    arch=['aarch64','arm64'] if m in {'arm64','aarch64'} else ['x86_64','amd64','x64']
    oses={'darwin':['macos','darwin','apple'],'linux':['linux'],'windows':['windows','win']}.get(s,[s])
    return oses,arch

def api_json(url):
    req=urllib.request.Request(url,headers={'User-Agent':'CtrlAltDelegate/5.8'})
    with urllib.request.urlopen(req,timeout=20) as r: return json.load(r)

def download(url,dst):
    req=urllib.request.Request(url,headers={'User-Agent':'CtrlAltDelegate/5.8'})
    with urllib.request.urlopen(req,timeout=60) as r, open(dst,'wb') as f: shutil.copyfileobj(r,f)

def choose_asset(assets):
    oses,archs=arch_tokens(); scored=[]
    for a in assets:
        n=a.get('name','').lower()
        if any(x in n for x in ['sha256','checksum','.sig','attestation','source']): continue
        score=sum(4 for x in oses if x in n)+sum(3 for x in archs if x in n)
        if n.endswith(('.tar.gz','.tgz','.zip','.tar.xz')): score+=2
        if score: scored.append((score,a))
    return max(scored,key=lambda x:x[0])[1] if scored else None

def verify_published_checksum(meta, asset, archive, dest):
    checksum_assets=[a for a in meta.get('assets',[]) if any(x in a.get('name','').lower() for x in ['sha256sum','sha256','checksums','checksum']) and not a.get('name','').lower().endswith(('.sig','.pem'))]
    if not checksum_assets: return {'published':False,'verified':False}
    for ca in checksum_assets:
        try:
            cp=dest/ca['name']; download(ca['browser_download_url'],cp); text=cp.read_text(errors='ignore')
            actual=hashlib.sha256(archive.read_bytes()).hexdigest().lower()
            for line in text.splitlines():
                if asset['name'] in line and re.search(r'\b[0-9a-fA-F]{64}\b',line):
                    expected=re.search(r'\b[0-9a-fA-F]{64}\b',line).group(0).lower()
                    if expected!=actual: raise RuntimeError(f'published SHA-256 mismatch for {asset["name"]}')
                    return {'published':True,'verified':True,'expected':expected,'source':ca['browser_download_url']}
        except UnicodeDecodeError:
            continue
    raise RuntimeError('checksum asset exists but selected release asset could not be verified')

def safe_zip_extract(z, target):
    target=target.resolve()
    for info in z.infolist():
        out=(target/info.filename).resolve()
        if target not in out.parents and out!=target: raise RuntimeError('unsafe zip member')
    z.extractall(target)

def extract_binary(archive,dest,name):
    tmp=dest/'extract'; shutil.rmtree(tmp,ignore_errors=True); tmp.mkdir(parents=True)
    if archive.name.endswith(('.tar.gz','.tgz','.tar.xz')):
        with tarfile.open(archive) as tf: tf.extractall(tmp,filter='data')
    elif archive.suffix=='.zip':
        with zipfile.ZipFile(archive) as z: safe_zip_extract(z,tmp)
    else: raise RuntimeError('unsupported release archive')
    hits=[p for p in tmp.rglob('*') if p.is_file() and p.name in {name,name+'.exe'}]
    if not hits: raise RuntimeError(f'{name} binary not found in release asset')
    bindir=dest/'bin'; bindir.mkdir(parents=True,exist_ok=True); out=bindir/hits[0].name; shutil.copy2(hits[0],out); out.chmod(out.stat().st_mode|0o111); return out

def install_github(name):
    repo=GITHUB[name]; meta=api_json(f'https://api.github.com/repos/{repo}/releases/latest'); asset=choose_asset(meta.get('assets',[]))
    if not asset: raise RuntimeError('no matching official release asset found')
    dest=TOOLS/name/meta['tag_name']; dest.mkdir(parents=True,exist_ok=True); arc=dest/asset['name']; download(asset['browser_download_url'],arc)
    checksum=verify_published_checksum(meta,asset,arc,dest)
    out=extract_binary(arc,dest,name)
    sha=hashlib.sha256(arc.read_bytes()).hexdigest()
    return {'provider':name,'repository':repo,'version':meta['tag_name'],'asset':asset['name'],'asset_sha256':sha,'published_checksum':checksum,'binary':str(out),'source':asset['browser_download_url']}

def install_playwright():
    if not shutil.which('npm'): raise RuntimeError('npm is required for isolated @playwright/mcp bootstrap')
    dest=TOOLS/'playwright-mcp'; dest.mkdir(parents=True,exist_ok=True)
    vr=subprocess.run(['npm','view','@playwright/mcp','version'],capture_output=True,text=True,check=True,timeout=20); version=vr.stdout.strip()
    subprocess.run(['npm','install','--prefix',str(dest),f'@playwright/mcp@{version}'],check=True)
    return {'provider':'playwright_mcp','version':version,'root':str(dest),'source':f'npm:@playwright/mcp@{version}'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('provider',choices=['crw','obscura','playwright_mcp']); ap.add_argument('--apply',action='store_true'); a=ap.parse_args()
    if not a.apply:
        print(json.dumps({'status':'DRY_RUN','provider':a.provider,'install_root':str(TOOLS),'policy':'project-local; no sudo; verify after install'},indent=2)); return 0
    TOOLS.mkdir(parents=True,exist_ok=True)
    info=install_playwright() if a.provider=='playwright_mcp' else install_github(a.provider)
    lockp=R/'planning/execution/TOOL-LOCK.json'; lock={'version':'5.8.1','tools':{}}
    if lockp.exists():
        try: lock=json.loads(lockp.read_text())
        except Exception: pass
    lock.setdefault('tools',{})[a.provider]=info; lockp.write_text(json.dumps(lock,indent=2)+'\n')
    print(json.dumps({'status':'INSTALLED_REQUIRES_SMOKE_TEST',**info},indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
