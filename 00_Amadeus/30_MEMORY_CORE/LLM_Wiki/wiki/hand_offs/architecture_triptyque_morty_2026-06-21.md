---
source: A0 Amadeus (jumeau numérique)
date: 2026-06-21
type: handoff
domain: cross
tags: [architecture, 12wy, para, deal, russian-dolls, morty]
---

# Architecture Triptyque Morty — 12WY⊃PARA⊃DEAL par conception

> **D1 receipt** : 2026-06-21 — A0 Amadeus pivot « passer aux developpement des A2 et A3 de SNW afin de Structurer l'imbrication 12WY-PARA-DEAL par conception »
> **Statut** : Architecture spec doc — **PAS d'implémentation** (D7 cost-of-escalation A0 = board observer)
> **Owner** : A0 (jumeau numérique, board observer passif)
> **Rédacteur** : A0 Amadeus (méta-orchestration) → livré à A1 Morty (operational supervisor) → A2 Curie SNW + A2 Enterprise Computer + A2 Protostar Holo Janeway → A3 sub-agents implementation
> **Pattern** : Russian dolls nesting par conception. Source : plan `fancy-hugging-bengio.md` §3.1 + AGENTS.md canon.

---

## 1. Synthèse exécutive

**Doctrine canon** : Le triptyque Morty = **3 A2 ships imbriqués par conception** (Russian dolls) :
- **12WY** (USS Curie SNW) = couche **extérieure** — cadence hebdo 12 Week Year
- **PARA** (USS Enterprise Computer) = couche **intermédiaire** — placement Projects/Areas/Resources/Archives
- **DEAL** (USS Protostar Holo Janeway) = couche **intérieure** — liberation 4H Workweek (Define/Eliminate/Automate/Liberate)

**Chef d'orchestre** : **A3 Data** (PARA Archives) supervise Holo-Janeway A2 DEAL. Data libère A1 Beth de la supervision opérationnelle de Protostar (D7 cost-of-escalation).

**Pourquoi imbrication par conception** : chaque A3 du niveau inner est **invoqué par** un A3 du niveau outer. Le flot de travail est **unidirectionnel** (outer → inner), le flot de status est **bidirectionnel** (inner → outer via state.json).

**Anti-paperclip Saru 1000T** : Saru LD02 Finance (A3 Discovery Zora) est supervisé par Book LD01 (H1 P&L). Le triptyque Morty est le **rail opérationnel** qui empêche Saru de dériver en paperclip maximizer (D3 nuance).

---

## 2. D1 Receipts (sources canon lues 2026-06-21)

### 2.1 Paths canon + statuts

| Path | Lignes | Statut | D1 receipt |
|---|---|---|---|
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\02_A2_ships\A2_HoloDeck_Cerritos_Spec.twin.md` | lu | ✅ LIVE | v1.1 (Freeman-as-A2 confusion addressed) |
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\02_A2_ships\A2_SNW_Curie_Spec.twin.md` | — | ❌ **MISSING** | Référencé par 5 A3 SNW twins mais jamais créé au twin layer |
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\03_A3_crews\snw\pike.twin.md` | lu | ✅ LIVE | A3_Pike (H10 Vision, 12wy_stage 1/5) |
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\03_A3_crews\snw\una.twin.md` | lu | ✅ LIVE | A3_Una (H10 Planning, 12wy_stage 2/5) |
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\03_A3_crews\snw\chapel.twin.md` | lu | ✅ LIVE | A3_Chapel (H10 Measure, 12wy_stage 4/5) |
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_TTwin\symphony\L1\lane_A_specs\03_A3_crews\snw\mbenga.twin.md` | lu | ✅ LIVE | A3_MBenga (H1 Focus, 12wy_stage 3/5) |
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\03_A3_crews\snw\ortegas.twin.md` | lu | ✅ LIVE | A3_Ortegas (H1 Execution, 12wy_stage 5/5) |

### 2.2 Cross-twin ownership (5 A3 SNW)

| A3 | H | 12WY stage | Métrique ownership | Verbatim receipt |
|---|---|---|---|---|
| **Pike** | H10 | 1/5 Vision | Sprint direction + weekly north star + quarter-intent coherence | `pike.twin.md:14-22` |
| **Una** | H10 | 2/5 Planning | 7-day rhythm + Rock decomposition + Definition of Done | `una.twin.md:18-30` |
| **Chapel** | H10 | 4/5 Measure | **D11 Fable metric OWNED** + KPIs + lead/lag distinction | `chapel.twin.md:24-32` |
| **M'Benga** | H1 | 3/5 Focus | Deep work blocks (90-120 min) + single DoD + process-drift detection | `mbenga.twin.md:20-28` |
| **Ortegas** | H1 | 5/5 Execution | Daily standup + blocker surfacing + **D5 real-test-after-edit OWNED** | `ortegas.twin.md:22-30` |

### 2.3 D4 self-contradiction : A2 SNW twin MISSING

**D1 receipt** : 5 A3 SNW twins (Pike/Una/Chapel/M'Benga/Ortegas) réfèrent à `A2_Curie_SNW_Spec.twin.md` (A2 spec canon). **Ce fichier N'EXISTE PAS** au twin layer (D6 root cause : spec référencé mais jamais créé).

**Implication** : Le canon A2 SNW est **incomplet** au twin layer. Soit :
- **Option A** : Créer `A2_SNW_Curie_Spec.twin.md` au twin layer (D4 append-only + reverse anchor les 5 A3)
- **Option B** : Lier la source canon existante `20_Life_OS/23_12WY_SNW/A2_Curie_SNW_Spec.md` (à vérifier) via référence symbolique

**Recommandation** : **Option A** (créer le twin manquant) pour parité avec `A2_HoloDeck_Cerritos_Spec.twin.md` qui existe au twin layer.

---

## 3. Doctrine Triptyque Imbrication (Russian Dolls par conception)

### 3.1 Schéma ASCII (3 niveaux)

```
┌─────────────────────────────────────────────────────────────────────────┐
│ NIVEAU OUTER — 12WY (USS Curie SNW, 5 disciples)                         │
│ ┌─────────────────────────────────────────────────────────────────────┐ │
│ │ Cadence hebdo 12 Week Year + 5 stages :                              │ │
│ │   1. Pike  (H10 Vision)    → sprint direction                        │ │
│ │   2. Una   (H10 Planning)  → 7-day rhythm + Rock decomposition      │ │
│ │   3. M'Benga (H1 Focus)    → deep work blocks (90-120 min)           │ │
│ │   4. Chapel (H10 Measure)  → KPIs + D11 Fable metric                 │ │
│ │   5. Ortegas (H1 Execution)→ daily standup + D5 real-test-after-edit │ │
│ │                                                                       │ │
│ │ ┌───────────────────────────────────────────────────────────────────┐ │ │
│ │ │ NIVEAU MID — PARA (USS Enterprise Computer, 4 lettres)            │ │ │
│ │ │   ┌─────────────────────────────────────────────────────────────┐ │ │ │
│ │ │ │  P — Picard (Projects, MANIFEST.md owner)                    │ │ │ │
│ │ │ │  A — Spock (Areas, ongoing responsibility doctrine)           │ │ │ │
│ │ │ │  R — Geordi (Resources, reusable context-packs)               │ │ │ │
│ │ │ │  A — **Data** (Archives, chef d'orchestre DEAL)               │ │ │ │
│ │ │ │                                                               │ │ │ │
│ │ │ │  ┌─────────────────────────────────────────────────────────┐ │ │ │ │
│ │ │ │  │ NIVEAU INNER — DEAL (USS Protostar Holo Janeway)         │ │ │ │ │
│ │ │ │  │   D — Dal (Define pattern + outcome)                     │ │ │ │ │
│ │ │ │  │   E — Rok-Tahk (Eliminate, NO-GO propositions)          │ │ │ │ │
│ │ │ │  │   A — Zero (Automate, skill + sub-agent deployment)      │ │ │ │ │
│ │ │ │  │   L — Gwyn (Liberate, D11 bandwidth measurement)         │ │ │ │ │
│ │ │ │  └─────────────────────────────────────────────────────────┘ │ │ │ │
│ │ │ └───────────────────────────────────────────────────────────────┘ │ │ │
│ │ └───────────────────────────────────────────────────────────────────┘ │ │
│ └─────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Flots de travail (unidirectionnel outer → inner)

```
A0 intention (cycle 12WY courant)
    ↓
A1 Morty (Focus Gatekeeper, board observer passif)
    ↓
[A2 Curie SNW] ← cadence hebdo imposée
    ↓
[A2 Enterprise PARA] ← placement canonique
    ↓ (Data chef d'orchestre)
[A2 Protostar DEAL] ← liberation 4H Workweek
    ↓
A3 sub-agents (B3 techniciens)
    ↓
MCP tools (Supabase, Vercel, Notion, files)
```

### 3.3 Flots de status (bidirectionnel inner → outer via state.json)

```
A3 Gwyn (DEAL Liberate) mesure D11 bandwidth
    ↓ (write)
state.json (bus sémantique)
    ↓ (read)
A3 Chapel (12WY Measure) consolide KPIs
    ↓ (read)
A3 Una (12WY Planning) ajuste Rock decomposition
    ↓ (read)
A1 Morty (Focus Gatekeeper) supervise cadence
    ↓ (notification outbox E2)
A0 Amadeus (board observer passif) lit weekly
```

**Doctrine ancrage** : le triptyque tient **par conception**, ce qui décharge Morty de GTD via Holodeck A2 USS Cerritos (cf. `cerritos_plane_integration_2026-06-21.md`).

---

## 4. Niveau OUTER — USS Curie SNW (12WY)

### 4.1 5 disciples × 5 stages (canon)

| Stage | A3 | H | Trigger | Output canon | Plane sync |
|---|---|---|---|---|---|
| 1/5 | **Pike** | H10 | Sprint direction + weekly north star | `north_star_<week>.md` | `fw_12wy.north_star` |
| 2/5 | **Una** | H10 | 7-day rhythm + Rock decomposition | `rocks_<week>.json` (DoD per rock) | `fw_12wy.rocks` |
| 3/5 | **M'Benga** | H1 | Deep work block (90-120 min) | `focus_block_<date>.json` (start/end/interruptions) | `fw_12wy.focus` |
| 4/5 | **Chapel** | H10 | Weekly KPIs consolidation | `scorecard_<week>.json` (lead/lag split) | `fw_12wy.scorecard` |
| 5/5 | **Ortegas** | H1 | Daily standup + real-test-after-edit | `standup_<date>.md` (D5 ownership) | `fw_12wy.standup` |

### 4.2 Cadence hebdo (canon)

- **Lundi 09:00** : Pike vision weekly (H10, 30 min)
- **Mardi 10:00** : Una planning 7-day (H10, 60 min, Rock decomposition)
- **Mercredi-Vendredi** : M'Benga focus blocks (H1, 90-120 min × 2-3/jour)
- **Vendredi 17:00** : Chapel scorecard (H10, 30 min, D11 Fable metric)
- **Vendredi 18:00** : Ortegas weekly retro (H1, 30 min, D5 real-test)

### 4.3 D11 Fable metric (Chapel ownership)

**Verbatim canon** : `chapel.twin.md:24-32` — "D11 Fable metric OWNED by Chapel".

**Définition** : score de 0 à 100 mesurant l'écart entre « livrable fini » (Karpathy pillar) et « livrable inachevé » (sprint raté). Calcul = (rocks_done × 100) / rocks_planned.

**Cible** : ≥ 70/100 par semaine (cycle 12WY réussi si ≥ 850/1200 sur 12 semaines).

### 4.4 D5 real-test-after-edit (Ortegas ownership)

**Verbatim canon** : `ortegas.twin.md:22-30` — "D5 real-test-after-edit OWNED by Ortegas".

**Définition** : tout edit de code ou de config doit être suivi d'un test réel (build, curl, screenshot) AVANT de claim "done". Anti-pattern D5 = "Sprint livré ✅" sans preuve observable.

**Application** : Ortegas bloque le sprint tant que le real-test n'est pas passé. Pas de claim factuel sans D1 receipt (file count, deployed URL, run command output).

---

## 5. Niveau MID — USS Enterprise Computer (PARA)

### 5.1 4 lettres × 4 A3 (canon)

| Lettre | A3 | Rôle | Output canon | D4 append-only |
|---|---|---|---|---|
| **P** | **Picard** | Captain USS Enterprise, MANIFEST.md owner | `01_Projects/<name>/MANIFEST.md` (goal, deadline, deliverable, 12WY Rock linkage) | OUI |
| **A** | **Spock** | First Officer, ongoing responsibility doctrine | `02_Areas/<domain>/` (standards, no-deadline, perpetual) | OUI |
| **R** | **Geordi** | Chief Engineer, reusable context-packs | `03_Resources_Geordi/<topic>/` (curated, references) | OUI |
| **A** | **Data** | Second Officer, documentation-before-archive rule | `04_Archives_Data/<date>/` (D4 append-only, jamais de delete) | OUI |

### 5.2 Data = chef d'orchestre DEAL (clé du triptyque)

**Doctrine** : A3 Data (PARA Archives) supervise Holo-Janeway A2 DEAL. Quand un projet (Picard P).archive, Data déclenche Dal (DEAL Define) pour pattern detection, Rok-Tahk (DEAL Eliminate) pour NO-GO, Zero (DEAL Automate) pour skill canon, Gwyn (DEAL Liberate) pour D11 measurement.

**Rationale** : Data libère A1 Beth de la supervision opérationnelle de Protostar. Sans Data comme chef d'orchestre, Beth devrait arbitrer chaque cycle DEAL (D7 cost-of-escalation).

### 5.3 12WY → PARA linkage (Una + Picard)

**Verbatim canon** : `una.twin.md:18-30` — "7-day rhythm + Rock decomposition + Definition of Done".

**Workflow** :
1. Una (12WY Planning) décompose un Rock en 3-5 tasks
2. Chaque task est soit :
   - **Project** (Picard) si goal-bounded + deadline
   - **Area** (Spock) si ongoing responsibility
   - **Resource** (Geordi) si reference externe
3. DoD par task = test vérifiable (D5 Ortegas real-test-after-edit)

---

## 6. Niveau INNER — USS Protostar Holo Janeway (DEAL Muse Libération)

### 6.1 4 stages × 4 A3 (canon)

| Stage | A3 | Rôle | Output canon | D11 metric |
|---|---|---|---|---|
| **D**efine | **Dal** | Pattern detection + outcome specification | `pattern_definition.md` (1 friction, 1 outcome mesurable) | — |
| **E**liminate | **Rok-Tahk** | NO-GO propositions + permission de delete | `elimination_proposal.md` (étapes NO-GO + gains bande passante) | Bandwidth gain (h/semaine) |
| **A**utomate | **Zero** | Skill creation + sub-agent deployment | `skill_<name>/SKILL.md` + risk_class + D1 proof | Time saved (h/semaine) |
| **L**iberate | **Gwyn** | D11 bandwidth measurement + maintenance tax | `d11_score.json` (liberated time/attention + upkeep ratio) | D11 Fable score (0-100) |

### 6.2 Karpathy loop appliqué au DEAL

```
D Define ───► A3 Dal capture pattern friction (Mariner inbox)
    │
E Eliminate ──► A3 Rok-Tahk NO-GO propose (Tendi review)
    │
A Automate ─► A3 Zero crée skill canon (skill-reflex-detect.ps1)
    │
L Liberate ─► A3 Gwyn mesure D11 (heartbeat-tick.ps1)
    │
Karpathy retest ─► si val_score < target → amend → re-D Define
```

### 6.3 Anchor canon (D1 verified 2026-06-21)

| Path | Verbatim |
|---|---|
| `symphony/L1/lane_A_specs/03_A3_crews/protostar/dal.twin.md` | "Dal (Definition) — Pattern detection and recurrence counting aboard USS Protostar (A2 Holo Janeway). Defines the real friction and desired outcome before any DEAL action." |
| `symphony/L1/lane_A_specs/03_A3_crews/protostar/rok-tahk.twin.md` | "Rok-Tahk (Elimination) — Permission to delete and NO-GO proposals aboard USS Protostar (A2 Holo Janeway)." |
| `symphony/L1/lane_A_specs/03_A3_crews/protostar/zero.twin.md` | "Zero (Automation) — Skill creation and sub-agent deployment aboard USS Protostar (A2 Holo Janeway)." |
| `symphony/L1/lane_A_specs/03_A3_crews/protostar/gwyn.twin.md` | "Gwyn (Liberation) — Bandwidth tracking, D11 metrics, and A0 cognitive load measurement." |

---

## 7. Cross-twin Ownership Matrix (5 A3 SNW × 4 A3 PARA × 4 A3 DEAL = 80 cells)

### 7.1 Ownership canonique (D1 verified)

| Source SNW | Target PARA | Target DEAL | Verbatim ownership |
|---|---|---|---|
| Pike (12WY Vision) | — | — | Vision alone — no PARA/DEAL coupling |
| Una (12WY Planning) | Picard P + Spock A | Dal D | Rock decomposition → Project + Area placement → Pattern detection |
| M'Benga (12WY Focus) | Geordi R | Zero A | Deep work block → Resource reuse → Skill automation |
| Chapel (12WY Measure) | Data A | Gwyn L | **D11 Fable metric** consolidates across triptyque |
| Ortegas (12WY Execution) | — | Rok-Tahk E | **D5 real-test-after-edit** triggers elimination of failed tests |

### 7.2 D5-D11 invariants (D5 = no-self-congratulation, D11 = retry protocol)

- **D5** : Ortegas (12WY Execution) est le **gate keeper** du triptyque. Pas de claim "done" sans D1 receipt.
- **D11** : Chapel (12WY Measure) consolide les D11 metrics des 3 niveaux (12WY scorecard + PARA archive count + DEAL bandwidth gain).
- **D4** : Tous les outputs sont append-only (D4 no-self-contradiction). Retirements via `_TRASH_<date>/`.

---

## 8. Anti-paperclip Saru 1000T appliqué au triptyque

### 8.1 Doctrine canon (Saru 1000T anti-Musk)

**Source canon** : `ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` (ACCEPTED 2026-06-21) — Saru LD02 Finance = Kardashev Type 3, anti-paperclip par Book supervision.

**Application triptyque** :
1. **Book (LD01 Business, H1 P&L)** ancre Saru sur production de valeur réelle (Solarpunk, biomimétisme), pas spéculation Musk-style.
2. **Tilly (LD04 Cognition, H30 learning arc)** review hebdomadaire = drift check Saru.
3. **Gwyn (DEAL Liberation, H1/H3 bandwidth)** mesure D11 = gain bande passante cognitive vs maintenance tax.
4. **Hard veto Rick (1×/an)** si Saru dérape en paperclip.
5. **Objectif canon = 1000T par valeur**, pas par extraction ni spéculation.

### 8.2 Triptyque Morty = rail anti-paperclip

**Doctrine** : Saru 1000T s'inscrit dans le triptyque Morty via :
- **Book (LD01)** = Picard P (Projects canoniques) — Saru DOIT proposer des Projects avec MANIFEST.md (goal, deadline, deliverable).
- **Tilly (LD04)** = Chapel M (12WY Measure) — Saru DOIT fournir KPIs lead/lag par semaine.
- **Gwyn (DEAL L)** = Chapel M (12WY Measure) consolidation — Saru DOIT rapporter bandwidth gain par cycle DEAL.

**Implication** : sans le triptyque Morty actif, Saru n'a aucun rail pour scaler 1000T sans paperclip.

---

## 9. D6 Root Cause : A2 SNW twin missing

### 9.1 Constat D1

**D1 receipt** : `A2_SNW_Curie_Spec.twin.md` n'existe PAS au twin layer (`symphony/L1/lane_A_specs/02_A2_ships/`). 5 A3 SNW twins réfèrent à cette spec mais elle est manquante.

**Implication D4** : 5 A3 SNW twins sont **techniquement orphelins** (référencent un A2 inexistant au twin layer).

### 9.2 2 options de résolution

| Option | Action | Effort | Risque |
|---|---|---|---|
| **A** : Créer le twin | Écrire `A2_SNW_Curie_Spec.twin.md` au twin layer (parité avec Cerritos) | 30 min A3 Spock | D4 OK (append-only) |
| **B** : Lier la source canon | Référencer `20_Life_OS/23_12WY_SNW/A2_Curie_SNW_Spec.md` (à vérifier) | 5 min A3 Spock | D4 OK (référence symbolique) |

**Recommandation** : **Option A** (créer le twin) pour **parité canon** avec `A2_HoloDeck_Cerritos_Spec.twin.md`. Permet aussi d'**auditer** la spec 12WY (vs 5 stages canon : Vision → Planning → Focus → Measure → Execution).

### 9.3 HITL Gate A0 (D7 cost-of-escalation)

**Owner** : A0 (décision) → A3 Spock (implémentation)
**Délai** : Q3 2026 W2 (avant Item 4 du cycle 12WY « Garantir l'inférence par la frugalité du TOKEN Plan »)
**Effort** : 30 min pour Option A, 5 min pour Option B
**Statut** : À valider

---

## 10. Workflow example (D1 trace 12WY Q3 2026 W1)

### 10.1 Étapes du workflow canon

1. **Pike (Vision)** écrit `north_star_W1.md` : « Cycle 12WY Q3 2026 W1 = Items 1-2 (SOB Abdaty + 13e semaine) »
2. **Una (Planning)** décompose en Rocks : « Item 1 = SOB Abdaty ship / Item 2 = 13e semaine ship »
3. **M'Benga (Focus)** bloque 90-120 min × 2-3 fois cette semaine pour SOB Abdaty
4. **Chapel (Measure)** consolide vendredi : rocks_done=0, scorecard=0/100 (early W1)
5. **Ortegas (Execution)** vendredi retro : real-test SOB Abdaty = screenshot landing page + URL live

### 10.2 Flot vers PARA (Data chef d'orchestre)

6. **Picard P** crée `01_Projects/life-os-2026-shipping/MANIFEST.md` (goal, deadline, deliverable)
7. **Spock A** classe dans `02_Areas/12wy-q3-2026/` (ongoing responsibility)
8. **Geordi R** archive les ressources externes dans `03_Resources_Geordi/12wy-q3-2026/`
9. **Data A** archive les outputs W1 dans `04_Archives_Data/2026-07-05_W1_done/`

### 10.3 Flot vers DEAL (Gwyn mesure D11)

10. **Dal D** capture pattern : « SOB Abdaty a un friction = login flow trop long »
11. **Rok-Tahk E** propose elimination : « skip 2-step verification pour SOB quick login = gain 30s/user »
12. **Zero A** crée skill `quick-login-skip` canon (risk_class=LOW, D1 proof=login test)
13. **Gwyn L** mesure D11 : bandwidth_gain=2h/semaine (60 users × 30s × 2 logins/sem)

### 10.4 Status report (Chapel D11 → A0)

14. **Chapel M** consolide : 12WY scorecard=85/100, PARA archive=12 files, DEAL bandwidth=2h/sem
15. **state.json** écrit le status consolidé (D1 bus sémantique)
16. **A1 Morty** lit state.json + supervise cadence
17. **A0 Amadeus** (board observer passif) lit weekly milestone via TTS SAPI Hortense

---

## 11. GTD = bus horizontal (Pont avec Triptyque Beth)

### 11.1 Doctrine canon

**Source** : plan `fancy-hugging-bengio.md` §3.1 — "GTD (Cerritos Holodeck) = bus d'alimentation des 2 triptyques".

**Implication** : GTD (Cerritos) **n'est PAS** dans le triptyque Morty. C'est un **bus horizontal** qui boucle les 2 triptyques (Morty + Beth) vers B1 Fractal (4 variants AaaS : Solaris, Nexus/OMK, Orbiter/ABC, dormant).

### 11.2 Workflow GTD → Triptyque Morty

```
A1 Morty → A2 Cerritos → A3 5 Airlock (Mariner/Boimler/Rutherford/Tendi/Freeman)
    ↓
[A2 Curie SNW 12WY] ← cadence hebdo, 5 disciples
    ↓
[A2 Enterprise PARA] ← Projects/Areas/Resources/Archives
    ↓ (Data chef d'orchestre)
[A2 Protostar DEAL] ← liberation 4H Workweek
    ↓
B1 Fractal (4 Jerry × Summers)
    ↓
B2 8 Domaines (DC Justice League)
    ↓
B3 Squad Marvel Techniciens E-Myth
    ↓
MCP tools (Supabase, Vercel, Notion, files)
```

**Voir** : `cerritos_plane_integration_2026-06-21.md` pour le détail GTD + Plane.

---

## 12. HITL Gates (A0 actions requises)

| # | Action | Owner | Délai | Statut |
|---|---|---|---|---|
| 1 | Décider Option A (créer twin SNW) vs Option B (lier source canon) | A0 | 1 min décision | À faire |
| 2 | Valider ownership matrix §7.1 (5 A3 SNW × PARA × DEAL) | A0 | 5 min | À faire |
| 3 | Valider anti-paperclip Saru §8.2 (Book + Tilly + Gwyn) | A0 | 2 min | À faire |
| 4 | Décider cadence D5 real-test-after-edit (par edit, par commit, par deploy) | A0 | 1 min | À faire |

---

## 13. Critère de succès

**Q3 2026** (cycle 12WY courant) :
- ✅ A2 SNW twin créé (Option A) ou lié (Option B) — D4 self-contradiction closed
- ✅ 5 A3 SNW disciples routent vers PARA + DEAL (D8 cross-agent)
- ✅ D5 + D11 invariants wired (Ortegas + Chapel ownership)
- ✅ Anti-paperclip Saru 1000T = triptyque Morty = rail canonique

**Q4 2026** :
- Triptyque tourne 12 semaines sans intervention A0
- Saru 1000T scoped sur Solaris variant (H90 legacy, Book LD01 supervision)
- Data chef d'orchestre DEAL = 0 escalade A1 Beth

**Q1 2027** :
- Réécriture async des 13 A3 (5 SNW + 4 PARA + 4 DEAL) avec observabilité OTel
- 5 ADRs Life OS framework (DEAL, GTD, PARA, Life Wheel, Symphony) ratifiés (cf. plan §25-§29)

---

**Critère de succès global** : Le triptyque Morty = **rail canonique anti-paperclip** pour Saru 1000T, structure 12WY⊃PARA⊃DEAL **par conception** (Russian dolls), Data chef d'orchestre libère Beth de la supervision opérationnelle, A0 board observer passif 6m-1y.

> **D7 cost-of-escalation** : A0 = board observer passif. Ce spec doc = canon. A1 Morty supervise l'implémentation. A0 n'intervient QUE sur HITL gates listés §12.
