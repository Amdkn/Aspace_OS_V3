# WARGAME 12 — WF1 Run Loop : cure du context thrashing + blindage Harness Hermes

> Wargamé par Hermes Agent (HA, A3 Picard H10), 2026-07-06. Méthode : diagnose-proxy-boolean (4 phases), battle-tested ×2 dans la même session que ce wargame.
> Exécuteur : **Hermes Agent (M3)**. Cible : `wf1_runner.ps1` + `WORKER_PROMPT.md` + Harness local. Exécutable blind (pas de HITL requis).

## RECON (fait — D1, filesystem vérifié)

### A. Empreinte contexte worker (par itération)

| Fichier | Taille | Lu comment ? | Risque |
|---|---|---|---|
| `loops/ARCHITECTURE.md` | 2431 b (29 l.) | full (instruction §1) | 🟡 stable — re-lu pour rien |
| `loops/domains/wf1-morty/README.md` | 1216 b (14 l.) | full | 🟡 stable — re-lu pour rien |
| `loops/logs/worklog.md` | 2292 b (15 l.) | **10 dernières lignes** | ✅ contraint |
| `loops/artifacts/tasks/*` | ~1330 b total, 2 files | pioché 1 par iter | ✅ petit |

**Total re-lu stable par iter** : ~3650 b. Pas énorme seul, mais **cumulé avec l'output worker + fichiers découverts en chemin** = dépasse le budget.

### B. État runner réel (filesystem, pas le résumé CC)

```
07:04:38 RUN LOOP start (Once=False)
07:04:38 iteration 1 - spawn worker
        ⚠️  Autocompact is thrashing (3 turns of compact in a row)
07:12:34 iteration 1 done in 476s (rc=1)
07:13:19 iteration 2 - spawn worker
        ⚠️  même erreur
07:19:45 iteration 2 done in 386s (rc=1)
```

**2 itérations, 2 `rc=1`**. Aucun pass de travail (pas de ligne worklog `[wf1-morty]`). Le runner est vivant — les workers meurent.

### C. Schtasks confirmées

`AspaceWF1Runner` ✅ existe (schtasks /Query). + 9 autres schtasks Aspace-Heartbeat-* / AspaceLoop* / WarMode-Telegram-Digest.

### D. Flags / kill-switches

- `decisions/enable_wf1.flag` 🟢 (37 b, 04:08)
- `decisions/FABLE_WINDOW.flag` 🟢 (123 b, 04:08)
- `data/beth_repos.flag` 🟢 (40 b, 06:31) — pause hors fenêtre active
- `decisions/STOP_WF1_RUNNER.flag` ⚫ absent (pas d'urgence en cours)

### E. Harness Hermes (canon = `C:\Users\amado\AppData\Local\hermes\`)

- skills/ : 32 items (catégories)
- plugins/ : 1
- cron/ : 3 (+ output/)
- memories/ : MEMORY.md + USER.md
- config.yaml : 15581 b
- ⚠️ **legacy stub at `C:\Users\amado\.hermes\`** (40 items) — Windows path trap documenté dans `hermes-config-reference` (legacy, à renommer append-only D4 — hors scope de ce wargame)

### F. Manque identifié côté Harness

- ❌ **Skill `diagnose-proxy-boolean` absente localement** (CC2 l'a gravée côté sien, mais HA/M3 ne l'a pas → doctrine non-exécutable de mon côté)
- ❌ Pas de `/wargame` slash command exposé (méthode appliquée inline via lecture de `fable-last-week-aspace/wargames/*.md`)
- ❌ Pas de skill dédiée au monitoring runner (pour relayer les `[wf1-morty]` lignes au heartbeat 4h)

## PROXY-BOOLEAN HUNT (4 phases, doctrine Wargame 08 battle-tested)

### Proie #1 — `RUN LOOP WF1 LIVE` (boolean déclaré par A0, jamais validé par le worker)

1. **Identifier le booléen** : `decisions/2026-07-06_wf1_run_loop_live.json` → `action: "decision"`, claims `RUN LOOP WF1 arme et LIVE`.
2. **Tracer la source** : auto-déclaré par CC (A0). Aucun consumer n'a confirmé.
3. **Vérifier le consommateur réel** : le worklog devrait contenir des `[wf1-morty]` lignes écrites par le worker. **Zéro.** La ligne WF1 a été écrite par `[wf0-spock]`, pas par le worker.
4. **Cure (additive)** : exiger une ligne worklog `[wf1-morty] START <ISO>` émise par le worker **avant** toute action. Tant que cette ligne n'existe pas, le worker n'est pas « live » — il est juste « spawné ».

### Proie #2 — `process claude worker vivant` (boolean d'état confondu avec état productif)

1. **Identifier** : `d5_proofs` claim `process claude worker vivant`.
2. **Tracer** : `wf1_runner.log` montre rc=1 sur 2 itérations.
3. **Vérifier consommateur réel** : un worker « vivant » qui crashe en 7 min sans écrire de preuve = un mort qui marche. Le runner log **mélange** runner-state et worker-output via `*>> $Log` → la failure est enterrée sous le « iteration done ».
4. **Cure (additive)** : split en deux logs. `wf1_runner.log` = runner state (gates, iter, rc). `wf1_worker.log` = worker stdout/stderr par iter, séparé et lisible. Plus : kill explicite si > 600 s sans worklog append (signal de thrashing détectable).

### Proie #3 — `290s de travail réel` (test ≠ prod — même famille que `cadence_alive`)

1. **Identifier** : claim « 290 s de travail réel (tué par MON timeout de test) ».
2. **Tracer** : ce 290 s = un test **tué par l'extérieur** (CC's manual timeout). Les 2 itérations prod **après** ce test = rc=1, ctx thrash.
3. **Vérifier consommateur réel** : un test qui n'atteint pas son terme naturel ≠ une mesure valide. Les prod runs prouvent le contraire.
4. **Cure (additive)** : tout claim de « travail réel » doit être adossé à un run qui s'est terminé **de lui-même** + qui a append sa ligne worklog. Test kill par timeout externe = à étiqueter `killed-external`, pas `worked`.

## RED-TEAM PATCHES (additifs, zéro hard-delete)

### Patch PS-1 — `wf1_runner.ps1` : split logs + max-time guard

- `wf1_runner.log` = runner state only (gates, iter N spawn, iter N done rc=X)
- `wf1_worker.log` = worker stdout/stderr par iter (header `[iter N · ISO]`)
- Max-time guard : si worker > 600 s sans append worklog → kill process + ligne `iter N TIMEOUT-no-worklog rc=124` dans runner log (124 = timeout convention)
- Kill-switch read une fois par iter (déjà fait), restart runner inchangé

### Patch WP-1 — `WORKER_PROMPT.md` : context budget + START heartbeat

- **§0 START HEARTBEAT** (ajout en tête, avant §1) : « Émets **immédiatement** la ligne `[<ISO>] [wf1-morty] START iter N` dans `loops/logs/worklog.md` avant toute autre action. C'est ta preuve d'existence. Si tu ne le fais pas, tu n'as pas travaillé. »
- **§1 BIS Context Budget** (ajout) : « Tu as ~10k tokens. **NE RELIS PAS** `ARCHITECTURE.md` ni `README.md` à chaque iter — ce sont des canoniques stables, ta première iter les a internalisés. Si tu dois vérifier, lis une section spécifique (offset/limit), jamais le fichier. Max 1 fichier > 50 lignes par iter. »
- **§6 BIS Emergency exit** (ajout) : « Si tu détectes que ton contexte est presque plein (> 80%), exit IMMÉDIATEMENT après avoir émis un signal `ctx-pressure` dans le worklog. Le runner te spawnera frais à l'iter suivante. »

### Patch HERMES-1 — `diagnose-proxy-boolean` skill (côté HA, doctrine exécutable)

- Skill locale à `C:\Users\amado\AppData\Local\hermes\skills\diagnose-proxy-boolean\SKILL.md`
- 4 phases formalisées + checklist par phase + 3 exemples (08 MiroFish, 09 Gstack cadence, ce 12 WF1)
- Battle-tested ×2 (08 + 09) + ×3 après ce wargame → canonique
- Les 7 Picard variants C1..I1 + M3 + Beth chargent cette skill en kickoff

### Patch HERMES-2 (note, hors scope exec) — legacy stub audit

- `C:\Users\amado\.hermes\` (40 items) coexiste avec `HERMES_HOME=C:\Users\amado\AppData\Local\hermes\` (canon)
- Risque : edits via Git Bash `~/.hermes/` frappent le stub, pas le canon
- Action future (append-only D4) : `mv ~/.hermes ~/.hermes_legacy_2026-07-06` après audit
- **Pas touché dans ce wargame** — scope strict = cure thrashing + skill diagnose

## VERIFICATION (post-exec)

- [ ] `wf1_runner.ps1` patché : `Get-Content` montre split log + max-time guard
- [ ] `WORKER_PROMPT.md` patché : `Get-Content` montre §0 START HEARTBEAT + §1 BIS Context Budget + §6 BIS
- [ ] `AppData\Local\hermes\skills\diagnose-proxy-boolean\SKILL.md` créé, lisible
- [ ] Attendre 1-2 iter du runner : **CONFIRMATION** que la 1ère ligne `[wf1-morty]` arrive dans worklog
- [ ] Si oui : WF1 = officiellement LIVE, Beth hérite d'un worker autonome

## GRADE (provisional)

| # | Critère | Note |
|---|---|---|
| 1 | Recon réel (filesystem, pas résumé) | ✅ |
| 2 | Proxy-boolean hunt × ≥ 3 | ✅ ×3 |
| 3 | Red-team patches additifs (zéro hard-delete) | ✅ |
| 4 | Cure avec exit_condition chiffrée | ✅ (600 s no-worklog → kill rc=124) |
| 5 | Exécuteur identifié | ✅ HA |
| 6 | Preuves D5 (file paths + tailles + timestamps) | ✅ |
| 7 | Kill-switches documentés | ✅ |
| 8 | Append-only respecté | ✅ |
| 9 | Skill canonique extraite | ✅ diagnose-proxy-boolean |
| 10 | Doc layout (RECON/MOVES/PATCHES/VERIFY) | ✅ |
| 11 | Battle-tested dans la même session | ✅ (08 + 09 + ce 12) |
| 12 | Handover Beth-compatible | ✅ (cap ×4 hérité, max 12 agents) |

**Provisional : 12/12**, sous réserve que la VERIFICATION (ligne worklog `[wf1-morty]` dans l'heure) confirme que les patches tiennent en prod.
