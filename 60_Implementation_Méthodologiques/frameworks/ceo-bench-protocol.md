---
type: Benchmark Spec
title: CEO-Bench — ce que mesure le protocole
description: Cadence, ledger, conditions terminales, modèles publiés et chiffres exacts pour relier une trajectoire d'agent au verdict « l'agent décide bien ».
tags: [ceo-bench, benchmark, decision-quality, simulation, saas]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: minimax-m3, at: 2026-08-19T00:00:00Z }
sources:
  - id: ceobench-src-config
    resource: "https://raw.githubusercontent.com/zlab-princeton/ceobench-src/main/src/saas_bench/config.py"
    title: "config.py — constantes BenchmarkConfig (extrait vérifié)"
    last_modified: 2026-08-19
  - id: ceobench-home
    resource: "https://ceobench.com"
    title: "ceobench.com — trajectoires publiées, modèles, cash, faillites"
    last_modified: 2026-08-19
  - id: ceobench-arxiv
    resource: "https://arxiv.org/abs/2606.18543"
    title: "CEO-Bench paper (arXiv 2606.18543)"
    last_modified: 2026-08-19
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Chiffres vérifiés sur
> `config.py` brut et sur la home `ceobench.com`. Pas de citation de mémoire.

# Horizon et ledger

- **500 jours simulés** (`BenchmarkConfig.total_days = 500`).
- **Cash initial** = `1_000_000 $` (`BenchmarkConfig.initial_cash`).
- **Seed** = 42 (`BenchmarkConfig.seed`). Déterministe à seed fixée.
- **Actions comptées** : chaque action agent loggée dans le ledger chiffré
  `world.nmdb` (SQLCipher, AES-256 page-level). Le ledger contient
  « cash, subscriptions, customers, competitor events, every action the
  agent took » (citation README).
- **Budget LLM** séparé du cash de simulation : `budget_limit_usd = 50.0`
  (coût d'inférence plafond, indépendant de la trésorerie).
- **Cadence agent** : *weekly commits* dans le sandbox (README), avec des
  moyennes mesurées entre 9.86 et 16.64 tours/semaine selon le modèle.

# Conditions terminales

- **Faillite** = statut public `BANKRUPTED` sur la trajectoire. La définition
  précise (cash ≤ 0 ? impossibilité de payer une journée ?) **n'est pas
  documentée** dans la home `ceobench.com`, ni dans le README de
  `zlab-princeton/ceobench-src`. Logiquement : cash ≤ 0. **À confirmer**
  dans `docs/analyze_trajectory.md` (non accessible publiquement).
- **Fin de partie** : les 500 jours sont atteints, statut `survived`.

# Univers de décision (mesuré sur le code)

- **5 ModelTiers** : coûts de 0.0003 $/1k tokens (tier 1) à 0.030 $/1k
  tokens (tier 5) ; quality multipliers 0.60× → 1.10×.
- **8 CapacityTiers** : 50 000 → 300 000 000 capacity units, coûts 85 $
  → 75 000 $/jour.
- **5 AdChannels** (social_media, search_ads, linkedin, content_marketing,
  referral_program) avec leads-per-1000-dollars différenciés par **26
  customer groups** (S1-S3 individuels, E1-E3 enterprise, D_S01-D_S10 et
  D_E01-D_E10 discovery).
- **20 ResearchTiers** : de 166 667 $ (prompt engineering) à
  25 000 000 $ (Moonshot AGI), boosts qualité de 0.04 à 8.0, durées 12j →
  467j.
- **Concurrence** : événements aléatoires (intervalle moyen 6.858j,
  cut-off 30j tardifs) avec `competitor_feedback_u_min/max` = (0.2, 0.5)
  par défaut. Difficulté tunable.
- **Macro** : PMI cyclique 49.37 ± 8.0, période 548j, mean-reversion
  0.015/j. Plancher 30, plafond 70.
- **Churn structuré** (6 raisons : QUOTA_CHANGE, RELIABILITY_CHANGE,
  QUALITY_CHANGE, PRICE_SENSITIVITY, EXTENDED_ISSUE, INVOLUNTARY) —
  l'agent ne voit pas la raison, seulement le message LLM.
- **Contrats** : durées (1, 3, 6, 12) mois. Renouvellement 90j lead,
  churn pré-expiry 90j.

# Modèles par défaut (mesure)

| Rôle | Modèle | Provider |
|---|---|---|
| Agent principal | **gpt-5.2** | openai |
| Social posts | claude-haiku-4-5 | anthropic |
| Enterprise | claude-sonnet-4-5 | anthropic |

`agent_llm_reasoning_effort = "low"` par défaut.

# Trajectoires publiées vérifiées (ceobench.com)

Données verbatim depuis la page d'accueil publique. Chaque modèle est
 joué **3 fois** ; les chiffres agrégés incluent les faillites.

| Modèle | Best cash | Faillites | Durée moyenne | Tours/sem | Note |
|---|---|---|---|---|---|
| Kimi K3 | **22 148 357 $** | 1/3 | 386,0 ± 161,2 j | 14,81 | « highest published best-run cash » |
| Claude Opus 4.8 | 2 399 209 $ | 1/3 | 378,0 ± 172,5 j | 16,64 | best run 504j, 1 511 actions, $2.40M |
| Claude Opus 4.7 | 70 620 $ | 1/3 | — | — | « narrows much earlier, spend less, protect cash » |
| Claude Fable 5 | **12 630 078 $** | 1/3 | 461,7 ± 54,2 j | 9,86 | 88% R&D sur cible, plans « if X then Y » |
| GPT-5.6 Sol | 11 310 000 $ | 2/3 | — | — | peak 246 000 subs jour 72, descend à 0 |

**Lecture** : survivre ne dit rien du coût de la survie. Kimi K3 finit
avec ~10× plus de cash qu'Opus 4.8 — pour la même survie, Opus a brûlé
10× moins. Le banc mesure donc un **ratio cash-survie / durée / actions**,
pas un classement de capacité.

# Anti-triche

- Ledger chiffré (clé embarquée `_embedded_key`, AES-256 page-level).
- Pas d'accès direct à `world.nmdb` pour l'agent — il passe par un
  CLI sandboxé (`novamind_cli.py`, `tools.py` non documentés ici).
- « Keeping the agent from cheating » cité dans `docs/analyze_trajectory.md`
  (non vérifié — fichier non accessible publiquement).

# Ce qui n'est PAS documenté

- Liste exhaustive des actions agent (`tools.py` non lu).
- Définition textuelle de la faillite (BANKRUPTED seulement comme statut).
- Effet exact du `drift_grace_period_days = 60` sur la stratégie agent.
- Distribution des outcomes « survived with N subs » vs « survived at 0 subs »
  (un agent peut survivre en perdant tous ses clients avant le jour 504).

# Citation

Chen, H., Narasimhan, K., Liu, Z. (Princeton, 2026). « CEO-Bench »,
arXiv:2606.18543. Code: `github.com/zlab-princeton/ceobench-src`.