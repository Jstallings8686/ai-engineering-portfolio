#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
export PYTHONIOENCODING=utf-8
exec python "$ROOT/monitor.py" --report "$@"
