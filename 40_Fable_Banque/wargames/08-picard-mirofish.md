# WARGAME 08 — MiroFish (Picard, Lighting L1) : l'angle-mort du gouverneur sourd

> Wargamé par Fable 5, 2026-07-06 sous **GO Picard** (args A+ : « MiroFish sur un angle-mort Book précis »).
> Particularité : ce wargame a été **vécu en production pendant son écriture** — l'angle-mort a été trouvé
> dans les données, patché, et la guérison vérifiée. Les moves ci-dessous sont le REPLAY exécutable
> pour tout Picard variant (C1..I1) qui devra chasser le même pattern dans SON domaine.

## L'ANGLE-MORT (D1, trouvé pas décrété)
1. `book_loop.py::detect_mirofish_attached()` = grep « MiroFish » dans calendar.md → **proxy**, faux-vert garanti.
2. Zéro `mirofish-WKnn.md` dans `10_Projects/` (les projets existent, aucun rapport).
3. Le gouverneur WF3 venait de rendre **×8 = RISQUE** dans `loops/artifacts/signals/` — et `grep -c "signals" book_loop.py` = **0**. Le gouverné était sourd.
4. Pire : `next_boundary.rule` disait « si la compression a tenu → **accélère** » — accélérer vers le mur que le gouverneur annonçait.
**Pattern générique** : *un booléen de santé calculé par proxy (grep/trace) au lieu de la source de vérité = evaluation gaming structurel (risque nommé LD01-004).* Chaque Picard variant cherchera D'ABORD les booléens-proxy de son domaine.

## MOVES (replay exécutable, vérifié ce jour)
**M1 — Chasser le proxy** : lister les champs « attached/alive/ok » du loop du domaine → pour chacun, remonter à sa fonction. Trigger : SI la fonction lit autre chose que la source de vérité (grep de trace, présence de fichier non-daté) → angle-mort candidat.
- Observation : ici `mirofish_attached=True` pendant que le gouverneur criait RISQUE. Preuve : dry-run avant patch.
**M2 — Donner l'oreille (patch additif, ownership respecté)** : ajouter `read_governor_signals()` (lecture seule des `sim-*.md`, dernier verdict par fichier, `risque_unabsorbed` si RISQUE sans `status: absorbed`) + champ `mirofish_governor` + risk_flag + règle de boundary conditionnelle (RISQUE → CAP ×4, pas d'accélération). AUCUNE ligne existante supprimée.
- Observation post-patch : `{'signals_read': 2, 'verdicts': {x4: SOUTENABLE, x8: RISQUE}, 'risque_unabsorbed': True}` + rule = « CAP ×4 ». Vérifié dry-run.
- Échec probable : patcher le script d'un autre harness crée un conflit → **cause** : ownership Mavis. **Contre-action** : additif strict (nouveau champ, nouvelle fonction), le schéma existant intact ; épisode calendar informe Mavis/Hermes.
**M3 — Absorber par la queue (LOOP-002)** : signal RISQUE → task `tasks/cap-compression-x4.md` (owner wf2-book, **exit_condition chiffrée** : capacité ≥96/WK sur 2 WK → re-simuler) → signal `status: absorbed` + timeline.
- Observation : run réel suivant → `risque_unabsorbed: False`, rule normale — mais la décision CAP vit dans la queue avec sa condition de sortie. Le flag n'est plus un cri, c'est un contrat.
- Fork : SI un nouveau sim RISQUE apparaît → le flag se relève SEUL (la fonction relit à chaque tick) — pas de re-patch.

## ABORT CONDITIONS
1. Le loop du domaine n'a pas de gouverneur WF3 → créer le sim AVANT de patcher l'oreille (rien à entendre = rien à brancher).
2. Le patch exigerait de modifier une ligne existante du script d'autrui → STOP, faire le fix côté consommateur (contrat).

## VERIFICATION RUNS
1. Avant : dry-run → `risque_unabsorbed: True` + rule cappée. 2. Après absorption : run réel → `False` + rule normale + task en queue. 3. `grep -c signals <loop>.py` ≥ 1. (Les 3 exécutés ce jour, sorties collées ci-dessus.)

## RED-TEAM PASS
- **Échouée** : « le patch casse le schéma Mavis » — non : champ additif, `asdict` sérialise, 7/7 invariants doctrine intacts au run réel.
- **Réussie → patch** : « absorber = éteindre l'alarme sans agir (on crée la task et on l'oublie) » — patch intégré : l'absorption exige une **exit_condition chiffrée** dans la task ; une task cap-* sans exit_condition = signal PAS absorbable (la règle vit dans le README tasks/).

## SELF-GRADE : 12/12 — et c'est le seul wargame du lot dont chaque verification run a déjà tourné en vrai.
