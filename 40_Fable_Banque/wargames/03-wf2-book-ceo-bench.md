# WARGAME 03 — WF2 Book : CEO-Bench (Picard/MiroFish → Jerry+Summers/Gstack → W*)

> Wargamé par Fable 5, 2026-07-06. Exécuteur : **Hermes Agent** (runtime dev Book, `.hermes/book_dev_runtime.md`). Exécutable blind.
> Zone Book = append-only `30_decisions/` + `calendar.md` ; intouchables : Spec/BIBLIOGRAPHY/README.

## RECON (fait — D1)
- ADR-LD01-008 (coaching loop) ACCEPTED par Hermes 2026-07-05 ; ADR-LD01-011 (PoC OMK Nexus) ; ADR-LD01-010 (Hermes promu Picard-in-PARA).
- `citadel/cron/book_loop.py` EXISTE (Mavis) : gated `enable_book_loop.flag` ✓ posé ; sortie `cron/output/book-loop-*.json` ; anti-Ultron 8 invariants ; **schtask PAS installée** (c'est P3 du plan, pas ce wargame).
- Cible business : 100 × 1000$/mo (ADR-NEXUS-NICHE-001) ; Book = H1 P&L hebdo, PAS H10.

## MOVES

**M1 — Le tick CEO-Bench (cadence WK)**
- Action : définir dans `citadel/loops/domains/wf2-book/README.md` le tick : (1) lire dernier `book-loop-*.json` (état harness) ; (2) lire rapports MiroFish de Picard (wargame 08 : `10_Projects/<client>/mirofish-WKnn.md`) ; (3) bench 3 métriques : pipeline (leads qualifiés), MRR vs cible, close rate ; (4) lighting check Jerry (« lights on » par domaine) ; (5) verse Summers (récit client) ; (6) append épisode `LD01/99_meta/calendar.md`.
- Observation : un tick = un épisode calendar horodaté avec les 3 métriques chiffrées (ou `n/a` explicite — jamais inventées).
- Échec probable : métriques inventées quand la source manque → **cause** : M3-plausible-mais-faux. **Contre-action** : chaque chiffre cite son fichier source ; source absente → `n/a (RECON: <path attendu>)`.

**M2 — L'interface Book↔Picard**
- Action : convention : Picard écrit `30_Business_OS/10_Projects/<client>/mirofish-WKnn.md` ; Book LIT, ne modifie jamais un rapport Picard (ownership).
- Observation : le contrat wf2 nomme le glob exact ; 0 write de Book dans 10_Projects/.
- Fork : SI aucun rapport MiroFish pour la WK → Book bench quand même (métriques P&L directes) + signal `mirofish-missing` → queue Picard. Le bench ne bloque JAMAIS sur un input manquant.

**M3 — Le protocole d'escalade W* client**
- Action : seuils dans le contrat : drift projet > 20% du plan WK → signal à Jerry (dispatch B2 concerné) ; 2 WK consécutives rouges → remontée WF1 (le Pass de la WK+1 porte l'alerte) ; risque légal/PII → route DIRECTE mission 05 DLP, pas d'attente.
- Observation : 3 seuils, 3 routes, 0 judgment call.
- Échec probable : Book décide seul en H10 (hors de son horizon) → **cause** : dérive d'horizon. **Contre-action** : Book est verrouillé H1 (Spec intouchable) — toute décision > 1 semaine d'impact = signal, pas décision.

**M4 — Anti-« Jerry dit fini » (learned-helplessness inversée)**
- Action : règle : un item client passe `done` UNIQUEMENT si l'artefact livrable existe ET le verse Summers le référence (double preuve : fichier + récit).
- Observation : grep du contrat : « done = artefact + verse », présent.
- Échec probable : le verse narre un livrable inexistant (narration optimiste) → **cause** : Summers écrit depuis le plan, pas depuis le fichier. **Contre-action** : le verse cite le path du livrable ; verification run = Test-Path chaque path cité.

## ABORT CONDITIONS
1. `book_loop.py` exit 2 (flag retiré) → Book ne bench pas, signal `gate-closed`, STOP propre.
2. `calendar.md` inaccessible en append → STOP (la mémoire épisodique est le contrat de zone).

## VERIFICATION RUNS
1. `install-book-cron.ps1 -RunOnce` → exit 0 + nouveau `book-loop-*.json` (le bench a une source fraîche).
2. Après 1 tick : nouvel épisode calendar avec ≥1 métrique chiffrée sourcée (lire la dernière ligne).
3. `git -C <10_Projects>` (ou Test-Path) : aucun fichier modifié par Book hors zone LD01/loops (ownership prouvé).

## RED-TEAM PASS
- **Attaque échouée** : « le tick duplique book_loop.py » — non : book_loop = introspection harness (état 22 agents) ; le tick CEO-Bench = interprétation business PAR-DESSUS sa sortie. Producteur/consommateur, pas doublon.
- **Attaque réussie → patch** : « les 3 métriques restent n/a pour toujours (pas de clients au début) et le bench devient un rituel vide » — patch : tant que MRR=0, le bench traque les métriques d'AMORÇAGE (missions wargame 06/07 : leads contactés, quiz complétés) — le contrat définit les 2 jeux de métriques et la bascule au 1er client signé.

## SELF-GRADE : 12/12 — dont canon ✓ (Book H1, ownership zones, roster exact), Beth-compat ✓ (tick automatique, zéro action A+ requise)
