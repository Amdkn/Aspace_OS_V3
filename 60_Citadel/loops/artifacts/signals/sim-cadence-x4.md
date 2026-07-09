---
type: signal
status: open
tag: sim
sources: [cron/wf3_sim_runner.py]
seen: 1
---
# sim-cadence-x4 — prédiction MiroFish (SIMULATION, pas un fait)

Hypothèse : cycle 12WY compressé ×4 (arrivées 12/WK, capacité 60/WK, WIP 20).
Prédiction : DEAL WK13 atteignable — verdict SOUTENABLE.

**Conditions d'invalidation (forks à triggers, pas prophétie)** :
- SI les arrivées réelles > 12/WK observées 2 WK → re-simuler, prédiction caduque.
- SI un tick réel dure > 2× le budget → la compression ×4 est fausse en pratique.
- SI saturations réelles/WK > simulées → adopter la variation inférieure.

## Timeline
- [2026-07-06T04:08:04-04:00] [wf3-mirofish] run déterministe : done=624.0 · queue_fin=0.0 · saturations=0 · conservation=0 · verdict=SOUTENABLE
- [2026-07-06T12:49:20-04:00] [wf3-mirofish] run déterministe : done=624.0 · queue_fin=0.0 · saturations=0 · conservation=0 · verdict=SOUTENABLE
- [2026-07-07T00:49:19-04:00] [wf3-mirofish] run déterministe : done=624.0 · queue_fin=0.0 · saturations=0 · conservation=0 · verdict=SOUTENABLE
- [2026-07-07T12:49:18-04:00] [wf3-mirofish] run déterministe : done=624.0 · queue_fin=0.0 · saturations=0 · conservation=0 · verdict=SOUTENABLE
- [2026-07-07T22:20:06-04:00] [wf3-mirofish] run déterministe : done=624.0 · queue_fin=0.0 · saturations=0 · conservation=0 · verdict=SOUTENABLE
- [2026-07-08T00:49:21-04:00] [wf3-mirofish] run déterministe : done=624.0 · queue_fin=0.0 · saturations=0 · conservation=0 · verdict=SOUTENABLE
- [2026-07-08T08:43:47-04:00] [wf3-mirofish] run déterministe : done=624.0 · queue_fin=0.0 · saturations=0 · conservation=0 · verdict=SOUTENABLE
- [2026-07-08T12:49:21-04:00] [wf3-mirofish] run déterministe : done=624.0 · queue_fin=0.0 · saturations=0 · conservation=0 · verdict=SOUTENABLE
- [2026-07-08T14:43:24-04:00] [wf3-mirofish] run déterministe : done=624.0 · queue_fin=0.0 · saturations=0 · conservation=0 · verdict=SOUTENABLE
