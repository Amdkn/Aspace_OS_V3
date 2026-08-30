---
type: Bundle index
title: 80_Agent-OS — la couche d'observabilité et de supervision
description: Ce qui vient APRÈS le triptyque de migration V3 et après la mémoire OKF/OpenWiki : regarder l'état réel du système. Fusion de 80_Front-Office (pages de revue) et 90_Back-Office (schéma de cadence), plus le bureau qui les rend.
tags: [agent-os, observabilite, supervision, revue, cadence, sql, dashboards, bureau]
generated: { by: claude-opus-5, at: 2026-08-29T22:45:00Z }
verified:
  - { by: claude-opus-5, at: 2026-08-29T22:45:00Z }
sources:
  - id: front-office
    resource: "80_Front-Office/ (fusionné ici le 2026-08-29)"
    title: Pages de revue HTML et leur générateur
    last_modified: 2026-08-20
  - id: back-office
    resource: "90_Back-Office/ (fusionné ici le 2026-08-29)"
    title: Schéma SQL de la cadence et diagrammes Mermaid
    last_modified: 2026-08-20
  - id: bureau
    resource: "C:/Users/amado/agent-os/desktop — Vite + React, port 5555"
    title: Le bureau Agent OS, ses apps et son API de corpus
    last_modified: 2026-08-29
okf_version: "0.2"
---

# Sa place dans la chaîne

```
   sources  ──►  TRIPTYQUE DE MIGRATION V3  ──►  mémoire  ──►  OBSERVABILITÉ
                 ┌──────────────────────┐        ┌──────┐      ┌───────────┐
                 │ 1 distillation RDF   │        │ OKF  │      │ 80_Agent- │
                 │ 2 implémentation     │        │ Open │      │    OS     │
                 │ 3 ontologie          │        │ Wiki │      │  (ici)    │
                 └──────────────────────┘        └──────┘      └───────────┘
                  la porte d'argent               ce qui est     ce qu'on en voit
```

**Rien n'entre en V3 sans les trois filtres** (`scripts/porte_argent.py`). Une
fois entré et consigné en OKF, il faut encore pouvoir le **regarder** : c'est
cet étage. Il ne produit pas de connaissance, il en rend l'état visible.

Cette distinction est la raison de la fusion. `80_Front-Office` rendait les
pages, `90_Back-Office` tenait le schéma qui les alimente : deux moitiés d'une
même fonction, séparées par un numéro d'étage qui ne correspondait à aucune
frontière réelle.

# Files

- [index.md](index.md) — ce fichier.

# Directories

- [tableaux](tableaux/) — les pages de revue et leur générateur. Une page HTML
  autonome par vague, ouvrable depuis `file://`. C'est la forme **rapide** de la
  revue, à côté du podcast NotebookLM qui en est la forme lente. `generer.py`
  les produit ; `reviews/` porte celles déjà générées.
- [donnees](donnees/) — la cadence en relations. `schema/01_cadence.sql` dit
  l'**emboîtement** et le **compte** (vague, sprint, scrum, rock), ce que le RDF
  dit mal. `mermaid/` porte les diagrammes de cadence et d'escalade.

# Le bureau

L'interface vit hors du dépôt, dans `C:/Users/amado/agent-os/desktop` — un
projet Vite/React avec ses propres dépendances. **Elle n'est pas déplacée ici**
parce qu'un `node_modules` et un serveur de développement n'ont rien à faire
dans un corpus de connaissance ; le dépôt décrit, il n'exécute pas.

| | |
|---|---|
| Adresse | `http://127.0.0.1:5555` |
| Lanceur | `agent-os/desktop/lancer_agent_os.cmd` + raccourci Bureau |
| API du corpus | `tools/corpus-api.ts` — lecture seule, bornée à la racine V3 |

Apps installées au 2026-08-29 : **Observateurs**, **Mémoires**, **Cadre
externe**, **Corpus** (arborescence et compteurs vivants du corpus V3),
**Coach OS** (local et en ligne), **Life OS 2026** (local et en ligne).

# Comment vérifier que cet étage dit vrai

```bash
curl -s http://127.0.0.1:5555/api/corpus/mesures
```

Les compteurs sont lus **à chaud** sur le disque, jamais figés dans le code :
une mesure écrite en dur vieillit et ment. Si le nombre affiché diffère d'un
`grep` sur le corpus, c'est l'API qu'il faut corriger, pas le corpus.
