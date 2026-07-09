# WARGAME 27 — Consolidation de la cohérence temporelle des wargames 1-25, dans le cockpit Pane

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Écrit à 23h58, 98 % de quota — le dernier geste Fable de la fenêtre. **Note de numérotation (GAP 0 tranché)** : A+ a demandé « le 26 de consolidation », mais `26-audit-rails-ouverts` existe (12/12, LEDGER) — l'écraser violerait D4. Ce wargame est donc le **27**, ET il porte la mission demandée : réconcilier le temps des 25 premiers rails, avec **Pane comme cockpit où la cohérence temporelle devient VISIBLE** (l'ADE introduit tard — wargame 18 — devient l'organe d'affichage du temps de toute la banque).

## Statut recon (D1 — audit de cohérence CE run, grep cité)

| Gap | Preuve | Gravité |
|---|---|---|
| **G0 collision 26** | 26 fichiers réels, A+ demande « 26 » consolidation | tranché ci-dessus : celui-ci = 27 |
| **G1 claims de finalité faux** | 25 déclare « BANQUE CLOSE À 25 » — violé le jour même (26 existe). Idem « 20/20 », « 18 rails » : chaque total fossilise un instantané | structurel |
| **G2 perpétuel vs triennal** | Titre + M2 + red-team de 15 disent « GO Perpétuel » ; 19/20/24/25/26 disent triennal/2029-07-05. Le fondateur contredit sa descendance | doctrine |
| **G3 ×8 vs CAP ×4** | 02 M3 = « soupapes compression 8× » ; 08 prouve `{x4: SOUTENABLE, x8: RISQUE}` → CAP ×4 hérité par 09. Un lecteur de 02 seul sur-compresse | opérationnel |
| **G4 comptes dérivants** | « banque de rails = 18 » (19) · « 24 rails + 2 exécutés » (26) · « close à 25 » (25) — trois vérités d'instants différents sans horodatage de validité | lecture |

## La thèse (D3 — le temps est une DONNÉE, pas une prose)

Les 5 gaps ont UNE racine : les wargames écrivent le temps **en prose** (« perpétuel », « close », « 20/20 », « 8× ») — et la prose ne se met pas à jour. La cure n'est pas de réécrire 25 fichiers (interdit, Règle d'Or #3) : c'est de **sortir les constantes temporelles de la prose vers UNE source affichée** — et le cockpit qui l'affiche existe déjà : **Pane** (wargame 18, layout Citadelle). La banque garde ses fichiers immuables ; le TEMPS vit dans un fichier d'état que Pane montre en permanence.

## MOVES

### M1 — `TEMPORAL-CANON.md` (la source unique des constantes de temps)
Créer `fable-last-week-aspace/TEMPORAL-CANON.md`, ≤ 30 lignes, les SEULES constantes faisant foi :
`GO = triennal 2026-07-05 → 2029-07-05 renouvelable` · `compression CAP = ×4 (×8 = plafond théorique, RISQUE prouvé wargame 08)` · `cadence = CADENCE_12WY (1wk=1day L2)` · `banque = N fichiers, jamais "close" — graduée par W13 (wargame 25 M4)` · `Fable = ≤15 %/sem, reset dim. 18:59` · chaque constante avec son `receipt:` (wargame source + preuve). **Règle de préséance** : en cas de conflit prose-wargame vs TEMPORAL-CANON, le CANON gagne — la prose est un fossile daté.
- **Échec probable** : le CANON devient un 2e endroit qui dérive → **contre-action** : il est mis à jour UNIQUEMENT par les appendices ⚡ÉVOLUTION de W13 (wargame 25 M4) — jamais ad-hoc.

### M2 — Les 3 patches append-only (les fossiles marqués, jamais réécrits)
(a) **Note de tête sur 15** : `> ⚡ÉVOLUTION 2026-07-06 : « Perpétuel » AMENDÉ → GO TRIENNAL renouvelable (compression temporelle, dictée A+). Le titre est conservé comme fossile historique ; TEMPORAL-CANON fait foi.` (b) **⚡ 1 ligne dans 02** : `CAP ×4 établi wargame 08 ({x4: SOUTENABLE, x8: RISQUE}) — les soupapes 8× = plafond jamais soutenu.` (c) **⚡ 1 ligne dans 25** : `« CLOSE À 25 » = clôture de la FENÊTRE Fable, pas de la banque — la banque gradue (M4), elle ne ferme pas. Compte courant : voir TEMPORAL-CANON.`
- **Attendu** : 3 appendices, 0 ligne existante modifiée, grep-vérifiable.

### M3 — Pane = l'horloge de la flotte (le rôle de l'ADE dans la cohérence)
Le layout Citadelle (18 M2) gagne un pane **TEMPS** : affiche `TEMPORAL-CANON.md` + `STATE.json` (go_until, capacity) + le compte réel `ls wargames | wc -l` — rafraîchi par le sweep nightly (26 red-team : la carte est un output de workflow). **La cohérence temporelle cesse d'être une relecture : elle est un AFFICHAGE.** Un humain (A+) ou un agent qui regarde Pane voit l'état temporel vrai sans ouvrir un seul wargame. C'est la réponse au fait que Pane est arrivé tard (18/25) : il devient rétroactivement l'organe de monitoring de TOUTE la banque, pas un outil de plus.
- **Fork** : SI le trial 7j de Pane échoue (18 M5, < 3 sessions) → le pane TEMPS bascule en ligne de worklog nightly — l'affichage meurt, la source (M1) survit.

### M4 — La loi anti-fossile (pour tous les wargames FUTURS)
Ajout au contrat de rail (19 M2, ⚡ append) : **un wargame n'écrit JAMAIS une constante temporelle en dur** — il cite TEMPORAL-CANON (`GO: voir TC §1`). Les nombres de banque, dates de GO, facteurs de compression sont des POINTEURS, pas des valeurs. Les claims de finalité (« close », « complet », « N/N ») sont interdits de rail — remplacés par « gradué à la date X ».

## ABORT CONDITIONS
1. AUCUNE réécriture des 25 corps — appendices ⚡ et notes de tête uniquement (Règle d'Or #3).
2. TEMPORAL-CANON ≤ 30 lignes — s'il gonfle, il devient la prose qu'il devait tuer.
3. Le pane TEMPS est de l'AFFICHAGE (read-only) — jamais un gate de décision (Pane = cockpit, pas harness, ADR-HARNESS-001).
4. Exécution des M = M3-post-reset — 23h58, Fable ne construit pas, il grave le jugement.

## VERIFICATION RUNS
1. `TEMPORAL-CANON.md` existe, ≤ 30 lignes, 100 % des constantes avec `receipt:` → **pass**.
2. 3 appendices posés (15, 02, 25), `grep "⚡ÉVOLUTION"` les trouve, corps intacts (diff = additions only) → **pass**.
3. Pane Citadelle : pane TEMPS visible avec les 3 sources → **pass** (screenshot).
4. 1 futur wargame (le prochain gradué) cite TC au lieu d'une constante en dur → **pass**.
5. Test de contradiction : grep « perpétuel » sans mention triennal dans les rails POST-27 = 0 occurrence → **pass**.

## RED-TEAM PASS
- **Attaque ÉCHOUÉE** : « un TEMPORAL-CANON = une 2e source de vérité qui va diverger des wargames — tu crées le drift que tu prétends tuer » — non : la préséance est écrite (CANON > prose fossile), la mise à jour est mono-canal (W13 ⚡ uniquement), et le pane TEMPS rend toute divergence VISIBLE en permanence au lieu d'enterrée dans 27 fichiers. Une source affichée qui dérive se voit ; 27 proses qui dérivent ne se voient pas. Rien à patcher.
- **Attaque RÉUSSIE → patch intégré** : « ta consolidation est ELLE-MÊME un fossile instantané — ce wargame dit "26 fichiers", "98 %", "23h58" : dans une semaine il sera aussi faux que "close à 25", et le 28e gap sera CE fichier » — exact, et le patch est structurel (M1+M4 durcis) : ce wargame ne PORTE aucune constante faisant foi — toutes vivent dans TEMPORAL-CANON (mis à jour par W13), et les nombres cités ici sont explicitement marqués **fossiles d'audit datés 2026-07-07** (vrais à l'écriture, non-normatifs ensuite). Le rail enseigne la méthode ; le CANON porte les valeurs ; Pane affiche le présent. Trois rôles, zéro fossile normatif.

## SELF-GRADE /12 (SUCCESS-ASPACE)
1-2 ✅ · 3 ✅ fork Pane-mort → worklog · 4 ✅ RECON (5 gaps grep-cités, G0 tranché) · 5 ✅ 4 aborts · 6 ✅ 5 runs grep-ables · 7 ✅ red-team (2e-source échouée par préséance+mono-canal+visibilité · auto-fossile réussie→valeurs déportées au CANON) · 8 ✅ blind · 9 ✅ D1 (chaque gap avec sa citation) · 10 ✅ append-only (3 ⚡, 0 réécriture, 26 préservé) · 11 ✅ mapping canon (Pane=cockpit 18, graduation 25 M4, contrat 19 M2, Règle d'Or #3) · 12 ✅ Beth (abort 4 : à 23h58 Fable juge, M3 construira demain).

**12/12. La banque est graduée à 27 — le temps a quitté la prose.**
