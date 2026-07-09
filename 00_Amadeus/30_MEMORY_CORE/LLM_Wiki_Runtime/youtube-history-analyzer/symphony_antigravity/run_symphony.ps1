# 🎼 Symphony Conductor - Ralph Loop Executive
# Rôle : Exécution supervisée lot par lot avec transition de Persona.

$ErrorActionPreference = "Stop"

# Configuration
$SymphonyDir = "C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer"
$BatchDir    = "$SymphonyDir\symphony_antigravity\handoff_batches"
$Manifest    = Get-Content "$BatchDir\manifest.json" -Raw | ConvertFrom-Json

# Définition des Personas
$Personas = @("ALPHA", "BETA", "GAMMA", "DELTA", "EPSILON")

# Indexation globale
$CurrentBatchIndex = 0 # À ajuster selon l'état actuel (008 -> Index 7)

Write-Host "--- Début de la mission supervisée Symphony ---" -ForegroundColor Yellow

foreach ($Batch in $Manifest.batches) {
    if ($Batch.batch_index -lt 7) { continue }
    
    $BatchId = $Batch.batch_id
    $BatchFile = $Batch.file
    
    # Rotation des personas : (Index % 5)
    $Persona = $Personas[$Batch.batch_index % 5]
    
    Write-Host "[+] Processing $BatchId avec Persona $Persona" -ForegroundColor Cyan
    
    try {
        # Execution de la clarification (Gemini CLI)
        $Prompt = "Incarne le persona $Persona. Charge les données de $BatchFile. Rédige les fiches Premium Obsidian (140+ lignes). Injecte les DEAL drafts. Appelle la mise à jour statut via python symphony_antigravity/gemini_handoff_runner.py --process-batch $BatchFile."
        
        $process = Start-Process gemini -ArgumentList "-p", "`"$Prompt`"" -Wait -PassThru
        
        if ($process.ExitCode -eq 0) {
            Write-Host "[SUCCESS] Lot $BatchId terminé par $Persona" -ForegroundColor Green
        } else {
            Write-Host "[ERROR] Échec lot $BatchId. Exit code: $($process.ExitCode)" -ForegroundColor Red
            break 
        }
    } catch {
        Write-Host "[FATAL] Erreur exécution : $($_.Exception.Message)" -ForegroundColor Red
        break
    }
}
Write-Host "--- Mission Symphony Complétée ---" -ForegroundColor Yellow
