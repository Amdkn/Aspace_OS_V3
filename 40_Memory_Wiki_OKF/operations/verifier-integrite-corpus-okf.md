---
type: Playbook
title: Vérifier l'intégrité du corpus OKF — liens morts, frontmatter, confiance
description: Un script mesure ce que le canon exigeait de la seule vigilance humaine, et quatre pièges de résolution payés pour qu'il ne mente pas.
tags: [okf, integrite, liens-morts, verification, corpus]
generated: { by: claude-opus-5, at: 2026-08-24T21:40:00Z }
verified:
  - { by: process:verifier_okf, at: 2026-08-24T21:40:00Z }
sources:
  - id: script
    resource: scripts/verifier_okf.py
    title: Le validateur lui-même
    last_modified: 2026-08-24
  - id: mesure
    resource: "python scripts/verifier_okf.py — sortie du 2026-08-24"
    title: 2714 fichiers, 652 concepts, 2728 liens, 92 défauts
    author: process:verifier_okf
    last_modified: 2026-08-24
okf_version: "0.2"
---

# Vérifier l'intégrité du corpus OKF

```bash
python "C:/Users/amado/ASpace_OS_V3/scripts/verifier_okf.py"
```

Sort en `1` s'il reste des défauts bloquants, en `0` sinon. Aucune dépendance.

## Ce qu'il mesure, et pourquoi c'était nécessaire

Le canon posait deux règles que **rien ne vérifiait mécaniquement** :

> « Ne **jamais** poser de lien `[[nom]]` vers un concept qui n'existe pas —
> vérifier avant d'écrire. Un lien mort ment à l'avenir. »

et l'échelle de confiance déduite de `verified`. Les deux tenaient par la
discipline. Une règle tenue par la seule vigilance finit par céder — c'est
mesurable, et voici la mesure.

## État au 2026-08-24 (première exécution)

| | |
|---|---|
| Fichiers markdown scannés | 2714 |
| Concepts OKF (`okf_version`) | **652** |
| Liens `[[…]]` évalués | 2728 |
| **Liens morts** | **78 cibles, citées 124 fois** |
| Liens résolus par préfixe | 25 |
| Liens ambigus | 1 |
| Frontmatter incomplet | 14 concepts sur 652 |

Niveau de confiance du corpus :

| Niveau | Concepts | Part |
|---|---|---|
| Revu par un humain | 46 | 7 % |
| Confirmé par machine | 582 | **89 %** |
| Non vérifié | 24 | 3 % |

**Correction d'une croyance du canon** : le canon affirmait « aucun relu par un
humain ». C'est faux depuis — **46 concepts portent un `human:`**. Le goulot
reste la vérification, mais il n'est plus total.

## Le corpus lie par PRÉFIXE, pas par slug exact

Découverte qui change la lecture de tout compteur de liens : `[[b2-council-cadence]]`
vise `b2-council-cadence-and-chair.md`, qui existe. Un test d'égalité stricte
déclarait **90 liens morts dont la plupart résolvaient**.

Le script classe donc en cinq états, jamais en binaire :

| État | Sens |
|---|---|
| `exact` | le slug est le nom de fichier |
| `préfixe` | un seul fichier commence par ce slug — résout, mais fragile |
| `ambigu` | plusieurs candidats : le lecteur ne peut pas trancher |
| `malformé` | la cible existe, la forme est fautive (`[[cf. x]]`) |
| `mort` | aucun candidat |

Un lien `préfixe` **cesse de résoudre** le jour où un second concept partage ce
préfixe. C'est une dette silencieuse : 25 liens en dépendent aujourd'hui.

## Quatre pièges d'instrument payés pendant l'écriture

Chacun produisait un rapport faux — et un rapport faux ne se corrige pas, il
s'ignore.

1. **`os.path.splitext` coupe au dernier point.** `cf. b2-eight-domain-vetoes`
   devenait le slug `cf`. Ne retirer que l'extension `.md`, jamais par
   `splitext`, sur des cibles qui peuvent contenir des points.
2. **Les `[[…]]` dans du code ne sont pas des liens.** `[[:space:]]` est une
   classe POSIX, `[[1984, 2790]]` un tableau. Neutraliser blocs et spans de
   code avant de scanner — 30 faux positifs écartés.
3. **`_REVIEW_NOTEBOOKLM/` est une sortie générée.** Chaque concept y est
   recopié : compter ses défauts double le total et corriger la copie à la
   main serait perdu à la prochaine régénération.
4. **`xargs wc -c | tail -1` ment sur un gros corpus.** xargs découpe en lots,
   `tail -1` ne capte que le dernier total. Accumuler avec `awk`.

## Ce qu'il ne fait pas

Il ne construit **aucun graphe** — `concepts_vers_triplets.py` le fait déjà
pour `50_Distillation` et `60_Implementation`, `valider_triplets_aspace.py`
décide ce qui entre. Ce script dit seulement si le corpus tient debout **avant**
qu'on en extraie quoi que ce soit : un graphe bâti sur des liens morts
propagerait le mensonge au lieu de le signaler.

Il ne corrige rien non plus. Réparer un lien mort demande de savoir ce que
l'auteur voulait dire ; un script qui devinerait ferait pire que le défaut.

## Écart mesuré : la mémoire n'est pas où le canon la place

Le canon désigne `40_Memory_Wiki_OKF/` comme source de vérité. La mesure dit
autre chose sur la répartition des 652 concepts :

| Dossier | Concepts |
|---|---|
| `70_Onthologies/` | 300 |
| `50_Distillation/` | 262 |
| `60_Implementation_Méthodologiques/` | 57 |
| **`40_Memory_Wiki_OKF/`** | **23** |

Le bundle canonique porte **3,5 %** du corpus. Ce n'est pas signalé comme un
défaut par le script — c'est une question de gouvernance, pas d'intégrité —
mais elle est posée ici parce qu'elle change ce que « source de vérité » veut
dire en pratique.
