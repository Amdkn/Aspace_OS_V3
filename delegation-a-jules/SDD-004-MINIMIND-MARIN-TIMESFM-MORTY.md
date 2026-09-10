# SDD-004 : Architecture & Brainstorming — Le Modèle Fondation Souverain de Morty
## Triade MiniMind (64M) + Marin + TimesFM (CPU/NVMe Local)

* **Version :** 1.0.0-CANON
* **Date :** 2026-09-09
* **Architecte Souverain :** Amadou Kone (`amdkn`)
* **Visionnaire :** Rick Sanchez (Loi L0 — Souveraineté & Zéro Dépendance Cloud)
* **Pôle Conscience & Prédiction :** Morty (Gatekeeper A1 & Moteur Prédictif 1D/2D)
* **Standard :** OKF v0.2 / Inférence CPU Locale

---

## 1. Vision & Défi Cybernétique : Pourquoi un Modèle Fondation Local pour Morty ?

Jusqu'à présent, l'intelligence d'A'Space OS dépendait soit d'APIs cloud (Gemini, Claude), soit de règles statiques (Engram).
Si le réseau coupe, ou si les quotas sautent, **le jumeau numérique ne doit pas s'éteindre**.

**L'objectif :** Créer le **Modèle Fondation Local de Morty** capable de tourner en local sur CPU :
1. **Poids plume & Inférence instantanée :** Empreinte RAM < 150 Mo, latence < 30 ms sur CPU standard.
2. **Double Spécialisation :**
   - **Langage / Raisonnement Déterministe :** MiniMind (26M - 64M paramètres) pré-entraîné sur l'ontologie d'A'Space OS V3 via le compilateur **Marin**.
   - **Prédiction de Séries Temporelles (Chronobiologie) :** **TimesFM** (Google Research) pour modéliser les cycles 12 Week Year (12WY) et projeter les horizons **H1 à H90** de l'Ikigai et de la Discovery Wheel (LD01-LD08).

---

## 2. La Triade Technologique : Rôles & Synergies

```
                 ┌────────────────────────────────────────────────────────┐
                 │           LE GATEKEEPER PRÉDICTIF : MORTY              │
                 │      (20_Life_OS / 00_Gatekeepers_Beth_Morty)          │
                 └───────────────────────────┬────────────────────────────┘
                                             │
      ┌──────────────────────────────────────┼──────────────────────────────────────┐
      ▼                                      ▼                                      ▼
┌───────────────────────────┐  ┌───────────────────────────┐  ┌───────────────────────────┐
│     MINIMIND (64M)        │  │     MARIN COMPILER        │  │   TIMESFM (ZERO-SHOT)     │
│  Modèle Fondation Langage │  │  Pipeline de Tokenisation │  │   Prédiction de Séries    │
│  Inférence CPU Ultra-Fast │  │  & Distillation Canonique │  │   Temporelles H1-H90      │
│ (26M / 64M paramètres)    │  │  (70_Ontho + 40_OKF)      │  │ (12WY, Cycles Circadiens) │
└───────────────────────────┘  └───────────────────────────┘  └───────────────────────────┘
```

### A. MiniMind (jingyaogong/minimind) — Le Cerveau Symbolique CPU
- **Pourquoi MiniMind ?** Conçu pour être entraîné à partir de zéro en moins de 2 heures avec seulement 26M à 64M de paramètres.
- **Rôle dans A'Space OS :** Il devient le modèle SLM (Small Language Model) souverain de Morty.
- **Inférence CPU pure :** Grâce à des formats comme ONNX Runtime ou llama.cpp / GGUF, un modèle 64M quantifié en 4-bit (Q4_K_M) pèse **moins de 40 Mo** et génère plus de 60 tokens/seconde sur un processeur classique sans GPU.

### B. Marin (marin-community/marin) — La Forge de Compilation & Dataset
- **Pourquoi Marin ?** C'est un framework ultra-rapide de prétraitement, d'alignement et d'entraînement pour architectures transformers.
- **Rôle dans A'Space OS :**
  1. Extraire la mémoire certifiée (`40_Memory_Wiki_OKF/`), les triplets RDF (`70_Onthologies/`) et les 75 Actes de Gouvernance.
  2. Générer les paires d'entraînement de haute densité (Instruction Tuning déterministe).
  3. Piloter l'entraînement ou le fine-tuning de MiniMind sans perte de structure.

### C. TimesFM (google-research/timesfm) — L'Oracle des Séries Temporelles (H1-H90)
- **Pourquoi TimesFM ?** Modèle de fondation de Google Research spécialement pré-entraîné sur des milliards de points de séries temporelles pour de la prévision *zero-shot*.
- **Rôle dans A'Space OS :**
  - **Cycles 12 Week Year (12WY) :** Prédire la vitesse d'exécution, la dérive d'énergie et l'accomplissement des tactiques hebdomadaires.
  - **Horizons Ikigai (H1 à H90) :** Modéliser les 8 Domaines de Vie (LD01 à LD08) :
    * $H_1$ : Énergie et charge cognitive des prochaines 24 heures.
    * $H_7$ : Tendance de complétion du sprint hebdomadaire (River Song).
    * $H_{30}$ : Projection du cash-flow et de la jauge Business SOB (Clara / Bill).
    * $H_{90}$ : Bilan prédictif du cycle complet de 12 semaines.

---

## 3. Architecture d'Intégration Locale (Tech OS Kernel Substrat)

```
[Événements uc.db & Journal Append-Only]
                  │
                  ▼
   ┌──────────────────────────────┐
   │    TIMESFM ENGINE (CPU)      │ ────► Projections H1-H90 (Courbes & Probabilités)
   └──────────────┬───────────────┘
                  │ Vecteur d'état temporel
                  ▼
   ┌──────────────────────────────┐
   │    MINIMIND 64M (ONNX/GGUF)  │ ────► Synthèse textuelle & Arbitrage A1 Morty
   └──────────────┬───────────────┘
                  │ Décision / Alerte
                  ▼
     [Gatekeeper Beth (Veto)] ───► [Contrôleur Runtime / Antigravity TTS]
```

1. **Pipeline de Données Local :**
   Les métriques de vie (`20_Life_OS`) et les événements de `uc.db` alimentent un tableau SQLite / Pandas local.
2. **Inférence Séquentielle :**
   - TimesFM lit la fenêtre historique (ex. les 90 derniers jours).
   - TimesFM prédit les 14 prochains jours de charge cognitive et de productivité.
   - MiniMind ingère les prédictions et formule un diagnostic textuel de 2 phrases pour le briefing matinal d'Amadou Kone.
3. **Restitution Audio Instantanée :** Le texte de MiniMind est lu directement par le démon TTS local (`edge-tts`).

---

## 4. Feuille de Route d'Implémentation pour Jules & l'Équipe

1. **Phase 1 : Extraction & Dataset Marin**
   - Forger `10_Tech_OS/kernel/slm/marin_dataset_extractor.py` pour compiler les fiches OKF et les logs d'actes en tokens d'entraînement MiniMind.
2. **Phase 2 : Ingestion TimesFM Zero-Shot**
   - Créer `10_Tech_OS/kernel/timesfm/chronos_predictor.py` exploitant le checkpoint PyTorch/ONNX de TimesFM sur CPU.
   - Connecter les données de la Discovery Wheel (LD01-LD08).
3. **Phase 3 : Packaging MiniMind-Morty**
   - Entraîner le checkpoint MiniMind 26M/64M sur les invariants A'Space.
   - Exporter en format GGUF ou ONNX pour inférence à froid (< 50 Mo RAM).