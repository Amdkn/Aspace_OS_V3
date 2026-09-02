---
type: Architecture
title: La porte d'argent — le triptyque de filtres d'entrée en V3
description: Comment `scripts/porte_argent.py` applique les trois filtres (distillation RDF, implémentation méthodologique, formation d'ontologie), pourquoi le critère dépend du seau PARA, et la faute Jerry (juger le miroir au lieu de la chose vivante).
tags: [porte-argent, triptyque, para, gtd, verdict, inertie, v3]
generated: { by: claude-sonnet-4-6, at: 2026-08-30T01:10:00Z }
verified:
  - { by: human:amdkn, at: 2026-08-31T21:28:01Z }
  - { by: claude-sonnet-4-6, at: 2026-08-30T01:10:00Z }
sources:
  - id: script
    resource: "ASpace_OS_V3/scripts/porte_argent.py"
    title: Le script de la porte, avec la règle du propriétaire du 2026-08-29
    last_modified: 2026-08-29
  - id: methode
    resource: "ASpace_OS_V3/50_Distillation/METHODE.md"
    title: La méthode de distillation que le filtre 1 applique
    last_modified: 2026-08-30
okf_version: "0.2"
---

# La règle du propriétaire (2026-08-29)

« Rien n'entre dans V3 sans passer par cette triptyque de filtres avant de
finir dans OpenWiki et OKF » :

1. **Distillation RDF** → le substrat : ce qui est écrit, et où. Extraction
   scriptée, **100 % du périmètre, sans modèle** — la conformité à
   `METHODE.md` est explicite : faire lire les fichiers par un agent ne
   couvrirait qu'un échantillon en prétendant couvrir le tout.
2. **Implémentation méthodologique** → à quelle échelle (semaine, jour,
   deep-work) et sous quel mode (collaboratif, autonome) ça s'exécute. Un
   artefact sans rattachement n'est pas implémentable : c'est une note.
3. **Formation d'ontologie** → triplets Turtle, **URN** (`urn:aspace:`) et
   pas d'IRI HTTP inventés — conformité à `concepts_vers_triplets.py`.

Le script **applique** la chaîne existante (`extraire_substrat_rdf.py`,
`generer_briefs_distillation.py`, `concepts_vers_triplets.py`,
`monter_70_onthologies.py`) ; il ne la remplace pas. Le verdict par filtre
**peut être négatif** : « une porte qui laisse tout passer n'est pas une
porte ». Simulation par défaut ; `--appliquer` écrit dans
`50_Distillation/_substrat/`, `60_Implementation_Méthodologiques/domaines/`,
`70_Onthologies/sujets/`.

# Le critère dépend du seau PARA — correction du 2026-08-29

Juger une **Area** sur une échelle semaine/jour/deep-work est une faute de
catégorie : une Area est perpétuelle par définition, sans finalité
temporelle. Lui donner « PASSE » sur ce calcul valide l'inertie. Donc :

| Seau | Critère |
|---|---|
| Projet (Picard) | une **fin** — couverture d'échelle ≥ 50 %, un mode identifiable |
| Area (Spock) | un **standard tenu** (≥ 20 %) ET une **revue qui retire** (≥ 20 %) ; inertie = dette/revue ≤ 2,0 |
| Ressource (Geordi) | référence — aucune cadence attendue |
| Archive (Data) | non-usage — rien à mesurer |

Le ratio d'inertie (`dette / revue`) dit le cas visé : une Area avec beaucoup
de dette et peu de revue est un système mort qui continue de tourner. Le
propriétaire : « le maintien de standard de reproduction perpétuel sans
finalité temporelle est pire pour l'inertie induite dans un système mort par
des accumulations de défaut ».

# La faute Jerry — le miroir n'est pas la chose

`05_From_V2_Domains` vit sous `03_Resources_Geordi`, donc tout ce qui en vient
est une **RESSOURCE** — un miroir de lecture. Le 2026-08-29, la porte a rendu
un verdict sur une copie en croyant juger la Area vivante. Le seau est inscrit
dans l'arborescence, pas choisi. Les seaux vivants (`01_Projects_Picard`,
`02_Areas_Spock`) sont les sources prioritaires ; le miroir reste une source
légitime, mais son verdict porte sur un reflet.

# Ce que la porte n'est pas

Ce n'est **pas de l'archivage** : ce qui n'est pas utilisé est en **non-usage**
et se gère en PARA ; un domaine migré reste vivant dans Projects/Areas/
Resources. Les cinq temps GTD portent la lecture du triptyque : le substrat
est la **capture**, la couche méthodologique le **clarify** et l'**organize**,
l'ontologie rend le **review** possible, ce qui entre en V3 est ce sur quoi on
peut **engage**.

# Les exclusions qui empêchent le verdict dilué

Dépendances installées (`node_modules`…) ET sorties générées
(`graphify-out`, `graphify-burst`, `_exports`) : distiller une sortie revient
à distiller ce que le système a produit. Mesure sur `00_Jerry_Business_Pulse` :
107 265 fichiers → 5 232 sans `node_modules` → **4 766 dans `graphify-burst`**
→ ~466 documents réels. Sans exclusions, la porte expire ou son verdict est
une moyenne sur du remplissage. Le parcours élagage **à l'entrée du dossier**
(`os.scandir` en pile, jamais `rglob`) et le garde de jonction NTFS
(`FILE_ATTRIBUTE_REPARSE_POINT`, le même que [[cartographie-mesuree-v3]]).

# Usage

```bash
python ASpace_OS_V3/scripts/porte_argent.py --domaine 23_12WY_SNW            # simule
python ASpace_OS_V3/scripts/porte_argent.py --domaine 23_12WY_SNW --appliquer # écrit
```
