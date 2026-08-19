# BRIEF — frameworks d'orchestration et mesure de decision

## Ton perimetre EXCLUSIF en ecriture

```
C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/frameworks/
C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_frameworks.md
```

Tu ne touches a rien d'autre. Quatre autres agents travaillent en parallele.

## Ce que tu evalues, et dans cet ordre

### 1. CEO-Bench — la priorite

`https://github.com/zlab-princeton/ceobench-src`
`https://ceobench.com/trajectory-viewer/`

C'est un banc d'essai ou des modeles dirigent une entreprise simulee sur
500 jours. Les trajectoires publiees montrent quelque chose de **plus utile
qu'un classement de capacite** :

| Modele | Resultat | Cout |
|---|---|---|
| Claude Opus 4.8 | survit 500 j, 1 511 actions | **2,40 M$** |
| Kimi K3 | survit 500 j, 2 213 actions | **22,15 M$** |
| Claude Fable 5 | survit 500 j, 818 actions, 6 129 subs | 12,67 M$ |
| GPT-5.6 Sol | **faillite a 190 j** | — |

Un modele peut survivre en depensant dix fois plus qu'un autre. **Ce banc
mesure l'efficacite de decision, pas la capacite** — et c'est exactement ce
qui manque a Business OS pour savoir si B1, B2 et B3 decident bien.

Ce qu'on attend de toi :

- **le protocole exact** : quelles metriques, quel horizon, quelles actions
  sont comptees, comment la faillite est declaree ;
- **ce qui est transposable a Business OS** et ce qui ne l'est pas. Une
  simulation d'entreprise generique n'est pas OMK ni Coach OS ;
- **un gabarit d'adaptation** : quelles metriques de CEO-Bench se mappent sur
  quels signaux de Business OS, et lesquelles n'ont pas d'equivalent — les
  absences comptent autant que les correspondances.

**N'invente aucune metrique.** Si le depot ne documente pas un point, ecris
que le depot ne le documente pas.

### 2. RecursiveMAS

`https://github.com/RecursiveMAS/RecursiveMAS`

Des agents qui echangent des **vecteurs latents** plutot que du texte, avec un
module de traduction leger (*Recursive Link*) entre architectures differentes.
Gain annonce : de 73 % a 87 % sur des problemes mathematiques, moins de jetons.

Ce qu'on attend :

- ce que le depot **demontre reellement** contre ce que la communication
  annonce ;
- **la contrepartie, qui est le point le plus important** : un echange en
  vecteurs latents est **opaque a la lecture humaine**. Tout ce poste repose
  sur des rapports lisibles, des sources verifiables et des contradictions
  nommees. Un canal qu'on ne peut pas relire supprime cette possibilite.
  Dis franchement ou ce compromis est acceptable et ou il ne l'est pas ;
- si un usage **partiel** a du sens : latent entre agents d'une meme escouade,
  texte aux frontieres ou un humain relit.

### 3. Les orchestrateurs legers

LangChain, LangGraph, CrewAI, AutoGen — et **l'option de ne rien ajouter**.

Le contexte reel, mesure : le poste a deja une boucle qui tourne
(`_loop/boucle.sh`), 7 agents rendus, 0 echec, une memoire partagee
(`ETAT.md`) qui compose d'un tour a l'autre.

**La decision arretee par le proprietaire du produit est le parallelisme natif
par extension de `boucle.sh`, pas LangChain.** Ton travail n'est donc pas de
choisir — c'est de dire **ce qu'on perd** en restant natif, pour que le choix
soit tenu en connaissance de cause. Si un framework apporte quelque chose
d'irremplacable, nomme-le precisement.

## Ce qu'on attend a chaque tour

3 a 6 concepts OKF v0.2 dans `frameworks/`, en `kebab-case.md`, sources
reelles.

Plus **une ligne ajoutee** a
`C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/ETAT.md` sous une section
`## Frameworks` que tu creeras si elle manque. **En ajout seul, jamais de
reecriture** — trois autres agents ecrivent dans ce fichier.

## Si tu n'as pas d'acces web

Dis-le **en tete de rapport**, et travaille sur ce que le poste contient. Un
protocole de banc d'essai decrit de memoire est un protocole faux, et il
contaminerait toutes les decisions qui s'appuieraient dessus.

## Ton rapport

`_loop/RAPPORT_frameworks.md` — avec une section `## Historique`, une ligne par
tour.

Applique l'etape 3 du mode Fable sans indulgence : **attaque ta propre
recommandation.** Si tu conclus « adopter X », cherche ce qui rendrait cette
adoption regrettable dans six mois, et ecris-le.
