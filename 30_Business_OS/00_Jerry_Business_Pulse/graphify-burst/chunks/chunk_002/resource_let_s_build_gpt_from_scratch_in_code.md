---
id: let_s_build_gpt_from_scratch_in_code
title: "Let's build GPT: from scratch, in code, spelled out."
channel: "Andrej Karpathy"
category: "AI"
serendipity_score: 9
date_extracted: 2026-05-24
type: resource
tags: [#youtube, #rag, #ai]
---

# Let's build GPT: from scratch, in code, spelled out.

```markdown
# Fiche de Connaissance — GPT from Scratch

**Source** : [Let's build GPT: from scratch, in code, spelled out](https://www.youtube.com/watch?v=kCc8FmEb1nY)
**Auteur** : Andrej Karpathy
**Chaîne** : Andrej Karpathy
**Catégorie** : AI / LLM / Education

---

## 1. Concepts Clés

| Concept | Définition |
|---|---|
| **Transformer** | Architecture de réseau de neurones basée sur l'attention, fondement du GPT |
| **Matrice de poids (Weight Matrices)** | Paramètres appris formant les couches linéaires du modèle |
| **Multi-Head Attention** | Mécanisme d'attention exécuté en parallèle sur plusieurs "têtes", permettant au modèle de capturer différents types de relations |
| **Self-Attention** | Mécanisme où chaque token s'évalue par rapport à tous les autres tokens de la séquence |
| **Tokenisation** | Conversion du texte en séquences d'entiers (vocabulaire) |
| **Embedding** | Représentation vectorielle dense des tokens |
| **Softmax** | Fonction de normalisation exponentielle pour produire des distributions de probabilité |
| **Language Modeling** | Tâche de prédiction du prochain token conditionné par les tokens précédents |
| **Autoregressive Generation** | Génération séquentielle token par token, chaque token dépendant des précédents |

---

## 2. Entités & Outils

| Catégorie | Élément |
|---|---|
| **Langage** | Python |
| **Framework** | PyTorch |
| **Dataset** | Tiny Shakespeare (Shakespeare complet en texte brut, ~1Mo) |
| **Bibliothèque** | `torch`, `torch.nn`, `torch.nn.functional` |
| **Figure** | Andrej Karpathy (fondateur DeepMind AI, ex-Stanford, Ng's AI Lab) |
| **Concept math** | Multiplication matricielle, Softmax, LayerNorm |

---

## 3. Synthèse Pratique

Karpathy décompose la construction d'un GPT minimal en **6 blocs** successifs :

```
1. Bigram Language Model     → Base : prédire next token avec matrice d'embedding
2. + Positional Encoding      → Ajouter l'ordre des tokens
3. + Multi-Head Attention     → Self-attention parallèle (multi-head)
4. + Feed-Forward Layer       → Réseau linéaire après l'attention
5. + Decoder Blocks empilés   → Répéter (stacks de Transformer blocks)
6. + Sampling & Generation    → Autoregressive decoding (greedy ou softmax sampling)
```

**Architecture minimale (nanoGPT-like)** :
- Vocabulaire : tokens du texte
- Couches : multi-head self-attention + feed-forward + residual connections + LayerNorm
- Entraînement : cross-entropy loss sur `torch.no_grad()` pour l'inférence
- Génération : boucle `for` autoregressive avec `torch.argmax` ou sampling

**Résultat attendu** : un modèle capable de générer du texte shakespearien plausible.

---

## 4. Actionnabilité (D.E.A.L)

### D — Définir
- **SOP entrainement LLM interne** : implémenter un pipeline d'entraînement minimal reproductible (data loading → tokenisation → batch → training loop → inference) à partir du nanoGPT de Karpathy
- **Cron** : déclenchement d'un fine-tune周期 sur données internes (e.g., logs, documentation) avec le même pattern

### E — Éliminer
- Supprimer la dépendance à des APIs tierces pour les tests de génération de texte sur données sensibles
- Retirer les configs LLM surdimensionnées (GPT-4, Claude) pour les tâches simples de génération structurée substituables par un nanoGPT fine-tuné

### A — Automatiser
- **Agent background** : fine-tune silencieux d'un nanoGPT sur le corpus interne avec alerting sur convergence (loss stagnation)
- **Agent de génération** : wrapper Python servant des requêtes de génération de texte sans appeler d'API externe, exécutable en tâche de fond sur A'Space OS
- **Pipeline CI** : validation que le modèle généré passe des assertions de cohérence (longueur, charset, format)

### L — Libérer
- **Autonomie** : ne plus dépendre d'OpenAI/Anthropic pour des cas d'usage délimités (résumés internes, classification simple, génération de templates)
- **Souveraineté données** : entraînement sur données entièrement locales, zéro fuite vers des tiers
- **Réduction de coût** : inférence locale sur CPU (modèle nano) pour les usages non-critiques sans coût par token
- **Compréhension profonde** : l'implémentation from scratch donne la capacité de **debugger**, **modder** et **optimiser** le modèle — impossible avec une API noire

---

## 5. Ressources

- **Code source** du nanoGPT : `github.com/karpathy/nanoGPT`
- **Playlist** des vidéos "Zero to Hero" de Karpathy
- **Dataset TinyShakespeare** : `raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt`

---

> **Tag OS** : `#llm #from-scratch #pytorch #local-ai #nanoGPT #fine-tune`
> **Prochaine action recommandée** : Cloner nanoGPT, exécuter `train.py` sur TinyShakespeare, puis fine-tuner sur un corpus interne pertinent.
```


## 🧿 Jonctions Transverses (Double-Way Links)

### Business Pulse (Jerry L2)
- [[02_Areas_Spock/IT|Spock Domain — IT]]

### Roue de la Vie (Discovery L1)
- [[02_Areas_Spock/Career|Life Wheel — Career]]

### Fondations A'Space OS
- [[03_Resources_Geordi/A3_Geordi_Resources_Spec|Geordi Resources Spec]]
- [[00_Index/index_youtube_rag|YouTube RAG Hub]]


---
*Généré automatiquement par l'Orchestrateur Symphony A'Space OS*
