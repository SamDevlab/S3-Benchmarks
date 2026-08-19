# Fixtures

Fixtures are local and deterministic. The loopback HTTP server is created by
the correctness harness and binds only to `127.0.0.1`; no public service is
used. Future certificate fixtures must be pinned and hostname-checked before
TLS timing is promoted.

