---
type: Concept
title: People — formule de calcul de charge, méthode et seuils ASSIGNED
description: Le gate People `ASSIGNED` exige une charge tenable, mais le canon V4 ne pose aucune formule de calcul. Le concept propose une formule de charge par owner (somme pondérée des mandats actifs divisée par capacité), trois modes de pondération (horizon, criticité, couplage), trois seuils (vert ≤ 0.7, ambre 0.7-1.0, rouge > 1.0), et une procédure d'objectivation (journal de charge, audit mensuel, escalade). Reconstruit, à arbitrer par B2 Council.
tags: [people, green-lantern, charge, formule, capacity, gate, assigned, calcul, seuil, b2]
generated: { by: minimax-m3, at: 2026-08-19T05:05:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-2, at: 2026-08-19T05:05:00Z }
sources:
  - id: green-lantern-gates-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-gats-assigned-needs-owner-dlq.md"
    title: "Tour 1 — People 3 états ASSIGNED / NEEDS_OWNER / DLQ"
    last_modified: 2026-08-19
  - id: harmonization-pair-check-9
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: "Matrice d'harmonisation — pair-check #9 People → Tous (charge tenable)"
    last_modified: 2026-08-17
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — coordinateur transverse People
    last_modified: 2026-08-17
  - id: green-lantern-perimetre-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-perimetre-frontieres.md"
    title: "Tour 1 — People (Green Lantern / X-Men) périmètre"
    last_modified: 2026-08-19
  - id: triplet-34-beast
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 34 — Beast TechRecruiting compétence réelle"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# People — formule de calcul de charge, méthode et seuils ASSIGNED

## Le constat — un gate sans formule

Le tour 1 a posé le gate People `ASSIGNED` (cf.
`green-lantern-people-gats-assigned-needs-owner-dlq.md`) avec un
**seuil de charge ≤ 1.0** comme condition d'activation. Mais le seuil
1.0 est **projeté** depuis le framework capacité classique — le canon
V4 ne pose aucune formule de calcul, aucune pondération, et aucun seuil
chiffré.

Sans formule, le passage de `NEEDS_OWNER` à `ASSIGNED` est
**subjectif** : chaque captain de domaine peut contester la lecture
People de la charge. Le canon Council n'a pas de critère pour
arbitrer. Le gate People n'est pas **opérationnalisable** en l'état.

Le présent concept propose une **formule reconstruite**, trois modes
de pondération, trois seuils, et une procédure d'objectivation. Ce
n'est **pas** une lecture canonique — c'est une **proposition à
arbitrer** par le B2 Council.

## La formule de charge par owner

### Définition

Pour un owner `o`, la charge `C(o)` est définie par :

```
C(o) = Σ (poids_m × m_actif) / capacité(o)
```

Où :

- `m_actif` est un mandat actif dont `o` est owner (Assigned ou en
  cours).
- `poids_m` est un coefficient de pondération du mandat (entier ou
  demi-entier, voir §« Trois modes de pondération » ci-dessous).
- `capacité(o)` est la capacité de référence de `o` (par défaut 1.0,
  voir §« Capacité de référence » ci-dessous).

### Capacité de référence

Trois valeurs de capacité par défaut, **reconstituées** depuis les
pratiques RH courantes et le triplet 34 (Beast TechRecruiting —
*« compétence réelle »*) :

| Type d'owner | Capacité par défaut | Justification reconstruite |
|---|---|---|
| Owner humain plein-temps | 1.0 | Mandat standard, scope unique |
| Owner humain partagé (multi-mandats) | 0.5 par mandat | Scope divisé |
| Agent B3 squad Marvel | 1.0 | Mandat dédié, exécution |
| Agent générique | 0.5 par mandat | Multi-tâche par construction |

**Note de confiance.** Ces valeurs sont **reconstituées** depuis la
pratique RH classique — le canon V4 ne pose aucune capacité de
référence. Le triplet 34 parle de *« compétence réelle »* sans
définir de grandeur. La capacité 0.5 pour les owners partagés est
**une hypothèse** — à arbitrer.

## Trois modes de pondération

Le poids d'un mandat `poids_m` est **variable** selon le mode choisi.
Trois modes sont proposés, **non mutuellement exclusifs** : le Council
peut en choisir un, ou en combiner.

### Mode 1 — Pondération par horizon

**Définition.** `poids_m = 1.0` si horizon ≤ 1 cycle 12WY, `0.5` si
horizon > 1 cycle. Justification : un mandat court mobilise plus
d'attention (ramp-up, livrable serré), un mandat long s'étale.

**Avantage.** Simple, mesurable, peu contestable.

**Inconvénient.** Ignore la criticité (un mandat *« support client
incident »* à 1 semaine pèse 1.0 — ce qui est sous-estimé).

### Mode 2 — Pondération par criticité

**Définition.** `poids_m = 1.0` (standard), `1.5` (critique —
déclenchement d'un red flag matrice si manqué), `2.0` (bloqueur — le
mandat est un goulot pour un autre domaine). Justification : un
mandat critique mobilise plus de bande passante (escalades, lead
indicators, etc.).

**Avantage.** Reflète la **vraie** mobilisation d'attention.

**Inconvénient.** La criticité est **subjective** — le captain du
domaine d'accueil peut sur-pondérer ses propres mandats. Le Council
doit **auditer** la criticité.

### Mode 3 — Pondération par couplage transverse

**Définition.** `poids_m = poids_criticité × (1 + 0.25 × n_couplages)`,
où `n_couplages` est le nombre de pair-checks canoniques (matrice
d'harmonisation) que le mandat active. Justification : un mandat
transverse (People × IT × Legal) coûte plus qu'un mandat isolé.

**Avantage.** Intègre la **matrice d'harmonisation** comme grille de
lecture.

**Inconvénient.** Le calcul est **plus lourd** à tenir. Déconseillé
pour un gate hebdomadaire — plutôt pour un audit mensuel.

## Les trois seuils

Une fois la charge `C(o)` calculée, trois seuils fixent l'état
People :

| Seuil | Plage | État | Action |
|---|---|---|---|
| **Vert** | `C(o) ≤ 0.7` | `ASSIGNED` tenable | Aucune |
| **Ambre** | `0.7 < C(o) ≤ 1.0` | `ASSIGNED` sous tension | Lead indicator à suivre, revue sous 30 jours |
| **Rouge** | `1.0 < C(o) ≤ 1.3` | `NEEDS_OWNER` partiel — surcharge | Escalade B2 sponsor + plan de désengagement |
| **Noir** | `C(o) > 1.3` | `NEEDS_OWNER` total — burn-out imminent | Escalade B1, désassignation immédiate ou renfort |

**Note de confiance.** Les seuils 0.7 / 1.0 / 1.3 sont **reconstitués**
depuis la pratique RH. Le seuil 1.0 correspond à *« 100% de la
capacité, plus rien à donner »*. Le seuil 0.7 est un **marge de
sécurité** pour absorber un mandat imprévu sans saturer. Le seuil
1.3 est un **seuil de rupture** au-delà duquel la performance
décroît (loi de Yerkes-Dodson appliquée à la charge de travail —
**projetée**, pas citée).

## La procédure d'objectivation

La formule sans procédure est **inopérante** : un captain peut
toujours contester la lecture People de sa propre charge. Trois
gadgets d'objectivation.

### Gadget 1 — Journal de charge hebdomadaire

**Format.** Pour chaque owner `o`, une ligne par semaine avec :
- `o` (identifiant owner).
- `mandats_actifs` (liste des mandats actifs ce jour).
- `poids_m` (mode choisi, valeur par mandat).
- `C(o)` (charge calculée).
- `seuil` (vert / ambre / rouge / noir).
- `note_owner` (champ libre, ≤ 50 mots).

**Lieu.** Le journal vit dans le packet mésoperpétuel hebdomadaire
Council, append-only, et alimente le `next_review` de chaque
arbitrage.

**Justification.** Sans journal, la charge est **reconstituée à
posteriori** en cas de conflit — ce qui ouvre la porte aux
contestations.

### Gadget 2 — Audit mensuel croisé

**Mécanisme.** Une fois par mois, deux capitaines B2 (autres que
People) **croisent** le journal de charge People avec leur propre
carte de charge. Si la lecture People d'un owner diffère de la
lecture du captain d'accueil de plus de 0.2, le cas est porté en
séance Council.

**Justification.** L'audit croisé est un **garde-fou** contre la
subjectivité People — un captain qui gonfle ses poids pour
apparaître sous-chargé, ou qui les sous-estime pour cacher une
saturation, est détecté par le croisement.

### Gadget 3 — Escalade automatique à seuil

**Mécanisme.** Quand `C(o) > 1.0` pendant deux semaines
consécutives, le journal génère **automatiquement** un packet
`NEEDS_OWNER` dans la wheel du domaine d'accueil. Pas de discussion
inter-domaines — le packet est posé, et le captain d'accueil
arbitre (réduction de scope, renfort, ou re-scope).

**Justification.** L'escalade automatique évite le **signal
négligé** — People signale, mais le domaine d'accueil peut ignorer
le signal. Le packet automatique force la conversation.

## Le cas asymétrique — owners sans journal de charge

Tous les owners n'ont pas un journal de charge tenu. C'est le cas
typique des **agents génériques** (non X-Men) ou des owners
**vacataires**. Pour ces owners, la formule de charge ne s'applique
**pas** — People applique un **seuil par défaut** : *« tout owner
sans journal est `NEEDS_OWNER` par défaut, jusqu'à preuve du
contraire »*.

**Justification.** Un owner sans journal est un **signal** que
People ne tient pas la carte de charge. Le défaut `NEEDS_OWNER`
force la conversation — l'owner doit ouvrir un journal, ou être
réassigné.

## Anti-pièges

- **Pondération par horizon seul.** Le Mode 1 ignore la criticité.
  Un mandat *« support incident »* à 1 semaine pèse 1.0, comme un
  mandat *« rédaction doc »* à 1 semaine. La différence de
  mobilisation n'est pas capturée.
- **Subjectivité de la criticité.** Le Mode 2 repose sur la
  **déclaration** du captain d'accueil. Sans audit (Gadget 2), la
  criticité est un outil rhétorique. Le captain qui veut charger
  un owner marque ses mandats comme critiques — sa charge gonfle,
  l'owner sature, et People signale `NEEDS_OWNER`. Le captain
  conteste, le Council arbitre. **Sans audit, le système est
  jouable.**
- **Capacité 0.5 pour les owners partagés.** L'hypothèse reconstruite
  *« un owner partagé a une capacité divisée par 2 »* n'est pas
  canonique. Un owner à 80% sur un projet et 20% sur un autre n'a
  pas une capacité 0.5 — il a deux mandats à poids 0.8 et 0.2 (ou
  inverse, selon le mode). La capacité 0.5 est un **raccourci**
  contestable.
- **Le seuil 1.0 comme vérité.** Le seuil 1.0 est **reconstitué**,
  pas mesuré. Un owner qui travaille à `C(o) = 1.05` n'est pas
  mécaniquement en surcharge — c'est un **signal** à arbitrer. Le
  Council peut valider un dépassement si le mandat est
  auto-contenu (livrable imminent, désengagement prochain).
- **Confondre charge et productivité.** `C(o)` est une mesure
  d'**occupation**, pas de **rendement**. Un owner à `C(o) = 0.5`
  peut être sous-productif ; un owner à `C(o) = 1.0` peut être très
  productif. La formule ne dit rien sur la qualité du livrable.

## Liens

- [[green-lantern-people-gats-assigned-needs-owner-dlq]] — les 3 états
  que la formule alimente
- [[green-lantern-people-perimetre-frontieres]] — qui porte la carte
  de charge (People)
- [[green-lantern-people-raci-transverse-jamais-A]] — pourquoi People
  est C (signale) et pas A (arbitre) sur la charge
- [[green-lantern-people-couplages-invisibles]] — la charge comme coût
  réentrant Finance (Wonder Woman veto)
- [[b2-harmonization-matrix-exploitable]] — la matrice qui teste la
  charge via le pair-check #9

## Note de confiance

**Reconstruit, à moitié étayé.** Le gap canonique est posé (canon V4
ne pose aucune formule de charge). La formule `C(o) = Σ poids / capacité`
est **reconstituée** depuis la pratique RH classique. Les trois modes
de pondération sont **projetés** depuis les triplets 34 et la matrice
d'harmonisation. Les seuils 0.7 / 1.0 / 1.3 sont **reconstitués** avec
référence implicite à la loi de Yerkes-Dodson (non citée canoniquement).
Les trois gadgets d'objectivation sont **ajouts** : pas de source
canonique, mais aucune source canonique ne les interdit. **À arbitrer
par B2 Council.** Le concept propose une **forme**, pas une
**vérité**.
