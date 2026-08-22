"""Deterministic reactor + local-network correctness gate for S3 M1.73/M1.74.

The fixture is intentionally local and provider-neutral.  It does not require
public DNS or public internet and it does not publish performance numbers.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Any

from bootstrap.s3.async_core import PollKind
from bootstrap.s3.async_executor import DeterministicReactor
from bootstrap.s3.async_network import (
    AsyncNetworkError,
    AsyncNetworkErrorCode,
    AsyncNetworkService,
    PendingOperation,
    PendingResource,
    ProviderFailure,
)
from bootstrap.s3.network import NetworkAddress


EXPECTED: dict[str, Any] = {
    "reactor": {
        "first_ready": [1, 2],
        "coalesced": True,
        "after_close": [],
    },
    "tcp_loopback": {
        "connect_kinds": ["pending", "ready"],
        "write_kinds": ["pending", "ready"],
        "write_count": 5,
        "read_kinds": ["pending", "ready"],
        "read_data": "hello",
        "active_before_close": 1,
        "active_after_close": 0,
        "provider_close_count": 1,
    },
    "udp_loopback": {
        "send_kind": "ready",
        "send_count": 4,
        "receive_kinds": ["pending", "ready"],
        "received_data": "ping",
        "received_host": "127.0.0.1",
        "received_port": 9001,
        "message_order_preserved": True,
    },
    "dns": {
        "kind": "ready",
        "addresses": ["127.0.0.1:8080", "127.0.0.2:8080"],
    },
    "cancel_pending_resource": {
        "first_kind": "pending",
        "cancel_ok": True,
        "provider_close_count": 1,
        "active_handles": 0,
    },
    "resource_limit": {
        "first_kind": "ready",
        "second_kind": "failed",
        "second_error": "resource_limit",
        "active_handles": 1,
        "closed_resources": 1,
    },
}


def _require_ready(poll, operation: str):
    if poll.kind is not PollKind.READY:
        raise AssertionError(f"{operation} did not complete: {poll!r}")
    return poll.value


@dataclass(slots=True)
class _Stream:
    incoming: bytearray = field(default_factory=bytearray)
    closed: bool = False


class TcpLoopbackProvider:
    """Nonblocking deterministic TCP-like provider with exact resource identity."""

    def __init__(self) -> None:
        self.resource = _Stream()
        self.connect_calls = 0
        self.write_calls = 0
        self.read_calls = 0
        self.closed: list[object] = []

    def connect(self, _address):
        self.connect_calls += 1
        if self.connect_calls == 1:
            return PendingResource(self.resource)
        return self.resource

    def accept(self, _listener):
        return ProviderFailure(
            AsyncNetworkError(
                AsyncNetworkErrorCode.PROVIDER_FAILURE,
                "accept",
                "accept is not part of this bounded client loopback fixture",
            )
        )

    def read(self, stream, amount):
        self.read_calls += 1
        if self.read_calls == 1:
            return PendingOperation()
        if stream is not self.resource or stream.closed:
            return ProviderFailure(
                AsyncNetworkError(AsyncNetworkErrorCode.CLOSED, "read", "stream closed")
            )
        data = bytes(stream.incoming[:amount])
        del stream.incoming[: len(data)]
        return data

    def write(self, stream, data):
        self.write_calls += 1
        if self.write_calls == 1:
            return PendingOperation()
        if stream is not self.resource or stream.closed:
            return ProviderFailure(
                AsyncNetworkError(AsyncNetworkErrorCode.CLOSED, "write", "stream closed")
            )
        stream.incoming.extend(data)
        return len(data)

    def udp_send(self, _socket, _data, _address):
        return ProviderFailure(
            AsyncNetworkError(AsyncNetworkErrorCode.PROVIDER_FAILURE, "udp_send", "wrong fixture")
        )

    def udp_receive(self, _socket):
        return ProviderFailure(
            AsyncNetworkError(AsyncNetworkErrorCode.PROVIDER_FAILURE, "udp_receive", "wrong fixture")
        )

    def resolve(self, _host, _port):
        return ()

    def close(self, resource):
        if hasattr(resource, "closed"):
            resource.closed = True
        self.closed.append(resource)


@dataclass(slots=True)
class _DatagramSocket:
    queue: list[tuple[bytes, NetworkAddress]] = field(default_factory=list)
    closed: bool = False


class UdpLoopbackProvider:
    """Local deterministic UDP provider.

    M1.74 V1 has UDP send/receive operations but no separate public UDP socket
    constructor.  The generic network handle is therefore bootstrapped through
    the provider's connect hook solely for this fixture; UDP behavior itself is
    exercised only through AsyncNetworkService.udp_send/udp_receive.
    """

    def __init__(self) -> None:
        self.resource = _DatagramSocket()
        self.receive_calls = 0
        self.closed: list[object] = []

    def connect(self, _address):
        return self.resource

    def accept(self, _listener):
        return ProviderFailure(
            AsyncNetworkError(AsyncNetworkErrorCode.PROVIDER_FAILURE, "accept", "wrong fixture")
        )

    def read(self, _stream, _amount):
        return ProviderFailure(
            AsyncNetworkError(AsyncNetworkErrorCode.PROVIDER_FAILURE, "read", "wrong fixture")
        )

    def write(self, _stream, _data):
        return ProviderFailure(
            AsyncNetworkError(AsyncNetworkErrorCode.PROVIDER_FAILURE, "write", "wrong fixture")
        )

    def udp_send(self, socket, data, address):
        if socket.closed:
            return ProviderFailure(
                AsyncNetworkError(AsyncNetworkErrorCode.CLOSED, "udp_send", "socket closed")
            )
        socket.queue.append((bytes(data), address))
        return len(data)

    def udp_receive(self, socket):
        self.receive_calls += 1
        if self.receive_calls == 1:
            return PendingOperation()
        if socket.closed:
            return ProviderFailure(
                AsyncNetworkError(AsyncNetworkErrorCode.CLOSED, "udp_receive", "socket closed")
            )
        if not socket.queue:
            return PendingOperation()
        return socket.queue.pop(0)

    def resolve(self, _host, _port):
        return ()

    def close(self, resource):
        resource.closed = True
        self.closed.append(resource)


class DnsFixtureProvider:
    def connect(self, _address):
        return object()

    def accept(self, _listener):
        return object()

    def read(self, _stream, _amount):
        return b""

    def write(self, _stream, data):
        return len(data)

    def udp_send(self, _socket, data, _address):
        return len(data)

    def udp_receive(self, _socket):
        return b""

    def resolve(self, _host, port):
        return (
            NetworkAddress.numeric("127.0.0.1", port),
            NetworkAddress.numeric("127.0.0.2", port),
        )

    def close(self, _resource):
        return None


class PendingOnlyProvider(TcpLoopbackProvider):
    def connect(self, _address):
        self.connect_calls += 1
        return PendingResource(self.resource)


class ImmediateResourceProvider:
    def __init__(self) -> None:
        self.resources: list[object] = []
        self.closed: list[object] = []

    def connect(self, _address):
        resource = object()
        self.resources.append(resource)
        return resource

    def accept(self, _listener):
        return object()

    def read(self, _stream, _amount):
        return b""

    def write(self, _stream, data):
        return len(data)

    def udp_send(self, _socket, data, _address):
        return len(data)

    def udp_receive(self, _socket):
        return b""

    def resolve(self, _host, _port):
        return ()

    def close(self, resource):
        self.closed.append(resource)


def _run_reactor_case() -> dict[str, Any]:
    reactor = DeterministicReactor(max_registrations=4)
    z = reactor.register("z", 2).value_or(None)
    a = reactor.register("a", 1).value_or(None)
    if z is None or a is None:
        raise AssertionError("reactor registration failed")
    if reactor.signal("z").is_err or reactor.signal("a").is_err or reactor.signal("a").is_err:
        raise AssertionError("reactor signal failed")
    first = list(reactor.poll())
    coalesced = first == [1, 2]
    if reactor.signal("z").is_err:
        raise AssertionError("reactor re-signal failed")
    if reactor.close(z).is_err:
        raise AssertionError("reactor close failed")
    after_close = list(reactor.poll())
    return {
        "first_ready": first,
        "coalesced": coalesced,
        "after_close": after_close,
    }


def _run_tcp_case() -> dict[str, Any]:
    provider = TcpLoopbackProvider()
    service = AsyncNetworkService(provider, max_handles=4)
    address = NetworkAddress.numeric("127.0.0.1", 9000)
    future = service.connect(address)
    first = future.poll()
    second = future.poll()
    handle = _require_ready(second, "tcp connect")

    write_future = service.write(handle, b"hello")
    write_first = write_future.poll()
    write_second = write_future.poll()

    read_future = service.read(handle, 5)
    read_first = read_future.poll()
    read_second = read_future.poll()

    active_before = service.active_handles
    handle.close()
    handle.close()
    return {
        "connect_kinds": [first.kind.value, second.kind.value],
        "write_kinds": [write_first.kind.value, write_second.kind.value],
        "write_count": write_second.value,
        "read_kinds": [read_first.kind.value, read_second.kind.value],
        "read_data": bytes(read_second.value or b"").decode("ascii"),
        "active_before_close": active_before,
        "active_after_close": service.active_handles,
        "provider_close_count": len(provider.closed),
    }


def _run_udp_case() -> dict[str, Any]:
    provider = UdpLoopbackProvider()
    service = AsyncNetworkService(provider, max_handles=4)
    bootstrap = NetworkAddress.numeric("127.0.0.1", 9000)
    handle = _require_ready(service.connect(bootstrap).poll(), "udp handle bootstrap")
    destination = NetworkAddress.numeric("127.0.0.1", 9001)

    send = service.udp_send(handle, b"ping", destination).poll()
    receive_future = service.udp_receive(handle)
    receive_first = receive_future.poll()
    receive_second = receive_future.poll()
    data, address = _require_ready(receive_second, "udp receive")
    service.close(handle)
    return {
        "send_kind": send.kind.value,
        "send_count": send.value,
        "receive_kinds": [receive_first.kind.value, receive_second.kind.value],
        "received_data": bytes(data).decode("ascii"),
        "received_host": address.host,
        "received_port": address.port,
        "message_order_preserved": data == b"ping",
    }


def _run_dns_case() -> dict[str, Any]:
    service = AsyncNetworkService(DnsFixtureProvider())
    result = service.resolve("fixture.local", 8080).poll()
    addresses = _require_ready(result, "dns resolve")
    return {
        "kind": result.kind.value,
        "addresses": [f"{address.host}:{address.port}" for address in addresses],
    }


def _run_cancel_pending_resource_case() -> dict[str, Any]:
    provider = PendingOnlyProvider()
    service = AsyncNetworkService(provider)
    future = service.connect(NetworkAddress.numeric("127.0.0.1", 9002))
    first = future.poll()
    cancelled = future.cancel()
    return {
        "first_kind": first.kind.value,
        "cancel_ok": cancelled.is_ok,
        "provider_close_count": len(provider.closed),
        "active_handles": service.active_handles,
    }


def _run_resource_limit_case() -> dict[str, Any]:
    provider = ImmediateResourceProvider()
    service = AsyncNetworkService(provider, max_handles=1)
    first = service.connect(NetworkAddress.numeric("127.0.0.1", 9100)).poll()
    second = service.connect(NetworkAddress.numeric("127.0.0.1", 9101)).poll()
    if second.error is None:
        raise AssertionError("network resource limit did not fail closed")
    return {
        "first_kind": first.kind.value,
        "second_kind": second.kind.value,
        "second_error": second.error.code.value,
        "active_handles": service.active_handles,
        "closed_resources": len(provider.closed),
    }


def collect_results() -> dict[str, Any]:
    return {
        "reactor": _run_reactor_case(),
        "tcp_loopback": _run_tcp_case(),
        "udp_loopback": _run_udp_case(),
        "dns": _run_dns_case(),
        "cancel_pending_resource": _run_cancel_pending_resource_case(),
        "resource_limit": _run_resource_limit_case(),
    }


def verify_behavioral_contract() -> tuple[bool, dict[str, Any]]:
    actual = collect_results()
    canonical = json.dumps(actual, sort_keys=True, separators=(",", ":"))
    report = {
        "schema": "s3.network-loopback.correctness.v1",
        "fixture_scope": "deterministic_local_provider_no_public_internet",
        "performance_results_valid": False,
        "performance_status": "DEFERRED_UNTIL_NATIVE_REACTOR_ADAPTER_IS_BENCHMARKABLE",
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
