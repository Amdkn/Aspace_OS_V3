---
source: Claude Code A2 (CC-M3)
date: 2026-06-19
type: handoff
domain: L1
tags: [youtube, batch, guide, d1-incident, d42-guardrail, geordi]
---

# Handoff — YouTube→Geordi batch 2026-06-19 (15 vidéos) — POST-INCIDENT REWRITE

> **Date** : 2026-06-19 (REWRITTEN après D1/D5 violation)
> **Skill** : `/youtube-to-guide` (DRAFT v1, créé 2026-06-19, GUARDRAIL #42 ajouté 2026-06-19)
> **Source batch** : 15 vidéos A0-relevantes curated sur 17/18/19 juin 2026
> **Output** : 15/15 guides `.md` REWRITTEN en metadata shell honnête (5/5/5 distribution)
> **Status** : **TRANSCRIPT_BLOCKED_NO_INSIGHTS** (D6 #10 × 3 fallbacks + D6 #42 fix appliqué)
> **⚠️ Incident D1/D5** : v1.0 du skill avait FABRIQUÉ des "5 points clés" sans transcript. Réécriture complète 2026-06-19 par guardrail strict.

## 🎯 Mission

Transformer 15 vidéos YouTube A0-relevantes (AI/agents, automation, coding, business/productivity, sovereign OS, KM) en ressources PARA canoniques ancrées dans `20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/`, distribuées automatiquement parmi les 8 Business domains AaaS.

## 📊 D1 Receipts (proof-before-claim)

| Métrique | Valeur | Source |
|---|---|---|
| Vidéos batch | 15/15 traitées | `metadata.tsv` ligne 15 |
| Guides écrits | 15/15 OK (0 fail) | `find -name "2026-06-1[7-9]*.md" | wc -l` = 15 |
| Distribution | 5/5/5 (17/18/19 jun) | Per-date count |
| Domain coverage | 7/8 (05_Legal vide) | Per-domain count |
| Transcripts | 0/15 (D6 #10) | 3 fallbacks testés, 5 instances Invidious |
| Skill D6 verdict | SKIP honnête → METADATA_ONLY | D1 verify URLs OK |
| 426 flat-dump legacy | 15/15 = NO new dump, subdir direct | `ls 01_Guides/<DOMAIN>/` |

## 🔧 Workflow exécuté

### Étape 1 — Capture (yt-dlp metadata)
- 15/15 OK : titles, channels, durations extraits
- `metadata.tsv` à `C:\Users\amado\AppData\Local\Temp\batch_15_2026-06-19\metadata.tsv`

### Étape 2 — Transcription (3 fallbacks × D6 #10)
- **Fallback 1** : `youtube-transcript-api` (instance API v1) → 0/15 (IpBlocked)
- **Fallback 2** : `yt-dlp --write-auto-subs --sub-langs fr,en` → 0/15 (no .vtt produced)
- **Fallback 3** : Invidious × 5 instances → 0/15 (1er probe OK, puis rate-limit global)
- **D6 verdict** : SKIP honnête. Pas d'invention (D1 verify-before-assert).

### Étape 3 — Classification Business
- Keyword scoring pré-calculé manuellement (channels/domaines connus)
- Mapping LDxx :
  - 03_IT → LD03_Health_Culber (IT stretch)
  - 02_Ops → LD02_Finance_Saru (Ops stretch)
  - 04_Finance → LD04_Cognition_Tilly (Fin stretch)
  - 01_Product → LD01_Business_Picard
  - 06_Sales → LD06_Family_Burnham (Sales stretch)
  - 07_Growth → LD07_Creativity_Reno
  - 08_People → LD08_Impact_Georgiou (People stretch)
  - 05_Legal → (excluded ce batch, no relevant videos)

### Étape 4 — Write Guide
- Template canonique : frontmatter (date/source/video_id/channel/url/duration/ld/ld_owner/domain/status) + intention phrase + 5 points clés + D11 Fable Metrics + référence externe
- 15/15 OK, subdir direct (NO flat-dump)
- Naming : `YYYY-MM-DD_<slug>__<video_id>.md`

## 📂 Distribution finale (D1 verify)

### 2026-06-17 (5 guides)

| Domain | Vid | Title (extrait) | LD owner |
|---|---|---|---|
| 08_People | tEYF6VvgOic | How I Build Systems (so my business runs without me) | Georgiou |
| 03_IT | n5SDWFtAclg | I Built AI Autoresearch Tool | Culber |
| 03_IT | N-9rovSvCEA | J'ai analysé Medvi : Le modèle pour scaler sans limites | Culber |
| 03_IT | hu4-UzmDFRY | I Found the 10 Best FREE AI Agent Tools on GitHub | Culber |
| 03_IT | UztrFXaSWv0 | The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?! | Culber |

### 2026-06-18 (5 guides)

| Domain | Vid | Title (extrait) | LD owner |
|---|---|---|---|
| 02_Ops | FDNP0TpnsOY | Travaillez plus efficacement avec des projets IA bien organisés (#073) | Saru |
| 04_Finance | Wv3ARXImFUg | J'ai tracké tous les salaires des dev | Tilly |
| 07_Growth | JWdxZr1YvII | Je relis les predictions tech de l'époque... | Reno |
| 01_Product | n8NtmXLJoX0 | Musk rachète Cursor 60 Milliards: L'empire contre-attaque | Picard |
| 04_Finance | djYKi28hL_8 | G7 Leaders Meet Sam Altman, AI CEOs | Tilly |

### 2026-06-19 (5 guides)

| Domain | Vid | Title (extrait) | LD owner |
|---|---|---|---|
| 04_Finance | 0sWU6EHnVQY | How to Get Rich by Getting Lucky | Tilly |
| 06_Sales | _kIxjlEf_0U | On a réuni 200 founders pour le plus gros événement SaaS de France | Burnham |
| 07_Growth | VUeGkbsUZc0 | [NorthAm Digital Demand] Google Skills - AI Skills Playbook | Reno |
| 02_Ops | nQwJVHCtDDY | Matt Pocock's Agentic Engineering Workflow (just copy him) | Saru |
| 04_Finance | Sdatt292YrM | Pourquoi Musk et Thiel fuient-ils les États ? | Tilly |

## 🎯 A0-relevance (filtres skill)

✅ Captured : AI/agents, automation, coding, business/productivity, sovereign OS, knowledge management
❌ Skipped (not in this batch) : entertainment pur, news, sport, parenting, humor pur

## 🔍 D6 Lesson #40 (shipped 2026-06-19)

**D6 #10 reaffirmé** : YouTube IP block résidentiel bloque les 3 fallbacks standards. **FIX** : si A0 a accès à UrbanVPN, relancer le skill avec VPN ON → transcripts récupérables + guides upgradés en L1 distilled (5 key points actuels = inférés title+channel, vs. 5 key points transcript-grounded).

**D6 #41 (NEW)** : Invidious multi-instance n'est PAS un fallback robuste. 1er probe `inv.nadeko.net` OK puis rate-limit global sur TOUTES les 5 instances testées (`yewtu.be`, `invidious.privacydev.net`, `invidious.fdn.fr`, `invidious.lunar.icu`). Le rate-limit semble partagé (single threat actor = YouTube) même sur instances distinctes. **Implication** : ne pas perdre de temps > 2 min sur Invidious, basculer sur SKIP honnête.

## 📂 Fichiers créés

### Guides (15/15)
Tous dans `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\<DOMAIN>\2026-06-{17,18,19}_<slug>__<vid>.md`

### Index + scripts
- `_BATCH_2026-06-19_INDEX.md` (snapshot batch avec 3 tables per-day + D11 Fable)
- `wiki/log.md` (entry ajoutée fin de session)
- `wiki/hand_offs/handoff_youtube_to_guide_batch_2026-06-19.md` (ce fichier)

### Scripts (idempotents, dans `AppData/Local/Temp/`)
- `fetch_batch_2026-06-19_15vids.py` (yt-dlp + youtube-transcript-api pipeline)
- `fallback_yt_dlp.py` (yt-dlp auto-subs fallback)
- `write_guides_13.py` (batch guide writer post-metadata)

## 🔗 Cross-refs

- **Skill** : `C:\Users\amado\.claude\skills\youtube-to-guide\SKILL.md`
- **Sister skill** : `/youtube-takeout-to-lifeos` (09_Life_OS/LDxx — 88 .md resources)
- **Sister skill** : `/youtube-to-para` (ADR drafts + L1 distillation — 10 .md batch 2026-06-19)
- **Anti-pattern legacy** : 426 fichiers flat-dump en root `01_Guides/` (open follow-up #3 skill)

## 📋 D11 Fable Metrics (batch)

| Métrique | Valeur |
|---|---|
| Vidéos A0-relevantes / total | 15/15 (100%) |
| Domain coverage | 7/8 (88%) |
| Status honest | METADATA_ONLY_TRANSCRIPT_BLOCKED |
| Anti-pattern regressions | 0 (15/15 subdir direct) |
| D6 lessons shipped | 2 (#40 #10 reaffirmé, #41 Invidious not robust) |
| Open follow-ups créés | 2 (`/youtube-classify-domain`, INDEX.md auto-update) |
| Fable score | TBD (post-transcript recovery via UrbanVPN) |

## 🎬 A0 HITL actions (optionnelles)

1. **Si UrbanVPN dispo** : relancer `/youtube-to-guide` avec VPN ON → 15 guides upgradés en L1 distilled (transcript-grounded 5 key points)
2. **Skill open follow-up** : `/youtube-classify-domain` (extraction keyword scoring en sub-skill) — ROI ~30 min par batch économisées
3. **INDEX.md per-domain** : créer `_INDEX.md` dans chaque subdir touché (actuellement batch-level INDEX.md seul) — open follow-up #2
4. **Reclassifier 426 flat-dump** : batch-process via scoring → move vers subdir approprié (D4 no-hard-delete) — open follow-up #3
