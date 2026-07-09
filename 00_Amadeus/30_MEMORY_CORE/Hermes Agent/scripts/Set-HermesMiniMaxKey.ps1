$ErrorActionPreference = "Stop"

$distro = "ASpace-L0"
$secure = Read-Host "MiniMax Token Plan API key" -AsSecureString
$bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)

try {
    $plain = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
    if ([string]::IsNullOrWhiteSpace($plain)) {
        throw "MiniMax API key cannot be empty."
    }

    $previousWslEnv = $env:WSLENV
    $previousKey = $env:HERMES_MINIMAX_KEY_INPUT
    $env:HERMES_MINIMAX_KEY_INPUT = $plain
    $env:WSLENV = if ($previousWslEnv) {
        "${previousWslEnv}:HERMES_MINIMAX_KEY_INPUT/u"
    } else {
        "HERMES_MINIMAX_KEY_INPUT/u"
    }

    $bash = @'
set -euo pipefail

file="$HOME/.hermes/.env"
key="${HERMES_MINIMAX_KEY_INPUT:-}"

if [ -z "$key" ]; then
  echo "MiniMax API key was not passed into WSL." >&2
  exit 1
fi

ts=$(date +%Y%m%d_%H%M%S)
cp "$file" "$file.bak.$ts.minimax_key"

upsert_env() {
  local name="$1"
  local value="$2"
  if grep -q "^${name}=" "$file"; then
    python3 - "$file" "$name" "$value" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
name = sys.argv[2]
value = sys.argv[3]
lines = path.read_text().splitlines()
prefix = name + "="
for i, line in enumerate(lines):
    if line.startswith(prefix):
        lines[i] = prefix + value
        break
else:
    lines.append(prefix + value)
path.write_text("\n".join(lines) + "\n")
PY
  else
    printf '%s=%s\n' "$name" "$value" >> "$file"
  fi
}

upsert_env MINIMAX_API_KEY "$key"
upsert_env MINIMAX_BASE_URL "https://api.minimax.io/anthropic"
upsert_env HERMES_PROVIDER "minimax"
upsert_env HERMES_MODEL "MiniMax-M2.7"
upsert_env HERMES_BASE_URL "https://api.minimax.io/anthropic"

chmod 600 "$file"
systemctl --user restart hermes-gateway hermes-dashboard hermes-workspace
sleep 3
systemctl --user is-active hermes-gateway hermes-dashboard hermes-workspace
curl -fsS http://127.0.0.1:8642/health >/dev/null
echo "MiniMax key installed and Hermes services restarted."
'@

    $payload = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($bash))
    & wsl.exe -d $distro -- bash -lc "printf '%s' '$payload' | base64 -d | bash"
    if ($LASTEXITCODE -ne 0) {
        throw "WSL MiniMax key installation failed."
    }
}
finally {
    if ($bstr -ne [IntPtr]::Zero) {
        [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)
    }
    if ($null -eq $previousKey) {
        Remove-Item Env:\HERMES_MINIMAX_KEY_INPUT -ErrorAction SilentlyContinue
    } else {
        $env:HERMES_MINIMAX_KEY_INPUT = $previousKey
    }
    if ($null -eq $previousWslEnv) {
        Remove-Item Env:\WSLENV -ErrorAction SilentlyContinue
    } else {
        $env:WSLENV = $previousWslEnv
    }
}
