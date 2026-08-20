#!/usr/bin/env python3
"""Protocol-only fixture provider for the experimental benchmark bridge.

This provider exists to validate the runner contract. It is not a performance
reference and it does not implement wallet scanning or private-key recovery.
"""

from __future__ import annotations

import argparse
import hashlib
import time


GENERATOR_COMPRESSED = (
    "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--benchmark-id", required=True)
    parser.add_argument("--input-id", required=True)
    parser.add_argument("--loops", type=int, required=True)
    return parser


def main() -> int:
    args = create_parser().parse_args()
    if args.loops <= 0:
        raise SystemExit("--loops must be positive")

    started = time.perf_counter_ns()
    checksum = None

    if args.benchmark_id == "experimental.provider.roundtrip.v1":
        if args.input_id != "protocol-v1":
            raise SystemExit("unsupported input")
        value = 0
        for _ in range(args.loops):
            value = 42
        checksum = str(value)

    elif args.benchmark_id == "experimental.crypto.sha256.known-vector.v1":
        if args.input_id != "sha256-abc":
            raise SystemExit("unsupported input")
        digest = b""
        for _ in range(args.loops):
            digest = hashlib.sha256(b"abc").digest()
        checksum = digest.hex()

    elif args.benchmark_id == "experimental.crypto.secp256k1.public-vector.v1":
        if args.input_id != "secp256k1-generator-compressed":
            raise SystemExit("unsupported input")
        # Protocol fixture only: this public vector is intentionally not a
        # secp256k1 implementation. Real providers must compute their result.
        for _ in range(args.loops):
            checksum = GENERATOR_COMPRESSED

    else:
        raise SystemExit(f"unsupported benchmark: {args.benchmark_id}")

    kernel_ns = time.perf_counter_ns() - started
    print(f"checksum={checksum}")
    print(f"kernel_ns={kernel_ns}")
    print("provider_role=protocol-fixture")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
