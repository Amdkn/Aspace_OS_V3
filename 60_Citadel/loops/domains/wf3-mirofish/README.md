---
type: loop-contract
loop: wf3-mirofish
flag: enable_wf3.flag
trigger: schtask sim-runner (P3) | signal `sim-request`
rails: SUCCESS-ASPACE 12 pts (fable-last-week-aspace/) — les sims sont des wargames
---
# Contrat WF3 — MiroFish Predictive Swarm (SIMULATION, jamais le réel)

**Goal** : N simulations parallèles de cycles 12WY + variations de coaching Book, en worktrees ISOLÉS, pour que M3/Hermes/MC wargament comme Fable. Les résultats nourrissent WF2 en signals — la simulation ne touche JAMAIS le réel.
**Workflow** : `cron/wf3_sim_runner.py` (P4) : créer N worktrees (départ N=2) → chaque sim court une variation (cadence compressée, coaching variant, hypothèse marché) au format WARGAME ORDER → sortie `artifacts/signals/sim-<slug>.md` (prédiction + conditions + confiance) → worktrees nettoyés → worklog.
**Boundaries** : une sim n'écrit QUE dans son worktree + son signal de sortie · zéro écriture canon/LD01/10_Projects · une prédiction sans conditions d'invalidation = rejetée (pas de prophétie, des forks à triggers) · signaux taggés `sim` — WF2 les consomme comme hypothèses, jamais comme faits (D1).
**Backlog** : [ ] premier run N=2 (variation cadence ×4 vs ×8 sur cycle compressé).
**Timeline** : - [2026-07-06] contrat posé.
