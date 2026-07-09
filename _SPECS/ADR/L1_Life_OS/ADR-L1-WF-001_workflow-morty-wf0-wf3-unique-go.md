---
type: adr
id: ADR-L1-WF-001
title: Workflow de Morty — topologie WF0→WF3, Loop Engineering réel, Unique GO A+→Spock, portes gagnées
status: RATIFIED (plan approuvé A+ en Plan Mode 2026-07-06 ; implémentation P0-P5 livrée+vérifiée même nuit)
date: 2026-07-06
amends:
  - "ADR-LD01-004 §4.3 Phase 3 : clause « gated Rick S1 OBLIGATOIRE » → « Unique GO A+→Spock + invariants Beth (airlock) + cycles verts » (Rick n'est plus un veto depuis ADR-WARMODE-002 ; append-only, LD01-004 non réécrit)"
ratifies:
  - "ADR-LOOP-002 (était PROPOSED) tel qu'amendé §D4 ci-dessous"
sisters:
  - ~/.claude/plans/noble-swimming-spindle.md (le plan approuvé)
  - fable-last-week-aspace/wargames/01..04 (les rails blind)
  - ADR-WARMODE-002 (Beth seul veto) · ADR-LD01-004 (True Agent Autonomy) · ADR-NEXUS-NICHE-001
---

# ADR-L1-WF-001 — WF0→WF3 + Unique GO + Loop Engineering

## D1 — Topologie (typage strict : WF = strates · WK01-13 = semaines 12WY)

| Strate | Owner | Rôle | Rails (wargame) |
|---|---|---|---|
| **WF0** | Spock (A0 Amodei coache : A3 Spock → A2 Holo Deck/Cerritos → A1 Morty) | Airlock GTD×PARA : gouverne le pipeline Cerritos ×5, tient les invariants Beth, émet le **Pass** WF1 par WK | wargames/01 |
| **WF1** | Morty (A2 Curie WK01-12 · A2 Computer PARA · A2 Holo Janeway DEAL WK13) | Poupée russe 12WY⊃PARA⊃DEAL, N instances parallèles, soupapes chiffrées, preuve-ou-queue | wargames/02 |
| **WF2** | Book (A3 Picard/MiroFish → B1 Jerry+Summers/Gstack) | CEO-Bench RÉEL des W* clients L2 (les clients ne touchent jamais L1) | wargames/03 |
| **WF3** | MiroFish Predictive Swarm | SIMULATION : N cycles 12WY simulés + variations coaching, sandbox isolé, sortie = signals tag `sim` (hypothèses, jamais faits) | contrat wf3 |

## D2 — Le Unique GO (HITL poussé au maximum à droite)

**UN clic humain reste** : A+ pose `citadel/decisions/GO_SPOCK_UNIQUE.md` (template : `loops/GO_SPOCK_UNIQUE.template.md`). L'airlock vérifie GREEN ×2 (hystérésis) puis cascade `enable_wf0/wf1/wf3/ship_internal.flag`. **Révocation = supprimer le fichier** (kill-switch ClaudeClaw : défaut ON, urgence OFF). Aucun autre GO par item, par frontière, par session.

## D3 — Portes gagnées (HxH, choix A+ 2026-07-06)

- Test + Ship **interne** : au GO, immédiat.
- Ship **outboard** (prod client, outbound) : **gagné** par 3 cycles verts consécutifs (0 rollback + 0 fuite DLP) → flag auto-posé + Telegram. 1 rollback/fuite → retiré + compteur à 0. La porte se re-gagne, elle ne se re-négocie pas.
- **Beth = seul veto**, chiffré par `collectors/spock_airlock.py` (B1 sommeil · B2 ratio outillage/client · B3 cycles verts · B4 escalade). RED → le scope concerné se gèle mécaniquement ; les loops CONTINUENT, seule l'interpellation d'A+ gèle (B1). UNKNOWN s'affiche, ne bloque pas — jamais de faux GREEN.

## D4 — ADR-LOOP-002 ratifié tel qu'amendé

« Queues over loops » et « sandbox obligatoire » CONFIRMÉS (la queue = `loops/artifacts/tasks/` + Donna DLQ `_dlq/` ; le sandbox = worktrees/simspace, PORTE du parallélisme). « HITL rightward, jamais HITL-zéro » AMENDÉ : le Unique GO **est** le point le plus à droite — il reste un humain (le GO + la révocation + l'échantillonnage Spock review-the-producer), il n'y a plus d'humain PAR ITEM.

## D5 — Loop Engineering (réponse canon à « c'est quoi ce délire »)

Prompt engineering = 1 appel · context engineering = 1 session · **loop engineering = l'environnement AUTOUR des sessions** (quoi travailler, quand réveiller, comment passer l'état). Matérialisé : `citadel/loops/` (ARCHITECTURE + artifacts signals/tasks/tickets/docs + logs/worklog + 5 contrats domains). **Le composé** = toutes les loops lisent/écrivent `signals/`.

## D6 — Triggers 3 étages (D5-vérifiés cette nuit)

1. **OS 24/7** : 4 schtasks `Aspace*` installées state=Ready (`install-loops.ps1`) — Book 4h · Zora 24h · Heartbeat 4h · WF3Sim 12h. Installer ≠ activer : chaque script self-gated par son flag (exit 2 sinon — prouvé).
2. **Session CC** : CronCreate heartbeat e7339ac5 (pouls quand CC ouvert).
3. **Événementiel** : hooks (test-after-edit LIVE) + signals inter-loops.

## D1-receipts (preuves du 2026-07-06 ~00:47)

- `spock_airlock.py` exit 0 → `15_airlock.json` : **B1 RED réel** (nuits A+ détectées — l'instrument dit vrai dès le 1er souffle), B2 0.28 GREEN, cascade OFF (GO absent) ✓
- `heartbeat_os.py` exit 0 : airlock rc=0 → collector rc=0 → **Telegram OK: sent** ✓
- `wf3_sim_runner.py` : gate exit 2 sans flag ✓ ; simulate() discrimine : **×4 SOUTENABLE · ×8 RISQUE** (90 saturations, queue 472, DEAL WK13 compromis) — 1re prédiction MiroFish à contenu réel
- `book_loop.py` exit 0 : J2, T2, 7/7 invariants, 27 agents ✓
- 4 wargames 12/12 (LEDGER), chacun avec patch red-team
- D6 shipped : Join-Path 3-args = PS7-only (2×) · em-dash/UTF-8-sans-BOM casse PS5.1 (2e occurrence, garde-fou confirmé) · subagents CC→MiniMax-M3 inaccessibles depuis session Fable (fallback : exploration directe)

## Réversibilité

Tout : `install-loops.ps1 -Uninstall` · supprimer le GO · flags jetables · loops/ append-only. ADR-LD01-004 non réécrit (amendé par référence). Rien de détruit.
