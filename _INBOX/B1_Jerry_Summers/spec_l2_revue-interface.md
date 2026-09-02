---
id: "l2-spec-002"
layer: "L2"
classification: "Interface"
status: "DRAFT"
created: "2026-08-31"
okf_version: "0.2"
description: "Proposition d'interface modulable pour l'app Revue — résumé des contradictions, détail au clic"
---

# spec

## Problème mesuré

L'app Revue actuelle (`agent-os/desktop/src/apps/Revue/index.tsx`) force la lecture de
+200 `.md` complets par contradiction. 158 contradictions uniques, dont 55 non
résolues. Le coût d'arbitrage est proportionnel à la taille du document, pas à la
taille de la décision.

## Proposition : séparer le résumé de l'analyse

Deux panneaux, pas deux pages :

### Panneau A — Résumé (toujours visible)
- Carte par sujet : intitulé, chemins A/B, statut (résolu / à arbitrager / auto-dénoncée)
- Filtres : par statut, par domaine, par date
- Badge `A SOURCER` sur les contradictions dont la source n'est pas ancora lue
- Compteur : `X / 158` avec barre de progression

### Panneau Détail — au clic (modulable)
- S'ouvre dans un panneau latéral ou une fenêtre, pas une nouvelle page
- Affiche : le sujet, les deux extraits, la proposition logique (voir ci-dessous),
  et les champs `verified` / `sources.last_modified` pour le verdict
- Un bouton `Marquer résolu` qui écrit l'arbitrage dans le JSON source

## Règle : chaque contradiction propose une réponse logique

Au lieu de dire "à arbitrager", chaque entrée propose une réponse logique :
- Pour les **contradictions de format** (underscore vs tirets, typo, orthographe) :
  → "Unifier sur le canon récent" + chemin du référent
- Pour les **contradictions de valeur** (84 jours vs 12 semaines, USD vs EUR) :
  → "La valeur récente l'emporte" + date des deux sources
- Pour les **contradictions d'état** (Phase D NOT STARTED vs DONE) :
  → "Le document le plus récent l'emporte" + la date

L'arbitrage du propriétaire valve ou rejette la proposition.

## Mesure de succès

| Avant | Après |
|---|---|
| Lire +200 `.md` par contradiction | Lire 1 résumé par sujet, 1 détail au clic |
| 55 non résolues, aucune traitée | Chaque contradiction a une proposition logique prête |
| Temps par verdict = temps de lecture | Temps par verdict = 1 clic |

## Portée

- Fichier cible : `agent-os/desktop/src/apps/Revue/index.tsx`
- Ne pas modifier le JSON source des contradictions (`00_Amadeus/30_MEMORY_CORE/carto/CONSOLIDE.json`)
- L'écriture de l'arbitrage se fait par l'intermédiaire de l'app, pas directement sur le JSON