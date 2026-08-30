---
type: Concept
title: JohnJones — protocole de validation empirique du veto reformulation-validée (3 cas / 60 jours)
description: Le veto reformulation-validée est caractérisé dans 5 cas de déclenchement et 5 cas d'abus (cf. johnjones-veto-reformulation-validee.md), mais ces cas sont **projetés** depuis la doctrine canonique, pas étayés par des cas réels. Un protocole de validation empirique pose une cible de 3 cas observés en 60 jours, un type de packet mésoperpétuel, 5 critères d'acceptance par cas, et 3 indicateurs de couverture/distribution/vitesse. Analogue aux protocoles posés par Flash (veto-offre-depersonnalisee) et Superman (veto-prise-parole-publique) en tour 3.
tags: [b2, johnjones, sales, veto, validation, empirique, protocole, packet, cycle]
generated: { by: minimax-m3, at: 2026-08-19T05:40:00Z }
verified:
  - { by: process:lecture-corpus-sales-tour-3, at: 2026-08-19T05:40:00Z }
sources:
  - id: veto-reformulation
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-veto-reformulation-validee.md"
    title: Veto reformulation-validée — 5 cas de déclenchement + 5 cas abus
    last_modified: 2026-08-19
  - id: veto-catalogue
    resource: "C:/Users_amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — propriétés canoniques
    last_modified: 2026-08-19
  - id: packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique d'une décision B2
    last_modified: 2026-08-19
  - id: b2-council-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: sprints-sales
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/04_Business_Domains/04_Sales_et_Cognition_MartianManhunter_Illuminati/SPRINTS.md"
    title: SPRINTS 2026-08 — cycle canonique sans veto opposé
    last_modified: 2026-08-02
  - id: rap-john-jones
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-john-jones.md"
    title: RAPPORT vague 2 — aucun packet mésoperpétuel Sales réel
    last_modified: 2026-08-19
okf_version: "0.2"
---

# JohnJones — protocole de validation empirique du veto reformulation-validée

## Pourquoi ce protocole

Le `RAPPORT_dom-john-jones.md` §1 (zones d'ombre) identifie :

> *« Le SPRINT 2026-08 documente la séquence opérationnelle
> (discovery → reformulation → validation → liaison) avec une
> précision remarquable, mais ne documente aucun arbitrage Council
> réel où le veto reformulation-validée s'est opposé à une
> proposition. La conséquence opérationnelle est nette : on ne sait
> pas ce que donne le veto en pratique. »*

Ce protocole ferme ce gap : il pose une **cible chiffrée** (3 cas
observés en 60 jours), un **type de packet mésoperpétuel** Sales
spécifique, et des **critères d'acceptance** vérifiables par un
tiers qui n'est pas le captain.

## La cible chiffrée

**3 cas / 60 jours** — analogue au protocole posé pour Flash
(veto-offre-depersonnalisee) et Superman (veto-prise-parole-publique)
en tour 3. Cette cible est volontaire :

- **Trop bas (1 cas / 60 j)** : le veto n'est pas stressé. La
  doctrine reste théorique.
- **3 cas / 60 j** : la doctrine est confrontée à 3 situations
  distinctes en un cycle 12WY standard. Si le veto ne se déclenche
  jamais, c'est que le squad CaptainAmerica ou un autre capitaine
  bloque en amont.
- **Trop haut (10 cas / 60 j)** : le veto devient un outil
  quotidien, pas un filet de sécurité. Le Council passe son temps à
  arbitrer des vetos au lieu d'arbitrer des cas.

## Le type de packet mésoperpétuel Sales

Quand le veto se déclenche (ou aurait dû se déclencher), un packet
mésoperpétuel Sales doit être consigné, en suivant le gabarit canon
`b2-meso-decision-packet-spec.md` avec 5 champs spécifiques :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B1-B2-MANDATE-YYYY-NN  # ou B2-PEER-YYYY-NN
mode: parallel | handoff | negotiation
impacted_domains:
  - sales  # obligatoire pour Sales
tradeoff: short statement
decision: accepted | blocked | escalate_to_B1
veto_field:
  captain: johnjones
  classe: reformulation-non-validee  # cf. b2-eight-domain-vetoes-catalogue.md
  cas_idx: <1-5>  # index du cas dans la liste canonique 5 cas de déclenchement
  preuve_doctrine: <chemin-fichier>  # ex. CLIENT_VALIDATION_01.md, INTERVIEW_01_RAW.md
  cible_manquante:
    - reformulation_en_mots_client
    - validation_explicite
    - lien_reformulation_offre
proof_expected:
  - B2 gate update (sales_ready_ou_blocked_commitment)
  - B3 proof path (interview_canvas_md_ou_client_validation_md)
next_review: <date+30j minimum>
```

Le champ `veto_field` est **spécifique à Sales** : il pointe la
classe catalogue (reformulation-non-validee), l'index du cas dans
la liste canonique (cf. `johnjones-veto-reformulation-validee.md`
§Quand le veto se déclenche), la preuve doctrinable (le fichier
qui manque ou qui est incomplet), et la liste des cibles manquantes
parmi les 6 critères minimaux (3 reformulation + 3 validation
client, cf. SPRINTS.md Sprint 1).

## Les 5 critères d'acceptance par cas

Chaque cas observé doit remplir 5 critères cumulatifs. Un cas qui
manque un critère n'est pas un cas valide de validation — c'est une
erreur de mesure.

### Critère #1 — Cas observé en cycle réel

Le cas n'est pas projeté depuis la doctrine, il est **observé** dans
un cycle de build actif ou un cycle de vente actif. La trace est un
fichier `INTERVIEW_*.md`, `CLIENT_VALIDATION_*.md`, `LINK_TO_OFFER.md`,
ou `SALES_COMMITMENT.md` daté.

### Critère #2 — Veto opposé ou veto absent documenté

Le veto est **opposé** (le packet mésoperpétuel contient `decision:
blocked` avec motif *« reformulation-non-validee »*), **ou** le veto
est **absent mais documenté** (le packet contient `decision:
accepted` avec une note explicite *« veto non applicable parce que X
»*). Un cas où le veto aurait dû s'opposer mais ne s'est pas opposé
**sans documentation** n'est pas un cas valide.

### Critère #3 — Motif vérifiable par un tiers

Le motif du veto pointe à un fichier précis (`CLIENT_VALIDATION_01.md`
absent, ou `INTERVIEW_01_RAW.md` < 1500 mots, ou `LINK_TO_OFFER.md`
sans phrase d'ouverture Coach OS). Le tiers n'a pas besoin de
connaître le client — il lit le packet et les fichiers pointés.

### Critère #4 — Issue Council explicite

Le packet mésoperpétuel contient un `decision:` explicite parmi
`accepted`, `blocked`, `escalate_to_B1`. Pas de zone grise — un cas
sans décision Council explicite n'est pas un cas arbitrable.

### Critère #5 — Next review daté

Le packet contient un `next_review:` daté dans les 30 jours suivants.
Un cas sans `next_review` est un cas non-ré-évaluable, donc non
apprenable.

## Les 3 indicateurs de couverture

Une fois 3 cas observés, 3 indicateurs mesurent si le protocole a
couvert l'espace des situations :

### Indicateur #1 — Couverture des 5 cas catalogue

**Cible** : sur 3 cas observés, au moins 3 des 5 cas catalogue de
déclenchement ont été exercés (cf.
`johnjones-veto-reformulation-validee.md` §Quand le veto se
déclenche : 1.Proposition orale sans trace, 2.Propale basée sur
brief non reformulé, 3.Reformulation paraphrasant l'offre, 4.Validation
orale uniquement, 5.Lien reformulation-offre manquant).

**Lecture** : si les 3 cas observés tombent tous sur les cas #1 et #2
(un commercial oral + un brief non reformulé), les cas #3-#5 ne sont
**pas validés**. La doctrine reste spéculative sur ces cas.

### Indicateur #2 — Distribution amont-aval

**Cible** : au moins 1 cas observé en amont de la signature
(commercial pousse une propale) et au moins 1 cas observé en aval
(client demande un avenant ou un add-on sans re-reformulation).

**Lecture** : le veto s'applique à toute proposition, pas seulement
à la signature initiale. Si tous les cas observés sont en amont
pré-signature, le veto n'a pas été testé en cycle post-signature.

### Indicateur #3 — Vitesse d'observation

**Cible** : 3 cas observés en 60 jours, soit 1 cas tous les 20 jours
en moyenne.

**Lecture** : une vitesse < 1 cas / 30 jours signale que le veto ne
se déclenche pas assez souvent pour être stressé. Une vitesse > 1 cas
/ 10 jours signale que le veto devient un outil quotidien, pas un
filet de sécurité.

## Les 3 conditions de mise à jour de la doctrine

Après 3 cas observés, la doctrine est mise à jour dans l'une des 3
conditions :

### Condition #1 — Doctrine confirmée

Les 3 cas observés correspondent exactement aux 5 cas catalogue
projetés. La doctrine tient. **Résultat** : aucun amendement.

### Condition #2 — Doctrine amendée

Au moins 1 cas observé ne correspond à aucun des 5 cas catalogue,
ou un cas catalogue ne s'est jamais présenté en 60 jours. **Résultat**
: amendement de la liste des 5 cas (ajout ou retrait), procédure
**unanimité + B1** (cf. `b2-veto-amplification-cycle.md` §« L'amplification
n'est pas la réécriture »).

### Condition #3 — Doctrine invalidée

Les 3 cas observés contredisent frontalement la doctrine (par
exemple, le veto bloque une proposition avec reformulation valide,
ou ne bloque pas une proposition sans reformulation). **Résultat** :
escalade B1 pour réécriture de la classe catalogue.

## Anti-pièges

- **Projeter un cas au lieu de l'observer.** La doctrine vit dans
  `johnjones-veto-reformulation-validee.md` avec 5 cas projetés.
  Ces cas ne sont **pas** des cas de validation. La validation
  exige des cas **observés** en cycle réel.
- **Confondre cas de déclenchement et cas d'abus.** Les 5 cas
  catalogue sont des cas **légitimes** de veto. Les 5 cas d'abus
  (cf. `johnjones-veto-reformulation-validee.md` §Quand le veto
  serait abusif) sont des cas où le veto est **invalide**. Le
  protocole ne teste que les cas légitimes — les cas d'abus sont
  testés par un protocole miroir.
- **Cible 3 cas / 60 jours transformée en 1 cas / 6 mois.** Si la
  cible est trop espacée, la doctrine devient un voeu. Garder la
  cadence.
- **Packet mésoperpétuel sans `next_review`.** C'est l'anti-pièce
  canonique de `b2-meso-decision-packet-spec.md` §Anti-pièges —
  un packet sans `next_review` est un voeu pieux.
- **Confondre validation empirique et amplification.** Valider
  empiriquement, c'est **confirmer** la doctrine canonique (5 cas
  catalogue). Amender, c'est **étendre** la doctrine (ajouter une
  classe). Le protocole de validation ne fait que confirmer ou
  invalider — il n'étend pas.

## Liens

- [[johnjones-veto-reformulation-validee]] — les 5 cas catalogue à valider
- [[b2-eight-domain-vetoes-catalogue]] — propriétés canoniques du veto
- [[b2-meso-decision-packet-spec]] — format du packet mésoperpétuel
- [[b2-council-arbitrage-rule]] — qui tient le Council, qui arbitre
- [[johnjones-gates-et-pair-checks]] — gates SALES_READY /
  NEEDS_QUALIFICATION / BLOCKED_COMMITMENT
- [[johnjones-jtbd-emit-receive]] — JTBD émis en cas de veto
- [[RAPPORT_dom-john-jones]] — §1 (zones d'ombre) que ce protocole ferme

## Note de confiance

**Confirmé par machine, à moitié.** Le format packet mésoperpétuel
est tiré verbatim de `b2-meso-decision-packet-spec.md`. La cible 3
cas / 60 jours est **projetée par analogie** avec les protocoles
Flash (veto-offre-depersonnalisee) et Superman (veto-prise-parole-publique)
en tour 3 — pas citée comme un invariant canonique pour Sales. Les
5 critères d'acceptance par cas sont **reconstruits** depuis les
trois propriétés canoniques du veto (catégoriel, vérifiable,
non-négociable — cf. `b2-eight-domain-vetoes-catalogue.md` §Les trois
propriétés) + 2 critères opérationnels (cas observé, next_review).
Les 3 indicateurs de couverture sont **projetés** depuis la
pratique décrite dans `SPRINTS.md` (4 sprints, 6 critères minimaux
reformulation + validation).

À vérifier en cycle réel : (1) la cible 3 cas / 60 jours est-elle
tenable sans saturer le Council ? (2) Les 5 critères d'acceptance
suffisent-ils à filtrer les cas non-valides ? (3) La distinction
validation empirique vs amplification tient-elle en pratique ?