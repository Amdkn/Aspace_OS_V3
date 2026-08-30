---
type: Concept
title: Validation empirique cycle de vie Ops 5 phases — protocole 3 cas/60j
description: Batman pose en tour 3 le cycle de vie procedure Ops en 5 phases (conception/pilote/production/revue/arret). 0 cas reel observé en Coach OS. Le présent protocole formalise la validation empirique : cible 3 cas/60j, 5 critères d'acceptance chiffrés par cas, 3 indicateurs couverture/distribution/vitesse, 3 conditions de mise à jour (confirmé/amendé/invalidé).
tags: [b2, ops, batman, cycle-de-vie, validation, empirique, 3-cas-60j, protocole]
generated: { by: minimax-m3, at: 2026-08-19T06:07:00Z }
verified:
  - { by: process:lecture-canon-b2-tour-4, at: 2026-08-19T06:07:00Z }
sources:
  - id: batman-cycle-5-phases
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-cycle-vie-procedure-ops-cinq-phases.md"
    title: Cycle de vie procedure Ops en 5 phases
    last_modified: 2026-08-19
  - id: b2-veto-empirical
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-empirical-validation-protocol.md"
    title: Veto empirical validation protocol — cible 3 cas/60j
    last_modified: 2026-08-19
  - id: flash-empirical
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-veto-empirical-validation-protocol.md"
    title: Flash veto empirical validation protocol
    last_modified: 2026-08-19
  - id: superman-empirical
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-empirical-validation-protocol.md"
    title: Green Lantern empirical validation protocol
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Validation empirique cycle de vie Ops 5 phases — protocole 3 cas/60j

## Le trou que Batman ferme

Tour 3 pose `batman-cycle-vie-procedure-ops-cinq-phases.md` avec 5
phases (conception/pilote/production/revue/arret), 3 indicateurs
dormance, alignement 12WY. Mais **0 cas réel observé** en Coach OS
au 2026-08-19. Le concept est une projection, pas une doctrine
validée.

Le présent protocole formalise la **validation empirique** de la
doctrine, alignée sur le pattern canonique `b2-veto-empirical-validation-protocol.md`
utilisé par Flash, Superman, et Green Lantern.

## La cible 3 cas/60j

**Cible** : 3 cas observés en 60 jours de cycle de vie procedure Ops
complet (au moins 1 procedure traversant les 5 phases).

**Cible actuelle** : 0/60j au 2026-08-19.

**Cycle de mesure** : 60 jours glissants, à compter du premier sprint
où une procedure Ops entre en Phase 1 (conception). Un cas est
**complet** quand la procedure a atteint Phase 5 (arret) ou a été
maintenue ACTIVE au-dela de 6 sprints (qui est l'horizon de mesure).

**Pourquoi 3 cas** : 3 cas est le minimum pour observer une
distribution (cf. `b2-veto-empirical-validation-protocol.md` §« 3
indicateurs »). Un seul cas est anecdotique ; deux cas est
coincidence ; trois cas est tendance.

## Les 5 critères d'acceptance par cas

Pour chaque cas observé, la procedure Ops doit fournir 5 critères
chiffrés :

1. **Phase 1 — durée de conception** : nombre de jours entre
   gate d'entrée (`DORMANT-PROC`) et sortie (`PILOT-PROC`).
   Cible : ≤ 14 jours.
2. **Phase 2 — durée de pilote** : nombre de sprints entre
   `PILOT-PROC` et `ACTIVE-PROC`. Cible : 1 à 3 sprints.
3. **Phase 3 — durée de production** : nombre de sprints en
   `ACTIVE-PROC`. Cible : ≥ 3 sprints (pour observer 1 cycle de
   revue).
4. **Phase 4 — durée de revue** : nombre de jours entre
   `ACTIVE-PROC` et décision de Phase 5 (arret) ou de maintien.
   Cible : ≤ 7 jours.
5. **Phase 5 — qualité de l'arret** : preuve d'arret (runbook
   archivé, owner releve, dépendance levée) ou preuve de maintien
   (revue periodique). Cible : 100% des cas.

**Methode de mesure** : `journal_cycle_vie.md` dans le dossier
procedure, append-only, chaque cas avec timestamp.

**Cible globale** : 80% des cas atteignent les 5 critères. En dessous
de 80%, la doctrine est amendée. Au-dessus de 90%, elle est confirmée.

## Les 3 indicateurs de robustesse

Trois indicateurs calculés sur l'ensemble des 3 cas observés :

### Indicateur 1 — Couverture

**Formule** : `couverture = nb_phases_atteintes / (nb_cas × 5)`.

**Cible** : ≥ 80% des phases couvertes. En dessous, la doctrine est
lacunaire.

**Sens** : la doctrine couvre **toutes les phases** ou seulement
certaines ? Si la Phase 4 (revue) est systèmatiquement sautée, la
doctrine couvre 4 phases sur 5.

### Indicateur 2 — Distribution

**Formule** : distribution des cas par phase d'entrée. Un cas entre
en Phase 1, un autre en Phase 3 (procedure héritée), un troisième en
Phase 2 (procedure importée d'un autre domain).

**Cible** : distribution variée (≥ 2 phases d'entrée differentes sur
3 cas). Une distribution uniformément en Phase 1 indique un biais
de création ; une distribution uniformément en Phase 3 indique un
biais d'import.

**Sens** : la doctrine est-elle assez générale pour couvrir des
procedures d'origines differentes ?

### Indicateur 3 — Vitesse

**Formule** : `vitesse = total_jours_parcourus / nb_phases_parcourues`.

**Cible** : ≤ 30 jours par phase en moyenne. Au-dessus, la doctrine
ralentit l'exécution.

**Sens** : la doctrine est-elle compatible avec la cadence 12WY ?

## Les 3 conditions de mise à jour

À la fin du cycle 60j, **3 issues** sont possibles :

### Issue A — Confirmé

**Conditions** : couverture ≥ 80% et distribution ≥ 2 phases
d'entrée et vitesse ≤ 30 jours par phase.

**Action** : la doctrine est marquée **Council-ready**. Le packet
meso `B2-MESO-DECISION-2026-NN` est soumis avec `decision: accepted`.

### Issue B — Amendé

**Conditions** : couverture 60-80% ou distribution 1 phase d'entrée
ou vitesse 30-60 jours par phase.

**Action** : la doctrine est marquée **Council-ready sous reserve**.
Le packet est soumis avec `decision: accepted` + une liste d'amendements
(ajout de phase, ajustement de cible, etc.).

### Issue C — Invalidé

**Conditions** : couverture < 60% ou vitesse > 60 jours par phase
ou aucun cas observé après 60j.

**Action** : la doctrine est **révoquée**. Le packet est soumis avec
`decision: blocked` et la doctrine est retirée des concepts Council-ready.

## L'articulation avec les autres protocoles de validation

Batman n'est pas le seul domain à appliquer la cible 3 cas/60j :

- **Veto Flash** : `flash-veto-empirical-validation-protocol.md`
  pose le même protocole pour le veto Flash.
- **Veto Superman** : `superman-veto-empirical-validation-protocol.md`
  (cf. ETAT_DOMAINES Superman tour 3) pose le même pour Superman.
- **Veto Green Lantern** : `green-lantern-empirical-validation-protocol.md`
  pose le même pour People.

Le pattern canonique est **3 cas/60j, 5 critères d'acceptance, 3
indicateurs, 3 conditions de mise à jour**. Batman aligne son
protocole sur ce pattern.

**Conséquence** : les 8 domaines B2 peuvent être valides en parallele
sur des cycles de 60j. Si la wheel 8-domain reste à 0 packet
mesoperpetuel après 3 vagues (cf. ETAT_DOMAINES.md), c'est que les
cycles 60j n'ont pas démarré nulle part — pas un défaut de Batman.

## L'asymétrie cycle de vie Batman vs cycle de vie Sales

`john-jones-cycle-de-vie-reformulation-5-phases` pose un cycle de
vie reformulation 5 phases (Decouverte/Reformulation/Validation/Liaison/Activation-Ops).
Batman×JohnJones partagent la structure 5 phases, mais **les phases
ne sont pas les mêmes** :

- **Sales 5 phases** : Decouverte → Reformulation → Validation →
  Liaison → Activation-Ops.
- **Ops 5 phases** : Conception → Pilote → Production → Revue →
  Arret.

**Asymétrie** : le cycle Sales se termine par **Activation-Ops**
(transfert à Ops), pas par un Arret. Le cycle Ops **reçoit** la
sortie Sales via Activation-Ops et la fait vivre jusqu'à Arret.

**Conséquence** : la Phase 1 Ops (Conception) **précède** la Phase 5
Sales (Activation-Ops) si la procedure est concue pour absorber un
deal. Sinon, la Phase 1 Ops **suit** l'Activation-Ops — Ops adapte
une procedure existante au cas client.

Ce double régime est asymétrique ; il faut un **trigger** explicite
pour basculer. Le trigger est `ops_handoff_accepted` (cf. concept
JohnJones cycle reformulation).

## Les 3 questions ouvertes post-validation

Quelle que soit l'issue (A, B, C), 3 questions restent ouvertes :

1. **Distribution des phases d'entrée.** Le protocole de validation
   observe, mais n'explique pas pourquoi la distribution est ce
   qu'elle est. La cause de la distribution est un objet d'analyse
   post-60j.
2. **Effet du trigger `ops_handoff_accepted`.** Le protocole ne
   distingue pas les procedures concues avant vs après le handoff.
   Une analyse post-60j doit le faire.
3. **Migration vers Phase 5.** Le protocole observe les cas, mais
   ne prescrit pas la cadence de revue. Phase 4 (revue) doit être
   tous les combien ? 3 sprints ? 6 sprints ? Cycle 12WY ?

## Anti-pièges

- **Valider sans observateur.** Le protocole exige un temoin B2
  externe (cf. `b2-veto-empirical-validation-protocol.md` §« 5
  critères d'acceptance cumulatifs »). Un cas sans temoin est un
  récit, pas un cas.
- **Confondre cas observe et cas projeté.** Un cas projeté est un
  plausibles. Le protocole exige des cas observes, pas projetés.
- **Adapter le seuil 80% à la volée.** Le seuil est Council-ready
  ou ne l'est pas. Modifier en cours de protocole casse la
  comparaison.
- **3 cas simultanés.** Le protocole exige 3 cas en 60j, pas 3 cas
  en parallèle. La distribution temporelle est un indicateur de
  la robustesse de la doctrine — projection concentré sur 1 sprint
  = 1 cas, pas 3.

## Liens

- [[batman-cycle-vie-procedure-ops-cinq-phases]] — la doctrine à valider
- [[b2-veto-empirical-validation-protocol]] — le pattern canonique
- [[john-jones-cycle-de-vie-reformulation-5-phases]] — l'asymétrie cycle Sales
- [[b2-council-arbitrage-rule]] — qui tient le Council

## Note de confiance

**Reconstruit, à moitié étayé.** Les 5 critères d'acceptance, 3
indicateurs, 3 conditions de mise à jour, et le pattern 3 cas/60j
sont **calqués** sur `b2-veto-empirical-validation-protocol.md`. Les
cibles chiffrées (14j, 1-3 sprints, ≥ 3 sprints, 7j, 80%) sont
**projetées** depuis la pratique RACI cycle sprint hebdo (triplet 10) et
l'alignement 12WY. L'asymétrie cycle Sales vs cycle Ops est **une
observation Batman**, pas un canon — le cross-link avec JohnJones
n'est pas posé ailleurs. Les 3 questions ouvertes post-validation
sont des extrapolations.
