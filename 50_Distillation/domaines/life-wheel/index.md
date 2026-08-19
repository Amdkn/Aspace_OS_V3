---
type: Index
title: Index des concepts Life Wheel (LD01-LD08)
description: 17 concepts OKF v0.2 distilllés depuis la couche 22_Wheel_Discovery — les 8 LDs Discovery/ZORA, les 4 Jerry (J01-J04), le HARD SAFETY Beth, les AaaS variants, et la correction canon Book H1 / Saru H3.
tags: [index, life-wheel, zora, ld01-ld08, jerry-j01-j04, hard-safety, aaas-variants]
generated: { by: minimax-m3, at: 2026-08-19T04:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T04:00:00Z }
okf_version: "0.2"
---

# Index des concepts Life Wheel (LD01-LD08)

> Escouade 22_Wheel_Discovery — distillation V2 → V3 OKF v0.2.
> Couverture : 297 fichiers du corpus `09_Life_OS/` (8 LDs) + specs canoniques `22_Wheel_Discovery/`.
> Méthode complète : voir `60_Implementation_Méthodologiques/domaines/life-wheel.md`.
> Rapport de distillation : `50_Distillation/_briefs_vague2/RAPPORT_life-wheel.md`.

## Question qui commande cette vague

Quels documents canoniques de la V2 restent autorité après la migration V3, et lesquels sont dépassés sur un point précis tout en restant valables sur dix autres ? Quatre verdicts appliqués : `canon` (autorité), `synthese-datee` (dépassé sur un point), `superseded` (remplacé en entier), `orphelin` (sans rattachement).

# Files

## Couverture LD01-LD08 (les 8 personas Discovery)

- [LD01 Book — Career & Business H1](ld01-book-career-business.md) — A3 Book, horizon H1 weekly P&L, supervisé par J01 Jerry Prime. Sole rule : Book ne décide pas la stratégie seul.
- [LD02 Saru — Finance & Independence H3](ld02-saru-finance-independence.md) — A3 Saru, horizon H3 quarterly runway. Anti-paperclip 1000T : 3 garde-fous canon.
- [LD03 Culber — Health/Sleep/Energy H10](ld03-culber-health-sleep-energy.md) — A3 Culber, **HARD SAFETY** Beth veto automatic si RED. Primary gravity sensor de Life OS.
- [LD04 Tilly — Mind/Cognition H30](ld04-tilly-cognition-stop-authority.md) — A3 Tilly, **STOP authority** si Culber RED. Cascade LD03→LD04.
- [LD05 Stamets — Social/Relations H30](ld05-stamets-social-relations.md) — A3 Stamets, isolation RED = 1-turn escalation Beth.
- [LD06 Burnham — Family/Presence H10](ld06-burnham-family-presence.md) — A3 Burnham, bond fracture RED = 1-turn escalation Beth. Ancre Orbiter/ABC.
- [LD07 Reno — Creativity/Leisure H10](ld07-reno-creativity-leisure.md) — A3 Reno, joy starvation = slow poison. Couplage DEAL elimination.
- [LD08 Georgiou — Contribution/Impact H90](ld08-georgiou-contribution-impact.md) — A3 Georgiou, negative-reach RED = 1-turn escalation. Ancre Solaris.

## Mapping Jerry J01-J04 → LDxx

- [J01-J04 — Les 4 Jerry et leurs LDxx](jerry-j01-j04-mapping-ldxx.md) — Quatre Jerry (Prime / Bio / Nexus / Solarpunk) couvrent les 8 LD par bande transversale. Source canon `02_Areas_Spock/J0X_*`. Collision de nom détectée : J04 = `Creativity_Impact` (correct) vs `Creatry_Impact` (typo).

## Doctrines canon verrouillées

- [HARD SAFETY — doctrine Beth veto LD03 LD04](hard-safety-beth-veto-ld03-ld04.md) — Seuils chiffrés SDD-005 : LD03_minimum=4.0, LD04_minimum=3.5, multi_domain_alert=3. Cascade vérifiée à chaque Sunday Uplink.
- [Horizons canon H1/H3/H10/H30/H90](horizons-canon-h1-h3-h10-h30-h90.md) — Correction D3 : Saru = H3 (PAS H1), Book = H1 (PAS H10). Verrouillé 2026-06-21 sur alignement plan fancy-hugging-bengio §18.2.
- [Drift owner correction — Tilly+Spock NOT Saru+Stamets](drift-owner-correction-tilly-spock.md) — Plan §15.1.4 initialement mappait "Life Wheel drift → Saru+Stamets". Corrigé : drift = **Tilly (LD04) + Spock (Areas)**. D3 nuance critique.
- [AaaS 3 variants — Solaris / Nexus / Orbiter / 4e Dormant](aaas-3-variants-mapping-ldxx.md) — Book LD01 (Solaris ACTIF), Saru LD02 (Nexus/OMK CLOS 2026-06-20), Burnham LD06 (Orbiter ACTIF), Tilly+Culber (4e Dormant).

## Pipeline canon

- [Pipeline A0→A1→A2→A3 Discovery/ZORA](pipeline-a0-a1-a2-a3-discovery-zora.md) — Pattern strict : A0 board observer → A1 Beth (veto) → A2 Discovery (ZORA synthesis) → A3 twins (narrow findings). A3 ne compile JAMAIS de rapport final.
- [Sunday Uplink — revue hebdomadaire](sunday-uplink-revue-hebdomadaire.md) — Moment unique de revue : Discovery consolide ZORA state, Orville compile crew findings, Chapel expose Scorecard. Seul moment toléré pour escalader à A0.
