---
type: Concept
title: Claude Certified Architect Study Guide — orphelin, 1 PDF, jamais rattaché
description: Un PDF unique dans 02_Templates/, jamais cité ailleurs dans le corpus, ni par les MD utilisateurs ni par les guides. C'est une ressource tierce (Anthropic certification study guide) sans intégration.
tags: [orphelin, pdf, certification, anthropic, non-integre]
generated: { by: minimax-m3, at: 2026-08-19T20:25:00Z }
verified:
  - { by: process:recherche_grep_orphelin, at: 2026-08-19T20:25:00Z }
sources:
  - id: certified-architect-pdf
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Claude Certified Architect Study Guide/claude_architect_study_guide.pdf"
    title: "Claude Certified Architect Study Guide — PDF unique"
    last_modified: 2026-05
okf_version: "0.2"
---

# Claude Certified Architect Study Guide — orphelin

## Énoncé

Le dossier `Claude Certified Architect Study Guide/` contient **un seul fichier** : `claude_architect_study_guide.pdf`. C'est le **kit le plus petit** de la vague 2.

Le brief de la vague 2 demandait explicitement :

> `Memory Architect Kit` ne fait qu'un seul fichier. Soit c'est un embryon, soit
> c'est un index vers autre chose. Tranche.

Même question pour ce kit, et la réponse est plus tranchée : ce n'est **ni un embryon, ni un index**. C'est une **ressource tierce orpheline**.

## Verdict

**`orphelin`**.

## Pourquoi orphelin

1. **Aucun lien** vers ce dossier depuis aucun fichier MD utilisateur du corpus.
2. **Aucune mention** dans `claude-plugins-guide_2026-07-25.md`, dans `os-audit-SKILL.md`, ou ailleurs.
3. **Aucun rapport** avec les autres kits — pas de cohérence thématique (les autres kits sont des « moules d'architecture agent » ; celui-ci est une « ressource de certification Anthropic »).
4. **Le PDF semble être** un study guide officiel pour la certification Claude Certified Architect (un programme de formation partenaire Anthropic).

## Critères de rattachement possibles (et pourquoi ils échouent)

| Critère | Échec |
|---|---|
| Thématique | la certification est externe aux 9 autres kits qui sont des moules d'architecture |
| Auteur | tiers (probablement un partenaire de formation), pas Mark Kashef |
| Format | 1 PDF autonome, pas de SKILL.md / scripts / references attachés |
| Date | probablement récent (post-mai 2026), mais non-vérifiable |

## Action recommandée

**Laisser tel quel.** C'est une ressource de référence disponible, pas un moule d'architecture. Un futur distillateur pourrait :
- Soit la rattacher à un concept (e.g., « formation certifiante » si A'Space V3 crée un parcours de formation).
- Soit la déplacer vers un dossier `01_References_Tierces/` (qui n'existe pas encore mais serait cohérent avec la séparation « templates » / « ressources »).

Pour cette vague : **constater l'orphelinat, ne pas inventer un rattachement**.

## Comparaison avec les autres « petits » kits

| Kit | Fichiers | Verdict | Justification |
|---|---|---|---|
| Claude Certified Architect Study Guide | 1 (PDF) | `orphelin` | pas d'usage observé, pas de cohérence thématique |
| Memory Architect Kit | 2 (SKILL.md + PDF) | `synthese-datee` | modèle 7 couches applicable à A'Space V3 |
| fable-wargame-kit | 15 | `synthese-datee` (avec trace LEDGER) | mission réelle documentée |

La taille ne suffit pas à caractériser le statut : 1 fichier orphelin peut rester orphelin ; 2 fichiers peuvent être canoniques si leur contenu est riche.

## Concepts liés

- [[concept-kits-utilisation-trace]] — le tableau global des 9 kits
