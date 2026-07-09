---
name: area-domain-doctrine-distill
description: >-
  Distill a Jerry-Area business-domain PERPETUAL DOCTRINE file
  (03_<HERO>_<DOMAIN>_PRINCIPLES.md) from a Geordi resource-guide corpus, in the
  A'Space OS V2 L2 Business layer. Use this whenever Amadeus (A0) wants to
  "develop / build / distill / start" a Business domain from the Geordi guides —
  e.g. "développe le domaine Ops de Batman", "distille les guides Sales",
  "fais les domaines restants (IT, Finance, People, Legal)", "passe Sales en v2",
  "ajoute ces ressources à <domaine>". Also trigger when new resource fiches are
  added to a 03_Resources_Geordi/01_Guides/<NN>_<Domain> folder and the matching
  Area doctrine needs to be created or extended. This is the proven pattern
  already run for Growth (Superman), Product (Flash) and Ops (Batman) — reuse it
  instead of re-deriving the structure each time.
---

# Area Domain Doctrine Distiller

Turn a folder of Geordi resource guides into a **perpetual Area doctrine** — the
`03_<HERO>_<DOMAIN>_PRINCIPLES.md` file that a Jerry-Area business domain (one of
the 8 SOA squads) applies forever. Picard projects *reference* this doctrine;
they never re-derive it (DRY).

This skill exists because the same distillation has now been run by hand 3× and
the structure, paths, naming, and — most importantly — the **honesty rules** are
stable. Follow them and the 4 remaining domains (IT, Finance, People, Legal) plus
any v2 extensions become a repeatable 20-minute job instead of a from-scratch one.

## The job in one sentence

Read the real corpus for ONE domain → distill ~18 timeless principles (the WHY/WHAT)
→ write them into the canonical Area folder in the proven format → log it → leave an
honest extension queue for what's left.

---

## Step 0 — Identify the domain and resolve its paths

The 8 Business domains, their archetype hero, A3 squad, and folder indices differ
between the corpus tree and the Area tree. Read `references/domain-map.md` for the
full table. Resolve three paths up front:

- **Corpus** : `20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/<NN>_<Domain>/`
- **Doctrine target** : `…/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/<NN>_<Domain>_<Hero>_<Squad>/03_<HERO>_<DOMAIN>_PRINCIPLES.md`
- **Squad canon** : the sibling `B3_Squad_<Squad>/00_B3_SQUAD_CANON.md`

Path reality (this is Windows under a curly-apostrophe folder):
- Use Unix-style `C:/Users/amado/ASpace_OS_V2/...` in Bash; the on-disk parent is
  `ASpace_OS_V2` (no apostrophe in the Unix path).
- `Glob` times out on these deep space-containing paths — use `find` / `os.walk`
  via a Python heredoc instead.
- Always set `PYTHONIOENCODING=utf-8` for Python heredocs (the doctrine has `→`,
  `×`, `é`, emoji; the Windows console is cp1252 and will crash on print otherwise).
- Everything stays inside the Trust Zone `C:\Users\amado`. No external writes.

## Step 1 — Triage the corpus (this is where honesty starts)

Walk the corpus folder and classify every file before reading deeply:

1. **Signal** — guides genuinely about the domain (systematization for Ops,
   offers/pricing for Sales, etc.). These are your sources.
2. **Noise** — misfiled items (e.g. France-24 news articles, unrelated culture
   videos). Skip them; do not let them shape principles.
3. **Stub** — placeholder files ("Content not yet transcribed", ~400 bytes).

**Verify, don't guess, the stub/real split.** A real bug happened: a first pass
mis-flagged a full corpus as stubs and a PENDING doctrine was written, then had to
be retracted. Check byte size AND open a couple of files. Treat the result as fact
only after you've actually read content.

Decision gate from triage:
- **Rich real corpus** → full distillation, `status: CANONICAL`.
- **Thin real corpus (1-3 sources)** → `status: DRAFT_V1_DÉBUT`, fewer principles,
  honest "this is a début, extensible" note + a backlog table. (This is fine and
  truthful — see Sales.)
- **Genuinely empty / all stubs** → do NOT fabricate. Write a short
  `DRAFT_PENDING_CORPUS` scaffold that names the squad + lists what must be
  transcribed, and stop. Fabricating principles violates the proof contract.

## Step 2 — Ground the squad and the North Star (do not invent these)

- **Squad roster** is canon, not creative. Read `B3_Squad_<Squad>/00_B3_SQUAD_CANON.md`
  — it transcribes the Notion `AGENT_REGISTRY_DB`. The registry is prime. Use the
  real member names and their specialties for the "How the squad applies these"
  table. If a member's Ops role is uncertain, mark it provisional rather than
  asserting it. (One member is often a grounded **Build Gate / QA** — e.g.
  "Filtre Invisible Woman" in the Airtable adapter.)
- **North Star + KRs** come from the domain's `00_B2_DOMAIN_CONTROL_ROOM.md` and
  `README.md` (the KR table). Quote the real KR ids/targets; don't make up metrics.
- **The B2 owner is non-délégable on 1-2 decisions** the control room reserves
  (e.g. North Star definition, pricing). Leave an unchecked `[ ] Acceptance <Hero>`
  in the DoD framing.

## Step 3 — Distill the principles

Read the signal guides. Extract the **timeless WHY/WHAT** — the laws the squad
applies — not project-specific tactics (those live in Picard projects). Aim for ~18
for a rich corpus; fewer for a début.

Distillation discipline:
- **Faithful, not inventive.** Every principle must trace to something in the
  corpus (or a named public framework the corpus invokes — Hormozi value equation,
  E-Myth, AARRR, LWAS, etc.). Cite sources at the bottom. Never pad to hit 18.
- **Cluster the principles** by a natural spine. If the corpus repeats a framework
  (Ops corpus is unanimous on **DEAL** = Définir/Éliminer/Automatiser/Libérer),
  use it as the cluster spine. Otherwise use a funnel/lifecycle grouping
  (e.g. Growth = AARRR; Sales = Offer/Pricing/Model/Proof).
- **Each principle**: a bold one-line claim + 1-3 sentences of *why it matters*,
  and where useful a tag (which squad member leads, which KR it serves, which
  AARRR/lifecycle stage). Explain the why; avoid hollow MUSTs.
- **Boundary section** is mandatory: state how this domain differs from its
  neighbours so domains don't collide (Growth=acquisition, Sales=conversion,
  Product=value, Ops=repeatability…). One datum, one owner (ADR-MESH-L2-001):
  domains *point* at each other's data, never copy it.
- **Metrics are pointers, never copies.** Real numbers live in Airtable/analytics;
  doctrine references them, it doesn't restate them.

## Step 4 — Write the files (use the template)

Write the doctrine to the resolved target path using the exact section order in
`references/doctrine-template.md` (frontmatter → What this is → principles in
clusters → How the squad applies → North Star/boundary → anti-patterns → mesh
anchoring → DRY references → extension plan → source citations). Also write/refresh
the domain folder `README.md` (short: files, squad, North Star, DRY one-liner).

Match the sibling doctrines' voice exactly — read
`01_Growth_Superman_Guardians/03_SUPERMAN_GROWTH_PRINCIPLES.md` and
`04_Ops_Batman_Fantastic4/03_BATMAN_OPS_PRINCIPLES.md` as the gold reference before
writing, so the new file is a true sibling (same frontmatter keys, same tone, same
DRY/boundary conventions).

Use a `PYTHONIOENCODING=utf-8 python3` heredoc for the write when the content has
heavy Unicode; otherwise the `Write` tool is fine. Prefer writing the file in one
shot over many small edits.

## Step 5 — Log and queue the leftovers

- Append a dated entry to
  `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/skills_queue.md` summarizing
  what was distilled, the status, the principle count, and the squad grounding.
- If the corpus has a large unread backlog (e.g. a `*_AUDIT.md` index of dozens of
  videos like the Dan Martell corpus), record it as the **extension plan / v2
  backlog** inside the doctrine and, for the Growth-style case, as an `Inbox`
  note in that domain's `04_<HERO>_EXTRACTION_QUEUE.md`. Truthful "here's what's
  left" beats a falsely-complete file.
- Be transparent about provenance in the log: note whether principles came from
  full transcripts or A0-provided concept capsules, and flag any self-corrections.

---

## Honesty contract (the heart of this skill)

This skill is mostly judgment, not mechanics. The mechanics are easy; the value is
refusing to fabricate. Carry these through every step:

- **No fabricated principles.** Thin corpus → fewer principles + honest début.
  Empty corpus → PENDING scaffold, full stop.
- **Verify the corpus state** before declaring it stub/real/noise.
- **Ground squad + KRs** from canon (B3 squad file, control room), never invent.
- **Pointers, not copies** for metrics and cross-domain data.
- **Self-correct loudly.** If a prior pass was wrong (mis-triage, lost write),
  say so in the log and fix it rather than papering over it.

## Reference files

- `references/domain-map.md` — the 8 domains → hero / squad / folder indices /
  corpus path / done-status, plus the path-resolution recipe.
- `references/doctrine-template.md` — the exact output structure with placeholders
  and a filled mini-example.
