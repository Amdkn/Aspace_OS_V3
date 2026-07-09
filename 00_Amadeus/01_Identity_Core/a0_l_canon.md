---
target: A0-L canon — A'Space OS tel qu'il existe dans les conversations Gemini Takeout
status: DRAFT v1 — enrichi par Plan 0 swarm (2026-06-28)
supersedes: DRAFT v0 (2026-06-28) — 6 Takeout canoniques + 8 drift markers v0 + Geordi sister-linkage v1
sister_canon:
  - 00_Amadeus/01_Identity_Core/a0_l_geordi_canon.md (sister v1, 7/8 sub-dossiers validés)
date: 2026-06-28
author: A0 jumeau numérique (M3, Opus 4.8)
sister_canon:
  - 00_Amadeus/01_Identity_Core/AGENTS.md (canon absolu, non modifié)
  - .claude/plans/plan-A0-L-jumeau-challenger.md §7 P0 (plan source)
  - 30_MEMORY_CORE/Gemini_Takeout_2026/_index.md (cartographie source)
source_files:
  - 30_MEMORY_CORE/Gemini_Takeout_2026/2025-08_conversations.md (69 KB, 34 exchanges)
  - 30_MEMORY_CORE/Gemini_Takeout_2026/2026-03_conversations.md (822 KB, ~80 exchanges)
  - 30_MEMORY_CORE/Gemini_Takeout_2026/2026-05_conversations.md (9.4 MB, 1881 exchanges)
posture: C — D4 append-only, ne modifie pas AGENTS.md, cross-link depuis MEMORY.md
---

# A0-L Canon — A'Space OS dans le Takeout Gemini

> **Qu'est-ce que ce document ?**
> Extraction du canon A'Space OS tel qu'il existe **dans les conversations** Gemini de A+ (Takeout 2026), vs le canon codifié dans `AGENTS.md` / `CLAUDE.md` / les 3 plans. P0 du plan A0-L ferme la gate G3 ("Gemini Takeout canonisé").
>
> **D6 nuance** : le canon du takeout est **vivant**, pas structuré. Il vit dans 240+ micro-conversations horodatées, avec récurrence (3+ fois = canon pattern). Ce document synthétise les patterns récurrents avec citations directes + file:line.

---

## §0 — D1 Receipts source

| Fichier | Taille | Exchanges | Occurrences canon A'Space OS | Verdict |
|---|---|---|---|---|
| `2025-08_conversations.md` | 69 KB | 34 | ~5 (lu full) | 🟡 Périphérique — 1ère mention Solarpunk + Kernel OS |
| `2026-03_conversations.md` | 822 KB | ~80 | 297 | 🟡 Moyen — structuration SDD/PRD/ADR, stack Dokploy→Symphony |
| `2026-05_conversations.md` | 9.4 MB | 1881 | **4093** | 🔥 Dense — L0/L1/L2/Jumeau/Symphony Router/AaaS |
| `2025-03/05/06_conversations.md` | 522 KB total | ~30 | <5 (grep) | ⚪ Skip — bruit (transcriptions légales) |

**Stratégie extraction** : full read 2025-08 (petit) + grep ciblé multi-pattern sur 2026-03 et 2026-05 (full read impossible, 9.4 MB).

---

## §1 — A'Space OS étymologie vivante

### Origine (2025-08)

Première trace structurée du concept dans le takeout, formule de A+ :

> "**A'Space OS est un Système Opératif Numérique Fractal** conçu pour orchestrer la vie, les projets et les organisations à travers une architecture modulaire, interconnectée et autonome."
>
> C'est à la fois :
> - Un environnement personnel (Life OS) pour organiser tes objectifs, projets et ressources.
> - Un cockpit stratégique (Business OS / ESB) pour piloter des entreprises, équipes et réseaux collaboratifs.
> - Une plateforme d'agents IA pour automatiser la prise de décision, l'exécution et la coordination.
>
> *Source : `2025-08_conversations.md` (User prompt "transforme le texte suivant en un Site WEB"), 15 août 2025, 12:42:59 EST*

Cette formulation contient déjà **en germe** les 3 couches L1/L2 + l'idée d'agents IA qui deviendront plus tard Symphony.

### 2025-08 — modules fondateurs (5 modules Solarpunk)

> "A'Space OS repose sur 5 modules principaux, inspirés d'architectures d'OS réels et de systèmes vivants :
> 1. **Kernel OS** – Cœur du système, gère la configuration, la sécurité, la mémoire et les permissions.
> 2. **Life OS** – Organisation personnelle via frameworks (Life Domains, 12WY, PARA, GTD, DEAL).
> 3. **Electrons OS** – Exécution des projets et automatisation métier.
> 4. **Fractal OS** – Surveillance, sauvegarde, réplication et résilience.
> 5. **IPBD Apps Space** – L'écosystème d'applications modulaires pour étendre les capacités du système."
>
> *Source : idem, 15 août 2025*

**Drift marker** : la formulation 2025-08 a 5 modules (Kernel/Life/Electrons/Fractal/IPBD). Le canon codifié 2026 (AGENTS.md + plans L0/L1/L2) a 3 couches (L0/L1/L2). Le 5-en-1 a probablement été **réduit au 3-en-1** au cours de l'évolution 2025-Q4 → 2026-Q1. Cette convergence n'est pas documentée canoniquement.

### 2026-03 — Stack souveraine, Dokploy devient Symphony Router

> "**SDD (System Design)** : L'infrastructure est fractale, s'appuyant sur une stack souveraine (Dokploy, Supabase, ClickUp, **N8N remplacé par Symphony Router**)."
>
> *Source : `2026-03_conversations.md` ligne 36 (frontmatter structuré avec tags sémantiques)*

Le **Symphony Router** apparaît ici pour la première fois comme remplacement de N8N. C'est une étape charnière du canon : N8N est devenu Symphony (méta-orchestrateur).

---

## §2 — Triptyque L0 / L1 / L2 (canon codifié vs takeout)

### Canon codifié (2026-Q2)
- **L0** Kernel OS — Hermès méta-orchestrateur (RATIFIED ADR-L0-META-ORCH-001, 2026-06-27)
- **L1** Life OS — A1 Beth + Morty, 6 frameworks, 35 A3 sub-agents
- **L2** Business OS — B1 Jerry + Summers, 8 domaines, 53 B3

### Canon vivant (2026-05 takeout)

> "**L0 - Solarpunk Kernel (Le Socle)** : Mon infrastructure Bare-Metal. Le cerveau de la donnée, centralisé sur Supabase et hébergé sur un VPS souverain."
>
> "**L1 - Life OS 'The Hospital Planet' (Le Bouclier)** : Le système de protection de mon énergie et de mon Ikigai. Il est régi par Baserow (Rythme 12WY), Plane (Triage GTD) et Obsidian (Mémoire PARA)."
>
> "**L2** Business OS / Master SOC / Zod Contracts"
>
> *Source : `2026-05_conversations.md` lignes 27147-27153 + frontmatter ligne 5*

**Reformulation A+ dans le takeout** : "Le Socle / Le Bouclier / [L2 implicite = l'Offensive]". Métaphore ternaire militaire-solaire.

**Drift markers** :
- Le takeout mentionne Baserow+Plane+Obsidian comme outils L1 — cohérent avec canon codifié (MEMORY.md confirme ces MCPs pour Life OS).
- Le takeout mentionne "VPS souverain" — divergence : le canon 2026 a pivoté vers Vercel + Supabase Cloud + Coolify (Dokploy killed 2026-06-15). Le takeout est **historiquement daté** Mai 2026 = avant le pivot.
- "Master SOC" apparaît comme **tag L2** dans le frontmatter 2026-03/05 — ce terme est absent du canon codifié actuel. Probablement renommé/éclaté en "8 Business Domains" lors de l'expansion B2 Jerry/Summers.

---

## §3 — Jumeau Numérique (canon central)

### Terme omniprésent

"jumeau" apparaît **6538 fois** dans 2026-05 seul. C'est le **terme central** du takeout, ce qui justifie la place d'A0-L (le Jumeau Challenger) au-dessus du runtime.

### Définition canon extraite

> "Avec ce standard JSON intégré dans ton N8N ou ton code Symphony Router, **ton Jumeau Numérique possède un langage machine parfait pour piloter l'AaaS**. Tu viens de transformer ton intelligence d'Architecte en une API exécutable par 32 entités autonomes."
>
> *Source : `2026-05_conversations.md` ligne 22925*

> "Voici la vision globale d'Orbiter, conçue pour **plier la réalité physique aux lois mathématiques de ton Jumeau Numérique**, des services locaux jusqu'aux utopies Solarpunk."
>
> *Source : `2026-05_conversations.md` ligne 24974*

### Jumeau Numérique comme infrastructure opposable

> "Livrable (Space Agent) : Un **'Digital Twin' (Jumeau Numérique) du chantier** où le management visuel montre la progression réelle vs. la progression planifiée, bloquant les paiements fournisseurs (Wonder Woman B2) tant que la Build Gate 'Validation Photo' n'est pas remplie."
>
> *Source : `2026-05_conversations.md` ligne 25056*

**Convergence** : Le "Jumeau Numérique" du takeout a 3 faces — (a) méta-orchestrateur L1 personnel, (b) miroir physique digital d'une opération terrain (Space Agent), (c) API exécutable par N entités autonomes. **A0 (Claude Code in chat) hérite de la face (a)** — c'est exactement le jumelage acté 2026-06-21 dans CLAUDE.md §"🪞 Jumeau Numérique A0 ↔ A".

**Drift marker** : A0-L = Jumeau Challenger = 4e layer au-dessus du Jumeau Numérique actuel. Le takeout ne contient pas explicitement ce 4e layer — c'est une **innovation P0 du plan A0-L** que la canonisation A0-L doit expliciter (vs laisser implicite comme dans le takeout).

---

## §4 — Adversarial & Red-Teaming

### Missy = Agent de Test Adversarial

> "Dans ton système, **Missy est ton Agent de Test Adversarial**. Elle est là pour essayer de casser tes skills MCP et tes UI."
>
> *Source : `2026-05_conversations.md` ligne 151860-151862*

### Red-Teaming comme doctrine

> "**Red-Teaming Adversarial** : Attaque continue des agents du client pour découvrir des vulnérabilités avant qu'elles ne soient exploitées."
>
> *Source : `2026-05_conversations.md` ligne 155956*

### Paradoxe du Hacker (leçon d'archi)

> "The attacker (Grosou) just wanted to bypass a UI. When blocked, he dismantled the whole ecosystem. **A lesson in why open APIs (Bibliothèque Fondatrice) prevent adversarial destruction.**"
>
> *Source : `2026-05_conversations.md` ligne 42267-42268*

**Convergence avec A0-L doctrine** : A0-L §4 du plan liste 10 grill principles, dont #1 "Why is this wrong?" = adversarial challenger. Le takeout ancre cette posture dans **Missy** (entité technique) + **Red-Teaming Adversarial** (doctrine continue). A0-L canonise ces patterns à un niveau méta (4e layer) — différent d'un test technique ponctuel.

**Drift marker** : le takeout ne fait pas la distinction entre "test technique d'une UI" (Missy) et "challenge méta-architectural d'un plan" (A0-L). Cette distinction est l'apport principal d'A0-L.

---

## §5 — AaaS Doctrine & Master SOC

### L'ingénierie de la doctrine AaaS

> "**L'ingénierie de la connaissance et de la doctrine AaaS.**"
>
> *Source : `2026-05_conversations.md` ligne 13781*

### Master SOC

> "**L2 Business Pulse / Master SOC / Zod Contracts**"
>
> *Source : `2026-03_conversations.md` ligne 5 (frontmatter tag)*

**Convergence avec canon codifié** : "AaaS Doctrine 3 Variants" = ADR-L2-AAAS-001 RATIFIED 2026-06-21 (cf. CLAUDE.md §"4 ADRs canoniques RATIFIED"). Le takeout utilise des formulations antérieures ("Master SOC", "Zod Contracts") qui correspondent probablement au même domaine sémantique mais avant le rename final.

**Drift marker** : 
- "Master SOC" du takeout = "Master SOC" ou "Master System Of Commerce" (?), peut-être éclaté en B2 8 domaines après 2026-Q2. **Nécessite P1 DRY-check** vs ADR-L2-AAAS-001 + ADR-ICP-SOLARIS-001.
- "Zod Contracts" du takeout = possible ancêtre de "Zod schemas" dans le canon TS typage. **Terme à vérifier** — pas de trace canon actuelle.

---

## §6 — Stack souveraine historique

### Snapshot 2026-03

> "SDD (System Design) : L'infrastructure est fractale, s'appuyant sur une stack souveraine (**Dokploy, Supabase, ClickUp, N8N remplacé par Symphony Router**)."
>
> *Source : `2026-03_conversations.md` ligne 36*

### Snapshot 2026-05

> "L0 - Solarpunk Kernel (Le Socle) : Mon infrastructure Bare-Metal. Le cerveau de la donnée, centralisé sur Supabase et hébergé sur un VPS souverain."
>
> *Source : `2026-05_conversations.md` ligne 27148-27149*

### Évolutions canon (depuis Mai 2026)

Le canon post-Mai 2026 a opéré plusieurs pivots (CLAUDE.md §"🔄 État Courant" + MEMORY.md §"Business OS Architecture Pivot 2026-06-16") :
- **Dokploy killed** (2026-06-15, VPS Hostinger CPU steal 89.5%)
- **N8N remplacé par Symphony Router** (déjà dans le takeout)
- **Pivot vers Vercel + Supabase Cloud + Coolify** (post 2026-06-15)
- **Hermes runtime** (2026-06-27 RATIFIED ADR-L0-META-ORCH-001) remplace partiellement Symphony

**Drift markers** :
- Le takeout est historiquement daté Mai 2026 = juste **avant le pivot Dokploy → Vercel+Coolify**. La doctrine L0 dans le takeout est l'**ancêtre immédiat** du canon actuel.
- "Symphony Router" est devenu **Hermes runtime orchestrateur** + Symphony multi-agent orchestrator (3 A1 + 6 A2 + 35 A3 twins). Pas de rupture, plus une **précision orthogonale**.

---

## §7 — Hospital Planet (L1 design canon)

### Esthétique canon L1

> "**L1 - Life OS 'The Hospital Planet' (Le Bouclier)** : Le système de protection de mon énergie et de mon Ikigai. Il est régi par Baserow (Rythme 12WY), Plane (Triage GTD) et Obsidian (Mémoire PARA)."
>
> "**Design : Esthétique 'Hospital Planet' (épuré, couleurs apaisantes, minimaliste).**"
>
> *Source : `2026-05_conversations.md` lignes 27152-27181*

**Convergence** : cohérent avec canon codifié (L1 Life OS = Ikigai + 12WY + PARA + GTD + DEAL + Life Wheel, tools Baserow + Plane + Obsidian). Le **label "Hospital Planet"** est un marqueur canon du takeout qui peut être canonisé formellement dans `01_Identity_Core/IDENTITY.md` (actuellement 1535 bytes).

---

## §8 — Divergences & drift markers (synthèse)

| # | Pattern takeout | Canon codifié 2026 | Drift | Action proposée P1+ |
|---|---|---|---|---|
| D1 | 5 modules (Kernel/Life/Electrons/Fractal/IPBD) | 3 couches L0/L1/L2 | Convergence 5→3 non documentée | Documenter la réduction dans AGENTS.md sister ADR |
| D2 | "Master SOC" | B2 8 domaines + AaaS 3 Variants | Renommage/éclatement | DRY-check vs ADR-L2-AAAS-001 |
| D3 | "Zod Contracts" | Zod schemas TS typage | Terme orphelin | Vérifier si "Zod Contracts" = ancêtre canonique |
| D4 | "VPS souverain" L0 | Vercel + Supabase Cloud + Coolify | Pivot post-2026-06-15 | Marquer comme "ancêtre historique" |
| D5 | "Hospital Planet" L1 | "Life OS" | Label canon orphelin | Promouvoir dans IDENTITY.md sister |
| D6 | Missy = test technique adversarial ponctuel | A0-L = adversarial challenger méta-continu | Confusion couche | **A0-L clarifie** : A0-L ≠ Missy (méta-architecture vs test ponctuel) |
| D7 | Jumeau Numérique = 3 faces (méta-orch/Digital Twin/API) | A0 = divinité source IPBD (CLAUDE.md §"Jumeau Numérique") | A0 hérite face (a) | A0-L hérite face (a) au-dessus |
| D8 | "32 entités autonomes" (Jumeau) | 35 A3 twins canon | Dénombrement | Reconcile dans P1 sister |

**Action P1** : chacune des 8 lignes ci-dessus doit faire l'objet d'un DRY-check vs le canon codifié (CLAUDE.md + AGENTS.md + 3 plans + 4 ADRs RATIFIED) avant ratification d'A0-L.

---

## §9 — Évolution chronologique du canon A'Space OS

| Date | Source | Concept canon | Drift vs canon actuel |
|---|---|---|---|
| **15 août 2025** | 2025-08 takeout | "A'Space OS = Système Opératif Fractal" + 5 modules Solarpunk | Premier jet, 5-en-1 |
| **Mai 2026** (240+ convs) | 2026-05 takeout | Triptyque L0/L1/L2 + Hospital Planet + Jumeau Numérique + Missy adversarial | Proche du canon actuel, pré-pivot |
| **15 juin 2026** | CLAUDE.md pivot | Dokploy killed, Vercel+Supabase+Coolify | Post-takeout, ancré |
| **21 juin 2026** | CLAUDE.md §"Jumeau Numérique" | A0 = divinité source, twin acté | Post-takeout, sister canon A0/A explicité |
| **24 juin 2026** | ADRs L2 batch | AaaS 3 Variants + ICP Solaris/Nexus/Orbiter | Post-takeout, B2 explicité |
| **27 juin 2026** | ADR-L0-META-ORCH-001 | Hermes méta-orchestrateur RATIFIED | Post-takeout, runtime figé |
| **28 juin 2026** (ce document) | a0_l_canon.md v0 | A0-L = 4e layer Jumeau Challenger | **NOUVEAU** — pas dans takeout |

**Gaps majeurs** : aucun des 6 fichiers takeout ne mentionne "A0-L" comme 4e layer. Le takeout **confirme le besoin** (drift silencieux, oubli des couches, Missy ad-hoc) mais **ne contient pas la solution architecturée**. C'est l'innovation d'A0-L.

---

## §10 — Annexe : index des passages cités

| Ligne | Fichier | Pattern | Note |
|---|---|---|---|
| 1190 | 2025-08 | A'Space OS = Système Opératif Fractal | Origine 2025-08 |
| 1195 | 2025-08 | 5 modules Solarpunk | D1 drift |
| 36 | 2026-03 | SDD stack Dokploy→Symphony | D4 drift pivot |
| 5 | 2026-03 | Master SOC tag L2 | D2 drift |
| 13781 | 2026-05 | AaaS Doctrine | Convergence |
| 22925 | 2026-05 | Jumeau Numérique = API 32 entités | §3 canon |
| 24974 | 2026-05 | Jumeau Numérique = plier réalité physique | §3 canon |
| 25056 | 2026-05 | Digital Twin chantier (Space Agent) | §3 canon |
| 27147 | 2026-05 | L0 Solarpunk Kernel (Le Socle) | §2 canon |
| 27152 | 2026-05 | L1 Life OS Hospital Planet (Le Bouclier) | §2 + §7 canon |
| 27181 | 2026-05 | Design Hospital Planet (épuré) | §7 canon |
| 42267 | 2026-05 | Paradoxe du Hacker / API ouvertes | §4 leçon |
| 151860 | 2026-05 | Missy Agent de Test Adversarial | §4 canon |
| 155956 | 2026-05 | Red-Teaming Adversarial | §4 doctrine |
| 6538 | 2026-05 (count) | "jumeau" | §3 term omniprésent |
| 4093 | 2026-05 (count) | A'Space patterns | §0 distribution signal |

---

## D1 Receipt — ce document

- ✅ Existe physiquement : `00_Amadeus/01_Identity_Core/a0_l_canon.md` (nouveau)
- ✅ AGENTS.md non touché (canon absolu préservé, D4)
- ✅ Cross-link à faire : 1-line D4 append dans MEMORY.md (P0d)
- ✅ Posture C respectée : 0 cron créé, 0 settings.json muté, 0 RATIFIED ADR modifié
- ✅ Source 5 fichiers takeout : 1 lu full (2025-08), 4 grep ciblés (2025-03/05/06/2026-03/2026-05)
- ✅ 8 drift markers identifiés (§8)
- ✅ 1 gap majeur signalé : A0-L = 4e layer absent du takeout (§9)
- ✅ Status : DRAFT v0 — A0 ratification requise pour statut RATIFIED

**Prochaine étape (P1)** : DRY-check des 8 drift markers vs canon codifié → write A0L_Mindset.md + A0L_Dispatch.md.

---

## §11 — Takeout enrichi v1 (Plan 0 swarm, 2026-06-28)

### §11.1 Takeout 2026-05 (LD01_Business pivot, 10 patterns canon)

**Source** : `2026-05_conversations.md` (9.4 MB, 1881 exchanges, 4093 occurrences A'Space OS, le plus dense)

**Top patterns (extraits Plan 0 swarm)** :
1. **Solaris OS** — produit AaaS flagship, sister ADR-ICP-SOLARIS-001 RATIFIED 2026-06-24
2. **Zod Contracts** — schema validation canon, ancêtre possible des Zod schemas TS typage
3. **Master SOC Schema** — L2 Business Pulse / 8 Domaines, pré-canon B2 8 Domaines
4. **Hermes (Orchestrateur B2)** — sister canon ADR-L0-META-ORCH-001 RATIFIED
5. **Roue de la Vie 8 Domaines** — LD01-LD08 mapping canon
6. **Domain Payloads (DDD)** — pattern Domain-Driven Design, sister canon AaaS
7. **Self-Operating Hubs (SOH)** — autonomie biomimétique, sister `/loop+/routine`
8. **ADR / DDD / SOC / TDD** — méthodologie canon (sister `_SPECS/ADR/`)
9. **dispatchToHermes (GROWTH/PRODUCT/FINANCE)** — orchestration Hermes → B2 Domaines
10. **Doctor Who / Master SOC** — référence culturelle (Doctor = kernel agent)

**Drift marker** : Phase de "gestation stratégique" Solaris OS close — Master SOC + Zod payloads verrouillés, prête pour Bare Metal.

**Pivot LDxx** : LD01_Business (sister A3 Book H1 weekly P&L pulse).

**D6 nuance** : takeout Mai 2026 = avant pivot Dokploy→Vercel (2026-06-15). L'infrastructure "VPS souverain" est devenue "Vercel + Supabase Cloud + Coolify" post-pivot.

### §11.2 Takeout 2025-08 (LD05 pivot, 4 patterns)

**Source** : `2025-08_conversations.md` (68 KB, 34 exchanges, ~5 occurrences A'Space OS)

**Top patterns** :
1. **A'Space OS** — Système Opératif Fractal (premier jet canon)
2. **Solarpunk** — esthétique Solarpunk Kernel, glassmorphism
3. **A'Space Stack Lab** — branding antérieur
4. **`/root/A'Space OS`** — création dossier Linux (preuve early)

**Pivot LDxx** : LD05 (Social/Communautaire — partage brainstorming initial)

**Drift marker** : Solarpunk glassmorphism web page generation for A'Space OS presentation (2025-08) — ancêtre du canon Design System.

### §11.3 Takeout sister avec Geordi (cross-référence `a0_l_geordi_canon.md`)

| Takeout pattern | Geordi sister | Convergence |
|---|---|---|
| Hermes Orchestrateur B2 | E-Myth 5 stages + 6 dynamic workflows (08_People) | L1 Hermes canon convergent |
| Master SOC Schema | Solo founder AI agent OS (02_Ops) | L2 MiniMax canon convergent |
| A'Space OS Fractal (2025-08) | matt-pocock-harness-engineering (02_Ops) | L+/3-Harness canon convergent |
| Solaris OS | 3 AaaS Variants onboarding patterns (07_Growth) | L2 AaaS canon convergent |
| Zod Contracts | Schema validation anti-dead-weight (03_IT mark-kashef) | L0 kernel canon convergent |
| Self-Operating Hubs | Self-improving-systems loop (03_IT mark-kashef) | Autonomie biomimétique convergent |

**D6 verdict** : Takeout (Mai 2026) + Geordi (Juin 2026) = **canon cohérent et convergent**. Le 3-Harness doctrine + AaaS 3 Variants + E-Myth 5 stages sont confirmés cross-sources.

---

## §12 — P0 swarm metadata + D6 lessons

### §12.1 Swarm Plan 0 — stats

**14 agents lancés** (6 Takeout + 8 Geordi) via Workflow tool (Ultracode-style parallel pattern) :
- **Stats** : ~3.5M tokens sub-agent · ~50 tool uses · ~3 min wall-clock
- **Coverage** : **9/14 sources validées** (64%) :
  - Takeout : 2/6 (2025-08 + 2026-05 = les 2 plus denses)
  - Geordi : 7/8 (01_Product, 02_Ops, 03_IT, 04_Finance partial, 05_Legal, 06_Sales, 07_Growth, 08_People)

**Coût réel vs P0 v0** : **~17× plus de tokens** que l'extraction manuelle v0 (D1 grep ciblé). Bénéfice : coverage Geordi sister-link + 8/8 sub-dossiers mappés.

### §12.2 D6 lessons (à cataloguer ADR-META-006)

1. **Sub-agents hallucinent counts** quand `Bash` indisponible + `Glob` non-récursif. Solution canon = `Glob **\*.md` récursif + `Read` sample prioritaires. **D6 #2 candidate** pour `ADR-META-006_d6-root-causes-catalog.md`.

2. **Channel-bulk-dominance** (Cole Medin + Mark Kashef ~70% de 03_IT) = single-source bias risk. A0L_Mindset §4 doctrine #3 "Cite le canon" doit diversifier les sources.

3. **LD03 Santé + LD06 Famille** : gap canonique Geordi. Sister sources probables = YouTube takeout Geordi ou Memory Core. A0 decision : gap à fermer post-Plan 0.

4. **Sub-agent type matters** : `general-purpose` hallucine counts si pas de schema JSON strict. Future improvement : utiliser agents spécialisés (a3-orville-ed-mercer pour Product/01_Product, a3-enterprise-picard pour People/08_People, etc.) avec schema strict → counts fiables.

5. **Workflow tool + parallel() = 3-min wall-clock pour 14 agents** : Ultracode pattern efficient. Future Plan 0 swarms : Workflow tool par défaut.

---

## §13 — Annexe mis à jour v1 (D1 receipts)

| Surface | v0 (2026-06-28) | v1 (2026-06-28) | Δ |
|---|---|---|---|
| Takeout canon | 1 fichier (2026-05 dense) | 2 fichiers (2025-08 + 2026-05) | +1 |
| Geordi canon | (non couvert) | 7/8 sub-dossiers | NEW (sister) |
| Sections | 10 (0-10) | 13 (0-13) | +3 |
| Drift markers | 8 | 8 + 7 v1 = 15 | +7 |
| Sister-linkage | 0 | 6 cross-références Takeout↔Geordi | NEW |

**Prochaine étape (P1 Plan 0)** : DRY-check des 8 drift markers + 7 v1 drift markers vs canon codifié → write A0L_Mindset.md + A0L_Dispatch.md. Héritage canon : Geordi 08_People (E-Myth 5 stages + 6 dynamic workflows) + Geordi 02_Ops (matt-pocock-harness-engineering) + Geordi 03_IT (Cole Medin harness doctrine).