#!/usr/bin/env bash
set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <run_id_or_path>"
    exit 1
fi

RUN_DIR="$1"

if [ ! -d "$RUN_DIR" ]; then
    echo "ERROR: Directory $RUN_DIR does not exist."
    exit 1
fi

echo "Verifying artifacts in $RUN_DIR..."

MANIFEST="$RUN_DIR/manifest.json"
VERDICT="$RUN_DIR/report/verdict.json"

MISSING=0

if [ ! -f "$MANIFEST" ]; then
    echo "FAIL: Missing manifest.json"
    MISSING=1
else
    echo "OK: manifest.json found."
fi

if [ ! -f "$VERDICT" ]; then
    echo "FAIL: Missing report/verdict.json"
    MISSING=1
else
    echo "OK: report/verdict.json found."
fi

if [ "$MISSING" -eq 1 ]; then
    echo "Verification FAILED."
    exit 1
fi

echo "Verification SUCCESS."
exit 0
