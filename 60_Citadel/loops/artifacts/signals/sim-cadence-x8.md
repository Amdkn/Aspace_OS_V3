---
type: signal
status: absorbed
tag: sim
sources: [cron/wf3_sim_runner.py]
seen: 1
---
# sim-cadence-x8 — prédiction MiroFish (SIMULATION, pas un fait)

Hypothèse : cycle 12WY compressé ×8 (arrivées 12/WK, capacité 60/WK, WIP 20).
Prédiction : DEAL WK13 COMPROMIS — verdict RISQUE.

**Conditions d'invalidation (forks à triggers, pas prophétie)** :
- SI les arrivées réelles > 12/WK observées 2 WK → re-simuler, prédiction caduque.
- SI un tick réel dure > 2× le budget → la compression ×8 est fausse en pratique.
- SI saturations réelles/WK > simulées → adopter la variation inférieure.

## Timeline
- [2026-07-06T04:08:04-04:00] [wf3-mirofish] run déterministe : done=775.7 · queue_fin=472.3 · saturations=90 · conservation=1 · verdict=RISQUE
- [2026-07-06T05:05:00-04:00] [wf2-book] ABSORBE -> tasks/cap-compression-x4.md (cap x4 acte, boundary rule appliquee)
- [2026-07-06T12:49:20-04:00] [wf3-mirofish] run déterministe : done=775.7 · queue_fin=472.3 · saturations=90 · conservation=1 · verdict=RISQUE
- [2026-07-07T00:49:19-04:00] [wf3-mirofish] run déterministe : done=775.7 · queue_fin=472.3 · saturations=90 · conservation=1 · verdict=RISQUE
- [2026-07-07T12:49:18-04:00] [wf3-mirofish] run déterministe : done=775.7 · queue_fin=472.3 · saturations=90 · conservation=1 · verdict=RISQUE
- [2026-07-07T22:20:06-04:00] [wf3-mirofish] run déterministe : done=775.7 · queue_fin=472.3 · saturations=90 · conservation=1 · verdict=RISQUE
- [2026-07-08T00:49:21-04:00] [wf3-mirofish] run déterministe : done=775.7 · queue_fin=472.3 · saturations=90 · conservation=1 · verdict=RISQUE
- [2026-07-08T08:43:47-04:00] [wf3-mirofish] run déterministe : done=775.7 · queue_fin=472.3 · saturations=90 · conservation=1 · verdict=RISQUE
- [2026-07-08T12:49:21-04:00] [wf3-mirofish] run déterministe : done=775.7 · queue_fin=472.3 · saturations=90 · conservation=1 · verdict=RISQUE
- [2026-07-08T14:43:24-04:00] [wf3-mirofish] run déterministe : done=775.7 · queue_fin=472.3 · saturations=90 · conservation=1 · verdict=RISQUE
