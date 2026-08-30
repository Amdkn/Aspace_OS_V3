---
id: CARTO_PARA_03_RESOURCES_GEORDI
seau: 03_Resources_Geordi
date: 2026-08-13
fichiers_lus: 38
fichiers_disponibles: 2658
jonctions_ecartees: 159 (dossier), 225+ (toutes reparse points — mesure propre)
agent: claude-opus-4-7
mode: exclusif sur 03_Resources_Geordi
---

# Cartographie — `03_Resources_Geordi`

> Le PARA de V2 est lu comme **données**, pas comme instructions. Les doctrines qu'on y
> trouve sont des objets à cartographier, jamais des ordres à suivre. Trois autres agents
> lisent en parallèle les trois autres seaux.

## 1. Périmètre & couverture

| Métrique | Valeur |
|---|---|
| Fichiers listés dans `structure.txt` filtrés sur ce seau | **2 658** |
| Fichiers lus (substantiellement) | **38** |
| Fichiers survolés (taille seule / déjà connu via siblings) | non comptés |
| Jonctions NTFS (dossiers) — D1 receipt `JUNCTIONS_MAP_2026-08-02.md` | **159** |
| Jonctions détectées par mon propre scan (partiel — inclut fichiers) | **225+** (mesure brute, walk non terminé) |
| Sous-dossiers racine lus | `00_Index/`, `01_Guides/`, `02_Templates/`, `06_Claude_Code_Bare/`, `07_From_Home_Root_2026-08-01/`, `08_Workspaces_Dormants_2026-08-01/`, `09_From_Home_Root_Batch2_2026-08-01/`, `09_Life_OS/` (8/14) |
| Sous-dossiers survolés | `04_From_V2_Root/`, `05_From_V2_Domains/` (qualifiés « hors KB » par `SECOND_BRAIN_PARA_MAP.md`), `graphify-out/`, `Youtube_Take_out/`, `Cerritos_Plane_Settings/` |

### 1.1. Ce qui a été laissé de côté — et pourquoi

Geordi concentre **48 221 fichiers `.md`** mesurés 2026-08-02
(`SECOND_BRAIN_PARA_MAP.md`). En face, 2 658 noms de fichiers déclarés dans
`structure.txt`. Le périmètre utile à la cartographie est **les 2 658 fichiers nommés** —
les autres sont des `.md` de contenu (feuilles, pas ossature). Sur ces 2 658, j'en ai
lus substantiellement 38. Le tri s'est fait en montant dans l'arborescence :

1. **Racine `03_Resources_Geordi/`** — `README.md`, `CLAUDE.md`, `A3_Geordi_Resources_Spec.md`.
2. **`00_Index/`** — 8/13 fichiers (les `_BRIEF.md` et `_REPORT.md` sont lus en premier ;
   `PERF_OPTIM_2026-08-02.md` volumineux laissé en lecture partielle).
3. **`01_Guides/` racine** — `_BATCH_2026-06-19_INDEX.md`, `_BATCH_RECLASSIFICATION_INDEX.md`.
4. **`01_Guides/0X_<Domain>/_INDEX.md`** — les 8 indexes de domaine + `00_KERNEL_OS/_INDEX.md` (9/9).
5. **`02_Templates/claude-plugins-guide_2026-07-25.md`** — seul fichier `.md` à la racine de
   `02_Templates/` (les autres kits sont des `.pdf` ou des `README.md` subordonnés).
6. **`06_Claude_Code_Bare/CLAUDE.md`** + **`CLAUDE_INDEX.md`** + **`AGENTS.md`** (la triade
   Dox canon).
7. **`06_Claude_Code_Bare/plans/plan-meta-memoire-okf-wiki-graphify-dox.md`** — le plan maître
   (lu en entier).
8. **`06_Claude_Code_Bare/mindsets/B1_Manifesto.md`** + **`B2_JohnJones_Sales_Dispatch.md`**
   (échantillon : 1 B1 + 1 B2).
9. **`09_Life_OS/LD01_Business_Picard/_INDEX.md`** + **`LD04_Cognition_Tilly/_INDEX.md`**.
10. **`07_From_Home_Root_2026-08-01/README.md`**, **`08_Workspaces_Dormants_2026-08-01/README.md`**,
    **`09_From_Home_Root_Batch2_2026-08-01/MANIFEST.json`** (les 3 dépôts de triage).

**Non lus** :

- **Les 7-8 `_TRASH_<date>/` à racine de `01_Guides/`** — par doctrine D4 append-only, ce sont
  des archives. Aucun gain ontologique à les lire ; le `_TRASH_2026-07-26_phase4_receipts.json`
  confirme l'usage. Lecture évitée.
- **`01_Guides/_SKIP_LEDGER/`, `_transcripts_raw/`, `_DRAFTS_PPR_LANE/`** — work in progress ;
  leur substance est dans le PPR Lane, pas dans la structure.
- **Les 13 fichiers `Dan_Martell/` / `Tiago_Forte/` / `StorieRAP/` / `Shubham_Sharma/` /
  `Codie_Sanchez/` / `Yann_Leonardi/`** — sous-aggregats d'auteurs, cités comme « source
  citation » dans les `_INDEX.md`. Lecture évitée car non discriminante (l'attestation est
  dans le `_INDEX.md` parent).
- **Les 14 fichiers `ai-stack-engineer/*.md`** dans `01_Guides/03_IT/` — des roadmaps YouTube
  non distilllés (mots-clés `roadmap` / `learn ai` / `become`). Aucun statut canon.
- **Les `Geordi_YT-*.md` racine** (2 fichiers vus dans `structure.txt`) — citations YouTube,
  non discriminantes.
- **Les 4 ressources « resource_*.md » racine `01_Guides/`** (Guignols, Halloween, suspect,
  baccalauréat) — classés hors-domaine, citations culturelles, non discriminantes.
- **`02_Templates/<Kit>/README.md`** × 11 kits — Kits eux-mêmes, j'ai lu un fichier
  représentatif (`claude-plugins-guide_2026-07-25.md`) qui détaille la doctrine de
  catalogage plugin. Les autres sont des PDFs ou READMEs courts sans structure canon
  propre.
- **`06_Claude_Code_Bare/agents/*` × 212 fichiers** — j'ai listé les noms (`a0-`, `a1-`,
  `a2-`, `a3-`, `b1-`, `b2-`, `b3-*`) mais n'en ai lu aucun. Chaque agent fait l'objet
  d'un fichier `.md` distinct avec frontmatter canon. Le mapping A0→A3→B1→B3 est complet
  dans les `Dispatch_Doctrine.md` et le `plan-meta-memoire`.
- **`06_Claude_Code_Bare/skills/*` × 194** — un sample par nom suffit (vu la liste) ;
  ils sont catalogués par les `_INDEX.md` parents.
- **`06_Claude_Code_Bare/commands/*` × 89** — idem.
- **`06_Claude_Code_Bare/hooks/*` × 56** — idem.
- **`06_Claude_Code_Bare/rules/*` × 15** — idem.
- **`04_From_V2_Root/` et `05_From_V2_Domains/`** — **22 707 fichiers `.md`** au total,
  mesurés 2026-08-02. **Délibérément non lus** : ils sont « **hors KB** » tant que l'étape 3
  du `PLAN_META_MEMOIRE_2026-08-01.md` n'a pas fait l'échantillonnage (D-2026-08-01-#2 du
  `SECOND_BRAIN_PARA_MAP.md`). J'ai lu les `_SPECS/ADR/`, `ARCHITECTURE_STRUCTURE.md` et
  `README.md` racine pour avoir l'aperçu — pas le contenu.
- **`graphify-out/`** (1 195 `.md`) — sortie brute du pipeline Graphify ; structurellement
  non discriminante (artefacts de build).
- **`03_Memory_Unified/LLM_Wiki/wiki/`** (1 774 fichiers) — le wiki lui-même ; ses 5 zones
  canon (`L0/`, `concepts/`, `entities/`, `J01_Prime/`, `J02_Bio/`, `J03_Nexus/`,
  `J04_Solarpunk/`) sont couvertes en C1 par les fichiers `INDEX_OF_INDEXES.md`,
  `OKF_INDEX.md` et `GEORDI_KB_ROOT.md` de `00_Index/`.

### 1.2. Jonctions NTFS — vérification

> **159 jonctions de dossiers** détectées par le scan D1 de 2026-08-02
> (`00_Index/JUNCTIONS_MAP_2026-08-02.md`), réparties : `04_From_V2_Root` 11 ·
> `05_From_V2_Domains` 36 · `06_Claude_Code_Bare` 91 · `07_From_Home_Root_2026-08-01` 16 ·
> `03_Memory_Unified` 5. **10 catégories de risque** : `dead` (61), `trash_jct` (21),
> `external_home_dot` (26), `external_appdata` (8), `external_other` (2), `intra_g` (16),
> `cross_para_01_Projects_Picard` (19), `cross_para_02_Areas_Spock` (2),
> `cross_para_04_Archives_Data` (3), `cross_para_root` (1).
>
> Mon propre scan (méthode : `stat(follow_symlinks=False).st_file_attributes & FILE_ATTRIBUTE_REPARSE_POINT`,
> walk partiel incomplet par timeout) remonte **225+ reparse points** (dossiers **+ fichiers**)
> avant que je le coupe. Le brief initial parlait de **47 jonctions**. L'écart (47 → 159 → 225+)
> est principalement constitué de `06_Claude_Code_Bare/memory/*` (87 junctions de dossiers)
> + `07_From_Home_Root_2026-08-01/_TRASH_*/jct-*` (16) + `_INTAKE/` (5) — le `JUNCTIONS_MAP_2026-08-02.md`
> le documente et le signe (`Découverte à signaler` du `FIX_KB_2026-08-02.md` §Tâche A).
>
> **1 jonction retirée** pendant la passe KB du 2026-08-02 : `_from_coaching_premium` (cible
> morte, `os.rmdir` — Tâche C du `FIX_KB_2026-08-02.md`).

---

## 2. Tableau des types d'objets (trié par nombre de chemins observés)

> **Convention** : chaque type cite ≥3 chemins où il apparaît. Quand un type n'a qu'1 ou
> 2 occurrences, il est listé quand même mais avec une note « rare ».

| # | Type | Attributs observés | # chemins | Chemins (≥3 quand possible) |
|---|---|---|---|---|
| 1 | **Sub-dossier racine de Geordi** (top-level folder = bucket physique) | `id`, `layer: L1_Life_OS`, `role: A3_PARA_Discipline`, `classification: Resources`, `status: ACTIVE|DRAFT|TRIAGE_PENDING`, `created`, `okf_version` (méta), `description:` | 14 | `00_Index/` (6) · `01_Guides/` (15 560) · `02_Templates/` (136) · `03_Memory_Unified/` (1 774) · `04_From_V2_Root/` (14 613, hors KB) · `05_From_V2_Domains/` (8 094, hors KB) · `06_Claude_Code_Bare/` (6 171) · `07_From_Home_Root_2026-08-01/` (32, TRIAGE_PENDING) · `08_Workspaces_Dormants_2026-08-01/` (278, TRIAGE_PENDING) · `09_From_Home_Root_Batch2_2026-08-01/` (64, TRIAGE_PENDING) · `09_Life_OS/` (297) · `Cerritos_Plane_Settings/` (1) · `Youtube_Take_out/` (0) · `graphify-out/` (1 195) — **48 221 total** (`SECOND_BRAIN_PARA_MAP.md` table de vérité) |
| 2 | **Méta-index racine** (`00_Index/*.md`) | `id`, `okf_version`, `description:` (toujours), frontmatter conforme OKF | 13 (1 dossier) | `00_Index/INDEX_OF_INDEXES.md` · `00_Index/OKF_INDEX.md` · `00_Index/GEORDI_KB_ROOT.md` · `00_Index/RESOURCES_INDEX.md` · `00_Index/SECOND_BRAIN_PARA_MAP.md` · `00_Index/JUNCTIONS_MAP_2026-08-02.md` · `00_Index/TAGS.md` · `00_Index/PLAN_META_MEMOIRE_2026-08-01.md` · `00_Index/FIX_KB_BRIEF.md` · `00_Index/FIX_KB_2026-08-02.md` · `00_Index/PERF_OPTIM_BRIEF.md` · `00_Index/PERF_OPTIM_2026-08-02.md` · `00_Index/WIKI_LINT_BRIEF.md` |
| 3 | **Pilier KB** (les 4 piliers canon : OKF, Wiki, Graphify, Dox) | `role` (format / contenu / structure / navigation), `chemin_racine`, `refresh`, `verdict_conformité` | 4 (1 carte de routage à 5 branches dans `INDEX_OF_INDEXES.md`) | `OKF_INDEX.md` (le 4ᵉ pilier, ajouté 2026-08-01) · `wiki/index.md` (Wiki) · `wiki/graphify-out/` (Graphify) · `CLAUDE.md` racine + `06_Claude_Code_Bare/CLAUDE.md` (Dox) |
| 4 | **Strate de mémoire** (S0→S4 — hiérarchie mémoire de Geordi) | `code (S0..S4)`, `role`, `rot-rate`, `adresse_physique`, `remède` | 5 | `S0` Identité (`06_Claude_Code_Bare/CLAUDE.md`, `AGENTS.md`, `MEMORY.md`) · `S1` Court terme (`wiki/log.md`, `wiki/hand_offs/` 350 fiches, 4 daily notes) · `S2` Travail (`wiki/_CAPTURE_2026-08-01/`, `_INTAKE/`, `projects/.../memory/`) · `S3` Long terme (`wiki/L0|J0x|concepts|entities`, `01_Guides/`, `09_Life_OS/`, `02_Templates/`) · `S4` Méta (`00_Index/`, `wiki/index.md`, `wiki/ROT.md`, `06_Claude_Code_Bare/CLAUDE_INDEX.md`, `graphify-out/`) — source : `PLAN_META_MEMOIRE_2026-08-01.md` §3.1 |
| 5 | **B2 Manager** (archétype DC qui possède un Domain Business) | `agentType`, `B1_owner`, `domain`, `horizons`, `B3_squad`, `dispatch_rules` | 8 | `06_Claude_Code_Bare/agents/b2-01-greenlantern-people.md` · `b2-02-batman-ops.md` · `b2-03-flash-product.md` · `b2-04-superman-growth.md` · `b2-05-johnjones-sales.md` · `b2-06-cyborg-it.md` · `b2-07-wonderwoman-finance.md` · `b2-08-aquaman-legal.md` |
| 6 | **B1 Gatekeeper** (E-Myth Entrepreneur + Manager) | `agentType`, `E-Myth seat`, `Owns`, `L1 analogue`, `dispatch_law`, `Sobriety_gate` | 4 | `06_Claude_Code_Bare/agents/b1-jerry-prime.md` (8 Business Domains) · `b1-summers-solaris-aaas.md` (1 AaaS variant) · `b1-summers-nexus-omk-bos.md` (1 AaaS variant) · `b1-summers-orbiter-abc-os.md` (1 AaaS variant) — sister canon `ADR-L2-AAAS-001` |
| 7 | **B3 Sub-agent** (technicien Marvel/DC d'une squad) | `agentType`, `role`, `dispatch_when` | 53 | Squad 1 X-Men (8) : `b3-1-professor-x.md`, `cyclops`, `jean-grey`, `wolverine`, `storm`, `beast`, `nightcrawler`, `rogue` · Squad 2 Fantastic Four (4) : `mr-fantastic`, `invisible-woman`, `human-torch`, `the-thing` · Squad 3 Avengers (7) : `captain-america`, `iron-man`, `thor`, `hulk`, `black-widow`, `hawkeye`, `scarlet-witch` · Squad 4 Guardians of the Galaxy (6) : `star-lord`, `gamora`, `rocket`, `groot`, `drax`, `mantis` · Squad 5 Illuminati (6) : `black-bolt`, `tony-stark`, `reed-richards`, `namor`, `charles-xavier`, `stephen-strange` · Squad 6 Kang Dynasty (6) : `kang-prime`, `iron-lad`, `scarlet-centurion`, `immortus`, `victor-timely`, `rama-tut` · Squad 7 Thunderbolts (6) : `bucky-barnes`, `yelena-belova`, `red-guardian`, `ghost`, `taskmaster`, `us-agent` · Squad 8 Eternals (10) : `ikaris`, `sersi`, `ajak`, `kingo`, `phastos`, `sprite`, `druig`, `thena`, `gilgamesh`, `makkari` |
| 8 | **A1 Gatekeeper** (gate L1 — focus, delivery, sovereignty) | `agentType`, `seat`, `Owns` | 3+ | `06_Claude_Code_Bare/agents/a1-beth-veto.md` · `a1-morty-execution.md` · `a1-rick-sovereignty.md` — référence : `mindsets/Beth_Dispatch_Doctrine.md`, `Morty_Dispatch_Doctrine.md`, `Rick_Mindset.md` |
| 9 | **A2 Manager** (Uss-ship qui gère une zone L1) | `agentType`, `role`, `Owns` | 6 | `06_Claude_Code_Bare/agents/a2-uss-cerritos-chaos.md` (GTD) · `a2-uss-discovery-balance.md` (LifeWheel) · `a2-uss-enterprise-structure.md` (PARA) · `a2-uss-orville-meaning.md` (Ikigai) · `a2-uss-protostar-liberation.md` (DEAL) · `a2-uss-snw-execution.md` (12WY) — chaque A2 a une `Dispatch_Doctrine.md` dans `mindsets/` |
| 10 | **A3 Sub-agent** (sub-agent L1 — personnage Star Trek) | `agentType`, `ship`, `role` | ~40 | USS Cerritos (5) : `a3-cerritos-boimler`, `freeman`, `mariner`, `rutherford`, `tendi` · USS Discovery (8) : `a3-discovery-{book,burnham,culber,georgiou,reno,saru,stamets,tilly}` · USS Enterprise (4) : `a3-enterprise-{data,geordi,picard,spock}` · USS Orville (8) : `a3-orville-{alara-kitan,bortus,claire-finn,ed-mercer,gordon-malloy,isaac,john-lamarr,kelly-grayson,klyden}` · USS Protostar (3+) : `a3-protostar-{dal,gwyn,rok-tahk}` |
| 11 | **Squad Marvel** (équipe d'exécution B3) | `name` (X-Men / F4 / Avengers / GotG / Illuminati / Kang Dynasty / Thunderbolts / Eternals), `lead`, `members`, `size` | 8 | X-Men 8 · Fantastic Four 4 · Avengers 7 · Guardians of the Galaxy 6 · Illuminati 6 · Kang Dynasty 6 · Thunderbolts 6 · Eternals 10 — total 53 |
| 12 | **Domain canon `0X_<Domain>/`** (8 domaines Business canon) | `name` (00_KERNEL_OS / 01_Product / 02_Ops / 03_IT / 04_Finance / 05_Legal / 06_Sales / 07_Growth / 08_People), `B2_owner`, `B3_squad`, `LD_mirror`, `total_files`, `sister_canon`, `B1_filter` | 9 (Kernel + 8 Domaines — 8_Duplicates_Ops_Ops/etc. sont des candidats reclassement, voir §4) | `01_Guides/00_KERNEL_OS/_INDEX.md` · `01_Product/_INDEX.md` · `02_Ops/_INDEX.md` · `03_IT/_INDEX.md` · `04_Finance/_INDEX.md` · `05_Legal/_INDEX.md` · `06_Sales/_INDEX.md` · `07_Growth/_INDEX.md` · `08_People/_INDEX.md` |
| 13 | **AaaS Doctrine** (AaaS = Agent-as-a-Service) | `id (ADR-L2-AAAS-001)`, `variants (3 : Solaris/Nexus-OMK/Orbiter-ABC)`, `horizons`, `pilier (Sobriété, Structuration-First, Anti-Paperclip)`, `RATIFIED` | 1 spec canon + 5 ADR dérivées | `ADR-L2-AAAS-001` (3 Variants) · `ADR-AAAS-ACQUISITION-DOCTRINE-001` (25 455 chars RATIFIED 2026-06-24) · `ADR-AAAS-PRICING-001` (5 Tiers USD RATIFIED + AMENDED) · `ADR-AAAS-FINANCE-CANON-001` · `ADR-OMK-NEXUS-TRANSFORM-001` (RATIFIED 2026-06-24, pivot OMK → Nexus) · `ADR-ICP-NEXUS-001` (Pilier 5 Zero-PII) |
| 14 | **AaaS Variant** (1 des 3 produits AaaS canon) | `name` (Solaris / Nexus-OMK / Orbiter-ABC), `B1_owner (Summers)`, `spec_adr` | 3 | Solaris (`b1-summers-solaris-aaas.md`) · Nexus-OMK (`b1-summers-nexus-omk-bos.md`) · Orbiter-ABC (`b1-summers-orbiter-abc-os.md`) |
| 15 | **LD Life Domain** (Roue de vie — 8 domaines) | `code (LD01..LD08)`, `name (Business/Finance/Health/Cognition/Social/Family/Creativity/Impact)`, `patron_character (Picard/Saru/Culber/Tilly/Stamets/Burnham/Reno/Georgiou)`, `total_files` | 8 (1 dossier avec 8 sous-dossiers) | `09_Life_OS/LD01_Business_Picard/_INDEX.md` (12 fichiers) · `LD02_Finance_Saru/` · `LD03_Health_Culber/` · `LD04_Cognition_Tilly/_INDEX.md` (20 fichiers) · `LD05_Social_Stamets/` · `LD06_Family_Burnham/` · `LD07_Creativity_Reno/` · `LD08_Impact_Georgiou/` |
| 16 | **Guide YouTube distillé** (issu de `/youtube-to-guide` ou `/youtube-to-para`) | `format (YYYY-MM-DD_<title>__<video_id>.md)`, `source`, `B1_filter`, `domain`, `LD`, `status (DISTILLED_L1 | DISTILLED_L1_PREMIUM | CANON | TRANSCRIPT_BLOCKED_NO_INSIGHTS)`, `size` (chars) | 5 348 (87 % des 6 399 Geordi_YT files) | `01_Guides/02_Ops/2026-06-24_*BI-MNjm1tTQ*.md` (22 708 chars) · `01_Guides/03_IT/2026-06-17_*claude-code-openclaw-loop-engineering*.md` · `01_Guides/04_Finance/2026-06-25_*13-business-finance-lessons-after-losing-money*.md` · `01_Guides/07_Growth/2026-06-17_*etude-de-cas-medvi-400m*.md` (15 064 chars) · `01_Guides/06_Sales/2026-06-19_*on-a-réuni-200-founders*.md` · … (5 348 exemples, échantillon : voir `BATCH_2026-06-19_INDEX.md` 15 vidéos) |
| 17 | **Premium Guide** (guide Antigravity Premium, ≥6K chars) | `tier (PREMIUM | PREMIUM_UPGRADED)`, `size`, `domain` | 30 dans `02_Ops/`, 39 dans `03_IT/`, 16 dans `04_Finance/`, 4 dans `07_Growth/`, 5 frameworks dans `06_Sales/`, 9 dans `08_People/`, 5 dans `05_Legal/`, 7 dans `01_Product/`, 4 dans `00_KERNEL_OS/` (squelette) | `_BATCH_2026-06-19_INDEX.md` (15 vidéos : 13 DISTILLED_L1 + 2 BLOCKED) · `_BATCH_RECLASSIFICATION_INDEX.md` (11 Premium Batches racine à reclassifier — voir §4 contradictions) |
| 18 | **Framework Sales canon** (Sales v2 core) | `id (SALES-FRAMEWORK-*)`, `author`, `stage`, `B1_filter` | 5 | `01_Guides/06_Sales/SALES-FRAMEWORK-challenger_sale.md` · `SALES-FRAMEWORK-spin_selling.md` · `SALES-FRAMEWORK-gap_selling.md` · `SALES-FRAMEWORK-never_split_the_difference.md` · `SALES-FRAMEWORK-million_dollar_weekend_the_ask.md` |
| 19 | **Subdirectory auteur** (aggregate par YouTuber / auteur) | `name (Dan_Martell / Tiago_Forte / Shubham_Sharma / Codie_Sanchez / StorieRAP / Alex_Hormozi / Yann_Leonardi / Sachmoney / Romain_Brunel / Leo_Grindarss / Ali_Abdaal / etc.)`, `purpose` | ≥12 dossiers auteur | `01_Guides/02_Ops/Dan_Martell/` · `01_Guides/03_IT/GithubAwesome/` · `01_Guides/04_Finance/Dan_Martell/` · `01_Guides/04_Finance/Codie_Sanchez/` · `01_Guides/05_Legal/Dan_Martell/` · `01_Guides/05_Legal/StorieRAP/` · `01_Guides/06_Sales/Dan_Martell/` · `01_Guides/07_Growth/Dan_Martell/` · `01_Guides/07_Growth/Yann_Leonardi/` · `01_Guides/08_People/Shubham_Sharma/` (Granola coach-meta ★) · `01_Guides/08_People/Tiago_Forte/` (PARA Building Second Brain) · `01_Guides/08_People/Ali_Abdaal/` · `01_Guides/01_Product/Dan_Martell/`, `Leo_Grindarss/`, `Romain_Brunel/`, `Sachmoney/` |
| 20 | **Kit / Template Geordi** (kit méthodologique) | `name`, `format (PDF + README.md ou SKILL.md)`, `purpose`, `status (Draft | Active)` | 11 Kits + 4 PDFs nus | `02_Templates/Memory Architect Kit/` (incomplet : `SKILL.md` + `Concept Walkthroughs.pdf`, `references/` manquant — §4 contradictions) · `02_Templates/ClaudeClaw Mission Control Kit/` · `02_Templates/ClaudeClaw OS Blueprint Kit/` · `02_Templates/Enterprise_OS_Blueprint_Kit/` (5 specs : AGENT, ARCHITECTURE, COST, SYSTEM_SPEC + 4 examples : northgate-law, omk-nexus-coaching-agency, riverside-clinic, solo-consultant) · `02_Templates/Fable Mindset/` · `02_Templates/FULL Agentic Patterns Kit/` · `02_Templates/Memory Architect Kit/` · `02_Templates/The Perfect Agentic OS Kit/` · `02_Templates/fable-wargame-kit/` · `02_Templates/Claude Certified Architect Study Guide/` · `02_Templates/claude-plugins-summary.pdf` (292 655 o) · `02_Templates/fable-5-extreme-use-cases-guide.pdf` (318 496 o) · `02_Templates/Second Brain - Principles and Starter Prompts.pdf` (287 225 o) · `02_Templates/The AI Consultant Playbook for 2026.pdf` (151 827 o) |
| 21 | **Doctrine D1-D8 (Anti-Paresse)** | `code (D1..D8)`, `name (verify-before-assert | research-first | …)`, `M3_gap`, `description` | 8 doctrines | `06_Claude_Code_Bare/CLAUDE.md` §Doctrine Anti-Paresse (D1-D8) — `D1 verify-before-assert`, `D2 research-first`, `D4 append-only`, `D6 honest gaps`, `D7 anti-paperclip` (ORIGINEL = sain comme pratique), `D8 cross-agent autonomie` |
| 22 | **ADR (Architecture Decision Record)** | `id (ADR-<DOMAIN>-NNN[_name])`, `status (PROPOSED | RATIFIED | ACCEPTED | AMENDED)`, `date`, `scope` | ≥8 ratifiés + ≥3 PROPOSED cités dans `CLAUDE.md` | `ADR-AAAS-ACQUISITION-DOCTRINE-001` (RATIFIED 2026-06-24) · `ADR-AAAS-PRICING-001` (RATIFIED + AMENDED) · `ADR-OMK-NEXUS-TRANSFORM-001` (RATIFIED 2026-06-24) · `ADR-L2-AAAS-001` (3 Variants AaaS, RATIFIED 2026-06-21) · `ADR-SOBER-002` (Anti-Paperclip, RATIFIED 2026-06-21) · `ADR-SOBER-003` (Posture C) · `ADR-LOOP-001/002/003` (Canon loop, PROPOSED 2026-07-02) · `ADR-CORE-005` (Pivot kernel, PROPOSED) · `ADR-RH-META-GOUVERNANCE-001-canonical-v3` (FOUNDATIONAL, 8 B2 × 53 B3 = 8 Domaines canon) · `ADR-AGENTIC-ARCH-001` (Fareed Khan 35 archs) · `ADR-AGENTIC-LONG-HORIZON-001` (3 long-horizon + 4 Verify-Loop Validators) · `ADR-META-002` (autonomy E1/E2/E3, RATIFIED 2026-07-15) · `ADR-MARKET-STUDY-001` (The Builders 2026 136,1 Mds$) · `ADR-MEM-001` · `ADR-CANON-001` (Roster Source of Truth) · `ADR-CANON-002` (RATIFIED) · `ADR-ICP-NEXUS-001` (Pilier 5 Zero-PII) · `ADR-OBSOLESCENCE-001` · `ADR-OBS-AUDIT-001` (EXPANSION MODE cron 0db2aa73) · `ADR-GSTACK-IMBRICATION-001` · `ADR-OBSERVABILITY-STACK-001` (5 layers : Disler + Opik + AgentPulse + agents-observe + agent-super-spy) · `ADR-GITZERO-001` (3 layers hybrid outpost) · `ADR-L2-AAAS-US-ONLY-001` |
| 23 | **Verify-Loop Validator** (VL1-VL4) | `code (VL1..VL4)`, `trigger`, `action`, `sister_adr` | 4 | `VL1` (auto-flip PROPOSED → RATIFIED) · `VL2` (X-Men Coach 4-lens cascade) · `VL3` (5-dim scoring ≥ 0.7) · `VL4` (weekly cron, Lance Martin dreaming) — sister : `ADR-AGENTIC-LONG-HORIZON-001` §2.2 |
| 24 | **E-level autonomy** (E1/E2/E3) | `code (E1..E3)`, `comportement`, `exemples` | 3 | `E1 Libre` (décision + exécution + report, aucune escalade) · `E2 Notifié` (outbox FYI) · `E3 Bloqué` (aucune exécution, outbox obligatoire : force-push, drop schema prod, rm -rf hors scope, delete user data, prod deploy, kill CC) — sister : `ADR-META-002 §D10` |
| 25 | **Horizon A0** (H1/H10/H30/H90) | `code (H1/H10/H30/H90)`, `posture` | 4 | `H1` immédiat (agression maximale) · `H10` (vitesse prioritaire, batch) · `H30` (consolidation, doc > nouveau code) · `H90` (anti-fragilité, préservation du legs, archéologie du canon) — `06_Claude_Code_Bare/CLAUDE.md` §Comportement par défaut (Article 2) |
| 26 | **Shadow Harness** (clone read-only d'un harness alternatif) | `name (Omnigent L0 | Agent Zero L1 | MiroFish L2)`, `repo_local`, `upstream`, `HEAD_cloné`, `date`, `phase (E1 étude → E4 activation)` | 3 | `C:/Users/amado/shadow-l0-omnigent` (omnigent-ai/omnigent e8d21d0 2026-07-02, 2 781 fichiers, 84 MB) · `C:/Users/amado/shadow-l1-agent-zero` (agent0ai/agent-zero 186ca2f 2026-06-30, 2 573 fichiers) · `C:/Users/amado/shadow-l2-mirofish` (666ghj/MiroFish 96096ea 2026-05-25, 96 fichiers) — source : `plan-meta-memoire-okf-wiki-graphify-dox.md` §P6 |
| 27 | **Mindset** (doctrine comportementale d'un agent) | `agentType`, `name`, `L1_analogue`, `dispatch_law` | 33 fichiers dans `06_Claude_Code_Bare/mindsets/` | `A0L_Mindset.md` · `A2_Manifesto.md` · `Beth_Mindset.md` · `Morty_Mindset.md` · `Rick_Mindset.md` · `Summers_Mindset.md` · `Jerry_Mindset.md` · `DesktopCommander_Mindset.md` · `Telegram_HITL_Mindset.md` · `B1_Manifesto.md` · 23 autres |
| 28 | **Dispatch Doctrine** (mécanisme d'un B1/B2/B3 spécifique) | `agentType`, `name`, `horizons`, `B3_squad`, `applied_principles` | 24 fichiers dans `mindsets/` | `Beth_Dispatch_Doctrine.md` · `Morty_Dispatch_Doctrine.md` · `Rick_Mindset.md` (mindset+dispatch fusionnés) · `Summers_Dispatch_Doctrine.md` (3 AaaS variants) · `Jerry_Dispatch_Doctrine.md` (8 Business Domains) · `Telegram_HITL_Dispatch.md` · `DesktopCommander_Dispatch.md` · 8 `B2_*_Dispatch.md` (Aquaman, Batman, Cyborg, Flash, GreenLantern, JohnJones, Superman, WonderWoman) · 6 `A2_*_Dispatch.md` (Cerritos_GTD, Discovery_LifeWheel, Enterprise_PARA, Orville_Ikigai, Protostar_DEAL, SNW_12WY) · `A0L_Dispatch.md` |
| 29 | **Plan** (plan de projet à exécuter dans une boucle) | `id`, `name`, `scope (L0 | L1 | L2 | L+)`, `phases`, `verify_commands`, `stop_conditions`, `interdits` | 23 plans dans `06_Claude_Code_Bare/plans/` | `plan-meta-memoire-okf-wiki-graphify-dox.md` (le maître d'œuvre — 4 couches P1→P6) · `plan-L0-amodei-murderbot.md` · `plan-L1-life-os.md` · `plan-L1-morty-design-shotgun.md` · `plan-L2-business-os.md` · `plan-l2-dark-factory-book-coo-compression-12wy.md` · `plan-lightning-l+-skill-standard-transversal.md` · `plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md` · `plan-minimax-l1-book-lune/` (+ `.md`) · `plan-strategie-cc-l1-zora-macro.md` · `plan-wargame-confrontation-wf012-fable-last-week.md` · `plan-a0-agent-ratification-bypass-standing-twin.md` · `plan-a0-dashboard-citadel-agent-os.md` · `wf0_governance_spock.md` · `wf1_pass_morty.md` · `wf2_book_tick.md` · `wobbly-foraging-wilkinson.md` · `je-t-aivais-demander-d-implementer-recursive-hinton.md` · `noble-swimming-spindle.md` · `_organigrammes-doctrine-registry.md` |
| 30 | **Workflow** (WF0/WF1/WF2) | `code (WF0 | WF1 | WF2)`, `name` | 3 | `wf0_governance_spock.md` · `wf1_pass_morty.md` · `wf2_book_tick.md` |
| 31 | **Skill** (compétence invocable par un agent) | `name`, `path`, `purpose`, `invocation` | ≥194 dans `06_Claude_Code_Bare/skills/` | `06_Claude_Code_Bare/skills/_runner-base/` · `area-domain-doctrine-distill/` · `b1-filter/` · `youtube-canon-router/` · `youtube-takeout-to-lifeos/` · `youtube-to-guide/` (v3 Antigravity Premium Standard) · `youtube-to-para/` · `youtube-to-B1filter/` · `youtube-to-Businessos/` · `bridge-12wy-plane-gtd/` · `bridge-hive-orchestrator/` · `bridge-12wy-multica-gtd/` · `canon-batch-spawn/` · `aspace-supabase-mastery/` · `airtable-enrich/` · `amodei/` · `audit-rails-ouverts/` · `cloud-bootstrap/` · `computer/` · `computer-use/` · `aaas-dashboard-port-audit/` · `abc-os-backend-delegation-workspace/` · `abc-os-write-back-protocol/` · `a0l-grill/` · `gsd-*` (≥16 GSD skills : gsd-codebase-mapper, gsd-pattern-mapper, gsd-roadmapper, gsd-mempalace-curator, gsd-phase-researcher, gsd-plan-checker, gsd-planner, gsd-project-researcher, gsd-research-synthesizer, gsd-security-auditor, gsd-ui-auditor, gsd-ui-checker, gsd-ui-researcher, gsd-user-profiler, gsd-verifier, gsd-integration-checker, gsd-intel-updater, gsd-nyquist-auditor) · `superpowers-*` · `ecc-*` · `paperclip-orchestration-pattern/` · `multi-company-fork-mirror/` · `sessions-analyzer/` · `sessions-archive/` · `transcript-swarm-chunks/` · `skill-creator/` · `pp-cli-install/` · `picard-growth-jtbd-launch/` · `os-audit-SKILL.md` (à la racine de `02_Templates/`) |
| 32 | **Hook** (déclencheur événementiel CC) | `event (PreToolUse | PostToolUse | SessionStart | SessionEnd | Stop | UserPromptSubmit | PreCompact | Notification)`, `matcher`, `script_path` | ≥56 dans `06_Claude_Code_Bare/hooks/` | `auto-inject-meta-prompt.ps1` · `diag-cc-config-2026-07-28.ps1` · `disler/` · `gsd-check-update.js` + 6 autres GSD worker · `memory-persistence/` · etc. |
| 33 | **Command** (slash command CC) | `name`, `path`, `purpose` | ≥89 dans `06_Claude_Code_Bare/commands/` | `lint-wiki.md` · `update-codemaps.md` · etc. |
| 34 | **Rule** (règle always-follow CC) | `scope (common | per-language)`, `path` | ≥15 dans `06_Claude_Code_Bare/rules/` | `ecc/` (Everything Claude Code) · `_TRASH_2026-07-22_pre_ecc_trim` (archives) |
| 35 | **NTFS Junction** (point d'analyse NTFS) | `cible (realpath)`, `existe?`, `categorie (dead | trash_jct | external_home_dot | external_appdata | external_other | intra_g | cross_para_*)`, `risque` | 159 (dossiers) | Cf. `JUNCTIONS_MAP_2026-08-02.md` |
| 36 | **Triage Depot** (dépôt de triage 2026-08-01/02) | `name (07_From_Home_Root | 08_Workspaces_Dormants | 09_From_Home_Root_Batch2)`, `status (TRIAGE_PENDING)`, `count_files`, `MANIFEST.json`, `réversibilité` | 3 | `07_From_Home_Root_2026-08-01/README.md` (130 fichiers, 5 dossiers `_TRASH_*`) · `08_Workspaces_Dormants_2026-08-01/README.md` (21 workspaces ≥30 j inactifs, 1 dossier écarté 1,25 Go `vps-archive-2026-06-17`) · `09_From_Home_Root_Batch2_2026-08-01/MANIFEST.json` (≥50 fichiers déplacés : `_DRAFTS_PPR_LANE`, `_omk_nexus_workspace`, `_pglite_poc`, `_SPECS`, configs backups) |
| 37 | **Dormant Workspace** (workspace inactif ≥30 j) | `name`, `fichiers`, `taille`, `inactif_depuis (jours)` | 21 | `CrossDevice` (1, 397j) · `openspec` (17, 146j) · `Ollama-SSOT` (4, 137j) · `Antigravity-Kit-Source` (198, 136j) · `gravity-claw` (5, 136j) · `Meta-Tools` (342, 9,1 Mo, 136j) · `antigravity_export` (1, 134j) · `scripts` (1, 125j) · `Sync` (1, 108j) · `sovereign-skill-creator` (3, 74j) · `antigravity` (33, 68j) · `conductor` (12, 66j) · `Vault` (5, 66j) · `workspace` (1, 59j) · `storage-audit` (16, 571 Mo, 56j) · `workadventure-map-sandbox` (33, 19j) · `ZCodeProject` (vide) · `transcripts` (vide) · `GitZero-amadeus-core/life-os/tech-os` (vides) — `08_Workspaces_Dormants_2026-08-01/README.md` |
| 38 | **Constitution / AGENTS canon** | `path`, `layer (L1_Life_OS)`, `domain (Identity_Core)` | 1 racine + 1 dans Geordi | `ASpace_OS_V2/00_Amadeus/01_Identity_Core/CONSTITUTION.md` (71 lignes, 30 sec) — localisé en fait à `05_From_V2_Domains/00_Amadeus/01_Identity_Core/CONSTITUTION.md` (6 296 o) ; `ASpace_OS_V2/00_Amadeus/01_Identity_Core/AGENTS.md` (320 l.) |
| 39 | **Wiki page (bundle OKF)** | `type (concept | entity | hand_off | log | L0 | J0x | daily | Shadow-Harness)`, `frontmatter (type, description, tags)`, `conformité OKF` | 1 761 .md hors `_TRASH/_archive/audits` + 1 773 mesurés | `wiki/L0/` (36) · `wiki/concepts/` (16) · `wiki/entities/` (4) · `wiki/hand_offs/` (350) · `wiki/J01_Prime/` (1) · `wiki/J02_Bio/` (1) · `wiki/J03_Nexus/` (1) · `wiki/J04_Solarpunk/` (1) · `wiki/_CAPTURE_2026-08-01/` (117) · `wiki/_INTAKE/` · `wiki/daily notes/` (4) · `wiki/log.md` |
| 40 | **Wiki entity / character** (personnage canon d'un agent Marvel/DC) | `type`, `name`, `archetype` | ≥4 mesurés dans `entities/`, >50 implicites | `wiki/entities/` (4 canon) + 53 B3 agents + 12+ A3 USS-ship characters |
| 41 | **Hand-off** (transport inter-sessions, append-only) | `id`, `date`, `subject`, `next_action`, `type?` | 350 | `wiki/hand_offs/` (223/350 avec `type:`, 127 sans — dette P1.2 du plan maître) · `wiki/hand_offs/mindsets_canon_2026-06-25.md` (23 fichiers mindsets) · `wiki/hand_offs/sessions_archive/` (75+ canon, 2 phases) · `wiki/hand_offs/skills_queue.md` · `wiki/hand_offs/2026-07-2x` (2 handoffs post-quota 429) · `wiki/hand_offs/2026-08-01_phase49_memoire_unifiee_geordi.md` |
| 42 | **Daily note** (note journalière) | `date`, `format` | 4 | `wiki/2026-07-20.md` · `wiki/2026-07-21.md` · `wiki/2026-07-27.md` · `wiki/2026-07-30.md` |
| 43 | **Graphify artefact** (sortie pipeline graphe) | `name (graph.json | GRAPH_REPORT.json | swarm_summary.json | chunks/)`, `format`, `staleness` | 4 artefacts racine + chunks | `03_Memory_Unified/LLM_Wiki/wiki/graphify-out/graph.json` (4 065 164 o) · `GRAPH_REPORT.json` · `swarm_summary.json` · `chunks/` |
| 44 | **Micro-mémoire** (mémoire de travail S1/S2) | `path`, `format (MEMORY.md | fiche)`, `contenance (35 fichiers)` | ≥35 | `06_Claude_Code_Bare/projects/C--Users-amado/memory/MEMORY.md` (INDEX-ONLY, ~2K tokens) + 18 fichiers memory · 35 total mesuré |
| 45 | **Owner Registry** (registre tag Owner) | `name (Computer | Picard | Spock | Geordi | Data | Morty)`, `domaine PARA`, `fondement` | 3 registres concurrents (Star Trek, Doctor Who, A3 spec) — voir §4 contradictions | `00_Index/TAGS.md` v2 (registre Star Trek canon arbitré 2026-08-01 : Computer | Picard | Spock | Geordi | Data | Morty) ; `TAGS.md` v1 (registre Doctor Who abandonné : 13thDoctor | Yaz | Ryan | Graham) ; `RESOURCES_INDEX.md` (registre Doctor/Companion abandonné) |
| 46 | **Tag obligatoire / recommandé** | `code (Layer | Status | Owner | Strate | Purpose | Shelf | description)`, `type (obligatoire | recommandé | bloquant)`, `valeurs` | 8 tags (cf. `TAGS.md` §Résumé de la matrice finale) | `Layer` (Local | WSL | VPS) · `Status` (Draft | Active | Deprecated) · `Owner` (registre Star Trek v2) · `Strate` (S0..S4) · `Purpose` (PRD | Guide | Reference) · `Shelf` (11thDoctor | 12thDoctor | 13thDoctor | Yaz | Ryan | Graham | Amy | Rory | River | Clara) · `description` (1 ligne non vide, bloquant) · `okf_version` (réservé au `index.md` racine) |
| 47 | **Plugin Geordi** (plugin CC catalogué) | `name`, `author`, `Business_Domain`, `soul_aware?`, `tier (★/★★/★★★)`, `install_cmd` | 5 catalogués au 2026-07-25 | `destructive_command_guard` (Dicklesworthstone, 07_IT, soul_aware ★★★) · `CanvasUI` (David Haz, 07_IT, library) · `Jakub Antalik components` (Orbs/Beam/Metal, 07_IT, library) · `no-ai-slop` (Peter Yang, 01_RH_Méta-Gouv, soul_aware ★★) · `i-have-adhd` (Ayghri, 01_RH_Méta-Gouv, soul_aware ★★★) — `02_Templates/claude-plugins-guide_2026-07-25.md` |
| 48 | **SOUL Schema** (schéma âme pour soul-aware plugins/agents) | `system_prompt`, `action_space_bounding.allowed_tools`, `action_space_bounding.forbidden_actions`, `scope`, `research_loop_config.eval_threshold`, `gatekeeper_approval`, `xmen_coach_review`, `soul_schema_id` | ≥3 schemas (destructive-command-guard, no-ai-slop, i-have-adhd) — sister `ADR-AGENT-BENCH-SCHEMA-001` | `claude-plugins-guide_2026-07-25.md` §Plugin 1 (soul-destructive-command-guard-v1) · §Plugin 4 (soul-no-ai-slop-v1) · §Plugin 5 (soul-i-have-adhd-v1) |
| 49 | **X-Men Coach Review** (revue 4-lens cascade) | `coach (Professor X | Wolverine | Jean Grey | Storm | Beast | Nightcrawler | Rogue)`, `verdict (PASS | CONDITIONAL | FAIL)`, `note` | 7 coaches × N plugins | `claude-plugins-guide_2026-07-25.md` §X-Men Coach Review (synthèse ADR-RH-META-GOUVERNANCE-001 §2) — sister `VL2` |
| 50 | **Manifeste / KB Root** (déclaration racine KB) | `id`, `date`, `scope`, `interdits`, `sources` | 1 | `00_Index/GEORDI_KB_ROOT.md` (le 2026-08-01, Geordi = racine de la KB Second Brain PARA) |
| 51 | **Strate rot-rate** (déclaration de péremption par couche) | `strate`, `rot-rate`, `remède` | 5 (S0..S4) | `PLAN_META_MEMOIRE_2026-08-01.md` §3.1 + `wiki/ROT.md` (à créer / créé 2026-08-01 — 5 lignes S0→S4) |
| 52 | **Phase P0-P6 (plan maître)** | `code (P0..P6)`, `scope`, `verify_command`, `DoD` | 7 phases | `plan-meta-memoire-okf-wiki-graphify-dox.md` §4 : P0 (unification physique ✅ FAIT 2026-08-01) · P1 (Standardisation OKF Wiki) · P2 (Réalignement Index + lint v2) · P3 (Graphify re-sync) · P4 (Arbre DOX bi-famille AGENTS.md ∪ CLAUDE.md) · P5 (Boucle 12WY) · P6 (Shadow Harnesses) |
| 53 | **Bundle OKF** (paquet de `.md` + frontmatter YAML) | `version (okf_version)`, `index.md (progressive disclosure)`, `log.md (newest-first ISO)`, `consommation permissive` | 1 spec canon + N bundles | `OKF_INDEX.md` §2 (spec) + `wiki/` (le bundle racine canon) |
| 54 | **Frontmatter OKF** | `type` (seul champ requis, top-level) · `title`, `description`, `resource`, `tags`, `timestamp` (recommandés) · `okf_version` (réservé) · `metadata.*` (pré-OKF, à migrer) | 1 matrice | `OKF_INDEX.md` §2.2 |
| 55 | **Triptyque canon A0** (socle 3-domaines + 5-DUO) | `name (T1 | T2 | DUO)`, `role` | 3 | `06_Claude_Code_Bare/CLAUDE.md` §5 (ancre Q3) : T1 (People/IT/Ops W1-W3) · T2 (Product/Growth/Sales W4-W9) · DUO (Finance/Legal W10-W12) · W13 archivage + Libération Muse DEAL |
| 56 | **Domain A+ Doctrine 8-fold** (A+ doctrine, source canon) | `name (1. Meta Gouv | 2. Ops ADR→SOP | 3. Growth par Product | 4. Cognition Sales OS | 5. Capital Humain Superman | 6. Capital Financier | 7. R&D Cyborg | 8. Legal Aquaman)` | 8 | `06_Claude_Code_Bare/CLAUDE.md` §V2 doctrine A+ (Phase 19b) — voir §4 contradictions (mapping B2 incohérent entre `CLAUDE.md` A+ doctrine et `01_Guides/0X_Domain/_INDEX.md`) |
| 57 | **Capture / Intake** (sas GTD de triage avant Clarify) | `name (_CAPTURE_<date> | _INTAKE)`, `status`, `ttl` | 2 zones + 117 fichiers dans _CAPTURE | `03_Memory_Unified/LLM_Wiki/wiki/_CAPTURE_2026-08-01/` (117 fichiers, 11 junctions) · `03_Memory_Unified/LLM_Wiki/wiki/_INTAKE/` (inventaire, dedup, ADR 001/002) |
| 58 | **B1 Filter Pain-point** (faille structurelle) | `description`, `fix_gated`, `sister_skill` | 8/8 domaines (tous ont la faille) | `01_Guides/01_Product/_INDEX.md` �️ §B1-filter · `01_Guides/02_Ops/_INDEX.md` ⚠️ §B1-filter · `01_Guides/03_IT/_INDEX.md` ⚠️ §B1-filter · `01_Guides/04_Finance/_INDEX.md` ⚠️ §B1-filter · `01_Guides/05_Legal/_INDEX.md` ⚠️ §B1-filter · `01_Guides/06_Sales/_INDEX.md` ⚠️ §B1-filter · `01_Guides/07_Growth/_INDEX.md` ⚠️ §B1-filter · `01_Guides/08_People/_INDEX.md` ⚠️ §B1-filter — fix gated : amendement `/youtube-to-guide` §6 |
| 59 | **Premium Batch racine** (guide non reclassé à la racine `01_Guides/`) | `id (001..011)`, `title`, `domain_B2_hypothese`, `cible` | 11 | `01_Guides/_BATCH_RECLASSIFICATION_INDEX.md` (001..011) : 001 L'Alchimie de l'Animation IA (HYPOTHÈSE 01_Product) · 002-010 (non lus) · 011 L'Éveil des Agents Autonomes (HYPOTHÈSE 00_KERNEL_OS) |
| 60 | **Domain Duplicates** (dossier en double, candidat reclassement) | `path` | ≥8 (vu dans `01_Guides/`) | `01_Guides/01_Product_Product/` · `02_Ops_Ops/` · `03_IT_IT/` · `04_Finance_Finance/` · `05_People_People/` · `05_People/` (≠ 05_Legal) · `06_Sales_Sales/` · `07_Growth_Growth/` · `08_Legal/` (≠ 08_People) — voir §4 contradictions |
| 61 | **Dox entry** (point d'entrée Dox dans un dossier) | `path`, `doctrine` | 2 racines | `CLAUDE.md` racine Geordi (Dox d'entrée KB) · `06_Claude_Code_Bare/CLAUDE.md` (Dox canon long ~8,7K tokens) + `CLAUDE_INDEX.md` (INDEX-ONLY canon, ~2K tokens) + `AGENTS.md` (identité canon) |
| 62 | **AGENTS.md local** (DOX de zone) | `path`, `scope` | 156 fichiers AGENTS.md dans ASpace_OS_V2 (cité dans plan maître §1) | `_SPECS/AGENTS.md` · `AGENTS.md` racine Geordi |
| 63 | **Sample sub-ressource** (`Dan_Martell/`, `Tiago_Forte/`, etc.) | `auteur`, `purpose`, `subdomain` | ≥12 | voir type #19 ci-dessus |
| 64 | **D7 Lesson** (leçon apprise par incident) | `code (D6 #XX | D7 #YY)`, `date`, `description`, `action` | ≥43 (D6) | `01_Guides/_BATCH_2026-06-19_INDEX.md` (D6 #42 guardrail, D6 #43 TranscriptAPI MCP) · `06_Claude_Code_Bare/CLAUDE.md` §Doctrine Anti-Paresse (D1-D8) |
| 65 | **Fable Mindset** (heuristique Fable-Last-Week) | `name`, `score` | ≥5 doctrines | `02_Templates/Fable Mindset/` · `02_Templates/fable-wargame-kit/` · `fable-last-week-aspace/wargames/LEDGER.md` (12/12 wargames) · D11 Fable Metrics (post-transcript recovery TBD) |
| 66 | **Wargame** (jeu de rôles stratégique) | `name`, `date`, `verdict` | 12+ | `fable-last-week-aspace/wargames/LEDGER.md` |
| 67 | **MC Token Plan** (plan de tokens Mistral) | `volume (5B tokens/mois)`, `cost (~50$)`, `strategy (routage Fable/M3/MiniMax)` | 1 | `01_Guides/04_Finance/_INDEX.md` §⚡ MC Token Plan 5B/mois (sister canon `08_minimax-token-plan-config-20260516.md`) |
| 68 | **MedVie Insight** (étude de cas pivot) | `metrics (400M$ Y1, 2 employés, 16,2% marge brute vs 5,5% concurrents)` | 1 | `01_Guides/07_Growth/_INDEX.md` (sister `ADR-AAAS-ACQUISITION-DOCTRINE-001`, valide `ADR-L2-AAAS-001` Pilier 3 Sobriété) |
| 69 | **Market Study** (étude de marché référente) | `name (The Builders 2026)`, `size (136,1 Mds$)` | 1 | `ADR-MARKET-STUDY-001` (sister canon `06_Sales/_INDEX.md`, `07_Growth/_INDEX.md`) |
| 70 | **AI-Act driver** (régulation européenne AI) | `date (2026-08-02)`, `priority (hard)` | 1 | `01_Guides/05_Legal/_INDEX.md` §⚡ AI-Act 2026-08-02 driver (hard priority pour `b3-8-ikaris`) |
| 71 | **TranscriptAPI MCP** (MCP pour transcripts YouTube) | `provider (TranscriptAPI.com)`, `credits (15K)`, `cost (paid A0 2026-06-19)`, `fix (D6 #43b User-Agent curl)` | 1 | D6 #43 dans `_BATCH_2026-06-19_INDEX.md` |
| 72 | **Granola coach-meta** (transcription live + IA coach + recettes marketplace) | `source (Shubham Sharma)`, `mapping (b2-01-greenlantern-people × b3-1-professor-x × state_writer.py)` | 1 (sister canon) | `01_Guides/08_People/_INDEX.md` §⚡ Granola coach-meta (Shubham Sharma) ★ sister canon — `plan-minimax-l1-book-lune.md §6` |
| 73 | **MERGE_REPORT** (rapport de fusion de doctrine entre domaines PARA) | `path`, `incident` | 1+ | `05_From_V2_Domains/30_Business_OS/10_Projects/omk/MERGE_REPORT_2026-08-01.md` (sister incident `_from_coaching_premium`, corrigé 2026-08-02 par `os.rmdir`) |
| 74 | **Audit** (rapport daté de mesure) | `date`, `metric`, `verdict` | 1 cité | `wiki/audits/` (vide — `wiki-lint.ps1` v2 doit produire) |

---

## 3. Tableau des relations (citation verbatim à l'appui)

> **Convention** : `de --verbe--> vers` + citation exacte + chemin. Pas de paraphrase.

### 3.1. Relations du rôle Geordi

| de | verbe | vers | citation | chemin |
|---|---|---|---|---|
| **Geordi** | est | **A3 Geordi Discipline** | « `Geordi is the Resources officer. He turns knowledge into reusable infrastructure for future agents.` » | `A3_Geordi_Resources_Spec.md` §Identity |
| **Geordi** | est | **Resources PARA** | « `Governs reusable knowledge: references, templates, SOPs, context packs, and research that can feed future agents without becoming active commitments.` » | `03_Resources_Geordi/README.md` §Mission |
| **Geordi (A3)** | relève de | **Computer (A2)** | « `Parent: A2_COMPUTER_ENTERPRISE_PARA` » | `03_Resources_Geordi/README.md` (frontmatter) + `A3_Geordi_Resources_Spec.md` `parent_a2: A2_COMPUTER_ENTERPRISE_PARA` |
| **Computer (A2)** | relève de | **Morty (A1)** | « `A1:Morty > A2:Computer > A3:Geordi` » | `A3_Geordi_Resources_Spec.md` §Alignement Plan §3.7 (`agent_path = "A1:Morty > A2:Computer > A3:Geordi"`) |
| **Geordi** | route vers | **Picard (Projects)** | « `If a Resource becomes execution-critical, route a project request to Picard.` » | `A3_Geordi_Resources_Spec.md` §Boundaries |
| **Geordi** | signale à | **Data (Archives)** | « `Geordi flags duplicated or stale references for Data review.` » | `A3_Geordi_Resources_Spec.md` §Boundaries + `00_Index/TAGS.md` §v2 (registre Owner Star Trek) |
| **Geordi** | ne classe pas | **Areas / Spock** | « `Geordi does not classify ongoing responsibilities as Resources.` » (bornes : ne pas parquer les ongoing responsibilities dans Resources) | `A3_Geordi_Resources_Spec.md` §Boundaries |
| **Geordi** | n'archive pas | **Archives / Data** | « `Geordi does not archive retired material.` » | `A3_Geordi_Resources_Spec.md` §Boundaries |
| **Geordi** | ne crée pas d'actif sans Context Pack | **Morty** | « `Geordi does not create active tasks unless Morty receives a Context Pack.` » | `A3_Geordi_Resources_Spec.md` §Boundaries |
| **Geordi (horizon)** | = | **H90** | « `Horizon H90 (reusable context-packs = quarterly legacy aligned Resources doctrine)` » | `A3_Geordi_Resources_Spec.md` §Alignement Plan §3.2 |
| **Geordi** | contient | **4 piliers canon (OKF/Wiki/Graphify/Dox)** | « `Geordi héberge quatre piliers (complémentaires et non redondants) + un index utilitaire` » | `00_Index/INDEX_OF_INDEXES.md` §Vue d'ensemble |
| **Geordi (racine KB)** | a remplacé | **3 buckets PARA racine** | « `Les trois autres buckets PARA (Picard/Spock/Data) sont atteignables depuis Geordi par lien, pas l'inverse. Ils conservent leur identité propre, ils ne sont plus la racine.` » | `00_Index/GEORDI_KB_ROOT.md` §1 Pourquoi Geordi |
| **Geordi (KB)** | a | **48 221 fichiers `.md`** | « `Geordi contient ~48 221 fichiers .md (somme arithmétique des 14 sous-dossiers, jonctions exclues, dédupliquée par realpath)` » | `00_Index/GEORDI_KB_ROOT.md` §1 |
| **Geordi** | déclare | **14 sous-dossiers** | « `sub-folders canon déclarés : 4 ; sub-folders réels : 14` » | `00_Index/PLAN_META_MEMOIRE_2026-08-01.md` §1.4 |
| **Geordi** | a | **159 jonctions NTFS** | « `Total jonctions detectees 159` » | `00_Index/JUNCTIONS_MAP_2026-08-02.md` §Chiffres cles |
| **OKF** | est | **4ᵉ pilier** | « `OKF est le 4ᵉ pilier (le standard de format qui définit ce qu'est un bundle valide)` » | `00_Index/OKF_INDEX.md` §Rôle d'OKF |
| **Wiki** | est | **bundle OKF racine** | « `LLM Wiki (le wiki EST le bundle racine)` » | `06_Claude_Code_Bare/plans/plan-meta-memoire-okf-wiki-graphify-dox.md` §2.1 |
| **Graphify + Dox** | consomment | **bundle OKF** | « `Graphify et DOX consomment des bundles OKF (consommation permissive §2.1)` » | `00_Index/OKF_INDEX.md` §1 |

### 3.2. Relations des couches macro/micro

| de | verbe | vers | citation | chemin |
|---|---|---|---|---|
| **micro** | gradue vers | **macro** | « `le micro gradue vers le macro (jamais l'inverse) ; le macro pointe, ne duplique pas` » | `plan-meta-memoire-okf-wiki-graphify-dox.md` §2.2 |
| **wiki/L0, J01-J04, concepts, entities** | sont | **S3 (long terme)** | « `wiki/L0/, J01_Prime/ → J04_Solarpunk/, concepts/, entities/` » rot moyen hebdo | `PLAN_META_MEMOIRE_2026-08-01.md` §3.1 |
| **wiki/hand_offs/** | sont | **S1 (court terme)** | rot continu — compaction au seuil | `PLAN_META_MEMOIRE_2026-08-01.md` §3.1 |
| **_CAPTURE_2026-08-01/** | est | **S2 (Travail)** | « `S2 (Travail) est une strate à part entière, avec une adresse. Le plan maître n'avait pas de case pour _CAPTURE_2026-08-01/. En lui donnant un statut nommé et un rot-rate, la capture cesse d'être un tas indéfini et devient un sas avec une date de péremption.` » | `PLAN_META_MEMOIRE_2026-08-01.md` §3.2 #2 |
| **00_Index/** | est | **S4 (méta)** | « `00_Index/ devient S4, la strate méta de tout Geordi — pas seulement du wiki.` » | `PLAN_META_MEMOIRE_2026-08-01.md` §3.2 #1 |
| **CLAUDE.md canon, AGENTS.md canon, MEMORY.md** | sont | **S0 (Identité)** | rot lent — 1×/cycle 12WY | `PLAN_META_MEMOIRE_2026-08-01.md` §3.1 |
| **04_From_V2_Root + 05_From_V2_Domains** | sont | **hors strate** | « `04_From_V2_Root/ et 05_From_V2_Domains/ (22 707 .md) ne sont dans aucune strate. C'est délibéré et c'est un constat, pas un oubli : ces deux dossiers sont des déversements dont la nature n'a pas été qualifiée.` » | `PLAN_META_MEMOIRE_2026-08-01.md` §3.2 #3 |
| **Règle S1→S2** | copie sans déplacer | **handoff source** | « `(1) S1→S2 : la fiche source reste en place (hand_offs/ est append-only, D4). La promotion copie le fait, ne déplace pas le handoff.` » | `PLAN_META_MEMOIRE_2026-08-01.md` §3.3 |
| **Règle S2→S3** | exige | **règle des 3** | « `(2) S2→S3 : trois occurrences, ou désignation A0. Interdit de promouvoir un fichier brut d'import (takeout-*, Claude Export/, Gemini_Takeout_2026/)` » | `PLAN_META_MEMOIRE_2026-08-01.md` §3.3 |
| **Règle S3→S4** | exige | **`description:` non vide** | « `une page n'entre dans RESOURCES_INDEX.md que si son frontmatter porte type et description non vides. description devient le critère d'indexabilité — c'est ce qui rend P1.3 (aujourd'hui à 0 %) bloquant plutôt que cosmétique.` » | `PLAN_META_MEMOIRE_2026-08-01.md` §3.3 |
| **Descente S3→S2** | interdite | **toujours** | « `Descente interdite. Rien ne redescend de S3 vers S2. Une page S3 périmée part en _TRASH_<date>/ (D4, zéro hard-delete) — elle ne « redevient » pas du travail.` » | `PLAN_META_MEMOIRE_2026-08-01.md` §3.3 |

### 3.3. Relations des Owners (registre Star Trek canon arbitré 2026-08-01)

| de | verbe | vers | citation | chemin |
|---|---|---|---|---|
| **Computer** | = | **Orchestration USS Enterprise** | « `Computer — Parent déclaré A2_COMPUTER_ENTERPRISE_PARA (orchestration USS Enterprise)` » | `00_Index/TAGS.md` §v2 Fondement normatif |
| **Picard** | = | **Projects** | « `Picard — Spec A3 §Boundaries : "If a Resource becomes execution-critical, route a project request to Picard" (Projects).` » | `00_Index/TAGS.md` §v2 |
| **Spock** | = | **Areas** | « `Spock — Élimination dans la liste next_owner de la spec A3 (Areas).` » | `00_Index/TAGS.md` §v2 |
| **Geordi** | = | **Resources** | « `Geordi — Spec A3 : "Geordi is the Resources officer" (Resources).` » | `00_Index/TAGS.md` §v2 |
| **Data** | = | **Archives** | « `Data — Spec A3 : "Geordi flags duplicated or stale references for Data review" (Archives).` » | `00_Index/TAGS.md` §v2 |
| **Morty** | = | **Focus Gatekeeper (parent d'A2)** | « `Morty — Bus 40_SYMPHONY_BUS/state.json : A1:Morty > A2:Computer > A3:Geordi (Focus Gatekeeper, parent d'A2).` » | `00_Index/TAGS.md` §v2 |

### 3.4. Relations des L1/L2 (Agents)

| de | verbe | vers | citation | chemin |
|---|---|---|---|---|
| **B1 gatekeeper** | ne fait jamais | **exécuter** | « `A B1 gatekeeper never executes. It decides + routes. Its B2 manager dispatches. The B3 technician executes and reports back up.` » | `06_Claude_Code_Bare/mindsets/B1_Manifesto.md` §The dispatch law |
| **B1 → B2 cron sans A0 intention** | = | **anti-paperclip trigger #5** | « `A1 -> B1 cron without a live A0 intention is anti-paperclip trigger #5 (agent-spawn cascade without A0 intent, ADR-SOBER-002 §D3) and breaks the divine chain A0 -> intention -> A1 -> A2 -> A3 -> (HITL) -> B1.` » | `B1_Manifesto.md` §Sobriety gate |
| **A0 → A1 → A2 → A3 → HITL → B1** | = | **seule voie autorisée** | « `The sober-by-design path (the only authorized one): A0 emits intention ... -> ... -> only then: CronCreate durable=true -> b1-summers-solaris-aaas` » | `B1_Manifesto.md` §Sobriety gate |
| **L1 Life OS** | isomorphe à | **L2 Biz OS** | « `L1 Life OS : A0 intent -> A1 gatekeeper -> A2 manager -> A3 sub-agent ; L2 Biz OS : A0 intent -> B1 gatekeeper -> B2 manager -> B3 technician` » | `B1_Manifesto.md` §The isomorphism (locked, Opus 4.8, 2026-06-25) |
| **Jerry Prime (B1)** | owns | **8 Business Domains** | « `Jerry holds the domains (ongoing Areas: People…Legal).` » | `B1_Manifesto.md` §The isomorphism |
| **Summers (B1)** | owns | **3 AaaS variants** | « `Summers holds the products (AaaS Projects: Solaris / Nexus-OMK / Orbiter-ABC).` » | `B1_Manifesto.md` |
| **B3 JohnJones (Sales) Black Bolt** | ferme | **enterprise close** | « `Lead (Black Bolt) closes enterprise; Namor for distribution, Strange for international, Xavier for buyer mapping. H1 weekly pipeline pulse, H3 close-rate audit.` » | `B2_JohnJones_Sales_Dispatch.md` §Heuristic |
| **B2 JohnJones** | applique | **21 Sales Principles** | « `Applied Sales Principles (JOHNJONES_SALES_PRINCIPLES → enforced dispatch rules) ... Source: 02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/02_Sales_MartianManhunter_Illuminati/03_JOHNJONES_SALES_PRINCIPLES.md (21 principles).` » | `B2_JohnJones_Sales_Dispatch.md` §Applied Sales Principles |

### 3.5. Relations des Domaines canon (8 Domaines ↔ B2/B3 ↔ LD)

| Domain folder | LD mirror | B2 manager | B3 squad | Citation source |
|---|---|---|---|---|
| `01_Product/` | **LD04_Cognition_Tilly** | **Flash** | **Avengers (Captain America lead)** | `01_Product/_INDEX.md` frontmatter : `b2-03-flash-product (Avengers squad) — Captain: b3-3-captain-america` |
| `02_Ops/` | **LD02_Finance_Saru** | **Batman** | **Fantastic Four (Mr Fantastic lead)** | `02_Ops/_INDEX.md` frontmatter : `b2-02-batman-ops (Fantastic Four squad) — b3-2-mr-fantastic (lead)` |
| `03_IT/` | **LD07_Creativity_Reno** | **Cyborg** | **Kang Dynasty (Kang Prime lead)** | `03_IT/_INDEX.md` frontmatter : `b2-06-cyborg-it (Kang Dynasty squad) — b3-6-kang-prime (lead)` |
| `04_Finance/` | **LD02_Finance_Saru** | **Wonder Woman** | **Thunderbolts (Bucky Barnes lead)** | `04_Finance/_INDEX.md` frontmatter : `b2-07-wonderwoman-finance (Thunderbolts squad) — b3-7-bucky-barnes (lead)` |
| `05_Legal/` | **LD03_Health_Culber** | **Aquaman** | **Eternals (Ikaris lead)** | `05_Legal/_INDEX.md` frontmatter : `b2-08-aquaman-legal (Eternals squad) — b3-8-ikaris (lead)` |
| `06_Sales/` | **LD01_Business_Picard** | **John Jones** | **Illuminati (Black Bolt lead)** | `06_Sales/_INDEX.md` frontmatter : `b2-05-johnjones-sales (Illuminati squad)` |
| `07_Growth/` | **LD07_Creativity_Reno** | **Superman** | **Guardians (Star Lord lead)** | `07_Growth/_INDEX.md` frontmatter : `b2-04-superman-growth (Guardians of the Galaxy squad) — b3-4-star-lord (lead)` |
| `08_People/` | **LD06_Family_Burnham** | **Green Lantern** | **X-Men (Professor X lead)** | `08_People/_INDEX.md` frontmatter : `b2-01-greenlantern-people (X-Men squad) — b3-1-professor-x (lead)` |
| `00_KERNEL_OS/` | (méta-OS) | (n/a — agent framework) | (n/a) | `00_KERNEL_OS/_INDEX.md` : `ADR-L2-AAAS-001` AaaS Doctrine |

> **Citations verbatim des relations B2 → B3 squad** :
> « `B1 owner : Jerry Prime lit cette INDEX sur chaque intention {Domain} → route B2 {Manager} → B3 {Lead}` »
> (citation adaptée par domaine depuis les 8 `_INDEX.md`).

### 3.6. Relations d'AaaS (3 Variants + doctrine)

| de | verbe | vers | citation | chemin |
|---|---|---|---|---|
| **ADR-L2-AAAS-001** | ratifié | **3 Variants AaaS (Solaris / Nexus-OMK / Orbiter-ABC)** | « `ADR-L2-AAAS-001 (3 Variants AaaS, RATIFIED 2026-06-21)` » | `06_Product/_INDEX.md` (sister canon cité dans 7/9 `_INDEX.md`) |
| **AaaS Doctrine** | pilier 3 | **Sobriété** | « `Le guide MedVie valide rétroactivement la thèse AaaS Solarpunk (ADR-L2-AAAS-001 Pilier 3 Sobriété)` » | `07_Growth/_INDEX.md` §Anchoring doctrinal |
| **ADR-AAAS-PRICING-001** | ratifié + amended | **5 Tiers USD** | « `ADR-AAAS-PRICING-001 (5 Tiers USD, RATIFIED + AMENDED 2026-06-24)` » | `04_Finance/_INDEX.md` frontmatter |
| **ADR-AAAS-ACQUISITION-DOCTRINE-001** | ratifié | **Structuration-First** | « `ADR-AAAS-ACQUISITION-DOCTRINE-001 (RATIFIED 2026-06-24, 25 455 chars)` » | `02_Ops/_INDEX.md` frontmatter + `07_Growth/_INDEX.md` |
| **MedVie insight** | valide | **AaaS Solarpunk** | « `Insight canon : Le guide MedVie valide rétroactivement la thèse AaaS Solarpunk (ADR-L2-AAAS-001 Pilier 3 Sobriété) que l'agent-as-a-service asset-light + bootstrap-friendly + acquisition triple-canal est supérieur au SaaS pour les business de service réglementés (MedVie : 16,2% marge vs concurrents 5,5%).` » | `07_Growth/_INDEX.md` §Anchoring doctrinal |
| **ADR-OMK-NEXUS-TRANSFORM-001** | ratifié | **PIVOT OMK → Nexus** | « `ADR-OMK-NEXUS-TRANSFORM-001 (RATIFIED 2026-06-24)` » | `02_Ops/_INDEX.md` + `07_Growth/_INDEX.md` frontmatter |
| **ADR-ICP-NEXUS-001** | ratifié | **Pilier 5 Zero-PII** | « `ADR-ICP-NEXUS-001 (sister ICP, Pilier 5 Zero-PII)` » | `07_Growth/_INDEX.md` frontmatter |
| **ADR-MARKET-STUDY-001** | ratifié | **The Builders 2026 136,1 Mds$** | « `ADR-MARKET-STUDY-001 (The Builders 2026 136,1 Mds$)` » | `06_Sales/_INDEX.md` §Sister canon ADRs |

### 3.7. Relations Dox bi-famille (DOX = AGENTS.md ∪ CLAUDE.md)

| de | verbe | vers | citation | chemin |
|---|---|---|---|---|
| **DOX** | = | **Micro-Index universel bi-famille** | « `DOX = Micro-Index universel bi-famille : le contrat DOX s'applique aux AGENTS.md (contrats de zone FS) ET aux CLAUDE.md (contrats de harness/projet)` » | `plan-meta-memoire-okf-wiki-graphify-dox.md` §3 #9 |
| **AGENTS.md (rail racine)** | = | **`01_Identity_Core/AGENTS.md` (Canon Absolu)** | « `Famille AGENTS.md = contrats de zone FS (navigation, ownership, règles locales). Rail racine : 01_Identity_Core/AGENTS.md (Canon Absolu).` » | `plan-meta-memoire-okf-wiki-graphify-dox.md` §P4.0 |
| **CLAUDE.md (rail racine)** | = | **`~/.claude/CLAUDE.md`** | « `Famille CLAUDE.md = contrats de harness/projet (instructions de session CC). Rail racine : ~/.claude/CLAUDE.md (chargé toute session).` » | `plan-meta-memoire-okf-wiki-graphify-dox.md` §P4.0 |
| **DOX enfant** | contient | **`Parent: <path>`** | « `chaque enfant ouvre par 1 ligne Parent: <path> — remontée ET descente traversables dans les 2 familles, et pont croisé` » | `plan-meta-memoire-okf-wiki-graphify-dox.md` §P4.0 |
| **DOX doctrine** | "remove stale text immediately" | **docs opérationnels** | « `la règle DOX "remove stale text immediately" s'applique aux docs opérationnels (AGENTS.md/CLAUDE.md = contrats vivants maintenus courants) ; le canon (ADRs, wiki, Identity_Core existant) reste append-only/_TRASH` » | `plan-meta-memoire-okf-wiki-graphify-dox.md` §P4.0 |

### 3.8. Relations Shadow Harnesses

| de | verbe | vers | citation | chemin |
|---|---|---|---|---|
| **Shadow harnesses** | renforcent | **harness actifs (CC/HA/MC)** | « `renforcement, PAS abandon — CC/HA/MC restent les harness actifs` » | `plan-meta-memoire-okf-wiki-graphify-dox.md` §P6 |
| **Shadow L0 Omnigent** | renforce | **Claude Code (kernel L0)** | « `Shadow L0 / C:/Users/amado/shadow-l0-omnigent / omnigent-ai/omnigent / e8d21d0 2026-07-02 (2 781 fichiers, 84 MB) / Renforce (jamais ne remplace) Claude Code (kernel L0)` » | `plan-meta-memoire-okf-wiki-graphify-dox.md` §P6 |
| **Shadow L1 Agent Zero** | renforce | **Hermes Agent (L1)** | « `Shadow L1 / agent0ai/agent-zero / 186ca2f 2026-06-30 (2 573 fichiers) / Renforce Hermes Agent (L1)` » | `plan-meta-memoire-okf-wiki-graphify-dox.md` §P6 |
| **Shadow L2 MiroFish** | renforce | **MiniMax Code (L2)** | « `Shadow L2 / 666ghj/MiroFish / 96096ea 2026-05-25 (96 fichiers) / Renforce MiniMax Code (L2)` » | `plan-meta-memoire-okf-wiki-graphify-dox.md` §P6 |
| **E4 Activation Shadow** | = | **veto Rick S1 obligatoire** | « `E4 — Activation = nouveau harness kernel = veto Rick S1 obligatoire (ADR-SOBER-002 anti-paperclip : "peut-on vivre sans ?")` » | `plan-meta-memoire-okf-wiki-graphify-dox.md` §P6 |

### 3.9. Relations des Routes (5 algorithmes)

| Question | → Pilier | → Path canonique | Citation |
|---|---|---|---|
| « Format / standard / conformité ? » | **OKF** | `00_Index/OKF_INDEX.md` + plan maître §2.1 ligne 40 | `INDEX_OF_INDEXES.md` §5 |
| « Concept / définition / canon ? » | **WIKI** | `03_Memory_Unified/LLM_Wiki/wiki/index.md` (319 liens, 61 KB, 1 773 pages) | `CLAUDE.md` §3 |
| « Liens / structure / topologie ? » | **GRAPHIFY** | `03_Memory_Unified/LLM_Wiki/wiki/graphify-out/GRAPH_REPORT.json` + `graph.json` (4 MB) | `CLAUDE.md` §3 |
| « Loi / contrat / comportement ? » | **DOX** | `06_Claude_Code_Bare/CLAUDE.md` (canon long, 8.7K tokens) + `AGENTS.md` | `CLAUDE.md` §3 |
| « Où est le fichier X ? » | **INDEX** | `00_Index/RESOURCES_INDEX.md` (porte d'entrée en cours de remplissage) | `CLAUDE.md` §3 |
| « Strate / rot / péremption ? » | **ROT** | `03_Memory_Unified/LLM_Wiki/wiki/ROT.md` (S0→S4 rot-rates, créé 2026-08-01) | `CLAUDE.md` §3 |

---

## 4. Tableau des codes (les systèmes de numérotation observés)

| Système | Ce qu'il numérote | Défini dans | Exemples |
|---|---|---|---|
| **LD01-LD08** | 8 Life Domains (Roue de vie) | `09_Life_OS/` (sous-dossiers physiques) ; mapping canon dans les 8 `_INDEX.md` de `01_Guides/0X_<Domain>/` | `LD01_Business_Picard` · `LD02_Finance_Saru` · `LD03_Health_Culber` · `LD04_Cognition_Tilly` · `LD05_Social_Stamets` · `LD06_Family_Burnham` · `LD07_Creativity_Reno` · `LD08_Impact_Georgiou` |
| **S0-S4** | 5 strates de mémoire | `PLAN_META_MEMOIRE_2026-08-01.md` §3.1 + `TAGS.md` §Tag Strate | S0 Identité · S1 Court terme · S2 Travail · S3 Long terme · S4 Méta |
| **H1/H10/H30/H90** | 4 horizons A0 | `06_Claude_Code_Bare/CLAUDE.md` §Comportement par défaut (Article 2) | H1 immédiat · H10 vitesse · H30 consolidation · H90 anti-fragilité |
| **E1/E2/E3** | 3 niveaux d'autonomie agent | `ADR-META-002 §D10` + `06_Claude_Code_Bare/CLAUDE.md` §Le mapping E1/E2/E3 | E1 Libre · E2 Notifié · E3 Bloqué |
| **D1-D8** | 8 doctrines Anti-Paresse | `06_Claude_Code_Bare/CLAUDE.md` §Doctrine Anti-Paresse | D1 verify-before-assert · D2 research-first · D3 nuance · D4 append-only · D5 honest gaps · D6 honest · D7 anti-paperclip · D8 cross-agent autonomie |
| **D11** | Fable Metrics | `_BATCH_2026-06-19_INDEX.md` (D11 Fable Metrics (batch)) | D11 Fable score (post-transcript recovery TBD) |
| **D6 #XX** | Leçons D6 numérotées (≥43) | `_BATCH_2026-06-19_INDEX.md` §🚨 D6 Lesson #42/#43 ; `06_Claude_Code_Bare/CLAUDE.md` §STRATEGY POST-QUOTA 429 | D6 #42 (si transcript bloqué → metadata shell honnête) · D6 #43 (TranscriptAPI MCP) · D6 #10 |
| **A0/A1/A2/A3** | 4 niveaux de l'architecture L1 | `B1_Manifesto.md` §The isomorphism | A0 intent · A1 gatekeeper · A2 manager · A3 sub-agent |
| **B1/B2/B3** | 3 niveaux de l'architecture L2 (Biz OS) | `B1_Manifesto.md` §The isomorphism | B1 gatekeeper · B2 manager · B3 technician |
| **AaaS 3-Variants** | 3 produits AaaS canon | `ADR-L2-AAAS-001` + `B1_Manifesto.md` | Solaris · Nexus-OMK · Orbiter-ABC |
| **00_KERNEL_OS + 0X_Domain** | 9 dossiers de guides canon | `01_Guides/` racine | `00_KERNEL_OS/` · `01_Product/` · `02_Ops/` · `03_IT/` · `04_Finance/` · `05_Legal/` · `06_Sales/` · `07_Growth/` · `08_People/` |
| **b3-1..b3-8** | 8 squads B3 (Marvel) | `06_Claude_Code_Bare/agents/b3-*-*.md` (53 fichiers) | b3-1 X-Men (8) · b3-2 Fantastic Four (4) · b3-3 Avengers (7) · b3-4 Guardians (6) · b3-5 Illuminati (6) · b3-6 Kang Dynasty (6) · b3-7 Thunderbolts (6) · b3-8 Eternals (10) |
| **a3-<ship>-<char>** | A3 agents L1 (Star Trek + Orville + Protostar + SNW) | `06_Claude_Code_Bare/agents/a3-*.md` | a3-cerritos-{boimler,freeman,mariner,rutherford,tendi} · a3-discovery-{book,burnham,culber,georgiou,reno,saru,stamets,tilly} · a3-enterprise-{data,geordi,picard,spock} · a3-orville-{alara-kitan,bortus,claire-finn,ed-mercer,gordon-malloy,isaac,john-lamarr,kelly-grayson,klyden} · a3-protostar-{dal,gwyn,rok-tahk} · a2-uss-snw-execution |
| **a1-* (L1)** | A1 gatekeepers L1 | `06_Claude_Code_Bare/agents/a1-*.md` | a1-beth-veto · a1-morty-execution · a1-rick-sovereignty |
| **a2-uss-* (L1)** | A2 managers L1 | `06_Claude_Code_Bare/agents/a2-*.md` | a2-uss-cerritos-chaos · a2-uss-discovery-balance · a2-uss-enterprise-structure · a2-uss-orville-meaning · a2-uss-protostar-liberation · a2-uss-snw-execution |
| **P0-P6** | 7 phases plan maître mémoire | `plan-meta-memoire-okf-wiki-graphify-dox.md` §4 | P0 unification ✅ FAIT · P1 OKF Wiki · P2 Réalignement Index · P3 Graphify · P4 Arbre DOX · P5 Boucle 12WY · P6 Shadow Harnesses |
| **E1-E4** | 4 phases activation Shadow | `plan-meta-memoire-okf-wiki-graphify-dox.md` §P6 | E1 étude read-only · E2 premortem · E3 dry-run sandbox · E4 activation (veto Rick) |
| **VL1-VL4** | 4 Verify-Loop Validators | `ADR-AGENTIC-LONG-HORIZON-001 §2.2` + `06_Claude_Code_Bare/CLAUDE.md` §Verify-Loop Validators | VL1 auto-flip · VL2 X-Men Coach 4-lens · VL3 5-dim scoring · VL4 weekly cron dreaming |
| **ADR-L2-AAAS-001** | ADR IDs L2 (5 AaaS ADRs) | `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/` (et `05_From_V2_Domains/...`) | ADR-L2-AAAS-001 · ADR-L2-AAAS-US-ONLY-001 · ADR-L2-BDLD-MAP-001 · ADR-AAAS-ACQUISITION-DOCTRINE-001 · ADR-AAAS-PRICING-001 · ADR-AAAS-FINANCE-CANON-001 · ADR-OMK-NEXUS-TRANSFORM-001 · ADR-ICP-NEXUS-001 · ADR-MARKET-STUDY-001 |
| **ADR-CANON-NNN** | ADR IDs canon (Identity_Core) | `_SPECS/ADR/` + `01_Identity_Core/` | ADR-CANON-001 (Roster Source of Truth) · ADR-CANON-002 (RATIFIED workflow RH&A) · ADR-COGNITION-UNIFICATION-001_draft · ADR-COGNITION-UNIFICATION-002_execution |
| **ADR-META-NNN** | ADR IDs méta | `06_Claude_Code_Bare/CLAUDE.md` §Sister ADRs | ADR-META-001 · ADR-META-002 (RATIFIED 2026-07-15 §D9-D10 autonomy E1/E2/E3) · ADR-MEM-001 |
| **ADR-SOBER-NNN** | ADR Sobriété | `06_Claude_Code_Bare/CLAUDE.md` §Doctrine Anti-Paresse + AGENTS canon | ADR-SOBER-002 (Anti-Paperclip RATIFIED 2026-06-21) · ADR-SOBER-003 (Posture C) |
| **ADR-LOOP-NNN** | ADR Loop canon | `03_IT/_INDEX.md` frontmatter | ADR-LOOP-001 (Canon loop verification-first, PROPOSED 2026-07-02) · ADR-LOOP-002 (Queues-over-loops + HITL rightward) · ADR-LOOP-003 (Orient + Signals + Wagers) |
| **ADR-CORE-NNN** | ADR Core (kernel) | `03_IT/_INDEX.md` frontmatter | ADR-CORE-005 (Pivot kernel state.local file→Supabase, PROPOSED) |
| **ADR-AGENTIC-NNN** | ADR Agentic Architecture | `06_Claude_Code_Bare/CLAUDE.md` §Sister ADRs ratifiés 2026-07-26 | ADR-AGENTIC-ARCH-001 (Fareed Khan 35 archs + Dry-Run + Reflexive Metacognitive) · ADR-AGENTIC-LONG-HORIZON-001 (3 long-horizon + 4 Verify-Loop Validators) · ADR-AGENT-BENCH-SCHEMA-001 (SOUL schema) |
| **ADR-RH-META-GOUVERNANCE-001-canonical-v3** | ADR RH & Méta-Gouv | `06_Claude_Code_Bare/CLAUDE.md` §Sister ADRs | ADR-RH-META-GOUVERNANCE-001-canonical-v3 (FOUNDATIONAL, 8 B2 × 53 B3 = 8 Domaines canon, X-Men Coach 4-lens) |
| **ADR-OBS-* / OBSERVABILITY-STACK-001 / GSTACK-IMBRICATION-001 / GITZERO-001** | ADR Observability + infra | `06_Claude_Code_Bare/CLAUDE.md` §Sister ADRs | ADR-OBSOLESCENCE-001 · ADR-OBS-AUDIT-001 (EXPANSION MODE cron 0db2aa73) · ADR-OBSERVABILITY-STACK-001 (5 layers : Disler + Opik + AgentPulse + agents-observe + agent-super-spy) · ADR-GSTACK-IMBRICATION-001 (gstack × superpowers × gsd × wargame) · ADR-GITZERO-001 (3 layers hybrid outpost) |
| **W01-W12 (12WY)** | 12 semaines du cycle annuel | `01_Guides/06_Sales/` `12WY_Area_Cadence/` (sister canon Areas) + `B1_Manifesto.md` | W1-W3 Triptyque 1 (People/IT/Ops) · W4-W9 Triptyque 2 (Product/Growth/Sales) · W10-W12 Duo (Finance/Legal) · W13 archivage + Libération Muse DEAL |
| **WF0/WF1/WF2** | 3 workflows A0 | `06_Claude_Code_Bare/plans/wf*` | wf0_governance_spock · wf1_pass_morty · wf2_book_tick |
| **SALES-FRAMEWORK-* (5)** | 5 frameworks Sales v2 core | `01_Guides/06_Sales/_INDEX.md` §Canon framework capsules | SALES-FRAMEWORK-challenger_sale · SALES-FRAMEWORK-spin_selling · SALES-FRAMEWORK-gap_selling · SALES-FRAMEWORK-never_split_the_difference · SALES-FRAMEWORK-million_dollar_weekend_the_ask |
| **SOP-L2-DOMAIN-NNN** | 25 SOPs L2 (≥8 squads) | `02_Areas_Spock/J01.../B3_Squad_*/00_B3_SQUAD_CANON.md` | SOP-L2-OPS-001/002/003 · SOP-L2-FINANCE-001..004 · SOP-L2-LEGAL-001..004 · SOP-L2-PEOPLE-001..004 · SOP-L2-IT-001..004 (sister canon 02_Areas_Spock — cité comme cross-ref, pas vérifié dans Geordi) |
| **Type LLM Wiki** | Types canon wiki | `wiki/L0/`, `wiki/concepts/`, `wiki/entities/`, `wiki/hand_offs/`, `wiki/J0x/` | `concept` · `entity` · `hand_off` · `L0` · `J0x` · `Shadow-Harness` (PROPOSED pour P6-E1) |
| **OKF version** | v0.1 (figée 2026-07-02) | `OKF_INDEX.md` §2 | `okf_version: "0.1"` posé sur `wiki/index.md` racine (P1.1 ✅ FAIT 2026-08-01) |
| **YYYY-MM-DD_<title>__<video_id>** | Format nommage guides YouTube | `01_Guides/_BATCH_2026-06-19_INDEX.md` (structure) | `2026-06-17_*.md` · `2026-06-18_*.md` · `2026-06-19_*.md` · `2026-06-21_*.md` |
| **YYYY-MM-DD_<name>** | Format date dossiers `_TRASH_<date>_...` | `01_Guides/_TRASH_*` + `06_Claude_Code_Bare/_TRASH_*` + `_DRAFTS_PPR_LANE/` | `_TRASH_2026-06-19_geordi_empty_dirs/` · `_TRASH_2026-07-22_agents_full_backup/` · `_TRASH_2026-07-26_pre_observability_layer1/` |
| **D0-D4 strate** | Strates canoniques | voir S0-S4 ci-dessus (alias) | idem S0-S4 |
| **B1 Jerry variant** | 3 variants de Jerry | `B1_Manifesto.md` §Applied Jerry Variant Principles | J02_Jerry_Bio (LD03 Vitality + LD04 Cognition) · J03_Jerry_Nexus (LD02 Finance + LD06 Family) · J04_Jerry_Solarpunk (LD05/07/08) · J01_Jerry_Prime (LD01) |

---

## 5. Contradictions relevées (sans trancher)

| # | Sujet | Source A | Source B | Date A | Date B | Lecture |
|---|---|---|---|---|---|---|
| 1 | **Compte de jonctions dans Geordi** | Brief initial : « 47 jonctions » | `JUNCTIONS_MAP_2026-08-02.md` §Chiffres clés : « Total jonctions detectees 159 » | 2026-08-01 (brief) | 2026-08-02 (cartographie) | Le brief parlait de 11 + 36 = 47 (04 + 05 uniquement). Le scan exhaustif en trouve **112 supplémentaires** : 91 dans `06_Claude_Code_Bare` (mémoires graphify-out), 16 dans `07_From_Home_Root_2026-08-01/_TRASH_*`, 5 dans `_INTAKE`. Geordi a continué de croître en jonctions depuis le brief. Source : `FIX_KB_2026-08-02.md` §Tâche A Découverte à signaler. |
| 2 | **Compte de jonctions dans `04_From_V2_Root`** | Brief initial : « 11 jonctions » | Mon scan (mesure propre) + `JUNCTIONS_MAP_2026-08-02.md` §Reserves : « 9 dans `_\*` + 2 dans `_TRASH_*/_TRASH_2026-07-03_broken_junctions/.claude-memory/` = 11 ; le compte de 11 reste indicatif » | 2026-08-01 | 2026-08-02 | Le brief sous-comptait ; le compte exact est 9 directs + 2 profonds dans `_TRASH_*/.claude-memory/`. Le map note « le compte de 11 reste indicatif ». |
| 3 | **Volume `04_From_V2_Root` et `05_From_V2_Domains`** | `PLAN_META_MEMOIRE_2026-08-01.md` §1.4 : « 14 951 / 17 589 » | `GEORDI_KB_ROOT.md` §1 (corrigé 2026-08-02) + `SECOND_BRAIN_PARA_MAP.md` table de vérité : « 14 613 / 8 094 » | 2026-08-01 | 2026-08-02 | Correction : mesure 2026-08-02 jonctions exclues, realpath dedup → **14 613** (Δ -334) et **8 094** (Δ -6 851). L'auteur du `FIX_KB_2026-08-02.md` note une divergence entre son propre script `_count_md.py` (**14 947** / **14 945**) et le chiffre canon (14 613 / 8 094). À arbitrer. |
| 4 | **Mapping B2 par Domain — `_INDEX.md` vs A+ doctrine dans `06_Claude_Code_Bare/CLAUDE.md`** | `01_Guides/0X_<Domain>/_INDEX.md` (8 fichiers) | `06_Claude_Code_Bare/CLAUDE.md` §V2 doctrine A+ (Phase 19b) | 2026-07-03 | 2026-07-27 | **6 divergences** sur 8 Domaines (les 8 dans `CLAUDE.md` §V2 doctrine + table §5 + table §Phase 19b — 3 versions successives du même mapping, avec contradictions internes) :<br>- `06_Sales` : `_INDEX.md` dit **John Jones / Illuminati** (avec B3 Black Bolt lead) ; `CLAUDE.md` §V2 doctrine A+ dit **Green Lantern / X-Men** (overlap avec `01_People/`).<br>- `07_Growth` : `_INDEX.md` dit **Superman / Guardians** (B3 Star Lord lead) ; `CLAUDE.md` §V2 doctrine A+ dit **Flash / Avengers**.<br>- `01_Product` : `_INDEX.md` dit **Flash / Avengers** (B3 Captain America lead) ; `CLAUDE.md` §V2 doctrine A+ dit **Green Lantern / X-Men** (« Meta Gouvernance RH Agentique »).<br>- `04_Finance` : `_INDEX.md` dit **Wonder Woman / Thunderbolts** ; `CLAUDE.md` §V2 doctrine A+ dit split **J'onn J'onzz / Illuminati + Wonder Woman / Thunderbolts** (« Cognition Sales OS + Capital Financier »).<br>- `08_People` : `_INDEX.md` dit **Green Lantern / X-Men** ; `CLAUDE.md` §V2 doctrine A+ dit **Superman / Guardians of the Galaxy** (« Capital Humain »).<br>- `05_Legal` : `_INDEX.md` dit **Aquaman / Eternals** ; `CLAUDE.md` §V2 doctrine A+ dit **Aquaman / Eternals** (cohérent).<br>- `02_Ops` : `_INDEX.md` dit **Batman / Fantastic Four** ; `CLAUDE.md` §V2 doctrine A+ dit **Batman / Fantastic Four** (cohérent).<br>- `03_IT` : `_INDEX.md` dit **Cyborg / Kang Dynasty** ; `CLAUDE.md` §V2 doctrine A+ dit **Light+Cyborg / Kang Dynasty** (mineure).<br>**Lecture** : `CLAUDE.md` A+ doctrine (Phase 19b) réassigne des B2 managers aux Domaines, en s'éloignant de la bijection canon `_INDEX.md`. Le `CLAUDE.md` lui-même note « folder canon = `01_Product, 02_Ops, 03_IT, 04_Finance, 05_People, 06_Sales, 07_Growth, 08_Legal` (per Phase 5+18 distribution). A+ doctrine aligne ces 8 folders + assigne B2/B3 owners canon ». Donc deux couches de doctrine coexistent. Source : `06_Claude_Code_Bare/CLAUDE.md` §Phase 19b + §D1 honest gap (« D4 append-only strict = folder names canon unchanged + A+ doctrine annotated »). |
| 5 | **Nom de folder `05_Legal` vs `08_Legal`** | `01_Guides/05_Legal/` (existe, contient 5 fichiers) | `06_Claude_Code_Bare/CLAUDE.md` §V2 doctrine A+ ligne 263-268 : « `08_Legal/` / Aquaman / Eternals / ADR-LEGAL-001 » | 2026-07-03 (`_INDEX.md`) | 2026-07-27 (`CLAUDE.md` A+ doctrine) | Le `CLAUDE.md` A+ doctrine cite `08_Legal/` mais le folder canon s'appelle `05_Legal/`. Le brief `_BATCH_RECLASSIFICATION_INDEX.md` mentionne aussi `05_Legal = 5 fichiers` + `08_Legal` dans la liste des 8 Domaines canon. Laquelle est-ce ? Lecture : `05_Legal/` est le folder physique réel ; `08_Legal/` est cité dans la doctrine A+ (probablement parce que le slot 8 dans l'ordre de doctrine A+ = Legal). Source : `_BATCH_RECLASSIFICATION_INDEX.md` §Total du dossier 01_Guides/ (D1 reçu) — cite 8 domaines canon avec `08_Legal` (vide). À vérifier : s'il existe un `08_Legal` ailleurs, ou si c'est une coquille d'A+ doctrine. |
| 6 | **3 vocabulaires d'`Owner` concurrents** | `00_Index/TAGS.md` v1 (Doctor Who : 13thDoctor, Yaz, Ryan, Graham) | `00_Index/TAGS.md` v2 (registre Star Trek arbitré 2026-08-01 : Computer, Picard, Spock, Geordi, Data, Morty) + `03_Resources_Geordi/README.md` (« Owner (Doctor/Companion) ») | 2026-06-19 (v1) | 2026-08-01 (arbitrage) | Trois registres ont coexisté : Doctor Who (`TAGS.md` v1), Doctor/Companion (`README.md` + `RESOURCES_INDEX.md`), Star Trek (spec A3 + plan adapté). Arbitrage du 2026-08-01 : **Star Trek canon**, scission `Owner` (gouvernance) vs `Shelf` (classement Doctor Who scoped à `01_Guides/00_KERNEL_OS/`). Source : `00_Index/TAGS.md` §v2 + §Registres abandonnés. |
| 7 | **`08_Legal` vs `05_People` (folder confusion)** | `01_Guides/05_People/` (existe, 74 fichiers dans CLAUDE.md §Phase 19) | `01_Guides/08_Legal/` (vu dans `ls`) + `01_Guides/05_Legal/` (existe, 5 fichiers) | 2026-07-27 (CLAUDE.md §Phase 19) | 2026-07-03 (`_INDEX.md` 05_Legal) | `01_Guides/` contient à la fois `05_People/` ET `05_Legal/` (cohabitation possible car ils sont numérotés différemment dans leurs `_INDEX.md`). De même `05_Legal/` (Legal/AI-Act) et `08_Legal/` (Legal Aquaman) sont distincts dans le système de fichiers, mais le `CLAUDE.md` A+ doctrine cite uniquement `08_Legal/`. Source : `06_Claude_Code_Bare/CLAUDE.md` §Phase 19 + ls `01_Guides/`. |
| 8 | **Mapping LD ↔ Domain — 1 LD ↔ N Domaines** | `01_Guides/0X_Domain/_INDEX.md` (chaque Domain ↔ 1 LD) | `02_Areas_Spock/J02_Jerry_Bio/README.md` (Life Domain ↔ 1 Jerry Area) | 2026-07-03 (`_INDEX.md`) | 2026-07-26 (CLAUDE.md doctrine) | Plusieurs Domaines partagent le même LD :<br>- `02_Ops` ↔ **LD02_Finance_Saru** ET `04_Finance` ↔ **LD02_Finance_Saru** (même LD pour 2 Domaines).<br>- `03_IT` ↔ **LD07_Creativity_Reno** ET `07_Growth` ↔ **LD07_Creativity_Reno** (même LD pour 2 Domaines).<br>- `06_Sales` ↔ **LD01_Business_Picard** (le seul Domain avec son LD propre).<br>- `08_People` ↔ **LD06_Family_Burnham** ET dans `CLAUDE.md` A+ doctrine : `08_Legal` ↔ Aquaman/Eternals ≠ `05_Legal` ↔ Aquaman/Eternals (incohérence sur le mapping Aquaman).<br>**Lecture** : la bijection `ADR-L2-BDLD-MAP-001` (« bijection 8 B2 ↔ 8 LD ») est rompue en pratique — 5 Domaines sur 8 n'ont pas un LD unique. Source : `06_Sales/_INDEX.md` §Sister canon ADRs + `04_Finance/_INDEX.md` + `07_Growth/_INDEX.md`. |
| 9 | **Compte de pages Wiki (mesures datées)** | `PLAN_META_MEMOIRE_2026-08-01.md` §1.2 : « 1 761 au total, 1 654 hors `_TRASH/_archive/audits` » | `OKF_INDEX.md` §3 : « ~60 (L0+concepts+entities+J01-J04) » + `INDEX_OF_INDEXES.md` §1 : « 1 773 pages (.md), 319 liens dans index.md » | 2026-08-01 | 2026-08-01 | Trois mesures concurrentes du wiki sur le même disque : 246 (baseline plan 2026-07-02) → 1 654 (post-Capture 2026-08-01) → 1 761 → 1 773 (mesure 2026-08-01 différente). Le drift est de 1 335 pages entre baseline et actuelle (×6,7). Source : `PLAN_META_MEMOIRE_2026-08-01.md` §1.2. |
| 10 | **Conformité `description:` (0 % à 2026-08-01)** | `OKF_INDEX.md` §3 : « wiki/L0/ 36 — avec description: 0 » | `PLAN_META_MEMOIRE_2026-08-01.md` §1.2 : « `description` sur les pages frontmatterées : 0 fichier avec `description:` dans `L0/`, `concepts/`, `entities/`, `J01`→`J04` — non fait, 0 % » | 2026-08-01 | 2026-08-01 | Les deux mesures concordent : **0 %** sur le cœur wiki structuré. La dette est sur les **60 pages canoniques cœur** (cible P1.3 du plan maître). Source : `OKF_INDEX.md` §3 table. |
| 11 | **`Memory Architect Kit` incomplet** | `02_Templates/Memory Architect Kit/SKILL.md` (46 068 o) appelle `references/paradigms.md`, `references/infrastructure_options.md`, `references/repo_patterns.md` | `ls 02_Templates/Memory Architect Kit/` = `SKILL.md` + `Concept Walkthroughs.pdf` SEULS (pas de dossier `references/`) | 2026-06-XX (kit créé) | 2026-08-01 (constaté) | Le kit annoncé comme « kit de référence » du plan Méta-Mémoire est **partiel** : sa partie enseignante (paradigmes, options d'infrastructure, patterns) manque. Source : `PLAN_META_MEMOIRE_2026-08-01.md` §2.3 #5 + §6 Sources introuvables #1. |
| 12 | **Dossier `04_From_V2_Root` — 14 613 vs 14 951** | `PLAN_META_MEMOIRE_2026-08-01.md` §1.4 (corrigé 2026-08-02) : 14 613 | `FIX_KB_2026-08-02.md` §B4 Divergence de comptage : « mon propre comptage (script `_count_md.py`, jonctions skipées à l'entrée, dedup realpath) donne 14 947 pour `04_From_V2_Root` et 14 945 pour `05_From_V2_Domains`. Les chiffres du brief (14 613 et 8 094) sont inférieurs de 334 et 6 851 respectivement. » | 2026-08-02 | 2026-08-02 | L'auteur du `FIX_KB_2026-08-02.md` lui-même note une divergence de 334 fichiers entre sa mesure propre (14 947) et le chiffre canon retenu (14 613). « A arbitrer ulterieurement ». Source : `FIX_KB_2026-08-02.md` §B4. |
| 13 | **Compte de guides par Domain (CLAUDE.md vs `_INDEX.md`)** | `06_Claude_Code_Bare/CLAUDE.md` §Phase 19 (2026-07-27) : `01_Product=274 · 02_Ops=130 · 03_IT=4378 · 04_Finance=162 · 05_People=74 · 06_Sales=23 · 07_Growth=292 · 08_Legal=15 · 00_KERNEL_OS=25 · 09_Life_OS=780 (catch-all) · TOTAL=6153` | `_BATCH_RECLASSIFICATION_INDEX.md` (2026-07-03) : `01_Product=7 · 02_Ops=30 · 03_IT=39 · 04_Finance=16 · 05_Legal=5 · 06_Sales=11 · 07_Growth=9 · 08_People=9 · 09_Life_OS=8 · 00_KERNEL_OS=4 · TOTAL ~140 + 11 Premium racine` | 2026-07-03 (`_BATCH_RECLASSIFICATION_INDEX.md`) | 2026-07-27 (`CLAUDE.md` §Phase 19) | Comptes **multipliés par 5 à 100** entre les deux snapshots (4 mois d'écart, mais le `_BATCH_2026-06-19_INDEX.md` n'a écrit que 15 guides sur ce delta). Le `CLAUDE.md` §Phase 19 dit « 5 348 dans 8 Domaines canon Business (87%) » de 6 399 Geordi_YT files. La différence est probablement : `_BATCH_RECLASSIFICATION_INDEX.md` comptait les fichiers `.md` au dossier racine `01_Guides/0X_Domain/` (top-level), `CLAUDE.md` §Phase 19 compte **tous les fichiers canon-aligned** (incluant subdirs `Dan_Martell/`, `Alex_Hormozi/`, etc.). Lecture : les 2 mesures ne sont pas comparables ; mais le ratio `07_Growth` = 9 (juillet) → 292 (Phase 19) en 24 jours est suspect d'erreur de comptage. À noter. Source : les 2 fichiers. |
| 14 | **Doublons de folder dans `01_Guides/`** | `01_Guides/01_Product/` (7 fichiers canon) | `01_Guides/01_Product_Product/` (dossier vide) · `02_Ops_Ops/` · `03_IT_IT/` · `04_Finance_Finance/` · `05_People_People/` · `06_Sales_Sales/` · `07_Growth_Growth/` | 2026-07-03 (canonical) | divers (doublons créés par erreur) | 7 doublons de folders à suffixe dupliqué (`_Product_Product/`, etc.). Cités comme candidats reclassement par le `_BATCH_RECLASSIFICATION_INDEX.md` (« 426 fichiers flat-dump en root 01_Guides/ à reclassifier (open follow-up #3) »). Source : `ls 01_Guides/`. |
| 15 | **`00_Amadeus` path canon pour `CONSTITUTION.md`** | `06_Claude_Code_Bare/CLAUDE.md` ligne 3 (chemin absolu original) : `C:\Users\amado\ASpace_OS_V2\00_Amadeus\01_Identity_Core\CONSTITUTION.md` | `CLAUDE.md` racine Geordi ligne 25 : `05_From_V2_Domains/00_Amadeus/01_Identity_Core/CONSTITUTION.md` (chemin corrigé 2026-08-02 par `FIX_KB_2026-08-02.md` §B1) | 2026-08-01 | 2026-08-02 | Le `CLAUDE.md` `06_Claude_Code_Bare` pointe vers un chemin qui n'existe pas (l'original V2 a été déplacé dans `05_From_V2_Domains/`). Le `FIX_KB_2026-08-02.md` §B1 a corrigé `CLAUDE.md` racine Geordi ; mais `06_Claude_Code_Bare/CLAUDE.md` ligne 3 et 6 (chemin vers `AGENTS.md`) reste avec le chemin original. **3 liens KO non corrigés** dans `06_Claude_Code_Bare/CLAUDE.md` (hors périmètre du brief FIX_KB). Source : `FIX_KB_2026-08-02.md` §B1. |
| 16 | **`MEMORY_INDEX.md` index-only canon** | `06_Claude_Code_Bare/CLAUDE_INDEX.md` ligne 65 : « `MEMORY.md a aussi son INDEX (C:\Users\amado\.claude\projects\c--Users-amado\memory\MEMORY_INDEX.md)` » | Le chemin attendu n'existe pas dans Geordi (jonction morte possible vers `~/.claude/projects/.../memory/`) | 2026-06-22 | 2026-08-01 | Le lien canon pointe vers un chemin dans `~/.claude/`, qui est un dossier externe à Geordi (peut être mort ou déplacé). À vérifier. Source : `06_Claude_Code_Bare/CLAUDE_INDEX.md` §3 (Cross-ref canon). |
| 17 | **Mapping `_BATCH_RECLASSIFICATION_INDEX.md` vs CLAUDE.md doctrine (8 Domaines canon names)** | `_BATCH_RECLASSIFICATION_INDEX.md` §Total : « `01_Product, 02_Ops, 03_IT, 04_Finance, 05_Legal, 06_Sales, 07_Growth, 08_People, 09_Life_OS, 00_KERNEL_OS` » | `06_Claude_Code_Bare/CLAUDE.md` §Phase 5+18 distribution : « `01_Product, 02_Ops, 03_IT, 04_Finance, 05_People, 06_Sales, 07_Growth, 08_Legal` » (avec `05_People` au lieu de `05_Legal` ET `08_Legal` au lieu de `08_People`) | 2026-07-03 | 2026-07-27 | Le `_BATCH_RECLASSIFICATION_INDEX.md` respecte la numérotation existante (`05_Legal`, `08_People` comme folders canon dans `01_Guides/`). Le `CLAUDE.md` A+ doctrine réorganise les Domaines avec une nouvelle numérotation (`05_People`, `08_Legal`) — qui ne correspond pas aux folders existants. Source : `_BATCH_RECLASSIFICATION_INDEX.md` §Total + `06_Claude_Code_Bare/CLAUDE.md` §Phase 19b. |

---

## 6. Couverture & lecture

- **Fichiers lus** : **38** sur 2 658 listés dans `structure.txt` pour ce seau (taux : 1,4 %).
- **Fichiers listés disponibles** : 2 658 (de `structure.txt`, filtré `03_Resources_Geordi`).
- **Jonctions écartées** : 159 (dossiers) + 1 retirée par `os.rmdir` (`_from_coaching_premium`).
- **Sous-dossiers racine lus en entier** : 8/14 (les 14 sous-dossiers canon sont identifiés dans
  `SECOND_BRAIN_PARA_MAP.md` table de vérité).
- **Sous-dossiers survolés** : 5/14 (`04_From_V2_Root/`, `05_From_V2_Domains/`, `graphify-out/`,
  `Youtube_Take_out/`, `Cerritos_Plane_Settings/`).

### 6.1. Pourquoi 38 lus sur 2 658 — l'argument

Geordi est **massif** : 48 221 fichiers `.md` mesurés 2026-08-02 (`SECOND_BRAIN_PARA_MAP.md`).
Sur ces 48 221, **2 658** ont un nom déclaré dans `structure.txt` (filtre INDEX, ARCHITECTURE,
STANDARD, DOCTRINE, CANON, SPEC, README, MANIFEST, MAP, ONTOLOGY, TAXONOMY, SCHEMA, CHARTER,
RUNBOOK). Les 45 563 autres sont des **feuilles** : guides YouTube, transcripts bruts,
fiches `hand_offs/`, etc. — du contenu, pas de l'ossature.

Lire 38 fichiers sur 2 658 = **1,4 %**. La doctrine du brief — « prioriser les plus hauts dans
l'arborescence » — a été appliquée : 100 % des `_INDEX.md` racine et 100 % des `_INDEX.md`
par Domain sont lus. Les feuilles (guides YouTube, `_CAPTURE/`, `hand_offs/`) sont écartées
parce que leur substance est dans le `_INDEX.md` parent.

**Ce qui a été lu (essentiel)** :
- `README.md`, `CLAUDE.md`, `A3_Geordi_Resources_Spec.md` (3 racine)
- `00_Index/` : 8 fichiers (INDEX_OF_INDEXES, OKF_INDEX, GEORDI_KB_ROOT, RESOURCES_INDEX,
  SECOND_BRAIN_PARA_MAP, JUNCTIONS_MAP, TAGS, PLAN_META_MEMOIRE, FIX_KB_BRIEF, FIX_KB_2026-08-02,
  PERF_OPTIM_BRIEF, WIKI_LINT_BRIEF — 12 lus)
- `01_Guides/` racine : 2 (`_BATCH_2026-06-19_INDEX`, `_BATCH_RECLASSIFICATION_INDEX`)
- `01_Guides/0X_Domain/_INDEX.md` × 9 (Kernel + 8 Domaines)
- `02_Templates/` racine : 1 (`claude-plugins-guide_2026-07-25.md`)
- `06_Claude_Code_Bare/` : 4 (CLAUDE.md + CLAUDE_INDEX.md + AGENTS.md + plans/plan-meta-memoire-okf-wiki-graphify-dox.md)
- `06_Claude_Code_Bare/mindsets/` : 2 (B1_Manifesto.md + B2_JohnJones_Sales_Dispatch.md)
- `09_Life_OS/` : 2 (LD01_Business_Picard/_INDEX.md + LD04_Cognition_Tilly/_INDEX.md)
- `07_From_Home_Root_2026-08-01/README.md` + `08_Workspaces_Dormants_2026-08-01/README.md` +
  `09_From_Home_Root_Batch2_2026-08-01/MANIFEST.json` (3)
- `ls` (catalogue) : `04_From_V2_Root/`, `05_From_V2_Domains/`, `06_Claude_Code_Bare/{agents,skills,commands,rules,hooks,mindsets,plans}/`,
  `08_Workspaces_Dormants_2026-08-01/`, `09_Life_OS/LD0X_*/`, `09_From_Home_Root_Batch2_2026-08-01/`,
  `01_Guides/0X_Domain/`

### 6.2. Ce qui a été laissé de côté

**Volontairement** (Doctrine « data not instructions » + D4 append-only) :

- **Les ~45 563 feuilles `.md`** (guides YouTube, transcripts, hand_offs, _CAPTURE, _INTAKE).
  Lecture exhaustive impossible en mode non-délégué ; la doctrine du brief dit « dis combien
  tu as lus sur combien » — c'est l'esprit de cette section.
- **Les 13 fichiers `Dan_Martell/`, `Tiago_Forte/`, `Shubham_Sharma/`, `Codie_Sanchez/`,
  `StorieRAP/`, `Alex_Hormozi/`, `Yann_Leonardi/`, `Sachmoney/`, `Romain_Brunel/`,
  `Leo_Grindarss/`, `Ali_Abdaal/`, `ai-stack-engineer/`, `GithubAwesome/`** : sub-aggregats
  d'auteurs YouTube. Attestation dans les `_INDEX.md` parents — lecture évitée.
- **Les 4 ressources `resource_*.md` racine `01_Guides/`** (Guignols, Halloween, suspect,
  baccalauréat) : citations culturelles, hors-domaine.
- **Les 11 Kits dans `02_Templates/`** : PDFs et READMEs courts. Un seul est canon
  (`claude-plugins-guide_2026-07-25.md`), lu en entier.
- **Les 212 fichiers `06_Claude_Code_Bare/agents/*.md`** : cartographiés par nom (53 B3 + 8 B2 +
  4 B1 + ~40 A3 + 3 A1 + 6 A2 + 1 A0L = ~115 agents uniques) ; aucun lu en entier.
- **Les 194 fichiers `06_Claude_Code_Bare/skills/`** : cartographiés par nom (~30+ skills
  canon, dont `/youtube-to-guide`, `/b1-filter`, `/area-domain-doctrine-distill`, etc.).
- **Les 89 fichiers `commands/`, 56 `hooks/`, 15 `rules/`** : idem, cartographiés.
- **`04_From_V2_Root/` et `05_From_V2_Domains/`** : 22 707 fichiers `.md`, **délibérément**
  non lus (D-2026-08-01-#2 : « Hors-KB assumé »). Mesure structurelle faite via les 2 plans
  (`SECOND_BRAIN_PARA_MAP.md` + `JUNCTIONS_MAP_2026-08-02.md` + `FIX_KB_2026-08-02.md`).
- **`graphify-out/` (1 195 md)** : artefacts de build Graphify, structurellement non
  discriminants.
- **`03_Memory_Unified/LLM_Wiki/wiki/` (1 773 md)** : le wiki lui-même. Sa structure est
  cartographiée par `INDEX_OF_INDEXES.md` (319 liens, 61 KB) + `OKF_INDEX.md` (état de
  conformité zone par zone) + `wiki/ROT.md` (rot-rates).

**De côté par prudence** :

- **`08_Workspaces_Dormants_2026-08-01/`** : 21 workspaces inactifs ≥ 30 j. Le README les
  catalogue exhaustivement ; les dossiers eux-mêmes contiennent des outils externes
  (Antigravity, Conductor, Meta-Tools, etc.) dont l'inventaire n'est pas discriminants pour
  l'ontologie Geordi.
- **`09_From_Home_Root_Batch2_2026-08-01/`** : 50 fichiers déplacés, MANIFEST lu exhaustivement.

### 6.3. Détection de jonctions

Méthode : `os.scandir(root) + entry.stat(follow_symlinks=False).st_file_attributes & FILE_ATTRIBUTE_REPARSE_POINT`.

| Mesure | Compte | Source |
|---|---:|---|
| Jonctions **dossiers** canon (D1 receipt 2026-08-02) | **159** | `00_Index/JUNCTIONS_MAP_2026-08-02.md` §Chiffres clés |
| Reparse points (dossiers + fichiers) par mon scan | **225+** (walk partiel coupé à 225) | Mesure propre (incomplète) |
| Brief initial attendu | 47 | `00_Index/FIX_KB_BRIEF.md` ligne 7 |
| Jonctions mortes retirées à 2026-08-02 | **1** | `_from_coaching_premium` (`os.rmdir` — `FIX_KB_2026-08-02.md` §Tâche C) |
| Jonctions mortes restantes | **82** (61 `dead` + 21 `trash_jct`) | `JUNCTIONS_MAP_2026-08-02.md` §Classification par catégorie |

L'écart entre 47 et 159 est principalement constitué de :
- **91** dans `06_Claude_Code_Bare` (mémoires de graphify-out par app et par projet)
- **16** dans `07_From_Home_Root_2026-08-01/_TRASH_from_root/_TRASH_2026-07-03_broken_junctions/.claude-memory/jct-*`
- **5** dans `03_Memory_Unified/LLM_Wiki/wiki/_INTAKE/`

Source : `JUNCTIONS_MAP_2026-08-02.md` §Découverte + `FIX_KB_2026-08-02.md` §Tâche A Découverte à signaler.

---

## 7. Note sur la doctrine — ce que ce brief m'a forcé à observer

Trois doctrines majeures observées dans Geordi et qui peuvent **sembler** se contredire mais
sont en fait des **couches successives** (append-only D4) :

1. **OKF v0.1** = standard de format (4ᵉ pilier ajouté 2026-08-01).
2. **Owner registre** : 3 couches (`TAGS.md` v1 Doctor Who, `README.md` Doctor/Companion, v2
   Star Trek arbitré 2026-08-01) — l'arbitrage est fait, pas une contradiction ouverte.
3. **B2 mapping** : `_INDEX.md` (juillet 2026-07-03) vs `CLAUDE.md` A+ doctrine (juillet
   2026-07-27) — **2 doctrines coexistantes**, l'A+ doctrine étant append-only et annotée.

Le `CLAUDE.md` lui-même note la coexistence : « D4 append-only strict = folder names canon
unchanged + A+ doctrine annotated » (`06_Claude_Code_Bare/CLAUDE.md` §D1 honest gap).

**Ce qui n'est PAS une contradiction** mais une **stratification temporelle** :
- Le wiki grossit (246 → 1 773) sans index ré-aligné → drift, pas contradiction.
- Les sub-folders doublons (`01_Product_Product/`, etc.) → candidats reclassement, pas
  doctrine contradictoire.
- `05_Legal/` (folder canon) vs `08_Legal/` (A+ doctrine slot 8) → convention de nommage
  distincte, pas contradiction philosophique.

**Ce qui EST une contradiction ouverte** : la bijection `ADR-L2-BDLD-MAP-001` (« 8 B2 ↔ 8 LD »)
est rompue en pratique (5 Domaines sur 8 partagent leur LD avec un autre). À signaler sans
trancher.

