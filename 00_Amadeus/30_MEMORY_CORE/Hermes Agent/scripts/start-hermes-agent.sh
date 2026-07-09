#!/usr/bin/env bash
set -euo pipefail

export HERMES_HOME=/home/amadeus/.hermes
export XDG_RUNTIME_DIR="/run/user/$(id -u)"

for _ in $(seq 1 30); do
  if systemctl --user status >/dev/null 2>&1; then
    break
  fi
  sleep 1
done

systemctl --user daemon-reload || true
systemctl --user start hermes-gateway hermes-dashboard hermes-workspace

echo "--- active state ---"
systemctl --user is-active hermes-gateway hermes-dashboard hermes-workspace

echo "--- listeners ---"
ss -tlnp | grep -E ':8642|:9119|:3000' || true

echo "--- health ---"
curl -fsS http://127.0.0.1:8642/health
curl -fsS -o /dev/null -w "dashboard:%{http_code}\n" http://127.0.0.1:9119
