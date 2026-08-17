---
type: Concept
title: Règle de multiplicativité — plus l'artefact compose, plus on ralentit
description: Méta-règle tirée d'IndyDevDan : un artefact appliqué à mille exécutions mérite une heure d'écriture, une commande jetable n'en mérite aucune. Le canon du poste est multiplicatif — il se relit à chaque session.
tags: [prompt-systeme, meta, regle, ecriture]
generated: { by: minimax-m3, at: 2026-08-17T22:30:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T22:30:00Z }
sources:
  - id: indydevdan-extraction
    resource: 60_Implementation_Méthodologiques/_sources/indydevdan-prompt-systeme.md
    title: "IndyDevDan — extraction"
    last_modified: 2026-08-17
  - id: canon-section-1
    resource: C:/Users/amado/CLAUDE.md
    title: "Canon du poste — section §1"
    last_modified: 2026-08-15
okf_version: "0.2"
---

# Le principe

IndyDevDan : *« Plus la chose sur laquelle vous travaillez est multiplicative
pour le reste de votre travail, plus vous devez ralentir. »* Écrire à la
main, ne pas dicter, ne pas improviser. Un artefact appliqué à mille
exécutions mérite une heure ; une commande jetable, non.

La règle est contre-intuitive : l'instinct pousse à investir du temps là
où le gain est visible, c'est-à-dire les artefacts uniques. La règle
inverse l'effort : c'est sur les artefacts **récurrents** que l'investissement
paie — chaque exécution supplémentaire amortit le coût initial.

# L'application à ce poste

Le canon du poste (`C:/Users/amado/CLAUDE.md` et `C:/Users/amado/.claude/CLAUDE.md`)
est l'archétype de l'artefact multiplicatif. Il est lu :

- à chaque session CC (le moteur l'injecte en contexte au démarrage) ;
- à chaque brief rédigé à partir de lui (cinq sections copiées-collées
  depuis le canon) ;
- à chaque brief reçu par un agent héritant du canon parent.

L'amortissement est donc sans plafond. Une heure investie à améliorer le
canon s'amortit sur **chaque session future**, jusqu'à la fin du poste.

# Les artefacts à classer par multiplicativité

| Artefact | Multiplicativité | Investissement attendu |
|---|---|---|
| `C:/Users/amado/CLAUDE.md` (canon) | **maximale** — lu à chaque session | heure(s) de mise à jour, relecture humaine |
| `C:/Users/amado/.claude/CLAUDE.md` (mémoire) | **maximale** — idem | idem |
| Sections d'un bundle OKF | forte — réutilisées par distillation | minutes par section |
| Brief d'agent délégué | moyenne — cinq à vingt exécutions | minutes à un quart d'heure |
| Commande jetable (un `claude -p` isolé) | faible — une seule exécution | secondes |
| Capture d'écran d'un livrable | faible — preuve à un moment | secondes |

# Le piège de la règle

L'investissement asymétrique conduit à un piège : tout devient
« multiplicatif » dès qu'on y pense, et la paralysie s'installe. La règle
protectrice :

- **Un artefact est multiplicatif s'il sera réutilisé au moins cinq fois**
  dans les six mois. En dessous, il est jetable.
- **Un artefact est multiplicatif s'il est transmis à un agent qui n'a
  pas le contexte de l'auteur**. Au-dessus, l'effort d'écriture est
  amorti.
- **Un artefact est multiplicatif si son coût d'erreur est supérieur au
  coût d'écriture**. Un canon d'erreurs coûte plus cher à corriger plus
  tard que ce qu'il aurait coûté à écrire soigneusement.

# Le geste à poser

1. **Marquer au canon sa propre multiplicativité.** Une phrase en tête de
   chaque `CLAUDE.md` : *« Ce fichier est lu à chaque session. Chaque
   ligne ajoutée ici est lue mille fois. »* Ça n'est pas rhétorique — c'est
   un rappel appliqué à l'auteur de la prochaine édition.
2. **Réserver un créneau de revue du canon**, par exemple mensuel, où
   l'objectif unique est de traquer les règles sans source, les anciens
   pièges obsolètes, les formulations de remplissage. Le canon pourrit
   par adjonction ; il se nettoie par ré-écriture.
3. **À chaque ajout, écrire le pourquoi immédiatement.** Voir
   `purpose-et-pourquoi.md`. Une règle sans pourquoi est une règle qui
   finira par être contournée.

# Vérification

À chaque édition du canon, compter les lignes ajoutées et les lignes
retirées. Un canon qui ne perd jamais de lignes est un canon qui garde
des règles obsolètes. Viser un solde **neutre à légèrement négatif** sur
six mois — un canon qui maigrit est un canon qu'on a pensé à élaguer.

# Ce que la règle ne dit pas

La règle ne dit pas qu'il faut **ralentir** au point de ne plus ajouter.
Elle dit qu'il faut **investir** là où l'amortissement le justifie. Un
canon qui ne bouge pas est un canon qui ne répond plus à l'état du poste.
La cadence soutenue est l'amie de la qualité, à condition d'être
gouvernée par la règle de multiplicativité.
