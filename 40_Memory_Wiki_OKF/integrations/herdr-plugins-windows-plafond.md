---
type: Integration
title: Plugins Herdr — 866 au catalogue, deux plafonds cumulés sous Windows
description: 866 plugins au catalogue ; sur 36 manifestes lus, 13 déclarent windows et aucun des dix plus populaires. Deux plafonds se cumulent — plateforme et min_herdr_version — et un plugin installé peut n'être qu'une couche sur un binaire absent.
tags: [herdr, plugins, windows, wsl, marketplace, compatibilite, orchestration, llmtrim, securite]
generated: { by: claude-opus-5, at: 2026-08-29T01:05:00Z }
verified:
  - { by: human:amdkn, at: 2026-08-31T21:33:21Z }
  - { by: claude-opus-5, at: 2026-08-29T01:05:00Z }
  - { by: claude-opus-5, at: 2026-08-29T01:30:00Z }
sources:
  - id: herdr-dev-plugins
    resource: "https://herdr.dev/plugins/"
    title: Marketplace Herdr — index communautaire
    last_modified: 2026-08-29
  - id: github-topic
    resource: "GET api.github.com/search/repositories?q=topic:herdr-plugin&sort=stars"
    title: Source réelle de l'index — 886 dépôts portant le topic
    last_modified: 2026-08-29
  - id: update-082
    resource: "herdr update sur le poste — 0.7.4-preview vers 0.8.2-preview"
    title: Mise a jour du 2026-08-29 et etat des integrations apres coup
    last_modified: 2026-08-29
  - id: manifestes
    resource: "36 fichiers herdr-plugin.toml lus en raw.githubusercontent"
    title: Clause platforms déclarée par chaque plugin
    last_modified: 2026-08-29
okf_version: "0.2"
---

Le marketplace annonce **866 plugins sur 851 dépôts**. Le chiffre est réel et
trompeur : sous Windows, la quasi-totalité ne s'installe pas.

## L'index n'est pas une base, c'est un topic GitHub

`herdr.dev/plugins` est une vue sur les dépôts publics portant le topic
`herdr-plugin` et un manifeste `herdr-plugin.toml`. Pas de revue, pas de file
de soumission — le site le dit lui-même : *« Listings aren't reviewed by
Herdr, so install at your own discretion. »*

Conséquence pratique : **interroger l'API GitHub est plus rentable que de
cliquer la page**, qui pagine en JavaScript.

```bash
curl -s "https://api.github.com/search/repositories?q=topic:herdr-plugin&sort=stars&order=desc&per_page=60"
```

886 dépôts au 2026-08-29 — l'index du site en affiche 866, l'écart étant le
délai de rafraîchissement.

## Le plafond Windows, mesuré

La compatibilité se lit dans la clause `platforms` du manifeste :

```bash
curl -s "https://raw.githubusercontent.com/<owner>/<repo>/main/herdr-plugin.toml" \
  | grep -oiE 'platforms *= *\[[^]]*\]'
```

**Sur 36 manifestes lus, 13 déclarent `windows`.** Et surtout : **aucun des
dix plus populaires** ne le fait. Les plugins les plus étoilés — `herdr-reviewr`
(560★), `memex` (171★), `herdr-agent-quota`, `herdr-agent-usage`,
`herdr-navigator`, `herdr-spreader`, `herdmates`, `collie`,
`herdr-mobile-relay` — sont tous `["linux","macos"]`.

Ceux qui comptent le plus pour un poste d'orchestration sont précisément ceux
qui manquent : la surveillance de quota (`herdr-agent-quota`,
`herdr-agent-usage`) et la revue de diff d'agent (`herdr-reviewr`).

### Les 13 qui passent sous Windows

| Plugin | ★ | Ce qu'il fait | Réserve |
|---|---|---|---|
| `smarzban/herdr-file-viewer` | 494 | Visionneuse de fichiers git-aware | Windows en **preview** |
| `dcolinmorgan/herdr-remote` | 296 | Piloter ses agents depuis la barre de menu, le téléphone ou Telegram | — |
| `cloudmanic/herdr-plus` | 270 | Projets et actions rapides | — |
| `plannotator/herdr-annotate` | 184 | Annoter le terminal et renvoyer en contexte d'agent | — |
| `jhochenbaum/herdr-hunk-diff` | 98 | Revoir les diffs d'agent par hunk, commenter en retour | — |
| `iurysza/herdr-tab-smart-rename` | 67 | Nommer tabs et workspaces selon le contexte | — |
| `aigorahub/herdr-lantern` | 49 | Qui a besoin de vous, et vers quoi il travaille | — |
| `aemrebarut/herdr-dagr` | 46 | L'essaim d'agents en DAG vivant, avec portes de revue | Le manifeste note que **Herdr preview ne lance pas d'exécutable relatif au plugin sous Windows** |
| `fkiene/llmtrim-herdr` | 40 | Compresse les requêtes de chaque pane (−31 % entrée, −74 % sortie annoncés) | Chaque action a un jumeau PowerShell — conçu multi-plateforme |
| `madarco/agentbox-herdr-plugin` | 28 | Agents en parallèle dans des VM isolées | — |
| `ntindle/herdr-resurrect` | 23 | Snapshot/restauration de workspaces, façon tmux-resurrect | Une entrée du manifeste reste `linux/macos` |
| `natori-hrj/herdr-lazy` | 22 | Gestionnaire de plugins déclaratif avec vrai lockfile | **Aucun binaire précompilé sous Windows** — compile depuis les sources |
| `liamwh/herdr-rich-notifications` | 0 | Notifications natives sur changement d'état d'agent | Publié depuis quelques heures, non éprouvé |

## Levée du plafond : 0.7.4 → 0.8.2 (2026-08-29)

`herdr update` a porté le poste de `0.7.4-preview.2026-07-17` à
`0.8.2-preview.2026-08-19`. Trois effets mesurés, dont un inattendu.

**1. Le plafond de version tombe.** `herdr-hunk-diff` et `herdr-annotate`
s'installent. Quatre plugins actifs : `annotate`, `herdr-remote.relay`,
`jhochenbaum.hunkdiff`, `llmtrim.proxy`.

**2. Les intégrations doivent être réinstallées** — le binaire le dit lui-même
après la mise à jour. `claude` et `codex` passent de v7/v6 à **v8**.

**3. Hermes devient supporté sous Windows.** En 0.7.4, `herdr integration
install hermes` rendait `hermes integration is not supported on Windows` ;
en 0.8.2 il pose un plugin Python dans
`AppData\Local\hermes\plugins\herdr-agent-state\` et l'active dans
`hermes/config.yaml`. **Hermes passe de la détection par regex à un hook
autoritaire (v5).**

Le catalogue d'intégrations s'élargit aussi : `pi`, `omp`, `devin`, `qwen`,
`grok`, `antigravity-cli` apparaissent dans `integration status`, absents en
0.7.4.

**Leçon** : « non supporté sous Windows » est une réponse *datée*, pas une
propriété. Sur un canal preview vieux de six semaines, revérifier après mise à
jour avant de conclure qu'une capacité manque.

Les trois harnais Windows du poste sont désormais tous en hook autoritaire :

```
claude: current (v8)   codex: current (v8)   hermes: current (v5)
```

**Vérifier les dépendances déclarées par les hooks**, sans quoi un plugin
installé reste inerte. Les quatre en place réclament `node`, `bun`, `uv` et
`pwsh` — tous présents ici, mais aucun n'est garanti par l'installation du
plugin.

**`plugin action list` exige un serveur vivant.** Et le démarrer avec
`resume_agents_on_restore = true` **relance les panes d'agents** — ne pas le
faire si l'utilisateur vient de les fermer.

### Vérification complète, serveur relancé le 2026-08-29

`herdr server` (headless), puis :

- Serveur `running`, protocole 20, `compatible: yes`.
- **Les hooks tirent vraiment**, `exit_code: 0` : `llmtrim.proxy` →
  `pwsh bin/check-routing.ps1` sur `pane.agent_detected` (c'est bien le
  **jumeau PowerShell** qui s'exécute), `herdr-remote.relay` →
  `uv run --script relay/on_event.py`, `jhochenbaum.hunkdiff` →
  `node dist/bin/event.js`, les deux derniers sur `pane.agent_status_changed`.
- `annotate` ne déclare **aucun hook d'événement** — journal vide, ce qui est
  normal, pas une panne. Il expose 3 actions.
- **25 actions, dont 20 utilisables sous Windows.** `hunkdiff` en fournit 12,
  dont `send-review` (renvoyer la revue à l'agent) : la boucle de vérification
  recherchée.
- `resume_agents_on_restore = true` **est prouvé** : un pane `claude` a été
  repris au démarrage du serveur.
- `llmtrim diagnose` rend `exit 1` — ce n'est **pas** un échec du plugin mais
  `llmtrim doctor` qui compte ses étapes de configuration en attente. La chaîne
  plugin → binaire est établie (`binary ✓ v0.13.2`), contre
  `program not found` avant l'installation du CLI.

**Un serveur démarré depuis le shell d'un agent lui est rattaché** : le
processus a pour parent `bash.exe`. Il meurt avec ce shell. Pour un serveur
durable, le lancer depuis son propre terminal — même famille de piège que le
relais et le gardien WSL.

## Le second plafond : la version, pas la plateforme

Déclarer `windows` ne suffit pas. Chaque manifeste porte aussi un
`min_herdr_version`, et le poste est en **0.7.4** :

```
Error: plugin requires Herdr 0.8.0 or newer; current Herdr is 0.7.4
```

`herdr-hunk-diff` et `herdr-annotate` sont refusés par ce seul motif, alors
qu'ils déclarent bien `windows`. `herdr-remote` et `llmtrim-herdr`
(`min_herdr_version = 0.7.0`) passent. **Deux plafonds indépendants se
cumulent** : la plateforme et la version. Vérifier les deux avant de conclure
qu'un plugin est incompatible.

## « Installé » ne veut pas dire « fonctionne »

Mesure du 2026-08-29 sur `llmtrim.proxy`, installé et `enabled` :

```
statut: failed | erreur: program not found
```

Le plugin n'est qu'une **couche d'intégration** : il appelle un binaire
`llmtrim` qui s'installe séparément (`npm install -g @llmtrim/cli`). Un plugin
peut donc être installé, activé, exposer ses actions, et ne rien faire.

Le geste qui tranche :

```bash
herdr plugin action invoke <action_id> --plugin <plugin_id>
herdr plugin log list --limit 5      # status, error, stdout du dernier appel
```

Attention à la syntaxe : c'est `invoke <action_id> --plugin <id>`, pas
`invoke <plugin> <action>` — cette dernière rend `unknown option`.

Les actions portent chacune leur propre clause `platforms`, avec des **jumeaux
Windows en `pwsh`** (`open-dashboard` / `open-dashboard-win`). Le listing
paraît dupliqué ; il ne l'est pas.

## Ce que llmtrim est réellement — à décider en connaissance de cause

Les « −31 % / −74 % » annoncés ne viennent pas d'un réglage. `llmtrim doctor`
le dit sans détour : c'est un **intercepteur HTTPS**.

`llmtrim setup` « sets HTTPS_PROXY + CA trust in your environment (shell
profile on POSIX, **HKCU\Environment** on Windows), enables run-at-login,
wires Claude Code integrations (statusline, guard, /sub, compact), and starts
the interceptor ».

Trois conséquences à peser :

1. **Il installe une autorité de certification** pour déchiffrer le trafic.
   Mitigation réelle : la CA est *name-constrained* aux domaines d'API LLM, donc
   elle ne peut pas signer pour un site quelconque.
2. **Il écrit dans `HKCU\Environment`** — exactement le mécanisme qui, sur ce
   poste, écrase les exports de shell. Toute variable posée là gagne contre un
   `export` de session.
3. **Il modifie la configuration de Claude Code** (statusline, guard, `/sub`,
   compact), un fichier déjà réécrit en fin de session.

Rien de tout cela n'a été exécuté : poser une CA racine et des variables
d'environnement persistantes est une décision du propriétaire du poste, pas
d'un agent.

## La réserve qui vise le canal, pas le plugin

Le manifeste de `herdr-dagr` porte cette phrase :

> On Windows, where Herdr preview cannot launch plugin-relative executables…

Le poste est sur le canal **preview** (`0.7.4-preview.2026-07-17`). Tout plugin
Windows livrant un exécutable dans son propre dossier est donc suspect **par le
canal, pas par le plugin**. À vérifier avant d'accuser un plugin de ne pas
marcher.

## Ce que ça implique pour l'architecture du poste

L'écosystème de plugins vit **du côté Linux**. Un poste qui fait tourner ses
agents sous Windows via Herdr y accède à peine. Deux voies, et elles ne
s'excluent pas :

- **Rester sous Windows** et se limiter aux 13 ci-dessus — suffisant pour la
  revue de diff, les notifications et le nommage, insuffisant pour la
  surveillance de quota.
- **Faire tourner un second serveur Herdr dans WSL** (build Linux). Le
  catalogue s'ouvre en entier, et c'est l'environnement Linux de répétition
  avant mise en production. Mesure du 2026-08-29 : **aucun Herdr n'est
  installé dans WSL** (`command -v herdr` → absent), alors qu'Ori y lance
  déjà 8 harnais — voir [[herdr-ori-substrat-orchestration]].

## Avant d'installer quoi que ce soit

Rien n'est relu par Herdr. Un plugin déclare des hooks
`{ on: <event>, command: [...] }` : **installer un plugin, c'est accepter qu'un
dépôt tiers exécute des commandes à chaque événement de l'espace de travail.**
Le nombre d'étoiles ne dit rien de ce que fait le code.

Lire le manifeste avant d'installer, pas après :

```bash
curl -s "https://raw.githubusercontent.com/<owner>/<repo>/main/herdr-plugin.toml"
```

## Comment vérifier

```bash
herdr plugin list --json     # ce qui est reellement installe
herdr plugin log list        # ce que les plugins ont fait
herdr channel show           # preview ou stable — determine la reserve ci-dessus
```

## Comment retirer

`herdr plugin uninstall <plugin_id|owner/repo>`, ou `herdr plugin disable` pour
neutraliser sans désinstaller.
