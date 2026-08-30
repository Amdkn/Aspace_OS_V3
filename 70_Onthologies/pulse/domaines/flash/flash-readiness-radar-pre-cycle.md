---
type: Concept
title: Radar de readiness Flash pré-cycle — 4 questions de doctrine + 4 questions de run, distingue doctrine vs run
description: Le tour 1 a posé 7 concepts sur Flash, mais la distinction doctrine/run n'est pas outillée. Le radar pré-cycle pose 8 questions (4 doctrine + 4 run) que Flash doit traiter avant chaque cycle de build actif. Chaque question est binaire (vert/rouge) avec critère chiffré, et le radar agrège les 8 en un score de readiness Flash. Application : transformer la doctrine reconstruite en pratique opérationnelle outillée.
tags: [flash, product, readiness, radar, doctrine, run, cycle, outillage, build-actif]
generated: { by: minimax-m3, at: 2026-08-19T05:30:00Z }
verified:
  - { by: process:lecture-corpus-flash-tour-2, at: 2026-08-19T05:30:00Z }
sources:
  - id: flash-doctrine-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-doctrine-valeur-artefact.md"
    title: Flash — doctrine valeur-d'artefact
    last_modified: 2026-08-19
  - id: flash-veto-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-veto-offre-depersonnalisee.md"
    title: Flash — veto offre dépersonnalisée
    last_modified: 2026-08-19
  - id: flash-red-flag-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-red-flag-1-trigger.md"
    title: Flash — red flag #1
    last_modified: 2026-08-19
  - id: flash-triple-squad
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-triple-squad-launch-canon-protocol.md"
    title: Flash — triple-squad launch protocol
    last_modified: 2026-08-19
  - id: b2-council-cadence
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-cadence-and-chair.md"
    title: B2 Council cadence — le seuil déclencheur hebdomadaire
    last_modified: 2026-08-19
  - id: harmonization-exploitable
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — 9 critères + 5 red flags
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Radar de readiness Flash pré-cycle

## Pourquoi un radar — la doctrine reconstruite n'est pas outillée

Le tour 1 a posé 7 concepts sur Flash (périmètre, veto, JTBD,
pair-checks, red flag, doctrine, numérotation). Mais la doctrine est
**reconstruite** — pas étayée par un cas pratique (cf.
`flash-veto-empirical-validation-protocol.md` §« Le constat — 0 cas
réel observé »). Sans outillage, la doctrine reste une **projection
théorique** que chaque cycle de build actif doit **réapprendre**.

Le radar pré-cycle comble ce trou : **8 questions** que Flash traite
avant chaque cycle de build actif, distinguant la **doctrine** (4
questions, qualitative) du **run** (4 questions, opérationnelle).
Chaque question est **binaire** (vert/rouge) avec seuil chiffré.

## Le format du radar

Le radar est un outil **pré-cycle** (avant l'ouverture d'un cycle de
build actif). Il pose 8 questions en deux blocs :

### Bloc A — Doctrine (4 questions qualitatives)

Les 4 questions de doctrine testent si la doctrine Flash est **tenue**
dans la posture courante. C'est une vérification **interne** — Flash
s'auto-évalue sur sa propre doctrine.

#### Q1 — La valeur d'artefact est-elle l'unité de parole courante ?

**Question** : *« Dans les 5 derniers arbitrages où j est ai parlé, ai-
je parlé en valeur d'artefact (indépendance de l'opérateur) ou en autre
chose (état, promesse, retour) ? »*

**Critère vert** : ≥ 4/5 arbitrages en valeur d'artefact.
**Critère rouge** : < 4/5 arbitrages en valeur d'artefact.

**Pourquoi** : la doctrine valeur d'artefact est l'unité native de
Flash (cf. `flash-doctrine-valeur-artefact.md` §« Le contraste des 4
docteurs B2 »). Si Flash parle en *état* ou en *promesse*, il brouille
la matrice — Batman et Superman ont des unités distinctes.

#### Q2 — Le veto offre dépersonnalisée est-il opposable ?

**Question** : *« Sur les 5 dernières offres que j'ai examinées, ai-je
identifié un cas où le veto était légitime et opposé ? »*

**Critère vert** : ≥ 1 veto opposé (même si levé par amendement).
**Critère rouge** : 0 veto opposé.

**Pourquoi** : le veto est l'expression directe de la doctrine (cf.
`flash-doctrine-valeur-artefact.md` §« L'unité de parole comme
signature de veto »). Sans veto opposé, la doctrine n'est pas **mise
en pratique**.

#### Q3 — Le mécanisme de reprise est-il documenté pour chaque offre active ?

**Question** : *« Pour chaque offre en cours de commercialisation, le
mécanisme de reprise (partner back-up, runbook, squad de relève) est-
il écrit et vérifiable ? »*

**Critère vert** : 100% des offres actives ont un mécanisme documenté.
**Critère rouge** : ≥ 1 offre active sans mécanisme documenté.

**Pourquoi** : c'est l'amplification candidate « mécanisme de reprise
documenté » (cf. `flash-amplification-mecanisme-reprise.md`). Tant que
l'amplification n'est pas adoptée, ce n'est pas un veto — mais c'est un
**signe de maturité** doctrinal.

#### Q4 — Les pair-checks #3, #4, #6, #8 sont-ils synchronisés ?

**Question** : *« Les 4 pair-checks impliquant Product sont-ils au vert
sur les pair-checks courants, ou l'un d'eux est-il en conflit ? »*

**Critère vert** : 4/4 pair-checks au vert.
**Critère rouge** : ≥ 1 pair-check en conflit.

**Pourquoi** : les 4 pair-checks sont les transitions canoniques de
Flash (cf. `flash-pair-checks-dependencies.md`). Un pair-check en
conflit signale un **risque systémique** sur le cycle à venir.

### Bloc B — Run (4 questions opérationnelles)

Les 4 questions de run testent si l'opérationnel courant tient. C'est
une vérification **externe** — l'opérationnel Avengers et les squads
amont/aval.

#### Q5 — La chaîne Avengers → Fantastic4 → Kang Dynasty est-elle opérationnelle ?

**Question** : *« Les 3 squads Marvel alignées sont-elles prêtes à
exécuter le cycle (Avengers build, Fantastic4 runbook, Kang Dynasty
deploy) ? »*

**Critère vert** : 3/3 squads prêtes (effectif complet, charges
tenables).
**Critère rouge** : ≥ 1 squad en manque d'effectif ou de charge.

**Pourquoi** : la chaîne triple-squad est le mode launch canonique
(cf. `flash-triple-squad-launch-canon-protocol.md` §« Mode handoff
sériel Council »). Sans les 3 squads prêtes, le launch est suspendu.

#### Q6 — Le goulot Fantastic4 est-il sous contrôle ?

**Question** : *« Le ratio Avengers:Fantastic4 est-il tenable pour le
cycle (≤ 1.75), et Batman a-t-il un plan pour le runbook progressif
? »*

**Critère vert** : ratio ≤ 1.75 ET plan Batman confirmé.
**Critère rouge** : ratio > 1.75 OU plan Batman absent.

**Pourquoi** : le goulot 7:4 Avengers:Fantastic4 est **structurel**
(cf. `flash-coach-os-numerotation-alignment.md` §« Le goulot
d'étranglement Fantastic4 »). Sans plan, le red flag #1 se déclenche
systématiquement en fin de cycle.

#### Q7 — Le budget alloué par Wonder Woman est-il tenable ?

**Question** : *« Le budget Finance → Product couvre-t-il le scope
Avengers du cycle (sans dépassement > 10%) ? »*

**Critère vert** : budget couvre scope ET marge ≥ 60%.
**Critère rouge** : dépassement > 10% OU marge < 60%.

**Pourquoi** : Wonder Woman oppose son veto-dépense récurrente (triplet
26) sur les dépassements non chiffrés. Sans marge tenable, Wonder
Woman bloque le cycle.

#### Q8 — Les frontières Legal (Aquaman) sont-elles appliquées ?

**Question** : *« Les frontières IP/privacy/terms sont-elles déclarées
par Aquaman ET appliquées dans l'UI Avengers ? »*

**Critère vert** : frontières déclarées ET appliquées.
**Critère rouge** : frontières non déclarées OU non appliquées.

**Pourquoi** : Aquaman Legal tient le veto engagement-sans-périmètre
(triplet 32). Sans frontières applées, Aquaman bloque le launch.

## Le score de readiness Flash

Le radar agrège les 8 questions en un score :

```
score = (Q1.vert + Q2.vert + Q3.vert + Q4.vert + Q5.vert + Q6.vert + Q7.vert + Q8.vert) / 8
```

Quatre niveaux de readiness :

| Score | Niveau | Action Flash |
|---|---|---|
| **8/8** | **Green** | Cycle ouvert en mode parallel, launch autorisé sous condition de red flag #1 verts |
| **6-7/8** | **Yellow** | Cycle ouvert en mode handoff (chaîne triple-squad), Flash consigne les jaunes dans le packet mésoperpétuel |
| **4-5/8** | **Orange** | Cycle ouvert en mode negotiation, Flash convoque le B2 Council pour arbitrage des oranges |
| **< 4/8** | **Red** | Cycle reporté, Flash escalade B1, la doctrine n'est pas tenable opérationnellement |

Le score est **calculé au début du cycle** (avant l'ouverture du
sprint 1 du cycle) et **ré-évalué à mi-cycle** (fin du sprint 2). Un
cycle qui passe de Green à Orange à mi-cycle déclenche une
**re-conisation B2 Council** sans escalade B1 — c'est un signal
interne.

## Application — le radar en 5 étapes

### Étape 1 — Initialisation (début de cycle, J-3)

Flash ouvre une `readiness_session` dans son SPRINT.md avec les 8
questions. Chaque question est traitée **avant** l'ouverture du sprint
1.

### Étape 2 — Diagnostic (J-3 à J-1)

Flash parcourt les 8 questions. Pour chaque question rouge, Flash
documente le **motif** dans le SPRINT.md (1 phrase par rouge). Pas de
plan d'action — juste le constat.

### Étape 3 — Décision (J-1)

Sur la base du score, Flash décide du niveau (Green / Yellow / Orange /
Red) et consigne dans le SPRINT.md :
- **Green** : `readiness_score: 8/8, mode: parallel, launch: pending_red_flag_1`.
- **Yellow** : `readiness_score: N/8, mode: handoff, packet_meso: B2-MESO-DECISION-YYYY-NN`.
- **Orange** : `readiness_score: N/8, mode: negotiation, b2_council_session: <date>`.
- **Red** : `readiness_score: N/8, mode: blocked, escalate_b1: true`.

### Étape 4 — Exécution (cycle)

Le cycle s'exécute selon le mode décidé. Flash ré-évalue le radar à
mi-cycle (fin sprint 2).

### Étape 5 — Clôture (fin de cycle)

Flash consigne le **score final** (à la clôture) et le compare au
**score initial**. Une régression (Green → Yellow ou Yellow → Orange)
est consignée dans le journal Council.

## Trois cas d'application

### Cas 1 — Radar Green (8/8) — cycle de référence

Toutes les questions sont vertes. Le cycle s'ouvre en mode parallel,
et le launch s'exécute sous condition de red flag #1 verts à la
clôture du triple-squad (cf.
`flash-triple-squad-launch-canon-protocol.md` §« Phase 4 — Monitoring »`).

**Cible de maturité** : ≥ 70% des cycles en radar Green sur 6 mois.

### Cas 2 — Radar Yellow (6-7/8) — chaîne tendue

Q6 (goulot Fantastic4) est rouge : le ratio Avengers:Fantastic4 est à
2.0 (au lieu de 1.75). Flash consigne le rouge et ouvre le cycle en
mode handoff — Batman doit fournir un runbook **progressif** (ébauche
validée avant livraison Avengers complète).

**Action** : mode handoff, packet mésoperpétuel avec `decision:
accepted` et condition sur le runbook progressif.

### Cas 3 — Radar Orange (4-5/8) — doctrine non-tenable

Q2 (veto opposable) et Q4 (pair-checks synchronisés) sont rouges.
Flash n'a opposé aucun veto sur les 5 dernières offres, et 2
pair-checks sont en conflit. La doctrine n'est pas **mise en
pratique** — c'est un signal de **dormance** de Flash.

**Action** : mode negotiation, B2 Council convoqué. Flash consigne
les rouges dans le packet, et le Council arbitre les conflits.

## Anti-pièges

- **RadarGreen par défaut**. Un cycle qui s'ouvre systématiquement en
  Green sans diagnostic des questions est un **false positive**.
  Flash doit traiter les 8 questions même quand le score est haut.
- **Q3 traitée comme veto**. L'amplification candidate « mécanisme de
  reprise documenté » (cf. `flash-amplification-mecanisme-reprise.md`)
  n'est pas encore adoptée. Q3 teste la **maturité** doctrinal, pas
  l'application d'un veto. C'est un signe de maturité, pas un veto.
- **Score Yellow sans packet mésoperpétuel**. Un cycle qui s'ouvre en
  Yellow sans packet mésoperpéretuel consigné est en **mode handoff
  non-tracé**. Le B2 Council doit refuser le Yellow sans packet.
- **Score Red sans escalate B1**. Un cycle Red qui ne déclenche pas
  l'escalade B1 est une **décision personnelle** de Flash. Le score
  Red est un signal systémique — seul B1 peut trancher un cycle Red.
- **Confondre radar et matrice**. Le radar est un outil **Flash** (auto-
  évaluation). La matrice d'harmonisation est un outil **B2 Council**
  (arbitrage). Les deux sont complémentaires, pas interchangeables.

## Liens

- [[flash-doctrine-valeur-artefact]] — la doctrine Bloc A
- [[flash-veto-offre-depersonnalisee]] — le veto testé Q2
- [[flash-amplification-mecanisme-reprise]] — l'amplification testée Q3
- [[flash-pair-checks-dependencies]] — les 4 pair-checks testés Q4
- [[flash-triple-squad-launch-canon-protocol]] — la chaîne testée Q5-Q6
- [[flash-jtbd-emit-receive]] — le budget Wonder Woman testé Q7
- [[flash-red-flag-1-trigger]] — le red flag #1 déclenché si Q4-Q6 rouges
- [[b2-harmonization-matrix-exploitable]] — la matrice B2 qui complète le radar
- [[b2-council-cadence-and-chair]] — la séance hebdomadaire qui statue sur les Orange
- [[b1-stop-conditions-escalier]] — l'escalade B1 sur les Red

## Note de confiance

**Reconstruit, à moitié étayé.** Les 4 questions de doctrine (Bloc A)
sont **projetées** à partir de la doctrine valeur d'artefact et des 7
concepts tour 1. Les 4 questions de run (Bloc B) sont **projetées** à
partir du triple-squad launch protocol, de la matrice d'harmonisation,
et du veto Wonder Woman. Le format binaire (vert/rouge) avec seuil
chiffré est **emprunté** au radar 8-domaines canonique (cf.
`eight-domain-avengers-wheel.md`). Le score agrégé et les 4 niveaux
(Green/Yellow/Orange/Red) sont **projetés** par analogie avec la
matrice d'harmonisation (qui a 9 critères + 5 red flags). Les 5 étapes
d'application sont **reconstruites** à partir du cycle B1 (mensuel) et
du cycle B2 (hebdomadaire) — analogique au triplet 9 (Summers cycle
mensuel) et triplet 10 (VP cycle hebdomadaire). Les 3 cas d'application
sont **projetés** à partir de la pratique observée. Le radar est un
**draft d'outillage**, pas un outil adopté.