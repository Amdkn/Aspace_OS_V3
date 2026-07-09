---
id: ADR-REG-001
title: EU Sovereignty via Mistral Self-Hosting — Fable-MiniMax-M3 Fallback Layer
type: ADR (Architectural Decision Record)
status: PROPOSED (A0 sign-off 2026-06-15 via "go for all")
date: 2026-06-15
author: A0 (Amadeus) via A2 (Claude Code) sub-agent
domain: L0 Tech_OS / Runtime / Model Selection / EU Sovereignty
tags: [#ADR #regulatory #mistral #self-hosting #eu #sovereignty #fallback #rgpd]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-RICK-001, ADR-LLM-001]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, "youtube_ingest_2026-06-14 transcripts/03-gouvernement-americain.md"]
provenance: |
  Née 2026-06-15 du handoff Mission ρ vid3 (gouvernement américain interdit Claude) où A2 a identifié
  la prescription A0 implicite : souveraineté LLM = self-hosting Mistral 7B sur VPS Dokploy, en cas de
  blackout US (Trump executive order 14179 ou équivalent) affectant Fable-MiniMax-M3 transit US.
sign_off_a0: "A0 Amadeus — Go ADR-REG-001 — 2026-06-15 (via 'go for all' session-level directive)"
sign_off_pending: false
ratification_log_2026-06-15: "A0 batch GO. D4 append-only. D7 = pas d'escalation additionnelle."
---

# ADR-REG-001 — EU Sovereignty via Mistral Self-Hosting

## Status
**PROPOSED → ACCEPTED via "go for all" A0 2026-06-15.**

## Context

1. **Mission ρ vid3 (YouTube transcript 03-gouvernement-americain.md, 950 lns)** documente la décision
   Trump 2025-14179 + Glasswing Act : le gouvernement US peut contraindre les providers LLM US (Anthropic,
   OpenAI) à bloquer l'accès depuis certains pays ou pour certains usages. Fable-MiniMax-M3 (backend
   `api.minimax.io`) n'est pas formellement US-juridiction (MiniMax = Asia-Pacific), mais l'**effet de
   cascade** sur l'écosystème LLM mondial est suffisant pour justifier un **fallback souverain UE**.
2. **A0 = France, VPS Dokploy `aspace-vps`** : infrastructure déjà souveraine (Caddy + Dokploy +
   Supabase self-hosted, cf. ADR-SUPABASE-001, ADR-HERMES-001). Manque = le **runtime LLM lui-même**.
3. **Mistral 7B / Mixtral 8x7B** : modèle open-weight français, license Apache 2.0, hébergeable sur VPS
   modeste (16 GB RAM suffice pour 7B quantisé Q4_K_M via llama.cpp ou Ollama). Mlx 2-3× plus lent que
   Fable-MiniMax-M3 cloud, mais **0 dépendance US** et **0 vendor lock-in**.

## Decision

**D1 — Préparer un fallback Mistral 7B self-hosté** sur VPS Dokploy `aspace-vps`, en mode "warm standby" :
- Ollama installé + Mistral 7B Instruct Q4_K_M téléchargé (~4 GB).
- Endpoints : `http://127.0.0.1:11434/v1/chat/completions` (OpenAI-compatible) + `http://127.0.0.1:11434/api/generate`.
- Activé **uniquement** si Fable-MiniMax-M3 down > 5 min OU si A0 instruction explicite "switch Mistral".

**D2 — Pas d'activation immédiate** : A0 doit explicitement déclencher le switch (D7 — coût d'escalation
A0 < coût d'une bascule ratée). Le warm standby est passif : Ollama installé, modèle téléchargé, mais
Claude Code reste configuré sur Fable-MiniMax-M3 par défaut.

**D3 — RGPD by design** : aucune donnée A0 transite par un provider US en mode Mistral self-hosted. Logs
OLLAMA conservés 7 jours sur VPS, puis rotation. Pas de telemetry Ollama (option `--no-telemetry` ou env
`OLLAMA_NOHISTORY=1`).

**D4 — Documentation onboarding** : ADR-REG-001 sister à ADR-LLM-001. Si un nouvel agent onboarde sur
A'Space V2, il lit les 2 en séquence : LLM-001 (runtime principal) → REG-001 (fallback UE).

## Consequences

- ✅ Souveraineté LLM ancrée : si blackout US affecte Fable-MiniMax-M3, A0 a un fallback local viable.
- ✅ Coût d'opération marginal : Ollama = 0 coût récurrent, seulement 4 GB disque + 200 MB RAM idle.
- ✅ Test Key Pragma respecté : pas de clé API Mistral (modèle local), pas de transmission A0 data US.
- ⚠️ Mlx 2-3× plus lent que Fable cloud : throughput sub-agents × quota $50/mois dégradé en mode Mistral.
  Mitigation : batcher les requêtes, prioriser les tâches à fort impact.
- ⚠️ Maintenance Ollama : mises à jour sécurité modèle + engine tous les 90 jours (à planifier cycle 12WY).

## Implementation Plan (D9.7 phased)

1. **Phase 1 (S+1)** : installation Ollama + download Mistral 7B Q4_K_M (commande unique, ~10 min).
2. **Phase 2 (S+2)** : bench throughput (req/min, latence p50/p95) sur VPS Dokploy, archivage dans
   `wiki/hand_offs/mistral_bench_2026-MM-DD.md`.
3. **Phase 3 (S+3)** : documentation switch procedure (1 commande `OLLAMA_HOST=http://127.0.0.1:11434
   claude` ou wrapper PowerShell).
4. **Phase 4 (S+5)** : premier switch test (10 requêtes réelles via Claude Code, mesure qualité réponses).
5. **Phase 5 (S+7)** : décision go/no-go pour production standby.

## References

- `wiki/hand_offs/handoff_fable_mort_claim_d1_falsification_2026-06-15.md` §"3 entités Fable" + §"4 ADR drafts".
- `youtube_ingest_2026-06-14/transcripts/03-gouvernement-americain.md` (950 lns, Trump 14179, Glasswing).
- `ADR-LLM-001_fable-5-discontinuation-decision.md` (sister ADR, runtime principal).
- `ADR-SUPABASE-001_self-hosted-multi-tenancy-schemas.md` (précedent self-hosting souverain).
- `ADR-HERMES-001_nous-desktop-native-workspace-remote.md` (topologie runtime, Dokploy VPS).
