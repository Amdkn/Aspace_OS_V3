# Artifact Templates

Fill placeholders `<...>` from JTBD-001's real pains/persona and the mode calibration. Keep frontmatter
keys identical to JTBD-001 (project, scope, b2_owner, mode string). Codes: `<MODE>` ∈ {SOLARIS, NEXUS,
ORBITER}; `<MC>` (mode code) ∈ {SOL, NEX, ORB}; `<PFX>` = project prefix (e.g. `MAR`).

---

## JTBD-002 — ICP filter (Gamora)

```markdown
---
id: <PFX>_<MODE>_B3_GROWTH_002_ICP_FILTER
jtbd_id: <PFX>-<MC>-B3-GROWTH-002
source_rock: <PFX>-<MC>-B2-GROWTH-2026-01
layer: B3_SWARM_EXECUTION
scope: Summer Project
project: <project_id>
mode: <full mode string from JTBD-001>
domain: Growth
b2_owner: Superman
guardian_lead: Gamora
supports: [Mantis, Star-Lord]
principles_ref: [P1, P9, P11, P3]
evidence_grade: HYPOTHESIS
context_pack: urn:aspace:rag:<project-slug>-growth   # bridge id Symphony injects into the Guardian agent (see SKILL.md "Runtime consumer")
status: REVIEW_READY
updated: <date>
---

# JTBD-002 — <MODE> ICP Filter — <Project name>

> **Job** : *Produce an ICP filter with explicit rejection criteria so Superman accepts which prospects the loop targets and which it refuses.* **Lead** : Gamora. **Principes** : P1/P9/P11/P3.
> ⚠️ HYPOTHESIS. Anti-pattern P1/P2 respecté. Aucune mutation externe.

## 1. ICP (fit positif) — 80/20 (P11)
<who the loop should target, derived from JTBD-001 persona; Pareto: the 20% worth chasing>

## 2. 3 critères de rejet (P9 — un filtre d'entrée, pas une porte ouverte)
- **R1 — <mode-calibrated rejection>** : <why this disqualifies, ties to a JTBD-001 pain>
- **R2 — <...>** : <...>
- **R3 — <...>** : <...>

## 3. Pourquoi refuser protège la marge (P10/P3)
<good churn / precision: refusing bad-fit prospects now prevents toxic churn + protects ABM economics>

## 4. Handoff & DoD
- **← JTBD-001** · **→ JTBD-003 (Groot)** : l'ICP cadre à qui le painkiller parle.
- [x] ICP fit · [x] 3 critères de rejet explicites · [x] anti-pattern P1/P2 · [ ] **Acceptance Superman**

*B3 artifact (Guardians/Gamora) under Superman. Last sync: <date>*
```

---

## JTBD-003 — Painkiller variants (Groot)

```markdown
---
id: <PFX>_<MODE>_B3_GROWTH_003_PAINKILLER_VARIANTS
jtbd_id: <PFX>-<MC>-B3-GROWTH-003
source_rock: <PFX>-<MC>-B2-GROWTH-2026-01
layer: B3_SWARM_EXECUTION
scope: Summer Project
project: <project_id>
mode: <full mode string>
domain: Growth
b2_owner: Superman
guardian_lead: Groot
supports: [Star-Lord, Drax]
principles_ref: [P8, P16, P18, P14]
evidence_grade: HYPOTHESIS
context_pack: urn:aspace:rag:<project-slug>-growth   # bridge id Symphony injects into the Guardian agent (see SKILL.md "Runtime consumer")
status: REVIEW_READY
# legal_gate: true   ← include ONLY for compliance-bound projects (see special-cases.md)
updated: <date>
---

# JTBD-003 — <MODE> Painkiller Message Variants — <Project name>

> **Job** : *Produce 3 testable painkiller variants tied to P8/P13/P16 so Superman picks the message to test.* **Lead** : Groot. **Principes** : P8/P16/P18/P14.
> ⚠️ HYPOTHESIS. Débloqué par directive A0 (acceptance VOC JTBD-001). Drax kill-gate actif.

## 1. 3 variants (painkiller, pas vitamine — P8)
> Persona dominant : **<Process Com profile(s) from JTBD-001>** (P16).
- **V1 — <name>** : « <message> » (← PAIN-0X)
- **V2 — <name>** : « <message> » (← PAIN-0X)
- **V3 — <name>** : « <message> » (← PAIN-0X)

## 2. Cadre (<mode angle: brand/expertise/reliability>)
<the framing logic for this mode + what proof backs the promise>

## 3. Drax kill-gate (P5/P6/P10)
Killed si : <CTR < baseline, OU pas de résonance Mantis, OU promesse intenable par l'Ops>.

## 4. Handoff
- **← JTBD-001/002** · **→ JTBD-004 (Rocket)** : variant gagnant = message de l'asset/experiment.
- **Désaccord productif** : Drax peut killer V<n> si <promesse non tenable> → risque de churn.

## 5. DoD
- [x] 3 variants P8/P16-tagged · [x] cadre <mode> · [x] kill-gate Drax · [x] handoff · [ ] **Acceptance Superman**

*B3 artifact (Guardians/Groot) under Superman. Last sync: <date>*
```

---

## JTBD-004 — Non-paid experiment + RICE (Rocket)

```markdown
---
id: <PFX>_<MODE>_B3_GROWTH_004_EXPERIMENT_RICE
jtbd_id: <PFX>-<MC>-B3-GROWTH-004
source_rock: <PFX>-<MC>-B2-GROWTH-2026-01
layer: B3_SWARM_EXECUTION
scope: Summer Project
project: <project_id>
mode: <full mode string>
domain: Growth
b2_owner: Superman
guardian_lead: Rocket
supports: [Drax, Star-Lord, Groot]
principles_ref: [P6, P7, P12, P15, P14]
evidence_grade: HYPOTHESIS
context_pack: urn:aspace:rag:<project-slug>-growth   # bridge id Symphony injects into the Guardian agent (see SKILL.md "Runtime consumer")
status: REVIEW_READY
updated: <date>
---

# JTBD-004 — <MODE> Non-Paid Experiment + RICE — <Project name>

> **Job** : *Design 1 instrumented non-paid experiment with RICE + lead/lag so Superman greenlights the first organic loop.* **Lead** : Rocket. **Principes** : P6/P7/P12/P15/P14.
> ⚠️ HYPOTHESIS. Anti-pattern P1/P2 respecté. Aucune mutation externe (<gate any scrape/send on A0 + credential>).

## 1. Expérience (canal <mode> : <channel from mode calibration>)
**Hypothèse** : <organic channel action> génère <mode-fit qualified outcome>.
```yaml
channel: <mode channel + principle tags>
asset: <the non-paid asset> + opt-in (P15)
message: variant gagnant (JTBD-003)
referral_loop: <P12 referral mechanism if applicable>
```

## 2. RICE
```yaml
reach: "<estimate, organic>"
impact: "<which PAIN it attacks>"
confidence: "medium — HYPOTHESIS"
effort: "<low/med>"
score: "à calculer par Superman (P5)"
```

## 3. Lead / Lag + build gate
```yaml
lead_indicator: "<measurable organic action; CPQL mesurable>"
lag_indicator: "<mode-fit outcome — see mode calibration>"
build_gate: "CPQL < 80€ green · Pipeline ≥ 5k€/sem (canon Notion)"
kill_rule: "Drax — si <0 outcome après N pièces>, kill le format (P10)"
```

## 4. Proof plan
Log <opt-ins/metrics count only>, capture analytics, premier <outcome> → `03_SHARED_CONTEXT_AND_PROOF_LOG.md`.

## 5. Handoff & DoD
- **← JTBD-003** · **→ Superman** (RICE + greenlight).
- [x] 1 experiment non-payant · [x] RICE (cadre) · [x] lead/lag + gate · [x] proof plan · [x] anti-pattern P1/P2 · [ ] **Acceptance Superman**

*B3 artifact (Guardians/Rocket) under Superman. Last sync: <date>*
```

---

## Proof-log entry (append to B3 03_SHARED_CONTEXT_AND_PROOF_LOG.md)

If the file is still the bare template (ends at the "Productive Disagreement" paragraph), append a
`\n\n---\n\n## Active State Log\n\n` header first, then this entry:

```markdown
### <date> — JTBD-001/002/003/004 (full Guardians squad) → REVIEW_READY (A0-unblocked)<add ", Legal sign-off pending" if compliance-bound>

```yaml
source_b2_rock: <PFX>-<MC>-B2-GROWTH-2026-01
source_jtbd: [<PFX>-<MC>-B3-GROWTH-001, -002, -003, -004]
current_goal: "Complete the <mode> Growth loop: VOC + ICP filter + 3 painkiller variants + 1 instrumented non-paid experiment"
active_member: [Mantis (001), Gamora (002), Groot (003), Rocket (004)]
peer_reviewed_by: Drax   # kill-gate sections present in 003 + 004
artifact_paths:
  - JTBD-001_<MODE>_VOC_PACKET.md
  - JTBD-002_<MODE>_ICP_FILTER.md
  - JTBD-003_<MODE>_PAINKILLER_VARIANTS.md
  - JTBD-004_<MODE>_EXPERIMENT_RICE.md
proof_paths:
  - "<one-line pointer to the key section of each artifact>"
evidence_grade: HYPOTHESIS
lead_indicator: "<mode lead indicator — TARGET only; evidence: pending>"
lag_indicator: "<mode lag indicator — TARGET only; evidence: pending>"
# Metrics are pointers, not copies (ADR-MESH-L2-001: Airtable = HOW MUCH, one owner per datum).
# While HYPOTHESIS there is no real number. Once an experiment measures one, the owner is the
# Airtable Growth record; reference it here instead of writing the number in prose:
airtable_record: "<rec... / URL once measured — base appmWf5Xm7w9Ae0ky, 🦸 Leads & Audits or 💸 Sales Pipeline>"
context_pack: urn:aspace:rag:<project-slug>-growth   # bridge to Symphony Airtable adapter (Growth slot)
status: review_ready
blocks_unblocks: "A0 directive unblocked the dependency gates; pending Superman acceptance (P5 RICE arbitrage non-délégable)"
next_authority_needed: "Superman (B2) acceptance<; Legal sign-off (mandatory) if compliance-bound>; no external mutation pending A0 gate"
```
```
