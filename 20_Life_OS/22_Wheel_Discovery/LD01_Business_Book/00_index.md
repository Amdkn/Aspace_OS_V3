---
okf_version: "0.1"
type: book-doctrine-root
title: LD01 Book — Career & Business (A3 Discovery Crew)
description: Organigramme Doctrine de Book LD01. Source de vérité canonique accessible à tous les harnesses (Claude Code, Hermes, MiniMax, Shadows) sans verrouillage d'outil. Le présent index sert de rail de traversée OKF (§6 progressive disclosure).
timestamp: 2026-07-04T12:00:00-04:00
domain: LD01_Career_Business
agent: A3_Book
horizon: H1_Weekly_PnL
variant: AaaS_Solaris_Kardashev_Type_3
parent_dox: C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\AGENTS.md
sister_plans:
  - C:\Users\amado\.claude\plans\plan-meta-memoire-okf-wiki-graphify-dox.md
  - C:\Users\amado\.claude\plans\plan-minimax-l1-book-lune.md
  - C:\Users\amado\.claude\plans\fancy-hugging-bengio.md
children:
  - 10_methodology/00_CARDIA_overview.md
  - 20_skeleton/00_module_template.md
  - 30_decisions/ADR-LD01-001_organigramme_doctrine.md
  - 30_decisions/ADR-LD01-002_agnostic_harness_access.md
  - 90_manifests/manifest.cross-harness.md
  - 99_meta/doctrine_lock_map.md
---

# LD01_Business_Book — Index Racine (OKF v0.1)

> **D1 receipt** : `okf_version: "0.1"` posé 2026-07-04 par MiniMax (posture C — additive only, conforme métamémoire §3 décision #1).

## 1. Identité canon

- **Nom canon** : Book (`A3_Book` — Cleveland "Book" Booker, Discovery crew reference)
- **Domaine** : LD01 Career & Business (Life Wheel · Wheel of Discovery)
- **Statut** : `SHADOW_ACTIVE` (cf. `A3_Book_LD01_Spec.md`)
- **Horizon canon** : **H1 Weekly P&L** — PAS H10. Verrouillé par `symphony/L1/lane_A_specs/03_A3_crews/discovery/book.twin.md`
- **Variant AaaS** : **Solaris** (Civilisation Kardashev Type 3, H90 Legacy 1000T par valeur Solarpunk/biomimétisme — Benyus + Aberkane)
- **Twin** : `book.twin.md` (canon absolu, ce folder en est le miroir filesystem)

## 2. Doctrine de traversée (DOX walk — toujours lire racine → cible)

1. Ouvrir ce `00_index.md` (root of progressive disclosure)
2. Lire `AGENTS.md` (contrat de zone filesystem — ownership + Local Contracts + Verification)
3. Lire `CLAUDE.md` (contrat de harness/projet)
4. Selon la tâche, plonger dans le module `XX_*` correspondant :
   - `10_methodology/` → *comment* décider (CARDIA-TDD)
   - `20_skeleton/` → *comment* structurer un module
   - `30_decisions/` → *pourquoi* on a choisi (ADR append-only)
   - `90_manifests/` → *qui* consomme (cross-harness)
   - `99_meta/` → *quand* et *combien* (calendar, rot-rates)

## 3. Ponts vers l'existant (lecture additive)

| Fichier existant | Rôle dans l'organigramme | Action |
|---|---|---|
| `A3_Book_LD01_Spec.md` | Identité canonique A3 Book (immutable) | CONSERVER tel quel — référence obligatoire |
| `BIBLIOGRAPHY.md` | Les 6 livres canoniques Business (CF A0 2026-05) | CONSERVER tel quel — loader pour `20_skeleton/40_BIBLIOGRAPHY_6livres/` si expansion |
| `01_Guides_Business/` | Junction Physique vers Geordi Premium guides | CONSERVER — sert d'entrée aux guides YouTube distillés |
| `README.md` | Handoff A3 (minimaliste §1-19) | CONSERVER — préserver format |

> **Posture C** : tout ajout est additif. Aucune réécriture des fichiers existants. Aucune migration destructrice.

## 4. Liens parents (remontée DOX)

- Parent canon : `C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\AGENTS.md` (à venir en P4.2 organigrammes-doctrine)
- Parent Life OS : `C:\Users\amado\ASpace_OS_V2\20_Life_OS\` (index racine à venir)
- Parent Amadeus Core : `C:\Users\amado\ASpace_OS_V2\01_Identity_Core\AGENTS.md` (canon absolu)

## 5. Liens enfants (descente DOX)

Voir frontmatter `children:` ci-dessus + navigation §2.

## 6. Source de vérité canonique (anti-paperclip)

**Cette structure filesystem est l'unique source de vérité.**
- `.claude/CLAUDE.md`, `.mavis/disposition.md`, `.hermes/disposition.md` = **registres de harnesses** (pointeurs, pas copies)
- `book.twin.md` dans `symphony/` = référence sémantique (canon sister, jamais dupliqué)
- L'outil de harness ne contient AUCUN état canonique propre : il *consomme* l'organigramme.
