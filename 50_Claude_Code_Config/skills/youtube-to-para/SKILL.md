---
name: youtube-to-para
description: Transforme une capture YouTube (image/URL) OU des transcriptions collées in-chat par A0 en ressource PARA → principes ADR → amélioration du Harness. Workflow 5 étapes (WebSearch → transcript → handoff insights → ADR drafts → distillation L1 Research) + mode in-chat (skip étapes 1-2, video_id UNKNOWN honnête). Invoke quand A0 partage une capture YouTube historique, colle des transcriptions, dit "j'ai regardé des vidéos" / "extrait les transcripts" / "transforme en PARA" / "crée des ADR à partir des vidéos", ou en fin de cycle 12WY pour bilan. ROUTAGE TRIO (voir §Trio) — ce skill = l'ENTRÉE du funnel (ingestion + ADR drafts) ; la distillation Premium par vidéo = /youtube-to-guide ; la capture bulk takeout = /youtube-takeout-to-lifeos. ROI : ~30 min par batch de 10 vidéos économisées (vs 3-5h manuel).
---

# 🎬 YouTube → PARA — Pipeline d'ingestion transcripts

## Goal
Transformer l'historique YouTube A0 (captures, URLs, titres clickbait) en **ressources PARA
canoniques** ancrées dans le wiki A'Space + **ADR drafts** proposés à ratification + **distillation
L1 Research Pulse** (knowledge opéralionnel cycle 12WY).

## ⚡ MISE À JOUR 2026-07-02 (run loops — leçons intégrées, évolution sans destruction)

### §Trio — Routage des 3 skills YouTube (le fix anti-doublon)

> **D6 leçon 2026-07-02** : la session a failli créer un doublon 2× (le Skill Reflex a poussé la création alors que `/youtube-to-guide` existait depuis le 06-22 et que ce skill existait depuis le 06-15). **Règle : `ls ~/.claude/skills/ | grep -i <thème>` AVANT toute proposition de création.**

| Skill | Rôle dans le funnel | Output | LLM |
|---|---|---|---|
| **`/youtube-to-para`** (CE skill) | **ENTRÉE** : ingestion batch (capture/URL/transcript in-chat) → transcripts bruts + handoff insights + **ADR drafts** | `wiki/hand_offs/youtube_ingest_<date>/` + `_SPECS/ADR/<layer>/` | oui (insights + cross-cuts) |
| **`/youtube-to-guide`** | **DISTILLATION Premium** par vidéo : standard Antigravity 6-16K chars (8 sections, glossaire, matrice outillage, DEAL, annexes) | `01_Guides/<0X_DOMAIN>/` (8 subdirs Business) | oui (deep) |
| **`/youtube-takeout-to-lifeos`** | **CAPTURE bulk** mécanique du takeout (watch-history.html) | `09_Life_OS/LDxx_*/` (Life Wheel) | non (scripts) |

**Funnel complet** : capture (takeout/para) → distillation (`/youtube-to-guide`) → **doctrine L2** (`/area-domain-doctrine-distill` re-distille les `03_*_PRINCIPLES.md` quand ≥3 guides nouveaux — le hook SessionStart flagge l'obsolescence automatiquement).

### Mode transcript-in-chat (nouveau, prouvé run 2026-07-02)

Quand A0 **colle les transcriptions directement en chat** (pas d'URL, pas de capture) :
- **Skip Étapes 1-2** (pas de WebSearch, pas de fetch) — le transcript est déjà dans le contexte.
- **`video_id: UNKNOWN` + `watch_url: null`** — JAMAIS inventé (doctrine CLAUDE.md). Frontmatter `source_note:` = « transcript fourni par A0 in-chat <date> ».
- Étapes 3-4-5 inchangées. Pas de risque context-blowup (le transcript est déjà chargé).

### Étape 4 renforcée — format ADR canon (pattern ADR-LOOP-001/002/003)

- **1 ADR = 1 doctrine cross-vidéos** (thème récurrent ≥2 vidéos), JAMAIS 1 ADR = 1 vidéo.
- Frontmatter obligatoire : `id / title / date / author / status: PROPOSED / ratified: null / layer / preserves / sister / tags`. **`sister:` liste les guides sources** ; **`preserves:` liste les ADRs/mindsets respectés**.
- Corps : `## Décision` (lois numérotées impératives) · `## Rationale` · `## Conséquences` · `## Rejeté` (anti-patterns écartés).
- Layers : `L0_Tech_OS` (harness/loops/infra) · `L1_Life_OS` · `L2_Business_OS`. Numéro = max du namespace + 1 (`ls` d'abord).
- **Jamais de self-ratify** — la ratification appartient à A0 (Règle d'Or #3).

### Étape 5 corrigée — la distillation délègue

L'ancien path (`01_Guides/09_Life_OS/LD0X`) mélangeait deux arbres. Canon : la distillation Premium **délègue à `/youtube-to-guide`** (→ `01_Guides/<0X_DOMAIN>/`) ; la capture Life Wheel légère reste en `09_Life_OS/LDxx_*/` (format takeout). Les deux fiches se lient par `sister:` frontmatter.

---

## Triggers (D1 receipts sessions antérieures)

| Trigger | Match observé | Source |
|---------|---------------|--------|
| A0 partage capture YouTube (image) | 2026-06-14 (12 vidéos) + 2026-06-15 (3 vidéos) | sessions antérieures |
| A0 dit "j'ai regardé des vidéos" / "voici mon historique" | 2026-06-14 | session youtube_ingest_2026-06-14 |
| A0 dit "extrait les transcripts" / "transforme en PARA" | 2026-06-15 (Mission ρ) | handoff_fable_mort_claim |
| Fin de cycle 12WY (tous les 12 semaines) | 2026-09-07 (fin cycle 06/15 → 09/07) | ADR-Meta-000 E1-E12 |

**3+ triggers matchent** = Skill Creator Reflex Phase 2 (CLAUDE.md global) autorise création
autonome par agent, sans A0 GO.

## Workflow (5 étapes, ~30 min par batch de 10 vidéos)

### Étape 1 — Image → URLs (1-2 min par capture)

**Input** : capture YouTube A0 (image) ou URLs explicites.

**Output** : liste de 1-N URLs à traiter.

**Méthode** :
```bash
# Si capture image : extraire URLs via reverse image search (optionnel) ou demander A0 confirmation
# Si URLs explicites : les parser directement
# Format de stockage canonique :
mkdir -p "ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/youtube_ingest_$(date +%Y-%m-%d)/transcripts"
echo "URLs à traiter:" > "ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/youtube_ingest_$(date +%Y-%m-%d)/urls.txt"
```

**D1 receipt** : fichier `urls.txt` créé avec 1+ URLs.

### Étape 2 — WebSearch titre + chaîne → video_id (2-3 min par vidéo)

**Input** : URL ou titre YouTube.

**Output** : `video_id` (11 chars) + métadonnées (chaîne, durée, date publish).

**Méthode** :
```python
# Python avec youtube-transcript-api
import subprocess
result = subprocess.run(
    ["python", "-c", f"""
from youtube_transcript_api import YouTubeTranscriptApi
# Extract video_id from URL
url = '{url}'
video_id = url.split('v=')[1].split('&')[0] if 'v=' in url else url.split('/')[-1].split('?')[0]
print(f'video_id: {{video_id}}')
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['fr', 'en'])
text = ' '.join([t['text'] for t in transcript])
print(f'duration: {{transcript[-1][\"start\"] + transcript[-1][\"duration\"]:.0f}}s')
print(f'lines: {{len(transcript)}}')
print('---TRANSCRIPT---')
print(text)
"""],
    capture_output=True, text=True
)
print(result.stdout)
```

**D1 receipt** : video_id extrait, transcript retourné (D1 verify HTTP 200 youtube-transcript-api).

**Note Fallback** : si youtube-transcript-api échoue (rate limit, vidéo privée, captions désactivées) :
- Essayer Invidious instance (https://yewtu.be / https://invidious.snopyta.org).
- Essayer yt-dlp (NON disponible sur Windows ce environnement, fallback DuckDuckGo HTML).
- Dernier recours : SKIP honnête (D6 root cause), pas d'invention.

### Étape 3 — Transcript → Handoff insights (5-10 min par vidéo)

**Input** : transcript brut (200-1500 lignes typiquement).

**Output** : fichier transcript formaté + section insights structurée.

**Méthode** :
```bash
# Stocker transcript brut (canonique)
video_id="ABC123XYZ"
title="Titre YouTube (extrait via oEmbed)"
python -c "
import sys
sys.stdout = open('${transcript_path}', 'w', encoding='utf-8')
print('# ${title} — video_id ${video_id}')
print('Date: $(date +%Y-%m-%d)')
print('Source: YouTube ${url}')
print()
print('## Transcript complet')
print()
# ... (transcript lines avec timestamps)
"
```

**Insights extraction** (5-10 bullets par vidéo) :
1. **Thème central** : 1 phrase résumant le sujet.
2. **Concepts clés** : 3-5 notions techniques/méthodologiques distinctes.
3. **ADR candidates** : 0-3 ADR drafts qui pourraient être proposés (principe, anti-pattern, doctrine).
4. **Cross-cuts thématiques** : liens avec autres vidéos du batch ou ADR canoniques (META-001, RICK-001, etc.).
5. **Actionnables A0** : 0-3 décisions/skill/agents à créer ou amender.

**D1 receipt** : fichier transcript.md créé avec 200+ lignes + section insights 5-10 bullets.

### Étape 4 — Cross-cuts batch → ADR drafts (10-15 min par batch)

**Input** : N fichiers transcript.md + insights extraits.

**Output** : 0-5 ADR drafts proposés + 1 handoff canonique batch.

**Méthode** :
- Identifier thèmes récurrents (≥ 2 vidéos qui mentionnent X).
- Pour chaque thème récurrent, vérifier si ADR canonique existe (Grep `_SPECS/ADR/`).
- Si non, créer DRAFT dans layer approprié (L0 = infra, L1 = life OS, L2 = business OS).
- Format ADR compact (≤ 200 lignes) : frontmatter + Context + Decision + Consequences + References.

**Handoff canonique** (1 par batch) :
```bash
# Emplacement
"ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/youtube_ingest_${date}/youtube_ingestion_handoff_${date}.md"

# Sections obligatoires (D6 root cause — chaque section a une raison d'être)
1. Contexte (pourquoi ce batch)
2. Table index vidéos (N rows : #, titre, video_id, durée, thème, ADR draft #)
3. Insights par vidéo (5-10 bullets × N)
4. Cross-cuts thématiques (3-5 themes + count)
5. ADR drafts proposés (0-5 drafts, à ratifier par A0)
6. Open follow-ups (skill `/youtube-to-para` itéré, L1 distillation prochaine, etc.)
```

**D1 receipt** : handoff handoff_${date}.md créé avec 6 sections, 0 video_id inventé (D1 verify
chaque video_id via `curl https://www.youtube.com/oembed?url=...&format=json`).

### Étape 5 — Distillation L1 Research Pulse (à la demande A0, hors batch)

**Input** : handoff ${date} ratifié par A0.

**Output** : ressources PARA canoniques dans
`20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/09_Life_OS/LD0X_<domaine>/`.

**Méthode** : transformer chaque transcript en guide 1-page (LD04_Cognition_Tilly style) :
- 1 phrase d'intention.
- 3-5 points clés.
- 1 mini-tableau métrique (D11 Fable).
- 1 référence externe (HuggingFace, blog post, paper).

**D1 receipt** : guide créé, DOI/index mis à jour dans
`LD0X_<domaine>/_INDEX.md`.

## Doctrine ancrage

- **D1 verify-before-assert** : 0 video_id inventé. Chaque URL = oEmbed verify 200.
- **D2 research-first** : avant de conclure un thème, vérifier si ADR canon existe.
- **D3 nuance over literal** : titres clickbait YouTube ≠ contenu réel. D1 verify transcript AVANT
  de dériver ADR.
- **D4 no-self-contradiction** : append-only handoff, pas d'écrasement transcript existant.
- **D5 proof-before-claim** : "voici 3 ADR drafts" = 3 fichiers .md créés, pas prose.
- **D6 root cause** : si youtube-transcript-api fail, escalader honnêtement (SKIPPED), pas
  fallback inventé.
- **D7 cost-of-escalation A0** : A0 valide le handoff final, A2 ne spam pas 50 questions mid-batch.
- **D8 cross-agent** : sub-agent A3 peut paralléliser Étape 2 (10 vidéos = 10 sub-agents).

## Skill boundary

**OÙ OUI** :
- Captures YouTube A0 (image ou URL).
- URLs individuelles partagées en chat.
- Bilan fin de cycle 12WY (auto-trigger si A0 ouvre bilan).

**OÙ NON** :
- Articles web non-YouTube (utiliser WebFetch + Read).
- Podcasts (workflow différent, Whisper transcription).
- Livres/papers (utiliser Context7 ou Read direct).
- Vidéos sans captions (SKIP honnête, proposer alternative).

## Output structure (canonique)

```
ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/youtube_ingest_<YYYY-MM-DD>/
├── urls.txt                              # Étape 1 : URLs à traiter
├── transcripts/
│   ├── 01-<title-slug>-<video_id>.md    # Étape 2-3 : par vidéo
│   ├── 02-<title-slug>-<video_id>.md
│   └── ...
├── youtube_ingestion_handoff_<YYYY-MM-DD>.md  # Étape 4 : handoff batch
└── distillation_L1_<YYYY-MM-DD>/        # Étape 5 (à demande)
    └── LD0X_<domaine>/
```

## References (D2 research-first)

- **Run de référence 2026-07-02 (mode in-chat + ADR canon)** : 4 transcriptions loops collées par A0 → 4 guides Premium `01_Guides/03_IT/2026-07-02_*.md` (10,4-11,6K chars, via /youtube-to-guide) + 4 captures légères `09_Life_OS/LD07_Creativity_Reno/*__GUIDE.md` + `ADR-LOOP-001/002/003` PROPOSED (`_SPECS/ADR/L0_Tech_OS/`). ~25 min.

- `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/youtube_ingest_2026-06-14/youtube_ingestion_handoff_2026-06-14.md` (premier run, 12 vidéos).
- `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_fable_mort_claim_d1_falsification_2026-06-15.md` (deuxième run, 3 vidéos).
- `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_fable_to_minimax_distillation_2026-06-15.md` (troisième run, 3 vidéos, distillation).
- `~/.claude/CLAUDE.md` section "🎬 YouTube Ingestion Pipeline" (doctrine, append-only 2026-06-14).
- `~/.claude/skills/skill-creator/SKILL.md` (méta-skill, Phase 2 autonomie doctrine).
- `ADR-MEMO-000_auto-research-karpathy-loop-claude-code_DRAFT.md` (sister, auto-research doctrine).
- `ADR-INFRA-004_jsonl-mining-extract-mindset-pipeline.md` (sister, JSONL mining pipeline).
- `ADR-Meta-000_12-week-year-cycle-doctrine_DRAFT.md` (cycle 12WY = bilan fin cycle = trigger Étape 5).
- youtube-transcript-api : https://github.com/jdepoix/youtube-transcript-api (vérifié installé).

## Quick start (cheat sheet A2)

```bash
# A0 partage capture YouTube
# → Appeler ce skill
# → Étape 1 : extraire URLs (Read image ou AskUserQuestion)
# → Étape 2 : sub-agent en parallèle par URL (10 vidéos = 10 sub-agents background)
# → Étape 3 : merge transcripts dans transcripts/
# → Étape 4 : rédiger handoff handoff_<date>.md (6 sections)
# → Étape 5 (optionnel) : distillation L1 si A0 demande
# → Présenter handoff à A0 pour ratification ADR drafts
```
