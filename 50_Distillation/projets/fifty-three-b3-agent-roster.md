---
type: Concept
title: 53 B3 Agent Roster
description: Roster canonique de 53 agents B3 du projet OMK — organisés en 8 squads Marvel (X-Men, Avengers, Fantastic4, Guardians, Illuminati, Thunderbolts, Kang Dynasty, Eternals), profils documentés `_doctrine/agents/b3-*.md`.
tags: [concept, b3, agents, roster, 53, omk, marvel, squads]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraire_substrat_rdf, at: 2026-08-17T19:50:00Z }
  - { by: process:lecture_concepts_picard, at: 2026-08-17T21:00:00Z }
sources:
  - id: roster-08-legal
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/01_B3_AGENT_ROSTER.md"
    title: 01 B3 Agent Roster — Legal (Aquaman/Eternals, 2026-05-27)
    last_modified: 2026-05-27
  - id: roster-04-ops
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/04_Ops_Batman_Fantastic4/01_B3_AGENT_ROSTER.md"
    title: 01 B3 Agent Roster — Ops (Batman/Fantastic4)
    last_modified: 2026-05-27
  - id: roster-01-growth
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/01_Growth_Superman_Guardians/01_B3_AGENT_ROSTER.md"
    title: 01 B3 Agent Roster — Growth (Superman/Guardians)
    last_modified: 2026-05-27
okf_version: "0.2"
---

# 53 B3 Agent Roster

## Définition

**53 agents B3** constituent le roster canonique d'OMK Business OS. Ce
sont les **unités d'exécution** au niveau B3 — *the agency IS the product,
not a tool* (Ownerbook T1 §2). Chaque agent a un profil documenté
(`_doctrine/agents/b3-*.md`) avec rôle, horizon, et sister canon.

## Répartition par squad

| Squad | B2 captain | Domaine | Agent count (estimé) |
|-------|-----------|---------|----------------------|
| **X-Men** | GreenLantern (People) | 07 | ~7 |
| **Fantastic4** | Batman (Ops) | 04 | ~4 |
| **Avengers** | Flash (Product) | 03 | ~7 |
| **Guardians of the Galaxy** | Superman (Growth) | 01 | ~7 |
| **Illuminati** | JohnJones (Sales) | 02 | ~7 |
| **Thunderbolts** | WonderWoman (Finance) | 06 | ~7 |
| **Kang Dynasty** | Cyborg (IT) | 05 | ~7 |
| **Eternals** | Aquaman (Legal) | 08 | ~7 |

Les 8 Roster files font 400-470 mots chacun, taille cohérente. Le
compte exact 53 vient du Ownerbook T1 (DoD-1) :
> "verify: `ls .claude/agents/b3-1-* | wc -l` ≥ 7 (X-Men squad canon)"

## Le pattern de la fiche roster

Chaque `01_B3_AGENT_ROSTER.md` (~400-470 mots) documente :
- Nom et rôle canonique
- Horizon (H10 / H30 / H90)
- B2 owner + sister canon
- Trigger phrases (pour dispatch Uplink B2→B3)
- Edge cases / anti-patterns

## Le 53 — pourquoi ce nombre

Le nombre 53 est **assertif, pas calculé**. Ownerbook T1 DoD-1 attend
"≥7 agents par squad" sans donner le total cible. C'est un invariant
formulé dans le canon avant d'être compté. **Action-Reaction** : un
audit qui voudrait vérifier devrait faire
`find .claude/agents -name 'b3-*.md' | wc -l` — verb cité par Ownerbook
T1 mais pas exécuté dans le corpus visible.

## Cycle de mise à jour

Les 8 Roster files sont datés **2026-05-27** (synchrones). C'est la
trace d'une **vague de documentation** B3 — à cette date, les 8 B2
captains ont écrit ou fait écrire les listings de leur squad. Trois
mois plus tard, aucune révision ne vient публиquer un changelog
d'effectif.

## Sources de la doctrine

- **ADR-CANON-001** "53 B3 roster source of truth" — référencé
  Ownerbook T1 Abort-A
- **B2_DEFINITION_OF_DONE_SPEC.md** — référencé pour les minimums
  People/Ops/Product
- **W40 §M1+M2 patches** — l'IT infra absorbé à L0 Rick (Cyborg devient
  R&D External Discovery) — peut affecter l'effectif Kang Dynasty

## Liens

- [[omk-business-os]] — le projet qui porte le roster
- [[triptyque-v4-t1-t2-t3]] — la structure qui consomme les squads
- [[eight-domain-avengers-wheel]] — le mapping B2 → B3

## Note de confiance

**Confirmé par machine.** 8 Roster files lus via substrat. Le compte 53
vient du Ownerbook T1, pas d'un comptage exhaustif. Les profils
individuels `b3-*.md` n'ont pas été lus dans cette distillation.

*Standing : 8 Roster files présents, profils individuels non vérifiés.*
