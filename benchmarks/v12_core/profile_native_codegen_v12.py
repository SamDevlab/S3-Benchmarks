#!/usr/bin/env python3
"""V12 core: inspect actual S3/GCC x86-64 disassembly and classify gaps.

The specialist C reference is algorithmically different from S3's dense
fixed-width polynomial loops (it iterates sparse nonzero bits using ctz).
Do NOT attribute the whole wall-time gap to backend implementation alone.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent
S3_ROOT=HERE.parents[2]/"S3"
BASE=HERE.parents[0]/"v11_core"
sys.path.insert(0,str(S3_ROOT))

from bootstrap.s3.pipeline import compile_source, OptimizationLevel
from bootstrap.s3.gf2_ir_certificate import certify_gf2_ir
from bootstrap.s3.gf2_dynamic_native import compile_certified_gf2_dynamic


def run_tool(*args):
    return subprocess.run(args,check=True,capture_output=True,text=True,timeout=90).stdout


def classify_code(text):
    funcs={}
    current=None
    for line in text.splitlines():
        m=re.match(r"^\s*[0-9a-f]+ <([^>]+)>:\s*$",line)
        if m:
            current=m.group(1)
            funcs[current]=[]
        elif current and re.match(r"^\s*[0-9a-f]+:\s+[0-9a-f ]+\s+\S+",line):
            funcs[current].append(line)
    return funcs


def metrics(lines):
    mnemonics=[]
    for line in lines:
        text=line.split("\t")
        if len(text)>=3:
            opcode=text[2].strip().split()
            if opcode: mnemonics.append(opcode[0])
    branches=sum(s.startswith("j") for s in mnemonics)
    conditional=sum(s.startswith("j") and s not in ("jmp","jmpq") for s in mnemonics)
    calls=sum(s.startswith("call") for s in mnemonics)
    pushes=sum(s in ("push","pop","pushq","popq") for s in mnemonics)
    stack_refs=sum(("[rsp" in line or "[rbp" in line) for line in lines)
    return {"static_instructions":len(mnemonics),"branch_instructions":branches,
            "conditional_branches":conditional,"calls":calls,
            "stack_push_pop":pushes,"stack_memory_refs":stack_refs}


def source(w):
    return f"""export fn update(x: i64) -> i64:
    mut left: i64 = i64_or(i64_shl(x, 1), i64_shr(x, {w-1}))
    mut right: i64 = i64_or(i64_shl(x, {w-1}), i64_shr(x, 1))
    return i64_and(i64_xor(left, right), {(1<<w)-1})
export fn main() -> i64:
    return 0
"""


def main():
    output={"campaign":"S3_V12_NATIVE_ASSEMBLY_RESEARCH",
            "provenance":"real S3 x86-64 ELF and GCC -O3 C known specialist, same host",
            "limitations":[
                "Static assembly instruction counts are NOT dynamic executed instruction counts.",
                "The GCC specialist C loops over set bits; S3 fixed-width polynomial loops have a different algorithmic operation count.",
                "No CPU PMU hardware counters measured, no general backend speedup claim.",
                "Only W16/W32 analyzed. Native codepaths and runtime wrappers differ.",
            ],
            "cases":[]}
    snippets=[]
    for width in (16,32):
        program=compile_source(source(width),optimization=OptimizationLevel.O1,predictive_exact=False)
        ir,_=program.require_ordinary_artifacts()
        cert=certify_gf2_ir(ir,"update",width)
        with compile_certified_gf2_dynamic(
            ir,cert,enable_experimental=True,algorithm="auto"
        ) as s3:
            so=Path(s3._temp.name)/"dynamic.so"
            nms=run_tool("nm","-an",str(so))
            s3_funcs=classify_code(run_tool("objdump","-d","-M","intel",str(so)))
            relevant={name:lines for name,lines in s3_funcs.items()
                      if "@plt" not in name and any(key in name for key in
                             ("certified_step_dynamic","gf2_mul_cyclic","gf2_square_cyclic","gf2_rotl_w"))}
            if not relevant:
                raise AssertionError("S3 output symbols absent; no analysis allowed")
            with tempfile.TemporaryDirectory(prefix="s3_v12_c_ref_") as tmp:
                c=Path(tmp)/"reference"
                run_tool("gcc","-O3","-g","-std=c11",str(BASE/"compare_s3_native_auto.c"),
                         "-o",str(c),"-ldl")
                gcc_funcs=classify_code(run_tool("objdump","-d","-M","intel",str(c)))
                gcc_relevant={name:lines for name,lines in gcc_funcs.items()
                              if any(key in name for key in ("cyclic_reference","poly_mul","rotate_w"))}
                if not gcc_relevant:
                    raise AssertionError("GCC C specialist symbols absent; no comparative claim")
                output["cases"].append({
                    "width":width,
                    "s3_source_ir_sha256":cert.ir_sha256,
                    "s3_assembly_sha256":s3.manifest.emitted_assembly_sha256,
                    "s3_selected_algorithm":s3.manifest.selected_algorithm,
                    "s3_functions":{name:metrics(lines) for name,lines in relevant.items()},
                    "gcc_specialist_functions":{name:metrics(lines) for name,lines in gcc_relevant.items()},
                    "s3_function_count":len(relevant),
                    "gcc_specialist_function_count":len(gcc_relevant),
                    "s3_native_smoke_checks":s3.manifest.native_smoke_checks,
                })
                snippets.append(f"### W={width} / S3 backend generated assembly")
                for name,lines in relevant.items():
                    snippets.append(f"FUNCTION {name} / {len(lines)} assembly lines")
                    snippets.extend(line.rstrip() for line in lines[:240])
                snippets.append(f"### W={width} / GCC specialist generated assembly")
                for name,lines in gcc_relevant.items():
                    snippets.append(f"FUNCTION {name} / {len(lines)} assembly lines")
                    snippets.extend(line.rstrip() for line in lines[:240])
                print("PROFILE",width,
                      "S3",[(name,metrics(lines)["static_instructions"]) for name,lines in relevant.items()],
                      "C",[(name,metrics(lines)["static_instructions"]) for name,lines in gcc_relevant.items()],
                      flush=True)
    out=HERE/"native_codegen_profile_v12.json"
    out.write_text(json.dumps(output,indent=2),encoding="utf-8")
    (HERE/"native_codegen_disassembly_excerpt_v12.txt").write_text(
        "\n".join(snippets),encoding="utf-8",
    )
    print("OUTPUT",out,flush=True)


if __name__=="__main__":
    main()
