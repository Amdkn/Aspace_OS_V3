$OpenClawPath = "C:\Aspace00\openclaw"
Set-Location $OpenClawPath

Write-Host "--- OPENCLAW LOCAL DOMAIN INITIALIZATION ---" -ForegroundColor Cyan

# 1. Environment Configuration
if (-not (Test-Path ".env")) {
    Write-Host "Creating .env from template..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
    Write-Host ".env created. Please update it with your strategic keys." -ForegroundColor Green
} else {
    Write-Host ".env already exists." -ForegroundColor Gray
}

# 2. Dependency Management (pnpm detected via lock file)
if (Get-Command "pnpm" -ErrorAction SilentlyContinue) {
    Write-Host "pnpm detected. Installing dependencies..." -ForegroundColor Yellow
    pnpm install
} elseif (Get-Command "npm" -ErrorAction SilentlyContinue) {
    Write-Host "pnpm not found. Falling back to npm..." -ForegroundColor Yellow
    npm install
} else {
    Write-Host "Error: No package manager (npm/pnpm) found." -ForegroundColor Red
    exit 1
}

Write-Host "--- ENVIRONMENT READY ---" -ForegroundColor Cyan
Write-Host "To start OpenClaw: npm run dev" -ForegroundColor Green
