---
type: Concept
title: CARDIA-TDD — méthode d'écriture canonique + organigramme Doctrine
description: Méthode canon pour tout module A'Space : 6 propriétés par construction (Choix par défaut Autonome Réversible Durable Intégratif Atomique) + pattern organigramme folder-based.
tags: [cardia-tdd, organigramme, doctrine, adr, dox, folder-based, additive]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: cardia-overview
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/10_methodology/00_CARDIA_overview.md
    title: CARDIA-TDD — Choix par défaut Autonome Réversible Durable Intégratif Atomique
    last_modified: 2026-07-04
  - id: adr-001
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/30_decisions/ADR-LD01-001_organigramme_doctrine.md
    title: ADR-LD01-001 — Organigramme Doctrine
    last_modified: 2026-07-04
  - id: agents-md
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/AGENTS.md
    title: AGENTS.md — LD01 Business Book
    last_modified: 2026-07-04
okf_version: "0.2"
---

# CARDIA-TDD — méthode d'écriture canonique + organigramme Doctrine

CARDIA-TDD est la méthode canon pour écrire un module A'Space OS — par défaut **Autonome Réversible Durable Intégratif Atomique**, testable par construction (TDD). C'est l'évolution du pattern "plan markdown plat" qui ne survivait pas aux compactions de contexte.

## Les 6 propriétés CARDIA

| Propriété | Sens |
|---|---|
| **C**hoix par défaut | Le module est le default ; les dérogations sont explicites |
| **A**utonome | Il s'exécute sans intervention constante, gated HITL aux mutations |
| **R**éversible | Toute action peut être annulée par un chemin documenté |
| **D**urable | Il survit aux compactions, drift, et changements de harness |
| **I**ntégratif | Il s'insère dans DOX bi-famille (filesystem + harness) |
| **A**tomique | Une décision / un module, pas un monolithe |

## Pourquoi cette méthode (verbatim ADR-LD01-001)

> *"Tu me corriges systématiquement parce que je rate des pans entiers du contexte à chaque tour. La racine n'est pas ma discipline, c'est l'outil. Un plan en markdown dans `~/.claude/plans/` n'a aucune garantie de persister entre sessions, aucune garantie que je le relise, aucune garantie qu'il capture la carte mentale complète."*

Le pattern historique d'un seul `.md` long ne survit pas aux compactions, souffre de drift, capture rarement la carte mentale complète.

## Pattern organigramme Doctrine (folder-based)

Pour tout module canonique A'Space :

```
00_index.md                    ← root of progressive disclosure (≤ 50 lignes)
AGENTS.md                      ← contrat de zone filesystem (ownership, Local Contracts)
CLAUDE.md                      ← sister contract pour harnesses (CC/HA/MC/Shadow L1)
10_methodology/00_CARDIA_overview.md   ← *comment* décider
20_skeleton/00_module_template.md      ← *comment* structurer un module
30_decisions/ADR-LD01-NNN_*.md         ← *pourquoi* on a choisi (append-only)
90_manifests/manifest.cross-harness.md ← *qui* consomme
99_meta/calendar.md                    ← *quand* et *combien* (épisode-mémoire)
99_meta/doctrine_lock_map.md           ← pont avec les plans source
99_meta/rot-rates.md                   ← péremption déclarée par module
```

## Local Contracts verrouillés (lecture-seule)

1. **Additivité stricte** : toute mutation = append (nouveau `.md` ou nouvelle section dans un fichier existant).
2. **Frontmatter OKF** : tout `.md` créé DOIT ouvrir par un frontmatter YAML conforme §6 OKF (au minimum `type` top-level).
3. **D1 receipt** : tout nouveau module DOIT avoir au moins 1 vérifieur chiffré (commande → sortie).
4. **ROT déclaré** : tout nouveau module DOIT apparaître dans `99_meta/rot-rates.md` avec sa cadence de péremption.
5. **Heritage canon** : les fichiers spec sont intouchables — toute référence passe par eux.

## Avantages (D1 receipts)

- **Survit aux compactions** : les modules sont chargés à la demande.
- **Drift = 0** : chaque module a son D1 receipt ; le récepteur sait où est la vérité.
- **Carte mentale préservée** : la méthode impose un `00_index.md` racine qui sert de carte.
- **Anti-paperclip renforcé** : append-only structurel, pas seulement de discipline.
- **Cross-harness** : un folder filesystem est lisible par TOUT harness — pas un tool-lock.

## Coûts assumés

- Migration des 4 plans principaux vers organigrammes Doctrine (estimé 4-8 h avec gain récurrent).
- Risque de duplication entre `book.twin.md` (symphony canon) et `LD01_Business_Book/` folder — mitigation : twin = sémantique, folder = filesystem, règle DOX dans `00_index.md` §6.
- Charge cognitive sur harnesses (apprentissage CARDIA-TDD) — mitigation : `00_CARDIA_overview.md` ≤ 200 lignes.

## Anti-patterns CARDIA-TDD

- Hard-delete d'un `.md` (utiliser `_TRASH/` ou préfixe `DEPRECATED_`).
- Réécriture d'un spec canon (intouchable).
- Création de doublons dans une junction (c'est un pointeur, pas une copie).
- Cron automatique sans HITL A0 explicite.
- Secret en clair dans un `.md` (PAT, token, secret — voir D5 via Windows Credential Manager).