---
type: Integration
title: 9Router et OmniRoute au démarrage de Windows
description: Câblage des deux routeurs LLM locaux au boot, ports séparés, liaison localhost, et état réel des sources gratuites.
tags: [routeur, llm, autostart, windows, openrouter, agentrouter, orcarouter, 9router, omniroute]
generated: { by: "claude-opus-5", at: "2026-08-21T07:30:00Z" }
verified:
  - { by: "claude-opus-5", at: "2026-08-21T07:30:00Z" }
sources:
  - id: disque-local
    resource: "C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/routers/"
    title: "Lanceurs .cmd et .vbs, journaux de démarrage"
    last_modified: 2026-08-21
  - id: openrouter-limits
    resource: "https://openrouter.ai/docs/api_reference/limits"
    title: "OpenRouter — API credit & rate limits"
    last_modified: 2026-08-21
  - id: agentrouter
    resource: "https://agentrouter.org"
    title: "AgentRouter — relais compatible Anthropic, crédits offerts"
    last_modified: 2026-08-21
  - id: orcarouter
    resource: "https://www.orcarouter.ai/"
    title: "OrcaRouter — passerelle BYOK sans marge, Continuum AI"
    last_modified: 2026-08-21
okf_version: "0.2"
---

# 9Router et OmniRoute au démarrage

## Ce qui est en place

Deux routeurs LLM locaux démarrent avec la session Windows, sur le même motif
que `agentgateway` : un `.vbs` dans le dossier Démarrage qui appelle un `.cmd`
en fenêtre masquée.

| Routeur | Port | Liaison | Lanceur |
|---|---|---|---|
| OmniRoute v3.8.49 | 20128 | 127.0.0.1 | `20_Harness/routers/omniroute.cmd` |
| 9Router v0.5.55 | 20129 | 127.0.0.1 | `20_Harness/routers/9router.cmd` |
| agentgateway (préexistant) | 3300 | 0.0.0.0 | `20_Harness/agentgateway/run.cmd` |

Les `.vbs` sont dans
`AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/`, copiés depuis
`20_Harness/routers/` — l'original versionné reste la référence.

## Quatre pièges payés pendant le câblage

**Les deux routeurs ont le même port par défaut : 20128.** Laissés tels quels,
ils ne peuvent pas coexister au démarrage — le second échoue en silence dans une
fenêtre masquée. 9Router est déplacé en 20129.

**9Router se lie à `0.0.0.0` par défaut**, ce qui expose la passerelle à tout le
réseau local. `--host 127.0.0.1` est obligatoire, pas cosmétique.

**9Router s'arrête sur un menu interactif « Choose Interface »** qui attend une
frappe clavier. Le serveur HTTP démarre avant le menu, donc le port répond quand
même — c'est ce qui rend le piège trompeur. Sans `--tray`, le processus reste
suspendu sur un `stdin` que personne n'alimentera jamais au boot. Avec `--tray`,
le journal annonce « Router is now running in system tray. Close this terminal
if you want. » — c'est la trace à chercher pour valider.

**OmniRoute est un serveur Next.js : il lit `HOSTNAME`, pas `HOST`.** Poser
`HOST=127.0.0.1` ne fait rien ; le serveur annonce `Network: http://0.0.0.0:20128`
et répond au réseau. Seul `set "HOSTNAME=127.0.0.1"` le confine.

## Comment vérifier que ça marche

Ne pas tester par `start` depuis Git Bash — le répertoire courant n'est pas
transmis, le `.cmd` ne démarre pas et **aucun journal n'est écrit**. Un dossier
sans fichier `.log` signifie « jamais lancé », pas « lancé et muet ».

Tester par le mécanisme réel du boot :

```bash
cscript //nologo "C:\Users\amado\ASpace_OS_V3\00_Amadeus\20_Harness\routers\9router.vbs"
```

Puis, après ~45 s :

```bash
curl -s -o /dev/null -w "%{http_code}\n" --max-time 15 http://127.0.0.1:20129/
curl -s -o /dev/null -w "%{http_code}\n" --max-time 15 http://127.0.0.1:20128/api/health
```

Attendus : **307** pour 9Router (redirection vers son UI), **401** pour OmniRoute.

Le 401 d'OmniRoute est un **succès**, pas une panne : la route est classée
`x-omniroute-route-class: MANAGEMENT` et exige `OMNIROUTE_API_KEY`. Le CLI
`omniroute health` répond « Server not running » dans ce cas — **il ment**, parce
qu'il sonde une route protégée avec un délai court. La mesure qui fait foi est
`curl -v`, qui montre le 401 et les en-têtes.

## OmniRoute ne route rien pour l'instant

Mesuré au démarrage : `AutoRefreshDaemon — checking 0 credentials`, `Config Dir:
Not found`, et pour chaque alias :

```
[AUTO] auto/coding:pro matched no connected models; returning an empty pool.
[AUTO] auto/minimax   matched no connected models; returning an empty pool.
[AUTO] auto/zai       matched no connected models; returning an empty pool.
```

**Aucun fournisseur n'est connecté.** Les deux routeurs sont debout mais vides ;
ils ne peuvent servir de repli tant qu'aucune clé n'y est déposée.

## Paysage des sources — deux catégories à ne pas confondre

C'est la confusion qui a motivé cette note. « Routeur » recouvre deux choses
qui ne se substituent pas.

### Sources de quota (elles fournissent l'inférence)

| Source | Nature de la limite | Ce qui se passe quand on la dépasse |
|---|---|---|
| Ollama Cloud | quota par fenêtre de temps | 429 |
| NVIDIA NIM | quota par fenêtre de temps | 429 |
| OpenRouter | 20 req/min **et** 50 req/jour ; 1 000/jour à vie dès 10 $ d'achat unique | 429 |
| AgentRouter | crédits (100–200 $ offerts), pas de fenêtre | solde à zéro, définitif |

### Couches de routage (elles ne fournissent aucun quota)

**OrcaRouter**, **OmniRoute** et **9Router** sont dans cette catégorie :
ils répartissent le trafic vers des fournisseurs dont **on apporte les clés**.
OrcaRouter revendique zéro marge sur le BYOK et une version Lite auto-hébergeable
sous licence MIT. Aucun des trois n'ajoute de quota gratuit.

Corollaire : ajouter OrcaRouter à côté d'OmniRoute et 9Router ne résout pas un
429. Trois routeurs devant zéro fournisseur routent zéro requête.

### OpenRouter parle nativement l'API Anthropic

Mesure du 2026-08-21 : OpenRouter expose une **Anthropic Skin**, un endpoint au
format Messages d'Anthropic. Claude Code s'y branche **sans proxy** — ni
OmniRoute, ni 9Router, ni `y-router`. Le raisonnement étendu et l'usage d'outils
passent intacts.

```
ANTHROPIC_BASE_URL   = https://openrouter.ai/api      # SANS /v1
ANTHROPIC_AUTH_TOKEN = sk-or-v1-…                     # bearer
ANTHROPIC_API_KEY    = ""                             # vide, pas absent
```

Trois pièges, chacun produisant une panne qui accuse le mauvais coupable :

- **`/v1` en trop.** CC ajoute `/v1/messages` lui-même ; `…/api/v1` donne
  `…/api/v1/v1/messages` → 404. Plusieurs tutoriels donnent encore l'ancienne forme.
- **`ANTHROPIC_API_KEY` supprimé au lieu d'être vidé.** Il part en `x-api-key`
  et serait lu comme une credential Anthropic directe, en conflit avec le bearer.
- **Login Anthropic en cache.** Il écrase les variables et rend des
  « model not found ». `/logout` une fois, puis relancer.

Outillage posé : `00_Amadeus/20_Harness/openrouter/bascule_openrouter.py`
(saisie masquée de la clé, backup avant écriture, `--revert`). **À lancer CC
fermé** — CC réécrit `settings.json` en fin de session.

### Le prix affiché ne prédit pas le coût réel — le cache lu, oui

C'est le résultat le plus utile de la mesure du 2026-08-21. En session Claude
Code, l'entrée écrase la sortie en volume : à chaque tour, CC renvoie le même
préfixe. Sur ce poste, les deux `CLAUDE.md` plus `MEMORY.md` pèsent **36 040
octets, ~10 000 tokens**, avant le prompt système, les schémas d'outils et
l'historique. Texte identique octet pour octet, tour après tour.

Le catalogue expose `input_cache_read` et `input_cache_write`. Sur la plupart
des modèles retenus, **l'écriture est gratuite** : le cache est automatique,
aucun `cache_control` à poser. L'économie arrive sans configuration.

| Modèle | Entrée $/M | Cache lu $/M | Gain | Sortie $/M | Contexte |
|---|---|---|---|---|---|
| `xiaomi/mimo-v2.5` | 0,140 | **0,0028** | **×50** | 0,28 | 1 050 000 |
| `inclusionai/ling-3.0-flash` | 0,021 | 0,0042 | ×5 | 0,06 | 262 144 |
| `deepseek/deepseek-v4-flash` | 0,081 | 0,0162 | ×5 | 0,16 | 1 048 576 |
| `openai/gpt-oss-120b` | 0,030 | 0,0300 | **×1 — nul** | 0,17 | 131 072 |

Simulation, 50 tours, ~40 K tokens d'entrée par tour, 1,5 K de sortie :

| | sans cache | 85 % de cache | 95 % de cache |
|---|---|---|---|
| `deepseek/deepseek-v4-flash` | $0,174 | $0,064 | $0,051 |
| `xiaomi/mimo-v2.5` | $0,301 | $0,068 | **$0,040** |

**Le classement s'inverse.** MiMo est 1,7× plus cher au prix affiché et devient
le moins cher dès 95 % de réutilisation. Choisir un modèle sur son prix d'entrée
sans regarder son prix de cache conduit au mauvais choix — `openai/gpt-oss-120b`
en est l'exemple : entrée bon marché, cache sans aucun bénéfice.

### Le banc d'outils tranche ce que le prix ne dit pas

Un modèle bon marché qui ne sait pas émettre un `tool_use` valide ne pilote pas
Claude Code, quel que soit son tarif. `00_Amadeus/20_Harness/openrouter/banc_outils.py`
mesure trois épreuves sur l'**Anthropic Skin** — le chemin exact de CC ; un test
via `/chat/completions` ne prouverait rien, c'est un autre protocole :

1. émission d'un `tool_use` valide avec les champs requis,
2. acceptation d'un `tool_result` et poursuite cohérente,
3. cache lu observé au second appel (préfixe de ~22 000 tokens).

Résultat du 2026-08-21 : **`xiaomi/mimo-v2.5` 3/3** et
**`deepseek/deepseek-v4-flash` 3/3**.

MiMo était écarté du premier profil pour un seul motif — fiabilité en usage
d'outils non mesurée. La mesure l'a levé, il passe **principal**. C'est la seule
raison légitime de promouvoir un modèle : une épreuve passée, pas un prix
attrayant.

Profil retenu (2026-08-21, après banc) : `xiaomi/mimo-v2.5` en principal /
Opus / Sonnet, `inclusionai/ling-3.0-flash` en Haiku / small-fast. Repli éprouvé
en session le même jour : `deepseek/deepseek-v4-flash`.

**Anti-piège de restauration.** Un `--revert` qui rend « le backup le plus
récent » est un piège dès la deuxième bascule : le plus récent est déjà une
config basculée, pas l'état d'origine. Le script liste donc chaque sauvegarde
avec son `ANTHROPIC_BASE_URL` et son modèle, et demande laquelle restaurer.
Défaut corrigé avant d'avoir servi.

### Les variantes `:batch` : 50 % de remise contre l'asynchronisme

Remise **uniforme de 50 %** sur tout le catalogue — `openai/gpt-5.6-luna`
$0,20/$1,20 → $0,10/$0,60 ; `anthropic/claude-opus-5` $5/$25 → $2,50/$12,50.

La contrepartie est le traitement différé, jusqu'à 24 h. **Inutilisable en
session interactive**, mais adapté à une vague de revue de corpus, qui n'a
aucune raison d'être synchrone. Un piège de lecture : sur les pages de modèles,
le prix affiché en bas de tableau est souvent celui de la variante `:batch`, ce
qui fait croire à un tarif interactif qui n'existe pas.

**Effet de bord observé le 2026-08-21 :** avec `ANTHROPIC_SMALL_FAST_MODEL`
pointé sur un modèle mort, l'outil `WebFetch` de CC échoue — il s'appuie sur le
petit modèle rapide. Un `WebFetch` en panne est donc un symptôme de
configuration de modèle, pas un problème réseau.

### Le registre bat `settings.json` — la bascule peut réussir sans effet

Mesure du 2026-08-21, après une bascule appliquée et vérifiée dans le fichier :
Claude Code a redémarré en affichant `MiniMax-M3 with xhigh effort`. Le fichier
était juste ; il n'était simplement pas la source qui gagne.

`HKCU:\Environment` portait cinq variables permanentes :

```
ANTHROPIC_BASE_URL          = https://api.minimax.io/anthropic
ANTHROPIC_API_KEY           = sk-cp-…
ANTHROPIC_AUTH_TOKEN        = sk-cp-…          <- masque meme la cle OpenRouter
ANTHROPIC_MODEL             = MiniMax-M3
ANTHROPIC_SMALL_FAST_MODEL  = MiniMax-M3
```

**Ordre de précédence : registre > `settings.json`.** Retirer `ANTHROPIC_MODEL`
du fichier pour libérer les slots Opus/Sonnet/Haiku ne sert à rien tant que le
registre le réimpose. Et `ANTHROPIC_AUTH_TOKEN` en `sk-cp-…` masque la clé
OpenRouter même si l'URL de base est corrigée : on obtient une authentification
MiniMax envoyée à OpenRouter, donc un échec qui accuse la clé.

Ces variables avaient été posées **exprès** — c'est ce qui faisait tourner la
délégation MiniMax depuis PowerShell sans réexporter à chaque shell. Les retirer
arrête ce chemin. Pour garder les deux, enrober le lancement MiniMax dans un
script qui exporte les variables pour ce seul processus, au lieu de les rendre
globales.

Outillage : `00_Amadeus/20_Harness/openrouter/purge_env_registre.py`
— lecture seule par défaut, `--appliquer` sauvegarde puis retire, `--restaurer`
remet. Diffuse `WM_SETTINGCHANGE`, sans quoi seuls les processus lancés après
une réouverture de session verraient le changement.

**Le terminal courant garde l'ancien environnement.** Vérifier depuis celui-là
ne prouve rien — ouvrir un nouveau terminal avant de conclure.

**Piège de sécurité rencontré.** Le dossier `backups/` contient les valeurs en
clair (c'est le prix de la restauration : un backup illisible ne restaure rien)
et n'était pas ignoré par git, dans un dépôt poussé. `.gitignore` posé ;
vérification faite qu'aucun backup n'avait jamais été commité. Un outil de
sauvegarde de configuration crée un dépôt de secrets par construction — poser
l'exclusion **en même temps** que le script, pas après.

### Ce qui distingue OpenRouter d'AgentRouter

OpenRouter se **régénère chaque jour** — c'est une rente. AgentRouter est un
**stock qui s'épuite sans se reconstituer** ; les 200 $ annoncés proviennent de
gists affiliés et de vidéos, pas d'une documentation officielle, et le montant
varie selon les sources (100 $, 125 $, 175 $, 200 $). Pour une vague de revue
qui repasse tous les jours, seul le palier journalier d'OpenRouter tient.

## Anti-pièges

- **Ne pas croire `omniroute health`** : il rend « Server not running » sur un
  serveur parfaitement vivant. Utiliser `curl -v` sur `/api/health`.
- **Un `.log` absent ≠ un agent muet.** Il veut dire que le `.cmd` n'a jamais
  démarré. Vérifier l'existence du fichier avant d'en lire le contenu.
- **Le premier appel HTTP à OmniRoute après le boot peut dépasser 60 s** :
  Next.js compile ses routes à la demande. Ne pas conclure à la panne sur un
  seul `curl` qui expire.
- **agentgateway écoute toujours sur `0.0.0.0:3300`.** Il n'a pas été touché ici,
  mais il reste exposé au réseau local — voir
  [[composio-mcp-as-gateway]] pour le raisonnement sur ce canal.

## Ce qui reste à faire

Déposer au moins une clé de fournisseur dans OmniRoute (`omniroute providers`)
pour que le repli existe réellement. Tant que `checking 0 credentials` figure
dans le journal, les deux routeurs sont des coquilles.

## Smoke test delegation → M3 : 200/429 (2026-08-21)

Test de fumée « délégation à M3 » ordonné par l'utilisateur le 2026-08-21,
depuis une session DeepSeek/OpenRouter. L'API MiniMax répond :

| Appel | Résultat |
|---|---|
| `GET /v1/models` — clé `MINIMAX_API_KEY` du registre `HKCU\Environment` | **200** — clé valide, compte existe |
| `POST /v1/messages` (MiniMax-M3) | **429** `rate_limit_error` |

Message de refus rapporté tel quel :

```
The Token Plan usage limit has been reached. To avoid interruption, please
upgrade your plan or buy credits and turn on auto consumption. (2067)
```

**Conclusion : le smoke test échoue côté quota — la clé `sk-cp-…` (plan) ne
permet pas de puiser en pay-as-you-go.** Décision en une phrase : la bascule
automatique vers MiniMax-M3 par cette clé reste suspendue tant que le quota
n'est pas rechargé.

Le premier PONG mesuré passait par le canal OpenRouter hérité, pas par M3 —
la clé n'était pas lue. Relire la clé au registre exige `MSYS_NO_PATHCONV=1`,
sinon `/v` est mangé par Git Bash.

Références à garder : le profil OKF existant dans la même liste
d'integrations, concept « routeur LLM ».
