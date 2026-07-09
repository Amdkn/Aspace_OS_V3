---
adr_id: ADR-WORKFLOW-001
title: Workflow Orchestration Topologies — Swarm / Mesh / Hierarchical / Pipeline-by-Design
status: DRAFT
date: 2026-06-22
author: A0 jumeau numérique (delegated to Claude Code A2)
level: L0_Kernel_OS
scope: A'Space OS V2 — 3 A1 / 6 A2 / 35 A3 / 4 MCP / 6 bridges
related:
  - ADR-META-001 (Anti-Paresse D1-D8)
  - ADR-META-005 (Hooks automation)
  - ADR-RICK-001 (OpenHarness incarnation)
  - ADR-L2-AAAS-001 (AaaS Doctrine 3 variants)
  - handoff_a0_jumeau_numerique_2026-06-21
  - handoff_a3_data_cartography_v1_2_2026-06-21
  - handoff_a0_divinity_arsenal_2026-06-20
  - fable-autor-research-loop-symphony-agentos (rule)
---

# ADR-WORKFLOW-001 — Workflow Orchestration Topologies

## 1. Context (D6 root cause)

L'OS agentique A'Space manque d'un **vocabulaire canonique** pour décrire comment 35 A3 + 4 MCP + 6 bridges doivent collaborer. Conséquence observée :

- Mélange implicite de patterns dans les handoffs récents (graphify = swarm partiel, YouTube→PARA = pipeline, weekly 12WY = hiérarchique)
- Routage A1 ambigu (Beth vs Morty sur Mesh = risque D3 nuance)
- Risque D6 réinvention : chaque session A0 ré-derive "qui appelle qui"

**Objectif** : 4 topologies pures, mappées 1-1 à des use cases, routées par A1, auditables D1-D8.

## 2. Topologie A — Hierarchical (canon actuel)

```
A0 (intention, chat méta-orchestration)
  └─ A1 Gatekeeper (Beth | Morty | Rick)       ← routage par intention
       └─ A2 Orchestrator (6 engines)          ← Currie/Zora/Orville/Computer/Holo Deck/Holo Janeway
            └─ A3 Twin (35 actifs)             ← capture / process / persist
                 └─ MCPs / Bridges (10)
```

**Use cases** : weekly 12WY, governance, sprint planning, GTD triage, audit trail.
**Force** : autorité claire, D4 append-only trivial, single A1 sponsor.
**Faiblesse** : latence (4 hops), bottleneck A1 si intention ambiguë.
**D3 nuance** : A0 ne s'adresse JAMAIS à A3 directement (jumeau numérique doctrine).
**Anti-pattern** : court-circuit A1/A2 (A0 → A3 = breach D3, escalade D7 ~100×).

## 3. Topologie B — Swarm (Fable 4-step loop)

```
[A3 X] → capture → [A3 Y] → process → [A3 Z] → persist → loop
   ↑___________________________________________________|
```

**Use cases** : auto-research, multi-source ingestion (YouTube batch), wiki sync, Memory Core ↔ `.claude/memory` alignment, pattern distillation.
**Force** : émergence, parallélisme, Fable 4-pillar alignment (dense penser / fini livrable / relecture / vérité).
**Faiblesse** : drift sans convergence, D4 append-only discipline critique, D6 root-cause facile à manquer.
**Gouvernance** : un A2 sponsor (ex: Curie SNW pour cycle 12WY auto-research), A1 supervision Beth ou Morty.
**Anti-pattern** : swarm sans sponsor A2 = chaos (D6 lesson ships 2026-06-16) ; swarm sans `.processed.json` = re-run non-idempotent.

## 4. Topologie C — Mesh (full-connectivity)

```
[A3] ↔ [A3] ↔ [A3]
  ↕      ↕      ↕
[MCP] ↔ [MCP] ↔ [Bridge]
  ↕      ↕      ↕
[A3] ↔ [A3] ↔ [A3]
```

**Use cases** : recherche cross-LDxx (ex: Stamets LD05 social ↔ Saru LD02 finance ↔ Book LD01 business), SaaS Cloud pre-mortem 4 MCPs (Baserow+Affine+Plane+Obsidian), complexe routage dynamique.
**Force** : optionalité max, routage dynamique selon dispo, fail-over naturel.
**Faiblesse** : explosion combinatoire, audit difficile, D7 cost-of-escalation si mesh diverge.
**Gouvernance** : A1 Rick Sobriété activé temporairement (mode alerte, 7 hard-stop triggers D3), A2 sponsor = Protostar Holo Janeway (DEAL = Liberate par design).
**Anti-pattern** : mesh permanent = inefficiency + D6 contradiction (35 A3 × N calls = combinatorial) ; mesh sans ledger central = audit impossible.

## 5. Topologie D — Pipeline-by-Design (sequential stages)

```
[takeout.html] → [categorize.py] → [88 .md] → [PARA placement] → [Geordi canonical]
   stage 1           stage 2         stage 3         stage 4
   capture           process         persist         loop (idempotent)
```

**Use cases** : transformations déterministes (YouTube→PARA, graphify burst, takeout→Geordi, MEMORY.md split, ADR draft → wiki publish).
**Force** : reproductibilité, idempotence (`.processed.json` pattern), D4 append-only natif.
**Faiblesse** : pas adaptatif au changement, brittle si input schema évolue.
**Gouvernance** : A2 Enterprise Computer (PARA owner) pour stage 4, A1 Morty supervision.
**Anti-pattern** : skip stages (perdre intermediate state), pipeline non-idempotent (re-run = dupes), schema change sans migration script (D6 rupture).

## 6. Matrice routing A1 → topologie

| Intention A0 (exemples) | Topologie | A1 sponsor | A2 sponsor | Exemple canon |
|---|---|---|---|---|
| "Weekly review 12WY" | Hierarchical | Morty | Curie SNW | handoff SNW weekly |
| "Bilan YouTube du cycle" | Pipeline | Morty | Enterprise Computer | youtube-takeout-to-lifeos |
| "Auto-research Fable X" | Swarm | Beth ou Morty | selon domain | graphify-swarm-burst |
| "Cross-LDxx impact audit" | Mesh | Beth (Discovery) | Protostar Holo Janeway | SaaS Cloud pre-mortem |
| "Cadrage décision kernel" | Hierarchical | Rick (Sobriété) | Rick direct | Q4 2026 / Q1 2027 only |
| "PARA placement validé" | Pipeline | Morty | Enterprise Computer | ADR-INFRA-003 §D1 |
| "Ikigai convergence check" | Swarm | Beth | Orville Meaning | cycle W12 |
| "DEAL pattern detection" | Mesh | Beth | Protostar Holo Janeway | Dal definition |

## 7. Composition rules (topologies peuvent-elles nicher ?)

| Nested | Allowed ? | Reason |
|---|---|---|
| Pipeline inside Hierarchical | ✅ Oui | stage 1 capture = A3 Mariner, mais stage 2 process = A2 Computer |
| Swarm inside Hierarchical | ✅ Oui | A2 Curie orchestre swarm A3 de son engine |
| Mesh inside Hierarchical | ⚠️ Vigilance | A2 Protostar supervise mesh interne, mais A1 Rick sobriété activée |
| Pipeline inside Swarm | ❌ Non | swarm = émergence, pipeline = déterministe — conflit ontologique |
| Mesh inside Swarm | ⚠️ Possible mais redondant | swarm = déjà quasi-full-connectivity |
| Hierarchical inside anything | ❌ Non | hierarchical = top-level uniquement (A0 = apex) |

## 8. Anti-patterns transversaux (D1-D8 overlay)

| D# | Anti-pattern | Topologie(s) affectée(s) |
|---|---|---|
| D1 | Claim sans receipt (no file/byte/count proof) | toutes |
| D2 | Action sans research canon first | toutes |
| D3 | Confusion niveaux (A0 ↔ A ↔ A1 ↔ A3) | Hierarchical surtout |
| D4 | Modification canon existant (vs append-only) | toutes |
| D6 | Ré-derive archi au lieu de lire ADR | toutes |
| D7 | Escalade A0 mid-workflow | toutes, Swarm + Mesh surtout |
| D8 | Cross-agent drift (Claude ≠ Codex ≠ Gemini) | toutes |

## 9. Hooks overlay (ADR-META-005 IMPLEMENTED)

- **PreToolUse destructive guard** : log-only Q3 2026, hard-block Q4 2026
- **PostToolUse rotation 7j** : log tool outputs, archive weekly
- **SubagentStart throttle 1/10** : prevent A3 swarm explosion
- **SubagentStop cleanup** : release MCP/budget

## 10. Successor ADRs à écrire (post-RATIFICATION)

1. **ADR-WORKFLOW-002** : Routing decision tree (intent parser → A1 sponsor → topology)
2. **ADR-WORKFLOW-003** : Mesh governance (ledger central, Rick sobriété triggers)
3. **ADR-WORKFLOW-004** : Pipeline handoff contract standard (`.processed.json` schema)
4. **ADR-WORKFLOW-005** : Swarm convergence protocol (quorum, sponsor override)
5. **ADR-WORKFLOW-006** : A2 sponsor accountability matrix (6 engines × 4 topologies)

## 11. Open questions pour A0 ratification

1. **Mesh = which scope ?** SaaS Cloud only, ou eligible à d'autres contexts ?
2. **Swarm convergence : quorum ou sponsor override ?** (D6 risk : swarm diverge, qui tranche ?)
3. **Rick Sobriété : combien de mesh sessions/an sont tolérables ?** (doctrine "1×/an max" = pour kernel pivots, mesh = runtime quotidien = conflit ?)
4. **Pipeline stage gates : validation humaine A0 ou A1 suffit ?** (D7 cost-of-escalation)
5. **Composition rules : figer dans ADR ou laisser émerger ?** (YAGNI vs D6 root-cause prevention)

## 12. Status

**DRAFT** — needs A0 review (chat méta-orchestration level only) + A1 Beth/Morty avis (Ikigai + Focus) + A2 sponsor acknowledgement.
**Pas de RATIFICATION** avant que les 5 open questions soient tranchées par A0 verbal GO.

---

*Draft produced 2026-06-22 in tight-mode session (junction wiki/ + MEMORY.md §"START HERE" only, full CLAUDE.md dropped per A0 Turn 3 strategy). ADR-WORKFLOW-001 to supersede implicit topology references in 6 handoffs canon (graphify, youtube-ingest, SaaS Cloud, OMK, abc-os, Life-OS-2026).*
