---
type: Concept
title: Flash Product — sources JTBD closed-loop, 4 questions ouvertes fermées + 3 cas chaînés
description: Le tour 1 a listé 6 sources JTBD entrantes mais a laissé 4 questions ouvertes (People onboarding format, Ops handoff inverse, gate NEEDS_SCOPE chaînée, scope Squad multi-source). Le concept ferme ces 4 questions avec format YAML explicite, 3 cas chaînés (Sales→Product→Ops, People→Product→Finance, Legal→Product→Finance→Growth), et procédure de re-écification en cas de scope non-formalisé.
tags: [flash, product, jtbd, sources, closed-loop, people, ops, finance, chain, yaml]
generated: { by: minimax-m3, at: 2026-08-19T05:25:00Z }
verified:
  - { by: process:lecture-corpus-flash-tour-2, at: 2026-08-19T05:25:00Z }
sources:
  - id: flash-jtbd-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-jtbd-emit-receive.md"
    title: Flash — paquets JTBD émis et reçus (tour 1)
    last_modified: 2026-08-19
  - id: rapport-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-flash.md"
    title: Rapport de l'escouade Flash — vague 2 (tour 1) §"4 questions ouvertes sur JTBD sources"
    last_modified: 2026-08-19
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — JTBD packet format
    last_modified: 2026-08-19
  - id: b3-vocab
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-veto-and-signal-vocabulary.md"
    title: B3 veto and signal vocabulary — gates READY/BLOCKED par domaine
    last_modified: 2026-08-19
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Flash/Avengers
    last_modified: 2026-08-17
  - id: triplet-41
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 41 — B3 interdit-combler-trou"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Flash Product — sources JTBD closed-loop

## Les 4 questions ouvertes du tour 1

Le rapport tour 1 (`RAPPORT_dom-flash.md` §« Ouvert » lignes 31)
identifie 4 questions ouvertes sur les sources JTBD entrantes :

1. **People onboarding format** — quel est le format YAML du paquet
   JTBD Flash émis par Green Lantern pour onboarder un Avengers ? Le
   tour 1 cite le format général mais pas le **format People
   spécifique**.
2. **Ops handoff inverse** — quand Batman émet un paquet vers Flash
   (handoff inverse Product → Ops → Product), quel est le format ?
   Le tour 1 mentionne Ops comme source n°6 sans expliciter le handoff
   inverse.
3. **Gate NEEDS_SCOPE chaînée** — quand Flash émet `NEEDS_SCOPE`,
   comment le paquet remonte-t-il à la source amont (Sales, People,
   Finance, Legal) ? Le tour 1 mentionne la remontée mais pas le
   **mécanisme de chaînage**.
4. **Scope Squad multi-source** — quand plusieurs sources amont
   émettent simultanément (ex : Sales signe un deal ET People
   onboarde), comment le scope est-il consolidé ? Le tour 1 mentionne
   les 6 sources mais pas le mécanisme de **consolidation**.

Le concept ferme ces 4 questions avec format YAML explicite, 3 cas
chaînés, et procédure de re-formalisation.

## Format YAML explicite — paquet JTBD Flash entrant

Le format JTBD Flash entrant est une instanciation du format canonique
(cf. `b2-b3-jtbd-handoff-contract.md` §« Le format conjoint ») avec
les champs spécifiques à Flash :

```yaml
jtbd_packet_id: B3-JTBD-FLASH-YYYY-NN
source_domain: <growth|sales|people|finance|legal|ops>
intent: <verbe à l'infinitif décrivant l'intention du paquet>
scope:
  livrable: <description courte de l'artefact à produire>
  do_d_chiffre: <seuil chiffré : taux, latence, montant>
  cadence: <durée du sprint B3 en semaines>
squad_cible: avengers
contract_signed:
  b2_sponsor: flash
  b3_squad_lead: captainamerica
  signed_at: YYYY-MM-DD
proof_expected:
  forme: capture|log|metrique|temoignage
  chemin: <path-or-url>
indicators:
  lead: [<metrique>, <metrique>]
  lag: [<metrique>, <metrique>]
escalade:
  first_stop: flash  # B2 sponsor
  seuil_temps: 24h
```

Trois champs sont **spécifiques** à Flash :

1. **`source_domain`** — l'un des 6 (growth, sales, people, finance,
   legal, ops). Le champ est obligatoire — sans lui, le paquet est
   invalide (analogue au champ `source_mandate` du packet
   mésoperpétuel — cf. `b2-meso-decision-packet-spec.md` §«
   `source_mandate` »).
2. **`intent`** — verbe à l'infinitif décrivant l'intention du paquet.
   C'est le **JTBD** (Jobs To Be Done) — l'intention qui motive le
   paquet, pas le livrable.
3. **`squad_cible: avengers`** — Flash ne dispatche que vers Avengers.
   Un paquet JTBD Flash qui ciblerait un autre squad est invalide.

## Question 1 fermée — People onboarding format

Le paquet JTBD Flash émis par Green Lantern pour onboarder un Avengers
suit le format ci-dessus avec les champs spécifiques :

```yaml
jtbd_packet_id: B3-JTBD-FLASH-YYYY-NN
source_domain: people
intent: onboarder_agent_avengers
scope:
  livrable: <nom de l'agent Avengers, ex: scarletwitch>
  do_d_chiffre: <critère de sortie vérifiable — ex: "scope H90 transformation documenté">
  cadence: <durée d'onboarding : 2-4 semaines>
squad_cible: avengers
contract_signed:
  b2_sponsor: flash
  b3_squad_lead: captainamerica  # ou hawkeye selon scope
  signed_at: YYYY-MM-DD
proof_expected:
  forme: capture  # capture de la fiche b3-*.md ou du SOUL.md
  chemin: <chemin relatif vers la fiche agent>
indicators:
  lead: [<couverture de formation>, <nb de scrums tenus>]
  lag: [<scope tenu>, <DoD rempli>]
escalade:
  first_stop: flash  # B2 sponsor
  seuil_temps: 24h
```

Trois champs **distinctifs** :

- **`intent: onboarder_agent_avengers`** — verbe spécifique à People.
- **`do_d_chiffre`** porte le **critère de sortie** vérifiable (le
  veto Green Lantern canonique — triplet 25 — teste ce critère, mais
  Flash porte la cohérence avec Product).
- **`proof_expected.forme: capture`** — la preuve est la fiche
  `b3-*.md` de l'agent onboardé (analogue au triplet 41 — *« B3
  interdit-combler-trou »* : la fiche doit exister avant la première
  mission).

## Question 2 fermée — Ops handoff inverse

Le paquet JTBD Flash émis par Batman (handoff inverse) suit le format
ci-dessus avec les champs spécifiques :

```yaml
jtbd_packet_id: B3-JTBD-FLASH-YYYY-NN
source_domain: ops
intent: preparer_maintenance_artefact  # ou adapter_artefact_pour_run
scope:
  livrable: <nom de l'artefact à adapter>
  do_d_chiffre: <seuil de maintenabilité — ex: "taux d'incidents < 5/mois">
  cadence: <durée du handoff inverse : 1-2 semaines>
squad_cible: avengers
contract_signed:
  b2_sponsor: flash
  b3_squad_lead: captainamerica  # ou hulk selon scope
  signed_at: YYYY-MM-DD
proof_expected:
  forme: log  # log d'incidents passés ou runbook produit
  chemin: <chemin relatif vers le runbook>
indicators:
  lead: [<couverture du runbook>, <nb de SOPs produites>]
  lag: [<taux d'incidents réel>, <charge support tenable>]
escalade:
  first_stop: flash  # B2 sponsor
  seuil_temps: 24h
```

Trois champs **distinctifs** :

- **`source_domain: ops`** — Ops est la source amont dans le handoff
  inverse (rare, mais existe — cf. `flash-jtbd-emit-receive.md` §«
  6. Ops (Batman / Fantastic Four) »).
- **`intent: preparer_maintenance_artefact`** ou **`adapter_artefact_pour_run`**
  — verbes spécifiques à Ops.
- **`proof_expected.forme: log`** — la preuve est le runbook produit
  ou le log d'incidents.

**Note sur la rareté** : le handoff inverse Ops → Product est rare
parce que la matrice canonique pose Ops en **aval** de Product
(pair-check #3). Il se déclenche quand Batman détecte qu'un artefact
ne peut pas être maintenu en l'état (ex : logique algorithmique trop
complexe) et demande à Flash de l'amender.

## Question 3 fermée — Gate NEEDS_SCOPE chaînée

Quand Flash émet `NEEDS_SCOPE` (cf. `b3-vocab` §« Couche 2 »), le
paquet remonte **automatiquement** à la source amont via le mécanisme
de chaînage :

```yaml
jtbd_packet_id_returned: B3-JTBD-FLASH-YYYY-NN-RETURN
jtbd_packet_id_origin: B3-JTBD-FLASH-YYYY-NN
source_domain_origin: <la source amont qui a émis le paquet original>
intent: formaliser_scope
scope:
  livrable: <la clarification attendue — ex: "scope H90 transformation de ScarletWitch">
  do_d_chiffre: <seuil chiffré de la clarification>
  cadence: <durée de re-formalisation : 1 semaine>
squad_cible: <la squad amont — ex: x-men pour people, illuminati pour sales>
contract_signed:
  b2_sponsor: <le captain amont — ex: green_lantern>
  b3_squad_lead: <le lead amont — ex: professorx pour people>
  signed_at: YYYY-MM-DD
proof_expected:
  forme: capture  # capture du scope formalisé
  chemin: <chemin relatif vers le scope amendé>
escalade:
  first_stop: flash  # B2 sponsor originel
  seuil_temps: 24h
```

Cinq champs **distinctifs** :

- **`jtbd_packet_id_returned`** — id du paquet de retour (suffixe
  `-RETURN`).
- **`jtbd_packet_id_origin`** — id du paquet originel qui a émis le
  `NEEDS_SCOPE`.
- **`source_domain_origin`** — la source amont qui a émis le paquet
  originel.
- **`intent: formaliser_scope`** — verbe spécifique du chaînage.
- **`squad_cible`** — la squad amont qui porte la re-formalisation.

**Le paquet de retour est signé conjointement** par le B2 sponsor
originel (Flash) et le B2 sponsor amont (Green Lantern, JohnJones,
etc.). C'est la **double signature** du contrat B2 → B3 (cf.
`b2-b3-jtbd-handoff-contract.md` §« Le rôle du capitaine B2 sponsor »).

## Question 4 fermé — Scope Squad multi-source

Quand plusieurs sources émettent simultanément (ex : Sales signe un deal
ET People onboarde), Flash **consolide** les scopes en un seul
paquet Avengers. Format :

```yaml
jtbd_packet_id: B3-JTBD-FLASH-YYYY-NN
consolidation:
  sources: [<sales>, <people>]
  intent: <verbe à l'infinitif du scope consolidé>
scope:
  livrable: <livrable consolidé>
  do_d_chiffre: <seuil chiffré du scope consolidé>
  cadence: <durée du sprint B3 consolidé>
squad_cible: avengers
contract_signed:
  b2_sponsor: flash
  b3_squad_lead: captainamerica
  b2_cosigners: [<johnjones>, <green_lantern>]
  signed_at: YYYY-MM-DD
```

Trois champs **distinctifs** :

- **`consolidation.sources`** — liste des sources amont (au moins 2).
- **`b2_cosigners`** — co-signatures B2 des capitaines amont
  (analogue à la double signature B2 → B3, étendue à N capitaines).
- **`intent`** — verbe unique décrivant le scope consolidé.

**Procédure de consolidation** :

1. **Détection** — CaptainAmerica identifie que plusieurs paquets
   JTBD entrants concernent le même livrable.
2. **Regroupement** — CaptainAmerica agrège les paquets en un seul
   `jtbd_packet_id` avec `consolidation.sources`.
3. **Co-signature** — Flash convoque les capitaines amont pour
   co-signer le paquet consolidé. Chaque co-signeur valide que son
   scope est respecté.
4. **Dispatch** — le paquet consolidé est dispatché à Avengers avec
   `proof_expected` combinant les preuves des sources amont.

Si la consolidation est **impossible** (les scopes sont
contradictoires), Flash émet `NEEDS_SCOPE` vers chaque source amont,
et le chaînage (Question 3) prend le relais.

## Trois cas chaînés — quand Flash reçoit de plusieurs sources

### Cas 1 — Sales→Product→Ops (chaîne 3-domaines)

Sales signe un deal avec scope `coaching 6 mois premium`. Le paquet
arrive chez Flash. Flash produit l'artefact, puis envoie un paquet
Ops (handoff Phase 2 du triple-squad launch — cf.
`flash-triple-squad-launch-canon-protocol.md`). Batman produit le
runbook, puis Kang Dynasty déploie. Launch autorisé.

**Trois paquets chaînés** : `JTBD-FLASH-NN` (Sales) → `JTBD-FLASH-NN`
(Avengers) → `JTBD-FLASH-NN` (Ops handoff). Chaque paquet a sa
double signature, et les trois paquets sont tracés dans le journal
Council avec `meso_decision_id` unique.

### Cas 2 — People→Product→Finance (chaîne 3-domaines avec budget)

Green Lantern onboarde ScarletWitch (specialty H90 transformation
scope). Le paquet arrive chez Flash. Flash produit un livrable de
formation ScarletWitch, qui consomme un budget de formation.
Wonder Woman alloue le budget via un paquet Finance → Product. Flash
consolide People + Finance dans un seul scope Avengers.

**Trois paquets chaînés** : `JTBD-FLASH-NN` (People onboarding) →
`JTBD-FLASH-NN` (Finance budget) → `JTBD-FLASH-NN` (consolidé
People+Finance). Le paquet consolidé a 2 co-signeurs B2 (Green
Lantern + Wonder Woman).

### Cas 3 — Legal→Product→Finance→Growth (chaîne 4-domaines)

Aquaman déclare les frontières IP/privacy/terms. Flash applique les
frontières dans le code et l'UI (pair-check #2 — Legal → Product).
Wonder Woman chiffre le coût de mise en conformité (pair-check #6 —
Finance → Product). Superman Growth signale le besoin marché
(`GROWTH_READY`). Flash consolide les 3 sources amont en un seul
scope Avengers (Legal + Finance + Growth).

**Quatre paquets chaînés** : `JTBD-FLASH-NN` (Legal frontières) →
`JTBD-FLASH-NN` (Finance coût) → `JTBD-FLASH-NN` (Growth signal) →
`JTBD-FLASH-NN` (consolidé Legal+Finance+Growth). Le paquet
consolidé a 3 co-signeurs B2 (Aquaman + Wonder Woman + Superman).

## Procédure de re-formalisation en cas de scope non-formalisé

Quand un paquet amont arrive avec un scope **non-formalisé**
(`NEEDS_SCOPE` côté amont), Flash applique la procédure :

1. **Détection** — Flash lit le paquet amont et constate que le scope
   est en prose, pas chiffré.
2. **Émission NEEDS_SCOPE chaînée** — Flash émet un paquet de retour
   (Question 3) avec intent `formaliser_scope`.
3. **Attente** — Flash attend la reformalisation. Si le paquet de
   retour n'arrive pas sous 24h, Flash escalade au B2 sponsor amont
   (cf. `b2-b3-jtbd-handoff-contract.md` §« Le seuil d'escalade »).
4. **Reprise** — Quand le paquet amont reformalisé arrive, Flash
   agrège le scope dans le paquet Avengers (consolidation Question 4)
   ou poursuit la chaîne.

## Anti-pièges

- **Paquet JTBD émis sans `source_domain`.** Un paquet Flash sans
  source amont identifiable est invalide — CaptainAmerica ne sait pas
  à qui signaler un trou.
- **Paquet de chaînage sans `jtbd_packet_id_origin`.** Le paquet de
  retour NEEDS_SCOPE doit citer le paquet originel. Sans cette
  référence, le chaînage est cassé et Flash ne peut pas tracer
  l'historique.
- **Consolidation sans co-signature B2 amont.** Un paquet consolidé
  signé par Flash seul est un ordre, pas un contrat. Les capitaines
  amont doivent co-signer pour s'engager sur le scope.
- **Confondre handoff inverse et chaînage.** Le handoff inverse (Ops →
  Product) est **unidirectionnel** (Ops demande à Flash d'amender).
  Le chaînage (Product → Amont) est **bidirectionnel** (Flash demande
  à l'amont de reformaliser). Les deux ont des formats distincts.
- **CaptainAmerica qui consolide sans Flash.** La consolidation est
  une décision B2 (Flash), pas une décision B3 (CaptainAmerica).
  CaptainAmerica peut **proposer** la consolidation, mais Flash
  décide.

## Liens

- [[flash-jtbd-emit-receive]] — les 6 sources JTBD tour 1
- [[b2-b3-jtbd-handoff-contract]] — le contrat bilatéral B2 → B3
- [[b3-veto-and-signal-vocabulary]] — les gates READY/BLOCKED par domaine
- [[flash-triple-squad-launch-canon-protocol]] — la chaîne Avengers→Fantastic4→Kang Dynasty
- [[flash-pair-check-people-product-candidate-v5]] — la formalisation People → Product comme pair-check #10
- [[flash-domain-perimeter]] — les 4 frontières floues dont Sales → Product
- [[triplet-41-b3-interdit-combler-trou]] — l'interdit B3 qui pose la discipline de signalement

## Note de confiance

**Confirmé par machine, à moitié étayé.** Les 4 questions ouvertes
sont **identifiées** dans le rapport tour 1. Le format YAML général
est **instanciation** du format canonique
`b2-b3-jtbd-handoff-contract.md` §« Le format conjoint ». Les 3 cas
chaînés sont **reconstruits** à partir de la pratique observée et des
pair-checks canoniques (Sales→Product en #1 implicite,
People→Product en #10 candidat V5, Legal→Product en #8,
Finance→Product en #6, Growth→Product implicite). La procédure de
re-formalisation en cas de NEEDS_SCOPE est **projetée** à partir du
mécanisme de chaînage NEEDS_SCOPE → retour et du seuil 24h du contrat
B2 → B3. Les champs distinctifs (`consolidation.sources`,
`b2_cosigners`, `jtbd_packet_id_returned`) sont **projetés** par
extrapolation du format canonique. Le concept ferme 4 questions mais
**n'a pas été testé** en cycle réel (0 packet mésoperpétuel Flash
dans le corpus visible — cf. `flash-veto-empirical-validation-protocol.md`).