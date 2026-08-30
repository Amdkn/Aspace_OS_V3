---
type: Concept
title: Aquaman — triple signature Aquaman + Batman + Thena pour la defensibilité
description: Le defensibility binder (Forme 4 du catalogue JTBD Aquaman) exige une signature tripartite : Aquaman (Legal doctrine), Batman (Ops exécution et decision log), Thena (Eternals defense squad). Cette triple signature est distincte de la double signature B2 sponsor + B3 lead du contrat B2→B3 — elle engage trois rôles opérationnels distincts. Tour 3 formalise le pattern, identifie 4 cas d'application, 3 cas d'abus, et la procédure de levée par escalade B1.
tags: [b2, aquaman, batman, thena, defensibility, triple-signature, eternals, incident, breach]
generated: { by: minimax-m3, at: 2026-08-19T05:30:00Z }
verified:
  - { by: process:lecture-canon-aquaman-tour-3, at: 2026-08-19T05:30:00Z }
sources:
  - id: aquaman-jtbd
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-jtbd-emit-receive.md"
    title: Aquaman catalogue JTBD émis et reçus
    last_modified: 2026-08-19
  - id: aquaman-couplages
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-couplages-invisibles.md"
    title: Aquaman couplages invisibles
    last_modified: 2026-08-19
  - id: aquaman-dormant
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-dormant-activation.md"
    title: Aquaman transition dormant ↔ activation
    last_modified: 2026-08-19
  - id: aquaman-pair-check-10
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-pair-check-10-legal-risk-launch.md"
    title: Aquaman pair-check #10 Legal risk → Launch
    last_modified: 2026-08-19
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — quand une décision mésoperpétuelle devient un JTBD packet
    last_modified: 2026-08-19
  - id: triplet-thena
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 22 — Aquaman pairedWith Eternals (Thena defense)"
    last_modified: 2026-08-17
  - id: rapport-batman-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/ETAT_DOMAINES.md"
    title: "ETAT_DOMAINES — Batman tour 2 mentionne couplage Ops×Legal-Aquaman"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman — triple signature Aquaman + Batman + Thena pour la defensibilité

## D'où vient le pattern

La Forme 4 du catalogue JTBD Aquaman
([[aquaman-jtbd-emit-receive]] §Forme 4) pose le defensibility binder :

```yaml
jtbd_id: B3-LEGAL-DEFENSIBILITY-DOC-2026-06
proof_required:
  - binder signed by Thena
  - owners roster signed by Aquaman + Batman
lead_indicator: binder ready in <24h after incident declared
lag_indicator: 0 successful plaintiff claims in 12 months post-incident
coupling:
  veto_cible: n/a (pas un veto déclenché, c'est une production en aval)
  pair_check: hors matrice (couplage indirect Aquaman ↔ Batman)
```

Le binder exige **trois signataires** :

- **Thena** (Eternals defense squad, triplet 22) — signe le binder
  en tant que squad lead defense.
- **Aquaman** — signe le owners roster en tant que B2 captain
  doctrine.
- **Batman** — signe le owners roster en tant que B2 captain Ops
  exécution et decision log.

Cette **triple signature** est distincte de la double signature B2
sponsor + B3 lead posée par [[b2-b3-jtbd-handoff-contract]] §« Le
format conjoint ». Le contrat B2→B3 oppose **B2 sponsor** + **B3
squad lead** ; la triple signature Aquaman oppose **trois capitaines
ou leads de rangs B2 et B3** pour un objet spécifique (le binder de
defensibilité).

## Pourquoi trois, pas deux

Trois signataires sont nécessaires parce que **trois rôles
opérationnels distincts** sont engagés dans le binder :

1. **Rôle doctrinal** (Aquaman). Le binder doit refléter la doctrine
   Legal — quelles décisions étaient permises, lesquelles étaient
   bloquées, lesquelles ont été escaladées. Seul Aquaman peut signer
   ce volet.
2. **Rôle exécution** (Batman). Le binder doit documenter la chaîne
   d'exécution Ops — qui a fait quoi, à quel moment, avec quels
   outils. Seul Batman (Ops) peut signer ce volet.
3. **Rôle defense** (Thena). Le binder doit être techniquement
   *admissible* en cas de litige — la structure, les annexes, les
   références juridiques doivent suivre les standards de la defense.
   Seul le squad lead defense (Thena chez Eternals) peut signer ce
   volet.

**Double signature** (par exemple Aquaman + Batman) ne suffit pas —
le binder serait *doctrinalement correct* et *opérationnellement
traçable*, mais pas *techniquement admissible*. **Quadruple
signature** (ajout d'un quatrième signataire) est *overkill* — la
defensibilité ne demande pas plus que trois rôles opérationnels
distincts.

## Les 4 cas d'application de la triple signature

### Cas 1 — Incident opérationnel majeur

Un incident Ops (par exemple breach de données, panne de production
de plus de 4 heures, perte de données client) qui engage la
responsabilité légale de l'organisation. Le binder documente :

- La chaîne d'exécution Ops (Batman signe).
- La doctrine Legal applicable (Aquaman signe).
- La structure admissible en cas de litige (Thena signe).

**Déclencheur** : Batman signale l'incident dans `pulse/b2/.../Batman`
sous format incident report, Aquaman initie le binder en moins de
24h.

### Cas 2 — Breach de données

Un Cyborg (IT) signale une breach de données (accès non-autorisé,
exfiltration, perte de support). Le binder doit documenter :

- La chaîne d'incident IT (Batman + Cyborg co-documentent, Batman
  signe le volet Ops).
- La doctrine Legal privacy (Aquaman signe — RGPD, AI Act, ou
  régulation sectorielle).
- La structure admissible pour le regulator (Thena signe).

**Déclencheur** : Cyborg émet le signal breach, Aquaman initie le
binder en moins de 24h (cf. lead_indicator Forme 4).

### Cas 3 — Litigation entrante

Une plainte, une assignation, ou une regulator inquiry arrive. Le
binder doit documenter l'historique des décisions et de l'exécution
*avant* la litigation pour démontrer la *due diligence* de
l'organisation. Signataires :

- Batman signe le decision log historique.
- Aquaman signe la doctrine applicable à chaque décision.
- Thena signe la cohérence du binder avec la stratégie de defense.

**Déclencheur** : Aquaman (Forme 4) ou Batman (incident) initie le
binder dès réception de l'assignation.

### Cas 4 — Régulation sectorielle émergente

Une régulation nouvelle (par exemple AI Act, DMA, RGPD extension)
entre en vigueur ou change d'interprétation. Aquaman initie un
binder *proactif* pour cartographier la doctrine Legal actuelle vs
la nouvelle régulation.

**Déclencheur** : Aquaman (Forme 4 proactive — *« Aquaman lui-même
initie une revue de defensibilité proactive (régulation
sectorielle qui change) »*, cf. [[aquaman-jtbd-emit-receive]] §Forme
4). Batman signe le volet exécution (impact sur les Ops actuelles),
Thena signe la cohérence defense.

## Les 3 cas d'abus de la triple signature

### Abus 1 — Triple signature pour un objet non-defensibility

La triple signature est **spécifique au binder de defensibilité**.
L'utiliser pour d'autres objets (par exemple un contract template
Forme 3 ou un privacy review Forme 1) est de l'overreach — la triple
signature n'a de sens que lorsque **trois rôles opérationnels
distincts** sont engagés, ce qui n'est le cas que pour le binder.

**Reproche** : Batman signe un contrat commercial (Forme 3, qui
relève d'Aquaman + Green Lantern + Phastos). Batman n'est pas dans
le périmètre de la Forme 3. Forcer sa signature est de l'overreach.

### Abus 2 — Triple signature sans incident réel

Un Aquaman qui initie la triple signature *« par prudence »* sans
incident, breach, litigation, ou régulation émergente déclenche un
coût complet (squad defense activée, decision log figé, owners
roster signé) sans contrepartie.

**Reproche** : Aquaman en état SHADOW_ACTIVE (cf.
[[aquaman-dormant-activation]]) qui initie un binder *« au cas où »*
gaspille les ressources Eternals (Thena + squad defense). L'amplification
de veto (cf. [[aquaman-veto-amendment-perimetre-insuffisant]]) ne
couvre pas cette activation — c'est un autre type d'abus.

### Abus 3 — Triple signature avec un signataire hors rôle

La triple signature exige Aquaman (Legal), Batman (Ops), Thena
(defense squad lead). Un quatrième signataire (par exemple Wonder
Woman pour Finance, ou Superman pour Growth) **n'est pas légitime**
— il n'a pas de rôle opérationnel distinct dans la defensibilité.

**Reproche** : Wonder Woman signe un binder parce qu'un aspect
financier est en cause (par exemple une perte de revenu liée à
l'incident). C'est de l'overreach. Wonder Woman peut être *informée*
mais pas signataire.

## La procédure de levée de la triple signature

Trois issues possibles quand un binder est signé :

1. **Archivage** (cas standard). Le binder est archivé dans
   `03_Master_Agreements/defensibility/` avec les trois signatures.
   Aucun escalation.
2. **Litigation engagée**. Le binder est transmis à Thena (Eternals
   defense) qui active la procédure de contentieux. Aquaman + Batman
   sont *témoins* (interrogables), pas *parties*. L'escalade B1 est
   *non obligatoire* mais *recommandée* si la litigation touche le
   North Star.
3. **Escalade B1**. Si le binder révèle une décision B1 ou B2 qui
   engage la responsabilité *politique* de l'organisation (par
   exemple une décision d'aller en regulator inquiry), Aquaman +
   Batman + Thena co-signent un packet d'escalade B1.

## L'état Aquaman et la triple signature

La triple signature exige **Aquaman en état ACTIVE** (cf.
[[aquaman-dormant-activation]]). Un Aquaman en état Dormant ou
SHADOW_ACTIVE ne peut pas signer un binder — la signature engage sa
responsabilité sur la doctrine, ce qui n'est possible qu'en ACTIVE.

**Conséquence** : un projet pré-launch (Aquaman SHADOW_ACTIVE) qui
subit un incident doit soit (a) escalader B1 pour activer Aquaman, soit
(b) traiter l'incident *sans triple signature* (Batman seul + Thena —
risque de binder non-doctrinal). L'option (a) est la voie canonique.

## Le couplage avec le pair-check #10

Le pair-check #10 Legal risk → Launch (cf.
[[aquaman-pair-check-10-legal-risk-launch]]) peut déclencher la
triple signature *avant* un launch risqué. C'est un usage *proactif*
de la triple signature, distinct des 4 cas d'application ci-dessus
qui sont *réactifs* (post-incident).

**Différence** : la triple signature proactive (pair-check #10)
produit un binder *de préparation*, pas un binder *de réponse*.
L'objet est différent : *« que ferons-nous si le launch déclenche une
litigation ? »*, pas *« que s'est-il passé pendant l'incident X ? »*.

## Anti-pièges

- **Confondre triple signature et contrat B2→B3.** Le contrat B2→B3
  oppose **B2 sponsor + B3 squad lead**. La triple signature oppose
  **trois capitaines ou leads de rangs B2 et B3**. Les deux sont
  compatibles (Thena peut être B3 squad lead ET signataire du
  binder), mais pas identiques.
- **Aquaman SHADOW_ACTIVE qui signe.** La signature engage la
  responsabilité d'Aquaman. Sans état ACTIVE, la signature n'a pas
  de force — un binder signé par un Aquaman SHADOW_ACTIVE est
  *inadmissible* en cas de litige.
- **Batman qui signe un objet non-Ops.** Batman signe le volet
  *exécution* du binder. Si l'objet n'a pas de volet exécution
  Ops (par exemple un binder doctrinal pur), Batman ne signe pas.
- **Thena qui signe un objet non-défense.** Thena signe le volet
  *defense* du binder. Si l'objet n'a pas de volet défense (par
  exemple un audit interne sans risk de litige), Thena ne signe
  pas. Un audit pur Aquaman + Batman suffit.
- **Quadruple signature.** La triple signature est le **maximum**
  opérationnel pour un binder. Ajouter un quatrième signataire
  (Wonder Woman, Superman, etc.) est de l'overreach et n'améliore
  pas l'admissibilité — l'admissibilité dépend de la couverture
  des rôles, pas du nombre de signatures.

## Liens

- [[aquaman-jtbd-emit-receive]] — Forme 4 (defensibility doc) qui
  ancre la triple signature
- [[aquaman-couplages-invisibles]] — Couplage Aquaman ↔ Batman qui
  motive la double signature Aquaman + Batman
- [[aquaman-dormant-activation]] — la condition ACTIVE pour signer
- [[aquaman-pair-check-10-legal-risk-launch]] — la triple signature
  proactive déclenchée par le #10
- [[b2-b3-jtbd-handoff-contract]] — la double signature B2 sponsor +
  B3 lead (compatible, distincte)
- [[aquaman-veto-amendment-perimetre-insuffisant]] — l'amplification
  veto qui ne couvre pas l'abus de triple signature *par prudence*

## Note de confiance

**Confirmé par machine pour les sources, reconstruit pour la
synthèse.** La Forme 4 du catalogue JTBD est citée verbatim avec
ses deux signatures (Thena + Aquaman/Batman co-signe). Le triplet 22
ancré Thena defense est cité verbatim. Le pattern *triple
signature* est **reconstruit** par généralisation de la double
signature Aquaman + Batman + Thena de la Forme 4 — c'est une
**projection** depuis la Forme 4, pas une doctrine citée ailleurs
dans le corpus. Les 4 cas d'application sont **projetés** depuis les
déclencheurs de la Forme 4 (Batman incident, Cyborg breach,
Aquaman proactive). Les 3 cas d'abus sont **projetés** depuis les
anti-pièges de la doctrine veto ([[aquaman-veto-amendment-perimetre-insuffisant]]
§Anti-pièges) et de la doctrine dormant
([[aquaman-dormant-activation]] §Anti-pièges). La procédure de
levée (3 issues) est **reconstruite** par symétrie avec les 4
issues du veto catalogue ([[b2-eight-domain-vetoes-catalogue]]).
**À vérifier en cycle** : (1) Thena est-elle bien le squad lead
defense dans tous les cas, ou faut-il un autre agent Eternals pour
les breaches RGPD spécifiques ?, (2) la signature Aquaman peut-elle
être donnée *avant* la signature Batman (ordre chronologique), ou
faut-il un ordre canonique ?, (3) Wonder Woman doit-elle être
*informée* (pas signataire) dans tous les cas où l'incident a un
volet financier, ou seulement dans certains ?
