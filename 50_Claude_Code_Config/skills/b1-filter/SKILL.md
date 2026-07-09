---
name: b1-filter
description: Délègue le B1-filter (classification des guides Geordi contre la bijection ADR-L2-BDLD-MAP-001) au modèle M3 — déterministe d'abord (script E1, zéro token), agents M3 seulement pour le résidu (E2 orphelins). Use when A0 says "b1-filter", "b1 filter", "classifie les guides", "LD mapping", "frontmatter guides", "sweep geordi", or when /youtube-to-guide flags UNFILTERED guides. Modes - audit / fix / classify.
---

# /b1-filter — Le filtre B1 mécanisé (PRD-B1-FILTER-M3-001)

> **Doctrine** : une bijection est un lookup, pas un jugement. Le script fait 90 % du travail à coût zéro ;
> les agents M3 (modèle par défaut de la session CC = MiniMax-M3) ne classifient QUE les orphelins.
> Sisters : `ADR-L2-BDLD-MAP-001` (table de vérité §D3) · `PRD-B1-FILTER-M3-001` · `/youtube-to-guide` §6.

## Périmètre (STRICT)

- Racine : `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\`
- Le script ignore `_TRASH*` et `_INDEX.md`. **Jamais** de mutation hors de cette racine, jamais un RATIFIED.
- Patch additif uniquement : on corrige/ajoute des champs frontmatter, on ne supprime rien.

## Mode 1 — `audit` (défaut, zéro mutation)

```bash
PYTHONIOENCODING=utf-8 "C:/Python314/python.exe" \
  "C:/Users/amado/.claude/skills/b1-filter/scripts/b1_filter_sweep.py" --audit
```

Rapport : `ok / violations / no_frontmatter / orphans_E2`. Ajouter `--json` pour la sortie machine.
**Toujours auditer avant de fixer** (D1) — coller le rapport dans la réponse.

## Mode 2 — `fix` (corrections déterministes E1)

```bash
PYTHONIOENCODING=utf-8 "C:/Python314/python.exe" \
  "C:/Users/amado/.claude/skills/b1-filter/scripts/b1_filter_sweep.py" --fix
```

Corrige `ld:` / `b2_owner:` d'après le dossier parent (bijection D3), ajoute `sister_b1: jerry-prime`
si absent (on ne touche pas un variant Summers déjà choisi), crée un frontmatter minimal si absent.
**Preuve d'idempotence obligatoire** : re-lancer `--audit` après — violations doit être 0, et un 2e `--fix`
doit rapporter `unchanged` partout.

## Mode 3 — `classify` (résidu E2 → agents M3)

Pour chaque fichier `orphans_E2` du rapport JSON, lancer UN agent (Agent tool, prompt court, **ne pas
surclasser le modèle** — l'agent hérite du modèle de session ; si la session tourne sur un modèle cher,
passer `model: haiku` ou dispatcher vers un harness M3) :

```
Lis UNIQUEMENT le frontmatter + les 40 premières lignes de <path>.
Classifie dans EXACTEMENT un domaine : 01_Product | 02_Ops | 03_IT | 04_Finance |
05_Legal | 06_Sales | 07_Growth | 08_People.
Réponds en JSON strict: {"domain": "0X_Name", "b1_reason": "<1 ligne>"}
En cas de doute réel entre 2 domaines, choisis celui du GOULOT business (pas du sujet de surface)
— ex. une vidéo outil-IA dont la leçon est le pricing → 04_Finance, pas 03_IT.
```

Puis appliquer au fichier le bloc du domaine choisi (mêmes champs que le mode fix) + `b1_reason:`.
Batch : paralléliser par groupes ≤ 8 agents ; chaque agent = 1 fichier, jamais le dossier entier
(règle contexte : max 1 fichier > 50 lignes par agent).

## Les 3 `_INDEX.md` dérivés (correction manuelle gated, D1 2026-07-06)

`02_Ops` (dit LD02→canon **LD01_Book**) · `06_Sales` (dit LD01→canon **LD05_Stamets**) ·
`07_Growth` (dit LD07→canon **LD08_Georgiou**). Correction = ⚡ÉVOLUTION append dans l'index
(nouvelle ligne d'amendement), PAS une réécriture de l'historique. Le script ne touche pas les
`_INDEX.md` par design — c'est un acte éditorial, pas mécanique.

## Boucle fermée (où ça s'insère)

1. **À la source** : `/youtube-to-guide` §6 exige le bloc `b1_filter` à la naissance (la table est dans le §6).
2. **Rattrapage** : ce skill en on-demand, ou pioché par le worker WF1 (backlog §2b) — 1 sweep = 1 itération.
3. **Interdit** : cron auto sans A0 GO (ADR-SOBER-002 Posture C).

## Definition of Done

- [ ] Rapport audit AVANT collé (D1)
- [ ] `--fix` exécuté + re-audit = 0 violation (idempotence prouvée par le 2e run)
- [ ] Orphelins E2 classifiés avec `b1_reason:` (ou listés `blocked-<slug>` si illisibles)
- [ ] 1 ligne worklog `[b1-filter]` avec les compteurs
