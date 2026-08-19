---
type: Tradeoff
title: RecursiveMAS — ce que le dépôt démontre vs ce qu'il annonce
description: Synthèse technique arXiv 2604.25917 et dépôt RecursiveMAS : gains chiffrés, protocole d'entraînement Inner-Outer Loop, et la contrepartie structurale (opacité) qui rendrait l'adoption regrettable dans 6 mois.
tags: [recursivemas, latent-space, multi-agent, tradeoff, opacity]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: minimax-m3, at: 2026-08-19T00:00:00Z }
sources:
  - id: recursivemas-arxiv
    resource: "https://arxiv.org/abs/2604.25917"
    title: "Recursive Multi-Agent Systems (Zou et al., 28 avr. 2026 v1, 13 juil. 2026 v2)"
    last_modified: 2026-08-19
  - id: recursivemas-repo
    resource: "https://github.com/RecursiveMAS/RecursiveMAS"
    title: "Dépôt GitHub — README, inference/, train/"
    last_modified: 2026-08-19
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine** sur les gains arXiv
> et la structure du dépôt. **Marqué extrapolation** sur la partie
> « contrepartie opérationnelle ».

# Ce que le papier démontre

Titre : *Recursive Multi-Agent Systems* (Zou J., Pan R., Qiu R., Lu P.,
Diao S., Jiang J., Tong H., Zhang T., Buehler M. J., He J., Zou J.).
arXiv:2604.25917, v1 = 28 avril 2026, v2 = 13 juillet 2026.

**Gains agrégés revendiqués (papier)** :

- Amélioration accuracy moyenne : **+8,3 %**
- Speedup end-to-end : **1,2× à 2,4×**
- Réduction tokens : **34,6 % à 75,6 %**

**Banc d'essai** :

- 9 benchmarks : `math500`, `gpqa`, `medqa`, `mbppplus`, `aime25`,
  `aime26`, `livecodebench`, `bamboogle`, `hotpotqa`.
- 4 styles de collaboration : Sequential, Mixture, Distillation,
  Deliberation.
- Single-run par (style × config), publiés comme **référence** — le
  README précise que les checkpoints HF « are for quick, plug-and-play
  exploration … but NOT a single replacement for the task-specific
  training setups ».

**Scores publiés par configuration** (extraits, single-run) :

- Sequential-Scaled : math500=88.5, gpqa=65.7, medqa=82.7, aime25=86.7,
  aime26=90.0, livecodebench=42.1
- Sequential-Light : math500=78.0, gpqa=32.3, medqa=32.0, mbppplus=37.3,
  aime25=33.3, aime26=20.0
- Distillation : gpqa=68.7, medqa=82.7, mbppplus=72.6, aime26=86.7,
  livecodebench=43.0
- Mixture : gpqa=42.7, medqa=61.3, aime26=46.7, livecodebench=22.8
- Deliberation : gpqa=65.3, aime26=90.0, bamboogle=54.4, hotpotqa=43.6

⚠️ **Le claim "73% → 87%" mentionné dans le brief n'apparaît pas dans
le README.** C'est une **reformulation libre** — la séquence 73 → 87 ne
correspond à aucune transition (style, benchmark) publiée. À écarter
comme reformulation non sourcée.

# Architecture technique

- **RecursiveLink** : module léger qui permet aux agents d'échanger,
  raffiner, faire évoluer des états latents entre les rondes de
  récursion. **Architecture interne non documentée** dans le README
  (renvoyée au papier).
- **Inner-Outer Loop training** :
  - *Inner loop* : warm-up au niveau modèle pour chaque agent.
  - *Outer loop* : entraînement du RecursiveLink au niveau système.
- **Code publié** : `inference/run.py`, `inference/dataset/`,
  `inference/inference_utils/`, `train/train_inner.py`,
  `train/train_outer.py`, `train/data/`, `train/outer/`. Données
  d'entraînement sur HF (`RecursiveMAS/*`).

# Ce qui n'est PAS démontré publiquement

- Mécanisme exact de la traduction latent ↔ texte. Le README dit
  « exchange, refine, and evolve latent states across recursion rounds »
  sans préciser le protocole.
- Hyperparamètres des inner/outer loops (renvoyés à `train/README.md`).
- Coût d'entraînement total (GPU-heures, dollars). Aucune ligne sur le
  papier dans ce qu'on a lu.
- Stabilité des gains au-delà des 9 benchmarks (pas de test sur
  tâches de gouvernance, de rédaction, de revue de code).

# La contrepartie — l'opacité

Un échange en vecteurs latents est **opaque à la lecture humaine**. Pas
de log textuel, pas de citation, pas de référence. Pour notre poste :

- **Toute décision d'agent doit pouvoir être tracée**. Le mode Fable
  exige « chaque affirmation doit pouvoir être ramenée à un fichier
  précis ». Un canal latent ne le permet pas — la sortie est un
  vecteur, pas un texte.
- **Toute revue de gatekeeper (Rick-Morty) doit lire un livrable**.
  Un livrable latent n'est pas lisible.
- **Toute contradiction doit être nommée**. Une contradiction entre
  deux tours latents n'a pas de surface textuelle où s'imprimer.
- **Le canon OKF** est conçu pour des humains et des machines qui lisent
  du texte. Le format `[[wikilink]]` exige des concepts nommés en clair.

# Où ce compromis est acceptable (usage partiel)

Un usage **hybride** est concevable :

1. **Latent intra-escouade** : entre agents d'une même escouade (B1
   seul, B2 seul, B3 seul), là où l'opacité ne franchit pas la frontière
   humaine. Le latent économise des tokens (34-75 % selon papier), le
   texte reste aux jonctions (B1↔B2, B2↔B3, Agent↔Humain).
2. **Texte aux frontières** : tout ce qui sort d'une escouade vers une
   autre, ou vers un humain, redevient texte. C'est le seul point où la
   relecture est possible.
3. **Checkpoints texte** : on exige du système un export texte
   périodique (par tour, par décision majeure) qui rejoue l'état
   latent en langage naturel. Coût supplémentaire, mais sans ça, plus
   d'audit.

# Où ce compromis est inacceptable (usage total)

- **Substitut au texte B1↔B2**. Le `b1-mandate-acceptance-check.md`
  exige un format YAML lisible par les capitaines B2. Si le mandat
  sort en vecteur latent, l'acceptance check ne peut pas exister.
- **Substitut aux concepts OKF**. Les concepts doivent être en clair
  pour être indexés (`70_Onthologies/pulse/<étage>/`). Un concept
  latent n'est pas un concept au sens OKF.
- **Substitut aux rapports de tour**. `RAPPORT_<étage>.md` doit être
  lisible. Un rapport latent n'a pas de lecteur.

# Ce qui rendrait l'adoption regrettable dans 6 mois

1. **Dette d'audit**. Six mois de logs latents = six mois de décisions
   intraçables. Si un incident survient (mauvais livrable accepté),
   personne ne peut reconstruire la chaîne de décision.
2. **Dette de revue**. Rick-Morty et les capitaines B2 lisent du texte.
   Un système latent les rend aveugles. La revue devient « tout passe »
   ou « rien ne passe » — pas une décision éclairée.
3. **Vendor lock-in progressif**. Les checkpoints HF sont « for
   plug-and-play exploration, NOT a single replacement for task-specific
   training setups ». Si on s'habitue à un échange latent, on perd la
   capacité de migrer vers un autre système sans ré-entraîner.
4. **Incompatibilité avec le canon**. Le canon OKF est notre mémoire.
   Y intégrer du latent = créer une mémoire parallèle qui ne se
   synchronise pas avec l'autre.

# Décision de fait

**Ne pas adopter RecursiveMAS tel quel.** Le gain numérique existe
(+8,3 % accuracy, 1,2-2,4× speedup, 34-75 % tokens) mais la contrepartie
d'opacité est incompatible avec le mode Fable et le canon OKF. Si un
usage partiel est tenté, ce sera intra-escouade seulement, avec export
texte obligatoire aux frontières — et cela reste à prototyper.

# Citation

Zou J. et al. *Recursive Multi-Agent Systems*. arXiv:2604.25917, 2026.
Code : github.com/RecursiveMAS/RecursiveMAS.