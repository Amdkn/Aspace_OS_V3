---
type: Concept
title: Patterns positifs et négatifs — ce qu'on reproduit, ce qu'on évite
description: Section 2 du prompt système appliquée à ce poste : deux listes explicites posées une fois, qui évitent de répéter à chaque brief le ton et les tics à proscrire.
tags: [prompt-systeme, patterns, ton, tics]
generated: { by: minimax-m3, at: 2026-08-17T22:05:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T22:05:00Z }
sources:
  - id: indydevdan-extraction
    resource: 60_Implementation_Méthodologiques/_sources/indydevdan-prompt-systeme.md
    title: "IndyDevDan — extraction"
    last_modified: 2026-08-17
  - id: canon-poste
    resource: C:/Users/amado/CLAUDE.md
    title: "Canon du poste — racine du profil"
    last_modified: 2026-08-15
okf_version: "0.2"
---

# Le principe

IndyDevDan : *« Deux listes explicites : reproduis ceci, évite cela. »* La
liste positive sert de cible, la liste négative sert de garde-fou contre les
tics du modèle. Les deux ensemble valent plus que la somme — un agent qui
n'a que les positifs imite le ton, un agent qui n'a que les négatifs finit
par produire un texte frileux.

Les positifs visent le *quoi* et le *comment* ; les négatifs visent les *tics*
— les formules que le modèle produit sans y être invité, et qui font baisser
la qualité d'une réponse sans qu'un lecteur les pointe nominativement.

# L'écart mesuré

Le canon du poste contient bien des **interdits** dispersés
(« pas d'emojis sauf demande », « pas de tirets cadratins abusifs »), mais
**aucune liste de positifs**. Conséquence : un agent qui découvre le canon
sait ce qu'il ne doit pas faire, pas ce qu'il doit viser. Il produit un texte
qui évite les fautes, pas un texte qui ressemble à ce poste.

L'écart est asymétrique : les négatifs sont couverts à 60-70 % (règles
dispersées), les positifs à 0 %. C'est le déficit structurel.

# Les positifs à poser dans le canon

Issus des deux fichiers `_sources/`, filtrés sur ce qui s'applique ici :

1. **La règle du canon ouvre sur son piège.** Une règle sans son pourquoi
   raconte une prohibition, pas une raison — voir `purpose-et-pourquoi.md`.
2. **Une vérification visuelle ou mesurée** termine chaque concept qui touche
   à l'interface ou à la performance. Pas de « ça devrait marcher ». La
   phrase qui oblige : *« montrez la capture »*, *« montrez le compteur »*.
3. **Un concept sans source** est une invention. Préférer une couverture
   partielle déclarée à une couverture totale prétendue.
4. **Le lecteur peut couper le courant en une phrase.** Une réponse d'agent
   qui ne se comprend pas au premier paragraphe n'est pas écrite.
5. **Écrire en français.** Le poste est francophone. Les termes techniques
   anglais restent en anglais quand ils n'ont pas d'équivalent stable.
6. **Citer le chemin, pas le nom.** « `50_Distillation/.../index.md` » plutôt
   que « le fichier » ou « l'index ». Un chemin est vérifiable, un nom ne
   l'est pas.

# Les négatifs à poser dans le canon

Tics observés dans les réponses récentes :

- les formulations de remplissage : *« certainly »*, *« worth noting »*,
  *« loadbearing »*, *« here's the honest truth »* ;
- les **tirets cadratins** employés pour aérer au lieu de points — un tiret
  paragraphe remplace une phrase, et la perd ;
- les **listes à puces** là où une phrase suffit — un découpage en puces
  aplatit une hiérarchie d'arguments ;
- les **résumés de ce qui vient d'être fait** (« j'ai donc créé trois
  fichiers ») — la table des changements suffit, si elle est nécessaire ;
- les **euphories de fin** (« n'hésitez pas à me solliciter ») ;
- les **emojis** autres que ceux de l'utilisateur, jamais.

# Le geste

Ajouter au canon une section explicite **« Patterns »**, après la table des
matières et avant les pièges. Format : deux listes à puces, gardes-fous
positifs puis négatifs, une ligne par entrée. La liste négative doit
explicitement citer les tics observés — un agent auquel on dit *« pas de
formules de remplissage »* obéit moins bien qu'un agent auquel on liste
les formules.

Vérifiable : ouvrir n'importe quelle réponse d'agent récente, compter les
occurrences des tics listés, et viser zéro. Une seule occurrence révélée
par le comptage = la liste est incomplète, pas l'agent fautif.

# Pourquoi cette section n'est pas déjà en place

Les positifs sont plus difficiles à poser que les négatifs : un négatif est
une faute à éviter, un positif est un ton à imiter. Imposer un ton demande
de l'avoir soi-même, et cet exercice n'a pas été fait dans le canon. La
liste ci-dessus est une première distillation — elle gagne à être contestée
et affinée session après session.
