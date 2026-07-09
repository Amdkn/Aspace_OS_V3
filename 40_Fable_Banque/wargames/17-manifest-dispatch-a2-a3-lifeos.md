# WARGAME 17 — Manifest de Dispatch A2/A3 Life OS (compléter l'isomorphie mindsets par l'analyse comparative Fable)

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Exécuteur privilégié : **Fable 5 pendant les 30 % de quota restants (reset dim. 18:59)** — c'est un travail de distillation doctrine, son sweet spot ; sinon tout harness A0. Mission : compléter la couche `~/.claude/mindsets/` avec le versant A2/A3 Life OS manquant, calqué sur le pattern B2 prouvé, chaque fichier portant les gates mimétiques Fable.

## Statut recon (D1, 2026-07-06)

| Fait | Preuve CE run |
|---|---|
| 26 fichiers mindsets existants | `ls mindsets/` : A0L ×2 · A1 ×5 (Beth/Morty/Rick + 2 dispatch) · B1 ×5 · **B2 ×8 dispatch** · Telegram ×2 · DesktopCommander ×2 · _BASELINES · _LESSONS |
| **GAP : zéro fichier A2, zéro trigger par-A3** | le côté A n'a que Beth_Dispatch (Orville→9, Discovery→8, Protostar→4) et Morty_Dispatch (SNW→5, Enterprise→4, Cerritos→5) — les A3 y sont des COMPTES, pas des lignes de dispatch avec triggers comme les B3 |
| L'analyse comparative Fable = la source | `_DISCIPLINE_BASELINES.md` : **Fable-5 = cible mimétique ★** (913 beats/25 sessions) — reason-first 88 % vs M3 53 · re-evaluate 87 vs 50 · reasoning 82 vs 51 · real-test 63 vs 33. « Close toward Fable, not Opus » |
| Le template prouvé | `B2_Batman_Ops_Dispatch.md` : squad table (agentType/role/dispatch-when) + Law + Heuristic + Applied Principles + anti-dormancy `_LESSONS_APPLIED.md` |
| Roster A3 canon (35, vérifié registre agents) | Orville 9 (Mercer/Grayson/Malloy/Finn/Bortus/Kitan/Isaac/Lamarr/Klyden) · Discovery 8 (Book/Saru/Culber/Tilly/Stamets/Burnham/Reno/Georgiou) · SNW 5 (Pike/Una/M'Benga/Ortegas/Chapel) · Enterprise 4 (Picard/Spock/Geordi/Data) · Cerritos 5 (Mariner/Boimler/Tendi/Rutherford/Freeman) · Protostar 4 (Dal/Rok-Tahk/Zero/Gwyn) |

## MOVES

### M1 — A2_Manifesto.md (le verrou d'isomorphie, miroir de B1_Manifesto)
1 fichier : les 6 A2 ships = Managers-Orchestrateurs du Life OS, isomorphes aux 8 B2 héros (A2↔B2 déjà posé par ADR-L2-A2B2-MAP-001). Law commune : *un A2 décide+route dans son framework, ne fait jamais le travail A3, remonte à son A1*. Concurrency canon : Beth 9+8 = 17 > 16 → **stagger** (Protostar délégué à Data/Archives de Morty) ; Morty 5+4+5 = 14 ≤ 16 → one pass. + le bloc mimétique Fable (les 4 gates, chiffres exacts des baselines).
- **Attendu** : fichier ≤ 120 lignes, même squelette que B1_Manifesto (disposition layer → mécanisme = les 6 fichiers M2).
- **Échec probable** : re-dériver l'isomorphie au lieu de citer ADR-L2-A2B2-MAP-001 → contre-action : le manifesto CITE, ne réinvente pas (D2).
- **Fork** : SI conflit avec Beth/Morty_Dispatch existants → les fichiers A1 restent la loi de ROUTAGE inter-ships ; les nouveaux fichiers A2 = le dispatch INTRA-ship. Zéro réécriture des A1 (D4).

### M2 — Les 6 fichiers A2_*_Dispatch (le manifest lui-même, batch)
`A2_Orville_Ikigai_Dispatch.md` · `A2_Discovery_LifeWheel_Dispatch.md` · `A2_SNW_12WY_Dispatch.md` · `A2_Enterprise_PARA_Dispatch.md` · `A2_Cerritos_GTD_Dispatch.md` · `A2_Protostar_DEAL_Dispatch.md`. Chacun, template B2 exact :
1. **Header Law** (qui dispatche, sous quel A1, quel horizon)
2. **Table squad A3** : `agentType` | rôle | **dispatch when** (les triggers verbatim des définitions d'agents — ex. Cerritos : Freeman ← « je suis paralysé/quoi maintenant », Boimler ← « inbox plein », Rutherford ← « weekly review »…)
3. **Heuristic** (l'ordre : ex. SNW = Pike vision → Una plan → M'Benga focus → Ortegas exécution → Chapel mesure — la chaîne CADENCE_12WY)
4. **Applied Principles** : 3-5 règles enforced du framework (Ikigai Lock GO/NO-GO pour Orville ; drift LD01-08 pour Discovery ; DoD obligatoire pour SNW ; MANIFEST.md requis pour Enterprise/Picard ; capture-jamais-perdue pour Cerritos ; Define→Eliminate AVANT Automate pour Protostar)
5. **Bloc mimétique Fable** : chaque dispatch intra-ship exige les 4 gates (raisonner avant de router · ré-évaluer au retour A3 · tour avec raisonnement · test réel avant SHIP)
- **Attendu** : 6 fichiers ≤ 90 lignes chacun, chaque A3 des 35 a SA ligne de trigger.
- **Échec probable** : inventer un rôle A3 (le péché anti-CANON-001) → contre-action : chaque ligne recopie le trigger du registre `.claude/agents/` — lecture obligatoire AVANT écriture, fichier par fichier.
- **Fork** : SI un A3 du registre n'a pas de trigger clair → `RECON NEEDED` en ligne, jamais une invention.

### M3 — Le câblage (les fichiers doivent être LUS, pas beaux)
(a) Chaque définition d'agent `a2-uss-*` reçoit 1 ligne : « Charge ton dispatch : `mindsets/A2_<Ship>_Dispatch.md` » (le pattern des B2). (b) Le menu skills du wargame 16 M2 ajoute la ligne : « SI tu invoques un A3 → lis d'abord la table de son ship ». (c) `_LESSONS_APPLIED.md` : 6 entrées anti-dormancy.
- **Attendu** : invoquer `a2-uss-cerritos-chaos` → sa première action = lire son dispatch (observable au transcript).
- **Échec probable** : la ligne ajoutée mais jamais suivie (M3 laziness 53 %) → contre-action : formulation trigger (« AVANT ton premier dispatch, lis X ») pas descriptive — et l'evaluator (wargame 15 M4) note `ladder/dispatch-skipped`.

### M4 — Exécution Fable (le plan quota)
Les M1-M2 = 7 fichiers de distillation → **1 session Fable ≤ 15 % du quota restant** (batch write, pas d'itérations), AVANT dim. 18:59. M3 = mécanique, n'importe quel harness. Si le quota expire avant : M3-first (le câblage attend les fichiers, mais le template B2 permet à M3/Hermes de produire les 7 fichiers en qualité moindre + passe evaluator).
- **Fork** : SI Fable 100 % avant exécution → produire via M3 + tag `needs-fable-polish` — le contenu d'abord, le poli au prochain reset.

### M5 — Vérification
1. `ls mindsets/ | grep A2_ | wc -l` → **pass** = 7 (manifesto + 6).
2. grep de chaque `agentType` A3 canon dans son fichier → **pass** = 35/35 présents, zéro nom inventé (diff contre registre).
3. Invocation test d'1 A2 → **pass** = lit son dispatch avant de router.
4. `_LESSONS_APPLIED.md` +6 lignes → **pass** = anti-dormancy tracé.

## ABORT CONDITIONS
1. Un fichier exigerait de réécrire Beth/Morty_Dispatch → STOP (append-only, les A1 sont la loi inter-ships).
2. Divergence roster registre ↔ fichier en cours → STOP le fichier, D1 sur le registre, jamais de « probablement ».
3. Beth : batch en 1 session, pas de marathon nocturne pour battre le reset — si dimanche arrive, M4 fork.

## RED-TEAM PASS
- **Attaque ÉCHOUÉE** : « 7 fichiers de plus = context-bloat au SessionStart » — non : les mindsets sont du **lazy-load par agent** (chaque A2 lit LE SIEN à l'invocation, pattern B2 prouvé), rien n'entre dans le pre-load global. Le bloat ne peut pas se produire par construction.
- **Attaque RÉUSSIE → patch intégré** : « le dispatch intra-ship A2 va entrer en collision avec le dispatch inter-ships A1 : Morty_Dispatch dit déjà quoi router à Cerritos — un A2 zélé re-décidera, et deux couches décideront différemment le même ticket ». Patch (gravé en M1) : **partition stricte des juridictions** — A1 = QUEL ship reçoit l'intention ; A2 = QUEL A3 du ship exécute ; un fichier A2 ne contient AUCUNE règle inter-ships, et toute ligne qui en parle est une violation détectable au grep (`grep -l 'Orville\|Discovery' A2_Cerritos*` doit être vide hors header).

## SELF-GRADE /12 (SUCCESS-ASPACE)
1-2 ✅ · 3 ✅ forks triggers · 4 ✅ RECON NEEDED en ligne pour triggers A3 flous · 5 ✅ 3 aborts · 6 ✅ 4 runs · 7 ✅ red-team (bloat échouée par lazy-load · collision juridictions réussie→patch partition) · 8 ✅ blind (template + roster + chemins exacts) · 9 ✅ D1 (ls/head/baselines collés) · 10 ✅ append-only (A1 intouchés) · 11 ✅ roster 35/35 canon, zéro invention · 12 ✅ Beth (abort 3 : pas de marathon anti-reset).

**12/12.**
