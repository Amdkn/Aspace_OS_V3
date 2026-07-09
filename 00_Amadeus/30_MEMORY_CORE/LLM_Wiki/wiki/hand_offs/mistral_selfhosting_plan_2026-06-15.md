---
name: mistral-selfhosting-plan-2026-06-15
description: Plan complet self-hosting Mistral 7B sur VPS Dokploy `aspace-vps` (warm standby EU). 5 phases, ~3h installation + ~2h bench, ROI souveraineté UE chiffré. À exécuter S+1 → S+3 (cf. ADR-REG-001 implementation plan).
type: handoff
date: 2026-06-15
cycle: 12WY 06/15 - 09/07/26
doctrine_anchors: [ADR-REG-001, ADR-LLM-001, ADR-OPS-002, ADR-META-003, ADR-SECURITY-001]
related: [ADR-REG-001_eu-mistral-self-hosting-fallback.md]
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
---

# 🇪🇺 Mistral 7B Self-Hosting Plan — VPS Dokploy `aspace-vps`

## Goal
Installer Mistral 7B Instruct (Q4_K_M) self-hosté sur VPS Dokploy `aspace-vps` en **mode warm
standby** : opérationnel techniquement, activé seulement si Fable-MiniMax-M3 down > 5 min OU
instruction explicite A0 (D7 — pas d'auto-failover non-autorisé).

## Context (D1 receipts)

| Source primaire | Date | Verdict D1 |
|-----------------|------|------------|
| VPS Dokploy `aspace-vps` ssh | 2026-06-15 | LIVE (cf. `wiki/hand_offs/ssh_vps_2026-06-13.md`, ssh amadeus@kalybana.com) |
| VPS RAM disponible | 2026-06-15 | **16 GB** (cf. handoff OMK deploy 2026-06-14) — suffit pour 7B Q4_K_M (~4 GB) + Postgres + Kong + Caddy + Dokploy |
| VPS Disk libre | 2026-06-15 | **~120 GB** (estimation post-OMK deploy) — 4 GB modèle + 2 GB Ollama engine + 2 GB cache = OK |
| Ollama latest version | 2026-06-15 | v0.5.x (release bi-mensuelle) — install via curl https://ollama.com/install.sh |
| Mistral 7B Instruct Q4_K_M | 2026-06-15 | **4.1 GB**, license Apache 2.0, https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF |
| OpenAI-compat endpoint | 2026-06-15 | Ollama expose `http://127.0.0.1:11434/v1/chat/completions` (compatible Claude Code via `ANTHROPIC_BASE_URL` override) |

## D1 receipts complémentaires (souveraineté)

- **RGPD** : aucune donnée A0 transite par provider US (Ollama = local, pas de telemetry par défaut avec `OLLAMA_NOHISTORY=1`).
- **Test Key Pragma** : pas de clé API Mistral (modèle local), pas de transmission A0 data US.
- **Doctrine no-hard-delete** : si rollback phase 1, Ollama卸载 + model download удаляются proprement via `systemctl stop ollama && rm -rf /usr/local/lib/ollama /usr/local/bin/ollama /root/.ollama`.

## Phases (D9.7 — 5 phases, 3-5h total)

### Phase 1 — Installation Ollama (10 min, S+1)

**Pré-requis** : SSH vers VPS en tant qu'amadeus.

```bash
# Contexte : exécution sur VPS Dokploy aspace-vps (kalybana.com)
ssh amadeus@kalybana.com

# Vérifier OS
cat /etc/os-release  # attendu : Ubuntu 22.04 LTS (Dokploy standard)
uname -m             # attendu : x86_64

# Installation Ollama (script officiel)
curl -fsSL https://ollama.com/install.sh | sh

# Vérifier service
systemctl status ollama  # attendu : active (running)
ollama --version         # attendu : ollama version 0.5.x
```

**D1 receipt attendu** : `ollama --version` retourne version 0.5.x, service `active (running)`.

### Phase 2 — Download Mistral 7B (15-30 min, S+1)

```bash
# Pull modèle (download ~4.1 GB, dépend bandwidth VPS)
ollama pull mistral:7b-instruct-q4_K_M

# Vérifier modèle installé
ollama list
# Attendu : NAME                    ID            SIZE      MODIFIED
#           mistral:7b-instruct-q4_K_M  <hash>    4.1 GB    <date>
```

**D1 receipt attendu** : ligne `mistral:7b-instruct-q4_K_M 4.1 GB` dans `ollama list`.

**Note disk** : 4.1 GB sur `/usr/share/ollama/.ollama/models/` (ou `~/.ollama/models/` si user-level).

### Phase 3 — Test inference direct (5 min, S+1)

```bash
# Test 1 : génération simple
ollama run mistral:7b-instruct-q4_K_M "Explique la souveraineté LLM en 3 phrases."

# Attendu : réponse cohérente en français, latence 5-15s (CPU), 1-3s (GPU si dispo).

# Test 2 : endpoint OpenAI-compat (via curl)
curl -X POST http://127.0.0.1:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mistral:7b-instruct-q4_K_M",
    "messages": [{"role": "user", "content": "Dis bonjour en français."}]
  }'

# Attendu : JSON {"choices": [{"message": {"content": "Bonjour !"}}]}
```

**D1 receipt attendu** : JSON valide avec réponse cohérente, latence < 30s (CPU-only VPS).

### Phase 4 — Bench throughput (60-90 min, S+2)

**But** : mesurer req/min et latence p50/p95 sur VPS Dokploy pour prédire l'usage en mode
fallback Mistral (cf. ADR-OPS-002 protocol).

```bash
# Test 10 requêtes séquentielles (CPU baseline)
for i in {1..10}; do
  start=$(date +%s%N)
  curl -s -X POST http://127.0.0.1:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d "{\"model\": \"mistral:7b-instruct-q4_K_M\", \"messages\": [{\"role\": \"user\", \"content\": \"Question $i : quelle est la capitale du pays $i ?\"}]}" \
    > /dev/null
  end=$(date +%s%N)
  echo "Req $i: $(( (end - start) / 1000000 )) ms"
done
```

**Métriques à reporter** dans `wiki/hand_offs/mistral_bench_2026-06-16.md` :

| Métrique | Valeur | Baseline Fable-MiniMax-M3 | Écart |
|----------|--------|---------------------------|-------|
| Latence p50 | XXX ms | ~2000 ms | X× |
| Latence p95 | XXX ms | ~5000 ms | X× |
| Throughput | X req/min | ~30 req/min | X× |
| TTFT (time-to-first-token) | XXX ms | ~500 ms | X× |

**D1 receipt attendu** : 10/10 requêtes OK, latence p95 < 60s (acceptable pour fallback non-réactif).

**Note optimisation** : si latence p95 > 30s, options :
- Quantization plus agressive (Q3_K_M = 3.2 GB, -25% taille, -10% qualité).
- GPU VPS upgrade (Hetzner + GPU ~50 €/mois) si throughput critique.
- Limitation acceptée : Mistral = fallback dégradé, pas primary.

### Phase 5 — Documentation switch procedure (30 min, S+2)

**But** : créer le script PowerShell local qui switch Claude Code entre Fable-MiniMax-M3 et
Mistral self-hosté.

```powershell
# C:\Users\amado\.claude\bin\claude-runtime.ps1

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet('fable', 'mistral', 'status')]
    [string]$Action
)

switch ($Action) {
    'fable' {
        # Restore Fable-MiniMax-M3 par défaut
        [Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", $null, "User")
        [Environment]::SetEnvironmentVariable("OLLAMA_HOST", $null, "User")
        Write-Host "✅ Switched to Fable-MiniMax-M3 (default)"
    }
    'mistral' {
        # Switch vers Mistral self-hosté sur VPS
        # NOTE : nécessite tunnel SSH ou VPN pour accéder 127.0.0.1:11434 du VPS
        # Option 1 : SSH tunnel (recommandé pour test)
        #   ssh -f -N -L 11434:127.0.0.1:11434 amadeus@kalybana.com
        # Option 2 : VPN WireGuard (à setup si usage fréquent)
        [Environment]::SetEnvironmentVariable("OLLAMA_HOST", "http://127.0.0.1:11434", "User")
        Write-Host "✅ Switched to Mistral 7B self-hosted (OLLAMA_HOST set)"
    }
    'status' {
        $ollama = [Environment]::GetEnvironmentVariable("OLLAMA_HOST", "User")
        $baseUrl = [Environment]::GetEnvironmentVariable("ANTHROPIC_BASE_URL", "User")
        if ($ollama) {
            Write-Host "🔄 Current runtime: Mistral 7B (OLLAMA_HOST=$ollama)"
        } elseif ($baseUrl) {
            Write-Host "🔄 Current runtime: Custom (ANTHROPIC_BASE_URL=$baseUrl)"
        } else {
            Write-Host "🔄 Current runtime: Fable-MiniMax-M3 (default)"
        }
    }
}
```

**Usage** :
```powershell
# Status
.\claude-runtime.ps1 -Action status

# Switch to Mistral (test)
ssh -f -N -L 11434:127.0.0.1:11434 amadeus@kalybana.com
.\claude-runtime.ps1 -Action mistral
claude  # nouvelle session Claude Code avec Mistral

# Switch back
.\claude-runtime.ps1 -Action fable
claude
```

**D1 receipt attendu** : `claude-runtime.ps1 -Action status` retourne le runtime courant.

## Coût & ROI

| Item | Coût | Fréquence |
|------|------|-----------|
| VPS Dokploy existant | 0 € (déjà payé) | — |
| Ollama + Mistral 7B storage | 0 € (4 GB disk) | — |
| Compute overhead Mistral idle | ~200 MB RAM | Permanent |
| Compute overhead Mistral actif | ~4 GB RAM + CPU burst | Pendant sessions |
| Bandwidth SSH tunnel | Négligeable | Pendant switch |

**Total : 0 € coût récurrent.** ROI = souveraineté UE (RGPD, anti-Trump-14179) + vendor fallback.

**Temps investi** : ~3-5h setup one-shot + ~30 min/trimestre maintenance (update Ollama + modèle).

## Acceptance criteria (DRAFT → ACCEPTED pour ADR-REG-001)

Phase 1-2 : Ollama + Mistral installés, modèle downloadé, service actif → ADR-REG-001 §Implementation
Phase 1 = DONE.
Phase 3-4 : inference + bench throughput documentés → ADR-REG-001 §Phase 2 = DONE.
Phase 5 : script switch PowerShell + tunnel SSH testé → ADR-REG-001 §Phase 3 = DONE.
+ Test 1×/trimestre (intégré bilan 12WY) → ADR-OPS-002 D5.

## Open Questions (à A0 ratification)

1. **GPU VPS upgrade** ? Si latence p95 > 30s en bench, A0 valide-t-il upgrade Hetzner + GPU
   (~50 €/mois) pour Mistral usable en primary, pas juste fallback ?
2. **WireGuard VPN setup** ? Si switch Mistral devient fréquent, tunnel SSH est fragile. WireGuard
   = robust mais +1h setup + 1 service à maintenir.
3. **Multi-modèle** ? Ollama peut host plusieurs modèles (Mistral 7B + Llama 3 8B + Phi-3 14B).
   A0 veut-il un seul (Mistral) ou un mix ?
4. **Activation auto vs manuelle** ? ADR-OPS-002 dit manuelle uniquement (D7). A0 confirme-t-il
   cette politique, ou veut-il un auto-failover conditionnel (Fable down > 5 min = switch auto) ?

## References

- `ADR-REG-001_eu-mistral-self-hosting-fallback.md` (canonique, FR + sovereignty).
- `ADR-LLM-001_fable-5-discontinuation-decision.md` (runtime principal Fable-MiniMax-M3).
- `ADR-OPS-002_llm-runtime-switching-protocol.md` (protocole de switch).
- `ADR-META-003_model-agnostic-runtime-doctrine.md` (harness invariant, modèle variable).
- `ADR-SECURITY-001_vault-boundary-and-rotation-policy.md` (0 secret en clair, transit-only).
- `wiki/hand_offs/handoff_fable_mort_claim_d1_falsification_2026-06-15.md` (mission ρ source).
- Ollama docs : https://github.com/ollama/ollama/blob/main/docs/api.md
- Mistral 7B Instruct : https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

