# BRIEF — Distillation Life OS (A1 / A2 / A3)

> **Statut : prêt à lancer, bloqué sur quota.** Le canal M3 rend
> `429 · Token Plan usage limit has been reached` (mesuré 2026-08-20).
> Ce brief part dès que le plan MiniMax est rechargé.

## Le besoin, en un chiffre

La couche qui doit piloter les vagues de Sprint Life OS **n'existe presque pas
dans le graphe**.

| couche | fichiers qui la mentionnent | assertions où elle est **sujet** |
|---|---|---|
| A0 Amadeus | 170 | 18 |
| A1 Morty (Watcher) | 121 | **4** |
| A2 vaisseaux | 117 | 24 |
| **A3 conseils** | **140** | **2** |

C'est exactement la pathologie déjà confirmée sur Summer : **narrée partout,
prédiquée nulle part**. A3 porte les cycles 12WY trimestriels et l'escalade de
revue ; il dispose de **deux** assertions dans tout le corpus.

Et A0, qui doit **sortir** de la boucle de revue, en a 18 — neuf fois plus que
la couche censée le remplacer. Le graphe dit aujourd'hui le contraire de la
cible.

## La matière existe, et elle est nommée

`ASpace_OS_V2/.../05_From_V2_Domains/20_Life_OS/` — **159 fichiers `.md`**.
Les noms de dossiers portent déjà l'appariement vaisseau ↔ framework :

| dossier V2 | md | couche | ce qu'il porte |
|---|---|---|---|
| `00_Gatekeepers_Beth_Morty/` | 7 | **A1** | Beth (origin ontology) et Morty (Watcher, gatekeeper de complexité) |
| `21_Ikigai_Orville/` | 24 | A2 | Orville ↔ Ikigai |
| `22_Wheel_Discovery/` | **78** | A2 | Discovery ↔ Life Wheel — **le plus gros gisement** |
| `23_12WY_SNW/` | 16 | **A3** | SNW ↔ 12 Week Year — **la cadence trimestrielle** |
| `25_GTD_Cerritos/` | 13 | A2 | Cerritos ↔ GTD |
| `26_DEAL_Protostar/` | 11 | A2 | Protostar ↔ D.E.A.L. |
| `27_Cognition_LD04/` | 1 | A2 | LD04 ↔ Cognition (quasi vide — à dire, pas à combler) |
| `28_Blueprints/` | **0** | — | **vide**. Ne pas inventer son contenu. |

Ce que je n'ai **pas** : le mandat de chaque conseil A3, la règle d'escalade
A3→A2→A1, et le critère qui fait qu'une vague Life OS est acceptée. Ils sont
peut-être dans `23_12WY_SNW/`, ce sera à mesurer, pas à supposer.

## La cadence à encoder (dictée par le propriétaire, 2026-08-19)

```
5 Scrums   (B3, quotidien)   = 1 Sprint
4 Sprints  (B2, hebdomadaire)= 1 Rock
3 Rocks    (B1, mensuel)     = 1 Cycle 12WY   -> conseils A3, trimestriel
4 Cycles   12WY              = 1 année civile -> vaisseaux A2, garde annuelle
```

Escalade de revue : **A3 → A2 → A1 → le propriétaire**. A0 sort de la boucle.

## L'asymétrie temporelle — la contrainte qui structure tout

**Business OS (L2) est comprimé. Life OS (L1) ne l'est pas.**

En V0.3, si une vague de Scrum s'exécute en moins d'1 h machine, alors
1 Sprint ≈ 4-5 h et 1 Rock < 24 h — un trimestre de travail civil en moins
d'une semaine.

**Les vagues Life OS restent en temps non comprimé**, délibérément : c'est ce
qui préserve l'observabilité du multivers de possibilités. Comprimer les deux
couches rendrait l'arbitrage humain inauditable — on ne verrait plus *pourquoi*
une branche a été retenue, seulement qu'elle l'a été.

Cette règle doit apparaître comme une **assertion du graphe**, pas comme une
note de bas de page.

## Périmètre exclusif

**Lecture seule** : `05_From_V2_Domains/20_Life_OS/**` (159 md).

**Écriture autorisée, et nulle part ailleurs** :
- `50_Distillation/life/` — concepts OKF, un par objet distillé
- `70_Onthologies/triplets/life-a1.jsonl`, `life-a2.jsonl`, `life-a3.jsonl`
- `60_Implementation_Méthodologiques/life-cadences/`

Un agent par couche. **Trois agents, trois fichiers de triplets distincts** :
deux agents qui écrivent le même `.jsonl` se réécrivent sans le voir.

## Interdits

- Inventer le contenu de `28_Blueprints/` (0 fichier) ou gonfler
  `27_Cognition_LD04/` (1 fichier). **Déclarer le vide est le livrable.**
- Une assertion sans `source` pointant un fichier réel — le validateur la
  refuse, et une source inventée est pire qu'une source absente.
- Toucher à `70_Onthologies/pulse/**` : ces 37 concepts portent désormais un
  verdict humain V0. Les réécrire effacerait la seule revue existante.
- Reproduire la faute Areas/Projets : **toute assertion qui donne du poids à
  une couche doit avoir son pendant sur la couche qu'elle gouverne.** A3 sans
  ses Rocks, c'est Jerry sans ses Projets.

## Artefact obligatoire

Par agent, un `RAPPORT_<couche>.md` déclarant : fichiers réellement lus /
total, ce qui n'a pas été couvert et pourquoi, les contradictions refusées
d'être tranchées. **C'est la source la plus rentable pour la revue suivante**,
parce qu'elle contient les aveux.

## Critère d'acceptation

`python scripts/valider_triplets_aspace.py life` passe, et A3 sort avec
**au moins autant d'assertions sujet que A0**. En dessous, la couche censée
remplacer A0 dans la boucle de revue ne le peut pas.
