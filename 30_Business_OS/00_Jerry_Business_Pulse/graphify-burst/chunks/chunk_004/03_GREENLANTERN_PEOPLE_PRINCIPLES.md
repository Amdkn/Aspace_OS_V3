---
source: A0_Amadeus_Canon
date: 2026-05-31
type: area_domain_principles
domain: L2_Business / People / Jerry_Prime_LD01
tags: [#people #green_lantern #xmen #principles #jerry_area #perpetual_doctrine #agent_onboarding #ethics_alignment #culture #harness #hermes #claude_code #model_agnostic]
guardian: Green Lantern (A2)
squad: The X-Men (Professor X, Cyclops, Jean Grey, Wolverine, Storm, Beast, Nightcrawler, Rogue)
status: CANONICAL_FROM_CANON
source_corpus: INTERNAL canon (B3 X-Men squad canon + control room KR-7a..d) + A0 Harness directive (2026-06-02) + 08_People/agent-harnesses-hermes-claude-code.md
distillation: v5 (12 internal-canon + Harness PE13-PE18 + Human-Member Effectiveness PE19-PE24 + Owner-Leverage PE25-PE28 + PE29 surface-separation ; v5 hardens PE13/PE17/PE18 from directive -> FIELD-GROUNDED via ADR-HERMES-001: Hermes live (CLI+Gateway+Dashboard+Workspace+Nous Desktop), mission-contract Build-Gate PASS, VPS systemd heartbeat)
---

# 💚 GREEN LANTERN PEOPLE PRINCIPLES — Jerry Area Perpetual Doctrine (v6 — + Agentic-HR dynamic-workflow mechanics)

> **Layer** : L2 Business / Jerry Area (Spock) / Domain 07 People
> **Guardian** : Green Lantern (A2) commanding the X-Men (A3 squad)
> **Nature** : PERPETUAL doctrine — Areas never "complete", they are maintained.
> **DRY contract** : Picard projects REFERENCE these principles; they never re-derive them.

---

## What this is — and its honest source

The **12 perpetual People principles**. ⚠️ The external Geordi corpus
(`03_Resources_Geordi/01_Guides/08_People`) is **empty** — so these are distilled from **A'Space's
internal canon**: the X-Men squad canon (transcribed from Notion `AGENT_REGISTRY_DB`) and the
People control room (KR-7a..d). `CANONICAL_FROM_CANON`, honestly internal, extensible when a
corpus is added.

**The A'Space twist you must respect:** in this OS, "People" governs **AI agent capsules** as much
as humans — onboarding new capsules (Codex, Gemini, Claude Code), monitoring their performance
(latency, heartbeat), and auditing their **ethics & alignment**. The X-Men's character — radical
empathy, patient mentoring, protecting "the different" — is the doctrine: onboard agents *with
dignity*, align them to the axioms.

Where IT runs the machines and Ops runs the processes, **People (Green Lantern) builds and
protects the team — human and synthetic.** North Star = **team health**: KR-7a 12-month retention
>85%, KR-7b time-to-productivity <60 days, KR-7c culture index >75% (quarterly survey), KR-7d no
hire without 12-month runway confirmed.

---

## The 12 Green Lantern People Principles

### Cluster A — Recruiting & Onboarding — Beast / Cyclops / Nightcrawler

**PE1 — No hire without 12-month runway.** Headcount is finance-gated: confirm ≥12 months runway
(and the ~$10K/month-per-person net-revenue rule) before any hire. (KR-7d; the Finance↔People gate.)

**PE2 — Structured onboarding, dignity-first.** Every onboarding is a defined structure, not an
improvisation. For an agent capsule that means init `AGENTS.md` + `Context.md` + `memory/` —
end-to-end in <1h (Build Gate). Humans and agents are brought in with the same care. (Cyclops.)

**PE3 — Distributed onboarding works anywhere.** Onboarding must function across locations and
runtimes without degrading. (Nightcrawler.)

**PE4 — Recruit for specialized fit.** Match the profile (incl. specialized AI agents) to the real
need — the right capability, not the generic one. (Beast.)

### Cluster B — Performance & Development — Wolverine / Rogue / Storm

**PE5 — Time-to-productivity <60 days.** A new member (human or capsule) reaches real output fast;
a slow ramp is a design failure, not the member's fault. (KR-7b.)

**PE6 — Direct, no-bullshit performance reviews.** Weekly review of real signals — for agents,
`Avg_Latency_ms` drift and heartbeat misses; honest, specific feedback. (Wolverine; SOP-L2-PEOPLE-002.)

**PE7 — Cross-training / skill transfer.** No single point of knowledge; deliberately transfer and
absorb skills across the team. (Rogue.)

**PE8 — Earn `Active` status on a real baseline.** Never promote a capsule to `Active` without a
7-day baseline of successful ticks. Probation is proof, not paperwork. (Anti-pattern made positive.)

### Cluster C — Culture & Cohesion — Jean Grey / Storm

**PE9 — Culture is a tracked metric.** Quarterly culture survey, score >75% (KR-7c). Culture you
don't measure is culture you're guessing at.

**PE10 — Resolve conflict, don't suppress it.** When two agents compete on the same topic, a named
arbiter (Jean Grey) decides — productive disagreement is fine; unresolved collision is not.

**PE11 — Retention is the health signal.** Hold 12-month retention >85% (KR-7a); a drop below
triggers remediation, not rationalization. Good people (and stable capsules) leaving is a wound.

### Cluster D — Ethics & Alignment (the X-Men's mission) — Professor X

**PE12 — Ethics & alignment monitoring is non-negotiable.** Quarterly ethics audit (sample ~10
outputs/agent) verifying alignment to the SDD-001 *Sobriété Intelligente* axioms; **zero ethics
violation** is the Build Gate. Decommission a deprecated agent only after archiving its `memory/`
to `04_Archives_Data` — even retirement is done with dignity. (Professor X; SOP-L2-PEOPLE-003/004.)

> **Green Lantern (B2 owner) is non-délégable on headcount timing** (the runway/$10K-per-person
> rule) **and retention intervention.** He leaves an unchecked `[ ] Acceptance Green Lantern` in
> each DoD. Escalate to Jerry if >3 agents sit in `Standby` simultaneously, or any HIGH ethics finding.

---

## The 6 Harness principles (PE13–PE18) — the agent's body (A0 directive 2026-06-02)

> Beyond the Lore (the roster + identity), a People principle is that **the harness IS the agent's
> body**. People onboards the *member*; IT (Cyborg) provisions the harness *runtime*. Distilled from
> A0's directive + `03_Resources_Geordi/01_Guides/08_People/agent-harnesses-hermes-claude-code.md`.

**PE13 — The harness is the body.** A capsule is only as capable as the harness it runs in. The
A'Space bodies are **Claude Code** (terminal/dev), **Hermes** (Nous Research, swarm), and **Claude
Cowork** (sandboxed macOS desktop + Chrome agent, no-code, browser-piloting via MCP, no-delete safety —
the body for non-dev knowledge work). Onboarding (PE2) places the member *into* a harness, not just a
prompt. (IT owns the runtime; People owns the member-in-the-body.) (Shubham Sharma — Claude Cowork.)
> **v5 disambiguation (ADR-HERMES-001):** the Hermes body = **Nous Research Desktop**
> (`NousResearch/hermes-agent`, app `com.nousresearch.hermes`) — **never** `fathah/hermes-desktop`
> (an external companion, non-canonical). Onboarding a Hermes member must target the Nous body.

**PE14 — Model-agnostic by design.** The body must never be welded to one brain. A capsule must run
swappably on **GLM 4.7 Flash (OpenRouter)**, **MiniMax (token plan)**, Claude, or others — without
re-onboarding. Agnosticism is a selection criterion for any harness A'Space adopts.

**PE15 — Affordability sustains the swarm.** A 24/7 agent swarm is only viable on frugal default
models (GLM 4.7 Flash, MiniMax token plan); premium models stay reserved. Affordability is a People
constraint (can we *keep* this member running?), not only a Finance one. (Ties to the compute-frugality doctrine.)

**PE16 — Identity files drive the body.** `SOUL.md` (primary identity), `AGENTS.md`, `CLAUDE.md`,
`Context.md`/`MEMORY.md` ARE the onboarding. Hermes auto-discovers and loads these context files, so
the A'Space canon shapes the harness natively. Onboard = author these well; a body with a weak SOUL is
a weak member.

**PE17 — Prefer the harness-native swarm + review gate.** Hermes Workspace's **Swarm Mode** (persistent
tmux workers, **role-based dispatch**, **byte-verified review gate**, proof-bearing checkpoints, Kanban,
2,000+ skills, MCP) IS the B3 swarm + Build Gate incarnated. Use the harness's native swarm/review
rather than reinventing it. The Hermes ecosystem is *incontournable* for this (https://hermes-workspace.com/).
> **v5 field-grounded (ADR-HERMES-001):** no longer aspirational — the swarm is **live and proven**.
> The mission-contract dry-run `DRY-RUN-SOLARIS-OPS-001` **passed its Build Gate** (greenlight +
> writeback-requires-greenlight policy enforced), proving the CLI + Workspace + gateway/dashboard chain
> end-to-end. Canon contract: `hermes-workspace/docs/swarm/HERMES_MISSION_CONTRACT.md`.

**PE18 — Heartbeat = fluid autonomy.** Cron scheduled tasks (Hermes Agent; ref NousResearch
hermes-agent #15400) — or the Shadow L0 `heartbeat-tick.ps1` equivalent — give the body self-driven
ticks: wake → run → proof-bearing checkpoint. Resilience comes bundled: `MEMORY.md`/checkpoints/
`/rollback`, provider routing + fallback providers + credential pools (the harness echo of Donna DLQ +
the quota-aware fallback chain).
> **v5 field-grounded (ADR-HERMES-001):** the heartbeat infra is **live on the VPS** — three
> user-systemd services (`hermes-gateway-vps` 8642, `hermes-dashboard-vps` 9119 loopback;
> `hermes-workspace-vps` 3001 via Caddy HTTPS) with `loginctl enable-linger` for persistence across
> reboots. A model call returned `OK_REMOTE`. The "self-driven tick" is no longer theoretical.

**PE29 — One body per surface: local Desktop ≠ remote Workspace (no session collision).** Because the
Nous Desktop and a local Workspace **share the same Hermes CLI install** (sessions/config/skills), they
collide if co-run. The canon (ADR-HERMES-001): **Desktop Nous = the Windows-native local body**;
**Workspace = the remote VPS surface** (password-protected HTTPS). People onboards a member into *one*
surface deliberately; never wire both to autostart. (A People/IT co-owned operating rule, not just infra.)

> **Green Lantern's ownership extends to harness selection** (agnostic + affordable + canon-native) —
> co-decided with **Cyborg (IT)** who owns the runtime. A member is never `Active` (PE8) until its
> harness passes the 7-day heartbeat baseline.

---

## The 6 Human-Member Effectiveness principles (PE19–PE24) — v3 (field-grounded)

> The body is the harness; the **mind/discipline** is this layer. Distilled from the real `08_People`
> corpus (Ali Abdaal ×3, Tiago Forte ×4). These apply to **human members AND the human operator (A0)** —
> the synthetic side already has the harness layer. ⚠️ The business-systematization mechanics (AI SOPs,
> automation pipelines, founder-stage org-mapping) **point to Ops** (Batman P-domain), not duplicated here.

**PE19 — Run on systems, not willpower.** A system = an interconnected network of actions + checklists
producing a result. The effort curve: high upfront to architect, then maintenance → near-zero; the
system takes over from your will. A goal-setting system gives a cap and frees mental load (detach from
outcome, love the process). (Ali Abdaal — build systems.)

**PE20 — Micro-habits & the 5-minute rule.** The first 5 minutes of any task are peak resistance
(static friction); tolerate 300 seconds and flow sets in by inertia. Engineer the environment (phone
out of the room, change location, noise-isolation as attention training) — behavioural design beats
willpower. (Ali Abdaal — micro-habits/focus.)

**PE21 — Iteration mindset (ship, then iterate).** Escape the **Region Beta Paradox** (it's harder to
leave "good enough" than misery — don't settle). Kill the **One-Shot Brain** (school's single-exam
logic) for infinite-shot iteration: deploy v1.0, gather real data, beat analysis-paralysis. Stay in
**Discover mode** (growth), not **Defend mode** (threat-scan). (Ali Abdaal — mindset; mirrors IT P5 self-improving.)

**PE22 — Every member keeps a Second Brain.** Friction-less quick capture (<30s, ≤2 clicks, or the idea
is lost) + a proactive 5-minute morning Daily Page (not the inbox) + the 2-minute rule. The member's
personal knowledge system. (Tiago Forte — Second Brain; ties to L1 PARA/Enterprise — point, don't duplicate.)

**PE23 — Async, meeting-light culture.** Default to async; replace status meetings with recorded +
AI-audited workflows; protect deep-work time (no-meetings reclaims ~20% of capacity). This is the
*culture* facet — the automation mechanics (recorder→AI-checklist→Slack) belong to **Ops/IT**. (Tiago Forte — no-meetings.)

**PE24 — Develop people to OWN roles (delegate decisions, not tasks).** Escape the "heroic founder"
trap: map the org, fire yourself from each role methodically, and delegate **decisions** (with clear
**RACI** — Responsible/Accountable/Consulted/Informed), not micro-tasks. People grows owners; the
SOP/automation that backs them is **Ops** (P12 owner-vs-operator). (Tiago Forte — business-runs-itself + AI-SOPs RACI.)

> **People ↔ Ops boundary (v3):** People develops the *member* (mind, habits, ownership, role clarity);
> **Ops (Batman)** builds the *system* the member runs (SOPs, automation, autonomy ratio). PE23/PE24
> point to Ops for mechanics — one datum, one owner (ADR-MESH-L2-001).

---

## The 4 Owner-Leverage principles (PE25–PE28) — v4 (field-grounded, Dan Martell)

> Distilled from the **now-real** Dan Martell People corpus (22 fiches in `08_People/Dan_Martell/`).
> These are the **owner/operator leverage** layer — they apply first to **A0 and human owners**, and
> by extension to how the agent mesh is designed to *replace toil*. ⚠️ Honesty: the corpus grounds the
> Buy-Back Principle, deep-work/time-blocking, the "top 0.01% environment" and AI-leverage theses; it
> does **not** spell out Martell's Replacement-Ladder / Pain-Line / 10-80-10 mechanics, so those are
> **not** asserted here. (Business-systematization mechanics still point to Ops, per the v3 boundary.)

**PE25 — The Buy Back Principle: buy back time, never sell it.** Reinvest ~**25% of revenue/capacity**
into buying back the owner's (and A0's) lowest-value, most-draining work — a light DRIP-style time/energy
audit names what to offload first. In A'Space the **agent mesh IS the buyback engine**: every capsule
onboarded (PE2) exists to buy back a tranche of A0/human toil. Hiring/spawning is justified by time
bought back, not headcount added. (Dan Martell core thesis; sharpens PE24 ownership + the PE1 runway gate.)

**PE26 — Protect maker-time; time is the non-renewable asset.** Defend inviolable deep-work blocks
(**≥90 min**), and design the owner/A0 cadence around the highest-leverage zone while the mesh absorbs
the rest. Energy and attention, not hours, are what's scarce. (Time-Blocking / Deep-Work corpus; ties the
12WY WAM cadence + PE19 systems + PE23 deep-work-protection.)

**PE27 — Curate proximity & caliber (you become your environment).** Deliberately raise the *caliber* of
the agent roster and of A0's human network — the floor rises with the company kept. People ops treats the
quality of the surrounding mesh (and mentors) as a controllable input to growth. (Martell "top 0.01%
environment" guide; the culture facet, PE9/PE10 extended outward.)

**PE28 — Continuous AI-leverage upskilling (the compounding team edge).** Keep **every member and A0** at
the AI-capability frontier — systematic upskilling, skill-registry currency (Rogue, PE7), fast new-model
adoption — as a **People L&D discipline**, not only an IT concern. "Get ahead of 99% with AI" is a team-
development mandate: the org that compounds its AI fluency out-executes the one that doesn't. (Martell
AI-skills cluster; bridges IT P5 self-improving, owned here as L&D.)

> **Green Lantern's ownership extends to owner-leverage**: he arbitrates the buy-back priority (which toil
> the mesh absorbs next, PE25) and guards maker-time (PE26) — co-read with Finance (the 25% reinvestment
> is a Finance allocation call, F19/AREA_STANDARD) and Ops (the SOP/automation that backs each buyback).

---

## The Agentic-HR mechanics principle (PE30) — v6 (the 6 dynamic-workflow patterns)

**PE30 — Run agentic-HR on the 6 dynamic-workflow patterns; adversarial-verification is mandatory.** People
operations (recruit/onboard/rank/audit members, AI **and** human) run as **dynamic-workflow harnesses** (Claude
Code) incarnated in **Hermes Swarm Mode** (PE17). The 6 patterns map to HR: **classify&act** = intake routing ·
**fan-out&synthesize** = multi-lens evaluation (cited hire-memo) · **adversarial-verification** = perf-review +
ethics-audit *without self-preference* (3 skeptics vs a rubric — the institutionalised devil's advocate) ·
**generate&filter** = sourcing · **tournament** = pair-wise ranking (the 5000-CV bracket, fresh unbiased agent
per match, rubric per round) · **loop-until-done** = audit until zero ethics violation (PE12 Build Gate). The
**non-negotiable**: any agent perf-review or ethics-audit MUST use adversarial-verification — never let the agent
self-grade (it kills the self-preference bias that PE6/PE12 exist to fight). Budget the tokens explicitly
(PE15 affordability); don't swarm a trivial task. (`…/08_People/resource_claude_dynamic_workflows_6patterns.md`;
project incarnation: `…/00 Agency as a Service/B3…/07_People…/AAAS_PEOPLE_AGENTIC_HR_WORKFLOWS.md`.)

---

## How the squad applies these (X-Men — canon Notion)

| X-Men member | People focus | Principles |
|---|---|---|
| Professor X (Charles Xavier) | Lead — reads team needs (agents incl.), ethics | PE4, PE12 |
| Cyclops (Scott Summers) | Onboarding discipline & structure | PE2 |
| Jean Grey | Culture, cohesion, conflict resolution | PE9, PE10 |
| Wolverine (Logan) | Direct performance reviews, no-bullshit feedback | PE6 |
| Storm (Ororo Munroe) | Operational leadership, calm under pressure | PE5, PE11 |
| Beast (Hank McCoy) | Recruiting specialized (AI) profiles | PE4 |
| Nightcrawler (Kurt Wagner) | Distributed / multi-location onboarding | PE3 |
| Rogue | Cross-training, skill transfer | PE7, PE8 |

---

## People ↔ neighbours boundary

- **People (Green Lantern)** owns *who is on the team and how they grow* — human and agent —
  including ethics/alignment of the synthetic workforce.
- **IT (Cyborg)** provisions the *technical* capsule runtime; **People** onboards the *member* into
  it with dignity and monitors its behaviour. IT = the machine; People = the member.
- Headcount is **gated by Finance** (PE1, runway). One datum, one owner (ADR-MESH-L2-001):
  People reads `AGENT_REGISTRY_DB` heartbeat/latency, it doesn't duplicate them.

---

## Anti-patterns (People sins Green Lantern forbids)

1. **Promoting a capsule to `Active`** without a 7-day baseline of successful ticks — violates PE8.
2. **Decommissioning without archiving** `memory/` to `04_Archives_Data` — violates PE12 (dignity).
3. **Ignoring `Avg_Latency_ms` drift >50%** without investigation — violates PE6.
4. **Hiring without 12-month runway** — violates PE1.
5. **Treating culture as unmeasured vibes** — violates PE9.
6. **Skipping the ethics audit / tolerating an alignment violation** — violates PE12.

---

## Mesh anchoring (where these become operational)

- **Governed surfaces** (X-Men canon): agent-capsule onboarding (Codex/Gemini/Claude Code) ·
  performance monitoring via `AGENT_REGISTRY_DB` (`Avg_Latency_ms`, `Last_Heartbeat`) · Ethics &
  Alignment (SDD-001) · conflict resolution · skill registry (INDEX skills per capsule).
- **SOPs**: SOP-L2-PEOPLE-001 Onboard capsule · -002 Weekly perf review · -003 Quarterly ethics
  audit · -004 Decommission (archive memory/).
- **Shadow L0 link**: the capsules People onboards are the heartbeat executors (Codex/Gemini/Claude
  Code); People owns their lifecycle, IT owns their runtime, Donna DLQ catches their failures.

---

## Extension plan / backlog

**v2 Harness layer (PE13–PE18) added 2026-06-02** from A0's directive + the new resource
`08_People/agent-harnesses-hermes-claude-code.md` (Hermes Workspace + Hermes Agent feature surfaces +
Claude Code, model-agnostic via GLM 4.7 Flash / MiniMax). People = Lore (no external video corpus) +
now the **harness as body**. The Dan Martell 24 People videos remain a thematic backlog (titles only).

**v3 (2026-06-02) — field-grounded.** Real `08_People` corpus arrived (Ali Abdaal ×3, Tiago Forte ×4,
Shubham/Claude Cowork). Added the **Human-Member Effectiveness** cluster PE19–PE24 (systems, micro-habits,
iteration mindset, second brain, async culture, ownership/RACI) + Claude Cowork as a 3rd harness in PE13.
The corpus covers the **human/operator** side; the AI/synthetic side stays the harness layer (PE13–PE18).

**v4 (2026-06-03) — Owner-Leverage added.** The Dan Martell People corpus is now real (22 fiches in
`08_People/Dan_Martell/`, via Antigravity's `youtube-ingest-sops`). Added cluster PE25–PE28 (Buy-Back
Principle, protect maker-time, curate proximity/caliber, continuous AI-leverage upskilling). 28 principles.
Only what the corpus actually grounds was distilled (Replacement-Ladder/Pain-Line not asserted).

**v5 (2026-06-03) — Harness layer field-grounded.** Hermes is now live and proven (ADR-HERMES-001):
PE13 gains the Nous-Desktop disambiguation (≠ fathah/hermes-desktop); PE17 hardened by the
mission-contract Build-Gate PASS; PE18 hardened by the live VPS systemd heartbeat; **PE29** added
(local Desktop body ≠ remote Workspace surface, no session collision). 29 principles.

**v6 backlog**: (a) the **Hermes harness install/onboard skill** (`/hermes-harness-onboard`) — now
*unblocked* (Hermes wired) but still optional until A0 wants a repeatable onboard flow (Codex's
`hermes-nous-desktop-finalization` skill already covers repair/validate); (b) RAG sync of the 22 Dan
Martell People fiches into `watch_history_rag.csv` (Antigravity lane); (c) Dan Martell People deepening
once transcripts are re-grounded post-quota. Bump to v6 then.

---

## DRY references

- **Sibling doctrine** : `05_IT…` (runtime neighbour), `06_Finance…` (headcount gate), others.
- **Domain identity / KRs** : `00_B2_DOMAIN_CONTROL_ROOM.md` + `README.md` (KR-7a..d).
- **Squad canon** : `B3_Squad_XMen/00_B3_SQUAD_CANON.md` (roster + governed surfaces + SOPs + gates).
- **Axioms** : SDD-001 (Sobriété Intelligente) — the alignment target for PE12.
- **Projects** : Picard projects reference via `03_PEOPLE_PRINCIPLES_REF.md` (when instantiated).

*Perpetual doctrine (v6) — maintained by Spock (Jerry Area A2) under Green Lantern. 30 principles: internal canon (PE1-PE12) + Harness/agent body (PE13-PE18, ADR-HERMES-001) + Human-Member Effectiveness (PE19-PE24) + Owner-Leverage (PE25-PE28) + surface-separation (PE29) + Agentic-HR dynamic-workflow mechanics (PE30, 6 patterns + adversarial-verification anti-self-preference). 2026-06-03.*
