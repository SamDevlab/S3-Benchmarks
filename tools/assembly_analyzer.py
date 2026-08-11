"""
Quantitative assembly analysis tool for C and S3 x86-64 output.
Measures instruction counts, stack traffic, branches, function sizes, and binary sizes.
"""

import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

@dataclass
class AssemblyMetrics:
    variant: str
    line_count: int
    instruction_count: int
    call_count: int
    load_store_count: int
    stack_ops_count: int
    branch_count: int
    cond_branch_count: int
    binary_size_bytes: int
    text_section_bytes: int

def analyze_assembly_text(asm_text: str, variant_name: str, binary_path: Path | None = None) -> AssemblyMetrics:
    lines = asm_text.splitlines()
    line_count = len(lines)

    instruction_count = 0
    call_count = 0
    load_store_count = 0
    stack_ops_count = 0
    branch_count = 0
    cond_branch_count = 0

    # Common x86-64 mnemonic patterns (Intel & AT&T)
    call_re = re.compile(r"^\s*call\b", re.IGNORECASE)
    branch_re = re.compile(r"^\s*j\w+\b", re.IGNORECASE)
    cond_branch_re = re.compile(r"^\s*j(e|ne|g|ge|l|le|a|ae|b|be|z|nz|c|nc)\b", re.IGNORECASE)
    stack_re = re.compile(r"^\s*(push|pop)\b|\[r?bp\s*[-+]", re.IGNORECASE)
    load_store_re = re.compile(r"^\s*(mov|movzx|movsx|lea)\b", re.IGNORECASE)

    for line in lines:
        cleaned = line.split("#")[0].split(";")[0].strip()
        if not cleaned or cleaned.startswith(".") or cleaned.endswith(":"):
            continue

        instruction_count += 1

        if call_re.search(cleaned):
            call_count += 1
        if branch_re.search(cleaned):
            branch_count += 1
            if cond_branch_re.search(cleaned):
                cond_branch_count += 1
        if stack_re.search(cleaned):
            stack_ops_count += 1
        if load_store_re.search(cleaned):
            load_store_count += 1

    binary_size = 0
    text_size = 0

    if binary_path and binary_path.exists():
        binary_size = binary_path.stat().st_size
        try:
            proc = subprocess.run(
                ["size", str(binary_path)],
                capture_output=True,
                text=True,
                check=True,
            )
            # Example output: text data bss dec hex filename
            size_lines = proc.stdout.strip().splitlines()
            if len(size_lines) >= 2:
                parts = size_lines[1].split()
                if parts:
                    text_size = int(parts[0])
        except Exception:
            text_size = binary_size

    return AssemblyMetrics(
        variant=variant_name,
        line_count=line_count,
        instruction_count=instruction_count,
        call_count=call_count,
        load_store_count=load_store_count,
        stack_ops_count=stack_ops_count,
        branch_count=branch_count,
        cond_branch_count=cond_branch_count,
        binary_size_bytes=binary_size,
        text_section_bytes=text_size,
    )
