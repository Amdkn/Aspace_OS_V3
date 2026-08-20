---
type: Concept
title: B1 OMK T2 pivot US — exemple calibré de mandat B1→B2 sur pivot marché
description: Mandat B1 calibré sur le Rock B1-2 OMK Business OS (T2 Growth+Sales+Finance, pivot marché US 2026-07-15) avec intent, contraintes, success_signal selon la grammaire canonique. Sert d'exemple de référence pour tous les mandats B1 émis dans un Project daté pivot.
tags: [b1, b2, mandate, omk, pivot-us, t2, exemple, calibre]
generated: { by: minimax-m3, at: 2026-08-19T02:15:00Z }
verified:
  - { by: process:synthese-pulse-b1-tour-2, at: 2026-08-19T02:15:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: omk-project
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/omk-business-os.md"
    title: OMK Business OS — Triptyque V4 status ACTIVE 2026-07-15
    last_modified: 2026-08-17
  - id: omk-t2-ownerbook
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/ownerbooks/ownerbook_T2_growth_sales_finance.md"
    title: Ownerbook T2 Growth/Sales/Finance (Rock B1-2, 2026-07-15)
    last_modified: 2026-07-15
  - id: us-pivot
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/omk-us-market-pivot.md"
    title: OMK US Market Pivot
    last_modified: 2026-08-17
  - id: triplets-v3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets — 8 vetos Wonder Woman
    last_modified: 2026-08-17
okf_version: "0.2"
---

# B1 OMK T2 pivot US — exemple calibré de mandat B1→B2

OMK Business OS est passé en status **ACTIVE** le 2026-07-15 avec un
**pivot marché US** formel (cf. `omk-business-os.md`). Le pivot a deux
conséquences directes sur la grammaire des mandats B1 :

- Les références EUR historiques ne sont plus la cible — le segment
  devient Coach premium B2B $7.5-25K ACV + Enterprise mid-market.
- Le Triptyque V4 (T1 People+Ops+Product, T2 Growth+Sales+Finance,
  T3 Legal+R&D) impose que les mandates B1 soient routés par **rock**,
  pas par cycle complet. Trois rocks actifs = trois mandates pivot au
  minimum.

Ce concept pose le mandat B1 calibré pour le **Rock B1-2** (T2). Les
deux autres rocks (T1, T3) suivent la même grammaire, avec d'autres
intent/contraintes/signal.

## Le mandat Rock B1-2 — T2 Growth+Sales+Finance, pivot US

```yaml
b1_b2_mandate_id: B1-B2-MANDATE-2026-21
issued_at: 2026-08-19T10:00:00Z
issued_by: summer-coach-os
cycle: 12WY-2026-Q3-Q4
source_rock: B1-2 (T2 Growth+Sales+Finance, Ownerbook T2)

intent: |
  Le pivot marché US (2026-07-15) impose une traction monétaire qualifiée
  sur le segment Coach premium B2B $7.5-25K ACV, sous 60 jours. Sans
  preuve de demande monnayable avant fin de cycle, le pivot reste une
  déclaration — et le Rock B1-2 bascule en "declared not delivered".

contraintes:
  - Aucune dépense récurrente sans métrique de retour chiffrée à 30 jours
    (veto Wonder Woman — triplet v3 ligne 28, doctrine veto-dépense).
  - Aucun claim public US qui n'a pas passé la revue Legal Aquaman
    (AI Bill of Rights + 365 Conformité).
  - Toute référence EUR historique doit être marquée `LEGACY` dans le
    canon avant nettoyage — pas de suppression silencieuse.
  - Le coût par SQL qualifié US ne doit pas dépasser 1/4 du contrat
    moyen (cible ACV $7.5-25K, soit ≤ $1.875-6.25K par SQL).

success_signal: |
  20 SQLs qualifiés US segment premium B2B (ACV $7.5-25K) mesurés sur
  60 jours à compter de l'acceptance du mandat, avec coût par SQL
  vérifié ≤ $6.25K. Liste des SQLs jointe au rapport de mi-cycle.
  Cycle de mesure : 12WY-2026-Q3-Q4 (fin 2026-10-15).
```

## Pourquoi ce mandat respecte la grammaire

| Champ | Critère `b1-success-signal-spec.md` | Conformité |
|---|---|---|
| `intent` | Pourquoi ce mandat maintenant, dans le North Star | OK — réfère pivot US 2026-07-15 + Rock B1-2 Ownerbook T2 |
| `contraintes` | Limites non-négociables | OK — 4 contraintes, toutes sourcées (veto WW, Aquaman, doctrine canon, ratio ACV) |
| `success_signal` | Mesurable ou observable, mesurable privilégié | OK — compteur (20 SQLs), seuil (ACV $7.5-25K), délai (60j), source de vérité (CRM + Sales_Illuminati ABM LinkedIn) |

**Type de signal : mesurable.** Compteur naturel = nombre de SQLs
qualifiés trackés dans le pipeline Sales_Illuminati. Latence définie
(60j). Témoin = ABM LinkedIn + CRM. Pas besoin d'un substitut observable.

## Acceptance check (cf. `b1-mandate-acceptance-check.md`)

Les trois capitaines B2 destinataires du Rock B1-2 doivent attester
chacun en 24h :

| Captain | Domaine | Ce qu'il atteste |
|---|---|---|
| **Superman** | Growth (01) | Reformulation intent → traction US segment premium B2B ; contrainte coût par SQL ≤ 1/4 contrat ; DoD-Una : 3 sources de leads US calibrées (ABM LinkedIn + cold outbound + paid trial) |
| **JohnJones** (W40 V4) | Sales (02) | Reformulation intent → SQLs qualifiés US en pipeline ; DoD-Una : 3 critères de qualification scoring (ACV $7.5-25K, signataire identifié, besoin reformulé) |
| **Wonder Woman** | Finance (06) | Reformulation intent → ROI à 30 jours par source de lead ; contrainte veto-dépense tenue ; DoD-Una : 3 ratios financiers vérifiés (coût/SQL, payback, marge brute préservée) |

Si l'un des trois échoue à attester, le mandat est multi-destinataires
et doit passer par le **B2 Council** (cf. `b2-council-arbitrage-rule.md`)
avant acceptance. Le Council tranche en mode `negotiation` sur les
critères de scoring et le mode de comptage (SQL = MQL+ ou SQL = SQL
stricte senu Sales_Illuminati ?).

## Ce que ce mandat n'est PAS

- **Pas un plan d'exécution.** Le comment (cold outreach ABM,
  LinkedIn ads, paid trial SaaS) est du ressort B2 → B3, pas B1.
- **Pas un DoD.** Le DoD final est posé par le B2 captain (3 critères
  minimum) après acceptance, puis transformé en DoD packet selon le
  format B2 (cf. `b2-meso-decision-packet-spec`).
- **Pas une escalade.** Le mandat est de routine — wheel imbalance
  signe 1 (domaine Sales sous-doté) déclenche ce mandat, pas une
  crise North Star.

## Liens avec les autres concepts tour 2

- `b1-success-signal-spec.md` — la règle de choix mesurable/observable
  appliquée ici.
- `b1-mandate-acceptance-check.md` — le verrou de gouvernance en aval.
- `b1-mandate-packet-spec.md` — la grammaire amont.
- `b1-cycle-rollover-protocol.md` — la mesure se fait au rollover du
  12WY-2026-Q3-Q4 (2026-10-15).

## Le rollover de mi-cycle — ce qui est attendu

Mi-12WY (2026-09-01, ~45 jours après émission) :

- B2 Council publie un **meso-decision-packet** attestant la progression
  vers le signal (cible mi-cycle : 10 SQLs, soit 50% de l'objectif).
- Si la progression est < 30% de la cible, B2 Council remonte un
  arbitrage mode `negotiation` → possible escalade B1 pour amender le
  mandat (ajout de canaux, resserrement de cible, etc.).
- Si la progression est ≥ 70%, B1 confirme le cap et le cycle continue.

Rollover de fin de cycle (2026-10-15) :

- B2 publie le **proof_expected** listé dans le meso-decision-packet de
  mi-cycle. B1 tranche `accepted` ou `blocked` sur le signal.
- Si `blocked`, le Rock B1-2 est marqué `declared not delivered` et
  entre dans le cycle de rollover suivant (cf.
  `b1-cycle-rollover-protocol.md`).

## Sources

- `omk-business-os.md` — le projet OMK ACTIVE 2026-07-15.
- `ownerbook_T2_growth_sales_finance.md` — le Rock B1-2 et ses DoD-1.
- `omk-us-market-pivot.md` — les détails du pivot marché US.
- `v3-business.jsonl` ligne 28 — Wonder Woman veto-dépense (référence
  canon de la contrainte 1).

## Liens

- [[b1-mandate-packet-spec]] — la grammaire du paquet
- [[b1-success-signal-spec]] — la règle de choix du signal
- [[b1-mandate-acceptance-check]] — le verrou d'acceptance
- [[b1-cycle-rollover-protocol]] — la mécanique de mesure
- [[b2-council-arbitrage-rule]] — le routage multi-domaine
- [[b2-eight-domain-vetoes-catalogue]] — le veto Wonder Woman

## Note de confiance

**Confirmé par machine.** Mandat calibré à partir des éléments
explicites du corpus (Ownerbook T2, triplet v3 ligne 28, doctrine
pivot US 2026-07-15). Le ACV $7.5-25K et le segment Coach premium B2B
sont tirés verbatim de `omk-business-os.md` §« Trois questions ». Les
chiffres 20 SQLs / 60 jours / coût par SQL ≤ 1/4 contrat sont des
**estimations raisonnables** à valider avec un Ownerbook T2 récent —
non sourcées d'un Ownerbook précis dans cette passe. La mécanique
mi-cycle / fin de cycle est extrapolée depuis la cadence 12WY et
nommée nulle part comme un rituel formel.