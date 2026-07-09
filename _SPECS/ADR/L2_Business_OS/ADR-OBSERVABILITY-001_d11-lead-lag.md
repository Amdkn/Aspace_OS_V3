---
adr_id: ADR-OBSERVABILITY-001
titre: D11 Lead/Lag Metrics — OMK Nexus Landing Pages
type: Observability / Metrics Doctrine
domaine: L2_Business_OS
statut: RATIFIED
date_creation: 2026-07-06
date_ratification: 2026-07-06
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-3"
  context: "Ratification Tier 3 ops/QA — 6 ADR production gates ratifiés en bloc."
auteur: B1 E-Myth Gatekeeper (Jerry_Mindset disposition)
gate: SYSTEMIZE
sprint: Q3 2026 (12WY cycle 06/15 → 09/07)
owner: Jerry Prime (B1)

sisters_canon:
  - _SPECS/ADR/L2_Business_OS/ADR-ANTI-PAPERCLIP-001_saas-canon.md
  - _SPECS/ADR/L2_Business_OS/ADR-ICP-NEXUS-001_data-first-conformite.md
  - _SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_saas-pricing-canon.md
  - _SPECS/ADR/L0_Tech_OS/ADR-DEPLOY-001_vercel-pipeline.md
  - _SPECS/ADR/L2_Business_OS/ADR-LANDING-QA-001_pre-prod-checklist.md

sources_canons:
  - path: A3-snW-Chapel (médecin USS SNW, Measure specialist)
    role: agent sister canonique — lead/lag distinction
  - path: PRD-PORTFOLIO-B1-FRANCHISE §6 Tier 3 — PRD-UNIT-ECON-PROOF-001
    role: table de preuve coût-fixe-vs-Jevons (chiffres D11 input)
  - path: MEMORY.md §'ADR-LLM-COST-COMPARE-001 DATA ACTUALIZED 80% 2026-07-04'
    role: Token Plan canon A0 usage réel
  - path: MEMORY.md §'Plan Méta-Mémoire OKF 2026-07-02'
    role: 5 phases W3→W13 + boucle 12WY
  - path: plan-L2-business-os.md §13.5
    role: pricing canonique $1000×100 gated
  - path: ADR-DEPLOY-001 (créé ce turn)
    role: Vercel deployment pipeline sister
  - path: CLAUDE.md §'Doctrine Anti-Paresse D7'
    role: cost-of-escalation, D11 lead vs lag

vocabulaire_canon:
  - D11 = Doctrine Lead/Lag distinction (sister ADR-META-001)
  - LEAD = métrique prédictive du comportement futur
  - LAG = métrique de confirmation a posteriori
  - sister = source canonique liée (D1 receipts)
  - SKIPPED honnête = refus de quantifier sans source canon
  - HITL A0 = Human-In-The-Loop, validation Amadeus requise

chiffres_sister_canon:
  token_plan_a0:
    - "38.11M tokens/jour (usage réel A0)"
    - "772.20M tokens/7j"
    - "3.85B tokens/30j"
    - "$50/mois pour ~5.1B tokens (Token Plan A0)"
  pricing_cible:
    - "$1000/mois ×100 = $1.2M ARR (plan L2 §13.5)"
---

# ADR-OBSERVABILITY-001 — D11 Lead/Lag Metrics pour OMK Nexus Landing Pages

## 1. Contexte

Les deux Landing Pages OMK Nexus (FR : `omk-nexus-landing-page.vercel.app` · EN : `omk-nexus-landing-en.vercel.app`) sont en production depuis 2026-06-27 / 2026-06-29 (sisters canoniques `omk_nexus_phase_a_RETARGET_coach_first_2026-06-27.md` + `MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29'`). À ce stade, le Système ne dispose d'**aucune métrique de mesure** autre que les `200 OK` Vercel. Le présent ADR pose la **doctrine D11 lead/lag** comme garde-fou contre le paperclip « tracker tout, mesurer rien ».

Doctrine Anti-Paperclip (sister `ADR-ANTI-PAPERCLIP-001`) : **toute métrique publiée doit être sister-canon ou SKIPPED honnête**. Zéro chiffre inventé pour « faire la story ».

## 2. Décision

**Adopté** : la doctrine D11 lead/lag est la **seule métrique acceptée** pour observer les Landing Pages OMK Nexus. Les métriques sont classées en deux familles strictes, sans tierce voie « vanity ».

**Rejeté** :
- Google Analytics 4 (paperclip tier, GDPR hostile, hors-scope canon)
- Hotjar / Microsoft Clarity (paperclip tier, session-replay = paperclip)
- Tout tracker tiers avec cookie ou fingerprinting
- Compteurs vanity sans corrélat prédictif (ex. « nombre de visiteurs uniques » sans segmentation)

## 3. Principe D11 — Lead vs Lag

**Métrique LEAD** (prédictive) : signal **précurseur** qui corrèle avec un comportement futur. Si la lead se dégrade, on peut corriger **avant** que la lag ne confirme la perte.

**Métrique LAG** (confirmative) : signal **conséquent** qui mesure un comportement déjà advenu. Utile pour le bilan, insuffisante pour l'action en temps réel.

Anti-pattern D11 (interdit) :
- Vanity metric isolée (compteur sans corrélat)
- Lead sans fenêtre temporelle d'observation
- Lag présentée comme lead (storytelling rétrospectif)
- Mélange lead+lag dans un même dashboard (signe de mesure non-encore-séparée)

## 4. Métriques LEAD (D11 — predict)

Cinq métriques lead, classées par profondeur de funnel :

### 4.1 Time-to-A0
**Définition** : durée entre `landing` et premier `mailto:` ouvert (proxy : premier ping backend de tracking mailto).
**Sister canon** : `PRD-UNIT-ECON-PROOF-001 §6 Tier 3` (corrélation prospect quality).
**Fenêtre** : instantané par session.
**Seuil D11** : baseline mesurable S0 (semaine pre-launch) → évolution W_n vs W_0.

### 4.2 Scroll-depth
**Définition** : pourcentage de page scrollé avant `exit` (ou `unload`).
**Implémentation** : Vercel Analytics (auto) + `IntersectionObserver` custom optionnel.
**Sister** : sister FR/EN LIVE (Vercel Analytics intégré au deploy).
**Corrélat** : engagement qualitatif.

### 4.3 CTA hover rate
**Définition** : ratio `mouseover` sur CTA / `mousemove` global.
**Implémentation** : custom event `fetch()` ping backend maison (gated HITL A0).
**Corrélat** : friction de conversion (hover sans click = hésitation).

### 4.4 Hero dwell time
**Définition** : temps avant premier scroll depuis `DOMContentLoaded`.
**Implémentation** : Vercel Web Vitals + custom `performance.mark()`.
**Corrélat** : clarté du manifeste (sister `ADR-ICP-NEXUS-001` — Data First / Conformité).

### 4.5 Section engagement
**Définition** : temps passé par section (`IntersectionObserver` per-section timers).
**Implémentation** : custom event ping (gated HITL A0).
**Corrélat** : messaging efficacy.

## 5. Métriques LAG (D11 — confirm)

Cinq métriques lag, classées par profondeur de funnel :

### 5.1 Signups
**Définition** : `mailto:` CTA form submitted (proxy unique : Plunk open + click).
**Sister** : `PRD-UNIT-ECON-PROOF-001 §6 Tier 3`.
**Cadence** : agrégation 12WY cycle.

### 5.2 Conversion
**Définition** : `CTA click × time-to-action`.
**Fenêtre** : 30j par session unique (Vercel Analytics cookie-less).
**Sister** : funnel canonique Nexus (sister `plan-L2 §13.5`).

### 5.3 Bounce
**Définition** : `% sessions` avec `exit < 10s` sans scroll.
**Implémentation** : Vercel Analytics built-in.
**Sister** : corrélat landing quality (sister `ADR-LANDING-QA-001`).

### 5.4 Retention
**Définition** : revisit 30j (Vercel Analytics — pas de fingerprinting, agregation par IP hash éphémère).
**Fenêtre** : rolling 30j.
**Sister** : corrélat valeur perçue (sister `ADR-AAAS-PRICING-001`).

### 5.5 Affiliation 20% Stripe Connect (Medvi loop)
**Définition** : revenue Medvi via Stripe Connect 20% (sister PRD-NEXUS §5.4).
**Sister** : `plan-L2 §13.5` (boucle affiliation).
**Cadence** : 12WY cycle (gate trimestriel).

## 6. Infrastructure de mesure (sans tracking tiers)

| Outil | Usage | Sister canon | Tier |
|---|---|---|---|
| **Vercel Analytics** | page views, CWV, referrers (auto) | FR/EN LIVE sisters | gratuit, privacy-friendly |
| **Plunk** (open-source) | mailto CTA tracking, open + click | `PRD-UNIT-ECON-PROOF-001` | GDPR-compliant |
| **Custom events `fetch()`** | ping backend maison (4.3, 4.5) | gated HITL A0 | self-hosted |
| **Stripe Connect** | Medvi loop revenue | sister PRD-NEXUS §5.4 | canon L2 |

**Interdits** :
- Google Analytics 4 (paperclip tier)
- Hotjar / Microsoft Clarity (paperclip tier)
- Tout cookie tiers ou fingerprinting (violation Anti-Paperclip + GDPR)

## 7. Cadence de mesure

| Cadence | Métriques | Sister |
|---|---|---|
| **Quotidien** | page views, CWV rolling avg | Vercel Analytics |
| **Hebdomadaire** | scroll-depth median, hero dwell, CTA click rate | sister `Multi-Routines-12WY` |
| **12WY cycle** | conversion, signup velocity, pipeline value, Medvi loop | sister `Plan Méta-Mémoire OKF §10 runbook /loop CC-M3` |
| **Quarterly review** | pipeline value vs target $1.2M ARR | sister `plan-L2 §13.5` |

**Sister alignement** : `Plan Méta-Mémoire OKF 2026-07-02 §10` (runbook /loop CC-M3) + `Multi-Goal` + `Multi-Routines-12WY` si cycle 12WY.

## 8. Métriques Tier 3 — sister canoniques CITABLES (D1 receipts)

Les chiffres suivants sont **sister-canon** (citables D1) :

| Métrique Tier 3 | Valeur | Source canon |
|---|---|---|
| Usage A0 tokens/jour | 38.11M | `MEMORY.md §'ADR-LLM-COST-COMPARE-001 DATA ACTUALIZED 80% 2026-07-04'` |
| Usage A0 tokens/7j | 772.20M | idem |
| Usage A0 tokens/30j | 3.85B | idem |
| Token Plan A0 | $50/mois pour ~5.1B tokens | idem |
| Pricing cible L2 §13.5 | $1000/mois ×100 = $1.2M ARR | `plan-L2-business-os.md §13.5` |

**Règle D11 stricte** : toute métrique publiée doit pointer vers l'une de ces 5 sources sister, ou être marquée **SKIPPED honnête**. Aucune invention chiffrée tolérée (sister `ADR-ANTI-PAPERCLIP-001`).

## 9. Workflow QA D11 gates + Anti-patterns

### 9.1 Workflow QA D11 gates

1. **Baseline S0** : mesure pre-launch (semaine 0 = pre-deploy ou premier deploy)
2. **Mesure weekly** : cohort comparison W_0 vs W_n (sister `l1-weekly-snapshot`)
3. **Anomaly detection** : deviation > 50% vs baseline → escalade A0 (sister D7 cost-of-escalation, mais D11 n'escalade **pas** sauf vraie urgence)
4. **12WY quarterly review** : pipeline value vs target $1.2M ARR
5. **D11 publication gate** : tout chiffre publié = sister-canon ou SKIPPED

### 9.2 Anti-patterns interdits

1. **Tracking tiers** (cookie, fingerprinting) — paperclip hors-scope
2. **Vanity metrics** sans corrélat prédictif (compteur sans lead/lag)
3. **Chiffres inventés** pour « story » — sister `ADR-ANTI-PAPERCLIP-001`
4. **Google Analytics 4** — paperclip tier

### 9.3 Sister tooling canon

- Vercel Analytics (intégré auto au deploy sister FR/EN)
- Plunk (open-source email analytics, GDPR-compliant)
- Stripe Connect (canon L2, Medvi loop)
- Sisters agents : `multi-routines-12wy`, `l1-weekly-snapshot`, `aaas-dashboard-port-audit`

### 9.4 Doctrine d'escalade (D7)

L'escalade A0 sur ce sujet est **coûteuse** (D7, ~100×). Default = non-escalation. Escalade **uniquement** si :
- Anomaly > 50% détectée ET
- Cause technique non-identifiable par A2/A3 ET
- Sister canon (5 sources listées §8) ne fournit pas de réponse

---

## Annexe A — Chiffres sister-canon (citation verbatim)

> **MEMORY.md §'ADR-LLM-COST-COMPARE-001 DATA ACTUALIZED 80% 2026-07-04'** :
> "OpenRouter `/api/v1/models` 340 models curl direct → Claude Sonnet 5 $2/$10 · Sonnet 4.6 $3/$15 · Opus 4.8 $5/$25 · Haiku 4.5 $1/$5 · Fable 5 $10/$50 · MiniMax-M3 $0.30/$1.20. (2) **MiniMax Token Plan · Monthly Max** $50/mois pour ~5.1B tokens M3 (D1-verified via screenshots A0 `platform.minimax.io/console/usage` + `subscribe/token-plan`) — usage actuel A0: 38.11M tokens/jour, 772.20M/7j, 3.85B/30j."

## Annexe B — Liens sisters canoniques

- **Sister L2 ICP** : `_SPECS/ADR/L2_Business_OS/ADR-ICP-NEXUS-001_data-first-conformite.md`
- **Sister L2 Pricing** : `_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_saas-pricing-canon.md`
- **Sister L2 Anti-Paperclip** : `_SPECS/ADR/L2_Business_OS/ADR-ANTI-PAPERCLIP-001_saas-canon.md`
- **Sister L2 Landing QA** : `_SPECS/ADR/L2_Business_OS/ADR-LANDING-QA-001_pre-prod-checklist.md`
- **Sister L0 Deploy** : `_SPECS/ADR/L0_Tech_OS/ADR-DEPLOY-001_vercel-pipeline.md`
- **A3-snW-Chapel** : agent sister canonique (Measure specialist, lead/lag)
- **PRD-PORTFOLIO-B1-FRANCHISE §6 Tier 3** : table de preuve coût-fixe-vs-Jevons
- **MEMORY.md §'Plan Méta-Mémoire OKF 2026-07-02'** : 5 phases W3→W13 + boucle 12WY
- **plan-L2-business-os.md §13.5** : pricing canonique $1000×100 gated
- **CLAUDE.md §'Doctrine Anti-Paresse D7'** : cost-of-escalation, D11 lead vs lag

## Annexe C — SKIPPED honnête (à clarifier avant publication)

- **Taux de conversion benchmark** : SKIPPED (pas de sister canon pour benchmark SaaS B2B conformité)
- **Bounce rate moyen sectoriel** : SKIPPED (pas de sister canon sectoriel Nexus)
- **CTR CTA moyen** : SKIPPED (sera mesuré S0 baseline avant toute publication)
- **Retention 30j moyen** : SKIPPED (idem)

Toute publication ultérieure de ces chiffres devra faire l'objet d'une mesure réelle (W_n vs W_0) avant d'être sister-canon-ifiée.

---

**Statut** : DRAFT — En attente de ratification B1 Jerry + A0 HITL.
**Next step** : soumission `ratify-adr` (sister skill) après validation A0.
