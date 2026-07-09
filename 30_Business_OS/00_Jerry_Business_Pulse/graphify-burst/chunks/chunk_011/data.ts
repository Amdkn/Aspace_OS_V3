// SOLARIS — data layer
// Front-stage: only shows the L2 Business Pulse.
// Hierarchy B1 (Executive · Jerry/Summer) → B2 (VPs · Justice League DC)
// → B3 (Squads · Marvels). No mention of L0/L1.

import type {
  SolarisDomain,
  AnatomyTier,
  SolarisArchetype,
  SolarisParadigm,
  SolarisHolding,
  VaultArchData,
} from "./types";

// 8 expertise poles led by B2 VPs (Justice League DC)
export const SOLARIS_DOMAINS: SolarisDomain[] = [
  {
    id: "growth",
    n: "01",
    name: "Growth",
    sub: "Acquisition",
    role: "The Master SOC payload for acquisition. Star-Lord extracts via boolean queries, Groot detects tech footprints, Mantis scores intent, the Guardians orchestrate the OH/KY lead swarm.",
    vp: "B2.Superman",
    squads: ["B3.Star-Lord", "B3.Groot", "B3.Mantis", "B3.Guardians"],
    agents: 6,
    status: "active",
    metric: "247 leads / 24h",
    angle: 0,
  },
  {
    id: "sales",
    n: "02",
    name: "Sales",
    sub: "Closing",
    role: "Asynchronous qualification and e-sign vaults — every deal closes without a single discovery call.",
    vp: "B2.Flash",
    squads: ["B3.Daredevil", "B3.Black Widow"],
    agents: 4,
    status: "active",
    metric: "12 contracts / wk",
    angle: 45,
  },
  {
    id: "finance",
    n: "03",
    name: "Finance",
    sub: "Treasury",
    role: "Locks your margins, caps compute spend, invoices clients on value rather than hours.",
    vp: "B2.Cyborg",
    squads: ["B3.Iron Man", "B3.War Machine"],
    agents: 3,
    status: "stable",
    metric: "margin ≥ 70%",
    angle: 90,
  },
  {
    id: "ops",
    n: "04",
    name: "Ops",
    sub: "Operations",
    role: "Watches the flows, catches stalling agents, telemeters every B3 squad in real time.",
    vp: "B2.Batman",
    squads: ["B3.Donna", "B3.Punisher", "B3.Hawkeye"],
    agents: 5,
    status: "active",
    metric: "uptime 99.94%",
    angle: 135,
  },
  {
    id: "product",
    n: "05",
    name: "Product",
    sub: "Production",
    role: "Generates your deliverables — audits, reports, content, code — under your brand. B2 sign-off before release.",
    vp: "B2.Wonder Woman",
    squads: ["B3.Captain Marvel", "B3.Scarlet Witch", "B3.Vision"],
    agents: 7,
    status: "active",
    metric: "32 deliverables / wk",
    angle: 180,
  },
  {
    id: "it",
    n: "06",
    name: "IT",
    sub: "Systems",
    role: "Keeps your instance running. You never see it — it never goes down.",
    vp: "B2.Green Lantern",
    squads: ["B3.Spider-Man", "B3.Ant-Man"],
    agents: 2,
    status: "stable",
    metric: "0 incidents / 30d",
    angle: 225,
  },
  {
    id: "people",
    n: "07",
    name: "People",
    sub: "Memory",
    role: "Holds your brand memory — your tone, your clients, your standards — at the core of the factory.",
    vp: "B2.Martian Manhunter",
    squads: ["B3.Doctor Strange", "B3.Professor X"],
    agents: 3,
    status: "active",
    metric: "184 active SOPs",
    angle: 270,
  },
  {
    id: "legal",
    n: "08",
    name: "Legal",
    sub: "Compliance",
    role: "GDPR, contracts, veto rights on every outbound flow. Your compliance is non-negotiable.",
    vp: "B2.Aquaman",
    squads: ["B3.She-Hulk", "B3.Daredevil"],
    agents: 2,
    status: "vigilant",
    metric: "strict RLS",
    angle: 315,
  },
];

// ─── SOB hierarchy (Self-Operating Business) ─────────────────────
export const SOLARIS_ANATOMY: AnatomyTier[] = [
  {
    tier: "B1",
    name: "Executive Direction",
    codename: "Jerry / Summer",
    role: "The routing brain",
    desc: "Receives your orders (Payloads), translates your requirements into technical specifications, and orchestrates the production flow without you ever having to step in.",
    metaphor: "The CEO that never sleeps",
    headcount: "2 agents · 24/7 routing",
  },
  {
    tier: "B2",
    name: "VPs · Quality Assurance",
    codename: "Justice League DC",
    role: "Your department heads",
    desc: "They don't produce — they control. Before any deliverable ships to you, a VP — Batman on Ops, Aquaman on Legal, Wonder Woman on Production — mathematically verifies that production meets your standards and your Build Gates.",
    metaphor: "Your 8 department heads",
    headcount: "8 VPs · one per expertise pole",
    members: [
      "Superman",
      "Flash",
      "Cyborg",
      "Batman",
      "Wonder Woman",
      "Green Lantern",
      "Martian Manhunter",
      "Aquaman",
    ],
  },
  {
    tier: "B3",
    name: "Production Squads",
    codename: "Marvels",
    role: "Your specialized workforce",
    desc: "Swarms of software agents configured to crush precision tasks at the speed of light — data extraction, code drafting, content generation, formatting — under real-time supervision from the VPs.",
    metaphor: "Your execution squads",
    headcount: "32+ squads · parallel production",
    members: [
      "Star-Lord",
      "Groot",
      "Mantis",
      "Iron Man",
      "Captain Marvel",
      "Scarlet Witch",
      "Vision",
      "Spider-Man",
      "Doctor Strange",
    ],
  },
];

// ─── The 4 target archetypes (front-stage copy) ──────────────────
export const SOLARIS_ARCHETYPES: SolarisArchetype[] = [
  {
    id: "revops",
    code: "AR/01",
    name: "RevOps",
    fullName: "The Revenue Engineers",
    tag: "RevOps & performance agencies",
    glyph: "⚙️",
    painName: "Fragmentation",
    painDesc:
      "You spend more time patching broken integrations between your clients' CRMs and the ad platforms than actually optimizing ROAS.",
    remedyName: "Unification via SOC",
    remedyDesc:
      "Stop patching your data. Hand the engineering of your flows to our IT Squads. We build and maintain infallible data pipelines. You sell the revenue; our factory guarantees the plumbing.",
    pitch: "\u201CYou sell the revenue. Our factory guarantees the plumbing.\u201D",
    detection: "HubSpot + 3+ Zaps + Make public · multi-account",
    extractor: "B3.Groot · tech-stack detection",
    productCode: "SOC · Service-Oriented Communication",
    targets: [
      { k: "Signal", v: "HubSpot + multi-Zaps + public Stripe" },
      { k: "OH/KY density", v: "Very high · Cincinnati mid-market" },
      { k: "Lead target", v: "180-220 / month" },
    ],
  },
  {
    id: "forges",
    code: "AR/02",
    name: "Forges",
    fullName: "Content & Media Forges",
    tag: "Media · content · volume",
    glyph: "📝",
    painName: "Margin Bleed",
    painDesc:
      "Generating content is easy; verifying it, reformatting it, and managing client revisions destroys 80% of your margin and burns out your editors.",
    remedyName: "Paperclip Workspaces · B2 Flash QA",
    remedyDesc:
      "Plug your briefs into our factory. Our B3 agents generate — but more importantly, our B2 VPs validate semantic accuracy and brand tone before delivery. 10× your volume without hiring a single reviewer.",
    pitch: "\u201C10× your volume without hiring a single reviewer.\u201D",
    detection: "≥40 deliverables/mo · <2 visible QA · LinkedIn team ratio",
    extractor: "B3.Star-Lord · boolean ratio query",
    productCode: "B2 Flash · Content Forge",
    targets: [
      { k: "Signal", v: "High creator volume · low QA ratio" },
      {
        k: "OH/KY density",
        v: "Medium · Columbus / Lexington studios",
      },
      { k: "Lead target", v: "90-110 / month" },
    ],
  },
  {
    id: "aaa",
    code: "AR/03",
    name: "AAA",
    fullName: "AI Automation Agencies",
    tag: "Stop being a vendor — become a publisher",
    glyph: "🤖",
    painName: "The Cobbler's Paradox",
    painDesc:
      "You sell automation, yet your own back-office runs on manual processes. Your flows rely on public platforms that blow up your API costs the moment you scale.",
    remedyName: "Sovereignty · Cyborg Squads",
    remedyDesc:
      "Delegate the maintenance and deployment of your agents to our Cyborg squads. We turn your services agency into an actual software publisher — clean infrastructure, fixed costs, a real moat.",
    pitch: "\u201CGo from services agency to software publisher.\u201D",
    detection: "Make.com / n8n public footprint · entity age < 24 months",
    extractor: "B3.Mantis · AI intent scoring",
    productCode: "Cyborg squads · private control plane",
    ticket: "$1,555 / month",
    targets: [
      { k: "Signal", v: "Public Make/n8n · OpenAI reliance · <2 yrs" },
      { k: "OH/KY density", v: "Emerging · 2025 wave" },
      { k: "Lead target", v: "60-80 / month" },
    ],
    recommended: true,
  },
  {
    id: "boutiques",
    code: "AR/04",
    name: "Boutiques",
    fullName: "Strategy Boutiques · High-Ticket",
    tag: "Fractional CMO · prestige advisory",
    glyph: "♟️",
    painName: "The Glass Ceiling",
    painDesc:
      "You sell premium advisory, but clients always end up asking for execution. Saying yes drags you back into freelance hell. Saying no halves your LTV.",
    remedyName: "Pure AaaS · White Label",
    remedyDesc:
      "Stay the intellectual front. Sell strategic execution to your clients and let our ghost factory deliver the work under your logo. Keep 70% margin on services you never have to produce yourself.",
    pitch: "\u201CStay the face. Our factory ships under your brand.\u201D",
    detection:
      "LinkedIn headcount 1-3 · visible tier-1 clients · no delivery team",
    extractor: "B3.Guardians · solo-founder watch",
    productCode: "Pure AaaS · White-Label Factory",
    targets: [
      { k: "Signal", v: "1-3 founders · ≥3 tier-1 clients" },
      { k: "OH/KY density", v: "Low · surgical targeting" },
      { k: "Lead target", v: "20-30 / month" },
    ],
  },
];

// ─── The 3 psychological levers for 2026 ─────────────────────────
export const SOLARIS_PARADIGMS: SolarisParadigm[] = [
  {
    n: "01",
    name: "End of Time-Rental",
    promise:
      "You want to price on value or on outcome — not by the hour.",
    mechanism:
      "Solaris gives you a fixed production cost, which mathematically secures your value-based pricing downstream.",
    anchor: "$ per hour → $ per outcome",
  },
  {
    n: "02",
    name: "Anti-Commoditization Shield",
    promise:
      "If your end client knows how to use an LLM, you have to justify your price through a proprietary system — not a shared tool.",
    mechanism:
      "Your Solaris instance becomes that system. B1/B2/B3 hierarchy + brand memory = a defensible moat that belongs to you.",
    anchor: "shared tool → proprietary system",
  },
  {
    n: "03",
    name: "Zero-Management",
    promise:
      "The 2026 dream is no longer 50 employees. It's 3 superhumans orchestrating 50 software agents that never sleep.",
    mechanism:
      "B1 routes, B2 controls, B3 produces. You issue an order — your new async team executes it. No meetings, no planning, no unions.",
    anchor: "50 humans → 3 humans · 50 agents",
  },
];

// ─── Holding context (discreet topbar badge only) ────────────────
export const SOLARIS_HOLDING: SolarisHolding = {
  filiales: [
    {
      id: "solaris",
      code: "01/03",
      name: "SOLARIS",
      scope: "AaaS · agencies",
      active: true,
    },
    {
      id: "nexus",
      code: "02/03",
      name: "NEXUS",
      scope: "Citadel · regulated firms",
      active: false,
    },
    {
      id: "orbiter",
      code: "03/03",
      name: "ORBITER",
      scope: "Field · operations",
      active: false,
    },
  ],
};

// ─── Vault data per archetype ────────────────────────────────────
export const VAULT_BY_ARCH: Record<string, VaultArchData> = {
  revops: {
    slug: "revops-cincinnati",
    lead: "Lyrebird Performance",
    headline: "Five fragmentation points detected.",
    rows: [
      { l: "HubSpot ↔ Stripe: 14 fragmented Zaps", s: "high", t: "12ms" },
      {
        l: "Multi-touch attribution: 3 conflicting models",
        s: "high",
        t: "9ms",
      },
      {
        l: "Client A CRM ≠ Client B CRM (manual replication)",
        s: "high",
        t: "7ms",
      },
      {
        l: "Ad platforms: reporting copy-pasted · 4h / wk",
        s: "med",
        t: "5ms",
      },
      { l: "No versioning on data pipelines", s: "med", t: "4ms" },
    ],
    remedy: "IT Squads · bulletproof pipelines · you sell the revenue",
  },
  forges: {
    slug: "forges-columbus",
    lead: "Mason & Lark Studio",
    headline: "Margin Bleed measured — 78% lost on revisions.",
    rows: [
      {
        l: "Creator/QA ratio: 8 / 1 · critical Founder Load",
        s: "high",
        t: "14ms",
      },
      {
        l: "Avg client revision rounds: 7.2 per asset",
        s: "high",
        t: "8ms",
      },
      { l: "Prompt-Fatigue: 38% of senior time", s: "high", t: "6ms" },
      { l: "No brand RAG · 9% hallucination rate", s: "med", t: "5ms" },
      {
        l: "Templates: 12 versions, no source of truth",
        s: "low",
        t: "3ms",
      },
    ],
    remedy:
      "Paperclip Workspaces · B2 Flash validates before delivery · 10× without a reviewer",
  },
  aaa: {
    slug: "aaa-lexington",
    lead: "Halcyon Automation Co.",
    headline: "Cobbler's Paradox confirmed.",
    rows: [
      {
        l: "Back-office on Make.com · public scenarios",
        s: "high",
        t: "11ms",
      },
      {
        l: "OpenAI bill: $3,200 / mo · 71% of costs",
        s: "high",
        t: "9ms",
      },
      {
        l: "No control plane · no owned infrastructure",
        s: "high",
        t: "13ms",
      },
      {
        l: "AI flows delivered via public platforms",
        s: "med",
        t: "6ms",
      },
      { l: "No defensible technical moat", s: "med", t: "4ms" },
    ],
    remedy:
      "Cyborg squads · you become a software publisher · $1,555 ticket",
  },
  boutiques: {
    slug: "boutiques-louisville",
    lead: "Atelier Norden",
    headline: "Glass Ceiling identified.",
    rows: [
      {
        l: "Headcount: 2 founders · 0 delivery team",
        s: "high",
        t: "10ms",
      },
      {
        l: "Tier-1 clients: 4 · LTV capped at strategy",
        s: "high",
        t: "8ms",
      },
      {
        l: "Execution refused: 6 requests / qtr lost",
        s: "high",
        t: "7ms",
      },
      { l: "Past freelancers: 3 abrupt exits", s: "med", t: "5ms" },
      { l: "Tech white-label: nonexistent", s: "low", t: "3ms" },
    ],
    remedy: "Pure AaaS · ghost factory under your logo · 70% margin",
  },
};
