---
type: cadence-contract
loop: wf1-morty
status: CANON (dictée A+ 2026-07-06 — « c'était le manque de structuration claire de 12WY qui était ma dette d'exécution »)
sisters: ADR-WARMODE-004 (conduction) · ADR-L1-WF-001 · wargame 12 (thrashing cure) · wargame 13 (idempotence)
---
# CADENCE 12WY — la structure claire qui éteint la dette d'exécution

## La chaîne de responsabilité (qui tient quoi, à quelle échelle)

| Échelle | Responsable | Rôle exact |
|---|---|---|
| Cycle ~90 j (12WY) | **A2 Curie** (SNW) | Tient le cycle entier ; analyse de fin de cycle |
| Rock mensuel (4 sprints) | **A3 Pike** | Vision mensuelle, AJUSTÉE après l'exécution des 4 sprints d'Una |
| Sprint = 1 semaine de scope | **A3 Una** | Plan 7 jours ; **compression : 1 semaine de scope = 1-2 h de réalisation machine** (5-15 h de scope humain/jour) — c'est la compression que MiroFish simule (×4/×8) |
| Daily scrum / process control | **A3 M'Benga** | Contrôle de process quotidien, surcharge, drift |
| Measurement | **A3 Chapel** | Lead/lag scorecard, D11, benchmark d'exécution |
| Bilan Time Use | **W2 de fin de cycle** | Traçabilité complète → déclenche l'étage DEAL |

## La boucle d'un cycle (séquence déterministe, conduction WARMODE-004)

1. **Spock (WF0)** reçoit le GO Unique A0 → trigger Symphony Plane → **A2 Holo Deck (GTD Cerritos)** garde WF1 observable.
2. **WF1 Morty** (boucle vivante 24/7, `/loop` → `/multi-goal` → `/swarm-orchestrator`) orchestre les **5 A3 de Curie** (Pike/Una/M'Benga/Ortegas/Chapel).
3. **Sprints enchaînés avec annonce Telegram** : fin du sprint 1 (semaine 1 de scope) → push Telegram « W1 finalisée » → sprint 2 immédiat → push « démarrage sprint 3 » → etc. La transmission est le battement de cœur visible d'A+.
4. **WK1 du cycle courant** : structuration B1/B2/B3 People — création, configuration des rôles, prompts, tools de l'organigramme (le PRD-PORTFOLIO tier 1 en dépend).
5. **W2 de fin de cycle** : bilan **Time Use** (Chapel benchmark) → trigger **A2 Holo Janeway** qui orchestre ses A3 DEAL (Dal/Rok-Tahk/Zero/Gwyn) avec l'analyse d'**A2 Curie** → **Data** pousse aux **Archives**.
6. **DEAL passe en wargame puis MiroFish** → verdict → **STOP propre du WF2** (Picard/PARA) après Curie et Computer → Holo Janeway simplifie le projet exécuté.
7. **Picard** garde la responsabilité **H10 (10 ans)** ; **Book** tient le coaching **H1 (année en cours)**. L'expansion B1-B3 reste encadrée par les 5 A3 de Curie.

## Invariants (ce qui ne bouge jamais)
- Une semaine de scope N ne démarre pas tant que la N-1 n'a pas son push Telegram de finalisation (pas de chevauchement silencieux — anti-thrashing, wargame 12).
- La compression est bornée par le verdict MiroFish courant (aujourd'hui : **CAP ×4** tant que capacité < 96/WK — signal absorbé 2026-07-06).
- Tout artefact de sprint = fichier + ligne worklog (D1) ; tout retrait → _TRASH (D4).
- Boot-durabilité : la cadence survit au reboot (LogonTriggers PT5M-PT10M, `add_boot_triggers.ps1`).

## ⚡ÉVOLUTION 2026-07-06 — La table de compression (les maths du GO triennal)

| L1 plan | L2 exécution | Gardien |
|---|---|---|
| 1 semaine (sprint) | 1 jour | Una plan · M'Benga 5-7 daily · Ortegas exécution |
| 1 mois (Rock) | 1 semaine | Pike (vision ajustée post-sprints) |
| 1 cycle 12WY | 1 mois | Curie · Chapel Time Use en W2 |
| 1 an (4 cycles) | 1 trimestre | Spock H-horizons |
| 12 cycles (~3-4 ans civils) | ~1 an | GO triennal → graduation Book H1→H3, Picard H10→H30 |

Borne dure : compression soutenue ≤ ×4 tant que capacité < 96/WK (verdict MiroFish absorbé). Le GO de 3 ans = un H10 expérientiel complet — renouvelable par rite, suspendable par capacité, jamais tué par panique.
