---
type: loop-contract
loop: wf0-spock
flag: enable_wf0.flag (posé par GO_SPOCK_UNIQUE)
trigger: signal `governance-*` | heartbeat War Room | franchissement airlock
rails: fable-last-week-aspace/wargames/01-wf0-spock.md
---
# Contrat WF0 — Spock (Airlock GTD×PARA)

**Goal** : gouverner le pipeline GTD (Cerritos ×5 : Mariner/Boimler/Tendi/Rutherford/Freeman) + tenir l'airlock Beth + émettre le Pass WF1 par WK.
**Workflow** : lire worklog(10) → lire `data/15_airlock.json` → si GREEN : émettre/renouveler `decisions/pass_wf1_WKnn.json` → traiter signals `governance-*` → drainer les placeholders `(( input requis ))` via Rutherford (revue hebdo) → append worklog.
**Boundaries** : ne CRÉE jamais d'agent ni de cron ; se déclenche par signal, ne poll pas ; escalade A0 UNIQUEMENT sur contradiction d'intention (2 lectures canon divergentes citées). Doctrine : `02_Areas_Spock/WF0_governance.md` (à créer per wargame 01, exécuteur Opus).
**Backlog** : [ ] créer WF0_governance.md (wargame 01 M1-M3) · [ ] premier Pass WK courante.
**Timeline** : - [2026-07-06] contrat posé.
