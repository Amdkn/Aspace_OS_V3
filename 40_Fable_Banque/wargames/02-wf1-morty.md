# WARGAME 02 — WF1 Morty : Poupée russe 12WY ⊃ PARA ⊃ DEAL

> ⚡ÉVOLUTION 2026-07-08 : CAP ×4 établi wargame 08 (`{x4: SOUTENABLE, x8: RISQUE}`) — les soupapes 8× de M3 = **plafond théorique jamais soutenu**. Voir [TEMPORAL-CANON](../TEMPORAL-CANON.md) §compression. (wargame 27 M2b)

> Wargamé par Fable 5, 2026-07-06. Exécuteur : **Opus 4.8 (CC)**. Exécutable blind.

## RECON (fait — D1)
- Russian doll canon : `mindsets/Morty_Dispatch_Doctrine.md` (Curie/SNW 5 · Computer/PARA 4 · Cerritos/GTD 5 — concurrency 14 ≤ 16, one pass OK).
- Cycle 12WY Q3 2026 : départ 2026-06-15 → **WK actuelle à calculer au run** : `floor((today - 2026-06-15)/7)+1`. (Au 2026-07-06 : WK4.)
- `multi-loop-karpathy` skill existe (remplace /loop 7j pour cycles 12WY) — réutiliser, ne pas réinventer.
- ADR-LD01-005 : coût Phase 3 ≈ 0 dans le quota MiniMax (5.1Md/50$).

## MOVES

**M1 — Le « Pass » (jeton d'autorisation WF0→WF1)**
- Action : définir le format dans `citadel/loops/domains/wf1-morty/README.md` §Pass : JSON `{issued_by:"WF0-Spock", invariants_beth:"GREEN", wk_current:N, scopes:["curie","computer","janeway"], expires:"WK+1"}` écrit en `citadel/decisions/pass_wf1_WKnn.json` (append-only, un par WK).
- Observation : un Pass = un fichier horodaté ; les 3 A2 ne s'activent QUE si le Pass de la WK courante existe et invariants=GREEN.
- Échec probable : Pass périmé utilisé (WK a tourné) → **cause** : pas de champ expiry vérifié. **Contre-action** : chaque A2 recalcule WK au démarrage ; Pass.wk ≠ WK courante → refus + signal `pass-expired`.

**M2 — Mapping WK du cycle en cours**
- Action : table WK01-13 dans le contrat wf1 : WK01-12 = Curie (rocks), WK13 = Janeway DEAL (Define/Eliminate/Automate/Liberate) ; Computer/PARA = transversal continu.
- Observation : la table donne pour la date du run la WK et le mode actif, calculable sans question.
- Échec probable : confusion WF/WK (LE bug historique) → **cause** : notation ambiguë. **Contre-action** : préfixes stricts partout ; lint grep `\bW[0-9]` nu = interdit (toujours WF ou WK).

**M3 — Soupapes de la compression 8×**
- Action : documenter 3 soupapes : (a) saturation démon local → mode conservation : fréquence /2, jamais kill mid-write ; (b) KV-cache/contexte > 80% → compaction forcée + observation persistée AVANT ; (c) backlog queue > 20 items non-piochés → stop intake, drain d'abord (WIP limit).
- Observation : chaque soupape a un seuil chiffré + une action mécanique.
- Fork : SI 2 soupapes déclenchent ensemble → priorité (b) > (a) > (c) (perdre du contexte est irréversible, ralentir ne l'est pas).

**M4 — Anti-« travail non vérifié » (la contre-mesure M3-laziness)**
- Action : règle du contrat wf1 : tout tick qui ÉCRIT doit finir par un verification run réel (test, Test-Path, curl) loggé dans worklog — sinon l'item RETOURNE en queue avec tag `unverified`.
- Observation : worklog : chaque entrée write porte sa preuve ; zéro entrée `done` sans preuve.
- Échec probable : l'agent self-certifie (« tests pass » sans les courir) → **cause** : evaluation gaming (risque nommé LD01-004). **Contre-action** : la preuve = SORTIE de commande collée (exit code + 1 ligne), pas une phrase. Échantillonnage Spock hebdo (review-the-producer, LOOP-002).

**M5 — Transition WK12→WK13 (Janeway DEAL)**
- Action : checklist gel : (1) Curie fige les rocks (score final), (2) Computer archive → Data (documentation-before-archive), (3) Janeway D-E-A-L : ce qui se répète 2×+ → candidat skill (Zero), ce qui n'a servi à rien → Eliminate (Rok-Tahk), D11 mesuré (Gwyn), (4) Pass cycle+1 émis par WF0.
- Observation : 4 étapes, chacune un artefact nommé.
- Échec probable : WK13 sautée (cycle enchaîné direct) → **cause** : pression traction. **Contre-action** : le Pass cycle+1 EXIGE l'artefact DEAL de WK13 — mécaniquement impossible d'enchaîner sans.

## ABORT CONDITIONS
1. Pass introuvable ET invariants Beth ≠ GREEN → ne rien activer, signal `airlock-red`.
2. Le calcul WK donne > 13 → le cycle est fini sans DEAL → STOP, escalade A0 (état incohérent).

## VERIFICATION RUNS
1. Contrat wf1 existe, contient table WK + 3 soupapes chiffrées + règle preuve-ou-queue (grep seuils).
2. Simuler un Pass périmé (wk=1 aujourd'hui) → l'activation refuse (dry-run logique documentée).
3. grep `\bW[0-9]` nu dans les nouveaux fichiers → 0 hit.

## RED-TEAM PASS
- **Attaque échouée** : « la poupée russe crée 3 crons de plus » — non : UN trigger (le Pass), les 3 A2 sont des scopes du même tick.
- **Attaque réussie → patch** : « le WIP limit (soupape c) bloque tout si la queue ne draine jamais (items morts) » — patch : item non-pioché depuis 2 WK → auto-route Donna DLQ avec raison. La queue respire, la DLQ garde la trace (rien de perdu, D4).

## SELF-GRADE : 12/12 (mêmes 12 points que wargame 01 — tous tenus ; Beth-compat : la soupape (a) protège aussi les nuits d'A+ : mode conservation ≠ ping A+)
