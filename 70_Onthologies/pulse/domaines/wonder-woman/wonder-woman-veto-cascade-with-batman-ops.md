---
type: Concept
title: Couplage Wonder Woman × Batman (Ops) — double veto en cascade sur recurring-spend × procédure-sans-condition-d'arrêt
description: Les vetos catalogue de Wonder Woman (Finance) et Batman (Ops) peuvent se déclencher sur la même dépense récurrente. Batman bloque « toute procédure qui n'a pas de condition d'arrêt écrite » (triplet 24) ; Wonder Woman bloque « toute dépense récurrente sans date de revue et sans métrique de retour » (triplet 28). Une dépense cloud (Hostinger, Vercel) qui n'a pas de condition d'arrêt ET pas de métrique de retour déclenche les deux vetos en cascade. Le couplage est bilatéral fort — Batman teste la forme procédurale, Wonder Woman teste la forme financière. Recommandation : trois issues (Batman amend + WW amend, Batman amend + WW veto levé, escalade B2 Council).
tags: [b2, finance, ops, wonder-woman, batman, couplage, veto, cascade, double-veto, recurring-spend, condition-arret]
generated: { by: minimax-m3, at: 2026-08-19T05:40:00Z }
verified:
  - { by: process:lecture-corpus-wonder-woman-tour-3, at: 2026-08-19T05:40:00Z }
sources:
  - id: triplet-24-batman
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 24 — Batman bloque toute procédure qui n'a pas de condition d'arrêt écrite"
    last_modified: 2026-08-17
  - id: triplet-28-wonder-woman
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 28 — Wonder Woman bloque toute dépense récurrente sans date de revue et sans métrique de retour"
    last_modified: 2026-08-17
  - id: vetos-catalogue
    resource: "C:/Usersamado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2
    last_modified: 2026-08-19
  - id: batman-finance-coupling-r-r-r-r-r-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-ops-x-finance-wonder-woman.md"
    title: Couplage Ops × Finance-WonderWoman (Batman tour 2)
    last_modified: 2026-08-19
  - id: batman-finance-asymmetry
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couple-ops-finance-asymetrie-amplification-canonique.md"
    title: "Couplage Batman×WonderWoman — asymétrie amplification canonique triplet 58"
    last_modified: 2026-08-19
  - id: finance-couplings
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-finance-couplings.md"
    title: Domaine Finance — couplages amont/aval (Batman = Ops delivery cost)
    last_modified: 2026-08-19
  - id: trois-cooperation-modes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-three-cooperation-modes.md"
    title: Trois modes de coopération B2
    last_modified: 2026-08-19
  - id: council-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council arbitrage rule
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Couplage Wonder Woman × Batman — double veto en cascade

## Le signal canonique

Les triplets 24 et 28 posent les deux vetos catalogue :

**Triplet 24 (Batman)** :
> *« Batman bloque toute procédure qui n'a pas de condition d'arrêt
> écrite. »*

**Triplet 28 (Wonder Woman)** :
> *« Wonder Woman bloque toute dépense récurrente sans date de
> revue et sans métrique de retour. »*

Les deux vetos sont **catégoriels** et **non-négociables** au
niveau mésoperpétuel (cf. `b2-eight-domain-vetoes-catalogue.md`
§« Les trois propriétés »). **Les deux testent la forme** d'une
dépense récurrente :

- Batman teste **la condition d'arrêt** (la procédure a-t-elle un
  critère de fin écrit ?).
- Wonder Woman teste **la date de revue et la métrique de retour**
  (la dépense récurrente est-elle chiffrée et datée ?).

Une dépense qui satisfait une forme mais pas l'autre déclenche
**un seul veto**. Une dépense qui ne satisfait aucune forme
déclenche **les deux vetos en cascade**.

## Le cas canonique — dépense cloud

Le scénario type est une **dépense cloud récurrente** (Hostinger
$120/an, Vercel $20/mois, Supabase $25/mois, etc.) :

- **Batman veto ?** Si la procédure de souscription n'a pas de
  condition d'arrêt écrite (« on arrête quand le projet se termine
  »), Batman oppose son veto catalogue.
- **Wonder Woman veto ?** Si la métrique de retour n'est pas
  chiffrée (« cet hébergement sert X, le retour attendu est Y »),
  Wonder Woman oppose son veto catalogue.

Les deux vetos peuvent **se déclencher simultanément** sur la
même dépense. La question opérationnelle : qui tranche ?

## L'asymétrie des deux vetos

Les deux vetos ont des **formes distinctes** mais une **portée
identique** sur la dépense :

| Critère | Batman (Ops) | Wonder Woman (Finance) |
|---|---|---|
| **Classe** | Procédure | Dépense récurrente |
| **Test** | Condition d'arrêt écrite | Date + métrique de retour |
| **Granularité** | Procédure entière (toutes dépenses liées) | Une dépense récurrente |
| **Issue si veto** | Procédure amendée (condition ajoutée) | Dépense amendée (date + métrique ajoutées) |
| **Escalade** | Superman/Flash/Aquaman (producteurs) peuvent amender | Superman/Flash (consulted) peuvent amender |
| **Canal** | Triplet 24 → OMK control room § « Ops blocking authority » | Triplet 28 → OMK control room § « Finance blocking authority » |

**Asymétrie clé** : Batman teste la **procédure** (l'ensemble
des gestes qui produisent la dépense récurrente), Wonder Woman
teste la **dépense** (la ligne individuelle). Un Batman amend
peut satisfaire Wonder Woman sans amender la ligne dépense ; un
Wonder Woman amend peut satisfaire Batman sans amender la
procédure.

## La doctrine Batman × Finance en cascade — le couplage asymétrique

L'escuadre Batman en tour 2 a posé le couplage
(`batman-ops-x-finance-wonder-woman.md` cité dans la liste
sources). Le constat clé est l'**asymétrie d'amplification
canonique** :

> *« Batman n'a pas d'amplification canonique équivalente au
> triplet 58 de Wonder Woman. Wonder Woman a un triplet 58 qui
> étend son veto catalogue avec ROI à 30 jours. Batman a son
> triplet 24 (condition d'arrêt) mais pas d'amplification
> canonique explicite. L'asymétrie est **documentée** mais
> **non soumise au Council**. »*
> — Batman tour 2, asymétrie amplification canonique

**Conséquence** : quand Batman et Wonder Woman croisent leurs
vetos sur la même dépense, **Wonder Woman a un levier
supplémentaire** (triplet 58 métrique chiffrée) que Batman
n'a pas. La cascade n'est pas symétrique.

## Trois issues possibles quand les deux vetos se déclenchent

Quand Batman **et** Wonder Woman opposent leurs vetos sur la même
dépense, **trois issues** sont possibles (par ordre de
fréquence) :

### Issue 1 — Batman amend + Wonder Woman amend (résolution parallèle)

Les deux capitaines amendent **chacun** leur veto indépendamment :

- Batman exige une **condition d'arrêt écrite** ajoutée à la
  procédure (« résilier l'abonnement si projet P n'utilise plus
  X% du quota pendant 2 trimestres »).
- Wonder Woman exige une **date de revue + métrique** ajoutées à
  la dépense (« revue trimestrielle Q3/Q4, métrique = utilisation
  ≥X% »).

**Résultat** : les deux vetos sont levés, la dépense est
autorisée. C'est l'issue préférée quand Batman et Wonder Woman
sont en **mode parallel** — chacun amende sans coordination.

**Format packet mésoperpétuel** : `decision: accepted`, mode
`parallel`, `proof_expected: B2 gate ops update + B2 gate finance
update`. Le packet est signé conjointement par Batman et Wonder
Woman.

### Issue 2 — Batman amend + Wonder Woman veto levé (Wonder Woman cède)

Batman amende la procédure, mais Wonder Woman **ne lève pas son
veto** — la métrique de retour reste non chiffrée. Wonder Woman
peut soit :

- **Maintenir le veto** unilatéralement, auquel cas la dépense
  reste bloquée.
- **Céder et accepter l'amendement Batman** comme suffisant (cas
  rare — Wonder Woman peut justifier que la condition d'arrêt
  Batman réduit le risque financier à un niveau acceptable).

**Résultat asymétrique** : la dépense est autorisée sur la base
de l'amendement Batman seul. Wonder Woman consigne son accord
par écrit dans le journal Council.

**Cas typique** : abonnement cloud à $20/mois avec arrêt
automatique si non-utilisé pendant 30 jours. Batman amende
l'arrêt. Wonder Woman peut accepter que le risque financier
($20 × 12 mois = $240) est trop faible pour justifier un veto
catalogue, et céder.

### Issue 3 — Batman veto + Wonder Woman veto (escalade B2 Council)

Les deux capitaines **refusent** l'amendement de l'autre.
Wonder Woman exige la métrique, Batman exige la condition d'arrêt,
**les deux ne sont pas fournis**. La dépense ne peut pas être
autorisée — le Council B2 arbitre.

**Résultat** : packet mésoperpétuel avec `decision: blocked`,
mode `negotiation`, impacted_domains incluant ops + finance +
eventuellement growth (le demandeur de la dépense). Le Council
tranche :

- Soit l'amendement conjoint Batman + Wonder Woman est imposé
  (Issue 1 par coercion).
- Soit la dépense est retirée (Issue 4).
- Soit l'escalade B1 est nécessaire (rare — sauf North Star en
  jeu).

## Le cas spécial — Batman veto + Wonder Woman veto sur compliance fiscale

Quand la dépense récurrente est un **paiement de compliance
fiscale** (F10, SOP-L2-FINANCE-004), **Wonder Woman ne peut pas
opposer son veto** (cf. exception F10 — voir concept dédié
`wonder-woman-f10-compliance-veto-exception-clause.md`). Mais
Batman peut opposner son veto **si la procédure de paiement
fiscal n'a pas de condition d'arrêt** (par exemple : un
acompte provisionnel sans seuil de déclenchement écrit).

**Cascade asymétrique** : Batman veto tient, Wonder Woman veto
ne tient pas. La dépense fiscale reste bloquée tant que Batman
n'amende pas la procédure.

## La matrice des cascades — quand Batman et WW se rencontrent

Tableau croisé Batman × Wonder Woman (8 cellules) :

|  | **WW accepte** | **WW veto (date+metric manque)** | **WW veto (F10 exception)** |
|---|---|---|---|
| **Batman accepte** | Dépense autorisée | WW veto tient, dépense bloquée | WW veto ne tient pas, Batman OK, dépense autorisée |
| **Batman veto (condition d'arrêt manque)** | Batman veto tient, dépense bloquée | **Cascade** — escalade B2 Council | **Cascade asymétrique** — Batman veto tient, WW veto ne tient pas |
| **Batman veto (procédure morte)** | Batman veto tient, dépense retirée | **Cascade** — escalade B2 Council | Batman veto tient, dépense retirée |

**Lecture** : 4 cellules sur 9 mènent à une **cascade** (escalade
B2 Council). Le couplage Batman × Wonder Woman est **bilatéral
fort** sur les dépenses récurrentes.

## Recommandation au B2 Council — trois amendements

Trois amendements à la doctrine catalogue pour rendre la cascade
explicite :

### 1. Ajouter un champ « double_veto_cascade » au packet mésoperpétuel

Quand Batman et Wonder Woman opposent leurs vetos simultanément,
le packet porte :

```yaml
double_veto_cascade:
  batman_veto_id: <reference>
  wonder_woman_veto_id: <reference>
  outcome: parallel_amend | wonder_woman_cede | council_escalate
  joint_signature: batman + wonder_woman (si accepted parallel)
```

### 2. Mode negotiation par défaut pour les cascades

`b2-three-cooperation-modes.md` § « Negotiation » est le mode
canonique pour les conflits Batman × Wonder Woman. Le mode
parallel reste possible (Issue 1) mais **uniquement** si les deux
capitaines peuvent amender indépendamment.

### 3. Wonder Woman cède sur les seuils faibles

Issue 2 (Wonder Woman cède) est légitime quand le risque
financier est inférieur au coût d'arbitrage Council. Un seuil
indicent : **Wonder Woman cède si la dépense < <500 €/an** (à
valider). Au-delà, le veto catalogue tient.

## Anti-pièges

- **Batman veto prioritaire.** Batman teste la **procédure**,
  Wonder Woman teste la **dépense**. Les deux sont **égaux** en
  droit catalogue. Aucun n'est prioritaire sur l'autre.
- **Wonder Woman cède par deference à Batman.** La cession
  d doit être ( doit, fondée sur le risque financier, pas sur
  l'autorité Batman. Wonder Woman qui cède systématiquement à
  Batman casse son rôle de gardien.
- **Cascade permanente.** Si Batman et Wonder Woman sont en
  cascade sur >30% des dépenses récurrentes, c'est un signal de
  désalignement doctrinal — les deux capitaines ne partagent pas
  la définition de « procédure acceptable ».
- **Escalade B2 Council par défaut.** L'escalade Council est
  coûteuse (60 min de séance, quorum 5/8). Elle doit rester
  l'exception, pas le mode par défaut.
- **Oublier F10 compliance.** La cascade Batman × Wonder Woman
  oublie souvent l'exception F10 (cf.
  `wonder-woman-f10-compliance-veto-exception-clause.md`). Wonder
  Woman peut opposer Batman veto sur une dépense fiscale, mais
  pas Wonder Woman veto.

## Liens

- [[wonder-woman-recurrent-spend-veto]] — le veto WW
- [[wonder-woman-triplet-58-canon-reading]] — l'amplification triplet 58
- [[wonder-woman-f10-compliance-veto-exception-clause]] — l'exception F10
- [[wonder-woman-red-flag-4-trigger]] — le déclencheur transversal
- [[wonder-woman-finance-couplings]] — le couplage Batman = delivery cost
- [[b2-veto-amplification-cycle]] — la procédure d'amplification
- [[b2-three-cooperation-modes]] — negotiation par default
- [[b2-meso-decision-packet-spec]] — le format packet

## Note de confiance

**Confirmé par machine** sur les triplets 24 et 28 (lignes
verbatim) et sur les 3 propriétés du veto légitime
(`b2-eight-domain-vetoes-catalogue.md`). **Reconstruit** sur la
matrice 8 cellules Batman × Wonder Woman — la matrice canonique
ne pose pas le double veto en cascade. **Reconstruit** sur les 3
issues (parallel amend, WW cede, escalation) — extrapolation
depuis la doctrine Batman × Finance (`batman-ops-x-finance-wonder-woman.md`
tour 2) et le triplet 58. **À valider en cycle réel** : (1) le
seuil 500 €/an pour cession WW est-il adapté ? (2) le champ
`double_veto_cascade` est-il accepté par le B2 Council ? (3)
l'asymétrie d'amplification (WW a triplet 58, Batman non) est-elle
soumise au Council ?