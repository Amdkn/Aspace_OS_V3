---
type: Bundle index
title: 90_Back-Office — la cadence en relations, après le RDF
description: Le schéma SQL de la vague de Scrum et de son emboîtement, les vues que consomment les pages HTML, et les diagrammes Mermaid. La forme simplifiée qui vient après les triplets RDF et les concepts OKF.
tags: [back-office, sql, sqlite, cadence, scrum, sprint, rock, 12wy, mermaid, escalade]
generated: { by: claude-opus-5, at: 2026-08-20T10:00:00Z }
verified:
  - { by: process:sqlite-executescript-et-3-vues, at: 2026-08-20T10:00:00Z }
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Le schéma a été appliqué
> dans SQLite et ses trois vues ont été éprouvées sur des données de test.
> Les **valeurs de cadence** (5/4/3/4) sont des décisions du propriétaire,
> reprises telles quelles.

# Pourquoi un schéma SQL alors qu'il y a déjà du RDF

Le RDF dit **ce qui est vrai**. Il dit mal ce qui est *emboîté* et ce qui est
*compté*.

*« 5 Scrums font 1 Sprint »* n'est pas une assertion : c'est une **contrainte
d'intégrité**, et son intérêt est de pouvoir être **violée et signalée**. Un
triplet ne sait pas faire ça. Une vue SQL, si — `v_agregat_incomplet` rend
l'écart, pas la conformité.

C'est donc la vue simplifiée d'*après* la distillation : ce qu'on regarde pour
savoir **où en est** une vague, pas ce qu'on interroge pour savoir **pourquoi
elle existe**.

# Structure

| | |
|---|---|
| `schema/01_cadence.sql` | Le schéma. SQLite, aucun serveur. |
| `mermaid/cadence-et-escalade.md` | Trois diagrammes : emboîtement, escalade, flux d'une vague. |
| `_exports/` | Les bases générées. **Vide.** |

# Ce que le schéma encode

## L'emboîtement, avec sa règle de compte

```
5 Scrums   (B3, quotidien)    = 1 Sprint
4 Sprints  (B2, hebdomadaire) = 1 Rock
3 Rocks    (B1, mensuel)      = 1 Cycle 12WY   → conseils A3, trimestriel
4 Cycles   12WY               = 1 année civile → vaisseaux A2, garde annuelle
```

Ces nombres sont **écrits en dur** dans `genre_agregat.attendu` parce que ce
sont des décisions, pas des moyennes observées. Un agrégat qui s'en écarte
doit se voir, pas se normaliser en silence.

## L'asymétrie temporelle, portée par l'étage

`etage.compressible` vaut 1 pour Business OS et **0 pour Life OS**. Ce n'est
pas un réglage par vague : c'est une propriété de l'étage.

`vague.duree_machine_s` enregistre le temps machine réel, et `v_compression`
tranche — *« commodité atteinte »* seulement si une vague de Scrum tient sous
3600 s. **La compression est constatée, jamais décrétée.**

Life OS reste en temps non comprimé délibérément : c'est ce qui préserve
l'observabilité du multivers de possibilités. Comprimer les deux étages
rendrait l'arbitrage humain inauditable — on verrait qu'une branche a été
retenue, plus pourquoi.

## La sortie d'A0, rendue structurelle

`palier_revue` contient A3, A2, A1, puis `human:amdkn`. **A0 n'y figure pas.**
Sa sortie de la boucle de revue n'est pas une consigne en marge : c'est
l'absence d'une ligne, et aucune revue ne peut donc lui être rattachée.

## Les constats d'une vague

Une seule table `constat` pour les trois natures — `dette`, `avancee`,
`apprentissage` — parce qu'elles partagent le même cycle de vie et la même
page. Les séparer imposerait trois requêtes là où la page en fait une.

`preuve` porte le chemin d'une capture, d'un diff, d'un log ou d'une sortie
reproductible : les quatre formes du contrat de preuve B3.

## La jonction vers le corpus OKF

`concept_lie` **pointe** vers les concepts, ne les duplique pas. Deux sources
de vérité, et celle qui dérive en silence est toujours celle qu'on regarde.

# Les vues, et ce qu'elles servent

| vue | ce qu'elle répond |
|---|---|
| `v_agregat_incomplet` | quel agrégat ne ferme pas, et de combien |
| `v_compression` | la commodité temporelle est-elle atteinte, mesurée |
| `v_escalade` | où en est la revue, qui doit trancher ensuite, combien de dettes ouvertes |
| `v_dette_revue` | combien de concepts attendent encore un humain |

# Un piège déjà payé, dans le schéma

`v_escalade` calcule ses agrégats en **sous-requêtes corrélées**, pas par un
`GROUP BY` sur une double jointure. Joindre `revue` et `constat` ensemble
multiplierait les lignes et gonflerait le compte de dettes par le nombre de
paliers franchis.

**Un tableau de bord qui exagère la dette est aussi faux que celui qui la
cache.** La première version faisait cette faute ; elle a été corrigée après
que SQLite l'ait signalée.

# L'état réel, sans enjoliver

Le schéma est **appliqué et éprouvé, mais vide**. Aucune vague n'y est
enregistrée. Les diagrammes décrivent une machine dont une seule pièce tourne
— le tampon de verdict, qui a fait passer 37 concepts sur 424 en revue humaine.

Voir [[../80_Front-Office/index]] pour les pages qui consommeront ces vues.
