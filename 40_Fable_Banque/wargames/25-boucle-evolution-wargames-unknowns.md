# WARGAME 25 — La Boucle d'Évolution des Wargames : traîner les 4 boîtes d'inconnues vers la lumière, sans jamais interrompre WF0

> ⚡ÉVOLUTION 2026-07-08 : « CLOSE À 25 » = clôture de la **FENÊTRE Fable**, PAS de la banque — la banque gradue (M4), elle ne ferme pas (26 puis 27 gravés depuis). Compte courant : voir [TEMPORAL-CANON](../TEMPORAL-CANON.md) §banque. (wargame 27 M2c)

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Le dernier de la fenêtre Fable (97 %). Mission : faire de la banque (25 rails) un ORGANISME — les wargames évoluent en parallèle entre chaque cycle 12WY, nourris par les rêves de Beth (wargame 24), structurés par Curie/SNW, exécutés en L2 par Picard (WF2) via WF1 Morty / Symphony Plane (Holo Deck), sous le GO triennal WF0 de Spock — pour A0-Amodei. Source du cadre : Mark Kashef (capture A+ CE run) : *« Every unknown lives in one of four boxes. Your prompt only fills the first box. The wargame drags the other three into the light. »*

## Statut recon (D1 — état de la banque CE run)

| Fait | Preuve |
|---|---|
| La banque = 24 rails 12/12 + 2 exécutés live | LEDGER 30 lignes ; wargame 17 (manifest) et 22 M2+M4 (ranking+tribunal) exécutés avec preuves |
| Les known-unknowns sont DÉJÀ marqués dans les rails | chaque wargame porte ses `RECON NEEDED` (18 M1-M3), ses `assumed:` (20 M1, 23 M3), ses gates non-levés — dispersés, jamais récoltés |
| Les unknown-knowns ont leur organe | wargame 24 : le rêve D2 de Beth = exactement « ce que la flotte fait déjà mais que la doctrine n'a pas écrit » |
| Les tripwires d'unknown-unknowns existent | REJECTs surprises evaluator · D6 catalog (ADR-META-006) · compteur de diversité des rêves · deltas `/last30days` — des capteurs, jamais reliés à la banque |
| La cadence hôte existe | CADENCE_12WY : W13 = rétro Chapel + ouverture DEAL — la fenêtre d'évolution SANS toucher WF0 |
| Quota | Fable 97 % — ce wargame clôt la fenêtre ; toute la boucle tourne en M3 |

## Les 4 boîtes, mappées sur les organes (la thèse)

```
┌────────────────────────────┬─────────────────────────────────┐
│ KNOWN KNOWNS               │ KNOWN UNKNOWNS                  │
│ = la banque (25 rails)     │ = les RECON NEEDED + assumed:   │
│ organe: LEDGER + registry  │ organe: REGISTRE À RÉCOLTER (M1)│
│ action: exécuter (ranking) │ action: sondes M3 inter-cycles  │
├────────────────────────────┼─────────────────────────────────┤
│ UNKNOWN KNOWNS             │ UNKNOWN UNKNOWNS                │
│ = la flotte le fait déjà,  │ = invisible PAR DÉFINITION      │
│   la doctrine l'ignore     │ organe: TRIPWIRES seulement     │
│ organe: rêves Beth D2 (24) │ (pas de registre — voir red-team│
│ action: promotion → rails  │ action: latence de détection    │
└────────────────────────────┴─────────────────────────────────┘
Le prompt remplit la boîte 1. La BOUCLE traîne les 3 autres vers la lumière.
```

## MOVES

### M1 — Récolter les known-unknowns (le registre qui dormait dans les rails)
Script M3 : grep de tous les `RECON NEEDED` / `assumed:` / gates non-levés des 25 wargames → `UNKNOWNS-REGISTER.md` (1 ligne : inconnue · wargame source · sonde la moins chère · statut). Entre les cycles, le feeder Boimler (cadran 4) promeut les sondes comme tickets M3 ordinaires — **les inconnues se résolvent dans les creux, jamais en interrompant WF0**.
- **Attendu** : le registre, 100 % sourcé, chaque inconnue avec sa sonde chiffrée.
- **Échec probable** : le registre gonfle sans se vider → **contre-action** : une inconnue sans sonde exécutée en 2 cycles = archivée avec mention honnête « jugée non-porteuse », pas gardée par confort.

### M2 — Le canal unknown-knowns : rêve → rail (le pont 24→25)
Chaque rêve profond mensuel de Beth (24 M2) tague ses patterns promus : ceux qui révèlent une PRATIQUE de flotte non-doctrinée (« les agents font X systématiquement, aucun wargame ne le couvre ») deviennent des **candidats-wargame** dans une file dédiée. Curie/SNW les structure à W13 ; A0-Amodei arbitre lesquels méritent un rail (coût M3 + polish, loi wargame 19 M1 — Fable seulement si le jugement l'exige).
- **Attendu** : ≥ 1 candidat/mois tracé `dream-ref → candidat → rail ou rejet motivé`.

### M3 — Les tripwires d'unknown-unknowns (l'humilité structurelle)
PAS de registre — voir red-team. Quatre fils déjà tendus, à RELIER à la banque : (a) REJECT evaluator sur un cas qu'aucun rail ne prévoyait, (b) entrée D6 catalog (erreur système nouvelle), (c) alarme du compteur de diversité des rêves (saturation = on ne voit plus), (d) delta `/last30days` (le monde a bougé). Chaque déclenchement = ticket `wargame-candidate-UU` automatique. **La métrique est la LATENCE** (tripwire → nouveau rail), jamais la « couverture » — prétendre couvrir l'invisible est le mensonge structurel à refuser.
- **Attendu** : les 4 fils câblés vers la file M2 ; latence médiane mesurée au scorecard Chapel.

### M4 — L'évolution des rails eux-mêmes (append-only, versionnée par cycle)
À W13 de chaque cycle 12WY (la fenêtre Chapel, WF0 jamais interrompu) : chaque wargame dont des MOVES ont été exécutés/invalidés/dépassés reçoit un **appendice ⚡ÉVOLUTION C<n>** (résultats réels vs attendus, moves morts, moves nés) — le corps original JAMAIS réécrit (Règle d'Or #3). Un rail dont TOUS les moves sont clos = gradué → `wargames/_GRADUATED/` avec sa fiche de récolte (`/harvest`, wargame 22 M5). Un rail sans AUCUN move exécuté en 2 cycles = archivé `_TRASH_<date>` avec autopsie 3 lignes.
- **Attendu** : la banque respire — graduations IN _GRADUATED, morts honnêtes OUT, appendices datés.

### M5 — La chaîne de délégation complète (qui fait quoi, épelé une fois)
```
A0-Amodei : arbitre les candidats, review les diffs de rêve      (jamais n'exécute)
Spock/WF0 : le GO triennal + airlock capacité — JAMAIS interrompu (la boucle vit dans W13 + les creux)
Beth      : rêve mensuel → unknown-knowns → candidats             (le sens)
Curie/SNW : structure les candidats en rails à W13 (Una DoD, Pike cap, Chapel mesure)
Morty/WF1 : exécute les sondes + moves élus via tickets Plane (Holo Deck tient les statuts)
Picard/WF2: consomme les rails L2 (client-facing) — MiroFish simule AVANT tout move irréversible
Pane      : le cockpit où A+ VOIT la boucle tourner (wargame 18)  (observation, pas gate)
```
- **Attendu** : ce bloc collé en tête du UNKNOWNS-REGISTER — la boucle a UN schéma de pouvoir, pas dix interprétations.

### M6 — La mesure de la boucle (Chapel, 3 chiffres, pas plus)
Scorecard trimestriel : (1) **taux de conversion** inconnue→résolue (M1), (2) **latence UU** tripwire→rail (M3), (3) **ratio méta/exécution** — les tokens dépensés à faire évoluer les wargames ÷ tokens à exécuter leurs moves, plafonné à **15 %** : au-delà, la boucle se mange elle-même (abort 3).

## ABORT CONDITIONS
1. WF0 n'est JAMAIS interrompu par la boucle — l'évolution vit à W13 et dans les creux du feeder ; un conflit de fenêtre = l'évolution attend, jamais l'inverse.
2. Aucun rail réécrit — appendices ⚡ÉVOLUTION uniquement ; graduation et mort passent par _GRADUATED/_TRASH datés.
3. Ratio méta/exécution > 15 % au scorecard → gel des évolutions 1 cycle, exécution seulement (l'organisme qui ne fait que muter est une tumeur).
4. Beth : la boucle tourne en M3 dans les fenêtres mortes — zéro heure Fable sans arbitrage A0-Amodei explicite, zéro nuit blanche machine pendant les sessions A+.

## VERIFICATION RUNS
1. `UNKNOWNS-REGISTER.md` existe, 100 % des inconnues sourcées wargame+ligne → **pass**.
2. 1 cycle complet : ≥ 3 sondes exécutées, statuts à jour dans le registre → **pass**.
3. 1 candidat né d'un rêve, tracé bout-en-bout (dream-ref → W13 → rail ⚡ ou rejet motivé) → **pass**.
4. 1 tripwire UU déclenché → ticket automatique → latence mesurée → **pass**.
5. W13 : ≥ 1 appendice ⚡ÉVOLUTION posé + le ratio méta/exécution ≤ 15 % au scorecard → **pass**.

## RED-TEAM PASS
- **Attaque ÉCHOUÉE** : « bureaucratie auto-référentielle — des wargames sur les wargames, du nombrilisme de process pendant que rien ne ship » — non : la boucle est jugée sur UN critère externe falsifiable (M6) : les moves EXÉCUTÉS qu'elle produit, plafonnée à 15 % de méta, avec mort automatique des rails stériles (M4, 2 cycles sans exécution = _TRASH). Une bureaucratie ne prévoit ni son plafond ni sa propre mort ; cette boucle grave les deux. Rien à patcher.
- **Attaque RÉUSSIE → patch intégré** : « le quadrant unknown-unknowns est un THÉÂTRE épistémique — par définition on ne peut pas lister l'invisible ; tout "registre UU" sera une liste de known-unknowns déguisés, et la boucle prétendra couvrir ce qu'elle ne peut structurellement pas voir — le proxy-boolean épistémologique » — exact, et le patch est l'AVEU architectural (M3 durci) : la boîte 4 n'a **AUCUN registre, aucune liste, aucune couverture revendiquée** — seulement des tripwires (des capteurs de surprise, pas des prédictions) et UNE métrique honnête : la latence de détection. La boucle ne promet pas de voir l'invisible ; elle promet de réagir VITE quand l'invisible se manifeste — et le compteur de diversité des rêves (24 M3) garde le seul angle mort restant : le jour où plus rien ne surprend, c'est qu'on ne regarde plus.

## SELF-GRADE /12 (SUCCESS-ASPACE)
1-2 ✅ · 3 ✅ forks implicites (archivage honnête, gel méta) · 4 ✅ RECON (banque, LEDGER, organes 24, tripwires inventoriés) · 5 ✅ 4 aborts · 6 ✅ 5 runs + 3 chiffres Chapel · 7 ✅ red-team (bureaucratie échouée par plafond+mort-automatique · théâtre-UU réussie→aveu architectural, latence pas couverture) · 8 ✅ blind · 9 ✅ D1 (le rail refuse de revendiquer l'invisible) · 10 ✅ append-only (⚡ par cycle, _GRADUATED, _TRASH) · 11 ✅ mapping canon complet (M5 : la chaîne A0-Amodei→Spock→Beth→Curie→Morty→Picard→Pane épelée une fois) · 12 ✅ Beth (abort 4 + la boucle vit dans les creux, jamais dans les heures de vie).

**12/12. LA BANQUE EST CLOSE À 25 — et elle est désormais VIVANTE.**
