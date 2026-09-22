#!/usr/bin/env python3
import argparse, datetime, hashlib, json, os, pathlib, subprocess, time
ROOT = pathlib.Path('/tmp/s3-bench-native-resume-20260922-074209')
BASE_VARIANTS = [
    ('A', 'S3_FFI_O0_BASELINE', ROOT / 'baseline-O0.so'),
    ('B', 'S3_FFI_O0_NO_BUDGET', ROOT / 'diagnostic-O0.so'),
    ('C', 'S3_FFI_O1_BASELINE', ROOT / 'baseline-O1.so'),
    ('D', 'S3_FFI_O1_NO_BUDGET', ROOT / 'diagnostic-O1.so'),
    ('E', 'GCC_O2', ROOT / 'gcc-O2.so'),
    ('F', 'CLANG_O2', ROOT / 'clang-O2.so'),
]
FRAME_VARIANTS = [
    ('A', 'S3_FFI_O0_NO_BUDGET', ROOT / 'diagnostic-O0.so'),
    ('B', 'S3_FFI_O0_NO_BUDGET_NO_FRAME_BUDGET', ROOT / 'diagnostic-O0-no-frame.so'),
    ('C', 'S3_FFI_O1_NO_BUDGET', ROOT / 'diagnostic-O1.so'),
    ('D', 'S3_FFI_O1_NO_BUDGET_NO_FRAME_BUDGET', ROOT / 'diagnostic-O1-no-frame.so'),
    ('E', 'GCC_O2', ROOT / 'gcc-O2.so'),
    ('F', 'CLANG_O2', ROOT / 'clang-O2.so'),
]
K = 750000
EXPECTED = '2444.096'
INLINE_WARMUPS = 0
EXTERNAL_WARMUP_SAMPLES = 5
REPETITIONS = 30
AFFINITY = '0'
HOST_FINGERPRINT = '9f6c7cbbdbbc2d056ffc306f76a1dcd9df194e15167cb037542da54e97b59393'

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def run_one(key, label, path, phase, sample_index, execution_order):
    command = ['taskset', '-c', AFFINITY, str(ROOT / 'ffi_driver'), str(path), 'scientific.xsbench.compatible_lookup.medium', label, 'xs_lookup_batch', str(K), EXPECTED, str(INLINE_WARMUPS)]
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=120.0, check=False)
    except subprocess.TimeoutExpired as exc:
        return {'run': phase, 'sample_index': sample_index, 'variant_key': key, 'variant': label, 'execution_order': execution_order, 'timestamp': started, 'elapsed_ns': None, 'result': None, 'exit_code': None, 'correctness_status': 'TIMEOUT', 'timeout_seconds': 120.0, 'artifact_sha256': sha(path), 'K': K, 'inline_warmups': INLINE_WARMUPS, 'CPU_affinity': 0, 'host_fingerprint': HOST_FINGERPRINT, 'command': command, 'stdout': exc.stdout or '', 'stderr': exc.stderr or ''}
    record = {'run': phase, 'sample_index': sample_index, 'variant_key': key, 'variant': label, 'execution_order': execution_order, 'timestamp': started, 'elapsed_ns': None, 'result': None, 'exit_code': proc.returncode, 'correctness_status': 'FAIL' if proc.returncode else 'MISSING', 'artifact_sha256': sha(path), 'K': K, 'inline_warmups': INLINE_WARMUPS, 'CPU_affinity': 0, 'host_fingerprint': HOST_FINGERPRINT, 'command': command, 'stdout': proc.stdout, 'stderr': proc.stderr}
    lines = proc.stdout.strip().splitlines()
    if lines:
        try:
            payload = json.loads(lines[-1])
            record['elapsed_ns'] = payload.get('elapsed_ns')
            record['result'] = payload
            record['correctness_status'] = payload.get('status', record['correctness_status'])
            record['exit_code'] = proc.returncode
        except json.JSONDecodeError:
            pass
    return record

def write_jsonl(path, record):
    with path.open('a', encoding='utf-8') as f:
        f.write(json.dumps(record, sort_keys=True) + '\n')
        f.flush()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--session', choices=['G','H','I','J'], required=True)
    ap.add_argument('--mode', choices=['budget', 'frame'], default='budget')
    ap.add_argument('--out', type=pathlib.Path, required=True)
    args = ap.parse_args()
    variants = FRAME_VARIANTS if args.mode == 'frame' else BASE_VARIANTS
    args.out.mkdir(parents=True, exist_ok=True)
    warm_path = args.out / f'warmups-{args.session}.jsonl'
    run_path = args.out / f'run_{args.session.lower()}.jsonl'
    metadata = {'session': args.session, 'mode': args.mode, 'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'K': K, 'inline_warmups': INLINE_WARMUPS, 'external_warmup_samples': EXTERNAL_WARMUP_SAMPLES, 'repetitions': REPETITIONS, 'balanced_interleaving': True, 'fresh_process': True, 'clock': 'CLOCK_MONOTONIC_RAW', 'cpu_affinity': 0, 'host_fingerprint': HOST_FINGERPRINT, 'variants': [{'key': k, 'label': l, 'path': str(p), 'artifact_sha256': sha(p), 'bytes': p.stat().st_size} for k,l,p in variants]}
    (args.out / f'metadata-{args.session}.json').write_text(json.dumps(metadata, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    for key, label, path in variants:
        for warm_index in range(1, EXTERNAL_WARMUP_SAMPLES + 1):
            rec = run_one(key, label, path, f'{args.session}_WARMUP', warm_index, key)
            write_jsonl(warm_path, rec)
            print(json.dumps({'phase': 'warmup', 'session': args.session, 'sample_index': warm_index, 'variant': label, 'status': rec['correctness_status'], 'elapsed_ns': rec['elapsed_ns']}, sort_keys=True), flush=True)
    for rep in range(REPETITIONS):
        rotated = variants[rep % len(variants):] + variants[:rep % len(variants)]
        for ordinal, (key, label, path) in enumerate(rotated, start=1):
            rec = run_one(key, label, path, args.session, rep + 1, f'{rep + 1}:{ordinal}')
            write_jsonl(run_path, rec)
            print(json.dumps({'phase': args.session, 'sample_index': rep + 1, 'execution_order': f'{rep + 1}:{ordinal}', 'variant': label, 'status': rec['correctness_status'], 'elapsed_ns': rec['elapsed_ns']}, sort_keys=True), flush=True)
    metadata['ended_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    metadata['warmup_records'] = sum(1 for _ in warm_path.open(encoding='utf-8'))
    metadata['run_records'] = sum(1 for _ in run_path.open(encoding='utf-8'))
    (args.out / f'metadata-{args.session}.json').write_text(json.dumps(metadata, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    for src, dst in ((warm_path, args.out / f'warmups-{args.session}.json'), (run_path, args.out / f'run_{args.session.lower()}.json')):
        rows = [json.loads(line) for line in src.read_text(encoding='utf-8').splitlines() if line.strip()]
        dst.write_text(json.dumps(rows, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'session': args.session, 'status': 'COMPLETE', 'warmup_records': metadata['warmup_records'], 'run_records': metadata['run_records']}, sort_keys=True), flush=True)

if __name__ == '__main__':
    main()
