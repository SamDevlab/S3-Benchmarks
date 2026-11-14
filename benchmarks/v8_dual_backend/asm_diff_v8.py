#!/usr/bin/env python3
"""Differential codegen report: S3 backend vs GCC for the same verified IR (V8 Wave 08).

Usage: asm_diff_v8.py <artifact_dir> <function> [--out report.json]

Reads mode_B.so (S3 predictive native) and mode_E.so (GCC on C emitted from the same
transformed IR), plus mode_A / mode_F (conventional IR on both backends), and mode_D
(hand-written C math), disassembles ``<function>`` with objdump and prints instruction
class counts, code size and register usage.
"""

from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import subprocess

ARTS = {
    "A_S3_CONV": "mode_A.so",
    "B_S3_PRED": "mode_B.so",
    "G_S3_PRED_CLEAN_EXACT": "mode_G.so",
    "C_GCC_CONV_MANUAL": "mode_C.so",
    "D_GCC_MANUAL_MATH": "mode_D.so",
    "E_GCC_AUTO_MATH": "mode_E.so",
    "F_GCC_CONV_FROM_S3_IR": "mode_F.so",
}

CALL = re.compile(r"\bcall")
BRANCH = re.compile(r"\b(j[a-z]+)\b")
DIV = re.compile(r"\b(idiv|div)[a-z]*\b")
MUL = re.compile(r"\b(imul|mul)[a-z]*\b")
LOADSTORE = re.compile(r"\bmov[a-z]*\b.*\(")
GPR = re.compile(r"%(r[a-z0-9]+|e[a-z]{2}|[a-d]l)\b")
XMM = re.compile(r"%[xy]mm\d+")
OVF = re.compile(r"\bj(o|no|c|nc|b|ae)\b")


def disasm_symbol(so: pathlib.Path, sym: str) -> list[str]:
    out = subprocess.check_output(["objdump", "-d", "--no-show-raw-insn", "-M", "att", str(so)], text=True)
    lines = out.splitlines()
    body: list[str] = []
    inside = False
    for ln in lines:
        m = re.match(r"^[0-9a-f]+ <([^>]+)>:$", ln)
        if m:
            inside = m.group(1) == sym
            continue
        if inside and re.match(r"^\s+[0-9a-f]+:\s", ln):
            body.append(ln.split(":", 1)[1].strip())
    return body


def symbol_size(so: pathlib.Path, sym: str) -> int | None:
    out = subprocess.check_output(["nm", "-S", "--defined-only", str(so)], text=True)
    for ln in out.splitlines():
        p = ln.split()
        if len(p) >= 4 and p[3] == sym:
            return int(p[1], 16)
    return None


def stats(insns: list[str]) -> dict:
    mnems = collections.Counter(i.split()[0] for i in insns if i)
    regs = collections.Counter()
    for i in insns:
        for r in GPR.findall(i):
            regs[r] += 1
    return {
        "instructions": len(insns),
        "calls": sum(1 for i in insns if CALL.search(i)),
        "branches": sum(1 for i in insns if BRANCH.match(i.split()[0]) if i.split()[0].startswith("j")),
        "overflow_branches": sum(1 for i in insns if OVF.match(i.split()[0])),
        "div_instructions": sum(1 for i in insns if DIV.match(i.split()[0])),
        "mul_instructions": sum(1 for i in insns if MUL.match(i.split()[0])),
        "memory_operand_movs": sum(1 for i in insns if LOADSTORE.search(i)),
        "stack_memory_refs": sum(1 for i in insns if "(%rsp)" in i or "(%rbp)" in i),
        "distinct_gprs": len(regs),
        "xmm_ymm_uses": sum(1 for i in insns if XMM.search(i)),
        "top_mnemonics": mnems.most_common(8),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("artifact_dir")
    ap.add_argument("function")
    ap.add_argument("--out")
    a = ap.parse_args()
    d = pathlib.Path(a.artifact_dir)
    rep = {}
    for tag, fname in ARTS.items():
        so = d / fname
        ins = disasm_symbol(so, a.function)
        rep[tag] = {"symbol_size_bytes": symbol_size(so, a.function), **stats(ins)}
    print(json.dumps(rep, indent=1))
    if a.out:
        pathlib.Path(a.out).write_text(json.dumps(rep, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
