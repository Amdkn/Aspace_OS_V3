---
type: Concept
title: Superman Growth — patterns de coopération parallel / handoff / negotiation
description: Superman Growth entre en parallel (40% des cas), handoff (40%), et negotiation (20%) — projection par lecture de la matrice d'harmonisation. Les pair-checks #5 (Finance→Growth) et #7 (Legal→Growth) sont presque toujours handoff. Le pair-check #1 (Growth→Sales) alterne parallel et negotiation selon la stabilité de l'ICP. Superman entre rarement en escalation B1 — sauf quand le veto canonique tient face à un mandat B1.
tags: [superman, growth, parallel, handoff, negotiation, modes, cooperation, pattern]
generated: { by: minimax-m3, at: 2026-08-19T04:05:00Z }
verified:
  - { by: process:lecture-corpus-superman, at: 2026-08-19T04:05:00Z }
sources:
  - id: three-modes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-three-cooperation-modes.md"
    title: Trois modes de coopération B2 — parallel / handoff / negotiation
    last_modified: 2026-08-19
  - id: harmonization
    resource: "C:/Users/ADO/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — 9 critères cross-domaines
    last_modified: 2026-08-19
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2
    last_modified: 2026-08-19
  - id: council-arbitrage
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Superman Growth — patterns de coopération parallel / handoff / negotiation

## Les trois modes — rappel canonique

`b2-three-cooperation-modes.md` pose les trois modes :

- **parallel** : aucun transfert cross-domaine détecté. Les
  domaines agissent indépendamment. **Pas de packet mésoperpétuel**.
- **handoff** : un transfert obligatoire a été détecté. Le
  séquencement est tracé dans le packet.
- **negotiation** : deux DoDs ou plus sont en conflit et
  nécessitent un tradeoff.

## Distribution projetée pour Superman — 40/40/20

Par lecture de la matrice d'harmonisation et des pair-checks RACI
qui touchent Superman :

| Mode | % projeté des cas Superman | Logique |
|---|---|---|
| **parallel** | ~40% | Superman agit sans couplage (campagnes paid media isolées, content sans handoff Sales, brand work sans Legal) |
| **handoff** | ~40% | Superman reçoit un amont Legal ou Finance séquentiel (mandat Aquaman avant publication, mandat Wonder Woman avant dépense) |
| **negotiation** | ~20% | Superman et Sales ont un conflit d'ICP, ou Superman et People se disputent Brand |

**Projection**, pas un comptage canonique — aucun cycle OMK réel
n'a encore été mesuré. Le canon Council-arbitrage confirme
*« aucun packet mésoperpétuel n'existe encore »* dans `b2-council-arbitrage-rule.md` §« Note de confiance ».

## Les 5 cas parallel Superman

Le mode parallel est **par défaut** tant qu'aucun transfert
cross-domaine n'est détecté. Pour Superman :

### 1. Paid media sur segment déjà qualifié

Growth lance une campagne paid media sur un segment déjà ICP
qualifié par Sales. Sales n'est pas sollicité. Product, Ops, IT
ne sont pas sollicités. **Parallel** — pas de packet mésoperpétuel.

### 2. Content production sans claim public

Groot_Content produit un article de fond (SEO, blog technique)
sans claim public (pas de mention de résultat client, pas de
promesse ROI). Legal n'est pas sollicité. **Parallel**.

### 3. VoC research interne

Mantis_VoC produit une étude de satisfaction interne
(non publiée). Aquaman n'est pas sollicité (pas de parole
publique). **Parallel**.

### 4. Automation sequence (Rocket_Auto)

Rocket_Auto automatise une séquence email sur un segment
qualifié, sans nouveau claim. **Parallel** — pas de transfert
cross-domaine.

### 5. Ciblage ICP update (Gamora_Target)

Gamora_Target met à jour la segmentation ICP sur la base de
données first-party, sans changer la promesse publique. **Parallel**.

Dans les 5 cas, **aucun packet mésoperpétuel n'est nécessaire**.
C'est la majorité du travail opérationnel Growth.

## Les 5 cas handoff Superman

Le mode handoff est déclenché par les pair-checks amont où
Superman est **Accountable** (Finance → Growth, Legal → Growth).

### Handoff 1 — Aquaman dormant → Superman publie un case-study

Aquaman est dormant (pas de contrat signé, cf.
`b2-areas-dormants-doctrine.md`). Superman reçoit un mandat B1
*« publier un case-study client X »*. Le signal Superman réveille
Aquaman (déclencheur B pair, cf. `b2-areas-dormants-doctrine.md`
§« Les trois déclencheurs de réveil »). **Séquencement** :
Aquaman consigne le réveil → Aquaman statue sur le périmètre de
l'accord → Superman publie. **Mode handoff obligatoire** — la
publication ne peut pas commencer avant la fin de l'accord Aquaman.

### Handoff 2 — Wonder Woman veto dépense récurrente

Wonder Woman veto une dépense récurrente paid media (Rocket_Auto)
qui n'a pas de métrique de retour chiffrée (triplet 28 + 58).
**Séquencement** : Superman amende le mandat pour inclure la
métrique (Rocket_Auto ajoute `metrique_retour: MQL-ICP-US, seuil: 1000,
fenetre: 30j`) → Wonder Woman lève le veto → Superman démarre la
dépense. **Mode handoff**.

### Handoff 3 — Aquaman veto case-study sans accord

Aquaman veto un case-study Mantis_VoC dont le client n'a pas
signé d'autorisation de publication. **Séquencement** : Mantis
recueille l'autorisation → Aquaman consigne l'accord dans
`Master_Agreements/` → Superman publie via Groot. **Mode handoff**.

### Handoff 4 — Finance × Growth : dépense hors mandat

Un mandat B1 *« pivoter US premium »* n'a pas alloué de budget
paid media. Wonder Woman alloue la dépense **après** que Superman
ait défini le scope. **Séquencement** : Superman scope →
Wonder Woman alloue → Superman dépense. **Mode handoff**.

### Handoff 5 — IT déploie analytics stack

Cyborg (IT) déploie l'analytics stack (Mixpanel/Amplitude).
Superman utilise le stack en aval. **Séquencement** : Cyborg
déploie → Superman configure les événements → Superman lit les
données. **Mode handoff** (cf. `pair-checks-dependencies.md` §«
Couplage Superman ↔ IT »).

## Les 3 cas negotiation Superman

Le mode negotiation est déclenché par conflit de DoDs.

### Negotiation 1 — Superman vs Sales : ICP non stabilisé

Sales (JohnJones) a un DoD ICP qui exige des MQL avec intent
signal fort. Superman a un DoD MQL basé sur la démographie
(taille, secteur, géographie) sans intent. **Conflit** : Sales
rejette 60% des MQL Superman, Superman stagne sur ses volumes.

**Négociation** : le Council tranche — DoD amendé, l'ICP est
*démographie + intent minimum* (un signal intent faible est
acceptable si la démographie est forte). **Mode negotiation**.

### Negotiation 2 — Superman vs People : Brand work cross-périmètre

People mandate StarLord_Story pour un livrable Brand
(manifeste de marque). Superman mandate aussi StarLord pour un
livrable Growth (storytelling client). Les deux DoDs sont
légitimes et utilisent le même agent.

**Négociation** : le Council tranche — séquencement temporel
(Pendaison → Brand, puis Pendaison → Growth) ou répartition
du squad lead (StarLord sur Brand, Drax_Closing sur Growth).
**Mode negotiation**.

### Negotiation 3 — Superman vs Finance : trade-off runway vs scale

Wonder Woman détecte que la runway est à 6 mois. Superman
demande une augmentation de la dépense paid media pour scaler
US premium. **Conflit** : Wonder Woman veut conserver la
runway, Superman veut scaler.

**Négociation** : le Council tranche sur la base de North Star
> cycle > risque > effort (cf. `b2-council-arbitrage-rule.md`
§« Pourquoi pas B1 »). Décision typique : *scale réduit avec
métrique de retour à 30 jours, coupe si non tenue*. **Mode
negotiation**.

## Les cas escalate_to_B1 — quand Superman remonte

`b2-council-arbitrage-rule.md` §« Quand le Council escalade à B1 »
pose 3 situations :

1. **Conflit de North Star** — Superman mandate pivoter US ET EU
   simultanément, le North Star ne tient pas. **Escalade B1**.
2. **Violation de cycle** — Superman demande un sprint hors
   12WY. **Escalade B1**.
3. **Boundary non-négociable tierce** — le veto Superman tient
   face à un mandate B1 lui-même. **Escalade B1** pour réécriture
   de la classe.

Pour Superman, le **cas #3** est le plus probable : un mandat B1
*« promettre un ROI court terme »* entre en conflit avec le veto
Superman *« promesse que la delivery ne tient pas »*. Superman
**escalade B1** parce que le veto tient au niveau mésoperpétuel
— seul B1 peut réécrire la classe catalogue.

## Pourquoi Superman entre rarement en escalation B1

Comparé aux autres capitaines, Superman escalade **rarement** :

| Capitaine | Veto | Cas d'escalade B1 typique |
|---|---|---|
| Green Lantern | recrutement sans mandat | mandat B1 qui force un recrutement non-mandaté |
| Batman | procédure sans condition d'arrêt | mandat B1 qui impose une procédure sans arrêt |
| Flash | valeur personne-dépendante | mandat B1 qui impose une offre personne-dépendante |
| JohnJones | proposition sans problème reformulé | mandat B1 qui force une proposition non-reformulée |
| **Superman** | **promesse non tenue** | **mandat B1 qui force une promesse non-tenable** |
| Wonder Woman | dépense sans revue | mandat B1 qui force une dépense sans date |
| Cyborg | fournisseur cloud-only sans sortie | mandat B1 qui force un fournisseur cloud-only |
| Aquaman | prestation sans accord écrit | mandat B1 qui force une prestation sans accord |

Superman entre en escalation B1 quand le **mandat B1 exige
explicitement** une promesse non-tenable. C'est le cas où le
mandat B1 **est lui-même** en violation de la classe catalogue.
Rare en pratique — mais **le plus défensif** des 8 vetos : le
veto Superman est le dernier rempart avant qu'une promesse
publique ne soit publiée.

## Anti-pièges

- **Parallel par défaut sans scan.** Sans la matrice
  d'harmonisation en amont, Superman déclare parallel des cas
  qui sont en fait handoff (cf. `b2-three-cooperation-modes.md`
  §« Anti-pièges »). Le scan matrice est obligatoire avant chaque
  mandat.
- **Handoff avec rework possible.** Si Aquaman ou Wonder Woman
  peuvent commencer avec une version dégradée, c'est **negotiation**,
  pas handoff.
- **Negotiation avec un DoD abandonné.** Si Superman renonce à un
  DoD sans nouveau DoD équivalent (cf. `b2-three-cooperation-modes.md`
  §« Risque »), c'est une perte — pas un tradeoff. Escalade B1.
- **Mode figé.** Un changement de mode en cours d'exécution
  n'est **pas** un changement de décision. C'est une nouvelle
  décision. Append-only.

## Liens

- [[b2-three-cooperation-modes]] — la doctrine des trois modes
- [[b2-harmonization-matrix-exploitable]] — la matrice 9 critères
- [[b2-pair-check-raci-by-rank]] — Superman A sur Finance→Growth et
  Legal→Growth
- [[b2-council-arbitrage-rule]] — quand escalader B1
- [[pair-checks-dependencies]] — pair-checks Superman
- [[veto-catalogue-concrete]] — cas concrets de veto
- [[veto-amplification-candidate]] — amplification qui modifie les
  patterns de coopération

## Note de confiance

**Projets, à moitié étayé.** La distribution 40/40/20 est une
projection par lecture de la matrice + RACI + triplet 28/58. Aucun
cycle OMK réel n'a été mesuré (le canon Council note *« aucun
packet mésoperpétuel n'existe encore »*). Les 5 parallel + 5
handoff + 3 negotiation + escalate B1 sont **reconstruits** par
lecture critique du canon + projection de la pratique documentée.
La rareté d'escalade B1 pour Superman est **projetée** par
comparaison avec les 7 autres vetos catalogue.
