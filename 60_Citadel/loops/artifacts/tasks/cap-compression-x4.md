---
type: task
status: queued
owner: wf2-book
origin: loops/artifacts/signals/sim-cadence-x8.md
wk: WK04
exit_condition: capacite mesuree >= 96 items/WK sur 2 WK consecutives (alors re-simuler x8) OU fin de cycle
---
# Cap compression x4 (verdict gouverneur WF3)

Le gouverneur MiroFish (run deterministe 2026-07-06) : x8 = RISQUE (90 saturations, queue residuelle 472,
DEAL WK13 compromis) vs x4 = SOUTENABLE. Decision Book (H1) : Dark Factory cadence CAP x4 tant que la
capacite ne scale pas. Preuve d'application : book_loop next_boundary.rule = "GOUVERNEUR RISQUE non-absorbe
-> cadence CAP x4" (dry-run 2026-07-06). Cette task ABSORBE le signal.
