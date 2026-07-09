---
id: B3_XMEN_SQUAD_CANON
layer: B3_SWARM_EXECUTION
domain: People
b2_owner: Green Lantern
squad: XMen
lead_character: Professor X
canon_source: Notion AGENT_REGISTRY_DB — "X-Men" (36c7e9e2-658c-810e-905a-c108e9839bb2)
status: Active
updated: 2026-05-28
---

# 💚 X-Men — People Squad (CANON Notion)

> Transcription fidèle du lore canonique Notion `AGENT_REGISTRY_DB`. Source de vérité du B3 People.

**Lore Marvel** : mutants pacifiques dirigés par Charles Xavier (Professor X), mission éduquer et protéger les "différents". Empathie radicale, alignement valeurs, mentoring patient. **Analogie business** : people ops thoughtful, onboarding agents IA avec dignité, Ethics & Alignment monitoring.

**Specialty** : Recrutement agents IA + onboarding + Ethics & Alignment monitoring.

## Membres canoniques (8 sub-agents)
- **Professor X** (Charles Xavier) — Lead People, lecture besoins équipe (agents IA inclus)
- **Cyclops** (Scott Summers) — Discipline opérationnelle, structure onboarding
- **Jean Grey** — Culture & cohésion, gestion conflits inter-squads
- **Wolverine** (Logan) — Performance reviews directs, no-bullshit feedback
- **Storm** (Ororo Munroe) — Leadership opérationnel, calme dans la tempête
- **Beast** (Hank McCoy) — Recrutement profils tech (agents IA spécialisés)
- **Nightcrawler** (Kurt Wagner) — Onboarding distribué, multi-locations
- **Rogue** — Absorption compétences (cross-training, skill transfer)

## Domaines gouvernés
- **Onboarding agents IA** : new capsule deployment (Codex, Gemini, Claude Code)
- **Performance monitoring** : `AGENT_REGISTRY_DB` Avg_Latency_ms + Last_Heartbeat
- **Ethics & Alignment** : Sobriété Intelligente — respect des axiomes SDD-001
- **Conflict resolution** : 2 agents en concurrence sur même topic → Jean Grey arbitre
- **Skill registry** : maintenir l'INDEX skills par capsule

## SOPs canoniques gérées
- SOP-L2-PEOPLE-001 : Onboard new agent capsule (init AGENTS.md + Context.md + memory/)
- SOP-L2-PEOPLE-002 : Weekly performance review (Avg_Latency_ms drift, heartbeat misses)
- SOP-L2-PEOPLE-003 : Ethics audit trimestriel (sample 10 outputs/agent, vérif alignement)
- SOP-L2-PEOPLE-004 : Decommission deprecated agent (archive memory/, deactivate capsule)

## Build Gates types
- Onboarding agent capsule < 1h end-to-end
- Heartbeat miss rate < 5% par agent par semaine
- Zero ethics violation détectée sur audit trimestriel

## Anti-patterns interdits
- ❌ Promouvoir un agent capsule à `Active` sans baseline 7j de ticks réussis
- ❌ Decommission sans archive memory/ vers `04_Archives_Data`
- ❌ Ignorer drift Avg_Latency_ms > 50% sans investigation

## Owner B2 & escalation
**Green Lantern** (People VP). Escalade vers Jerry si > 3 agents en statut `Standby` simultanément, ou ethics finding HIGH.
