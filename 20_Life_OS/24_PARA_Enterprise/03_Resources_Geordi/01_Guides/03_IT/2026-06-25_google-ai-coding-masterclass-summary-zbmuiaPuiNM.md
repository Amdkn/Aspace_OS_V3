---
domain: 03_IT
ld: LD07_Creativity_Reno
b2_owner: cyborg-it
sister_b1: jerry-prime
b1_filter: APPLIED_E1_DETERMINISTIC (sweep 2026, ADR-L2-BDLD-MAP-001 D3)
---
# Guide PREMIUM — Google's AI Coding Masterclass (synthèse Cole Medin)

> **video_id**: `zbmuiaPuiNM`
> **url**: https://youtu.be/zbmuiaPuiNM
> **channel**: Cole Medin (synthèse d'un article Google "AI-Driven SDLC", ~51 pages)
> **transcript raw**: `01_Guides/_transcripts_raw/zbmuiaPuiNM.md` (24 382 chars)
> **domaine**: `03_IT` — génie logiciel, agentic engineering, harness
> **horizon**: H30 (apprentissage continu) — utile aussi en H1 daily-build
> **daté**: 2026-06-25

---

## 1. Concepts glossaire (5-6)

### 1.1 SDLC (Software Development Life Cycle)
"the process to go from idea all the way to production. So, requirement gathering at the start all the way to review, deployment, and maintenance." Le SDLC n'est **pas** juste "écrire du code" — il englobe le front-loaded (PRD, stakeholder meetings, design) **et** le back-loaded (testing, review, deploy, maintenance). Dans le SDLC piloté par IA ("AI-driven SDLC"), les deux extrémités restent humaines et lentes ; seul **le milieu** (implémentation) devient "minutes or hours" au lieu de "weeks". **Le nouveau goulot d'étranglement, c'est la qualité des spécifications.**

### 1.2 Spectrum (pas binaire)
"AI coding is a spectrum, not a switch." Trois niveaux, **à choisir selon le job** (pas une progression morale) :
- **Vibe coding** — "prompt sans beaucoup de planning, validation 'does it seem to work'". Spec = casual natural language. Vérif = superficielle. **Risque élevé**, acceptable pour POC/MVP jetables.
- **Structured AI-assisted** — prompts détaillés + spot-checking manuel. Spec plus riches, vérif intermédiaire.
- **Agentic engineering** — "entire engineered set of resources and workflows": specs **ingénierées comme le code**, automated evals, CI gates, LLM judges, code review par agent séparé. **C'est ici que vit la fiabilité.**

### 1.3 Harness (90% du système)
"the set of context, rules, tools, and workflows that you bring into the AI coding assistant." **Le LLM = 10%. Le harness = 90%.** C'est ce qu'on **contrôle** (le modèle, on ne le contrôle pas). Primitive canonique du harness (cf. Anthropic cloud-code best practices, repris par Google) :
- **Global rules** (CLAUDE.md / instructions système)
- **Hooks** (actions déterministes dans le lifecycle)
- **Skills** (workflows packagés, chargé à la demande)
- **MCP servers** (outils externes)
- **Sub-agents** (rôles spécialisés)

**Preuve empirique citée** : "terminal bench 2.0… Lane chain was able to increase it 13.7 points. Like that's the difference between Sonnet and Opus. Like you can make sonnet work as well as Opus if you have the right system."

### 1.4 Static vs Dynamic Context
- **Static context** = "loaded into the coding agent session guaranteed every single time" (system prompt, rules core, guardrails). **Fiable mais coûteux** (ça remplit le window up-front). **Doit rester lean.**
- **Dynamic context** = "information that the agent has to actually seek out" (skills, conventions par partie du code, RAG search). **Efficace et scalable**, mais risque que l'agent ne le charge pas au bon moment.

**Leçon canonique** : *"rather than embedding every piece of specialized knowledge into the agent system prompt, skills allow the agent to remain a lightweight generalist that flexes into specialist roles on demand through progressive disclosure."* Donc **un seul agent généraliste + skills à la demande** > multi-agents spécialisés en dur. L'industrie converge vers ça.

### 1.5 Factory Model
"we are responsible for designing the system, creating the harness and then the agent is the one that is actually producing our code and documentation." Pattern récurrent : `plan → build → quality gates (test + eval) → iterate → human review → ship`. Le rôle humain = designer du système, pas écrivain de code.

**Variante critique** : **deux sessions agent séparées** — un planning agent (accumule contexte, biais), un coding agent (reçoit le plan comme artefact, code dans sandbox). Évite le **context rot** (l'agent qui s'écrase sous son propre historique).

### 1.6 Conductor vs Orchestrator
- **Conductor** = "we had our tab complete. We're still steering every move, working in individual files." (= ancien mode, prompt-by-prompt)
- **Orchestrator** = "coding agent handling much larger tasks spanning entire code bases… agents running in parallel. We're really scaling our output."

**Note de Cole (désaccord partiel)** : "I don't think you're always moving between the two. I think… when you build the harness to be reliable enough and you're confident in your rules and workflows, you can always live at this level [orchestrator]." Donc : **le conductor est un état transitoire**, on en sort quand le harness est mûr. C'est un **graduation event**, pas une alternance perpétuelle.

---

## 2. Outillage matrice (3-5)

| Composant harness | Outil canonique | Quand l'activer | Anti-pattern |
|---|---|---|---|
| **Global rules** | `CLAUDE.md` à la racine + `.claude/rules/` | Day 0 du projet. Lean, exemples canoniques, anti-patterns. | Mur de 800 lignes que l'agent skimme et ignore. |
| **Skills** (workflows packagés) | Skills dans `~/.claude/skills/<name>/SKILL.md` | Quand un workflow se répète ≥3× ou checklist ≥5 étapes. Progressive disclosure = chargé à la demande. | Tout mettre en static context ⇒ context rot. |
| **MCP servers** | `.mcp.json` + tools scopés par projet | Besoin d'API externes (Notion, Supabase, transcript, DNS, Vercel). Auth User scope. | `--y npx` volatile → préférer `.cmd` globaux (D6 lesson MCP persistence v2). |
| **Hooks** (PreToolUse / PostToolUse) | `settings.json` hooks section | Lifecycle déterministe : format on save, log D1 receipts, blocker destructif. | Trop de hooks = friction + faux positifs (Sobriété Rick : 2/4 hooks ship, 2 veto). |
| **Sub-agents** (rôles) | `~/.claude/agents/<name>/agent.md` | **Quand la skill ne suffit plus** (besoin d'un contexte isolé long-running). | Multi-agents rigides en hard = anti-pattern (cf. §1.4 — préférer 1 généraliste + skills). |
| **CI gates / evals** | GitHub Actions + evals JSON | Quality gate post-agent. Bloquant avant merge. | Skip les evals = "vibe coding déguisé en agentic". |

**Outil sponsorisé dans la vidéo** : **Better DB** — semantic cache + observability pour agents en prod (open-source). À considérer pour le layer "observability/tracing" du harness (§1.3 couche supérieure).

---

## 3. Perspective Souveraine ASpace (200+ mots)

**Le harness EST le canon.** Pour A'Space OS V2, on ne "code" plus — on **ingénière un harness qui contient le canon, les skills, les hooks, les MCP, les agents, les evals**. Le harness est *"an engineered resource that lives in version control just like the code itself"* — exactement la doctrine que Beth (Ikigai) et Morty (Focus) appliquent déjà : `CLAUDE.md` = static canon, `MEMORY.md` = static canon, `wiki/` = static canon indexé, `skills/` = dynamic progressive disclosure, `agents/` = dynamic sub-roles.

L'erreur du passé (avant 2026-06-21) était de croire qu'on "buildait des agents spécialisés en dur" — exactement le pattern que Google *et* Cole condamnent : *"people used to do way too much before is they would have these really complicated multi-agent systems with all these specialists."* Dans A'Space, le passage de **35 A3 hard-codés** (legacy v0, archivés en `_TRASH_2026-06-15_legacy_v0/`) à **35 A3 dynamiques + skills à la demande** est précisément cette migration. Le jumelage A0 ↔ A (2026-06-21) est le **conductor qui devient orchestrator** : on ne tape plus chaque action B3 technicien, on cadre l'intention A0 et le harness (Claude Code A2 + skills + MCP + hooks) exécute.

**Sobriété check (Rick C137)** : la tentation est d'ajouter toujours plus de hooks, plus de skills, plus d'agents — c'est le **paperclip maximizer du harness**. La doctrine SOBER-002 dit *"high capital expenditure… scales extremely well because the output of your AI coding assistants are better and better over time"* — donc on investit upfront dans **un harness lean**, puis on l'**évolue** (system evolution mindset : *"where could we make our workflows or our rules… better so that issue is less likely to come up again?"*). C'est l'inverse exact du vibe coding jetable.

**Concrètement pour A'Space** : (a) **garder `CLAUDE.md` lean** — déléguer le détail aux skills/memory files (déjà fait via junction `wiki/`), (b) **audit harnais Vague 2** (2026-06-21 : 2/4 hooks ship, 2 Rick veto) = Sobriété appliquée, (c) **investir le ROI des skills canon-batch-spawn** (-86% sur 1 sprint, sister-ADRs × N) dans le harness plutôt que dans des agents one-shot.

---

## 4. DEAL (4 phases)

### D — Define
**Friction réelle** : Cole passe des semaines à expliquer l'agentic engineering ; Google écrit 51 pages ; tout le monde ré-derive la même architecture harness. **Outcome désiré** : un mental model + une terminologie commune pour "comment on ingénieurie le harness IA", partageable entre A0 (jumeau), A1 (gatekeepers), A2 (engines), A3 (twins).

### E — Eliminate
**Kill** :
- La croyance "AI coding = vibe coding OR agentic engineering" (binaire faux → spectrum)
- La croyance "le modèle compte à 100%" (faux — 10%, harness = 90%)
- L'idée de "toujours bouger entre conductor et orchestrator" (faux — graduation, pas alternance)
- L'instinct "créer plus d'agents spécialisés" (anti-pattern — 1 généraliste + skills)
- La vérification superficielle "does it seem to work" sur du code prod-bound

**Garde** :
- Le POC/MVP vibe coding **quand le code est jetable**
- Le debugging granulaire **quand l'orchestrator ne suffit pas**
- Les skills spécialisées **dynamiques** (≠ agents en dur)

### A — Automate
- **Skill `/canon-batch-spawn`** (déjà live 2026-06-24, ROI -86%) → automating sister-ADR creation
- **Skill `/graphify-swarm-burst`** → automating knowledge graph builds (251 MB corpus, 9.5s merge)
- **Skill `/youtube-to-guide`** (celle que tu lis) → automating transcript → premium guide pipeline
- **Hooks Vague 2** : PostToolUse rotation 7j + SubagentStart throttle 1/10 (déjà ship)
- **MCP `transcript-api`** : thin stdio↔HTTPS JSON-RPC forwarder (pattern "thin proxy over OAuth-discovery MCP")

### L — Liberate
**Bande passante libérée** : A0 n'a plus besoin d'expliquer 51 pages à chaque nouvel agent / session — le harness encode le canon. Le coût d'escalade D7 (A0 escalation ~100×) baisse drastiquement parce que **les agents ont le contexte dès le system prompt**.

**Métrique D11 (Gwyn Liberate)** : mesurer "avant vs après" — combien d'explications redondantes A0 a-t-il dû fournir en Q2 2026 vs Q3 2026 ? Cible : -70% sur les 4 frameworks Life OS canoniques (Ikigai, Life Wheel, 12WY, PARA, GTD, DEAL).

---

## 5. Token economics (le crossover capital/opex)

> "at first when you're first adopting AI coding assistance… vibe coding is going to be cheaper. It's lower capital expenditure because you don't have to dedicate yourself or a team to design the initial harness. But the problem is it's very high operational expenditure because you start burning through millions and millions of tokens iterating on slop code."
>
> "agentic engineering… has that high capital expenditure because you have to dedicate your time up front… but then it scales extremely well… you want to just take the dive and build that system up front because… agentic engineering is **three to 10 times more reliable and cheaper** than vibe coding."

**Trade-off canon** :
| Mode | CapEx (initial) | OpEx (running) | Quand |
|---|---|---|---|
| **Vibe coding** | Bas (juste un prompt) | Haut (brûle tokens sur slop) | POC, MVP, code jetable |
| **Agentic engineering** | Haut (build harness) | Bas (système évolue, ROI cumulatif) | Prod, scaling, organisation |

**Pour A'Space** : on est **deep dans la zone CapEx agentic engineering** depuis 2026-06-21 (jumelage A0↔A + 35 skills canon + 5/5 smoke tests hooks + 4 SaaS Cloud MCPs live). Le crossover est **derrière nous**. Mesurer l'OpEx descendant maintenant — c'est le **D11 Fable score** que Chapel (A3 SNW H10) owns.

---

## 6. Spec quality is the new bottleneck

> "the specification quality is the new bottleneck."

C'est **la phrase la plus importante de la vidéo**. Si le front-loaded (spec) et le back-loaded (validation) restent humains, et que **la qualité de la spec** est le nouveau goulot, alors :

**Doctrine A0↔A alignée** :
- **Front-loaded** = `CLAUDE.md` + skills + MEMORY.md = spec canonique du harness A'Space. A0 émet l'intention → A0 ne tape plus la spec au kilomètre, elle est dans le canon.
- **Back-loaded** = validation = evals + CI gates + code review + smoke tests. Hooks Vague 2 = deterministic validation, pas humaine.

**Le piège** : croire que "mieux spec = plus de spec". Faux. **Mieux spec = spec lean + canon indexé** (juncion `wiki/`, junction `graphify-out-master`). Le harnais lean est **plus fiable** qu'un mur de 800 lignes que l'agent skimme.

---

## 7. System evolution mindset (le meta-loop)

> "Whenever you encounter an issue with your AI coding assistant… instead of just fixing the bug and moving on, you actually talk to your coding agent like you have it do some retrospection and say, 'where could we make our workflows or our rules… better so that issue is less likely to come up again?'"

**Boucle de feedback** :
1. Issue rencontré → fix immédiat
2. Rétrospection : *pourquoi le harnais n'a pas catch ça ?*
3. Amélioration du harnais (rule / skill / hook / eval)
4. Commit en version control
5. Issue moins probable la prochaine fois

**C'est exactement le pattern A0↔A twin digital** : chaque handoff D4 append-only dans `wiki/hand_offs/` est une amélioration du harnais. D6 Catalog (ADR-META-006, 2026-06-23) = system evolution mindset formalisé.

**Pour OpenClaw Heartbeat / A3 LEARN step** : ce mindset EST le Phase 2 Hermes-style self-improvement. *"the cost of false-positive skill creation (~5 min) << cost of A0 escalation (~100x)"* — donc on crée la skill en autonomie, on ne demande pas GO à A0.

---

## 8. Annexes

### Annexe A — Les 5 primitives du harness (verbatim Cole)

> "It's your global rules. It's your hooks like the deterministic actions you want in your life cycle your skills. So, the workflows that you have packaged up, uh, your ways that you search your codebase, the MCP servers, and your sub agents, like these are all of the primitives, as I call them, for working with literally any AI coding assistant."

### Annexe B — Diagramme harness en 3 couches (Google)

```
┌─────────────────────────────────────────────┐
│  Top layer : observability + tracing         │  ← production
│              + scaling                       │
├─────────────────────────────────────────────┤
│  Middle layer : eval infrastructure          │  ← iterate autonome
│                  (CI gates, tests, judges)    │
├─────────────────────────────────────────────┤
│  Core layer : LLM (10%)                      │
│               + harness (90%) :               │
│               - instructions (CLAUDE.md)      │
│               - MCP servers                   │
│               - guardrails                    │
│               - hooks                         │
│               - skills                        │
└─────────────────────────────────────────────┘
```

### Annexe C — Comparaison 3 niveaux (verbatim table Google)

| Dimension | Vibe coding | Structured AI-assisted | Agentic engineering |
|---|---|---|---|
| **Spec intensity** | casual NL prompts | detailed prompts | engineered specs (repeatable process) |
| **Verification** | "does it seem to work" | manual testing, spot-checking | tests + CI/CD + LLM judges + 2nd-agent code review |
| **Risk profile** | high (disposable only) | medium | low (systematic verification) |

### Annexe D — Crossover math (rough order)

| Horizon | Vibe cost (cumul) | Agentic cost (cumul) | Ratio |
|---|---|---|---|
| Semaine 1 | $50 (LLM API) | $500 (harness build) | 10× plus cher agentic |
| Mois 1 | $5K (slop iterations) | $1.5K (harness + lean iterations) | 3.3× moins cher agentic |
| Trimestre 1 | $50K (still slop) | $5K (harness + lean) | **10× moins cher agentic** |
| Année 1 | $200K+ (pas de scaling) | $15K (system evolution) | **13× moins cher agentic** |

(Estimations indicatives — chiffres réels = LLMs API cost + token counts à mesurer via Better DB semantic cache.)

### Annexe E — Liens canoniques A'Space

- `wiki/hand_offs/handoff_a0_jumeau_numerique_2026-06-21.md` — twin digital, conductor→orchestrator graduation
- `_SPECS/ADR/L1_Life_OS/ADR-META-005_hooks-automation.md` — hooks Sobriété scope (2/4 ship, 2 Rick veto)
- `_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md` — system evolution mindset formalisé
- `_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md` — sobriété kernel
- `MEMORY.md` §"Doctrine Anti-Paresse" — D1-D8 (Verify, Research, Nuance, No-Contradiction, Proof, Root-cause, Cost-of-Escalation, Cross-agent)
- Skill `/canon-batch-spawn` (2026-06-24) — automating sister-ADR canon
- Skill `/youtube-to-guide` (celle-ci) — transcript → premium guide
- Skill `/graphify-swarm-burst` — knowledge graph 251 MB corpus, 9.5s merge

---

*Guide généré via /youtube-to-guide v3 (Antigravity Premium Standard) — pipeline Cole Medin synthesis of Google AI-Driven SDLC.*