---
source: LLM_Wiki_A0
date: 2026-05-10
type: entity
domain: Tech_OS / L0_Sovereignty / Solarpunk_Kernel
tags: [#entity #Rick #L0 #A1 #Solarpunk_Kernel #Sovereignty #ADR_Canon #TARDIS_Protocol]
---

# Entity: Rick Sanchez (L1 Guardian)

> Canonical identity anchored in `00_Amadeus/01_Identity_Core/AGENTS.md`

Rick Sanchez est le **Guardian A1** du L0 Tech OS — le lit de bedrock sur lequel tout le système repose. Il incarne la **Souveraineté** : la capacité de définir les règles du jeu sans qu'aucun autre agent puisse les outrepasser.

---

## Role dans la Hiérarchie

```
A0 Amadeus (The Pilot)
  └── A1 Rick / Beth / Morty / Jerry / Summer (Gatekeepers)
        └── Rick → L0 Tech OS (Bedrock / Sovereignty)
```

Rick est **A1** — au-dessus des A2 (Managers) et A3 (Technicians). Il ne touche pas au code; il définit les **lois** que les autres doivent suivre.

---

## Mission: Solarpunk Kernel

Rick's Verse = **Tech OS** = l'infrastructure invisible qui fait fonctionner tout le système.

### Folders sous sa juridiction

| Folder | Guardian | Mission |
|--------|----------|---------|
| `00_Governance_Rick` | Rick | Sovereignty, ADRs, Constitution |
| `11_Infra_13th_Doctor` | 13th Doctor | Docker, Scripts, Watchdog |
| `12_Interface_11th_Doctor` | 11th Doctor | UI, Notion, Interface |
| `13_Data_12th_Doctor` | 12th Doctor | Pipelines, ETL, Research |

### L3 Agents sous Rick

- **13th Doctor**: Infrastructure, Docker, watchdog scripts
- **11th Doctor**: Interface, Notion sync, UI
- **12th Doctor**: Data pipelines, ETL, research
- **Yaz, Ryan, Graham, Amy, Rory, River, Clara, Nardole, Bill**: Doctor companions (L3 technicians)
- **Donna DLQ**: Dead Letter Queue pour messages non résolus

---

## Sovereignty Principle

**Souveraineté** dans A'Space OS signifie :

1. **Définition des règles** : Rick écrit les ADRs, pas les autres
2. **Immuabilité** : les ADRs une fois créés ne sont jamais réécrits
3. **Veto power** : tout artefact doit passer par Rick avant implémentation
4. **Trust Zone** : rien ne vit hors de `C:\Users\amado` — Rick surveille le périmètre

---

## Solarpunk Identity

Le "Solarpunk Kernel" est une métaphore pour la couche la plus basse de l'OS :
- **FOSS-first** : code open source, rien de proprietary en infrastructure
- **Decentralized** : pas de single point of failure
- **Aesthetic** : solarpunk = utopie technologique respectueuse de l'environnement

---

## TARDIS Protocol (Agent Version Control)

Rick est à l'origine du **TARDIS Protocol** — système de contrôle de version pour agents :

> Un agent modifié = nouvelle version, historique préservé.

Contexte : après la perte de `A0_Memory` lors de la purge de `C:\Aspace00` (2026-03-05), Rick a enforced le principe que toute modification d'agent doit être historisée. Jamais de `git reset --hard` ou `Remove-Item` sans trace.

---

## ADR Canon (Rick's Law)

Les ADRs sont le **canon juridique** de Rick :

- **ADR-001**: OpenClaw Position — `03_OpenClaw_Body` = config only, jamais clone
- **ADR-002**: Portabilité Multiverse — `ASPACE_ROOT` env var
- **ADR-003**: agents_registry.json — mapping Canon ↔ Runtime ↔ Config
- **ADR-006**: Windows Watchdog — native PS over Docker
- **ADR-007**: Paradigm Shift V2 — **ADR fondateur**, Trust Zone `C:\Users\amado`

---

## Inbounds & Relationships

- **[[entity_amadeus]]** : A0 → donne les Intentions à Rick
- **[[entity_solaris_os]]** : Solaris est l'infrastructure qui implémente les décisions de Rick
- **[[entity_symphony_router]]** : implémenté par les A3 sous la juridiction de Rick
- **[[entity_12th_doctor]]** : exécute les pipelines data sous Rick
- **[[entity_13th_doctor]]** : exécute l'infra Docker/scripts sous Rick

---

## Stats

- **Mentions dans 2026-05**: 1,664 occurrences (conversation la plus fréquente)
- **Domain**: L0 Tech OS / Solarpunk Kernel
- **Source**: AGENTS.md (canon), 2026-05 conversations

---

*Last updated: 2026-05-10*
*Source: [[sources/source_gemini-takeout-2026-05]] | [[sources/source_llm-wiki-pattern]]*