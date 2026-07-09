# PRD Proposal: Agentic Local Adapters (ALA) Ingestion Standard

## Problem Statement
The current `CLI-Anything` implementation is tied to `Claude Code`, making it incompatible with the native `Antigravity` and `Gemini CLI` workflows on Windows. Agents lack a standardized way to "ingest" local software capabilities into their reasoning loop without falling back to cloud APIs or fragile RPA.

## Target User
- **Amadeus (A0)**: Commands the infrastructure via high-level intention.
- **Antigravity / Gemini CLI (A3)**: Executes the ingestion and uses the resulting adapters.
- **A'Space Web OS Agents**: Consume the exported ALA capabilities via the Open Claw bridge.

## Vision (E-Myth 10-Year Lens)
We are building the "Ingestion Layer" of a sovereign AI Operating System. This is not just a tool, but a fundamental capability of the OS to evolve and acquire new technical skills by digesting existing open-source ecosystems.

## Success Criteria
| Criterion | Measurable | Done When |
|-----------|------------|-----------|
| **Fork Readiness** | Repository setup | `CLI-Anything` forked and adapted to Gemini CLI logic. |
| **Workflow Integration** | Manual execution | A `.agent/workflow` can trigger the 7-phase ingestion loop. |
| **Gateway Discovery** | API accessibility | An ingested tool (e.g. Excalidraw) is visible as a Skill in Open Claw. |
| **Toolbox Expansion** | Agent usage | An A3 agent uses an ALA command to solve a task during an iteration. |

## Scope
- **IN Scope**:
  - Forking `HKUDS/CLI-Anything` logic.
  - Creating ` Antigravity/Gemini CLI` Skills for ingestion.
  - Standardizing the `schema.json` format for ALA.
  - Implementing the Discovery Bridge in Open Claw.
- **OUT of Scope**:
  - Supporting WSL L0 in this phase (Focus remains on Windows Host).
  - Developing the desktop software itself.
  - Cloud-based MCP integration (Sovereignty first).
