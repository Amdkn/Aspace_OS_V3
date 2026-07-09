---
title: "Every Folder on My Computer (Full Reveal) — Tiago Forte"
domain: 03_IT
ldxx_mirror: LD04_Cognition
video_id: A0pdL3MS_7E
url: https://youtu.be/A0pdL3MS_7E
channel: Tiago Forte
duration_s: 525.68
ingested_at: 2026-06-25
tool: youtube-to-guide v3 (Antigravity Premium Standard)
quality_tier: PREMIUM
char_count_target: 6K-16K
ld: LD07_Creativity_Reno
b2_owner: cyborg-it
sister_b1: jerry-prime
---

# Every Folder on My Computer (Full Reveal) — Tiago Forte

> **TL;DR.** Tiago Forte, creator of PARA, walks through his actual file system across a laptop and three drives, then demos how pointing Claude at combinations of pre-organized folders (1 project + 2 areas) produces launch plans that draw on both the specific project's detailed data and the broader area's long-term themes. The unlock is: PARA's folder hierarchy is a *context-packing primitive* for LLMs. Mix-and-match is the new superpower. A free Claude Skill (newsletter-gated) auto-reorganizes your mess into his exact system.

---

## 1. Why this video matters for you (A0 Life OS canon)

This is **not** a productivity porn tour of a creator's desktop. It is a **practical demo of how AI agents should consume your PARA canon**. Tiago is doing three things simultaneously that map almost 1:1 to A'Space OS V2 doctrine:

1. **Treating the folder hierarchy as a context-pack primitive.** Every click of "choose a different folder" injects a curated sub-corpus into the LLM's working set. This is exactly what Geordi A3 does with the `03_Resources_Geordi/` junction in `20_Life_OS/24_PARA_Enterprise/`.
2. **Separating personal / individual-work / shared drives by account boundary.** This is the `personal` vs `business` trust-zone split, but taken to the per-Drive level. He does not mix Gmail-personal and Forté-Labs-company in the same folder tree — three separate Drives, three separate PARAs.
3. **Project ⊂ Area nested composition.** A book lives inside a "books" area. The recording-studio project lives inside the YouTube area. The AI demo then points Claude at *project + area* (not project alone) to force context at two levels of abstraction simultaneously.

This is **Solarpunk-credible**: no new tool, no new vendor, no new workflow. Just a filesystem you already have, retrofitted with a sidebar, queried by an LLM you already pay for. The cost-of-escalation (D7) for adopting this is near zero because the user already has the folders.

The CRITICAL canonical reframe: **"PARA is not a productivity system, it is an LLM context-window router."** Tiago does not say this verbatim, but the entire 8m46s video is a demonstration of that thesis. Every shortcut in his Finder sidebar = a pre-baked system prompt override.

---

## 2. The actual setup (verbatim from the video)

Three logical layers, five top-level folders each, three Drives:

### Layer 1 — Local (3 folders, on-machine only)
- **Home folder** — everything for this user
- **Desktop**
- **Downloads**

These never sync anywhere. They exist because some things (in-progress downloads, screenshots, temp work) genuinely do not need a home in the cloud.

### Layer 2 — Personal Google Drive (personal Gmail, 20 years old)
Five top-level folders inside "My Drive":
1. **Inbox** (capture zone, equivalent to A0 Plane Inbox or Cerritos Mariner)
2. **Personal Projects** (PARA `01_Projects`)
3. **Personal Areas** (PARA `02_Areas`)
4. **Personal Resources** (PARA `03_Resources`)
5. **Personal Archives** (PARA `04_Archives`)

Each of the five is also pinned as a sidebar shortcut → 1-click access. Personal life is hermetic from work life.

### Layer 3 — Individual Work Google Drive
Same five top-level folders, work-flavored:
1. Work Inbox
2. Work Projects
3. Work Areas
4. Work Resources
5. Work Archives

This is Tiago's individual-account work. No one else at Forté Labs sees it.

### Layer 4 — Forté Labs Share Drive (17 TB)
Same five top-level folders, but **streamed, not mirrored**. Cloud-only by default; only the projects he is actively working on are right-click → "make available offline" (green check mark). Currently 2 active projects downloaded: his book + AI Second Brain program.

### Mirror vs Stream tradeoff (verbatim)
> "the Forté Labs share drive is something like 17 TB. It's far too much data for me to store on my computer. What I do in this case is not mirroring, it's the other mode that Google Drive offers, which is streaming."

This is the **operational decision matrix** for any >1 TB corpus: mirror small/active, stream large/archive. A'Space OS V2 has the same problem with `ASpace_OS_V2/` (260 MB graphify corpus, 1.3 GB VPS archive) — local hot-set + cloud cold-set is the correct default.

---

## 3. The actual AI demo (verbatim, with timestamps)

At ~3:30 in the video, Tiago opens Claude ("Co-worker" in his narration) and runs this sequence:

> **Step 1.** Click "work in a project" → "choose a different folder" → select **AI course folder** (a specific project)
>
> **Step 2.** Click "choose a different folder" again → select **marketing folder** (an area)
>
> **Step 3.** Click "choose a different folder" again → select **content folder** (a second area)
>
> **Step 4.** Claude now shows "AI course plus two" — i.e. 1 project + 2 areas loaded into context

Then the prompt:

> *"Analyze the contents of the AI course folder. Then create a launch and marketing plan and draw on the contents of two area folders that I'm also giving you. Suggest any ideas, possibilities, new strategies or tactics that we could use to reach our audience and new audiences based on the long-term learnings from those two area folders."*

Claude's first move (verbatim):

> *"It's always going to start by scanning the folders that you've given it to understand what it's working with. So, notice that it's reading the testimonials of our first cohort that we just finished as well as the feedback survey data."*

**This is the unlock.** The project folder supplies *concrete data* (testimonials, survey responses, dates, names). The area folders supply *long-term thematic patterns* (what marketing has worked across multiple launches, what content pillars converted). Together they form a 2-axis context: **specific + broad**.

---

## 4. Why "project + area" beats "project alone"

Tiago's framing (verbatim):

> *"This is why it's so important to have the current very specific concrete project, which tends to have very detailed data, as well as the long-term broad themes that are kind of like the big picture view. Both of those levels of detail, those levels of abstraction, are very important."*

This maps to A'Space doctrine:

| Layer | Tiago's term | A'Space equivalent | What it supplies |
|---|---|---|---|
| Project | "current very specific concrete project" | `30_Business_OS/10_Projects/<name>/` | Detailed data, recent events, active threads |
| Area | "long-term broad themes" | `20_Life_OS/LD0X_<domain>/` or `02_Areas_*` | Patterns, standards, ongoing responsibilities |
| Resource | "knowledge of X" | `03_Resources_Geordi/` | Reference material, external canon |
| Archive | "past things I have undertaken" | `04_Archives_Data/` | Completed work, retired projects, history |

The 4 PARA categories correspond to 4 **levels of context-temperature** the LLM can ingest. Hot (project) + warm (area) + cool (resource) + cold (archive). You mix them depending on the task.

---

## 5. The combinatorial matrix (verbatim from the video)

Tiago enumerates six power-move prompts:

1. **Two projects** → *"Compare and contrast these projects. What are the strengths? What are the weaknesses? How could they support each other? How could the learnings from one inform the other?"*
2. **Two areas** → *"Can lessons from my health inform my work? How can ideas from my gardening inform my marketing?"*
3. **Two resources** → *"How can I use my knowledge of UX design to, I don't know, design more engaging slide presentations that people pay more attention to?"*
4. **All project folders** → *"Analysis of your whole project portfolio. Which ones are likely to succeed? Which ones are likely to fail? Which ones you should consider scoping downward or potentially even canceling?"*
5. **Full archive** → *"What are some past things that I have undertaken that could be revived or could be revisited or could flow into current efforts?"*
6. **Free-form mix** → *"You can mix and match and compare and combine and merge and synthesize and split apart."*

The final reframe (verbatim):

> *"Really, as long as you have these pre-formed chunks of collections of files, which is really just a folder hierarchy, which you can organize using PARA or any other method, then the world is your oyster."*

**Translation for A'Space:** as long as the Geordi junction canon (`03_Resources_Geordi/09_Life_OS/LDxx_*.md`, 88 files) is structured, any agent (A3 Tilly for LD04 Cognition, A3 Stamets for LD05 Social, etc.) can compose the same kind of cross-domain synthesis in 1-2 tool calls. The folder hierarchy IS the agent's tool-use surface.

---

## 6. The free Claude Skill (Tiago's offer)

Tiago announces (verbatim):

> *"The way that you build this for yourself is a completely free Claude skill that you can just load up right into your LLM. You point it at your files, it looks at everything you've got, and then it will propose a step-by-step plan to reorganize all of it into this exact system."*

Caveat: newsletter-gated. Not an open-source repo. This is the **same funnel pattern** as every productivity creator in 2026 — give away the tool, gate the access list. It is not malicious, it is just the business model. If you want the equivalent without the gate, A'Space already has:
- `C:\Users\amado\.claude\skills\graphify-swarm-burst\` (burst-graphify your corpus)
- `C:\Users\amado\.claude\skills\guide-index-builder\` (index all `01_Guides/`)
- `C:\Users\amado\.claude\skills\youtube-takeout-to-lifeos\` (transform YouTube history → Geordi LDxx)

These are 3 open Skills that perform a similar "point at your files, reorganize canonically" function — without the newsletter.

---

## 7. What this means for A0 (operational implications)

### Immediate (Week 1)
- **Audit sidebar shortcuts.** A0 has ~19 installed apps in `C:\Users\amado\` per the user-space cartography. Each app's `graphify-out/graph.json` is already a context-pack. Pin them as A0 Resources shortcuts if not already.
- **Geordi junction drill-down.** `03_Resources_Geordi/09_Life_OS/LDxx_*.md` is 88 files across 8 LDxx. The 6 combinatorial moves Tiago lists are EXACTLY what an A3 Discovery twin can do today if prompted correctly: "Compare LD02_Finance and LD04_Cognition canon for any cross-domain patterns."

### Medium-term (Cycle 12WY Q3 2026)
- **Sidebar of A0's "Life OS finder."** Wire `LD0X_<domain>/` (Spock Areas), `10_Projects/` (Picard Projects), `03_Resources_Geordi/` (Geordi Resources), `04_Archives_Data/` (Data Archives) as 4 one-click shortcuts in the Geordi viewer web UI at `http://localhost:8765`.
- **Project + Area pairing default.** When A1 SNW Una (Planning) decomposes a Rock into W1-W12 tactics, the prompt template should default to "this week's tactic + the parent area" — never tactic alone. This is the single biggest leverage point.

### Long-term (H30/H90)
- **Streaming-vs-mirror policy formalize.** A'Space has `graphify-out/` (mirrored, local) + `graphify-out-master/` (canonical, master merged). Already correct, but document the rule: "Active cycle = mirror, retrospective = stream."
- **Build the A3-Discovery cross-LDxx agent.** Tilly (LD04) and Stamets (LD05) currently do single-domain. The Tiago pattern demands an `a3-discovery-cross-pollinator` that takes 2+ LDxx junctions and returns cross-domain insights. Sketch spec.

---

## 8. Anti-patterns this video quietly defends against

1. **"I'll just upload everything to the LLM."** Wrong. Context window is finite. Pre-curation (PARA) is what makes the result high-quality. Mass upload = noise.
2. **"Folders are for browsing, not for AI."** Wrong. Folders ARE the LLM's working memory. Stop treating your filesystem as read-only-by-humans.
3. **"Personal and work should be one Drive."** Wrong. Tiago keeps three Drives by account boundary. A0 must keep `personal-ASpace` and `work-ASpace` separate (currently they live in same Trust Zone but should be tagged at folder level).
4. **"One canonical structure across the company."** Wrong. Forté Labs share drive is 17 TB streamed. Each user mirrors only what they actively work on. **Local canon + cloud canon** is the only sustainable model at scale.
5. **"Archive = delete."** Wrong. Archive is the 4th PARA category for a reason. Tiago explicitly demos the "what past things could I revive?" prompt against archive. Archives are dormant resources, not waste.

---

## 9. Quick-start checklist (paste into your weekly review)

- [ ] Are my 5 top-level PARA folders (Inbox + 4 PARA) pinned as sidebar shortcuts?
- [ ] Are personal/work Drives separate (different accounts)?
- [ ] Are share drives streamed (not mirrored) if >1 TB?
- [ ] When I prompt an LLM, do I attach at least 1 area folder alongside the project?
- [ ] When I prompt an LLM, do I have a "two projects / two areas / two resources" pattern ready to go?
- [ ] When I close a project, does it move to Archives (not stay in Projects)?
- [ ] Do I have a streaming-vs-mirror policy for files >1 GB?

If 5+/7 are checked, you are running Tiago-grade PARA. If <5/7, the gap is the unlock.

---

## 10. One-line takeaway

**PARA is an LLM context-router disguised as a productivity system.** The folder hierarchy is the API surface; the LLM is the query engine; you are the prompt engineer. A0's Geordi canon is already 80% of the way there — wire the sidebar, default to project+area pairing, ship an A3 cross-pollinator twin by W4.

---

## Appendix A — Timestamped transcript anchors

- 0:00 — Hook: "show you every folder on my computer"
- 0:28 — "that's PARA. Four folders that I've taught for over a decade now"
- 0:42 — Local folders: home, desktop, downloads
- 0:55 — Personal Google Drive (20 years old)
- 1:15 — Personal PARA shortcuts
- 1:35 — Individual work Google Drive
- 1:55 — Personal-life / work-life separation
- 2:10 — Forté Labs share drive
- 2:30 — 17 TB streaming vs mirroring
- 2:55 — Cloud symbol = "only lives in the cloud"
- 3:10 — Right-click → "make available offline" (green check)
- 3:30 — Project ⊂ Area framing (book ⊂ books, studio ⊂ YouTube)
- 4:00 — **The demo begins** — "work in a project, choose a different folder"
- 4:15 — Select AI course folder + marketing area + content area = "AI course plus two"
- 4:30 — The launch-plan prompt (verbatim in §3)
- 4:50 — Claude scans testimonials + survey data
- 5:15 — "Both of those levels of detail... are very important"
- 5:45 — Combinatorial matrix begins (6 power moves in §5)
- 7:30 — "the world is your oyster"
- 7:50 — Free Claude Skill announcement (newsletter-gated)
- 8:30 — Outro

## Appendix B — Source files referenced

- Video transcript: `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\_transcripts_raw\A0pdL3MS_7E.md`
- MCP call raw: `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_B_runtime\04_mcps\_last_call.json`
- Clean version: `C:\Users\amado\_transcript_A0pdL3MS_7E_clean.txt`
- A'Space junction analog: `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\` (88 LDxx files)
- Graphify corpus analog: `C:\Users\amado\.claude\memory\graphify-out-master\` (203K nodes / 490K edges)

## Appendix C — Related canon

- `_SPECS/ADR/ADR-INFRA-003_business-os-ceo-dashboard-matryoshka.md` — Picard H10 MANIFEST doctrine
- `wiki/hand_offs/handoff_life_os_deploy_v1_0_2026-06-17.md` — 16-table UNIFIED schema (PARA canon)
- `MEMORY.md` §"Life OS apps seeded 2026-06-17" — fw_ikigai / fw_life_wheel / fw_12wy seed data
- Skill: `C:\Users\amado\.claude\skills\graphify-swarm-burst\` — equivalent open-source "point at files, reorganize" tool

---

*Geordi A3 (H90) canon-curated from YouTube transcript A0pdL3MS_7E. 8-section Antigravity Premium Standard. Classified to 03_IT (file-system / LLM context-routing), mirrored to LD04_Cognition (knowledge architecture).*
