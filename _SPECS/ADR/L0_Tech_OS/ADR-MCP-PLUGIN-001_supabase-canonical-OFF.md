---
id: ADR-MCP-PLUGIN-001
title: Plugin `supabase@claude-plugins-official` reste canoniquement OFF
date: 2026-06-28
author: A0 jumeau numérique (Opus)
status: PROPOSED
ratified: null (A0 ratify in-session, after F2 close)
layer: L0 — Tech OS / MCP Wiring
preserves:
  - ADR-META-006 D6 Root Causes Catalog (#1 entrée airtable/clickup post-CC-restart 2026-06-23 — sister anti-pattern)
  - ADR-L0-META-ORCH-001 (Hermes méta-orchestrateur, Local-First, Posture C)
  - ADR-SOBER-002 Anti-paperclip (no auto-toggle kernel P0)
sister:
  - wiki/hand_offs/l0_mcp_pivots_premortem_live.md (live D1 state map, F2 entry)
  - wiki/hand_offs/l0_mcp_pivots_premortem_pending_actions.md (F2 = A0_GO_REQUIRED queue)
  - _SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md (D6 #1 pattern)
  - .claude/mindsets/Rick_Mindset.md (SOBRIÉTÉ + Donna DLQ)
closes_action:
  - F2 (pending actions queue, live MCP pivots premortem 2026-06-28)
tags: [#ADR #mcp #plugin #supabase #sober #posture-c #OFF #d6 #catalog]
---

# ADR-MCP-PLUGIN-001 — Plugin Supabase officiel reste canoniquement OFF

## Contexte

Dans `~/.claude/settings.json` ligne ~20, le plugin `supabase@claude-plugins-official` est explicitement mis à `false`. Cet état est **documenté comme D6 #1** dans le catalog append-only `ADR-META-006` (date 2026-06-23, post-CC-restart) — l'entrée consigne que le plugin officiel échoue au démarrage de Claude Code (cause racine non totalement isolée : combinaison suspectée npm-cache stale / resolution du même nom que `mcp__supabase__*` qui crée un conflit de namespace).

**État D1 vérifié 2026-06-28 (per premortem live)** :

| Surface | Custom MCP `supabase` × 3 | Plugin officiel |
|---|---|---|
| Servers (`.mcp.json`) | `supabase` · `supabase-omk` · `supabase-abc` (10 serveurs totaux) | absent (toggle `false`) |
| SessionStart digest | `✓ Connected` × 3 | n/a (pas démarré) |
| Couverture fonctionnelle | `apply_migration`, `execute_sql`, `list_tables`, `get_advisors`, `list_edge_functions`, `deploy_edge_function` × 3 instances | redondant |
| Risque connu | aucun (D1 OK) | D6 #1 catalogué (restart fail) |

L'action **F2** dans le queue `l0_mcp_pivots_premortem_pending_actions.md` est `A0_GO_REQUIRED` : décision toggle `false → true` (Option A, risquée) ou laisser OFF (Option B, recommandée par le premortem live 2026-06-28). Ce ADR formalise l'Option B.

## Décision

**Le plugin `supabase@claude-plugins-official` reste canoniquement `false`** dans `~/.claude/settings.json`. Pas de mutation de la config. Pas d'activation du plugin à quelque moment que ce soit sans nouveau ADR ratifié.

### Justification (5 axes)

1. **Couverture fonctionnelle déjà atteinte** : les 3 custom MCPs `supabase` / `supabase-omk` / `supabase-abc` couvrent l'intégralité des 6 outils nécessaires (`apply_migration`, `execute_sql`, `list_tables`, `get_advisors`, `list_edge_functions`, `deploy_edge_function`) avec scoping per-project distinct. Le plugin officiel n'apporte aucune capability additionnelle.
2. **Risque D6 #1 actif** : activer le plugin recrée mécaniquement la condition de la D6 #1 cataloguée. Tant que la root cause n'est pas isolée (cf. anti-pattern D6 = "creuser le cas précis avant de spéculer"), re-toggle = re-fault.
3. **Surface inutile** : ajouter le plugin officiel duplique 10 outils (3 instances × ~6 outils + plugin × N outils) sans gain opérationnel. Le `SessionStart` digest deviendrait plus bruité (≥30 serveurs vs 10).
4. **Doctrine Sobriété (Rick S1)** : Rick Mindset §"GROUND→SOBER→REASON→ACT" prescrit default NO-GO sur nouvelle complexité. Le plugin n'est pas load-bearing — il est strictement ornemental.
5. **Posture C + Anti-paperclip (ADR-SOBER-002)** : tout toggle kernel P0 (settings.json) exige HITL A0 + ADR ratifié. C'est exactement ce que ce document accomplit formellement.

## Conséquences

### Positives
- Stabilité CC restart (D6 #1 ne peut plus se reproduire sur ce toggle).
- Digest SessionStart reste lisible (10 serveurs Connected = suffisant).
- Custom MCPs restent source-of-truth Supabase → A3 agents routent via `mcp__symphony-supabase__*` (Life OS) / `mcp__supabase-omk__*` (Nexus OMK) / `mcp__supabase-abc__*` (Orbiter ABC) — déjà canon ADR-ICP-NEXUS-001 / ADR-ICP-ORBITER-001 / ADR-L2-AAAS-001 §D2 Solaris AaaS.

### Risques résiduels
- **Custom MCP failure** : si un jour l'un des 3 custom MCPs tombe en `✗ Failed`, la couverture Supabase rétrécit. **Garde-fou** : monitor D6 catalog — toute nouvelle entrée touchant `supabase` / `supabase-omk` / `supabase-abc` doit déclencher une **ré-évaluation** de cette décision (cf. §"Trigger de re-évaluation" ci-dessous).
- **Plugin officiel évolutif** : si Anthropic publie une version plugin sans le bug D6 #1 (improbable à court terme, le bug n'est pas isolé), re-toggling peut redevenir attractif. **Garde-fou** : Posture C = nouveau cycle ADR obligatoire, pas de toggle direct.

### Trigger de re-évaluation (uniquement ce qui rouvre le débat)

1. **D6 entrée touchant custom MCP Supabase** (`mcp__supabase*` `✗ Failed` non-récupérable).
2. **Plugin officiel update** corrigeant explicitement la D6 #1 (à vérifier dans release notes Anthropic).
3. **A0 explicite** : "active le plugin supabase" → cycle ADR-MCP-PLUGIN-002.

## Alternatives écartées

- **Option A (toggle ON)** : recrée D6 #1 (mécaniquement, sans isolation de root cause). Pas de gain opérationnel. **Écartée**.
- **Per-customer toggle** (plugin ON pour OMK seulement, OFF pour ABC + Life OS) : over-engineering (D6 admission). Le plugin charge globalement, le scoping per-project est impossible côté `settings.json`. **Écartée** (techniquement non-viable + conceptuellement absurde).
- **Ré-écrire le plugin officiel en fork local** : anti-pattern D7 (complexité multiplicative pour 0 valeur). Custom MCPs = canon, plugin = bruit. **Écartée**.

## Status

**PROPOSED 2026-06-28 (Opus, draft F2 close).** En attente de ratification A0 in-session pour clôture définitive de F2. Une fois ratifié → `status: RATIFIED`, `ratified: 2026-06-28 (GO A0)`, et le premortem pending actions file append la ligne de clôture F2 (D4 append-only).

## Sister canon links

- [ADR-L0-META-ORCH-001](ADR-L0-META-ORCH-001_hermes-meta-orchestrator.md) — Hermes méta-orchestrateur runtime (Posture C respectée)
- [ADR-META-006](../L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md) — D6 #1 entrée airtable/clickup post-CC-restart 2026-06-23 (anti-pattern sœur)
- [l0_mcp_pivots_premortem_live.md](../../../00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/l0_mcp_pivots_premortem_live.md) — F2 entry, D1 state map 2026-06-28
- [l0_mcp_pivots_premortem_pending_actions.md](../../../00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/l0_mcp_pivots_premortem_pending_actions.md) — F2 A0_GO_REQUIRED queue (sera mis à jour avec ligne de clôture à ratification)
- [Rick_Mindset.md](../../../../.claude/mindsets/Rick_Mindset.md) — SOBRIÉTÉ kernel + Donna DLQ
