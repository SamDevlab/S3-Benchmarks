from __future__ import annotations

import argparse
import ctypes
import json
import os
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path

CONFIGS = [
    ("v1_baseline", False, False, False, False),
    ("hp02_only", True, False, False, False),
    ("hp03_only", False, True, False, False),
    ("hp10_only", False, False, True, False),
    ("hp02_hp03", True, True, False, False),
    ("hp02_hp10", True, False, True, False),
    ("hp03_hp10", False, True, True, False),
    ("hp02_hp03_hp10", True, True, True, False),
    ("v3_selective", False, False, False, True),
]


def _atomic_write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    except BaseException:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)
        raise


def _run_config_worker(cfg_name: str, hp02: bool, hp03: bool, hp10: bool, selective: bool, trials: int, warmups: int) -> dict:
    s3_root = Path("/mnt/c/Users/samue/Desktop/gemini/S3")
    sys.path.insert(0, str(s3_root))
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "high_perf_v2"))

    from bootstrap.s3.backends.x86_64 import NativeToolchain, X8664Backend
    from bootstrap.s3.backends.x86_64.instruction_budget import InstructionBudgetMode
    from bootstrap.s3.pipeline import OptimizationLevel, compile_source
    import run_high_perf_v2 as hpv2

    s3_src_path = Path(__file__).resolve().parents[1] / "high_perf_v1" / "kernels.s3"
    s3_src = s3_src_path.read_text(encoding="utf-8")
    t0 = time.perf_counter()
    _, ap = compile_source(s3_src, OptimizationLevel.O1).require_ordinary_artifacts()
    compile_s = time.perf_counter() - t0

    t1 = time.perf_counter()
    if selective:
        backend = X8664Backend(
            max_instructions=200_000_000,
            register_allocation=True,
            instruction_budget_mode=InstructionBudgetMode.LOOP_HYBRID,
            selective_hp_cost_model=True,
        )
    else:
        backend = X8664Backend(
            max_instructions=200_000_000,
            register_allocation=True,
            instruction_budget_mode=InstructionBudgetMode.LOOP_HYBRID,
            enable_hp02=hp02,
            enable_hp03=hp03,
            enable_hp10=hp10,
        )
    asm = backend._generate_ffi(ap)
    emit_s = time.perf_counter() - t1

    with tempfile.TemporaryDirectory() as td:
        so = NativeToolchain.detect().build_shared(asm, Path(td) / f"{cfg_name}.so")
        txt = hpv2._text_bytes(so)
        fns = hpv2._bind(ctypes.CDLL(str(so)))
        runners, dumpers = hpv2.make_workloads(fns)
        kernels = {}
        for k_name, fn in runners.items():
            for _ in range(warmups):
                fn()
            samples = []
            for _ in range(trials):
                ts = time.perf_counter()
                fn()
                samples.append((time.perf_counter() - ts) * 1000.0)
            kernels[k_name] = statistics.median(samples)
        dumps = {k_name: dump() for k_name, dump in dumpers.items()}
    return {
        "status": "ok",
        "text_bytes": txt,
        "compile_s": round(compile_s, 6),
        "emit_s": round(emit_s, 6),
        "kernels": {k: round(v, 4) for k, v in kernels.items()},
        "checksum": {k: round(sum(abs(float(x)) for x in v[:64]), 6) for k, v in dumps.items()},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=9)
    parser.add_argument("--warmups", type=int, default=2)
    parser.add_argument("--timeout-s", type=int, default=45)
    parser.add_argument("--out", type=Path, default=Path("benchmarks/v3_ablation_and_gpu/results_cpu_ablation.json"))
    parser.add_argument("--worker", type=str, default=None)
    args = parser.parse_args()

    if args.worker is not None:
        cfg = next(c for c in CONFIGS if c[0] == args.worker)
        print(json.dumps(_run_config_worker(*cfg, trials=args.trials, warmups=args.warmups)), flush=True)
        return

    results: dict[str, dict] = {}
    for idx, cfg in enumerate(CONFIGS, start=1):
        name = cfg[0]
        t0 = time.perf_counter()
        proc = subprocess.run(
            [sys.executable, __file__, "--worker", name, "--trials", str(args.trials), "--warmups", str(args.warmups)],
            capture_output=True,
            text=True,
            timeout=args.timeout_s,
            check=False,
        )
        elapsed = time.perf_counter() - t0
        if proc.returncode != 0:
            results[name] = {"status": "error", "stderr": (proc.stderr or "")[-400:]}
            print(f"[{idx}/{len(CONFIGS)}] {name:16s} | ERROR ({elapsed:.2f}s)", flush=True)
        else:
            entry = json.loads(proc.stdout.strip().splitlines()[-1])
            entry["elapsed_s"] = round(elapsed, 3)
            results[name] = entry
            k = entry["kernels"]
            print(
                f"[{idx}/{len(CONFIGS)}] {name:16s} | .text={entry['text_bytes']:6d}B | "
                f"axpy={k['axpy_f64_50k']:.3f} | st1d={k['stencil_1d_4096x50']:.3f} | "
                f"st2d={k['stencil_2d_64x64x20']:.3f} | mat={k['matmul_f64_48']:.3f} | "
                f"thom={k['thomas_f64_2048']:.3f} | ver={k['verlet_osc_10k']:.3f}",
                flush=True,
            )
        _atomic_write_json(args.out, results)


if __name__ == "__main__":
    main()
