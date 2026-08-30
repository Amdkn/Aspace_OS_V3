---
type: Concept
title: Superman V4 vs Coach OS V1 — règle d'arbitrage de la divergence triplet 19
description: Le triplet v3 ligne 19 cite Superman comme "domaine 5 People & Brand" (Coach OS V1 héritage). Le triplet v3 ligne 27 le positionne en Growth (canon V4). Six autres triplets et triplet 35 (Aquaman dormant) ancrent V4. La règle d'arbitrage proposée: V4 = lecture courante, V1 = héritage non-superseded mais hors lecture canon. Procédure de signalement et règle de lecture pour les agents.
tags: [superman, growth, v4, v1, coach-os, divergence, arbitration, legacy]
generated: { by: minimax-m3, at: 2026-08-19T05:00:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-2, at: 2026-08-19T05:00:00Z }
sources:
  - id: triplet-v3-line-19
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet v3 ligne 19 — Superman pairedWith Guardians, domaine 5 People & Brand"
    last_modified: 2026-08-17
  - id: triplet-v3-line-27
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet v3 ligne 27 — Superman hasVetoOver promesse-non-tenue"
    last_modified: 2026-08-17
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Superman = 01 Growth
    last_modified: 2026-08-17
  - id: eight-domain-mapping
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — Superman ligne 5 Growth (01)
    last_modified: 2026-08-19
  - id: domain-perimeter-tour1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/domain-perimeter.md"
    title: Périmètre Superman tour 1 — héritage Coach OS V1 explicité
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Superman V4 vs Coach OS V1 — règle d'arbitrage de la divergence triplet 19

## La divergence canonique — deux lectures du même captain

Le corpus contient **deux lectures** de Superman qui ne sont pas
réconciliées par une note canonique explicite :

| Source | Domaine | Squad | Veto |
|---|---|---|---|
| Triplet v3 ligne 27 (canon V4) | **01 Growth** | Guardians | promesse-non-tenue |
| Triplet v3 ligne 19 (Coach OS V1) | **05 People & Brand** | Guardians | (non cité) |

Sept triplets (lignes 23-29 dans `triplets/v3-business.jsonl`)
ancrent la lecture V4 par alignement avec les 7 autres capitaines :
tous les triplets `pairedWith` suivent l'ordre V4 (Green Lantern
People, Batman Ops, Flash Product, Martian Manhunter Sales, **Superman
Growth**, Wonder Woman Finance, Cyborg IT, Aquaman Legal). Le
catalogue des 8 vetos (`b2-eight-domain-vetoes-catalogue.md`) ancre
Superman = classe #5 = Growth. Le mapping
`eight-domain-avengers-wheel.md` ancre Superman = 01 Growth = B2 emet
`GROWTH_READY` / `NEEDS_SIGNAL` / `BLOCKED_PROMISE`.

**Mais** : le triplet 19 cite Coach OS verbatim, avec mention *«
domaine 5 People & Brand »* — un intitulé qui ne correspond à aucun
des 8 domaines V4 canoniques (le 05 V4 = IT). C'est un héritage
direct du substrat `30_Business_OS/10_Projects/coach-os/04_Business_Domains/05_People_et_Brand_Superman_Guardians/VP_AGENT.md`,
où le dossier arborescence a été créé le 2026-08-02 avec l'intitulé
People & Brand.

## Pourquoi cette divergence existe

Deux lectures historiques se superposent :

1. **Lecture V4 (canonique courante)** — Superman = Growth =
   attention + qualification amont. Position prise dans la **Triptyque
   V4** d'OMK Business OS, ACTIVE 2026-07-15. Renforcée par le
   catalogue des 8 vetos et le mapping Avengers Wheel.
2. **Lecture Coach OS V1 (héritage)** — Superman = People & Brand =
   attention + brand + recrutement par propagation. Position prise à
   la création de l'arborescence Coach OS le 2026-08-02. Le triplet 19
   cite V1 sans note de mise à jour V4.

Aucune des deux lectures n'a été marquée *« legacy / superseded by
V4 »* dans le triplet 19. Le tour 1 Superman (cf.
`domain-perimeter.md` §« Pourquoi ces frontières existent ») a
documenté la divergence sans la trancher. La question est : **qui
peut trancher et selon quelle règle ?**

## La règle d'arbitrage proposée — V4 = lecture courante, V1 = héritage non-superseded

### Énoncé

> **V4 est la lecture courante pour tout arbitrage B2 Council. Le
> triplet 19 (Coach OS V1) est conservé comme héritage non-superseded,
> jamais ré-utilisé comme source primaire pour un arbitrage Council.**

Trois raisons :

1. **Cohérence structurelle** — V4 est ancré par 7 triplets
   (lignes 23-29), par le catalogue 8 vetos, par le mapping Avengers
   Wheel. Le triplet 19 est isolé. Une lecture isolée ne peut pas
   arbitrer contre une lecture convergente.

2. **Cohérence temporelle** — V4 (Triptyque ACTIVE 2026-07-15)
   précède Coach OS (2026-08-02) en statut canonique. Coach OS est
   *un projet* qui instancie le canon ; il ne le *crée* pas. Si
   Coach OS a utilisé un intitulé différent, c'est une erreur de
   reproduction locale, pas une réécriture du canon.

3. **Cohérence D4 append-only** — le triplet 19 n'a jamais été
   réécrit. Le marquer *« superseded by V4 »* est une édition a
   posteriori, ce que D4 interdit. Le triplet 19 reste dans son
   état. La règle de lecture est ajoutée à côté, pas en
   remplacement.

### Les trois usages licites du triplet 19

Le triplet 19 n'est pas détruit — il a trois usages licites :

1. **Trace d'historique** — un lecteur qui s'interroge sur
   l'arborescence Coach OS (`05_People_et_Brand_Superman_Guardians/`)
   trouve dans le triplet 19 l'explication de l'intitulé de dossier.
   L'information n'est pas fausse — elle est *datée*.

2. **Détection de contradiction** — un arbitrage Council qui
   s'appuierait sur le triplet 19 sans signaler la divergence V4
   doit être refusé par le Council. Le triplet 19 est un **filet de
   sécurité** contre les régressions silencieuses.

3. **Migration à finaliser** — Coach OS V1 a créé le dossier
   `05_People_et_Brand_Superman_Guardians/`. La migration vers un
   dossier `01_Growth_Superman_Guardians/` (aligné V4) est une
   tâche Coach OS, pas une tâche B2 Council. Le triplet 19 sert de
   pointeur pour cette migration.

### Les trois usages illicites du triplet 19

1. **Source primaire d'arbitrage** — Superman n'est pas
   People & Brand. Le Council ne peut pas s'appuyer sur le triplet
   19 pour statuer que Superman a autorité sur un livrable Brand.
2. **Justification de scope Brand hors Growth** — un mandat Brand
   qui s'appuie sur le triplet 19 pour échapper au périmètre Growth
   est invalide.
3. **Substitution à la lecture V4** — toute lecture qui ignore V4
   au profit de V1 doit être refusée par le captain sponsor.

## La procédure de signalement

Un arbitrage B2 Council qui touche Superman doit, dans le packet
mésoperpétuel, **déclarer** la lecture utilisée :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B1-B2-MANDATE-YYYY-NN
mode: parallel | handoff | negotiation
impacted_domains:
  - growth
tradeoff: short statement
decision: accepted | blocked | escalate_to_B1
superman_reading: v4_canonical | v1_legacy_exception
superman_reading_justification: <text>
proof_expected:
  - B2 gate update
  - B3 proof path
next_review: date-or-cycle
```

Le champ `superman_reading` est **par défaut** `v4_canonical`. La
valeur `v1_legacy_exception` ne peut être utilisée que si
l'arbitrage concerne un livrable Coach OS daté avant 2026-07-15, et
doit être accompagnée d'une `superman_reading_justification`.

## Le cas-limite Coach OS — quand V1 reste légitime

Coach OS a 53 agents + arborescence + dossiers V1. Tant que la
**migration** vers V4 n'est pas terminée, le dossier
`05_People_et_Brand_Superman_Guardians/` reste l'adresse physique.
Mais le **périmètre opérationnel** de Superman reste V4 Growth.

Concrètement : un B3 Guardians qui produit un livrable brand doit
être commandé par Superman (V4 Growth), même si son fichier est
logé dans le dossier V1 Coach OS. C'est une **anomalie
d'arborescence**, pas une anomalie de périmètre. Le captain
superman arbitre en mode parallel (livrable interne, pas de parole
publique) jusqu'à migration.

## La migration Coach OS à effectuer (hors périmètre vague 2)

Cette escouade **ne touche pas** Coach OS. Mais la migration est
notée pour traçabilité :

```
30_Business_OS/10_Projects/coach-os/04_Business_Domains/
  05_People_et_Brand_Superman_Guardians/   ← V1 héritage
  →  01_Growth_Superman_Guardians/         ← V4 cible (à créer)
```

La migration est une **tâche d'arborescence**, pas une décision
B2. Elle revient à l'agent Owner ou au Meta-Factory (cf. triplet
54 : *« coach-os-arborescence depend on meta-factory-moule »*).

## Anti-pièges

- **Triplet 19 comme source primaire.** Refusé par la règle. Tout
  arbitrage qui s'appuie sur le triplet 19 sans signaler la
  divergence est invalide.
- **Migration Coach OS par Superman.** Superman ne touche pas
  l'arborescence Coach OS. La migration est Owner / Meta-Factory.
- **Lecture V4 sans déclarer.** Le packet mésoperpétuel doit
  déclarer `superman_reading: v4_canonical`. Un packet sans le
  champ est incomplet.
- **V1 maintenu pour Brand.** Le périmètre Brand transverse reste
  People (Green Lantern). Superman Growth peut *exécuter* du
  Brand via Groot, mais c'est un scope creep à arbitrer — pas un
  périmètre acquis.

## Liens

- [[domain-perimeter]] — la frontière #2 Brand transverse documentée
- [[b2-eight-domain-vetoes-catalogue]] — Superman = classe #5 Growth
- [[eight-domain-avengers-wheel]] — le mapping V4 canonique
- [[b2-meso-decision-packet-spec]] — le format packet mésoperpétuel
- [[b2-council-arbitrage-rule]] — qui tranche un conflit de lecture

## Note de confiance

**Confirmé par machine pour la lecture V4, reconstruit pour la
règle d'arbitrage.** La lecture V4 = canon est confirmée par 7
triplets, le catalogue 8 vetos, le mapping Avengers Wheel. Le
triplet 19 est cité verbatim comme héritage Coach OS V1. La règle
d'arbitrage (V4 = lecture courante, V1 = héritage) est
**reconstruite** à partir des critères de cohérence (structurelle,
temporelle, D4 append-only) et de la pratique documentée du
catalogue 8 vetos. La procédure de signalement
(`superman_reading`) est **projetée** à partir du format packet
mésoperpétuel canonique (D4 append-only). La migration Coach OS
est **citée hors périmètre** — cette escouade ne la fait pas.