---
source: youtube-takeout-to-lifeos
date: 2026-06-21
type: video-resource
ld: LD04_Cognition_Tilly
ld_domain: Cognition
a3_owner: Tilly
video_id: oGE_Dwz-rMk
title: "Omnigent: The New Meta-Harness for EVERY Coding Agent — Claude Code, Codex, Pi, More"
author: Cole Medin
channel: "Cole Medin"
watch_url: https://www.youtube.com/watch?v=oGE_Dwz-rMk
raw_date: "21 juin 2026"
status: CAPTURED
tags: [#youtube, #geordi, #ld04, #life-wheel, #meta-harness, #orchestration, #claude-code, #codex, #pi, #omnigent, #databricks]
a0_cycle: "12WY Q3 2026 — Item 5 (YouTube → PARA Resources)"
a0_doctrine_link: "/multi-backend skill"
---

# Omnigent: The New Meta-Harness for EVERY Coding Agent

> **Channel**: Cole Medin
> **Watched**: 21 juin 2026 (2026-06-21)
> **LDxx**: LD04_Cognition_Tilly
> **URL**: https://www.youtube.com/watch?v=oGE_Dwz-rMk

## Résumé (200 mots)

Omnigent est un **meta-harness open-source** (par Databricks, dirigé par leur CTO, dogfooded en interne) qui orchestre plusieurs agents de codage IA (Claude Code, Codex, Pi, Kimmy, Ollama local) au-dessus d'une couche unique. La thèse centrale : **avec la récente mise à l'écart de Fable 5, on ne peut plus compter sur les LLMs pour s'améliorer** — il faut rendre le **système autour du LLM** plus puissant. Le harness (system prompt + tools + skills + rules + workflows) compte autant, voire plus, que le modèle. Le meta-harness est la couche AU-DESSUS qui orchestre plusieurs harnesses ensemble pour des workflows longs. Deux exemples "ship-in-a-box" : **Paulie** (Claude implémente, Codex review) et **Debbie** (deux agents argumentent, orchestrateur synthétise). Setup en <10 minutes via commande unique. Custom agents via primitives : executor + skills + agents délégués + guardrails Python + sandbox (Docker/E2B). **Human-in-the-loop** natif pour actions dangereuses (force-push). Session partagée cross-device. **Le point clé** : faire la code review dans une session séparée réduit le biais du LLM.

## Why this is in LD04_Cognition_Tilly (D3 nuance)

**LD04 Cognition Tilly** — pas LD01 Business Book. Raison D3 :
- Sujet = **orchestration d'agents cognitifs** (comment penser AVEC plusieurs IA), pas stratégie business
- Pattern canonique LD04 (NotebookLM agentic, Antigravity SDK, Caching problem AI agents) = cognition orchestrative pure
- Book LD01 traiterait si : workflow Omnigent appliqué à un deal commercial, ROI OMK ABC, monétisation de l'orchestration
- Tilly = ship's scientist (LD04 Cognition officer, H30 = 30-day learning arc) — exactement le bon twin pour ce type de ressource cognitive
- Cross-ref DIRECT avec **H30 horizon** (30-day learning arc) : Omnigent accélère l'apprentissage en distribuant les biais

## 5-10 Bullets Insights (français)

1. **Le harness compte autant que le modèle** : avec Fable 5 écarté, on ne peut plus compter sur "le prochain meilleur LLM". L'effort d'ingénierie doit aller dans le **système autour du LLM** (system prompt + tools + skills + rules + workflows). Pattern OpenHarness/Symphony déjà ancré chez A0 — Omnigent valide cette thèse à l'échelle industrielle (Databricks).

2. **Code review dans une session séparée = anti-biais fondamental** : "Si on ne fait pas ça, le LLM construit trop de biais" (Cole Medin). Pattern : **Claude implémente, Codex review** dans 2 sessions distinctes, orchestrateur supervise. C'est exactement ce que A0 fait déjà avec ses propres sessions (`aliases.current.sessionPath`).

3. **Meta-harness = couche d'orchestration au-dessus des harnesses** : primitives simples = (config + skills + agents délégués). Chaque agent sub-délégué peut avoir son propre executor (Claude/Codex/Pi), guardrails, sandbox. **Debbie** orchestre un débat Claude vs GPT (2 rounds + synthèse) — équivalent canonique de notre **multi-perspective analysis** pattern (agents.md §"Multi-Perspective Analysis").

4. **Setup en <10 minutes, dogfooded par Databricks en prod** : CTO-driven, utilisé par leur équipe engineering au quotidien. Open-source, credentials réutilisés depuis CLI existants. Pattern "ship-in-a-box" = preuve de viabilité pour A0 d'envisager sérieusement d'intégrer ce genre de couche au-dessus de son **Harness Claude Code existant** plutôt que de tout réécrire.

5. **Human-in-the-loop natif pour actions dangereuses** : guardrails Python co-localisés avec config agent. Exemple : bloquer force-push par défaut, exiger approbation humaine. **C'est exactement ce qu'ADR-META-001 D7 appelle "coût d'escalade A0"** — Omnigent formalise ce pattern avec primitives natives.

6. **Cross-device sync + session partagée** : tu commences sur desktop, tu continues sur phone. Implications pour A0 : pourrait potentiellement avoir un agent qui le suit cross-device (mais watch out pour le **paradoxe surveillance** vu dans la doctrine TTS).

7. **Sandbox flexible** : Docker local pour dev, E2B pour prod. Sécurise l'exécution sans bloquer l'agent. Combiné avec les guardrails Python = "policy-as-code" au niveau agent.

8. **Custom agents générés par l'agent lui-même** : Cole Medin n'a PAS écrit le code Python de son custom agent — il a juste demandé à son AI coding assistant "look at Paulie and Debbie, build me this". **Pattern agentic-self-replication** = exactement ce que `/multi-backend` skill vise à permettre pour A0.

## Citations verbatim (transcript)

> [0:00-0:24] *"There is a new open-source tool that was released just over the weekend. It's called Omni Agent. And we're going to unpack this today because it is a very powerful and free-to-use meta harness."*

> [0:47-1:00] *"A meta harness is a tool that allows you to run longer AI coding workflows, mixing AI coding assistance. And so the most classic example that people really like right now is using Claude Code for the implementation in a workflow and then reviewing that code with Codex."*

> [1:30-1:45] *"If there's one lesson we can learn this year for AI coding, it's that the harness matters as much as or maybe even more than the model. And it's even more apparent right now with the recent ban of Fable 5."*

> [2:00-2:15] *"If the LLM can't get better, then we better make the system around the LLM more powerful. See, your harness is everything like your system prompt, tools, skills, workflows, rules, all of that together packaged up is our harness for making a single AI coding assistant more reliable for us."*

> [2:15-2:35] *"The meta harness. This is what a lot of people are really starting to lean into right now. This is the next big thing for AI coding. Instead of making one coding agent better, what if we have the layer above that orchestrates many AI coding assistants working together on larger tasks?"*

> [3:50-4:10] *"I had this up and running in like literally less than 10 minutes. I was able to run this workflow going between Claude and Codex so easily. And I know this is a pretty simple example of orchestrating a larger AI coding workflow, but it is very important, at least at a very fundamental level, to do your code review in a separate coding agent session from your implementation. Otherwise, the LLM builds up way too much bias."*

> [4:25-4:50] *"I would encourage you to just try it, especially because of how easy it is with Omni Agent to run this kind of thing now."*

> [11:30-11:50] *"What I want to show you really quickly is how we can work in the same session both on our phones and on our computer. And you can do this across the internet. So, you can work with people across the globe as well."*

## Patterns cross-agent (D8)

| Pattern Omnigent | Équivalent A'Space | Statut |
|------------------|---------------------|--------|
| **Code review dans session séparée** | `aliases.current.sessionPath` + doctrine "Test Key Pragma" (sessions séparées pour impl/review) | ✅ déjà appliqué (sessions multiples) |
| **Orchestrateur + sub-agents délégués** | A2 engines (Orville/Discovery/SNW/Enterprise/Cerritos/Protostar) + 35 A3 twins | ✅ canon, plus structuré |
| **Skills partagées cross-agent** | `.claude/skills/` (skills canon) + `.claude/agents/` | ✅ canon |
| **Guardrails Python** | `rules/security.md` + hooks PreToolUse + ADR-META-001 D1-D8 | ✅ canon, plus déclaratif |
| **Human-in-the-loop pour actions dangereuses** | Doctrine "coût d'escalade A0" (D7) + `/loop` ScheduleWakeup | ✅ partiellement appliqué |
| **Cross-device sync** | TTS SAPI Hortense + SESSION_HANDOFF + Telegram bridge | 🟡 ad-hoc, pas meta-harness |
| **Debbie : 2 agents argumentent** | `agents.md` §"Multi-Perspective Analysis" (factual/senior/security/consistency/redundancy) | ✅ canon |
| **Custom agent auto-généré** | `/skill-creator` + Phase 2 Hermes-style self-improvement | ✅ canon (Phase 2 plus fort) |
| **Sandbox Docker/E2B** | VPS Hostinger + Dokploy (kill en cours) → Supabase Cloud + Vercel | 🟡 pivot Architecture |

## Cross-ref `/multi-backend` skill (D8)

**Omnigent = pattern canonique pour `/multi-backend`** :
- Backend ≠ modèle unique = **N modèles orchestrés** (Claude Code + Codex + Pi + Kimmy + Ollama local)
- Chaque backend a ses **strengths** (Claude impl, Codex review, Pi lightweight, Ollama offline)
- Orchestrateur choisit quel backend pour quelle sous-tâche = **routing cognitif**
- Setup <10 min, dogfooded en prod = preuve de viabilité
- **A0 application directe** : pourrait plug Omnigent OU reproduire le pattern dans son propre Symphony runtime (ce qui est plus aligné avec doctrine "sovereignty first")

**Recommandation D7** (non-escalade) : A0 NE DOIT PAS basculer sur Omnigent dans cette session. **Note ce pattern pour review Q4 2026** lors du prochain pivot kernel. En attendant, le pattern est **déjà canon** dans Symphony multi-agent — la vidéo valide la thèse.

## D1 Receipts

- [x] **Transcript fetched** via `mcp__transcript-api__get_youtube_transcript` (format=text, send_metadata=true)
- [x] **Metadata confirmed** : Title=Omnigent Meta-Harness, Author=Cole Medin, channel=UCMwVTLZIRRUyyVrkjDpn4pA, thumbnail present
- [x] **LDxx choisi avec justification D3** : LD04_Cognition_Tilly (orchestration cognitive, pas business)
- [x] **A3 twin** : Tilly (H30 30-day learning arc, ship's scientist — Cognition officer)
- [x] **Pattern cross-ref `/multi-backend`** documenté (D8)
- [x] **8 bullets insights** + 8 citations verbatim + 9 patterns cross-agent

## Anti-pattern guards respectés

- D1 : verify before assert — transcript relu intégralement, pas résumé inférré
- D2 : research-first — WebSearch SKIP (transcript MCP direct)
- D3 : nuance prioritaire — LD04 pas LD01 (orchestration cognitive ≠ business strategy)
- D7 : non-escalade — recommandation "review Q4 2026" pas "GO switch now"
- D8 : cross-agent — patterns mappés à A2/A3 canon A'Space

## See also

- Geordi 09_Life_OS/ cartography (`.claude/memory/userspace-cartography.md`)
- CLAUDE.md §"User-Space Cartography" — anti-pattern guard
- LD04 sibling guides : `2026-06-19_notebooklm-agentic-ai-update-is-huge-agentic-coder-now__57L3vmQLzwQ.md`, `2026-06-19_antigravity-sdk-digital-simulated-world__xlALU-kyFdw.md`, `2026-06-19_caching-problem-ai-agents__4Afvll6TQXA.md`
- Skill canonique : `/multi-backend`
- ADR-META-001 (Doctrine Anti-Paresse) — `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md`
