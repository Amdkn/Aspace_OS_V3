---
type: Integration
title: Herdr et Ori — le substrat d'orchestration, mesuré
description: Herdr expose 25 événements runtime et un wait bloquant sur l'état d'un agent ; Ori est un pont OpenRouter natif dont la config vivait aux valeurs de scaffolding — mcp.json absent, persona par défaut. Audité et corrigé le 2026-08-29.
tags: [herdr, ori, orchestration, runtime, events, mcp, skills, schedules, wsl, openrouter, config, audit]
generated: { by: claude-opus-5, at: 2026-08-28T18:40:00Z }
verified:
  - { by: claude-opus-5, at: 2026-08-28T18:40:00Z }
  - { by: claude-opus-5, at: 2026-08-29T00:36:00Z }
sources:
  - id: herdr-schema
    resource: "herdr api schema --json (244 913 octets)"
    title: Schéma de l'API socket Herdr 0.7.4-preview
    last_modified: 2026-08-28
  - id: ori-sdk
    resource: "/home/amdkn7/.ori/global/.ori/sdk/{index.ts,enums.ts} (WSL Ubuntu-24.04)"
    title: SDK de features Ori généré pour la version installée
    last_modified: 2026-08-28
  - id: herdr-config-template
    resource: "Gabarit de config commente embarque dans herdr.exe 0.7.4-preview"
    title: Reference des options de config.toml (aucune doc sur disque)
    last_modified: 2026-08-29
  - id: ori-mcp-skill
    resource: "~/.ori/global/.ori/snapshot/*/adding-mcp-servers/SKILL.md (WSL)"
    title: Skill integree Ori — connecter un serveur MCP
    last_modified: 2026-08-29
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

Aucune intégration n'était installée au 2026-08-28 ; Herdr ne fonctionnait
alors que par regex. **État au 2026-08-29 : `claude` (v7) et `codex` (v6) sont
installées** — vérifié par `herdr integration status`. Les quatre autres
proposées (`copilot`, `droid`, `kimi`, `qodercli`) restent absentes, et c'est
correct : les agents correspondants ne sont pas sur ce poste.

Conséquence : `[session] resume_agents_on_restore` devient réellement effectif,
puisqu'il exige des intégrations rapportant une référence de session.

### Plugins

Surface complète dans l'API : `plugin.link`, `plugin.unlink`,
`plugin.list`, `plugin.enable`, `plugin.disable`, `plugin.action.list`,
`plugin.action.invoke`, `plugin.pane.open`, `plugin.log.list`. Un manifeste
de plugin déclare des hooks `{ on: <event>, command: [...] }` — donc un
plugin peut réagir à un événement en lançant une commande.

### La config, et où se trouve sa documentation

**Il n'y a aucun fichier de doc dans l'installation de Herdr.** La référence
des options de `config.toml` est un **gabarit commenté embarqué dans
`herdr.exe`** : il documente chaque clé et, par ses lignes commentées, la
valeur par défaut. On l'extrait en lisant les chaînes du binaire autour de
`# Background notification popup delivery`.

Sections : `[ui]` (19 clés), `[ui.sidebar.agents]`, `[ui.sidebar.spaces]`,
`[ui.toast]`, `[ui.toast.herdr]`, `[ui.toast.clipboard]`, `[ui.sound]`,
`[ui.sound.agents]`, `[keys]`, `[[keys.command]]`, `[worktrees]`, `[session]`,
`[remote]`, `[experimental]`.

Audit du 2026-08-29 : la config faisait 97 octets, quatre réglages. **La
plupart des défauts étaient déjà les bons** — `confirm_close`,
`[ui.sound] enabled`, `resume_agents_on_restore` sont à `true` par défaut.
C'est un résultat d'audit, pas un échec : recopier des défauts dans un fichier
de config fait passer une copie pour un choix délibéré.

Trois changements retenus, tous porteurs :

| Clé | Avant | Après | Pourquoi |
|---|---|---|---|
| `ui.agent_panel_sort` | `spaces` (défaut) | `priority` | Avec plusieurs agents en vol, la question est « lequel me réclame », pas « où vit-il » |
| `ui.toast.delivery` | `herdr` | `system` | Un toast `herdr` ne s'affiche que **dans** Herdr : pendant un batch délégué, il arrive dans une fenêtre qu'on ne regarde pas |
| `session.resume_agents_on_restore` | implicite | explicite `true` | Ne devient effectif qu'avec les intégrations, installées depuis peu |

`herdr config check` valide, `herdr server reload-config` applique **à chaud** —
`status: applied`, zéro diagnostic, sans redémarrer le serveur.

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

**Le même piège frappe Hermes, et coûte une clé.** Hermes existe des deux
côtés : `~/.hermes/` dans WSL et `AppData\Local\hermes\` sous Windows. Les deux
états sont **indépendants**. Côté WSL, `auth.json` ne garde qu'une empreinte
(`secret_fingerprint`) et pointe vers une variable d'environnement vide ; la
clé OpenRouter vivante était dans le `.env` **Windows**. Chercher d'un seul
côté conclut à tort qu'elle n'existe plus — détail dans
[[relais-openrouter-modeles-custom]].

Deux pièges WSL connexes : la distro **par défaut** de ce poste est
`docker-desktop`, pas `Ubuntu-24.04` — tout appel `wsl` nu tombe à côté de
l'installation d'Ori ; et `wsl -l -v` peut afficher `Running` alors que le
service refuse toute connexion (`Wsl/Service/0x8007274c`), état qui exige un
`wsl --terminate Ubuntu-24.04`.

### Ori est un pont OpenRouter natif — il double le relais maison

Mesure du 2026-08-29, et c'est le constat qui porte le plus loin :
**`ori` est bâti sur OpenRouter de bout en bout.** `ori login` ne connaît que
lui, et chaque sous-commande de lancement est décrite comme « Launch X with
Ori's OpenRouter environment » : `ori claude`, `ori codex`, `ori grok`,
`ori opencode`, `ori hermes`, `ori omp`, `ori dsh`, `ori prime-agent`.

```bash
ori claude --model z-ai/glm-5.3-flash -- -p "Reponds exactement: PONG"
# -> PONG
```

`--model` accepte **n'importe quel identifiant de modèle OpenRouter**, et le
lancement passe la validation locale de Claude Code sans relais. C'est
exactement le service que rend [[relais-openrouter-modeles-custom]], mais
natif, supporté, sans port ni gardien.

**Les deux ne se remplacent pas pour autant** : `ori claude` lance le Claude
Code **de WSL** (`/usr/bin/claude`), le relais sert celui de **Windows**. Pour
un batch délégué, `ori claude` est strictement supérieur — rien à maintenir.
Pour une session Windows, le relais reste la seule voie.

### La persona par défaut contredisait le canon du poste

`~/.ori/global/ori.md` était le gabarit de scaffolding, jamais touché :

```yaml
model: ~anthropic/claude-opus-latest
```
> I'm an intern! I'm concise, prefer small reviewable changes, and I ask
> before taking risky actions.

Deux défauts, et le premier n'est pas celui qu'on croit. **`~anthropic/…` ne
consomme pas le quota Anthropic** : tout passe par OpenRouter, donc c'est du
crédit, pas du quota. L'enjeu est le coût, pas la rareté — Opus pour un
« intern » qui fait de petites tâches est un choix cher par défaut, pas un
choix fait.

Le second est plus grave : « I ask before taking risky actions » est
l'exact inverse de la consigne tenue sur ce poste, où un prompt de confirmation
entre deux étapes est de la dette. Une persona de scaffolding qu'on ne relit
pas gouverne l'agent en silence.

Réécrite le 2026-08-29 (sauvegarde `ori.md.bak.*` à côté) : modèle
`z-ai/glm-5.3-flash`, et une persona qui exécute au lieu de demander, vérifie
au lieu de croire, et déclare ce qu'elle n'a pas fait. Mesuré : **0,000243 $
le tour** contre plusieurs cents avec Opus.

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

### MCP — câblé le 2026-08-29

`ori mcp list` / `ori mcp test` lisent un `mcp.json` **à la racine du
workspace**, ou le chemin pointé par `ORI_MCP_CONFIG`.

Aucun `mcp.json` n'existait au 2026-08-28 : Ori avait zéro serveur MCP,
indépendamment des 17 sources de l'agentgateway — voir
[[composio-mcp-as-gateway]]. Les deux canaux restent disjoints.

État au 2026-08-29 : `~/.ori/global/mcp.json` déclare **context7** (2 outils)
et **composio** (7 outils), tous deux `connected`.

**Ori refuse les serveurs `stdio`.** Un serveur déclaré en stdio ressort
`skipped — stdio bypasses the vault: the proxy variables are never passed to
the child, and its env is never substituted`. C'est un choix du modèle de
sécurité d'Ori, pas une panne — et la skill `adding-mcp-servers` donne pourtant
un exemple stdio en premier. **Tout serveur utile à Ori doit être `type:
"http"`.**

**`ORI_MCP_CONFIG` est indispensable, pas optionnel.** Ori cherche `mcp.json`
dans le **répertoire courant** — « never a home-level config », dit la skill.
Lancé depuis un projet quelconque, il ne voit donc aucun serveur. La variable
est posée dans `~/.ori/ori-env.sh`, sourcé par le wrapper (ci-dessous).

Les secrets restent hors fichier : `mcp.json` ne porte que
`"x-consumer-api-key": "${COMPOSIO_CONSUMER_KEY}"`, et `ori-env.sh` relit la
valeur à chaud depuis `settings.json`. Aucune copie nouvelle sur le disque.

### Le wrapper doit aussi porter l'environnement

Le correctif de PATH de `ori.cmd` ne suffisait pas : un shell non-login ne
fournit **aucune** variable, donc `${COMPOSIO_CONSUMER_KEY}` et
`ORI_MCP_CONFIG` manquaient tous deux. Poser l'export dans `~/.bashrc` ne sert
à rien — il n'est pas lu. D'où `~/.ori/ori-env.sh`, sourcé par le wrapper.

**Ne jamais écrire `&&` ni `||` dans la chaîne passée à `sh -c` depuis un
`.cmd`.** Les guillemets simples sont une notion de shell POSIX ; **cmd.exe les
ignore** et voit ses propres opérateurs, donc il coupe la commande en deux et
WSL reçoit une chaîne non terminée :

```
/bin/bash: -c: line 1: unexpected EOF while looking for matching `'
```

Utiliser `if … ; then … ; fi`, sans métacaractère cmd. Payé le 2026-08-29.

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
herdr config check          # doit rendre "config: ok"
```

Pour Ori, **passer par un `.bat`**, pas par `cmd /c "ori …"` depuis bash : la
double couche de citation casse la chaîne avant WSL, et `cmd /c` rend parfois
la seule bannière de cmd sans rien exécuter.

```bat
call "C:\Users\amado\bin\ori.cmd" harness list
call "C:\Users\amado\bin\ori.cmd" mcp list --human
```

`harness list` rend **deux listes** qu'il ne faut pas confondre :
`data.harnesses` (features enregistrées — 1, le runloop intégré) et
`data.launchable` (CLI externes lançables — 8/8 installés). Lire la première
en croyant lire la seconde fait conclure à tort que sept harnais ont disparu.

## Comment le retirer

Herdr : `herdr server stop`, puis
`herdr integration uninstall <agent>` pour chaque hook posé. Le binaire
vit dans `~/.herdr/packages/standalone/releases/`.
Ori : `ori workspace reset` archive le workspace global et le reconstruit
depuis le gabarit — c'est réversible, l'archive est conservée.
