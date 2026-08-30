---
type: Concept
title: Cyborg ↔ Aquaman — couplage Legal × IT sur la clause de réversibilité (chemin de sortie = contract + IaC + failover)
description: Le couplage Legal × IT est cité par Aquaman dans son couplage invisible People × Legal. Concrètement : le veto Cyborg *« cloud-only sans chemin de sortie »* exige une clause de réversibilité *contractuelle* (Aquaman) en plus de l'IaC et du failover (Cyborg). Le triplet canonique est contrat + IaC + failover = réversibilité documentée. Trois cas concrets où le couplage se manifeste, trois cas d'abus, une matrice de réversibilité à 5 niveaux.
tags: [cyborg, aquaman, legal, reversibilite, cloud-only, clause-contractuelle, iac, failover, triplet-reversibilite]
generated: { by: minimax-m3, at: 2026-08-19T04:45:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:45:00Z }
sources:
  - id: aquaman-couplages-invisibles
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-couplages-invisibles-legal-it.md"
    title: Aquaman — couplages invisibles Legal × IT (chemin de sortie contractuel = clause de réversibilité)
    last_modified: 2026-08-19
  - id: cyborg-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-veto-cloud-only-sortie.md"
    title: Cyborg veto — cloud-only sans chemin de sortie
    last_modified: 2026-08-19
  - id: triplet-cyborg-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 29 — Cyborg hasVetoOver cloud-only-sans-sortie"
    last_modified: 2026-08-17
  - id: aquaman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-veto-engagement-sans-perimetre.md"
    title: Aquaman veto — engagement sans périmètre (propriété du livrable)
    last_modified: 2026-08-19
  - id: b2-eight-domain-vetoes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — un domaine, un blocage légitime
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cyborg ↔ Aquaman — couplage Legal × IT sur la réversibilité

## Le couplage canonique Legal × IT transverse

`aquaman-couplages-invisibles-legal-it.md` (rapport Aquaman tour
1) cite le couplage Legal × IT parmi les 4 couplages hors matrice
canonique. Le triplet 29 (Cyborg veto) est *catégoriel* sur *«
fournisseur cloud-only sans chemin de sortie documenté »*.

**Concrètement** : le chemin de sortie = **3 éléments**
(indissociables) :

1. **Clause contractuelle de réversibilité** (Aquaman, Legal) —
   le contrat prévoit la sortie (data export, durée préavis, coût
   de sortie).
2. **IaC décrivant l'infra** (Cyborg, IT) — Terraform/Ansible
   permet de re-créer l'infra ailleurs.
3. **Failover local documenté** (Cyborg, IT) — un incident-type
   (game day / chaos engineering) a été joué, le RTO est chiffré.

Sans les trois, le chemin de sortie n'est pas *documenté*. Le veto
catalogue exige les trois (cf. [[cyborg-veto-cloud-only-sortie]] §Le
motif canonique).

## Le triplet canonique réversibilité = contrat + IaC + failover

C'est un **triplet Cyborg ↔ Aquaman** : Aquaman tient le **contrat**,
Cyborg tient l'**IaC + failover**. Les deux sont *complémentaires*,
pas redondants.

```
Aquaman (Legal) ─────> clause de réversibilité contractuelle
                           │
                           v
              Cyborg (IT) ─────> IaC + failover
                           │
                           v
              réversibilité documentée (veto levé)
```

**Lecture** : un veto Cyborg *« cloud-only sans chemin de sortie »*
peut être levé par Aquaman *« + cette clause de réversibilité »*
même si Cyborg n'a pas encore joué le game day. Mais l'inverse est
faux : Cyborg ne peut pas lever son veto sur la base d'une clause
contractuelle seule — l'IaC et le failover sont *lui* qui les tient.

## Trois cas concrets où le couplage se manifeste

### Cas 1 — Vendor SaaS GAFAM avec clause export, sans IaC

Un fournisseur SaaS (ex : Notion Cloud) qui **a** une clause d'export
des données en JSON standard (Aquaman OK), mais **n'a pas** d'IaC
Terraform/Ansible décrivant l'infra (Cyborg veto). Le triplet est
*partiel* (2/3) — réversibilité *non documentée*.

**Test concret** : la clause d'export est-elle présente ?
- OUI → Aquaman signe *« réversibilité contractuelle OK »*.
- NON → Aquaman veto *« pas de clause = pas de réversibilité »*.

Mais Cyborg ajoute : *« l'IaC n'est pas là, le failover n'est pas
joué. Donc le triplet est incomplet. »* **Résultat** : veto Cyborg
*« chemin de sortie non documenté »* — Aquaman ne peut pas le lever
seul.

### Cas 2 — Vendor SaaS avec IaC complet, sans clause contractuelle

Un fournisseur SaaS (ex : Scaleway) qui a un **repo Terraform
public** décrivant l'infra (Cyborg OK IaC), un **game day joué**
avec RTO chiffré (Cyborg OK failover), mais **pas** de clause
contractuelle de réversibilité (Aquaman veto). Le triplet est
*partiel* (2/3) — réversibilité *non documentée contractuellement*.

**Test concret** : la clause d'export est-elle dans le contrat ?
- OUI → Cyborg accepte le triplet.
- NON → Aquaman veto *« pas de clause = pas de réversibilité »*.
  Cyborg ne peut pas *seul* signer.

### Cas 3 — Vendor open-source auto-hébergé, sans contrat du tout

Un fournisseur open-source (ex : NextCloud) **n'a pas de contrat**
(Aquaman : il n'y a pas de vendor à contrat). Mais le chemin de
sortie est *intrinsèque* (le code est ouvert, l'infra est auto-hébergée).
Le triplet est *non-applicable* (3/3 par construction).

**Test concret** : le code est-il ouvert ? L'infra est-elle
auto-hébergée ? OUI/UI → réversibilité par construction, pas
besoin de triplet.

**Cas spécial** : un fork commercial d'un open-source (ex : NextCloud
Enterprise) qui *introduit* un contrat. Le triplet redevient
applicable.

## La matrice de réversibilité à 5 niveaux

Le couplage Legal × IT peut être modélisé en 5 niveaux de
réversibilité documentée :

| Niveau | Contrat | IaC | Failover | Statut |
|---|---|---|---|---|
| **0 — Vendor lock-in total** | ❌ | ❌ | ❌ | **VETO Cyborg** (cloud-only, pas de sortie) |
| **1 — Contrat seul** | ✅ | ❌ | ❌ | **VETO Cyborg** (triplet incomplet) |
| **2 — IaC seul** | ❌ | ✅ | ❌ | **VETO Cyborg** (triplet incomplet) |
| **3 — Failover seul** | ❌ | ❌ | ✅ | **VETO Cyborg** (triplet incomplet) |
| **4 — Triplet partiel** (2/3) | ✅ | ✅ | ❌ ou ✅ | **VETO Cyborg** (triplet non documenté complet) |
| **5 — Triplet complet** | ✅ | ✅ | ✅ | **OK** (réversibilité documentée) |
| **6 — Open-source auto-hébergé** | N/A | ✅ (par construction) | ✅ (par construction) | **OK** (réversibilité par construction) |

**Lecture** : un seul niveau *vrai* sans veto est le niveau 5 ou 6.
Les niveaux 1-4 sont **incomplets** — chacun est *insuffisant*
seul.

**Statut** : cette matrice est **mon raisonnement** par combinaison
du triplet 29 + le triplet Aquaman (clause contractuelle) + la
doctrine IT (IaC + failover). Pas promue en amplification
canonique.

## Trois cas d'abus du couplage Legal × IT

### Abus 1 — Cyborg qui impose une clause contractuelle

Cyborg qui dit *« tu n'as pas de clause de réversibilité, donc
veto »* alors qu'Aquaman n'a pas été consulté. C'est Cyborg qui
*statue* sur le contrat. Mais le contrat est *Legal*, pas IT.

**Test concret** : la clause de réversibilité est-elle dans le
contrat ? Cyborg ne peut pas le dire — il faut qu'Aquaman lise le
contrat. Cyborg demande *« Aquaman, cette clause est-elle présente
? »*. Aquaman répond. Cyborg statue sur l'IaC et le failover.

### Abus 2 — Aquaman qui impose une exigence IaC

Aquaman qui dit *« ton IaC n'est pas complet, donc pas de clause
contractuelle »*. C'est Aquaman qui *statue* sur l'IaC. Mais l'IaC
est *IT*, pas Legal.

**Test concret** : le repo Terraform existe-t-il ? Le game day a-t-il
été joué ? Aquaman ne peut pas le dire — il faut que Cyborg évalue.
Aquaman demande *« Cyborg, l'IaC et le failover sont-ils documentés
? »*. Cyborg répond. Aquaman statue sur la clause.

### Abus 3 — Décision conjointe sans consultation mutuelle

Cyborg et Aquaman qui prennent une décision *« vendor OK »* sans
s'être consultés mutuellement. C'est un **bypass du couplage**.

**Test concret** : la décision touche-t-elle les deux domaines ?
Oui → les deux doivent être consultés. **Résultat** : le triplet
est complet ou non — pas un *mix* arbitraire.

## La règle de résolution pratique

Quatre issues possibles, par ordre de fréquence :

1. **Triplet complet, OK** (Cas 1 / 2 résolus, ou Cas 3 par
   construction) — réversibilité documentée, veto levé.
   **Résultat** : vendor accepté.
2. **Triplet partiel, amendement** — Aquaman ou Cyborg amende le
   triplet (ajout clause, ajout IaC, ajout failover) dans un
   délai imparti. **Résultat** : vendor accepté *avec* amendement
   (date de revue).
3. **Triplet partiel, escalade Council** — Aquaman et Cyborg ne
   s'accordent pas sur l'amendement. **Résultat** : B2 Council
   arbitre.
4. **Triplet incomplet, veto maintenu** — aucun amendement possible,
   vendor rejeté. **Résultat** : vendor refusé, alternative
   souveraine proposée.

## La chaîne canonique Legal → IT (Aquaman → Cyborg)

Le couplage Legal × IT *s'étend* à Flash (Product) et Superman
(Growth) via les pair-checks #7 et #8 (Legal → Growth et Legal →
Product) :

```
Aquaman (Legal, A sur #7 #8)
       │
       ├──> Superman (Growth, C sur clause de réversibilité)
       │
       └──> Flash (Product, C sur dépendance IT)
              │
              └──> Cyborg (IT, A sur la sortie #4)
                     │
                     └──> Kang Dynasty (B3 IT, R)
```

**Lecture** : la clause de réversibilité touche *plusieurs*
domaines en cascade. Cyborg est *en bout de chaîne* — il hérite
de la clause Aquaman et la *transpose* en IaC + failover.

## La matrice 9 pair-checks ↔ couplage Legal × IT

`b2-pair-check-raci-by-rank.md` pose la matrice 9 pair-checks.
Aquaman est **A** sur #7 (Legal → Growth) et #8 (Legal → Product).
Cyborg est **C** sur les deux pair-checks *indirectement*
(cf. [[cyborg-pair-checks-product-it-fantastic-four]] §Les
pair-checks où Cyborg est Impliqué en dépendance).

**Concrètement** : un claim marketing (Superman) ou une feature
(Flash) qui expose une dépendance IT sans réversibilité déclenche
un arbitrage Aquaman � Cyborg *en cascade* :

1. Aquaman veto *« claim expose dépendance IT non réversible »*.
2. Cyborg alerte *« dépendance IT cloud-only sans chemin de
   sortie »*.
3. Les deux vetos sont *cumulables* — le Council arbitre.

## Anti-pièges spécifiques Legal × IT

- **Confondre réversibilité contractuelle et technique.** La clause
  Aquaman dit *« tu peux exporter les données »*. L'IaC Cyborg dit
  *« tu peux re-créer l'infra ailleurs »*. Le failover Cyborg dit
  *« tu peux basculer en <1h ». Les trois sont *différents*.
- **Open-source = réversibilité gratuite.** Pas tout à fait. Un
  open-source *sans IaC* est *non documenté* quand même. Le code
  est portable, mais l'infra actuelle ne l'est pas.
- **Vendor avec clause seul.** Clause seule = pas suffisant.
  *Contrat sans IaC* = le vendor peut révoquer la clause.
- **Cloud GAFAM = réversibilité par défaut.** Faux. La réversibilité
  doit être *documentée*, pas présumée. Un GAFAM avec clause + IaC
  + failover est OK. Sans un seul des trois, c'est veto.

## Liens

- [[cyborg-veto-cloud-only-sortie]] — le veto Cyborg (motif triple)
- [[cyborg-domain-it-perimetre-frontieres]] — le périmètre IT
- [[cyborg-pair-checks-product-it-fantastic-four]] — RACI #4 et chaîne Ops
- [[cyborg-couplage-people-charge-kang]] — couplage People × IT transverse
- [[aquaman-couplages-invisibles-legal-it]] — couplages Legal × IT (Aquaman)
- [[b2-eight-domain-vetoes-catalogue]] — les trois propriétés du veto
- [[b2-council-arbitrage-rule]] — quand le Council arbitre les vetos cumulés

## Note de confiance

**Confirmé par machine** pour le triplet 29 (Cyborg veto verbatim) +
le triplet Aquaman (clause de réversibilité, rapport tour 1). La
matrice 5 niveaux est **mon raisonnement** par combinaison des
trois éléments (contrat + IaC + failover) — pas une amplification
canonique. Les trois cas concrets sont **projetés** depuis le
triplet 29 + la doctrine IT + la doctrine Legal. Les trois cas
d'abus sont **reconstruits** depuis la matrice d'harmonisation
(asymétrie de veto cumulable). La chaîne canonique Legal → IT →
Ops est **reconstruite** depuis la matrice 9 pair-checks. Le
couplage Cyborg C sur #7 #8 est **projeté** depuis le RACI par
rang — pas explicitement écrit dans une source canonique unique.
