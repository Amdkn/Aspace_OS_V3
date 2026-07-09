param (
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$ClaudeArgs
)

# Configuration LiteLLM pour Claude Code
$ConfigPath = Join-Path $PSScriptRoot "config.yaml"

Write-Host "⚡ Initialisation du pont LiteLLM vers OpenRouter (GLM 4.7 Flash)..." -ForegroundColor Cyan

# Vérification de la clé API
if (-not $env:OPENROUTER_API_KEY) {
    Write-Host "ATTENTION : OPENROUTER_API_KEY n'est pas défini dans l'environnement." -ForegroundColor Yellow
    Write-Host "Veuillez définir la variable d'environnement OPENROUTER_API_KEY avant de lancer ce script." -ForegroundColor Yellow
    Write-Host "Exemple: `$env:OPENROUTER_API_KEY='sk-or-v1-...'`" -ForegroundColor Gray
    exit 1
}

# Lancer LiteLLM en arrière-plan
$job = Start-Job {
    param($config)
    litellm --config $config --port 4000
} -ArgumentList $ConfigPath

Write-Host "⏳ Attente du démarrage de LiteLLM sur le port 4000..." -ForegroundColor Gray
Start-Sleep -Seconds 3

# Configurer les variables d'environnement pour Claude Code
$env:ANTHROPIC_BASE_URL = "http://localhost:4000"
$env:ANTHROPIC_API_KEY = "sk-dummy-key" # LiteLLM intercepte et utilise la clé OpenRouter

Write-Host "🚀 Lancement de Claude Code (Modèle par défaut intercepté et redirigé vers GLM 4.7 Flash)..." -ForegroundColor Green

# Lancer Claude avec les arguments passés
claude $ClaudeArgs

Write-Host "🛑 Arrêt du pont LiteLLM..." -ForegroundColor Cyan
Stop-Job -Job $job
Remove-Job -Job $job
