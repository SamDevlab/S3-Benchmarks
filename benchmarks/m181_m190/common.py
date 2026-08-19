"""Shared deterministic checks for the M1.81-M1.90 campaign.

This campaign is intentionally explicit about its S3 checkout.  Results are
characterization-only unless a separately pinned reference toolchain is
available and the observable contract passes first.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import socket
import sys
import tempfile
import threading
import time
from typing import Callable


CAMPAIGN = "m181-m190"
EXECUTABLE_CHECKS = (
    "async_task",
    "await_chain",
    "channels",
    "executor",
    "process_io",
    "http_loopback",
    "registry_cache",
    "reproducibility",
)


@dataclass(frozen=True)
class Check:
    name: str
    status: str
    observed: object
    expected: object
    applicability: str
    note: str = ""

    def as_json(self) -> dict[str, object]:
        return asdict(self)


def s3_root() -> Path:
    value = os.environ.get("S3_REPO", "")
    if not value:
        raise RuntimeError("S3_REPO must point to the campaign checkout")
    root = Path(value).resolve()
    if not (root / "bootstrap" / "s3").is_dir():
        raise RuntimeError(f"S3_REPO is not an S3 checkout: {root}")
    text = str(root)
    if text not in sys.path:
        sys.path.insert(0, text)
    return root


def _equal(name: str, observed: object, expected: object, *, note: str = "") -> Check:
    return Check(name, "PASS" if observed == expected else "FAIL", observed, expected, "PERFORMANCE_ELIGIBLE", note)


def _deferred(name: str, note: str) -> Check:
    return Check(name, "DEFERRED", None, None, "DEFERRED", note)


def _async_task() -> tuple[object, object]:
    s3_root()
    from bootstrap.s3.async_core import AsyncFuture, complete, pending

    step_count = [0]

    def step(_frame):
        if step_count[0] == 0:
            step_count[0] += 1
            return pending()
        step_count[0] += 1
        return complete(7)

    future = AsyncFuture(step)
    first = future.poll()
    second = future.poll()
    observed = {"value": second.value, "polls": step_count[0], "states": [first.state.value, second.state.value]}
    expected = {"value": 7, "polls": 2, "states": ["suspended", "completed"]}
    return observed, expected


def _await_chain() -> tuple[object, object]:
    s3_root()
    from bootstrap.s3.pipeline import compile_source, run_source

    source = (
        "async fn leaf() -> i64:\n"
        "    return 3\n"
        "async fn middle() -> i64:\n"
        "    return await leaf()\n"
        "async fn main() -> i64:\n"
        "    first: i64 = await middle()\n"
        "    second: i64 = await leaf()\n"
        "    return first + second\n"
    )
    compilation = compile_source(source)
    observed = {"value": run_source(source), "async_functions": len(compilation.async_ir.functions)}
    expected = {"value": 6, "async_functions": 3}
    return observed, expected


def _executor() -> tuple[object, object]:
    s3_root()
    from bootstrap.s3.async_core import AsyncFuture, complete
    from bootstrap.s3.async_futures import MoveOnlyFuture
    from bootstrap.s3.async_threads import BoundedThreadExecutor, ThreadExecutorLimits

    executor = BoundedThreadExecutor(limits=ThreadExecutorLimits(max_workers=2, max_tasks=4, max_ready=4))
    try:
        for value in (2, 4, 6):
            owner = MoveOnlyFuture(AsyncFuture(lambda _frame, value=value: complete(value)))
            if executor.spawn(owner).is_err:
                raise RuntimeError("executor admission failed")
        deadline = time.monotonic() + 3.0
        polls = []
        while len(polls) < 3 and time.monotonic() < deadline:
            polls.extend(executor.take_polls())
            time.sleep(0.002)
        observed = {"values": sorted(item.poll.value for item in polls), "polls": len(polls), "tasks_after": executor.task_count}
    finally:
        executor.close()
    expected = {"values": [2, 4, 6], "polls": 3, "tasks_after": 0}
    return observed, expected


def _channels() -> tuple[object, object]:
    s3_root()
    from bootstrap.s3.async_channels import AsyncChannel, ChannelErrorCode, OwnedMessage

    observed = []
    for capacity in (1, 8, 64):
        channel = AsyncChannel[int](capacity=capacity)
        sender, receiver = channel.split()
        total = capacity * 2 + 3
        received: list[int] = []
        next_value = 0
        while next_value < total:
            message = OwnedMessage(next_value)
            result = sender.send(message)
            if result.is_ok:
                next_value += 1
                continue
            error = result.error_or(None)
            if error is None or error.code is not ChannelErrorCode.FULL:
                raise RuntimeError("channel admission failed")
            item = receiver.recv()
            if item.is_err:
                raise RuntimeError("channel drain failed")
            received.append(item.value_or(None).move().value_or(None))
        sender.close()
        while True:
            item = receiver.recv()
            if item.is_ok:
                received.append(item.value_or(None).move().value_or(None))
                continue
            error = item.error_or(None)
            if error is None or error.code is not ChannelErrorCode.CLOSED:
                raise RuntimeError("channel close contract failed")
            break
        receiver.close()
        observed.append({
            "capacity": capacity,
            "count": len(received),
            "first": received[0],
            "last": received[-1],
            "checksum": hashlib.sha256(",".join(map(str, received)).encode("ascii")).hexdigest(),
            "closed": channel.closed,
        })
    expected = []
    for capacity in (1, 8, 64):
        values = list(range(capacity * 2 + 3))
        expected.append({
            "capacity": capacity,
            "count": len(values),
            "first": values[0],
            "last": values[-1],
            "checksum": hashlib.sha256(",".join(map(str, values)).encode("ascii")).hexdigest(),
            "closed": True,
        })
    return observed, expected


def _process_io() -> tuple[object, object]:
    s3_root()
    from bootstrap.s3.async_io import AsyncIOService

    with tempfile.TemporaryDirectory(prefix="s3-m181-process-") as directory:
        service = AsyncIOService(root=Path(directory))
        result = service.run_process(
            sys.executable,
            ("-c", "import sys; sys.stdout.write('s3-process-ok')"),
            timeout=5.0,
        ).await_once(max_polls=2)
    if result.is_err:
        raise RuntimeError(result.error_or(None).detail)
    output = result.value_or(None)
    observed = {"stdout": output.stdout.decode("ascii"), "stderr": output.stderr.decode("ascii"), "returncode": output.returncode}
    expected = {"stdout": "s3-process-ok", "stderr": "", "returncode": 0}
    return observed, expected


def _serve_once(response: bytes) -> tuple[int, threading.Thread]:
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    port = listener.getsockname()[1]

    def serve() -> None:
        try:
            connection, _address = listener.accept()
            with connection:
                connection.settimeout(2.0)
                connection.recv(4096)
                connection.sendall(response)
        finally:
            listener.close()

    thread = threading.Thread(target=serve, daemon=True)
    thread.start()
    return port, thread


def _http_loopback() -> tuple[object, object]:
    s3_root()
    from bootstrap.s3.async_http import BoundedHTTPClient, SocketHTTPTransport

    body = b"loopback-ok"
    response = b"HTTP/1.1 200 OK\r\nContent-Length: 11\r\nConnection: close\r\n\r\n" + body
    port, thread = _serve_once(response)
    client = BoundedHTTPClient(SocketHTTPTransport())
    result = client.get(f"http://127.0.0.1:{port}/result").await_once(max_polls=2)
    thread.join(timeout=2.0)
    if result.is_err:
        raise RuntimeError(result.error_or(None).detail)
    payload = result.value_or(None)
    observed = {"status": payload.status, "body": payload.body.decode("ascii"), "body_sha256": hashlib.sha256(payload.body).hexdigest()}
    expected = {"status": 200, "body": "loopback-ok", "body_sha256": hashlib.sha256(body).hexdigest()}
    return observed, expected


class _RegistryFixtureTransport:
    def __init__(self, body: bytes) -> None:
        self.body = body

    def request(self, *, scheme: str, host: str, port: int, request: bytes, max_response_bytes: int, timeout: float) -> bytes:
        del port, timeout
        if scheme != "https" or host != "registry.fixture":
            raise ValueError("unexpected registry authority")
        return b"HTTP/1.1 200 OK\r\nContent-Length: " + str(len(self.body)).encode("ascii") + b"\r\nConnection: close\r\n\r\n" + self.body


def _registry_cache() -> tuple[object, object]:
    s3_root()
    from bootstrap.s3.async_http import BoundedHTTPClient
    from bootstrap.s3.registry_transport import BoundedVerifiedCache, HTTPSContentAddressedRegistry

    body = b"verified-registry-object"
    digest = hashlib.sha256(body).hexdigest()
    client = BoundedHTTPClient(_RegistryFixtureTransport(body))
    registry = HTTPSContentAddressedRegistry(client, cache=BoundedVerifiedCache(max_entries=2, max_bytes=1024))
    first = registry.fetch(digest).await_once(max_polls=2)
    second = registry.fetch(digest).await_once(max_polls=2)
    if first.is_err or second.is_err:
        raise RuntimeError("registry fixture fetch failed")
    observed = {"digest": first.value_or(None).digest, "first_cache": first.value_or(None).from_cache, "second_cache": second.value_or(None).from_cache, "cache_keys": len(registry.cache.keys)}
    expected = {"digest": digest, "first_cache": False, "second_cache": True, "cache_keys": 1}
    return observed, expected


def _signature() -> Check:
    if importlib.util.find_spec("cryptography") is None:
        return _deferred("signature", "cryptography provider is unavailable on this host")
    s3_root()
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    from bootstrap.s3.package_signatures import PackageSignatureEnvelope, PackageSignatureService, PublicTrustStore, TrustedPublicKey, canonical_signing_payload

    body = b"signed-package"
    private = Ed25519PrivateKey.generate()
    public = private.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    digest = hashlib.sha256(body).hexdigest()
    envelope = PackageSignatureEnvelope("demo", "1.0", digest, "publisher", "key-1", b"", (("source_commit", "fixture"),))
    signature = private.sign(canonical_signing_payload(envelope))
    envelope = PackageSignatureEnvelope(envelope.name, envelope.version, envelope.digest, envelope.publisher, envelope.key_id, signature, envelope.provenance, envelope.source)
    store = PublicTrustStore()
    store.add(TrustedPublicKey("key-1", "publisher", public))
    verified = PackageSignatureService(store).verify(envelope, body)
    return _equal("signature", verified.is_ok, True, note="Ed25519 provider-backed verification")


def _reproducibility() -> tuple[object, object]:
    s3_root()
    from bootstrap.s3.toolchain_distribution import ToolchainBundler

    license_text = (s3_root() / "LICENSE").read_text(encoding="utf-8")
    files = {"bin/s3": b"deterministic", "lib/manifest.txt": b"fixture"}
    bundler = ToolchainBundler()
    first = bundler.build(files, license_text=license_text, metadata={"commit": "fixture", "version": "1.0"})
    second = bundler.build(files, license_text=license_text, metadata={"commit": "fixture", "version": "1.0"})
    bundler.verify(first)
    bundler.verify(second)
    return {"sha256": first.sha256, "bytes": len(first.data)}, {"sha256": second.sha256, "bytes": len(second.data)}


def _aarch64_structure() -> Check:
    s3_root()
    from bootstrap.s3.arm64_integration import LinuxAArch64Integration
    from bootstrap.s3.pipeline import compile_source

    source = "fn main() -> i64:\n    return 7\n"
    artifact = LinuxAArch64Integration().build_program(compile_source(source).assembly)
    observed = {"target": artifact.target.name, "structural": artifact.structural_valid, "native": artifact.execution_status.value, "instructions": artifact.instruction_count}
    expected = {"target": "linux-aarch64", "structural": True, "native": "deferred_by_environment", "instructions": artifact.instruction_count}
    return Check("aarch64_structure", "PASS" if observed == expected else "FAIL", observed, expected, "STRUCTURAL_ONLY", "Windows host cannot execute Linux AArch64")


def _tls_policy() -> Check:
    s3_root()
    from bootstrap.s3.async_http import SocketHTTPTransport

    transport = SocketHTTPTransport()
    context = transport._tls_context
    observed = {"verify_mode": context.verify_mode.name, "check_hostname": context.check_hostname}
    expected = {"verify_mode": "CERT_REQUIRED", "check_hostname": True}
    return Check("tls_policy", "PASS" if observed == expected else "FAIL", observed, expected, "STRUCTURAL_ONLY", "No local certificate fixture is installed for handshake timing")


def run_check(name: str) -> Check:
    if name == "signature":
        return _signature()
    if name == "aarch64_structure":
        return _aarch64_structure()
    if name == "tls_policy":
        return _tls_policy()
    functions: dict[str, Callable[[], tuple[object, object]]] = {
        "async_task": _async_task,
        "await_chain": _await_chain,
        "channels": _channels,
        "executor": _executor,
        "process_io": _process_io,
        "http_loopback": _http_loopback,
        "registry_cache": _registry_cache,
        "reproducibility": _reproducibility,
    }
    try:
        observed, expected = functions[name]()
        note = "independent deterministic reference contract; no external timing claim"
        return _equal(name, observed, expected, note=note)
    except Exception as error:
        return Check(name, "FAIL", type(error).__name__, "successful bounded execution", "PERFORMANCE_ELIGIBLE", str(error))


def run_all() -> list[Check]:
    checks = [run_check(name) for name in EXECUTABLE_CHECKS]
    checks.extend((run_check("tls_policy"), run_check("signature"), run_check("aarch64_structure")))
    return checks


def render(checks: list[Check]) -> dict[str, object]:
    statuses = [item.status for item in checks]
    return {
        "schema": "s3.m181-m190.correctness.v1",
        "campaign": CAMPAIGN,
        "s3_commit": os.environ.get("S3_COMMIT", "UNSPECIFIED"),
        "status": "FAIL" if "FAIL" in statuses else "PASS_WITH_DEFERRED" if "DEFERRED" in statuses else "PASS",
        "checks": [item.as_json() for item in checks],
        "deferred": statuses.count("DEFERRED"),
        "failed": statuses.count("FAIL"),
        "passed": statuses.count("PASS"),
    }


if __name__ == "__main__":
    print(json.dumps(render(run_all()), indent=2, sort_keys=True))
    raise SystemExit(1 if any(item.status == "FAIL" for item in run_all()) else 0)
