#!/usr/bin/env python3
"""
Corpus generator for S3 jsmn benchmarks.
Generates deterministic test cases within the current S3 input capacity (96 bytes, 32 tokens).
Seed fixed: 0x53334A534D4E ("S3JSMN")
"""

import json
import random
from pathlib import Path

SEED = 0x53334A534D4E
INPUT_CAPACITY = 96
TOKEN_CAPACITY = 32

def generate_corpus(base_dir: Path) -> list[Path]:
    random.seed(SEED)

    tiny_dir = base_dir / "tiny"
    small_dir = base_dir / "small"
    medium_dir = base_dir / "medium"
    large_dir = base_dir / "large"
    gen_dir = base_dir / "generated"

    for d in (tiny_dir, small_dir, medium_dir, large_dir, gen_dir):
        d.mkdir(parents=True, exist_ok=True)

    # Fixed Tiny fixtures
    tiny_fixtures = {
        "tiny_01_empty_obj.json": "{}",
        "tiny_02_empty_arr.json": "[]",
        "tiny_03_pair.json": '{"a":1}',
        "tiny_04_arr.json": "[1,2,3]",
        "tiny_05_string.json": '"hello"',
        "tiny_06_bool_null.json": "[true,false,null]",
    }
    for filename, content in tiny_fixtures.items():
        (tiny_dir / filename).write_text(content, encoding="utf-8")

    # Fixed Small fixtures
    small_fixtures = {
        "small_01_flat.json": '{"a":1,"b":"val","c":true,"d":null}',
        "small_02_nested.json": '{"a":[1,{"b":"x"}],"c":false}',
        "small_03_escapes.json": '{"str":"a\\n\\t\\\"b"}',
        "small_04_unicode.json": '{"unicode":"\\u0041"}',
        "small_05_mixed.json": '["text",12345,{"k":true},[1,2]]',
    }
    for filename, content in small_fixtures.items():
        (small_dir / filename).write_text(content, encoding="utf-8")

    # Medium & Large fixtures (for C baseline, BLOCKED_BY_S3_API for current S3 kernel)
    medium_content = json.dumps({"items": [{"id": i, "name": f"item_{i}", "active": i % 2 == 0} for i in range(25)]})
    (medium_dir / "medium_01_sample.json").write_text(medium_content, encoding="utf-8")

    large_content = json.dumps({"dataset": [{"id": i, "values": [i, i * 2, i * 3]} for i in range(150)]})
    (large_dir / "large_01_sample.json").write_text(large_content, encoding="utf-8")

    # Generated fixtures (deterministic random generation within 96 bytes)
    gen_files = []

    # 1. Flat Object
    obj1 = {f"k{i}": i * 10 for i in range(4)}
    txt1 = json.dumps(obj1, separators=(",", ":"))
    p1 = gen_dir / "gen_01_flat_obj.json"
    p1.write_text(txt1, encoding="utf-8")
    gen_files.append(p1)

    # 2. Flat Array
    arr2 = [i * 5 for i in range(8)]
    txt2 = json.dumps(arr2, separators=(",", ":"))
    p2 = gen_dir / "gen_02_flat_arr.json"
    p2.write_text(txt2, encoding="utf-8")
    gen_files.append(p2)

    # 3. Nested Object
    obj3 = {"x": {"y": {"z": 42}}, "w": True}
    txt3 = json.dumps(obj3, separators=(",", ":"))
    p3 = gen_dir / "gen_03_nested_obj.json"
    p3.write_text(txt3, encoding="utf-8")
    gen_files.append(p3)

    # 4. Nested Array
    arr4 = [[1, 2], [3, 4], [5]]
    txt4 = json.dumps(arr4, separators=(",", ":"))
    p4 = gen_dir / "gen_04_nested_arr.json"
    p4.write_text(txt4, encoding="utf-8")
    gen_files.append(p4)

    # 5. Mixed
    mix5 = {"status": "ok", "code": 200, "data": [1, False]}
    txt5 = json.dumps(mix5, separators=(",", ":"))
    p5 = gen_dir / "gen_05_mixed.json"
    p5.write_text(txt5, encoding="utf-8")
    gen_files.append(p5)

    # 6. String Heavy
    str6 = {"msg": "hello", "usr": "admin", "tag": "test"}
    txt6 = json.dumps(str6, separators=(",", ":"))
    p6 = gen_dir / "gen_06_string_heavy.json"
    p6.write_text(txt6, encoding="utf-8")
    gen_files.append(p6)

    # 7. Primitive Heavy
    prim7 = [True, False, None, 0, -123, 9999]
    txt7 = json.dumps(prim7, separators=(",", ":"))
    p7 = gen_dir / "gen_07_primitive_heavy.json"
    p7.write_text(txt7, encoding="utf-8")
    gen_files.append(p7)

    all_generated = list(tiny_dir.glob("*.json")) + list(small_dir.glob("*.json")) + list(gen_dir.glob("*.json"))
    for f in all_generated:
        sz = f.stat().st_size
        assert sz <= INPUT_CAPACITY, f"Fixture {f.name} size {sz} exceeds S3 capacity {INPUT_CAPACITY}"

    return all_generated

if __name__ == "__main__":
    base = Path(__file__).parent
    files = generate_corpus(base)
    print(f"Generated {len(files)} compliant benchmark fixtures (seed={hex(SEED)}).")
