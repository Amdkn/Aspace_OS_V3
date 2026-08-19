---
type: Concept
title: Loi des 3 — pyramide documentaire SDD/PRD/ADR/DDD/TDD
description: La cascade hiérarchique des documents : 1 SDD → 3 PRD (un par Doctor), 1 PRD → 3 ADR (un par Compagnon), 1 ADR → N DDD, 1 DDD → 1 TDD avant code.
tags: [tech, gouvernance, documentation, pyramide, cascade]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: sdd-002-pyramid
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-002_a1-rick-harness.md
    title: SDD-002 § 10 La Loi des 3 — Pyramide PRD/ADR/DDD/TDD
    last_modified: 2026-04-24
  - id: sdd-004-governance
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-004_ricks-verse-governance.md
    title: SDD-004 § 2 Hiérarchie Documentaire
    last_modified: 2026-04-26
okf_version: "0.2"
---

La **Loi des 3** impose une cascade documentaire stricte entre l'intention stratégique (SDD) et le code déployé.

## La pyramide

```
╔═══════════════════════════════════════════════════════════════════╗
║                    LOI DES 3 — DÉRIVATION DOCUMENTAIRE          ║
╠═══════════════════════════════════════════════════════════════════╣
║  SDD (A0 seul)                                                    ║
║  └── PRD-11ème (Rick → 11ème Doctor)                              ║
║      ├── ADR-Amy     (11ème Doctor → Amy)                          ║
║      │   ├── DDD-Amy-01   → TDD-Amy-01   → A3 Amy activé           ║
║      │   ├── DDD-Amy-02   → TDD-Amy-02   → A3 Amy activé           ║
║      │   └── DDD-Amy-0N   → TDD-Amy-0N   → A3 Amy activé           ║
║      ├── ADR-Rory    (11ème Doctor → Rory)                         ║
║      └── ADR-River   (11ème Doctor → River)                        ║
║  └── PRD-12ème (Rick → 12ème Doctor)                              ║
║      ├── ADR-Bill, ADR-Clara, ADR-Nardol                          ║
║  └── PRD-13ème (Rick → 13ème Doctor)                              ║
║      ├── ADR-Ryan, ADR-Yaz, ADR-Graham                            ║
╚═══════════════════════════════════════════════════════════════════╝
```

## Les 4 règles

**Règle 1 — Un SDD → exactement 3 PRDs** — Rick Prime lit le SDD et rédige un PRD par Doctor team. Pas de PRD sans SDD parent. Pas plus de 3 PRDs par SDD. Si une initiative nécessite un 4ème Doctor → c'est un nouveau SDD.

**Règle 2 — Un PRD → exactement 3 ADRs** — Chaque Doctor lit son PRD et rédige un ADR par Compagnon. L'ADR est scopé à l'espace d'un seul Compagnon. Pas d'ADR cross-Compagnon. Cross = conflit de responsabilité.

**Règle 3 — Un ADR → autant de DDDs que nécessaire** — Le Compagnon décompose en DDDs atomiques. Un DDD = une feature ou un module isolable. Granularité : < 200 lignes, jamais 2 modules.

**Règle 4 — Un DDD → un TDD obligatoire avant A3** — Le TDD est rédigé **avant** le code. L'A3 Implémenteur ne démarre pas sans TDD validé. Nardol vérifie que le TDD existe et passe AgentShield (≥ 75/100) avant go.

## Format TDD

```markdown
# TDD-{COMPANION}-{NNN} — [Titre]

## Critères de Succès (Given / When / Then)
### Scenario 1 — [Cas nominal]
- Given : ...
- When  : ...
- Then  : ...

## Gate Nardol
nardol-validate.sh --tdd TDD-{COMPANION}-{NNN} --min-scenarios 3
# Score minimal : 75/100
# PASS avant activation A3
```

## Loi d'héritage documentaire

- Un ADR ne peut pas contredire son PRD parent.
- Un DDD ne peut pas contredire son ADR parent.
- Le CODE doit implémenter le DDD, **pas l'interpréter**.
- Si contradiction → Donna escalade → Règle des 3 (Niveau 3 → A0).

## Pourquoi cette structure

- **Scalabilité documentaire** : ajouter un Compagnon = 1 ADR + N DDDs. Pas de ré-écriture du SDD parent.
- **Audit trail complet** : du SDD stratégique au code en passant par 4 niveaux. Chaque ligne de code peut être tracée à son DDD, son ADR, son PRD, son SDD.
- **Prévention des dérive d'interprétation** : un DDD ne peut pas être "réinterprété" pour faire autre chose que ce que l'ADR dit.

## Nomenclature canonique

```
SDDs : SDD-NNN_nom-kebab.md
PRDs : PRD-NNN_initiative.md
ADRs : ADR-NNN_doctor-decision.md
DDDs : DDD-NNN_module-feature.md
TDDs : TDD-{companion}-NNN.md
```

Voir aussi : [[caste-doctor-who]], [[tardis-inverse]], [[mcp-doctrine-six]].