"""MoneyPrinterTurbo-inspired provider pipeline correctness gate.

This is a bounded integration workload, not a port of MoneyPrinterTurbo.  The
provider registry is benchmark-local and intentionally mirrors only the useful
architectural shape: stable provider metadata is separate from adapter/runtime
execution.  The actual I/O path exercises S3 M1.66/M1.74/M1.75 hosted contracts
against deterministic local fixtures with no secrets or public internet.

JSON parsing/serialization in this first integration gate belongs to the Python
benchmark harness.  The report states that limitation explicitly; it is not
presented as an S3 JSON-runtime feature.
"""

from __future__ import annotations

import hashlib
import json
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from bootstrap.s3.async_core import PollKind
from bootstrap.s3.async_network import (
    AsyncNetworkError,
    AsyncNetworkErrorCode,
    AsyncNetworkService,
    PendingOperation,
    PendingResource,
    ProviderFailure,
)
from bootstrap.s3.async_tls import (
    AsyncTlsClient,
    AsyncTlsConfig,
    AsyncTlsError,
    AsyncTlsErrorCode,
    AsyncTlsService,
    Failure,
    Ready,
    WantRead,
    WantWrite,
)
from bootstrap.s3.network import NetworkAddress
from bootstrap.s3.os_services import CrossPlatformOSServices, HostPath


class PipelineError(ValueError):
    pass


@dataclass(frozen=True, slots=True)
class ProviderSpec:
    provider_id: str
    adapter: str
    hostname: str
    port: int
    request_path: str
    default_model: str

    def __post_init__(self) -> None:
        if not self.provider_id or not self.adapter or not self.hostname:
            raise PipelineError("provider metadata must be non-empty")
        if isinstance(self.port, bool) or not isinstance(self.port, int) or not 1 <= self.port <= 65535:
            raise PipelineError("provider port must be in [1, 65535]")
        if not self.request_path.startswith("/") or not self.default_model:
            raise PipelineError("provider request path/model is invalid")

    def resolve_model(self, configured: str | None) -> str:
        value = (configured or "").strip()
        return value or self.default_model


PROVIDER_REGISTRY = (
    ProviderSpec(
        provider_id="fixture-openai",
        adapter="openai_compatible",
        hostname="fixture.local",
        port=9443,
        request_path="/v1/chat/completions",
        default_model="fixture-chat-v1",
    ),
    ProviderSpec(
        provider_id="fixture-gemini",
        adapter="gemini",
        hostname="gemini.fixture.local",
        port=9444,
        request_path="/v1/generate",
        default_model="fixture-gemini-v1",
    ),
)


@dataclass(frozen=True, slots=True)
class PipelineConfig:
    provider: str
    prompt: str
    output: str
    model: str = ""

    @classmethod
    def parse(cls, raw: str) -> "PipelineConfig":
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as error:
            raise PipelineError("config JSON is invalid") from error
        if not isinstance(value, dict):
            raise PipelineError("config must be an object")
        provider = value.get("provider")
        prompt = value.get("prompt")
        output = value.get("output")
        model = value.get("model", "")
        if not isinstance(provider, str) or not provider or len(provider) > 128:
            raise PipelineError("provider id is invalid")
        if not isinstance(prompt, str) or not prompt or len(prompt.encode("utf-8")) > 4096:
            raise PipelineError("prompt is invalid or exceeds 4096 bytes")
        if not isinstance(output, str) or not output or len(output) > 240:
            raise PipelineError("output path is invalid")
        if not isinstance(model, str) or len(model) > 256:
            raise PipelineError("model is invalid")
        return cls(provider=provider, prompt=prompt, output=output, model=model)


def _provider(provider_id: str) -> ProviderSpec:
    match = next((item for item in PROVIDER_REGISTRY if item.provider_id == provider_id), None)
    if match is None:
        raise PipelineError(f"unknown provider: {provider_id}")
    return match


def _result_value(result, operation: str):
    if result.is_err:
        raise PipelineError(f"{operation} failed: {result.error_or(None)!r}")
    return result.value_or(None)


def _poll_terminal(future, operation: str, *, max_polls: int = 8):
    polls = []
    for _ in range(max_polls):
        current = future.poll()
        polls.append(current)
        if current.kind is not PollKind.PENDING:
            if current.kind is not PollKind.READY:
                raise PipelineError(f"{operation} failed: {current.error!r}")
            return polls, current.value
    raise PipelineError(f"{operation} exceeded deterministic poll bound")


def _write_text(os_service: CrossPlatformOSServices, path: str, text: str) -> None:
    try:
        host_path = HostPath(path)
    except ValueError as error:
        raise PipelineError(f"output path rejected: {path!r}") from error
    handle = _result_value(os_service.open_text(host_path, "w"), "open for write")
    if handle is None:
        raise PipelineError("open for write returned no handle")
    try:
        _result_value(handle.write(text), "write text")
    finally:
        handle.close()


def _read_text(os_service: CrossPlatformOSServices, path: str) -> str:
    try:
        host_path = HostPath(path)
    except ValueError as error:
        raise PipelineError(f"input path rejected: {path!r}") from error
    handle = _result_value(os_service.open_text(host_path, "r"), "open for read")
    if handle is None:
        raise PipelineError("open for read returned no handle")
    try:
        value = _result_value(handle.read(), "read text")
        if not isinstance(value, str):
            raise PipelineError("text read returned non-string")
        return value
    finally:
        handle.close()


@dataclass(slots=True)
class _Transport:
    address: NetworkAddress
    closed: bool = False


class _LocalNetworkProvider:
    def __init__(self, expected_port: int) -> None:
        self.expected_port = expected_port
        self.transport: _Transport | None = None
        self.connect_calls = 0
        self.resolve_calls = 0
        self.closed: list[object] = []

    def resolve(self, host: str, port: int):
        self.resolve_calls += 1
        if not host.endswith("fixture.local") or port != self.expected_port:
            return ProviderFailure(
                AsyncNetworkError(
                    AsyncNetworkErrorCode.PROVIDER_FAILURE,
                    "resolve",
                    "fixture host/port mismatch",
                )
            )
        return (NetworkAddress.numeric("127.0.0.1", port),)

    def connect(self, address: NetworkAddress):
        self.connect_calls += 1
        if address.host != "127.0.0.1" or address.port != self.expected_port:
            return ProviderFailure(
                AsyncNetworkError(
                    AsyncNetworkErrorCode.PROVIDER_FAILURE,
                    "connect",
                    "fixture address mismatch",
                )
            )
        if self.transport is None:
            self.transport = _Transport(address)
        if self.connect_calls == 1:
            return PendingResource(self.transport)
        return self.transport

    def accept(self, _listener):
        return ProviderFailure(
            AsyncNetworkError(
                AsyncNetworkErrorCode.PROVIDER_FAILURE,
                "accept",
                "server accept is out of scope",
            )
        )

    def read(self, _stream, _amount):
        return PendingOperation()

    def write(self, _stream, _data):
        return PendingOperation()

    def udp_send(self, _socket, _data, _address):
        return ProviderFailure(
            AsyncNetworkError(AsyncNetworkErrorCode.PROVIDER_FAILURE, "udp_send", "out of scope")
        )

    def udp_receive(self, _socket):
        return ProviderFailure(
            AsyncNetworkError(AsyncNetworkErrorCode.PROVIDER_FAILURE, "udp_receive", "out of scope")
        )

    def close(self, resource):
        if hasattr(resource, "closed"):
            resource.closed = True
        self.closed.append(resource)


@dataclass(slots=True)
class _TlsSession:
    transport: _Transport
    closed: bool = False


class _LocalTlsProvider:
    def __init__(self, spec: ProviderSpec) -> None:
        self.spec = spec
        self.handshake_calls = 0
        self.write_calls = 0
        self.read_calls = 0
        self.closed: list[object] = []
        self.request_bytes: bytes | None = None
        self.response_bytes: bytes | None = None

    def handshake(self, connection: _TlsSession, hostname: str):
        self.handshake_calls += 1
        if hostname != self.spec.hostname or connection.transport.closed:
            return Failure(
                AsyncTlsError(AsyncTlsErrorCode.HOSTNAME, "handshake", "fixture hostname mismatch")
            )
        if self.handshake_calls == 1:
            return WantRead()
        return Ready(True)

    def write(self, connection: _TlsSession, data: bytes):
        self.write_calls += 1
        if connection.closed or connection.transport.closed:
            return Failure(AsyncTlsError(AsyncTlsErrorCode.CLOSED, "write", "fixture session closed"))
        if self.write_calls == 1:
            return WantWrite()
        self.request_bytes = bytes(data)
        try:
            header, body = self.request_bytes.split(b"\r\n\r\n", 1)
            request = json.loads(body.decode("utf-8"))
        except (ValueError, UnicodeError, json.JSONDecodeError) as error:
            return Failure(AsyncTlsError(AsyncTlsErrorCode.IO, "write", f"invalid request: {error}"))
        expected_first_line = f"POST {self.spec.request_path} HTTP/1.1".encode("ascii")
        if not header.startswith(expected_first_line) or not isinstance(request, dict):
            return Failure(AsyncTlsError(AsyncTlsErrorCode.IO, "write", "invalid request envelope"))
        prompt = request.get("prompt")
        model = request.get("model")
        provider = request.get("provider")
        if not isinstance(prompt, str) or not isinstance(model, str) or provider != self.spec.provider_id:
            return Failure(AsyncTlsError(AsyncTlsErrorCode.IO, "write", "invalid request payload"))
        response = {
            "id": "fixture-0001",
            "model": model,
            "provider": provider,
            "text": prompt.upper(),
        }
        self.response_bytes = json.dumps(
            response,
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        return Ready(len(data))

    def read(self, connection: _TlsSession, amount: int):
        self.read_calls += 1
        if connection.closed or connection.transport.closed:
            return Failure(AsyncTlsError(AsyncTlsErrorCode.CLOSED, "read", "fixture session closed"))
        if self.read_calls == 1:
            return WantRead()
        if self.response_bytes is None:
            return Failure(AsyncTlsError(AsyncTlsErrorCode.IO, "read", "request was not written"))
        return Ready(self.response_bytes[:amount])

    def close(self, connection: _TlsSession):
        connection.closed = True
        self.closed.append(connection)


def _canonical_request(spec: ProviderSpec, model: str, prompt: str) -> bytes:
    body = json.dumps(
        {"model": model, "prompt": prompt, "provider": spec.provider_id},
        ensure_ascii=True,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    header = (
        f"POST {spec.request_path} HTTP/1.1\r\n"
        f"Host: {spec.hostname}\r\n"
        "Content-Type: application/json\r\n"
        f"Content-Length: {len(body)}\r\n"
        "\r\n"
    ).encode("ascii")
    return header + body


def _execute_pipeline(config_mapping: Mapping[str, object]) -> dict[str, Any]:
    network_provider: _LocalNetworkProvider | None = None
    tls_provider: _LocalTlsProvider | None = None
    network_service: AsyncNetworkService | None = None
    network_handle = None
    tls_client: AsyncTlsClient | None = None
    result: dict[str, Any] = {}
    error_text: str | None = None

    with tempfile.TemporaryDirectory(prefix="s3-provider-pipeline-") as temporary:
        root = Path(temporary)
        os_service = CrossPlatformOSServices(root=root, environment={})
        config_text = json.dumps(config_mapping, ensure_ascii=True, separators=(",", ":")) + "\n"
        _write_text(os_service, "config.json", config_text)

        try:
            config = PipelineConfig.parse(_read_text(os_service, "config.json"))
            spec = _provider(config.provider)
            model = spec.resolve_model(config.model)

            network_provider = _LocalNetworkProvider(spec.port)
            network_service = AsyncNetworkService(network_provider, max_handles=2)
            dns_polls, addresses = _poll_terminal(
                network_service.resolve(spec.hostname, spec.port),
                "resolve provider",
            )
            if not isinstance(addresses, tuple) or len(addresses) != 1:
                raise PipelineError("fixture DNS must resolve exactly one address")

            connect_polls, network_handle = _poll_terminal(
                network_service.connect(addresses[0]),
                "connect provider",
            )
            if network_handle is None or not isinstance(network_handle.resource, _Transport):
                raise PipelineError("network connection returned invalid transport")

            tls_provider = _LocalTlsProvider(spec)
            session = _TlsSession(network_handle.resource)
            tls_polls, tls_client = _poll_terminal(
                AsyncTlsService(tls_provider).handshake(
                    session,
                    AsyncTlsConfig(spec.hostname, max_read_write=8192),
                ),
                "TLS handshake",
            )
            if not isinstance(tls_client, AsyncTlsClient):
                raise PipelineError("TLS handshake returned invalid client")

            request = _canonical_request(spec, model, config.prompt)
            write_polls, write_count = _poll_terminal(tls_client.write(request), "TLS write")
            read_polls, response_bytes = _poll_terminal(tls_client.read(8192), "TLS read")
            if not isinstance(response_bytes, bytes):
                raise PipelineError("provider response is not bytes")
            try:
                response = json.loads(response_bytes.decode("utf-8"))
            except (UnicodeError, json.JSONDecodeError) as error:
                raise PipelineError("provider response JSON is invalid") from error
            if not isinstance(response, dict):
                raise PipelineError("provider response must be an object")

            output = {
                "id": response.get("id"),
                "model": response.get("model"),
                "provider": response.get("provider"),
                "text": response.get("text"),
            }
            output_text = json.dumps(
                output,
                ensure_ascii=True,
                sort_keys=True,
                separators=(",", ":"),
            ) + "\n"
            _write_text(os_service, config.output, output_text)
            output_readback = _read_text(os_service, config.output)

            result = {
                "provider": spec.provider_id,
                "adapter": spec.adapter,
                "model": model,
                "dns_kinds": [poll.kind.value for poll in dns_polls],
                "dns_addresses": [f"{item.host}:{item.port}" for item in addresses],
                "connect_kinds": [poll.kind.value for poll in connect_polls],
                "tls_kinds": [poll.kind.value for poll in tls_polls],
                "write_kinds": [poll.kind.value for poll in write_polls],
                "write_count_matches": write_count == len(request),
                "read_kinds": [poll.kind.value for poll in read_polls],
                "verify_certificate": tls_client.config.verify_certificate,
                "verify_hostname": tls_client.config.verify_hostname,
                "request_path": spec.request_path,
                "request_sha256": hashlib.sha256(request).hexdigest(),
                "response_id": response.get("id"),
                "response_text": response.get("text"),
                "output_text": output_readback,
                "output_sha256": hashlib.sha256(output_readback.encode("utf-8")).hexdigest(),
            }
        except PipelineError as error:
            error_text = str(error)
        finally:
            if tls_client is not None:
                tls_client.close()
            if network_handle is not None:
                network_handle.close()

        cleanup = {
            "network_started": network_provider is not None,
            "network_close_count": len(network_provider.closed) if network_provider is not None else 0,
            "tls_close_count": len(tls_provider.closed) if tls_provider is not None else 0,
            "network_active_handles": network_service.active_handles if network_service is not None else 0,
        }
        if error_text is not None:
            return {"error": error_text, **cleanup}
        result.update(cleanup)
        return result


EXPECTED: dict[str, Any] = {
    "registry": {
        "ids": ["fixture-openai", "fixture-gemini"],
        "default_model": "fixture-chat-v1",
        "explicit_model": "custom-model-v2",
        "adapter": "openai_compatible",
    },
    "pipeline": {
        "provider": "fixture-openai",
        "adapter": "openai_compatible",
        "model": "fixture-chat-v1",
        "dns_kinds": ["ready"],
        "dns_addresses": ["127.0.0.1:9443"],
        "connect_kinds": ["pending", "ready"],
        "tls_kinds": ["pending", "ready"],
        "write_kinds": ["pending", "ready"],
        "write_count_matches": True,
        "read_kinds": ["pending", "ready"],
        "verify_certificate": True,
        "verify_hostname": True,
        "request_path": "/v1/chat/completions",
        "response_id": "fixture-0001",
        "response_text": "HELLO S3",
        "output_text": "{\"id\":\"fixture-0001\",\"model\":\"fixture-chat-v1\",\"provider\":\"fixture-openai\",\"text\":\"HELLO S3\"}\n",
        "network_started": True,
        "network_close_count": 1,
        "tls_close_count": 1,
        "network_active_handles": 0,
    },
    "determinism": {
        "same_request_sha": True,
        "same_output_sha": True,
        "same_output_text": True,
    },
    "unknown_provider": {
        "rejected": True,
        "network_started": False,
        "network_close_count": 0,
        "tls_close_count": 0,
    },
    "path_escape": {
        "rejected": True,
        "network_started": True,
        "network_close_count": 1,
        "tls_close_count": 1,
        "network_active_handles": 0,
    },
}


def collect_results() -> dict[str, Any]:
    default_spec = _provider("fixture-openai")
    registry = {
        "ids": [item.provider_id for item in PROVIDER_REGISTRY],
        "default_model": default_spec.resolve_model(""),
        "explicit_model": default_spec.resolve_model("custom-model-v2"),
        "adapter": default_spec.adapter,
    }

    first_config: dict[str, object] = {
        "provider": "fixture-openai",
        "prompt": "hello s3",
        "output": "out/result.json",
        "model": "",
    }
    second_config: dict[str, object] = {
        "model": "",
        "output": "out/result.json",
        "prompt": "hello s3",
        "provider": "fixture-openai",
    }
    first = _execute_pipeline(first_config)
    second = _execute_pipeline(second_config)
    if "error" in first or "error" in second:
        raise AssertionError(f"positive provider pipeline failed: {first!r} / {second!r}")

    pipeline = {
        key: value
        for key, value in first.items()
        if key not in {"request_sha256", "output_sha256"}
    }
    determinism = {
        "same_request_sha": first["request_sha256"] == second["request_sha256"],
        "same_output_sha": first["output_sha256"] == second["output_sha256"],
        "same_output_text": first["output_text"] == second["output_text"],
    }

    unknown = _execute_pipeline(
        {
            "provider": "missing-provider",
            "prompt": "hello",
            "output": "out/result.json",
        }
    )
    unknown_provider = {
        "rejected": "unknown provider" in str(unknown.get("error", "")),
        "network_started": unknown["network_started"],
        "network_close_count": unknown["network_close_count"],
        "tls_close_count": unknown["tls_close_count"],
    }

    escaped = _execute_pipeline(
        {
            "provider": "fixture-openai",
            "prompt": "hello s3",
            "output": "../escape.json",
        }
    )
    path_escape = {
        "rejected": "open for write failed" in str(escaped.get("error", "")),
        "network_started": escaped["network_started"],
        "network_close_count": escaped["network_close_count"],
        "tls_close_count": escaped["tls_close_count"],
        "network_active_handles": escaped["network_active_handles"],
    }

    return {
        "registry": registry,
        "pipeline": pipeline,
        "determinism": determinism,
        "unknown_provider": unknown_provider,
        "path_escape": path_escape,
    }


def verify_behavioral_contract() -> tuple[bool, dict[str, Any]]:
    actual = collect_results()
    canonical = json.dumps(actual, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
    report = {
        "schema": "s3.provider-pipeline.correctness.v1",
        "reference_shape": "MoneyPrinterTurbo provider registry / service layering",
        "fixture_scope": "deterministic_local_no_public_internet_no_secrets",
        "json_parser_scope": "python_benchmark_harness_not_s3_runtime_feature",
        "process_step": "not_included_in_v1_pipeline",
        "performance_results_valid": False,
        "performance_status": "DEFERRED_UNTIL_EQUIVALENT_NATIVE_S3_APPLICATION_WORKLOAD_EXISTS",
        "public_internet_required": False,
        "external_provider_calls": False,
        "secrets_required": False,
        "certificate_verification_required": True,
        "hostname_verification_required": True,
        "expected": EXPECTED,
        "actual": actual,
        "actual_sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
        "passed": actual == EXPECTED,
    }
    return report["passed"], report


if __name__ == "__main__":
    passed, report = verify_behavioral_contract()
    print(json.dumps(report, indent=2, sort_keys=True))
    raise SystemExit(0 if passed else 1)
