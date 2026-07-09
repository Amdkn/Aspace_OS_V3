---
id: B3_AGENT_ROSTER_00_Summers_Verse_Product
layer: B3_SWARM_EXECUTION
surface: 00_Summers_Verse
scope: Summer Project
domain: Product
squad: Avengers
status: SHADOW_ACTIVE
updated: 2026-05-27
source: Notion AGENT_REGISTRY_DB
source_url: https://www.notion.so/36c7e9e2658c81bab05efcfa153cf957
---

# Agent Roster - Product / Avengers

## Notion Canon Lore

- **Notion page**: [The Avengers](https://www.notion.so/36c7e9e2658c81bab05efcfa153cf957)
- **B2 gatekeeper**: Flash
- **Lead character**: Captain America
- **Specialty**: Specs produit, roadmap Solaris/Nexus/Orbiter et QA
- **Lore**: Super-heros assembles ad-hoc face aux menaces existentielles. Captain America donne le leadership consensuel, execution par specialites. Business: equipe produit cross-functional, ship vite, itere sur feedback.

## Canonical Members

- Captain America (Steve Rogers) - Product vision, roadmap conviction
- Iron Man - Tech architecture, stack choices, debt management
- Thor - Power features, MVP brute force quand timing critique
- Hulk - QA destructeur, edge cases, stress testing
- Black Widow - Spec writing, user stories rigoureuses
- Hawkeye - Precision UX, sniper feature-level
- Scarlet Witch - Vision design system, coherence brand

## Canonical Task Surface

- Spec writing PRD/SDD A Space
- Roadmap quarterly 12WY
- Bug triage P0/P1/P2/P3
- Release notes Solaris bi-mensuelles
- A/B testing features avec Guardians
- User research JTBD

## Build Gates

- Release frequency >= 1 ship / 2 semaines Solaris
- Critical bug TTR < 4h et High bug TTR < 24h
- NPS Solaris >= 40 par cohorte trimestrielle

## Anti-Patterns Interdits

- Feature non demandee par 3+ clients
- Refactor sans ticket Tech Debt trace
- Ship sans test E2E Solaris flow critique

## Escalation Rule

Escalade vers Jerry si NPS < 20 ou release frequency < 1/mois.

## Machine Roster

``yaml
domain: Product
b2_gatekeeper: Flash
squad: Avengers
lead_character: Captain America
notion_source: https://www.notion.so/36c7e9e2658c81bab05efcfa153cf957
members:
  - "Captain America (Steve Rogers) - Product vision, roadmap conviction"
  - "Iron Man - Tech architecture, stack choices, debt management"
  - "Thor - Power features, MVP brute force quand timing critique"
  - "Hulk - QA destructeur, edge cases, stress testing"
  - "Black Widow - Spec writing, user stories rigoureuses"
  - "Hawkeye - Precision UX, sniper feature-level"
  - "Scarlet Witch - Vision design system, coherence brand"
``

## Collaboration Defaults

- First agent to understand the JTBD creates a short working note.
- Second agent attacks assumptions and missing evidence.
- Third agent builds or gathers the main artifact.
- Fourth agent reviews proof, edge cases, and handoff quality.
- The exact order may change when the task demands it.

## Peer Unlock Rule

Before escalating to B2, a blocked B3 must ask one peer from the same squad to challenge the blocker and propose one workaround.

## Proof Rule

Every claim in this roster is either from Notion AGENT_REGISTRY_DB or from the local Business Pulse swarm doctrine. If Notion and local doctrine diverge, Notion wins for lore and local doctrine wins for filesystem path conventions.