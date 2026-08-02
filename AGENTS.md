# AGENTS.md — canon A'Space OS V3

> **Loi L0 — Rick.** *Un système qui ne sait pas se répliquer n'est pas un système,
> c'est un document.*

Cette loi remplace l'ancienne — « la sobriété est la clé de la liberté », adossée à la peur
du paperclip. Elle est abrogée le 2026-08-02. La sobriété était une prudence ; elle n'a produit
aucune valeur, elle a produit 48 000 fichiers de description et un opérateur en goulot
d'étranglement. La nouvelle loi n'est pas prudentielle, elle est **constructive**.

---

## 1. Le théorème fondateur

Von Neumann, années 1940 : quel est le minimum requis pour qu'une machine construise une
copie fonctionnelle d'elle-même ?

Le paradoxe : si une machine se copie, la copie a besoin d'une description complète de la
machine — mais la description fait partie de la machine, donc elle a besoin de sa propre
description. Régression infinie.

**L'échappatoire est la dualité du ruban.** La description est utilisée deux fois, de deux
manières incompatibles :

- le **constructeur** la *lit et l'interprète* pour bâtir ;
- le **copieur** la *duplique en aveugle*, sans jamais la comprendre.

C'est cette asymétrie, et rien d'autre, qui brise la régression.

## 2. Les quatre organes

| Organe | Symbole | Rôle | Où, dans V3 |
|---|---|---|---|
| Ruban | φ | la description, complète | `00_Amadeus/60_Tape_Specs/` |
| Constructeur | A | bâtit depuis φ | `10/20/30_*_OS/` |
| Copieur | B | duplique φ sans l'interpréter | `10_Tech_OS/kernel/` |
| Contrôleur | C | ordonne A et B, **puis détache** | `_INBOX/` + `kernel/uc.db` |

Le dernier verbe est le seul qui compte : **détacher**. Un agent qu'on invoque n'est pas
autonome, quel que soit le nombre de threads. V2 avait φ et rien d'autre.

## 3. Le test du ruban

> Si un constructeur doit poser une question à l'opérateur, le ruban est incomplet.

C'est le critère opérationnel, et il est binaire. Une spec qui exige une clarification humaine
n'est pas une spec : c'est une note. Elle retourne à `_INBOX`.

## 4. Ce que Conway impose à la structure

Trois règles suffisent à atteindre la Turing-complétude. La complexité du Jeu de la Vie n'est
jamais déclarée — elle **émerge** de l'interaction de cellules idiotes.

Deux conséquences, non négociables :

**La racine reste minimale.** Chaque dossier ajouté est une règle en plus, et les règles en
plus ne créent pas de capacité : elles la figent. Une taxonomie riche est inerte par
construction — c'est l'erreur exacte de V2.

**Un agent n'est pas un dossier.** Un planeur n'est pas une structure : c'est un motif qui
persiste en se déplaçant, sans qu'aucune cellule ne voyage. Dans V3, un agent est un **item
qui traverse des états dans la file**, pas un répertoire. Ce qui bouge, c'est l'agencement.

## 5. Les lois tenues par la machine

Ces règles ne dépendent d'aucune discipline. Elles sont dans le schéma SQL, et la base refuse
la transaction qui les viole.

**Loi de prédiction.** Rien n'atteint `review` ni `done` sans qu'une prédiction ait été
enregistrée *avant* l'exécution. Une prédiction postérieure à l'acte n'est pas une
vérification, c'est une justification.

**Loi de détachement.** `done` n'est atteignable que depuis `review`. La descendance est
lâchée parce qu'elle a prouvé, jamais parce qu'on l'espère.

**Loi du bail.** Tout travail réclamé porte une échéance. Un agent qui meurt rend son travail
à la file tout seul. Sans elle, une panne bloque une branche pour toujours et l'opérateur
redevient le superviseur.

## 6. Ce que V3 n'est pas

V3 **n'archive pas** et **ne documente pas son propre passé**. Le savoir réutilisable vit dans
la base de connaissance V2 :

```
ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\
```

V2 est la mémoire. V3 est le runtime. Un fichier qui n'exécute rien et contre lequel rien ne
s'exécute n'a pas sa place ici — il appartient à Geordi.

## 7. Chaîne d'outils

| Étape | Outil | Produit |
|---|---|---|
| écrire le ruban | `/spec-loop` · `/bmad` | φ dans `60_Tape_Specs/` |
| bâtir | `/gstack` · `/superpower` · `/gsd` | l'artefact |
| prédire puis vérifier | `/sim-mirofish` | `prediction` pré-enregistrée, puis scorée |
| mesurer | `/ceo-bench` — sqlite + sqlite-vec | calibration |
| boucler | `/loopany` · `/wargames` | la descendance |

---

*Canon V3, 2026-08-02. Abroge et remplace le canon V2 hérité.*
