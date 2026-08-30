---
type: Concept
title: Doctrine remonte volume amont — protocole d'observation à 0 cas
description: La doctrine Batman « remonte à Summers des faits, pas des décisions » (triplets 56/57) est étendue en tour 3 au volume (trigger charge_derivee). 0 cas observé en cycle. Le présent protocole formalise l'observation : infrastructure minimum (compteur, journal, seuil), conditions de declenchement, periodicité de revue, asymétrie trigger vs seuil fixe.
tags: [b2, ops, batman, doctrine, remonte, volume, amont, protocole-observation, 0-cas]
generated: { by: minimax-m3, at: 2026-08-19T06:10:00Z }
verified:
  - { by: process:lecture-canon-b2-tour-4, at: 2026-08-19T06:10:00Z }
sources:
  - id: batman-doctrine-remonte-fait
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-doctrine-remonte-fait-non-decision.md"
    title: Doctrine remonte-fait triplets 56/57
    last_modified: 2026-08-19
  - id: batman-couplage-superman
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-superman-growth-volume-charge.md"
    title: Couplage Ops×Superman-Growth volume charge derivee
    last_modified: 2026-08-19
  - id: batman-couplage-johnjones
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-john-jones-sales-taux-signature.md"
    title: Couplage Ops×JohnJones-Sales debit signature
    last_modified: 2026-08-19
  - id: triplets-v3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: Triplets 56/57 — Batman remonte à Summers des faits
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Doctrine remonte volume amont — protocole d'observation à 0 cas

## Le trou que Batman ferme

Tour 3 pose le **trigger `charge_derivee`** (cf.
`batman-couplage-superman-growth-volume-charge.md` §« trigger
charge_derivee ») comme extension de la doctrine remonte-fait
(triplets 56/57). Mais :

- **0 cas observé** en cycle de Batman en tour 3 (cf. ETAT_DOMAINES.md
  Batman tour 3, ligne d'ouverture).
- **Le trigger est inobservé** — Batman ne sait pas **comment**
  observer un volume amont qui ne s'est pas encore manifesté.
- **0 infrastructure minimum** n'est posée (compteur, journal,
  metric).

Le présent protocole formalise l'**infrastructure d'observation**
qui permet à Batman de détecter un volume amont *avant* qu'il ne
sature Ops. Le protocole ne **declenche** pas le trigger ; il
**permet** au trigger de se declencher.

## Les 4 asymétries de la doctrine remonte volume amont

### 1. Asymétrie 1 — Seuil fixe vs trigger adaptatif

La doctrine canonique triplet 56/57 parle de **faits** (procedure-sans-condition-arret).
Un fait est binaire : la procedure a ou n'a pas de condition d'arret.
Le volume est **continu** : la charge derivee peut être 12%, 28%, 30%,
33%, 60%. Le binaire ne suffit pas.

Batman propose un **trigger adaptatif** : la detección du volume
amont depend du **profil historique** d'Ops, pas d'un seuil fixe.
Un Ops à 80% de capacity ne declenche pas à 30% de charge dérivée ;
un Ops à 110% de capacity declenche à 25%.

C'est une **asymétrie avec la doctrine remonte-fait** : la
remonte-fait est binaire (oui/non), la remonte-volume est
contextuelle (le seuil depend du profil).

### 2. Asymétrie 2 — Détection continue vs événementielle

La remonte-fait est **événementielle** : le procedure-sans-condition-arret
est detecté à la conception (Phase 1), pas en cours. La remonte-volume
est **continue** : la charge derivee évolue en flux, et Batman doit
l'observer en flux.

C'est une **asymétrie de métrique** : événementielle → log
ponctuel, continu → métrique fenêtrée.

### 3. Asymétrie 3 — Batman seul vs Batman + B2 captain amont

La remonte-fait est une **initiative Batman** (Batman détecte et
remonte). La remonte-volume est une **remontée conjointe** Batman +
B2 captain amont (Superman pour Growth, JohnJones pour Sales).
Batman ne peut pas observer seul la charge dérivée — c'est l'amont
qui la genere.

C'est une **asymétrie de légitimité** : Batman A sur la conséquence
(Ops), Batman C sur la cause (l'amont). La détection conjointe
est legitimée par le RACI par rang (Batman A = aval, Superman/JohnJones
C = amont).

### 4. Asymétrie 4 — Log à Batman seul vs journal Council

La remonte-fait est consignée dans le **journal Batman**
(triplets 56/57). La remonte-volume est consignée dans le **journal
Council** (B2_DC_DIRECTION_COUNCIL_DECISIONS.md). Le volume est
cross-domaine ; il regarde le Council, pas Batman seul.

C'est une **asymétrie de destination** : la trace d'un fait est
locale, la trace d'un volume est partagée.

## L'infrastructure minimum

### Compteur 1 — Charge Ops totale

**Métrique** : `charge_ops_totale = (charge_livraison + charge_support
+ charge_runbook) / capacity_ops_planifiee`.

**Fréquence** : sprint-level (1 mesure / sprint).

**Cible** : maintenir la mesure pendant 6 sprints avant de figer
le baseline.

**Stockage** : `outillage/charge_ops_totale.md`, append-only.

### Compteur 2 — Charge dérivée amont

**Métrique** : `charge_derivee = (charge_livraison_onboarding +
charge_support_lead) / capacity_ops_planifiee`.

**Fréquence** : sprint-level.

**Cible** : disaggregation par captain amont (Superman, JohnJones,
Flash).

**Stockage** : `outillage/charge_derivee_amont.md`, append-only.

### Compteur 3 — Seuil adaptatif

**Métrique** : `seuil_trigger = f(charge_ops_totale)`.

**Fréquence** : sprint-level.

**Formule projetée** : `seuil_trigger = 0.3 - (charge_ops_totale -
1.0) × 0.5` (à calibre). Plus Ops est saturé, plus le seuil est
bas. Si Ops est à 120% de capacity, le seuil tombe à 25%.

**Cible** : la formule est validée sur 3 cycles (cf. protocole
validation empirique).

**Stockage** : `outillage/seuil_trigger.md`.

### Compteur 4 — Compteur de triggers

**Métrique** : `nb_triggers_declenchés = count(events where
charge_derivee ≥ seuil_trigger)`.

**Fréquence** : evenementielle.

**Cible** : 0 cas observé au 2026-08-19. La cible est d'avoir
**au moins 1 cas** d'ici 2026-10-19 (60 jours).

**Stockage** : `outillage/journal_triggers.md`.

## Les conditions de declenchement

Le trigger `charge_derivee` se declenche quand :

1. **Condition C1** : `charge_derivee ≥ seuil_trigger` au compteur sprint.
2. **Condition C2** : la tendance est **significative** (sur au moins
   2 sprints consecutifs, pas un one-shot).
3. **Condition C3** : Batman a **confirmation** par le captain amont
   (Superman ou JohnJones) que le volume est soutenable ou non.

**Issue si 3 conditions tenues** : packet mesoperpetuel
`B2-MESO-DECISION-2026-NN` avec `mode: negotiation`,
`impacted_domains: [ops, growth]` (ou sales), `decision: accepted`
avec gel conjointe ou escalation B1.

**Issue si condition C3 manque** : Batman ne peut pas declencher
seul. Le trigger est suspendu tant que la confirmation amont manque.

## La periodicité de revue

**Revue sprint** : vérification des 4 compteurs. Pas de declenchement
sans franchir les 3 conditions.

**Revue mensuelle** : vérification de la formule du seuil adaptatif.
Ajustement si necessaire.

**Revue cycle 12WY** : soumission packet mesoperpetuel même si 0 cas
observé, pour traçabilité. La remontée « 0 cas observé » est elle-même
un fait.

## Le cas 0 cas observé

À la date 2026-08-19, **0 cas observé**. Conséquences :

1. **Pas de declenchement** possible. Le trigger est inobserve.
2. **Pas de calibration** du seuil adaptatif. La formule projetée
   reste projetée.
3. **Pas de confirmation** par captain amont (C3 manque systematiquement).
4. **Pas de cycle 12WY** passé pour observer. Le premier cycle 12WY
   de mesure commence avec le sprint 2026-09.

L'observation « 0 cas » est en soi un **fait** — Batman remonte
au Council que la doctrine est **posée mais inactive**. Le Council
peut demander acceleration ou prolongation.

## L'asymétrie trigger vs seuil fixe

La doctrine canonique pose des seuils fixes (par exemple `charge_recurrente`
≥ 30% pour Wonder Woman). Batman propose un **trigger adaptatif**
parce que la capacity Ops peut varier. Trois cas illustrent :

- **Cas X** : Capacity Ops 80%, charge dérivée 28%. Seuil fixe
  30% → pas de trigger. Seuil adaptatif (0.3 - (0.8 - 1.0) × 0.5
  = 0.4) → pas de trigger non plus. Alignement.
- **Cas Y** : Capacity Ops 110%, charge dérivée 28%. Seuil fixe
  30% → pas de trigger. Seuil adaptatif (0.3 - (1.1 - 1.0) × 0.5
  = 0.25) → trigger declenché. Detection.
- **Cas Z** : Capacity Ops 50%, charge dérivée 35%. Seuil fixe
  30% → trigger. Seuil adaptatif (0.3 - (0.5 - 1.0) × 0.5 = 0.55)
  → pas de trigger. Pas de faux positif.

Le seuil adaptatif est plus **fin** que le seuil fixe. Il évite
les faux positifs (Ops空闲) et les faux négatifs (Ops saturé).

## Pourquoi pas un seuil fixe

Un seuil fixe (par exemple 30% inconditionnel) est plus simple
mais provoque deux erreurs :

- **Faux positif** : Ops空闲, charge dérivée 30%, gel déclenché inutilement.
- **Faux négatif** : Ops sature, charge dérivée 28%, pas de gel —
  c'est l'inverse de la detection escomptée.

Le seuil adaptatif est plus précis. C'est la **métrique fenêtrée**
qui permet la detection.

## Anti-pièges

- **Confondre trigger et seuil.** Le trigger est l'**événement**,
  le seuil est la **valeur**. Le protocole pose les deux.
- **Calibrer le seuil sans 6 sprints.** Le baseline est 6 sprints.
  Un seuil calibre sur 1 sprint est un seuil au hasard.
- **Déclencher sans C3.** Sans confirmation amont, le trigger est
  unilateral. Batman A sur la conséquence, mais C sur la cause.
- **Considérer 0 cas comme défaut du protocole.** 0 cas peut être
  le signe que la doctrine fonctionne (Ops non saturé) ou qu'elle
  est inappliquée (Batman n'observe pas). Le protocole exige de
  distinguer les deux.

## Liens

- [[batman-doctrine-remonte-fait-non-decision]] — la doctrine source
- [[batman-couplage-superman-growth-volume-charge]] — le trigger charge_derivee
- [[batman-couplage-john-jones-sales-taux-signature]] — le trigger debit_signature
- [[b2-veto-empirical-validation-protocol]] — la cible 3 cas/60j
- [[b2-council-arbitrage-rule]] — le journal Council

## Note de confiance

**Reconstruit, à moitié étayé.** La doctrine source (triplets 56/57)
est verbatim. L'extension au volume (trigger charge_derivee) est
posée en tour 3 mais **non Council-ready**. Le protocole d'observation
est **projeté** à partir de la pratique RACI cycle sprint hebdo
(triplet 10) et des concepts couplage Batman tour 3. La formule
seuil adaptatif est **calquée** sur la logique « seuil ajuste à la
capacity ». Les 4 asymétries sont **des observations Batman**, pas
unanimement étayées. La cible 1 cas observé d'ici 2026-10-19 est
une preference Batman, pas un canon.
