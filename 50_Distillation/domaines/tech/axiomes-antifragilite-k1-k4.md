---
type: Concept
title: Trois axiomes antifragiles — RAW, dégradation gracieuse, mémoire procédurale
description: Les trois axiomes du Solarpunk Kernel Core : Read-After-Write systémique, mode dégradé gracieux, mémoire procédurale (Pattern × 3 → Skill).
tags: [tech, antifragilite, axioms, raw, kernel]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: sdd-001-axioms
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-001_solarpunk-kernel-core.md
    title: SDD-001 § 2.1 Les 3 Axiomes du Kernel Antifragile
    last_modified: 2026-04-27
  - id: heart-002
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-HEART-002_heartbeat-anti-panique-openclaw-paperclip.md
    title: ADR-HEART-002 D2 Read-After-Write systémique
    last_modified: 2026-05-26
okf_version: "0.2"
---

L'antifragilité du Solarpunk Kernel n'est pas un slogan — c'est **trois axiomes** vérifiables.

## Axiome 1 — Read-After-Write systémique

**Aucune écriture n'est réussie tant qu'une lecture indépendante ne confirme le contenu.** EXIT 0 sans RAW = hallucination K2.

```bash
# Pattern canonique Write-AndVerify
function Write-AndVerify {
  param($Path, $Content, $RetryMax = 3)
  for ($i = 0; $i -lt $RetryMax; $i++) {
    Set-Content -Path $Path -Value $Content -Encoding UTF8 -Force
    Start-Sleep -Milliseconds 100
    $readback = Get-Content -Path $Path -Raw
    if ($readback -eq $Content) { return $true }
  }
  throw "RAW failed after $RetryMax attempts: $Path"
}
```

Les writes critiques (config, ADR, SOP, token) **doivent** passer par RAW. Les writes non-critiques (logs, telemetry) peuvent skipper RAW pour performance.

## Axiome 2 — Dégradation gracieuse

Chaque service L0.3 fonctionne en **mode dégradé** si son MCP upstream est indisponible. Mode dégradé ≠ arrêt total.

- Yaz (Hostinger MCP down) → fallback sur script bash avec token `HOSTINGER_API_TOKEN` lue depuis env vars + log degraded mode.
- Ryan (Dokploy MCP down) → pause déploiements, alerte Donna DLQ.
- Graham (Supabase MCP down) → bascule RAG sur `WIKI.md` filesystem local + cache pgvector local.

**Corollaire** : un service qui ne démarre pas en mode dégradé n'est pas un service Kernel.

## Axiome 3 — Mémoire procédurale (Procedural Memory Loop)

- Chaque incident non-trivial → entrée append dans `WIKI.md` (Graham).
- Pattern × 3 (incident observé 3 fois) → Skill Hermes Nous auto-encodé.
- Kernel sans WIKI vide = Kernel sans mémoire = Kernel fragile.

```bash
# Trigger auto-encodage Skill
if grep -c "^## \[" "$WIKI" -ge 3; then
  # 3+ entrées → propose Skill à A0 pour validation
  echo "Pattern × 3 détecté — proposer Skill Hermes Nous"
fi
```

## Conséquence : le Kernel devient antifragile

À chaque panique du même type, le Kernel devient **plus fort** : le pattern est documenté, le Skill est encodé, la prochaine occurrence est gérée sans intervention humaine. C'est l'inverse exact de la fragilité (qui se consume) ou de la résilience (qui retourne à T0 sans apprendre).

## Anti-patterns

- K2 Hallucination de Succès : EXIT 0 sans RAW → garantir K2 si observé.
- Mode dégradé = arrêt total : ce n'est pas du Kernel, c'est un daemon fragile.
- WIKI.md non append-only : on édite une entrée au lieu de "CORRECTION du [DATE]".

Voir aussi : [[paniques-k1-k4-kernel]], [[tardis-inverse]], [[loi-l0]].