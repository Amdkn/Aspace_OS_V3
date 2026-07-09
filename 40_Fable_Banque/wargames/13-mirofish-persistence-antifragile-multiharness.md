# WARGAME 13 — MiroFish : Persistance · Antifragilité · Idempotence · Multi-Harness parallèle

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Exécuteur cible : **n'importe quel harness A0 par défaut** (CC, MC/MiniMax Code, Omnigent shadow-l0, Hermes) — per ADR-HARNESS-001, aucun n'a le droit de dire « pas mon rôle ». Ton job = la route pour durcir MiroFish (WF3) afin que N harness puissent le déclencher EN PARALLÈLE sans corruption, que ses artefacts survivent à tout restart, et que 2 runs identiques produisent exactement 1 état.

## Statut au moment du wargame (D1 receipts, recon 2026-07-06)

| Fait | Preuve lue CE run |
|---|---|
| Runner déterministe, zéro LLM, gate flag | `citadel/cron/wf3_sim_runner.py` docstring + `gate()` sur `decisions/enable_wf3.flag` (présent : « posed by spock_airlock ») |
| 2 runs aujourd'hui, sorties IDENTIQUES | worklog 04:08 + 12:49 → `done=775.7 · queue_fin=472.3 · saturations=90` deux fois = déterminisme prouvé |
| Signaux persistants + absorbés | `artifacts/signals/sim-cadence-x{4,8}.md`, timeline append-only, `[wf2-book] ABSORBE → tasks/cap-compression-x4.md` |
| Contrat boundaries | `loops/domains/wf3-mirofish/README.md` : sim n'écrit QUE worktree+signal, jamais canon ; prédiction sans conditions d'invalidation = rejetée |
| **GAP 1 — pas de lock** | grep du runner : aucun lockfile/mutex — 2 harness simultanés = writes entrelacés sur le même `sim-*.md` |
| **GAP 2 — `seen: 1` figé** | `sim-cadence-x8.md` header dit `seen: 1` après 2 runs — le compteur ne suit pas la timeline |
| **GAP 3 — schtask non prouvé** | `schtasks /query | grep aspace/loop/wf` = vide ce run + UAC `Access is denied` 16:25 (turn-journal) → RECON NEEDED : `schtasks /query /tn <nom exact>` |

## MOVES

### M1 — Singleton lock (le patron wf1 déjà prouvé aujourd'hui)
Ajouter au runner un lockfile `cron/wf3.lock` (PID+timestamp, atomic create `O_EXCL`) pris AVANT toute écriture, libéré en `finally`. Lock âgé > 10 min = stale, réclamable (crash antérieur).
- **Attendu si OK** : 2 lancements simultanés → le 2e log `[wf3-mirofish] SKIP: lock held by PID <n>` et exit 0 ; exactement 1 timeline line ajoutée.
- **Échec probable** : lock orphelin après kill → cause : pas de check stale → **contre-action** : si mtime lock > 600 s ET PID mort → réclamer + logger `lock-reclaimed`.
- **Fork** : SI le harness ne peut pas créer le fichier (permission) → route B : écrire le signal dans `simspace/` et flagger `blocked-lock-permission`, ne JAMAIS écrire sans lock.

### M2 — Idempotence au niveau FICHIER (run-id dedupe)
Le déterminisme du calcul ne suffit pas : la timeline append à chaque run. Introduire `run_id = sha1(slug + date_jour + params)` ; avant d'appender, grep du run_id dans le signal — présent → n'appender rien, incrémenter `seen:` seulement.
- **Attendu si OK** : 3 runs même jour → 1 seule ligne timeline nouvelle max, `seen: 3`.
- **Échec probable** : le header YAML réécrit à la main casse le parse → cause : édition manuelle → **contre-action** : parse tolérant, si `seen` illisible → le recréer à 1 + ligne `seen-reset` dans worklog.
- **Fork** : SI params (VARIATIONS) ont changé depuis le dernier run → nouveau run_id → nouvelle ligne timeline légitime + tag `params-changed` (ce n'est PAS un doublon).

### M3 — Persistance prouvée (survit au restart, schtask réel)
(a) Les signaux sont des fichiers : déjà persistant. (b) Prouver le déclencheur : `schtasks /query /fo LIST /tn "<tâche wf3>"` doit répondre ; sinon l'installer via `install-loops.ps1` en session élevée (l'UAC de 16:25 est la route connue : élévation requise, pas un bug).
- **Attendu si OK** : la query retourne `Ready` + `Next Run Time` ; après reboot simulé (kill runner + relance schtask) le signal repart sur le même run-id dedupe.
- **Échec probable** : `Access is denied` hors élévation → cause : UAC → **contre-action** : flagger `blocked-uac-elevation` pour A+ (2 min manuelle), NE PAS contourner l'UAC.
- **Fork** : SI la tâche existe mais `Last Result != 0` → lire `logs/` du runner d'abord (D6 : collecter le message exact), pas de re-théorisation.

### M4 — Antifragilité (corruption → auto-reconstruction)
Un `sim-*.md` corrompu/supprimé n'est PAS une perte : le runner est déterministe → re-run = reconstruction exacte. Ajouter au début du runner : si signal existant mais frontmatter non parsable → renommer en `_TRASH_<date>/` (D4 no-hard-delete) + regénérer + ligne worklog `signal-rebuilt`.
- **Attendu si OK** : `echo garbage > sim-cadence-x4.md` puis run → fichier reconstruit identique (diff nul sur le corps), original en _TRASH.
- **Échec probable** : la timeline historique (absorptions WF2) est perdue dans la reconstruction → cause : la timeline n'est pas dérivable du calcul → **contre-action** : avant _TRASH, extraire les lignes `[wf2-*]` parsables et les re-appender au signal neuf (le vécu survit, le corps est recalculé).
- **Fork** : SI même la re-extraction échoue → le signal neuf porte `timeline-lost: <path _TRASH>` — trace honnête, pas d'invention.

### M5 — Multi-harness parallèle : la QUEUE arbitre, pas les harness (ADR-LOOP-002)
CC, MC, Omnigent ne lancent PAS le runner directement en concurrence : chacun dépose un fichier `artifacts/signals/sim-request-<harness>-<runid>.md` (déjà prévu au contrat : `trigger: schtask | signal sim-request`). Le runner (singleton M1) consomme les requests au prochain tick, exécute UNE fois par run_id distinct, et tague le request `absorbed`.
- **Attendu si OK** : 3 harness déposent en même temps → 3 requests, 1 run (même run_id) ou N runs (params distincts), zéro écriture concurrente sur les signaux.
- **Échec probable** : un harness impatient court-circuite la queue et exécute le runner direct → cause : persona-shield inversé (« moi je peux ») → **contre-action** : le lock M1 le neutralise mécaniquement (SKIP), et le request reste en queue — le design pardonne l'indiscipline.
- **Fork** : SI un request reste > 24 h non absorbé → le déposant le tague `stale-request` et alerte worklog (le silence est interdit, ADR-LOOP-003 signals).

### M6 — Boundary inviolée (le réel jamais touché)
Re-vérifier après M1-M5 que le runner n'écrit toujours QUE : lock, simspace/ (nettoyé), signals/, worklog. Zéro écriture canon/LD01/10_Projects/plans.
- **Attendu si OK** : `git status`-like diff des paths écrits ⊆ {cron/, artifacts/signals/, logs/} — collé dans le rapport.
- **Échec** : tout path hors liste → **ABORT immédiat** (voir ci-dessous).

## ABORT CONDITIONS
1. Un move exige d'écrire hors de `citadel/` → STOP, flag `boundary-violation`, rien n'est commité.
2. `enable_wf3.flag` absent au moment d'un run réel → exit 2 silencieux du runner = comportement CORRECT, ne pas « réparer » en recréant le flag à la main (seule la cascade GO_SPOCK_UNIQUE le pose).
3. L'UAC bloque ET A+ absent → flag `blocked-uac-elevation`, la mission continue sur M1/M2/M4/M5 (indépendants du schtask).
4. Beth : rien ici ne touche vie/santé A+ — si un move se met à exiger une intervention nocturne récurrente d'A+, c'est un design raté → STOP et redesign.

## VERIFICATION RUNS (l'exécuteur les court dans cet ordre)
1. `python wf3_sim_runner.py & python wf3_sim_runner.py` (parallèle) → **pass** = 1 seule nouvelle ligne timeline + 1 `SKIP: lock held` dans les logs.
2. Re-run ×2 même jour → **pass** = `seen:` incrémente, timeline stable (grep run_id = 1 occurrence).
3. Corruption test (M4) → **pass** = diff corps nul, `_TRASH_<date>/` contient l'original, lignes `[wf2-*]` préservées.
4. `schtasks /query /fo LIST /tn <tâche>` → **pass** = `Ready` + Next Run Time affiché (ou flag UAC honnête).
5. Dépôt de 2 `sim-request-*` par 2 harness différents → **pass** = les 2 tagués `absorbed` au tick suivant, zéro doublon signal.
6. Boundary diff (M6) → **pass** = liste des paths écrits collée, tous dans la liste blanche.

## RED-TEAM PASS
- **Attaque qui a ÉCHOUÉ contre le design** : « supprimer `enable_wf3.flag` en plein run pour corrompre l'état » — le gate n'est lu qu'au démarrage, la sim est read-only sur le réel et son signal reste valide ; pire cas = un run de plus refusé au tick suivant. Rien à patcher.
- **Attaque qui a RÉUSSI → patch intégré** : « le déterminisme masque la non-idempotence : 2 harness lancent le runner à la même seconde, les `open(..., 'a')` s'entrelacent → timeline garblée dans `sim-cadence-x4.md`, et comme les CONTENUS sont identiques, personne ne le remarque (faux vert, cousin du proxy-boolean guéri ce matin) ». Patch = M1 lock atomic + M2 run_id dedupe — c'est devenu le cœur du wargame.

## SELF-GRADE /12 (SUCCESS-ASPACE)
| # | Critère | Verdict |
|---|---|---|
| 1-2 | Observation attendue + échec/cause/contre-action par move | ✅ M1-M6 |
| 3 | Forks à triggers, zéro judgment call | ✅ (SI…→route) |
| 4 | RECON NEEDED explicites | ✅ GAP 3 schtask + check exact |
| 5 | Abort conditions | ✅ 4, dont la n°2 anti-« réparation » du gate |
| 6 | Verification runs épelés avec pass | ✅ 6 runs |
| 7 | Red-team : 1 échouée + 1 réussie→patch | ✅ |
| 8 | Exécutable blind mid-tier | ✅ commandes + paths exacts |
| 9 | D1 receipts | ✅ table statut (fichiers lus ce run) |
| 10 | Append-only / _TRASH | ✅ M4 |
| 11 | Mapping canon (WF3=sim, jamais le réel ; roster) | ✅ contrat cité |
| 12 | Beth-compat | ✅ abort n°4 |

**12/12.**
