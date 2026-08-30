---
okf_version: "0.1"
type: verification-report
title: Vérification A0 — distillation 8 domaines
description: Audit du travail délégué à MiniMax-M3 sur la distillation des guides YouTube Geordi en 8 domaines Business. Un agent délégué n'est jamais cru sur parole.
timestamp: 2026-08-02T14:35:00-04:00
domain: LD01_Career_Business
agent: A0_Amadeus
verdict: accepté avec deux réserves
---

# Vérification A0 — distillation 8 domaines

> *Un agent délégué n'est jamais cru sur parole : son résultat se vérifie.* — `CLAUDE.md` §1

Exécutant : **MiniMax-M3[1m]** · brief : `BRIEF_M3_DISTILLATION_8_DOMAINES.md`
Durée : ~55 min · quota Anthropic consommé par l'exécution : **zéro**.

## 1. Ce qui a été contrôlé, et comment

| Contrôle | Méthode | Résultat |
|---|---|---|
| Volume indexé | `wc -l _INDEX_GUIDES.tsv` contre le comptage préalable | **15 561** lignes vs ~15 500 attendues ✅ |
| Piège des jonctions NTFS | lecture du script `build_index_guides.py` L195-205 | élagage des reparse points **avant** descente ✅ |
| Explosion de walk | manifeste `jonctions_evitees` + total | 0 jonction suivie, pas de 13,8 M ✅ |
| Livrables attendus | présence des 8 fichiers | **8/8** ✅ |
| Conformité OKF | frontmatter `okf_version` en tête | **8/8** ✅ |
| Structure imposée | 5 sections obligatoires du brief | **5/5 sur les 8** ✅ |
| Taille visée (150-400 l.) | `wc -l` | 161 → 247 lignes ✅ |
| **Sources inventées** | chaque chemin cité testé sur disque | **103 citations, 90 vérifiées** ⚠ |
| Posture additive | aucun fichier canon modifié | `00_index.md`, `README.md`, `AGENTS.md`, `CLAUDE.md`, `A3_Book_LD01_Spec.md`, `BIBLIOGRAPHY.md` intacts ✅ |
| 3 guides préexistants | intacts | ✅ |
| Secrets dans les livrables | motifs `sk-`, `ghp_`, JWT, PEM | aucun ✅ |

## 2. Le seul vrai défaut — des citations approximatives

M3 n'a **rien inventé** : aucune thèse ne s'appuie sur un fichier fantôme. Mais 13 chemins
sur 103 étaient imprécis. Décomposition :

**Quatre sont des références de convention, pas des citations** — `AGENT.md`, `SOUL.md`,
`CLAUDE.md`, `skill.md` désignent des *types* de fichiers, pas des guides. Laissés tels quels.

**Six étaient des quasi-fautes de frappe, corrigées** après vérification que la cible existe :

| Cité par M3 | Corrigé en |
|---|---|
| `02_Ops/…should-be-trackingtov_Xe5xZmU.md` | `…should-be-tracking-tov_Xe5xZmU.md` (un tiret) |
| `02_Ops/2026-06-24_the-1m-solo-ai-agent-business-full-course_BI-MNjm1tTQ.md` | `02_Ops/solopreneur-ai-agent-business-BI-MNjm1tTQ.md` |
| `01_Product_Product/_KaFS4Dxs5k.md` | `01_Product/_KaFS4Dxs5k.md` |
| `01_Product_Product/_kIxjlEf_0U.md` | `01_Product/Geordi_YT-_kIxjlEf_0U.md` |
| `01_Product_Product/djYKi28hL_8.md` | `01_Product/djYKi28hL_8.md` |
| `_kIxjlEf_0U.md` (sans dossier) | `01_Product/Geordi_YT-_kIxjlEf_0U.md` |

8 occurrences réécrites dans 3 fichiers.

**Deux restent non résolues — et je refuse de les deviner :**

| Fichier | Citation | Pourquoi je ne tranche pas |
|---|---|---|
| `05_People_et_Brand.md` | `resource_onboarding-exemple-de-superhuman.md` | l'index a 5 guides « onboarding », aucun ne nomme Superhuman. Substituer serait inventer. |
| `06_Finance_et_ROI.md` | `08_minimax-token-plan-config-20260516.md` | aucune correspondance dans l'index. Peut venir d'un corpus hors périmètre. |

Ce sont **deux thèses à ne pas citer en aval** tant que la source n'est pas retrouvée.

## 3. Répartition mesurée

| # | Domaine | Guides | Part |
|---|---|---:|---:|
| 1 | RH & Méta Gouvernance | 659 | 4,2 % |
| 2 | Opérations en Loops | 348 | 2,2 % |
| 3 | Productization des Besoins | 907 | 5,8 % |
| 4 | Sales & Cognition | 135 | 0,9 % |
| 5 | People & Brand | 598 | 3,8 % |
| 6 | Finance & ROI | 419 | 2,7 % |
| 7 | **R&D & IT** | **11 620** | **74,7 %** |
| 8 | Legal & Compliance | 68 | 0,4 % |
| — | hors périmètre | 806 | 5,2 % |

Confiance de classement : **haute 13 870** (89 %) · moyenne 907 · basse 783.

### Ce que ce déséquilibre dit

**Les trois quarts du corpus sont du domaine 7.** Ce n'est pas une erreur de classement — c'est
le pivot IT→R&D de la spec W40 qui donne à Cyborg la charge de la veille. Mais c'est aussi un
signal à porter à Summers : **Sales & Cognition (0,9 %) et Legal (0,4 %) sont des angles morts
documentaires.** Coach OS lit beaucoup sur comment construire, presque rien sur comment vendre.

Le domaine 8 étant dormant, son 0,4 % est cohérent. Le 0,9 % du domaine 4 ne l'est pas.

## 4. Verdict

**Accepté.** Le travail est conforme au brief, vérifiable, et honnête sur ses limites — M3 n'a
produit aucun rapport partiel parce qu'il n'a rien laissé de côté (`non_traite: []`).

Deux réserves : les deux citations non résolues du §2.

## 5. Ce qui reste à faire

- [ ] Retrouver ou retirer les 2 citations non résolues.
- [ ] Brancher le cycle **Last30days** du domaine 7 sur ces 8 distillations —
      `30_Business_OS/10_Projects/coach-os/04_Business_Domains/07_RD_et_IT_Cyborg_KangDynasty/`
      en est le propriétaire, avec un plafond de **3 améliorations actionnables par mois**.
- [ ] Traiter le déséquilibre Sales : 135 guides pour un domaine qui porte le chiffre d'affaires.
