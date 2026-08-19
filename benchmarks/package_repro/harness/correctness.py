"""Correctness preflight for S3 package resolution, registry cache, and bundles.

This workload intentionally avoids public registries and performance claims.
It locks deterministic/package-supply-chain behavior first, using only local
fixtures and the S3 M1.56/M1.79/M1.80 contracts.
"""

from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
import tarfile
import tempfile
import zipfile
from typing import Any, Callable

from bootstrap.s3.package_dependencies import (
    PackageDependency,
    PackageDependencyError,
    PackageLock,
    PackageManifest,
)
from bootstrap.s3.registry_client import RegistryClient, RegistryError, RegistryLock
from bootstrap.s3.toolchain_distribution import DistributionError, ToolchainBundler


EXPECTED: dict[str, Any] = {
    "dependency_lock": {
        "mapping_order_invariant": True,
        "lock_sha_invariant": True,
        "topological_order": ["shared", "left", "right", "app"],
        "shared_source": "vendor/shared",
        "shared_revision": None,
        "conflicting_reachable_identity_rejected": True,
        "unreachable_conflict_isolated": True,
        "root_source": ".",
        "root_revision": None,
    },
    "registry": {
        "read_only": True,
        "exact_lock_match": True,
        "cache_survives_object_removal": True,
        "cache_hash_mismatch_rejected": True,
        "installed_paths": ["src/lib.s3", "src/main.s3"],
        "installed_contents_match": True,
        "path_traversal_rejected": True,
        "duplicate_canonical_path_rejected": True,
        "member_limit_rejected": True,
        "publish_rejected": True,
    },
    "toolchain_bundle": {
        "byte_identical_across_input_order": True,
        "sha256_identical": True,
        "manifest_file_paths": ["bin/s3", "lib/core.s3"],
        "zip_entry_order": ["LICENSE", "MANIFEST.json", "bin/s3", "lib/core.s3"],
        "fixed_timestamps": True,
        "fixed_permissions": True,
        "license_present": True,
        "verify_passed": True,
        "corruption_rejected": True,
        "machine_path_rejected": True,
        "traversal_path_rejected": True,
        "reserved_path_rejected": True,
        "remote_publish_rejected": True,
    },
}


def _expect_raises(error_type: type[BaseException], callback: Callable[[], object], contains: str | None = None) -> bool:
    try:
        callback()
    except error_type as error:
        return contains is None or contains.lower() in str(error).lower()
    return False


def _dependency_graph(*, conflicting_reachable: bool = False, add_unreachable_conflict: bool = False) -> dict[str, PackageManifest]:
    shared = PackageManifest("shared", "1.0.0")
    left = PackageManifest(
        "left",
        "1.0.0",
        (PackageDependency("shared", "vendor/shared"),),
    )
    right_source = "vendor/other-shared" if conflicting_reachable else "vendor/shared"
    right = PackageManifest(
        "right",
        "1.0.0",
        (PackageDependency("shared", right_source),),
    )
    app = PackageManifest(
        "app",
        "1.0.0",
        (
            PackageDependency("left", "vendor/left"),
            PackageDependency("right", "vendor/right"),
        ),
    )
    manifests: dict[str, PackageManifest] = {
        "app": app,
        "left": left,
        "right": right,
        "shared": shared,
    }
    if add_unreachable_conflict:
        manifests["unused"] = PackageManifest(
            "unused",
            "1.0.0",
            (PackageDependency("shared", "vendor/unreachable-conflict"),),
        )
    return manifests


def _run_dependency_lock_case() -> dict[str, Any]:
    manifests = _dependency_graph()
    first = PackageLock.resolve("app", manifests)
    reverse_mapping = dict(reversed(tuple(manifests.items())))
    second = PackageLock.resolve("app", reverse_mapping)

    entries = {entry.name: entry for entry in first.entries}
    conflict_rejected = _expect_raises(
        PackageDependencyError,
        lambda: PackageLock.resolve("app", _dependency_graph(conflicting_reachable=True)),
        "inconsistent dependency identity",
    )
    with_unreachable = PackageLock.resolve("app", _dependency_graph(add_unreachable_conflict=True))

    return {
        "mapping_order_invariant": first.text == second.text,
        "lock_sha_invariant": first.sha256 == second.sha256,
        "topological_order": list(first.topological_order),
        "shared_source": entries["shared"].source,
        "shared_revision": entries["shared"].revision,
        "conflicting_reachable_identity_rejected": conflict_rejected,
        "unreachable_conflict_isolated": with_unreachable.text == first.text,
        "root_source": entries["app"].source,
        "root_revision": entries["app"].revision,
    }


def _tar_bytes(members: tuple[tuple[str, bytes], ...], *, gzip: bool = False) -> bytes:
    output = io.BytesIO()
    with tarfile.open(fileobj=output, mode="w:gz" if gzip else "w") as archive:
        for name, content in members:
            info = tarfile.TarInfo(name)
            info.size = len(content)
            info.mtime = 0
            info.uid = 0
            info.gid = 0
            info.uname = ""
            info.gname = ""
            archive.addfile(info, io.BytesIO(content))
    return output.getvalue()


def _make_registry(base: Path, payload: bytes, **limits: int) -> tuple[RegistryClient, RegistryLock]:
    digest = hashlib.sha256(payload).hexdigest()
    root = base / "registry"
    (root / "objects").mkdir(parents=True)
    (root / "objects" / "package.tar").write_bytes(payload)
    (root / "index.json").write_text(
        json.dumps(
            {
                "format": "s3.registry.index.v1",
                "packages": [
                    {
                        "name": "demo",
                        "version": "1.0.0",
                        "sha256": digest,
                        "object": "objects/package.tar",
                    }
                ],
            },
            sort_keys=True,
        ),
        encoding="utf-8",
    )
    return RegistryClient(root, **limits), RegistryLock("demo", "1.0.0", digest)


def _run_registry_case() -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="s3-bench-registry-") as directory:
        base = Path(directory)
        payload = _tar_bytes(
            (
                ("src/main.s3", b"fn main() -> i64:\n    return 1\n"),
                ("src/lib.s3", b"fn value() -> i64:\n    return 7\n"),
            )
        )
        client, lock = _make_registry(base / "primary", payload)
        exact_lock_match = client.resolve("demo", "1.0.0") == lock
        artifact = client.fetch(lock)
        object_path = client.root / "objects" / "package.tar"
        object_path.unlink()
        cache_survives = client.fetch(lock).archive == payload

        install = base / "install"
        installed_paths = list(client.install(artifact, install))
        contents_match = (
            (install / "src" / "main.s3").read_bytes() == b"fn main() -> i64:\n    return 1\n"
            and (install / "src" / "lib.s3").read_bytes() == b"fn value() -> i64:\n    return 7\n"
        )

        # Corrupt the immutable cache after the successful round trip.  A cache
        # hit must still verify the content hash and fail closed.
        cache_path = client.cache / lock.sha256
        cache_path.write_bytes(b"corrupted-cache")
        cache_hash_mismatch = _expect_raises(
            RegistryError,
            lambda: client.fetch(lock),
            "SHA-256",
        )

        traversal_payload = _tar_bytes((("../escape.s3", b"escape"),))
        traversal_client, traversal_lock = _make_registry(base / "traversal", traversal_payload)
        traversal_rejected = _expect_raises(
            RegistryError,
            lambda: traversal_client.install(traversal_client.fetch(traversal_lock), base / "traversal-out"),
            "traversal",
        )

        duplicate_payload = _tar_bytes(
            (("src/main.s3", b"one"), ("src/./main.s3", b"two"))
        )
        duplicate_client, duplicate_lock = _make_registry(base / "duplicate", duplicate_payload)
        duplicate_rejected = _expect_raises(
            RegistryError,
            lambda: duplicate_client.install(duplicate_client.fetch(duplicate_lock), base / "duplicate-out"),
            "duplicate canonical",
        )

        oversized_payload = _tar_bytes((("large.s3", b"x" * 2048),), gzip=True)
        limit_client, limit_lock = _make_registry(
            base / "limits",
            oversized_payload,
            max_member_bytes=1024,
        )
        member_limit_rejected = _expect_raises(
            RegistryError,
            lambda: limit_client.install(limit_client.fetch(limit_lock), base / "limits-out"),
            "member exceeds",
        )

        publish_rejected = _expect_raises(
            RegistryError,
            lambda: client.publish(artifact),
            "read-only",
        )

        return {
            "read_only": client.read_only,
            "exact_lock_match": exact_lock_match,
            "cache_survives_object_removal": cache_survives,
            "cache_hash_mismatch_rejected": cache_hash_mismatch,
            "installed_paths": installed_paths,
            "installed_contents_match": contents_match,
            "path_traversal_rejected": traversal_rejected,
            "duplicate_canonical_path_rejected": duplicate_rejected,
            "member_limit_rejected": member_limit_rejected,
            "publish_rejected": publish_rejected,
        }


def _run_toolchain_bundle_case() -> dict[str, Any]:
    bundler = ToolchainBundler()
    files_a = {"bin/s3": b"compiler", "lib/core.s3": b"fn core() {}\n"}
    files_b = {"lib/core.s3": b"fn core() {}\n", "bin/s3": b"compiler"}
    first = bundler.build(
        files_a,
        license_text="Apache-2.0\n",
        metadata={"version": "1.80", "instruction_limit": "100000"},
    )
    second = bundler.build(
        files_b,
        license_text="Apache-2.0\n",
        metadata={"instruction_limit": "100000", "version": "1.80"},
    )
    bundler.verify(first)

    with zipfile.ZipFile(io.BytesIO(first.data), "r") as archive:
        infos = archive.infolist()
        entry_order = [info.filename for info in infos]
        fixed_timestamps = all(info.date_time == (1980, 1, 1, 0, 0, 0) for info in infos)
        fixed_permissions = all(((info.external_attr >> 16) & 0o777) == 0o644 for info in infos)
        license_present = archive.read("LICENSE") == b"Apache-2.0\n"
        manifest = json.loads(archive.read("MANIFEST.json"))
        manifest_paths = [item["path"] for item in manifest["files"]]

    corrupted_output = io.BytesIO()
    with zipfile.ZipFile(io.BytesIO(first.data), "r") as source, zipfile.ZipFile(
        corrupted_output, "w", compression=zipfile.ZIP_STORED
    ) as target:
        for info in source.infolist():
            data = source.read(info.filename)
            if info.filename == "bin/s3":
                data = b"changed-compiler"
            target.writestr(info, data)
    corrupted = type(first)(corrupted_output.getvalue(), first.manifest)

    return {
        "byte_identical_across_input_order": first.data == second.data,
        "sha256_identical": first.sha256 == second.sha256,
        "manifest_file_paths": manifest_paths,
        "zip_entry_order": entry_order,
        "fixed_timestamps": fixed_timestamps,
        "fixed_permissions": fixed_permissions,
        "license_present": license_present,
        "verify_passed": True,
        "corruption_rejected": _expect_raises(
            DistributionError,
            lambda: bundler.verify(corrupted),
        ),
        "machine_path_rejected": _expect_raises(
            DistributionError,
            lambda: bundler.build(
                {"C:\\Users\\user\\secret": b"x"},
                license_text="Apache-2.0",
                metadata={},
            ),
            "rejected",
        ),
        "traversal_path_rejected": _expect_raises(
            DistributionError,
            lambda: bundler.build(
                {"../escape": b"x"},
                license_text="Apache-2.0",
                metadata={},
            ),
            "rejected",
        ),
        "reserved_path_rejected": _expect_raises(
            DistributionError,
            lambda: bundler.build(
                {"LICENSE": b"override"},
                license_text="Apache-2.0",
                metadata={},
            ),
            "reserved",
        ),
        "remote_publish_rejected": _expect_raises(
            DistributionError,
            lambda: bundler.publish(first),
            "local-only",
        ),
    }


def collect_results() -> dict[str, Any]:
    return {
        "dependency_lock": _run_dependency_lock_case(),
        "registry": _run_registry_case(),
        "toolchain_bundle": _run_toolchain_bundle_case(),
    }


def verify_behavioral_contract() -> tuple[bool, dict[str, Any]]:
    actual = collect_results()
    canonical = json.dumps(actual, sort_keys=True, separators=(",", ":"))
    passed = actual == EXPECTED
    return passed, {
        "schema": "s3.package-repro.correctness.v1",
        "performance_results_valid": False,
        "performance_status": "DEFERRED_UNTIL_EQUIVALENT_NATIVE_RESOLVER_WORKLOAD_EXISTS",
        "public_registry_required": False,
        "registry_publishing_supported": False,
        "remote_release_supported": False,
        "expected": EXPECTED,
        "actual": actual,
        "actual_sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
        "passed": passed,
    }


if __name__ == "__main__":
    ok, report = verify_behavioral_contract()
    print(json.dumps(report, indent=2, sort_keys=True))
    raise SystemExit(0 if ok else 1)
