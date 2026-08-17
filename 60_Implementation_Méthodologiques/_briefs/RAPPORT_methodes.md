---
type: Project
title: Rapport — conversion des deux sources en concepts OKF appliqués
description: Bilan de la passe : fichiers lus, fichiers écrits, périmètre non couvert, contradictions entre sources, et niveau de confiance.
tags: [rapport, méthodes, distillation]
generated: { by: minimax-m3, at: 2026-08-17T23:00:00Z }
verified:
  - { by: process:auto-verification, at: 2026-08-17T23:00:00Z }
sources:
  - id: brief-methodes
    resource: 60_Implementation_Méthodologiques/_briefs/BRIEF_methodes.md
    title: "Brief de la passe"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Couverture

## Fichiers lus

| Fichier | Lu en intégralité | Source de mesures |
|---|---|---|
| `60_Implementation_Méthodologiques/_sources/indydevdan-prompt-systeme.md` | oui | structure des six sections, formulations exactes |
| `60_Implementation_Méthodologiques/_sources/echelle-autonomie-agents.md` | oui | les cinq étapes, les quatre chantiers, les chiffres |
| `60_Implementation_Méthodologiques/index.md` | oui | convention du bundle, contradiction utile nommée |
| `60_Implementation_Méthodologiques/prompt-systeme/index.md` | oui | état initial du sous-bundle |
| `60_Implementation_Méthodologiques/autonomie-agents/index.md` | oui | état initial du sous-bundle |
| `60_Implementation_Méthodologiques/_briefs/GARDE_FOU.md` | oui | règles de format OKF et interdits |
| `C:/Users/amado/CLAUDE.md` | non, seulement les sections §1 et §1bis citées par le brief | oui sur ces sections |
| `C:/Users/amado/.claude/CLAUDE.md` | non — lecture non requise par le brief | non |

Le canon du poste n'a pas été lu en intégralité : le brief m'autorisait à
m'appuyer sur les sections explicitement citées par les `_sources/`
(§1, §1bis, §6). Les concepts s'appuient donc sur des citations et
paraphrases des sections connues, et sur les **tableaux d'écart mesuré**
fournis par les sources — pas sur une lecture exhaustive du canon.

## Fichiers disponibles non lus

`C:/Users/amado/CLAUDE.md` comporte d'autres sections (notamment §2
*« Ne pas polluer la racine »*, §3 *« Où vivent les choses »*, §3bis
*« Les MCP »*, §4 *« Piège de ce disque »*, §5 *« Déplacements »*,
§7 *« Orchestration »*, §8 *« SPEC SaaS builder »*) que je n'ai pas
ouvertes. Les concepts qui s'y référeraient (par exemple, un concept
sur l'orchestration par défaut) seraient plus solides s'ils étaient
adossés à ces sections. **Couverture partielle assumée.**

# Fichiers écrits

## Sous-bundle `prompt-systeme/` (7 concepts)

| Concept | Écart principal comblé |
|---|---|
| `purpose-et-pourquoi.md` | pourquoi dispersé dans le canon ; à regrouper en sommaire |
| `patterns-positifs-negatifs.md` | négatifs partiels, positifs à zéro |
| `points-de-reference.md` | embryon `D4` non étendu à D/R/F |
| `bornes-operationnelles.md` | interdits dispersés en anecdotes |
| `alias.md` | aucun raccourci déclaré |
| `exemples-distillation-contexte.md` | aucune paire *« voila comment on fait / voila comment on ne fait pas »* |
| `regle-multiplicativite.md` | méta-règle non explicitée dans le canon |

## Sous-bundle `autonomie-agents/` (5 concepts)

| Concept | Priorité du brief |
|---|---|
| `examen-prealable.md` | **1** — la commande unique et l'obligation de la lancer |
| `agent-relecteur-mandat.md` | **3** — mandat d'un agent relecteur neuf |
| `bacs-a-sable-worktree.md` | **4** — ce que `git worktree` changerait et coûterait |
| `goodhart-compteur-jetons.md` | **5** — la jauge de jetons situe, ne note pas |
| `tension-qualite-quantite.md` | exigence particulière du brief — traiter la tension de front |

## Index mis à jour

- `60_Implementation_Méthodologiques/prompt-systeme/index.md` — section `# Files` complétée à 7 lignes.
- `60_Implementation_Méthodologiques/autonomie-agents/index.md` — section `# Files` complétée à 5 lignes.

## Rapport

- `60_Implementation_Méthodologiques/_briefs/RAPPORT_methodes.md` — ce fichier.

# Périmètre non couvert

Quatre manques, à ouvrir dans une passe suivante :

1. **L'échelle en cinq étapes de Cherny** n'a pas son concept dédié. Le
   brief ne l'exigeait pas, mais le chiffre « 11 $ par employé et par
   mois » et la télémétrie 22 000 développeurs/+441 % sont des points
   d'entrée utiles pour un concept *« situer l'étape du poste »*. Le
   chantier est à l'étape 2 sur trois, à l'étape 1 sur l'examen —
   notion qui pourrait être posée comme un diagnostic récurrent.
2. **Les trois questions pour situer une équipe** (combien d'agents,
   quelle boucle de vérification, qui relit) ne sont pas déclinées en
   concept. Elles pourraient servir de gabarit d'auto-évaluation annuelle.
3. **Le test de Cherny** (*« un ingénieur l'aurait-il fait comme ça ? »*)
   et **le test physique** (lancer deux chantiers, fermer l'écran,
   partir deux heures) ne sont pas posés comme rituels. Ils sont
   mentionnés dans `tension-qualite-quantite.md` mais pas nommés.
4. **L'astuce avancée d'IndyDevDan** (prendre une bonne réponse d'un
   autre modèle, la nettoyer, la poser en exemple) est mentionnée dans
   `exemples-distillation-contexte.md` mais pas développée : comment
   on sélectionne la réponse source, à quelle fréquence on l'ajoute,
   quel crédit on donne à l'auteur original.

# Contradictions entre les deux sources

Les deux sources **ne se contredisent pas**, mais elles **tirent dans
des directions opposées** sur trois points. Je ne tranche pas — je
nomme.

## 1. Sur la cadence d'adoption

- **IndyDevDan** : *« plus c'est multiplicatif, plus on ralentit »*.
  Implique un investissement long à l'écriture du canon.
- **IA et Stratégie** : *« Commencer à deux agents, pas dix »*.
  Implique qu'on accepte de monter en parallèle **tôt**, à petite échelle.

Tension : passer du temps sur le canon retarde l'étape 2. Monter en
parallèle sans canon tenu produit du gaspillage. La résolution possible
est dans `tension-qualite-quantite.md`, section *« grille de décision »*,
mais c'est une grille, pas une réponse.

## 2. Sur la taille du canon

- **IndyDevDan** : ajoute **six sections** au prompt système, plus une
  méta-règle.
- **IA et Stratégie** : le canon doit « tout ce qu'on répète à l'oral,
  session après session, doit y redescendre ». **Pas de plafond explicite.**

Tension : un canon qui grandit无限ement devient illisible. Les concepts
que j'ai écrits tentent des garde-fous (plafond de 8-10 paires
d'exemples, plafond de quatre alias, plafond de sept bornes), mais
aucune des deux sources ne propose un plafond. **C'est une décision
qui reste à trancher.** Une candidate : plafond de 200-300 lignes au
canon global, avec des bundles OKF pour le reste.

## 3. Sur la confiance dans la boucle

- **IndyDevDan** : la qualité d'une réponse est l'alpha et l'oméga.
  Examen et relecture sont des moyens, pas des fins.
- **IA et Stratégie** : *« 31 % de fusions supplémentaires se font sans
  aucune revue »*. La confiance se construit **avant** l'augmentation
  du nombre d'agents.

Tension : IndyDevDan ne parle pas de boucle de vérification ; IA et
Stratégie considère que sans boucle, l'essaim ne mérite pas d'exister.
**L'absence de boucle de vérification dans la première source est un
trou**. Sans elle, le prompt système le mieux écrit reste sans défense
contre un livrable qui satisfait la lettre et rate l'esprit.

## 4. Sur la métrique de progression

- **IndyDevDan** : implicite — la qualité d'une réponse s'améliore en
  précision, en concision, en absence de tics.
- **IA et Stratégie** : explicite — la jauge de jetons (1 M / 10 M /
  100 M / 1 Mds) situe une étape, mais l'avertit du piège Goodhart.

Tension : la jauge de jetons est **trop grossière** pour mesurer la
qualité d'un canon. Mais c'est la seule métrique partagée. Le concept
`goodhart-compteur-jetons.md` pose la critique, et propose
**« concepts publiés et durables »** comme métrique de remplacement —
sans la valider empiriquement. C'est une hypothèse de travail, pas une
réponse.

# Niveau de confiance

Tous les concepts sont à **« confirmé par machine »** (acteur `process:`),
conformément à la consigne du GARDE_FOU. Aucun `human:` n'a été
ajouté, et **aucun concept n'a été revu par un humain**.

La conséquence est claire : les actions proposées (commande
`examen.sh`, liste d'alias, mandats de relecteur…) sont des **hypothèses
de design**, pas des décisions arbitrées. Chaque concept gagnerait à
être validé sur un cas réel avant d'être considéré comme prêt à servir.

# Recommandation pour la suite

Une seule, en respect de la règle de multiplicativité : **valider
d'abord le concept `examen-prealable.md`**, parce qu'il est le plus
rentable et le moins risqué. Une commande d'examen réussie sur trois
chantiers-pilotes prouve la promesse et finance les débats
ultérieurs sur les autres chantiers.

Tout le reste — worktree, relecteur, alias, patterns — peut attendre
qu'un examen vert soit routinier.
