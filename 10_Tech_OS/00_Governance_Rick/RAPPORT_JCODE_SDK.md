# RAPPORT — `jcode/sdk` et le point d'extension pour un Sandbox Gateway

> Date : 2026-08-14 · Lecture : clone shallow en `%TEMP%\jcode_inspect\jcode` (commit HEAD de `main`).
> Question : **`1jehuang/jcode` expose-t-il un point d'extension — plugin, sandbox, hôte d'outils — sur lequel un adaptateur *Sandbox Gateway* pourrait se brancher ?**

## Réponse

**Non.** jcode n'expose ni plugin runtime, ni trait d'extension public pour
ajouter une capacité sans forker, ni hôte d'outils, ni sandbox d'exécution.
La conclusion provisoire du brief est confirmée — mais ce n'est pas un
manque ; c'est une posture assumée par l'auteur.

Preuve la plus nette, `README.md:620` :

> *"Jcode is inventing a new form of customizability. One that doesn't limit
> you to what a plugin or extension can do. Tell your jcode agent to enter
> self dev mode, and it will start modifying its own source code. Jcode is
> optimized to iterate on itself."*

L'extension est par fork + recompilation, pas par greffe dynamique.

## 1 · Point d'extension — n'existe pas

### Ce qui existe et *n'est pas* un point d'extension

**`sdks` en lecture seule.** Deux SDKs strictement client, qui spawn un
processus jcode et dialoguent avec lui par socket :

- `sdk/typescript/README.md:3-4` — *"TypeScript SDK for the **jcode harness
  API** (protocol v1) — the stable, versioned boundary between the jcode
  agent runtime and any client."*
- `crates/jcode-sdk/src/lib.rs:1-11` — *"Rust SDK for the jcode harness.
  […] This crate is what you actually build a client with: connect, drive
  sessions, stream events. […] It is the Rust counterpart of `sdk/typescript`."*
- `crates/jcode-sdk/src/launch.rs:209` — `command.spawn()` : le SDK lance
  un *vrai* binaire jcode en sous-processus. Aucun couplage statique.

**`crates/jcode-harness-api`** est un protocole wire NDJSON sur socket
Unix (ou pipe nommé Windows). `lib.rs:7-14` :

> *"Every frame is one JSON object on one line (NDJSON). Every frame carries
> `v`, the protocol major version. Clients must ignore unknown fields and
> skip unknown event kinds. Additive changes bump `API_VERSION_MINOR`;
> breaking changes bump `API_VERSION_MAJOR`."*

Le couple requête/réponse est **figé** : `requests.rs` énumère 31
variantes `ApiRequest` (Hello, SendMessage, Rewind, Compact, SetModel, …)
terminées par un `#[serde(other)] Unknown`, et `events.rs` énumère 27
variantes `ApiEvent` terminées pareil. `Unknown` est un catch-all
forward-compat : *"Servers reply with an error frame"* (`requests.rs:194`)
— pas un point de registration.

**`crates/jcode-tool-core::Tool`** (`src/lib.rs:145`) est un trait
asynchrone (`name`, `description`, `parameters_schema`, `execute`) et il
existe bien. Mais il vit dans le workspace interne (`jcode-tool-core`
n'est pas publié sur crates.io) et la liste des outils est **hardcodée**
dans `crates/jcode-app-core/src/tool/mod.rs:190` (`fn base_tools`,
privée, statique via `OnceLock`) : `read`, `write`, `edit`, `patch`,
`apply_patch`, `bash`, `browser`, `webfetch`, `websearch`, `memory`,
`gmail`, `swarm`, `selfdev`, … — 30+ outils, **pas un seul** enregistré
depuis l'extérieur. `Registry::empty()` (`mod.rs:180`) est `pub`, mais
la seule façon de peupler autre chose est `Registry::new()` (`mod.rs:302`)
qui rappelle `base_tools()`. Ajouter un outil = ouvrir
`crates/jcode-app-core/src/tool/mod.rs`, ajouter la ligne, recompiler.

**`crates/jcode-base/src/registry.rs`** n'est PAS un registre de plugins.
C'est un registre de *serveurs jcode* lancés (`~/.jcode/servers.json`),
utilisé pour que plusieurs clients découvrent quel daemon écoute sur
quel socket. Aucun lien avec l'extension.

**`crates/jcode-gateway-types`** ne contient que des `lib.rs` types —
`pub struct` et `enum` partagés entre deux autres crates. Pas de
runtime, pas de handler. Il a été ajouté à la workspace mais aucun
appelant ne le branche sur un serveur.

### Ce qui ressemble à un point d'extension et ne l'est pas

**Lifecycle hooks** (`docs/HOOKS.md`, `docs/SPAWN_HOOK.md`) — ces hooks
sont des **commandes externes** que vous déclarez dans `~/.jcode/config.toml` :

```toml
[hooks]
pre_tool      = "~/bin/jcode-tool-policy"   # gate
post_tool     = ""                          # observer
```

`pre_tool` peut *bloquer* un tool call (exit 2 = refus, message d'erreur
retourné au modèle). `turn_end`, `session_start`, `session_end`,
`post_tool` sont des observers spawnés détachés. Le `spawn_hook`
contrôle où s'ouvrent les fenêtres headed. **Aucun de ces hooks
n'ajoute une capacité à jcode** : ce sont des programmes que vous
lancez à côté, qui reçoivent stdin/env et rendent un code de sortie.

**`Tool` trait exposé** — pourrait *théoriquement* se prêter à un
chargement dynamique (libloading, WASM, etc.). Mais : (a) aucun
mécanisme de chargement n'est implémenté, (b) le trait n'est pas
publié sur crates.io, (c) `jcode-tool-core` est `path = "…"` dans
`Cargo.toml`, (d) `Registry::insert_tool` (`mod.rs:158`) est privé.

### Ce qui est *publié* sur crates.io

`publish = false` est explicite pour `jcode-harness-api`,
`jcode-harness-api-server`, `jcode-sdk`, `jcode-gateway-types`. Pour
`jcode-tool-core` et `jcode-tool-types`, pas de `publish = false`
explicite, mais aucune publication constatée (versions `0.1.0`,
dépendances en `path = "…"` du workspace).

**Conclusion §1** : aucun trait, registre, crate, hook, ou surface
NDJSON qui permette d'ajouter une capacité à jcode sans forker le
workspace et recompiler.

## 2 · Sandbox — n'existe pas (pour le code)

Recherche `sandbox|seccomp|landlock|isolate|jail|nsjail|bwrap|container`
dans tout le repo : 58 fichiers, presque tous des faux positifs.

**Preuve directe**, `crates/jcode-command-risk/src/lib.rs:1-33` :

> *"jcode executes `bash` tool calls with no gate of its own: the only
> check in `ToolRegistry::execute` is an opt-in external `pre_tool` hook,
> which is off by default. A model that decides to run `rm -rf ~` is
> obeyed immediately. That is issue #604, where a user lost their home
> directory. […] This is defense in depth, not a sandbox. A determined or
> unlucky `sh -c "$(printf ...)"` can defeat any static parser."*

L'auteur le dit en clair : le command-risk classifier est un *filtre
statique* (Safe / Low / Confirm / Catastrophic), pas un sandbox. Le
bash tool exécute dans le shell de l'utilisateur, sans isolation.

**Usages du mot "sandbox" qui n'en sont pas :**

- `docs/ONBOARDING_SANDBOX.md` — sandbox = `JCODE_HOME` + `JCODE_RUNTIME_DIR`
  pointant un dossier jetable. C'est de l'isolation de *configuration*
  (credentials, transcripts), pas de code.
- `crates/jcode-base/src/auth/test_sandbox.rs` — `tempfile::TempDir`
  pour tests unitaires auth.
- `crates/jcode-app-core/src/tool/discover.rs` (~lignes 1893, 1980) —
  produit "Stripe sandbox MCP" (un serveur tiers), pas une sandbox jcode.
- `scripts/onboarding_sandbox.sh`, `scripts/stale_server_upgrade_sandbox.sh`
  — scripts shell de mise en place.

**`docs/SECURITY_DEPENDENCIES.md`, `docs/SAFETY_SYSTEM.md`** — le système
de sécurité est un classifieur de blast radius + permission prompt
humain. Aucun `seccomp`, `landlock`, `bwrap`, `container`, etc. n'est
mentionné.

**Conclusion §2** : l'exécution de code (notamment via le tool `bash`)
se fait dans le shell utilisateur, sans isolation. Le mot "sandbox" est
utilisé à d'autres fins.

## 3 · MCP — jcode est *client*, jamais hôte

**Preuve directe** : `crates/jcode-base/src/mcp/client.rs:153-165` :

```rust
let mut command = Command::new(&config.command);
command
    .args(&config.args)
    .envs(&env)
    .stdin(Stdio::piped())
    .stdout(Stdio::piped())
    .stderr(Stdio::piped());
…
let mut child = command.spawn()?;
```

jcode **spawn des processus serveurs MCP** (configurable dans
`~/.jcode/config.toml`, voir `McpServerConfig`) et converse avec eux
en JSON-RPC sur stdio. C'est le pattern client MCP canonique.

**`crates/jcode-app-core/src/tool/mcp.rs:1-114`** — un *tool* `mcp`
exposé à l'agent (`mcp_management`), avec actions `list`, `connect`,
`disconnect`, `reload`. Plus un module `McpManager`
(`crates/jcode-base/src/mcp/manager.rs`) qui maintient le pool de
sous-processus.

**Aucune commande `mcp serve` n'existe.** Grep `cli/dispatch.rs` ne
trouve que `api-bridge` — qui bridge l'API publique jcode, pas une
quelconque exposition MCP.

**Pour un Sandbox Gateway** : un serveur MCP pourrait tourner à côté,
attendre qu'un jcode le *découvre* et le *connecte*, et exposer ses
outils. Mais le serveur MCP est alors un *fournisseur de tools* que
jcode consomme, pas un point où jcode se laisse étendre. Tous les
outils MCP finissent dans le `Registry` de jcode avec un préfixe
`mcp__<server>__<tool>`.

**Conclusion §3** : jcode est strictement *client* MCP. Pas d'hôte,
pas de bridge MCP inter-process. Un Sandbox Gateway qui voudrait
s'intégrer *comme outil* passerait par MCP côté client — donc il
faudrait que jcode le *config* explicitement et le *spawn* lui-même.

## 4 · Le SDK, pour qui ?

`sdk/typescript/README.md:3-8` :

> *"TypeScript SDK for the **jcode harness API** (protocol v1) — the
> stable, versioned boundary between the jcode agent runtime and any
> client. […] desktop2 is built on this crate rather than on the raw
> protocol, so the SDK's design is exercised by a real, shipping client
> every day."*

Deux clients documentés (`README.md:57-95`) :

- `JcodeClient.launch(options)` — *Embed jcode as an agent engine*.
  Lance une instance privée avec son propre état, sessions, sockets.
- `JcodeClient.connect(options)` — *Automate the user's own jcode*.
  S'attache au jcode déjà lancé via `jcode api-bridge`.

Dans les deux cas, le SDK *pilote* jcode par le socket d'API. Il n'a
aucune visibilité sur le runtime de jcode. C'est la même histoire
pour `crates/jcode-sdk` (`src/lib.rs:1-11`) :

> *"Rust SDK for the jcode harness. […] This crate is what you actually
> build a client with: connect, drive sessions, stream events. […]
> Desktop2 is built on this crate rather than on the raw protocol."*

**Conclusion §4** : le SDK s'adresse à quelqu'un qui *pilote* jcode
depuis l'extérieur. Il ne s'adresse pas à quelqu'un qui veut étendre
jcode. Le point d'entrée du couplage est `jcode api-bridge` (cf.
`src/cli/args.rs:544`).

## 5 · Surface d'un couplage — deux chemins, deux coûts

Pour un Sandbox Gateway qui voudrait s'attacher à jcode, deux chemins
existent et aucun n'est "plug-and-play" :

### Chemin A — Bundle jcode, compiler un nouveau tool

C'est le chemin "self-dev" du README. Coût : **fork + recompilation**.
Surface à toucher :

- 1 nouveau fichier dans `crates/jcode-app-core/src/tool/` (par
  convention `<mono-consonne>.rs`, ex. `sandbox_gateway.rs`),
  implémentant `jcode_tool_core::Tool` (5 méthodes : `name`,
  `description`, `parameters_schema`, `execute`, plus `to_definition`
  par défaut).
- 1 ligne dans `crates/jcode-app-core/src/tool/mod.rs:190` (`base_tools`)
  + `pub mod sandbox_gateway;` au sommet du fichier.
- Optionnel : config entry dans `crates/jcode-base/src/config.rs` pour
  pointer vers l'endpoint du gateway.

**Types publics à toucher : 2** (le `Tool` trait + l'insertion dans
`base_tools`). La "frontière" est juste le trait `Tool` et
`ToolContext` (`jcode-tool-core/src/lib.rs:103`). Mais le couplage est
un couplage *de build* : chaque release jcode peut casser (toutes les
releases sont annoncées avec changements cassants — voir
`Compatibility` côté SDK).

### Chemin B — Embarquer le Gateway comme serveur MCP

Aucun fork, mais aucun couplage *de runtime* non plus : jcode lance
le serveur MCP via `tokio::process::Command`, parle JSON-RPC avec lui
sur stdio, et listes ses tools. Le Gateway devient juste un tool
parmi d'autres (préfixe `mcp__gateway__…`). Le Gateway doit :

- Implémenter le protocole MCP serveur (handshake, initialize,
  tools/list, tools/call) — ~150-300 LOC selon le langage.
- Être déclarable dans `~/.jcode/config.toml` côté jcode
  (`{ command = "...", args = [...] }`).
- Spawn par jcode à la connexion (comme tous les serveurs MCP).

**Types publics à toucher : 0** côté jcode. La "frontière" est
uniquement le protocole MCP — la même que pour n'importe quel
serveur MCP. Si le Gateway meurt, jcode le déconnecte et l'agent
voit un tool indispo.

### Comparaison

| | Chemin A (fork) | Chemin B (MCP) |
|---|---|---|
| Fork jcode | oui | non |
| Recompilation jcode | oui | non |
| Surface jcode touchée | 2 types | 0 |
| Surface MCP nécessaire | non | protocole MCP serveur |
| Couplage runtime | lien statique Rust | JSON-RPC sur stdio |
| Surface blast radius | jcode entier | 1 tool MCP |
| Coût de migration sur release jcode | fort (membres workspace) | faible (protocole MCP) |

## Verdict

> **Non.** Le seul mécanisme d'extension de jcode est *forker, modifier
> un trait interne, recompiler* (chemin A) ou s'aligner sur le
> *rôle* d'un serveur MCP (chemin B). Aucun des deux n'est un
> point d'extension au sens où deepseek-harness/Cordis l'est —
> `1jehuang/jcode` est explicitement positionné contre l'idée de
> plugin.
>
> Pour un Sandbox Gateway, le chemin B (MCP serveur) est le moins
> invasif : zéro fork, couplage protocolaire générique, et le
> Gateway tourne déjà dans son propre process — il *est* la sandbox
> par construction. La limite est qu'on n'obtient qu'un *tool* dans
> jcode, pas une extension au moteur.
>
> Si la question cachée est "deepseek-harness vs jcode", la thèse
> du brief tient : jcode est un client rapide, pas un socle à
> plugins. Mais le brief demandait de trancher la question du
> *point d'extension*, pas de choisir entre les deux dépôts.

## Ce que je n'ai pas pu lire

- **`crates/jcode-protocol`** — protocole *interne* (vs l'API publique
  `jcode-harness-api`). Le `doc` header du `lib.rs` n'a pas été
  ouvert ; il pourrait y avoir un trait ou registre interne non
  exposé. Mais : (a) le brief demande un point d'extension *public*
  pour un adaptateur externe, (b) `jcode-protocol` est workspace-local
  (`publish = false` vraisemblable). Sans pertinence pour la question.
- **`crates/jcode-desktop2`** — utilise `jcode-sdk`. Confirmé via le
  README SDK (`sdk/typescript/README.md:9`), pas vérifié fichier par
  fichier.
- **`crates/jcode-swarm-core`** — non ouvert. Mais le swarm tool est
  enregistré comme tous les autres dans `base_tools` (`mod.rs:298`)
  et utilise `communicate::CommunicateTool`. Pas un système à
  plugins.
- **`docs/audits/CODE_QUALITY_AUDIT_2026-04-18.md`** — contient une
  mention "sandbox" dans son titre/sommaire, non ouvert. Si une
  refonte sandbox y est proposée, ça ne change rien au verdict
  présent (audit, pas code mergé).
- **`crates/jcode-base/src/mcp/schema_cache.rs`**, `protocol.rs` —
  détails du client MCP. Lu le `client.rs` qui confirme le rôle
  client ; pas exploré les caches/quotas.

## Verdict final

**À la question, en une phrase : non, jcode n'expose pas de point
d'extension sur lequel un adaptateur Sandbox Gateway pourrait se
brancher sans soit forker le workspace, soit se conformer au rôle
d'un serveur MCP tiers.**

— Amadeus, 2026-08-14
