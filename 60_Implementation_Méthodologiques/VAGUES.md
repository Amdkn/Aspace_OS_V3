---
type: Playbook
title: Les vagues d'orchestration, et le rituel D.E.A.L. entre chacune
description: Vague 1 en rotation à cinq agents, Vague 2 en parallélisme natif par domaine, et entre les deux un passage obligé — définir, éliminer, automatiser, libérer.
tags: [orchestration, vagues, deal, 12wy, ceo-bench, recursivemas, business-os]
generated: { by: claude-opus-5, at: 2026-08-18T02:20:00Z }
verified:
  - { by: human:amdkn, at: 2026-08-18T02:15:00Z }
sources:
  - id: decision
    resource: "arbitrage utilisateur — parallélisme natif plutôt que LangChain, D.E.A.L. entre chaque vague, supervision CEO-Bench"
    author: human:amdkn
    last_modified: 2026-08-18
  - id: boucle
    resource: 60_Implementation_Méthodologiques/_loop/boucle.sh
    title: La boucle de Vague 1
    last_modified: 2026-08-18
  - id: ceobench
    resource: https://github.com/zlab-princeton/ceobench-src
    title: CEO-Bench — banc d'essai de direction d'entreprise
    last_modified: 2026-08-18
  - id: recursivemas
    resource: https://github.com/RecursiveMAS/RecursiveMAS
    title: RecursiveMAS — échange de vecteurs latents entre agents
    last_modified: 2026-08-18
okf_version: "0.2"
---

> **Niveau de confiance : revu par un humain.** Le découpage en vagues, le refus
> de LangChain et le rituel D.E.A.L. sont des décisions du propriétaire du
> produit, pas des conclusions d'analyse.

# Vague 1 — en cours

Cinq agents en rotation, deux en parallèle au maximum.

| Agent | Étage | Question directrice |
|---|---|---|
| `b1` | direction | qu'est-ce qui se décide ici, et qu'est-ce qui **ne** s'y décide **pas** ? |
| `b2` | coordination | quand deux domaines veulent la même ressource, qui tranche ? |
| `b3` | exécution | qu'est-ce qu'un paquet de travail bien formé ? |
| `protocoles` | MCP, A2A, AG-UI, ACP, UCP | quelle couche, quel transport, quel risque |
| `frameworks` | CEO-Bench, RecursiveMAS, orchestrateurs | que perd-on à rester natif ? |

Rotation sur dix paires, équilibrée : `b1` 5, `b3` 5, `b2` 4, `protocoles` 3,
`frameworks` 3. La première version en servait `b3` une fois sur trois — un
déséquilibre de la table, pas des agents.

**Ce que Vague 1 doit produire pour que Vague 2 existe** : la conception du
parallélisme par domaine. Tant que B2 n'a pas posé la règle d'arbitrage entre
domaines, huit escouades en parallèle se marcheraient dessus.

# Entre chaque vague — le rituel D.E.A.L.

**Passage obligé.** Aucune vague ne démarre sans que la précédente ait été
passée aux quatre gestes, dans cet ordre. L'ordre compte : automatiser avant
d'éliminer fige le gaspillage au lieu de le supprimer.

## Définition

Qu'est-ce que la vague a réellement produit ? Compté, pas estimé — nombre de
concepts, de triplets, de tours, d'échecs.

Et **qu'est-ce qu'elle devait produire et n'a pas produit ?** Cette question-là
est la plus utile, et c'est celle qu'on saute.

## Élimination

Qu'est-ce qui a tourné **sans rien produire** ? Un agent servi cinq fois qui
rend trois concepts ne mérite pas cinq tours. Un brief qui génère du remplissage
se coupe avant de s'optimiser.

**La règle du poste s'applique : trois occurrences avant d'automatiser, cinq
avant que ça rembourse.** En dessous de trois, ce n'est pas un motif, c'est une
occurrence.

## Automatisation

Ce qui reste après élimination, et **seulement** ce qui reste, se script.
Chaque geste répété trois fois dans la vague devient une ligne de `boucle.sh`
ou un script de `scripts/`.

## Libération

Qu'est-ce que cette vague permet d'arrêter de surveiller ? La mesure de succès
n'est pas « on produit plus » mais **« on regarde moins »**.

Le test est physique, et il est emprunté à l'échelle d'autonomie : lancer la
vague, fermer l'écran, partir deux heures. Si l'idée est insupportable, la
boucle de vérification n'est pas finie.

# Compression temporelle — 12WY en heures machine

Les 12 semaines deviennent des **sprints d'heures machine**. Un cycle 12WY
humain se joue en une session de boucle : ce qui prenait douze semaines de
calendrier tient dans une échéance de cinq heures.

**Ce que la compression ne change pas** : le nombre de décisions humaines. Un
sprint machine qui produit quarante concepts vous laisse toujours les mêmes
arbitrages à trancher. La compression accélère la production, pas la décision —
et c'est la décision qui reste le goulot.

# Vague 2 — conçue, pas lancée

## Parallélisme natif par domaine

**Huit escouades, une par domaine Business**, plutôt que deux agents en
rotation. En étendant `boucle.sh`, **pas** en ajoutant LangChain.

Raison du refus, à tenir en connaissance de cause : la boucle actuelle marche —
sept agents rendus, zéro échec, une mémoire partagée qui compose d'un tour à
l'autre. LangChain ajouterait une couche Python entre le poste et `claude -p`,
avec sa propre instabilité, pour un gain qui se code en une extension de tableau
bash.

**Ce que ce refus coûte** est le travail de l'agent `frameworks` : le nommer
précisément, pour que le choix reste révocable.

## Supervision par CEO-Bench

CEO-Bench mesure l'**efficacité de décision**, pas la capacité. Les trajectoires
publiées le montrent : un modèle survit 500 jours à 2,40 M$ quand un autre y
met 22,15 M$ pour le même résultat.

C'est précisément ce qui manque à Business OS : savoir si B1, B2 et B3 décident
**bien**, pas seulement s'ils produisent. Le gabarit d'adaptation — quelles
métriques se mappent sur quels signaux — est attendu de l'agent `frameworks`.

## RecursiveMAS — sous condition

Échange de vecteurs latents entre agents d'une même escouade, texte aux
frontières.

**La condition n'est pas négociable** : tout ce poste repose sur des rapports
lisibles, des sources vérifiables et des contradictions nommées. Un canal qu'on
ne peut pas relire supprime la possibilité même de vérifier.

L'usage acceptable est donc **intra-escouade seulement** — là où la sortie est
de toute façon revue à la frontière par un humain ou par un agent relecteur. Un
échange latent entre B1 et B2 rendrait l'arbitrage inauditable, et l'arbitrage
est exactement ce qu'on veut pouvoir relire.

# L'ordre, et pourquoi il ne se contourne pas

```
Vague 1  →  D.E.A.L.  →  conception Vague 2  →  D.E.A.L.  →  Vague 2
```

Lancer huit escouades avant que B2 ait posé la règle d'arbitrage, c'est
reproduire à huit le silo qu'on a mis une passe entière à réparer sur quatre
bundles. Le cloisonnement protège de l'écrasement et coûte la connectivité :
c'est mesuré, pas supposé.
