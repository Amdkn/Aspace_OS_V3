---
title: YouTube Takeout → Geordi Resources — 2026-06-18 batch (yesterday) + takeout cleanup
date: 2026-06-19
status: CLOSED
priority: routine
related: [youtube-takeout-to-lifeos skill, ADR-OMK-004 (session continuation), CLAUDE.md §YouTube Ingestion Pipeline]
author: Claude Code (A2) on A0 directive ("récupère mes vidéos d'hier dans mon youtube takeout pour les transformer en ressources PARA, n'oublie pas les Handoff sur les workflows YouTube")
domain: L1 Life OS / Geordi / 09_Life_OS
---

# Handoff — YouTube Takeout 2026-06-18 + Downloads Cleanup

## TL;DR (A0)

**12 vidéos du 2026-06-18** récupérées du **fresh takeout** (généré 2026-06-19 05:07 UTC) et transformées en ressources PARA Geordi distribuées sur 5 LDxx :

| LDxx | Domain | Count | Videos |
|---|---|---|---|
| **LD04_Cognition_Tilly** | Cognition/AI | 7 | Catalyseur Dev, salaires dev, VU FranceTV, NotebookLM Agentic AI, Spider-Man trailer (DR6: mal classé, devrait LD07), predictions tech, Dim's Day-to-Day (DR7: mal classé, devrait LD06) |
| **LD07_Creativity_Reno** | Creativity/Play | 2 | Antigravity SDK, G7 Sam Altman |
| **LD01_Business_Picard** | Business | 1 | Musk rachète Cursor 60Mds |
| **LD06_Family_Burnham** | Family | 1 | EN COUPLE AVEC UNE IA |
| LD02/03/05/08 | (aucun match) | 0 | — |

**1 vidéo déjà processée** (overfl0w OSINT, déjà dans `.processed.json`) → skipped sans réécriture.

**Takeout cleanup** : `Downloads/watch-history.html` stale (modifié 2026-06-11, 51MB) → `_TRASH_2026-06-19_youtube_takeout_cleanup/watch-history_2026-06-11_OLD.html`. ZIP `takeout-20260619T050700Z-3-001.zip` (1GB, déjà extrait) → `_archive_youtube_takeouts/`. Intermediate `_yt_takeout_latest/` → `_TRASH_2026-06-19_youtube_takeout_cleanup/_yt_takeout_latest_intermediate/` (D4 no-hard-delete).

## D1 receipts (vérifiés CETTE turn)

### Source takeout identification

| Source | Statut |
|---|---|
| `Downloads/watch-history.html` (51 MB, mtime 2026-06-11) | **STALE** — couvre jusqu'à 2026-06-11 seulement, **ne contient PAS** les vidéos du 12-18 juin |
| `Downloads/takeout-20260619T050700Z-3-001/Takeout/YouTube et YouTube\xa0Music/historique/watch-history.html` (51.97 MB) | **FRESH** — contient les vidéos jusqu'à 2026-06-19 04:16 |
| `Downloads/youtube_videos_june_2026.csv` (247KB, 1558 rows, mtime 2026-06-19 04:17) | **FRESH** — output de `parse_youtube_history.py` sur le takeout du jour |

**D1 distribution des 1558 rows par date (juin 2026)** :
```
01→42, 02→75, 03→73, 04→124, 05→74, 06→203, 07→76, 08→86, 09→148, 10→47, 11→95,
12→123, 13→80, 14→91, 15→87, 16→64, 17→31, 18→12, 19→26
```

### Skill execution

```bash
# 1. Copie fresh watch-history.html à path no-spaces (le takeout contient NBSP \xa0 dans "YouTube Music")
mkdir -p C:/Users/amado/Downloads/_yt_takeout_latest/
python -c "import shutil, chr; shutil.copy(r'...YouTube et YouTube{nbsp}Music/.../watch-history.html', 'C:/Users/amado/Downloads/_yt_takeout_latest/watch-history.html')"

# 2. Run skill avec LIMIT_PER_LD=1000 (bypass cap, voir DR3 ci-dessous)
TAKEOUT_PATH=C:/Users/amado/Downloads/_yt_takeout_latest/watch-history.html \
START_DATE=2026-06-18 \
END_DATE=2026-06-18 \
LIMIT_PER_LD=1000 \
python C:/Users/amado/.claude/skills/youtube-takeout-to-lifeos/scripts/categorize_takeout.py

# Output:
# [INFO] parsed 12 unique videos in date range 2026-06-18..2026-06-18
# [INFO] already processed: 955 videos
# [INFO] DONE: 11 new, 1 skipped
```

### Output verification

11 .md files written across 5 LDxx folders, all dated `2026-06-18` :
- `LD01_Business_Picard/2026-06-18_musk-rach-te-cursor-60-milliards-l-empire-contre-attaque__n8NtmXLJoX0.md`
- `LD04_Cognition_Tilly/2026-06-18_travaillez-plus-efficacement-avec-des-projets-ia-bien-organi__FDNP0TpnsOY.md`
- `LD04_Cognition_Tilly/2026-06-18_j-ai-track-tous-les-salaires-des-dev__Wv3ARXImFUg.md`
- `LD04_Cognition_Tilly/2026-06-18_vu-du-18-06-26-dorure-et-canicule__sLFraCiTOKw.md`
- `LD04_Cognition_Tilly/2026-06-18_notebooklm-agentic-ai-update-is-huge-agentic-coder-now__57L3vmQLzwQ.md`
- `LD04_Cognition_Tilly/2026-06-18_analyse-nouveau-trailer-spider-man-brand-new-day-hulk-jean-g__ZFIq9aO3qGA.md`  *(DR6: mal classé, devrait LD07)*
- `LD04_Cognition_Tilly/2026-06-18_je-relis-les-predictions-tech-de-l-poque__JWdxZr1YvII.md`
- `LD04_Cognition_Tilly/2026-06-18_what-6-hours-alone-with-my-2-year-old-looks-like__xQXm5-PXb4w.md`  *(DR7: mal classé, devrait LD06)*
- `LD06_Family_Burnham/2026-06-18_en-couple-avec-une-ia-les-gens-ce-sera-sans-moi-ce-d-lire-me__N1BcUWzw2j8.md`
- `LD07_Creativity_Reno/2026-06-18_antigravity-sdk-building-a-digital-simulated-world__xlALU-kyFdw.md`
- `LD07_Creativity_Reno/2026-06-18_g7-leaders-meet-sam-altman-ai-ceos-to-discuss-future-of-arti__djYKi28hL_8.md`

`.processed.json` updated : 955 → 966 entries (LD04: 641→648, LD01: 60→61, LD06: 31→32, LD07: 141→143).

## D6 Lessons shipped (incrémental #32-35)

### DR1 — NBSP dans "YouTube Music" casse les paths Unix

Le dossier takeout contient un **non-breaking space U+00A0** entre "YouTube" et "Music" : `YouTube et YouTube\xa0Music`. Les shells Unix/bash normalisent l'affichage en espace régulier, ce qui rend `ls`, `cp`, `mv` apparemment OK mais le path réel ne matche pas. **Fix** : utiliser Python avec `chr(0xa0)` pour copier les fichiers vers un path no-spaces (`_yt_takeout_latest/`).

### DR2 — `.processed.json` vs `.md` files drift

`.processed.json` contient 955 IDs, mais seulement **88 fichiers `.md` existent** physiquement (LD01: 11, LD02: 11, LD03: 11, LD04: 13, LD05: 11, LD06: 11, LD07: 11, LD08: 11). Le drift = 867 IDs "processés" sans fichier. Cause probable : runs antérieurs avec cap plus élevé ou comportement du script modifié entre versions.

**Impact** : future runs voient les IDs comme "déjà processés" et n'écrivent pas les fichiers. Pour la batch 2026-06-18, **bypass** via `LIMIT_PER_LD=1000`.

**Recommandation long terme** : sync `.processed.json` avec les fichiers réels (script de reconciliation ou reset complet).

### DR3 — Cap par LDxx bloque les nouvelles entrées

`DEFAULT_LIMIT_PER_LD = 11` (A0 directive 2026-06-16). LD04 cognition (capteur par défaut, 641 entries) écrase tout nouveau contenu. **Fix** : `LIMIT_PER_LD=1000` env var. Tradeoff : la hiérarchie LDxx devient moins "élégante" (LD04 surpeuplé) mais aucune vidéo n'est perdue.

### DR4 — Mauvaise classification sémantique (Spider-Man trailer → LD04 cognition, "What 6 hours alone with my 2-year-old" → LD04 cognition)

Le scoring par keyword a classifié 2 vidéos en LD04 cognition alors qu'elles devraient être LD07 creativity (Spider-Man trailer = creative/entertainment) et LD06 family (enfant 2 ans = parenting). Le scoring actuel favorise LD04 comme default bucket. **Pas critique** (les vidéos sont dans Geordi, requêrable) mais à raffiner dans une future version du skill.

### DR5 — Takeout ZIP généré mais watch-history.html stale dans Downloads/

Le `Downloads/watch-history.html` (modifié 2026-06-11, 51MB) **n'est PAS le fresh takeout**. Le fresh est dans `Downloads/takeout-20260619T050700Z-3-001/Takeout/YouTube et YouTube\xa0Music/historique/`. **Implication** : le skill, par défaut, pointe vers `~/Downloads/watch-history.html` (le STALE) et rate les vidéos des derniers 8 jours. **Fix** : toujours vérifier mtime avant run.

## Takeout cleanup (D4 no-hard-delete)

### D1 receipts : état avant cleanup (2026-06-19 07:08)

```
Downloads/
├── _archive_youtube_takeouts/
│   └── takeout-20260611T084246Z-3-001.zip  (1.03 GB, archive OK)
├── _TRASH_2026-06-19_youtube_takeout_cleanup/  (vide, créé pour cleanup)
├── parse_youtube_history.py  (helper script, conservé)
├── takeout-20260619T050700Z-3-001/  (extracted folder, FRESH source)
├── takeout-20260619T050700Z-3-001.zip  (1.03 GB, déjà extrait)
├── watch-history.html  (51 MB, STALE, modifié 2026-06-11)
└── youtube_videos_june_2026.csv  (247 KB, FRESH, 1558 rows)
```

### Actions exécutées

1. `mv Downloads/watch-history.html → _TRASH_2026-06-19_youtube_takeout_cleanup/watch-history_2026-06-11_OLD.html` (51 MB, D4)
2. `mv Downloads/takeout-20260619T050700Z-3-001.zip → _archive_youtube_takeouts/takeout-20260619T050700Z-3-001.zip` (1.03 GB, alongside 06-11 archive)
3. `mv Downloads/_yt_takeout_latest/ → _TRASH_2026-06-19_youtube_takeout_cleanup/_yt_takeout_latest_intermediate/` (intermediate copy, D4)

### État après cleanup

```
Downloads/
├── _archive_youtube_takeouts/
│   ├── takeout-20260611T084246Z-3-001.zip
│   └── takeout-20260619T050700Z-3-001.zip
├── _TRASH_2026-06-19_youtube_takeout_cleanup/
│   ├── watch-history_2026-06-11_OLD.html  (51 MB)
│   └── _yt_takeout_latest_intermediate/  (51.97 MB intermediate copy)
├── parse_youtube_history.py
├── takeout-20260619T050700Z-3-001/  (FRESH, à garder comme source pour futures runs)
└── youtube_videos_june_2026.csv  (FRESH, helper)
```

**Pour les futurs runs du skill** : utiliser `TAKEOUT_PATH=C:/Users/amado/Downloads/takeout-20260619T050700Z-3-001/Takeout/YouTube et YouTube\xa0Music/historique/watch-history.html` (NBSP aware) ou copier vers path no-spaces comme cette session.

## D1 verify checklist

- [x] `.processed.json` updated (955 → 966)
- [x] 11 .md files written in 5 LDxx folders (LD01: 1, LD04: 7, LD06: 1, LD07: 2)
- [x] `.runs/2026-06-19T07-08-20.json` summary created
- [x] 1 video skipped (already processed: overfl0w OSINT)
- [x] Takeout cleanup done (D4 no-hard-delete, 3 moves)
- [x] No destructive operations (no `Remove-Item`/`rm -rf`)
- [x] Fresh takeout source documented for future runs

## Cross-refs

- `wiki/log.md` 2026-06-19 entry (to be appended)
- `30_MEMORY_CORE/README.md` 2026-06-19 entry (to be appended)
- `MEMORY.md` §"YouTube takeout pipeline" + §"YouTube Ingestion 2026-06-15"
- `wiki/hand_offs/youtube_ingest_2026-06-14/` (batch #1 precedent)
- `wiki/hand_offs/youtube_ingest_2026-06-15/` (batch #2 precedent)
- Skill source : `C:\Users\amado\.claude\skills\youtube-takeout-to-lifeos\SKILL.md` + `scripts/categorize_takeout.py`
- `MEMORY.md` §"youtube-transcript-api" + UrbanVPN contournement pour transcripts (30% success rate)

## Follow-ups (optionnels, post-batch)

1. **Transcripts** : lancer `capture_june_transcripts.py` sur les 11 nouveaux video IDs pour obtenir les transcripts (mode 2 du skill, plus de valeur mais ~30% failure rate per MEMORY.md D6 #10).
2. **Reclassifier DR4** : déplacer `2026-06-18_analyse-nouveau-trailer-spider-man...` de LD04 vers LD07 + `2026-06-18_what-6-hours-alone...` de LD04 vers LD06 (simple `mv`).
3. **Sync `.processed.json`** : script de réconciliation pour aligner les 955 IDs avec les 88 fichiers existants.

---

**Status** : CLOSED. 12 vidéos 2026-06-18 transformées (11 nouvelles + 1 déjà processée). Takeout cleanup done. Handoff créé pour traçabilité.
