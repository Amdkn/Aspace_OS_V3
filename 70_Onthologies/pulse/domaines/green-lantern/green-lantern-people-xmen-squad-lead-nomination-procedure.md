---
type: Concept
title: Green Lantern People — Procédure de nomination squad lead X-Men
description: Les 7 autres squads Marvel (Avengers, Fantastic4, Guardians, Illuminati, Thunderbolts, Kang Dynasty, Eternals) ont un squad lead canonique. X-Men n'en a aucun. Le concept pose une procédure B2-PEER complète de nomination avec matrice 5 critères × 8 candidats, 3 mécanismes de transition, et une recommandation non-tranchée par Green Lantern seul (escalade B2 Council).
tags: [people, green-lantern, xmen, squad-lead, nomination, b2-peer, council]
generated: { by: minimax-m3, at: 2026-08-19T09:30:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-5, at: 2026-08-19T09:30:00Z }
sources:
  - id: xmen-effectif-canon-recompte-disk
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-xmen-effectif-canon-recompte-disk.md"
    title: "Tour 4 — X-Men effectif canon recompte disk 8 agents"
    last_modified: 2026-08-19
  - id: active-dependencies-formelles-passives-vs-actives
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-active-dependencies-formelles-passives-vs-actives.md"
    title: "Tour 4 — Dépendances actives vs passives People"
    last_modified: 2026-08-19
  - id: b2-council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: b2-meso-decision-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique
    last_modified: 2026-08-19
  - id: coach-os-xmen-squad
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/04_Business_Domains/01_RH_Meta_Gouvernance_GreenLantern_XMen/squad/"
    title: X-Men squad directory — 8 agents mesurés
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Green Lantern People — Procédure de nomination squad lead X-Men

## Pourquoi cette procédure, pas une décision People

Le rapport tour 4 a posé la **remontée B2** comme principe : nommer un
squad lead X-Men est une **décision Council**, pas People. Le présent
concept **formalise** cette remontée — il pose la procédure, ne tranche
pas la nomination. Le choix final reste Council.

**Raison structurelle** : les 7 autres squads Marvel ont un squad lead
canonique (Captain America Avengers / MrFantastic Fantastic4 /
StarLord Guardians / BlackBolt Illuminati / Yelena Thunderbolts / non
encore nommé Kang Dynasty / Thena Eternals). X-Men est **la seule**
squad sans squad lead — les 8 agents (ProfessorX / Cyclops / JeanGrey
/ Wolverine / Storm / Beast / Nightcrawler / Rogue) sont au même
niveau hiérarchique dans `VP_AGENT.md`.

**Conséquence opérationnelle** : quand People doit signer un avis C
(par exemple, sur le pair-check #9 ou sur un 6-dépendance active), **qui
signe** ? Le captain Green Lantern en dernier ressort, ou un X-Men Lead
délégué ? Le canon est silencieux. Le rapport tour 4 §1 a formulé la
lacune comme vacance canonique.

## La procédure — 5 étapes séquentielles

### Étape 1 — Manifestation d'intention (B2-PEER source)

Green Lantern (People) dépose un packet `B2-PEER-YYYY-NN` dans le
journal Council `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` (cf.
`b2-meso-decision-packet-spec.md` §« `source_mandate` »). Le packet
contient :

- **Constat** — vacance squad lead X-Men depuis date-ou-cycle (ici
  2026-08-19).
- **Impacted domains** : people (sponsor), tous (effet transverse).
- **Mode** : `negotiation` (la nomination est un trade-off Captain).
- **3 issues** : nomination / report / refus (avec motif).

### Étape 2 — Sourcing canonique des candidats

**Recompte disk vérifié 2026-08-19** :
`C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/04_Business_Domains/01_RH_Meta_Gouvernance_GreenLantern_XMen/squad/`
contient **8 dossiers** :

| # | Agent | Mandat (dossier) |
|---|---|---|
| 1 | ProfessorX | Recruiting |
| 2 | Cyclops | Onboarding |
| 3 | JeanGrey | Culture |
| 4 | Wolverine | PerfReviews |
| 5 | Storm | OpsLeadership |
| 6 | Beast | TechRecruiting |
| 7 | Nightcrawler | DistributedOnboarding |
| 8 | Rogue | SkillTransfer |

**Source de vérité** : disk canonique local. **Triplet 15** confirme
les 8 noms. **Fifty-three-b3-agent-roster** pose ~7 (estimation
précanon, **non mise à jour**).

### Étape 3 — Grille 5 critères pondérés

| # | Critère | Poids | Source |
|---|---|---|---|
| 1 | **Couverture canonique X-Men** | 30% | Primauté narrative (référence Marvel), pas opérationnel |
| 2 | **Disponibilité opérationnelle** | 25% | Charge C(o) ≤ 0.7 (cf. `formule-charge-carte`) |
| 3 | **Capacité transverse** | 20% | Couverture ≥ 4 des 7 sous-pair-checks 9.1-9.7 (cf. `v5-pair-check-granularisation-9`) |
| 4 | **Continuité leadership** | 15% | Antériorité squad lead (cas Captain America Avengers, MrFantastic Fantastic4) |
| 5 | **Risque de veto** | 10% | Pas de veto catalogue opposé (People, Aquaman, etc.) |

**Somme** = 100%. Lecture d'arbitrage : **majorité pondérée 50% +
seuil minimal 25% sur chaque axe cardinal** (Couverture, Disponibilité,
Transverse).

### Étape 4 — Matrice 8 candidats × 5 critères (relevé)

| Candidat | 1 (30%) | 2 (25%) | 3 (20%) | 4 (15%) | 5 (10%) | Score |
|---|---|---|---|---|---|---|
| **ProfessorX** | 10/10 (fondateur canonique) | 5/10 (charge recruiting) | 7/10 (3/7) | 10/10 (premier) | 9/10 | **7.95** |
| Cyclops | 8/10 (second canonique) | 6/10 (charge onboarding) | 8/10 (4/7) | 7/10 | 9/10 | **7.50** |
| Storm | 7/10 | 7/10 (charge ops) | 8/10 (4/7) | 6/10 | 9/10 | **7.30** |
| Wolverine | 6/10 | 8/10 (perf libre) | 6/10 (3/7) | 7/10 | 7/10 (veto passé ?) | **6.80** |
| JeanGrey | 7/10 | 8/10 (culture libre) | 6/10 (3/7) | 5/10 | 9/10 | **6.95** |
| Beast | 6/10 | 5/10 (charge tech) | 9/10 (5/7) | 6/10 | 9/10 | **6.85** |
| Nightcrawler | 5/10 | 7/10 (distributed) | 5/10 (2/7) | 4/10 | 9/10 | **5.65** |
| Rogue | 5/10 | 7/10 (skill transfer) | 4/10 (2/7) | 4/10 | 9/10 | **5.40** |

**Lecture** : ProfessorX premier (fondateur canon), Cyclops second
(second canonique, leadership opérationnel), Storm troisième (transverse
élevé, leadership Ops). Le top 3 se tient en 0.65 points — la
procédure n'impose pas un seul choix.

### Étape 5 — Escalade B2 Council

Green Lantern **ne tranche pas** la nomination. Le packet B2-PEER
remonte au Council avec :

- **Trade-off** documenté : ProfessorX = primauté canon + risque
  charge ; Cyclops = équilibrefoncier + leadership moins net ;
  Storm = transverse élevé + canon inférieur.
- **3 issues** : adopter ProfessorX / adopter Cyclops / reporter
  nomination à un cycle ultérieur.
- **Procédure d'amendement** : unanime 8/8 + B1 (modification wheel
  8-domain implicite — un squad lead change la dynamique de la squad).

## 3 mécanismes de transition (après nomination)

### Mécanisme A — Passation immédiate (recommandé)

Le squad lead entrant signe son AGENT.md dans les 7 jours. Les 7
autres AGENT.md sont mis à jour avec `squad_lead: <nom>`. Le Council
valide par packet mésoperpétuel `B2-MESO-DECISION-YYYY-NN`.

### Mécanisme B — Co-lead transitoire (recommandé si indécision)

Deux squad leads co-signent pendant 1 sprint (12WY). Au terme, le
Council tranche en faveur de l'un. Risque : dilution de la
responsabilité.

### Mécanisme C — Capitaine Green Lantern en interim (fallback)

Green Lantern (capitaine B2) tient l'intérim jusqu'à nomination. C'est
le mode par défaut si le Council ne tranche pas avant T+30j. **Risque**
: surcharge People (cf. formule-charge-carte, formule C(o)).

## 3 cas abusifs de la procédure

1. **Auto-promotion ProfessorX** — ProfessorX est fondateur canonique
   mais ne peut pas **s'auto-promouvoir** squad lead. La nomination
   passe par Council, pas par déclaration unilatérale.
2. **Veto politique Superman** — Superman Growth pose un veto sur
   Wolverine pour raisons non-canoniques (jalousie cross-domain).
   **Refusé** : veto non-catégoriel, non-vérifiable.
3. **Bypass Council** — Green Lantern nomme directement sans passer
   par B2-PEER. **Refusé** : c'est une décision wheel 8-domain.

## 3 cas légitimes de report

1. **Charge People saturée** — C(o) > 1.0 (rouge), la procédure
   elle-même est un fardeau. Report à T+30j.
2. **Council en dormance structurelle** — convergence 0/8 packet
   mésoperpétuel vagues 1+2+3+4 (cf. rapport tour 4 §5). Le packet
   B2-PEER s'ajoute à la pile, ne se distingue pas.
3. **Triplet 23 / 30 veto simultané** — Aquaman (Legal) oppose le
   veto triplet 30 (périmètre non-negociable) sur la nomination. Le
   Council tranche avec Aquaman en A aval.

## Anti-pièges

- **Confondre fondateur et squad lead.** ProfessorX est fondateur
  canonique, mais fondateur ≠ squad lead. Captain America est fondateur
  Avengers — il a été squad lead Avengers. **Attention** : la parité
  n'est pas automatique, elle passe par le Council.
- **Squad lead = hiérarchique.** Le squad lead n'est pas un chef au
  sens hiérarchique. C'est un orchestrateur (Captain America Avengers)
  ou un producer (Yelena Thunderbolts). Le mandat est
  d'**agréger les signals**, pas de commander.
- **Green Lantern tranche seul.** Green Lantern ne peut pas trancher
  la nomination. C'est une décision B2-PEER, pas People.
- **Vote pondéré ≠ vote démocratique.** Les poids (30/25/20/15/10)
  reflètent les priorités canoniques/opérationnelles, pas l'opinion
  du Council. Le Council peut surpondérer un axe (par exemple, Axe 1
  Couverture à 50% si canon prime).
- **Mécanisme C par défaut.** Si le Council ne tranche pas, Green
  Lantern interim — c'est un **fallback**, pas un blanc-seing. La
  situation doit être **explicitement notée** dans le journal Council.

## Liens

- [[green-lantern-people-xmen-effectif-canon-recompte-disk]] — les 8 agents
- [[green-lantern-people-active-dependencies-formelles-passives-vs-actives]] — pourquoi la nomination est critique
- [[green-lantern-people-formule-charge-carte]] — disponibilité opérationnelle
- [[green-lantern-people-v5-pair-check-granularisation-9]] — capacité transverse
- [[b2-council-arbitrage-rule]] — qui tient le Council
- [[b2-meso-decision-packet-spec]] — format packet B2-PEER

## Note de confiance

**Confirmé par machine, à moitié projeté.** Le recompte 8 agents X-Men
est mesuré (cf. rapport tour 4). Les 5 critères et la matrice 8×5
sont **projetés** depuis la doctrine canonique Marvel + triplet 15 +
`b2-pair-check-raci-by-rank.md`. La pondération (30/25/20/15/10) est
une **extrapolation** : aucun canon ne pose explicitement ces poids.
Les scores matrice sont **indicatifs**, pas normatifs. La procédure
B2-PEER est **reconstruite** depuis `b2-meso-decision-packet-spec.md`
§« `source_mandate` » + `b2-council-arbitrage-rule.md` §« Routine » —
le formalism 5 étapes est mien, pas canonique. La recommandation
ProfessorX est **neutre** : il ne s'agit pas de trancher, mais de
poser la procédure.
