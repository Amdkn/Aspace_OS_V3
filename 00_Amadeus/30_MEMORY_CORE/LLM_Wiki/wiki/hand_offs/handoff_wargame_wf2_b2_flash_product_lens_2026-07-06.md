---
title: "Wargame WF2 — A3 Picard (H10 Projects) vu par B2 Flash Product (H10 Spec Iterations)"
date: 2026-07-06
lens: b2-03-flash-product (⚡)
target_workflow: WF2 — A3 Enterprise Picard supervision (H10 — 12WY projects)
sister_squad: B3 Avengers — Captain America (lead, product vision) · Iron Man (tech product/premium UX) · Thor (flagship/roadmap) · Hulk (scale/stress) · Black Widow (competitive intel/data) · Hawkeye (spec accuracy/metrics) · Scarlet Witch (chaos-engineering/reality-bending UX)
sister_adrs_ratified:
  - ADR-LANDING-CRAFT-001 (RATIFIED 2026-07-06 — méta-process 7-phases Jack Roberts-inspired)
  - ADR-LANDING-QA-001 (RATIFIED 2026-07-06 — 5 critères Self-Critique + barème + JSON canon)
doctrine_anchors:
  - ADR-META-001 (D1-D8 — Anti-Paresse)
  - ADR-SOBER-002 (anti-paperclip — promises 2027 + chiffres inventés)
  - ADR-CANON-001 (Roster Source of Truth Avengers)
  - ADR-INFRA-003-Picard-H10 (project canon H10)
  - ADR-LD01-008 (loop engineering coaching — H10 → H1 aggregator Book)
  - ADR-ANTI-TEMPLATE-001 (DRAFT 2026-07-06 — 7 listes noires)
  - ADR-LANDING-AESTHETIC-001 (DRAFT 2026-07-06 — doctrine positive)
  - ADR-DESIGN-SYSTEM-001 (DRAFT 2026-07-06 — tokens canon)
  - ADR-ANTI-PAPERCLIP-001 (DRAFT 2026-07-06 — interdits textuels)
  - plan-lightning-l+-skill-standard-transversal (10 invariants 2026-07-05)
draft_status: wargame lens, NOT ratified
method: action / réaction / picard_capte? / contre / failure / abort
---

# ⚡ Wargame WF2 — A3 Picard supervision through B2 Flash Product lens

> **Lecture** : 5-10 angles morts où A3 Picard (capitaine des 12WY projects, H10 horizon) manque
> visibilité produit côté **B2 Flash — Product spec iterations (H10)** et son escouade **B3 Avengers**
> (Captain America · Iron Man · Thor · Hulk · Black Widow · Hawkeye · Scarlet Witch).
>
> **Posture** : cette liste est volontairement hostile — chaque angle est un scénario où le canon
> Picard actuel laisse A0 dans le noir côté produit. Sister-ADRs Landing ratifiées
> (LANDING-CRAFT-001 + LANDING-QA-001) ancrent la doctrine QA-gate. Aucune ligne n'invente de
> chiffre ; toutes les références citent un fichier canon.

---

## Angle mort #1 — Vision morale / product north-star absente du MANIFEST

> **Domaine B3** : Captain America (lead canon — product vision / moral north star / spec integrity)

| Champ | Contenu |
|---|---|
| **Action** | A0 ouvre un project via le 3-question gate Picard (`a3-enterprise-picard.md` l.39-45) : deadline ✓ / goal-bounded ✓ / owner + next_review ✓ → MANIFEST.md écrit (frontmatter l.50-62). |
| **Réaction** | Captain America (B3 lead) flag : un project n'a pas de **product vision / moral north star** dans sa frontmatter. Le 3-question gate teste « output-bounded » mais pas « purpose-anchored ». Sister-canon Avengers B3 : `b3-3-captain-america.md` role = « product vision, moral north star, spec integrity ». |
| **Picard capte?** | **NON.** La frontmatter canon (`a3-enterprise-picard.md` l.50-62) porte 7 champs : `project`, `owner`, `status`, `start_date`, `next_review`, `linked_12wy_rock`, `linked_area`, `junction` — **aucun champ** `product_vision`, `moral_north_star`, `icp_persona`, ou `jtbd`. |
| **Contre (par Flash)** | Sister-canon `ADR-LANDING-CRAFT-001 §2.4` pilar « D1 Verify-Before-Assert » + Jack Roberts 5 questions (sister `ADR-LANDING-QA-001 §2.3`). Ajouter dans MANIFEST `product_vision: <1 phrase impérative>` + `jtbd: <Jobs-To-Be-Done canon>` + `icp_persona: <Marcus|Harrison|David|...>`. |
| **Failure mode** | Project livré sans north star = drift d'objectif en H10. Sister QA-001 §4.4 PENDING gate : si Jack Roberts 5q ne sont pas fermes (qui/action/objections/vibe/brand_assets), la QA gèle — équivalent Picard, le 3-question gate devrait geler aussi. |
| **Abort criterion** | Project `status: active` sans `product_vision` ferme → Picard signale Cap America via `wiki/hand_offs/`. Sister-canon : `ADR-CANON-001` §Avengers. |

**D1 receipt** : `a3-enterprise-picard.md` lignes 50-62 = frontmatter actuelle, aucun champ
vision. `C:\Users\amado\.claude\agents\b3-3-captain-america.md` = role vision/moral-north-star.

---

## Angle mort #2 — Premium UX / armor-grade polish manquant côté frontmatter

> **Domaine B3** : Iron Man (tech product / premium UX / engineering lead)

| Champ | Contenu |
|---|---|
| **Action** | A0 ship un project Next.js + Vercel. Picard écrit MANIFEST + crée junction `apps/<role>/` (per `ADR-INFRA-002`). |
| **Réaction** | Iron Man (B3) flag : le canon ne capture pas **l'identité technique premium** du project (framework, type-system, design-system sister-canon, animation library, performance budget). Sister-canon : `ADR-LANDING-CRAFT-001 §5.1 Phase 1 Research` exige lecture de `SKILL-frontend-design.md` ; `ADR-DESIGN-SYSTEM-001` (DRAFT 2026-07-06) tokens canoniques. |
| **Picard capte?** | **NON.** Aucune trace canonique de `framework`, `tech_stack`, `design_system`, `performance_budget` (LCP/INP/CLS cibles per `ecc/web/performance.md`), `a11y_target` (WCAG 2.2 AA per A11y architect canon). |
| **Contre (par Flash)** | Ajouter frontmatter : `framework: nextjs|astro|vite|vanilla` · `design_system: <tokens-canon-path|null>` · `cwv_target: {lcp: 2.5s, inp: 200ms, cls: 0.1}` · `a11y_target: WCAG-2.2-AA`. Si project sans `design_system` ET phase 4 brief de `ADR-LANDING-CRAFT-001` applicable → Picard refuse `status: active`. |
| **Failure mode** | Projects « actifs » avec tech stack par défaut = drift V1 Inter Tight / purple gradient (sister V1 honnie empirique `ADR-LANDING-CRAFT-001 §2.2`). QA gate `ADR-LANDING-QA-001 §3.1` critère C1 (Anti-template) FAIL silencieusement si pas de design_system déclaré en frontmatter. |
| **Abort criterion** | Project `tier: T1` ou `T0` (sister Batman lens angle #4) sans `cwv_target` défini → Iron Man escalade B2 Flash → Cap America → Book H1 aggregator. |

**D1 receipt** : `a3-enterprise-picard.md` l.50-62 = 7 champs canon, aucun tech. V1 honnie
empirique `C:\Users\amado\omk-nexus-landing-3-personas\index.html` (paths absolus D1-shipped
`ADR-LANDING-CRAFT-001 §2.2`) = root cause Inter Tight + system-ui.

---

## Angle mort #3 — Flagship roadmap signal absent → Thor ne sait pas quoi hammer

> **Domaine B3** : Thor (flagship products / premium tiers / hammer-grade roadmap)

| Champ | Contenu |
|---|---|
| **Action** | A0 gère 5 projects actifs en parallèle. Picard les cerne en H10 (`status: active` + `linked_12wy_rock`). L+ Standard invariant #7 (« Wager mesurable — H10 input = 1 MANIFEST.md/cycle »). |
| **Réaction** | Thor (B3) flag : sans signal **flagship tier**, tous les rocks sont égaux. D11 anti-pattern canon (`a3-enterprise-picard.md` l.105) : « 1-3 per quarter » comme cap, mais **pas de hiérarchie flagship/mainstream/experimental** comme crible. Sister-canon : `ADR-LANDING-CRAFT-001 §3.1 Phase 4 ★ GATE B1 #1 ★` Brief ULTRA-PRESCRIPTIF distingue flagship/secondary. |
| **Picard capte?** | **PARTIELLEMENT.** Le `linked_12wy_rock` lie à un Rock 12WY (qui a un tier T1/T2 implicite), mais **pas de classification produit-side** (flagship / premium / starter / experimental). L'invariant L+ #7 cadence ≠ criticité. |
| **Contre (par Flash)** | Sister-canon `mindsets/B2_Flash_Dispatch_Doctrine.md` (posture C 0 cron) + `ADR-LANDING-CRAFT-001 §3.2` activation gate C1/C2/C3. Frontmatter Picard s'enrichit de `product_tier: flagship|premium|mainstream|experimental` + `kill_switch: YYYY-MM-DD` (date de décision GO/NO-GO). Si `kill_switch` dépassé sans décision → Thor escalade. |
| **Failure mode** | A0 traite 5 rocks comme égaux. Le flagship qui mérite Thor (premium tier + flagship roadmap) est noyé sous 4 rocks mainstream. Drift D6 (« A0's actual use pattern »). |
| **Abort criterion** | `product_tier: flagship` + `kill_switch` dépassé 14j sans décision → Picard refuse H10 graduation. |

**D1 receipt** : `a3-enterprise-picard.md` l.50-62 + l.105 (D11 metric « 1-3 per quarter » anti-pattern
>10 = scatter). Pas de `product_tier`. Sister-canon `ADR-LANDING-CRAFT-001 §4.4 Phase 4 Brief
ULTRA-PRESCRIPTIF` = la brief **distingue** flagship, mais ne **persist** pas en canon.

---

## Angle mort #4 — Scale / stress test gates absents (Hulk n'a pas de cible à briser)

> **Domaine B3** : Hulk (scale product / performance / gamma-tier capacity)

| Champ | Contenu |
|---|---|
| **Action** | Project passe `status: active`. Sister-canon Iron Man angle #2 — pas de `cwv_target` ni `scale_target`. |
| **Réaction** | Hulk (B3) flag : sans **scale / stress test gates**, pas de barème pour « ça tient ou ça casse ». Sister-canon `mindsets/B2_Flash_Dispatch_Doctrine.md` Avengers = Hulk role « stress test products, scale, gamma-tier capacity ». Pas de sister ADR canonnant les seuils scale (concurrent users, RPS, data volume). |
| **Picard capte?** | **NON.** Frontmatter actuelle = 0 champ scale. `a3-enterprise-picard.md` muet sur stress / load testing / chaos engineering. Sister-canon Scarlet Witch angle #7 = chaos-engineering sister discipline. |
| **Contre (par Flash)** | Sister-canon `ecc/web/performance.md` (LCP < 2.5s, INP < 200ms, CLS < 0.1) + `ecc/web/testing.md` (visual regression aux breakpoints 320/768/1024/1440). Frontmatter : `scale_target: { concurrent_users: N, rps: N, data_volume: <size> }` + `last_stress_test: YYYY-MM-DD` + `chaos_drill: <passed|pending|never>`. |
| **Failure mode** | Project `tier: T0` (sister Batman #4) ship en prod sans scale_target. Premier traffic burst = cascade → improvisation Hulk-style (juste après la casse, pas avant). |
| **Abort criterion** | `tier: T0` OU `tier: T1` + traffic > 1000 users/jour sans `scale_target` → Hulk signale B2 Flash → B1 Jerry. |

**D1 receipt** : `a3-enterprise-picard.md` = 0 mention scale/stress/chaos. Sister-canon
`ecc/web/performance.md` + `ecc/web/testing.md` = cibles chiffrées mais **pas persistées en
MANIFEST**.

---

## Angle mort #5 — Competitive intel / data product = angle mort Black Widow

> **Domaine B3** : Black Widow (competitive intel / espionage UX / sticky retention / security product / data)

| Champ | Contenu |
|---|---|
| **Action** | A0 ship un project landing. Sister-canon `ADR-LANDING-CRAFT-001 §3.1` Phase 1 Research exige recherche ICP, marché, concurrents implicites. |
| **Réaction** | Black Widow (B3) flag : le canon Picard n'enregistre **aucun signal concurrentiel** ni **data product hook**. Sister-canon : `b3-3-black-widow.md` role = « competitive intel, espionage UX, sticky retention, security product, data ». |
| **Picard capte?** | **NON.** Frontmatter canon = 0 champ concurrent, 0 champ retention, 0 champ telemetry privacy-aware. Sister-canon `ADR-ANTI-PAPERCLIP-001 §C1` + `ADR-SOBER-002` = Anti-Paperclip = « pas de claims 2027 non sourcés », mais **pas de persistance de la preuve concurrentielle**. |
| **Contre (par Flash)** | Sister-canon `ADR-LANDING-CRAFT-001 §4.1 Phase 1 Research` (5 critères score-gated) + `ADR-MARKET-STUDY-001` (DRAFT 2026-06-24 TAM 136,1 Mds$). Frontmatter : `competitors: [name1, name2, name3]` + `differentiation: <1 phrase anchor>` + `retention_metric: { metric: <activation|retention|engagement>, target: <%> }` + `telemetry: <PostHog|self-host|none>` (D1 receipts obligatoire sister `ADR-ANTI-PAPERCLIP-001`). |
| **Failure mode** | Project ship sans savoir contre qui il joue. Sister-canon `ADR-ICP-NEXUS-001` RATIFIED 2026-06-24 fixe 3 ICP canon (Marcus/Harrison/David) — mais la frontmatter project **ne capture pas contre qui**. Drift D6 (anti-paperclip) : A0 raconte la même histoire que les concurrents. |
| **Abort criterion** | Project landing sans `competitors` + `differentiation` à `status: active` → Black Widow refuse la promotion. |

**D1 receipt** : `a3-enterprise-picard.md` l.50-62 = 0 champ concurrent. Sister-canon
`ADR-ICP-NEXUS-001` RATIFIED + `ADR-LANDING-CRAFT-001 §4.1 Phase 1 Research` 5 critères canon.

---

## Angle mort #6 — Spec accuracy / Hawkeye n'a pas de target hit-rate

> **Domaine B3** : Hawkeye (spec accuracy / requirement traceability / target hit-rate / analytics product / metrics)

| Champ | Contenu |
|---|---|
| **Action** | A0 ship un project. Picard certifie via 3-question gate (deadline / goal-bounded / owner+next_review). Sister-canon L+ invariant #7 « Wager mesurable ». |
| **Réaction** | Hawkeye (B3) flag : « Wager mesurable » sans **mesure réelle** = pari vide. Hawkeye role = « spec accuracy, requirement traceability, target hit-rate ». Sister-canon QA `ADR-LANDING-QA-001 §3` 5 critères Self-Critique — mais ces 5 critères sont **landing-only** ; un project non-landing (e.g. infrastructure, pipeline) n'a pas de sister-gate. |
| **Picard capte?** | **PARTIELLEMENT.** L+ invariant #7 dit « 1 MANIFEST.md/cycle → 1 fiche P&L hebdo » (Book H1 aggregator). Mais **le MANIFEST lui-même ne porte pas de spec criteria** (5 questions Jack Roberts sister QA-001 §2.3 : qui/action/objections/vibe/brand_assets → qui / specification / done / measured / named). |
| **Contre (par Flash)** | Sister-canon `ADR-LANDING-QA-001 §5.2` export JSON canonique schema_version `omk-qa-v1` — généraliser à un **project-spec schema** `omk-project-spec-v1` : `{ id, spec_criteria: [list], hit_rate_pct: float, last_audit_iso: timestamp }`. Hawkeye signe la trace. |
| **Failure mode** | Project « actif » sans spec_criteria = drift progressif. D11 metric « 1-3 per quarter » (Picard canon l.105) ne dit pas **combien de criteria hit**. Anti-pattern : un Rock 12WY livré « done » sans spec_criteria documentée = pari à l'aveugle. |
| **Abort criterion** | `status: active` > 30j sans `spec_criteria` (≥ 3 critères Hawkeye) → Hawkeye refuse la graduation H10 suivante. |

**D1 receipt** : `a3-enterprise-picard.md` l.50-62 = 0 spec field. `L+ Skill Standard` ligne 7 =
« Wager mesurable » mais pas « Wager criterion-anchored ». Sister-canon `ADR-LANDING-QA-001 §5.2`
JSON schema = E1 script déterministe lookup pattern (`PRD-B1-FILTER-M3-001 §2`).

---

## Angle mort #7 — Chaos-engineering / reality-bending features = angle mort Scarlet Witch

> **Domaine B3** : Scarlet Witch (chaos-engineering / reality-bending features / hex-magic UX)

| Champ | Contenu |
|---|---|
| **Action** | Project ship en prod. A0 ne teste jamais le **mode chaos** : edge cases, dégraded paths, AI hallucination, partial failure. |
| **Réaction** | Scarlet Witch (B3) flag : sister-canon role « chaos-engineering, reality-bending features, hex-magic UX » — pas de **chaos drill plan** dans Picard canon. Sister-canon `ADR-LANDING-CRAFT-001 §7.2` anti-patterns QA, mais aucune persistance du chaos test en frontmatter. |
| **Picard capte?** | **NON.** 0 champ `chaos_drill`, `failure_mode_enumeration`, `graceful_degradation_path`. Sister-canon `ADR-ANTI-PAPERCLIP-001` (pas de chiffres inventés) contraste avec **pas de chaos testing** : on ship sans savoir comment le produit se dégrade. |
| **Contre (par Flash)** | Sister-canon `ecc/web/testing.md` testing priority 1-2-3 (visual / a11y / performance), pas de chaos. Frontmatter : `chaos_drill: { last_run_iso, scenarios: [list], coverage_pct }` + `graceful_degradation: <1 phrase>` + `failure_modes: [list]`. Scarlet Witch contrôle l'enumeration. |
| **Failure mode** | Project live, premier edge case (e.g. user 401 sur un edge function, rate limit Vercel, Supabase connection blip) = UX cassée. Scarlet Witch s'active en pompier (H1), pas en预防 (H10). |
| **Abort criterion** | `tier: T0` OU traffic > 5000 users/jour sans `chaos_drill` documenté > 90j → Scarlet Witch signale B2 Flash → B1 Jerry. |

**D1 receipt** : `a3-enterprise-picard.md` = 0 mention chaos / failure-mode. Sister-canon
`b3-3-scarlet-witch.md` role chaos-engineering. Pas de sister ADR chaos-testing canonisé.

---

## Angle mort #8 — Coaching handoff Picard graduation → Cap America signoff

> **Domaine B3** : Captain America (lead canon) + Iron Man + Hawkeye — co-signature Avengers

| Champ | Contenu |
|---|---|
| **Action** | Picard certifie un project `status: active` (per D11 metric « 1-3 per quarter »). Book H1 weekly aggregator (sister `ADR-LD01-008` loop-engineering) reçoit le signal. |
| **Réaction** | Avengers (B3) devraient avoir un **gate d'product-quality** parallèle à l'Ops gate sister Batman lens #8. Sister-canon QA `ADR-LANDING-QA-001 §7.1` workflow QA Phase 7 = gate bloquant pour SHIP landing — sister-symmetric : gate product-quality pour SHIP project. |
| **Picard capte?** | **PARTIELLEMENT.** L'invariant #7 L+ Skill Standard engage Picard à produire MANIFEST — mais ne **vérifie pas** les gates produit (vision / tech / flagship / scale / intel / spec / chaos) avant `status: active`. La graduation est un acte unilatéral Picard, sans co-signature Avengers. |
| **Contre (par Flash)** | Avant `status: active`, Picard POSTULE aux Avengers un mini-audit (7-checkpoint : vision ✅ tech ✅ flagship ✅ scale ✅ intel ✅ spec ✅ chaos ✅). Cap America signe `product_quality: SIGNED` dans la frontmatter. Sans cette signature, Picard **DOIT** rester à `status: initiated`. Sister-canon : `ADR-LANDING-QA-001 §4.2 Loi C1 = gate critique » → sister-symmetric « Avengers gate critique = status:active ». |
| **Failure mode** | Projects « actifs » sans product_quality = drift silencieux. Book H1 aggregator ramasse des rocks qui ne devraient pas exister. Anti-pattern « graduer un project sans product signoff » documenté implicite en D6 « root cause = A0's actual use pattern ». |
| **Abort criterion** | `status: active` sans `product_quality: SIGNED` → Picard refuse la canonisation. Escalade B2 Flash → B1 Jerry. |

**D1 receipt** : `a3-enterprise-picard.md` lignes 76-82 = canonization checklist 5 points. Aucun
gate product quality. `L+ Skill Standard` ligne 7 = « Wager mesurable » mais pas « Wager
co-signé Avengers ».

---

## Synthèse pour coaching A3 Book (sister H1 aggregator)

> **Cible** : A3 Book (Calypso) — aggregator H1 weekly P&L du L1 Life OS, owner du sister-canon
> `a3-discovery-book.md`. Il reçoit les rocks Picard H10 et agrège en fiche P&L hebdo.
> Sister-canon `ADR-LD01-008` loop-engineering coaching.

### 4 métriques produit à proposer à Book comme inputs H10 enrichis

1. **`product_vision_clarity` (count)** = nombre de projects actifs avec `product_vision` ferme (1 phrase impérative) — alimente Book H1 si < 100% (anti-drift). Source : nouveau champ Picard frontmatter (Cap America angle #1).
2. **`design_system_coverage` (% projects)** = % projects actifs avec `design_system` sister-canon (`ADR-DESIGN-SYSTEM-001` HYPOTHÈSE) déclaré. Anti-pattern : 0% sur projet landing = V1 honnie redux (sister `ADR-LANDING-CRAFT-001 §2.3`). Source : nouveau champ (Iron Man angle #2).
3. **`flagship_kill_switch_age` (jours max)** = âge max des `kill_switch` sur `product_tier: flagship`. Si > 14j sans décision → flag Thor. Source : nouveau champ `product_tier` + `kill_switch` (Thor angle #3).
4. **`spec_hit_rate_avg` (%, 12WY cycle)** = moyenne des hit_rate sur `spec_criteria` Hawkeye across projects actifs. Anti-pattern < 60% = drift chaos engineering. Source : nouveau champ (Hawkeye angle #6).

### 3 escalades types vers Beth veto (L1 Conscience)

| Trigger | Escalade |
|---|---|
| Project actif > 30j sans `product_vision` | Picard → Flash B2 → Cap America B3 (lead) → Book H1 |
| Project landing sans `design_system` sister-canon | Picard → Flash → Iron Man B3 → gate QA Phase 7 `ADR-LANDING-QA-001 §3.1` C1 |
| `product_tier: flagship` + `kill_switch` dépassé 14j | Picard → Flash → Thor B3 → Book H1 aggregator |

### 1 doctrine gap visible après ce wargame

> **Doctrine à proposer** (NON ratifiée — à A0 GO) :
> *« Aucun project Picard ne passe `status: active` sans septuple co-signature Avengers
> (Cap America vision · Iron Man tech · Thor flagship · Hulk scale · Black Widow intel ·
> Hawkeye spec · Scarlet Witch chaos). Sister-symmetric au Ops gate sister Batman lens #8
> et au Landing QA gate `ADR-LANDING-QA-001 §4.2` Loi C1. »*
>
> **Sister-canon candidat** : `ADR-PRODUCT-PROJECT-GATE-001` (à ratifier en Q3 2026 cycle 12WY).

### Anti-patterns protégés (D6)

- ❌ Ne PAS ajouter de gates produit sans A0 HITL (Posture C + ADR-SOBER-002 §6 anti-paperclip).
- ❌ Ne PAS muter `a3-enterprise-picard.md` depuis cette lens (L+ invariant #3 — A3 Book spec append-only strict).
- ❌ Ne PAS inventer de chiffre spec / hit_rate tant que Hawkeye ne les a pas négociés avec A0 (D1 receipts = only D1 receipts).
- ❌ Ne PAS dupliquer le gate `ADR-LANDING-QA-001` (Landing-only) en gate générique project — sister-symmetric ≠ duplication.

---

## D1 receipts (sources canon lues pour ce wargame)

- `C:\Users\amado\.claude\agents\b2-03-flash-product.md` — Flash B2 manager identity + horizon H10
- `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` — Picard full spec, frontmatter l.50-62, D4 l.100, D11 metric l.105
- `C:\Users\amado\.claude\agents\a3-discovery-book.md` — Book H1 aggregator identifier (sister-recevoir)
- `C:\Users\amado\.claude\agents\b3-3-captain-america.md` — product vision / moral north star (lead Avengers)
- `C:\Users\amado\.claude\agents\b3-3-iron-man.md` — tech product / premium UX / engineering lead
- `C:\Users\amado\.claude\agents\b3-3-thor.md` — flagship products / premium tiers / hammer-grade roadmap
- `C:\Users\amado\.claude\agents\b3-3-hulk.md` — stress test products / scale / gamma-tier capacity
- `C:\Users\amado\.claude\agents\b3-3-black-widow.md` — competitive intel / espionage UX / sticky retention / data
- `C:\Users\amado\.claude\agents\b3-3-hawkeye.md` — spec accuracy / requirement traceability / target hit-rate
- `C:\Users\amado\.claude\agents\b3-3-scarlet-witch.md` — chaos-engineering / reality-bending features / hex-magic UX
- `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-LANDING-CRAFT-001_meta-process-creation.md` (RATIFIED 2026-07-06) — méta-process 7-phases
- `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-LANDING-QA-001_5-criteres-self-critique.md` (RATIFIED 2026-07-06) — 5 critères QA + barème
- `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-ICP-NEXUS-001_icp-nexus-structuration.md` (RATIFIED 2026-06-24) — 3 ICP canon Marcus/Harrison/David
- `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-MARKET-STUDY-001_*.md` (DRAFT 2026-06-24) — TAM 136,1 Mds$
- `C:\Users\amado\.claude\rules\ecc\web\performance.md` — CWV targets (LCP < 2.5s, INP < 200ms, CLS < 0.1)
- `C:\Users\amado\.claude\rules\ecc\web\testing.md` — testing priority 1-5 (visual / a11y / perf / cross-browser / responsive)
- `C:\Users\amado\omk-nexus-landing-3-personas\index.html` — V1 honnie empirique (Inter Tight + system-ui violation)

## Open follow-ups (NOT actions — just signals)

1. Sister-canon `ADR-PRODUCT-PROJECT-GATE-001` à proposer à A0 ratification Q3 2026.
2. Sister-canon `ADR-DESIGN-SYSTEM-001` (HYPOTHÈSE) à canoniser — sister-canon des 5 landing ADRs.
3. Sister-canon `ADR-LANDING-AESTHETIC-001` (HYPOTHÈSE) à canoniser — feeder QA C2 + C4.
4. Sister-canon `ADR-LANDING-COPY-001` (HYPOTHÈSE) à canoniser — sister-canon copywriting canonique 3 personas.
5. Cross-link `a3-enterprise-picard.md` frontmatter l.50-62 vers Avengers H10 (sans mutation du spec, par linked-instruction).
6. Sister-coaching A3 Book : intégrer 4 métriques produit (product_vision_clarity / design_system_coverage / flagship_kill_switch_age / spec_hit_rate_avg) dans agrégat P&L hebdo.
7. Couple avec sister lens Batman #8 (Ops gate F4) + sister lens Cyborg IT (Kang Dynasty IT gate) pour triple co-signature avant `status: active` — à A0 GO.

---

**⚡ B2 Flash Product — 2026-07-06, lens wargame WF2. Aucune ligne n'écrit dans un canon sans A0 GO
(per ADR-SOBER-002 §6). Le présent fichier est un signal diagnostique, pas une modification du canon.
Sister-symmetric au sister wargame B2 Batman Ops `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md`.**
