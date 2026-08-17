---
type: Playbook
title: Distiller un corpus qu'aucun agent ne peut lire
description: Extraction scriptée exhaustive d'abord, distillation sémantique déléguée ensuite — et la règle qui interdit de faire passer un échantillon pour un inventaire.
tags: [distillation, okf, rdf, delegation, m3, methode]
generated: { by: claude-opus-5, at: 2026-08-17T20:20:00Z }
verified:
  - { by: process:inventaire-para-v2, at: 2026-08-17T19:50:00Z }
sources:
  - id: mesure-corpus
    resource: "50_Distillation/_mesures/corpus_md.json — 63 260 .md sur 725 607 fichiers"
    author: process:inventaire-para-v2
    last_modified: 2026-08-17
  - id: canon-delegation
    resource: "C:/Users/amado/CLAUDE.md — hiérarchie de délégation et les cinq pièges d'invocation"
    title: Canon du poste
    last_modified: 2026-08-17
  - id: rdf
    resource: https://www.w3.org/TR/rdf12-concepts/
    title: RDF 1.2 Concepts and Abstract Data Model
    last_modified: 2026-08-17
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Les volumes viennent d'un
> comptage réel du disque ; la méthode est une décision, pas une mesure.

# Le problème de taille

Le PARA de la V2 contient **725 607 fichiers**. Environ 519 000 sont du `.js`,
`.map`, `.ts` et `.mjs` — des dépendances installées, pas de la connaissance.

Le corpus qui porte du sens, ce sont les **63 260 fichiers `.md`**, 336 Mo.

**Aucun agent ne peut lire 63 260 fichiers.** À vingt fichiers par appel, c'est
trois mille appels ; la qualité s'effondre bien avant le quota. Un essaim qui
prétendrait « explorer chaque recoin » produirait un échantillon déguisé en
exhaustivité — et c'est précisément le genre de résultat sur lequel on bâtit
pendant des mois avant de découvrir le trou.

# Les deux temps

## 1. Extraction scriptée — 100 % du corpus, sans LLM

`scripts/extraire_substrat_rdf.py` lit chaque `.md` et en extrait le
frontmatter, le titre, le plan des titres, les liens (wiki et Markdown), les
tags, la date et le volume.

Ce que ça donne, c'est déjà la matière première d'un graphe RDF :

| Élément extrait | Rôle dans le triplet |
|---|---|
| chemin du fichier | **sujet** (identifiant stable) |
| clé de frontmatter | **prédicat** |
| valeur de frontmatter | **objet** littéral |
| `[[wikilink]]` ou lien Markdown | **prédicat de relation** vers un autre sujet |
| titres `#`/`##` | hiérarchie interne, donc relations de composition |

**Le script ne comprend rien, et c'est pourquoi il peut tout lire.** Il ne sait
pas si un document dit vrai ni s'il est périmé. Il dit ce qui est écrit et où.

## 2. Distillation sémantique — déléguée, sur l'extraction

Les agents reçoivent le JSONL, pas le corpus. Il leur sert de carte : quels
dossiers portent les documents structurants, quels `[[wikilink]]` sont les plus
cités — ce sont les nœuds du graphe —, quels documents sont récents donc proches
du canon actuel.

Ils n'ouvrent en profondeur que ce que la carte désigne. **Un agent qui lit dans
l'ordre alphabétique aura consommé son budget dans les dossiers les moins
intéressants.**

# Ce qui se délègue, et comment

Un agent par seau PARA, **périmètre d'écriture exclusif**, écrit dans son brief
et rappelé comme un interdit. Sans ce cloisonnement, deux agents se réécrivent
sans que ni l'un ni l'autre ne le voie.

| Agent | Seau | Corpus | Cible |
|---|---|---|---|
| `areas` | `02_Areas_Spock` | 444 | 14 concepts |
| `projets` | `01_Projects_Picard` | 2 154 | 16 concepts |
| `archives` | `04_Archives_Data` | 12 284 | 12 concepts |
| `ressources` | `03_Resources_Geordi` | 48 378 | 20 concepts |

Le lancement passe par `_briefs/lance.sh`, qui neutralise les cinq pièges du
canon : précédence d'environnement, `PATH` absolu, brief par **stdin** et jamais
en argument, garde-fou concaténé en tête, lancements échelonnés.

Il ajoute un sixième contrôle : **il refuse de démarrer si le substrat du seau
est absent ou vide.** Lancer un agent sans sa carte, c'est le condamner à la
lecture alphabétique.

# La règle qui tient tout

**Une couverture partielle déclarée vaut mieux qu'une couverture totale
prétendue** — et c'est la seule des deux qui soit utilisable ensuite.

Chaque rapport doit dire combien de fichiers ont été **réellement lus**, sur
combien de disponibles. Le seau `areas` (444 fichiers) peut viser
l'exhaustivité ; `ressources` (48 378) ne le peut pas, et doit l'écrire.

Corollaire, hérité d'une campagne précédente : **ne jamais croire un compteur
global mesuré pendant que les autres agents écrivent.** Quatre agents ont un
jour rapporté « 94 erreurs » puis « 83 » en mesurant chacun les éditions en vol
des trois autres. Seule la mesure finale, tout le monde arrêté, a un sens.

# Ce que cette méthode ne fait pas

Elle ne juge pas si un document est vrai. Le corpus contient des documents
périmés, contredits par du code plus récent — c'est déjà arrivé, et un rapport
précédent l'a formulé ainsi : *le code était en avance sur le document pris pour
source de vérité.*

Les agents ont donc l'ordre de **nommer les contradictions sans les trancher**.
L'arbitrage appartient au propriétaire du produit, pas à l'agent qui distille.
