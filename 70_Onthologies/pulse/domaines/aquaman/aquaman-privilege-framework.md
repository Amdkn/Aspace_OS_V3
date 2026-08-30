---
type: Concept
title: Aquaman — Privilege Framework (attorney-client + work-product + business)
description: Le Privilege Framework distingue trois régimes documentaires — Attorney-Client Privileged (AC), Attorney Work Product (WP), et Business (non-privileged). Chaque régime a des règles de tagging (préfixe `PRIV-`, `WP-`, `BIZ-`), de distribution (cercle restreint vs cercle étendu), et de levée (moyen vs lourd vs impossible). C'est une doctrine Aquaman ACTIVE distincte de la triple signature (qui défend post-incident) : le privilege défend *en temps réel*, par marquage documentaire à l'émission. 4 cas d'application, 3 cas d'abus, 3 issues de levée.
tags: [b2, aquaman, privilege, attorney-client, work-product, defensibility, tagging, confidentiality]
generated: { by: minimax-m3, at: 2026-08-19T07:00:00Z }
verified:
  - { by: process:lecture-canon-aquaman-tour-6, at: 2026-08-19T07:00:00Z }
sources:
  - id: aquaman-defensibility
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-defensibility-triple-signature.md"
    title: Aquaman triple signature — defensibility binder post-incident
    last_modified: 2026-08-19
  - id: aquaman-legal-hold
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-legal-hold-doctrine.md"
    title: Aquaman Legal Hold — data freeze pré-litige
    last_modified: 2026-08-19
  - id: aquaman-jtbd
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-jtbd-emit-receive.md"
    title: Aquaman catalogue JTBD émis et reçus
    last_modified: 2026-08-19
  - id: aquaman-classification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-classification-risques-4-formes.md"
    title: Aquaman classification 4 formes (privacy/claim/IP/contract)
    last_modified: 2026-08-19
  - id: b2-veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: B2 catalogue 8 vetos
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman — Privilege Framework (attorney-client + work-product + business)

## La question que le corpus ne posait pas

Un dossier Legal produit des **documents de trois natures
différentes**, et chaque nature a un régime juridique distinct.
Un email entre Aquaman et un client sur *« que pensez-vous de
notre exposition sur ce contrat ? »* est **Attorney-Client
Privileged** — il ne peut pas être produit à la partie adverse
ni au régulateur en cas de contentieux. Une note interne
d'Aquaman *« stratégie de défense : plaider la nullité pour
vice de procédure »* est **Attorney Work Product** — protégé
contre la production, mais avec un régime distinct (et
généralement plus faible que l'AC). Une note interne *« voici
les jalons du projet X »* est **Business** — non-protégée par
privilege, productible sur subpoena.

Tours 1 à 5 ont posé la **triple signature**
([[aquaman-defensibility-triple-signature]]) et le **Legal Hold**
([[aquaman-legal-hold-doctrine]]) — les deux *protègent a
posteriori* (après incident, ou en anticipation). Ils n'ont pas
posé le **tagging à l'émission** : la discipline par laquelle
chaque document créé en pratique Legal est *catégorisé* au
moment de sa création. C'est l'objet de ce concept.

## Définition opérationnelle

Le **Privilege Framework** est une doctrine Aquaman ACTIVE qui :

1. **Marque chaque document** émis par Aquaman ou par un agent
   Eternals au moment de sa création — préfixe de tagging
   obligatoire dans le titre ou l'identifiant.
2. **Restreint la distribution** selon le régime — un document
   privileged ne circule qu'au cercle restreint auteur +
   destinataires nominés.
3. **Documente le cercle** — pour chaque document privileged,
   Aquaman tient un journal court qui liste les destinataires
   nominaux. L'élargissement du cercle exige une nouvelle
   entrée.
4. **Prépare la levée** — un privilege levé par erreur (par
   exemple un email AC envoyé à un destinataire non-couvert) est
   un *waiver* ; la doctrine minimise ce risque par tagging
   systématique.

## Les 3 régimes

| Préfixe | Régime | Cercle | Levée par |
|---|---|---|---|
| `PRIV-` | **Attorney-Client Privileged** | Auteur Aquaman + destinataires nommés | Waiver exprès d'Aquaman (exceptionnel) |
| `WP-`   | **Attorney Work Product**   | Auteur Aquaman + Batman (si co-signé triple signature) | Substantielle concurrence d'intérêts (rare) |
| `BIZ-`  | **Business** (non-privileged) | Cercle étendu B2 + B3, distribution libre | Subpoena, demande adverse, audit interne |

### `PRIV-` — Attorney-Client Privileged

Protège la **communication** entre un avocat et son client, lorsque
la communication est *confidentielle* et *dans le but de demander
ou fournir un avis juridique*. Le préfixe `PRIV-` est obligatoire.

**Exemples** : email d'Aquaman à un client sur
*« l'exposition au titre III du Sarbanes-Oxley »* ; note interne
Aquaman sur *« analyse de la jurisprudence In re Acme Corp. »*

**Cercle** : auteur Aquaman + destinataires nommés (client
uniquement, ou agent Eternals sous mandat explicite Aquaman
*formellement* couvert par le privilege — peu de juridictions
couvrent les agents IA, d'où l'importance du tagging).

**Levée** : uniquement par waiver exprès d'Aquaman — donc par
décision documentée. Une erreur (email envoyé à un destinataire
non-couvert) peut lever le privilege implicitement (le *waiver par
inadvertance*). Un email `BIZ-` ensuite internalisé comme
`PRIV-` *ne rétroagit pas* — la couverture n'est pas acquise.

### `WP-` — Attorney Work Product

Protège le **travail préparatoire** d'un avocat en anticipation
de contentieux — c'est le *« fruit de l'activité mentale de
l'avocat »*. Le préfixe `WP-` est obligatoire.

**Exemples** : mémo interne Aquaman *« stratégie de défense :
plaidons la nullité pour vice de procédure »* ; liste de témoins
préparée par Thena (Eternals defense squad) ; calendrier de
production eDiscovery interne.

**Cercle** : auteur Aquaman + tiers co-signataires (Batman pour
la triple signature, Thena pour l'exécution défensive). Plus large
que `PRIV-`, mais toujours restreint.

**Levée** : plus difficile que `PRIV-` à lever, parce que le
work product est un *fait* (la stratégie de défense existe, a
été pensée) plutôt qu'une *communication*. Une cour peut ordonner
la production sous certaines conditions (substantial need +
inability to obtain equivalent without undue hardship, critère
FRCP Rule 26(b)(3) aux US).

### `BIZ-` — Business

Tout le reste. Document de gouvernance, de process, de
coordination — qui n'a aucun privilege et qui est productible sur
subpoena. Le préfixe `BIZ-` est **par défaut** si aucun autre
préfixe n'est appliqué.

**Exemples** : compte-rendu d'une réunion B2 Council ; packet
mésoperpétuel ; email de coordination Batman ↔ Superman.

**Cercle** : distribution libre ; pas de marquage nominatif.

**Levée** : subpoena, demande adverse, audit interne — sans
condition préalable.

## Les 4 cas d'application légitime

1. **Note d'analyse Aquaman pour client** → `PRIV-` ; cercle =
   Aquaman + client.
2. **Stratégie de défense signée triple (Aquaman + Batman +
   Thena)** → `WP-` ; cercle = Aquaman + Batman + Thena.
3. **Email Aquaman à Superman sur l'alignement d'un claim**
   → `BIZ-` ; cercle = Aquaman + Superman + Batman (récipiendaire
   de l'alignement).
4. **Document d'analyse interne Aquaman qui sera transmis à
   outside counsel** → `PRIV-` ; cercle = Aquaman + outside
   counsel nommé + client.

## Les 3 cas d'abus

1. **Marquage `PRIV-` par défaut**. Un agent Eternals qui tague
   *tous* ses outputs `PRIV-` sans discrimination casse la
   doctrine. Le privilege perd sa valeur quand il est systématique.
2. **Marquage rétroactif**. Un document créé `BIZ-` re-tagué
   `PRIV-` *après* qu'un contentieux se déclare ne devient pas
   privileged pour autant. C'est du *after-the-fact privilege*,
   inopposable.
3. **Cercle non documenté**. Un document `PRIV-` sans journal de
   destinataires ne peut pas prouver son caractère confidentiel —
   et perd donc sa protection en cas de contentieux.

## Les 3 issues de levée

Un privilege est levé par l'une des trois issues suivantes :

1. **Waiver exprès** — décision écrite d'Aquaman de renoncer au
   privilege sur un document spécifique (par exemple pour
   produire le document à un régulateur dans le cadre d'une
   coopération).
2. **Crime-fraud exception** — si le document a été créé pour
   commettre ou couvrir un crime ou une fraude, le privilege
   tombe (*crime-fraud exception*, doctrine commune aux US et
   au FR).
3. **Inadvertance** — un document `PRIV-` envoyé par erreur à
   un destinataire non-couvert, ou un document `BIZ-` qui
   révèle le contenu d'un `PRIV-`. Le privilege est levé *pour
   le document entier* par la doctrine du *subject matter
   waiver*.

## Liens avec les concepts existants

- **Triple signature ([[aquaman-defensibility-triple-signature]])** :
  la triple signature Aquaman + Batman + Thena signe un binder
  qui contient des documents `PRIV-` et `WP-` ; le Privilege
  Framework tagging *précède* la signature.
- **Legal Hold ([[aquaman-legal-hold-doctrine]])** : le Hold
  fige *tous* les documents — y compris ceux qui sont tagging
  `PRIV-`. Le tagging permet, lors de la production eDiscovery
  post-Hold, de *filtrer* les documents privileged (ils ne sont
  pas produits à la partie adverse).
- **Classification 4 formes ([[aquaman-classification-risques-4-formes]])** :
  la classification Aquaman porte sur les **risques** (privacy,
  claim, IP, contract) ; le Privilege Framework porte sur les
  **régimes documentaires**. Les deux sont orthogonaux — un
  même document peut être `privacy + claim` (classification
  risque) et `PRIV-` (régime documentaire).
- **Cycle 5 phases ([[aquaman-cycle-de-vie-legal-5-phases]])** :
  chaque phase produit des documents tagués selon leur régime.
  La phase 5 (Binder) consolide le tagging final et prépare la
  levée (ou la conservation) du privilege.

## Anti-pièges

- **Tagger en fin de cycle, pas à l'émission**. Le tagging à
  l'émission protège contre l'erreur de mémoire ; le tagging en
  fin de cycle est reconstructif et sujet à contestation.
- **Confondre tagging et chiffrement**. Le tagging `PRIV-` est
  une *déclaration d'intention*, pas une protection technique.
  Le chiffrement des disques et la restriction d'accès sont des
  *garde-fou techniques* distincts, complémentaires.
- **Distribuer un `PRIV-` à un cercle élargi sans le retaguer**.
  L'élargissement du cercle peut *ne pas* lever le privilege
  si tous les destinataires sont eux-mêmes tenus au secret (par
  exemple un co-counsel), mais doit être consigné dans le
  journal. À défaut de journal, le privilege est *à risque*.
- **Présumer que les agents IA Eternals sont couverts**. Peu de
  juridictions reconnaissent la confidentiality des échanges
  avec un agent IA non-encadré. Aquaman doit explicitement
  *nommer* les agents dans le cercle privileged et tenir un
  journal des prompts/réponses couvert. À défaut, le tagging
  `PRIV-` *ne protège pas*.
- **Ignorer le crime-fraud**. Un document tagged `PRIV-` qui
  documente une fraude perd son privilege. Le tagging n'est pas
  un bouclier légal absolu — il documente l'intention, il ne
  crée pas la légalité.

## Liens

- [[aquaman-defensibility-triple-signature]] — binder qui contient
  les documents privileged
- [[aquaman-legal-hold-doctrine]] — data freeze qui inclut les
  `PRIV-` et `WP-`
- [[aquaman-jtbd-emit-receive]] — catalogue des paquets émis,
  chacun avec un régime documentaire implicite
- [[aquaman-classification-risques-4-formes]] — orthogonal au
  tagging privilege
- [[aquaman-cycle-de-vie-legal-5-phases]] — cycle qui marque les
  régimes documentaires à chaque phase
- [[aquaman-outside-counsel-management-fee-discipline]] — outside
  counsel comme cercle privilégié

## Note de confiance

**Confirmé par doctrine, reconstruit sur A'Space.** Le Privilege
Framework repose sur des doctrines juridiques établies (FRCP
26(b)(3), Sarbanes-Oxley §307, équivalents FR CPC et règles
déontologiques du barreau) — pas une projection. L'ancrage
canonique A'Space est cependant indirect : aucun triplet v3,
aucun Ownerbook T1, aucun des 23 concepts Aquaman existants ne
pose la doctrine tagging. Le concept est **reconstruit** depuis
les doctrines juridiques externes + le pattern Aquaman (triple
signature, Hold, classification 4 formes).

**Particularité IA notable** : la couverture privilege des
échanges avec un agent IA *n'est pas tranchée* dans la
majorité des juridictions. Le concept note que le tagging
`PRIV-` *ne protège pas* par défaut un échange agent IA sans
encadrement explicite — un gap juridique réel à 2026-08-19.

**À vérifier en cycle** :
- Le cycle de vie 5 phases ([[aquaman-cycle-de-vie-legal-5-phases]])
  précise-t-il le tagging par phase ? Sinon, un addendum pourrait
  lister les préfixes attendus (Phase 1 Intake : `BIZ-`, Phase 2
  Scoping : `WP-`, Phase 3 Drafting : `WP-` + `PRIV-`, Phase 4
  Review : `WP-`, Phase 5 Binder : tous).
- Une motion de censure Aquaman (cf.
  [[aquaman-veto-antisèche-pattern-detection]]) peut-elle
  s'appliquer à un tagging `PRIV-` abusif ? Probable — c'est une
  *catégorisation juridique erronée*, analogue au veto politique.
- Le format du journal de cercles privilégiés est-il posé
  ailleurs dans le canon ? Probablement pas — extension à
  proposer au concept catalogue JTBD ([[aquaman-jtbd-emit-receive]]).

**Limite** : les juridictions US et FR ont des régimes de
privilege significativement différents (l'AC privilege américain
est plus formalisé ; le *secret professionnel* français est plus
étroit en pénal mais plus large en civil). Ce concept pose la
doctrine *générale* — un addendum par juridiction pourrait être
requis pour une pratique transfrontalière.
