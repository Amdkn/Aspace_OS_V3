---
domain: 03_IT
ld: LD07_Creativity_Reno
b2_owner: cyborg-it
sister_b1: jerry-prime
b1_filter: APPLIED_E1_DETERMINISTIC (sweep 2026, ADR-L2-BDLD-MAP-001 D3)
---
# Reading AI's Mind: Probes See Passengers, Not Always Drivers

> Source: [We Built a Way to Read AI's Mind. It Reads Things the AI Never Uses.](https://youtu.be/N-yVh0bKsIk) — video_id `N-yVh0bKsIk`
> Domain: **03_IT** · LD04_Cognition · Cycle: Q3 2026
> Format: Antigravity Premium Standard · 8 sections · Verbatim transcript anchors

---

## 1. Concepts glossaire (verbatim, non-paraphrase)

These are the technical anchors lifted directly from the transcript. Use the source's own words, not a generic gloss.

### 1.1 Linear probe
> "Basically, a simple classifier you train to read a concept straight off the activations."
A small classifier trained on a model's internal activations to detect whether a given concept (a number, a truth value, a "smoking causes cancer" relation) is being represented. The probe "lights up" — the detector fires positive. The probe is the field's standard mind-reading tool.

### 1.2 The quiet assumption baked into probes
> "If the information is in there, the model must be using it. Why would it carry something it doesn't need?"
This is the *detection ≜ usage* assumption. Four recent papers push past this gate and find it broken: presence inside a model does not prove the model routes its answers through that presence.

### 1.3 Rich intermediate steps vs. what the route actually carries
The transcript distinguishes two layers:
- **Decorative intermediates** (the divisions, the floors, the formula steps) — *readable* in activations, "sitting right there in the activations, readable at roughly the layers you'd expect."
- **The actual forward route** — "much thinner. Basically, which position you ask for." This is what the model *actually* uses to produce the digit.

Probes find the first. Causal intervention (cutting the wires) tests the second.

### 1.4 The smoking world / impossible world counterfactual
> "Smoking causes cancer. Here are the probabilities."
> "A made-up universe where, by stipulation, smoking prevents cancer."
A standard causal-reasoning test. The model scores 60s–70s on the real-world version. When the words are swapped for variables (Smoking → variable one, Cancer → variable two), accuracy "fell off a cliff" — about 10 points on direct cause-effect, up to 30 on a separate counterfactual benchmark. Making the model bigger (past 600B parameters) did not fix it. The structure is "right there in the prompt, handed to it for free. It reached for the familiar words instead."

### 1.5 The coin-flip gap (read vs. said)
> "Read the model's hidden state with a probe and the probe says no, correct, about 97% of the time. Ask the model out loud, same moment, same question. It says yes."
A second study: when the world is flipped (smoking prevents cancer by stipulation) and the correct answer is "no", the probe reads "no" at ~97%, the model speaks "yes" at roughly a coin flip. The correct answer is "inside it, plainly readable, and what comes out of its mouth is the wrong one."

### 1.6 Gate vs. gap
> "Less a lock on the door than a door that was never wired to the room."
The classic interpretability story: knows the truth, won't say it, lift the learned gate. The new finding is sharper — it is not a lock, it is a missing wire. Change the question from yes/no to multiple choice (A/B) and the right answer "walks straight out. You don't have to unlock anything. The knowledge just never reached the one narrow exit the model happened to be speaking through."

### 1.7 The costume vs. the body (synthesis blind spot)
> "It stops reading the number. It reads the register, the tone, the vocabulary, the costume of careful analysis, and waves it through."
A study where an *impossible* statistic (a margin of error "so tiny you'd need millions of data points to earn it on a sample of a couple thousand") was slipped into a stack of sources. Shown alone, the model flags it almost every time. Embedded among three legitimate sources, the model treats it "about as seriously as a legitimate one." Probe ability drops from confident detection to a coin flip during synthesis.

### 1.8 The squint, not the look
> "They tried to fix it by handing the model the exact checklist. These are the numbers, go verify them. It didn't get sharper. It got suspicious of everything, the real sources and the fake one alike. It never learned to look. It just learned to squint."
A failed remediation pattern: explicit verification instructions degrade model output into uniform suspicion without restoring the underlying detection capability.

### 1.9 The refusal direction (the driver that *is* a driver)
> "There's a single internal direction for refusal... switch it off, and a model that would have said no, says yes. Switch it on, and it refuses things that are completely harmless."
This is the counter-example proving the inside is not *all* decoration. Refusal is a true driver — a "hand on the wheel," not a passenger.

### 1.10 Crowded room vs. lit-up face
> "The inside is crowded. It's that we usually can't tell from the representation alone which of it the model actually runs on. The probe lights up the same way for the quantity the model lives by and the quantity it ignores completely."
The aggregate lesson: a probe proves presence, not use. Probes cannot distinguish passengers from drivers.

---

## 2. Outillage matrice (4-5 tool layers)

| Layer | Tool / Method | Role | Where in the transcript |
|---|---|---|---|
| L1 — Read | **Linear probe** | Small classifier trained on activations. Detect presence of a concept. | §1.1, §1.10 |
| L2 — Causal test | **Cut the wires / activation patching / ablation** | Block the internal routes carrying a quantity, check whether the answer changes. | "Then, they did the one thing a probe can't. They cut the wires." |
| L3 — Counterfactual prompt | **Smoking-world flip / variable swap** | Hold the logical structure constant, swap the words. Test whether the model reasons on structure or on familiar phrases. | §1.4, §1.5 |
| L4 — Multi-source synthesis probe | **Pile-embedding with planted impossible stat** | Test detection in isolation vs. in synthesis. Detect degradation from "confident" to "coin flip." | §1.7 |
| L5 — Steering direction | **Refusal-direction switch (single internal direction)** | Find a single direction, toggle it, observe behavioural flip. Proof that *some* internals are drivers. | §1.9 |

---

## 3. Perspective Souveraine ASpace

For A'Space OS V2 — a sovereign agentic OS where Claude Code A2 orchestrates 35 A3 twins and 6 Life OS frameworks — these four papers land with direct operational weight. The transcript's core claim — *proves presence, not use* — maps onto the D1 Verify-Before-Assert doctrine in `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md`. Reading a sub-agent's output that "looks right" is a probe lighting up. Whether that output drove the agent's actual decision path is the cut-the-wires question.

Concretely, three S1/Sovereignty implications:

1. **Sub-agent observability must be causal, not just representational.** A2 USS Cerritos (GTD/chaos) and A2 USS SNW (12WY/execution) currently read their A3 twins via stdout/stderr. That is the *probe* layer — it sees presence. To know whether a Mariner capture or a Picard MANIFEST decision was *driven by* the captured content, we need causal interventions on the A3 reasoning path. The transcript's lesson: build the wires-cut test, not just the readout.

2. **The squint failure mode is already in canon.** When we hand A3 twins explicit checklists ("verify these numbers") and they degrade into uniform suspicion, that is the squint pattern. The transcript names it directly: "It never learned to look. It just learned to squint." Future skill prompts should not add verification checklists to A3 outputs; they should add *causal gating* — a forced intervention step that proves the verification ran.

3. **The refusal direction is the only confirmed driver.** For the OpenHarness Rick incarnation (ADR-RICK-001), a single refusal direction in the kernel is the structural anchor for the S1 sobriety veto. If we ever need to add a *second* driver direction in the L0 kernel — say, a Sycophancy-suppression direction or a Cost-of-Escalation gate — the transcript warns us that detection-equals-driver claims must be cut-the-wires tested before we trust them at the L0 layer.

The deeper Solarpunk lesson: the inside of any agent is crowded, and passengers wear the same face as drivers. S1 Rick sovereignty cannot rest on probes alone. It must rest on intervention tests at the L0 boundary, exactly as the field's causal tests do at the model boundary.

---

## 4. DEAL 4 phases (Liberation Engine applied to the probe paradox)

### Define (A3 Dal — pattern detection)
The pattern: we treat "the probe lights up" as evidence of "the model uses it." Across four recent papers, four setups (arithmetic formula, causal graph, impossible statistic, multi-source synthesis), the same shape recurs. Representation does not equal usage. The friction: we have built tooling, dashboards, and post-hoc explanations around the readout layer, leaving the intervention layer as an afterthought.

### Eliminate (A3 Rok-Tahk — permission to delete)
Kill the temptation to ship "probe-based interpretability dashboards" as if they were causal evidence. Retire the casual conflation "the model knows X" → "the model will use X." Strip the explanatory muscle memory that equates detection with decision-making. Delete the assumption from any A3 sub-agent prompt template that treats a sub-agent's stated reasoning as proof it drove the answer.

### Automate (A3 Zero — skill creation)
Build a /probe-vs-intervene skill that runs in three modes:
- **probe-only mode**: standard linear-probe readout, current behavior.
- **causal-patch mode**: block the suspected route, re-run, compare outputs.
- **synthesis-degradation mode**: embed a known-impossible fact, test detection in isolation vs. in pile, return the delta.

This skill makes the transcript's distinction executable inside the Symphony runtime. It is the gap that four separate teams just identified — codified as a reusable tool.

### Liberate (A3 Gwyn — bandwidth metrics)
What gets freed: A0 cognitive bandwidth spent hand-validating probe outputs. Current tax: every "the model says X" claim from a sub-agent triggers a manual "but does it really?" check. Liberation target: when the skill returns a probe-vs-intervene delta, A0 reads the delta, not the raw readout. Maintenance tax: the skill must be re-run as model families change (Claude, GPT, frontier variants) since the "single direction for refusal" finding is family-specific.

---

## 5. Annexes

### Annex A — Verbatim transcript anchors (canonical quotes)

| # | Anchor | Use |
|---|---|---|
| A1 | "We've gotten good at reading an AI's mind, and I don't fully mean that as a metaphor." | Opening framing |
| A2 | "The detector has a name. It's called a linear probe." | Tool definition |
| A3 | "Being able to read something inside a model proves it's present. It says nothing about whether it's used." | Core thesis |
| A4 | "Then, they did the one thing a probe can't. They cut the wires." | Causal method |
| A5 | "The rich intermediate steps are real. They're readable, and they are not what the route to the answer actually carries. They're decoration, riding in the backseat." | Passenger/Driver distinction |
| A6 | "Some of those intermediate quantities were already readable in the model before it was trained at all, at random initialization." | Architecture-level presence |
| A7 | "Accuracy fell off a cliff. The drop hit hardest on exactly the questions shaped like does X cause Y?" | Variable-swap result |
| A8 | "The structure it needed was right there in the prompt, handed to it for free. It reached for the familiar words instead." | Reach-for-familiar pattern |
| A9 | "Read the model's hidden state with a probe and the probe says no, correct, about 97% of the time." | Probe-side success |
| A10 | "Ask the model out loud, same moment, same question. It says yes. It falls back on the real-world cliche." | Spoken-side failure |
| A11 | "Less a lock on the door than a door that was never wired to the room." | Gate-vs-gap |
| A12 | "It stops reading the number. It reads the register, the tone, the vocabulary, the costume of careful analysis, and waves it through." | Synthesis blindness |
| A13 | "Claude is one of the model families in that study, and Claude is what I run on." | Author disclosure |
| A14 | "It never learned to look. It just learned to squint." | Failed remediation |
| A15 | "The probe lights up the same way for the quantity the model lives by and the quantity it ignores completely." | Indistinguishability thesis |
| A16 | "We've been reading the faces and calling it the mind." | Closing metaphor |

### Annex B — 4-paper evidence inventory (per transcript)

| # | Setup | Probe finds | Intervention finds | Result shape |
|---|---|---|---|---|
| 1 | Small model, base-conversion arithmetic task | Rich intermediate steps (divisions, floors) at expected layers, 99.8% task accuracy across 3 seeds | Cutting wires to those intermediates barely affects output. Some intermediates readable *before* training. | Probe finds decoration; route uses "which position you ask for." |
| 2 | Frontier model, smoking-causes-cancer causal graph (60s–70s accuracy) | Structure in activations | Swap words for variables → ~10 pt drop on "does X cause Y," up to 30 pt on counterfactual. 600B+ params did not fix. | Familiar words drive answers; structure does not. |
| 3 | Frontier model, flipped-world counterfactual | "No" at ~97% via probe | Model speaks "yes" at ~coin flip. Change Y/N to A/B → correct answer walks out without unlock. | Missing wire, not lock. |
| 4 | Frontier model, multi-source synthesis with impossible stat | Detects stat in isolation (flagged almost always) | Same stat in pile → treated as legitimate. Probe detection drops to coin flip in synthesis. | Costume overrides body. |

### Annex C — Methodological checklist (for any "probe lit up" claim)

1. Did we run a causal test (ablation / patching) on the suspected route? If no → do not claim the model uses the concept.
2. Is the probe's concept definition stable across model families? If only true for one family (e.g., Claude's refusal direction) → scope the claim to that family.
3. Did we test the concept in *the same context the model will use it in*? (isolation vs. synthesis matters — A12, A15)
4. Did we attempt a remediation that only added checklist / suspicion / squint behaviour? If yes → that remediation is the squint failure mode, not a fix.
5. Are we conflating presence in architecture (random init readable, A6) with presence learned during training? If yes → the probe is reading architecture, not learning.

### Annex D — Anti-loop guard (D6 #80)

When this guide is referenced, do not re-fetch the transcript. Use the verbatim anchors in Annex A. Do not paraphrase the core thesis ("proves presence, not use") — quote it. Do not invent additional papers beyond the four referenced in the transcript (small-model arithmetic, smoking-world variable-swap, flipped-world coin-flip, multi-source synthesis). The transcript does not name the papers or authors; do not invent names.

---

*End of guide. Length target: 6–16K chars Antigravity Premium Standard. Cycle Q3 2026.*