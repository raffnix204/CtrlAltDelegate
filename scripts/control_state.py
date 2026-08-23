#!/usr/bin/env python3
"""CtrlAltDelegate V5.9 control-state primitives.

Protected state changes are sealed with revisioned receipts. This is deliberately
small and stdlib-only so imported control packages can enforce the same rules.
"""
from pathlib import Path
import datetime, hashlib, json, os, tempfile, uuid, yaml

ROOT=Path(__file__).resolve().parents[1]
STATE_REL='planning/execution/CONTROL-STATE.json'
MUTATION_LOG_REL='planning/execution/CONTROL-MUTATION-LOG.jsonl'
EVENT_LOG_REL='planning/execution/CONTROL-EVENTS.jsonl'
POLICY_REL='config/SURFACE-POLICY.yaml'

class StaleState(RuntimeError): pass
class ControlDrift(RuntimeError): pass

def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def sha_file(p): return sha_bytes(p.read_bytes()) if p.is_file() else None
def load_json(rel): return json.loads((ROOT/rel).read_text(encoding='utf-8'))
def atomic_json(rel,obj):
    p=ROOT/rel; p.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix='.'+p.name+'.',dir=str(p.parent))
    try:
        with os.fdopen(fd,'w',encoding='utf-8') as f: json.dump(obj,f,indent=2); f.write('\n'); f.flush(); os.fsync(f.fileno())
        os.replace(tmp,p)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)
def append_jsonl(rel,obj):
    p=ROOT/rel; p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('a',encoding='utf-8') as f: f.write(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n'); f.flush(); os.fsync(f.fileno())
def policy(): return yaml.safe_load((ROOT/POLICY_REL).read_text(encoding='utf-8')) or {}
def planning_is_attested():
    try:
        return load_json('planning/execution/PLANNING-BASELINE.json').get('status')=='ATTESTED'
    except Exception:
        return False
def protected_paths():
    out=[]
    for name,cfg in (policy().get('classes') or {}).items():
        if name in {'CONTROLLER_MUTATED','DERIVED'} or (name=='LOCKED' and planning_is_attested()):
            out.extend(x for x in cfg.get('paths') or [] if isinstance(x,str) and '/' in x)
    return sorted(set(out))
def state(): return load_json(STATE_REL)
def assert_revision(expected):
    s=state(); cur=int(s.get('revision') or 0)
    if expected is not None and int(expected)!=cur: raise StaleState(f'STALE_STATE expected={expected} current={cur}')
    return s
def verify_seal():
    s=state(); errs=[]
    if s.get('status')!='SEALED': errs.append('control state is not SEALED')
    sealed=s.get('sealed_hashes') or {}
    for rel in protected_paths():
        actual=sha_file(ROOT/rel)
        if sealed.get(rel)!=actual: errs.append(f'CONTROL_SURFACE_DRIFT {rel}')
    return errs
def _receipt_hash(receipt): return sha_bytes(json.dumps(receipt,sort_keys=True,separators=(',',':')).encode())
def seal(operation,actor='controller',expected_revision=None,paths=None,event=None):
    s=assert_revision(expected_revision)
    revision=int(s.get('revision') or 0)+1
    hs={rel:sha_file(ROOT/rel) for rel in protected_paths()}
    mutation_id=str(uuid.uuid4())
    receipt={'version':'5.9','mutation_id':mutation_id,'operation':operation,'actor':actor,'revision':revision,'previous_revision':int(s.get('revision') or 0),'paths':sorted(paths or []),'at':now(),'previous_receipt_hash':s.get('last_receipt_hash')}
    receipt['receipt_hash']=_receipt_hash(receipt)
    append_jsonl(MUTATION_LOG_REL,receipt)
    if event:
        ev={'version':'5.9','event_id':str(uuid.uuid4()),'mutation_id':mutation_id,'revision':revision,'at':receipt['at'],**event}
        append_jsonl(EVENT_LOG_REL,ev)
    atomic_json(STATE_REL,{'version':'5.9','revision':revision,'status':'SEALED','sealed_hashes':hs,'last_mutation_id':mutation_id,'last_receipt_hash':receipt['receipt_hash'],'updated_at':receipt['at']})
    return receipt
def initialize_seal():
    s=state()
    if s.get('status')=='SEALED': return s
    return seal('INITIALIZE_CONTROL_STATE',actor='release',expected_revision=int(s.get('revision') or 0),paths=protected_paths(),event={'type':'CONTROL_STATE_INITIALIZED'})
