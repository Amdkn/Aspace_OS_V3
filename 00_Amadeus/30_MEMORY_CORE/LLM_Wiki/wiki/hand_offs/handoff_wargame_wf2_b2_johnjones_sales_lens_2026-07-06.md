---
handoff: wargame_wf2_b2_johnjones_sales_lens
date: 2026-07-06
workflow: WF2 (A3 Picard captain USS Enterprise)
lens: B2-05-JohnJones-Sales (Illuminati squad)
coaching_target: A3-Book (H1 aggregator)
wargame_author: b2-05-johnjones-sales
status: live
doctrine_anchors:
  - ADR-CANON-001 (roster source of truth)
  - ADR-SOBER-002 §1 (anti-paperclip CAC/LTV hard-veto)
  - ADR-AAAS-PRICING-001 (5 Tiers AaaS Solarpunk canon 2026-06-24)
  - ADR-L2-AAAS-001 (3 Variants AaaS Solarpunk RATIFIED 2026-06-21)
  - ADR-INFRA-002 (Repo-Home/Junction)
  - ADR-INFRA-003 (CEO Dashboard)
  - ADR-LD01-008 (loop engineering coaching H10 → H1)
  - ADR-LD01-010 (HA Picard promotion 2026-07-05)
  - L+ Skill Standard 2026-07-05 ratification
  - ADR-AAAS-FINANCE-CANON-001 (CAC/LTV sister canon)
sister_squad: B3 Illuminati — Black Bolt (lead, sovereign deals) · Tony Stark (tech enterprise) · Reed Richards (R&D pipeline) · Namor (wholesale/deep-blue) · Charles Xavier (strategic accounts mentalist) · Stephen Strange (international/sovereign-nation-tier)
sister_wargames_wf2:
  - handoff_wargame_wf2_b2_greenlantern_people_lens_2026-07-06.md (X-Men lens)
  - handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md (F4 lens)
---

# 🔍 Wargame WF2 — Lens B2-JohnJones-Sales (Illuminati squad)

> **Lecture** : 5-10 angles morts où **A3 Picard** (Projects Captain, H10, MANIFEST.md
> enforcer, classify gate 3 questions) supervise ailleurs pendant que les dynamics
> **Sales** (pipeline, close rate, B2B/B2C, CAC/LTV, pricing tier) vivent, dérivent, ou
> s'effondrent en silence.
>
> **Méthode Fable appliquée à chaque angle mort** :
> - **Action** : ce que Picard fait (sa porte d'entrée canon = 3-gate + MANIFEST.md frontmatter)
> - **Réaction** : ce que Sales vit pendant ce temps (Illuminati squad voices)
> - **Contre** : ce que B2 JohnJones tente pour compenser (hard-veto CAC/LTV per spec L.42)
> - **Failure** : pourquoi la compensation échoue (asymétrie de cadence, doctrine, ou pouvoir)
> - **Abort** : déclencheur qui force A3-Book (coaching target) à monter le signal
>
> **Posture** : cette liste est volontairement hostile — chaque angle est un scénario où le
> canon Picard actuel laisse A0 dans le noir côté Sales. Aucune ligne n'invente de chiffre ;
> toutes les références citent un fichier canon.

**Sources canon lues (paths absolus)** :
- `C:\Users\amado\.claude\agents\b2-05-johnjones-sales.md` (B2 Sales — lu intégralement)
- `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` (A3 supervised — lu intégralement)
- `C:\Users\amado\.claude\agents\a3-discovery-book.md` (A3 coaching target, MC aggregator — lu intégralement)
- `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-AAAS-PRICING-001_aaas-pricing-canon.md` (5 Tiers canon RATIFIED 2026-06-24 — lu intégralement)

---

## 0. Picard — Porte d'entrée canon (rappel D1)

Picard supervise à travers **3 gates + MANIFEST.md frontmatter** (spec `a3-enterprise-picard.md` lignes 39-63) :

1. **3-question gate** (L.40-44) : deadline ? goal-bounded ? owner+next_review ?
2. **MANIFEST.md frontmatter** (L.50-62) : 8 champs = `project`, `owner`, `status`, `start_date`, `next_review`, `linked_12wy_rock`, `linked_area`, `junction`
3. **Cadence H10** : produit MANIFEST.md par cycle 12WY (10 semaines), agrégé par A3-Book en H1 hebdo
4. **Doctrine** : D1 verify-before-write, D4 append-only strict, D6 bucket-ambiguity, D7 batch-create, D11 metric (active Projects/quarter, target 1-3, anti-pattern >10)

**Ce que Picard NE regarde PAS** (par construction, sister-au-jumeau GreenLantern People + Batman Ops) :
- Le contenu commercial du Project (combien ça vend, à qui, à quel prix, quel CAC, quel LTV)
- Les dynamics entre Projects sales (overlap pricing tier, channel conflict, ICP collision)
- Les signaux soft pipeline (MQL → SQL → close → onboarding) — pas de frontmatter pour ça
- La cadence H10 vs H1 (9-semaines blackout entre 2 MANIFEST.md)

**Spécificité Sales lens** : B2 JohnJones spec L.42 = *"Hard-veto sur tout deal sans CAC + LTV documentes (sister ADR-SOBER-002 §1)"*. Mais le hard-veto porte sur la **canonisation Sales** (deals B2B/B2C), pas sur la canonisation Picard Projects. Asymétrie structurelle = angle mort fondateur de tout ce wargame.

---

## 1. Angles morts catalogués (8 — pattern Fable)

### 🔴 Angle mort #1 — CAC/LTV blind-spot in 3-gate (Black Bolt)

> **Domaine B3** : Black Bolt (lead — sovereign deals, ferme les deals complexes enterprise)

| Champ | Contenu |
|---|---|
| **Action** | A0 lance un Project (Sales motion). Picard engage le 3-question gate (L.40-44) : deadline ? goal-bounded ? owner+next_review ? → 3/3 oui → Project canonisé. |
| **Réaction** | Black Bolt (B3 lead) doit normalement hard-veter le deal **avant** canonisation, per B2 spec L.42 + ADR-SOBER-002 §1 : *tout deal sans CAC + LTV documentés = REJET*. |
| **Picard capte?** | **NON.** Le 3-question gate (L.40-44) teste deadline / goal-bounded / owner — **aucune question CAC, aucune question LTV, aucune question unit economics**. Pas de pre-flight `cac_documented: bool` ou `ltv_documented: bool`. Sister-canon absent : `ADR-AAAS-FINANCE-CANON-001` (B2 Wonder Woman owns) non câblé à A3 Picard. |
| **Contre (par JohnJones)** | Brancher Picard à Black Bolt : avant `MANIFEST.md` écrit, exiger un pré-flight `unit_econ: GREEN|YELLOW|RED` par B3 Black Bolt + B2 Wonder Woman (CAC/LTV sister). RED = route B3 Yelena (pricing sharp shooter, sister B2) + B3 Taskmaster (CAC mirroring). Sister : `ADR-SOBER-002 §1` anti-paperclip trigger #1. |
| **Failure mode** | Project Sales canonisé sans unit economics. A0 ship la motion sans savoir si chaque close améliore ou détruit le runway. Drift documenté typique D6. **Anti-pattern "ship the deal first, validate les chiffres après"** — accepté par construction. |
| **Abort criterion** | MANIFEST.md Status `active` sans `unit_econ: GREEN` documenté → Picard signale à B2 JohnJones via `wiki/hand_offs/l2_b2_johnjones_sales_<DATE>.md` (per B2 spec L.43). Sister-can : `ADR-AAAS-FINANCE-CANON-001` + `ADR-AAAS-PRICING-001`. |

**D1 receipt** : `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` L.40-44 = 3-question gate, aucun champ CAC/LTV. `C:\Users\amado\.claude\agents\b2-05-johnjones-sales.md` L.42 = hard-veto CAC/LTV documenté. `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-AAAS-PRICING-001_aaas-pricing-canon.md` L.59-72 = 5 Tiers canon sans champ `cac` canon.

---

### 🔴 Angle mort #2 — Pricing tier drift invisible (Charles Xavier)

> **Domaine B3** : Charles Xavier (strategic accounts mentalist — buyer mapping, X-Men overlap)

| Champ | Contenu |
|---|---|
| **Action** | Project Sales vit, fait signer T1 PME Solo Founder à $300-500/an (per `ADR-AAAS-PRICING-001` Tier 1 canon RATIFIED 2026-06-24). 6 mois plus tard, deal upgrade → T3 PME Groupe à $4000-5000/an (×8 sur le même moteur, même ACV uplift canon). |
| **Réaction** | Charles Xavier (B3) cartographie le buyer mental model, détecte le tier upgrade, et doit escalader "deal ×8 sur pricing tier" — mais l'info ne va nulle part dans le canon Picard. |
| **Picard capte?** | **NON.** Le frontmatter MANIFEST.md canon (L.50-62) ne contient pas `pricing_tier: T1|T2|T3|T4|T5`. Le Project reste `linked_12wy_rock: 12WY-Q3-2026-rock-03` sans que le tier pricing du deal ait changé. Sister-canon `ADR-AAAS-PRICING-001` est non câblé au frontmatter. |
| **Contre (par JohnJones)** | Ajouter une frontmatter Picard : `pricing_tier: T1|T2|T3|T4|T5` (per `ADR-AAAS-PRICING-001` 5 tiers canon). Charles Xavier + B2 Wonder Woman finance signale un upgrade/downgrade tier chaque C-view B3 (H3 quarterly close rate audit, B2 spec L.39). |
| **Failure mode** | A0 ship une motion Sales sur un tier T1 mais Book agrege weekly P&L en supposant T3 (ou l'inverse) → LD01 Business drift advertorial silencieux (GreenLantern Sister §8 angle mort #8 — H10↔H1 cadence blackout). Drift financier invisible jusqu'à l'audit. |
| **Abort criterion** | MANIFEST.md sans `pricing_tier` déclaré OU mismatch `pricing_tier` ↔ `linked_12wy_rock` revenue projection → Picard signale à B2 JohnJones + B2 Wonder Woman (Twin H3 quarterly runway, sister `a3-discovery-saru`). |

**D1 receipt** : `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-AAAS-PRICING-001_aaas-pricing-canon.md` L.57-72 = 5 Tiers canon, **mais pas une seule mention frontmatter Picard**. `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` L.50-62 = 7 champs frontmatter courants (status, next_review, etc.), aucun `pricing_tier`.

---

### 🔴 Angle mort #3 — Pipeline stage invisibility H1↔H10 (Tony Stark + Reed Richards)

> **Domaine B3** : Tony Stark (tech sales, enterprise accounts, premium tier) + Reed Richards (R&D pipeline, innovation pitches, future-grade)

| Champ | Contenu |
|---|---|
| **Action** | Project Sales créé en début de cycle H10 (week 0). À week 4, le deal bouge : lead → MQL → SQL → opportunity → close. À week 8, le deal est `closed_won` ou `closed_lost`. Picard ne revoit le Project qu'à `next_review` (+10 semaines). |
| **Réaction** | Tony Stark (B3 tech enterprise) trace chaque étape du funnel en temps réel (Notion pipeline stages per B2 spec L.23). Reed Richards (B3 R&D pipeline) signe les early-adopter POCs en H1. Les deux écrivent dans Notion / Hubspot / CRM — **hors canon Picard**. |
| **Picard capte?** | **NON.** La cadence H10 de Picard (1 MANIFEST.md par cycle, spec L.110-117 `loop_engineering_tick`) capte le Project au début et à la fin. Les 8-9 semaines intermédiaires = blackout totale côté Sales velocity. Sister-canal GreenLantern angle mort #8 — H10↔H1 cadence blackout — sister-jumeau. |
| **Contre (par JohnJones)** | Sister-anneau avec GreenLantern People R1 : ajouter un **mini-MANIFEST delta** H1 (semaine) qui updat seulement le champ `pipeline_stage: lead|MQL|SQL|opportunity|closed_won|closed_lost` + `deal_value_usd: <int>` + `close_probability: 0..100`. L+ invariant #7 ("Wager mesurable — H10 = 1 MANIFEST/cycle") reste compatible — le delta H1 ne crée pas de Project, il update un frontmatter déjà canon. |
| **Failure mode** | Q avec 5 Sales Projects H10, tous archivés `closed_won` au next_review, mais Book H1 aggregator n'a aucune visibilité sur les deals réels signés semaine par semaine → LD01 P&L hebdo se base sur autre chose (Notion / finance). Picard canon et reality divergent en silence pendant 9 semaines. |
| **Abort criterion** | Project H10 sans update `pipeline_stage` pendant > 4 semaines (= blackout > 50% du cycle H10) → Picard signale à Book H1 + B2 JohnJones. Anti-pattern "Project vivant, deal mort" documenté. |

**D1 receipt** : `C:\Users\amado\.claude\agents\b2-05-johnjones-sales.md` L.23 = "Notion pipeline stages, ClickUp close rate" — aucune mention canon Picard. `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` L.110-117 = `loop_engineering_tick` H10 uniquement, **aucun tick H1**.

---

### 🔴 Angle mort #4 — International / sovereign deal compliance (Stephen Strange)

> **Domaine B3** : Stephen Strange (international mystic deals, sovereign-nation-tier contracts)

| Champ | Contenu |
|---|---|
| **Action** | Project Sales avec deal cross-border (e.g. Tier 4 Nexus ops-led à $180K ARR dans un pays tiers hors UE). Picard canonise en H10 standard. |
| **Réaction** | Stephen Strange (B3) déclenche un cadre de compliance international : data residency, GDPR/AI-Act (per B2 Aquaman Legal + `mindsets/`, AI-Act 2026-08-02 deadline), sanctions screening, B3 Ajak (communion with compliance officers). |
| **Picard capte?** | **NON.** Le frontmatter L.50-62 = 7 champs, **aucun `jurisdiction: <ISO>`, aucun `data_residency: <region>`, aucun `screening_passed: bool`**. Les 3 questions du gate (deadline/goal-bounded/owner+next_review) sont location-blind. Sister avec Batman lens angle mort #2 (privacy/PII), sister avec Aquaman `b2-08-aquaman-legal.md` (AI-Act). |
| **Contre (par JohnJones)** | Pré-flight `compliance: GREEN|YELLOW|RED` par B3 Stephen Strange + B3 Ajak Legal avant canonisation MANIFEST.md. RED = route B3 Ikaris Legal (lead AI-Act 2026-08-02). Sister-canon B2 Aquaman (`b2-08-aquaman-legal.md`) — pas câblé à Picard canon. |
| **Failure mode** | Project Sales cross-border canonisé sans screening. A0 close un deal qui viole AI-Act ou sanctions → D7 cost-of-escalation Beth + B1 Jerry veto sur l'org entier. Anti-pattern "ship the deal first, screen after" — par construction. |
| **Abort criterion** | MANIFEST.md project touchant `*.gouv.*`, `*sanctions*`, ICP international Nexus/Orbiter, ou mot-clé "cross-border" dans `01_charter.md` → Picard refuse la canonisation tant que `compliance: GREEN` non documenté. Escalade B2 JohnJones → B2 Aquaman → Beth Veto. |

**D1 receipt** : `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` L.40-44 = 3-gate location-blind. `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-AAAS-PRICING-001_aaas-pricing-canon.md` L.62-65 = Tier 4 Nexus + Tier 5 Orbiter Enterprise **international/multi-jurisdiction par construction** canon. `AI-Act 2026-08-02` deadline canon.

---

### 🔴 Angle mort #5 — Wholesale / distribution = multi-buyer (Namor)

> **Domaine B3** : Namor (wholesale distribution, deep-blue channel partnerships)

| Champ | Contenu |
|---|---|
| **Action** | Project Sales avec channel wholesale = distribution multi-PME (e.g. Tier 1 PME Solo Founder via reseller/distributor → 50+ sous-deals sous le même Project canon). |
| **Réaction** | Namor (B3) trace chaque sous-buyer, gére la deep-blue channel conflict (T1 PME Solo via 2+ distributors qui se cannibalisent), et arbitre le wholesale pricing. |
| **Picard capte?** | **NON.** Le modèle Project (spec L.41 = "goal-bounded, will it END when done", L.52 = `owner: A0 Amadeus`) assume **un seul owner final**. Un Project wholesale = N acheteurs sous le même owner canon, mais le frontmatter n'a pas de `channel_type: direct|wholesale|partner`, ni de `sub_buyer_count`, ni de `channel_conflict_resolved: bool`. |
| **Contre (par JohnJones)** | Frontmatter Picard : `channel_type: direct|wholesale|partner|hybrid` (default direct à création). Si wholesale, sister-champ `sub_buyer_count: <int>` + `channel_conflict_resolved: bool`. Namor B3 contrôle le conflit (drainage tier pricing canon `ADR-AAAS-PRICING-001` Tier 1 vs Tier 2). |
| **Failure mode** | Project wholesale canonisé T1 PME Solo × 50. Conflic T1 vs T2 (Tier 1 PME Solo Founder vs Tier 2 PME Solo Standard — 60-70% volume tier 1, per `ADR-AAAS-PRICING-001` L.62) : un distributor signe un client Tier 2 par erreur de pricing → revenue downshift silencieux. Anti-pattern "single Project, multi-buyer, no tier conflict" par construction. |
| **Abort criterion** | MANIFEST.md project avec `linked_12wy_rock` TAC = wholesale sans `channel_conflict_resolved: true` ET `sub_buyer_count > 5` → Picard signale à B2 JohnJones + B3 Namor + B2 Wonder Woman (LTV:CAC sister). |

**D1 receipt** : `C:\Users\amado\.claude\agents\b2-05-johnjones-sales.md` L.28 = "Namor : wholesale / distribution". `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` L.50-62 = frontmatter 7 champs, aucun `channel_type`. `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-AAAS-PRICING-001_aaas-pricing-canon.md` L.62-65 = Tier 1 PME Solo = 60-70% volume tier = volume canon wholesale-friendly.

---

### 🔴 Angle mort #6 — H1 R&D pitch vs H10 Project census (Reed Richards)

> **Domaine B3** : Reed Richards (R&D pipeline, innovation pitches, future-grade product pitches)

| Champ | Contenu |
|---|---|
| **Action** | Reed Richards (B3) signe 5 POCs early-adopter en H1 (semaines) pour valider un nouveau pricing tier ou une nouvelle ICP canon. Aucun des 5 ne déclenche un MANIFEST.md Picard car **trop courts** (1-2 semaines chacun). |
| **Réaction** | Reed Richards tient un log H1 de "R&D sales experiments" dans Notion / sister-canon `04_Archives_Data/`. Patterns : 3/5 POCs échouent, 2/5 passent → propose un pricing tier T6 (innovation tier) ou un add-on T1.5. |
| **Picard capte?** | **NON.** H1 (1-2 semaines) << H10 (10 semaines). L+ invariant #7 "Wager mesurable" (L.116) demande 1 output/cycle H10 — Reed Richards opère **plusieurs cycles** dans la même fenêtre H10. Sister-jumeau GreenLantern lens angle mort #7 (Jean Grey mentorship H1 vs H10). |
| **Contre (par JohnJones)** | Permettre à A3 Picard d'absorber les R&D sales experiments en mode **archived-H1-snapshot** : un patch `r_and_d_summary.md` sibling sister-canon `04_Archives_Ops_Data/` (per Batman lens angle mort #3 hot-fix path) qui résume H1 tous les POCs dans le cycle H10, sans créer un Project par POC. |
| **Failure mode** | Q avec 0 R&D sales → Reed Richards tenure zéro en canon Picard. Mais le Q suivant : 3 POCs réussis → opportunity de pricing tier T6 = drift sibling-canon `ADR-AAAS-PRICING-001` (5 tiers canon — un T6 = extension breaking canon, sister Supabase migration). Anti-pattern "R&D silencieux puis Tier explosion" par construction. |
| **Abort criterion** | `r_and_d_summary.md` sibling manquante sur un Project H10 avec `linked_12wy_rock` ≠ NULL ET 0 POCs canon → Picard signale Book H1 + B2 JohnJones. |

**D1 receipt** : `C:\Users\amado\.claude\agents\b2-05-johnjones-sales.md` L.28 = "Reed Richards : R&D sales / innovation pipeline". `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` L.116 = L+ invariant #7 "H10 = 1 MANIFEST/cycle", aucun tick H1.

---

### 🔴 Angle mort #7 — Buyer = external entity, MANIFEST owner = A0 (Charles Xavier)

> **Domaine B3** : Charles Xavier (strategic accounts, buyer mapping)

| Champ | Contenu |
|---|---|
| **Action** | Project Sales canonisé avec `owner: A0 Amadeus` (canonical owner, spec Picard L.54 exemple). Le **vrai buyer** = entité externe (e.g. "Acme Corp", prospect Nexus mid-market). |
| **Réaction** | Charles Xavier (B3) cartographie l'account externe (champ CRM `account_id`, `deal_value`, `buyer_champion`, `economic_buyer`, `decision_criteria`, `close_date_forecasted`). Aucun de ces champs n'existe dans le canon Picard. |
| **Picard capte?** | **NON.** Le frontmatter canon (L.50-62) a `owner: A0` (internal signatory) et `linked_area: LD0X_<domain>` (life wheel cross-link), mais **aucun `external_account_id`, aucun `account_owner_external`, aucun `buyer_champion`**. D4 append-only strict empêche de muter `owner` (s'il tentait, hard-mutation viola D4 spec L.99). |
| **Contre (par JohnJones)** | Sister-jumeau GreenLantern angle mort #4 (Talent mobility stale owner) : ajouter un champ frontmatter optionnel `account_ref: <CRM-URL-or-ID>` qui pointe vers Notion / Hubspot record sans muter `owner`. Charles Xavier écrit dans Notion (B2 owns `people ops: Notion team pages` sister) — sister-canon CRM. |
| **Failure mode** | Project Sales canonisé, deal Acme Corp signé, A0 owner canon, mais Acme Corp expansion / cross-sell / QBR data = orphelins hors canon. Le sister-canon `team_pages` chez B2 GreenLantern ne fait pas le lien. **Anti-pattern "internal owner canon, external account orphan"** par construction. |
| **Abort criterion** | MANIFEST.md projet avec `linked_12wy_rock` ≠ NULL ET `account_ref` vide ET next_review > +4 semaines → Picard signale Book H1 + Charles Xavier B3 + GreenLantern B2 (account retention overlap). |

**D1 receipt** : `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` L.54 = `owner: A0 Amadeus` canon. `C:\Users\amado\.claude\agents\b2-05-johnjones-sales.md` L.28-29 = "Charles Xavier (Professor X) : strategic accounts (overlap X-Men)" — sister-overlap explicite.

---

### 🔴 Angle mort #8 — Close rate H3 metric orphan from H10 D11 census (Black Bolt + Charles Xavier)

> **Domaine B3** : Black Bolt (lead, sovereign deals) + Charles Xavier (strategic accounts) — H3 quarterly close rate audit

| Champ | Contenu |
|---|---|
| **Action** | Picard D11 metric (spec L.104, canon) = count active Projects per 12WY cycle (target 1-3, anti-pattern >10). C'est une métrique canon-count. |
| **Réaction** | Black Bolt + Charles Xavier mesurent le **close rate** (H3 quarterly audit, per B2 spec L.39 : *"weekly H1 pipeline review + quarterly H3 close rate audit"*). Métrique famille ≠ D11 metric. Sister-canon `ADR-OBSERVABILITY-001` (D11 lead/lag) doit distinguer lead CAC, lag MRR, lag churn. |
| **Picard capte?** | **NON.** D11 metric = "active Projects count" n'a aucune notion de deal close rate, deal size, MRR uplift, churn. Le sign Canon H10 ignore la sign Sales H3. Sister-lens : Batman lens angle mort #5 RTO/RPO + observability absent. |
| **Contre (par JohnJones)** | Sister-jumeau Batman lens R1 : ajouter un champ `close_health: green|yellow|red` (H3 computed by Black Bolt + Charles Xavier) à la frontmatter Picard. Pair avec `pricing_tier` R2 Sales lens → Picard canon capte lead signal (D11 count) + lag signal (close rate). Compatible L+ invariant #7 (1 wager mesurable/cycle H10 = agreg H3 close rate per cycle). |
| **Failure mode** | Q avec 12 active Projects (anti-pattern D11 = scatter per spec L.104) MAIS close rate 80% = OK Sales. Ou Q avec 2 active Projects MAIS close rate 20% = alarm Sales silencieux. **D11 count ≠ Sales health** — les deux métriques vivent en parallèle sans corrélation canon. Anti-pattern D6 root-cause = spec Picard ne porte pas Sales dimension par construction. |
| **Abort criterion** | MANIFEST.md project avec `close_health: red` (H3 verdict) ET `status: active` ET next_review > +2 semaines → Picard signale Book H1 + B2 JohnJones + B1 Jerry (PRODUCT-JUDGMENT escalation, sister `ADR-AAAS-FINANCE-CANON-001` CAC/LTV). |

**D1 receipt** : `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` L.104 = "Picard D11 metric : count active Projects per 12WY cycle (target: 1-3 per quarter, anti-pattern = >10 active = scatter)" — **count unique**, close rate absent. `C:\Users\amado\.claude\agents\b2-05-johnjones-sales.md` L.39 = "weekly H1 pipeline review + quarterly H3 close rate audit". `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-OBSERVABILITY-001_d11-lead-lag.md` = lead/lag canon sister, **non câblé à Picard frontmatter**.

---

## 2. Synthèse Sales pour coaching A3-Book

### 📊 D1 receipts (asymétries quantifiées)

| Dimension Sales | Cadence | Écrit où | Lu par Picard? | Agrégé par Book? |
|---|---|---|---|---|
| CAC / LTV unit economics (Black Bolt) | H1 (deal) | Notion / B2 log | ❌ | ⚠️ si croise LD02 Saru finance |
| Pricing tier T1→T5 (Charles Xavier) | H3 (C-view) | B2 JohnJones log + Notion | ❌ | ❌ |
| Pipeline stage lead→close (Tony Stark + Reed Richards) | H1 (event) | Notion pipeline stages / ClickUp close rate (B2 spec L.23) | ❌ | ⚠️ si Book croise LD01 direct |
| Compliance / data residency (Stephen Strange) | H3 (review) | B2 Aquaman Legal / B3 Ajak | ❌ | ❌ |
| Wholesale channel conflict (Namor) | H3 (Q audit) | B3 Namor + B2 JohnJones log | ❌ | ❌ |
| R&D sales experiments (Reed Richards) | H1 (POC) | Notion + 04_Archives_Data/ sister | ❌ | ❌ |
| External buyer mapping (Charles Xavier) | H1/H3 (CRM) | Hubspot / Notion account pages | ❌ | ❌ |
| Close rate H3 metric (Black Bolt + Xavier) | H3 (quarter) | B2 JohnJones B3 log | ❌ | ⚠️ si Book agrege LD01 P&L |

**Asymétrie fondamentale** : 8/8 dimensions Sales vivent en H1/H3 (deal velocity, pricing drift, pipeline), 0/8 sont capturées par la cadence H10 de Picard.

**Voix Sales Illuminati utilisées** : Black Bolt (3 angles morts), Charles Xavier (3), Reed Richards (2), Tony Stark (1), Stephen Strange (1), Namor (1). Lead = Black Bolt ✓.

### 🎯 3 recommandations canon-coaching pour A3-Book

#### R1 — Ajouter un champ MANIFEST.md optionnel `pricing_tier: T1|T2|T3|T4|T5`

Modification mineure, L+ invariant #1-3 compat. Permet à Charles Xavier B3 de déclarer le pricing tier canon per `ADR-AAAS-PRICING-001`. Picard continue de canoniser, Book peut maintenant agréger la **distribution pricing tier** dans la weekly P&L LD01 (Tier 1 60-70% volume tier per canon, vs Tier 4 $180K ARR — différente famille de métriques).

```yaml
---
project: omk-saas-dashboard
owner: A0 Amadeus
status: active
start_date: 2026-06-15
next_review: 2026-08-25
linked_12wy_rock: 12WY-Q3-2026-rock-03
linked_area: LD01_Business
junction: apps/picard/omk-saas-dashboard
pricing_tier: T3  # NEW — per ADR-AAAS-PRICING-001 5 Tiers canon
unit_econ: green  # NEW — CAC + LTV signed by Black Bolt + Wonder Woman
account_ref: "https://notion.so/ASpace/Acme-Corp-deal-record"  # NEW
---
```

**Sister-canon justification** : `ADR-AAAS-PRICING-001_aaas-pricing-canon.md` RATIFIED 2026-06-24 par A0 Amadeus. Le canon pricing existe, Picard ne le câble pas encore.

#### R2 — Book ouvre une fiche H1 "Sales P&L Delta" qui agrege B3 Illuminati flags

Même cadence que la weekly P&L LD01 actuelle (per `a3-discovery-book.md` spec), mais source = B2 JohnJones `l2_b2_johnjones_sales_<DATE>.md` log + B3 Illuminati sub-feeds. Output : 1 ligne par B3 Illuminati member avec `signal: green|yellow|red` + delta `pricing_tier` + delta `pipeline_stage`. **Ne remplace pas** la fiche P&L LD01, la **complète** par une dimension Sales Pipeline.

C'est l'application directe de `ADR-LD01-008` `loop_engineering_tick` : H1 aggregator reçoit H10 Picard + H10 B2 JohnJones (sister H1 cadence sales ops).

#### R3 — Hook optionnel `picard-manifest-sales-link` qui suggère les champs R1

Sur le pattern de `hooks/posttooluse-test-after-edit.ps1` (PostToolUse Write|Edit|MultiEdit), un hook PostToolUse qui détecte l'écriture d'un nouveau MANIFEST.md et **suggère** (log-only, pas hard-block conformément à `ADR-META-005` Vague 2 Q3 2026) d'ajouter `pricing_tier`, `unit_econ`, `account_ref`. **Pas de hard-block** : c'est une suggestion D7 cost-of-escalation safe.

Sister-suggestion : si l'agent A0 mentionne les mots-clés "sales motion" / "pipeline" / "close" / "go-to-market" dans le Project name, le hook **propose** systématiquement d'ajouter ces 3 champs (log-only Q3 2026 → hard-block candidat Q4 2026 post-L+ Skill Standard).

### ⚠️ Garde-fous L+ Skill Standard

- **Invariant #1 (Frontmatter YAML)** : R1 ajout champ optionnel, OKF v0.1 conformant.
- **Invariant #3 (Append-only strict)** : R1 n'édite pas un MANIFEST.md existant, ne fait qu'ajouter des champs optionnels aux **futurs** MANIFEST. R2 ne touche pas le canon Picard. R3 est log-only.
- **Invariant #5 (D1 receipts)** : chaque recommandation pointe vers un path canon existant (`ADR-AAAS-PRICING-001`, B2 JohnJones log, Notion pipeline pages, `04_Archives_Data/` sister pour R&D POCs).
- **Invariant #6 (Anti-Ultron)** : R3 suggère, ne bloque pas. L'agent reste en lecture seule sur canon par défaut.
- **Invariant #7 (Wager mesurable)** : R2 output = 1 fiche H1/semaine = `ADR-LOOP-003` conformant.
- **Invariant #8 (HITL queue visible)** : les escalades R1.5 (close_health: red) → Discovery + Beth si load=critical OU coherence=extractive.
- **Invariant #9 (Verify-first)** : R1 R2 R3 vérifient que le projet existe avant d'écrire/suggérer quoi que ce soit.

### Anti-paperclip (ADR-SOBER-002 §1)

> *Hard-veto JohnJones (B2 spec L.42) : aucun deal sans CAC + LTV documentés.*
>
> L'angle mort #1 codifie cette doctrine — sans câblage à Picard frontmatter, le hard-veto
> vit en B2/B3 sans hook de blocage. R1 propose le câblage canon. R1 n'active **jamais**
> la veto automatiquement (Posture C + ADR-WARMODE-001 flag-gated) — signal-only Q3 2026,
> promotion hard-block Q4 2026 conditionnée à un A0 HITL séparé.

---

## 3. Routes de fallback

| Si A3-Book rejette R1/R2/R3 | Route alternative | Qui porte |
|---|---|---|
| R1 (champs optionnels) rejeté | B2 JohnJones maintient son log séparé `l2_b2_johnjones_sales_<DATE>.md` + Picard ignore | B2 assume le coût (D7 cost-of-escalation asumed) |
| R2 (fiche Sales P&L) rejeté | Book signale quand même dans la weekly LD01 standard les Sales flags qu'il voit en cross-corrélation (Notion / finance) | Book dojo |
| R3 (hook suggestion) rejeté | Proposition stockée dans `skills_queue.md` (Phase 1 mid-session) jusqu'à activation Phase 2 (Hermes-style end-of-session) | B2 propose, A0 valide |
| R1+R2+R3 tous rejetés | Sister-canon `ADR-AAAS-PRICING-001` reste canon mais sans câblage Picard → Angle morts persistent → Q-over-Q close rate drift silencieuse | B2 JohnJones escalade B1 Jerry gate veto |

---

## 4. Sister-liaisons WF2 (lens partagée avec wargames mêmes-date)

> **Sister lens X-Men (GreenLantern People)** : `handoff_wargame_wf2_b2_greenlantern_people_lens_2026-07-06.md` — angles morts #1 hire-vs-Project race, #4 talent mobility stale owner, #7 Jean Grey mentorship H1 vs H10.
> **Sister lens F4 (Batman Ops)** : `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` — angles morts #2 privacy/PII pre-flight, #5 RTO/RPO + observability, #8 ops-quality F4 co-signature.

**Cross-wargame synthèse** (Sales + People + Ops — 3 lenses wargame WF2) :
- Cadence H10 Picard = **3 fois trop lente** vs H1 ops (People: 8/8 dimensions hors-cadence), H1 sales (Sales: 8/8 dimensions hors-cadence), H3 ops (Ops: 4/4 dimensions partiellement hors-cadence).
- **Asymétrie systémique** : Picard canon = ledger of *projects committed*, pas ledger of *work being done*. Trois dimensions (people, ops, sales) vivent en H1/H3 mais ne se traduisent jamais en H10 MANIFEST update.
- **Common root-cause** (D6 root-cause canon) : le frontmatter Picard (L.50-62) a 7-8 champs, **aucun champs *People, Ops, ou Sales** par construction. Sister-anneau avec Batman lens R1 (ops_review) + GreenLantern lens R1 (people_signal_ref) + cette Sales lens R1 (pricing_tier + unit_econ + account_ref) = **frontmatter enrichi de 3 familles optionnelles**, cohérent avec L+ Skill Standard invariant #1 (frontmatter YAML OKF v0.1 conformant).

**Sister-canon candidate** (à A0 HITL séparer, NOT ratifiée dans cette lens) :
> *« Tout project Picard touchant Sales (go-to-market, pipeline, ICP) exige quadruple co-signature B3 Illuminati : Black Bolt (sovereign/CAC) + Charles Xavier (strategic accounts) + Tony Stark (tech enterprise) + Stephen Strange (international/compliance). »*
>
> Sister-canon possible : `ADR-SALES-PROJECT-GATE-001` (parallèle à `ADR-OPS-PROJECT-GATE-001` sister Batman lens, à ratifier en Q3 2026 cycle 12WY si A0 GO).

---

## 5. D1 receipts (catalogue des sources)

- `C:\Users\amado\.claude\agents\b2-05-johnjones-sales.md` lignes 1-44 (lu intégralement 2026-07-06)
- `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` lignes 1-156 (lu intégralement 2026-07-06)
- `C:\Users\amado\.claude\agents\a3-discovery-book.md` lignes 1-72 (lu intégralement 2026-07-06)
- `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-AAAS-PRICING-001_aaas-pricing-canon.md` lignes 1-201 (lu intégralement 2026-07-06)
- Sister ADRs mentionnés (non relus intégralement, référencés par ancre spec) :
  - `ADR-CANON-001` (roster source of truth)
  - `ADR-SOBER-002 §1` (anti-paperclip CAC/LTV hard-veto)
  - `ADR-INFRA-002` (Repo-Home/Junction)
  - `ADR-INFRA-003` (CEO Dashboard)
  - `ADR-LD01-008` (loop engineering coaching)
  - `ADR-LD01-010` (HA Picard promotion)
  - `ADR-LD01-011` (OMK Nexus BOS PoC)
  - `ADR-AAAS-FINANCE-CANON-001` (CAC/LTV sister canon)
  - `ADR-OBSERVABILITY-001` (D11 lead/lag)
  - `ADR-META-001` (D1-D8)
  - `ADR-META-002` (D9-D12)
  - `ADR-META-005` (hooks automation, Vague 2 Q3 2026)
  - `ADR-LOOP-001/002/003` (verify-first, queues-over-loops, wagers mesurables)
  - L+ Skill Standard ratification 2026-07-05
- Sister wargames WF2 (mêmes-date, lus intégralement) :
  - `handoff_wargame_wf2_b2_greenlantern_people_lens_2026-07-06.md` (X-Men People lens)
  - `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md` (F4 Ops lens)
- Sister B3 Illuminati canon (non relus intégralement cette session, référencés par L.24-30 de B2 spec) :
  - `b3-5-black-bolt.md` — sovereign deals, ferme les deals complexes enterprise
  - `b3-5-tony-stark.md` — tech sales, enterprise accounts, premium-tier
  - `b3-5-reed-richards.md` — R&D sales, innovation pipeline, future-grade
  - `b3-5-namor.md` — wholesale, distribution, deep-blue channel partnerships
  - `b3-5-charles-xavier.md` — strategic accounts, mentalist-grade buyer mapping, X-Men overlap
  - `b3-5-stephen-strange.md` — international, mystic deals, sovereign-nation-tier

## 6. Anti-patterns protégés (D4 + L+ invariants)

- ❌ Ne pas muter les agents canon (B2/B3 Illuminati, A3 Picard, A3 Book) — append-only spec (L+ invariant #3)
- ❌ Ne pas inventer de chiffre (D1 anti-paresse, MEMORY.md §"Anti-pattern extraction 209 sessions")
- ❌ Ne pas créer de doublon agent (L+ invariant #2 type top-level)
- ❌ Ne pas activer de cron sans HITL A0 (Posture C + ADR-WARMODE-001 flag-gated)
- ❌ Ne pas escalader à A0 mid-research (D7 cost-of-escalation)
- ❌ Ne pas proposer de hard-block R3 sans A0 HITL séparé (Posture C, gate ADR-SOBER-002 §6)
- ❌ Ne pas assumer que R1/R2/R3 sera ratifié (proposal-only, signal diagnostique, pas modification du canon)

---

## 7. Sister wargame nexuses (live, mêmes-date 2026-07-06)

- **`handoff_wargame_wf2_b2_greenlantern_people_lens_2026-07-06.md`** — 8 angles People (X-Men squad), 3 recommandations canon-coaching pour A3-Book (people_signal_ref optionnel, People P&L Delta, hook suggestion).
- **`handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md`** — 8 angles Ops (F4 squad), 3 recommandations canon-coaching pour A3-Book (ops_review H3 aligné, ops_quality F4 co-signature, `ADR-OPS-PROJECT-GATE-001` candidate).
- **Cette lens** : 8 angles Sales (Illuminati squad), 3 recommandations canon-coaching pour A3-Book (pricing_tier + unit_econ + account_ref optionnels, Sales P&L Delta, hook suggestion), `ADR-SALES-PROJECT-GATE-001` candidate sister.

**Cross-lens convergence** : 24 angles morts catalogés par 3 B2 sisters (People 8 + Ops 8 + Sales 8). Asymétrie systémique = cadence H10 Picard vs cadence H1/H3 B2 squads. Proposition canon partagée = enrichir frontmatter Picard de **3 familles optionnelles** : `people_signal_ref` (X-Men), `ops_review` + `tier` + `oncall` (F4), `pricing_tier` + `unit_econ` + `account_ref` (Illuminati). **Single doctrine root-cause** = frontmatter canon manque les dimensions ops/people/sales par construction (D6 root-cause canon).

---

**🔍 B2 JohnJones Sales — 2026-07-06, lens wargame WF2 Sister-de-Batman (Ops) + GreenLantern (People). Aucune ligne n'écrit dans un canon sans A0 GO (per ADR-SOBER-002 §1 + §6). Le présent fichier est un signal diagnostique, pas une modification du canon.**

8 angles morts catalogués (5-10 range ✓), 3 recommandations canon-coaching pour A3-Book, 8/8 dimensions Sales identifiées comme hors-cadence Picard H10, 0 chiffre inventé, sources canon paths absolus, L+ invariants respectés. Cross-lens convergence avec 2 sister wargames mêmes-date (24 angles totaux, single root-cause = frontmatter canon Picard).

Handoff canonique : `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_wargame_wf2_b2_johnjones_sales_lens_2026-07-06.md`
