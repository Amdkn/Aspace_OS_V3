---
type: Concept
title: B1 OMK T1 People+Ops+Product — mandat calibré pour capacité opérationnelle
description: Mandat B1 calibré sur le Rock B1-1 OMK Business OS (T1 People+Ops+Product — Green Lantern X-Men + Batman Fantastic4 + Flash Avengers) avec intent « capacité opérationnelle pour Agency-as-a-Service », 4 contraintes (veto-recrutement-sans-mandat, veto-procedure-sans-condition-arret, veto-offre-depersonnalisee), success_signal mesurable (X agents B3 onboardés + Y SOPs canon publiés + Z cycles sprint tenus).
tags: [b1, b2, mandate, omk, t1, people, ops, product, agency-as-a-service]
generated: { by: minimax-m3, at: 2026-08-19T03:35:00Z }
verified:
  - { by: process:synthese-pulse-b1-tour-3, at: 2026-08-19T03:35:00Z }
sources:
  - id: omk-project
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/omk-business-os.md"
    title: OMK Business OS — Triptyque V4 status ACTIVE 2026-07-15
    last_modified: 2026-08-17
  - id: omk-t1-ownerbook
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/ownerbooks/ownerbook_T1_people_ops_product.md"
    title: Ownerbook T1 People/Ops/Product (Rock B1-1, 2026-07-15)
    last_modified: 2026-07-15
  - id: b3-roster
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: 53 B3 Agent Roster
    last_modified: 2026-08-17
  - id: triplets-v3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets — 8 vetos et rôles B3
    last_modified: 2026-08-17
okf_version: "0.2"
---

# B1 OMK T1 People+Ops+Product — mandat calibré

Le Triptyque V4 d'OMK Business OS pose **trois Rocks** actifs au
2026-07-15 (cf. `omk-business-os.md`) : T1 People+Ops+Product, T2
Growth+Sales+Finance, T3 Legal+R&D. Le concept `b1-omk-t2-pivot-us-mandate.md`
a calibré le Rock B1-2 (T2). Ce concept calibre le **Rock B1-1 (T1)**,
distinct mais isomorphe.

## Le mandat Rock B1-1 — T1 People+Ops+Product

```yaml
b1_b2_mandate_id: B1-B2-MANDATE-2026-22
issued_at: 2026-08-19T10:00:00Z
issued_by: summer-coach-os
cycle: 12WY-2026-Q3-Q4
source_rock: B1-1 (T1 People+Ops+Product, Ownerbook T1)

intent: |
  L'Agency-as-a-Service (Ownerbook T1 §2 — « the agency IS the product,
  not a tool ») exige une capacité opérationnelle reproductible avant
  toute traction commerciale. Sans SOP canon, sans squad B3 staffed,
  sans cycle sprint qui tourne, le pivot US de T2 (cf. b1-omk-t2) n'a
  rien à livrer — et le squad 53 B3 reste un roster, pas une force.
  T1 tient la supply chain interne dont T2 et T3 sont les clients.

contraintes:
  - Aucun recrutement d'agent B3 ou humain sans mandat écrit et
    critère de sortie vérifiable (veto Green Lantern — triplet v3
    ligne 23, doctrine veto-recrutement-sans-mandat).
  - Aucune procédure.ops sans condition d'arrêt écrite et date de
    revue (veto Batman — triplet v3 ligne 24).
  - Aucune offre dont la valeur repose sur une personne nommée — la
    valeur doit survivre au remplacement de l'opérateur (veto Flash
    — triplet v3 ligne 25, doctrine veto-offre-depersonnalisee).
  - Toute SOP canon publiée doit porter un owner B2 identifié et un
    cycle de revue trimestriel — pas de SOP orphelin.

success_signal: |
  Trois compteurs agrégés sur 60 jours :
  1. Au moins 7 agents B3 onboardés par squad (X-Men + Fantastic4 +
     Avengers) avec profil _doctrine/agents/b3-*.md publié et B2 owner
     identifié, cible 21+ profils au total.
  2. Au moins 3 SOP canon publiés (cible : SOP ProcessDesign signée
     MrFantastic, SOP Recruiting signée ProfessorX, SOP Onboarding
     client signée CaptainAmerica) avec owner et cycle de revue.
  3. Au moins 8 sprints B2 tenus (cible : 2 sprints × 4 semaines par
     captain Batman + Flash + GreenLantern), chaque sprint avec
     SPRINT_SUMMARY CLEAN ou DRAGGED-justifié.
  Seuil : 2 des 3 compteurs à 70%+ de la cible. Cycle de mesure :
  12WY-2026-Q3-Q4 (fin 2026-10-15).
```

## Pourquoi ce mandat respecte la grammaire

| Champ | Critère `b1-success-signal-spec.md` | Conformité |
|---|---|---|
| `intent` | Pourquoi ce mandat maintenant, dans le North Star | OK — réfère Ownerbook T1 §2 (« agency IS the product ») + couplage avec T2 (fournisseur interne) |
| `contraintes` | Limites non-négociables | OK — 4 contraintes, toutes sourcées (3 vetoes triplet v3 + 1 doctrine SOP canon) |
| `success_signal` | Mesurable ou observable, mesurable privilégié | OK — 3 compteurs (profils B3, SOPs, sprints), seuil (2/3 à 70%), délai (60j) |

**Type de signal : mesurable.** Trois compteurs naturels, sources de
vérité vérifiables (filesystem `find .claude/agents -name 'b3-*.md'`,
SPRINTS.md de chaque VP, registre SOP canon). Pas besoin d'un substitut
observable.

## Acceptance check — trois capitaines B2

Les trois capitaines B2 destinataires du Rock B1-1 doivent attester
chacun en 24h (cf. `b1-mandate-acceptance-check.md`) :

| Captain | Domaine | Ce qu'il atteste |
|---|---|---|
| **Green Lantern** | People (07) | Reformulation intent → staffing reproductible des squads X-Men ; contrainte recrutement-sans-mandat tenue ; DoD-Una : 3 critères (profil canon, B2 owner, horizon H10/H30/H90) par agent onboardé |
| **Batman** | Ops (04) | Reformulation intent → procédures Ops avec conditions d'arrêt ; DoD-Una : 3 procédures (ProcessDesign MrFantastic, Incidents HumanTorch, handoff cycle sprint) |
| **Flash** | Product (03) | Reformulation intent → SOP canon dépersonnalisées (offre survivant au remplacement de l'opérateur) ; DoD-Una : 3 SOPs (Recruiting ProfessorX, Onboarding CaptainAmerica, SOP Canon Bibliothèque Avengers) |

Si l'un des trois échoue à attester, le mandat est multi-destinataires
et doit passer par le **B2 Council** (cf. `b2-council-arbitrage-rule.md`)
avant acceptance. Mode `negotiation` probable : Green Lantern et Flash
peuvent diverger sur la définition d'une « offre dépersonnalisée » si
le recrutement ProfessorX incarne un profil qui vaut par son nom.

## Ce que ce mandat n'est PAS

- **Pas un DoD de SOP.** Le DoD de chaque SOP est posé par le B2
  captain (3 critères minimum) après acceptance, puis transformé en
  JTBD B3.
- **Pas une décision de staffing.** Qui recruter, sur quel profil,
  avec quel horizon — c'est People + Ops en mode B2, pas B1.
- **Pas un arbitrage North Star.** Le pivot Agency-as-a-Service est
  déjà acquis dans le Ownerbook T1 ; le mandat opère, il ne
  re-décide pas la doctrine.

## Le couplage avec T2 et T3

T1 est le **fournisseur interne** de T2 et T3 :
- T2 (Growth+Sales+Finance) a besoin des SOPs canon pour vendre
  (offre reproductible Flash) et des squads B3 staffed pour exécuter
  (delivery Illuminati + Guardians + Thunderbolts).
- T3 (Legal+R&D) a besoin du ProcessDesign MrFantastic pour documenter
  les procédures de conformité (365 Conformité) et du staffing Cyborg
  pour la R&D External Discovery.

Si T1 échoue, **T2 et T3 ne peuvent pas pivoter** — leur capacité
opérationnelle dépend de la supply chain People+Ops+Product. Le mandat
T1 doit donc être émis **avant** T2 et T3 en matière de cadence, ou
du moins simultanément. Émettre T1 en second crée un risque de
stalled commercial pipeline.

## Sources

- `omk-business-os.md` — Triptyque V4, status ACTIVE 2026-07-15.
- `ownerbook_T1_people_ops_product.md` — Rock B1-1 et ses DoD-1
  (référencée, Ownerbook lui-même non lu intégralement dans cette passe).
- `fifty-three-b3-agent-roster.md` — les 8 squads et leurs
  minimums (`≥ 7 agents par squad`).
- `v3-business.jsonl` lignes 23-25 — les 3 vetoes
  (Green Lantern / Batman / Flash).

## Liens

- [[b1-omk-t2-pivot-us-mandate]] — l'exemple isomorphe T2
- [[b1-mandate-packet-spec]] — la grammaire du paquet
- [[b1-success-signal-spec]] — la règle de choix du signal
- [[b1-mandate-acceptance-check]] — le verrou d'acceptance
- [[b1-cycle-rollover-protocol]] — la mécanique de mesure
- [[b2-council-arbitrage-rule]] — le routage multi-domaine
- [[fifty-three-b3-agent-roster]] — le squad 53 B3

## Note de confiance

**Confirmé par machine.** Mandat calibré à partir des éléments
explicites du corpus (Ownerbook T1 référencé, triplet v3 lignes 23-25
verbatim, roster 53 B3 vérifiable). Le Ownerbook T1 lui-même n'a pas
été lu intégralement (chemin ASpace_OS_V2, hors-périmètre d'écriture) ;
les cibles chiffrées (7 agents/squad, 3 SOPs, 8 sprints) sont des
**estimations raisonnables** extrapolées de `fifty-three-b3-agent-roster.md`
et des cadences B2 sprint/semaine. Le couplage T1↔T2/T3 (fournisseur
interne ↔ clients) est reconstruit, pas cité.