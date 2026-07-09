---
id: J01_B3_GROWTH_001_GUARDIANS_GTM_PACKET
jtbd_id: J01-B3-GROWTH-2026-001
source_rock: J01-B2-GROWTH-2026-01
layer: B3_AREA_WARP_CORE
surface: Jerry Area J01 LD01 Business
scope: Area (perpetual doctrine — canonical reference for Picard projects)
domain: Growth
b2_owner: Superman
guardian_lead: Gamora
supports: [Mantis, Star-Lord, Groot, Rocket, Drax]
principles_ref: [P1, P3, P5, P6, P7, P8, P9, P11, P12, P13, P14, P15, P16, P18]
evidence_grade: HYPOTHESIS (doctrine synthesis from Yann Leonardi corpus — field validation per §5)
status: REVIEW_READY
updated: 2026-05-29
---

# JTBD-GROWTH-001 — Guardians AaaS GTM Packet (canonical, Area-level) — Jerry / Superman

> **Job** : *When the AaaS Growth loop needs a canonical go-to-market reference, the full Guardians squad produces an ICP filter + VOC + painkiller hypotheses + a first instrumented experiment, so Superman can prioritize (P5 RICE) and the Picard projects can calibrate per mode without re-deriving doctrine.*
> **Lead** : Gamora (ICP/precision). **Squad** : Mantis (VOC), Groot (message), Rocket+Drax (experiment/kill), Star-Lord (ICP hunt).
> ⚠️ **Evidence grade = HYPOTHESIS** — synthèse doctrine ancrée sur le corpus Yann Leonardi (P1–P18) ; pas d'interviews réelles. Validation §5. **Source de vérité Area** : les projets Picard héritent et calibrent par mode (Solaris/Nexus/Orbiter), ils ne re-dérivent pas.

## 1. North Star + cadre AARRR
**NSM** : *ICP-qualified AaaS opportunities generated from non-paid channels.* (P4, Superman non-délégable.)
Boucle prioritaire = **Acquisition organique → Activation → Rétention** avant tout canal payant (anti-pattern P1/P2).

## 2. ICP filter canonique (Gamora — P1/P9/P11) — 3 critères de rejet
> Filtrer AVANT de vendre protège LTV/CAC (P3) et concentre le 80/20 (P11).

| # | Critère de rejet | Signal | Principe |
|---|------------------|--------|----------|
| R1 | **Pas de budget/ASP-fit** (cherche le moins cher) | sensibilité prix > valeur, compare au tarif horaire | P3 (LTV/CAC) |
| R2 | **Pas operator-ready** (veut une baguette magique, refuse le système) | "fais-le pour moi sans que je change rien" | P9 (filtre entrée) |
| R3 | **Hors 80/20** (segment à faible récurrence/upside) | one-shot, pas de besoin récurrent, no expansion | P11 (Pareto) |

**Scoring** : 0 rejet = ICP-fit · 1 rejet = nurture · ≥2 rejets = decline (bon churn, P10 — Drax).

## 3. VOC (Mantis — P7q/P13/P16) — synthèse canon
Les 5 pains génériques AaaS (dépendance fondateur, absence de système, échecs passés, plafond de scaling, crédibilité) sont **déclinés par mode** dans chaque projet Picard (cf. leurs `JTBD-001_<MODE>_VOC_PACKET.md`). Persona Process Com dominant varie par mode ; base psychologique commune = **Travaillomane + Persévérant** (preuve/méthode) sauf Solaris (Empathique) et community (Empathique).

## 4. Painkiller hypotheses (Groot — P8/P16) — 3 variants canoniques
> Painkiller, pas vitamine (P8). Drax kill les variants faibles (P5).

- **V1 — Liberté opérationnelle** : « Un business qui tourne sans vous au centre. » (cible la dépendance fondateur)
- **V2 — Système transférable** : « Vos opérations en système documenté et délégable. » (cible l'absence de SOP)
- **V3 — Preuve > promesse** : « Pas un cours/une agence de plus — un OS implémenté qui reste. » (cible la méfiance post-échec)

**Drax kill-gate** : tout variant dont le CTR copy < baseline OU sans signal qualitatif Mantis = killed (P5/P6).

## 5. Premier experiment non-payant (Rocket — P6/P7q/P12/P15) + RICE
```yaml
experiment: "1 essai de preuve (case study/framework) publié sur 1 canal organique, opt-in instrumenté (P15), boucle referral légère (P12)"
rice:
  reach: "audience organique atteignable (est.)"
  impact: "high — teste la promesse painkiller V-gagnant"
  confidence: "medium — HYPOTHESIS, pas encore de baseline"
  effort: "low — 1 pièce de contenu + 1 opt-in"
lead_indicator: "≥1 pièce de preuve publiée + opt-in instrumenté (CPQL mesurable)"
lag_indicator: "≥1 ICP-qualified AaaS opportunity from the non-paid piece"
build_gate: "CPQL < 80€ green · Pipeline ≥ 5k€/sem green (canon Notion)"
```

## 6. Handoff & autorité
- **Picard projects** héritent ce packet et calibrent par mode (Solaris/Nexus/Orbiter). Ce fichier = référence canonique, pas à dupliquer (DRY).
- **Superman (P4/P5)** : arbitre NSM + RICE ; **escalade Jerry** si CPQL > 150€ / 14j.
- **Désaccord productif** : Drax doit pouvoir killer un variant painkiller même soutenu par Groot si la donnée ne suit pas.

## 7. DoD auto-check (Rock J01-B2-GROWTH-2026-01)
- [x] ICP filter + critères de rejet · [x] VOC 5 pains (renvoi projets) · [x] 3 painkiller variants · [x] 1 experiment RICE + lead/lag · [x] proof = artefact inspectable · [x] zéro mutation externe · [ ] **Acceptance Superman**

*B3 Area artifact (Guardians, Gamora lead) under Superman. Canonical reference for Picard. Last sync: 2026-05-29*
