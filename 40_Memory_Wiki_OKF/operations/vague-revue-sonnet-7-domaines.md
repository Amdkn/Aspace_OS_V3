---
type: Playbook
title: Vague de revue Sonnet 5 — 230 concepts, 7 domaines, et ce qu'elle a trouvé
description: Sept domaines relus intégralement par des sous-agents Sonnet 5 ; la synthèse externe attribuait au corpus des affirmations qu'il ne contient pas.
tags: [revue, okf, sonnet, sous-agents, verification, notebooklm, confiance, 8-domaines]
generated: { by: "claude-opus-5", at: "2026-08-22T22:00:00Z" }
verified:
  - { by: "claude-opus-5", at: "2026-08-22T22:00:00Z" }
  - { by: "process:revue-sonnet-5", at: "2026-08-22T22:00:00Z" }
sources:
  - id: rendus-revue
    resource: "ASpace_OS_V3/70_Onthologies/_revue/REVUE_70_Onthologies-pulse-domaines-*.md"
    title: "Sept fichiers de revue, 230 concepts couverts"
    last_modified: 2026-08-22
  - id: corpus-domaines
    resource: "ASpace_OS_V3/70_Onthologies/pulse/domaines/"
    title: "Les 8 domaines, 258 concepts"
    last_modified: 2026-08-22
okf_version: "0.2"
---

# Vague de revue Sonnet 5 — 7 domaines

## Le résultat brut

Sept sous-agents Sonnet 5, un par domaine, périmètre exclusif, lancés depuis la
session. **Couverture intégrale sur les sept** — aucun rendu partiel.

| Domaine | Couverture | accepter | réserver | rejeter | Tokens |
|---|---|---|---|---|---|
| batman | 33/33 | 5 | 28 | 0 | 279 k |
| cyborg | 30/30 | 11 | 16 | 3 | 299 k |
| flash | 35/35 | 1 | 32 | 2 | 333 k |
| green-lantern | 35/35 | 4 | 29 | 2 | 316 k |
| john-jones | 30/30 | 3 | 25 | 2 | 290 k |
| superman | 32/32 | 6 | 23 | 3 | 299 k |
| wonder-woman | 35/35 | 23 | 11 | 1 | 330 k |
| **Total** | **230/230** | **53** | **164** | **13** | **2,15 M** |

Coût mesuré : **7 points de forfait Pro hebdomadaire pour 98 concepts**, soit
environ 9,3 k tokens par concept. Onze minutes de mur pour trois agents en
parallèle.

## La trouvaille principale : la synthèse externe surinterprète le corpus

Quatre affirmations restituées par NotebookLM comme des faits établis ont été
soumises aux agents pour vérification. **Aucune ne tient au niveau annoncé.**

**Le barème d'affiliation 50 $ / 150 $ / 250 $ n'existe pas.** Verdict
wonder-woman après lecture des 35 fichiers :

> *« **Aucune occurrence.** […] La synthèse externe qui attribue ce barème à ce
> domaine ne trouve aucun support dans le corpus. »*

Les seuls chiffres monétaires du corpus sont des seuils de remise, des
concentrations fournisseur, des coûts SaaS et des exemples de deals. Un barème
précis sans origine traçable est le type d'affirmation le plus dangereux :
il inspire confiance sans la mériter.

**`NON_FORCED` (Sales) est reconstruit, pas sourcé.** Le nom capitalisé
n'apparaît qu'au tour 5, comme *proposition* non adoptée. Et le corpus se
prémunit lui-même contre l'amalgame :

> *« Ne pas ajouter `SALES_DORMANT` comme 4ᵉ gate. C'est un mimétisme Aquaman. »*

**Les trajectoires de Green Lantern sont l'œuvre d'un seul auteur.** Verdict :

> *« Des reconstructions d'un seul auteur (MiniMax-M3), présentées par lui-même
> comme non-canoniques. […] Si la synthèse externe présente ces deux points
> comme des faits établis du corpus, **c'est une sur-lecture**. »*

**La squad Thunderbolts n'a aucune preuve d'exécution.** Tout son matériel
opérationnel est *projeté par symétrie* avec d'autres squads, jamais observé :

> *« Le corpus documente abondamment ce que devrait faire Thunderbolts sans
> jamais établir qu'elle a déjà fait quoi que ce soit. »*

Ce qui recoupe la mesure du runtime : zéro agent B3 Thunderbolts, jamais.

**La règle qui en sort** : la doctrine des domaines dormants dit que *« seul
Legal a un triplet dormant explicite »*. Toute trajectoire d'un autre domaine
présentée avec le même degré de certitude est une extrapolation. Un outil de
synthèse aplatit les niveaux de confiance — c'est sa fonction, pas son défaut.
Le niveau se rétablit en relisant la source, jamais en relisant la synthèse.

## Trois trous structurels trouvés en passant

**Deux formats de triplets coexistent.** Les concepts citent
`triplets/v3-business.jsonl` (JSON Lines) ; le graphe mesuré vit dans
`triplets/*.ttl` (Turtle). La distillation n'en lit qu'un. Détail dans
[[couche-b-absente-du-runtime]].

**Deux domaines revendiquent le numéro 01.** Le dossier de Green Lantern est
`01_RH_Meta_Gouvernance_GreenLantern_XMen`, tandis que
`eight-domain-avengers-wheel.md` pose « Superman = 01 Growth ». Le corpus traite
abondamment la collision de *nom* (People & Brand vs Growth) et **ignore
complètement** la collision de *numéro*.

**L'alias `J'onn J'onzz` est absent des 30 concepts Sales.** Le capitaine y est
nommé *Martian Manhunter* (legacy) et *JohnJones* (canon W40 V4). Une recherche
par l'alias le plus reconnaissable du personnage rend un faux négatif total sur
un domaine entier qui lui est consacré.

## Anti-pièges de la vague elle-même

**Compter les verdicts avec `reserver` sans accent en manque la totalité.** Les
tableaux écrivent **« réserver »**. Un filtre naïf a rendu 0 sur des fichiers
qui en portaient 28.

**Un rendu à forte proportion d'`accepter` mérite un second regard.** Six
domaines sur sept tournent entre 1 et 11 `accepter` pour 16 à 32 `réserver`.
wonder-woman rend **23 `accepter` pour 11 `réserver`** — inversion nette du
rapport. Le brief prévient qu'un « accepter » de complaisance fait passer une
affirmation non vérifiée pour une décision du propriétaire. Ce domaine est
celui à relire en premier.

**Un agent qui déclare ses propres limites vaut mieux qu'un agent sûr de lui.**
green-lantern a signalé que plusieurs de ses verdicts s'appuient sur des
concepts hors de son périmètre qu'il n'avait pas le droit de lire, et
« resteraient à confirmer ». C'est le garde-fou qui fonctionne.

## Ce qui reste

Les 230 concepts sont **relus par machine, pas par un humain**. Aucun `verified`
n'a été touché, aucun tampon apposé — c'est le verrou qu'aucun script ne peut
poser à la place de l'utilisateur. Les sept fichiers de revue sont des
**propositions** ; l'arbitrage reste entier.

Restent hors de cette vague : les 11 lots de `50_Distillation` et
`60_Implementation_Méthodologiques` du fichier `LOTS_REVUE.txt`, soit 128
concepts jamais relus.
