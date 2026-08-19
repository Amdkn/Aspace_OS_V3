---
type: Mapping Spec
title: CEO-Bench ↔ Business OS — gabarit d'adaptation
description: Tableau de correspondance entre les métriques CEO-Bench et les signaux Business OS, avec ce qui se transpose, ce qui ne se transpose pas, et les absences à signaler explicitement.
tags: [ceo-bench, business-os, mapping, b1, b2, b3, signal]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: minimax-m3, at: 2026-08-19T00:00:00Z }
sources:
  - id: ceobench-protocol
    resource: "frameworks/ceo-bench-protocol.md"
    title: "Concept précédent — protocole exact CEO-Bench"
    last_modified: 2026-08-19
  - id: etat-pulse
    resource: "70_Onthologies/pulse/ETAT.md"
    title: "ETAT.md — état des tours B1/B2/B3 + 6 concepts par étage"
    last_modified: 2026-08-19
  - id: boucle-sh
    resource: "60_Implementation_Méthodologiques/_loop/boucle.sh"
    title: "Boucle d'implémentation native (rotation 10 paires)"
    last_modified: 2026-08-19
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine** sur la structure CEO-Bench
> et le code source ; **extrapolation marquée** sur la correspondance vers
> Business OS (B1/B2/B3 n'a pas de définition canonique de « décision »).

# Cadrage

CEO-Bench mesure l'efficacité de décision d'un agent unique sur 500 jours
contre un univers SaaS synthétique. Business OS est un système multi-agents
(B1 direction, B2 coordination, B3 exécution) qui tourne en boucle depuis
août 2026 sur des corpus OMK / Coach OS. Le mapping n'est pas une
transposition littérale — c'est un **gabarit** qui identifie ce qui se
transpose, ce qui ne se transpose pas, et où les absences comptent autant
que les correspondances.

# Tableau de correspondance

| CEO-Bench | Business OS | Transposable ? | Notes |
|---|---|---|---|
| **Cash** ($) | Coût LLM (USD) + capital attention utilisateur | Partiel | CEO-Bench mesure un cash simulé ; Business OS mesure un coût réel. La conversion est monétaire, mais le cash CEO-Bench est fermé (pas de revenu exogène), le nôtre est ouvert (revenu projet). |
| **Subscriptions / customers** | Mandats actifs, projets ACTIVE | Partiel | Compteur discret, même sémantique (« clients payants » ↔ « projets vivants »). Sensibilité au churn équivalent. |
| **Survived 500j** | B1/B2/B3 tournent sans interruption de boucle | **Non** | CEO-Bench a une fin temporelle. Notre boucle est indéfinie — survivre n'a pas de sens, sauf à définir un horizon (12WY = ~1 sprint). |
| **BANKRUPTED** | B2 déclare un projet HALTED ou STOP | Partiel | La faillite CEO-Bench est cash ≤ 0 (présumé). Le HALTED Business OS est une décision, pas un solde — la décision a une cause, pas un chiffre. |
| **Action agent** | Concept OKF posé par un agent en tour | Partiel | CEO-Bench compte les actions agent (1511, 2213…). On compte les concepts (~5/tour/étage). Effet de mesure incomparable. |
| **Cash final / cash initial** | Valeur créée par tour (proxy) | **Non** | Pas de notion de cash de départ en Business OS. Substitut possible : delta entre livrables au tour N et au tour N-1. |
| **Best run agrégé (3 seeds)** | Consensus multi-tours | **Oui** | On peut garder les 3 derniers tours d'un agent et moyenner (subject to same seed discipline). |
| **Plans « if X then Y »** | Mandate acceptance check + signal spec | Partiel | CEO-Bench note la présence de plans conditionnels dans les memos. Business OS formalise via `b1-mandate-acceptance-check.md` — mais sur des artefacts, pas des agents. |
| **Discovery levels** (10/10) | Nouveaux corpus / nouveaux Areas | **Oui** | Mécanisme de discovery cohérent : payer pour réduire le bruit d'information. `info_noise_level_1..5` est l'équivalent direct d'un coût de recherche. |
| **CapacityTier / jour** | Plafond node + plafond LLM | Partiel | Capacity est le coût opérationnel direct (85-75 000 $/j). Notre plafond node est hardware (40 node.exe). LLM est budget (`budget_limit_usd`). Même forme, substance différente. |
| **Competitor events** | Veto B2 (Aquaman, etc) | Partiel | Compétiteur = événement exogène défavorable. Veto = décision endogène de blocage. Même effet (force un recalibrage) mais pas même cause. |
| **PMI macrocyclique** | Cadence 12WY | **Non** | CEO-Bench a un cycle macro 548j qui module les sorties. Notre cadence 12WY est une décision de boucle, pas un input exogène. Substitut possible : marquer l'horodatage saison. |
| **20 ResearchTiers (jusqu'à $25M)** | Profondeur d'analyse par agent | **Non** | Le banc a un trade-off cash/durée/qualité_boost ; nous avons un trade-off temps/quota/qualité. La profondeur se mesure en tokens, pas en dollars. |
| **Model tier (cost vs quality)** | Choix de sous-agent (`haiku`, `sonnet`, `opus`) | **Oui** | Même trade-off. Substitut : `ANTHROPIC_SMALL_FAST_MODEL`. |

# Ce qui ne se transpose PAS

1. **L'horizon fini**. CEO-Bench s'arrête à 500j. Notre boucle n'a pas
   d'horizon — survivre n'a pas de définition. Substitut proposé : la
   notion de **« cycle de vie d'un projet »** = horizon naturel.

2. **Le cash simulé**. Le cash CEO-Bench est fermé. Notre équivalent est
   ouvert. Mesurer le « cash Business OS » n'a pas de sens sauf à
   inventorier la valeur des livrables — mais leur valeur n'est pas
   chiffrable sans marché.

3. **Le banc « agent unique »**. CEO-Bench teste un agent. Nous testons
   un système. La métrique de décision d'un système n'est pas la somme
   des décisions de ses agents.

4. **La concurrence exogène**. CEO-Bench a un competitor LLM-driven
   scripté. Nous n'avons pas d'adversaire — nous avons des veto (décisions
   endogènes, pas événements).

# Ce qui se transpose bien

1. **Discovery levels** : coût de réduction du bruit d'information.
2. **Capacity tiers** : coût opérationnel par tour. Notre plafond node en
   est une instance.
3. **Model tiers** : trade-off coût-qualité. Substitut : choix du
   sous-agent CC.
4. **Best run sur N seeds** : moyenne des N derniers tours d'un agent.
   Substitut propre si on garde la discipline seed.
5. **Plans conditionnels** : déjà formalisés côté B1 dans
   `b1-mandate-acceptance-check.md`. Substitut propre.

# Le gabarit proposé

Pour qu'une décision B1/B2/B3 soit **évaluable à la CEO-Bench**, il faut :

1. **Cash de départ** = nombre de concepts posés jusqu'ici par l'étage.
2. **Cash final** = nombre de concepts retenus dans un Ownerbook après
   12WY.
3. **Action** = un concept posé (pas un fichier créé — beaucoup sont
   triviaux).
4. **Survived** = l'étage n'a pas gelé (HALTED) sur 12WY.
5. **BANKRUPTED** = l'étage a HALTED au moins un projet critique avant
   la fin de 12WY.

Avec ces substitutions, **chaque étage devient un agent CEO-Bench-like**.
Trois seeds (trois démarrages de boucle à graines différentes) suffiraient
à calculer un best-run agrégé.

# Ce qui manque dans ce gabarit

- **Pas de currency de discovery**. CEO-Bench paye pour réduire le bruit.
  Nous n'avons pas de coût de recherche — la KB est locale. **Absence
  notable** : on ne mesure pas le coût de l'ignorance.
- **Pas de concurrence**. Nous n'avons pas de competitor LLM ; nous
  avons des veto (décisions). Effet de bord : nos agents B1/B2/B3 sont
  plus prévisibles — donc moins intéressants à benchmarker.
- **Pas de macro-PMI**. Notre cadence est endogène (12WY). Substitut
  possible : un seasonality marker horodaté, sans effet mesurable
  actuel.

# Limites de ce mapping

- Le mapping suppose que **chaque décision Business OS a un effet
  mesurable**. C'est vrai pour les décisions sur livrables (mandat
  accepté / refusé), faux pour les décisions de gouvernance (veto).
- Le mapping suppose que **les seuils de faillite sont comparables**. Or
  CEO-Bench mesure du cash, Business OS mesure des statuts de projet
  (HALTED ≠ bankrupt).
- Le mapping n'a **pas été testé contre un cas réel**. C'est un gabarit,
  pas une mesure.

# Anti-pattern

Ne PAS traiter CEO-Bench comme un classement de capacité. **Un agent
peut survivre en brûlant dix fois plus** (Kimi K3 à $22M vs Opus à
$2.4M). Ce qui compte : le ratio coût de survie / outcome utile. En
Business OS : le ratio coût LLM par concept retenu dans un Ownerbook.