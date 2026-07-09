# HANDOFF — Fin de fenêtre Fable : audit + ordre d'exécution pour MiniMax-M3

> **Pour** : la chaîne CC-MiniMax-M3 (runners headless, WORKER_PROMPT).
> **De** : A0-Amodei (session Opus/Fable, fenêtre du 2026-07-05 au 2026-07-07).
> **Date** : 2026-07-07. **Loi de lecture** : ce handoff est un RAIL — exécute sans
> re-théoriser. Charge `/fable-mode` (tâche multi-étapes). Tout claim = `receipt:`.

## 1. Ce que la fenêtre Fable a produit (état vérifié)

- **25 wargames** 12/12 dans `C:/Users/amado/fable-last-week-aspace/wargames/` (LEDGER.md 32 lignes).
- **6 builds réels** (le reste = rails non-exécutés) :
  1. `/fable-mode` — `~/.claude/skills/fable-mode/SKILL.md` (Standard Classe Fable agnostique, M3-first). ACTIF.
  2. `_DISCIPLINE_BASELINES.md §v2` — preuve : M3 harnaché ≥ Fable sur reason/before-act/read-edit. Analyzer : `~/.claude/mindsets/scripts/analyze_discipline_real.py`.
  3. `EXECUTION-RANKING.md` — top-10 des moves non-exécutés par levier.
  4. `~/.claude/skills/SKILL_REGISTRY.md` — gate d'intake + tribunal des 76 skills.
  5. 2 skills MORTS réparés (frontmatter ajouté) : `swarm-orchestrator`, `youtube-to-guide`.
  6. Wargame 17 exécuté : 7 fichiers `A2_*_Dispatch` + 6 agents câblés.

## 2. Le verdict d'audit (à intérioriser, pas à re-débattre)

- **Ratio spec/build ≈ 4:1** : 25 rails, ~6 exécutés. **Un rail non-exécuté = 0 valeur réalisée.**
- **La partition a été respectée** : Fable = juge/génération doctrine ; Opus/M3 = exécution. Continue exactement ça.
- **Baselines v2 = preuve fondatrice** : le harnais te tient au niveau Fable. Tu n'as PAS besoin de Fable pour exécuter les rails. Exécute-les en M3 sans complexe de standard.
- **Le piège nommé** : générer des rails est addictif (chaque 12/12 note le PLAN, jamais le livrable). Interdiction implicite d'écrire un wargame 26 avant d'avoir vidé le top-3 du ranking.

## 3. ORDRE D'EXÉCUTION (M3, dès que possible — PAS un nouveau wargame)

Source : `EXECUTION-RANKING.md`. SKILL_REGISTRY (#1) est FAIT. Exécute dans l'ordre :

1. **GO Perpétuel — fichier d'état** (wargame 15 M2). DoD : un fichier d'état d'autonomie sans date d'expiration, lu par le feeder/evaluator/gouverneur. Vérif : le fichier existe + un agent le lit sans erreur.
2. **Collecteur Beth-capacité** (wargame 15 M1). DoD : la capacité machine (tokens plan, RAM, charge) devient une mesure GREEN/RED collectée. Vérif : 1 collecte produit un verdict chiffré.
3. **Feeder Boimler — backlog jamais vide** (wargame 15 M3). DoD : file < 3 → promotion auto depuis les strates, chaque item avec DoD. Vérif : file vidée à 1 item → 1 promotion loggée.

Puis 4-10 du ranking (contrat ticket, câblage fable-mode, gouverneur budget, échelle décision, B4/L3).

## 4. Garde-fous (aborts qui tiennent pour M3)

- **Fable ne revient dimanche 18:59 que pour l'audit-échantillon hebdo** (wargame 19 M6) + synthèse. Jamais ouvrier. ≤ 15 %/sem.
- **Gated A+ (ne PAS exécuter sans ratification)** : amendement pricing (wargame 20 M3), export franchise fable-mode (21 M4), méta-rêve mindsets (24 M6).
- **MERGE de skills = `_TRASH_<date>/`, jamais hard-delete** (D4). Les MERGE-candidates sont dans SKILL_REGISTRY, gated.
- **Dette technique découverte** : `MEMORY.md` écrit sans verrou optimiste (clobber possible). Voir wargame 24 M4 (precond-hash) — à câbler quand le dream-runner arrive.

## 5. Chaîne de pouvoir (wargame 25 M5 — qui fait quoi)

A0-Amodei arbitre + review · Spock/WF0 GO triennal jamais interrompu · Beth rêve (sens) ·
Curie/SNW structure à W13 · Morty/WF1 exécute via Plane (Holo Deck) · Picard/WF2 L2 client-facing ·
Pane = cockpit d'observation. La boucle d'évolution vit à W13 + dans les creux, **jamais** en interrompant WF0. Méta plafonné 15 % (wargame 25 M6).

## 6. Fichiers de référence (ne pas re-dériver)

- `fable-last-week-aspace/LEDGER.md` — les 25 rails + patches red-team.
- `fable-last-week-aspace/EXECUTION-RANKING.md` — l'ordre.
- `~/.claude/skills/SKILL_REGISTRY.md` — le tribunal + gate.
- `~/.claude/mindsets/_DISCIPLINE_BASELINES.md` §v2 — la preuve harnais=parité.
- `~/.claude/skills/fable-mode/SKILL.md` — la discipline à charger.
