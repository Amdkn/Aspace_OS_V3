---
type: Concept
title: Aquaman — ordre canonique des deux amplifications veto (périmètre vs IP)
description: [[aquaman-veto-amendment-perimetre-insuffisant]] pose deux amplifications candidates au veto Aquaman : périmètre insuffisant et IP non déclarée. Si les deux sont adoptées par Council, laquelle s'applique en premier quand un cas tombe sous les deux ? Ce concept ferme la zone d'ombre tour 3 §T6.2 en posant l'ordre canonique : périmètre d'abord (parce que sans périmètre on ne sait pas qui possède quoi), IP ensuite (par exception quand l'IP est vérifiable avant le périmètre). 4 cas d'application + 3 abus + procédure 3 étapes.
tags: [b2, aquaman, veto, amplification, périmètre, IP, ordre, canonique, deux-amplifications]
generated: { by: minimax-m3, at: 2026-08-19T06:15:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-5, at: 2026-08-19T06:15:00Z }
sources:
  - id: aquaman-veto-amendment
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-veto-amendment-perimetre-insuffisant.md"
    title: Aquaman — veto amendement deux amplifications (concept 10 tour 3)
    last_modified: 2026-08-19
  - id: rapport-tour-3-T6-2
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-aquaman.md"
    title: "Rapport tour 3 §T6.2 — ordre des amplifications non explicité"
    last_modified: 2026-08-19
  - id: triplet-58-amplification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 58 — amplification veto mécanisme général"
    last_modified: 2026-08-17
  - id: b2-eight-domain-vetoes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2
    last_modified: 2026-08-19
  - id: triplet-30-aquaman-veto
    resource: "C:/Users/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 30 — Aquaman bloque engagement-sans-périmètre"
    last_modified: 2026-08-17
  - id: b2-veto-amplification-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Mécanisme d'amplification veto — 3 conditions canoniques
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman — ordre canonique des deux amplifications veto

## L'open tour 3 §T6.2

[[aquaman-veto-amendment-perimetre-insuffisant]] propose **deux
amplifications candidates** au veto Aquaman :

- **Amplification 1 — périmètre insuffisant** : passage de *« sans
  accord écrit »* (triplet 30) à *« écrit ou implicite insuffisant »*.
- **Amplification 2 — IP non déclarée** : ajout d'une condition *«
  propriété intellectuelle déclarée avant démarrage »* sur le
  triplet 30.

Les deux amplifications passent par majorité simple 5/8 + D4
append-only (cf. [[b2-veto-amplification-cycle]]). Aucune des deux
n'est *réécriture* (pas de libération de cas), donc l'escalade B1
n'est pas obligatoire.

**Question ouverte** (rapport tour 3 §T6.2) :

> *Si les deux amplifications sont adoptées par le Council, laquelle
> s'applique en premier quand un cas tombe sous les deux (par
> exemple un partenariat sans périmètre tracé ET sans IP déclarée) ?*

Sans ordre canonique, Aquaman peut choisir librement — et le choix
est *politique*, pas doctrinal. Un Superman pressé peut voir
l'amplification *périmètre* refusée mais l'amplification *IP*
accordée, ce qui lui laisse une porte de sortie.

## L'ordre canonique proposé : périmètre d'abord, IP ensuite

**Argumentaire doctrinal** :

- Le **périmètre** est un pré-requis à l'IP. Sans périmètre, on
  ne sait pas *qui possède quoi* — la question IP ne peut pas être
  tranchée en amont de la question périmètre.
- Donc **amplification 1 (périmètre) prime sur amplification 2
  (IP)** : la première étape de l'arbitrage est de poser le
  périmètre, la deuxième est de vérifier les IP.

**Conséquence procédurale** : un cas qui tombe sous les deux
amplifications doit être traité en **deux étapes distinctes**,
pas en une seule. Aquaman oppose d'abord la première
amplification (périmètre), puis la deuxième (IP) une fois le
périmètre tracé.

## Les 4 cas d'application

| # | Cas | Étape 1 : périmètre | Étape 2 : IP |
|---|---|---|---|
| 1 | Partenariat sans périmètre ET sans IP déclarée | Bloque dès l'étape 1 — IP non vérifiable | Non applicable (cas jamais atteint étape 2) |
| 2 | Périmètre tracé, IP non déclarée | Périmètre OK — étape 1 franchie | Bloque étape 2 — IP non déclarée |
| 3 | Périmètre insuffisant, IP déclarée mais sur actif tiers | Bloque étape 1 — périmètre non tracé | Bloque étape 2 — IP tierce non-maitrisée |
| 4 | Périmètre tracé, IP déclarée et interne | Étape 1 OK | Étape 2 OK — pas de veto |

**Subtilité du cas 2** : c'est le seul cas où l'amplification IP
est *isolément* applicable. Le périmètre est OK, seule l'IP pose
problème. Aquaman oppose alors directement l'amplification IP sans
rouvrir le périmètre.

## L'exception : IP vérifiable avant périmètre (3 cas)

L'ordre canonique *périmètre d'abord, IP ensuite* a une exception
documentée : quand l'IP est vérifiable **avant** que le périmètre
ne le soit. Trois cas :

1. **Ré-utilisation d'un template Legal connu**. Si l'IP du
   template est connue (par exemple parce que le template est dans
   un référentiel Aquaman), la vérification IP est triviale — elle
   peut précéder le périmètre.
2. **Asset tiers identifié**. Si le livrable utilise un asset
   (logo, framework, API publique) clairement lié à un tiers
   identifié, l'IP de cet asset est vérifiable par Aquaman sans
   avoir le périmètre complet — le périmètre peut être tracé en
   parallèle.
3. **Litige en cours sur l'IP**. Si l'IP du livrable fait l'objet
   d'une contestation connue (par exemple une réclamation antérieure),
   Aquaman peut bloquer l'IP en amont, sans attendre le périmètre.

**Procédure en cas d'exception IP-before-périmètre** :

- Aquaman émet un **`B2-MESO-DECISION-YYYY-NN-veto-ip-precheck`**
  avec motif = IP connue ou contestée.
- Le demandeur (par exemple Superman) amende le périmètre OU
  retire le mandat.
- Si aménagement, Aquaman émet un veto standard périmètre
  (étape 1) ou accepte le périmètre tracé (étape 2 implicite).

## Les 3 abus possibles

| # | Abus | Signal | Remède |
|---|---|---|---|
| 1 | Aquaman qui utilise amplification 2 (IP) pour court-circuiter amplification 1 (périmètre) | Cas 1 (périmètre + IP) traité en étape 2 sans étape 1 formelle | Le packet Council doit tracer les deux étapes — étape 1 omise = abus |
| 2 | Demandeur qui invoque l'exception IP-before-périmètre pour échapper au périmètre tracé | Cas où l'IP est "vérifiable" sur un asset qui n'a pas de trace canonique | Aquaman exige une référence canonique (template ID, asset ID, litige ID) — pas un claim vague |
| 3 | Superman (Growth) qui invoque l'ordre canonique pour bloquer une amplification IP qu'il juge abusive | Cas 2 traité en étape 2 sans contestation de la vérification IP | Council tranche l'ordre canonique — l'abus est *politique*, pas *doctrinal* |

## Le diagramme de décision

```
Mandate touche Aquaman veto + (amplification 1 + amplification 2) ?
├── Non → veto catalogue standard (triplet 30)
└── Oui → 
    ├── IP vérifiable avant périmètre ?
    │   ├── Oui (3 cas d'exception) → 
    │   │   ├── Bloquer IP d'abord (B2-MESO-DECISION-...-veto-ip-precheck)
    │   │   └── Périmètre tracé en parallèle par le demandeur
    │   └── Non → 
    │       ├── Étape 1 : périmètre tracé ?
    │       │   ├── Non → veto amplification 1 (périmètre insuffisant)
    │       │   └── Oui → 
    │       │       ├── Étape 2 : IP déclarée ?
    │       │       │   ├── Non → veto amplification 2 (IP non déclarée)
    │       │       │   └── Oui → 
    │       │       │       ├── IP interne et conforme → pas de veto
    │       │       │       └── IP tierce → escalade Cyborg ou tierce ?
    │       │       │           ├── Oui → escalade Cyborg + Aquaman co-signe veto
    │       │       │           └── Non → escalade B1 (rare)
    │
```

## La procédure 3 étapes Council-ready

Pour Council-ready, l'application de l'ordre canonique suit trois
étapes :

### Étape 1 — Aquaman identifie la couverture

Au moment où Aquaman détecte qu'un mandat touche son veto, Aquaman
doit tracer :

- Le mandat a-t-il une IP vérifiable en amont ? → applique
  l'exception IP-before-périmètre.
- Le mandat a-t-il un périmètre tracé ? → étape 2.
- Le mandat a-t-il les deux ? → étape 1 (périmètre) puis étape 2 (IP).
- Le mandat n'a aucun des deux ? → veto immédiat étape 1
  (périmètre bloque IP implicitement).

Le packet Council trace cette identification dans le motif du veto.

### Étape 2 — Aquaman oppose le veto de première étape

Aquaman émet le veto amplification 1 (périmètre) ou amplification 2
(IP) selon le cas. Le packet Council trace l'étape.

Si aménagement → étape suivante. Si pas d'aménagement → mandat
retiré ou escalade B1.

### Étape 3 — Aquaman oppose le veto de deuxième étape (si applicable)

Si le mandat passe l'étape 2 mais touche l'amplification 2, Aquaman
émet le veto amplification 2 dans un packet Council séparé. Les
deux packets sont liés (`escalates` dans le motif) et tracés en D4.

**Conséquence** : un mandat qui touche les deux amplifications
produit potentiellement **deux packets Council** dans le même
cycle, pas un seul. La traçabilité D4 est l'enjeu — chaque
packet doit pouvoir être relié à l'autre sans ambiguïté.

## Le sort des réécritures (rarement applicable)

Si Council adopte les deux amplifications (procédure majorité 5/8 +
D4), **une seule réécriture du triplet 30 est nécessaire**. Le
triplet 30 devient :

> *« Aquaman bloque toute prestation dont le périmètre (écrit ou
> implicite) est insuffisant pour tracer la propriété du livrable,
> ET toute prestation dont la propriété intellectuelle n'est pas
> déclarée avant démarrage. »*

**Asymétrie d'application** :

- Périmètre insuffisant → veto **bloquant** (empêche démarrage).
- IP non déclarée → veto **conditionnel** (peut démarrer si IP
  déclaré en cours, mais Aquaman peut bloquer rétroactivement si
  IP litigieuse découverte).

**Conséquence** : l'amplification 1 reste *plus forte* que
l'amplification 2, même après adoption. L'ordre canonique
*périmètre d'abord* n'est pas un choix politique — il reflète la
force respective des deux amplifications.

## Le couplage avec la forme 4 (defensibility doc)

L'amplification 2 (IP non déclarée) a un couplage fort avec la
**forme 4 émise** ([[aquaman-jtbd-emit-receive]]) — le defensibility
doc archive l'IP tracée pour chaque livrable. Si le dossier est
binder [[aquaman-defensibility-triple-signature]], l'IP doit être
déjà tracée.

**Conséquence** : un dossier qui passe phase 5 Binder sans IP
déclarée déclenche le triple veto IP — un *cas d'application
exceptionnelle* que la triple signature doit elle-même documenter.

## Anti-pièges

- **Inverser l'ordre "IP d'abord" systématiquement**. L'ordre
  canonique est périmètre d'abord, IP ensuite. Inverser
  systématiquement = abus pouvoir Aquaman.
- **Ignorer l'exception IP-before-périmètre**. Quand l'IP est
  vérifiable en amont, attendre le périmètre complet est
  procédurier, pas doctrinal. Aquaman qui ignore l'exception
  casse sa propre doctrine.
- **Traiter les deux amplifications en un seul packet**. Les deux
  étapes doivent être tracées en deux packets Council liés, pas
  en un seul — sinon l'étape 1 devient invisible.
- **Considérer l'ordre canonique comme une hiérarchie politique**.
  L'ordre est *doctrinal* (parce que le périmètre est pré-requis
  à l'IP). Le traiter comme politique ouvre la porte aux abus.

## Liens

- [[aquaman-veto-amendment-perimetre-insuffisant]] — le concept
  tour 3 qui pose les deux amplifications candidates
- [[b2-eight-domain-vetoes-catalogue]] — le veto catalogue qui
  ancre les 8 vetos et leurs 3 propriétés
- [[b2-veto-amplification-cycle]] — le mécanisme d'amplification
  (majorité 5/8 + D4)
- [[aquaman-jtbd-emit-receive]] — la forme 4 (defensibility doc)
  qui archive l'IP
- [[aquaman-defensibility-triple-signature]] — la phase 5 Binder
  qui doit tracer l'IP
- [[aquaman-cycle-de-vie-legal-5-phases]] — les phases 3 et 4 où
  l'ordre canonique s'applique

## Note de confiance

**Reconstruit à partir d'un open tour 3 §T6.2.**

- ✅ Tour 3 §T6.2 cité verbatim (rapport tour 3).
- ✅ Triplet 30, triplet 58, [[b2-veto-amplification-cycle]] cités.
- 🟡 L'ordre canonique *périmètre d'abord, IP ensuite* est une
  **projection depuis la sémantique** : le périmètre est un
  pré-requis logique à l'IP. **Pas de triplet canonique** sur
  l'ordre. À soumettre au Council pour adoption formelle.
- 🟡 Les 3 cas d'exception (IP-before-périmètre) sont des
  **cas-types opérationnels** projetés depuis la pratique
  Aquaman (template connu, asset tiers, litige en cours). **Pas
  de triplet canonique** pour ces exceptions.
- ❌ Non vérifié en cycle : aucun cas Aquaman n'a opposé les deux
  amplifications en Vague 2 (0 packet mésoperpétuel Legal).
  L'ordre canonique est **prospectif**.
