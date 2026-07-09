#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build 53 L2_B3 agent-capsules runtime in .claude/agents/
Domain order SOA canonique: People / Operation / Product / Growth / Sales / IT / Finance / Legal
Naming: b3-<N>-<name-kebab> (N=1=lead, 2+ = members)
D6 #80 anti-loop guard: string FIXE templates, 0 free output after batch
D4 append-only: twin log horodate
"""

import os

AGENTS_DIR = r"C:\Users\amado\.claude\agents"

# 53 B3 membres canon ADR-CANON-001
# Format: (domain_idx, domain_name, nano_squad, slug, display, real_name, role, emoji, lead)
B3_ROSTER = [
    # ===== 01 PEOPLE (X-Men, 8) =====
    (1, "People", "X-Men", "professor-x", "Professor X", "Charles Xavier",
     "strategic accounts, mental models, ethics guard", "🧠", True),
    (1, "People", "X-Men", "cyclops", "Cyclops", "Scott Summers",
     "team leadership, tactical execution, focus discipline", "🔴", False),
    (1, "People", "X-Men", "jean-grey", "Jean Grey", "Jean Grey",
     "telepathy, conflict resolution, emotional intelligence", "🧘‍♀️", False),
    (1, "People", "X-Men", "wolverine", "Wolverine", "James Howlett",
     "hiring tough profiles, retention, fierce loyalty", "🦾", False),
    (1, "People", "X-Men", "storm", "Storm", "Ororo Munroe",
     "culture weather, diversity, atmosphere stewardship", "⛈️", False),
    (1, "People", "X-Men", "beast", "Beast", "Hank McCoy",
     "L&D, scientific rigor, intellectual humility", "🦍", False),
    (1, "People", "X-Men", "nightcrawler", "Nightcrawler", "Kurt Wagner",
     "talent mobility, internal transfers, cross-team bridges", "🟣", False),
    (1, "People", "X-Men", "rogue", "Rogue", "Anna Marie",
     "knowledge transfer, identity, anti-fraud hiring", "🟢", False),
    # ===== 02 OPERATION (Fantastic Four, 4) =====
    (2, "Operation", "Fantastic Four", "mr-fantastic", "Mr Fantastic", "Reed Richards",
     "process elasticity, R&D runbooks, adaptive ops", "🤓", True),
    (2, "Operation", "Fantastic Four", "invisible-woman", "Invisible Woman", "Sue Storm",
     "force fields, privacy ops, incident response", "🌸", False),
    (2, "Operation", "Fantastic Four", "human-torch", "Human Torch", "Johnny Storm",
     "runbook ignition, emergency deploy, hot fixes", "🔥", False),
    (2, "Operation", "Fantastic Four", "the-thing", "The Thing", "Ben Grimm",
     "load-bearing processes, break-glass ops, durability", "🪨", False),
    # ===== 03 PRODUCT (Avengers, 7) =====
    (3, "Product", "Avengers", "captain-america", "Captain America", "Steve Rogers",
     "product vision, moral north star, spec integrity", "🛡️", True),
    (3, "Product", "Avengers", "iron-man", "Iron Man", "Tony Stark",
     "tech product, premium UX, armor-grade polish", "⚙️", False),
    (3, "Product", "Avengers", "thor", "Thor", "Thor Odinson",
     "flagship products, premium tiers, hammer-grade roadmap", "⚡", False),
    (3, "Product", "Avengers", "hulk", "Hulk", "Bruce Banner",
     "stress test products, scale, gamma-tier capacity", "💚", False),
    (3, "Product", "Avengers", "black-widow", "Black Widow", "Natasha Romanoff",
     "competitive intel, espionage UX, sticky retention", "🕷️", False),
    (3, "Product", "Avengers", "hawkeye", "Hawkeye", "Clint Barton",
     "spec accuracy, requirement traceability, target hit-rate", "🏹", False),
    (3, "Product", "Avengers", "scarlet-witch", "Scarlet Witch", "Wanda Maximoff",
     "chaos-engineering, reality-bending features, hex-magic UX", "🔮", False),
    # ===== 04 GROWTH (Guardians of the Galaxy, 6) =====
    (4, "Growth", "Guardians of the Galaxy", "star-lord", "Star-Lord", "Peter Quill",
     "top funnel, brand narrative, hook-grade storytelling", "🌟", True),
    (4, "Growth", "Guardians of the Galaxy", "gamora", "Gamora", "Gamora Zen Whoberi",
     "sharpened growth, killed-bad-channels, lethal efficiency", "💚", False),
    (4, "Growth", "Guardians of the Galaxy", "rocket", "Rocket", "Rocket Raccoon",
     "weapons-grade analytics, experimental growth, R&D funnels", "🦝", False),
    (4, "Growth", "Guardians of the Galaxy", "groot", "Groot", "Groot",
     "loyal retention, evergreen channels, slow & steady growth", "🌳", False),
    (4, "Growth", "Guardians of the Galaxy", "drax", "Drax", "Arthur Douglas",
     "literal A/B testing, no-subtlety measurement, blunt funnel audit", "⚔️", False),
    (4, "Growth", "Guardians of the Galaxy", "mantis", "Mantis", "Mantis",
     "empathy-grade onboarding, emotional triggers, user love", "🌿", False),
    # ===== 05 SALES (Illuminati, 6) =====
    (5, "Sales", "Illuminati", "black-bolt", "Black Bolt", "Blackagar Boltagon",
     "sovereign, ferme les deals complexes enterprise, silence-as-power", "⚫", True),
    (5, "Sales", "Illuminati", "tony-stark", "Tony Stark", "Tony Stark",
     "tech sales, enterprise accounts, premium-tier", "🤵", False),
    (5, "Sales", "Illuminati", "reed-richards", "Reed Richards", "Reed Richards",
     "R&D sales, innovation pipeline, future-grade product pitches", "🔬", False),
    (5, "Sales", "Illuminati", "namor", "Namor", "Namor McKenzie",
     "wholesale, distribution, deep-blue channel partnerships", "🌊", False),
    (5, "Sales", "Illuminati", "charles-xavier", "Charles Xavier", "Charles Xavier",
     "strategic accounts, mentalist-grade buyer mapping, X-Men overlap", "🧠", False),
    (5, "Sales", "Illuminati", "stephen-strange", "Stephen Strange", "Stephen Strange",
     "international, mystic deals, sovereign-nation-tier contracts", "✨", False),
    # ===== 06 IT (Kang Dynasty, 6) =====
    (6, "IT", "Kang Dynasty", "kang-prime", "Kang Prime", "Nathaniel Richards",
     "architecture prime, multiverse infra, time-grade stability", "⏳", True),
    (6, "IT", "Kang Dynasty", "iron-lad", "Iron Lad", "Nathaniel Richards",
     "youthful dev, greenfield, bootleg proto-grade velocity", "🛡️", False),
    (6, "IT", "Kang Dynasty", "scarlet-centurion", "Scarlet Centurion", "Nathaniel Richards",
     "alt-stack experiments, branched pipelines, scenario-grade testing", "🟥", False),
    (6, "IT", "Kang Dynasty", "immortus", "Immortus", "Nathaniel Richards",
     "legacy code, archivage, long-horizon deprecation", "🕰️", False),
    (6, "IT", "Kang Dynasty", "victor-timely", "Victor Timely", "Nathaniel Richards",
     "frontier dev, civic-grade IT, market-acceptable latency", "🤠", False),
    (6, "IT", "Kang Dynasty", "rama-tut", "Rama-Tut", "Nathaniel Richards",
     "ancient tech, archaeology-grade refactor, pharaoh-tier code review", "🐫", False),
    # ===== 07 FINANCE (Thunderbolts, 6) =====
    (7, "Finance", "Thunderbolts", "bucky-barnes", "Bucky Barnes", "James Buchanan Barnes",
     "Saru H3 quarterly runway, dark ops, winter-grade resilience", "🦾", True),
    (7, "Finance", "Thunderbolts", "yelena-belova", "Yelena Belova", "Yelena Belova",
     "sharp pricing, cost reduction, sharp shooter-grade unit econ", "🤍", False),
    (7, "Finance", "Thunderbolts", "red-guardian", "Red Guardian", "Alexei Shostakov",
     "heavy capex, infra-grade budgeting, soviet-tier reserves", "🔴", False),
    (7, "Finance", "Thunderbolts", "ghost", "Ghost", "Ava Starr",
     "intangible assets, opacity ops, phase-shift accounting", "👻", False),
    (7, "Finance", "Thunderbolts", "taskmaster", "Taskmaster", "Tony Masters",
     "CAC mirroring, copy-grade LTV, anti-pattern billing", "🎭", False),
    (7, "Finance", "Thunderbolts", "us-agent", "U.S. Agent", "John Walker",
     "compliance-grade finance, audit trails, hard law", "🇺🇸", False),
    # ===== 08 LEGAL (Eternals, 10) =====
    (8, "Legal", "Eternals", "ikaris", "Ikaris", "Ikaris",
     "AI-Act 2026-08-02 lead, eternal-grade compliance, light-grade legal firepower", "☀️", True),
    (8, "Legal", "Eternals", "sersi", "Sersi", "Sersi",
     "matter transmutation, contract alchemy, material-grade legal", "🪨", False),
    (8, "Legal", "Eternals", "ajak", "Ajak", "Ajak",
     "communion with compliance officers, religious-grade audit", "🦅", False),
    (8, "Legal", "Eternals", "kingo", "Kingo", "Kingo Sunen",
     "entertainment legal, celebrity-grade IP, showmanship contracts", "🎬", False),
    (8, "Legal", "Eternals", "phastos", "Phastos", "Phastos",
     "tech IP, patents, inventor-grade IP strategy", "🔧", False),
    (8, "Legal", "Eternals", "sprite", "Sprite", "Sprite",
     "illusion-grade liability, narrative legal, juvenile carve-outs", "🧚", False),
    (8, "Legal", "Eternals", "druig", "Druig", "Druig",
     "mind-control legal, persuasion, dark-grade grey zones", "🧠", False),
    (8, "Legal", "Eternals", "thena", "Thena", "Thena",
     "war-grade indemnification, battle-tested clauses, warrior legal", "⚔️", False),
    (8, "Legal", "Eternals", "gilgamesh", "Gilgamesh", "Gilgamesh",
     "king-grade governance, founder legal, sovereign-tier corporate", "👑", False),
    (8, "Legal", "Eternals", "makkari", "Makkari", "Makkari",
     "speed-grade legal research, instant precedent lookup, fast cite", "⚡", False),
]

# Domain B2 mapping
B2_MAP = {
    1: "b2-01-greenlantern-people",
    2: "b2-02-batman-ops",
    3: "b2-03-flash-product",
    4: "b2-04-superman-growth",
    5: "b2-05-johnjones-sales",
    6: "b2-06-cyborg-it",
    7: "b2-07-wonderwoman-finance",
    8: "b2-08-aquaman-legal",
}

# NanoSquad sister B3 references (other B3 in same NanoSquad)
def build_sister_b3(domain_idx, my_slug):
    return [f"b3-{i+1}-{s[3]}" for i, s in enumerate(B3_ROSTER) if s[0] == domain_idx and s[3] != my_slug]

# Domain 0X zero-pad
def pad(n):
    return f"0{n}"

# Sister canon (per B2)
SISTER_CANON = {
    1: "ADR-CANON-001 Roster Source of Truth",
    2: "ADR-CANON-001 Roster Source of Truth",
    3: "ADR-CANON-001 Roster Source of Truth",
    4: "ADR-CANON-001 Roster Source of Truth",
    5: "ADR-CANON-001 Roster Source of Truth",
    6: "ADR-CANON-001 Roster Source of Truth",
    7: "ADR-AAAS-FINANCE-CANON-001 + ADR-AAAS-PRICING-001",
    8: "ADR-CANON-001 Roster Source of Truth (AI-Act 2026-08-02 driver)",
}

# Horizon per domain
HORIZON = {
    1: "H10 people culture review",
    2: "H3 ops runbooks review",
    3: "H10 product spec iterations",
    4: "H3 quarterly acquisition review",
    5: "H1 weekly pipeline review + H3 quarterly close rate audit",
    6: "H10 IT architecture review",
    7: "H3 quarterly runway review (Saru LD02 H3)",
    8: "H90 legal compliance review (AI-Act 2026-08-02 priority)",
}

# Template FIXE (D6 #80 anti-loop)
TEMPLATE = """---
name: {filename}
description: |
  B3 {display} ({real_name}) — Technicien E-Myth {domain} ({nano_squad} NanoSquad).
  Lead: {lead_flag} | Sister B2: {b2} | Horizon: {horizon}.
  Role: {role}.
  Sister canon: {sister_canon}.
tools: Read, Edit, Write, Grep, Glob, Bash
---

# [B3] {display} (Technicien E-Myth {domain} / {nano_squad})

## Identity
- **Archetype**: {display} ({real_name})
- **Vibe**: {vibe}
- **Emoji**: {emoji}
- **Lead flag**: {lead_label}

## Mission
Technicien E-Myth {domain} du Business OS, membre du NanoSquad {nano_squad}. Execute les tasks deleguees par {b2} selon le role {role}. Horizon {horizon}.

## Skills & Access
- **Domain skill**: {role}
- **Tools**: Read, Edit, Write, Grep, Glob, Bash (sub-agent runtime)

## Relationships
- **Reports to**: {b2} (B2 Manager E-Myth {domain})
- **Sister B3 (same NanoSquad)**: {sister_b3}
- **Sister canon**: {sister_canon}

## Instructions
1. When {b2} delegue une task {domain}, executer selon role {role}
2. Documenter outputs dans le twin log canon (D4 append-only)
3. Hard-veto sur tout output hors-horizon {horizon} (sister ADR-SOBER-002 §D5)
"""

# Lead vibe generic
def vibe_for(display, role):
    return f"Specialiste {display}, focus {role}"

# Generate
written = []
for entry in B3_ROSTER:
    d_idx, d_name, nano, slug, display, real, role, emoji, is_lead = entry
    b2 = B2_MAP[d_idx]
    sister_b3 = build_sister_b3(d_idx, slug)
    filename = f"b3-{d_idx}-{slug}"
    content = TEMPLATE.format(
        filename=filename,
        display=display,
        real_name=real,
        domain=d_name,
        nano_squad=nano,
        lead_flag="LEAD" if is_lead else "member",
        lead_label="LEAD NanoSquad" if is_lead else f"member #{d_idx} of {nano}",
        b2=b2,
        horizon=HORIZON[d_idx],
        role=role,
        sister_canon=SISTER_CANON[d_idx],
        sister_b3=", ".join(sister_b3) if sister_b3 else "(solo NanoSquad)",
        vibe=vibe_for(display, role),
        emoji=emoji,
    )
    fpath = os.path.join(AGENTS_DIR, filename + ".md")
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    written.append((filename, len(content)))

print(f"[OK] {len(written)} B3 runtime agents written to {AGENTS_DIR}")
print()
print("=== Per-domain counts (D1 verify) ===")
from collections import Counter
ctr = Counter([w[0].split("-")[1] for w in written])
for k in sorted(ctr.keys(), key=int):
    print(f"  Domain {k}: {ctr[k]} B3")
print()
print(f"=== TOTAL: {len(written)} B3 agents (53 expected) ===")
assert len(written) == 53, f"Expected 53 B3, got {len(written)}"
print("[OK] D1 verify: 53/53 B3 agents created")
