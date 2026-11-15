#!/usr/bin/env python3
"""Diagnostic only: compute exact unreachable AssemblyOpcode delta from legacy test.

Executes ONLY the source fixture/setup portion of the existing test
up through the first assertion; does not suppress any assertion.
"""
from __future__ import annotations
import ast
import importlib.util
import inspect
import json
import sys
from pathlib import Path
import textwrap

ROOT=Path(__file__).resolve().parent
S3=ROOT.parents[2]/"S3-Quality"
sys.path.insert(0,str(S3))
file=S3/"tests"/"test_native_x86_64.py"
spec=importlib.util.spec_from_file_location("_s3_legacy_opcode_probe",file)
mod=importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)
func=mod.test_native_backend_emits_every_current_opcode
tree=ast.parse(textwrap.dedent(inspect.getsource(func)))
f=tree.body[0]
setup=[]
for node in f.body:
    if isinstance(node,ast.Assert):
        break
    setup.append(node)
else:
    raise RuntimeError("Fixture must include an assertion")
code=compile(ast.fix_missing_locations(ast.Module(body=setup,type_ignores=[])),str(file),"exec")
context=dict(vars(mod))
exec(code,context,context)
seen=context["seen"]
unqualified=context["native_unqualified"]
missing=set(mod.AssemblyOpcode)-unqualified-seen
result={
    "coverage_source":str(file),
    "total_known_opcodes":len(mod.AssemblyOpcode),
    "opcodes_emitted_from_existing_sources":len(seen),
    "previously_unqualified_aggregate":[x.name for x in sorted(unqualified,key=lambda v:v.name)],
    "new_unseen":[x.name for x in sorted(missing,key=lambda v:v.name)],
    "unseen_count":len(missing),
}
(ROOT/"opcode_coverage_audit_20261115.json").write_text(
    json.dumps(result,indent=2,ensure_ascii=False)+"\n","utf-8",
)
print(json.dumps(result,indent=2,ensure_ascii=False))
