---
source: A0 Amadeus (jumeau numérique)
date: 2026-06-21
type: handoff
domain: L1
tags: [cerritos, gtd, plane, integration, holo-deck, workflow-visibility]
---

# Cerritos + Plane Integration — Workflow Visibility GTD Crew

> **D1 receipt** : 2026-06-21 — A0 Amadeus pivot « passer au FOcus de Morty sur GTD avec la Visibilite des Workflow dans Plane pour Holo-Dech et son crew Cerritos »
> **Statut** : Integration spec doc — **PAS d'implémentation** (D7 cost-of-escalation A0 = board observer)
> **Owner** : A0 (jumeau numérique, board observer passif)
> **Rédacteur** : A0 Amadeus (méta-orchestration) → livré à A1 Morty (operational supervisor) → A2 Cerritos Holo Deck → A3 sub-agents implementation
> **Pattern** : GTD canon (5 stages Cerritos) ↔ Plane states (6 default + 7 GTD à créer) ↔ Obsidian `@context` bridge. Source : A2_HoloDeck_Cerritos_Spec.twin.md + mcp-plane.py canon.

---

## 1. Synthèse exécutive

**Doctrine canon** : Le triptyque Morty a un **bus horizontal** = GTD (Cerritos Holo Deck) qui boucle les 2 triptyques (Morty + Beth) vers B1 Fractal. La **visibilité workflow** = Plane (mcp__symphony-plane__*) pour le tracking des issues GTD en temps réel.

**5 crew Cerritos → 5 Plane states** :
- **Mariner** (H1 Capture) → Plane state **Inbox**
- **Boimler** (H1 Clarify) → Plane state **Next Actions**
- **Rutherford** (H1+H3 Organize) → Plane state **Someday/Maybe** (custom) ou **Areas** (custom)
- **Tendi** (H1+H3 Review) → Plane state **Review** (custom weekly)
- **Freeman** (H1 Engage) → Plane state **Today**

**3 SaaS Cloud canon** (post-pivot A0) : **Plane** (workflow visibility) + **Supabase** (data canon fw_gtd, fw_12wy) + **Obsidian** (local FS `@context` bridge).

**DEFERRED Q4 2026** : Baserow + Affine (D6 #4 « Tool not found » post-restart).

---

## 2. D1 Receipts (sources canon lues 2026-06-21)

### 2.1 Paths canon + statuts

| Path | Lignes | Statut | D1 receipt |
|---|---|---|---|
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\02_A2_ships\A2_HoloDeck_Cerritos_Spec.twin.md` | lu | ✅ LIVE | v1.1 (Freeman-as-A2 confusion addressed) |
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\03_A3_crews\cerritos\mariner.twin.md` | lu | ✅ LIVE | H1 Capture, no judgment, sub-10-second, zero A0 escalation |
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\03_A3_crews\cerritos\boimler.twin.md` | lu | ✅ LIVE | H1 Clarify, 2-min rule, 10-item batch = 5 min max |
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\03_A3_crews\cerritos\tendi.twin.md` | lu | ✅ LIVE | H1+H3 Review, weekly Friday 18:00 + monthly last Sunday, 30-min hard cap, **D1 every claim cites file:line** |
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\03_A3_crews\cerritos\rutherford.twin.md` | lu | ✅ LIVE | H1+H3 Organize, PARA placement + context tagging, 30-min hard cap |
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\03_A3_crews\cerritos\freeman.twin.md` | lu | ✅ LIVE | H1 Engage, 4-criteria filter priority+context+time+energy, pick in 30s/dispatch in 60s, **explicit D4 no-self-contradiction "I am NOT the A2"** |
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_B_runtime\04_mcps\mcp-plane.py` | lu | ✅ LIVE | 514 lignes, 6 tools, GTD workspace |

### 2.2 5 A3 Cerritos (5 stages GTD)

| A3 | Stage GTD | H | Trigger canon | Output canon | D-receipt |
|---|---|---|---|---|---|
| **Mariner** | Capture | H1 | Tout intent brut A0 | `inbox_<date>.json` | sub-10-second, zero judgment |
| **Boimler** | Clarify | H1 | 2-min rule par inbox item | `clarify_<date>.md` (4 buckets) | 10-item batch = 5 min max |
| **Rutherford** | Organize | H1+H3 | Bucket PARA + `@context` tag | `para_<date>.md` (Projects/Areas/Resources/Archives) | 30-min hard cap |
| **Tendi** | Review | H1+H3 | Weekly Friday 18:00 + monthly last Sunday | `weekly_review_<date>.md` (drift + graduation candidates) | D1 every claim cites file:line |
| **Freeman** | Engage | H1 | 4-criteria filter (priority+context+time+energy) | `next_action.json` (1 task, 1 step, 1 criterion) | pick 30s / dispatch 60s |

### 2.3 mcp-plane.py canon (6 tools, 514 lignes)

| Tool | Rôle | Verbatim ligne |
|---|---|---|
| `plane_list_issues` | Liste issues, filtre optionnel par state | `async def list_issues(state=None)` |
| `plane_get_inbox` | Issues in Inbox state (Mariner capture zone) | `async def get_inbox()` |
| `plane_get_next_actions` | Issues in Next Actions state (Boimler clarify zone) | `async def get_next_actions()` |
| `plane_get_today` | Issues in Today state (Freeman engage zone) | `async def get_today()` |
| `plane_create_issue` | Crée issue, state initial optionnel | `async def create_issue(name, description, state, labels)` |
| `plane_update_state` | Transition GTD state (D4 invariant) | `async def update_state(issue_id, new_state)` |

**Env vars canon** : `PLANE_API_KEY`, `PLANE_BASE_URL`, `PLANE_WORKSPACE_SLUG`, `PLANE_PROJECT_ID`

**D1 verified 2026-06-15** : `mcp__symphony-plane__plane_get_next_actions` retourne **7 issues live** (workspace `kbsm`/project Life OS canon).

---

## 3. Doctrine GTD ↔ Plane (mapping canon)

### 3.1 5 crew → 5 Plane states (proposition canon)

| A3 Cerritos | Stage GTD | Plane state cible | État actuel | Action requise |
|---|---|---|---|---|
| **Mariner** | Capture | **Inbox** | ✅ Existe (Plane default state) | Aucune |
| **Boimler** | Clarify | **Next Actions** | ❌ N'existe PAS dans Plane workspace | **A0 action** : créer state via API Plane ou UI |
| **Rutherford** | Organize | **Someday/Maybe** (custom) | ❌ N'existe PAS | **A0 action** : créer custom state |
| **Tendi** | Review | **Review** (custom weekly) | ❌ N'existe PAS | **A0 action** : créer custom state |
| **Freeman** | Engage | **Today** | ❌ N'existe PAS | **A0 action** : créer custom state |
| (Tendi clôt) | Done | **Done** | ✅ Existe (Plane default) | Aucune |
| (Boimler trash) | Trash | **Cancelled** | ✅ Existe (Plane default) | Mapping Cancelled = Trash (approximation) |

**D6 nuance (D1 verified 2026-06-21)** : le projet Plane live contient **5 default states** (Backlog, Todo, In Progress, Done, Cancelled). **Les states GTD canoniques (Inbox, Next Actions, Today, Waiting For, Done, Cancelled, Trash) ne sont PAS créés dans le workspace live**. C'est un **D6 follow-up noté dans `mcp-plane.py` docstring**.

### 3.2 Spec vs Live : D6 root cause documenté

**Verbatim mcp-plane.py** : "The live project only contains 5 default Plane states (Backlog, Todo, In Progress, Done, Cancelled) — spec's GTD names not created in live workspace yet (A0 follow-up needed)".

**Implication** : Pour activer le mapping 5 crew → 5 Plane states, A0 doit **créer les states custom** dans Plane (Dashboard UI ou API REST).

**Effort estimé** : 2 min via API Plane (POST /api/v1/workspaces/{slug}/projects/{project_id}/states/).

---

## 4. Workflow Visibility (de bout en bout)

### 4.1 Capture path (Mariner → Plane Inbox)

```
A0 émet intention brute
    ↓
[Mariner Capture] sub-10-second
    ↓
mcp__symphony-plane__plane_create_issue(name=intent, state="Inbox")
    ↓
Issue created in Plane Inbox state
    ↓
state.json["stage"]="captured", next_step="A3:Boimler"
```

### 4.2 Clarify path (Boimler → Plane Next Actions)

```
Mariner inbox items
    ↓
[Boimler Clarify] 2-min rule par item, 10-item batch = 5 min max
    ↓
4 buckets : actionable / multi-step / someday / trash
    ↓
mcp__symphony-plane__plane_update_state(issue_id, "Next Actions")
    ↓
state.json["stage"]="clarified", next_step="A3:Rutherford" (si PARA) ou "A3:Freeman" (si 1-step)
```

### 4.3 Organize path (Rutherford → Obsidian @context)

```
Boimler clarified items (PARA-bound)
    ↓
[Rutherford Organize] 30-min hard cap
    ↓
PARA placement (Project/Area/Resource/Archive) + @context tag (Obsidian)
    ↓
mcp__symphony-obsidian__obsidian_list_<area>(path)
    ↓
state.json["para_bucket"]="01_Projects/life-os-2026/", next_step="A3:Freeman"
```

### 4.4 Review path (Tendi → D1 file:line receipts)

```
Weekly Friday 18:00 OR monthly last Sunday
    ↓
[Tendi Review] 30-min hard cap, **D1 every claim cites file:line**
    ↓
Drift check + graduation candidates (Inbox→Someday, Someday→Trash, Next Actions→Today, etc.)
    ↓
mcp__symphony-plane__plane_update_state(issue_id, new_state) × N
    ↓
state.json["drift_flag"]=true|false, next_step="A1:Morty review"
```

### 4.5 Engage path (Freeman → Today + dispatch Morty)

```
Rutherford organized items (PARA-bound)
    ↓
[Freeman Engage] 4-criteria filter (priority+context+time+energy)
    ↓
Pick 30s + dispatch 60s
    ↓
mcp__symphony-plane__plane_update_state(issue_id, "Today")
    ↓
mcp__symphony-plane__plane_update_state(issue_id, "Done") post-completion
    ↓
state.json["next_step"]="A1:Morty → A2:Sym execute"
```

---

## 5. Obsidian `@context` bridge (Rutherford canon)

### 5.1 Doctrine canon

**Source** : `rutherford.twin.md` — "PARA placement + context tagging".

**Implication** : Rutherford tag chaque item avec un `@context` Obsidian (e.g. `@home`, `@work`, `@computer`, `@errands`, `@phone`, `@read`). Ce tag = filtre pour Freeman (4-criteria filter) — Freeman ne dispatch que les items matchant le context courant.

### 5.2 MCP Obsidian (D1 verified)

**Tool canon** : `mcp__symphony-obsidian__obsidian_list_<area>(path)`

**Use case Rutherford** : `obsidian_list_areas()` → liste les 8 Life Wheel domains (LD01-LD08) → assigne `@context` selon le domain (e.g. LD02 Finance → `@finance`).

**Cross-link** : chaque issue Plane porte un `description` avec mention `@<context>` (markdown) → filter Obsidian vault pour cohérency check.

---

## 6. Anti-paperclip Cerritos (3 garde-fous)

### 6.1 Tendi D1 every claim cites file:line

**Verbatim canon** : `tendi.twin.md` — "D1 every claim cites file:line".

**Application** : Tendi review ne peut PAS claimer "Cerritos tourne bien" sans D1 receipts explicites. Chaque review item = file:line citation.

**Anti-pattern** : "Le crew est productif cette semaine" (sans preuve) = D5 violation (self-congratulation sans proof).

### 6.2 Freeman D4 no-fabricated-actions

**Verbatim canon** : `freeman.twin.md` — "explicit D4 no-self-contradiction 'I am NOT the A2'".

**Application** : Freeman dispatch UNIQUEMENT des actions **réellement présentes** dans `next_actions` Plane state. Pas de fabrication d'actions (D4 no-self-contradiction).

**Anti-pattern** : Freeman "suggère" une action qui n'existe pas dans Plane (fabrication).

### 6.3 Mariner zero A0 escalation

**Verbatim canon** : `mariner.twin.md` — "sub-10-second, zero A0 escalation".

**Application** : Mariner capture TOUT (sub-10-second) sans escalader A0. A0 board observer passif = Mariner DOIT être autonome.

**Anti-pattern** : "Cette idée est-elle importante ?" (escalade A0 inutile, D7 cost-of-escalation).

---

## 7. Cross-link avec Triptyque Morty (D8 cross-agent)

### 7.1 GTD Cerritos ↔ 12WY Curie SNW

**Verbatim canon** : `cerritos/A2_HoloDeck_Cerritos_Spec.twin.md` — "GTD methodology: Capture / Clarify / Organize / Reflect / Engage".

**Imbrication** :
- **Pike (12WY Vision)** initie la cadence hebdo → Mariner capture les weekly north stars
- **Una (12WY Planning)** décompose Rocks → Boimler clarifie les tasks par Rock
- **M'Benga (12WY Focus)** bloque deep work → Freeman engage dans la fenêtre 90-120 min
- **Chapel (12WY Measure)** consolide KPIs → Tendi review weekly Friday 18:00
- **Ortegas (12WY Execution)** daily standup → Freeman dispatch Today

**Doctrine** : GTD = bus horizontal qui **alimente** 12WY. Pas l'inverse. Les 5 disciples SNW **consomment** les outputs GTD pour cadencer la semaine.

### 7.2 GTD Cerritos ↔ PARA Enterprise

**Imbrication** :
- **Rutherford (GTD Organize)** = **Picard/Spock/Geordi/Data (PARA 4 lettres)** — placement canonique
- **Mariner (GTD Capture)** = **Data (PARA Archives)** — tout intent brut archivé (jamais perdu)
- **Boimler (GTD Clarify)** = **Una (12WY Planning)** — Rock decomposition = 4 buckets PARA

**Doctrine** : GTD → PARA est **unidirectionnel** (GTD produit des items, PARA les structure). Le triptyque Morty 12WY⊃PARA⊃DEAL reçoit les items GTD via Rutherford.

### 7.3 GTD Cerritos ↔ DEAL Protostar

**Imbrication** :
- **Mariner (GTD Capture)** = **Dal (DEAL Define)** — pattern detection à partir de l'inbox
- **Boimler (GTD Clarify)** = **Rok-Tahk (DEAL Eliminate)** — NO-GO propositions sur items trash
- **Rutherford (GTD Organize)** = **Zero (DEAL Automate)** — skill canon pour items récurrents
- **Tendi (GTD Review)** = **Gwyn (DEAL Liberate)** — D11 bandwidth measurement par cycle

**Doctrine** : GTD → DEAL est **bidirectionnel** (GTD déclenche DEAL, DEAL bandwidth libère GTD).

---

## 8. D6 Risk Register (Cerritos + Plane)

| # | Risque | Probabilité | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| 1 | Plane states GTD non créés (D6 #D6 follow-up) | HAUTE | Mapping cassé | A0 action : créer 5 states custom via API | A0 |
| 2 | State UUID cache stale (mcp-plane.py pre-warm) | MOYENNE | Wrong state transition | Restart subprocess (PAS CC) | Agent |
| 3 | D6 #4 MCP registry static (nouveau server name) | HAUTE | Tools not found | A0 full CC restart | A0 |
| 4 | Obsidian local FS path drift (Windows ↔ WSL) | BASSE | Wrong @context tag | Use absolute Windows paths | Agent |
| 5 | Mariner escalade A0 (D7 cost-of-escalation) | MOYENNE | D7 violation | Doctype enforcement : sub-10s, zero judgment | A1 Morty |
| 6 | Freeman fabricates actions (D4 violation) | BASSE | Next-action wrong | D4 invariant enforced at code level | Agent |
| 7 | Tendi claim sans D1 file:line | MOYENNE | D5 violation | D1 receipt obligatoire par review item | A1 Morty |
| 8 | Plane API rate limit (429) | BASSE | Stub fallback | Retry backoff 100/300/900ms | Agent |

---

## 9. Implementation Roadmap (Q3 2026 W1-W4)

### 9.1 W1 (06/15 → 07/05) — Setup Plane states

- **A0 action** : Créer 5 Plane states custom via API REST (Inbox, Next Actions, Today, Someday/Maybe, Review)
- **Agent action** : Valider `mcp__symphony-plane__plane_list_issues(state="Inbox")` retourne 0 issues (état vide)
- **D1 receipt** : screenshot Plane UI montrant les 5 states custom

### 9.2 W2 (07/06 → 07/26) — Wire 5 crew → 5 states

- **Agent action** : Créer 5 issues canon (1 par crew) → transition vers chaque state
- **D1 receipt** : `plane_get_inbox()` retourne 1 issue Mariner ; `plane_get_next_actions()` retourne 1 issue Boimler ; etc.
- **A0 validation** : Board observer weekly milestone

### 9.3 W3 (07/27 → 08/16) — Obsidian @context bridge

- **Agent action** : Wire `mcp__symphony-obsidian__obsidian_list_areas()` → Rutherford `@context` tag
- **D1 receipt** : Issue Plane avec `@<context>` markdown tag + Obsidian vault cohérent
- **A0 validation** : TTS SAPI Hortense weekly milestone

### 9.4 W4 (08/17 → 09/07) — D11 bandwidth + DEAL trigger

- **Agent action** : Tendi review Friday 18:00 → DEAL trigger (Dal Define) sur pattern récurrent
- **D1 receipt** : `d11_score.json` (Gwyn DEAL Liberate) + Cerritos state.json consolidé
- **A0 validation** : TTS SAPI Hortense bi-weekly milestone

---

## 10. HITL Gates (A0 actions requises)

| # | Action | Owner | Délai | Effort | Statut |
|---|---|---|---|---|---|
| 1 | Créer 5 Plane states custom (Inbox/Next Actions/Today/Someday/Maybe/Review) | A0 | W1 | 2 min via API ou UI | **À faire (D6 follow-up)** |
| 2 | Décider cadence Tendi review (weekly Friday 18:00 vs mensuel) | A0 | W1 | 1 min | À faire |
| 3 | Valider @context tag list (8 Life Wheel domains + @home/@work/@computer) | A0 | W2 | 5 min | À faire |
| 4 | Décider si Freeman dispatch = `mcp__symphony-plane__plane_update_state` direct ou via Morty A1 | A0 | W2 | 1 min | À faire |
| 5 | Valider anti-paperclip 3 garde-fous §6 (Tendi D1, Freeman D4, Mariner D7) | A0 | W3 | 5 min | À faire |

---

## 11. Critère de succès

**Q3 2026 W1** (07/05 fin) :
- ✅ 5 Plane states custom créés
- ✅ 5 crew routent vers 5 states (D1 verified)
- ✅ mcp__symphony-plane__ 6 tools tous fonctionnels

**Q3 2026 W2** (07/26 fin) :
- ✅ Obsidian @context bridge wired
- ✅ Freeman dispatch = 30s pick + 60s dispatch (D4 invariant)
- ✅ 0 escalation A0 mid-cycle (D7 cost-of-escalation)

**Q3 2026 W4** (09/07 fin) :
- ✅ Tendi review hebdo déclenché DEAL Dal Define sur pattern récurrent
- ✅ Gwyn D11 bandwidth = X h/semaine (à mesurer, baseline = 0)
- ✅ A0 board observer passif 12 semaines (0 intervention A0)

**Q4 2026** :
- D11 bandwidth consolidé cross-triptyque (12WY scorecard + PARA archive + DEAL liberate)
- Baserow + Affine re-intégrés (D6 #4 résolu)
- Triptyque complet (Morty + Beth) tourne 6 mois sans intervention A0

**Q1 2027** :
- 5 ADRs Life OS framework ratifiés (DEAL, GTD, PARA, Life Wheel, Symphony)
- Cible "Automatisation complète 2027" activée (cf. plan §13)

---

**Critère de succès global** : GTD Cerritos = **bus horizontal** visible dans Plane, 5 crew routent vers 5 states canoniques, Obsidian `@context` bridge wired, D11 bandwidth measurement live, A0 board observer passif 6m-1y.

> **D7 cost-of-escalation** : A0 = board observer passif. Ce spec doc = canon. A1 Morty supervise l'implémentation. A0 n'intervient QUE sur HITL gates listés §10. **PAS d'implémentation code** par A0 (D7 alarm si A0 touche un `.py`).
