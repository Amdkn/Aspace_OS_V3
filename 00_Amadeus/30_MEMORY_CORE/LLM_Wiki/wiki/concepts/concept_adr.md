---
source: LLM_Wiki_A0
date: 2026-05-10
type: concept
domain: A0_Sovereignty / Tech_OS / ADR_Canon
tags: [#concept #ADR #Architecture_Decision_Record #Immutability #Canon #Rick_Law]
---

# Concept: ADR (Architecture Decision Records)

> Le canon juridique de Rick. Créé une fois, jamais réécrit.

Un **ADR** est un enregistrement d'une décision architecturale — le *pourquoi* et non le *quoi*. Les ADRs sont le mécanisme par lequel [[entity_rick|Rick]] governance le Tech OS.

---

## Format Standard

```markdown
# ADR-XXX: Titre de la Décision

## Status
Accepted | Deprecated | Superseded

## Context
Contexte de la décision (problème, contraintes)

## Decision
Ce qui a été décidé

## Consequences
- ✅ Positif: ...
- ❌ Négatif: ...
```

---

## Règles Absolues (Rick's Law)

1. **Immuabilité**: Un ADR une fois créé ne est jamais réécrit
2. **Nouveaux ADRs**: Une nouvelle décision → un nouveau ADR (pas de rewrite)
3. **Canon first**: Toute anomalie → nouvelle ADR, pas modification
4. **Ancrage**: Tout ADR doit être ancrée dans [[entity_amadeus|AGENTS.md]]

---

## ADR Actifs Connus

| ID | Sujet | Règle clé |
|----|-------|-----------|
| **ADR-001** | OpenClaw Position | `03_OpenClaw_Body` = config only, jamais clone |
| **ADR-002** | Portabilité Multiverse | `ASPACE_ROOT` env var — pas de chemins hardcodés |
| **ADR-003** | agents_registry.json | Mapping Canon ↔ Runtime ↔ Config |
| **ADR-006** | Windows Watchdog | Native PS persistence over Docker |
| **ADR-007** | **Paradigm Shift V2** | Trust Zone `C:\Users\amado` — **ADR fondateur** |

ADR-007 est le plus important — c'est l'ADR qui fonde le système entier.

---

## ADR vs. SDD

| | ADR | SDD |
|--|-----|-----|
| Granularité | Décision unique | Spécification complète |
| Longueur | 1 page | Multi-pages |
| Fréquence | Une par décision | Une par feature |
| Immuabilité | Stricte | Une seule version canonique |

---

## Liens

- [[entity_rick]]: Rick écrit et maintient les ADRs
- [[entity_tardis_protocol]]: TARDIS Protocol historise les modifications d'ADRs
- [[concept_sovereignty]]: La souveraineté de Rick s'exprime via les ADRs

---

## Source

- [[sources/source_gemini-takeout-2026-05]] (1,097 mentions dans Mai 2026)
- [[sources/source_gemini-takeout-2026-03]] (135 mentions en Mars 2026, inception des ADRs)

---



---

## Inbounds

- [[concept_adr]]
*Last updated: 2026-05-10*