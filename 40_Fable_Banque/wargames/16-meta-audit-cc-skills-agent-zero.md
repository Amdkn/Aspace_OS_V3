# WARGAME 16 — Méta-audit de l'usage Claude Code : les skills oubliées reviennent aux agents + réveil d'Agent Zero

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Exécuteur : tout harness A0 (ADR-HARNESS-001). Mission : (a) rendre les 77 skills VISIBLES aux agents des cascades WF0/WF1/WF2+L2 pour l'autonomie No-HITL — une skill qu'aucun agent n'invoque n'existe pas ; (b) poser le gate d'intake pour tout futur skill/hook/plugin/harness ; (c) réveiller Agent Zero en sandbox comme harness d'interface navigateur, cap Life OS / WorkAdventure (wargame 14).

## Statut recon (D1, 2026-07-06)

| Fait | Preuve CE run |
|---|---|
| **77 skills** installées dans `~/.claude/skills/` | `ls | wc -l` = 77 |
| **2/77 laissent une trace runtime** | grep worklog : `/wargame` ×3 · `skill /diagnose-proxy-boolean` ×1 — le reste = zéro invocation loggée |
| Le réflexe skills existe pour A+ seulement | hook `UserPromptSubmit` SKILL REFLEX matche les prompts d'A+ — **les workers `claude -p` des runners n'ont AUCUN menu de skills** |
| Agent Zero cloné, dormant | `C:/Users/amado/shadow-l1-agent-zero/` git `186ca2f` (agent.py, agents/, api/, docker/, docs/, extensions/) — P6 Shadow E1 in-loop, E2-E4 gated Rick |
| Le précédent mécanisé existe | `/b1-filter` (E1 déterministe + E2 résiduel) = le patron exact à répliquer pour le registre skills |
| RECON NEEDED | (a) port du webui Agent Zero (lire `conf/` avant run — collision possible avec 8765 graphify / 8770 warmode) ; (b) liste des hooks actifs réels : `settings.json` §hooks |

## Le diagnostic (D6 root cause)

L'oubli n'est pas un défaut de mémoire d'A+ — c'est un **défaut de routage** : les skills sont indexées pour l'HUMAIN (hook réflexe sur tes prompts) mais **invisibles aux AGENTS** qui font 99 % des itérations. Une skill sans agent-owner = un guide Geordi sans `b1_filter:` — le même bug, une couche au-dessus. La cure est le même patron : registre déterministe + injection dans les prompts + sweep.

## MOVES

### M1 — Télémétrie d'usage (mesurer avant de router)
`citadel/collectors/collector_16_skills.py` : scanne `~/.claude/skills/*/SKILL.md` (nom + description 1 ligne) ; grep `worklog.md` + `wiki/log.md` + turn-journal pour compter les invocations ; sortie `data/16_skills_usage.json` + digest « forgotten top-20 » (0 invocation + haute valeur).
- **Attendu** : rapport `77 skills · N invoked · 20 forgotten prioritaires` en 1 run.
- **Échec probable** : les invocations in-session (Skill tool) ne loggent pas dans worklog → cause : seuls les runners loggent → **contre-action** : compter ce qui est PROUVABLE et le dire (`traceable_only: true`) — pas de faux précis.
- **Fork** : SI un skill n'a pas de SKILL.md parsable → liste `malformed`, candidat _TRASH (M5).

### M2 — Le menu de skills injecté aux agents (le cœur)
Chaque WORKER_PROMPT de runner (wf1, gstack L2, futurs W×) reçoit une section `## SKILLS À TA DISPOSITION` — **INDEX-ONLY, max 8 par domaine**, résolue par mapping domaine→skills. Seed du mapping (les oubliées à haute valeur, mappées à leur agent-owner) :

| Skill oubliée | Owner (cascade) | Quand l'agent DOIT l'invoquer |
|---|---|---|
| `/guide-search` + `/guide-cross-search` | tout worker avant de lire le corpus | chercher AVANT de re-lire 1000 guides (anti context-bloat) |
| `/context-bloat-detector` | WF0 Spock (hebdo) | pre-load > 80K tokens |
| `/premortem-fill` | WF3 MiroFish | avant tout nouveau serveur/harness |
| `/lint-wiki` | A3 Data (Archives, 1×/trimestre) | hygiène wiki post-burst |
| `/consolidate-memory` | A3 Data (W2 de cycle) | dédupe MEMORY.md |
| `/diagnose-proxy-boolean` | evaluator M4 (wargame 15) | tout métrique « toujours vert » |
| `/harness-audit` | WF0 Spock (mensuel) | drift de config harness |
| `/l0-watchdog-scrape` | heartbeat (vendredi) | rapport L0 hebdo |
| `/l1-research-pulse` | W2-Rock auto-research | pulse lundi |
| `/b1-filter` | worker WF1 (backlog §2b) | 453 orphelins E2 restants |
| `/learn` + `/instinct-*` | evaluator post-RETURN | distiller la leçon d'un échec |
| `/last30days` | W2-Rock veille | **PAS ENCORE INSTALLÉE** (wargame 15 : 2 commandes marketplace) |

- **Attendu** : la prochaine itération wf1 logge au moins 1 invocation de skill du menu.
- **Échec probable** : le worker ignore le menu (M3 laziness mesurée) → cause : menu descriptif sans déclencheur → **contre-action** : formuler en triggers conditionnels (« SI tu vas lire > 3 guides → `/guide-search` D'ABORD ») — le format fork-à-trigger des wargames, pas une liste passive.
- **Fork** : SI le menu gonfle le prompt > budget → réduire à 5 skills + pointeur vers `SKILL_REGISTRY.md`.

### M3 — Le gate d'intake (tout futur skill/hook/plugin/harness)
`~/.claude/skills/SKILL_REGISTRY.md` : 1 ligne par skill — `nom · domaine B2 · WF owner · agent owner · trigger · statut (active|dormant|_TRASH)`. Règle d'or nouvelle : **rien ne s'installe sans sa ligne de registre** (skill, hook, plugin, MCP, harness — même gate). Sweep `collector_16` flagge les `UNREGISTERED`.
- **Attendu** : `77/77 registered` après le premier sweep de rattrapage ; tout ajout futur naît enregistré.
- **Échec probable** : le registre devient un 78e document mort → cause : pas de consommateur → **contre-action** : le registre EST la source du menu M2 (générer M2 depuis M3) — un registre lu à chaque itération ne meurt pas.
- **Fork** : SI un plugin marketplace s'auto-met-à-jour (last30days) → statut `managed-upstream`, pas de pin local.

### M4 — Réveil d'Agent Zero (sandbox, harness d'interface navigateur)
Étapes : (1) lire `conf/` + README du clone pour le port et le modèle backend (RECON NEEDED a) ; (2) pointer le backend sur MiniMax OpenAI-compat (comme Hermes) — jamais une clé en clair dans les conf commitées ; (3) `docker compose` OU `python agent.py` en sandbox, port non-conflictuel ; (4) 3 expériences documentées : tâche fichier local, tâche web, tâche déléguée à un sous-agent ; (5) verdict d'intégration : Agent Zero = **harness d'interface navigateur d'A+** (l'UI que CC n'a pas), candidat embed **Life OS** (iframe dashboard) puis **room WorkAdventure** (wargame 14 M2 `openWebsite`).
- **Attendu** : webui accessible localhost, 1 tâche complétée bout-en-bout, screenshot.
- **Échec probable** : le clone date (186ca2f) et l'upstream a bougé → cause : drift E1 → **contre-action** : NE PAS pull (le clone est un shadow gelé E1) — expérimenter tel quel, noter le delta pour la décision E2 (gated Rick).
- **Fork** : SI le backend refuse l'endpoint MiniMax → tester avec le fallback Anthropic-compat ; si aucun ne passe → `blocked-agent-zero-backend` + le wargame continue (M1-M3 indépendants).

### M5 — Élagage (77 → un arsenal vivant)
Depuis le rapport M1 : les skills `malformed` + doublons évidents (ex. 3 variantes multi-backend, skills one-shot périmées) → proposition `_TRASH_2026-07/` (D4, jamais hard-delete), validée par l'échelle de décision (Morty tranche, pas A+).
- **Attendu** : registre final < 60 lignes `active`, le reste `dormant|_TRASH` — un menu qui tient dans un prompt.
- **Échec probable** : élaguer une skill utilisée hors-trace → cause : télémétrie partielle (M1) → **contre-action** : quarantaine `dormant` 30 jours avant _TRASH ; réactivation = 1 ligne.

### M6 — Boot & cascade (la boucle se referme)
Le menu M2 + registre M3 entrent dans les prompts des runners déjà boot-durables (LogonTriggers PT5M-PT10M) → chaque cascade WF0→WF1→WF2+L2 démarre avec son arsenal visible. Ligne worklog par itération : `[skills] invoked: <liste|none>` — la télémétrie M1 se nourrit seule.

## ABORT CONDITIONS
1. Agent Zero exige une élévation/écrit hors sandbox → STOP M4, flag (E2-E4 restent gated Rick).
2. Le menu M2 dégrade mesurablement les itérations (évaluator RETURN en hausse) → rollback au menu 5 items.
3. Un élagage M5 casse un hook actif → restaurer depuis _TRASH (réversible par construction).
4. Beth : l'expérimentation Agent Zero = curiosité bornée à 2 h/session — pas une 4e usine à maintenir avant que la 1re (citadel) soit dans sa routine.

## VERIFICATION RUNS
1. `collector_16_skills.py` ×2 → **pass** = rapport + idempotent.
2. Itération wf1 post-menu → **pass** = ligne `[skills] invoked:` non-vide dans le worklog.
3. Installer une skill test SANS registre → **pass** = sweep la flagge `UNREGISTERED`.
4. Agent Zero : `curl -sI localhost:<port>` → **pass** = 200 + screenshot webui.
5. Restaurer 1 skill depuis _TRASH → **pass** = réactive en 1 move.

## RED-TEAM PASS
- **Attaque ÉCHOUÉE** : « le registre M3 est un point de défaillance unique — corrompu, plus aucun agent n'a de skills » — non : le menu est INJECTÉ dans les prompts générés (copie), et les skills restent invocables sans registre ; au pire le sweep signale `registry-unreadable` et régénère depuis `ls skills/` (déterministe, patron wargame 13 M4).
- **Attaque RÉUSSIE → patch intégré** : « injecter le catalogue aux workers recrée le context-bloat que `/context-bloat-detector` existe pour tuer : 77 descriptions ≈ des milliers de tokens par itération × 24/7 = le budget M5 du wargame 15 fond en silence ». Patch : menu **INDEX-ONLY max 8 skills/domaine, format trigger conditionnel 1 ligne**, résolu par domaine du ticket (le mapping B1-filter réutilisé) — jamais le catalogue entier.

## SELF-GRADE /12 (SUCCESS-ASPACE)
1-2 ✅ · 3 ✅ forks triggers · 4 ✅ 2 RECON NEEDED (port A0-zero, hooks actifs) · 5 ✅ 4 aborts · 6 ✅ 5 runs · 7 ✅ red-team (registre SPOF échouée · context-bloat réussie→patch INDEX-ONLY) · 8 ✅ blind · 9 ✅ D1 (ls/grep/git collés) · 10 ✅ _TRASH quarantaine · 11 ✅ mapping cascades/owners canon · 12 ✅ Beth (abort 4 : 2 h max, pas de 4e usine).

**12/12.**
