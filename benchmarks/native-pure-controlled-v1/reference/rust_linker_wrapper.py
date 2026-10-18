#!/usr/bin/env python3
"""Rust linker proxy: execute the selected C linker and record its wall time."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path


start = time.perf_counter_ns()
result = subprocess.run([os.environ.get("CC", "gcc"), *sys.argv[1:]], check=False)
elapsed = time.perf_counter_ns() - start
record = os.environ.get("S3_LINK_TIMING_FILE")
if record:
    Path(record).write_text(json.dumps({"linker": os.environ.get("CC", "gcc"), "elapsed_ns": elapsed}) + "\n", encoding="utf-8")
raise SystemExit(result.returncode)
