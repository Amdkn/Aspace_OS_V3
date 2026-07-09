---
id: ADR-AGENTIC-001
title: L2 Agentic Commerce Doctrine — Marvel/DC NanoSquads Multi-Agent Coordination
type: ADR (Architectural Decision Record)
status: PROPOSED (A0 sign-off 2026-06-15 via "go for all", à valider scope Templates mission 4)
date: 2026-06-15
author: A0 (Amadeus) via A2 (Claude Code) sub-agent
domain: L2 Business_OS / Agentic Commerce / Multi-Agent Coordination
tags: [#ADR #l2-business #agentic-commerce #nanosquad #marvel-dc #coordination]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-CANON-001, ADR-OMK-001, ADR-OMK-002, ADR-OMK-003]
related: [AGENTS.md, "AGENTS.md L2 Business Pulse (Fractal) — 8 Secteurs SOA01-SOA08 + Marvel/DC Nano Squads"]
provenance: |
  Née 2026-06-15 de l'analyse mission 4 (PARA Geordi 02_Templates) : template Tilly
  `05_l2_agentic_commerce_nanosquads` détecté. Doctrine à formaliser : 8 secteurs SOA01-SOA08
  (Business Pulse fractal) coordonnés par Marvel/DC NanoSquads (X-Men/Avengers/Guardians/F4/Thunderbolts/Eternals/Kang),
  avec ownership produit, RLS, et pattern coordination inter-squad.
sign_off_a0: "A0 Amadeus — Go ADR-AGENTIC-001 — 2026-06-15 (via 'go for all' session-level directive, scope à valider)"
sign_off_pending: false
ratification_log_2026-06-15: "A0 batch GO. D4 append-only. D7 = pas d'escalation additionnelle."
---

# ADR-AGENTIC-001 — L2 Agentic Commerce Doctrine

## Status
**PROPOSED → ACCEPTED via "go for all" A0 2026-06-15** (scope templates mission 4 — A0 priorise
au prochain tour si hypothèse A2 erronée).

## Context

1. **Mission 4 (2026-06-15)** : A2 a identifié 5 templates candidats. Le présent ADR couvre
   template **#5** présumé = "L2 Agentic Commerce NanoSquads" (Tilly canon tier 1).
2. **AGENTS.md L2 Business Pulse** déjà spécifie : 8 Secteurs SOA01-SOA08 + Marvel/DC Nano Squads
   (People=X-Men, IT=Kang Dynasty, Ops=F4, Product=Avengers, Growth=Guardians, Finance=Thunderbolts,
   Legal=Eternals).
3. **ADR-CANON-001** ancre le roster source-of-truth (Notion `AGENT_REGISTRY_DB`).
4. **ADR-OMK-001/002/003** déjà démontrent le pattern : dual-product dashboard (SaaS + internal),
   PG roles strict, MCP supabase-aspace.
5. **Manque** = doctrine **coordination inter-squad** explicite (qui appelle qui, sous quelles
   conditions, avec quel pattern de handoff).

## Decision

**D1 — 8 secteurs SOA01-SOA08 = perimeter L2** :
- SOA01-SOA03 : core commerce (sales, marketing, product).
- SOA04-SOA06 : support (finance, legal, ops).
- SOA07-SOA08 : meta (governance, knowledge).

**D2 — 7 Marvel/DC NanoSquads = execution** (canon AGENTS.md) :

| NanoSquad | Secteur SOA owner | Mission |
|----------|-------------------|---------|
| **X-Men (People)** | SOA03 (HR adjacent) | Talent, formation, culture |
| **Kang Dynasty (IT)** | SOA04-SOA05 (Infra) | Plateforme, sécurité, scalabilité |
| **F4 (Ops)** | SOA05 (Ops) | Daily operations, incident response |
| **Avengers (Product)** | SOA01-SOA02 (Product) | Discovery, build, ship |
| **Guardians (Growth)** | SOA01 (Sales/Marketing) | Acquisition, retention, brand |
| **Thunderbolts (Finance)** | SOA04 (Finance) | Comptabilité, forecast, runway |
| **Eternals (Legal)** | SOA06 (Legal) | Compliance, contrats, RGPD |

**D3 — Coordination inter-squad = handoff explicite** :
- Pattern : NanoSquad A termine un livrable → handoff à NanoSquad B via
  `wiki/hand_offs/nanosquad_handoff_<date>_<topic>.md` (append-only).
- D1 receipts obligatoires dans chaque handoff (chemin:fichier:ligne).
- D2 research-first : si handoff nécessite recherche, sub-agent dédié (pas de mélange d'expertise).

**D4 — RLS strict par squad** : chaque squad voit uniquement les données de son scope SOA.
Implémentation = `Accept-Profile: omk_saas` header (cf. OMK-001) + PG roles
`aspace_admin`/`aspace_observer` (cf. OMK-002). Pas de cross-squad data leak.

**D5 — Roster canon = Notion** (cf. ADR-CANON-001) : modifications roster = Notion `AGENT_REGISTRY_DB`
update, sync vers AGENTS.md local. Skill `/replicate-squads` encapsule le workflow.

## Consequences

- ✅ 8 secteurs SOA + 7 NanoSquads = matrice claire ownership L2.
- ✅ Handoff explicite = traçabilité D1 receipts entre squads.
- ✅ RLS strict = sécurité données par squad.
- ✅ Roster canon Notion = source unique de vérité (pas de drift).
- ⚠️ Coût initial : peupler `AGENT_REGISTRY_DB` Notion (A0 ou sub-agent dédié, ~3-5h).

## References

- `02_Templates` PARRA Geordi mission 4 (template source Tilly `05_l2_agentic_commerce_nanosquads`).
- `AGENTS.md` L2 Business Pulse (Fractal) — 8 Secteurs SOA01-SOA08 + Marvel/DC NanoSquads canon.
- `ADR-CANON-001_roster-source-of-truth.md` (roster Notion canon).
- `ADR-OMK-001_dual-product-dashboard-multitenant_RATIFIED.md` (exemple product).
- `ADR-OMK-002_pg-roles-provisionning.md` (RLS pattern).
- `ADR-OMK-003_mcp-supabase-aspace.md` (MCP wrapper per-squad).
- `~/.claude/skills/replicate-squads/` (skill roster sync, si créé).
