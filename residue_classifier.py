#!/usr/bin/env python3
"""Non-destructive filename heuristics; no content or secret detection."""
import argparse
import json
import os
from datetime import datetime,timezone
from pathlib import Path

__version__='0.1.0'
WORKSPACE=Path.cwd()
REPORT=WORKSPACE/'residue-classifier-report.json'
RULES={'canonical':['STATE.md','NEXT-ACTION.md','ACTIVATION-REGISTRY.md'],
       'local_only_prefixes':['memory/errors.md'],
       'runtime_prefixes':['projects/xzenia/state/','logs/','data/']}

def classify(rel):
    rel=Path(rel).as_posix()
    if rel in RULES['canonical']: return 'canonical'
    if rel in RULES['local_only_prefixes']: return 'local_only'
    if any(rel.startswith(p) for p in RULES['runtime_prefixes']): return 'runtime_or_state'
    return 'review_needed'

def scan(workspace,output=None,max_files=500):
    workspace=Path(workspace).resolve(strict=True)
    if not workspace.is_dir(): raise ValueError('workspace must be a directory')
    if max_files<1: raise ValueError('max_files must be positive')
    rows=[];truncated=False
    excluded=Path(output).resolve() if output is not None else None
    for root,dirs,files in os.walk(workspace,followlinks=False,onerror=lambda error: (_ for _ in ()).throw(error)):
        dirs[:]=sorted(d for d in dirs if d!='.git' and not (Path(root)/d).is_symlink())
        for name in sorted(files):
            path=Path(root)/name
            if path.is_symlink() or not path.is_file() or path==excluded: continue
            if len(rows)==max_files: truncated=True;break
            rel=path.relative_to(workspace).as_posix()
            rows.append({'path':rel,'class':classify(rel)})
        if truncated:break
    return {'schemaVersion':1,'classifierVersion':__version__,
            'generatedAt':datetime.now(timezone.utc).isoformat(),'safe':True,
            'destructiveActions':[],'sampled':len(rows),'maxFiles':max_files,
            'truncated':truncated,'method':'filename heuristics; no content inspection','rows':rows}

def run(workspace=None,output=None,max_files=500,stdout=False):
    destination=Path(output) if output is not None else REPORT
    out=scan(workspace if workspace is not None else WORKSPACE,None if stdout else destination,max_files)
    if not stdout: destination.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))
    return out

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version',action='version',version=__version__)
    parser.add_argument('--workspace',type=Path,default=Path.cwd())
    parser.add_argument('--output',type=Path)
    parser.add_argument('--max-files',type=int,default=500)
    parser.add_argument('--stdout',action='store_true',help='Return report without writing a file')
    args=parser.parse_args(argv)
    try:
        run(args.workspace,args.output or args.workspace/'residue-classifier-report.json',args.max_files,args.stdout)
    except (OSError,ValueError) as error:
        print(json.dumps({'schemaVersion':1,'error':{'code':'SCAN_FAILED','message':str(error)}}))
        return 1
    return 0
if __name__=='__main__': raise SystemExit(main())
