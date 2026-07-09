---
id: ADR-SKILLS-CANON-001
title: Skills Canon — Inventaire + Activation Conditions pour DDD Landing Pages OMK Nexus
status: RATIFIED
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-0"
  context: "Ratification Tier 0 foundational DDD Landing Pages — 4 ADR bases (ANTI-TEMPLATE + ANTI-PAPERCLIP + SKILLS-CANON + WORKFLOW) ratifiés en bloc suite Phase 5 multi-workflow validée."
date: 2026-07-06
deciders: A0 (Amadeus, divinité source)
proposed_by: B1 E-Myth Gatekeeper (J01_Prime Jerry Prime ↔ B1 Summers Nexus OMK BOS, sister canon ADR-L2-AAAS-001)
domain: L2_Business_OS
tags: [skills, canon, inventory, activation, landing-pages, omk-nexus, e-myth, b1-gatekeeper, a0-ultimatum, ddd]
related:
  - CLAUDE.md §"🛠️ Doctrine Skill Creator Reflex (Anti-Répétition)"
  - CLAUDE.md §"Doctrine Anti-Paresse" (ADR-META-001)
  - MEMORY.md §"Topic summaries" (skills canon pointers)
  - ADR-SOBER-002 (Anti-Paperclip, sobriety gate)
  - ADR-L2-AAAS-001 (AaaS Doctrine 3 Variants, sister canon)
  - ADR-ICP-NEXUS-001 (ICP Nexus OMK, sœur landing)
  - ADR-LANDING-AESTHETIC-001 (sœur landing canon — HYPOTHÈSE si pas encore canonisé)
  - PRD-B1-FILTER-M3-001 (sœur PRD canon — HYPOTHÈSE)
supersedes: none
sources_canons:
  - C:\Users\amado\.claude\CLAUDE.md
  - C:\Users\amado\.claude\memory\MEMORY.md
  - C:\Users\amado\.claude\skills\<repertories canon>
  - C:\Users\amado\.claude\plugins\cache\claude-plugins-official\<repertoires Anthropic>
  - C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\META\ADR-META-001_anti-paresse-verify-before-assert.md
  - C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L1_Life_OS\ADR-META-005_hooks-automation.md
  - C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md
---

# ADR-SKILLS-CANON-001 — Skills Canon Inventory + Activation Conditions

> **Purpose** : Établir l'inventaire canonique des skills activées pour le DDD Landing Pages OMK Nexus, leurs **activation conditions** (trigger phrase canon), **sister-canon links**, **lifecycle**, et **anti-patterns interdits**. Ce document est **l'ADR de référence** pour tout A2/A3/B3 qui ouvre une skill dans un workflow Landing.

---

## 1. Contexte (Context)

**Pourquoi maintenant.** Le DDD (Domain-Driven Design) Landing Pages OMK Nexus est un projet L2 multi-workflow qui mobilise :

- 3 AaaS sisters (Solaris/Nexus/Orbiter) sister-canon ADR-L2-AAAS-001
- 3 ICP distincts (Coach/Mentor/Avocat × fr/en) sister-canon ADR-NEXUS-LANDING-PERSONAS-001
- Cycle 12WY Q3 2026 (06/15 → 09/07/26) sister-canon plan-L1-life-os.md §11
- Architecture : Vercel (FE) + Supabase Cloud (BE) + Hermes+Claude (workflow) + Coolify (N8N only)

**Le risque.** Sans inventaire canonique, on observe 3 dérives typiques :
1. **Skill fantôme** (invoquée dans le chat mais inexistante sur disque) → D6 root-cause classique
2. **Skill dupliquée** (même intent couvert par 2+ skills) → confusion routage A3
3. **Skill obsolète** (cassée, brisée, ou supplantée) → D7 cost-of-escalation si A0 escalade

**Doctrine upstream.** Cet ADR s'inscrit dans la chaîne :
```
A0 intention
  → B1 E-Myth Gatekeeper (Jerry Prime ↔ Summers Nexus)        ← CET ADR scope
    → A2 USS <Ship> Manager (Orville/Cerritos/Discovery/SNW/Enterprise/Protostar)
      → A3 <Name> execute + skill invocation
```

---

## 2. Décision (Decision)

**On ratifie** un inventaire canonique à **5 tiers** (A→E), chaque skill pointer-explicitement vers :
- Son **trigger phrase canon**
- Son **sister-canon ADR** (le cas échéant)
- Sa **HYPOTHÈSE / ✅ Status d1**
- Son **lifecycle phase** (initiation / first-use / mature / retire)
- Son **anti-pattern flag** (le cas échéant)

**On interdit** (Tier E) :
- Skills cassées (ex : `clara-voice` per MEMORY.md)
- Skills fantômes (inventées en chat, absentes de `~/.claude/skills/`)
- Skills redondantes sans sœur canon

---

## 3. Inventaire canonique par Tier (D1-verified)

### Tier A — Création Landing (frontend-design-grade)

| # | Skill | Path (D1) | Status | Trigger phrase canon | Sister-canon |
|---|---|---|---|---|---|
| A.1 | `frontend-design` | `C:\Users\amado\.claude\plugins\cache\claude-plugins-official\frontend-design\76b35e91d1c9\skills\frontend-design\SKILL.md` | ✅ Status d1 | "build a landing page", "redesign this UI", "audit the visual quality" | ADR-LANDING-AESTHETIC-001 (HYPOTHÈSE — sister canon à canoniser), CLAUDE.md §"Web Design Quality Standards" |
| A.2 | `frontend-design:frontend-design` | idem ci-dessus (namespace) | ✅ Status d1 | (sub-skill namespace invocation) | idem |
| A.3 | `dataviz` | plugin entry per system-reminder ; **non trouvé dans `~/.claude/plugins/cache/claude-plugins-official/` ce cycle** | ⚠️ HYPOTHÈSE | "build a dashboard chart", "make this graph consistent with the design system" | ADR-LANDING-AESTHETIC-001 §"data viz" (HYPOTHÈSE) |
| A.4 | `swarm-orchestrator` | `C:\Users\amado\.claude\skills\swarm-orchestrator\SKILL.md` | ✅ Status d1 | "orchestrate a swarm", "fan-out this workflow", "parallelize these A3 sub-tasks" | CLAUDE.md §"Doctrine Swarm Orchestration", A2 Protostar §Liberate |

> **Note Tier A** : ces skills sont les briques de **création directe** de la Landing (visuels, charts, copy, interactions). Sister-canon **pointent vers ADR-LANDING-AESTHETIC-001** qui reste à canoniser (D1: pas trouvé dans `_SPECS/ADR/L2_Business_OS/` ce cycle).

---

### Tier B — Gouvernance (B1 + B3-grade)

| # | Skill | Path (D1) | Status | Trigger phrase canon | Sister-canon |
|---|---|---|---|---|---|
| B.1 | `b1-filter` | `C:\Users\amado\.claude\skills\b1-filter\SKILL.md` | ✅ Status d1 | "classifie les guides Geordi", "E-Myth filter this guide", "is this doctrine or noise" | PRD-B1-FILTER-M3-001 (HYPOTHÈSE — sister PRD à canoniser), B1 Jerry Prime |
| B.2 | `ratify-adr` | `C:\Users\amado\.claude\skills\ratify-adr\SKILL.md` | ✅ Status d1 | "ratify this ADR", "promote to canonical", "validate ADR gates" | ADR-META-001 §D5 ratification gates, B1 Gatekeeper canon |
| B.3 | `premortem-fill` | `C:\Users\amado\.claude\skills\premortem-fill\SKILL.md` | ✅ Status d1 | "premortem this project", "list F1-F15 risks", "fill the premortem template" | ADR-SOBER-002 Anti-Paperclip trigger #1-7, A0 ultimatum log |
| B.4 | `canon-batch-spawn` | `C:\Users\amado\.claude\skills\canon-batch-spawn\SKILL.md` | ✅ Status d1 | "spawn canon batch", "create N ADRs in parallel", "canonize 4-10 files in one pass" | CLAUDE.md §"Skill Creator Reflex" Phase 2, A2 Protostar §Liberate |

> **Note Tier B** : ce sont les **gouvernance-gates**. Chaque skill ouvre/ferme un état canonique (DRAFT→RATIFIED, _TRASH→archives, etc.). **Toujours invoquer avant** les skills Tier A pour cadrer l'intention.

---

### Tier C — Orchestration méta (multi-routines-grade)

| # | Skill | Path (D1) | Status | Trigger phrase canon | Sister-canon |
|---|---|---|---|---|---|
| C.1 | `multi-goal` | `C:\Users\amado\.claude\skills\multi-goal\SKILL.md` | ✅ Status d1 | "track N goals in parallel", "multi-goal scorecard", "12WY multi-objective" | plan-L1-life-os.md §11 (12WY Q3 2026), A2 USS SNW Execution |
| C.2 | `multi-routines-12wy` | `C:\Users\amado\.claude\skills\multi-routines-12wy\SKILL.md` | ✅ Status d1 | "run multi-routines 12WY", "scorecard weekly", "H1/H10/H30/H90 routine sync" | ADR-L2-BDLD-MAP-001, A2 USS Discovery Balance |
| C.3 | `wargame` | `C:\Users\amado\.claude\skills\wargame\SKILL.md` | ✅ Status d1 | "wargame this ICP", "3-ICP variants stress-test", "competitive wargame" | ADR-L2-AAAS-001 §D2 (3 sisters), ADR-ICP-NEXUS-001 |
| C.4 | `loop` | system-reminder entry (built-in CC) ; non-disk-resident | ✅ Status d1 | "/loop 5m /<skill>", "poll this every N minutes" | CLAUDE.md §"Fable × Auto-Research × /loop × Symphony" |

> **Note Tier C** : orchestration méta des routines du cycle. **Toujours invoquer APRES** Tier B (gouvernance cadrée) et **AVANT** Tier A (création outillée).

---

### Tier D — Ops canon (multi-workflow + openspec + replicate)

| # | Skill | Path (D1) | Status | Trigger phrase canon | Sister-canon |
|---|---|---|---|---|---|
| D.1 | `multi-workflow` | `C:\Users\amado\.claude\skills\multi-workflow\` (dir exists, **no SKILL.md at root — HYPOTHÈSE** sub-skill structure) | ⚠️ HYPOTHÈSE | "fan-out this workflow", "N workflows in parallel" | CLAUDE.md §"Skill Creator Reflex" (multi-workflow sister) |
| D.2 | `openspec-apply-change` | `C:\Users\amado\.claude\skills\openspec-apply-change\` (no SKILL.md found — HYPOTHÈSE) | ⚠️ HYPOTHÈSE | "/opsx:apply", "apply this OpenSpec change" | OpenSpec canon (3 sisters), A2 USS Enterprise Structure |
| D.3 | `openspec-archive-change` | idem D.2 dir | ⚠️ HYPOTHÈSE | "/opsx:archive", "retire this OpenSpec" | idem D.2 |
| D.4 | `openspec-explore` | idem D.2 dir | ⚠️ HYPOTHÈSE | "/opsx:explore", "explore an OpenSpec change space" | idem D.2 |
| D.5 | `openspec-propose` | idem D.2 dir | ⚠️ HYPOTHÈSE | "/opsx:propose", "propose a new OpenSpec change" | idem D.2 |
| D.6 | `replicate-squads` | `C:\Users\amado\.claude\skills\replicate-squads\SKILL.md` (✅) + `scripts\replicate_squads.ps1` | ✅ Status d1 | "replicate squad roster", "build B3 from canon" | ADR-CANON-001 (Roster Source of Truth), B1 E-Myth |

> **Note Tier D** : ops infrastructurels. `openspec-*` ont des répertoires créés mais aucun SKILL.md trouvé — **HYPOTHÈSE = à vérifier au D6 #4** (CC tool registry static, voir MEMORY.md §"MCP add OMK+ABC 2026-06-17 (D6 #4 NEW)").

---

### Tier E — OBSOLÈTE / broken / redirigés (D1 receipts)

| # | Skill | Status | Action canonique | Source |
|---|---|---|---|---|
| E.1 | `clara-voice` | ⚠️ **BROKEN** (per MEMORY.md §apps + CLAUDE.md §Clara Voice hands-free) | Rediriger vers **SAPI Hortense** Stop hook pattern ; voir `C:\Users\amado\.claude\rules\hooks.md §"Stop Hook TTS Pattern (SAPI Hortense)"` | D1-verified via MEMORY.md + CLAUDE.md |
| E.2 | Telegram MCP (`plugin:telegram:telegram`) | ⚠️ **DORMANT** (per `mindsets/Telegram_HITL_Mindset.md` 2026-06-25) | **NE PAS activer** sauf A0 GO explicite ; 4 HITL gates pending | D1-verified via MEMORY.md §"Telegram HITL + Desktop Commander 2026-06-25" |

> **Anti-pattern Tier E** : invoquer ces skills = D7 cost-of-escalation immédiat. **Jamais auto-activer** sans A0 HITL GO.

---

## 4. Activation Conditions (le *quand*)

### 4.1 Règle d'or (gate B1)

```
Avant toute invocation Tier A → Tier B → Tier C → Tier D
                            (gouvernance) (méta) (ops)
                              ↓
                            Tier A (création outillée)
```

**Pourquoi**. Sister-canon ADR-L2-AAAS-001 impose que chaque livraison L2 passe par une **gouvernance cadrée** (B1) AVANT l'outillage (Tier A). Inversion = D6 #4 root cause classique (skill invocée hors-cadre).

### 4.2 Trigger phrases canon (vocabulary strict)

| Trigger | Skill attendue | Tier |
|---|---|---|
| "build a landing page" | `frontend-design` | A.1 |
| "classifie les guides Geordi" | `b1-filter` | B.1 |
| "ratify this ADR" | `ratify-adr` | B.2 |
| "premortem this project" | `premortem-fill` | B.3 |
| "spawn canon batch" | `canon-batch-spawn` | B.4 |
| "multi-goal scorecard" | `multi-goal` | C.1 |
| "H1/H10/H30/H90 routine sync" | `multi-routines-12wy` | C.2 |
| "3-ICP variants stress-test" | `wargame` | C.3 |
| "/loop 5m /<skill>" | `loop` | C.4 |
| "fan-out this workflow" | `multi-workflow` | D.1 ⚠️ HYPOTHÈSE |
| "/opsx:apply" | `openspec-apply-change` | D.2 ⚠️ HYPOTHÈSE |
| "replicate squad roster" | `replicate-squads` | D.6 |

### 4.3 Sister-canon lookup rapide

| Si la skill sert... | Sister-canon |
|---|---|
| une Landing OMK Nexus | ADR-ICP-NEXUS-001 + ADR-NEXUS-LANDING-PERSONAS-001 |
| une canonisation ADR | ADR-META-001 + ADR-META-005 (hooks automation) |
| une sobriété check | ADR-SOBER-002 Anti-Paperclip |
| un ICP wargame | ADR-L2-AAAS-001 §D2 |
| un 12WY cycle | plan-L1-life-os.md §11 + 36 (cycles Q3-Q4 2026) |

---

## 5. Skill Creator Reflex Phase 2 (cite verbatim depuis CLAUDE.md)

> *"À la fin d'une session (ou quand le travail en cours se termine naturellement et qu'aucune nouvelle question n'est pendante), l'agent **automatise la création du skill** sans demander l'accord de A0. Le réflexe est l'autorisation, pas une demande."*
> — CLAUDE.md §"Doctrine Skill Creator Reflex"

### 5.1 Triggers obligatoires (CLAUDE.md)

1. **Répétition** : la même séquence de 3+ tool calls a été exécutée 2× dans la session.
2. **Checklist longue** : ≥5 étapes mêlant Bash/Edit/Write.
3. **Documentation de workflow** : .md dans MEMORY_CORE qui décrit "comment faire X" avec commandes shell.
4. **Scaffold detection** : fichiers générés selon template récurrent (ADR, agent capsule, etc.).
5. **Handoff manuel** : brief pour autre agent avec procédure exécutable.

### 5.2 Phase 2 — Création autonome (Hermes-style)

À la fin d'une session, l'agent **automatise** la création du skill sans demander A0 GO :

```
1. Auditer la session pour les 5 triggers
2. Identifier le skill le plus utile (le + observé, + répétitif, ROI le + haut)
3. Invoquer /skill-creator avec brief complet (triggers, ROI, test cases)
4. Écrire dans wiki/log.md : "Skill /<name> créé en autonomie (Hermes-style). Trigger : [X]. ROI : ~X min."
5. Signaler à A0 dans le rapport final de session — A0 peut review/veto post-hoc
```

**Rationale** (CLAUDE.md) : *"le coût d'escalade A0 (D7, ~100×) dépasse largement le coût d'une fausse création de skill (~5 min perdues)"*.

---

## 6. Anti-patterns interdits

| # | Anti-pattern | Tier | Sanction |
|---|---|---|---|
| AP.1 | Invoquer `clara-voice` MCP au lieu de SAPI Hortense | E.1 | D7 cost-of-escalation immédiat + break TTS |
| AP.2 | Invoquer Telegram MCP sans A0 HITL GO | E.2 | D6 #4 root cause (plugin cassé sans check `.mcp.json`) |
| AP.3 | Invoquer une skill Tier A sans Tier B préalable | A | D6 #6 swarm `rc=1` partial |
| AP.4 | Invoquer une skill inventée en chat mais absente du disque | n/a | Skill fantôme = pas d'effet → A0 escalade D7 |
| AP.5 | Invoquer `frontend-design` sans avoir chargé le sister-canon `web/design-quality.md` | A.1 | Sortie template-like bannie par `rules/ecc/web/design-quality.md §"Anti-Template Policy"` |
| AP.6 | Dupliquer un skill (même intent, 2 skills) | n/a | D6 confusion routage A3 → ratifier le doublon ou `_TRASH_<date>/` |
| AP.7 | Oublier D4 append-only (modifier une skill existante vs append + nouvelle) | n/a | D4 violation = `_TRASH_<date>_obsolete_<skill>/` |

---

## 7. Lifecycle (4 phases)

```
[Initiation] → [First-Use] → [Mature] → [Retire]
     DRAFT        HYPOTHÈSE    ✅ Status d1   _TRASH_<date>/
```

### 7.1 Phase Initiation

- **Critère** : skill mentionnée pour la 1ère fois dans canon, sans path D1-verified
- **Statut** : DRAFT (ce document, par exemple pour `multi-workflow` D.1 / `dataviz` A.3 / `openspec-*` D.2-D.5)
- **Action** : lister dans §3 avec ⚠️ HYPOTHÈSE + flagger comme TODO D1-verification

### 7.2 Phase First-Use

- **Critère** : SKILL.md existe sur disque MAIS pas encore ratifié dans un ADR sister
- **Statut** : ✅ Status d1 (path verified) MAIS ⚠️ pas sister-canon
- **Action** : invoquer 1× en production, puis promote §3 vers Mature si DoD atteint

### 7.3 Phase Mature

- **Critère** : SKILL.md + sister-canon ADR + ≥3 invocations sans D6 incident
- **Statut** : ✅ Status d1 + ✅ Sister-canon
- **Action** : ratifier dans ADR-sister (ex : `replicate-squads` + ADR-CANON-001 ✅)

### 7.4 Phase Retire

- **Critère** : skill cassée, supplantée, ou D7 cost-of-escalation > ROI
- **Statut** : ⚠️ OBSOLÈTE
- **Action** : déplacer dans `_TRASH_<date>_obsolete_<skill>/` (D4 append-only, **jamais hard-delete**)

---

## 8. Conséquences (Consequences)

### 8.1 Positives

- **D1-receipts systématiques** : aucune skill invoquée sans path vérifié
- **Tier-ordered routing** : Tier B → C → D → A (gouvernance d'abord)
- **Sister-canon links** : chaque skill pointer-explicitement vers son ADR-sister
- **Anti-pattern table** : 7 interdits nommés + sanction

### 8.2 Négatives / risques

- **D6 #4 latent** : CC tool registry STATIC ; nouvelles skills ajoutées au `.mcp.json` ignorées jusqu'au CC restart (cf. MEMORY.md §"MCP add OMK+ABC 2026-06-17 (D6 #4 NEW)")
- **HYPOTHÈSE inventory** : 6 skills (A.3, D.1, D.2, D.3, D.4, D.5) marquées ⚠️ — D1-verification à faire avant Tier Mature
- **Skill Creator Reflex Phase 2 drift** : risque de sur-création si l'agent n'audite pas les 5 triggers correctement

### 8.3 Coût d'escalade (D7)

- **A0 escalade D7** ≈ 100× coût du travail original
- **Skill-creation cost-of-error** ≈ 5 min perdues (fausse création)
- **Asymétrie** : Phase 2 (Hermes-style) privilégie la **création** sur l'**escalade**

---

## 9. Annexes

### 9.1 D1 receipts (preuves filesystem)

**A-Space skills (✅ d1, SKILL.md trouvé) :**
- `C:\Users\amado\.claude\skills\b1-filter\SKILL.md`
- `C:\Users\amado\.claude\skills\swarm-orchestrator\SKILL.md`
- `C:\Users\amado\.claude\skills\canon-batch-spawn\SKILL.md`
- `C:\Users\amado\.claude\skills\premortem-fill\SKILL.md`
- `C:\Users\amado\.claude\skills\ratify-adr\SKILL.md`
- `C:\Users\amado\.claude\skills\skill-creator\SKILL.md`
- `C:\Users\amado\.claude\skills\multi-goal\SKILL.md`
- `C:\Users\amado\.claude\skills\multi-routines-12wy\SKILL.md`
- `C:\Users\amado\.claude\skills\wargame\SKILL.md`
- `C:\Users\amado\.claude\skills\replicate-squads\SKILL.md` (+ `scripts\replicate_squads.ps1`)

**Anthropic official plugin cache (✅ d1, SKILL.md trouvé) :**
- `C:\Users\amado\.claude\plugins\cache\claude-plugins-official\frontend-design\76b35e91d1c9\skills\frontend-design\SKILL.md`

**HYPOTHÈSE (skill listée dans MEMORY.md ou system-reminder, MAIS pas de SKILL.md trouvé ce cycle) :**
- `multi-workflow` (dir exists, no SKILL.md at root)
- `dataviz` (system-reminder entry, absent du plugin cache ce cycle)
- `openspec-apply-change`, `openspec-archive-change`, `openspec-explore`, `openspec-propose` (4 dirs, no SKILL.md)

### 9.2 Inventaire global `~/.claude/skills/` (D1 — 2026-07-06)

**73 skills canonisées** (incluant `_TRASH/`, `learned/`, `ecc/` subdirs) :
a0l-grill · aaas-dashboard-port-audit · abc-os-backend-delegation · abc-os-backend-delegation-workspace · abc-os-write-back-protocol · airtable-enrich · area-domain-doctrine-distill · aspace-supabase-mastery · b1-filter · bridge-12wy-plane-gtd · canon-batch-spawn · cloud-bootstrap · configure-ecc · context-bloat-detector · context7-mcp · diagnose-proxy-boolean · ecc · find-docs · github-cli-orchestration · graphify-swarm-burst · graphify-viewer · guide-cross-search · guide-domain-stats · guide-index-builder · guide-search · guide-trim-large · hostinger-dns-orchestration · l0-deploy-verify · l0-watchdog-scrape · l1-research-pulse · l1-weekly-snapshot · l2-competitor-pulse · l2-e2e-pr · l2-linkedin-prospect · learned · market-study-derive · mcp-mastery · multi-backend · multi-goal · multi-loop-karpathy · multi-routines-12wy · multistream-deliver · notebooklm-bridge · openspec-apply-change · openspec-archive-change · openspec-explore · openspec-propose · picard-audit-and-prod-workflow · picard-growth-jtbd-launch · picard-repo-home · pp-cli-install · premortem-fill · pricing-canon-derive · ratify-adr · replicate-squads · sessions-archive · skill-creator · strategy-session-meta · supabase-cloud-mcp-orchestration · swarm-chunk-transcript · swarm-orchestrator · sym_supabase_drain · symphony-fabuleux-discipline · symphony-phase2-batch · symphony-pilot · symphony-pilot-runtime · takeout-delta-ingest · test-a1-profiles · tilly-fable-rhythm · transcript-swarm-chunks · vercel-deploy-from-github · wargame · writing-great-skills · youtube-takeout-to-lifeos · youtube-to-guide · youtube-to-para

### 9.3 Sister-canon links (cross-references)

| Sister-canon | Fichier | Lien vers Tier |
|---|---|---|
| ADR-L2-AAAS-001 | `_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` | C.3 wargame |
| ADR-ICP-NEXUS-001 | `_SPECS/ADR/L2_Business_OS/ADR-ICP-NEXUS-001_icp-nexus-structuration.md` | A.1 frontend-design (Landing Nexus) |
| ADR-NEXUS-LANDING-PERSONAS-001 | `_SPECS/ADR/L2_Business_OS/ADR-NEXUS-LANDING-PERSONAS-001_3-landings-distinctes-icp.md` | A.1 (3 personas) |
| ADR-CANON-001 | `_SPECS/ADR/L2_Business_OS/ADR-CANON-001_roster-source-of-truth.md` | D.6 replicate-squads |
| ADR-META-001 | `_SPECS/ADR/META/ADR-META-001_anti-paresse-verify-before-assert.md` | B.2 ratify-adr + all |
| ADR-META-005 | `_SPECS/ADR/L1_Life_OS/ADR-META-005_hooks-automation.md` | C.2 multi-routines-12wy |
| ADR-SOBER-002 | `_SPECS/ADR/L1_Life_OS/ADR-SOBER-002_sobriety-anti-fragility.md` (HYPOTHÈSE — pas trouvé ce cycle, sister canon implicite per CLAUDE.md) | B.3 premortem-fill |
| ADR-L2-BDLD-MAP-001 | `_SPECS/ADR/L2_Business_OS/ADR-L2-BDLD-MAP-001_business-domains-lifewheel-bijection.md` | C.2 multi-routines-12wy |
| CLAUDE.md §"Skill Creator Reflex" | `C:\Users\amado\.claude\CLAUDE.md` | B.4 canon-batch-spawn + A3-Protostar |
| CLAUDE.md §"Doctrine Swarm Orchestration" | `C:\Users\amado\.claude\CLAUDE.md` | A.4 swarm-orchestrator |
| CLAUDE.md §"Fable × Auto-Research × /loop × Symphony × Agent OS" | `C:\Users\amado\.claude\rules\fable-autor-research-loop-symphony-agentos.md` | C.4 loop |
| rules/ecc/web/design-quality.md | `C:\Users\amado\.claude\rules\ecc\web\design-quality.md` | A.1 frontend-design |

### 9.4 Notes ouvertes (TODO D1-verification)

- [ ] **A.3 dataviz** : vérifier présence dans `~/.claude/plugins/cache/` après CC restart (D6 #4)
- [ ] **D.1 multi-workflow** : confirmer SKILL.md location (root ou sub-skill)
- [ ] **D.2-D.5 openspec-*** : vérifier SKILL.md après CC restart
- [ ] **ADR-LANDING-AESTHETIC-001** (sister Tier A) : canoniser si pas encore fait
- [ ] **PRD-B1-FILTER-M3-001** (sister Tier B.1) : canoniser si pas encore fait
- [ ] **ADR-SOBER-002** path exact : vérifier `_SPECS/ADR/L1_Life_OS/` ou `_SPECS/ADR/META/`

---

> **Auteur** : B1 E-Myth Gatekeeper (Jerry Prime ↔ Summers Nexus OMK BOS) · 2026-07-06
> **Statut** : DRAFT — soumis à A0 ratification
> **Prochaine action** : A0 review §3 (tier classification) + §6 (anti-patterns) + §9.4 (TODO D1-verification)