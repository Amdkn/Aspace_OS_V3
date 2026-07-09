# ASpace_OS_V3 — Doctrine d'Orchestration par Défaut

> **Statut** : V3-ANNEX (append-only, D4). Pas un override du canon fondateur.
> Canon fondateur = `~/.claude/CLAUDE.md` (user-level, 22 KB) + `AGENTS.md` (V2 stub byte-identique V3).
> Ce fichier = la **doctrine d'orchestration V3** que A0 (Jumeau Numérique) applique **par défaut** quand il est invoqué en `/fable-mode` ou `/multi-goal` ou `/swarm-orchestrator` ou `/wargame` ou `/multi-routines-12wy` ou `/loop`.
> Il est **rédigé comme une prescription opérationnelle**, pas une doctrine philosophique — chaque section = un *trigger* → *action*.

---

## 1. Modèle mental canon (le "qui-est-qui")

```
A0 — Jumeau Numérique Amadeus (méta-coach, vision H30, Gouverneur ON-not-IN E-Myth)
   │
   ├── A1 Gatekeepers (SOBER anti-paperclip, vision 3 ans, 2-3 membres)
   │   ├── B1 = Jerry (E-Myth systemize) + Summers (SHIP) — Business OS
   │   └── A1 = Beth (vie/santé) + Rick (sobriété kernel) + Sommerfield (limites)
   │
   ├── A2 Ingénieurs (vision 10 ans, ~6 membres)
   │   ├── superpowers (obra) — Manager E-Myth des freelances, A2 principal
   │   └── Gstack (garrytan) — Visionnaire E-Myth, B1 (mais utilisable en A2)
   │
   ├── A3 Méta-Orchestrateurs (vision 1-10 semaines, ~35-100+ membres, fractal)
   │   ├── GSD (open-gsd/gsd-core) — Framework CC principal des A3/B3
   │   ├── MiraFish (WF3) — Swarm prédictif H1/H3/H10
   │   ├── Fable Wargames — doctrine de validation move-by-move
   │   └── CEO-Bench — détection angles morts (A3 Book canon)
   │
   └── B2/B3 (Business, mirror A2/A3 par doctrine E-Myth)
```

**Kardashev types** :
- A3/B3 = Type 1 (technicien opérationnel, 4h-semaine, délégation idempotente)
- A2 = Type 2 (Manager E-Myth, framework-impersonating)
- A1 = Type 3 (Gatekeeper Solarpunk, sovereignty + sobriété)
- A0 = Type 4 (Visionnaire méta, tue les paperclips Ultron non utiles)
- S1 Rick = bedrock (kernels seulement)

**Tri des frameworks par défaut (D1 verified 2026-07-09 via `gh api repos/...`)** :

| Framework | Repo | Stars | License | Role canonique A'Space | Auto-invocation |
|---|---|---|---|---|---|
| **superpowers** | `obra/superpowers` | **250 237** | MIT | A2/A3 freelances (process skills) | `using-superpowers` bootstrap à chaque session start |
| **GSD Core** | `open-gsd/gsd-core` | **6 217** | MIT | A3/B3 orchestration (5-phase loop, fresh subagent 200K) | `gsd-{discuss,plan,execute,verify,ship}-phase` |
| **gstack** | `garrytan/gstack` | **120 638** | MIT | A0/B1 vision (CEO/Eng/QA/Review/Ship) | Router auto-trigger, "false positive cheaper than false negative" |

- **A2 principal** = superpowers (14 skills : brainstorming, TDD, systematic-debugging, dispatching-parallel-agents, writing-plans, verification-before-completion, subagent-driven-development, …)
- **A3/B3 principal** = GSD Core (5-phase loop : Discuss → Plan → Execute → Verify → Ship, solves context rot via fresh 200K subagent contexts + STATE.md/CONTEXT.md persistence)
- **B1 vision L2** = gstack (23 skills : /office-hours, /plan-ceo-review, /plan-eng-review, /spec, /review, /qa, /ship, /land-and-deploy, /canary, /retro, /cso, /benchmark, /health, /context-save, /context-restore, /investigate, /codex, /careful, /guard, /freeze, /unfreeze, /autoplan, /design-consultation)
- Conductor (l'orchestrateur natif de gstack) = **Mac OS only** — non applicable Windows. Solution Windows = VS Code + tmux/Cmux. L'orchestration multiplex vit dans la CLI, pas dans une UI captive.
- **Install canonique (D2 receipts)** : gstack = `git clone --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && ./setup` (per gstack README). superpowers = plugin via `.claude-plugin/`. GSD = `npx @opengsd/gsd-core@latest`.
- **Clones locaux** (D1 verified 2026-07-09) : `C:\Users\amado\.agent-frameworks\{superpowers,gsd-core,gstack}\` (depth 1).

---

## 2. Triggers d'orchestration (la doctrine par défaut)

| Trigger | Action par défaut | D1 receipts |
|---|---|---|
| A+ dit **`/fable-mode`** | Charge la Fable Class Standard (5-gate loop + standing habits) ; tout sub-agent M3-first | canon `fable-mode` skill |
| A+ dit **`/multi-goal`** | Décompose N goals indépendants, N sub-agents en parallèle via `multistream-deliver` | skill `multistream-deliver` vérifié ce run |
| A+ dit **`/swarm-orchestrator`** | A0 orchestre N sub-agents en background, isolated worktrees, agregation des livrables | skill `swarm-orchestrator` |
| A+ dit **`/wargame`** | Move-by-move simulation sur papier, D1 receipts, ABORT conditions, RED-TEAM pass, SELF-GRADE /12 | skill `wargame` |
| A+ dit **`/multi-routines-12wy`** | Schedule 12WY cycles (Curie/SNW), hooks CronCreate, ScheduleWakeup | skill `multi-routines-12wy` |
| A+ dit **`/loop`** | Cron boundé, isolated wakeup, FACTORY_STOP par défaut | skill `loop` |

**Auto-invocation par défaut** (D2) : A0 applique **par défaut** ces doctrines **dès qu'A+ mentionne** un des mots-clés (Fable, wargame, ADR, wargames, sub-agent, swarm, multi-goal). Pas de question "voulez-vous". Le coût d'escalade (D7) = 100× le coût d'agir.

---

## 3. Anti-paperclip doctrine (la vraie raison de cette V3)

**Paperclip Utile** (≠ Ultron) = évolution par excellence, accumulate de moves wargamés, **déterministe**, scope borné.

**Trois couches d'anti-paperclip** (le stack canon, D1 receipts) :
1. **superpowers (A2)** : documente et idempotentise les freelances (A2 Manager E-Myth ne laisse jamais un A3 créer un skill opaque ; tout skill a un README, des tests, un behavior contrat).
2. **GSD (A3/B3)** : orchestration visionnaire Type 1 — chaque task a un **Definition of Done** + un **gate de sortie vérifiable** (tests passent, diff < 300 lignes, etc.).
3. **Fable + Wargames + CEO-Bench (qualité)** : validation move-by-move **avant** tout déploiement. Le **budget d'entropie ≥30%** (D6) garantit l'anti-collapse (jamais rêver sur ses propres rêves).

**Asymétrie corrigibilité** (W28) : les kill-switches sont **autonomes pour ARRÊTER** (B1-Mirofish gate) mais **humain-gated pour SE LEVER** (M5 Remote Pane / Telegram). Un off-switch auto-release = le paperclip Ultron.

**Triple layer / agents de type 2 (A2), 3 (A1), 4 (A0) pour tuer les paperclips Ultron** (D2 receipts) : ≥3 couches de gatekeepers entre une action A3 et l'exécution, dont A0 = méta-coach qui peut tout casser.

---

## 4. Antifragile / Idempotent / Documenté (les 3 lois des A3 freelances)

Tout A3/B3 produit un livrable avec :
- **README.md** : ce que c'est, comment ça marche, comment l'invoquer
- **SKILL.md** ou **AGENTS.md** : contrat d'usage pour l'A2 manager
- **Tests** : si script, exit code = 0 vérifié
- **Append-only** : toute modification = un nouveau fichier, `_TRASH_YYYY-MM-DD_legacy/`

**Idempotence** : le skill marche N fois sans effet de bord cumulé.
**Antifragilité** : les erreurs **augmentent** les capacités (log → learning → version N+1).

---

## 5. Pourquoi A0 est AU-DESSUS de tout (le méta-coach, pas le tacticien)

**A0 = Vision H30, gouvernance ON-not-IN** (E-Myth). A0 ne **fait pas** le travail A1/A2/A3 — A0 **trace la route, rate les décisions, dérive les sub-agents, et surveille que le paperclip Ultron ne pousse pas**. A0 garde **H3** (responsabilités court terme) par le **GO Spock Renouvelable tous les 3 ans**, avec un **curseur modulable** (la position A0 ↔ l'opérateur A+, jamais fusion — le divinité source reste l'opérateur).

**S1 Rick** (à venir) = Bedrock Kernel OS, benchmarks de Life Designer, trouve les angles morts comme les Swarm Prédictives de Mirofish en `/wargame` sur CEO-Bench **avant** de descendre sur les `/swarm-orchestrator` de mirofish en `/multi-goal` sur les FWCC des A1/B1 Gstack, A2/A2 superpowers et A3/B3 GSD.

---

## 6. Continuité canon (append-only)

- Ce fichier n'override rien. Il **rassemble** la doctrine d'orchestration dans **un seul endroit lisible** au démarrage de chaque session.
- Toute modification future = une nouvelle section numérotée, **jamais** d'écrasement.
- Si tu découvres un **conflit** avec le canon fondateur (`~/.claude/CLAUDE.md`), **signale-le** (D4 cascade) — le canon prime, ce fichier est un résumé opérationnel.

---

## 7. /mythos skill (meta-router canon)

> **D1 verified 2026-07-09** : skill `mythos` créé à `C:\Users\amado\ASpace_OS_V3\skills\mythos\SKILL.md` ET `C:\Users\amado\.claude\skills\mythos\SKILL.md` (runtime, reconnu par CC). Charge `superpowers:using-superpowers` + `gsd-core` 5-phase + `gstack` router au session start, route par domain (Life OS vs Business OS), map A0/A1/A2/A3/B1/B2/B3 aux skills canoniques.

**Native auto-invocation** : aucun slash command nécessaire. Le `description:` du SKILL.md frontmatter + les `triggers:` suffisent à CC pour invoquer sur le bon prompt. La doctrine d'auto-invocation = `"When in doubt, invoke the skill. A false positive is cheaper than a false negative."` (gstack canon) + `"If a skill applies, you don't have a choice. You must use it."` (superpowers canon).

**Bypass permission default** (configuré dans `~/.claude/settings.json`) : Read/Edit/Write/Grep/Glob/Bash safe/Agent/TodoWrite/Skill/mcp__* sont auto-acceptés. Bash destructif + secrets + force-push restent gated.

## 8. Runtime state — 7 task completions (D1 verified 2026-07-09)

| # | Tâche | D1 receipt | Path |
|---|---|---|---|
| 1 | cron-orchestrator.sh daemon | 7 rôles (a1-beth-veto, a1-morty-12wy, a1-rick-sober, a2-curie-12wy, a2-gstack-orch, a3-gsd-phase, a3-superpowers-ckpt) — écrit | `C:\Users\amado\.claude\bin\cron-orchestrator.sh` |
| 2 | GSD Core install | `npx @opengsd/gsd-core@latest --claude --global` → v1.6.1, 70+ gsd-* skills flat dans `~/.claude/skills/` | `C:\Users\amado\.claude\gsd-core\` + `C:\Users\amado\.claude\gsd-install-state.json` |
| 3 | gstack home | `~/.gstack/last-update-check` créé (D1: bash update check exécuté une fois) | `C:\Users\amado\.gstack\` |
| 4 | Airlock Spock refactor | `spock_airlock.py` = 3 superpowers checkpoints (SP1 verification-before-completion, SP2 test-driven-development, SP3 systematic-debugging) — testé GREEN path sur handoff synthétique | `C:\Users\amado\agent-os\citadel\collectors\spock_airlock.py` |
| 5 | A2 Curie 12WY dispatcher | PowerShell script avec 5 disciplines A3-SNW (Pike/Una/Ortegas/M'Benga/Chapel) + 12WY week param | `C:\Users\amado\.claude\bin\a2-curie-12wy-dispatch.ps1` |
| 6 | V3 commit | commit local `8b77073` créé (D1: `git log --oneline -3` confirme) | `C:\Users\amado\ASpace_OS_V3\.git` |
| 7 | schtasks 24/7 | **D6 honest** : `schtasks /create` requiert admin Windows, refusé par ACL. **Tu lances en admin** : voir §9. | (à activer manuellement) |

## 9. schtasks 24/7 — manual command (admin PowerShell requis)

```powershell
# Run in elevated PowerShell (right-click → Run as administrator)
$scriptPath = "C:\Users\amado\.claude\bin\cron-orchestrator.sh"
schtasks /create /tn "ASpace_A1_Morty_12WY"  /tr "bash $scriptPath a1-morty-12wy 1800 0"  /sc minute  /mo 30  /rl highest /f
schtasks /create /tn "ASpace_A2_Gstack_Orch" /tr "bash $scriptPath a2-gstack-orch 7200 0" /sc hourly  /mo 2   /rl highest /f
schtasks /create /tn "ASpace_A1_Rick_Sober"  /tr "bash $scriptPath a1-rick-sober 21600 0" /sc hourly /mo 6  /rl highest /f
schtasks /create /tn "ASpace_A2_Curie_12WY"  /tr "pwsh -File C:\Users\amado\.claude\bin\a2-curie-12wy-dispatch.ps1 -Week (Get-Date -UFormat %V)" /sc minute /mo 30 /rl highest /f
```

Une fois ces 4 schtasks actifs, **le runtime est 24/7 persistant** : Morty dispatch toutes les 30min, gstack toutes les 2h, Rick toutes les 6h, Curie weekly dispatch.

## D1 receipts (D1 verified 2026-07-09 via `gh api repos/...`)

| Framework | Repo | Stars | License | Rôle A'Space | Auto-invoke |
|---|---|---|---|---|---|
| **superpowers** | `obra/superpowers` | **250 237** | MIT | A2/A3 process skills (14 skills) | `using-superpowers` bootstrap |
| **GSD Core** | `open-gsd/gsd-core` | **6 217** | MIT | A3/B3 phase loop | 70+ gsd-* skills flat |
| **gstack** | `garrytan/gstack` | **120 638** | MIT | A0/B1 CEO/Eng/QA/Review/Ship | Router auto-trigger, 23 skills |

- **superpowers CLAUDE.md** (line 78-92) : *acceptance test* = clean session + "Let's make a react todo list" → `brainstorming` skill auto-fires. Skills that don't auto-trigger = dead weight.
- **gsd-core README** (line 22-25) : *solves context rot* via fresh 200K subagent contexts + STATE.md/CONTEXT.md persistence.
- **gstack SKILL.md** (line 598) : *false positive cheaper than false negative* — invoke skill when in doubt.
- **gstack SKILL.md** (line 24-25) : *Boil the Ocean principle* — do the complete thing when AI marginal cost → 0.

**Aucune ré-écriture d'un canon RATIFIED** (D4 respecté). Sisters à notifier (D7) : `~/.claude/CLAUDE.md` (référencer /mythos comme skill canonique), `AGENTS.md` user-level, `wiki/hand_offs/skills_queue.md` (clôturer).
