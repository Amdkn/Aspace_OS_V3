---
type: Concept
title: DOX — AGENTS.md hiérarchique comme contrat de travail
description: Framework d'AGENTS.md hiérarchique qui force l'agent à lire la chaîne racine → feuille avant toute opération. Hiérarchie immuable : Root > Child > Leaf.
tags: [tech, dox, agents-md, gouvernance]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: dox-fwk
    resource: 05_From_V2_Domains/10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery_dox/AGENTS.md
    title: DOX framework (Core Contract)
    last_modified: 2026-01-01
  - id: dox-ratification
    resource: 05_From_V2_Domains/10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/AGENTS.md
    title: DOX root work contract
    last_modified: 2026-06-10
okf_version: "0.2"
---

**DOX** (DOX = tiny AGENTS.md framework from Agent Zero) impose une **hiérarchie immuable** d'`AGENTS.md` que tout agent doit lire avant d'éditer quoi que ce soit.

## Core Contract

```
1. AGENTS.md files = binding work contracts for their subtrees
2. Work products / source materials / instructions / records / assets / durable docs
   must stay understandable from the nearest applicable AGENTS.md + every parent above
```

## Read Before Editing

L'agent **doit** lire dans l'ordre :
1. **Root AGENTS.md** du dépôt (workdir-level).
2. Identifier chaque fichier ou dossier qu'il prévoit de toucher.
3. Walk root → leaf, lire **chaque AGENTS.md** sur le chemin.
4. Si un parent AGENTS.md liste un enfant dont le scope contient le path, lire l'enfant et continuer.
5. **Nearest AGENTS.md = local contract + parent docs for repo-wide rules**.
6. **En cas de conflit** : le doc le plus proche contrôle les détails locaux, mais aucun child ne peut affaiblir DOX.

## Update After Editing

Chaque changement substantiel impose un **DOX pass** avant que la tâche soit close :
- changement de purpose / scope / ownership / responsibilities → AGENTS.md du plus proche owner.
- changement de structure durable / contrats / workflows / règles d'opération → idem.
- changement de user preferences durables → AGENTS.md du plus proche parent ou child.
- création / suppression / déplacement d'AGENTS.md → maj des indexes parents.

## Hiérarchie canonique appliquée à A'Space

```
ASpace_OS_V2/AGENTS.md
└── 10_Tech_OS/
    ├── 11_Infra_13th_Doctor/06_MCP_Mastery/AGENTS.md       (root MCP)
    │   ├── 01_hostinger/AGENTS.md                          (leaf DNS)
    │   ├── 02_github/AGENTS.md                             (leaf repos)
    │   ├── 03_dokploy/AGENTS.md                            (leaf VPS deploy)
    │   ├── 04_vercel/AGENTS.md                             (leaf frontend)
    │   ├── 05_supabase/AGENTS.md                           (leaf DB)
    │   └── 06_graphify/AGENTS.md                           (leaf knowledge graph)
```

## Style DOX

- Section order : Purpose / Ownership / Local Contracts / Work Guidance / Verification / Child DOX Index.
- Direct bullets, noms explicites, pas de duplication entre parents / enfants.
- Suppression des notes caduques — pas de diary entries.
- Trim des évidences.

## Pourquoi ça marche

L'agent qui touche un fichier sans avoir lu la chaîne DOX passe à côté de :
- Les contrats locaux (formats, hooks, scopes interdits).
- Les work guidance (workarounds documentés, anti-patterns connus).
- Les denylists (leaves qui interdisent explicitement certaines opérations).

C'est l'**anti-panique par lecture obligatoire** : la doc elle-même est un garde-fou, pas un souvenir post-hoc.

Voir aussi : [[mcp-doctrine-six]], [[vault-tier-pattern]], [[axiomes-antifragilite-k1-k4]].