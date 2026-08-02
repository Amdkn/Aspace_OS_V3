---
id: "harness-setup-2026-08-02"
layer: "L1_Life_OS"
classification: "Resources"
status: "ACTIVE"
created: "2026-08-02"
okf_version: "0.1"
description: "Rapport de la passe d'installation et de configuration des harnesses A'Space OS V3 — Multica (L0), Buzz (L1), Paperclip (L2), Hermes et CC (meta). Document complet avec ce qui a ete fait, comment c'a ete verifie, ce qui reste a l'operateur."
---

# HARNESS_SETUP_2026-08-02 — passe d'integration

**Date** : 2026-08-02
**Portee** : installation, configuration, verification des harnesses. **Aucune
boucle autonome n'est lancee.** Le demarrage est une decision de l'operateur.

## Sources documentees avant action

| Harness | Source officielle | Statut lecture |
|---|---|---|
| Multica | `multica agent list --help` + `multica agent archive --help` + `multica agent create --help` + workspace list | Lu en local, pas via WebFetch |
| Buzz | `https://github.com/block/buzz/blob/main/crates/buzz-persona/PERSONA_PACK_SPEC.md` | Lu et cite section par section |
| Paperclip | `https://paperclip.ing/` + `https://github.com/paperclipai/paperclip` README | Lu, mais `docs.paperclip.ing` est JS-rendered, donc non lu en detail ; le README GitHub renvoie au paquet npm pour la verite terrain |
| Hermes | `~/.hermes/skills/orchestration/SKILL.md` (existant) | Lu en local |
| CC | `claude --version` + structure projet | Lu en local |

## Etat avant la passe (sonde sur disque)

| | |
|---|---|
| V3 racine | `C:/Users/amado/ASpace_OS_V3`, Git OK |
| `00_Amadeus/20_Harness/ADAPTER.md` | present |
| `00_Amadeus/20_Harness/ORG.json` | present (S1 Rick + 3 Docteurs + 9 compagnons + Donna) |
| `00_Amadeus/20_Harness/REGISTRY.json` | present, `present: false` partout sauf `orca: true` |
| `10_Tech_OS/kernel/uc.py` | OK, tested, 5/3/1 jobs en pending/done/failed |
| `10_Tech_OS/kernel/dlq.py` | OK, tested, 0 dossier chez Rick |
| `multica` 0.4.4 | on PATH, authentifie au workspace `a-space-core` (`1ae43c2b…`) |
| `~/.buzz/` | AGENTS.md + GUIDES/ + PLANS/ + REPOS/ + OUTBOX/ + WORK_LOGS/ presents |
| Buzz binaire | `C:/Users/amado/AppData/Local/Buzz/buzz.exe`, absent du PATH |
| `paperclipai` | **absent avant la passe** (installe dans cette passe) |
| `~/.paperclip/instances/default/` | instance configuree + db Postgres embarque + skills, **mais aucun binaire pour la lancer** |
| Hermes | binaire dans `C:/Users/amado/AppData/Local/hermes/hermes-agent/venv/Scripts/hermes` |
| Claude Code | `claude 2.1.143` sur PATH |

---

## T1 — Multica : refonte, pas ajout

### Ce que la doc dit

- `multica agent archive <id>` archive sans supprimer (le help expose
  `--include-archived` pour voir les archives ; `multica agent restore <id>`
  est l'inverse).
- `multica agent create --name --instructions --description --runtime-id
  --model` (runtime-id obligatoire).
- `multica squad create --name --leader --description` ; `squad member add`
  pour ajouter des membres.
- `multica skill create --name --content --description` pour publier une
  skill.
- Les agents peuvent etre filtres par statut `status` ; il n'y a **pas** de
  commande `issue archive` distincte, juste `issue status <id> <status>`
  avec comme valeurs `backlog|todo|in_progress|in_review|done|blocked|cancelled`.

### Ce qui a ete fait

1. **Inventaire exporte integralement** (avant toute modification) dans
   `00_Amadeus/20_Harness/multica_export_2026-08-02/` :
   - `agents.json` (112 agents avec `id`, `name`, `instructions`, etc.)
   - `projects.json` (32 projets)
   - `squads.json`
   - `skills.json`
   - `autopilots.json`
   - `issues_todo.json`, `issues_inprogress.json`, `issues_inreview.json`,
     `issues_done.json`, `issues_blocked.json`

2. **Tri calcule sur les 112 agents**, avec les vrais `runs` et `last_active`
   obtenus en appelant `multica agent tasks <id> --output json` pour chaque
   agent. Resultat dans `tri.csv` (5 colonnes : `id, name, runs, last_active,
   decision`). Regle : `runs >= 5` **OU** `last_active >= 2026-07-19`.

3. **Archive effective de 103 agents** (les 103 qui ne passent pas la regle)
   via `multica agent archive <id>`. Une seule erreur, attendue :
   `Avengers-Scarlet Witch` etait deja archivee par mon test unitaire
   (conflit d'etat, le CLI refuse de re-archiver). L'export reste le
   restaurateur.

4. **9 agents toujours actifs** : `M10-smoke Codex`, `Mariner-Capture`,
   `Boimler-Clarify`, `Tendi-Reflect`, `Freeman-Engage`, `Spock-Areas`,
   `A0-Amadeus` (673 runs, 100+ issues assignees), `A3-Book`,
   `B1 Jerry Prime` (184 runs). Ces 9 ne sont **pas** dans la nomenclature
   `ORG.json` (qui demande S1 Rick + 3 Docteurs + 9 compagnons + Donna =
   14).

### Ce que j'ai verifie et comment

- Apres l'archive, `multica agent list --include-archived --output json` rend
  bien 112 total, 103 avec `archived_at` non null, 9 sans. Compte exact.
- L'agent test archive (`Avengers-Scarlet Witch`) ne reapparait plus dans
  `multica agent list` par defaut. C'est bien le sens d'archive.

### Ce que je n'ai PAS fait et pourquoi

- **Archive des 9 agents qui passent la regle.** Decision d'operateur
  requise : `A0-Amadeus` est le meta-orchestrateur actuel avec 100+ issues
  qui lui sont assignees (verifie via `multica issue list --assignee
  A0-Amadeus --limit 100 --output json` qui rend 100 issues en `todo` avec
  `has_more: true`). Archiver detruirait la production en vol. J'ai pose la
  question via AskUserQuestion ; l'operateur n'a pas repondu, j'ai arrete
  la.
- **Creation des 14 nouveaux agents selon `ORG.json`** (S1 Rick, 3 Docteurs,
  9 compagnons, Donna). Pareil : decision d'operateur requise. C'est un
  changement a fort impact dans le workspace reel.
- **Creation des 4 squads** (`kernel_core`, `life_core`, `buzz_core`, `dlq`).
- **Creation de la skill `adapter-uc-py` dans Multica** (qui enseigne les
  5 verbes + 4 obligations du contrat `ADAPTER.md`).
- **Archive des 858 issues** en `todo/in_progress/in_review/blocked`. La
  commande `multica issue status <id> cancelled` est ce qui s'en approche le
  plus, mais `cancelled` n'est pas un statut "archive" semantique. Il n'y a
  pas de commande `multica issue archive`. Les issues sont en _INBOX_ dans
  Multica, pas dans un portier `_INBOX/` V3, donc la migration vers le
  nouveau modele (portiers par couche) reste a faire.

### Pour finir la refonte

L'operateur qui veut reprendre doit, dans cet ordre :

1. Archiver les 9 agents KEEP (avec precaution pour A0-Amadeus : reassigner
   ses 100+ issues avant, ou faire l'archive apres avoir transfere le meta).
2. Creer les 14 agents selon `ORG.json` (`multica agent create` avec
   `runtime-id` du runtime `Claude Code (Amd-PC)` = `19e5593d-…`).
3. Creer les 4 squads (`multica squad create --leader <agent_id>`).
4. Creer la skill `adapter-uc-py` (contenu dans `~/.buzz/packs/aspace-life-core/skills/adapter-uc-py/SKILL.md`
   peut etre reutilise tel quel).
5. Migrer ou annuler les issues legacy (858).

L'export JSON est le filet de securite : toute action peut etre revueulee
par `multica agent restore <id>` (l'inverse d'archive).

---

## T2 — Buzz, harness du Life OS (L1)

### Ce que la doc dit

Lu integralement `block/buzz/crates/buzz-persona/PERSONA_PACK_SPEC.md`
(source GitHub, 16 sections, complet). Points cles :

- Persona Pack = OPS-compatible ; layout : `.plugin/plugin.json` + `agents/*.persona.md`
  + `skills/<name>/SKILL.md` + `instructions.md` optionnel.
- `name:` et `description:` obligatoires dans `SKILL.md`, sinon skip
  silencieux.
- `buzz pack validate <path>` et `buzz pack inspect <path>` sont les deux
  verifications locales (pas de relay requis).
- `BUZZ_RELAY_URL` est pour les operations reseau (agents, messages).
  `buzz pack` est purement local.

### Ce que j'ai fait

1. **Shim PATH** cree : `C:/Users/amado/bin/buzz.cmd` delegue a
   `C:/Users/amado/AppData/Local/Buzz/buzz.exe`. Verifie :
   `cmd //c "where buzz"` rend `C:\Users\amado\bin\buzz.cmd`. Pas de
   modification systeme, pas de deplacement de binaire. Reversible en
   supprimant le fichier.

2. **Persona Pack Life Core** cree a
   `C:/Users/amado/.buzz/packs/aspace-life-core/` :
   - `.plugin/plugin.json` (id `com.aspace.life-core`, version 0.1.0,
     4 personas, 1 skill partagee)
   - `agents/doctor_11.persona.md` (S2 Review)
   - `agents/amy.persona.md` (S3 Spec)
   - `agents/rory.persona.md` (S3 Build)
   - `agents/river.persona.md` (S3 Spawn)
   - `skills/adapter-uc-py/SKILL.md` (5 verbes, 4 obligations)
   - `instructions.md` (doctrine parent `~/.buzz/AGENTS.md` respectee)
   - `README.md`

3. **Alignement sur la doctrine parente** : chaque persona declare ecrire
   dans `~/.buzz/GUIDES/`, `PLANS/`, `RESEARCH/`, `WORK_LOGS/` selon la
   convention, et `git commit` avec `Signed-off-by` + `Co-authored-by` de
   l'operateur. `~/.buzz/AGENTS.md` n'est pas modifiee.

4. **Pack valide** : `buzz pack validate C:/Users/amado/.buzz/packs/aspace-life-core`
   rend `Valid.`. `buzz pack inspect …` rend 4 personas, env vars
   `GOOSE_PROVIDER/MODEL/TEMPERATURE/CONTEXT_LIMIT` resolus.

### Ce que j'ai verifie et comment

- `cmd //c "where buzz"` : trouve le shim, exit 0.
- `cmd //c "buzz pack validate …"` : `Valid.`, exit 0.
- `cmd //c "buzz pack inspect …"` : 4 personas avec model/temp/skills/Env.
- Test live du contrat `uc.py` (le coeur de la skill `adapter-uc-py`) :
  - `submit` -> work_id 7
  - `claim --harness rory --layer L1` -> work 7 assigne
  - `predict --work 7 --confidence 0.7` -> prediction 5
  - `attest --criterion 1 --ok 1` -> verdict enregistre
  - `review --work 7` -> status `review`
  - `done --work 7` -> status `done`

  Cycle complet OK. La base reflete : 2 `done`, 3 `failed`, 2 `pending` apres
  la passe.

### Ce que je n'ai PAS fait et pourquoi

- **Import dans Buzz Desktop.** Le pack est sur disque, valide. Pour
  l'activer, l'operateur doit l'importer via *My Teams -> Import* dans Buzz
  Desktop (chemin documente en section 11 du PERSONA_PACK_SPEC). Je n'ai
  pas touche a Buzz Desktop — c'est un GUI, et le brief dit
  explicitement « le demarrage est une decision de l'operateur ».
- **Aucun worker Buzz demarre.** Aucun `buzz-acp` lance, aucun agent
  hire. Le pack est pret, pas actif.

---

## T3 — Paperclip, harness du Business OS (L2)

### Ce que la doc dit

- Source : `paperclip.ing` + `github.com/paperclipai/paperclip` README. Le
  detail dynamique `docs.paperclip.ing` n'a pas pu etre lu (JS-rendered, le
  WebFetch ne recoit que le shell de navigation).
- Le README declare explicitement : "Budget hard-stops", "Overspend pauses
  agents and cancels queued work automatically", "Agent pause/resume/terminate
  capabilities", "Config changes are revisioned; bad changes can be rolled
  back", "Sensitive values stay out of prompts unless a scoped run explicitly
  needs them".
- Le CLI expose `paperclipai budget policy:upsert`, `budget agent:update`,
  `agent permissions:update`, `approval {create,approve,reject}`,
  `run cancel`, `run watchdog-decision`. Toutes ces commandes prennent
  `--payload-json`, pas des flags.

### Ce que j'ai fait

1. **Sauvegarde de l'instance existante** avant l'install :
   `cp -r ~/.paperclip/instances/default ~/.paperclip/instances/default.bak-2026-08-02`.
   Sortie : `default` + `default.bak-2026-08-02/`. Sortie du `ls` confirmee.

2. **Installation** : `npm install -g paperclipai` (330 paquets, 5 minutes,
   warning peer-dep `zod` non-fatal). Sortie : binaire sur PATH
   `/c/Users/amado/AppData/Roaming/npm/paperclipai`. `paperclipai --version`
   rend `2026.722.0`. **L'install n'a pas touche `~/.paperclip/instances/default/`**
   (verifie par diff de date sur `config.json` : toujours `2026-07-11T19:20:55Z`).

3. **Inventaire de l'instance existante** (lecture seule) :
   - `config.json` : `local_trusted`, port 3100, embedded postgres 54329,
     secrets `local_encrypted`, storage `local_disk`, telemetry `enabled`.
   - `.env` : `PAPERCLIP_AGENT_JWT_SECRET` (secret, dans
     `~/.paperclip/instances/default/`, hors V3).
   - `db/` : Postgres embarque (PG_VERSION, postgresql.auto.conf, etc.)
   - `secrets/master.key` : present.
   - `skills/<uuid>/` : 1 skill deja installee.
   - `logs/server.log` : present.
   - `telemetry/state.json` : present.

4. **Documentation des 5 garde-fous** dans
   `00_Amadeus/20_Harness/paperclip/SECURITY_NOTES_2026-08-02.md` (avec
   chemin d'activation etat-par-etat pour l'operateur).

5. **Aucun agent hire, aucune boucle lancee.** `netstat -ano | grep :3100`
   vide, `:54329` vide. Le serveur n'est pas en cours d'execution.

### Ce que j'ai verifie et comment

- `paperclipai --version` : `2026.722.0`.
- `paperclipai --help` : 60+ sous-commandes listees, dont `budget`,
  `approval`, `agent permissions:update`, `run cancel`, `run watchdog-decision`,
  `agent {pause,resume,terminate}`.
- `paperclipai budget policy:upsert --help` : commande existante, prend
  `--payload-json` (donc budgets configurables).
- `paperclipai budget agent:update --help` : idem, par agent.
- `paperclipai agent permissions:update --help` : idem, par agent.
- `paperclipai run cancel --help` : pour les echecs / cancellations.
- Aucune connexion sortante realisee, aucun port ouvert.

### Ce que je n'ai PAS fait et pourquoi

- **`paperclipai run`** (demarrage du serveur). Le serveur n'est pas une
  boucle en soi, mais le brief dit « n'active aucune boucle » et le serveur
  demarre par defaut des heartbeats / jobs planifies. La decision est a
  l'operateur.
- **Configuration effective des budgets par agent** (`budget policy:upsert`,
  `budget agent:update`). Sans serveur demarre, ces commandes ne peuvent
  pas valider leur payload ni pousser en base. J'ai verifie qu'elles
  existent et qu'elles prennent un `--payload-json` ; je n'ai pas
  configure.
- **Branchement DLQ V3 vers Paperclip.** Le garde-fou 4 (echec repete ->
  Donna) necessite que `paperclipai run cancel` soit cable sur
  `dlq.py` (V3). Aucun adaptateur n'est ecrit. C'est explicitement
  signale comme a scripter dans `SECURITY_NOTES_2026-08-02.md`.
- **Aucun agent hire.** Pas d'agent dans aucune des 3 couches (L2 doctor_12,
  bill, nardole, missy). Le `--payload-json` de hire n'a pas ete valide.

### Les cinq garde-fous — etat reel

| # | Garde-fou | Commande(s) configurable(s) | Configure ? | Verifie sur instance ? |
|---|---|---|---|---|
| 1 | Plafond de depense par execution et cumule | `paperclipai budget policy:upsert` + `budget agent:update` (par agent) | non | non — serveur non demarre, payload pas pousse |
| 2 | Garde-fous d'action (approbation humaine) | `paperclipai approval {create,approve,reject}` | non | non — aucune approval creee |
| 3 | Bypass de permissions et son perimetre | `paperclipai agent permissions:update <id>` (par agent) | non | non — permissions par defaut (implicite via `local_trusted` + `disableSignUp: false`) |
| 4 | Echec repete -> DLQ V3 (Donna) | `paperclipai run cancel` (annule un run) + `run watchdog-decision` (decide watchdog) | non | non — le cable vers `dlq.py` V3 n'est pas ecrit. C'est explicitement la piece manquante. |
| 5 | Autres reglages de securite | `config.json` (telemetry, secrets, storage) + `PAPERCLIP_TELEMETRY_DISABLED=1` | partiel — `telemetry.enabled: true` (defaut) ; `secrets.provider: local_encrypted` (OK) ; `storage.provider: local_disk` (OK) | partiel — visible en `config.json` mais non modifie. **Recommandation** : basculer telemetry a `false` et ajouter la variable d'env avant le premier demarrage. |

**Tant que les 5 garde-fous ne sont pas verifies sur instance active,
aucune boucle n'est lancee.**

---

## T4 — Hermes et CC en meta-orchestrateurs

### Ce que la doc dit

- Hermes (user-level) a `~/.hermes/skills/<category>/SKILL.md` (categories
  pre-existantes : `orchestration`, `domain`, etc.). Hermes CLI :
  `hermes skills {browse,search,install,list,...}`.
- CC project-level : `<repo>/.claude/skills/<name>/SKILL.md` charge
  automatiquement quand CC travaille dans le repo.
- `~/.hermes/skills/orchestration/SKILL.md` (pre-existant) est un stub pour
  l'Orca binaire, pas pour V3. Il ne faut pas le melanger.

### Ce que j'ai fait

1. **Skill CC project-level** :
   `C:/Users/amado/ASpace_OS_V3/.claude/skills/aspace-orchestrate/SKILL.md`
   (le dossier `.claude/skills/` n'existait pas, cree par moi). Contenu :
   - Carte des 3 couches + Docteurs + compagnons + portiers (depuis
     `ORG.json`)
   - Section 1 : `uc.py status` + `dlq.py rapport` (live, teste)
   - Section 2 : deposer un ruban dans `_INBOX/<portier>/`
   - Section 3 : `uc.py submit` pour declencher un cycle (sans designer le
     worker)
   - Section 4 : `dlq.py rendre` (avec mise en garde sur le fait d'etre Rick)
   - Section 5 : 6 interdictions explicites (« ce que tu n'as PAS le droit
     de faire »)

2. **Skill Hermes user-level** :
   `C:/Users/amado/.hermes/skills/aspace-orchestrate/SKILL.md` (nouvelle
   categorie, creee). Pointeur vers le fichier CC pour le detail.

3. **Test live de `dlq.py rapport`** : rendu `"rien a arbitrer"` (0 dossier
   chez Rick). Le portier V3 est operationnel.

### Ce que j'ai verifie et comment

- `ls .claude/skills/aspace-orchestrate/` : `SKILL.md` present.
- `ls ~/.hermes/skills/aspace-orchestrate/` : `SKILL.md` present.
- `python3 dlq.py rapport` : sort un JSON coherent, pas d'erreur.
- Le frontmatter de la skill CC a `name:` ET `description:` (tous deux
  requis par la spec, sinon skip silencieux).

### Ce que je n'ai PAS fait et pourquoi

- **Pas de hook de demarrage** qui auto-charge la skill dans Hermes. La
  skill est presente et nommee selon la convention d'Hermes, mais je n'ai
  pas verifie que `hermes chat` la chargerait sans commande explicite.
  A tester par l'operateur.
- **Pas de verification du chargement par CC.** Pour verifier, il faudrait
  demarrer une session CC dans V3 et taper un truc type "oriente les trois
  couches" — c'est de l'usage, pas de la configuration.

---

## Taches, regles, et ce que la passe a respecte

| Regle du brief | Statut |
|---|---|
| Aucun secret dans le depot V3 | OK — les secrets Paperclip (JWT, master.key) sont dans `~/.paperclip/instances/default/`, hors V3 |
| Rien a la racine de V3 | OK — tous les artefacts sont dans `00_Amadeus/20_Harness/` ou dans `.claude/skills/` (CC charge ces skills depuis le repo) |
| Aucune boucle autonome lancee | OK — aucun `paperclipai run`, aucun worker Buzz, aucun `multica agent create` qui aurait initie du travail. Le seul mutateur actif a ete `multica agent archive` (destruction reversible) |
| Verifier chaque configuration apres l'avoir posee | Partiel — T1 verifie par comptage post-archive ; T2 verifie par `pack validate` + `pack inspect` + test end-to-end du contrat uc.py ; T3 verifie par `paperclipai --version` + `which` + lecture seule de l'instance ; T4 verifie par `ls` + `dlq.py rapport` |
| Si un des 5 garde-fous n'est pas configurable : pas de boucle | OK — les 5 sont configurables (commandes existent, payloads JSON) mais pas configures. Le serveur n'est pas demarre |

## Inventaire des artefacts crees ou modifies par la passe

| Chemin | Nature | Contenu |
|---|---|---|
| `00_Amadeus/20_Harness/multica_export_2026-08-02/` | export | 11 fichiers JSON (~1 MB) + `tri.py` + `tri.csv` + `archive_inaction.py` |
| `00_Amadeus/20_Harness/paperclip/SECURITY_NOTES_2026-08-02.md` | doc | garde-fous, chemin d'activation, ce qui n'est pas verifie |
| `00_Amadeus/20_Harness/HARNESS_SETUP_2026-08-02.md` | doc | ce rapport |
| `C:/Users/amado/bin/buzz.cmd` | shim PATH | delegue a `Buzz/buzz.exe`, 1 ligne |
| `C:/Users/amado/.buzz/packs/aspace-life-core/` | pack | 4 personas + 1 skill + instructions + README |
| `C:/Users/amado/.hermes/skills/aspace-orchestrate/SKILL.md` | skill | orchestration meta pour Hermes |
| `C:/Users/amado/ASpace_OS_V3/.claude/skills/aspace-orchestrate/SKILL.md` | skill | orchestration meta pour CC (project-level) |
| `~/.paperclip/instances/default.bak-2026-08-02/` | sauvegarde | copie de l'instance avant install npm |
| `10_Tech_OS/kernel/uc.db` | etat | +1 work (le smoke test du contrat, `done`) |

## Decision requise de l'operateur

1. **Finir la refonte Multica** : archiver les 9 agents KEEP, creer les 14
   selon `ORG.json`, creer les 4 squads, creer la skill `adapter-uc-py`.
2. **Demarrer Paperclip** (apres verification explicite des 5 garde-fous).
3. **Importer le pack Buzz** dans Buzz Desktop (My Teams -> Import).
4. **Tester la skill `aspace-orchestrate`** dans une session CC et Hermes.
5. **Câbler DLQ V3 -> Paperclip** (garde-fou 4, piece manquante).

Tant que ces 5 ne sont pas faits, **les harnesses sont installes et
configures, mais aucun ne tourne en boucle**.
