---
source: A0 Amadeus (jumeau numérique)
date: 2026-06-30
type: doctrine
domain: L0
tags: [obsolete, doctrine, current-session, session-data, no-hard-delete, ratify]
---

# Obsolescence de la "Doctrine Current Session" — 2026-06-30

**Statut** : Ratifié par A0 (jumeau numérique). Doctrine annulée, artefacts neutralisés.

## Contexte

Le 2026-06-06, un agent a écrit dans `~/.claude/CLAUDE.md` une "Doctrine Current Session" décrivant :
- Un stockage des sessions dans `~/.claude/session-data/`
- Un alias `session-aliases.json` + un hook PowerShell pour les résoudre
- Un move de 30 sessions vers `session-data/_TRASH/2026-06-06_cleanup/`

**Le modèle mental était faux**. Claude Code runtime ne stocke JAMAIS les sessions dans `session-data/`. Il les range nativement dans `~/.claude/projects/<encoded-path>/<UUID>.jsonl`. Le `session-data/` n'a jamais été un chemin légitime.

## Symptôme rapporté par A0 le 2026-06-30

Sidebar Claude Code affiche "No sessions yet" alors que 28 sessions `.jsonl` sont bien présentes dans `projects/C--Users-amado/`.

## Cause racine vérifiée (D1)

| Fait vérifié | Preuve |
|---|---|
| 30 juin 03:08 — `.last-cleanup` modifié | timestamp fichier |
| Aucun script A'Space n'écrit dans `session-data/` | grep `session-data` dans `bin/` + `hooks/` = no match |
| `session-data/` ne contient QUE `_TRASH/` | `ls session-data/` |
| 28 sessions vivantes dans `projects/C--Users-amado/` | `ls projects/C--Users-amado/*.jsonl \| wc -l` = 28 |
| `.last-cleanup` = artefact Claude Code runtime, pas custom | timestamp coïncide avec session lock `ide/23697.lock` et `sessions/19624.json` |

## Action prise (2026-06-30)

Déplacement dans `_TRASH_2026-06-30_obsolete_current_session_doctrine/` (doctrine no-hard-delete respectée) :

```
session-aliases.json                                       → _TRASH/
bin/session-start-current.ps1                              → _TRASH/
session-data/_TRASH/2026-06-06_cleanup/ (30 .jsonl)        → _TRASH/false-doctrine-30-sessions/
session-data/_TRASH/                                       → supprimé (vide)
session-data/                                              → supprimé (vide)
```

## Amendement CLAUDE.md

Section "🎯 Doctrine Current Session" remplacée par "🪦 ~~Doctrine Current Session~~ — OBSOLÈTE" avec pointeur vers ce handoff.

## Hook SessionStart dans settings.json

Le hook pointe toujours vers `bin/session-start-current.ps1` qui n'existe plus. Exit silencieux au prochain démarrage (le script utilisait `$ErrorActionPreference = 'SilentlyContinue'`). **Neutralisation optionnelle** dans une PR séparée si A0 veut nettoyer `settings.json` aussi.

## Sessions vivantes — où elles sont

`~/.claude/projects/C--Users-amado/` contient 28 fichiers `.jsonl` correspondant à des sessions utilisables. Sidebar "No sessions yet" = cache UI. Reload Claude Code pour rescanner.

## Leçon (ADR-META-001 D6 root cause)

Avant d'écrire une "doctrine" sur le comportement d'un outil externe (Claude Code, Supabase, Vercel…), **vérifier le comportement réel** au lieu d'imposer un modèle mental. La doctrine du 6 juin ne s'appuyait sur aucune preuve vérifiée du runtime — juste sur une hypothèse fausse. Coût réel : 3 semaines de désalignement A0 ↔ agent avant détection.