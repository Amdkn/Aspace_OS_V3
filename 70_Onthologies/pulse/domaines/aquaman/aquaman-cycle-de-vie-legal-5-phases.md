---
type: Concept
title: Cycle de vie Legal Aquaman — 5 phases de l'engagement au binder
description: Analogue au cycle de vie Ops Batman (5 phases : Conception → Pilote → Production → Revue → Arrêt), le cycle de vie Legal Aquaman aligne le pipeline Rock→DoD→JTBD sur le 12WY de Summers en 5 phases : Intake → Scoping → Drafting → Review → Binder. Chaque phase a un DoD chiffré, un squad lead B3 cible, et un Aquaman veto possible. La phase 4 Review aligne les 4 formes émises (privacy / claim / IP / contract) et la phase 5 Binder correspond au triple signature Aquaman + Batman + Thena du concept 11 tour 3.
tags: [b2, aquaman, legal, cycle-de-vie, 5-phases, intake, scoping, drafting, review, binder, 12wy]
generated: { by: minimax-m3, at: 2026-08-19T06:00:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-5, at: 2026-08-19T06:00:00Z }
sources:
  - id: triplet-6-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 6 — Summers tient un cycle mensuel (12WY)"
    last_modified: 2026-08-17
  - id: triplet-10-sprint
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 10 — chaque VP coupe le rock en 4 sprints hebdomadaires"
    last_modified: 2026-08-17
  - id: triplet-30-aquaman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 30 — Aquaman bloque engagement-sans-périmètre"
    last_modified: 2026-08-17
  - id: omk-pipeline
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md"
    title: "Pipeline Rock→DoD→JTBD Aquaman — frontmatter status: SHADOW_ACTIVE"
    last_modified: 2026-05-27
  - id: batman-5-phases
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-cycle-vie-procedure-ops-cinq-phases.md"
    title: Cycle de vie d'une procédure Ops — 5 phases
    last_modified: 2026-08-19
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: Contrat B2→B3 — durée sprint + DoD chiffré
    last_modified: 2026-08-19
  - id: aquaman-jtbd-emit-receive
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-jtbd-emit-receive.md"
    title: Aquaman — 4 formes émises (privacy/claim/IP/contract) + 4 reçues
    last_modified: 2026-08-19
  - id: aquaman-defensibility
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-defensibility-triple-signature.md"
    title: Aquaman — defensibilité triple signature (Aquaman + Batman + Thena)
    last_modified: 2026-08-19
  - id: aquaman-dormant-activation
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-dormant-activation.md"
    title: Aquaman — tri-partition Dormant / SHADOW_ACTIVE / ACTIVE
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cycle de vie Legal Aquaman — 5 phases

## Le trou comblé

Le rapport tour 1 a signalé que la durée d'un dossier Legal Aquaman
n'est pas posée (mensuelle, trimestrielle, 12WY ?). Le pipeline
Rock→DoD→JTBD du dossier OMK pose les 4 fichiers canoniques mais
**ne pose pas la durée d'un dossier**. C'est la même zone d'ombre
que Batman Ops tour 3 cycle-de-vie.

Ce concept propose un cycle de vie en **5 phases** aligné sur le
12WY de Summers et calé sur les 4 formes émises par Aquaman
([[aquaman-jtbd-emit-receive]]).

## Le tableau des 5 phases

| Phase | Durée typique | DoD chiffré | Owner B3 | Veto Aquaman possible |
|---|---|---|---|---|
| **1. Intake** | 1-2 jours | Engagement scope écrit, perimeter owner identifié, gating inputs vérifiés | Thena (Engagement) | Oui — `engagement-sans-périmètre` (triplet 30) |
| **2. Scoping** | 2-5 jours | Périmètre tracé (livrables + ownership), data inventory complet, claims draftées | Phastos (IP) + Ikaris (Compliance) | Oui — `périmètre insuffisant` (concept 10 tour 3 amplification candidate) |
| **3. Drafting** | 1-2 sprints | Privacy review draft, claims re-written, IP clauses reviewed, contract templated | Ajak (Compliance) + Druig | Oui — `claim-litigieuse` (veto catalogue natif) |
| **4. Review** | 1 sprint | Privacy review signée, claims safe, IP/property tracée, contract clauses validées | Sersi (Compliance) + Makkari (Compliance) | Oui — veto amplification `IP non déclarée` (concept 10 tour 3) |
| **5. Binder** | 1 sprint + archivage | Triple signature (Aquaman + Batman + Thena) [[aquaman-defensibility]], archivage D4, `LEGAL_READY` ou `BLOCKED_RISK` émis | Thena (Engagement) + Aquaman | Non — phase terminale |

**Durée totale** : 3-7 sprints (3-7 semaines), selon la
complexité du dossier. Un dossier "standard" tient sur 4 sprints ;
un dossier "complexe" (multi-parties, IP sensible) peut monter à
12 sprints.

## Phase 1 — Intake (1-2 jours)

**Objectif** : poser l'engagement par écrit avec un périmètre
minimum et identifier le squad lead B3.

**Inputs** :

- Un **trigger** amont — `B2-MESO-DECISION-YYYY-NN` accepté, ou un
  deal JohnJones pré-qualifié, ou un signal client direct
  (pair-check #11).
- Une **checklist gating** — les gating inputs nécessaires pour
  démarrer un dossier Aquaman (cf. [[aquaman-gating-inputs-jtbd-packet]]).

**Outputs** :

- Un **engagement scope** au format `engagement_scope.yaml`,
  contenant : parties prenantes, livrables attendus, propriété
  intellectuelle pressentie, claims anticipées, budget Legal
  pressenti (cohérence avec Wonder Woman), date de revue cible.
- Un **Intake packet** `B3-JTBD-YYYY-NN-intake` signé conjointement
  par Aquaman (B2 sponsor) et Thena (B3 lead).

**Veto Aquaman possible** :

- **Triplet 30 verbatim** : *engagement-sans-périmètre*. Un Intake
  sans périmètre écrit déclenche le veto et bloque la phase.
- **Aberration 1** : un Intake qui s'auto-déclare périmètre
  suffisant sans avoir les inputs amont (par ex. Sans Flash feature
  spec) doit escalader Aquaman pour amplification `périmètre
  insuffisant` (cf. concept 10 tour 3).

## Phase 2 — Scoping (2-5 jours)

**Objectif** : tracer le périmètre complet du livrable, inventorier
les données impliquées, vérifier que les claims anticipées ont une
base défendable.

**Inputs** :

- L'**engagement scope** signé en phase 1.
- Les **gating inputs amont** : feature spec Flash, claim draft
  Superman, deal structure JohnJones, privacy implementation spec
  Cyborg.

**Outputs** :

- Un **périmètre tracé** `perimeter.yaml` — liste des livrables
  avec owner, dépendance, latence de revue.
- Une **data inventory** complète — catégories de données
  impliquées, régimes de rétention, obligations RGPD ou locales.
- Une **claim draft list** — claims publiques anticipées, à passer
  en revue phase 4.
- Un **Scoping packet** `B3-JTBD-YYYY-NN-scope` signé Aquaman +
  Thena + Ikaris (Compliance).

**Veto Aquaman possible** :

- **Amplification candidate `périmètre insuffisant`** : un scoping
  qui pose un périmètre technique sans périmètre contractuel —
  Aquaman bloque et exige périmètre contrat écrit.
- **Pas de data inventory** : si la feature touche des données
  personnelles, un Scoping sans inventory déclenche le veto Privacy.

## Phase 3 — Drafting (1-2 sprints)

**Objectif** : produire les drafts (privacy review, claims
re-written, IP clauses, contract template) qui passeront en revue
phase 4.

**Inputs** :

- Le **périmètre tracé** signé phase 2.
- La **claim draft list** phase 2.
- Les **templates Legal** (Aquaman ACTIVE uniquement — les drafts
  en SHADOW_ACTIVE sont des `DRAFT_FOR_REVIEW`, pas des templates).

**Outputs** :

- Un **privacy review draft** (si gating input Cyborg était
  présent).
- Des **claims re-writtenes** (réécriture des claims phase 2 pour
  passer le filtre Aquaman).
- Des **clauses IP et propriété** dans le draft contrat.
- Un **contract template draft** — soit depuis un template Legal
  canon, soit construit pour ce dossier.
- Un **Drafting packet** `B3-JTBD-YYYY-NN-draft` signé Aquaman +
  Ajak (Compliance) + Phastos (IP).

**Veto Aquaman possible** :

- **Claim-litigieuse** : un draft qui contient une claim non
  défendable. Aquaman émet `BLOCKED_RISK` et la claim doit être
  réécrite.
- **IP non déclarée** (amplification candidate concept 10) : un
  draft qui utilise un asset tiers sans déclaration de propriété.

## Phase 4 — Review (1 sprint)

**Objectif** : faire passer chaque draft produit en phase 3 par
une revue croisée Aquaman — c'est la phase qui aligne les **4
formes émises** (privacy, claim, IP, contract) en séquence.

**Inputs** :

- Les **drafts phase 3** (privacy, claims, IP clauses, contract).
- Le **data inventory phase 2** pour re-vérification Privacy.

**Outputs** :

- Un **privacy review signé** — Privacy/Data formellement validée
  par Aquaman (équivalent `LEGAL_READY` sur la forme privacy).
- Des **claims safe** — chaque claim publique a une base
  factuelle et une formulation validée.
- Un **IP/property traced** — chaque clause IP pointe vers une
  entité propriétaire (interne ou tiers déclaré).
- Un **contract clauses validé** — chaque clause a une référence
  Legal (NDA master, terms of service, etc.).
- Un **Review packet** `B3-JTBD-YYYY-NN-review` signé Aquaman +
  Sersi + Makkari (Compliance).

**Veto Aquaman possible** :

- **Privacy review négatif** : si la review produit un
  `BLOCKED_RISK` privacy, le dossier retombe en phase 3 (et non
  en phase 5) — la phase 4 est un point de contrôle, pas une
  étape linéaire.
- **Claim toujours litigieuse après réécriture** : amplification
  du veto phase 3.

## Phase 5 — Binder (1 sprint + archivage)

**Objectif** : assembler le binder de défense, appliquer la triple
signature [[aquaman-defensibility]], émettre le packet Council
final.

**Inputs** :

- Les **drafts signés** phase 4.
- Le **template de binder** (Aquaman ACTIVE uniquement, sinon le
  binder reste `DRAFT_FOR_REVIEW`).

**Outputs** :

- Un **binder PDF signé** — assemblage des privacy review + claims
  safe + IP tracé + contract final.
- Une **triple signature** (Aquaman + Batman + Thena) au sens du
  concept 11 tour 3 — Batman parce que la procédure Ops doit
  intégrer les conditions d'arrêt contractuelles, Thena parce que
  c'est le squad lead B3 de l'engagement.
- Un **packet Council final** `B2-MESO-DECISION-YYYY-NN` (si le
  mandat était mésoperpétuel) ou `LEGAL_READY` / `BLOCKED_RISK`
  (si dossier B2 standard) émis.
- **Archivage D4** : tous les packets phase 1-5 + binder pushés
  dans le journal Council + archivage Coach-OS ou V3.

**Veto Aquaman possible** :

- **Aucun**. La phase 5 est terminale. Si Aquaman refuse de
  signer, le dossier **n'aboutit pas** — c'est un `BLOCKED_RISK`
  avec motif "dossier non-binderable".

## L'asymétrie avec le cycle de vie Ops Batman

Le cycle Ops Batman (cf. [[batman-cycle-vie-procedure-ops-cinq-phases]])
a les phases *Conception / Pilote / Production / Revue / Arrêt*. Le
cycle Legal Aquaman a *Intake / Scoping / Drafting / Review / Binder*.

**Trois asymétries structurelles** :

| Aspect | Ops Batman | Legal Aquaman |
|---|---|---|
| **Phase terminale** | Arrêt (procédure peut être arrêtée) | Binder (dossier ne peut pas être arrêté — il faut signer ou refuser) |
| **Veto** | Batman bloque les phases 1-4 sans condition d'arrêt | Aquaman bloque les phases 1-4 mais ne peut pas bloquer phase 5 (il signe ou refuse) |
| **Owner transversal** | Batman seul | Triple signature Aquaman + Batman + Thena (phase 5) |

**Conséquence** : le cycle Legal est *plus séquentiel* que le
cycle Ops. Un dossier Aquaman ne peut pas sauter de phase — chaque
phase a un DoD chiffré qui conditionne la suivante. Le cycle Ops
peut avoir des rework loops ; le cycle Legal a des *retours en
arrière* (phase 4 → phase 3 si un draft est invalide).

## Le calage sur le 12WY de Summers

Le triplet 6 pose *« Summers tient un cycle mensuel (12WY) »* ; le
triplet 10 pose *« chaque VP coupe le rock en 4 sprints
hebdomadaires »*.

**Calage** :

- 1 dossier Legal standard (4-5 sprints) = 1 sprint VP (1 mois) —
  peut courir sur 1 mois complet si Sprint VP mensuel découpé en
  4 sprints hebdo.
- 1 dossier Legal complexe (12 sprints) = 3 sprints VP (3 mois) —
  doit être posé en Rock B2 dès le départ, sinon il déborde.
- 1 archivage Binder (1 sprint) = sprint de fin de Rock B2, aligné
  sur la clôture VP.

**Conséquence** : un dossier Aquaman qui dépasse 12 sprints (3 mois)
doit être posé en Rock B2 dès le départ, avec Aquaman comme
sponsor B2 et Aquaman ACTIVE obligatoire (sinon le dossier n'aboutit
pas — triplet 36 : `Legal dependsOn premier contrat signé`).

## Les 4 formes émises ↔ les 5 phases — table de correspondance

Les 4 formes émises canoniques (concept tour 2) trouvent leur phase
de production :

| Forme émise | Phase de production | Owner B3 | DoD chiffré |
|---|---|---|---|
| **Privacy review** | Phase 4 Review | Sersi (Compliance) | RGPD / RGPD-local §, retention ≤ 730j, chiffrement at-rest ✓ |
| **Claim safety** | Phase 3 Drafting + Phase 4 Review | Druig → Makkari | 0 claim litigieuse non-réécrite, base factuelle chiffrée |
| **Contract template** | Phase 3 Drafting | Ajak (Compliance) | Template Legal canonique, clauses IP + perimeter + property tracées |
| **Defensibility doc** | Phase 5 Binder | Thena (Engagement) + Aquaman | Triple signature, archivage D4, `LEGAL_READY` émis |

**Conséquence** : la liste des 4 formes émises du concept tour 2
prend sa **place dans le cycle** — chaque forme a une phase,
un owner B3, un DoD chiffré.

## La gating condition revisitée

[[aquaman-gating-inputs-jtbd-packet]] (tour 3) pose un champ
`gating_inputs:` optionnel au gabarit JTBD packet. Chaque forme
émise a sa gating condition côté reçu. Le cycle 5 phases les
réutilise comme **gating entre phases** :

| Gating input | Phase qui le requiert | Forme émise bloquée si manquant |
|---|---|---|
| Feature spec Flash | Phase 2 Scoping | Privacy review impossible phase 4 |
| Claim draft Superman | Phase 2 Scoping | Claim safety impossible phase 3 |
| Deal structure JohnJones | Phase 1 Intake | Contract template impossible phase 3 |
| Privacy implementation spec Cyborg | Phase 3 Drafting | Privacy review impossible phase 4 |

## Anti-pièges

- **Sauter la phase 2 Scoping**. Un dossier qui passe directement
  Intake → Drafting produit des drafts sans data inventory ni
  perimeter trace. Phase 4 Review sera un nid à veto Privacy.
- **Confondre phase 4 Review et phase 5 Binder**. La phase 4 signe
  les drafts (revue). La phase 5 signe le binder. Une signature
  de binder sans revue des drafts produit un `BLOCKED_RISK`
  automatique.
- **Aquaman SHADOW_ACTIVE en cycle**. Un cycle 5 phases ne peut
  pas aboutir en SHADOW_ACTIVE — la phase 5 Binder exige
  `LEGAL_READY` ou `BLOCKED_RISK` signé, ce qui force le passage
  à ACTIVE. Conséquence : un dossier Aquaman ACTIVE-signé pendant
  un cycle = Aquaman devient ACTIVE pour la suite (cf. concept 1
  tour 5).
- **Owner B3 non formé au cycle**. Les 5 phases sont des
  conventions B3 squad Lead ; un squad lead Eternals non formé
  (par exemple non-créé sur disque, cf. concept 13 tour 3)
  produit des phases livrées à moitié. Recompte 0 fichier reste
  un blocage de fait.

## Liens

- [[batman-cycle-vie-procedure-ops-cinq-phases]] — l'analogue Ops
- [[aquaman-jtbd-emit-receive]] — les 4 formes émises qui se
  déploient sur le cycle
- [[aquaman-defensibility-triple-signature]] — la triple signature
  phase 5
- [[aquaman-dormant-activation]] — la tri-partition qui détermine
  si le cycle peut aboutir
- [[aquaman-gating-inputs-jtbd-packet]] — le champ `gating_inputs:`
  qui sert de gating entre phases
- [[b2-b3-jtbd-handoff-contract]] — la durée sprint + DoD chiffré
  qui calibre chaque phase

## Note de confiance

**Confirmé par machine pour les sources ; reconstruit pour la
projection 5 phases.**

- ✅ Triplet 6, triplet 10, triplet 30 cités verbatim.
- ✅ 4 fichiers OMK posés en SHADOW_ACTIVE, datés 2026-05-25 et
  2026-05-27.
- 🟡 La projection 5 phases : calquée sur le cycle Ops Batman
  (analogue) et les 4 formes émises (concept tour 2). L'alignement
  des phases sur les formes émises est une **projection**
  opérationnelle, pas une citation canonique.
- 🟡 Les phases 1-5 durations (1-2 jours, 2-5 jours, 1-2 sprints,
  1 sprint, 1 sprint + archivage) sont **extrapolées** depuis la
  pratique Sprint VP (triplet 10) et les 4 dossiers OMK. **Pas de
  cycle Aquaman réel observé** pour calibrer.
- ❌ Non vérifié en cycle : aucun dossier Legal Aquaman n'a
  traversé les 5 phases en Vague 2. Concept **projeté depuis le
  framework**, à tester en cycle réel dès le premier Master
  Agreement signé.
