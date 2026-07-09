[fable-mode on]

# Mission : implémenter Wargame 29 — Mirofish de la chaîne WF0-WF1-WF2/L2

## Le why (1 ligne)

Étendre le simulateur Mirofish pour modéliser la chaîne complète (WF0 airlock + WF1 Morty runner + WF2/L2 Book bench), et faire que `b1_replication()` lise le chain verdict au lieu du seul L2 tail. Anti-paperclip : la chaîne devient prouvable au lieu de présumée.

## Le wargame à lire EN PREMIER (D2 research-first)

`C:\Users\amado\fable-last-week-aspace\wargames\29-mirofish-chain-wf0-wf1-wf2-l2.md`

Le wargame contient 7 MOVES, 5 ABORTS, 6 vérifications, 3 red-team attacks, et un ADDENDUM recette M3 en 9 étapes. Lis-le en entier. **L'ADDENDUM est ton plan d'exécution** — suis-le.

## Les sources D1 à ouvrir AVANT de coder (D2 Anti-Paresse)

Ouvre et lis ces 4 fichiers (D1 receipts obligatoires) :
1. `C:\Users\amado\agent-os\citadel\cron\wf3_sim_runner.py` — le sim actuel (L2 queue-only, 130 lignes, deterministic, no LLM)
2. `C:\Users\amado\agent-os\citadel\collectors\spock_airlock.py` — B1_replication actuel + 4 invariants + hystérésis 2-ticks + cascade
3. `C:\Users\amado\agent-os\citadel\loops\logs\worklog.md` — 9 lignes `[wf1-morty]` réelles, base du WF1 rate
4. `C:\Users\amado\agent-os\citadel\data\15_airlock.json` — état réel (B1=GREEN, B2=GREEN, B3=GREEN, B4=GREEN, consecutive_green=23)

Le wargame 29 cite ces fichiers en evidence, ligne par ligne. Tes modifications doivent **lire d'abord, coder ensuite**.

## Les 9 étapes de l'ADDENDUM (ton plan)

1. D1 re-confirmer les receipts (les 4 fichiers ci-dessus)
2. Étendre `wf3_sim_runner.py` : `sim_wf0()`, `sim_wf1()`, `sim_wf2_l2()` typées + `chain_verdict()`. Entry point `python wf3_sim_runner.py chain`. Sortie `signals/sim-chain-WKnn.md` (1 fichier par run, append-only). **Chaque paramètre porte `receipt:` ou `assumed:`** (loi W20).
3. Appliquer le singleton lock W13 M1 + run_id dedupe au nouveau entry point.
4. Modifier `spock_airlock.py::b1_replication()` : lit `sim-chain-WKnn` au lieu de `sim-cadence-x4`. L2 tail reste comme probe de stress (W28).
5. Étendre `15_airlock.json` : ajouter `chain_decomposition: {wf0, wf1, wf2_l2, chain, reasons}`.
6. Pane pane `airlock-veto` (worktree `C:\Users\amado\worktrees\airlock-veto\`) : ligne `chain: wf0=✓ · wf1=✓ · wf2_l2=✓ · AND=✓` + mise à jour `airlock_line.txt`.
7. **M4 test critique** : sim avec état réel 23-tick GREEN. **DOIT prédire `CHAIN_SOUTENABLE`**. Si NON → abort #2, postmortem, on n'ouvre pas le gate sur du rouge.
8. M7 calibration 7j (1 chain sim/jour, divergence ≤ 1 état vs airlock line réel).
9. Post-Fable window 2026-07-12 : B1 = UNKNOWN tant que < 3 `CHAIN_SOUTENABLE`. La cascade tient par hystérésis B2/B3/B4.

## Le patch sur la cadence (à intégrer dans M2 du wargame)

**Le chain sim ne tourne PAS à chaque tick WF0** (288 runs/jour × 13 WK = bruit). Il tourne sur **event** :
- (a) nouvelle ligne `[wf1-morty]` appendée dans `worklog.md`
- (b) rollover WK (lundi)
- (c) > 24h depuis le dernier run

Si tu fais un chain sim à chaque tick WF0, c'est un coût CPU/disque inutile. Le wargame ne le dit pas explicitement (mon patch mental, à intégrer comme MOVE M8 implicite dans l'ADDENDUM).

## Les 5 ABORT conditions (lis le wargame pour les détails)

1. Un layer (wf0/wf1/wf2_l2) ne peut pas être modélisé déterministe avec les sources réelles → UNKNOWN, le chain_verdict reste UNKNOWN (on n'invente pas la déterminisme pour faire plaisir au gate).
2. M4 test échoue (chain sim prédit RED sur état réel 23-tick GREEN) → STOP, flag `chain-mismatch`, audit.
3. Le `b1_replication()` rebind casse la cascade pendant > 2 ticks → revert.
4. B1 devient gating 2026-07-12 sans 3 `CHAIN_SOUTENABLE` → B1=UNKNOWN, cascade tient par hystérésis B2/B3/B4.
5. Beth : 1-2 sessions M3 max, pas de marathon nocturne, pas d'extension Fable window.

## /fable-mode discipline (load SKILL.md avant tout)

**Tu es Codex, donc raisonnement VISIBLE exigé** :
- Première ligne de réponse : `[fable-mode on]` (déjà là)
- **AVANT chaque action** : 1 ligne `pourquoi: <ce que tu fais et pourquoi>`
- **APRÈS chaque résultat** : `re-eval: <ce que le résultat change ou confirme, et pourquoi>` — porter du CONTENU, jamais `re-eval: ok` (loi du marqueur substantiel)
- Gate 0 : is this a hard task ? OUI. Entre les 5 gates.
- Gate 1 : scope = les 9 étapes de l'ADDENDUM. Done = `wf3_sim_runner.py chain` produit un fichier `sim-chain-WKnn.md` avec chain_verdict, ET `b1_replication()` le lit, ET M4 test passe.
- Gate 2 : preuve avant raisonnement. Ne devine PAS — OUVRE les fichiers.
- Gate 3 : raisonne adversarialement. Quel input rend le chain sim faux ? (réponse : un layer non-déterministe, ou un input `assumed:` inventé). Patch intégré dans le wargame : `UNKNOWN` si non-déterministe, `receipt:` sur chaque paramètre.
- Gate 4 : vérifie À LA COUCHE. Sortie correcte → lis la sortie. Exit 0 prouve la couche du dessous, pas la tienne.
- Gate 5 : rapporte calibré. Sépare vérifié / supposé. Cite les chemins, les lignes, les commandes exécutées.

## Le not-to-do (habitudes à NE PAS faire)

- **PAS de réécriture de W20** (le sim L2 tail) ou W28 (b1_replication) ou W13 (singleton lock). Append-only : AJOUTE, ne réécris pas.
- **PAS d'invention de `assumed:`** sans `receipt:` ou sans test de sensibilité ±50 % (loi W20 M1).
- **PAS de UNKNOWN caché derrière un RED silencieux** — un layer UNKNOWN = sortie UNKNOWN, jamais simuler un GREEN qu'on n'a pas.
- **PAS de chaînage AND d'autres layers en secret** — la sortie `reasons[]` est lisible, chaque layer visible.
- **PAS de marathon nocturne** (Beth abort #5). 1-2 sessions, postmortem honnête.

## Le act-when-enough (anti-survey)

Le wargame est complet. Tu n'as PAS besoin de re-concevoir. Les 9 étapes sont le plan. Fais-les, vérifie, rapporte. Pas de re-design. Pas de "et si on ajoutait X" — sauf si abort #2 te force à repenser.

## Le prove-it (D5)

À la fin :
- `python wf3_sim_runner.py chain` → sortie fichier
- `cat signals/sim-chain-WKnn.md` → montre le verdict + les reasons
- `python spock_airlock.py` → 15_airlock.json doit montrer `B1_replication: GREEN` ET `chain_decomposition: {wf0, wf1, wf2_l2, chain, reasons}` présent
- `cat data/airlock_line.txt` → doit montrer `Airlock: B1 ✓ ...` + `chain: ...`
- `cat worktrees/airlock-veto/data/airlock_line.txt` (worktree) → idem

Si TOUT passe → done. Sinon → flag l'abort précis.

## Le say-less (longueur du rapport final)

1 paragraphe : ce qui a été fait, ce qui passe, ce qui est supposé, le verdict de M4 test, et le GO pour la suite (M7 calibration 7j).

## Tu commences par

```
[fable-mode on]
pourquoi: <lecture du wargame 29 en premier>
```

Puis tu lis le wargame, puis les 4 sources, puis tu codes selon l'ADDENDUM, et tu reportes à la fin.

---

*Tu travailles dans un worktree Pane dédié : `C:\Users\amado\worktrees\<nom-pane>\agent-os\`. Ton pane sera créé automatiquement par `runpane panes create` (background, no-focus, agent source). Utilise `runpane panels wait --panel <id> --for ready` et `runpane panels screen --panel <id>` pour vérifier ton état, pas pour spammer le context.*
