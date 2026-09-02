---
id: archives-echecs-payes-2026-03-08
titre: "Échecs déjà payés dans les sessions (mars–août 2026) — le passé révolu qui ne doit pas être rejoué"
seau: archives
okf_version: "0.2"
created: 2026-09-01
sources:
  - id: tranche-01
    resource: "50_Distillation/_partiels/tranche_01.analyse.md"
    title: "Tranche 1/10 — intentions 2026-03-08 → 2026-06-22"
  - id: tranche-02
    resource: "50_Distillation/_partiels/tranche_02.analyse.md"
    title: "Tranche 2/10 — intentions 2026-06-22 → 2026-07-10"
  - id: tranche-03
    resource: "50_Distillation/_partiels/tranche_03.analyse.md"
    title: "Tranche 3/10 — intentions 2026-07-10 → 2026-07-16"
  - id: tranche-04
    resource: "50_Distillation/_partiels/tranche_04.analyse.md"
    title: "Tranche 4/10 — intentions 2026-07-16 → 2026-07-20"
  - id: tranche-05
    resource: "50_Distillation/_partiels/tranche_05.analyse.md"
    title: "Tranche 5/10 — intentions 2026-07-20 → 2026-07-26"
  - id: tranche-06
    resource: "50_Distillation/_partiels/tranche_06.analyse.md"
    title: "Tranche 6/10 — intentions 2026-07-26 → 2026-08-02"
  - id: tranche-08
    resource: "50_Distillation/_partiels/tranche_08.analyse.md"
    title: "Tranche 8/10 — intentions 2026-08-05 → 2026-08-12"
  - id: tranche-09
    resource: "50_Distillation/_partiels/tranche_09.analyse.md"
    title: "Tranche 9/10 — intentions 2026-08-12 → 2026-08-20"
  - id: tranche-10
    resource: "50_Distillation/_partiels/tranche_10.analyse.md"
    title: "Tranche 10/10 — intentions 2026-08-20 → 2026-08-28"
  - id: substrat-sessions
    resource: "50_Distillation/_substrat/05_Sessions.jsonl"
    title: "Carte des sessions (2 325 lignes) — jamais les sessions brutes"
---

> **Niveau de confiance : partiel déclaré.** Les 10 analyses de tranches ont été
> lues en entier ; la carte `05_Sessions.jsonl` a été interrogée par motifs
> (grep), pas lue ligne à ligne. Les sessions brutes n'ont **jamais** été
> ouvertes (interdit METHODE.md). Chaque affirmation cite sa tranche ou un
> identifiant de session de la carte.

# Ce que les sessions disent du passé révolu

## 1. Les outils abandonnés

- **Antigravity / Gemini — abandoné le 2026-03-08.** La session
  `05_Sessions/codex/rollout-2026-03-08T18-15-21-019ccf84-ef77-7e31-9c1b-9db9f8d829e9.md`
  (carte, 19,8 Mo) porte le titre explicite : « j'abandonne definitivement le
  chat d'antigravity l'IDE de merde de Gemini ». Les tranches suivantes ne
  montrent plus d'usage actif d'Antigravity ; sa doctrine de mandat survit
  pourtant importée telle quelle dans `CLAUDE.md` (bloc « Doctrine
  opérationnelle — sync GEMINI.md, 2026-08-31 »). *(tranche_01 + session
  rollout-2026-03-08)*
- **Multica — la machine qui consommait sans produire.** Juillet : des
  « stubs » par dizaines (~45 sessions à ~70 mots « You were just created… »
  sur les 11-12 et 16 juillet — *tranche_03* ; ~26 chat assistants identiques
  le 08-03 — *tranche_07* ; 14× le même prompt le 08-02 — *tranche_06*).
  Crash sur compaction documenté par l'utilisateur : « Multica se crash dans
  les compaction de contexte, probablement qu'il ne possède pas 1M de fenêtre »
  — session `05_Sessions/claude/938ca6a9-a319-4d76-a30f-297cfafac767.md`
  (2026-07-17), corroborée par les dizaines de marqueurs « This session is
  being continued… » de la tranche 4. *(tranche_04, tranche_06, tranche_07)*

## 2. La boucle du rejeu — mesurée dans les sessions

Le fait le plus lourd du corpus : le système d'orchestration se relance au
lieu de travailler.

- **GARDE-FOU** : ~70 occurrences d'août (×18 le 08-10, ~35 le 08-17→08-19,
  ×~35 le 08-20, ~24 le 08-20/21/22 — *tranches 8, 9, 10*).
- **MODE FABLE** : ×~50 le seul 08-19 — *tranche_09*.
- **LES SEPT CADENCES** : ×~45 le 08-12 + ×28 le 08-13 — *tranches 8, 9*.
- Le 08-12 n'apporte que ~40-50 intentions uniques sur 250 ; les copies
  identiques rejouent le même brief (*tranche_09*).
- Coût direct : le 07-10, « j'ai crammé mon quota de 5h d'opus en 1 Super
  Execution » (*tranche_02*) ; sessions monstres de rejeu (112k et 133k mots
  le 06-25 pour le **même prompt** relancé — *tranche_02*).

**Interprétation (mienne, pas une mesure) :** le GARDE-FOU est réécrit parce
que la compaction garde les faits et perd l'autorisation ; le rejeu est le
symptôme, la perte de mandat la cause. A SOURCER : le lien causal n'est pas
établi par une session, il est reconstruit.

## 3. Les échecs d'infrastructure, datés

- **08-01, la nuit blanche perdue** : hook `stop.py` qui échoue en boucle
  (« Failed to spawn »), frustration brute documentée. Session
  `05_Sessions/claude/62a76f61-4924-4610-a00b-79c003586463.md`. *(tranche_06)*
- **08-09, Agent OS « fiasco complet »** : une session de 6 917 mots —
  l'outlier massif de la tranche — « mon Agent OS est un Fiasco complet lance
  le en Localhost » ; sessions `05_Sessions/claude/a33e5890-6c07-4c91-b933-218aabc123cd.md`
  et `05_Sessions/claude/agent-a7bdaa1bbc6378000.md`. *(tranche_08)*
- **Quota 429, stalls 600 s, retries** pendant le D7 FULL BURN du 07-27
  (phases 5 → 24.8, MEGA-AGENT par lots de 200 jusqu'à 16 500 vidéos,
  interruptions utilisateur répétées sur les phases 21a/21b). *(tranche_06)*
- **Bug d'instrument (encodage)** : `ITÉRATION` corrompu en `ITÃ‰RATION` dans
  les briefs WORKER WF1 — problème de génération des briefs, pas de lecture ;
  le prompt WF1 (448 mots) revient ~9× sur la semaine du 07-11→07-16. La
  session WF1 de 2026-07-06 (`05_Sessions/claude/1ee808e8-e6f3-4e36-b1e8-a9fe65dec50d.md`)
  en est un exemplaire. Lignes corrompues de la tranche 5 (mots déformés,
  lignes 43-44, 50, 88-92, 128-139) et une ligne gonflée à 69 537 mots pour un
  prompt de tick standard — l'instrument d'extraction lui-même a menti sur
  quelques lignes. *(tranches 2, 3, 5)*

## 4. Ce que ces échecs ont produit (positif)

- La nuit blanche du 08-01 a produit le diagnostic « mémoire éparpillée hors
  Geordi » et poussé la consolidation du 08-02. *(tranche_06)*
- Le crash Multica a directement motivé la fondation de la gouvernance du
  07-16 : Constitution Article 7 (réversibilité) + D6 anti-pollution, avec un
  REDO après un brief contradictoire « falsification ». *(tranche_03)*
- Le 08-23, après tout ça, la journée la plus structurée : audits exécutés en
  direct sans workflow, 8 relectures de concepts OKF. *(tranche_10)*

# Contradictions détectées

1. **V2 encore canon vs V3 fondée.** Toute la tranche 1 (mars–juin) pointe
   vers `ASpace_OS_V2` ; V3 n'est fondée que le 07-09 (*tranche_02*). Les
   documents d'avant juillet décrivent un monde qui n'existe plus — mais
   l'AGENTS.md du seau dit aussi que « V2 est la mémoire ». Ne pas trancher.
2. **Le 08-09, « fiasco complet » vs usage continu.** La tranche 8 enregistre
   l'échec d'Agent OS en localhost ; le bloc carte de `CLAUDE.md` décrit
   aujourd'hui `agent-os/desktop` fonctionnel (port 5555). L'échec du 08-09
   et l'état actuel coexistent sans document de réconciliation. A SOURCER.
3. **Autonomie réclamée vs rejeu massif.** Les tranches 3-4 notent « presque
   tout est du brief machine » (quasi aucune intention humaine) — l'orchestration
   a tourné seule ; c'est précisément ce « seul » qui a produit les ~45 stubs
   Multica et la boucle des cadences. L'autonomie désirée (D1) est à la fois
   le but et l'agent des échecs listés ici.
4. **Comptes de tranches non fiables.** La tranche 4 annonce 250 intentions
   mais contient ~440 puces ; la tranche 5 a des lignes corrompues. Les
   volumes cités ci-dessus (~45 stubs, ~70 GARDE-FOU) sont des ordres de
   grandeur extraits d'analyses qui admettent leurs propres défauts.
5. **Mojibake d'origine incertaine.** `ITÃ‰RATION` est attribué par la
   tranche 2 à la génération des briefs ; les lignes corrompues de la
   tranche 5 suggèrent une corruption en aval (extraction/capture). Deux
   instruments différents sont suspects ; rien ne les disculpe l'un ni
   l'autre.

# Couverture réelle

- Lus intégralement : `METHODE.md`, `archives/index.md`, les **10/10**
  analyses de tranches `_partiels/tranche_01..10.analyse.md`.
- Interrogée par motifs seulement : `05_Sessions.jsonl` (2 325 lignes de
  carte) — 5 greps, jamais de lecture complète.
- Non lus : les 12 284 fichiers de `04_Archives_Data/` eux-mêmes ; les
  sessions brutes (interdit). Les counts « ~45 stubs », « ~70 GARDE-FOU »
  viennent des analyses, qui s'appuient sur le rapport d'intentions V3
  (commit 311799c) — pas d'un recomptage indépendant.