# AGENTS.md — _INBOX (DOX child)

This is a **DOX child AGENTS.md** under the A'Space OS V3 root `AGENTS.md`. It contains local instructions for the `_INBOX/` subtree (the test of the tape: every note is either admitted or refused).

## Scope

- `_INBOX/_admis/` — admitted notes (became tape specs).
- `_INBOX/_refuses/` — refused notes (did not pass the 4 tape checks).
- `_INBOX/A1_Beth_Morty/` — A1 (Beth Alignement + Morty Execution) inbox.
- `_INBOX/B1_Jerry_Summers/` — B1 (Jerry CEO) inbox.
- `_INBOX/S1_Rick/` — S1 (Rick) inbox.

## Local rules

1. **The tape is binary.** Per Rick LAW: a spec that requires human clarification is not a spec — it returns to `_INBOX`. The 4 controls are: completeness, testability, no-cycle, owner-declared.
2. **D4 append-only.** Notes in `_admis/` are never edited; new context goes to a new file. Refused notes are kept in `_refuses/` for trace.
3. **Inbox is queue, not store.** Items move out of `_INBOX/` once they become specs (`60_Tape_Specs/`), Kernel Cores, or Personas.

## Cross-references

- Root: [`/AGENTS.md`](../../AGENTS.md)
- Tape Specs: [`/00_Amadeus/60_Tape_Specs/`](../../00_Amadeus/60_Tape_Specs/)
- OpenWiki: `~/.openwiki/wiki/`.
