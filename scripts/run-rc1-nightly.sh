#!/usr/bin/env sh
set -eu
exec python -m benchmarks.rc1.automation --mode nightly "$@"
