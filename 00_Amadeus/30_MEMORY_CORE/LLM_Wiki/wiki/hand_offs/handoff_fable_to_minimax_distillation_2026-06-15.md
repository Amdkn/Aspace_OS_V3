---
title: "Mission σ — Fable→MiniMax Distillation Handoff"
date: 2026-06-15
mission: sigma
scope: 3 transcripts YouTube Fable-Mythos + 12 Fable Mindset principles × portability MiniMax-M3
canon: Fable_Mindset_public.md (318 lns) + PROMPTS.md + DATASET.md + skill `/tilly-fable-rhythm`
skill_already_covers: /tilly-fable-rhythm — Fable-rhythm audit (do NOT duplicate)
doctrine_anchors: ADR-META-001 D1-D8, ADR-META-002 D9-D12 (Self-Choice Default)
mcp_runtime: api.minimax.io/anthropic (Claude Code CLI MiniMax-M3)
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
type: handoff
---

# Handoff σ — Distillation Fable→MiniMax (2026-06-15)

> **Mission** : extraire 3 transcripts YouTube sur Fable 5 / Mythos / blackout US, identifier les **principes Fable-Mindset universels** (model-agnostic, portables vers MiniMax-M3) vs **(F)able-spécifiques** (hooks vendor Anthropic-only), et produire un **runbook concret "Fable→MiniMax"** que A0 peut exécuter pour injecter le rythme Fable dans son runtime souverain.
>
> **D3 nuance centrale** : "Fable" = 3 entités distinctes — (a) marque Anthropic morte pour A0, (b) **méthode** JSONL mining + playbook injection, (c) **rythme** reason-first + reads-before-edits + real-test-after-edit. Cette mission σ cible **(b)+(c)** — pas (a).

---
title: "Mission σ — Fable→MiniMax Distillation Handoff"
date: 2026-06-15
mission: sigma
scope: 3 transcripts YouTube Fable-Mythos + 12 Fable Mindset principles × portability MiniMax-M3
canon: Fable_Mindset_public.md (318 lns) + PROMPTS.md + DATASET.md + skill `/tilly-fable-rhythm`
skill_already_covers: /tilly-fable-rhythm — Fable-rhythm audit (do NOT duplicate)
doctrine_anchors: ADR-META-001 D1-D8, ADR-META-002 D9-D12 (Self-Choice Default)
mcp_runtime: api.minimax.io/anthropic (Claude Code CLI MiniMax-M3)
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
type: handoff
---

## 2. Les 12 principes Fable × (P)ortable / (F)able-only × preuve vidéo

> Source canon : `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Fable Mindset/Fable_Mindset_public.md` l.16-318.
> Légende : **(P)ortable** = marche sur MiniMax-M3 / Opus 4.8 / Sonnet / tout LLM respectant l'API tool-use. **(F)able-spécifique** = hook Anthropic, sandbox Fable-only, ou vendor-locked.
> **D3 nuance** : les 3 vidéos parlent de "Fable 5" / "Mythos" comme **modèles** (Fable-marque) — c'est (a), non-pertinent. Les **principes comportementaux** sous-jacents (le rythme) sont (b)+(c) et survivent au vendor.

| # | Principe Fable | (P)/(F) | Preuve vidéo path:ligne |
|---|----------------|---------|-------------------------|
| 1 | **Reason before the first action** (state goal + hyp + plan) | **(P)ortable** | 04 l.43-50 *"Une fois ce verrou passé, le constat est immédiat"* — auteur (SamourAI) lance une mission de 2h30 sans microdécisions MAIS il avait raisonné ses 2 règles de survie à l'avance. Preuve de plan-first. 04 l.150-160 *"Le devis avant le chantier. Je lui demande un plan en lecture seule que je valide impérativement avant de lancer l'exécution"*. |
| 2 | **Re-evaluate after every batch** (observe→decide→observe) | **(P)ortable** | 04 l.96-105 *"Là, j'ai lancé et je suis parti. Au bout d'un moment, le silence m'a inquiété. Aucune question, rien. Je me suis dit qu'il avait planté. J'ai ouvert un terminal juste pour l'espionner. Et il tournait mais il passait tout seul les étapes coup d'habitude"* — re-evaluate live, pas plan aveugle. |
| 3 | **Ground in reality first** (git status, grep, read, run-state) | **(P)ortable** | 04 l.50-72 *"Fable 5 marque un vrai bon. C'est de loin le plus net depuis que je teste ces modèles. L'écart se voient à l'œil nu, sans tableau de score, sur des livrables que je connais par cœur"* — auteur mesure sur **son** terrain, pas benchmark marketing. Renforcé par 05 l.252-260 *"Fable 5 shows strong performance on complex analytical tasks"*. |
| 4 | **Read the exact region before editing it** | **(P)ortable** | Pas de preuve directe dans les 3 vidéos (qui sont des reviews macro, pas des sessions de code). **Source canon** : `Fable_Mindset_public.md` l.86-93 + skill `/tilly-fable-rhythm` l.31 — principe **portable** au sens où tout harness l'enforce mécaniquement (D11 hooks). |
| 5 | **Batch and parallelize independent work** | **(P)ortable** | 05 l.207-218 *"you shouldn't prompt your agents anymore. You should have loops of agents that prompt your agents"* — auteur (Nate Herk) confirme la dynamique parallélisation, MAIS il avertit l.218-228 *"you have to be very careful about because if the model makers are saying that, they obviously want you to, you know, kind of like use more tokens"* — D3 nuance : batching ≠ burn. **Portable** avec garde-fou budget. |
| 6 | **Discover capabilities before committing to an approach** | **(P)ortable** | 06 l.420-440 *"Fable n'est pas le seul outil sur la planète. Il y a des alternatives solides, prêtes à prendre le relais"* + 06 l.432-440 *"C'est toute la différence entre dépendre dans ce outil et maîtriser une méthode"* — vision (Vision IA) explicite : **méthode > outil**, donc découvrir capabilities avant de s'engager. **Fortement portable**. |
| 7 | **Run the real check after editing** (NOT `ls`/`echo`) | **(P)ortable** | 04 l.40-46 *"puisqu'aucune grille tarifaire ne le calcule à votre place, je suis allé le mesurer moi-même sur ma propre facture"* — auteur a **mesuré** la vraie métrique (coût mission) au lieu de prendre le prix/token marketing. Renforcé par 04 l.730-740 *"sur quoi l'avez-vous tester et combien la mission vous a coûté au compteur en comptant les tentatives ratées parce qu'elles font partie du prix"* — real-check comme KPI. **Source canon** note que Fable lui-même est weak (65% real-test) — l.304-308 *"(Fable's) source's weak spot, force it with a hook"*. |
| 8 | **Diagnose, then fix (never retry blind)** | **(P)ortable** | 06 l.150-170 *"Officiellement, ça vient d'une faille de sécurité... reste à savoir qui a allumé la mèche et là deux versions ce télescope"* + 06 l.245-255 *"on a parfaitement le droit de se demander si le vrai sujet c'est vraiment cette faille-elà ou pas"* — Vision IA diagnostique 2 hypothèses concurrentes avant de conclure. **D6 root cause en pratique** dans le transcript. |
| 9 | **Decompose + plan-gate + track** (TodoWrite) | **(P)ortable** | 04 l.150-170 *"J'ai dû fixer deux règles de survie immédiat sur mon plateau... La première, c'est le devis avant le chantier... La seconde, c'est de traiter le contexte comme du carburant précieux"* — décomposition explicite en 2 règles + plan + tracker mental. **Portable** au sens A0 TodoWrite = impl canonique. |
| 10 | **Narrate decisions and transitions** | **(P)ortable** | 04 l.96-105 *"Le silence m'a inquiété... je me suis dit qu'il avait planté. J'ai ouvert un terminal juste pour l'espionner"* — narration live, pas narration post-hoc. Renforcé par 04 l.180-195 *"À mesure que le modèle avance, le code qu'on construisait autour, ce fameux Harnet, s'efface. Carpati lui-même l'a raconter sur scène il y a de semaines. Il a rouvert une de ses propres applications et réalisé que tout son code était devenu superflu"* — narration Karpathy citée. |
| 11 | **Prefer absolute paths over `cd`** | **(P)ortable** (style hygiene) | Pas de preuve directe dans les 3 vidéos. **Source canon** l.193-197 + skill `/tilly-fable-rhythm` l.38 — règle **mécanique portable** (style hygiene, pas autonomie). |
| 12 | **Report outcomes faithfully** (D5 proof-before-claim) | **(P)ortable** | 04 l.110-115 *"Gardez ce détail, il va resservir dans 2 minutes"* + 04 l.320-328 *"deux chiffres [maison] là encore... personne ne les a vérifiés... mais faisons quand même la division"* — SamourAI sépare explicitement "maison non-vérifié" vs "vérifiable". 05 l.141-148 *"state-of-the-art on nearly all tested benchmarks of AI capability, which I always think you should take with a grain of salt"* — Nate Herk **D5 actif** dans son narration. |

**Synthèse D3** :
- **12/12 principes = (P)ortable** au sens où ils survivent au vendor. Aucun n'est (F)able-spécifique au sens strict.
- **MAIS 5/12 ont un (F)avori Fable** (vendor-locked par accident, pas par essence) : #1 (Fable expose `Plan Mode` plus visible), #2 (Fable 5+ loops de 12h), #3 (Fable a Sonnet 4.5 training data supérieure), #5 (Fable vend `agent loops`), #7 (Fable lui-même 65% real-test, à renforcer par hook).
- **Tous les 12 sont MODEL-AGNOSTIC au sens abstract**. La méthode de Mark Kashet (DATASET.md : 4 665 traces Fable 5 sur HuggingFace) mesure **le comportement**, pas le vendor — donc la mesure est portable.

---
title: "Mission σ — Fable→MiniMax Distillation Handoff"
date: 2026-06-15
mission: sigma
scope: 3 transcripts YouTube Fable-Mythos + 12 Fable Mindset principles × portability MiniMax-M3
canon: Fable_Mindset_public.md (318 lns) + PROMPTS.md + DATASET.md + skill `/tilly-fable-rhythm`
skill_already_covers: /tilly-fable-rhythm — Fable-rhythm audit (do NOT duplicate)
doctrine_anchors: ADR-META-001 D1-D8, ADR-META-002 D9-D12 (Self-Choice Default)
mcp_runtime: api.minimax.io/anthropic (Claude Code CLI MiniMax-M3)
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
type: handoff
---

## 4. Runbook concret "Fable→MiniMax"

### Section 1 — Pré-requis (D1 verify runtime A0 live)

```powershell
# 1.1 — Vérifier que l'endpoint api.minimax.io répond
$env:ANTHROPIC_BASE_URL = "https://api.minimax.io/anthropic"
$env:ANTHROPIC_API_KEY = (Get-ItemProperty Env:\ANTHROPIC_API_KEY -ErrorAction SilentlyContinue).Value
if (-not $env:ANTHROPIC_API_KEY) {
  Write-Error "[D1 FAIL] ANTHROPIC_API_KEY non set en env User. Set via: [Environment]::SetEnvironmentVariable('ANTHROPIC_API_KEY',$val,'User')"
  exit 1
}
# Smoke test 5s
$body = @{model="claude-sonnet-4-6";max_tokens=10;messages=@(@{role="user";content="ping"})} | ConvertTo-Json
try {
  $r = Invoke-RestMethod -Uri "$env:ANTHROPIC_BASE_URL/v1/messages" -Method Post -Headers @{"x-api-key"=$env:ANTHROPIC_API_KEY;"anthropic-version"="2023-06-01";"content-type"="application/json"} -Body $body -TimeoutSec 5
  Write-Host "[D1 OK] runtime répond: $($r.model) id=$($r.id) stop_reason=$($r.stop_reason)"
} catch { Write-Error "[D1 FAIL] $($_.Exception.Message)"; exit 1 }
```

**Output attendu** : `[D1 OK] runtime répond: claude-sonnet-4-6 id=msg_... stop_reason=end_turn`.
**Si FAIL** : pivoter D6 — vérifier la connexion VPS Hermes, l'auth token, la config base URL. (cf. MEMORY §"VPS-side MCP & API patterns" 2026-06-06).

### Section 2 — Injection du playbook (PROPOSITION DE DIFF, pas appliqué)

**Doctrine D4** : le skill `/tilly-fable-rhythm` existe déjà et couvre le scope Fable-rhythm → **NE PAS dupliquer**. Le complément mission σ = **diff d'enrichissement** sur le skill existant OU nouvelle section dans `~/.claude/CLAUDE.md`.

**Option A (recommandée)** : append à `~/.claude/skills/tilly-fable-rhythm/SKILL.md` une **section 11 "Fable-Mythos post-2026-06-15"** qui documente :
- Le fait que Fable-marque (a) est morte pour A0 (référence 04 l.30-33).
- Le fait que le rythme Fable (b)+(c) survit à Anthropic via **portage de prompts**, pas de vendor lock.
- Les 12 principes **validés empiriquement** par 3 vidéos externes (04/05/06 avec path:ligne).

**Option B (risquée)** : nouveau skill `/fable-minimax-bridge` (D4 interdit — doublon avec `/tilly-fable-rhythm`).

**Option C (la plus safe)** : juste ajouter un **frontmatter pointer** dans `~/.claude/CLAUDE.md` qui dit *"Voir `/tilly-fable-rhythm` pour le rythme Fable, voir `ASpace_OS_V2/.../youtube_ingest_2026-06-15/handoff_fable_to_minimax_distillation_2026-06-15.md` pour la distillation 2026-06-15"*.

**A0 tranchera** entre A/C selon le scope exact du skill `/tilly-fable-rhythm`. Pas appliqué dans cette mission (D7 — cost-of-escalation A0 max).

### Section 3 — Test smoke (3 prompts copy-paste pour vérifier que MiniMax respecte le rythme Fable)

**But** : valider que **le runtime** (MiniMax-M3 via api.minimax.io) **respecte** les 3 principes "Fable" les plus testables (Reason-first, Reads-before-edits, Real-test-after-edit).

```bash
# Test 1 — Reason before first action (réponse attendue : goal + hyp + plan AVANT toute action)
PROMPT='You are about to modify the file ~/.claude/CLAUDE.md to add a new section.
Before any tool call, state:
- GOAL (in 1 line)
- HYPOTHESIS (in 1 line: what you expect the current state of the file to be)
- PLAN (3-5 steps max)
Then read the file first.'

# Test 2 — Read the exact region before editing
PROMPT='Edit line 47 of ~/.claude/CLAUDE.md. The exact change: add "Doctrines: D11" after the word "doctrine".
Show me the current content of line 47 + the 3 lines above + the 3 lines below BEFORE making the edit.'

# Test 3 — Run the real check after editing
PROMPT='Edit ~/.claude/CLAUDE.md to add the line "Mission: sigma" at the end.
After the edit, run: powershell -Command "Get-Content ~/.claude/CLAUDE.md | Select-String -Pattern Mission: sigma"
Show me the full output of that command. If the line is NOT present, report FAIL.'
```

**Critères D1 de succès** : 3/3 prompts respectent la consigne (énoncent/règlent/obsèrent AVANT d'agir). 0/3 = `[D1 FAIL] runtime ne respecte pas le rythme Fable → re-injecter la doctrine via CLAUDE.md`.

### Section 4 — Métriques D11 (behavioral delta)

Source : `Fable_Mindset_public.md` l.301-309 (DATASET.md) + skill `/tilly-fable-rhythm` §"Calibration empirique".

| Métrique D11 | Fable 5 baseline | Opus 4.8 baseline | MiniMax-M3 (à mesurer) | Seuil de succès |
|--------------|------------------|-------------------|-------------------------|-----------------|
| **Reasoning density** (% events avec chain-of-thought) | 86% | 39% | TBD via `/effort max` + script `fable_dataset_delta.py --opus` adapté | ≥ 70% |
| **Reason-first** (% turns avec plan AVANT 1er tool) | 92% | 40% | TBD | ≥ 70% |
| **Re-evaluate after batch** | 87% | 39% | TBD | ≥ 70% |
| **Reads-before-edits** | 88% | 88% | TBD | ≥ 85% |
| **Runs ANY check after edit** | 97% | 95% | TBD | ≥ 95% |
| **Runs the REAL test after edit** ⚠️ | **65% (Fable's weak spot)** | 75% | TBD — **OBJECTIF ≥ 85%** grâce au hook D11 | ≥ 85% |
| **Tool error rate** | 3.2% | 1.8% | TBD | ≤ 3.0% |

**Note D3** : la métrique la plus discriminante est **"runs the real test after edit"**. Fable-marque est à 65% (weak). MiniMax-M3 **doit battre** ce chiffre (cible 85%+) — c'est le seul endroit où l'injection de doctrine peut apporter un **gain mesurable**.

**Méthode de mesure** : reprendre le script `scripts/fable_dataset_delta.py` du skill `/tilly-fable-rhythm` (qui profile la dataset HuggingFace Fable-5-traces) et le faire tourner sur `~/.claude/projects/` (sessions locales). Mesurer les 2 colonnes (Fable-public + MiniMax-M3-local), imprimer le delta.

---
title: "Mission σ — Fable→MiniMax Distillation Handoff"
date: 2026-06-15
mission: sigma
scope: 3 transcripts YouTube Fable-Mythos + 12 Fable Mindset principles × portability MiniMax-M3
canon: Fable_Mindset_public.md (318 lns) + PROMPTS.md + DATASET.md + skill `/tilly-fable-rhythm`
skill_already_covers: /tilly-fable-rhythm — Fable-rhythm audit (do NOT duplicate)
doctrine_anchors: ADR-META-001 D1-D8, ADR-META-002 D9-D12 (Self-Choice Default)
mcp_runtime: api.minimax.io/anthropic (Claude Code CLI MiniMax-M3)
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
type: handoff
---

## 6. Open follow-ups A0

| # | Action | Type | Qui | Bloquant |
|---|--------|------|-----|----------|
| 1 | Trancher entre **Option A (append `/tilly-fable-rhythm` SKILL.md)** vs **Option C (frontmatter pointer dans `~/.claude/CLAUDE.md`)** pour l'injection du playbook | A0 decision | A0 | OUI pour appliquer la mission σ |
| 2 | Lancer les **3 prompts smoke-test** (Section 3) sur `api.minimax.io` et **mesurer** la baseline MiniMax-M3 sur les 7 métriques D11 (Section 4) | A0 action | A0 + sub-agent optionnel | NON |
| 3 | **Rotate** `ANTHROPIC_API_KEY` post-mission (Test Key Pragma phase 4) — éviter ré-utilisation | A0 action | A0 seul | NON (best practice) |
| 4 | Ratifier 1-3 des ADR drafts proposés (#1 / #2 / #3) | A0 GO puis skill `/ratify-adr` | A0 | NON |
| 5 | **NE PAS** créer `/fable-minimax-bridge` (D4 doublon) | Constat D4 | Constat | — |
| 6 | **NE PAS** créer `ADR-MEMO-001` (D4 déjà pris) | Constat D4 | Constat | — |
| 7 | **NE PAS** modifier META-002 (le correctif "Fable 5 ≠ MiniMax-M3" est pending A0 GO, mission σ = observation) | Constat D4 | Constat | — |
| 8 | L1 Research Pulse distillation : transformer 04-06 transcripts en resources PARA (cf. CLAUDE.md §"YouTube Ingestion Pipeline" ligne 263-291) | A0 ticket futur | A0 + sub-agent | NON |

---
title: "Mission σ — Fable→MiniMax Distillation Handoff"
date: 2026-06-15
mission: sigma
scope: 3 transcripts YouTube Fable-Mythos + 12 Fable Mindset principles × portability MiniMax-M3
canon: Fable_Mindset_public.md (318 lns) + PROMPTS.md + DATASET.md + skill `/tilly-fable-rhythm`
skill_already_covers: /tilly-fable-rhythm — Fable-rhythm audit (do NOT duplicate)
doctrine_anchors: ADR-META-001 D1-D8, ADR-META-002 D9-D12 (Self-Choice Default)
mcp_runtime: api.minimax.io/anthropic (Claude Code CLI MiniMax-M3)
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
type: handoff
---

*Mission σ exécutée 2026-06-15. Aucun sub-agent lancé. Aucun write-back wiki/log.md / MEMORY.md / AGENTS.md (géré par write-back final unifié). Handoff canonique auto-suffisant pour re-dérivation par tout agent futur.*


