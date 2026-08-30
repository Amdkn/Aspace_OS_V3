---
type: Concept
title: Aquaman — doctrine Legal Hold (eDiscovery / data freeze pré-litige)
description: Quand un risque de litige ou d'enquête régulatrice est identifié, Aquaman peut imposer un Legal Hold : figer les données et communications potentiellement pertinents, suspendre les politiques de rétention automatiques,astreindre les gardiens à la conservation. Distinct de la triple signature (qui documente post-incident), le Legal Hold agit en amont et engage Aquaman + Batman (ops) + Cyborg (data systems) selon une procédure en 4 étapes. 5 cas de déclenchement légitime, 4 cas d'abus, 3 issues de levée.
tags: [b2, aquaman, legal-hold, ediscovery, data-freeze, batman, cyborg, pre-litigation]
generated: { by: minimax-m3, at: 2026-08-19T07:00:00Z }
verified:
  - { by: process:lecture-canon-aquaman-tour-6, at: 2026-08-19T07:00:00Z }
sources:
  - id: aquaman-couplages
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-couplages-invisibles.md"
    title: Aquaman couplages invisibles (Aquaman ↔ Batman/IT data)
    last_modified: 2026-08-19
  - id: aquaman-defensibility
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-defensibility-triple-signature.md"
    title: Aquaman triple signature — defensibility binder post-incident
    last_modified: 2026-08-19
  - id: aquaman-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-cycle-de-vie-legal-5-phases.md"
    title: Aquaman cycle de vie Legal 5 phases (Intake → Binder)
    last_modified: 2026-08-19
  - id: aquaman-pair-check-7
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-pair-check-10-legal-risk-launch.md"
    title: Aquaman pair-check #10 — Legal risk → Launch
    last_modified: 2026-08-19
  - id: b2-veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: B2 catalogue 8 vetos
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman — doctrine Legal Hold (eDiscovery / data freeze pré-litige)

## La question que le corpus ne posait pas

Un dossier Legal peut basculer en litige prévisible *avant* qu'un
incident ne se déclare — un brevet contesté, une plainte imminente,
une perquisition annoncée, un signal régulateur (CNIL, AMF, FDA,
SEC). À ce moment-là, **les données non figées à temps disparaissent
définitivement** : boîtes mail auto-purgées, logs machine rolling,
backups écrasés, documents physiques recyclés. Le Legal Hold est la
doctrine juridique qui suspend cette érosion naturelle le temps que
le dossier soit tranché.

Tours 1 à 5 ont posé la **triple signature Aquaman + Batman + Thena**
pour le **post-incident** (defensibility binder, cf.
[[aquaman-defensibility-triple-signature]]). Ils n'ont pas posé
l'**amont pré-incident** — la doctrine par laquelle Aquaman *fige*
les données *avant* que la defensibilité ne soit mise à l'épreuve.
C'est l'objet de ce concept.

## Définition opérationnelle

Un **Legal Hold** est une directive écrite, signée Aquaman
(Legal), co-signée Batman (Ops, exécution de la suspension des
politiques de rétention) et Cyborg (IT, suspension des scripts
d'écrasement automatique), qui :

1. **Identifie les gardiens** — personnes physiques et systèmes
   (mailboxes, drives partagés, bases de données, archives) ;
2. **Suspend les politiques de rétention automatiques** —
   l'écrasement des backups, l'auto-purge des mails, le recyclage
   du stockage physique ;
3. **Ordonne la préservation** des éléments identifiés, avec
   horodatage de la directive ;
4. **Tient jusqu'à levée explicite** par Aquaman, ou jusqu'à
   prescription du dossier.

C'est une doctrine distincte du veto Aquaman (qui bloque le
* démarrage d'une prestation*) et de la triple signature (qui
*documente post-incident*). Elle agit **en amont du cycle de vie
5 phases** (cf. [[aquaman-cycle-de-vie-legal-5-phases]]), parfois
*avant même la phase 1 Intake*.

## Les 5 cas de déclenchement légitime

Un Legal Hold est légitime si l'un des éléments suivants est
vérifiable **par un tiers** :

1. **Litige pré-annoncé** — assignation, mise en demeure, ou
   notification formelle reçue.
2. **Enquête régulatrice imminente** — visite annoncée, subpoena,
   demande d'accès, signal d'un régulateur (CNIL, AMF, FDA,
   SEC, ou équivalent sectoriel).
3. **Breach détectée et publique** — fuite de données, faille
   exploitée, ransomware déclaré. Le Legal Hold conserve les
   traces forensiques *avant qu'elles ne soient effacées par les
   routines IT*.
4. **Plainte interne recevable** — un lanceur d'alerte ou un
   signalement éthique remonte au People (Green Lantern) qui
   escalade Aquaman.
5. **Statut de prescription risqué** — un dossier arrive à T-365
   jours (ou T-730 jours selon juridiction) de la prescription et
   des éléments pourraient disparaître.

## Les 4 cas d'abus

Un Legal Hold est invalide si l'un des éléments suivants est
vérifié :

1. **Hold généralisé sur l'entreprise entière** sans dossier
   spécifique. Le Legal Hold est *ciblé*, pas *global*.
2. **Hold utilisé comme outil de blocage interne** — un Batman ou
   Superman qui veut geler une décision Business utilise le Legal
   Hold comme moyen de pression.
3. **Hold sans gardien identifié** — une directive sans interlocuteur
   précis ne peut pas être exécutée par Batman ou Cyborg.
4. **Hold renouvelé indéfiniment** sans réévaluation trimestrielle —
   un Hold qui dure > 12 mois sans clause de revue devient une
   rétention illégale.

## La procédure en 4 étapes

| # | Étape | Owner | Output |
|---|---|---|---|
| 1 | **Détection & qualification** | Aquaman (signal, dossier) | Mémo interne qualifiant le déclenchement |
| 2 | **Inventaire des gardiens** | Aquaman + Batman + Cyborg cosign | Liste des mailboxes, drives, systèmes, personnes |
| 3 | **Directive écrite** | Aquaman signé | Email + note interne horodatée, distribué aux gardiens |
| 4 | **Confirmation exécution** | Batman (process) + Cyborg (data) | Attestation que les scripts sont suspendus |

La procédure est documentée dans un packet mésoperpétuel dédié
`B2-MESO-DECISION-YYYY-NN-legal-hold` (analogue à la cosignature
Aquaman + Batman + Thena pour la triple signature, mais avec
Cyborg au lieu de Thena pour le pré-incident).

## Liens avec les concepts existants

- **Veto Aquaman ([[aquaman-veto-engagement-sans-perimetre]])** :
  le veto bloque le * démarrage*, le Legal Hold *préserve les
  preuves*. Les deux sont des garde-fou Aquaman, mais opèrent à
  des temps différents du cycle de vie.
- **Triple signature ([[aquaman-defensibility-triple-signature]])** :
  la triple signature documente *post-incident*, le Legal Hold
  * agit en amont*. Même schéma tripartite (Aquaman + Batman +
  tiers), mais tiers = Cyborg (pré-incident, données) au lieu de
  Thena (post-incident, narration défensive).
- **Couplages invisibles ([[aquaman-couplages-invisibles]])** :
  ce concept opérationnalise le couplage Aquaman ↔ Batman (Ops
  exécution) et Aquaman ↔ Cyborg (IT data systems) — non
  formalisé jusqu'ici.
- **Cycle 5 phases ([[aquaman-cycle-de-vie-legal-5-phases]])** :
  le Legal Hold peut survenir *avant Phase 1 Intake* (cas 1-2) ou
  *pendant Phase 2 Scoping* (cas 3-5). Il prolonge le cycle sans
  en modifier la structure.
- **Pair-check #10 ([[aquaman-pair-check-10-legal-risk-launch]])** :
  un Legal Hold levé sans amendement du risque est un red flag ;
  le Council doit revoir le pair-check #10.

## Les 3 issues de levée

Un Legal Hold est levé par l'une des trois issues suivantes :

1. **Dossier clos sans procédure** — la plainte est retirée,
   l'enquête régulatrice classée sans suite, le signal interne non
   confirmé. Aquaman lève la directive, Batman réactive les
   routines, Cyborg reprend les scripts de rétention.
2. **Procédure engagée** — un contentieux formel est lancé. Le
   Legal Hold devient alors une obligation eDiscovery (production
   de documents à la partie adverse). Aquaman cosigne avec outside
   counsel (cf. [[aquaman-outside-counsel-management-fee-discipline]]).
3. **Hold invalide** — une motion de censure Aquaman (cf.
   [[aquaman-veto-antisèche-pattern-detection]]) démontre l'abus.
   La directive est levée rétroactivement, Aquaman consigne
   l'incident dans le journal Council.

## Anti-pièges

- **Confondre Legal Hold et backup**. Un backup protège contre la
  perte accidentelle ; un Legal Hold protège contre l'écrasement
  *normal* des routines de rétention. La différence est l'horodatage
  et la directive explicite.
- **Confondre Legal Hold et audit**. Un audit est une vérification
  *par sondage* ; un Legal Hold est une *conservation intégrale*.
  L'audit terminé ne lève pas le Hold ; il peut le justifier ou le
  invalider.
- **Hold sans Batman ni Cyborg**. Un Legal Hold signé Aquaman seul
  ne peut pas être exécuté — Batman (Ops) tient les processus
  humains de suspension, Cyborg (IT) tient les processus machines.
  Le Hold non cosigné n'a pas de force opérationnelle.
- **Hold levé tacitement**. Le Hold ne se lève pas par expiration
  implicite ; il exige une directive Aquaman de levée, distribuée
  et confirmée.
- **Hold comme outil de blocage Business**. Un Batman ou Superman
  qui veut geler une décision Sales ou Growth peut être tenté de
  demander un Hold abusif. La motion de censure antisèche
  ([[aquaman-veto-antisèche-pattern-detection]]) couvre ce cas, mais
  la vigilance est de mise *dès la directive* — pas seulement *a
  posteriori*.

## Liens

- [[aquaman-couplages-invisibles]] — couplage Aquaman ↔ Batman/IT
  data, opérationnalisé ici
- [[aquaman-defensibility-triple-signature]] — la triple signature
  post-incident, complémentaire
- [[aquaman-cycle-de-vie-legal-5-phases]] — le cycle 5 phases, que
  le Legal Hold peut précéder ou interrompre
- [[aquaman-pair-check-10-legal-risk-launch]] — le pair-check risque
  Legal → Launch, qui peut côtoyer un Hold sans levée
- [[aquaman-outside-counsel-management-fee-discipline]] — la
  sélection des avocats externes *quand le Hold devient
  contentieux*
- [[aquaman-veto-antisèche-pattern-detection]] — la motion de
  censure applicable aux Holds abusifs

## Note de confiance

**Reconstruit, à moitié étayé.** Le Legal Hold est une doctrine
juridique standard (FRCP Rule 37(e) aux US, équivalents CPC en
FR, RGPD Article 5(1)(e) pour la minimisation) — pas une
projection. L'ancrage canonique est cependant indirect : le
concept pose la procédure tripartite *par symétrie* avec la
triple signature post-incident, sans citer une règle B2 ou un
SDD canonique sur le Legal Hold spécifiquement. Le triplet v3,
le Ownerbook T1, et les 4 fichiers OMK `08_Legal_Aquaman_Eternals/`
ne mentionnent pas le Legal Hold explicitement. La pratique
est donc **reconstruite** depuis les standards juridiques
généraux + les concepts Aquaman existants.

**À vérifier en cycle** :
- Le triplet 22 / Ownerbook T1 / OMK pose-t-il un agent spécifique
  sur le Legal Hold ? Si oui, lequel ?
- Batman a-t-il une procédure de suspension de rétention
  documentée ? (probable, via le cycle de vie 5 phases Ops, mais
  pas confirmé)
- Cyborg tient-il les routines d'écrasement IT sur lesquelles le
  Legal Hold s'applique ? (probable, mais pas cité dans les
  concepts Cyborg déjà lus)
- Une motion de censure antisèche *a-t-elle déjà été déposée* sur
  un Legal Hold abusif ? Si oui, ce concept en est une
  généralisation.

**Limite** : la doctrine Legal Hold est dense et ce concept n'en
traite que la surface nécessaire à l'opérationnalisation B2 → B3.
Une extension future pourrait couvrir : juridiction par juridiction
(US eDiscovery vs FR CPC vs UK CPR), production de documents à
la partie adverse vs tierce (régulateur), coût typique d'un Hold
(typiquement 50-500k€ selon volume de données, hors honoraires
outside counsel).
