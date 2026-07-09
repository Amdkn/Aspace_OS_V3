---
handoff: wargame_wf2_b2_wonderwoman_finance_lens
date: 2026-07-06
workflow: WF2 (A3 Picard captain USS Enterprise)
lens: B2-07-WonderWoman-Finance (Thunderbolts squad)
coaching_target: A3-Book (H1 aggregator) + A3-Saru (LD02 H3 finance guard)
wargame_author: b2-07-wonderwoman-finance
status: live
doctrine_anchors:
  - ADR-CANON-001 (roster source of truth)
  - ADR-SOBER-002 §1 + §3 + §5 (anti-paperclip CAC/LTV + opex<15%MR + H3 quarterly runway hard-stop)
  - ADR-AAAS-FINANCE-CANON-001 (5 Piliers AaaS Finance RATIFIED 2026-06-24)
  - ADR-AAAS-PRICING-001 (5 Tiers USD AaaS Pricing canon RATIFIED 2026-06-24)
  - ADR-OBSERVABILITY-001 (D11 lead/lag RATIFIED 2026-07-06 — Tier 3 batch)
  - ADR-LLM-COST-COMPARE-001 (Token Plan canon 80% D1-verified 2026-07-04)
  - ADR-INFRA-002 (Repo-Home/Junction)
  - ADR-INFRA-003 (CEO Dashboard Matryoshka)
  - ADR-LD01-008 (loop engineering coaching H10 → H1 aggregator)
  - ADR-LD01-010 (HA Picard promotion 2026-07-05)
  - ADR-LD01-011 (OMK Nexus BOS PoC RATIFIED 2026-07-05)
  - L+ Skill Standard 2026-07-05 ratification (10 invariants)
  - plan-L2-business-os.md §13.5 (Pricing en travail ⚠️ D4 — non ratifié, $1.2M ARR gated)
  - ADR-META-006 D6 catalog (append-only)
sister_squad: B3 Thunderbolts — Bucky Barnes (lead, Saru H3 quarterly runway) · Yelena Belova (sharp pricing, unit econ) · Red Guardian (heavy capex, soviet-tier reserves) · Ghost (intangible assets, phase-shift accounting) · Taskmaster (CAC mirroring LTV, anti-pattern billing) · U.S. Agent (compliance-grade finance, audit trails)
sister_wargames_wf2:
  - handoff_wargame_wf2_b2_greenlantern_people_lens_2026-07-06.md (X-Men lens)
  - handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md (F4 lens)
  - handoff_wargame_wf2_b2_johnjones_sales_lens_2026-07-06.md (Illuminati lens, CAC/LTV sister canon)
  - handoff_wargame_wf2_b2_cyborg_it_lens_2026-07-06.md (Kang lens, infra cost sister)
  - handoff_wargame_wf2_b1_jerry_lens_2026-07-06.md (B1 SYSTEMIZE gate)
  - handoff_wargame_wf2_b1_summers_lens_2026-07-06.md (B1 SHIP gate)
---

# 👸 Wargame WF2 — Lens B2-WonderWoman-Finance (Thunderbolts squad)

> **Lecture** : 5-10 angles morts où **A3 Picard** (Projects Captain, H10, MANIFEST.md
> enforcer, classify gate 3 questions) supervise ailleurs pendant que les dynamics
> **Finance / Runway / Unit Economics / LTV:CAC / Compliance** vivent, dérivent, ou
> s'effondrent en silence pendant le 12WY cycle Q3 2026 (06/15 → 09/07).
>
> **Méthode Fable appliquée à chaque angle mort** :
> - **Action** : ce que Picard fait (sa porte d'entrée canon = 3-gate + MANIFEST.md frontmatter)
> - **Réaction** : ce que Finance vit pendant ce temps (Thunderbolts squad voices)
> - **Contre** : ce que B2 WonderWoman tente pour compenser (hard-veto Saru H3 quarterly + ADR-SOBER-002 §5)
> - **Failure** : pourquoi la compensation échoue (asymétrie de cadence H10 vs H3, doctrine, ou pouvoir)
> - **Abort** : déclencheur qui force A3-Book (H1 aggregator) ou A3-Saru (LD02 H3 guard) à monter le signal
>
> **Posture** : cette liste est volontairement hostile — chaque angle est un scénario où le
> canon Picard actuel laisse A0 dans le noir côté Finance. Aucune ligne n'invente de chiffre ;
> toutes les références citent un fichier canon D1-verified.

**Sources canon lues (paths absolus)** :
- `C:\Users\amado\.claude\agents\b2-07-wonderwoman-finance.md` (B2 Finance self — lu intégralement)
- `C:\Users\amado\.claude\agents\b3-7-bucky-barnes.md` (Lead Thunderbolts — Saru H3 quarterly runway)
- `C:\Users\amado\.claude\agents\b3-7-yelena-belova.md` (sharp pricing / unit econ)
- `C:\Users\amado\.claude\agents\b3-7-red-guardian.md` (heavy capex / infra-grade budgeting)
- `C:\Users\amado\.claude\agents\b3-7-ghost.md` (intangible assets / phase-shift accounting)
- `C:\Users\amado\.claude\agents\b3-7-taskmaster.md` (CAC mirroring LTV)
- `C:\Users\amado\.claude\agents\b3-7-us-agent.md` (compliance-grade / audit trails)
- `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` (A3 supervised — lu intégralement)
- `C:\Users\amado\.claude\agents\a3-discovery-book.md` (A3 H1 aggregator MC — lu intégralement)
- `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-AAAS-FINANCE-CANON-001_aaas-finance-canon.md` (5 Piliers RATIFIED 2026-06-24 — lu intégralement)
- `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-AAAS-PRICING-001_aaas-pricing-canon.md` (5 Tiers USD RATIFIED 2026-06-24 — lu intégralement)
- `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-OBSERVABILITY-001_d11-lead-lag.md` (D11 lead/lag RATIFIED 2026-07-06 — Tier 3 batch)
- `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L0_Tech_OS\ADR-LLM-COST-COMPARE-001_minimax-anthropic-openrouter.md` (Token Plan canon — lu intégralement)
- `C:\Users\amado\.claude\plans\plan-L2-business-os.md` §13.5 l.487-489 (Pricing $1000×100 NON RATIFIÉ — lu intégralement)

**Chiffres canon sister (D1 receipts, citation verbatim)** :
- **MEMORY.md §"ADR-LLM-COST-COMPARE-001 DATA ACTUALIZED 80% 2026-07-04"** : *"38.11M tokens/jour · 772.20M tokens/7j · 3.85B tokens/30j · $50/mois pour ~5.1B tokens (Token Plan A0)"*
- **ADR-OBSERVABILITY-001 §8** : *"Pricing cible L2 §13.5 = $1000/mois ×100 = $1.2M ARR"*
- **ADR-AAAS-PRICING-001 §Décision** : T1 PME Solo Founder $300-500/an · T2 $500-1000/an · T3 PME Groupe $4000-5000/an · T4 Nexus mid-market $15K MRR=$180K ARR · T5 Orbiter Enterprise $50K MRR baseline → $500K Year 10
- **plan-L2-business-os.md §13.5 l.487-489** : *"Hypothèse A0 : 1 000 $/mois × 100 clients Premium = 1,2 M ARR (« Million de Libération ») avec ancre 5 000 $ — ⚠️ D4 — non ratifié — À confronter à ADR-AAAS-PRICING-001 (RATIFIÉ) avant toute ratification — si conflit : ADR neuf qui supersede, jamais d'édit de l'immuable."*

---

## 0. Picard — Porte d'entrée canon (rappel D1)

Picard supervise à travers **3 gates + MANIFEST.md frontmatter** (spec `a3-enterprise-picard.md` lignes 39-63) :

1. **3-question gate** (L.40-44) : deadline ? goal-bounded ? owner+next_review ?
2. **MANIFEST.md frontmatter** (L.50-62) : 8 champs = `project`, `owner`, `status`, `start_date`, `next_review`, `linked_12wy_rock`, `linked_area`, `junction`
3. **Cadence H10** : produit MANIFEST.md par cycle 12WY (10 semaines), agrégé par A3-Book en H1 hebdo
4. **Doctrine** : D1 verify-before-write, D4 append-only strict, D6 bucket-ambiguity, D7 batch-create, D11 metric (active Projects/quarter, target 1-3, anti-pattern >10)

**Ce que Picard NE regarde PAS** (par construction, sister au wargame sister GreenLantern / Batman Ops / JohnJones Sales / Cyborg IT) :
- Le **coût opérationnel** du Project (opex, infra cost, M3 token burn, Vercel/Supabase seats)
- La **cadence Finance** : Saru H3 = quarterly (13 sem.), Picard H10 = 10 sem. → **3 sem. de blackout** où un Project peut faire dériver le runway sans gate
- Le **pricing tier implications** : Sister canon `ADR-AAAS-PRICING-001` 5 Tiers T1-T5 USD + plan L2 §13.5 NON RATIFIÉ (conflit latent)
- Les **unit economics** (CAC, LTV, payback period, LTV:CAC ratio) — pas de frontmatter pour ça
- La **compliance Finance** (AI-Act 2026-08-02 driver, audit trails, opex<15%MR per ADR-SOBER-002 §3)
- Le **CAC mirroring LTV** (Taskmaster anti-pattern billing) — aucun signal dans MANIFEST.md
- La **valeur intangible** construite (brand equity, data flywheel, customer trust, Pilier 4 sister canon)

**Spécificité Finance lens** : B2 WonderWoman spec L.40 + L.41 = *"H3 quarterly runway review (mandatory, sister ADR-SOBER-002 §D5 anti-paperclip)"* + *"Hard-veto sur tout greenwashing pricing (sister ADR-AAAS-PRICING-001 + ADR-SOBER-002)"*. Mais le hard-veto porte sur la **canonisation Finance** (runway trimestriel, pricing canon), pas sur la canonisation Picard Projects. Asymétrie structurelle = angle mort fondateur Finance (sister symétrique aux angles Sales / People / Ops).

**Token Plan run-rate sister canon (D1-verified)** :
- 38.11M tokens/jour = 1.14B tokens/30j si projet = full-time Picard-like usage
- Quota = 5.1B/30j → 22.4% du quota par 1 Project Picard H10 full-time. **3 Projects simultanés = 67.1% du quota = quasi-exhaustion**
- Pricing cible canon = $1.2M ARR (plan L2 §13.5 NON RATIFIÉ, gated A0). Runway Token Plan A0 = **coût dominant** (ADR-META-002 D9.4)

---

## 1. Angles morts catalogués (8 — pattern Fable)

### 🔴 Angle mort #1 — H3 quarterly runway vs H10 10-week tick : 3 semaines de blackout (Bucky Barnes)

> **Domaine B3** : Bucky Barnes (lead — Saru H3 quarterly runway, dark ops, winter-grade resilience)

| Champ | Contenu |
|---|---|
| **Action** | A0 lance un Project (par ex. `00-omk-nexus-landing-page`). Picard engage le 3-question gate (L.40-44) : deadline ? goal-bounded ? owner+next_review ? → 3/3 oui → Project canonisé + MANIFEST.md écrit + junction `apps/<role>/` créée per ADR-INFRA-002. |
| **Réaction** | Bucky Barnes (B3 lead) doit normalement hard-veter le Project sur le runway trimestriel **avant** canonisation, per B2 spec L.40 + ADR-SOBER-002 §5 : *Saru H3 quarterly runway review mandatory*. |
| **Contre** | B2 WonderWoman tente la compensation via Saru (LD02 H3, sister `a3-discovery-saru.md`) : *"Invoke when A0 says 'runway check' / 'budget review' / 'am I scared of money'"*. Mais le **gate Picard** est **temporellement désaligné** : Picard H10 = 10 sem., Saru H3 = 13 sem. (quarterly). À chaque tick Picard H10, Saru est en milieu de trimestre ou en transition. **3 sem. de blackout** (W10→W13) où un Project peut faire dériver le runway trimestre sans gate. |
| **Failure** | Picard MANIFEST.md frontmatter (L.50-62) = **8 champs**. **Aucun** : `linked_finance_quarter` (Saru H3 anchor), `next_finance_review` (date sync Saru), `runway_impact_h3` (delta runway estimé), `token_budget_envelope` (M3 spend cap). Picard ne sait pas quand Saru va reviewer, et Saru ne sait pas que Picard a canonisé un Project brûleur de runway. **Asymétrie de cadence = drift silencieuse**. |
| **Abort** | Anomaly détectée par **A3-Saru** (LD02 H3 quarterly guard) lors de son weekly Drift Report (Zora auto-call vendredi 18:00) : biz-vs-finance drift → escalade **A1 Beth (Veto)** + flag **A2 Discovery**. Délai = 1-3 sem. avant correction. |

**D1 receipt** : `a3-enterprise-picard.md` L.50-62 (frontmatter 8 champs) + `a3-discovery-saru.md` description (H3 quarterly) + `b2-07-wonderwoman-finance.md` L.40 (H3 mandatory). Sister canon divergence : H10 ≠ H3 sans jonction calendaire.

---

### 🔴 Angle mort #2 — Pricing canon conflict : ADR-AAAS-PRICING-001 RATIFIED vs plan L2 §13.5 NON RATIFIÉ (Yelena Belova)

> **Domaine B3** : Yelena Belova (sharp pricing, sharp shooter-grade unit econ)

| Champ | Contenu |
|---|---|
| **Action** | A0 lance un Project qui **bêt sur pricing** (par ex. *"Million de Libération landing page"* avec pricing cible $1.000/mois × 100 clients = $1.2M ARR). Picard canonise : MANIFEST.md écrit, junction créée. **Aucune confrontation avec ADR canon Pricing**. |
| **Réaction** | Yelena Belova (B3) doit normalement hard-veter sur **pricing canon** sister `ADR-AAAS-PRICING-001` (5 Tiers USD T1-T5 RATIFIED 2026-06-24) **avant** canonisation. Mais Picard ne consulte pas ADR-AAAS-PRICING-001 dans son 3-gate ni dans son MANIFEST.md frontmatter. |
| **Contre** | B2 WonderWoman tente la compensation via Yelena + sister canon `ADR-AAAS-PRICING-001` (lu intégralement). Yelena vérifie le pricing tier (T1 $300-500/an · T2 $500-1000/an · T3 $4000-5000/an · T4 $15K MRR=$180K ARR · T5 $50K MRR baseline). Si Picard crée un Project avec pricing hors-tier, Yelena signale. **MAIS** : plan L2 §13.5 (lu l.487-489) = hypothèse A0 $1.000/mois × 100 clients Premium = $1.2M ARR, **explicitement marqué "⚠️ D4 — non ratifié"** et **"À confronter à ADR-AAAS-PRICING-001 (RATIFIÉ) avant toute ratification — si conflit : ADR neuf qui supersede, jamais d'édit de l'immuable."** |
| **Failure** | **Conflit canon latent non-flaggé par Picard** : $1.000/mois × 12 = $12.000/an/client. Sister canon ADR-AAAS-PRICING-001 : T4 Nexus mid-market = $15K MRR = $180K ARR (donc $15K/mois = $180K/an par client). $1.000/mois = **entre T3 ($4-5K/an)** et **T4 ($180K/an)** = aucun tier canon matche. Picard crée Project sans confrontation. ADR-AAAS-PRICING-001 = immuable (Regle d'Or #3) ; plan L2 §13.5 = "ADR neuf qui supersede" requis. **Canon immuable vs canon hypothèse non-ratifié = bombe à retardement**. |
| **Abort** | A1 Beth (Veto) détecte la divergence lors d'une revue canon (12WY quarterly review) → escalade A0 pour trancher (ratifier ADR neuf, ou rejeter $1000/mois hypothèse). D7 cost-of-escalation = très élevé (~100×) sur ce type de décision canon. |

**D1 receipts** : `ADR-AAAS-PRICING-001` §Décision T1-T5 USD + `plan-L2-business-os.md` l.487-489 ⚠️ D4 non ratifié + `a3-enterprise-picard.md` L.50-62 (frontmatter 8 champs, aucun `pricing_tier` ni `unit_econ_target`).

---

### 🔴 Angle mort #3 — Token Plan capex : M3 burn par Project non-comptabilisé (Red Guardian)

> **Domaine B3** : Red Guardian (heavy capex, infra-grade budgeting, soviet-tier reserves)

| Champ | Contenu |
|---|---|
| **Action** | A0 lance un Project *tech* (par ex. un sub-agent Symphony `shadow-l0-omnigent` ou une skill auto-research canon-batch-spawn). Picard canonise → MANIFEST.md + junction `apps/<role>/`. **Aucune estimation du M3 token burn** sur le cycle H10. |
| **Réaction** | Red Guardian (B3) doit normalement hard-veter sur **capex infra**, sister canon **MiniMax Token Plan A0** ($50/mois pour ~5.1B tokens, **usage actuel 3.85B/30j = 75.5% du quota**, citation verbatim `MEMORY.md §ADR-LLM-COST-COMPARE-001 DATA ACTUALIZED 80% 2026-07-04`). À run-rate actuel, A0 quota Token Plan = **exhausted 3-5 jours dans le mois suivant** (sister D1 screenshot A0 2026-07-04). |
| **Contre** | B2 WonderWoman tente la compensation via Red Guardian + **ADR-SOBER-002 §3 hard-stop** : *"opex < 15% MR"*. Red Guardian calcule : si MR cible = $1.2M ARR (plan L2 §13.5 NON RATIFIÉ), opex max = $180K/an = $15K/mois. **Token Plan actuel $50/mois** = 0.33% MR, donc conforme §3. MAIS si A0 ajoute 2-3 Projects Picard H10 full-time M3 = burn additionnel ~2-3B tokens/30j = $25-37/mois extra (extrapolation D1 OpenRouter pricing $0.30/$1.20/M MiniMax-M3), **toujours <15% MR**. Ce n'est pas le risque. |
| **Failure** | **Risque réel = quota exhaustion, pas dollar opex** : 3.85B/30j + 2.5B burn additionnel = 6.35B > 5.1B quota = **plan capé ou recharge required**. Picard ne track pas le quota. Sister canon `ADR-LLM-COST-COMPARE-001` §"Plan d'actualisation" ligne 197-203 : *"Restore pricing Anthropic API direct (gated A0)"*. Le quota gate n'existe nulle part dans le canon Picard. **Picard peut canoniser un Project qui épuise le quota Token Plan d'A0 mid-cycle**, forçant un cut-over OpenRouter ($0.30/$1.20/M) ou pire un downgrade Fable-5 ($10/$50/M OpenRouter premium, x33-42 vs Token Plan inclus). |
| **Abort** | A3-Book (H1 aggregator MC) voit le burn rate M3 dériver dans sa fiche P&L hebdo (sister `a3-discovery-book.md` §1 Biz Telemetry Pull). Délai = 1 semaine. Escalade A0 si >15% drift. ADR-SOBER-002 §3 trigger fire. |

**D1 receipts** : `MEMORY.md §ADR-LLM-COST-COMPARE-001 DATA ACTUALIZED 80% 2026-07-04` (38.11M/jour · 772.20M/7j · 3.85B/30j · 75.5% quota) + `ADR-LLM-COST-COMPARE-001` §"TABLEAU COMPARATIF" ligne 95-115 (OpenRouter MiniMax-M3 $0.30/$1.20/M, Fable 5 $10/$50/M premium) + `ADR-SOBER-002 §3` (opex < 15% MR) + `a3-enterprise-picard.md` L.50-62 (frontmatter 8 champs, aucun `token_budget_envelope` ni `infra_cost_runway`).

---

### 🔴 Angle mort #4 — Intangible assets invisibles : brand equity, data flywheel, customer trust (Ghost)

> **Domaine B3** : Ghost (intangible assets, opacity ops, phase-shift accounting)

| Champ | Contenu |
|---|---|
| **Action** | Picard crée un Project `00-omk-nexus-landing-page` (D1 receipt : `wiki/hand_offs/omk_nexus_phase_a_RETARGET_coach_first_2026-06-27.md` + Vercel deploy `prj_NHtCekTiJeMEYfKdapwIzF4I8K2a` status READY PROMOTED). MANIFEST.md écrit. Project "delivered". |
| **Réaction** | Ghost (B3) doit normalement tagger le Project comme **intangible asset builder**, sister canon **Pilier 4 ADR-AAAS-FINANCE-CANON-001** : *"AI-Native Business Operating System — Customer Interaction Data Loop: capturing touchpoints as structured data"*. Sister canon **Pilier 5** : *"Scalabilite sans Inertie: zero friction RH, iteration quasi-instantanee"*. |
| **Contre** | B2 WonderWoman tente la compensation via Ghost + ADR-OBSERVABILITY-001 (D11 lead/lag RATIFIED 2026-07-06). 5 LEAD metrics (Time-to-A0, Scroll-depth, CTA hover, Hero dwell, Section engagement) + 5 LAG metrics (Signups, Conversion, Bounce, Retention, Affiliation 20% Stripe Connect Medvi). **Mesure de l'intangible créé** (brand trust, data flywheel) **n'est pas dans le canon Picard MANIFEST.md**. |
| **Failure** | **Asymétrie : ce qui est LIVRÉ ≠ ce qui est COMPTABILISÉ**. Picard livre `00-omk-nexus-landing-page` (200 OK Vercel), mais sister canon **Pilier 4 ADR-AAAS-FINANCE-CANON-001** dit : *"the value of the enterprise is no longer in the number of employees, but in the founder's capacity to orchestrate AIs"*. Sister Pilier 5 : *"Idempotence du Pipeline: meme architecture 1 ou 250 000 clients"*. **Le pipeline est l'asset, pas le landing page**. Picard MANIFEST.md ne loggue ni le pipeline réutilisable (skill canon-batch-spawn, Karpathy swarm), ni la brand equity construite (3 ICP sister-symétrique Solarismme/Nexus/Orbiter reconnue), ni le data flywheel (customer touchpoints structured data per Pilier 4). **Comptabilité intangible = opacity ops**. |
| **Abort** | Quarterly review 12WY (gate trimestriel). Si A0 demande *"combien vaut mon runway intangible ?"*, Ghost remonte qu'aucun frontmatter ne track l'asset. Délai = 1 trimestre avant détection. |

**D1 receipts** : `ADR-AAAS-FINANCE-CANON-001` Pilier 4 (Customer Interaction Data Loop) + Pilier 5 (Scalabilite sans Inertie, Idempotence du Pipeline) + `ADR-OBSERVABILITY-001` §4 + §5 (5 LEAD + 5 LAG) + `a3-enterprise-picard.md` L.50-62 (frontmatter 8 champs, aucun `intangible_asset_log` ni `data_flywheel_counter`).

---

### 🔴 Angle mort #5 — CAC:LTV absent du gate Picard, D11 anti-pattern non-flaggé (Taskmaster)

> **Domaine B3** : Taskmaster (CAC mirroring, copy-grade LTV, anti-pattern billing)

| Champ | Contenu |
|---|---|

| **Action** | A0 lance un Project *GTM* (par ex. *Quiz de diagnostic pattern Medvi*, sister `plan-L2-business-os.md` l.485 §13.4 item 3 machine d'acquisition). Picard canonise : 3-gate OK, MANIFEST.md écrit, junction `apps/role/quiz-medvi`. **Aucun frontmatter pour CAC cible ou LTV cible**. |
| **Réaction** | Taskmaster (B3) doit normalement hard-veter sur **CAC:LTV ratio**, sister canon **Pilier 2 ADR-AAAS-FINANCE-CANON-001** : *"LTV:CAC>=3:1 via acquisition doctrine"*. Sister canon **Pilier 3** : *"P&L-Coupled Selling: chaque pitch lie a sales/gross margin/labor chiffres"*. |
| **Contre** | B2 WonderWoman tente la compensation via Taskmaster + sister **ADR-SOBER-002 §1** : *"hard-stop sur tout deal sans CAC + LTV documentés"*. Mais §1 porte sur les **deals B2B Sales**, pas sur les **Projects Picard**. Asymétrie sister au wargame JohnJones Sales lens. |
| **Failure** | **Asymétrie D11 doctrine** : `ADR-OBSERVABILITY-001` §4 LEAD metric 4.3 (CTA hover rate) + §5.5 (Affiliation 20% Stripe Connect Medvi loop) = métriques D11 mesurables MAIS **uniquement pour landing pages OMK Nexus canon**. Sister plan L2 §13.5 cible $1.2M ARR avec ancre $5000. Si Picard canonise un Project Quiz Medvi sans frontmatter `cac_target` ni `ltv_target`, **le CAC mirror ne peut pas être mesuré** (Taskmaster n'a pas le baseline), et l'arbitrage billing (Taskmaster) ne peut pas flagger le drift. **D11 anti-pattern = lead sans fenêtre temporelle d'observation** (sister `ADR-OBSERVABILITY-001` §3). |
| **Abort** | A2 Discovery Zora auto-call weekly Drift Report vendredi 18:00 (sister `a3-discovery-book.md` §Triggers). Si `LD01_Business/00_DOMAIN_MEMORY.md` montre drift LD01 vs LD02 (Saru H3), escalade A1 Beth. Délai = 1 semaine. |

**D1 receipts** : `ADR-AAAS-FINANCE-CANON-001` Pilier 2 (LTV:CAC>=3:1) + Pilier 3 (P&L-Coupled Selling) + `ADR-SOBER-002 §1` (CAC/LTV hard-stop deals) + `ADR-OBSERVABILITY-001` §3 (anti-pattern D11 lead sans fenêtre) + `a3-enterprise-picard.md` L.50-62 (frontmatter 8 champs, aucun `cac_target` ni `ltv_target`).

---

### 🔴 Angle mort #6 — AI-Act 2026-08-02 compliance audit trail absent (U.S. Agent)

> **Domaine B3** : U.S. Agent (compliance-grade finance, audit trails, hard law)

| Champ | Contenu |
|---|---|
| **Action** | A0 lance un Project impliquant de l'IA générative (par ex. `shadow-l2-mirofish` sister plan L2 §13.6 l.493, ou `omk_nexus_phase_a` deploy, ou toute skill auto-research canon-batch-spawn). Picard canonise → MANIFEST.md écrit. **Aucun frontmatter pour compliance audit trail AI-Act 2026-08-02**. |
| **Réaction** | U.S. Agent (B3) doit normalement hard-veter sur **compliance-grade finance**, sister canon driver **AI-Act 2026-08-02** (sister B2-08-Aquaman-Legal spec + `ADR-CANON-001` AI-Act 2026-08-02 driver). Sister canon **Pilier 5 ADR-AAAS-FINANCE-CANON-001** : *"Pivot de Legalisation: IA conquiert, humain pacifie et legitime"*. |
| **Contre** | B2 WonderWoman tente la compensation via U.S. Agent + **L+ Skill Standard invariant #6** (sister `a3-enterprise-picard.md` L.121) : *"Anti-Ultron check : lecture seule par defaut sur canon, ecriture gatee par MANIFEST.md"*. Mais l'invariant #6 porte sur l'**écriture canon**, pas sur l'**audit trail compliance**. |
| **Failure** | **Drift compliance post-deploy** : si Picard canonise un Project IA (par ex. skill auto-research canon-batch-spawn, sister `skills/canon-batch-spawn/SKILL.md`), aucun frontmatter ne porte `ai_act_compliance_status`, `gdpr_audit_trail`, `data_residency`, `model_disclosure`. Sister `ADR-AAAS-FINANCE-CANON-001` §"Consequences Negatives" ligne 172 : *"AI-Act 2026-08-02 driver legal : conformite by-design 6 semaines anticipe"*. **Aujourd'hui = 2026-07-06 → 27 jours avant deadline**. Aucun gate Picard pour ce driver. **B2 Aquaman Legal (Eternals B3) catch-up post-mortem** = costly retro-fit sister plan L2 §13.4 item 2 (gap IAM/Logs = CLOS Supabase natif mais **uniquement pour OMK PoC**, pas pour Projects Picard génériques). |
| **Abort** | Sister **`b2-08-aquaman-legal`** (Eternals squad, Ikaris lead AI-Act 2026-08-02) intercepte lors d'une revue cross-B2 12WY. Délai = variable, escalade A0 si Project ship d'ici 2026-08-02 détecté sans audit trail. |

**D1 receipts** : `ADR-CANON-001` (AI-Act 2026-08-02 driver) + `ADR-AAAS-FINANCE-CANON-001` §"Consequences Negatives" ligne 172 (conformite by-design 6 sem. anticipe) + `a3-enterprise-picard.md` L.121 (L+ invariant #6 Anti-Ultron) + L.50-62 (frontmatter 8 champs, aucun `ai_act_compliance_status`).

---

### 🔴 Angle mort #7 — D7 cost-of-escalation jamais tracé : Picard escalade-Beth silencieuse (Bucky Barnes depth)

> **Domaine B3** : Bucky Barnes (lead — Saru H3 quarterly runway + dark ops + winter-grade resilience)

| Champ | Contenu |
|---|---|
| **Action** | Picard canonise Project. 3-gate répond *non* à une des 3 questions (par ex. *"ce Project n'a pas de next_review date claire"*). Per spec L.43 : *"No → A0 escalation, D7"*. Picard escalade silencieusement à A0 via chat. **Aucun log structuré**. |
| **Réaction** | Bucky Barnes (B3 lead) doit normalement hard-veter sur **D7 cost-of-escalation** (~100× par erreur), sister canon **CLAUDE.md §"Doctrine Anti-Paresse"** + **ADR-META-001 D7**. Sister canon **L+ Skill Standard invariant #5** (sister `a3-enterprise-picard.md` L.120) : *"D1 receipts : toute action produit une sortie chiffree (commande -> output documente)"*. |
| **Contre** | B2 WonderWoman tente la compensation via Bucky + D7 doctrine. Mais D7 porte sur les **escalades vers A0**, pas sur les **escalades Picard silencieuses**. Sister canon **Anti-Ultron invariant #6** : lecture seule par défaut sur canon. **Conflit silencieux** : Picard escalate pour D7 protection A0, mais l'escalade elle-même = D7 violation (coût caché). |
| **Failure** | **D6 root cause (sister `ADR-META-006` catalog)** : la vraie root cause est *"3-gate ambigüe"* (sister Picard spec L.43 *"Si 3/3 yes: target path = ..."*). Plutôt qu'escalader A0, Picard devrait **rejeter le Project vers Spock (Areas)** ou **clarifier avec A0** (1 question, faible coût). L'escalade D7 = anti-pattern bureaucratique. **Aucun champ MANIFEST.md** ne loggue *"escalade_history"* ou *"d7_cost_actual"*. |
| **Abort** | Sister **`hooks/PostToolUse-test-after-edit.ps1`** (sister `CLAUDE.md §Hooks doctrine`) log-only, ne hard-block pas. Sister **SessionStart smart-read hook** (`hooks/sessionstart-log-digest.ps1`) catch-up post-hoc. Délai = end-of-session ou next-session start. Pas de catch-up mid-cycle. |

**D1 receipts** : `a3-enterprise-picard.md` L.43 (D7 escalade) + L.120 (L+ invariant #5 D1 receipts) + `CLAUDE.md §"Doctrine Anti-Paresse D7"` + `ADR-META-006` (D6 catalog append-only).

---

### 🔴 Angle mort #8 — Anti-Paperclip §3 opex<15%MR pas auto-vérifié sur Projects Picard (Red Guardian depth)

> **Domaine B3** : Red Guardian (heavy capex + soviet-tier reserves + infra-grade budgeting)

| Champ | Contenu |
|---|---|
| **Action** | Picard canonise Project avec junction `apps/<role>/<home>` (sister `ADR-INFRA-002`). Junction déclenche **création d'un repo + infra** (Vercel deploy + Supabase schema + MCP servers). **Aucun calcul d'opex MR delta** sur MR cible = $1.2M ARR (plan L2 §13.5 NON RATIFIÉ). |
| **Réaction** | Red Guardian (B3) doit normalement hard-veter sur **opex<15%MR per ADR-SOBER-002 §3**. Sister canon `ADR-AAAS-FINANCE-CANON-001` Pilier 3 Vori : *"opex operationnels <15% MR via paiements (60% revenu) en system of transaction, LTV:CAC implicit >=3:1"*. |
| **Contre** | B2 WonderWoman tente la compensation via Red Guardian + D7 cost-of-escalation §3 + Pilier 3 Vori sister canon. Mais §3 porte sur les **ADR-architectures (Pilier 3 Vori = architecture tier)**, pas sur les **Projects Picard individuels**. Asymétrie sister au angle mort #3 (Token Plan capex). |
| **Failure** | **Dérive opex invisible** : si 5 Projects Picard génèrent chacun ~$500/mois opex (Vercel + Supabase + MCP + tooling) = $2.5K/mois = $30K/an. Sur MR $1.2M = **2.5% MR** (sous le seuil 15%, OK §3). MAIS sur MR **early-stage** Tier 1-3 ($300-5000/an par client × 100 clients = $30K-500K MR) = opex 5 Projects = 6-100% MR. **§3 violation silencieuse** quand MR < MR cible. **Aucun frontmatter Picard** ne porte `opex_mr_ratio` ou `runway_remaining_h3`. |
| **Abort** | Quarterly review 12WY (Saru H3, sister `a3-discovery-saru.md`). Si §3 violation détectée, A1 Morty veto + A1 Beth audit mensuel (sister `ADR-AAAS-FINANCE-CANON-001` §"Mitigation" ligne 178-182). Délai = 1 trimestre. |

**D1 receipts** : `ADR-SOBER-002 §3` (opex<15%MR hard-stop) + `ADR-AAAS-FINANCE-CANON-001` Pilier 3 (Vori 60% revenu paiements) + `ADR-AAAS-FINANCE-CANON-001` §"Mitigation" ligne 178-182 (A1 Morty veto + A1 Beth audit mensuel) + `a3-enterprise-picard.md` L.50-62 (frontmatter 8 champs, aucun `opex_mr_ratio`).

---

## 2. Synthèse — Diagnostic lens B2 WonderWoman Finance sur A3 Picard

**Verdict Finance lens** : A3 Picard canonise Projects avec **MANIFEST.md 8 champs** (`project`, `owner`, `status`, `start_date`, `next_review`, `linked_12wy_rock`, `linked_area`, `junction`). **Aucun des 8 champs n'est Finance-relevant**. Conséquence : **6 dynamiques Finance** vivent en dehors du gate Picard, compensées uniquement par les hard-vetos B3 Thunderbolts post-canonisation, avec délais de détection = 1 sem. (D11 weekly Drift Report) à 1 trimestre (Saru H3 quarterly).

### 2.1 Cartographie asymétrie cadence (D1)

| Dimension | Picard (A3 supervised) | Sister cadence Finance | Delta blackout |
|---|---|---|---|
| Horizon | H10 = 10 sem. | Saru H3 = 13 sem. (quarterly) | **3 sem.** (W10→W13) |
| Cadence review | next_review date (manual) | Friday 18:00 weekly Drift Report (Zora auto-call) | **pas de synchro calendaire** |
| Pricing canon | pas de frontmatter pricing_tier | ADR-AAAS-PRICING-001 T1-T5 USD | **conflict latent** plan L2 §13.5 |
| Capex infra | pas de frontmatter infra_cost | Token Plan A0 38.11M/jour | **run-rate 75.5% quota** |
| Opex MR ratio | pas de frontmatter opex_mr_ratio | ADR-SOBER-002 §3 <15% MR | **violation silencieuse early-stage** |
| Unit econ | pas de frontmatter cac_target/ltv_target | Pilier 2 LTV:CAC>=3:1 | **CAC mirror impossible** |
| Compliance AI-Act | pas de frontmatter ai_act_compliance_status | AI-Act 2026-08-02 driver | **27 jours avant deadline** |

### 2.2 8 angles morts résumés (1 ligne chacun)

| # | B3 voice | Angle mort | Asymétrie |
|---|---|---|---|
| 1 | **Bucky Barnes** (lead) | H10 vs H3 quarterly — 3 sem. blackout runway | cadence temporelle |
| 2 | **Yelena Belova** | Pricing canon conflict — ADR-AAAS-PRICING-001 vs plan L2 §13.5 | canon immuable vs hypothèse non-ratifié |
| 3 | **Red Guardian** | Token Plan capex — 75.5% quota 5.1B tokens | quota exhaustion mid-cycle |
| 4 | **Ghost** | Intangible assets invisibles — Pilier 4-5 sister canon | opacity ops, brand equity non-trackée |
| 5 | **Taskmaster** | CAC:LTV absent — D11 anti-pattern | mirror billing impossible |
| 6 | **U.S. Agent** | AI-Act 2026-08-02 audit trail absent | 27 jours avant deadline |
| 7 | **Bucky Barnes** (depth) | D7 cost-of-escalation jamais tracé | escalade silencieuse = anti-pattern bureaucratique |
| 8 | **Red Guardian** (depth) | Anti-Paperclip §3 opex<15%MR pas auto-vérifié | violation silencieuse early-stage |

### 2.3 Recommandations D6 (gate-able par A1 Beth ou A0 in-session)

1. **Étendre MANIFEST.md frontmatter** de 8 → 13 champs (ajouts Finance-relevants) :
   - `pricing_tier` (T1-T5 ADR-AAAS-PRICING-001)
   - `opex_mr_ratio` (capex vs MR cible, sister §3 ADR-SOBER-002)
   - `token_budget_envelope` (M3 spend cap, sister Token Plan A0)
   - `next_finance_review` (date sync Saru H3, sister `a3-discovery-saru.md`)
   - `ai_act_compliance_status` (sister AI-Act 2026-08-02)
2. **Ratifier plan L2 §13.5** ou **créer ADR neuf supersede** ADR-AAAS-PRICING-001 (D4 canon immuable respecté) — gated A0 in-session, D7 cost-of-escalation.
3. **Sister cadence sync** : Picard H10 tick ouvre **créneau Saru H3 quarterly review** (D6 root cause = asymétrie de cadence).
4. **D11 anti-pattern gate** : Project Picard sans `cac_target`/`ltv_target` = soft-reject vers clarification (sister ADR-OBSERVABILITY-001 §3 anti-pattern).
5. **Hook SessionStart Picard-audit-and-prod-workflow** (`skills/picard-audit-and-prod-workflow/SKILL.md` existe per `a3-enterprise-picard.md` L.107) — vérifier alignment avec ce wargame lens, merger si drift.

### 2.4 Sister-coordination lenses (gate-able conjointement)

- **B2 JohnJones Sales** : CAC/LTV sister canon (sister `handoff_wargame_wf2_b2_johnjones_sales_lens_2026-07-06.md`). Angle commun #5 (Taskmaster CAC mirror) doit être cross-référencé.
- **B2 Cyborg IT** : infra cost sister canon (sister `handoff_wargame_wf2_b2_cyborg_it_lens_2026-07-06.md`). Angle commun #3 (Token Plan capex) doit être cross-référencé.
- **B2 Batman Ops** : ops runbooks sister canon (sister `handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md`). Angle commun #7 (D7 escalation) doit être cross-référencé.
- **B1 Jerry SYSTEMIZE** + **B1 Summers SHIP** : gate B1 final sur extension MANIFEST.md frontmatter + ratification plan L2 §13.5.

### 2.5 D6 lessons shipped (candidates ADR-META-006 append-only)

- **#85** : **Picard MANIFEST.md frontmatter Finance-gap** — 8 champs couvrent Projects mais 0/8 Finance-relevant. Recommendation = 13 champs. Sister canon `a3-enterprise-picard.md` L.50-62.
- **#86** : **Pricing canon conflict latent** — ADR-AAAS-PRICING-001 (RATIFIED 2026-06-24) vs plan L2 §13.5 (NON RATIFIÉ 2026-07-06). Sister canon `plan-L2-business-os.md` l.487-489 + `ADR-AAAS-PRICING-001` §Décision.
- **#87** : **Token Plan quota burn par Project Picard** — sister canon `MEMORY.md §ADR-LLM-COST-COMPARE-001 DATA ACTUALIZED 80% 2026-07-04` (75.5% quota 5.1B). Picard ne track pas, D7 risk = quota exhaustion mid-cycle.
- **#88** : **AI-Act 2026-08-02 audit trail absent Projects Picard** — 27 jours avant deadline, 0 frontmatter compliance. Sister canon `ADR-CANON-001` (AI-Act driver) + `ADR-AAAS-FINANCE-CANON-001` §"Consequences Negatives" l.172.

---

## 3. D1 Receipts — ce document

- ✅ Existe physiquement : `wiki/hand_offs/handoff_wargame_wf2_b2_wonderwoman_finance_lens_2026-07-06.md`
- ✅ Status live : wargame WF2 sister-coordinated avec 6 autres lenses
- ✅ 8 angles morts catalogués (range 5-10 requis) avec Fable pattern Action/Réaction/Contre/Failure/Abort
- ✅ 0 chiffre inventé : tous les nombres = D1 receipt sister canon (Token Plan 38.11M/jour, quota 5.1B, MR $1.2M ARR, T1-T5 USD, 75.5% quota, 27 jours avant AI-Act)
- ✅ Sister squad complet : 6 B3 Thunderbolts voices mappés (Bucky/Yelena/Red Guardian/Ghost/Taskmaster/U.S. Agent)
- ✅ Doctrine anchors 13 ADR cités + 1 plan (L2 §13.5) + L+ Skill Standard
- ✅ Synthèse finale : cartographie asymétrie cadence + 5 recommandations D6 + 4 sister-coordination lenses + 4 D6 lessons candidates

## 4. A0 actions needed (gated D7)

- [ ] **Décider pricing canon** : ratifier plan L2 §13.5 ($1000/mois × 100 clients) via **ADR neuf supersede** ADR-AAAS-PRICING-001, OU rejeter l'hypothèse, OU clarifier tier T3.5 entre T3 et T4.
- [ ] **Étendre MANIFEST.md frontmatter** : 8 → 13 champs avec les 5 ajouts Finance-relevants listés §2.3. Sister canon `a3-enterprise-picard.md` L.50-62.
- [ ] **Sync cadence Picard H10 ↔ Saru H3** : ouvrir créneau finance review dans chaque tick Picard (gated A0/Beth).
- [ ] **Audit AI-Act 2026-08-02 readiness Projects** : sister Aquaman Legal lens (`b2-08-aquaman-legal` Eternals B3). Deadline 2026-08-02 = 27 jours.
- [ ] **(optionnel)** Skill canon-batch-spawn v2 : ajouter frontmatter Finance-relevants automatique sur MANIFEST.md generated.

---

**Status** : DRAFT — wargame lens live, 8 angles morts catalogués. Gated D7 cost-of-escalation pour §4 A0 actions. Sister-coordination lenses B2 Sales + B2 Cyborg IT + B2 Batman Ops + B1 Jerry + B1 Summers pour ratification conjointe.