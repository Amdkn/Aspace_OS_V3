$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$envPath = Join-Path $root ".env"

if (Test-Path -LiteralPath $envPath) {
    Write-Output ".env already exists. No changes made."
    exit 0
}

$bytes = New-Object byte[] 24
[System.Security.Cryptography.RandomNumberGenerator]::Fill($bytes)
$password = [Convert]::ToBase64String($bytes).TrimEnd("=") -replace "[+/]", "x"

$content = @(
    "WIKI_PORT=3080"
    "POSTGRES_DB=wiki"
    "POSTGRES_USER=wikijs"
    "POSTGRES_PASSWORD=$password"
) -join [Environment]::NewLine

[System.IO.File]::WriteAllText($envPath, $content, [System.Text.UTF8Encoding]::new($false))
Write-Output ".env created with a generated local database password."
Write-Output "Do not commit or paste .env contents."
