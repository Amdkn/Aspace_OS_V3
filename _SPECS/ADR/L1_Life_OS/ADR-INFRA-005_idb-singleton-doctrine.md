# ADR-INFRA-005 — IDB Singleton Doctrine (IndexedDB Connection Sharing)

> **Status**: RATIFIED (auto-ratifié via fix V0.7.6 PROD 2026-06-23)
> **Owner**: A1 Morty (Focus opérationnel) · **Rédacteur**: A3 Spock (Areas L1)
> **Validateur**: A2 Picard (Projects captain)
> **Cycle**: Q3 2026 W2 (Item 8 Business OS par Life OS)
> **Anchor**: handoff_para_debug_resolved_2026-06-23.md §3

## 1. Contexte

Le bug PARA debug 2026-06-23 (handoff canon 473 lignes) a révélé que la classe
`DomainDB` dans `src/lib/idb.ts`capturait `this.db: IDBDatabase | null` à
l'instance level. Conséquences D6 observées :

1. **HMR Vite rebuild** crée une nouvelle instance `new DomainDB('aspace_ld01_business')`
   qui ouvre une **deuxième** connexion IDB sur la même base. La première connexion
   reste vivante → la nouvelle instance peut soit (a) bloquer sur `indexedDB.open()`
   (`onblocked`), soit (b) recevoir une `InvalidStateError` au `.transaction()` parce
   que `this.db` capture la connexion avant qu'elle ne soit fermée.

2. **Multi-instance pattern** (ld01DB + ld02DB + ... ld08DB exportés comme singletons
   module-level) masque le bug en dev mode, mais en prod build (Vite optimize + chunks)
   l'instanciation peut doubler si le bundle re-évalue les imports.

3. **Race condition observable** : après hard-refresh, `hydrate()` lit `null` items
   alors que IDB contient bien les 3 AaaS Variants canon.

## 2. Décision

**Doctrine IDB Singleton** : un module-level `Map<dbName, Promise<IDBDatabase>>`
garantit qu'une seule connexion IDB existe par nom de base à travers toutes les
instances `DomainDB`. Implémentation canon dans `src/lib/idb.ts` :

```typescript
const dbCache: Map<string, Promise<IDBDatabase>> = new Map();

class DomainDB {
  async init(): Promise<void> {
    if (this.db) return;
    let dbPromise = dbCache.get(this.dbName);
    if (!dbPromise) {
      dbPromise = new Promise<IDBDatabase>((resolve, reject) => { /* open IDB */ });
      dbCache.set(this.dbName, dbPromise);
    }
    this.db = await dbPromise;
  }
}
```

**Avantages** :
- 1 connexion IDB par `dbName` (ld01..ld08) quelque soit le nombre de `DomainDB` instanciés.
- HMR-safe (Vite rebuild ne duplique pas la connexion).
- `db.onclose` handler éjecte l'entrée cache → reconnexion propre après fermeture navigateur.
- `request.onblocked` rejette proprement (D6 no-silent-failure).

## 3. Alternatives rejetées

- **A: Lazy init à chaque appel `getAll`/`put`** — overhead × 8 LDs × N actions, bloquant.
- **B: WeakRef sur connexion IDB** — non supporté par TS 5.8 target esnext, source de bugs GC.
- **C: Pool de connexions** — IDB n'a pas de concept de pool, single-connection-only par base.

## 4. Conséquences

- `src/lib/idb.ts` ligne 4 : `dbCache` ajouté en module-level.
- `DomainDB.init()` réécrite (50 lignes → 35 lignes, plus simple).
- `request.onblocked` ajouté (D6 lesson : silent failure = anti-pattern).
- `db.onclose` handler → cache eviction (propre reconnect).

## 5. Tradeoffs acceptés

- **Tradeoff 1** : `dbCache` n'est jamais nettoyé manuellement → reste en mémoire
  jusqu'au page reload. Acceptable car 8 LDs × ~50KB metadata = ~400KB.
- **Tradeoff 2** : si une connexion IDB est fermée par le navigateur (quota, user
  action), `db.onclose` éjecte mais les instances existantes conservent leur
  `this.db` stale → forcer un reload. Acceptable (rare, recovery par refresh).

## 6. Critère de succès

- [x] Fix ship V0.7.6 commit `8f9ab59` pushé GitHub + Vercel auto-deploy
- [x] 0 erreur TS sur fichiers édités (`fw-para.store.ts` + `idb.ts`)
- [ ] Smoke test E2E post-deploy : refresh page Life-OS-2026 → 3 AaaS Variants visibles dans PARA
- [ ] Mesure : avant fix 0% hydratation, après fix 100% hydratation (3/3 items)

## 7. Anti-patterns interdits

- ❌ `this.db = null` à la fin d'une opération (casse le partage).
- ❌ `indexedDB.deleteDatabase(this.dbName)` depuis le store applicatif (D4 append-only).
- ❌ Catch-all silencieux autour de `request.onerror` (D6 root-cause canon).

## 8. Doctrine Anti-Paresse ancrage

- **D1** : bug confirmé par lecture source verbatim (lignes 41-75 idb.ts).
- **D2** : re-fix préalable nécessite lecture code source réel, pas théorie.
- **D3** : nuance = `this.db` était *techniquement* correct en single-instance, mais
  le pattern était *structurellement* fragile en multi-instance HMR.
- **D4** : `dbCache` est append-only, jamais reset (sauf onclose browser).
- **D6** : `InvalidStateError` aurait été le 6e re-fix sans lecture source.
- **D7** : 1 cycle debug → 1 fix racine au lieu de 5 patchs partiels (V0.7.0→V0.7.5).

## 9. Cross-refs

- ADR-INFRA-006 `hydrate-aggregate-8-lds-doctrine.md` (frère jumeau V0.7.6)
- `wiki/hand_offs/handoff_para_debug_resolved_2026-06-23.md` (closure canon)
- `src/lib/idb.ts` lignes 1-55 (implémentation V0.7.6)
- ADR-FRAMEWORK-002 `invariant-3-isolated-idb-per-area.md` (invariant originel)