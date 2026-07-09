# 🎼 Trigger Symphony Conductor Track — Swarm Parallele avec Rick's Harness (Ralph Loop)
# Réf : SDD-002 A1 Rick Harness / Standard A'Space OS V2
# Localisation : symphony_antigravity/trigger_symphony_conductor.ps1

$ErrorActionPreference = "Stop"

# Configuration
$SymphonyDir = "C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer"
$BatchDir    = "$SymphonyDir\symphony_antigravity\handoff_batches"
$GeordiDir   = "C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides"

if (-not (Test-Path "$BatchDir\manifest.json")) {
    Write-Host "[!] Manifest not found. Generating batches first..." -ForegroundColor Yellow
    python "$SymphonyDir\symphony_antigravity\gemini_handoff_runner.py"
}

$Manifest = Get-Content "$BatchDir\manifest.json" -Raw | ConvertFrom-Json

# Définition des Personas
$Personas = @("ALPHA", "BETA", "GAMMA", "DELTA", "EPSILON")
$MaxRetries = 3

Write-Host "--- 🛡️ Démarrage du Conductor sous Rick's Harness ---" -ForegroundColor Yellow
Write-Host "Cible : Analyse Haute-Fidélité avec Gemini 3.1 Flash-Lite" -ForegroundColor Cyan

foreach ($Batch in $Manifest.batches) {
    $BatchId = $Batch.batch_id
    $BatchFile = $Batch.file
    $Persona = $Personas[$Batch.batch_index % 5]
    
    Write-Host "`n==================================================" -ForegroundColor Yellow
    Write-Host "[+] Lot: $BatchId | Agent: $Persona" -ForegroundColor Yellow
    Write-Host "==================================================" -ForegroundColor Yellow
    
    $Success = $false
    $RetryCount = 0
    $CorrectionWarning = ""
    
    # Résolution des fichiers attendus pour nettoyage en cas d'échec
    $BatchData = Get-Content $BatchFile -Raw | ConvertFrom-Json
    $ExpectedFiles = @()
    foreach ($vid in $BatchData) {
        $slug = $vid.title.ToLower()
        # Regex replacement equivalent in PS
        $slug = [regex]::Replace($slug, '[^a-z0-9\s]', '')
        $slug = [regex]::Replace($slug, '\s+', '_')
        if ($slug.Length -gt 80) { $slug = $slug.Substring(0, 80) }
        $ExpectedFiles += "resource_$slug.md"
    }

    while (-not $Success -and $RetryCount -lt $MaxRetries) {
        $RetryCount++
        if ($RetryCount -gt 1) {
            Write-Host "⚠️ Tentative d'auto-correction Ralph Loop ($RetryCount/$MaxRetries) pour $BatchId..." -ForegroundColor DarkYellow
        }
        
        $Prompt = "Incarne le persona $Persona. Charge les données de $BatchFile. Pour chaque vidéo du lot : rédiges la fiche premium Obsidian (140+ lignes sans placeholders ni stubs du genre '[Contenu technique]'), injectes proprement le draft sémantique D.E.A.L dans C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\affine_deal_drafts.md sans créer de doublon, puis appelles la mise à jour de statut dans watch_history_rag.csv via python symphony_antigravity/gemini_handoff_runner.py --process-batch $BatchFile. $CorrectionWarning"
        
        Write-Host "[*] Lancement de Gemini CLI..." -ForegroundColor Gray
        $process = Start-Process gemini -ArgumentList "-p", "`"$Prompt`"" -Wait -PassThru
        
        Write-Host "[*] Évaluation du livrable par Rick's Harness..." -ForegroundColor Gray
        $evalProcess = Start-Process python -ArgumentList "symphony_antigravity/harness_evaluator.py", "`"$BatchFile`"" -Wait -NoNewWindow -PassThru
        
        if ($evalProcess.ExitCode -eq 0) {
            Write-Host "✅ [SUCCESS] Lot $BatchId validé par le Harness à la tentative $RetryCount !" -ForegroundColor Green
            $Success = $true
        } else {
            Write-Host "❌ [REJECT] Le lot $BatchId a échoué aux critères de densité ou contient des placeholders." -ForegroundColor Red
            
            # Nettoyage des fichiers invalides pour éviter la pollution sémantique
            Write-Host "[*] Nettoyage des fichiers rejetés..." -ForegroundColor Gray
            foreach ($file in $ExpectedFiles) {
                $filePath = Join-Path $GeordiDir $file
                if (Test-Path $filePath) {
                    Remove-Item $filePath -Force
                    Write-Host "  - Supprimé: $file" -ForegroundColor DarkGray
                }
            }
            
            # Message de réprimande pour la boucle Ralph d'auto-correction
            $CorrectionWarning = "🚨 CRITICAL WARNING: Ta précédente génération pour ce lot a été REJETÉE par le validateur de densité car elle contenait des stubs de texte court ou des placeholders comme '[Contenu technique...]'. Tu es strictement interdit de résumer, de tronquer ou de mettre des '[...]'. Tu dois rédiger TOUT le texte développé avec de vraies analyses denses, détaillées et verbeuses (>140 lignes par guide) !"
        }
    }
    
    if (-not $Success) {
        Write-Host "🚨 [FATAL] Échec définitif du lot $BatchId après $MaxRetries tentatives." -ForegroundColor Red
        Write-Host "Arrêt du Conductor pour inspection de la DLQ." -ForegroundColor Red
        break
    }
}

Write-Host "`n--- Mission Symphony Complétée ---" -ForegroundColor Yellow
