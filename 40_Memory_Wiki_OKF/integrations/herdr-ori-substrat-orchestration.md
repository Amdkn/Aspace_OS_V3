---
type: Integration
title: Herdr et Ori — le substrat d'orchestration, mesuré
description: Herdr expose 25 événements runtime et un wait bloquant sur l'état d'un agent ; Ori est un agent déclaratif à features TypeScript qui tourne dans WSL et ne voit donc aucun harnais Windows.
tags: [herdr, ori, orchestration, runtime, events, mcp, skills, schedules, wsl]
generated: { by: claude-opus-5, at: 2026-08-28T18:40:00Z }
verified:
  - { by: claude-opus-5, at: 2026-08-28T18:40:00Z }
sources:
  - id: herdr-schema
    resource: "herdr api schema --json (244 913 octets)"
    title: Schéma de l'API socket Herdr 0.7.4-preview
    last_modified: 2026-08-28
  - id: ori-sdk
    resource: "/home/amdkn7/.ori/global/.ori/sdk/{index.ts,enums.ts} (WSL Ubuntu-24.04)"
    title: SDK de features Ori généré pour la version installée
    last_modified: 2026-08-28
  - id: ori-agents-md
    resource: "/home/amdkn7/.ori/global/AGENTS.md"
    title: Guide canonique du workspace Ori
    last_modified: 2026-08-23
okf_version: "0.2"
---

Deux outils que rien ne rattachait l'un à l'autre dans ce bundle, et qui
forment pourtant les deux moitiés d'un substrat d'orchestration : **Herdr
tient les terminaux et sait quand un agent a fini ; Ori tient les modèles et
sait lancer un agent.** Ce qui suit est mesuré le 2026-08-28, pas déduit.

## Herdr — un serveur, un socket, 25 événements

Version **0.7.4-preview**, binaire dans
`AppData/Local/Programs/Herdr/bin/herdr.exe`, config dans
`AppData/Roaming/herdr/config.toml`, socket dans le même dossier
(`herdr.sock`). Architecture client/serveur : `herdr server` tourne en
arrière-plan, le client s'y attache. `--no-session` est l'échappatoire
monolithique.

### Ce qui en fait un substrat d'orchestration

Ce n'est pas un multiplexeur de terminaux de plus. Trois primitives le
distinguent :

```bash
herdr agent start <name> [--cwd PATH] [--split right|down] [--env K=V] -- <argv...>
herdr agent wait <target> --status <idle|working|blocked|unknown> [--timeout MS]
herdr wait output <pane_id> --match <text> [--regex] [--timeout MS]
```

`agent wait` **bloque jusqu'à ce que l'agent change d'état**. C'est la
condition d'arrêt que toute boucle d'orchestration réclame et que le
`sleep` d'un script ne donne jamais correctement.

### Les 25 événements de runtime

Émis par le serveur, lisibles via l'API socket :

`workspace_created`, `workspace_updated`, `workspace_metadata_updated`,
`workspace_closed`, `workspace_renamed`, `workspace_moved`,
`workspace_focused`, `worktree_created`, `worktree_opened`,
`worktree_removed`, `tab_created`, `tab_closed`, `tab_renamed`,
`tab_moved`, `tab_focused`, `pane_created`, `pane_closed`, `pane_updated`,
`pane_focused`, `pane_moved`, `pane_output_changed`, `pane_exited`,
`pane_agent_detected`, `pane_agent_status_changed`, `layout_updated`.

**Trois seulement sont abonnables** (`events.subscribe`) :
`pane.output_matched`, `pane.agent_status_changed`, `pane.scroll_changed`.
Les autres se lisent, ne se souscrivent pas. Confondre les deux listes
fait écrire un abonnement qui ne se déclenchera jamais.

### Comment Herdr sait qu'un agent travaille

Deux mécanismes, et le second est plus fiable que le premier :

1. **Détection par regex sur le terminal.** Des manifestes TOML versionnés
   (`AppData/Local/herdr/agent-detection/remote/*.toml`, ~20 agents, mis à
   jour automatiquement) déclarent des règles priorisées qui scrutent le
   titre OSC et les dernières lignes non vides. Exemple réel pour Claude
   Code : `osc_title_working` (priorité 1100) matche les caractères braille
   ou demi-cercles du spinner ; `live_turn_working` (970) matche
   `esc to interrupt`. Chaque règle porte des clauses `not` pour éviter
   qu'un prompt utilisateur n'imite le signal.
2. **Hooks installés dans l'agent lui-même.**
   `herdr integration install claude` pose
   `~/.claude/hooks/herdr-agent-state.ps1`, qui rapporte l'état de façon
   autoritaire. 14 intégrations disponibles : `pi`, `omp`, `claude`,
   `codex`, `copilot`, `devin`, `droid`, `kimi`, `opencode`, `kilo`,
   `hermes`, `qodercli`, `cursor`, `mastracode`.

**Mesure du 2026-08-28 : aucune intégration n'est installée.** Herdr
fonctionne donc uniquement par regex. C'est le premier levier à actionner
avant de bâtir quoi que ce soit dessus.

### Plugins

Surface complète dans l'API : `plugin.link`, `plugin.unlink`,
`plugin.list`, `plugin.enable`, `plugin.disable`, `plugin.action.list`,
`plugin.action.invoke`, `plugin.pane.open`, `plugin.log.list`. Un manifeste
de plugin déclare des hooks `{ on: <event>, command: [...] }` — donc un
plugin peut réagir à un événement en lançant une commande.

## Ori — un agent déclaratif, pas un lanceur

`ori` n'est pas un binaire Windows : c'est un **wrapper `.cmd` vers WSL**
(`C:\Users\amado\bin\ori.cmd`), et tout son état vit dans
`/home/amdkn7/.ori/` côté Ubuntu-24.04.

### La conséquence qui coûte le plus cher

`ori harness list` ne voit qu'**un seul harnais installé** : `/usr/bin/claude`,
et annonce les sept autres (`codex`, `grok`, `opencode`, `hermes`, `omp`,
`prime-agent`, `dsh`) comme non installés.

**C'est faux, et la cause n'est pas celle qu'on croit.** Mesure du
2026-08-28 : `~/.local/bin/` contient déjà des installations Linux natives
de `codex` (→ `~/.codex/packages/standalone/current/bin/codex`), `dsh`
(→ `@deepseek-ai/dsh`) et `grok` (→ `~/.grok/bin/grok`). Rien ne manquait.

La cause racine est dans le lanceur Windows lui-même. `C:\Users\amado\bin\ori.cmd`
contenait :

```cmd
wsl.exe -d Ubuntu-24.04 -- /home/amdkn7/.local/bin/ori %*
```

`wsl -- <chemin>` démarre un shell **non-login et non-interactif** : ni
`.bashrc` ni `.profile` ne sont chargés, donc `~/.local/bin` n'est jamais
ajouté au PATH. Ori cherchait ses harnais dans un PATH qui ne contenait pas
le répertoire où il est lui-même installé.

C'est **exactement le même piège** que celui payé le 2026-08-27 sur les
scripts de rotation de clés, où `bash.exe` lancé avec un chemin de script en
argument ne trouvait plus `grep` ni `date`. Le symptôme diffère, le
mécanisme est identique : un shell non-login n'hérite d'aucun PATH enrichi.

Correctif appliqué (`ori.cmd` et `ori.ps1`, sauvegardes `.bak.*` à côté) :

```cmd
wsl.exe -d Ubuntu-24.04 -- sh -c 'export PATH="$HOME/.local/bin:$PATH"; exec "$HOME/.local/bin/ori" "$@"' ori %*
```

Le `ori` après le script fournit `$0`, `%*` devient `"$@"`.

**Résultat mesuré après correctif : 1 harnais visible sur 8 → 8 sur 8.**
`claude` (`/usr/bin/claude`), plus `codex`, `grok`, `opencode`, `hermes`,
`omp`, `prime-agent`, `dsh` — tous résolus dans `/home/amdkn7/.local/bin/`.

Conséquence à retenir : **`prime-agent` et `dsh` étaient déclarés
« introuvables » dans `coach-os-app/_runtime/bridge/harnesses.json`
(sondage du 2026-08-24), et ce sondage était fait côté Windows.** Ils
existent, en Linux, dans WSL. Une sonde ne mesure que le système d'où elle
part ; conclure « non installé » à partir d'un seul côté d'une frontière WSL
est une erreur de méthode, pas une donnée.

Deux pièges WSL connexes : la distro **par défaut** de ce poste est
`docker-desktop`, pas `Ubuntu-24.04` — tout appel `wsl` nu tombe à côté de
l'installation d'Ori ; et `wsl -l -v` peut afficher `Running` alors que le
service refuse toute connexion (`Wsl/Service/0x8007274c`), état qui exige un
`wsl --terminate Ubuntu-24.04`.

### Le workspace global est un dépôt Bun

`~/.ori/global/` : un `package.json`, un `bun.lock`, un `.git`, un
`AGENTS.md`, et un dossier `features/`. Le modèle d'extension est le
TypeScript, pas le fichier de config.

Contributions déclarables par une feature (types du SDK) :
`ApiContribution` (routes HTTP), `ChatContribution`, `CommandContribution`,
`AgentHarnessContribution`, `ProvisionsContribution`, `HooksContribution`.

Deux natures de hooks : `Hook<T>` diffusé (`BroadcastHookHandler`) et
`PipelineHook<T>` transformant (`PipelineHookHandler`). Les fichiers
`.ori/feature-hooks.d.ts` et `.ori/feature-apis.d.ts` sont **générés et
vides tant qu'aucune feature ne déclare rien** — ce sont des points
d'augmentation TypeScript, pas de la documentation.

### Les 35 événements de runtime d'Ori

`AgentRuntimeEventTag` dans `.ori/sdk/enums.ts`. Granularité bien plus fine
que Herdr, parce qu'Ori voit l'intérieur de la boucle d'agent :

- **Session** : `session.started`, `session.succeeded`, `session.failed`
- **Run / Turn** : `run.started`, `turn.started`, `turn.succeeded`, `turn.failed`
- **Item** : `item.started`, `item.updated`, `item.completed`
- **Outil** : `tool.started`, `tool.progress`, `tool.output.delta`,
  `tool.succeeded`, `tool.failed`, `tool.result.succeeded`, `tool.result.failed`
- **Flux** : `assistant.text.delta`, `content.delta`, `reasoning.delta`
- **Permission** : `permission.requested`, `permission.reason.delta`, `permission.resolved`
- **Élicitation** : `elicitation.requested`, `elicitation.resolved`
- **Compaction** : `compaction.started`, `compaction.completed`,
  `compaction.cancelled`, `compaction.failed`
- **Retry** : `retry.scheduled`, `retry.completed`, `retry.cancelled`, `retry.failed`
- **Erreur** : `runtime.error`, `runtime.warning`

**Partage des rôles** : Herdr voit *qu'un* agent travaille ; Ori voit *ce
que* l'agent fait. Les deux ne se remplacent pas.

### Routines = schedules, et elles n'arment pas toutes seules

Une routine Ori est un `feature.ts` exportant `defineSchedule({ cron, run | markdown })`.
Scaffoldé par `ori features new <name> --kind schedule --features <dir>`,
jamais écrit à la main.

Deux pièges documentés par la skill intégrée `schedule` :

- **L'export doit être nommé et unique.** `export const schedule = ...`.
  Un `export default ... satisfies FeatureModule` **fait échouer le
  chargement**, même posé à côté de l'export nommé.
- **Une routine ne s'arme jamais dans le tour qui l'écrit.** Il faut un
  démon en veille (`ori dev`, `ori start --watch`) qui applique le rechargement
  à une frontière de run. Le champ qui fait foi est `armed` dans
  `ori schedules` — un cron et une prochaine échéance affichés ne prouvent
  rien. `ori schedules trigger <name>` déclenche à la demande.

Portée globale = `~/.ori/global/features` (tout projet) ; portée dépôt =
`./features` (seulement sous `ori dev` dans ce dépôt).

### Skills — Ori fait le pont WSL vers Windows

Six skills intégrées : `adding-mcp-servers`, `code-review`, `create-eval`,
`inspect-logs`, `schedule`, `writing-tests`.

Mais surtout, `materialized-skills.json` montre qu'Ori **matérialise aussi
les skills du côté Windows** en les lisant depuis `/mnt/c/` :
`composio`, `find-skills`, `orchestration`, `unlazy`, `scroll-film-studio`,
`scroll-world`, `seed-dance` — captées depuis
`C:\Users\amado\.agents\skills\` et `C:\Users\amado\.claude\skills\`.

Convention d'écriture : skill racine à
`<feature-root>/<feature-id>/SKILL.md`, skills imbriquées à
`<feature-root>/<feature-id>/skills/<nom>/SKILL.md`. **Ne jamais éditer
`.agents/skills` ni `.claude/skills`** : ce sont des vues snapshot
régénérées.

### MCP

`ori mcp list` / `ori mcp test` lisent un `mcp.json` **à la racine du
workspace**, ou le chemin pointé par `ORI_MCP_CONFIG`.

**Mesure du 2026-08-28 : aucun `mcp.json` n'existe.** Ori a donc zéro
serveur MCP configuré, indépendamment des 17 sources de l'agentgateway —
voir [[composio-mcp-as-gateway]]. Les deux canaux sont disjoints.

## Le piège du CLI contextuel

`ori --help` exécuté depuis `C:\Users\amado` **ne liste pas** `code`, `dev`,
`schedules`, `features`, `logs`, `start`. Les six existent pourtant et
répondent — vérifié un par un depuis `~/.ori/global`. La liste des
sous-commandes dépend de la présence d'un workspace dans le répertoire
courant.

Conséquence : **conclure « la commande n'existe pas » depuis le help est
faux.** Il faut la tester depuis un workspace. Corollaire mesuré le même
jour : `ori-help` et `ori-doctor` (avec un tiret) n'existent pas ; ce sont
`ori help` et `ori harness-doctor`.

## Comment vérifier que ça marche

```bash
herdr agent list            # doit lister le pane et son agent_status
herdr integration status    # dit quels hooks sont poses
cmd /c "ori auth"           # authenticated: true + source du credential
cmd /c "ori harness list"   # ce qu'Ori voit REELLEMENT, pas ce qu'on croit
```

## Comment le retirer

Herdr : `herdr server stop`, puis
`herdr integration uninstall <agent>` pour chaque hook posé. Le binaire
vit dans `~/.herdr/packages/standalone/releases/`.
Ori : `ori workspace reset` archive le workspace global et le reconstruit
depuis le gabarit — c'est réversible, l'archive est conservée.
