#!/usr/bin/env bash
# Shim → the canonical installer lives at repo root (deliverable #8).
# Keeps both `bash install.sh` and `bash scripts/install.sh` working, no drift.
exec bash "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/install.sh" "$@"
