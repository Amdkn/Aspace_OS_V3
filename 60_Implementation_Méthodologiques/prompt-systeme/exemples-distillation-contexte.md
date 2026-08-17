---
type: Concept
title: Exemples — la distillation en contexte
description: Section 6 du prompt système : des paires « voici comment on communique » / « voici comment on ne communique pas », tirées de vraies réponses récentes et nettoyées à la main.
tags: [prompt-systeme, exemples, distillation, few-shot]
generated: { by: minimax-m3, at: 2026-08-17T22:25:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T22:25:00Z }
sources:
  - id: indydevdan-extraction
    resource: 60_Implementation_Méthodologiques/_sources/indydevdan-prompt-systeme.md
    title: "IndyDevDan — extraction"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Le principe

IndyDevDan : *« Des paires *voici comment on communique* / *voici comment on
ne communique pas*, avec de vraies réponses. »* L'astuce avancée : prendre
une réponse d'un autre modèle qu'on trouve bonne, la nettoyer à la main, et
la poser en exemple. C'est la distillation en contexte — technique
antérieure à GPT-4 et qui continue de fonctionner.

L'effet est plus fort qu'une consigne : un agent qui voit dix exemples
 produit une réponse qui ressemble aux dix ; un agent qui voit dix consignes
 produit une réponse qui essaie de toutes les respecter.

# L'écart mesuré

Le canon du poste ne contient **aucun exemple**. Les consignes sont
purement déclaratives. Conséquence vérifiable : un agent qui découvre le
canon peut appliquer les règles au pied de la lettre et produire un texte
qui n'a pas le ton attendu — parce que le ton n'est jamais montr é, seulement
prescrit.

L'écart est d'autant plus grand que le poste dispose déjà de la matière
première : les **bonnes réponses** de la session, et les **mauvaises**
aussi. Les deux sont dans le journal — la première version du brief,
la dernière passe, l'aller-retour avec l'utilisateur. Personne ne les a
extraites, nettoyées, et posées en exemple.

# Les paires à poser dans le canon

Trois paires, choisies sur la variété des tons et la fréquence des
occurrences :

### Paire 1 — L'énoncé de règle

**À éviter :**
> *« Il est important de noter que les agents ne doivent pas faire de
> modifications dans des fichiers qui ne sont pas dans leur périmètre. Cela
> pourrait entraîner des conflits avec d'autres agents qui travaillent en
> parallèle. »*

**À reproduire :**
> *« Tu écris uniquement dans les fichiers nommés par le brief. Un fichier
> hors liste est intouchable, même pour corriger une typo. »*

Différence : la première paraphrase la règle en trois phrases molles ; la
seconde pose la règle en une phrase, durcie par un cas (« même pour
corriger une typo »).

### Paire 2 — Le rapport de fin de tâche

**À éviter :**
> *« J'ai donc créé trois concepts dans le bundle prompt-systeme, et j'ai
> également mis à jour les fichiers index.md. N'hésitez pas à me faire part
> de vos remarques ou si vous souhaitez des modifications. »*

**À reproduire :**
> *« 3 concepts écrits dans `prompt-systeme/`. Index mis à jour. Rapport
> dans `_briefs/RAPPORT_methodes.md`. Non couvert : néant. »*

Différence : la première redit ce qui a été fait, en prose, avec une
euphorie de fin ; la seconde est une table de livraison, sans narration.

### Paire 3 — La réponse à une question piège

**À éviter :**
> *« C'est une excellente question ! Vous avez tout à fait raison de
> souligner que ce point mérite attention. Voici quelques éléments de
> réponse : ... »*

**À reproduire :**
> *« Couverture partielle : OKF v0.2 est documenté dans deux endroits
> (`40_Memory_Wiki_OKF/OKF.md` et `30_MEMORY_CORE/...`), avec divergences
> sur le format de `verified`. Je n'ai pas arbitré — voir
> `RAPPORT_methodes.md`, section contradictions. »*

Différence : la première dérive vers la flatterie et perd le signal ; la
seconde donne la réponse utile et nomme ses limites.

# Le geste

Ajouter au canon une section **« Exemples »** avec les trois paires
ci-dessus. Les paires sont tirées d'**observations** récentes ; chaque
exemple cite sa date d'observation dans le frontmatter et son fichier
source si pertinent.

**Entretien** : à chaque nouvelle observation d'un bon ou mauvais ton,
ajouter une paire — et barrer la paire obsolète. La section reste
circonscrite à un plafond de 8-10 paires, sinon elle devient un corpus
qu'aucun agent ne lit en entier.

Vérifiable : confronter une réponse d'agent récente aux trois paires. Si
elle ne ressemble à aucune des trois positives, soit les exemples sont
insuffisants, soit l'agent ne les a pas lus.

# Pourquoi pas plus d'exemples

Au-delà de 8-10 paires, la loi des rendements décroissants s'installe :
l'agent cesse de saisir un **ton** et commence à mémoriser des **cas**.
Distiller, c'est réduire — la section Exemples doit rester plus courte
que la section Bornes, sinon elle a pris la place de la règle.
