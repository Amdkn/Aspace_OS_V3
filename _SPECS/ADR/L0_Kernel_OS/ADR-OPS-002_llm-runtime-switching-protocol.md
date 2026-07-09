---
id: ADR-OPS-002
title: LLM Runtime Switching Protocol — Fable-MiniMax-M3 ↔ Mistral Self-Hosted
type: ADR (Architectural Decision Record)
status: PROPOSED (A0 sign-off 2026-06-15 via "go for all")
date: 2026-06-15
author: A0 (Amadeus) via A2 (Claude Code) sub-agent
domain: L0 Tech_OS / Runtime / Operations / Failover
tags: [#ADR #ops #failover #llm-switching #warm-standby #incident-response]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-LLM-001, ADR-REG-001]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, "ADR-SUPABASE-001", "ADR-HERMES-001"]
provenance: |
  Née 2026-06-15 du handoff Mission ρ vid2 (Fable 5 fin) + Mission σ distillation : A2 a identifié le
  besoin d'un protocole de bascule runtime entre Fable-MiniMax-M3 (principal) et Mistral 7B self-hosté
  (fallback UE) avec health-check, automatic failover conditionnel (pas d'auto-switch non-autorisé), et
  observabilité logs.
sign_off_a0: "A0 Amadeus — Go ADR-OPS-002 — 2026-06-15 (via 'go for all' session-level directive)"
sign_off_pending: false
ratification_log_2026-06-15: "A0 batch GO. D4 append-only. D7 = pas d'escalation additionnelle."
---

# ADR-OPS-002 — LLM Runtime Switching Protocol

## Status
**PROPOSED → ACCEPTED via "go for all" A0 2026-06-15.**

## Context

1. **ADR-LLM-001** ancre Fable-MiniMax-M3 comme runtime principal.
2. **ADR-REG-001** ancre Mistral 7B self-hosté comme fallback UE.
3. **Manque** = le **protocole opérationnel** de bascule : qui déclenche, comment, sous quelles conditions,
   avec quel logging, et quel retour arrière.

## Decision

**D1 — Health check passif toutes les 60s** : un cron PowerShell `~/.claude/bin/llm-healthcheck.ps1` test
l'endpoint principal `https://api.minimax.io/anthropic/v1/messages` (POST minimal avec 401 attendu) et
logue `timestamp, status, latency_ms` dans `wiki/hand_offs/llm_health.log`. **Aucun switch automatique** sur
health check fail — alerte log seulement.

**D2 — Switch = action manuelle A0 uniquement** (D7 — pas d'auto-failover non-autorisé) :
- Commande : `claude-runtime switch mistral` (alias PowerShell) → modifie env `ANTHROPIC_BASE_URL` →
  relance Claude Code CLI avec `OLLAMA_HOST=http://127.0.0.1:11434`.
- Retour : `claude-runtime switch fable` → restore env par défaut.
- Documentation : `~/.claude/bin/claude-runtime.ps1` (script unique, idempotent, dry-run support).

**D3 — Conditions de switch recommandées (D7 — A0 décide)** :
- Fable-MiniMax-M3 down > 5 min confirmé (3 health checks consécutifs fail).
- A0 instruction explicite (verbale ou chat) "switch mistral pour test" ou "switch mistral pour production".
- Incident RGPD : A0 ordonne blackout US immédiat.

**D4 — Logs structurés** : chaque switch log une ligne JSON dans `wiki/hand_offs/llm_switches.log` :
```json
{"ts":"2026-MM-DDTHH:MM:SSZ","actor":"A0","from":"fable-mini-max-m3","to":"mistral-7b","reason":"[A0 input]","duration_s":0}
```
D4 append-only (jamais de modif destructive, rotation après 365 jours).

**D5 — Test obligatoire 1×/trimestre** (intégré au cycle 12WY bilan) : A0 ordonne un switch test
Fable → Mistral, mesure 10 requêtes, restore. But = valider que le protocole marche AVANT qu'un vrai
incident force la bascule.

## Consequences

- ✅ Runtime A'Space V2 a un failover documenté (vs improvisation en cas de panne).
- ✅ Logs permettent audit事后 ("combien de switchs en 2026 ?", "combien de temps Mistral a-t-il été actif ?").
- ✅ Pas d'auto-failover = pas de risque de cascade accidentelle (D7 — A0 reste in-the-loop).
- ⚠️ Coût opérationnel marginal : 1 cron health check + 1 script switch + logs rotation.

## Implementation Plan (D9.7)

1. **Phase 1 (S+1)** : écrire `~/.claude/bin/llm-healthcheck.ps1` + `claude-runtime.ps1` (≤80 lignes
   chacun, idempotent).
2. **Phase 2 (S+2)** : déployer health check en cron toutes les 60s (Task Scheduler Windows).
3. **Phase 3 (S+3)** : premier switch test Fable → Mistral (10 requêtes, mesure qualité + latence).
4. **Phase 4 (S+5)** : intégrer le test 1×/trimestre au checklist bilan 12WY.

## References

- `ADR-LLM-001_fable-5-discontinuation-decision.md` (runtime principal).
- `ADR-REG-001_eu-mistral-self-hosting-fallback.md` (fallback UE).
- `~/.claude/CLAUDE.md` section "Runtime LLM (backend)" — env vars canon.
- `ADR-SUPABASE-001_self-hosted-multi-tenancy-schemas.md` (précedent ops protocol).
- `ADR-HERMES-001_nous-desktop-native-workspace-remote.md` (topologie Dokploy VPS).
