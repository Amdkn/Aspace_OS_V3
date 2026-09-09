# AGENTS.md — 10_Tech_OS (DOX child)

This is a **DOX child AGENTS.md** under the A'Space OS V3 root `AGENTS.md`. It contains local instructions for the `10_Tech_OS/` subtree (the constructor mechanism, kernel, replication).

## Scope

- `10_Tech_OS/00_Governance_Rick/` — Rick's governance (LAW.md, SOUL.md, WATCHDOG.md).
- `10_Tech_OS/11_Kernel_Core_13th/` — L0 Kernel Core (instanced from replicator/gabarit).
- `10_Tech_OS/12_Life_Core_11th/` — L1 Life Core (operates 20_Life_OS).
- `10_Tech_OS/13_Buzz_Core_12th/` — L2 Buzz Core (operates 30_Business_OS).
- `10_Tech_OS/kernel/` — shared kernel: uc.db, schema.sql, gate.py, review.py, dlq.py, harness.py, bridge_paperclip.py, uc.py.

## Local rules

1. **The kernel is sacred.** `kernel/uc.db` is the production state. Do not edit `schema.sql` without an ADR. Migration is via `uc.py`.
2. **Three Cores, one gabarit.** `11_Kernel_Core_13th/`, `12_Life_Core_11th/`, `13_Buzz_Core_12th/` are instances of the same template. They are NOT separate codebases.
3. **Rick does not govern the 3 OS.** Rick governs the mechanism that produces them (`replicator/`). Rick does not replace individual Core governance.
4. **Watchdog has 3 thresholds.** vivant (A0 écrit < 10 min), bien portant (node < 45, cadences ≤ 2, disk > 5 Go), anti-fragile (cause + guard code + guard seen + lesson). Read `WATCHDOG.md` before touching `kernel/`.

## Cross-references

- Root: [`/AGENTS.md`](../../AGENTS.md)
- Memory: [`/00_Amadeus/30_MEMORY_CORE/`](../../00_Amadeus/30_MEMORY_CORE/) — **archival candidate**.
- OpenWiki: `~/.openwiki/wiki/`.

## D4 append-only — audits de vivance

- **2026-08-30 — Preuve de vivance.** Un port qui écoute, un roster peuplé, une base avec des items ou un gardien WSL ne prouvent pas qu'A'Space agit. Toute affirmation « V3 est vivant » doit montrer un cycle continu et horodaté `ruban complet → claim → prédiction antérieure au started_at → construction réelle → revue indépendante → scoring → descendance`, après démarrage à froid et avec reprise d'un worker tué. Tant que ce certificat n'existe pas, qualifier séparément les primitives disponibles, l'infrastructure joignable et l'agence autonome.

## Journal Append-Only (DOX)
- `2026-09-09` : Implémentation du moteur Engram (`engram_loader.py`), du Gatekeeper A1 Beth (`beth_filter.py`) et de la suite de tests unitaires (`test_engram.py`). Validation binaire py_compile à 0 erreur. (Bill Potts & Nardole).
