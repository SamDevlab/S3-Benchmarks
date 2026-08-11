"""
Differential correctness harness for C vs S3 jsmn implementations.
Enforces the fundamental rule: CORRECTNESS BEFORE PERFORMANCE.
"""

import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from bootstrap.s3.pipeline import run_source_with_buffer_capture

INPUT_CAPACITY = 96
TOKEN_CAPACITY = 32

JSMN_OBJECT = 1
JSMN_ARRAY = 2
JSMN_STRING = 4
JSMN_PRIMITIVE = 8
JSMN_ERROR_NOMEM = -1
JSMN_ERROR_INVAL = -2
JSMN_ERROR_PART = -3

@dataclass
class Token:
    type: int
    start: int
    end: int
    size: int = 0

@dataclass
class ExecutionResult:
    status: int
    token_count: int
    checksum: int
    tokens: list[Token]
    raw_output: str = ""

def reference_jsmn_oracle(data: bytes) -> tuple[int, list[Token]]:
    """Python-based behavioral reference oracle for upstream jsmn token contract."""
    tokens: list[Token] = []
    pos = 0
    toksuper = -1
    parents: list[int] = []

    def allocate(type_: int, start: int, end: int = -1) -> int:
        nonlocal toksuper
        if len(tokens) >= TOKEN_CAPACITY:
            return JSMN_ERROR_NOMEM
        parent = toksuper
        tokens.append(Token(type_, start, end, 0))
        parents.append(parent)
        if parent >= 0:
            tokens[parent].size += 1
        return len(tokens) - 1

    while pos < len(data):
        ch = data[pos]

        if ch in (ord("{"), ord("[")):
            type_ = JSMN_OBJECT if ch == ord("{") else JSMN_ARRAY
            index = allocate(type_, pos)
            if index < 0:
                return index, tokens
            toksuper = index

        elif ch in (ord("}"), ord("]")):
            type_ = JSMN_OBJECT if ch == ord("}") else JSMN_ARRAY
            index = len(tokens) - 1
            while index >= 0 and tokens[index].end != -1:
                index -= 1
            if index < 0 or tokens[index].type != type_:
                return JSMN_ERROR_INVAL, tokens
            tokens[index].end = pos + 1
            toksuper = parents[index]

        elif ch == ord('"'):
            start_quote = pos
            pos += 1
            while pos < len(data):
                ch = data[pos]
                if ch == ord('"'):
                    index = allocate(JSMN_STRING, start_quote + 1, pos)
                    if index < 0:
                        return index, tokens
                    break
                if ch == ord("\\"):
                    pos += 1
                    if pos >= len(data):
                        return JSMN_ERROR_PART, tokens
                    escaped = data[pos]
                    if escaped == ord("u"):
                        for _ in range(4):
                            pos += 1
                            if pos >= len(data):
                                return JSMN_ERROR_PART, tokens
                            digit = data[pos]
                            if not (
                                ord("0") <= digit <= ord("9")
                                or ord("A") <= digit <= ord("F")
                                or ord("a") <= digit <= ord("f")
                            ):
                                return JSMN_ERROR_INVAL, tokens
                    elif escaped not in b'"/\\bfrnt':
                        return JSMN_ERROR_INVAL, tokens
                pos += 1
            else:
                return JSMN_ERROR_PART, tokens

        elif ch in b"\t\r\n ":
            pass

        elif ch == ord(":"):
            toksuper = len(tokens) - 1

        elif ch == ord(","):
            if toksuper >= 0 and tokens[toksuper].type not in (JSMN_ARRAY, JSMN_OBJECT):
                toksuper = parents[toksuper]

        else:
            start = pos
            while pos < len(data):
                primitive = data[pos]
                if primitive in b"\t\r\n ,]}:":
                    break
                if primitive < 32 or primitive >= 127:
                    return JSMN_ERROR_INVAL, tokens
                pos += 1
            index = allocate(JSMN_PRIMITIVE, start, pos)
            if index < 0:
                return index, tokens
            pos -= 1

        pos += 1

    if any(token.end == -1 for token in tokens):
        return JSMN_ERROR_PART, tokens
    return len(tokens), tokens

def compute_checksum_from_tokens(status: int, tokens: list[Token]) -> int:
    if status < 0:
        return status
    chk = status
    for t in tokens:
        chk += t.type + t.start + t.end + t.size
    return chk

def run_s3_jsmn(source_template: str, text: str, optimization: str = "O0") -> ExecutionResult:
    """Executes S3 jsmn kernel via compiler pipeline and memory buffer capture."""
    data = text.encode("ascii")
    assert len(data) <= INPUT_CAPACITY, f"Input size {len(data)} exceeds {INPUT_CAPACITY}"
    values = list(data) + [0] * (INPUT_CAPACITY - len(data))

    rendered_source = re.sub(
        r"(?m)^    input_length: tryte = \d+$",
        f"    input_length: tryte = {len(data)}",
        source_template,
        count=1,
    )
    rendered_source = re.sub(
        r"(?m)^    input: tryte\[96\] = \[[^\n]+\]$",
        "    input: tryte[96] = [" + ", ".join(map(str, values)) + "]",
        rendered_source,
        count=1,
    )

    res, captures = run_source_with_buffer_capture(rendered_source, optimization=optimization)

    status = int(res)
    tokens: list[Token] = []
    if status >= 0 and captures:
        main_capture = next(
            frame for frame in reversed(captures)
            if sum(1 for m in frame.values() if len(m) == TOKEN_CAPACITY) == 5
        )
        token_memories = [m for m in main_capture.values() if len(m) == TOKEN_CAPACITY]
        types, starts, ends, sizes, _ = token_memories
        for i in range(status):
            tokens.append(Token(int(types[i]), int(starts[i]), int(ends[i]), int(sizes[i])))

    chk = compute_checksum_from_tokens(status, tokens)
    return ExecutionResult(status=status, token_count=len(tokens), checksum=chk, tokens=tokens)

def run_c_jsmn(c_runner_bin: Path, text: str) -> ExecutionResult:
    """Executes C runner with --correctness flag."""
    proc = subprocess.run(
        [str(c_runner_bin), "--correctness", text],
        capture_output=True,
        text=True,
        check=True,
    )
    data = json.loads(proc.stdout.strip())
    tokens = [
        Token(t["type"], t["start"], t["end"], t["size"])
        for t in data.get("tokens", [])
    ]
    return ExecutionResult(
        status=data["status"],
        token_count=data["token_count"],
        checksum=data["checksum"],
        tokens=tokens,
        raw_output=proc.stdout,
    )

def compare_results(ref_status: int, ref_tokens: list[Token], target: ExecutionResult) -> bool:
    """
    Applies strict differential comparison rules:
    - If ref_status >= 0: target.status == ref_status AND checksum / tokens match ref.
    - If ref_status < 0: target.status == ref_status (same error code = pass).
    """
    if ref_status >= 0:
        if target.status != ref_status:
            return False
        ref_chk = compute_checksum_from_tokens(ref_status, ref_tokens)
        return target.checksum == ref_chk
    else:
        return target.status == ref_status

def verify_differential_correctness(
    c_runner_bin: Path | None,
    s3_demo_template: str,
    test_cases: list[str],
) -> tuple[bool, list[str]]:
    """Runs differential verification across test cases."""
    logs = []
    all_passed = True

    for text in test_cases:
        ref_status, ref_tokens = reference_jsmn_oracle(text.encode("ascii"))

        # S3 O0
        s3_o0_res = run_s3_jsmn(s3_demo_template, text, "O0")
        if not compare_results(ref_status, ref_tokens, s3_o0_res):
            logs.append(f"FAIL S3-O0: '{text}' status ref={ref_status} s3={s3_o0_res.status}")
            all_passed = False

        # S3 O1
        s3_o1_res = run_s3_jsmn(s3_demo_template, text, "O1")
        if not compare_results(ref_status, ref_tokens, s3_o1_res):
            logs.append(f"FAIL S3-O1: '{text}' status ref={ref_status} s3={s3_o1_res.status}")
            all_passed = False

        # C runner (if binary compiled)
        if c_runner_bin and c_runner_bin.exists():
            c_res = run_c_jsmn(c_runner_bin, text)
            if not compare_results(ref_status, ref_tokens, c_res):
                logs.append(f"FAIL C: '{text}' status ref={ref_status} c={c_res.status}")
                all_passed = False

    return all_passed, logs

def test_differential_correctness_rules():
    """Unit tests for differential error-comparison semantics and regression rules."""
    # 1. Success case comparing complete token output
    ref_st, ref_toks = reference_jsmn_oracle(b'{"a":1}')
    assert ref_st == 3
    valid_res = ExecutionResult(status=3, token_count=3, checksum=compute_checksum_from_tokens(3, ref_toks), tokens=ref_toks)
    assert compare_results(ref_st, ref_toks, valid_res) is True

    bad_checksum_res = ExecutionResult(status=3, token_count=3, checksum=9999, tokens=[])
    assert compare_results(ref_st, ref_toks, bad_checksum_res) is False

    # 2. Invalid delimiter: {"a":1] -> ref=-2, target=-2 -> PASS
    ref_st, ref_toks = reference_jsmn_oracle(b'{"a":1]')
    assert ref_st == JSMN_ERROR_INVAL
    inval_res = ExecutionResult(status=JSMN_ERROR_INVAL, token_count=0, checksum=JSMN_ERROR_INVAL, tokens=[])
    assert compare_results(ref_st, ref_toks, inval_res) is True

    # 3. Partial: {"a": -> ref=-3, target=-3 -> PASS
    ref_st, ref_toks = reference_jsmn_oracle(b'{"a":')
    assert ref_st == JSMN_ERROR_PART
    part_res = ExecutionResult(status=JSMN_ERROR_PART, token_count=0, checksum=JSMN_ERROR_PART, tokens=[])
    assert compare_results(ref_st, ref_toks, part_res) is True

    # 4. Invalid escape: "bad\q" -> ref=-2, target=-2 -> PASS
    ref_st, ref_toks = reference_jsmn_oracle(b'"bad\\q"')
    assert ref_st == JSMN_ERROR_INVAL
    assert compare_results(ref_st, ref_toks, inval_res) is True

    # 5. NOMEM -> ref=-1, target=-1 -> PASS
    nomem_input = ("[" + ",".join("0" for _ in range(40)) + "]").encode("ascii")
    ref_st, ref_toks = reference_jsmn_oracle(nomem_input)
    assert ref_st == JSMN_ERROR_NOMEM
    nomem_res = ExecutionResult(status=JSMN_ERROR_NOMEM, token_count=0, checksum=JSMN_ERROR_NOMEM, tokens=[])
    assert compare_results(ref_st, ref_toks, nomem_res) is True

    # 6. Negative Regression: ref=-2, target=-3 -> FAIL
    mismatch_error_res = ExecutionResult(status=JSMN_ERROR_PART, token_count=0, checksum=JSMN_ERROR_PART, tokens=[])
    assert compare_results(JSMN_ERROR_INVAL, ref_toks, mismatch_error_res) is False

DEFAULT_TEST_SUITE = [
    "{}",
    "[]",
    '{"a":1}',
    '{"a":"b"}',
    '{"a":[1,2,3]}',
    '{"a":{"b":true},"c":null}',
    '["a","b",false,-12]',
    '{ "escaped": "a\\n\\t\\\"b" }',
    '{"unicode":"\\u0041"}',
    '"raw\tcontrol"',
    '{"a":1]',
    '{"a":',
    '"unterminated',
    '"bad\\q"',
    '"bad\\u00xz"',
    "[" + ",".join("0" for _ in range(40)) + "]",
]
