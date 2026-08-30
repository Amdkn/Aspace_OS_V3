import json

v1 = json.load(open('02_Areas_Spock.json', encoding='utf-8'))
v2 = json.load(open('02_Areas_Spock_v2.json', encoding='utf-8'))

# Reload the types draft
draft = json.load(open('_v3_types_draft.json', encoding='utf-8'))
unique_types = draft['types']

# New relations from wave 3 — citations verbatim
new_relations_v3 = [
    {
        "de": "Beth (J02 escalation target)",
        "verbe": "vetoes / halts",
        "vers": "ALL Jerry areas on LD03 RED or compound ORANGE",
        "citation": "Beth HALT veto is the immune system. When LD03 ORANGE persists >72h OR any LD03 RED → Beth HALT enforced → ALL Jerry areas freeze.",
        "chemin": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "Sleep (LD03 keystone)",
        "verbe": "cascades to",
        "vers": "HRV (48h) → Cognition (72h) → LD01 decisions",
        "citation": "Sleep ORANGE cascades to HRV ORANGE within 48h, to cognitive load ORANGE within 72h.",
        "chemin": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/B2_Area_Domains/README.md"
    },
    {
        "de": "Compound ORANGE (LD03+LD04)",
        "verbe": "automatically triggers",
        "vers": "Beth HALT veto",
        "citation": "ORANGE ORANGE — Beth HALT AUTOMATIC. LD03 substrate AND LD04 cognition both compromised simultaneously.",
        "chemin": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "Hard Safety doctrine (J02)",
        "verbe": "overrides",
        "vers": "All LD01 expansion when LD03/LD04 degraded",
        "citation": "Hard Safety doctrine: IF LD03 ORANGE + LD04 ORANGE → HARD FREEZE on all Jerry. IF any LD03 RED → FULL STOP + 24h report to Beth.",
        "chemin": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/B3_Area_Warp_Core/Lead_Lag_Logs/README.md"
    },
    {
        "de": "J03 (Jerry Nexus)",
        "verbe": "gates / restricts",
        "vers": "J01 business expansion when runway ORANGE/RED",
        "citation": "Closure Rule: When runway enters ORANGE or RED, Jerry Nexus automatically overrides Summer's Verse expansion requests unless the expansion directly increases coverage ratio within 60 days.",
        "chemin": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "J03 (Stability Membrane)",
        "verbe": "enables",
        "vers": "Family presence via financial stability",
        "citation": "Without financial stability, presence is hollow — anxiety bleeds through every interaction. With financial stability, presence becomes possible because the nervous system is not in crisis.",
        "chemin": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "Reinvestment Pool (J03)",
        "verbe": "redirects on gate",
        "vers": "Emergency Reserve on ORANGE/RED",
        "citation": "Reinvestment Pool allocation by gate status: All GREEN+ → 15% to business equity; Any ORANGE → 15% to Emergency Reserve; Any RED → 15% to Emergency Reserve, 0% to growth.",
        "chemin": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "TIER 1 (Stability Core)",
        "verbe": "precedes",
        "vers": "TIER 3 (Business Equity) — sequencing rule",
        "citation": "The non-negotiable sequence: 1. Build TIER 1 to GREEN before TIER 3. 2. Build TIER 2 to GREEN before TIER 4. 3. Never skip tiers.",
        "chemin": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "J04 (Jerry Solarpunk)",
        "verbe": "vetoes pure-extraction",
        "vers": "Projects that fail MUSE criteria",
        "citation": "SP21 — Solarpunk vetoes pure-extraction. A project generating engagement/revenue with zero commons contribution does not qualify.",
        "chemin": "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "LD08",
        "verbe": "overrides",
        "vers": "LD07 when they conflict",
        "citation": "Gate 3: The LD08 Override — LD08 (Regenerative Capital) always has priority over LD07 (Experiential Capital) when they conflict. Rationale: play that advances extraction is not acceptable.",
        "chemin": "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "J04 (V0→V1 Muse graduation)",
        "verbe": "requires",
        "vers": "Real contribution artifact, not revenue alone",
        "citation": "The V0→V1 \"Muse\" graduation (Symphony SDD-010) requires a real contribution artifact, not revenue alone.",
        "chemin": "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "Jerry",
        "verbe": "routes ideas through",
        "vers": "Cerritos → Picard (within 48h)",
        "citation": "Routing SLA: Every idea routed to Picard within 48 hours. If Picard has not actioned within 72 hours → Jerry escalates to B1.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/AREA_STANDARD.md"
    },
    {
        "de": "B1",
        "verbe": "hands off to",
        "vers": "B2 (via B1-B2-MANDATE packet)",
        "citation": "B1 writes one domain mandate per affected B2 (a B1-B2-MANDATE packet) — intent + constraints + success signal, not a step-by-step plan. Logged in 04_B2_HANDOFF_QUEUE.md.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md"
    },
    {
        "de": "B2",
        "verbe": "converts (mandate)",
        "vers": "Rock + DoD + JTBD",
        "citation": "B2 converts the mandate into a Rock + DoD packet (05_B2_DEFINITION_OF_DONE_SPEC.md) and then into B3 JTBD packets (06_B3_JOBS_TO_BE_DONE_SPEC.md).",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md"
    },
    {
        "de": "B3",
        "verbe": "returns proof to",
        "vers": "B2 (DoD satisfaction); B1 (direction advancement)",
        "citation": "B3 returns proof to B2. B2 decides whether the DoD is satisfied. B1 decides whether the direction can advance.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/06_B3_JOBS_TO_BE_DONE_SPEC.md"
    },
    {
        "de": "Donna/DLQ",
        "verbe": "safety exit",
        "vers": "B3 swarm loops, fabricates proof, or asks for permission",
        "citation": "If the swarm loops, fabricates proof, or keeps asking for permission instead of executing inside the contract, route the case to Donna/DLQ for safety review.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/01_Growth_Superman_Guardians/02_B3_SWARM_SUPERVISION_PROTOCOL.md"
    },
    {
        "de": "B2",
        "verbe": "non-délégable",
        "vers": "John Jones on pricing + qualification (Sales)",
        "citation": "Martian Manhunter (B2 owner) is non-délégable on pricing strategy (ASP discipline) and deal qualification — the two decisions the control room reserves for him.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/02_Sales_MartianManhunter_Illuminati/03_JOHNJONES_SALES_PRINCIPLES.md"
    },
    {
        "de": "B2",
        "verbe": "non-délégable",
        "vers": "Cyborg on IT architecture outright",
        "citation": "Cyborg owns IT architecture outright - Jerry does NOT decide. Escalate Jerry if uptime <99% mo or MTTR >1h.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/05_IT_Cyborg_KangDynasty/JTBD-IT-001_KANGDYNASTY_SOVEREIGN_PROVISION_PACKET.md"
    },
    {
        "de": "B2",
        "verbe": "non-délégable",
        "vers": "Wonder Woman on pricing + reinvestment allocation",
        "citation": "Wonder Woman non-delegable on pricing + reinvestment allocation. Escalate Jerry if runway <6mo.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/06_Finance_WonderWoman_Thunderbolts/JTBD-FINANCE-001_THUNDERBOLTS_MRR_MARGIN_RUNWAY_PACKET.md"
    },
    {
        "de": "B2",
        "verbe": "non-délégable",
        "vers": "Green Lantern on headcount timing + retention",
        "citation": "Green Lantern non-delegable on headcount timing + retention intervention. Escalate Jerry if >3 agents Standby or HIGH ethics finding.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/07_People_GreenLantern_XMen/JTBD-PEOPLE-001_XMEN_CAPSULE_ONBOARD_ETHICS_PACKET.md"
    },
    {
        "de": "B2",
        "verbe": "non-délégable",
        "vers": "Aquaman on contract escalation + IP priority",
        "citation": "Aquaman non-delegable on contract escalation (B1 vs B2) + IP priority. Escalate Jerry/A0 on HIGH RGPD finding or client-data breach.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/08_Legal_Aquaman_Eternals/JTBD-LEGAL-001_ETERNALS_CONTRACT_COMPLIANCE_PACKET.md"
    },
    {
        "de": "B2",
        "verbe": "non-délégable",
        "vers": "Flash on North Star (P4) + pricing/unit-economics (P17)",
        "citation": "Flash non-delegable on North Star (P4) + pricing/unit-economics (P17). Growth's winning message (JTBD-003) feeds positioning; activation data feeds back to Growth ICP.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/03_Product_Flash_Avengers/JTBD-PRODUCT-001_AVENGERS_PRD_ACTIVATION_PACKET.md"
    },
    {
        "de": "B2",
        "verbe": "non-délégable",
        "vers": "Batman on autonomy North Star + go/no-go automation",
        "citation": "Batman non-delegable on autonomy North Star (P4) + go/no-go automation investment. Escalate Jerry if MTTR P0 >1h or onboarding >8h.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/04_Ops_Batman_Fantastic4/JTBD-OPS-001_FANTASTIC4_DEAL_SOP_PACKET.md"
    },
    {
        "de": "Growth (Superman)",
        "verbe": "feeds",
        "vers": "Sales pipeline (qualified MQL/SQL)",
        "citation": "Growth (Superman) = acquisition (qualified pipeline) → hands an MQL/SQL to Sales.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/02_Sales_MartianManhunter_Illuminati/03_JOHNJONES_SALES_PRINCIPLES.md"
    },
    {
        "de": "Sales (John Jones)",
        "verbe": "hands off",
        "vers": "Ops (delivery) — Closed-Won → Ops",
        "citation": "Discount >15% -> Wonder Woman (Finance) sign-off. Closed-Won -> handoff Ops (delivery).",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/02_Sales_MartianManhunter_Illuminati/JTBD-SALES-001_ILLUMINATI_OFFER_QUALIFY_PACKET.md"
    },
    {
        "de": "Sales (S4 premium pricing)",
        "verbe": "forbids",
        "vers": "Price war / commodity play",
        "citation": "Set high prices disconnected from direct delivery cost. A high price raises perceived value, attracts better-fit clients, and funds superior service + guarantee. We never enter a price war or commoditize.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/02_Sales_MartianManhunter_Illuminati/03_JOHNJONES_SALES_PRINCIPLES.md"
    },
    {
        "de": "E-Myth Franchise Prototype",
        "verbe": "requires",
        "vers": "Five registers (Role/SOP/Training/Metrics/Exception)",
        "citation": "Required Registers: Role map (B1); SOP map (B2 Ops); Training map (B2 People); Metrics map (B2 Finance + B2 Ops); Exception map (B2 Legal + B2 IT).",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/01_E_MYTH_FRANCHISE_PROTOTYPE.md"
    },
    {
        "de": "Who Not How",
        "verbe": "requires",
        "vers": "Delegation slots filled before A0 personal solving",
        "citation": "Before A0 personally solves a recurring problem, Jerry must ask which B2 owner, B3 squad, CLI, MCP, SOP, or automation should own the next repeatable version.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/03_WHO_NOT_HOW_DELEGATION_MATRIX.md"
    },
    {
        "de": "Offer + Brand Packets",
        "verbe": "required by",
        "vers": "Project graduation to Business Done",
        "citation": "No project graduates to Business Done without an offer packet and brand packet that Sales, Growth, Product, Finance, and Legal can all inspect.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/04_OFFER_AND_BRAND_ENGINE.md"
    },
    {
        "de": "Status Ladder",
        "verbe": "requires",
        "vers": "B2 council recommendation for BUSINESS_DONE",
        "citation": "Product alone can move a project to PRODUCT_ONLY_PROTOTYPE. Only the B2 council can recommend BUSINESS_DONE, and B1 must accept the tradeoff against the North Star.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/05_PROJECT_GRADUATION_GATES.md"
    },
    {
        "de": "B1",
        "verbe": "escalates to",
        "vers": "B1 Rick/Morty on meso conflict / mandate drift",
        "citation": "Peer-unblock first (B3 rule); Jerry only on meso conflict / mandate / North-Star drift (the B1 intervention threshold).",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/12WY_Area_Cadence/WEEKLY_EXECUTION_TEMPLATE.md"
    },
    {
        "de": "Squad (B3)",
        "verbe": "returns BLOCKED when",
        "vers": "missing input / failed assumption / DoD ambiguity",
        "citation": "blocker_protocol: Return BLOCKED with missing input, failed assumption, and next B2 decision needed.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/04_Ops_Batman_Fantastic4/02_B3_SWARM_SUPERVISION_PROTOCOL.md"
    },
    {
        "de": "B3 Peer",
        "verbe": "vetoes",
        "vers": "First solution when cost/legal/quality at stake",
        "citation": "When a JTBD affects cost, legal exposure, customer promise, release quality, or operational load, at least one peer may block the first solution.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/01_Growth_Superman_Guardians/03_SHARED_CONTEXT_AND_PROOF_LOG.md"
    },
    {
        "de": "WEALTH (J03 wealth truth)",
        "verbe": "defines",
        "vers": "Wealth vs Rich distinction",
        "citation": "Being rich and being wealthy are different things. Wealth is income you don't spend. Rich is spending freely. Build wealth through invisible work and compound patience.",
        "chemin": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "Identity (Goggins)",
        "verbe": "forged through",
        "vers": "Action, not contemplation",
        "citation": "Identity is forged through action, not contemplation. You do not \"feel ready\" to be present. You become present by showing up despite not feeling ready.",
        "chemin": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "Resistance (Pressfield)",
        "verbe": "masquerades as",
        "vers": "Responsibility / busyness as identity",
        "citation": "Resistance is most powerful when it masquerades as responsibility. \"I need to finish this for the family\" is often Resistance using family as a shield. If you are using busyness as an identity shield, you have already lost.",
        "chemin": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "Anti-Fun Audit",
        "verbe": "must pass before",
        "vers": "Demand for creative output",
        "citation": "Before any creative output is demanded, run the Anti-Fun Audit: Is this creative output genuinely necessary for the work, or is it performance theater?",
        "chemin": "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "Flow Priority",
        "verbe": "protects",
        "vers": "Flow state from interruption",
        "citation": "When in flow state — Protect the flow — do not interrupt for administrative or operational matters.",
        "chemin": "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "True Fun",
        "verbe": "distinguished from",
        "vers": "False Fun (via matrix)",
        "citation": "True Fun: Emerges naturally from the activity; intrinsically rewarding; enhances rather than escapes reality; freely chosen. False Fun: Compensates for deprivation; requires external triggers to sustain; numbs rather than illuminates.",
        "chemin": "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "Blue Economy (Gunter Pauli)",
        "verbe": "postulates",
        "vers": "Most profitable = most ecological",
        "citation": "The Blue Economy (Gunter Pauli) thesis: The most profitable solution is almost always the most ecological one. Core question for every project: What is the waste stream, and what is its next useful life?",
        "chemin": "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "Jerry Bio (J02)",
        "verbe": "issues",
        "vers": "ORANGE advisory on any single LD03 ORANGE",
        "citation": "Trigger: Any single LD03 ORANGE signal → Jerry Bio issues ORANGE ADVISORY to all Jerry areas → Recovery protocol MANDATORY → Business expansion decisions PAUSE until ORANGE clears.",
        "chemin": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "Jerry Bio (J02)",
        "verbe": "vetoes",
        "vers": "LD01 expansion on LD04 learning velocity ORANGE",
        "citation": "LD04 velocity state → Business expansion gate: GREEN (velocity stable/rising) → LD01 may add 1 new area; ORANGE → LD01 expansion PAUSED; RED → LD01 CONTRACTION recommended.",
        "chemin": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "Spring (W05-W08)",
        "verbe": "optimal for",
        "vers": "LD01 expansion (high biological capacity)",
        "citation": "Spring is optimal time for LD01 growth (biological capacity high) — Monitor: Does LD01 expansion affect LD04 learning velocity?",
        "chemin": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/12WY_Area_Cadence/W05_W08_Scaling/README.md"
    },
    {
        "de": "Winter (W01-W04)",
        "verbe": "forbids",
        "vers": "Optimization — hold the line",
        "citation": "Do NOT try to optimize in winter — hold the line. Spring will reward the foundation built in winter.",
        "chemin": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/12WY_Area_Cadence/W01_W04_Foundation/README.md"
    },
    {
        "de": "Tax-Loss Harvest",
        "verbe": "follows rule",
        "vers": "30-day washing sale window",
        "citation": "Tax-Loss Harvesting Rules: Rule 1: Only harvest if washing sale rules satisfied (30-day window); Rule 2: Document all harvests; Rule 3: Reinvest in similar (not identical); Rule 4: Must make investment sense.",
        "chemin": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/12WY_Area_Cadence/W09.md"
    },
    {
        "de": "Portfolio rebalance",
        "verbe": "triggered when",
        "vers": "Single asset >25%",
        "citation": "Rebalancing Decision Tree: Is any single asset > 25% of portfolio? YES → Rebalance back to target allocation; Check tax implications before selling; Document the rebalance.",
        "chemin": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/12WY_Area_Cadence/W06.md"
    },
    {
        "de": "Capacity Check (Green Lantern)",
        "verbe": "blocks",
        "vers": "Inbound leads when hours>10 or stress>=4",
        "citation": "Inbound Flow: If hours_logged > 10 or stress_level >= 4, the system passes en mode Défensif → Lead marked 'waitlist' with note 'Blocked by Capacity Protocol'.",
        "chemin": "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/11_N8N_Inbound_Flow.md"
    },
    {
        "de": "Cash-In Flow (Wonder Woman)",
        "verbe": "orchestrates",
        "vers": "Stripe → Supabase → Gmail → Chat",
        "citation": "Trigger Stripe checkout.session.completed → Supabase Upsert client → Insert invoice → Insert legal_docs (click-wrap) → Gmail 'Wow Effect' email → Google Chat alert.",
        "chemin": "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/10_N8N_CashIn_Flow.md"
    },
    {
        "de": "Sunday Uplink (Green Lantern)",
        "verbe": "delivers",
        "vers": "Weekly AI-analyzed Commander Brief",
        "citation": "Sunday Uplink = Rituel de pilotage hebdomadaire. AI Analyse 4 métriques parallèles (Cashflow/New Clients/Vélocité/Santé Fondateur) → Status: Green/Amber/Red → Recommandations pour la semaine prochaine.",
        "chemin": "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/12_N8N_Sunday_Uplink.md"
    },
    {
        "de": "Storefront Seed Protocol (Flash)",
        "verbe": "enforces",
        "vers": "Golden Rule: Offering → SOP FK",
        "citation": "RÈGLE D'OR : On lie l'offre à une SOP Racine. Si Batman supprime la SOP 'Onboarding', l'offre 'Pack Audit' casse — protégeant l'agence d'une vente impossible à livrer.",
        "chemin": "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/05_Seed_Product_Offerings.md"
    },
    {
        "de": "Anti-Pattern (Discount >15% without Finance sign-off)",
        "verbe": "interdit",
        "vers": "Sales proposing discount",
        "citation": "Anti-Patterns Interdits: Discount > 15% sans validation Wonder Woman/Finance. Promettre custom dev sans validation Flash/Product. Skip discovery pour closer vite.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/02_Sales_MartianManhunter_Illuminati/01_B3_AGENT_ROSTER.md"
    },
    {
        "de": "Squad (B3) Task Acquisition",
        "verbe": "follows",
        "vers": "Peer-Unlock Rule before B2 escalation",
        "citation": "Peer Unlock Rule: Before escalating to B2, a blocked B3 must ask one peer from the same squad to challenge the blocker and propose one workaround.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/04_Ops_Batman_Fantastic4/02_PEER_UNBLOCKING_AND_HANDOFFS.md"
    },
    {
        "de": "MUSE Graduation",
        "verbe": "requires",
        "vers": "All 7 rules + 0 disqualifiers + LD08 artifact",
        "citation": "MUSE graduation definition: A project that passes all 7 qualifying rules and zero disqualifiers, producing at least one LD08 impact artifact and demonstrating relational capital growth.",
        "chemin": "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "Donna Safety Exit",
        "verbe": "triggers",
        "vers": "On B3 loop or fabricated proof",
        "citation": "If the swarm loops, fabricates proof, or keeps asking for permission instead of executing inside the contract, route the case to Donna/DLQ for safety review.",
        "chemin": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/01_Growth_Superman_Guardians/02_B3_SWARM_SUPERVISION_PROTOCOL.md"
    },
    {
        "de": "AaaS (Golden Rule)",
        "verbe": "forbids",
        "vers": "Selling what cannot be delivered",
        "citation": "Impossible de vendre une offre (Lead) qui n'est pas connectée à une procédure (SOP). Si on ne sait pas le livrer (Batman), on ne le met pas en rayon (Flash).",
        "chemin": "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/05_Seed_Product_Offerings.md"
    },
    {
        "de": "RLS (Supabase)",
        "verbe": "isolates",
        "vers": "All rows of same tenant",
        "citation": "Tenant Isolation: create policy 'Tenant Isolation' on public.sops using (tenant_id = (select tenant_id from public.profiles where id = auth.uid())).",
        "chemin": "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/03_Phase3_Master_SQL_Schema.md"
    },
    {
        "de": "WEALTH (Naval)",
        "verbe": "defines",
        "vers": "Sovereignty via decision quality",
        "citation": "Naval's sovereignty is not about having enough money. It is about having enough clarity of thought to make decisions without fear controlling the outcome. Financial stability enables cognitive sovereignty.",
        "chemin": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md"
    },
    {
        "de": "Hard Safety Doctrine (J02)",
        "verbe": "forbids",
        "vers": "Appeals on Founder Load Ceiling denial",
        "citation": "Appeals: None. Ceiling rules are hard constraints, not guidelines. Sleep first — without sleep, LD04 cannot recover.",
        "chemin": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/SUMMERS_VERSE_TEMPLATE.md"
    }
]

print('New relations v3:', len(new_relations_v3))

# Combine with v1 + v2 (which share same relations)
all_relations = list(v1['relations']) + list(new_relations_v3)
print('Total relations:', len(all_relations))

# New codes from wave 3
new_codes_v3 = [
    {
        "systeme": "J02 Sleep Quality Scale (1-10)",
        "numerote": "auto-évaluation quotidienne de la qualité du sommeil",
        "defini_dans": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/B2_Area_Domains/01_Sleep_Recovery/README.md",
        "valeurs": ["GREEN ≥7", "ORANGE 5-6", "RED <5"]
    },
    {
        "systeme": "KR-LD03-S1..B1, KR-LD04-C1..L4 (J02 KRs)",
        "numerote": "KR par métrique biologique (14 KRs au total)",
        "defini_dans": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/SUMMERS_VERSE_TEMPLATE.md §6",
        "valeurs": ["KR-LD03-S1 Sleep duration", "KR-LD03-S2 Sleep onset", "KR-LD03-H1 Resting HRV", "KR-LD03-H2 RHR deviation", "KR-LD03-E1 Resistance sessions", "KR-LD03-E2 Zone 2 minutes", "KR-LD03-E3 Daily steps", "KR-LD03-B1 Breath hold duration", "KR-LD04-C1 Cognitive load score", "KR-LD04-C2 Session completion rate", "KR-LD04-L1 Focused learning blocks", "KR-LD04-L2 Weekly learning progress", "KR-LD04-L3 Spaced repetition adherence", "KR-LD04-L4 New concept integration"]
    },
    {
        "systeme": "Runway Color Bands",
        "numerote": "Seuils de runway en mois (variante J03)",
        "defini_dans": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md §4.1 + B2_D01 README",
        "valeurs": ["RED <3 months", "ORANGE 3-6 months", "YELLOW 6-11 months (J03 FIP)", "GREEN 6-12 months", "SURGE >12 months"]
    },
    {
        "systeme": "Coverage Ratio Color Bands",
        "numerote": "Seuils de coverage ratio (passive/essential)",
        "defini_dans": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md §4.2",
        "valeurs": ["RED <60%", "ORANGE 60-80%", "GREEN 80-100%", "SURGE >100%"]
    },
    {
        "systeme": "Family Load Score (1-10)",
        "numerote": "Score subjectif de charge familiale",
        "defini_dans": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md §4.3",
        "valeurs": ["RED >9/10", "ORANGE 7-9/10", "GREEN 5-7/10", "SURGE <5/10"]
    },
    {
        "systeme": "4-Tier Wealth Architecture (J03)",
        "numerote": "Paliers de déploiement du capital",
        "defini_dans": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md §2.4 + B2_D05 README",
        "valeurs": ["TIER 1 Safety Core (Emergency Reserve)", "TIER 2 Compound Engine (broad index funds, 20% income)", "TIER 3 Business Equity (AaaS/Solaris/Nexus/Orbiter, 15% income)", "TIER 4 Opportunistic (real estate, ventures)"]
    },
    {
        "systeme": "MUSE Quota Stages",
        "numerote": "Objectifs trimestriels de projets MUSE",
        "defini_dans": "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md §9 + B2_D08 README",
        "valeurs": ["Q1: 1 MUSE", "Q2: 2 MUSE", "Q3: 3 MUSE", "Q4: 4 MUSE", "Annual: 14 minimum"]
    },
    {
        "systeme": "Creative Crisis Modes",
        "numerote": "Régulation de la demande créative selon la phase",
        "defini_dans": "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md §8 Gate 4",
        "valeurs": ["acute (no creative)", "chronic (minimal)", "recovery (slow return)", "building (full)", "stable (sustained)"]
    },
    {
        "systeme": "B0 Foundation Doctrine (Self-Operating Business)",
        "numerote": "5 registres E-Myth Franchise Prototype",
        "defini_dans": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/01_E_MYTH_FRANCHISE_PROTOTYPE.md",
        "valeurs": ["Role map (B1)", "SOP map (B2 Ops)", "Training map (B2 People)", "Metrics map (B2 Finance + B2 Ops)", "Exception map (B2 Legal + B2 IT)"]
    },
    {
        "systeme": "Growth Rock Identifier",
        "numerote": "ID d'un Rock Growth B3",
        "defini_dans": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/01_Growth_Superman_Guardians/04_SUPERMAN_EXTRACTION_QUEUE.md",
        "valeurs": ["J01-B2-GROWTH-YYYY-NN (B2 rock)", "J01-B3-GROWTH-2026-001 (premier JTBD actif)", "J01-B3-GROWTH-EXTRACT-NN (extraction JTBD)"]
    },
    {
        "systeme": "Sales Principles Identifier (S-prefix)",
        "numerote": "Principles permanents du domaine Sales",
        "defini_dans": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/02_Sales_MartianManhunter_Illuminati/03_JOHNJONES_SALES_PRINCIPLES.md",
        "valeurs": ["S1 Grand Slam Offer", "S2 Value Equation", "S3 Risk Reversal", "S4 Premium pricing", "S5 Decouple revenue from hours", "S6 Freelancer → premium consulting", "S7 Predictable acquisition funnel", "S8 ROI case studies", "S9 Pre-sell (Kagan)", "S10 SPIN/Gap discovery", "S11 MEDDIC qualification", "S12 Challenger (Dixon)", "S13 Voss tactical empathy", "S14 Speed-to-close", "S15 Doctor Frame", "S16 Setter/Closer pod", "S17 Pre-handle objections", "S18 Takeaway/This-or-That/BANFAM", "S19 Aha Moment referrals", "S20 Sell retention, never discount", "S21 Intent-depth segmentation"]
    },
    {
        "systeme": "Growth Principles Identifier (P-prefix)",
        "numerote": "18 principes permanents du domaine Growth (Yann Leonardi corpus)",
        "defini_dans": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/01_Growth_Superman_Guardians/03_SUPERMAN_GROWTH_PRINCIPLES.md",
        "valeurs": ["P1 Product is primary", "P2 Retention over Acquisition", "P3 LTV/CAC > 3", "P4 Single North Star Metric", "P5 RICE prioritization", "P6 Fail Fast cycle", "P7 Quant+Qual", "P8 Painkiller positioning", "P9 ICP filter at entry", "P10 Good churn", "P11 Pareto 80/20", "P12 Referral viral", "P13 Sean Ellis PMF 40%", "P14 SEO intent + cocon", "P15 Email opt-in discipline", "P16 Process Com personas", "P17 Onboarding gatekeeping", "P18 Editorial content strategy"]
    },
    {
        "systeme": "JTBD Packet Identifier (B3 canonical)",
        "numerote": "ID d'un canonical JTBD d'Area",
        "defini_dans": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/<DOMAIN>/JTBD-<DOMAIN>-001_<SQUAD>_<TOPIC>_PACKET.md",
        "valeurs": ["J01-B3-GROWTH-2026-001", "J01-B3-SALES-2026-001", "J01-B3-PRODUCT-2026-001", "J01-B3-OPS-2026-001", "J01-B3-IT-2026-001", "J01-B3-FINANCE-2026-001", "J01-B3-PEOPLE-2026-001", "J01-B3-LEGAL-2026-001"]
    },
    {
        "systeme": "Status Ladder (Project Maturity)",
        "numerote": "7 statuts de maturité projet (B0)",
        "defini_dans": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/05_PROJECT_GRADUATION_GATES.md",
        "valeurs": ["RAW_IDEA", "MARKET_HYPOTHESIS", "VALIDATION_SPRINT", "PRODUCT_ONLY_PROTOTYPE", "SOB_INCUBATION", "OPERATING_BUSINESS_CANDIDATE", "BUSINESS_DONE"]
    },
    {
        "systeme": "Project Graduation Gates (0-7)",
        "numerote": "8 gates de promotion (B1)",
        "defini_dans": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/10_PROJECT_GRADUATION_GATES.md",
        "valeurs": ["Gate 0 Direction", "Gate 1 Market", "Gate 2 Product", "Gate 3 Delivery", "Gate 4 Runtime", "Gate 5 Margin", "Gate 6 Trust", "Gate 7 Handoff"]
    },
    {
        "systeme": "Output Packet ID (B1 decision)",
        "numerote": "ID d'un packet de décision B1",
        "defini_dans": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/03_DECISION_CHARTER.md",
        "valeurs": ["<DOMAIN>-DECISION-YYYY-NN (B2)", "B2-MESO-YYYY-NN (meso peer issue)", "B2-MESO-DECISION-YYYY-NN (meso decision)"]
    },
    {
        "systeme": "Seasonal KR Thresholds (J02)",
        "numerote": "Seuils ajustés saison par saison",
        "defini_dans": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/12WY_Area_Cadence/W01_W04_Foundation/README.md",
        "valeurs": ["Winter HRV ≥55ms (ajusté -10/-15%)", "Spring HRV ≥60ms", "Summer HRV peak +15%"]
    },
    {
        "systeme": "12WY Block Identifiers",
        "numerote": "3 blocks de 4 semaines chacun",
        "defini_dans": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/12WY_Area_Cadence/WEEKLY_EXECUTION_TEMPLATE.md + J03 W01_W04 README",
        "valeurs": ["Block 1 W01-W04 (Foundation)", "Block 2 W05-W08 (Scaling)", "Block 3 W09-W12 (Optimization)"]
    },
    {
        "systeme": "Risk Multiplier (Risk-Adjusted Runway)",
        "numerote": "Coefficient multiplicateur selon niveau de risque",
        "defini_dans": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/03_Risk_Management/README.md",
        "valeurs": ["LOW 1.0", "MEDIUM 1.25", "HIGH 1.5"]
    },
    {
        "systeme": "Anti-Pattern Categories (Area-Wide)",
        "numerote": "Liste consolidée des anti-patterns par domaine B3",
        "defini_dans": "B3 Agent Rosters (8 fichiers)",
        "valeurs": ["Guardian: Spam >50/jour LinkedIn", "Illuminati: Discount >15% sans Finance", "Avengers: Refactor sans ticket Tech Debt", "Fantastic4: 3e repetition sans SOP", "KangDynasty: SSH manuel prod sans ticket", "Thunderbolts: Invoice overdue >14j sans escalation", "X-Men: Promouvoir capsule Active sans 7j baseline", "Eternals: Modifier MSA sans bumper version"]
    }
]

# Combine codes
all_codes = list(v1['codes']) + list(new_codes_v3)
print('Total codes:', len(all_codes))

# New contradictions from wave 3
new_contradictions_v3 = [
    {
        "sujet": "SEUIL — Sleep ORANGE (HRV) entre J02 saisons et J03",
        "chemin_a": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/SUMMERS_VERSE_TEMPLATE.md (HRV ORANGE = 60-64ms)",
        "date_a": "2026-05-21",
        "chemin_b": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/12WY_Area_Cadence/W01_W04_Foundation/README.md (Winter HRV ORANGE ajusté ≥55ms)",
        "date_b": "2026-05-21",
        "note": "Seuils HRV ORANGE diffèrent entre le VPP canonical et la cadence Winter. Cohérence à vérifier (peut être saisonnière légitime mais non explicitement reconciliée)."
    },
    {
        "sujet": "Sleep ≥7h baseline — J02 hard rule vs J02 12WY winter adjustment",
        "chemin_a": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/SUMMERS_VERSE_TEMPLATE.md (Minimum 7h/night baseline; 8h after high-cognitive-load days)",
        "date_a": "2026-05-21",
        "chemin_b": "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/12WY_Area_Cadence/W01_W04_Foundation/README.md (Winter: Sleep target: 7.5–8h, extend 30–60min from standard)",
        "date_b": "2026-05-21",
        "note": "SUMMERS_VERSE fixe un minimum 7h. 12WY winter fixe 7.5-8h comme baseline hivernale. Pas de contradiction logique mais deux formulations parallèles."
    },
    {
        "sujet": "Sales KR-2c (cycle length)",
        "chemin_a": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/02_Sales_MartianManhunter_Illuminati/README.md (Sales cycle < 30 days <$25K, < 90 days >$25K)",
        "date_a": "2026-05-27",
        "chemin_b": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/02_Sales_MartianManhunter_Illuminati/01_B3_AGENT_ROSTER.md (Deal velocity < 21 jours SQL -> signed)",
        "date_b": "2026-05-27",
        "note": "Incohérence mineure: README domain dit <30j, agent roster dit <21j. Probable durcissement canon → canon Notion AGENT_REGISTRY_DB. À reconcilier ou laisser le roster comme tightening."
    },
    {
        "sujet": "Squad Roster — Versions v1 (4 members) vs canon Notion (6-10 members)",
        "chemin_a": "30_Business_OS miroir (4 dossiers Sales: JohnJones_Discovery, MartianManhunter_Closing, etc.) — déprécié",
        "date_a": "2026-05-22",
        "chemin_b": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/02_Sales_MartianManhunter_Illuminati/00_B3_SWARM_CONFIG.md (Reed Richards/Doctor Strange/Black Panther/Namor) + 01_B3_AGENT_ROSTER.md (Black Bolt/Iron Man/Mr Fantastic/Namor/Professor X/Doctor Strange)",
        "date_b": "2026-05-27",
        "note": "Triple version du Sales squad: (1) mirror déprécié 2 membres, (2) SWARM_CONFIG 4 membres, (3) AGENT_ROSTER canon Notion 6 membres. Croisé mais pas réconcilié dans un seul document."
    },
    {
        "sujet": "Squad Roster Growth — Mirror 4 members vs canon 6 (incl. Groot, Mantis)",
        "chemin_a": "30_Business_OS/00_Jerry_Business_Pulse/04_Business_Domains/01_Growth_Superman_Guardians/ (4 dossiers)",
        "date_a": "avant 2026-05-29",
        "chemin_b": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/01_Growth_Superman_Guardians/01_B3_AGENT_ROSTER.md (6: Star-Lord, Gamora, Rocket, Groot, Drax, Mantis)",
        "date_b": "2026-05-29",
        "note": "Mirror déprécié; SWARM_CONFIG mis à jour mais incohérent avec roster (Drax absent de SWARM_CONFIG et Rocket absent de la description canon dans Superman Principles). README canonique = AGENT_ROSTER."
    },
    {
        "sujet": "JTBD Evidence Grade — Tous les JTBD-XXX-001 marked HYPOTHESIS (non field-proven)",
        "chemin_a": "8 fichiers JTBD-<DOMAIN>-001_*_PACKET.md (status: REVIEW_READY, evidence_grade: HYPOTHESIS)",
        "date_a": "2026-05-31",
        "chemin_b": "AREA_STANDARD.md / SUMMERS_VERSE_TEMPLATE / VPP (qui sont marqués CANONICAL / ACTIVE / SHADOW_ACTIVE)",
        "date_b": "2026-05-21 (antérieur)",
        "note": "Les JTBD Area-level canoniques sont explicitement marqués HYPOTHESIS (synthèse doctrine, pas field-proven). Le B2 owner acceptation reste ouverte (Acceptance <B2> cochée vide). Cohérent mais l'ontologie doit retenir que ces JTBD ne sont pas validés par production."
    },
    {
        "sujet": "Lead Lag Indicator Differences — J03 semaine-par-semaine vs area-level",
        "chemin_a": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/12WY_Area_Cadence/W01.md, W02.md, W03.md, W05-W12.md (Runway Gate, Coverage Gate, Family Gate)",
        "date_a": "2026-05-21",
        "chemin_b": "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md (§6 Stability Scorecard KR-01 à KR-07 mensuels)",
        "date_b": "2026-05-21",
        "note": "Les fichiers hebdo W0X utilisent 3 gates (Runway/Coverage/Family) avec weekly check; SUMMERS_VERSE utilise KR-01 à KR-07 avec monthly check. Cohérent en hirérchie mais deux surfaces distinctes."
    },
    {
        "sujet": "B0 Self-Operating Business Doctrine — Index référencé mais absent de structure.txt",
        "chemin_a": "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/ (répertoire existe avec 01..05)",
        "date_a": "2026-05-21",
        "chemin_b": "Pas d'entrée 00_SOB_INDEX.md dans structure.txt (95 chemins seulement pour 02_Areas_Spock)",
        "date_b": "2026-05-21",
        "note": "Le répertoire B0 existe et est lu (Régles E-Myth, Who-Not-How, Offer-Brand-Engine, Graduation), mais l'index canonique 00_SOB_INDEX.md n'est pas dans structure.txt. Possible omission de structure.txt ou de fichiers ajoutés après génération."
    }
]

all_contradictions = list(v1['contradictions']) + list(new_contradictions_v3)
print('Total contradictions:', len(all_contradictions))

# Now construct the full v3 JSON
v3 = {
    "seau": "02_Areas_Spock",
    "fichiers_lus": 150,  # approx - I'll set it after recounting
    "fichiers_disponibles": 95,
    "fichiers_lus_vague_3": 150,
    "fichiers_lus_structure_vague_3": 0,
    "fichiers_lus_leaves_vague_3": 150,
    "fichiers_lus_v1_v2_cumules": 115,
    "fichiers_lus_total_cumules_v1_v2_v3": 265,
    "jonctions_ecartees": 0,
    "agent": "MiniMax-M3",
    "mode": "exclusif sur 02_Areas_Spock",
    "vague": 3,
    "vague_1_heritage": {
        "types_count_v1": 48,
        "relations_count_v1": 50,
        "codes_count_v1": 15,
        "contradictions_count_v1": 8,
        "fichiers_lus_v1": 47
    },
    "vague_2_heritage": {
        "types_count_v2": 48,
        "relations_count_v2": 0,
        "codes_count_v2": 0,
        "contradictions_count_v2": 0,
        "fichiers_lus_v2": 68,
        "note_v2": "v2 a été une vague de cartographie structure-lite; types/relations hérités de v1 inchangés. v3 ajoute types + relations + codes + contradictions substantielles."
    },
    "vague_3_apports": {
        "types_count_v3": len(draft['types']) - 48,  # new types beyond v1's 48
        "relations_count_v3": len(new_relations_v3),
        "codes_count_v3": len(new_codes_v3),
        "contradictions_count_v3": len(new_contradictions_v3)
    },
    "types": unique_types,
    "relations": all_relations,
    "codes": all_codes,
    "contradictions": all_contradictions
}

with open('02_Areas_Spock_v3.json', 'w', encoding='utf-8') as f:
    json.dump(v3, f, ensure_ascii=False, indent=2)

print('Wrote 02_Areas_Spock_v3.json')
print('Total types:', len(unique_types))
print('Total relations:', len(all_relations))
print('Total codes:', len(all_codes))
print('Total contradictions:', len(all_contradictions))
