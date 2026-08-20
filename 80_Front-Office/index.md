---
type: Bundle index
title: 80_Front-Office — les pages de revue, centralisées par jonctions
description: Une page HTML autonome par vague, ouvrable en un clic depuis file://. La forme rapide de la revue, à côté du podcast NotebookLM qui en est la forme lente.
tags: [front-office, revue, html, dashboard, jonctions, vague, scrum]
generated: { by: claude-opus-5, at: 2026-08-20T10:00:00Z }
verified:
  - { by: process:generation-3-pages-reelles, at: 2026-08-20T10:00:00Z }
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Le générateur a été exécuté
> sur trois dossiers réels et ses chiffres recoupent le corpus. La structure
> d'ensemble (tableaux de bord A3, jonctions) est **conçue, pas éprouvée**.

# À quoi sert cet étage

NotebookLM rend un podcast de vingt minutes : excellent pour découvrir un
corpus en marchant, inutilisable pour répondre à *« où en est cette vague ? »*.

Cet étage répond en trois secondes.

## La contrainte de forme, qui n'est pas cosmétique

**Chaque page est autonome** : aucun CSS externe, aucun JS distant, aucune
police à télécharger. Elle s'ouvre depuis `file://` sans serveur et sans
réseau.

Une page de revue qui exige une chaîne de build est une page qu'on ne regarde
pas — et la revue est déjà le goulot.

## Ce que la page montre en premier

**Ce qui ne va pas.** Une page qui ouvre sur *« 258 concepts produits »*
félicite ; une page qui ouvre sur *« 258 concepts, 0 relu »* informe. Seul le
second chiffre appelle un geste.

# Structure

| | |
|---|---|
| `generer.py` | Le générateur. Une vague → une page. |
| `reviews/` | Les pages de revue B3 — une par vague de Scrum. |
| `dashboards/` | Les tableaux de bord A3 — vision B1 agrégée. **Vide : à construire.** |
| `_gabarits/` | Gabarits partagés. **Vide** — le CSS est pour l'instant dans `generer.py`, ce qui garantit l'autonomie des pages. |
| `_assets/` | **Vide, et volontairement.** Un asset partagé casserait `file://`. |

# L'usage

```bash
python 80_Front-Office/generer.py 70_Onthologies/pulse/domaines/batman --titre "Vague 2 — Domaine Batman"
```

## Les constats d'une vague

Les dettes, avancées et apprentissages viennent d'un `constats.json` déposé
dans le dossier de vague par l'agent qui la clôt :

```json
[ { "nature": "dette", "titre": "…", "detail": "…", "preuve": "chemin/vers/preuve" } ]
```

`nature` vaut `dette`, `avancee` ou `apprentissage`. **Un constat sans
`preuve` s'affiche marqué « sans preuve »** — il n'est pas caché, il est
signalé, parce qu'un constat sans preuve est une opinion.

Si le fichier est absent, la page le dit et ne fabrique rien.

# Ce qui a été mesuré

Trois pages générées sur des dossiers réels le 2026-08-20 :

| page | concepts | en attente d'un humain |
|---|---|---|
| étage B1 | 15 | **0** |
| étage B3 | 11 | **0** |
| domaine Batman | 33 | **33** |

Les zéros de B1 et B3 sont le résultat direct du tampon V0. Le 33/33 de Batman
est la dette restante, rendue visible pour la première fois.

# Ce qui manque

- **Les tableaux de bord A3** (`dashboards/`) : la vision B1 agrégée, et
  l'app de simplification de revue déclenchée après chaque vague.
- **Les jonctions NTFS** vers les dossiers de vague. Rappel du canon :
  pour supprimer une jonction, `os.rmdir` **uniquement** — `rmtree`, `rm -rf`
  et `Remove-Item -Recurse` suivent le lien et détruisent la cible réelle.
- **Une page d'index** listant toutes les vagues.

Voir [[../90_Back-Office/index]] pour le schéma qui alimentera ces vues.
