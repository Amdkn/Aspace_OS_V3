---
source: LLM_Wiki_A0
date: 2026-05-17
type: summary
domain: A0_Sovereign / Autonomous_Research / Agentic_Loops
tags: [#Karpathy #AutoResearch #LLM #Autonomous_Agent #Training_Loop #Agentic_Pattern]
---

# Karpathy AutoResearch

**Source:** Andrej Karpathy — https://github.com/karpathy/autoresearch
**Repo stats:** 81.4k ⭐, 11.8k forks, Python 83% / Jupyter 17%, License MIT.
**Type:** Open-source codebase + research methodology.
**Slug:** `karpathy-autoresearch`
**Companion source:** [[source_llm-wiki-pattern]] (sibling pattern by same author — compounding memory).

---

## Core Thesis

> *"Give an AI agent a small but real LLM training setup and let it experiment autonomously overnight. It modifies the code, trains for 5 minutes, checks if the result improved, keeps or discards, and repeats."*

Auto-research transforms an LLM agent from a one-shot answerer into a **researcher with a clock**. The agent iterates on hypotheses with measurable improvement signals. Karpathy's insight: research doesn't need a human in every loop — it needs a *measurable proxy of progress* and *bounded experiment cost*.

---

## The Three-File Architecture

| File | Mutability | Owner | Role |
|---|---|---|---|
| `prepare.py` | **Immutable** | Human | Constants, data preparation, tokenizer. The "physics" of the experiment. |
| `train.py` | **Agent-modified** | LLM agent | Model architecture, optimizer, training loop. The "hypothesis space." |
| `program.md` | **Human-modified** | Human | Agent instructions, research direction, goals. The "research grant." |

**The separation is sacred** : agent never touches `prepare.py` (preserves comparability), human never touches `train.py` (preserves agentic autonomy), agent never modifies its own `program.md` (preserves direction).

---

## Hyperparameters (knobs the agent tunes)

| Parameter | Default | Purpose |
|---|---|---|
| `DEPTH` | 8 | Model complexity primary knob |
| `WINDOW_PATTERN` | `SSSL` / `L` | Attention banding pattern |
| `TOTAL_BATCH_SIZE` | (power of 2) | Total training batch |
| `DEVICE_BATCH_SIZE` | — | Per-device batch |
| `MAX_SEQ_LEN` | — | Max sequence length |
| `EVAL_TOKENS` | — | Validation data volume |
| `vocab_size` | 8192 | Tokenizer vocabulary |

**Time-budget fixed: 5 minutes per training run**, regardless of hardware. This is the genius — it normalizes experiments and lets the agent throw many hypotheses at a wall in finite time.

---

## 7 Tips for Smaller Compute (verbatim from README)

1. Use lower-entropy datasets (TinyStories).
2. Decrease `vocab_size` proportionally.
3. Lower `MAX_SEQ_LEN` significantly.
4. Reduce `EVAL_TOKENS` volume.
5. Lower `DEPTH` (e.g. 8 → 4).
6. Use `L` `WINDOW_PATTERN` instead of `SSSL` (banded attention is GPU-inefficient on small setups).
7. Decrease `TOTAL_BATCH_SIZE` keeping it powers of 2 (e.g. 2^14 ≈ 16K or less).

---

## Notable Forks (multi-platform autonomous research)

| Fork | Platform | Notes |
|---|---|---|
| miolini/autoresearch-macos | macOS | Apple Silicon baseline |
| trevin-creator/autoresearch-mlx | macOS (MLX) | Apple ML framework, optimized for unified memory |
| jsegov/autoresearch-win-rtx | Windows | NVIDIA RTX CUDA |
| andyluo7/autoresearch | AMD | ROCm path |

→ The fork ecosystem is itself an emergent auto-research signal : the *community* iterates on the *platform abstraction layer* while individuals iterate on the *training loop*.

---

## Mapping to A'Space OS V2

| AutoResearch | A'Space Equivalent | Why |
|---|---|---|
| `prepare.py` (immutable) | `01_Identity_Core/AGENTS.md` + `_SPECS/ADR/*` | The Canon — never rewritten, only extended. |
| `train.py` (agent-modified) | Shadow L0 Executor Mesh (Codex/Gemini/Claude) | Where executors apply patches, refactor, ship code. |
| `program.md` (human-modified) | A0 Intention emission (3-Turn Air Lock) | A0 dictates direction; never touches configs. |
| 5-min time-budget | 12WY weekly cadence + ratio 50/30/20 | Bounded experiment cost in human-scale time. |
| Hyperparameter sweep | SPAD framework + ADR variations | Parametric exploration of architecture choices. |

→ **A'Space is auto-research at the OS layer** : the Canon is `prepare.py`, the Shadow L0 mesh is `train.py`, A0 Amadeus + Symphony emit the `program.md`.

---

## The "Stop Re-Deriving, Start Compiling" Doctrine (cross-pattern)

Karpathy's two artifacts ([[source_karpathy-autoresearch|AutoResearch]] + [[source_llm-wiki-pattern|LLM Wiki]]) form a **single compounding agentic doctrine** :

| Pattern | What compounds | Where it sits |
|---|---|---|
| **LLM Wiki** | Knowledge / memory | Across queries (vertical: time) |
| **AutoResearch** | Hypotheses / improvements | Across experiments (vertical: iteration) |

Together = a fully autonomous research operating system. Memory + Evolution.

---

## Risks & Critiques

1. **Reward hacking** : 5-min eval-loss is a proxy that can be gamed (e.g. memorize tiny val set). Real research requires multi-metric reward design.
2. **Local optima trap** : greedy keep/discard converges to nearest hill, not global frontier. Karpathy mitigates via human-tuned `program.md` injecting exploration pressure.
3. **Single-loss tyranny** : eval-loss alone doesn't capture interpretability, robustness, OOD generalization.
4. **Hardware bias** : a hypothesis that wins on 5-min RTX-3090 might lose on H100 with 1-day budget.

A'Space corollary : the Shadow L0 executor mesh inherits these risks. Multi-executor diversity (Codex / Gemini / Claude) is the mitigation — different "reward shapers" exploring different valleys.

---

## Operational Use

A0 can spawn an A'Space auto-research run by:

1. Fixing the Canon in `_SPECS/ADR/` (prepare).
2. Writing a `program.md` for the mission (e.g. "Improve LLM Wiki query latency by 30%").
3. Letting Shadow L0 mesh iterate on patches (train).
4. Measuring against a frozen eval (e.g. wiki lint score, page-creation throughput).
5. Logging durable wins in `LLM_Wiki/wiki/log.md`.

---

## Inbounds

- [[source_llm-wiki-pattern]] — Karpathy's other canonical pattern.
- [[entity_autoresearch]] — Entity page for this codebase.
- [[concept_autonomous_research_loop]] — Pattern abstraction across domains.

## References

- README excerpt processed via Context7-equivalent WebFetch 2026-05-17.
- Gist (LLM Wiki sibling) : https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
