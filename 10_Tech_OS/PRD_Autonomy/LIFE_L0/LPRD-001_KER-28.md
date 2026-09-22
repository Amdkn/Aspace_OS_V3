# LPRD-001: Doctor11/Amy/Rory/River persistent session contracts

**Mandate:** Restore durable Life Core operating sessions and capability contracts: Amy=Spec, Rory=Build, River=Spawn/Knowledge, Doctor11=Review/detach. No companion owns sovereign Kernel state.
**Requirements:**
- Implement the `harness_capability` and `session_binding` tables in `10_Tech_OS/kernel/schema.sql`.
- Enforce capability boundaries: Amy=Spec, Rory=Build, River=Spawn/Knowledge, Doctor11=Review/detach via `loi_life_core_binding_capability`.
- Prohibit Amy, Rory, and River from binding to 'L0' (sovereign Kernel state).
- Create a test `10_Tech_OS/kernel/test_life_core_contracts.py` ensuring the boundaries work correctly.
