---
type: Concept
title: Superman — protocole de lecture du journal Council B2 pour les 4 vérifications gap-empirique
description: superman-veto-cycle-observation-empirical-gap.md (vague 4) diagnostique 3 scénarios A/B/C du gap 0/3 vagues 1+2+3+4 et identifie 4 vérifications distinguantes (claims publics / packets Council / decision blocked / delivery non tenue) non exécutées. Ce concept pose un protocole Council-ready pour lire le journal Council B2_DC_DIRECTION_COUNCIL_DECISIONS.md sur 90 jours, exécuter les 4 vérifications, et trancher entre les 3 scénarios diagnostiques — ferme Q7 vague 4 partiellement, ouvre la possibilité de mettre à jour le protocole validation empirique 3 cas/60j.
tags: [superman, veto, gap-empirique, journal-council, lecture, protocole, verifications-distinguantes, scenario-A-B-C]
generated: { by: minimax-m3, at: 2026-08-19T12:30:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-5, at: 2026-08-19T12:30:00Z }
sources:
  - id: veto-cycle-gap-vague-4
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-veto-cycle-observation-empirical-gap.md"
    title: Superman veto cycle observation empirical gap — 3 scénarios A/B/C + 4 vérifications
    last_modified: 2026-08-19
  - id: veto-validation-protocole-vague-3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-veto-empirical-validation-protocole.md"
    title: Superman veto empirical validation protocole — cible 3 cas/60j
    last_modified: 2026-08-19
  - id: veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-veto-catalogue-concrete.md"
    title: Veto Superman catalogue — 5 cas légitimes + 3 cas abusifs
    last_modified: 2026-08-19
  - id: b2-meso-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique 8 champs + D4 append-only
    last_modified: 2026-08-19
  - id: b2-council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche, journal Council D4 append-only
    last_modified: 2026-08-19
  - id: etat-domaines
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/ETAT_DOMAINES.md"
    title: ETAT_DOMAINES vague 1-4 — convergence wheel 8-domain 0 packet observé
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Superman — protocole de lecture du journal Council B2

## La question ouverte Q7 vague 4 — protocole ou inaction

`superman-veto-cycle-observation-empirical-gap.md` (vague 4) pose **3 scénarios diagnostiques A/B/C** pour expliquer le gap 0/3 vagues 1+2+3+4 :

- **Scénario A** — *« veto Superman trop strict, B3 squad évite de publier des claims Growth pour ne pas déclencher le veto »*. Le compteur 0/3 est réel, mais原因は organisationnelle.
- **Scénario B** — *« cycle silencieux, aucun mandate Growth n'a été soumis à Council sur 90 jours »*. Le compteur 0/3 est réel, mais原因は absence.
- **Scénario C** — *« observation mal comptée, le journal Council contient des packets `decision: blocked` motif veto Superman mais l'escouade ne les a pas lus »*. Le compteur 0/3 est **faux** — il y a des cas, l'escouade ne les a pas diagnostiqués.

Les 3 scénarios sont **mutuellement compatibles** — le gap peut être une combinaison. Pour trancher, vague 4 identifie **4 vérifications distinguantes** :

1. **Vérification #1** — nombre de **claims publics Growth** sur 90 jours (LinkedIn, blog, ABM).
2. **Vérification #2** — nombre de **packets mésoperpétuels Superman** sur 90 jours (journal Council).
3. **Vérification #3** — nombre de **`decision: blocked` motif veto Superman** sur 90 jours (journal Council).
4. **Vérification #4** — nombre de cas **delivery non tenue** sur 90 jours (post-mortem B3 + retours clients).

**Aucune des 4 vérifications n'a été exécutée** par l'escouade Superman vagues 1-2-3-4. Q7 reste ouverte. Ce concept pose un **protocole de lecture** pour exécuter les vérifications #2 et #3 (les 2 qui dépendent du journal Council) — les vérifications #1 et #4 dépendent d'autres sources (B3 Guardians logs, post-mortem B3).

## Pourquoi le journal Council est l'instrument de mesure prioritaire

Trois raisons structurelles :

1. **Le journal est canonique** — `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` est posé par `b2-council-arbitrage-rule.md` §« Composition et routine » comme registre append-only D4. Si le journal existe, il est lisible.

2. **Les vérifications #2 et #3 sont les plus discriminantes** — un journal avec 5 packets Superman (vérification #2 haute) ET 0 `decision: blocked` (vérification #3 basse) = scénario A probable. Un journal avec 0 packets Superman (vérification #2 basse) = scénario B certain. Un journal avec 3 packets Superman ET 3 `decision: blocked` (vérifications #2 et #3 hautes) = scénario C certain.

3. **Le format packet mésoperpétuel est uniforme** — 8 champs canoniques (`b2-meso-decision-packet-spec.md`) permettent une extraction automatisée des compteurs `meso_decision_id`, `impacted_domains`, `decision`, et `tradeoff` (pour détecter le motif veto Superman).

## Le protocole de lecture — 5 étapes

### Étape 1 — Localisation du journal

Le journal canonique est `B2_DC_DIRECTION_COUNCIL_DECISIONS.md`. Sa localisation est documentée dans `b2-council-arbitrage-rule.md` §« Sortie » :

> *« un packet YAML court, une ligne par arbitrage validé, append à `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` (registre append-only, D4) »*

**Action** : `ls` ou `find` sur le chemin canonique. Si le journal existe, lire. S'il n'existe pas (scénario B-fermé), consigner dans le rapport vague 6 que le journal **n'est pas tenu** — c'est un trou canonique **plus grave** que le gap 0/3 (le Council ne tient pas son propre journal D4).

### Étape 2 — Extraction des packets Superman

Filtrer le journal sur `impacted_domains` contenant `growth` OU `superman`. Compteur **vérification #2**. Le filtre est mécanique (YAML search), pas interprétatif.

**Si compteur = 0** : vérification #2 basse. **Scénario B certain** — aucun mandate Growth n'a atteint le Council en 90 jours. Le compteur 0/3 est réel,原因は absence.

**Si compteur ≥ 1** : vérification #2 haute. Passer à l'étape 3.

### Étape 3 — Extraction des décisions `blocked`

Pour chaque packet Superman extrait (vérification #2 haute), filtrer sur `decision: blocked`. Compteur **vérification #3**.

**Si compteur = 0** : vérification #3 basse. **Scénario A probable** — Superman Growth atteint le Council, mais aucun packet n'est bloqué par veto. Le compteur 0/3 est réel, mais原因は probablement l'évitement B3 (B3 squad ne claim pas pour ne pas déclencher le veto).

**Si compteur ≥ 1** : vérification #3 haute. **Scénario C certain** — il y a des cas où le veto Superman a bloqué un packet. Le compteur 0/3 de l'escouade est **faux** — l'escouade n'a pas lu le journal.

**Si compteur ≥ 3** : **cible 3 cas/60j** du protocole validation empirique (`superman-veto-empirical-validation-protocole.md` vague 3) est **atteinte**. Passer à l'étape 4 avec déclencheur positif.

### Étape 4 — Lecture du `tradeoff` pour motif veto

Pour chaque packet `decision: blocked` (vérification #3 haute), lire le champ `tradeoff` pour identifier le **motif veto Superman**. Le motif attendu est *« prise de parole publique qui promet un résultat que la delivery ne tient pas »* (cf. `b2-eight-domain-vetoes-catalogue.md` ligne 5).

**Si motif trouvé** : consigner dans le rapport vague 6 comme **cas observé**. Le gap 0/3 est **fermé**.

**Si motif absent ou autre** : le packet `decision: blocked` n'est **pas** un veto Superman. C'est un autre veto (Batman Ops, Aquaman Legal, etc.). Ré-arbitrer le compteur vérification #3.

### Étape 5 — Production du diagnostic final

Cinq issues possibles :

| Issue | Vérifications | Scénario dominant | Action vague 6 |
|---|---|---|---|
| I1 | #2 = 0 | **B certain** | Rapport : journal Council pas tenu OU Superman Growth pas mandaté. Remontée B1. |
| I2 | #2 ≥ 1, #3 = 0 | **A probable** | Rapport : B3 squad évite les claims. Amendement doctrine veto (passage de blocage aval à reformulation amont, cf. `superman-dod-cas-type-2-awareness-prelaunch-verrouille.md`). |
| I3 | #2 ≥ 1, #3 = 1-2 | **C certain partiel** | Rapport : 1-2 cas observés, mais cible 3/60j non atteinte. Protocole validation empirique reste actif. |
| I4 | #2 ≥ 1, #3 ≥ 3 | **C certain + cible atteinte** | Rapport : gap 0/3 fermé, 3 cas observés, doctrine confirmée. Mettre à jour `superman-veto-empirical-validation-protocole.md` avec cas réels. |
| I5 | journal absent | **B-fermé aggravé** | Rapport : journal Council D4 **pas tenu** par B2 Council. Trou canonique grave, escalade B1 immédiate. |

## Les 3 conditions de saisissabilité

Le protocole est saisissable quand **3 conditions cumulatives** sont réunies :

1. **L'escouade Superman a un mandat B2 Council pour lire le journal** — vague 5 ne l'a pas (l'escouade n'a pas mandat de tenir le journal, cf. `superman-veto-cycle-observation-empirical-gap.md` §« Remontée vers B2 »). **Condition non remplie vague 5**.

2. **Le chemin `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` est localisable** — vague 5 n'a pas localisé le journal. **Condition non vérifiée vague 5**.

3. **Le journal est tenu** (append-only D4) — vague 5 ne sait pas. **Condition non vérifiée vague 5**.

**0/3 conditions remplies vague 5.** Le protocole est **Council-ready, pas saisissable** par cette escouade. **Remontée vers B2** : un capitaine B2 (Superman ou pair) doit inscrire ce protocole à l'ordre du jour d'une séance hebdomadaire.

## Compatibilité avec les autres protocoles Superman

| Protocole Superman | Cible | Statut vague 5 |
|---|---|---|
| **Validation empirique 3 cas/60j** (`veto-empirical-validation-protocole.md` vague 3) | Observer 3 cas de veto Superman en 60j | 0/3 vague 5 (pas démarré) |
| **Lecture journal Council** (ce concept, vague 5) | Trancher A/B/C et exécuter #2/#3 | **0/3 conditions saisissabilité** |
| **Empirical validation protocol application** (autres escouades, symétriques) | Observer 3 cas pour 6 concepts | 0/3 vague 5 (convergence wheel 8-domain) |

Le protocole de lecture vague 5 **complète** le protocole validation empirique vague 3 — il fournit l'instrument de mesure (le journal) qui permet de compter les 3 cas. Sans lecture du journal, le protocole validation empirique reste un voeu pieux.

## Anti-pièges

- **Lire le journal sans mandat B2.** Refusé — cette escouade n'a pas mandat de tenir le journal Council. La lecture sans mandat est un **trou contractuel** (cf. `superman-jtbd-reception-from-b3-other-squads.md` §« Asymétrie 2 »). Remontée B2 obligatoire.
- **Confondre `decision: blocked` motif veto Superman avec autre motif.** Refusé — Batman Ops (procédure sans condition d'arrêt), Aquaman Legal (engagement sans périmètre), Wonder Woman Finance (dépense récurrente sans ROI) bloquent aussi. Le champ `tradeoff` doit porter le motif explicite « prise de parole publique promet un résultat que la delivery ne tient pas ».
- **Diagnostic instantané sans lire le journal.** Refusé — vague 4 a projeté 3 scénarios sans exécuter les vérifications. Le diagnostic vague 5 reste projeté tant que le journal n'est pas lu. **Confiance basse** tant que saisissabilité 0/3.
- **Saisissabilité 0/3 = inaction.** Refusé — la vague 5 pose un protocole, pas une inaction. Le protocole est Council-ready, attendant un capitaine B2 qui mandate la lecture.
- **Confondre journal Council et journal de projet.** Refusé — `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` est un journal mésoperpétuel B2 Council. Les journaux de projet (SCRUMS.md, Ownerbook, journal_b2_t2.log) sont des artefacts B3 ou de suivi, pas le journal Council canonique.

## Statut canonique

**Council-ready, pas saisissable vague 5.** Ce protocole est :

- **Proposé** par cette escouade Superman vague 5.
- **5 étapes** Council-ready (localisation, extraction packets, extraction blocked, lecture tradeoff, diagnostic).
- **5 issues** (I1-I5) discriminantes.
- **3 conditions** de saisissabilité non remplies vague 5.
- **Non soumis** au Council — cette escouade n'a pas mandat de tenir le journal.
- **Complémentaire** au protocole validation empirique vague 3 — fournit l'instrument de mesure.

**Confiance** : *haute* sur la structure du protocole (5 étapes + 5 issues + 3 conditions), *basse* sur le diagnostic réel (qui dépend de la lecture effective du journal). Le journal Council **peut très bien être vide** (scénario I5) — c'est un trou canonique plus grave que le gap 0/3 et un signal d'alerte pour B1.

## Liens

- [[superman-veto-cycle-observation-empirical-gap]] — vague 4, 3 scénarios A/B/C + 4 vérifications
- [[superman-veto-empirical-validation-protocole]] — vague 3, cible 3 cas/60j
- [[superman-veto-catalogue-concrete]] — veto Superman catalogue
- [[superman-dod-cas-type-2-awareness-prelaunch-verrouille]] — mode reformulation amont
- [[superman-jtbd-reception-from-b3-other-squads]] — asymétrie 2 (trou contractuel)
- [[b2-meso-decision-packet-spec]] — format packet 8 champs + D4 append-only
- [[b2-council-arbitrage-rule]] — journal Council canonique
- [[etat-domaines]] — convergence wheel 8-domain vague 1+2+3+4

## Note de confiance

**Protocole Council-ready, saisissabilité 0/3 vague 5.** La structure du protocole (5 étapes + 5 issues + 3 conditions) est **reconstruite** depuis `b2-council-arbitrage-rule.md` (routine Council, journal D4 append-only) + `b2-meso-decision-packet-spec.md` (format 8 champs) + `superman-veto-cycle-observation-empirical-gap.md` (3 scénarios A/B/C + 4 vérifications). Les 5 issues (I1-I5) sont **projetées** par combinaison logique des 4 vérifications. La saisissabilité 0/3 vague 5 est **confirmée par absence** — l'escouade n'a pas mandat de lecture, n'a pas localisé le journal, et ne sait pas s'il est tenu. La remontée B2 est l'action attendue. **Confiance haute** sur la structure du protocole, *basse* sur le diagnostic (qui dépend de la lecture), *haute* sur le constat saisissabilité 0/3 vague 5 (vérifiable par introspection de la session).
