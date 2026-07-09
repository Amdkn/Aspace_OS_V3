---
type: loop-contract
loop: wf2-book
flag: enable_book_loop.flag (✓ déjà posé 2026-07-05)
trigger: schtask 4h (P3) — script existant `citadel/cron/book_loop.py` (NE PAS dupliquer)
rails: fable-last-week-aspace/wargames/03-wf2-book-ceo-bench.md
---
# Contrat WF2 — Book (CEO-Bench réel : Picard/MiroFish → Jerry+Summers/Gstack → W* clients)

**Goal** : bench H1 P&L hebdo des W* clients L2. Les clients ne touchent JAMAIS L1.
**Workflow (tick)** : lire dernier `cron/output/book-loop-*.json` → lire `10_Projects/<client>/mirofish-WKnn.md` (lecture seule — ownership Picard) → bench : amorçage (leads contactés, quiz complétés) tant que MRR=0, puis pipeline/MRR-vs-100×1000$/close-rate dès le 1er client → lighting Jerry → verse Summers (cite le PATH de chaque livrable) → append épisode `LD01/99_meta/calendar.md` + worklog.
**Boundaries** : chiffre sans source = `n/a (RECON: <path>)` — jamais inventé · `done` = artefact + verse (double preuve) · drift >20% → signal Jerry · 2 WK rouges → alerte dans le Pass WK+1 · PII/légal → route DLP directe · Book décide en H1 seulement (au-delà = signal).
**Backlog** : [ ] premier tick post-schtask · [ ] bascule métriques au 1er client signé.
**Timeline** : - [2026-07-06] contrat posé (book_loop.py de Mavis = producteur ; ce tick = consommateur business).
