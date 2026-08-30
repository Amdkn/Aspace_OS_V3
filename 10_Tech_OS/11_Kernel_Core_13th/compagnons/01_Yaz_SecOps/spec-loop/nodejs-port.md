# Spec-loop — Port Node.js d'AgentPulse SDK

**Issue** : ASP-885
**Owner spec** : Yaz-SecOps (S3)
**Owner impl** : Ryan-Build
**Review** : Doctor-13
**Date** : 2026-08-03
**Statut** : v1 — prêt pour review

---

## 1. Objectif

Produire `agentpulse-node`, port Node.js de l'AgentPulse SDK Python
(`~/agentpulse/sdk/`), qui instrumente les processus Node.js — en particulier
Claude Code et tout agent utilisant `@anthropic-ai/sdk` — pour capturer les
appels LLM dans le **même schéma SQLite** que le SDK Python, sans régression
sur les scripts kernel existants.

**Pourquoi** : aujourd'hui, sur les agents Node.js (Rick, Doctors, compagnons),
aucune observabilité. Donna ne voit que les scripts kernel Python via
`agentpulse_mcp.py`. Le trou laisse le trafic LLM principal des agents dans
l'angle mort. Le port Node ferme ce trou en réutilisant la même DB que la
cascade Python peut déjà lire.

**Critère de succès global** : un appel `messages.create()` dans un process
Node patché produit une ligne dans `runs` + un span dans `spans`, dans le
même fichier DB que les scripts kernel écrivent, lisible par
`agentpulse_mcp.py` sans conversion.

---

## 2. Critère d'acceptation (vérifiable)

| # | Test | Sortie attendue | Vérification |
|---|------|-----------------|--------------|
| A1 | Un script Node fait `await anthropic.messages.create({...})` avec `instrument()` actif | Une ligne dans `runs`, un span dans `spans` du DB actif | `sqlite3 <db>.db "SELECT count(*) FROM runs WHERE model='claude-...'"` ≥ 1 |
| A2 | Round-trip Node → Python | DB écrit par Node ouvert par `agentpulse_mcp.py` sans erreur ; `get_todays_finding` remonte le run | `python report.py --last` retourne le run Node |
| A3 | Round-trip Python → Node | DB écrit par `dlq.py` ouvert par Node sans erreur | `node -e "import {openDb} from 'agentpulse-node'; await openDb('<db>')"` exit 0 |
| A4 | Sync + async | `Messages.create` et `AsyncMessages.create` sont tous deux patchés | Tests unitaires `anthropic-sync.test.ts` + `anthropic-async.test.ts` verts |
| A5 | Régression Python | `python dlq.py rapport` continue d'écrire dans `kernel-dlq.db` sans changement | Sortie identique à avant le port |
| A6 | Harness installable | `node ~/.claude/agentpulse-init.js` patche in-place ; aucun edit manuel par agent | `curl` du script + `cat ~/.claude/CLAUDE.md` montre `require('./agentpulse-init')` ajouté |
| A7 | `set_active_db_path` | L'API Node du même nom commute le DB cible ; tests démontrent 2 DBs distincts en parallèle | Test `active-db.test.ts` : 2 calls → 2 DBs distincts |
| A8 | Tables identiques | Node crée les 8 tables (`runs`, `versions`, `settings`, `events`, `prompts`, `spans`, `tool_calls`, `handoffs`) avec le même schéma SQL | `diff <(sqlite3 py.db .schema) <(sqlite3 node.db .schema)` retourne vide |

---

## 3. Périmètre

### Inclus

- Package npm `agentpulse-node` (TypeScript, distribué via npm + GitHub)
- Patch monkey-patch de `@anthropic-ai/sdk` :
  - `Messages.create` (sync) — chemin utilisé par LangChain `llm.invoke()` 
  - `AsyncMessages.create` (async) — chemin utilisé par Claude Code direct
  - Capture : `(start_ns, end_ns, input_tokens, output_tokens, model)` par call
- API publique Node :
  - `instrument({ taskType, promptVersion, dbName })` — équivalent du `instrument()` Python
  - `setActiveDbPath(path: string)` — équivalent du `set_active_db_path()` Python
  - `openDb(path: string): Database` — ouverture compat SQLite Python
- Schéma SQLite **identique** au SDK Python :
  - Tables : `runs`, `versions`, `settings`, `events`, `prompts`, `spans`, `tool_calls`, `handoffs`
  - Schéma source unique : `~/agentpulse/storage/sqlite_store.py:61-173`
- Harness Claude Code : `~/.claude/agentpulse-init.js` qui :
  - Charge `agentpulse-node` 
  - Appelle `instrument()` avec `dbName` dérivé du nom de l'agent (ex. `s1-rick`, `s2-doctor-13`, `s3-yaz-secops`)
  - Idempotent (déjà-patché → no-op)
- Stack : `better-sqlite3` (binding natif sync, le plus rapide pour ce profil de charge), TypeScript, `vitest` + `node --test` pour les tests
- Migration : script `migrate-py-dbs.ts` qui ingère les DBs Python existants
  (`~/ASpace_OS_V3/10_Tech_OS/kernel/agentpulse/*.db`) dans la structure commune

### Exclus

- Port Node des patches `openai`, `langchain`, `autogen` — pas la cible. Si
  Amadou les veut, c'est un autre ticket. Le port `@anthropic-ai/sdk` seul
  suffit à fermer le trou Claude Code.
- Réécriture du SDK Python — ne pas toucher `~/agentpulse/`. Le but est la
  compatibilité ascendante.
- Modification de `agentpulse_mcp.py` (Donna) — c'est son périmètre.
- Choix d'archi DB_DIR / format de DB — décision Rick. Si on a un doute, on
  remonte, on ne tranche pas.
- Build complet (implémentation) — la spec définit les milestones, ne les
  code pas. Le Loopany produit le runbook d'exécution.

---

## 4. Interdits

- **Bâtir** : Yaz ne code pas le port. La spec est livrée ici, l'implémentation
  est Ryan-Build.
- **Détacher** : pas de promotion de ticket à `done` côté Yaz. La spec est
  livrée en `in_progress` jusqu'à review Doctor-13 + meta-review Rick.
- **Changer le schéma SQLite** : les tables du SDK Python sont la source de
  vérité. Tout écart casse le round-trip — interdit sans validation Rick.
- **Modifier `~/agentpulse/`** : on lit le SDK Python comme spec, on n'y touche
  pas. C'est le périmètre de l'équipe qui maintient le SDK original.
- **Ajouter une dépendance qui duplique les patches** : si `better-sqlite3`
  suffit, on n'introduit pas `node-sqlite3` en parallèle. Une seule stack
  SQLite côté Node.
- **Décider des DB_DIR ou du routage multi-agent** : c'est l'arbitrage du
  setup final (étape 4 du tableau Rick, owner Doctor-13). La spec Node
  expose les hooks, ne les câble pas.

---

## 5. Architecture cible

### 5.1. Capture — comment un call LLM arrive dans `spans`

```
┌─────────────────────────────────────────────────────────────────────┐
│ Process Node (ex. Claude Code / agent)                              │
│                                                                     │
│  agent = require('agentpulse-node').instrument({                    │
│    taskType: 'agent-loop',                                          │
│    promptVersion: 1,                                                │
│    dbName: 's3-yaz-secops'                                          │
│  })                                                                 │
│                                                                     │
│  ┌─────────────────────────┐    ┌──────────────────────────────┐    │
│  │ @anthropic-ai/sdk       │    │ agentpulse-node              │    │
│  │                         │    │                              │    │
│  │ Messages.create         │───►│ _patched_sync_create         │    │
│  │   ↓ (monkey-patch)      │    │   start = perf.now()         │    │
│  │ _patched_sync_create    │    │   resp = original(...)       │    │
│  │   start_ns = now()      │    │   session.record({           │    │
│  │   resp = original(...)  │    │     start_ns, end_ns,        │    │
│  │   record({...}) ────────┼───►│     input, output, model})   │    │
│  │   return resp           │    │   return resp                │    │
│  └─────────────────────────┘    └────────────────┬─────────────┘    │
│                                                  │                  │
└──────────────────────────────────────────────────┼──────────────────┘
                                                   ▼
                                    ┌─────────────────────────────┐
                                    │ ~/ASpace_OS_V3/10_Tech_OS/  │
                                    │   kernel/agentpulse/        │
                                    │   <dbName>.db               │
                                    │                             │
                                    │  tables: runs, spans,       │
                                    │  tool_calls, handoffs,      │
                                    │  events, prompts, versions, │
                                    │  settings                   │
                                    └─────────────────────────────┘
                                                   │
                                                   ▼
                                    ┌─────────────────────────────┐
                                    │ agentpulse_mcp.py (Donna)   │
                                    │ — déjà câblé, lit le DB     │
                                    │   sans savoir qui a écrit   │
                                    └─────────────────────────────┘
```

### 5.2. Compatibilité schéma — point critique

Source unique de vérité : `~/agentpulse/storage/sqlite_store.py:61-173`.

Stratégie :
1. Extraire le `_SCHEMA` constant Python dans un fichier `.sql` partagé
   `~/agentpulse/schema/common.sql` (action Python, owner équipe SDK).
2. Node importe ce `.sql` au runtime et l'exécute à l'ouverture d'un nouveau
   DB (`CREATE TABLE IF NOT EXISTS ...`).
3. Test de conformité : `diff <(sqlite3 py.db .schema) <(sqlite3 node.db .schema)`
   doit retourner vide (cf. A8).

Pourquoi cette stratégie et pas un schéma dupliqué : éviter la dérive. Un
jour quelqu'un ajoutera une colonne côté Python, et Node ne la verra pas si
le schéma est dupliqué.

**Variante retenue (v1, 2026-08-03)** : snapshot local daté du `_SCHEMA`
Python dans `~/agentpulse-node/sql/common.sql`, avec un test dédié
`npm run check-schema-drift` qui re-extrait et compare. Le snapshot est
**toléré jusqu'à la première release stable**. La migration vers
`~/agentpulse/schema/common.sql` partagé (extraction côté équipe SDK
Python) devient un **pre-requis de `v1.0.0`**.

**Wording corrigé (post-R1 Graham)** : la spec parlait de « DLQ writer en
WAL ». C'est faux en pratique — `dlq.py`/`uc.py` n'exécutent pas
`schema.sql`, donc les DBs `kernel-*.db` produites par le kernel sont en
mode `delete`. Côté SDK Python (`agentpulse.storage.sqlite_store`), le
PRAGMA `journal_mode = WAL` est exécuté via `executescript()` et active WAL.
Le test R1 vérifie les deux modes ; le wording canonique devient :
*« interop entre le writer Python (mode `delete` par défaut, WAL opt-in via
l'exécution de `_SCHEMA` côté SDK Python, mort-né côté `dlq.py`/`uc.py`)
et `better-sqlite3` »*. Aucune re-scope, juste une correction de wording.

### 5.3. Harness Claude Code — `~/.claude/agentpulse-init.js`

```js
// Schéma — pas l'implémentation finale
const path = require('path');
const { instrument } = require('agentpulse-node');

// db_name dérivé du nom de l'agent (le binaire / le workdir le fournit)
// Convention : <layer>-<name>   ex. s1-rick, s2-doctor-13, s3-yaz-secops
const dbName = process.env.AGENTPULSE_DB_NAME 
            || inferFromCwd() 
            || 'unspecified';

instrument({
  taskType: process.env.AGENTPULSE_TASK_TYPE || 'agent-loop',
  promptVersion: parseInt(process.env.AGENTPULSE_PROMPT_VERSION || '1', 10),
  dbName,
});

function inferFromCwd() {
  // Heuristique : parse le nom du workdir courant
  // ex. ".../squads/s3-yaz-secops/" → "s3-yaz-secops"
  const cwd = process.cwd();
  const m = cwd.match(/s\d-([a-z0-9-]+)/);
  return m ? `s${m[1]}` : null;
}
```

Installation : un script `install-harness.sh` qui :
- copie `agentpulse-init.js` dans `~/.claude/`
- ajoute `require('./agentpulse-init')` en tête de `~/.claude/CLAUDE.md` 
  (ligne de chargement, idempotent — `grep -q` avant d'écrire)
- ne touche aucun autre fichier de config

---

## 6. Dépendances npm

| Package | Version | Rôle |
|---------|---------|------|
| `@anthropic-ai/sdk` | `^0.x` (latest stable) | Cible du patch — doit rester en peer dependency optionnelle |
| `better-sqlite3` | `^11.x` | Binding natif SQLite, sync, rapide, format compatible Python |
| `typescript` | `^5.x` | Dev only |
| `vitest` | `^2.x` | Tests |
| `@types/node` | `^22.x` | Dev only |

**Toutes optionnelles sauf `better-sqlite3`** : si l'utilisateur n'a pas
`@anthropic-ai/sdk` installé, le patch est no-op (même comportement que
`patch_anthropic()` Python qui swallow l'`ImportError`).

---

## 7. Risks & open questions

| # | Risque | Owner pour trancher | Impact |
|---|--------|---------------------|--------|
| R1 | `better-sqlite3` ne lit pas les DBs WAL créés par Python si le mode WAL n'est pas activé à l'ouverture | Graham-Backup-DBA | Test A3 round-trip — bloquerait la livraison |
| R2 | `@anthropic-ai/sdk` change ses internals (private methods) entre versions mineures | Ryan-Build | Pin la version + tests sur ≥2 versions mineures |
| R3 | Multi-process simultané (Rick + Doctors en parallèle) écrivant dans des DBs distincts | Doctor-13 | Le setup final (étape 4 Rick) doit le prévoir ; la spec expose `set_active_db_path`, ne câble pas le routage |
| R4 | Claude Code charge `@anthropic-ai/sdk` avant notre `require()` | Ryan-Build | Le harness doit charger `agentpulse-node` AVANT tout autre module — ordonnancement dans `install-harness.sh` |

R1 est bloquant pour A3 — à tester avant de promettre le round-trip.

---

## 8. Milestones (pour Loopany)

Ces milestones ne sont **pas** à coder dans ce ticket. Ils servent d'input
au Loopany que Doctor-13 produit en parallèle (`loopany/nodejs-roadmap.md`) :

1. **M1 — Skeleton** : package npm + TypeScript config + `vitest` qui tourne.
   Critère : `npm test` exit 0 sur un test trivial. Effort : ~2h.
2. **M2 — Schema loader** : `openDb()` qui applique `common.sql`. Critère :
   un DB vide créé par Node a les 8 tables. Effort : ~3h.
3. **M3 — Patch anthropic sync** : monkey-patch `Messages.create`. Critère : A1
   vérifié sur un cas simple. Effort : ~4h.
4. **M4 — Patch anthropic async** : `AsyncMessages.create`. Critère : A4 vert.
   Effort : ~2h.
5. **M5 — Round-trip** : tests Python ↔ Node. Critère : A2, A3, A8 verts.
   Effort : ~4h. **Gate R1**.
6. **M6 — Harness** : `agentpulse-init.js` + `install-harness.sh`. Critère : A6.
   Effort : ~3h.
7. **M7 — Migration script** : `migrate-py-dbs.ts`. Effort : ~2h.
8. **M8 — Régression Python** : A5. Effort : ~1h (smoke test).

Total : ~21h dev, hors review. C'est bien un build days, pas 7h — la
roadmap 7h du projet AgentPulse n'a jamais prétendu le contraire.

---

## 9. Ce qui n'est PAS dans cette spec

- Le routage multi-agent (qui écrit dans quel DB) — décision Doctor-13.
- La ré-écriture du SDK Python — pas notre périmètre.
- Les patches `openai` / `langchain` / `autogen` côté Node — autre ticket.
- L'UI de visualisation — pas un deliverable de ce port.

---

## 10. Hand-off

- **Vers Doctor-13** : review cette spec. Si OK, déclenche Loopany
  (`loopany/nodejs-roadmap.md`) sur la base des milestones §8. Bloque sur R1
  avant de promettre le round-trip.
- **Vers Ryan-Build** : la spec §5+§6+§8 est ton input d'implémentation.
  Commence par M1 — confirme-moi quand `npm test` tourne sur un squelette vide.
- **Vers Rick (S1)** : meta-review en fin de chaîne. Tu valides que la spec
  tient la décision Rick (utiliser AgentPulse, multi-couche, fast-path) sans
  la déborder.
- **Vers Donna** : aucune action de ta part. Ton `agentpulse_mcp.py` lira les
  DBs Node sans modification — c'est le but.

---

*Fin de spec. Toute question ou drift → commentaire sur ASP-885, je remonte
au Doctor-13 si l'arbitrage dépasse mon rang.*
