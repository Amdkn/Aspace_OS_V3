---
type: Concept
title: Aquaman — la transition dormant ↔ activation, trois états distincts
description: Aquaman a trois états opérationnels distincts — dormant (triplet 35, Coach-OS), SHADOW_ACTIVE (dossier OMK 08_Legal), et ACTIVE (premier livrable émis). Le seuil d'activation n'est pas le même selon le contexte projet. La doctrine "Aquaman dormant" est sur-généralisée si elle est appliquée hors Coach-OS. Tour 2 nuance la question 1 du brief (où s'arrête le périmètre).
tags: [b2, aquaman, dormant, shadow-active, activation, master-agreements, omk, coach-os]
generated: { by: minimax-m3, at: 2026-08-19T04:10:00Z }
verified:
  - { by: process:lecture-canon-aquaman-tour-2, at: 2026-08-19T04:10:00Z }
sources:
  - id: triplet-35
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 35 — Aquaman steward domaine dormant"
    last_modified: 2026-08-17
  - id: triplet-36
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 36 — domaine Legal dependsOn premier contrat signé"
    last_modified: 2026-08-17
  - id: legal-readme-omk
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/README.md"
    title: "08 Legal - Aquaman / Eternals — frontmatter status: SHADOW_ACTIVE"
    last_modified: 2026-05-25
  - id: legal-control-room-omk
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: "Legal Control Room — frontmatter status: SHADOW_ACTIVE"
    last_modified: 2026-05-27
  - id: legal-pipeline-omk
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md"
    title: "Rock → DoD → JTBD Pipeline — frontmatter status: SHADOW_ACTIVE"
    last_modified: 2026-05-27
  - id: legal-swarm-supervision-omk
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/02_B3_SWARM_SUPERVISION_PROTOCOL.md"
    title: "B3 Swarm Supervision Protocol — frontmatter status: SHADOW_ACTIVE"
    last_modified: 2026-05-27
okf_version: "0.2"
---

# Aquaman — la transition dormant ↔ activation

## Pourquoi cette nuance compte

Le concept [[aquaman-domaine-legal-perimetre]] pose la doctrine *«
Aquaman dormant tant que `00_Summers_CEO/03_Master_Agreements/`
reste vide »* (triplet 35). Cette doctrine est **vérifiée verbatim**
pour Coach-OS — la source du triplet 35 est
`coach-os/.../Aquaman_Eternals/VP_AGENT.md`.

Mais la même Aquaman, dans le projet OMK, a un frontmatter
`status: SHADOW_ACTIVE` sur les 4 fichiers canoniques du dossier.
**SHADOW_ACTIVE et dormant ne sont pas synonymes.**

- **Dormant** = *flow de production gelé*, veto catalogue valide,
  pair-checks Consulted tiennent.
- **SHADOW_ACTIVE** = *flow de production activé en mode shadow* —
  la squad B3 peut produire des *drafts* (privacy reviews, contract
  templates), mais les *outputs* ne sont pas *Business Done* sans
  revue B2 + signature humaine.

Ce concept distingue les **trois états** possibles d'Aquaman et
formalise les seuils de transition.

## Les trois états opérationnels

### État 1 — Dormant (Coach-OS, pré-Master Agreement)

**Définition** : aucun fichier dans `00_Summers_CEO/03_Master_Agreements/`.

**Propriétés** :
- Pas de `SPRINTS.md` Legal produit.
- Pas de JTBD émis vers Eternals.
- Veto catalogue **tient** sur les pair-checks qui touchent Legal.
- Pair-checks #7 et #8 restent Consulted.
- Squad Eternals catalogué mais non activé.

**Source** : triplet 35 (verbe `stewards`) — *« Aquaman steward
Legal & Compliance en état dormant : ne produit rien tant que
`00_Summers_CEO/03_Master_Agreements/` reste vide — un domaine dormant
qui produit est un coût sans contrepartie. »*

**Conséquence opérationnelle** : un Aquaman en état dormant qui
produit un `SPRINTS.md` Legal *avant* le premier Master Agreement
crée un livrable sans consumer. C'est un anti-piège ([[aquaman-antipieges-faux-pas-typiques]]
§Anti-piège 1).

### État 2 — SHADOW_ACTIVE (OMK, et tout projet en pré-launch)

**Définition** : le frontmatter `status: SHADOW_ACTIVE` est posé sur
les 4 fichiers canoniques du dossier domaine (`README.md`,
`00_B2_DOMAIN_CONTROL_ROOM.md`, `01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md`,
`02_B3_SWARM_SUPERVISION_PROTOCOL.md`). Aucun livrable *Business Done*
n'a été émis, mais la squad peut tourner.

**Propriétés** :
- `SPRINTS.md` Legal peut être produit en *shadow* (drafts non
  Business Done).
- JTBD packets émis vers Eternals, mais outputs marqués
  `DRAFT_FOR_REVIEW`, pas `LEGAL_READY`.
- Veto catalogue tient *et* est *proactivement* vérifié sur les
  claims publiques (le projet OMK peut publier des claims en
  pré-launch, et Aquaman les examine *avant* qu'elles aillent en
  production).
- Squad Eternals activé en *shadow execution* — les agents
  produisent des artefacts mais Aquaman ne signe pas.

**Source** : frontmatter des 4 fichiers OMK
`08_Legal_Aquaman_Eternals/`* datés 2026-05-25 et 2026-05-27.

**Conséquence opérationnelle** : SHADOW_ACTIVE est un état *plus
avancé* que dormant, mais *moins avancé* que ACTIVE. Un projet qui
utiliserait le label `SHADOW_ACTIVE` doit avoir (a) des 4 fichiers
canoniques posés, (b) une squad cataloguée, (c) un flow de production
shadow qui tourne.

### État 3 — ACTIVE (premier livrable signé)

**Définition** : Aquaman a émis au moins un `LEGAL_READY` ou un
`BLOCKED_RISK` *non-shadow*, c'est-à-dire que le B2 captain a
signé un packet mésoperpétuel et que la sortie est *Business Done*
(pas *DRAFT_FOR_REVIEW*).

**Propriétés** :
- `SPRINTS.md` Legal en cycle normal.
- JTBD packets émis en mode normal (pas shadow).
- Veto catalogue tient *et* est opposable — un Aquaman ACTIVE qui
  oppose un veto arrête la production, pas seulement le shadow.
- Pair-checks #7 #8 deviennent des blocages durs (le `BLOCKED_RISK`
  émis n'est plus *draft*, il est *operational*).
- Squad Eternals activé en *full execution* — les agents produisent
  et Aquaman signe.

**Source** : implicite — la doctrine opérationnelle (cf.
`b2-meso-decision-packet-spec.md` et `b2-council-arbitrage-rule.md`)
suppose un Aquaman ACTIVE pour émettre des packets mésoperpétuels.
**Aucun packet mésoperpétuel Legal n'a été observé en Vague 1 ou
Vague 2** (cf. rapport tour 1 §4.3).

**Conséquence opérationnelle** : un Aquaman ACTIVE peut bloquer un
launch par veto, ce qu'un Aquaman SHADOW_ACTIVE ne peut pas (un
veto sur un draft est un signal, pas un arrêt). La différence est
*engagement contractuel* — un veto ACTIVE engage la responsabilité
d'Aquaman sur la décision de blocage.

## Le seuil d'activation

Chaque état a son seuil, et **les seuils ne sont pas les mêmes**.

| État | Seuil d'entrée | Seuil de sortie |
|---|---|---|
| **Dormant** | (état initial) | Premier fichier dans `00_Summers_CEO/03_Master_Agreements/` (triplet 36) |
| **SHADOW_ACTIVE** | 4 fichiers canoniques posés + squad cataloguée + frontmatter `status: SHADOW_ACTIVE` | Premier `LEGAL_READY` ou `BLOCKED_RISK` signé |
| **ACTIVE** | Premier livrable Business Done signé | (état terminal — pas de retour à SHADOW_ACTIVE prévu) |

**Trois lectures** :

1. **Pour Coach-OS** : le seuil Dormant → SHADOW_ACTIVE n'est pas
   posé. Coach-OS peut sauter directement à ACTIVE quand le premier
   Master Agreement est signé, ou rester Dormant jusqu'à un audit
   B1 qui force l'activation. **À clarifier** : aucun triplet ne
   pose le seuil Dormant → SHADOW_ACTIVE pour Coach-OS.
2. **Pour OMK** : le seuil Dormant (jamais observé) → SHADOW_ACTIVE
   a été franchi le 2026-05-25 (date des fichiers OMK). Le seuil
   SHADOW_ACTIVE → ACTIVE n'a pas été franchi — les 4 fichiers
   canoniques OMK sont toujours `status: SHADOW_ACTIVE` au
   2026-08-19, sans qu'aucun packet mésoperpétuel Legal n'ait été
   enregistré.
3. **Pour un nouveau projet** : un projet qui copie la structure
   OMK pose d'abord les 4 fichiers en SHADOW_ACTIVE, puis monte à
   ACTIVE quand le premier livrable est signé. **Ouverture** :
   faut-il un état *PRE_DORMANT* pour les projets qui n'ont pas
   même pas les 4 fichiers canoniques posés ?

## La triple asymétrie entre les trois états

### Asymétrie 1 — La production

- Dormant : pas de production.
- SHADOW_ACTIVE : production shadow (drafts).
- ACTIVE : production signée (Business Done).

**Conséquence** : un Aquaman SHADOW_ACTIVE *peut* produire un
privacy review, mais ce review n'est pas *Business Done*. Un Flash
(Product) qui demande un privacy review à un Aquaman SHADOW_ACTIVE
reçoit un draft — et doit savoir qu'il engage sa propre
responsabilité sur la base d'un draft, pas d'un `LEGAL_READY`.

### Asymétrie 2 — Le veto

- Dormant : veto catalogue tient mais ne s'oppose *jamais* (pas de
  pair-check à bloquer).
- SHADOW_ACTIVE : veto catalogue s'oppose en mode *shadow* — c'est
  un signal, pas un arrêt. Superman (Growth) peut choisir de
  publier la claim malgré le veto Aquaman, en gardant trace que le
  veto a été émis.
- ACTIVE : veto catalogue s'oppose en mode *operational* — la
  production est arrêtée jusqu'à amendement ou escalade B1.

**Conséquence** : un Superman qui publie une claim *avec* un veto
shadow Aquaman non levé engage Superman, pas Aquaman. C'est une
*information*, pas un *blocage*.

### Asymétrie 3 — Le coût

- Dormant : coût zéro (pas de production, pas de veto opposé).
- SHADOW_ACTIVE : coût modéré (production shadow, veto shadow,
  squad activée mais non signée).
- ACTIVE : coût complet (production signée, veto opposable, squad
  en full execution).

**Conséquence** : le passage à SHADOW_ACTIVE a un coût qui doit
être *budgeté* (Wonder Woman — Finance — veto *« dépense récurrente
sans date de revue »*). Le passage à ACTIVE a un coût plus élevé
encore — c'est l'engagement complet d'Aquaman sur la production.

## L'anti-bottleneck appliqué à la transition

Le pipeline Rock → DoD → JTBD pose l'anti-bottleneck rule (cf.
`01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md` §Anti-Bottleneck) : *« If B2
must answer more than one clarification before B3 can start, the
JTBD is too vague. Rewrite the job, not the swarm. »*

Appliqué à la transition d'état : si Aquaman doit clarifier plus
d'une fois *quel* état il occupe (Dormant / SHADOW_ACTIVE / ACTIVE)
avant que B3 Eternals puisse produire, alors **la doctrine d'état
est trop vague**. La clarification doit être explicite dans le
frontmatter — c'est pour ça que les 4 fichiers OMK ont
`status: SHADOW_ACTIVE` en YAML, pas en prose.

**Conséquence pour la doctrine** : un Aquaman sans frontmatter
explicite est *forcé* de clarifier son état à chaque cycle. Un
Aquaman avec frontmatter `status: SHADOW_ACTIVE` n'a pas à le
clarifier — il l'a posé une fois.

## Anti-pièges

- **Appliquer la doctrine dormant hors Coach-OS.** Le triplet 35 est
  Coach-OS-spécifique. Un OMK qui se déclare *dormant* est
  sém-erroné — OMK est SHADOW_ACTIVE.
- **Confondre SHADOW_ACTIVE et ACTIVE.** Un Aquaman SHADOW_ACTIVE
  qui émet un `LEGAL_READY` *non-shadow* sort de son mandat. Le
  packet mésoperpétuel doit porter `status: ACTIVE` ou
  `status: SHADOW_DRAFT`, pas un statut inventé.
- **Sauter SHADOW_ACTIVE.** Un projet qui n'a pas posé les 4
  fichiers canoniques ne peut pas être SHADOW_ACTIVE. Il est
  Dormant (état par défaut) jusqu'à ce que les fichiers soient
  posés.
- **Croire que ACTIVE est irréversible.** Un Aquaman ACTIVE peut
  redescendre à SHADOW_ACTIVE si B1 amende le seuil d'activation
  (par exemple en cas de pause cycle). Le catalogue mésoperpétuel
  doit tracer la transition, pas l'effacer.

## Liens

- [[aquaman-domaine-legal-perimetre]] — le périmètre (7 surfaces)
  et l'état dormant posé en tour 1
- [[aquaman-squad-eternals-et-dormance]] — la tension effectif
  Eternals (10 / 4 / ~7)
- [[aquaman-jtbd-emit-receive]] — les 4 formes émises, qui ne
  s'activent qu'à partir de SHADOW_ACTIVE
- [[aquaman-couplages-invisibles]] — couplage Aquaman ↔ Wonder
  Woman (honoraires juridiques) qui devient actif à partir de
  SHADOW_ACTIVE
- [[aquaman-veto-engagement-sans-perimetre]] — le veto dont la
  force opérationnelle dépend de l'état (Dormant → shadow,
  ACTIVE → operational)

## Note de confiance

**Confirmé par machine pour les sources ; reconstruit pour la
synthèse trois états.** Le triplet 35-36 et les frontmatters OMK
`satus: SHADOW_ACTIVE` sont cités verbatim. **La tri-partition
(Dormant / SHADOW_ACTIVE / ACTIVE) est reconstruite** à partir du
frontmatter OMK et de la doctrine d'arbitrage mésoperpétuel — elle
n'est pas posée comme un triplet canonique ou un SDD. **À vérifier
en cycle** : (1) un Aquaman peut-il rester Dormant sans jamais
passer à SHADOW_ACTIVE ?, (2) un Aquaman SHADOW_ACTIVE peut-il
sauter à ACTIVE sans transition ?, (3) un Aquaman ACTIVE peut-il
redescendre à SHADOW_ACTIVE sans escalade B1 ? **Ces trois questions
restent ouvertes** et sont reportées au rapport tour 2.