"""Structural correctness preflight for S3 M1.77/M1.78 ARM64 backends.

This module intentionally avoids performance claims.  The current S3 ARM64
backends expose reviewable ABI/header contracts but do not yet emit a complete
native object/executable suitable for fair code-quality or runtime comparison
with LLVM.  The gate therefore locks exactly the semantics S3 currently
models, and records the missing contracts explicitly.
"""

from __future__ import annotations

import hashlib
import json
import struct
from typing import Any

from bootstrap.s3.backends.aarch64 import (
    AARCH64_ELF_MACHINE,
    AAPCS64_ARGUMENT_REGISTERS,
    Aapcs64Call,
    AArch64Backend,
    AArch64BackendError,
    ExecutionCertification as LinuxExecutionCertification,
)
from bootstrap.s3.backends.macos_arm64 import (
    ARM64_CPU_TYPE,
    MACHO64_MAGIC,
    MachOBackend,
    MachOBackendError,
    ExecutionCertification as MacExecutionCertification,
)
from bootstrap.s3.targets import (
    LINUX_AARCH64_TARGET,
    MACOS_ARM64_TARGET,
    arm64_target_catalog,
    apple_arm64_target_catalog,
    cross_platform_target_catalog,
)


UNMODELED_CONTRACTS = [
    "floating_point_argument_registers",
    "explicit_16_byte_stack_alignment_proof",
    "aggregate_argument_classification",
    "aggregate_return_and_sret",
    "elf_sections_and_relocations",
    "macho_load_commands_sections_and_relocations",
    "machine_code_encoding",
    "native_link_and_execution",
]


EXPECTED: dict[str, Any] = {
    "targets": {
        "linux": {"name": "linux-aarch64", "architecture": "aarch64", "environment": "linux"},
        "macos": {"name": "macos-arm64", "architecture": "arm64", "environment": "macos"},
        "linux_catalog": ["linux-aarch64"],
        "macos_catalog": ["macos-arm64"],
        "cross_catalog_contains": ["linux-aarch64", "macos-arm64"],
    },
    "aapcs64_scalar": {
        "argument_registers": [f"x{index}" for index in range(8)],
        "locations_10_args": [
            "x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "[sp+0]", "[sp+8]"
        ],
        "return_register": "x0",
        "stack_slot_stride_bytes": 8,
    },
    "linux_elf": {
        "magic_hex": "7f454c46",
        "class": 2,
        "endianness": 1,
        "type": 2,
        "machine": 183,
        "version": 1,
        "entrypoint": 4096,
        "header_bytes": 64,
    },
    "macos_macho": {
        "magic": 0xFEEDFACF,
        "cpu_type": 0x0100000C,
        "cpu_subtype": 0,
        "file_type": 2,
        "ncmds": 0,
        "sizeofcmds": 0,
        "header_bytes": 32,
    },
    "scalar_emission": {
        "text": ".text\n    mov x0, #7\n    ret\n",
        "instruction_count": 2,
        "linux_macos_match": True,
        "deterministic": True,
    },
    "execution_certification": {
        "linux": "execution_certification_deferred",
        "macos": "execution_certification_deferred",
    },
    "invalid_inputs": {
        "negative_argument_count_rejected": True,
        "wrong_return_register_rejected": True,
        "oversized_immediate_rejected": True,
        "negative_macho_subtype_rejected": True,
    },
    "unmodeled_contracts": UNMODELED_CONTRACTS,
}


def _rejected(callable_) -> bool:
    try:
        callable_()
    except (AArch64BackendError, MachOBackendError):
        return True
    return False


def _targets() -> dict[str, Any]:
    cross_names = cross_platform_target_catalog().names
    return {
        "linux": {
            "name": LINUX_AARCH64_TARGET.name,
            "architecture": LINUX_AARCH64_TARGET.architecture,
            "environment": LINUX_AARCH64_TARGET.environment,
        },
        "macos": {
            "name": MACOS_ARM64_TARGET.name,
            "architecture": MACOS_ARM64_TARGET.architecture,
            "environment": MACOS_ARM64_TARGET.environment,
        },
        "linux_catalog": list(arm64_target_catalog().names),
        "macos_catalog": list(apple_arm64_target_catalog().names),
        "cross_catalog_contains": [
            name for name in ("linux-aarch64", "macos-arm64") if name in cross_names
        ],
    }


def _aapcs64_scalar() -> dict[str, Any]:
    call = Aapcs64Call(10)
    locations = [call.location(index) for index in range(10)]
    stack_offsets = [0, 8]
    return {
        "argument_registers": list(AAPCS64_ARGUMENT_REGISTERS),
        "locations_10_args": locations,
        "return_register": call.return_register,
        "stack_slot_stride_bytes": stack_offsets[1] - stack_offsets[0],
    }


def _linux_elf() -> dict[str, Any]:
    payload = AArch64Backend().elf_header(entrypoint=0x1000).bytes
    return {
        "magic_hex": payload[:4].hex(),
        "class": payload[4],
        "endianness": payload[5],
        "type": struct.unpack_from("<H", payload, 16)[0],
        "machine": struct.unpack_from("<H", payload, 18)[0],
        "version": struct.unpack_from("<I", payload, 20)[0],
        "entrypoint": struct.unpack_from("<Q", payload, 24)[0],
        "header_bytes": len(payload),
    }


def _macos_macho() -> dict[str, Any]:
    payload = MachOBackend().header().bytes
    magic, cpu_type, cpu_subtype, file_type, ncmds, sizeofcmds, _flags, _reserved = struct.unpack(
        "<IiiIIIII", payload
    )
    return {
        "magic": magic,
        "cpu_type": cpu_type,
        "cpu_subtype": cpu_subtype,
        "file_type": file_type,
        "ncmds": ncmds,
        "sizeofcmds": sizeofcmds,
        "header_bytes": len(payload),
    }


def _scalar_emission() -> dict[str, Any]:
    linux = AArch64Backend()
    macos = MachOBackend()
    first = linux.emit_return(7)
    second = linux.emit_return(7)
    mac = macos.emit_return(7)
    return {
        "text": first.text,
        "instruction_count": len(first.instructions),
        "linux_macos_match": first == mac,
        "deterministic": first == second,
    }


def _execution_certification() -> dict[str, Any]:
    linux = AArch64Backend().execution_status()
    macos = MachOBackend().execution_status()
    if linux is not LinuxExecutionCertification.DEFERRED:
        raise AssertionError("Linux AArch64 execution unexpectedly became certified")
    if macos is not MacExecutionCertification.DEFERRED:
        raise AssertionError("macOS ARM64 execution unexpectedly became certified")
    return {"linux": linux.value, "macos": macos.value}


def _invalid_inputs() -> dict[str, Any]:
    return {
        "negative_argument_count_rejected": _rejected(lambda: Aapcs64Call(-1)),
        "wrong_return_register_rejected": _rejected(lambda: Aapcs64Call(1, return_register="x1")),
        "oversized_immediate_rejected": _rejected(lambda: AArch64Backend().emit_return(1 << 20)),
        "negative_macho_subtype_rejected": _rejected(lambda: MachOBackend().header(cpu_subtype=-1)),
    }


def collect_results() -> dict[str, Any]:
    return {
        "targets": _targets(),
        "aapcs64_scalar": _aapcs64_scalar(),
        "linux_elf": _linux_elf(),
        "macos_macho": _macos_macho(),
        "scalar_emission": _scalar_emission(),
        "execution_certification": _execution_certification(),
        "invalid_inputs": _invalid_inputs(),
        "unmodeled_contracts": list(UNMODELED_CONTRACTS),
    }


def verify_structural_contract() -> tuple[bool, dict[str, Any]]:
    actual = collect_results()
    canonical = json.dumps(actual, sort_keys=True, separators=(",", ":"))
    report = {
        "schema": "s3.aarch64-structural.v1",
        "performance_results_valid": False,
        "comparative_code_quality_valid": False,
        "llvm_oracle_execution": "DEFERRED_PINNED_REFERENCE_ONLY",
        "execution_benchmark_valid": False,
        "expected": EXPECTED,
        "actual": actual,
        "actual_sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
        "passed": actual == EXPECTED,
    }
    return report["passed"], report


if __name__ == "__main__":
    passed, report = verify_structural_contract()
    print(json.dumps(report, indent=2, sort_keys=True))
    raise SystemExit(0 if passed else 1)
