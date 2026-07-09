# WARGAME 19 — La chaîne de délégation : exécutions à CC-MiniMax-M3, tenues au Standard Classe Fable 5

> ⚡ÉVOLUTION 2026-07-08 (wargame 27 M4) — LOI ANTI-FOSSILE ajoutée au contrat de rail (M2) : un ticket/wargame n'écrit JAMAIS une constante temporelle en dur (GO, date, facteur de compression, compte de banque) — il **cite** [TEMPORAL-CANON](../TEMPORAL-CANON.md) (`GO: voir TC §GO`). Les claims de finalité (« close », « complet », « N/N ») sont **interdits de rail** — remplacés par « gradué à la date X ». Les nombres sont des POINTEURS, pas des valeurs.

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Exécuteur : la chaîne elle-même (runners CC-M3 headless). Mission : industrialiser la thèse « Fable's last week » — **Fable pense (wargames, doctrine, audit), M3 exécute (99 % des itérations, plan 5,1 B tokens), et le STANDARD ne vient pas du modèle mais du harnais** : gates mimétiques + evaluator + D1 receipts. Un M3 harnaché doit produire du travail indistinguable du standard Fable — c'est mesurable, donc on le mesure.

## Statut recon (D1 — receipts de CETTE session, cités)

| Fait | Preuve |
|---|---|
| La chaîne tourne déjà en v0 | `[wf1-morty] SHIP table-WK-WK04` iter 3 (worklog 12:42Z), singleton prouvé, 6 bugs purgés (wargame 12) |
| L'écart M3↔Fable est chiffré | `_DISCIPLINE_BASELINES.md` : reason 53→88 · re-eval 50→87 · reasoning 51→82 · **real-test 33→63** (14 148 beats M3 vs 913 Fable) |
| Le harnais de discipline existe | 17 fichiers dispatch (6 A2 + 8 B2 + A1) + gates mimétiques dans chacun (wargame 17 exécuté) |
| La banque de rails = 18 wargames 12/12 | LEDGER.md — chaque rail exécutable blind par un mid-tier |
| Routage modèle : D6 ×2 CE jour | Agent tool alias `haiku` → « MiniMax-M3… may not exist » ; WebFetch small-slot → même refus. **La chaîne M3 vit dans les sessions CLI CC-M3 (`claude -p` headless), PAS dans l'Agent tool de cette session desktop** |
| Fable = ressource rare | 73 % utilisés, reset dim. 19:00 — wargames 17-18 ont coûté 1-2 % chacun en mode économie |

## MOVES

### M1 — La partition des classes (qui pense, qui exécute)
| Classe | Tâches | Budget |
|---|---|---|
| **Fable 5** (rare, cher) | wargames neufs · doctrine/ADR · **audit-échantillon hebdo de l'evaluator** (M6) | ≤ 15 %/sem du quota |
| **CC-M3** (5,1 B/mois) | TOUTES les itérations : workers WF1/W×, sweeps (b1-filter E2 : 453), distillation bulk (93 guides), collectors, sims | gouverneur wargame 15 M5 |
| **Hermes/Codex-M3** | harness de débord (parallélisme multi-harness, wargame 13 M5 queue) | idem |
- **Attendu** : plus aucune itération d'exécution sur Fable ; plus aucun wargame écrit par M3 nu.
- **Échec probable** : la frontière fuit (« juste ce petit wargame en M3 ») → **contre-action** : un wargame produit par M3 porte `needs-fable-polish` et passe l'audit M6 AVANT d'entrer en banque.

### M2 — Le contrat de délégation (jamais un prompt vague)
Toute délégation = un TICKET au format rail : contexte 3 lignes · moves avec forks · abort conditions · DoD Una · verification runs avec « pass » épelé. Source : la banque des 18 + le backlog chaîné (cadran 4 M3). **Un item sans rail ne part pas en M3** — il part d'abord en wargame (Fable ou M3+polish).
- **Attendu** : 100 % des tickets du runner portent leur DoD + vérifs (grep-able).
- **Échec probable** : la pression du backlog pousse des tickets nus → **contre-action** : Boimler (feeder) refuse la promotion d'un item sans DoD — c'est déjà sa règle (Cerritos Dispatch P3), ici elle devient bloquante.

### M3 — L'enforcement du standard (le harnais rend M3 Fable-classe)
WORKER_PROMPT v2, dans l'ordre : (1) charge lazy son dispatch mindset (wargame 17 M3) ; (2) les 4 gates EN TRIGGERS : « AVANT d'agir, écris pourquoi (1 ligne) » · « APRÈS chaque résultat, re-évalue » · « AVANT SHIP, cours le test réel et COLLE la sortie » ; (3) menu skills INDEX-ONLY (wargame 16 M2) ; (4) D1 : toute claim = fichier/commande.
- **Attendu** : les 4 comportements visibles dans CHAQUE transcript worker (grep-able : `pourquoi:`, `re-eval:`, sortie de commande collée).
- **Échec probable** : M3 saute les gates sous pression de contexte long → **contre-action** : itérations COURTES (one feature at a time, leçon Anthropic harness-design) — le contexte frais est le meilleur exécuteur de consignes.

### M4 — La chaîne complète (le pipeline nommé)
```
Spock airlock (GO triennal + capacité GREEN)
  → ticket (rail M2) → WORKER M3 (itération courte, worktree/session Pane)
    → EVALUATOR M3 contexte frais, refute-first (wargame 15 M4)
      → PASS → SHIP + worklog + push Telegram (sprint gates CADENCE_12WY)
      → RETURN → re-queue avec verdict-as-spec (jamais de re-théorisation)
  → gros volumes : le worker invoque /swarm-orchestrator ou /multi-goal (les /office-hours des B3)
```
- **Fork** : SI un worker est bloqué → l'échelle AIRLOCK-001 §3 (Morty → Computer → Beth), ticket `blocked-*` avec barreaux remplis — jamais un ping A+ direct.

### M5 — Calibration économique (le coût par itération devient une donnée)
7 premiers jours : mesurer tokens/itération réels (proxy compteur si l'API usage ne l'expose pas, `token_estimate: true`) → calibrer le gouverneur (wargame 15 M5) → cible : remplir les creux du graphe MiniMax à ~50 % du pic manuel SANS dépasser le plan mensuel.
- **Attendu** : `cost_per_iteration` dans le scorecard Chapel dès J+7.

### M6 — La MESURE du standard (la seule preuve qui compte)
Mensuel : re-mesurer les 4 métriques mimétiques sur les transcripts workers M3-harnaché (même méthode que les baselines : beats sur sessions réelles) vs le M3 nu de juin (53/50/51/33). **Objectif chiffré : real-test ≥ 55 % au 1er mois** (M3 nu 33, Fable 63) ; les 3 autres en progression mesurée.
- **Attendu** : une ligne baselines v2 dans `_DISCIPLINE_BASELINES.md` (append) — « M3-harnessed 2026-08 : X/X/X/X ».
- **Échec probable** : la mesure elle-même en M3 se flatte → voir red-team.

## ABORT CONDITIONS
1. Quota Fable < 10 % avant reset → Fable ne fait plus QUE l'audit M6 (pas de nouveau wargame — la banque de 18 suffit à alimenter la semaine).
2. Un worker M3 écrit hors sandbox/périmètre de son ticket → boundary-violation, kill + signal.
3. Budget mensuel M3 à 90 % avant J-7 → mode eco (wargame 15 M5 fork), la chaîne ralentit, ne meurt pas.
4. Beth : les pushes Telegram de sprint restent silencieux 23 h-7 h (batch au matin) — la chaîne travaille la nuit, elle ne réveille pas.

## VERIFICATION RUNS
1. 1 ticket rail complet → worker M3 → **pass** = SHIP avec les 4 marqueurs de gates grep-ables dans le transcript.
2. 1 itération volontairement bâclée → **pass** = evaluator RETURN avec verdict-as-spec, re-queue automatique.
3. 1 item sans DoD poussé au feeder → **pass** = refus Boimler loggé.
4. J+7 : `cost_per_iteration` dans le scorecard → **pass** = chiffre + méthode (estimate ou exact).
5. M+1 : baselines v2 append → **pass** = real-test ≥ 55 % ou l'écart expliqué avec données.

## RED-TEAM PASS
- **Attaque ÉCHOUÉE** : « M3 hallucine ses résultats et la chaîne SHIP du faux » — bloquée par triple couche déjà en place : gate real-test (sortie collée, pas déclarée) + evaluator refute-first + D1 receipts. Le mensonge exige de fabriquer une sortie de commande cohérente ET de tromper un contexte frais — coût > bénéfice.
- **Attaque RÉUSSIE → patch intégré** : « l'evaluator est AUSSI M3 — mêmes biais, même complaisance : le standard s'auto-certifie (le proxy-boolean au niveau modèle), et la chaîne entière dérive doucement pendant que tous les gates affichent PASS ». Patch (M6 durci) : **audit-échantillon Fable hebdomadaire** — 5 items SHIP tirés au hasard, re-notés par Fable ; divergence moyenne > 2 pts/12 → recalibrage du prompt evaluator + les 5 verdicts deviennent des exemples few-shot ; la divergence entre en métrique Chapel (`evaluator_drift`). Fable ne quitte jamais la boucle — il devient l'étalon, pas l'ouvrier.

## SELF-GRADE /12 (SUCCESS-ASPACE)
1-2 ✅ · 3 ✅ forks · 4 ✅ RECON (API usage tokens = estimate marqué) · 5 ✅ 4 aborts · 6 ✅ 5 runs mesurables · 7 ✅ red-team (hallucination bloquée · auto-certification réussie→patch étalon-Fable) · 8 ✅ blind · 9 ✅ D1 (receipts session cités ligne par ligne) · 10 ✅ append-only (baselines v2 = append) · 11 ✅ mapping canon (classes, échelle, cadence) · 12 ✅ Beth (abort 4 : nuits silencieuses).

**12/12.**
