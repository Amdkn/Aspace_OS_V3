---
type: Quickstart
title: Démarrage rapide — chercher et écrire dans la mémoire
description: Le geste de lecture au début d'une tâche, le geste d'écriture à la fin, et les pièges de chemin déjà payés.
tags: [okf, memoire, quickstart]
generated: { by: claude-opus-5, at: 2026-08-17T15:10:00Z }
verified:
  - { by: human:amdkn, at: 2026-08-17T15:05:00Z }
sources:
  - id: canon-local
    resource: "~/.claude/CLAUDE.md — obligations de session"
    title: Canon du poste
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Chercher — au début d'une tâche

Le point d'entrée est [`index.md`](index.md), puis le sous-bundle qui
correspond au sujet. Quand le sujet est flou, une recherche plein texte sur les
`description:` du frontmatter rend mieux qu'un parcours d'arborescence :

```bash
grep -rn "^description:" "C:/Users/amado/ASpace_OS_V3/40_Memory_Wiki_OKF"
```

Avant de conclure qu'une connaissance manque, vérifier les deux autres
mémoires du poste, qui ne se recouvrent pas :

| Mémoire | Ce qu'elle contient |
|---|---|
| **ce bundle** | les concepts durables, avec provenance et niveau de confiance |
| `~/.claude/projects/*/memory/` | les faits courts de session, un par fichier |
| `~/.claude/CLAUDE.md` | le canon de comportement, pas les connaissances |

# Écrire — à la fin d'une tâche

1. Choisir le sous-bundle : `architecture/`, `integrations/`, `operations/`,
   `security/`.
2. Poser le fichier en `kebab-case.md`, avec le frontmatter décrit dans
   [OKF v0.2](OKF.md).
3. Renseigner `verified` **honnêtement** — c'est ce champ, et lui seul, qui
   distingue une mesure d'une supposition.
4. Ajouter la ligne correspondante dans l'`index.md` du sous-bundle.

# Trois pièges de chemin, déjà payés

**`openwiki/` n'est pas la mémoire.** C'est un clone du dépôt amont
`langchain-ai/openwiki` — l'outil qui *génère* des wikis. Il a son propre
`.git`, il est invisible depuis le statut du dépôt parent, et il ne se pousse
pas. Un concept écrit là est local à cette machine et meurt avec le disque.

**Écrire ne suffit pas à indexer.** Un fichier posé sans ligne dans l'`index.md`
de son sous-bundle existe sur le disque et n'existe pas pour le lecteur
suivant.

**`Write` ne crée pas les dossiers parents.** L'outil répond « success » sans
rien écrire quand le répertoire manque. Créer le dossier d'abord, contrôler
avec un `ls` après.

# Ce bundle est versionné

Il vit dans `Amdkn/ASpace_OS_V3` et part avec chaque push. C'est précisément la
raison de son existence : la mémoire précédente, écrite dans le clone amont, ne
partait nulle part.
