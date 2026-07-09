---
name: youtube-to-guide
description: Transform a YouTube video (URL or A0 screenshot) into ONE premium 8-section guide filed in Geordi Resources 01_Guides/<domain>/, auto-classified against the 8 Business AaaS domains via the RATIFIED bijection. Use when A0 says "transforme cette vidéo en guide", "guide premium", "youtube to guide", or shares a YouTube link for the guide pipeline. Distinct from youtube-to-para (which proposes ADRs / general PARA resources) and youtube-takeout-to-lifeos (bulk watch-history takeout) — this one is the single-video premium guide builder.
---

# YouTube to Guide — Skill (Antigravity Premium Standard)

> **Capture une vidéo YouTube → transcription → classification auto dans un des 8 Domaines Business AaaS → guide `.md` PREMIUM au standard Antigravity dans `01_Guides/<domaine>/`.**

## Goal

Transformer un lien vidéo (URL ou capture image A0) en **ressource PARA canonique PREMIUM** ancrée dans `20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/<DOMAIN>/`, structurée selon le **Gold Standard Antigravity** (8 sections sémantiques, glossaire de concepts, matrice d'outillage souveraine, perspective A'Space longue, protocole D.E.A.L, annexes numérotées). Cible : **6-16K chars par guide** (vs version superficielle = 2.5K = "token economy").

**Anti-patterns corrigés** :
- ❌ "5 points clés" superficiels (token economy)
- ❌ Intention phrase + bullets plats
- ✅ **Concepts en glossaire** (`<Concept>` : définition longue 50-100 mots)
- ✅ **Matrice d'outillage** (Outil × Rôle × Alignement Souverain A'Space)
- ✅ **Perspective Souveraine A'Space** (paragraphe long 200+ mots)
- ✅ **Protocole D.E.A.L** (Définir/Éliminer/Automatiser/Libérer)
- ✅ **Annexes numérotées** (Note A3-01, A3-02, ... deep dives)

## Trigger (D1 receipts sessions antérieures)

| Trigger | Match observé | Source |
|---------|---------------|--------|
| A0 partage URL YouTube ou capture d'écran | Multiple sessions 2026-06-13 → 2026-06-19 | Sessions /youtube-to-para + /youtube-takeout-to-lifeos |
| A0 dit "transforme en ressources PARA" / "fais des guides" | Session 2026-06-19 (5 fois) | Contexte business OS |
| Anti-pattern observé : 426 fichiers `.md` en root de `01_Guides/` non classifiés | D6 root cause session 2026-06-19 | Audit `01_Guides/` |
| **A0 review "économie de token / paresse intellectuelle"** vs Antigravity | 2026-06-19 | Session escalade — guides superficiels insuffisants |

## 8 Domaines Business AaaS (canonical mapping)

> ⚡ÉVOLUTION 2026-07-06 (D6 root cause du drift LD) : l'ancienne table ci-dessous était un **mapping
> positionnel naïf** (01→LD01, 02→LD02…) contredisant la bijection RATIFIED `ADR-L2-BDLD-MAP-001` §D3.
> C'était LA source des `ld:` faux (ex. Sales→LD06_Burnham). Table corrigée au canon — cf. §6 pour le gate.

| # | Subdir `01_Guides/` | LDxx Life Wheel mirror (CANON D3) | Category Antigravity prefix |
|---|---------------------|------------------------|----------------------------|
| 1 | `01_Product/` | LD04_Cognition_Tilly | Product Management / Architecture |
| 2 | `02_Ops/` | LD01_Business_Book | Systématisation / Automatisation |
| 3 | `03_IT/` | LD07_Creativity_Reno | AI / Code / Infrastructure |
| 4 | `04_Finance/` | LD02_Finance_Saru | Modèles d'Affaires / Arbitrage |
| 5 | `05_Legal/` | LD03_Health_Culber | Compliance / Contrats |
| 6 | `06_Sales/` | LD05_Social_Stamets | Go-to-Market / Pipeline |
| 7 | `07_Growth/` | LD08_Impact_Georgiou | Acquisition / Funnel |
| 8 | `08_People/` | LD06_Family_Burnham | Productivité / Mindset |

> **EXCLUSION** : `00_KERNEL_OS/` (infra kernel, vide par design) et `09_Life_OS/` (Life Wheel LDxx, géré par `/youtube-takeout-to-lifeos` skill).

## Workflow (4 étapes, ~8-12 min par vidéo)

### Étape 1 — Capture (30 sec)
Même que v1 : yt-dlp `extract_info` → title + channel + duration + upload_date + description.

### Étape 2 — Transcription (1-3 min)
**Working path confirmé** : TranscriptAPI MCP (D6 #43).
- MCP config dans `C:\Users\amado\.mcp.json` (mcp-remote wrapper, D6 #46).
- Si MCP tools visibles dans session : `mcp__transcript-api__get_youtube_transcript({video_url, format: "text"})`
- Si MCP tools PAS visibles (D6 #4) : workaround curl avec `User-Agent: curl/8.4.0` (D6 #43b).
- Fallback si erreur : `youtube-transcript-api` → `yt-dlp auto-subs` → `Invidious multi-instance` → SKIP honnête.

### Étape 3 — Classification Business (10 sec)
Keyword scoring sur title + description + transcript opener. Si égalité → A0 HITL.

### Étape 4 — Write Guide PREMIUM (8-10 min)

**Template Antigravity canonique** (8 sections sémantiques) :

```markdown
---
id: YT-<video_id>
title: "<title YouTube EXACT>"
channel: "<channel name>"
duration: "<MM:SS>"
date: "YYYY-MM-DD"
category: "<Domain> / <Sub-thematic>"
status: DISTILLED_L1_PREMIUM
b1_filter: REQUIRED (⚡ÉVOLUTION 2026-07-03 — cf. §6 B1 Jerry gating)
b1_owner: <b1 captain, default=jerry-prime, b2 owner for downstream routing>
domain: 0X_<Domain>   # same as 0X_ dir, lowercase typed
ld: <LDxx_LifeWheel_Domain>  # mandatory post-2026-07-03, must be consistent with b1.b2 mapping
sister_b1: <b1 variant>  # jerry-prime | summers-nexus-omk | summers-solaris-aaas | summers-orbiter-abc
b2_owner: <b2 manager>  # flash-product | batman-ops | cyborg-it | wonderwoman-finance | johnjones-sales | superman-growth | aquaman-legal | greenlantern-people
---

# 📖 <title YouTube>

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour le Domaine <DOMAIN> — <Sub-thematic>.

---

## 🧠 Concepts Clés à Haute Densité Sémantique

- **<Concept 1>** : Définition longue 50-100 mots du concept-clé #1 extrait du transcript, en langage technique précis. Pas de reformulation générique — utiliser les terms exacts de l'auteur.

- **<Concept 2>** : Définition longue 50-100 mots...

- **<Concept 3>** : ...

- **<Concept 4>** : ...

- **<Concept 5>** : ...

- **<Concept 6>** : ... (optionnel)

---

## 🛠️ Outillage Stratégique & Matrice d'Alignement

| Outil / Technologie / Approche | Rôle Stratégique | Alignement Souverain A'Space |
| :--- | :--- | :--- |
| **<Outil mentionné vidéo>** | Rôle dans le workflow décrit | Alternative souveraine dans A'Space OS (n8n, Obsidian, local DB, agents A3) |
| **<Outil 2>** | ... | ... |
| **<Outil 3>** | ... | ... |

---

## 🪐 Perspective Souveraine A'Space <DOMAIN>

Paragraphe long (200+ mots) connectant le contenu de la vidéo à la doctrine A'Space. Adresser :
- **Comment ce contenu s'intègre dans l'architecture A'Space existante** (skills, agents, MCPs, infra)
- **Quelle(s) action(s) concrète(s) A0 peut prendre dans les 30 jours** (H3 Saru horizon)
- **Quels A3 twins sont concernés** (Picard/Freeman/Cerritos/Discovery/Orville/Enterprise/Protostar)
- **Quels ADR canoniques sont impactés** (renvoi explicite)
- **Quelle doctrine A'Space est confirmée/infirmée/étendue** par ce contenu

---

## 🕹️ Protocole d'Exécution D.E.A.L

| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | Action immédiate liée au contenu de la vidéo | Objectif stratégique A'Space |
| **Éliminer** | Action de retrait / simplification | Réduction de friction |
| **Automatiser** | Action d'automatisation via n8n / agent A3 | Libération cognitive Hôte |
| **Libérer** | Action de délégation / scaling | Transformation business model |

---

## 🔬 Annexes Détaillées de l'Audit Sémantique & Technique

### Note <A3-NN> : <Titre deep-dive #1>
Deep dive sur un point spécifique du contenu — 100-200 mots.

### Note <A3-NN> : <Titre deep-dive #2>
Deep dive #2.

### Note <A3-NN> : <Titre deep-dive #3>
Deep dive #3.

---

*Fiche de connaissances souveraine d'<DOMAIN> générée sous A'Space OS V2 — Standard Antigravity Premium.*
```

**Cible qualité** :
- **6-16K chars par guide** (vs superficiel 2.5K)
- **5-6 concepts** dans la section glossaire (50-100 mots chacun)
- **2-4 outils** dans la matrice d'alignement
- **Perspective Souveraine** : paragraphe long (200+ mots)
- **DEAL** : 4 phases avec action concrète + objectif A'Space
- **Annexes** : 2-5 notes numérotées (Note A3-01, A3-02, ...)

## Sub-step critique — Atomicité anti-régression

1. **JAMAIS** écrire à `01_Guides/` racine (uniquement 8 subdirs Business)
2. **Si classification échoue** → A0 HITL avant d'écrire
3. **Cleanup atomic** : `mv` + update `_INDEX.md` + retrait de l'ancien index
4. **Anti-token-economy** : si guide < 6K chars, **ne pas shipper** — étendre les sections manquantes avant. Le standard Antigravity = 6K min, 16K optimal pour videos > 30min.

## D1 receipts par étape

| Étape | Output observable | Validation |
|-------|-------------------|------------|
| 1 | metadata dans stdout | title + channel non-vides |
| 2 | transcript dans `_transcripts_raw/<vid>.md` | `wc -l` ≥ 50 OU status BLOCKED honnête |
| 3 | domain dans frontmatter | 1 des 8 subdirs canoniques |
| 4 | guide écrit | `wc -c` ≥ 6000 (standard Antigravity) |

## Doctrine ancrage

- **D1 verify-before-assert** : 0 video_id inventé. TranscriptAPI MCP = source canonique post D6 #43.
- **D2 research-first** : keyword scoring puis A0 HITL si ambiguïté.
- **D3 nuance over literal** : titre clickbait ≠ contenu. D1 verify transcript AVANT classification.
- **D4 no-self-contradiction** : append-only files. Pas d'écrasement.
- **D5 proof-before-claim** : "j'ai écrit le guide" = `wc -c <path>` ≥ 6000 + `grep -c "Concepts Clés" <path>` = 1.
- **D6 root cause** : 3 fallbacks transcript avant SKIP honnête.
- **D7 cost-of-escalation A0** : 1 AskUserQuestion max par vidéo (classification ambiguë).
- **D8 cross-agent** : sub-agents A3 peuvent paralléliser pour batch > 5 vidéos.

## 🚨 D6 Lesson #NEW — CONTEXT BLOWUP PREVENTION (2026-06-22, A0 escalade)

**Violation observée** : transcripts longs (15-25K chars pour vidéos 60-90min) → blowup du Main Agent context → CC déclenche `/compact` automatiquement → si insuffisant, compactions successives → reasoning state brisé.

**Solution** : Étape 2 (Transcription) + Étape 4 (Write Guide) doivent utiliser **`/swarm-chunk-transcript`** skill pour processing parallèle via N sub-agents.

**Workflow révisé** :

```
Étape 2 (Transcription)
  ↓ Write transcript to _transcripts_raw/<vid>.md (D4 append-only)
  ↓ char_count check :
       < 6000 chars  → inline path (Main Agent reads full)
       6K-50K chars  → /swarm-chunk-transcript skill (Karpathy pattern)
       > 50K chars   → D6 BLOCKED + A0 HITL (D6 hard limit)
  ↓ If chunked: N sub-agents // (haiku, isolated context)
  ↓ Aggregated JSON output → disk only (not in Main Agent context)

Étape 3 (Classification) → cheap, Main Agent only

Étape 4 (Write Guide)
  ↓ Main Agent reads aggregated JSON ONLY (not raw transcript)
  ↓ Synthesize 6-16K char guide from structured insights
  ↓ Main Agent context usage ≤ 30% of original transcript size
```

**Acceptance Criteria** (révisés) :

| Étape | Output observable | Validation | D6 fix |
|-------|-------------------|------------|--------|
| 1 | metadata dans stdout | title + channel non-vides | — |
| 2 | transcript dans `_transcripts_raw/<vid>.md` | `wc -l` ≥ 50 OU status BLOCKED honnête | char_count check |
| 2a | swarm chunk aggregate JSON | `chunk_count = ceil(char_count/3000)` | if char_count > 6K |
| 3 | domain dans frontmatter | 1 des 8 subdirs canoniques | — |
| 4 | guide écrit | `wc -c` ≥ 6000 (standard Antigravity) | context usage ≤ 30% |

**Anti-pattern guards** :
- ❌ Load full 25K transcript into Main Agent context → /compact loop
- ❌ Use opus for chunk extraction (haiku = 10× cheaper, sufficient)
- ❌ Sequential chunk processing (defeats parallelism purpose)
- ❌ Aggregate in Main Agent context (write to disk, reference by path)

**Cross-ref** : `/swarm-chunk-transcript` skill (Karpathy pattern canonique).

## 🚨 D6 Lesson #42 — GUARDRAIL FABRICATION (incident 2026-06-19)

**Violation commise** : skill v1.0 a FABRIQUÉ des "5 points clés" + "Intention" sans transcript. **15/15 guides pollués** détectés.

**REGLE ABSOLUE** :
> Si transcript bloqué → écrire UNIQUEMENT un metadata shell honnête.
> JAMAIS de body fabrication. Status obligatoire `TRANSCRIPT_BLOCKED_NO_INSIGHTS`.

## 🚨 D6 Lesson #48 — ANTI-PARESE INTELLECTUELLE (incident 2026-06-19)

**Violation commise** : skill v2.0 a écrit 13 guides "distilled" superficiels (~2.5K chars) avec 5 bullets plats. A0 review : "économie de Token / paresse intellectuelle" vs standard Antigravity (6-16K chars avec 8 sections sémantiques).

**REGLE ABSOLUE** :
> Un guide "DISTILLED_L1" doit matcher le **standard Antigravity** :
> - 5-6 concepts en glossaire (50-100 mots chacun)
> - Matrice d'outillage Outil × Rôle × Alignement A'Space
> - Perspective Souveraine A'Space (paragraphe 200+ mots)
> - DEAL protocol (4 phases action/objectif)
> - Annexes numérotées (2-5 deep dives)
> - Footer "Fiche de connaissances souveraine..."

**Anti-pattern guards** :
- ❌ Guide < 6K chars = token economy / paresse intellectuelle
- ❌ 5 bullets plats au lieu de glossaire sémantique
- ❌ Section "Intention" + "5 points clés" + "D11 metrics" sans matrice/DEAL/annexes
- ✅ Guide ≥ 6K chars avec 8 sections Antigravity canoniques

## ✅ D6 Lesson #43 — TranscriptAPI MCP WORKING PATH

[Conservé — voir section historique]

**Add config (D6 #46)** : dans `C:\Users\amado\.mcp.json` :
```json
"transcript-api": {
    "command": "npx",
    "args": ["-y", "mcp-remote@latest", "https://transcriptapi.com/mcp",
             "--header", "Authorization: Bearer sk_..."]
}
```

## Cross-refs

- `/youtube-takeout-to-lifeos` (sister skill — 09_Life_OS/LDxx/)
- `/youtube-to-para` (sister skill — ADR drafts + L1 Geordi 09_Life_OS)
- **Standard Antigravity reference** : `01_Guides/02_Ops/ultimate-guide-to-systemize-your-business-in-2026.md`, `01_Guides/04_Finance/resource_claude_business_blueprint.md` (gold standard 6-16K chars)
- `_SPECS/ADR/ADR-OMK-004_pivot-supabase-cloud-vercel.md`

## Open follow-ups

1. **Skill `/youtube-classify-domain`** : extraction keyword scoring sub-skill
2. **INDEX.md auto-update** : script bash rebuild `_INDEX.md` per subdir
3. **Reclassification 426 flat-dump** : batch-process via scoring → move (D4 no-hard-delete)
4. **Quality gate** : CI hook qui refuse tout guide < 6K chars (anti-token-economy enforcement)

---

**Status** : DRAFT v3 (Antigravity Premium Standard) — créé par Claude Code (A2) sur directive A0 (escalade D7 légitime 2026-06-19). Objectif : aligner la qualité des guides `/youtube-to-guide` sur le standard Antigravity existant (6-16K chars, 8 sections sémantiques) plutôt que sur la version superficielle v2 (2.5K chars, bullets plats).
---

## ⚡ §Trio — Routage des 3 skills YouTube (ajout 2026-07-02, anti-doublon)

| Skill | Rôle | Output |
|---|---|---|
| `/youtube-to-para` | ENTRÉE du funnel : ingestion batch + handoff insights + ADR drafts | `wiki/hand_offs/youtube_ingest_<date>/` + `_SPECS/ADR/` |
| **`/youtube-to-guide`** (CE skill) | DISTILLATION Premium par vidéo (Antigravity 6-16K) | `01_Guides/<0X_DOMAIN>/` |
| `/youtube-takeout-to-lifeos` | CAPTURE bulk mécanique du takeout | `09_Life_OS/LDxx_*/` |

**Mode transcript-in-chat (prouvé run 2026-07-02)** : quand A0 colle le transcript en chat, skip Étapes 1-2 (capture/transcription) — `id: YT-UNKNOWN-<slug>`, `duration: "UNKNOWN"`, `source_note:` = « transcript fourni par A0 in-chat <date> ». JAMAIS de video_id inventé. Ajouter `sister:` vers la capture légère `09_Life_OS/LDxx` si elle existe. Run de référence : 4 guides loops `03_IT/2026-07-02_*.md` (10,4-11,6K chars chacun, 8 sections complètes).

---

## §6 — B1 Jerry Gating (ajout 2026-07-06, le « permanent fix gated » des 4 _INDEX.md — GO A+ ce jour)

> Sisters : `PRD-B1-FILTER-M3-001` · `ADR-L2-BDLD-MAP-001` §D3 (bijection RATIFIED) · skill `/b1-filter`.

**Règle** : aucun guide ne naît sans son bloc B1 complet. À l'Étape frontmatter, remplir OBLIGATOIREMENT :

```yaml
domain: 0X_<Domain>            # choisi par CONTENU (goulot business, pas sujet de surface)
ld: <valeur EXACTE de la table §"8 Domaines" corrigée ci-dessus>   # lookup, pas jugement
b2_owner: <flash-product|batman-ops|cyborg-it|wonderwoman-finance|johnjones-sales|superman-growth|aquaman-legal|greenlantern-people>
sister_b1: jerry-prime         # ou summers-nexus-omk|summers-solaris-aaas|summers-orbiter-abc si projet aval explicite
b1_reason: "<1 ligne : pourquoi CE domaine>"
```

1. **Le seul jugement est `domain:`** (quel goulot business le guide adresse). `ld:` et `b2_owner:` sont
   des LOOKUPS de la table — les inventer/deviner = violation. En cas de doute entre 2 domaines :
   celui du goulot, pas du sujet (vidéo outil-IA dont la leçon est le pricing → 04_Finance, pas 03_IT).
2. **Si le bloc ne peut pas être rempli** (contenu illisible, hors périmètre) → `status: UNFILTERED` +
   le guide sera rattrapé par `/b1-filter` (sweep déterministe E1 + classification M3 E2).
3. **ICP-gate aval** : si le guide sert un Project précis (défaut : `omk-nexus-coaching-premium`),
   l'ajouter en `downstream_project:`.
4. **Interdit** : reprendre l'ancien mapping positionnel (01→LD01…) — supersedé ce jour, la table
   corrigée + `ADR-L2-BDLD-MAP-001` §D3 font foi.
