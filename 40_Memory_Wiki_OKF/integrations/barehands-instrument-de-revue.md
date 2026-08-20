---
type: Integration
title: barehands — piloter le tableau à la main, sans forker (AGPL)
description: Analyse du dépôt jaredrhod/barehands. Sa licence AGPL interdit de le fondre dans Coach OS, mais son protocole HTTP le rend pilotable sans le modifier — ce qui en fait l'instrument de revue humaine qui manquait.
tags: [barehands, airglass, jarvis, revue, agpl, mediapipe, three-js, jumeau-numerique, okf, confiance]
generated: { by: claude-opus-5, at: 2026-08-19T10:00:00Z }
verified:
  - { by: process:github-mcp-lecture-directe, at: 2026-08-19T09:50:00Z }
sources:
  - id: readme
    resource: "https://github.com/jaredrhod/barehands/blob/main/README.md"
    title: "barehands — README (lu intégralement)"
    last_modified: 2026-08-19
  - id: serveur
    resource: "https://github.com/jaredrhod/barehands/blob/main/server.py"
    title: "server.py — 13 Ko, stdlib Python, lu intégralement"
    last_modified: 2026-08-19
  - id: config
    resource: "https://github.com/jaredrhod/barehands/blob/main/barehands.json.example"
    title: "barehands.json.example"
    last_modified: 2026-08-19
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Le protocole serveur et la
> licence sont lus dans le code, pas déduits. **Les gestes ne le sont pas** :
> `stage.html` fait 155 Ko et n'a pas été lu. Tout ce qui est dit ici des
> pincements, de la griffe et du claquement de mains vient du README — c'est-à-dire
> de l'auteur, pas d'une mesure.

# Ce que c'est, exactement

Trois fichiers utiles, aucune dépendance à installer :

| | |
|---|---|
| `server.py` | 13 Ko, **stdlib Python seule**. Sert `stage.html`, arbitre le média. |
| `stage.html` | **155 Ko, fichier unique**. Toute l'app. Pas de `package.json`, pas de build. |
| `barehands.json` | Le nom de l'assistant, le port, et la liste des « orbes ». |

Le suivi de main est **MediaPipe** (Google, Apache 2.0), le rendu 3D est
**three.js** (MIT) ; les deux se chargent depuis des CDN publics au premier
lancement. Le dépôt n'en redistribue aucun.

Ça tourne sur `127.0.0.1:8794`, dans Chrome, avec une webcam. `localhost` est
un contexte sécurisé — c'est précisément ce qui autorise le navigateur à
ouvrir la caméra sans HTTPS.

# La contrainte qui décide de tout : AGPL-3.0-or-later

**C'est la première chose à savoir, et elle n'est pas négociable par
préférence.**

L'AGPL dit : si vous faites tourner une version *modifiée* comme un service
que d'autres utilisent, votre version part sous la même licence, sources
ouvertes. Coach OS est un SaaS commercial. **Fondre du code barehands dans
Coach OS obligerait à ouvrir Coach OS.**

L'auteur propose une licence commerciale fermée par courriel
(`license@jaredrhod.com`). C'est une option, pas une nécessité — voir ci-dessous.

## Pourquoi ce n'est pourtant pas un obstacle

**Parce qu'il ne faut pas le forker. Il faut le piloter.**

barehands expose un protocole HTTP et un protocole de fichiers. Un programme
séparé qui parle à ce protocole, par-dessus une frontière de processus, n'est
pas une œuvre dérivée. C'est la frontière AGPL standard, et elle est ici
particulièrement nette puisque l'auteur *conçoit* explicitement son outil pour
être piloté de l'extérieur : « n'importe quoi qui écrit un fichier ou curl
localhost peut être le cerveau ».

**Règle à tenir : barehands tourne non modifié, dans son propre processus.
Notre code ne fait qu'écrire des fichiers et poster du JSON.**

# Le protocole, lu dans `server.py`

## Le cerveau parle au tableau

`POST /cmd` avec un JSON `{"a": "<verbe>", ...}`. La liste blanche est en dur :

```
add_img · add_card · clear · reset · hand · give · yank ·
hover · scroll_note · widget · explode · assemble · present
```

`present` est le verbe « montre-moi » : l'objet vole au centre, agrandi et
éclairé, tout le reste s'assombrit.

`bin/board.sh` et `bin/board-state.sh` enrobent ça en ligne de commande.

## Le tableau répond

`GET /state` rend la scène courante — ce qui est affiché. C'est ce qui permet
à un agent de **regarder avant de parler** au lieu d'affirmer à l'aveugle.

## L'anneau est un visage

Trois fichiers minuscules dans `state/`, lus par `GET /orb` :

| fichier | contenu |
|---|---|
| `state/state` | un mot : `idle` \| `listening` \| `thinking` \| `speaking` |
| `state/mood.json` | `{"mood": "green"\|"amber"\|"red", "ts": …}` — **périmé après 45 s** |
| `state/wave.json` | `{"samples": [0..1 ×64], "ts": …}` — **périmé après 0,6 s** |

Toute lecture échoue en douceur : pas de fichier, pas de problème, l'anneau
respire. Les horodatages ne sont pas décoratifs — un `mood` de plus de 45
secondes est ignoré, ce qui empêche un état mort de mentir indéfiniment.

## Les orbes sont des dossiers de markdown

```json
{ "title": "Notes", "path": "~/n_importe_quel_dossier", "kind": "notes" }
```

`GET /tree?orb=N` rend l'arborescence, `GET /note?f=N/<rel>` rend un fichier.
**Les deux sont en lecture seule, `.md` uniquement, et emprisonnés** dans le
dossier configuré : `root not in target.parents` → 404. `CLAUDE.md` est exclu
explicitement, l'auteur le considérant comme de la configuration d'agent, pas
comme une note.

Les images et modèles 3D passent par un **sas** : seul ce qui est réellement
sous `./media/` peut s'afficher. Une évasion rend 400. Un joli détail : si le
chemin exact rate mais qu'un *unique* fichier du même nom existe ailleurs dans
le sas, il se répare tout seul ; zéro ou plusieurs correspondances, 400.

# Ce que ça vaut pour nous, précisément

## Le raccord qui n'était pas prévu pour nous et qui tombe juste

Un orbe « notes » pointe vers **n'importe quel dossier de markdown**.

`40_Memory_Wiki_OKF/` est un dossier de markdown.
`_REVIEW_NOTEBOOKLM/` est un dossier de markdown.

Il n'y a **rien à écrire** pour que le corpus apparaisse sur le tableau. Une
ligne de configuration.

## Pourquoi c'est l'instrument de revue, et pas un gadget

Le goulot documenté dans [[notebooklm-revue-humaine]] est la vérification :
321 concepts, tous en `confiance: machine`, aucun relu.

NotebookLM résout la **sortie** — un podcast s'écoute en marchant. Il ne
résout pas l'**entrée** : après avoir écouté, il faut revenir devant un
éditeur de texte et modifier du frontmatter YAML à la main, concept par
concept. C'est là que la revue meurt.

barehands est exactement l'autre moitié : un tableau où l'on **attrape** un
concept, où on le **présente**, où on le **jette**. Le geste manquant est
celui qui appose `verified: [{by: human:amdkn}]`.

## Le trou honnête : le tableau ne sait pas écrire

**La liste blanche de `/cmd` ne contient aucun verbe d'écriture, et `/note`
est en GET seul.** Telle quelle, l'interface ne peut pas tamponner un verdict.

Poser un verbe `verify` obligerait à modifier `server.py` — donc à publier
cette modification sous AGPL. **Ce n'est pas un problème** : le bundle OKF
n'est pas un SaaS, et un petit service séparé qui écoute sur un autre port et
écrit le frontmatter est encore plus propre — il garde barehands intact et
maintient la mise à jour par `update.sh` sans conflit.

# Le risque à traiter avant de brancher quoi que ce soit

`server.py` écoute sur `127.0.0.1` — c'est le bon choix, et il n'y a
**aucune authentification**. Tout processus local peut lire n'importe quel
`.md` d'un orbe configuré via `GET /note`.

Or il reste sur ce poste **30 fichiers `.md` du corpus V2 portant des motifs
de secrets** (24× `ck_`, 5× `sk-`, un JWT), signalés et non revus.

**Ne pas pointer d'orbe vers un dossier non assaini.** Le sas média et la
prison des notes protègent contre l'évasion *hors* du dossier ; ils ne
protègent pas contre ce qui est *dedans*.

# Ce qui reste à vérifier

- `stage.html` n'a pas été lu (155 Ko). Les gestes, les seuils, le rendu
  trois.js, la page `?role=render` : tout cela est **déclaré par l'auteur**,
  non mesuré.
- Aucun lancement n'a été fait sur ce poste. Le premier essai dira si les CDN
  répondent et si la webcam est prise.
