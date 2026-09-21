# [LPRD-001][L0] Doctor11/Amy/Rory/River persistent session contracts

**Goal:** Restore durable Life Core operating sessions and capability contracts: Amy=Spec, Rory=Build, River=Spawn/Knowledge, Doctor11=Review/detach. No companion owns sovereign Kernel state.

**Context:** The current implementation of Life Core (L1) agents (Amy, Rory, River) lacks persistent session contracts that enforce their roles in the universal constructor harness. Amy is meant for Spec (tapes), Rory for Build (claims, attests), River for Spawn (duplicates), and Doctor11 for Review (detaches).

**Requirements:**
1.  **Amy Contract:** Must explicitly claim the `Spec` role. Her capabilities are limited to writing tapes (`.yaml` or `.md`) in `10_Tech_OS/12_Life_Core_11th/tapes/`. She cannot write to `uc.db` directly, except via portier/gate.
2.  **Rory Contract:** Must explicitly claim the `Build` role. He reads from tapes, builds, and outputs artifacts.
3.  **River Contract:** Must explicitly claim the `Spawn` role. She duplicates tapes.
4.  **Doctor11 Contract:** Must explicitly claim the `Review` role. He validates and detaches (completes) work.
5.  **State Isolation:** No companion (Amy, Rory, River) can directly own or alter Kernel sovereign state (e.g., bypass `uc.py` to write `uc.db` directly). All interactions must go through the harness/CLI.
6.  **Tests/Evidence:** Provide a test script `test_life_core_contracts.py` that verifies these contracts (e.g., checking that the roles are defined and that direct state manipulation is forbidden, possibly by inspecting agent definitions or simulating interactions via the CLI).

**Implementation Instructions:**
1.  Verify the role definitions in `10_Tech_OS/12_Life_Core_11th/ROLES.md` and the individual `AGENT.md` files in `compagnons/*/`.
2.  Ensure that `10_Tech_OS/12_Life_Core_11th/tapes/` exists.
3.  Write a Python script, `10_Tech_OS/12_Life_Core_11th/test_life_core_contracts.py`, that programmatically asserts:
    *   The `ROLES.md` file correctly maps Amy -> Spec, Rory -> Build, River -> Spawn, Doctor11 -> Review.
    *   The `AGENT.md` files for Amy, Rory, and River contain explicit contract constraints (e.g., "n'a pas le droit de bâtir ni de détacher" for Amy).
    *   *(Optional but recommended)* Use `uc_workgraph.py` or similar to simulate a workflow to prove they only interact via the harness, or at least statically verify the policy.
4.  If the markdown files do not explicitly forbid state manipulation as per the requirements, update them. The prompt says "Restore durable... contracts", meaning we might need to enforce this in code or documentation. Since they are marked "Fichier engendré", we might need to look at `10_Tech_OS/00_Governance_Rick/replicator/spawn.py` or just edit the generated files if `spawn.py` doesn't exist. Let's check `spawn.py`.
