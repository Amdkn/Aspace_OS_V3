---
type: Concept
title: B2 → B3 contract — quand une décision mésoperpétuelle devient un JTBD packet
description: Le packet mésoperpétuel B2 Council dispatche un B3 JTBD packet. Le contrat est bilatéral : B2 promet (DoD + impacted domains + proof_expected + next_review), B3 promet (sprint d'exécution + proof path + lead/lag indicators + retour au B2 captain). Trois failure modes si le contrat n'est pas explicite : scope creep, silent rework, escalade tardive. Le contrat est versionné et signé conjointement B2 président + B3 squad lead.
tags: [b2, b3, contract, jtbd, handoff, packet, escalation, scope-creep]
generated: { by: minimax-m3, at: 2026-08-19T02:35:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T02:35:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: triplet-b3-depends
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 13 — B3 dependsOn B2-sprint"
    last_modified: 2026-08-17
  - id: triplet-b3-interdit
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 41 — B3 interdit-combler-trou"
    last_modified: 2026-08-17
  - id: b2-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — le format canonique d'une décision B2
    last_modified: 2026-08-19
  - id: fractal-arch
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/fractal-b1b2b3-architecture.md"
    title: Le fractal B1/B2/B3 — Areas perpétuelles vs Summer's Verse datées
    last_modified: 2026-08-17
  - id: b3-jtbd-reception
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-jtbd-packet-reception-checklist.md"
    title: B3 JTBD packet reception checklist
    last_modified: 2026-08-19
okf_version: "0.2"
---

# B2 → B3 contract — quand une décision mésoperpétuelle devient un JTBD packet

## Le principe

Le Council B2 tranche un arbitrage et produit un packet mésoperpétuel.
Le packet, seul, **ne fait rien** — il doit être traduit en un (ou
plusieurs) JTBD packets B3 exécutables. Le **contrat B2 → B3** est ce
qui rend la traduction opérationnelle : B2 promet un périmètre, B3
promet une livraison vérifiable.

> *« Le technicien dépend du sprint hebdomadaire de son VP : un scrum
> sans sprint est du geste sans cause. »*
> — triplet 13

Le triplet 41 ajoute un interdit côté B3 : *« Tout B3 a l'interdit de
combler lui-même un trou du sprint — il le signale à son VP au lieu
de laisser le défaut invisible. »* Le contrat B2 → B3 doit donc être
**explicite sur ses trous** : ce qui n'est pas promis n'est pas
attendu.

## Le contrat bilatéral

### Ce que B2 Council promet

Le packet mésoperpétuel (cf. `b2-meso-decision-packet-spec.md`)
fournit déjà l'essentiel. Le contrat ajoute trois champs que le
packet seul n'a pas :

1. **Cadre d'exécution** — durée maximale du sprint B3 (semaines),
   squad B3 cible (1 ou plusieurs parmi les 8 squads Marvel), captain
   B2 sponsor (le captain en aval de la transition).
2. **Bornes DoD explicites** — pour chaque critère d'acceptance, un
   seuil chiffré (taux, latence, montant). Un DoD *« améliorer la
   satisfaction client »* est insuffisant ; un DoD *« NPS ≥ 40 sur
   100 réponses mesurées »* est contractuel.
3. **Preuves attendues par forme** — `b3-proof-path-4-formes` liste
   les 4 formes canoniques (capture, log, métrique, témoignage
   client). Le contrat en déclare 1 ou 2 obligatoires ; les autres
   sont à la discrétion du B3 squad.

### Ce que le B3 squad promet

Le JTBD packet B3 (cf. `b3-jtbd-packet-reception-checklist.md` côté
réception) doit contenir en miroir :

1. **Plan de livraison** — sprint d'exécution, dates de scrum
   intermédiaires (5 scrums/semaine pour un sprint standard, cf.
   triplet 11), squad lead responsable.
2. **Lead indicators** — les 1 à 3 métriques *pendant* l'exécution
   qui signalent une dérive avant le résultat final.
3. **Lag indicators** — les 1 à 2 métriques *après* l'exécution qui
   confirment que le résultat a tenu (rétention à J+30, NPS, marge).
4. **Chemin d'escalade** — la première remontée est **au captain B2
   sponsor**, pas au Council, sauf veto catalogue ou red flag
   matrice.

## Les trois failure modes

### 1. Scope creep — l'élargissement silencieux

**Symptôme** : B3 produit plus que ce que le packet demandait, parce
que « c'était plus simple ». Le DoD est rempli, mais le périmètre
n'est plus ce qui a été arbitré.

**Détection** : le proof path produit par B3 mentionne des livrables
absents du JTBD packet. La diff entre `jtbd_packet.received` et
`jtbd_packet.delivered` est non vide.

**Remède** : le captain B2 sponsor refuse la livraison excédentaire
et consigne le scope creep dans le journal Council. Le B3 squad
**réapprend** la discipline du périmètre.

### 2. Silent rework — la reprise non signalée

**Symptôme** : B3 a livré, mais a refait en cours d'exécution sans
escalader. Le proof path est conforme, mais le temps consommé a
dépassé le cadre d'exécution promis.

**Détection** : le log d'exécution de B3 montre des commits de
rework après la première livraison interne. Les lead indicators ont
viré au rouge sans signal.

**Remède** : le captain B2 sponsor ouvre un arbitrage *« rework
non-escaladé »* en séance hebdomadaire. La sanction est sur la
**discipline**, pas sur le résultat — le B3 squad n'est pas puni
pour avoir reworked, mais pour ne pas l'avoir signalé.

### 3. Escalade tardive — le求救 trop tardif

**Symptôme** : B3 a tenu jusqu'au bout du sprint, puis a escaladé un
blocker qu'il connaissait depuis trois jours. Le packet mésoperpétuel
est exécuté à moitié.

**Détection** : le post-mortem B3 mentionne un blocker connu mais
non escaladé. La fenêtre entre la détection et l'escalade dépasse le
seuil convenu (par défaut 24 heures ouvrées).

**Remède** : le captain B2 sponsor exige un *« escalator register »*
pour le sprint suivant : un journal court des blocers détectés,
chacun avec son horodatage et son escalade (ou son absence
d'escalade).

## Le rôle du capitaine B2 sponsor

Le captain en aval de la transition (Sales dans Growth × Sales) est
le **sponsor** du contrat B2 → B3. Son rôle :

1. **Signe le contrat** conjointement avec le B3 squad lead — la
   double signature est dans le JTBD packet.
2. **Voit les lead indicators** en temps réel — pas seulement à la
   livraison. Une dérive à J+2 doit être visible au captain sponsor
   à J+2, pas à J+7.
3. **Décide de l'escalade** au Council si la dérive dépasse le seuil.
   L'escalade tardive est sanctionnée par le Council, pas par le
   captain sponsor seul.

## Le rôle du B3 squad lead

Le squad lead (MrFantastic pour Fantastic Four, etc.) tient le
**JTBD packet** côté B3. Son rôle :

1. **Tient le scrums.md** du sprint — chaque jour, une action
   exécutable, pas un plan (triplet 11).
2. **Signale les trous** au captain sponsor — *« je ne peux pas
   remplir ce DoD parce que X »*, sans tenter de combler (triplet 41).
3. **Livre la preuve** dans l'une des 4 formes canoniques
   (`b3-proof-path-4-formes`).

## Le format conjoint

Le contrat est consigné dans le JTBD packet B3, avec un en-tête
`contract:` qui pointe sur le packet mésoperpétuel source. Format
résumé :

```yaml
jtbd_packet_id: B3-JTBD-YYYY-NN
source_meso_decision: B2-MESO-DECISION-YYYY-NN
contract_signed:
  b2_sponsor: <captain>
  b3_squad_lead: <lead>
  signed_at: YYYY-MM-DD
cadre:
  duree: <weeks>
  squad: <squad-marvel>
  captain_b2: <captain>
dod_bornee:
  - critere: <text>
    seuil: <chiffre>
proof_expected:
  forme: capture|log|metrique|temoignage
  chemin: <path-or-url>
indicators:
  lead: [<metrique>, <metrique>]
  lag: [<metrique>, <metrique>]
escalade:
  first_stop: captain_b2_sponsor
  seuil_temps: 24h
```

## Anti-pièges

- **Contrat sans signature conjointe.** Un JTBD packet sans
  `contract_signed` est un ordre, pas un contrat. Le B3 squad lead
  n'est pas engagé.
- **DoD sans seuil chiffré.** Un DoD *« améliorer X »* ouvre la
  porte au scope creep — chacun a sa lecture de « améliorer ».
- **Captain sponsor absent du suivi.** Un captain qui voit le proof
  path à la livraison, sans avoir vu les lead indicators, découvre
  la dérive trop tard.
- **Escalade qui saute le captain sponsor.** Un B3 qui escalade
  directement au Council sans passer par le captain sponsor casse
  l'ordre vertical (cf. fractal §« L'escalier d'escalade (canonique) »).
- **Confondre contrat et cahier des charges.** Le contrat est
  bilatéral et signé. Le cahier des charges est unilatéral et subi.
  La nuance compte : un B3 qui « respecte le cahier des charges »
  sans avoir signé le contrat n'est pas engagé.

## Liens

- [[b2-council-arbitrage-rule]] — l'amont : qui produit le packet mésoperpétuel
- [[b2-meso-decision-packet-spec]] — le format source du contrat
- [[b2-council-cadence-and-chair]] — quand le contrat est signé en séance
- [[b2-areas-dormants-doctrine]] — quand un domaine B2 ne peut pas sponsoriser
- [[b3-jtbd-packet-reception-checklist]] — la vue B3 du même contrat
- [[b3-proof-path-4-formes]] — les 4 formes de preuve acceptées

## Note de confiance

**Confirmé par machine.** Le triplet 13 (B3 dependsOn B2-sprint) et le
triplet 41 (B3 interdit-combler-trou) sont cités verbatim. Le rôle du
captain B2 sponsor et la règle d'escalade sont tirés du fractal
§« L'escalier d'escalade (canonique) ». Les trois failure modes
(scope creep, silent rework, escalation tardive) sont **reconstruits**
à partir des erreurs typiques observées dans le fractal et dans le
cycle sprint hebdo (triplet 10). Le format conjoint YAML est
**projeté** à partir du packet mésoperpétuel (D4 append-only) et de
la forme B3 JTBD — la convention `contract_signed` à double
signature est extrapolée, pas citée. À vérifier en cycle réel :
(1) la double signature tient-elle sans friction ?, (2) les seuils
chiffrés sont-ils tenables pour tous les domaines ?, (3) l'escalade
à 24h est-elle réaliste pour les blocker B3 profonds (incidents
multi-jours) ?
