# WARGAME 01 — WF0 Spock : Gouvernance GTD×PARA (Airlock)

> Wargamé par Fable 5, 2026-07-06. Exécuteur cible : **Opus 4.8 (CC)**. Exécutable blind.
> Mission : créer la couche WF0 qui libère Morty du double fardeau structure+traction.

## RECON (fait — D1)
- `mindsets/Morty_Dispatch_Doctrine.md` : Cerritos/GTD = 5 A3 (Mariner capture · Boimler clarify · Tendi organize · Rutherford reflect · Freeman engage) — **le pipeline GTD existe déjà en agents**, WF0 ne le recrée pas, il le GOUVERNE.
- ADR-LOOP-002 (PROPOSED) : queue > loop ; Donna DLQ = destination échecs.
- Typage adopté : `WF` = strates, `WK` = semaines 12WY. JAMAIS mélangés.
- Spock canon = `20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/` (Areas, mémoire long-terme).

## MOVES

**M1 — Créer la doctrine WF0 (fichier unique, append-only)**
- Action : écrire `24_PARA_Enterprise/02_Areas_Spock/WF0_governance.md` : rôle Spock (adjudicateur logique, mémoire Ikigai piliers/horizons, superviseur coachs LD01-08 de Zora), le pipeline gouverné (Cerritos×5), le typage WF/WK.
- Observation attendue : fichier créé, frontmatter OKF (`type:` top-level), ≤150 lignes.
- Échec probable : réécrire une doctrine Cerritos existante → **cause** : recon incomplet du dossier Areas_Spock. **Contre-action** : `ls` le dossier AVANT ; si un fichier gouvernance existe → étendre par section datée, ne pas dupliquer.
- Fork : SI `02_Areas_Spock/` contient déjà `J0x_*` structurés par variant → placer dans le J0x pertinent, PAS à la racine.

**M2 — Le protocole de fork des fragments (capture contradictoire/incomplète)**
- Action : section « Fork Protocol » dans WF0_governance.md : fragment GTD contradictoire → route (a) si contradiction factuelle vs canon → RECON task dans la queue avec le check exact ; (b) si incomplet → placeholder `(( input requis : X ))` + continue ; (c) si contradiction d'intention A+ → escalade A0 (SEUL cas d'escalade).
- Observation : 3 routes écrites avec triggers observables (pas de judgment call).
- Échec probable : sur-escalade (tout part en (c)) → **cause** : trigger (c) trop vague. **Contre-action** : (c) exige DEUX lectures canon divergentes citées — sinon route (a).

**M3 — Le mapping mémoire (ordinateur de bord)**
- Action : vérifier que les index existent : `wiki/index.md` (junction), `MEMORY.md`, cartographie userspace. Ajouter à WF0_governance.md la table « où Spock regarde pour X » (5-8 lignes max, pointeurs seulement).
- Observation : chaque pointeur `Test-Path` = True.
- Échec probable : pointeur vers un fichier déplacé → **cause** : drift canon. **Contre-action** : le pointeur cassé devient une RECON task, pas une invention de chemin.
- RECON NEEDED : est-ce que `gen_wiki_index.py` tourne encore sans erreur ? Check : `python C:\Users\amado\.claude\bin\gen_wiki_index.py` exit 0.

**M4 — Brancher WF0 sur la queue (pas une boucle)**
- Action : le contrat `citadel/loops/domains/wf0-spock/README.md` (créé en P1 du plan) référence WF0_governance.md ; le trigger = heartbeat existant + signal `governance-*` dans artifacts/signals/.
- Observation : contrat lie doctrine ↔ queue ; aucune boucle infinie créée.
- Échec probable : créer un cron dédié WF0 → **cause** : sur-ingénierie (Sobriété). **Contre-action** : WF0 se déclenche par SIGNAL, il ne poll pas.

## ABORT CONDITIONS
1. `02_Areas_Spock/` introuvable ou restructuré → STOP, flag ledger, ne pas créer ailleurs.
2. Un fichier gouvernance WF0 existe déjà avec un contenu divergent → STOP, sister-chain, escalade A0 (Règle d'Or #3).

## VERIFICATION RUNS (exécuteur)
1. `Test-Path WF0_governance.md` → True ; frontmatter `type:` présent (grep).
2. Les 3 routes du Fork Protocol contiennent chacune un trigger littéral « SI …ALORS » (grep "SI ").
3. Aucun nouveau cron créé (CronList inchangé / schtasks inchangé).
4. Épisode append dans `calendar.md`? — NON : WF0 est zone Spock, pas Book. Worklog loops/ suffit. (Piège évité.)

## RED-TEAM PASS
- **Attaque tentée** : « WF0 duplique Cerritos » — échouée : M1 gouverne le pipeline existant (les 5 A3 restent les exécutants), zéro agent créé.
- **Attaque réussie → patch** : « le Fork Protocol route (b) accumule des placeholders jamais résolus » — patch intégré : chaque `(( input requis ))` DOIT créer une task queue avec owner=Rutherford (reflect) ; la revue hebdo Rutherford draine les placeholders. Sans ça, la dette invisible s'accumule.

## SELF-GRADE (SUCCESS-ASPACE) : 12/12 — moves observables ✓ échecs+contre ✓ forks triggés ✓ RECON marqués ✓ aborts ✓ verifs ✓ red-team ✓ blind ✓ D1 ✓ append-only ✓ canon (WF/WK, roster Cerritos exact) ✓ Beth-compat (zéro charge A+) ✓
