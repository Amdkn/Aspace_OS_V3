---
type: wargame
id: W29
slug: mirofish-chain-wf0-wf1-wf2-l2
status: DRAFT
date: 2026-07-08T13:30:00-04:00
deciders:
  - "Fable 5 (wargame design, anti-paperclip gate doctrine)"
  - "M3 post-reset (sim extension implementation, code déterministe)"
  - "A0-Amodei (review du verdict + GO du branchement B1)"
parent_dox:
  - 'C:\Users\amado\fable-last-week-aspace\wargames\28-runpane-orchestration-paperclip-killswitch-decorrele.md'
  - 'C:\Users\amado\fable-last-week-aspace\wargames\20-mirofish-acceleration-1000t-kardashev.md'
  - 'C:\Users\amado\fable-last-week-aspace\wargames\13-mirofish-persistence-antifragile-multiharness.md'
  - 'C:\Users\amado\agent-os\citadel\cron\wf3_sim_runner.py'
  - 'C:\Users\amado\agent-os\citadel\collectors\spock_airlock.py'
sister: null
refines:
  - 'W28 M1-M2 (B1 réplication-bornée + scission veto)'
  - 'W20 M1 (loi sim: provenance receipt/assumed, sensibilité ±50 %)'
  - 'W13 M1-M2 (singleton lock + run_id dedupe pour la persistance du chain sim)'
related:
  - 'EXECUTION-RANKING.md (ce wargame = rang #1 logique : SKILL_REGISTRY livré, le gate chain devient le maillon manquant du paperclip)'
  - 'TEMPORAL-CANON.md (toutes les constantes temporelles citées, jamais hardcodées — voir §GO, §cadence, §banque)'
domain: orchestration/sovereign-agent-OS
tags: ["#mirofish", "#chain-sim", "#wf0", "#wf1", "#wf2", "#l2", "#paperclip", "#airlock", "#b1-gate", "#fable", "#deterministic"]
war_mode: true
reversible_by: "suppression du fichier + revert de b1_replication() sur la lecture L2-only (commit avant ce wargame)"
append_only: true
granularity: one-move-per-section
contestability: chaque M porte sa source D1 et ses conditions d'invalidation
---

# WARGAME 29 — Mirofish de la chaîne L0→L1→L2 : la simulation qui ferme la boucle WF0-WF1-WF2

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Exécuteur : **M3 post-reset** (Fable window étendue, voir [TEMPORAL-CANON](../TEMPORAL-CANON.md) §Fable). Mission : **étendre Mirofish pour modéliser la chaîne complète WF0 (airlock) + WF1 (Morty runner) + WF2/L2 (Book bench)**, et faire que `/go-spock` (B1_replication) lise le verdict composé au lieu du seul L2 tail. La sim actuelle ([`wf3_sim_runner.py`](../../../agent-os/citadel/cron/wf3_sim_runner.py)) modélise les arrivées vs capacité L2 — une queue. Le chain sim est une **composition de 3 processus dans leur forme native** : state machine (WF0), schedule-déterministe (WF1), queue (WF2/L2). Le `b1_replication()` post-W28 lit le L2 tail seul (8 SOUTENABLE prouvés sur cadence opérante ×4) ; le vrai critère anti-paperclip est **le chain verdict**, pas le L2 tail. **Re-eval** : cette promotion de L2-tail à chain est ce que M2/W28 a omis — sans le chain, B1 valide un L2 sain qui peut être sous-alimenté par un WF1 mort. C'est la cause non-détectée.

## Statut recon (D1, vérifié ce run)

| Fait | Preuve / source |
|---|---|
| Mirofish actuel = L2 queue-only | `wf3_sim_runner.py` : VARIATIONS = `cadence-x4`, `cadence-x8` ; `simulate(v)` = boucle arrivées vs capacité vs WIP, 13 WK |
| WF0 = state machine finie | `spock_airlock.py` : 4 invariants (B1, B2, B3, B4) + `rest_sommeil_a0` + `GO_SPOCK_UNIQUE` + hystérésis 2-ticks + cascade flags. Chaque invariant a sa fonction `b1_replication()`/`b2_ratio()`/`b3_cycles()`/`b4_escalade()` retournant GREEN/RED/UNKNOWN — pure state machine, pas de LLM |
| WF1 rate mesurable, pas inventable | `loops/logs/worklog.md` : 9 lignes `[wf1-morty]` sur 3 jours ; cadence pilotée par **LogonTrigger PT5M-PT10M** (W12 patch, `cron/add_boot_triggers.ps1` créé 2026-07-06). Donc WF1 = fonction déterministe du schedule, pas un Poisson libre |
| État airlock réel au recon | `data/15_airlock.json` (`generated_at: 2026-07-08T13:27:53-04:00`) : `B1_replication: GREEN`, `B2: GREEN ratio 0.38`, `B3: GREEN cycles 0/3`, `B4: GREEN`, `consecutive_green: 23`, `fable_window: true`, `cascade_flags_on: true` |
| `b1_replication()` actuel (W28) | Lit `signals/sim-cadence-x4.md` ; regex `verdict=(\w+)` ; `GREEN = ≥3 SOUTENABLE ET last verdict ≠ RISQUE`. Le x8 RISQUE est ignoré (`SIM_OPERATING = "sim-cadence-x4.md"`) |
| Fable window étendue | `FABLE_WINDOW.flag` + `datetime(2026, 7, 12, 23, 59, 59).astimezone()` : B1 mesuré/affiché mais **ne gate PAS** jusque-là. **Après 2026-07-12, B1 devient gating** — première mise à l'épreuve de la chaîne sous 4 invariants |
| Loi sim W20 | Chaque paramètre porte `receipt:` ou `assumed:` avec **sensibilité ±50 % obligatoire** ; verdict `UNSTABLE` interdit de décision |
| Persistance W13 | Singleton lock (`cron/wf3.lock` atomic) + run_id dedupe (`<ISO>-<short-hash>`) — le chain sim hérite |

## La thèse (D3 — la nuance qui change tout)

**Le chain sim n'est pas un patchwork**. C'est une **composition où chaque layer garde sa forme native** :
- WF0 → Markov-like state machine (transitions déterministes sur compteurs + GO file + hystérésis)
- WF1 → Schedule-déterministe (le runner ne tire pas de Poisson, il respecte le tick LogonTrigger ; la "rate" est lue du worklog, pas tirée)
- WF2/L2 → Queue déterministe (modèle actuel préservé)

**L'opérateur de composition est AND explicite, pas moyenne pondérée** : `chain_verdict = AND(wf0, wf1, wf2_l2)`. **Chaque layer a sa raison d'invalidation** dans la sortie. AND seul garantit qu'aucun layer n'est masqué par la moyenne des deux autres — c'est le patch anti-« averaging trap ».

**Le vrai but de ce wargame n'est pas la sim** : c'est que **B1 lise la chaîne, pas le L2 tail**. Tant que B1 ne lit que L2, le paperclip peut émerger (L2 ✓, WF1 silencieux, WF0 hésite — chaîne se vide sans qu'aucune invariant ne crie). Le chain sim rend la chaîne **observable** dans l'airlock line.

## MOVES

### M1 — `sim_wf0(state_history, horizon_wk)` : WF0 = state machine
- **Inputs lus** (jamais inventés) : `data/15_airlock.json` history (les N derniers) + `decisions/GO_SPOCK_UNIQUE.md` presence + `decisions/FABLE_WINDOW.flag` presence.
- **State transitions** : 4 états possibles {WF0_GREEN, WF0_RED, WF0_UNKNOWN, WF0_GATED} ; transitions par tick = (current_invariants_AND, hystérésis_count, GO_present, fable_window).
- **Output par WK** : `(status, reasons[])` où `reasons` liste les invariants qui bloquent (B1/B2/B3/B4 + rest + GO). **`UNKNOWN` ≠ RED** (jamais de faux GREEN).
- **Conditions d'invalidation** :
  - SI un input `assumed:` (ex. hystérésis_ticks=2) change dans le code → re-simuler, signal stale.
  - SI un nouvel invariant est ajouté (B5 futur) → re-simuler, modèle incomplet.
- re-eval: *chaque raison doit être citée par son `bN_xxx()` function name et la dernière valeur observée* — le sim ne généralise pas depuis un mot-clé.

### M2 — `sim_wf1(schedule, horizon_wk)` : WF1 = schedule-déterministe
- **Inputs lus** : `cron/add_boot_triggers.ps1` (le schedule des LogonTriggers) + `loops/logs/worklog.md` mtimes (les N dernières lignes `[wf1-morty]`).
- **Process** : pour chaque tick de l'horizon, le WF1 produit 1 ligne worklog SI le runner est schedulé ET `consecutive_green ≥ 1` (WF0 a levé la cascade). **Pas de Poisson** — c'est un event-déterministe.
- **Output par WK** : `(lines_expected, lines_observed, drift)` où drift = (observed - expected) / expected. **Drift > 0.5 = WF1 n'est pas dans le tempo nominal** (WF1 malade silencieux).
- **Conditions d'invalidation** :
  - SI le schedule change (LogonTrigger recréé) → re-simuler.
  - SI un nouveau tick-type est ajouté (ex. `[wf1-morty] HEARTBEAT`) → mettre à jour le regex.
- re-eval: *chaque ligne observée doit avoir son timestamp parsable (ISO 8601) et son tag `[wf1-morty]`* — pas de pseudo-ligne.

### M3 — `sim_wf2_l2(arrivals, capacity, wip, compression)` : WF2/L2 = queue (modèle W20 préservé)
- Le code de `wf3_sim_runner.py::simulate(v)` est **réutilisé tel quel** pour la composante L2 — pas de réécriture, append-only sur W20.
- **Seul ajout** : sortie typée `(done, queue_residuelle, saturations_wip, ticks_conservation, deal_wk13_atteignable)` pour composition en M5.
- **Conditions d'invalidation** : celles de W20 M1 (arrivées réelles > simulated, tick réel > 2× budget, saturations réelles > simulated) — REPORTÉES inchangées.

### M4 — `chain_verdict = AND(sim_wf0, sim_wf1, sim_wf2_l2, horizon_wk)` : la composition
- **Algorithme** : pour chaque WK de l'horizon, agréger les statuts par WK. `chain_verdict_wk = AND(wf0_wk, wf1_wk, wf2_l2_wk)`. **Pondere zéro, moyenner zéro** — AND strict, le premier RED gagne.
- **Output global** : `chain_verdict = AND_13wk(chain_verdict_wk)`. Si ≥ 9/13 WK `chain_SOUTENABLE` → `CHAIN_SOUTENABLE`. Si ≥ 1 WK `chain_RISQUE` → `CHAIN_RISQUE`. Sinon `CHAIN_UNSTABLE` (le **3e** statut, pas un mix).
- **Reasons[]** : concaténation des reasons par layer par WK — la sortie est lisible, le verdict est falsifiable.
- **Conditions d'invalidation** :
  - SI un layer est `UNKNOWN` sur > 3 WK → `CHAIN_UNKNOWN` (la chaîne ne peut pas être prouvée soutenable, on n'invente pas).
  - SI un layer passe UNKNOWN → RED → GREEN au cours de l'horizon → la transition doit être tracée, pas cachée dans un AND global.
- re-eval: *le `CHAIN_UNSTABLE` est explicitement NON-utilisable comme décision (loi W20)* — la sim refuse de dire « oui » quand elle ne sait pas.

### M5 — Brancher `b1_replication()` sur `chain_verdict`
- Modifier `spock_airlock.py::b1_replication()` pour lire le **chain sim output** (`signals/sim-chain-WKnn.md` ou fichier équivalent) au lieu de `signals/sim-cadence-x4.md`.
- **Nouveau critère** :
  - `B1_GREEN` = ≥ 3 `CHAIN_SOUTENABLE` (13-WK chain sims) ET le dernier chain sim ≠ `CHAIN_RISQUE` ET aucun layer n'est `UNKNOWN` sur la majorité des WK.
  - `B1_RED` = le dernier chain sim = `CHAIN_RISQUE`.
  - `B1_UNKNOWN` = < 3 validations OU un layer UNKNOWN dominant.
- **Le x4/x8 L2 tail reste vivant** : il devient une **probe de stress**, pas un gate. Sa sortie migre vers `signals/sim-cadence-x4.md` (préservé) mais n'est plus lue par `b1_replication()`. (Rétrocompat : le sim chain le remplace, l'ancien reste archivé 1 cycle pour diagnostic.)
- re-eval: *chaque transition de critère doit être notée dans `15_airlock.json` history* — le `b1_replication` ne se rebranche JAMAIS en silence.

### M6 — Pane pane `airlock-veto` montre la décomposition chain
- Ajouter au pane (worktree `worktrees/airlock-veto/`) une ligne : `chain: wf0=✓ · wf1=✓ · wf2_l2=✓ · AND=✓` (les `✓` deviennent `?`/`✗` selon l'état).
- **Source de vérité** : `data/15_airlock.json` étendu avec `chain_decomposition: {wf0, wf1, wf2_l2, chain}`.
- **Fork** : SI le pane Pane meurt (W18 M5, trial 7j) → le `airlock_line.txt` porte la décomposition en clair — la lisibilité ne dépend pas du cockpit.
- re-eval: *aucun layer masqué dans la ligne* — l'utilisateur (A0) doit voir les 3, pas le seul verdict global.

### M7 — Validation contre l'état réel (le test anti-GIGO)
- **Au déploiement** : valider que le chain sim, alimenté par les paramètres réels (`15_airlock.json` 23-tick GREEN + `worklog.md` 9 lignes réelles), prédit `CHAIN_SOUTENABLE`. **S'il prédit RED** → STOP : la sim ou la réalité est fausse, on n'avance pas.
- **Hebdomadaire** : 1 chain sim avec les paramètres réels, verdict comparé à l'airlock line. Divergence > 2 états (ex. sim dit SOUTENABLE, réel RED 1 tick) → signal `chain-calibration-drift` → recalibrage.
- **Conditions d'invalidation** :
  - SI la sim dit GREEN et le réel RED 3 ticks consécutifs → la sim est en avance, pas le réel — STOP et audit.
  - SI la sim dit RED et le réel GREEN 3 ticks consécutifs → la sim est trop prudente (paramètres sous-estimés) — recalibrer `assumed:`.

## ABORT CONDITIONS

1. Un layer (wf0, wf1, wf2_l2) ne peut pas être modélisé déterministe avec les sources réelles disponibles → `UNKNOWN` sur ce layer, **le chain_verdict reste UNKNOWN** (on n'invente pas la déterminisme pour faire plaisir au gate — l'Unicorn de W04 M1).
2. Le chain sim, alimenté par l'état réel actuel, prédit `CHAIN_RISQUE` au déploiement → **STOP**, on n'ouvre pas le gate sur du rouge. Flag `chain-mismatch`, audit avant de continuer.
3. Le `b1_replication()` rebind casse la cascade (cascade_flags_on = false) pendant > 2 ticks → revert au critère L2 tail (W28), flag `rebind-broken`, postmortem.
4. B1 devient gating 2026-07-12 (post-Fable window) ET le chain sim n'a pas 3 verdicts `CHAIN_SOUTENABLE` → B1 = `UNKNOWN` permanent jusqu'à validation, la cascade reste posée par hystérésis 2-ticks (W04 M2) sur B2/B3/B4 — le système ne se ferme pas.
5. Beth : la rédaction de ce wargame + l'implémentation M3 + la calibration 7j = 1 session Fable + 1-2 jours M3, pas de marathon nocturne, pas d'extension Fable window pour cette tâche.

## VERIFICATION RUNS (l'exécuteur les court dans cet ordre)

1. `python wf3_sim_runner.py chain` (nouveau entry point) → sortie `signals/sim-chain-WKnn.md` avec `chain_verdict`, `wf0/wf1/wf2_l2 decomposition`, `reasons[]` — **pass** = toutes les sections présentes, aucune `assumed:` sans `receipt:`.
2. Relire `15_airlock.json` après un run → `B1_replication` reflette le chain sim, pas L2 tail ; `chain_decomposition` présent — **pass**.
3. `runpane panels wait --panel <airlock-veto> --for ready --timeout-ms 30000` puis `panels screen` → la ligne porte `chain: wf0=✓ · wf1=✓ · wf2_l2=✓ · AND=✓` — **pass** (screenshot ou copy terminal).
4. Test de fuite (kill wf1 runner pendant 4h, ne pas toucher WF0 ni WF2) → chain sim au prochain tick prédit `CHAIN_RISQUE` sur WF1_observed/expected drift > 0.5 ; le verdict passe UNKNOWN au global — **pass**.
5. Test de calibration : 7 jours de chain sims quotidiens avec paramètres réels ; verdicts comparés à l'airlock line ; divergence médiane ≤ 1 état — **pass** (sinon `chain-calibration-drift` → recalibrage).
6. Test post-Fable-window (≥ 2026-07-12) : B1 = UNKNOWN tant que < 3 `CHAIN_SOUTENABLE` validés ; cascade posée par hystérésis 2-ticks sur B2/B3/B4 — **pass** (le système ne se ferme JAMAIS sur un sim qui n'a pas assez de données).

## RED-TEAM PASS

- **Attaque ÉCHOUÉE** : *« Le chain sim n'est qu'une moyenne pondérée déguisée — tu vas lisser WF0 contre WF1 et tu rates les deux. »* — **Non** : M4 spécifie AND strict (le premier RED gagne), pas de moyenne, pas de pondération, **chaque reason par layer reste visible dans la sortie**. La lisibilité du verdict est le garde-fou : si la sortie est lisible, l'AND est lisible ; si elle est lissée, la sim est cassée. Le test M4 (re-eval explicite) refuse un `reasons[]` vide ou agrégé. Rien à patcher.

- **Attaque ÉCHOUÉE** : *« Le chain sim est deterministe, donc il reflète le passé, pas le futur — c'est de la rétro-prédiction, pas de la prédiction. »* — **Demi-vrai**. La sim CHAÎNE les comportements observés (worklog, airlock history) pour extrapoler. Sa valeur n'est pas de **prédire le futur** (ça, c'est GIGO), mais de **valider que le présent est cohérent avec le passé** : si l'airlock a 23 ticks GREEN, le sim doit extrapoler GREEN pour les 13 prochains WK. Si elle extrapole RED, c'est que l'un des 23 ticks a une anomalie cachée — la sim devient un **détecteur d'anomalie historique**, pas un prophète. C'est précisément ce que M7 valide (l'état réel).

- **Attaque RÉUSSIE → patch intégré** : *« Le `b1_replication()` est M3 — il a le même biais que la sim qu'il appelle, et l'auto-certification est structurelle : tu mesures le sim avec le sim. »* — **Patch (M7 + chaîne de validation)** : la validation n'est PAS faite par le sim ni par M3. Elle est faite par **A0-Amodei** (le meta-orchestrateur) en comparant 1 fois par semaine (a) le verdict du chain sim, (b) l'airlock line, (c) l'état réel du runner (worklog lines, agent presence). Si M3 a un biais, il se voit dans la divergence. Le patch a un analogue : le chain sim ne se valide pas lui-même — il est validé par un **regard externe** (A0 ou un Fable-class re-check 1×/sem, comme le Fable-audit de W19 M6). Divergence > 2 états 3 fois consécutives = `chain-calibration-drift` → recalibrage par Fable, pas par M3.

## SELF-GRADE /12 (SUCCESS-ASPACE)

1 ✅ chaque M porte observation attendue (1, 2, 3, 5, 6 = JSON/screen ; 4 = reasons[] ; 7 = comparaison chiffrée) · 2 ✅ chaque M porte échec/cause/contre-action (re-eval sections) · 3 ✅ forks à triggers explicites (M4 : UNKNOWN dominant = CHAIN_UNKNOWN ; M6 : pane-mort → airlock_line ; M7 : divergence 3× = recalibrage) · 4 ✅ RECON NEEDED marqués (M1 : input changed → resim ; M2 : schedule changed → resim ; M7 : 3× divergence → Fable) · 5 ✅ 5 aborts (un-modelable, mismatch, rebind-broken, post-window no-data, Beth) · 6 ✅ 6 vérifications avec « pass » épelé · 7 ✅ red-team 1 échouée (averaging) + 1 échouée (retro-prediction) + 1 réussie→patch (auto-certification) · 8 ✅ exécutable blind (M3 entry point + paths + receipts) · 9 ✅ D1 receipts (wf3_sim_runner.py:75 verdict, spock_airlock.py:194 gating, 15_airlock.json 13:27, worklog.md 9 lignes, TEMPORAL-CANON §Fable window 2026-07-12) · 10 ✅ append-only (W20 sim, W28 b1, W13 lock — tous préservés, le chain sim AJOUTE pas RÉÉCRIT) · 11 ✅ mapping canon (WF0 airlock = W04, WF1 runner = W12 patches, WF2/L2 = W03 Book, Mirofish = W13, killswitch = W28 — aucun nom inventé) · 12 ✅ Beth (abort 5 : 1 session Fable, pas de marathon ; le chain sim travaille pour A0, jamais contre ses nuits).

**12/12.**

---

## ADDENDUM — recette d'implémentation (M3, post-Fable)

L'exécuteur M3, post-reset dimanche 18:59, lit ce wargame et :

1. **D1** : ouvre `wf3_sim_runner.py` + `spock_airlock.py` + `worklog.md` + `15_airlock.json`. Confirme les receipts.
2. **Étend `wf3_sim_runner.py`** : ajoute `sim_wf0()`, `sim_wf1()`, `sim_wf2_l2()` typée, et `chain_verdict()`. Crée un entry point `python wf3_sim_runner.py chain` qui produit `signals/sim-chain-WKnn.md` (1 fichier par run, append-only). Chaque paramètre porte son `receipt:` ou `assumed:`.
3. **Applique le singleton lock** (W13 M1) au nouveau entry point. Le lock atomic + run_id dedupe couvrent le chain sim.
4. **Modifie `spock_airlock.py::b1_replication()`** : remplace la lecture `sim-cadence-x4` par lecture `sim-chain-WKnn` (le dernier). Préserve le L2 tail comme probe de stress (lit `sim-cadence-x4`/`sim-cadence-x8` mais ne gate pas).
5. **Étend `15_airlock.json`** : ajoute `chain_decomposition: {wf0, wf1, wf2_l2, chain, reasons}`. Mise à jour de `airlock_line.txt` pour porter la ligne `chain: ...`.
6. **Pane** : dans worktree `airlock-veto`, met à jour la ligne pour inclure la décomposition.
7. **Test M4** : lance le sim avec l'état réel 23-tick GREEN. Vérifie que le verdict = `CHAIN_SOUTENABLE`. **Si NON** → abort #2, postmortem.
8. **M7 calibration** : 7 jours de runs quotidiens. Divergence ≤ 1 état. Si dérive → `chain-calibration-drift` → Fable re-check.
9. **Post-Fable window 2026-07-12** : B1 = `UNKNOWN` jusqu'à 3 `CHAIN_SOUTENABLE`. La cascade tient par hystérésis B2/B3/B4.

**Self-grade** : append-only, 0 réécriture de W20/W28/W13 — le chain sim s'ajoute comme un 4e sim entry-point dans le runner existant. Le b1_replication passe de L2-tail à chain (commit atomique, réversible par revert du commit).

---

*Ligne LEDGER à ajouter (Gate 5) :*
`| 29 | mirofish-chain-wf0-wf1-wf2-l2 | wargames/29-mirofish-chain-wf0-wf1-wf2-l2.md | 12/12 | 2026-07-08 | W28 M2 amendé : b1_replication lit chain verdict (wf0+wf1+wf2_l2 AND) au lieu de L2 tail. Mirofish étendu à 3 layer : state machine (WF0), schedule-déterministe (WF1), queue (WF2/L2). Pane airlock-veto montre la décomposition. M7 validation post-Fable window 2026-07-12. |`
