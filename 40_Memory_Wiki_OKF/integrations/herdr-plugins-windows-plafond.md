---
type: Integration
title: Plugins Herdr — 866 au catalogue, 13 utilisables sous Windows
description: Le marketplace Herdr compte 866 plugins, mais les manifestes déclarent presque tous platforms = ["linux","macos"] ; sur 36 manifestes lus, 13 supportent Windows, et aucun des dix plus populaires.
tags: [herdr, plugins, windows, wsl, marketplace, compatibilite, orchestration]
generated: { by: claude-opus-5, at: 2026-08-29T01:05:00Z }
verified:
  - { by: claude-opus-5, at: 2026-08-29T01:05:00Z }
sources:
  - id: herdr-dev-plugins
    resource: "https://herdr.dev/plugins/"
    title: Marketplace Herdr — index communautaire
    last_modified: 2026-08-29
  - id: github-topic
    resource: "GET api.github.com/search/repositories?q=topic:herdr-plugin&sort=stars"
    title: Source réelle de l'index — 886 dépôts portant le topic
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
