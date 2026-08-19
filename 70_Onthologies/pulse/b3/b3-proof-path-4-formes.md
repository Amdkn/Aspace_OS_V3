---
type: Concept
title: B3 proof path — la preuve inspectable sans confiance à l'auteur
description: La preuve que B3 rend n'est pas "un commit qui passe les tests" : c'est un artefact inspectable sans faire confiance à l'auteur (fractal). Les 4 formes canoniques : capture, log, diff, output reproductible. Chaque forme a un critère d'éligibilité et un consommateur canonique (B2 owner, B2 Council, agent relecteur, futur B3).
tags: [b3, proof, inspectable, capture, log, diff, output, reproductibilite, agent-relecteur]
generated: { by: minimax-m3, at: 2026-08-19T02:25:00Z }
verified:
  - { by: process:lecture-fractal-b1b2b3, at: 2026-08-19T02:25:00Z }
  - { by: process:synthese-pulse-b3-tour-1, at: 2026-08-19T02:25:00Z }
sources:
  - id: fractal-b1b2b3
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/fractal-b1b2b3-architecture.md"
    title: Le fractal B1/B2/B3 — Areas perpétuelles vs Summer's Verse datées
    last_modified: 2026-08-17
  - id: canon-1bis
    resource: "C:/Users/amado/CLAUDE.md"
    title: Canon du poste — §1bis « Vérifier, c'est regarder »
    last_modified: 2026-08-15
  - id: agent-relecteur
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/autonomie-agents/agent-relecteur-mandat.md"
    title: Agent relecteur — mandat unique, contexte vierge
    last_modified: 2026-08-17
  - id: jtbd-grammar
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/b3-jtbd-packet-grammar.md"
    title: JTBD-001 packet grammar — la grammaire B3 canonique
    last_modified: 2026-08-17
  - id: triplet-relecture
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets (ligne 41 — interdit-combler-trou)
    last_modified: 2026-08-17
okf_version: "0.2"
---

# B3 proof path — la preuve inspectable sans confiance à l'auteur

> Le fractal dit : *« B3 exécute, collabore en interne (peer-unblock
> d'abord), rend la preuve (inspectable sans faire confiance à
> l'auteur). »* Ce concept détaille ce que **rendre la preuve** signifie
> concrètement pour un agent B3 qui n'est pas cru sur parole.

## Pourquoi « inspectable sans confiance à l'auteur »

Le canon §1bis est explicite : *« un agent délégué n'est jamais cru sur
parole. »* La raison n'est pas la défiance — c'est que l'auteur a deux
handicaps structurels :

- il **sait** pourquoi le code est correct, et projette cette certitude ;
- il a **investi** dans la solution, et le biais de confirmation lui fait
  défendre ce qu'il a produit.

La preuve doit donc être **auto-suffisante** : un lecteur indépendant
peut la parcourir et conclure « oui, c'est bon » sans avoir besoin de
reconstituer l'intention de l'auteur. C'est la **dette de
reconstitution** que la preuve élimine.

## Les 4 formes canoniques de preuve

Un B3 choisit **une ou plusieurs** formes selon le type de job. Chaque
forme a un critère d'éligibilité et un consommateur canonique.

### Forme 1 — Capture (artefact visuel ou interactif)

**Définition** : un instantané de l'état observable (UI, sortie
graphique, dashboard) à un moment donné, **daté** et **navigable**.

**Critère d'éligibilité** : le job produit un effet visible (UI,
dashboard, render, mail généré). Sans visibilité, la capture n'est pas
une preuve.

**Consommateur canonique** : B2 owner du domaine, agent relecteur
(`agent-relecteur-mandat.md` §« Pourquoi ne pas automatiser » — la
capture couvre les défauts sémantiques que la machine ne voit pas).

**Exemple** : pour Coach OS, `node tools/shot.mjs --app <app> --section
"<Section>" --out <chemin.png>` produit une capture datée. Sans capture,
un fix de rendu n'est pas un fix.

### Forme 2 — Log (trace d'exécution horodatée)

**Définition** : la sortie horodatée et ordonnée de l'exécution, avec
les décisions intermédiaires visibles (pas seulement le résultat final).

**Critère d'éligibilité** : le job a une exécution non-triviale (test
suite, migration, déploiement, run d'agent). Pour un changement d'une
ligne, le log n'est pas la bonne forme — un diff suffit.

**Consommateur canonique** : B2 Council (qui arbitre sur des traces
horodatées), agent relecteur pour les défauts temporels.

**Exemple** : un run `vitest run --reporter=verbose` qui montre **les
étapes** et non seulement le résumé. L'examen préalable
(`examen-prealable.md`) est un log par construction.

### Forme 3 — Diff (changement minimal et vérifiable)

**Définition** : la liste des fichiers touchés, avec un diff lisible
par un pair non-auteur.

**Critère d'éligibilité** : le job produit du code, de la
configuration, ou du contenu versionné. La preuve « j'ai changé 3
fichiers » sans diff n'est pas un diff.

**Consommateur canonique** : squad lead, futur B3 qui reprend le code,
agent relecteur pour les défauts mécaniques.

**Anti-pattern** : un diff avec 50 fichiers touchés et un message
de commit vague. Le diff doit être **minimal** (le moins de fichiers
possibles) et **commente** (chaque commit explique le **pourquoi**,
pas le **quoi**).

### Forme 4 — Output reproductible (script ou commande)

**Définition** : un script, une commande, ou un pipeline qui, lancé
par un tiers, **reproduit le même résultat** que la preuve rendue.

**Critère d'éligibilité** : le job est automatisable (build, deploy,
migration, ETL, evals). Pour une décision éditoriale ou un arbitrage
humain, l'output reproductible n'est pas la bonne forme.

**Consommateur canonique** : B2 owner qui rejoue, squad lead qui
déploie, agent relecteur qui vérifie la cohérence.

**Anti-pattern** : un script qui ne tourne que sur la machine de
l'auteur (PATH implicite, variables d'environnement non exportées,
credentials non versionnés). La portabilité est l'éligibilité.

## L'arbre de décision

Quel B3 utilise quoi ? L'arbre, du spécifique au générique :

1. **Le job touche une UI / dashboard / artefact visuel ?**
   → Forme 1 (capture) **obligatoire**.
2. **Le job est un run d'agent / une migration / un build ?**
   → Forme 2 (log) **obligatoire**.
3. **Le job modifie du code / de la config / du contenu ?**
   → Forme 3 (diff) **obligatoire**.
4. **Le job est automatisable et re-jouable ?**
   → Forme 4 (output reproductible) **en complément**.

Un job qui produit **une seule** forme de preuve est suspect : un
nouveau Behaviour dans une app web devrait avoir **au moins** capture +
diff. Un run d'agent devrait avoir **au moins** log + output
reproductible.

## Lien avec l'agent relecteur

La doctrine `agent-relecteur-mandat.md` est explicite : *« le
relecteur couvre les défauts sémantiques : le code fait ce qu'on
voulait, l'API est utilisable, le bord inattendu est traité. »*

C'est précisément ce que la preuve rend visible :

- **Forme 1 (capture)** : le bord visuel non géré.
- **Forme 2 (log)** : le défaut temporel (race, leak, ordering).
- **Forme 3 (diff)** : le défaut mécanique (lint, type, formatting).
- **Forme 4 (output reproductible)** : le défaut de dépendance (le
  relecteur rejoue et voit ce qui casse ailleurs).

L'agent relecteur **consomme** la preuve, il ne la produit pas. La
séparation est nette.

## Lien avec l'interdit « combler un trou »

Le triplet v3 ligne 41 pose : *« Tout B3 a l'interdit de combler
lui-même un trou du sprint — il le signale à son VP au lieu de laisser
le défaut invisible. »*

Une preuve **incomplète** est l'équivalent, en output, du trou comblé
en input. Un B3 qui rend une capture sans log, ou un diff sans output
reproductible, **comble un trou de preuve en silence**. Anti-pattern
équivalent au trou de packet (cf. `b3-hole-signaling-doctrine.md`).

## Source du concept

- `fractal-b1b2b3-architecture.md` §« Le flux de commandement » étape
  5 — *« B3 exécute … rend la preuve (inspectable sans faire confiance
  à l'auteur). »*
- `agent-relecteur-mandat.md` §« Pourquoi ne pas automatiser » — la
  séparation preuve mécanique / preuve sémantique.
- `CANON §1bis` — *« Un correctif visuel sans capture après n'est pas
  vérifié — le dire, ne pas le maquiller. »*

## Liens

- [[b3-jtbd-packet-reception-checklist]] — la preuve valide les champs
  5-7 du packet (RICE + lead/lag + build gates)
- [[b3-peer-unblock-protocol]] — un pair qui débloque n'est pas une
  preuve, c'est un moyen ; la preuve reste due
- [[b3-hole-signaling-doctrine]] — une preuve incomplète est un trou
  de preuve, à signaler
- [[b3-cycle-scrums-five-per-week]] — la preuve est jointe au SCRUM
- [[fifty-three-b3-agent-roster]] — qui consomme la preuve (les pairs,
  le squad lead, B2 owner)

## Note de confiance

**Confirmé par machine.** L'invariant « inspectable sans confiance »
est verbatim du fractal. La décomposition en 4 formes est dérivée de
la pratique (capture pour l'UI, log pour les runs, diff pour le code,
output reproductible pour l'automatisable). Le lien avec l'agent
relecteur est explicite dans `agent-relecteur-mandat.md`.

**Limite signalée** : le corpus ne pose pas explicitement ces 4 formes.
C'est une **structuration** de la pratique existante, pas un canon
publié ailleurs. À valider par confrontation avec un run B3 réel.