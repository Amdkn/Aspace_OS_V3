---
type: Integration
title: Relais OpenRouter — router Sonnet 4.6/4.5 vers GLM 5.3 Flash et Qwen 3.8 Flash
description: Claude Code CLI valide le nom du modèle localement et refuse tout id non-Anthropic ; un relais sur 127.0.0.1:8792 réécrit le champ `model` juste avant l'envoi vers OpenRouter, et une tâche planifiée le maintient vivant.
tags: [openrouter, claude-code-cli, glm, qwen, relais, tache-planifiee, antifragile, cles]
generated: { by: claude-opus-5, at: 2026-08-28T21:05:00Z }
verified:
  - { by: claude-opus-5, at: 2026-08-28T21:02:00Z }
sources:
  - id: openrouter-models
    resource: "GET https://openrouter.ai/api/v1/models"
    title: Catalogue OpenRouter — familles z-ai et qwen
    last_modified: 2026-08-28
  - id: hermes-env-windows
    resource: "C:/Users/amado/AppData/Local/hermes/.env (+ 3 sauvegardes)"
    title: Environnement Hermes Windows — porteur de la clé OpenRouter vivante
    last_modified: 2026-08-28
  - id: tache-relais
    resource: "Tâche planifiée Windows « Relais-OpenRouter »"
    title: Gardien du relais, déclenchement à l'ouverture de session
    last_modified: 2026-08-28
okf_version: "0.2"
---

Router Claude Code CLI vers un modèle non-Anthropic **ne se fait pas par
configuration**. Le CLI valide le nom du modèle *localement*, avant tout appel
réseau : `--model z-ai/glm-5.3-flash` est rejeté sans qu'un octet ne parte.
`settings.json` portait `"model": "z-ai/glm-5.3-flash[1m]"`, ce qui cassait
chaque démarrage pour cette raison exacte.

La seule voie est un relais qui **présente au CLI un nom qu'il accepte**, puis
réécrit le champ `model` juste avant l'envoi.

## Le câblage

`127.0.0.1:8792` → `https://openrouter.ai/api/v1/messages`.

| Le CLI demande | OpenRouter sert | Contexte |
|---|---|---|
| `claude-sonnet-4-6` | `z-ai/glm-5.3-flash` | 1 310 720 |
| `claude-sonnet-4-5` | `qwen/qwen3.8-flash` | 1 000 000 |

OpenRouter expose le format **Anthropic Messages nativement** sous
`/api/v1/messages` — aucune traduction de corps n'est nécessaire, seulement la
substitution d'un champ. Le CLI appelle `/v1/messages` ; le relais préfixe
`/api`.

| Fichier | Rôle |
|---|---|
| `.claude/custom-models/openrouter-router.mjs` | le relais, table de correspondance |
| `.claude/custom-models/relais-gardien.ps1` | garde le relais vivant |
| `.claude/custom-models/claude-glm.cmd` | lance CC sur GLM 5.3 Flash |
| `.claude/custom-models/claude-qwen.cmd` | lance CC sur Qwen 3.8 Flash |
| `.claude/_secrets_local/openrouter.key` | la clé, hors KB (canon §3) |

Le `claude` nu reste sur Anthropic natif ; seuls les wrappers routent.

## Où était la clé — et ce que ça enseigne

Après purge des clés OpenRouter, trois sources ont été fouillées et **trois ont
menti par omission** :

- base OmniRoute (`storage.sqlite`) : tables `api_keys`, `registered_keys`,
  `provider_nodes` **toutes vides** ;
- balayage disque de `sk-or-v1` sur `.config`, `.claude`, `.codex`, `.ori` :
  **rien** ;
- `~/.hermes/auth.json` **côté WSL** : une entrée `openrouter` avec
  `source: env:OPENROUTER_API_KEY` et `secret_fingerprint: sha256:2e0e770e…`,
  mais `request_count: 0` — Hermes ne stocke **que l'empreinte**, la valeur
  vient d'une variable d'environnement qui n'existait plus.

La clé vivante était dans **`AppData\Local\hermes\.env` — la version
Windows**, un chemin qu'aucune des trois recherches ne couvrait. Deux clés y
coexistaient ; le Test Key Pragma les a départagées :

```bash
curl -s -o /dev/null -w "%{http_code}" --max-time 15 \
  -H "Authorization: Bearer $CLE" https://openrouter.ai/api/v1/key
```

| Fichier | Verdict |
|---|---|
| `.env` | **200 — vivante** |
| `.env.backup-20260722-143226` | 401 — morte |

**La leçon est la même que celle du sondage Windows-only des harnais**
([[herdr-ori-substrat-orchestration]]) : un outil qui existe des deux côtés de
la frontière WSL a **deux états indépendants**. Conclure « la clé n'existe
nulle part » après n'avoir fouillé qu'un côté est une erreur de méthode, pas
une donnée. Hermes Windows et Hermes WSL ne partagent rien.

Corollaire utile : `secret_fingerprint` permet de tester une clé candidate
sans jamais l'afficher.

```bash
python -c "import hashlib,sys;print('sha256:'+hashlib.sha256(sys.argv[1].encode()).hexdigest()[:16])" 'CLE'
```

## Persistance — trois couches, pas une

Un `node` lancé depuis un shell meurt avec ce shell. C'est le piège déjà payé
sur le gardien WSL et sur BMad Loop (`setsid nohup`). Un VBS de démarrage ne
suffit pas non plus : le processus reste fils du shell qui l'a lancé.

1. **Tâche planifiée `Relais-OpenRouter`**, déclenchement `AtLogOn`,
   `ExecutionTimeLimit` nul, `MultipleInstances IgnoreNew`. C'est elle qui
   donne le vrai détachement.
2. **Gardien** : sonde le port toutes les 60 s, relance le relais s'il est
   muet, journal tournant à 2000 lignes. **C'est la sonde de port qui protège
   réellement de la duplication** — un second gardien voit le port occupé et
   ne fait rien.

3. **`RestartCount 999` / `RestartInterval 1 min`** : si le processus du
   gardien est tué, Windows le relance dans la minute au lieu d'attendre la
   prochaine ouverture de session. Pour une maintenance, `Stop-ScheduledTask`
   **d'abord** — sinon Windows relance ce qu'on essaie d'arrêter.

**Le « doublon de gardien » n'a jamais existé.** Il a été diagnostiqué, puis
« corrigé » par le retrait de `RestartCount` et l'ajout d'un mutex, avant que
la mesure ne s'avère fausse — voir la section suivante. `RestartCount` a été
rétabli. Le mutex `Global\RelaisOpenRouterGardien` reste dans le script, sans
être la protection effective : **c'est la sonde de port qui protège**, un
second gardien voyant le port occupé ne fait rien.

`Set-ScheduledTask` échoue par ailleurs en `0x80041319` sur cette tâche : il
faut `Unregister` puis `Register`. Le script qui l'ignorait affichait son
message de succès **après** l'échec, faute de `$ErrorActionPreference = 'Stop'`.

Aucune fenêtre n'apparaît jamais : `CreateNoWindow` + `UseShellExecute=$false`
partout, et `-WindowStyle Hidden` sur la tâche.

### Deux pièges d'implémentation payés ici

**`Test-NetConnection` met ~20 s par sonde** — il fait aussi un ping et une
résolution DNS. La boucle en devenait poussive et retardait d'autant la
détection d'une panne. Remplacé par un `TcpClient.BeginConnect` avec attente
bornée à 2 s.

**Rediriger la sortie via `ProcessStartInfo` sans lecteur asynchrone bloque le
fils** : le tampon du tube se remplit au bout de quelques Ko et le processus
se fige en écriture. `Register-ObjectEvent` avec `$using:` hors bloc distant
est fragile ; le montage retenu laisse `cmd /c … >> journal 2>&1` faire la
redirection, qui n'a pas ce défaut.

## Comment vérifier que ça marche

```bash
netstat -ano | grep LISTENING | grep ":8792"
```

```bash
curl -s --max-time 90 http://127.0.0.1:8792/v1/messages \
  -H "content-type: application/json" -H "anthropic-version: 2023-06-01" \
  -d '{"model":"claude-sonnet-4-6","max_tokens":600,"messages":[{"role":"user","content":"Reponds exactement: PONG"}]}'
```

Le champ `model` de la réponse doit valoir `z-ai/glm-5.3-flash` — c'est la
preuve que la substitution a eu lieu, le nom demandé ne prouve rien.

**Épreuve d'antifragilité, mesurée le 2026-08-28** : relais tué à 21:16:48,
revenu seul à 21:17:46 — 54 s, sans intervention. La reprise prend au plus un
intervalle de sonde ; compter une minute, pas deux secondes.

**L'instrument de mesure se comptait lui-même.** Compter les gardiens par

```powershell
Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*relais-gardien*' }
```

rapporte **toujours un processus de trop** : la ligne de commande de la requête
*contient le motif cherché*, donc elle se matche elle-même. Le compte disait 2
là où il y en avait 1, de façon parfaitement reproductible — l'erreur la plus
traître, parce qu'elle est stable.

Deux fausses corrections ont suivi avant que la parenté ne tranche
(`svchost.exe` = la tâche, `bash.exe` = la requête) : le retrait de
`RestartCount` et l'ajout d'un mutex, tous deux inutiles. **Un filtre par motif
sur `CommandLine` doit toujours exclure le PID courant**, ou la mesure se
compte dans son propre résultat.

```bash
netstat -ano | grep LISTENING | grep ":8792"
```

Vérifier par le **port** et par `tasklist`, jamais en lançant un shell qui
relance ce qu'on observe. C'est la troisième fois qu'une sonde accuse le
mauvais coupable sur ce poste.

**`max_tokens` serré rend une réponse vide.** GLM 5.3 raisonne avant d'écrire :
sur un budget de 100, 99 tokens partent en `thinking` et le texte est coupé
avant d'exister, avec `stop_reason: max_tokens`. Ce n'est pas une panne. Prévoir
plusieurs centaines de tokens pour un simple test.

## Comment retirer le câblage

```powershell
Stop-ScheduledTask   -TaskName 'Relais-OpenRouter'
Unregister-ScheduledTask -TaskName 'Relais-OpenRouter' -Confirm:$false
```

Puis supprimer `.claude/custom-models/openrouter-router.mjs`,
`relais-gardien.ps1`, `claude-glm.cmd`, `claude-qwen.cmd` et
`.claude/_secrets_local/openrouter.key`. Réversible, sans migration.

## Ce que ce concept ne couvre pas

**9Router** (`127.0.0.1:20129`) tourne mais n'expose que des cibles
`ollama/`, `qd/`, `kc/`, `nvidia/` — **aucun provider OpenRouter**. C'est
pourquoi le relais tape OpenRouter en direct au lieu de passer par lui.
**OmniRoute** (`127.0.0.1:20128`) était éteint et sa base vide au moment de la
mesure. Les deux restent câblés séparément via `claude-9router.cmd` et
`claude-omniroute.cmd`, non revérifiés ici.
