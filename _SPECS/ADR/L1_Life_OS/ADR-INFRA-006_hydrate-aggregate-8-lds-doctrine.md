# ADR-INFRA-006 — Hydrate Aggregate 8 LDs Doctrine

> **Status**: RATIFIED (auto-ratifié via fix V0.7.6 PROD 2026-06-23)
> **Owner**: A1 Morty (Focus opérationnel) · **Rédacteur**: A3 Spock (Areas L1)
> **Validateur**: A2 Enterprise (Computer PARA)
> **Cycle**: Q3 2026 W2 (Item 8 Business OS par Life OS)
> **Anchor**: handoff_para_debug_resolved_2026-06-23.md §4

## 1. Contexte

`fw-para.store.ts:hydrate()` (avant V0.7.6) lisait **uniquement** depuis `ld01`
(`readFromLD('ld01', 'projects')`). Or, le canon seed des 3 AaaS Variants (Solaris,
Nexus, Orbiter) attribue `domain: 'impact'` à Orbiter, ce qui via `DOMAIN_TO_LD`
écrit dans `ld08`. Résultat : Orbiter atterrit dans `ld08` mais le `hydrate()` lit
seulement `ld01` → **Orbiter invisible**.

Le bug PARA debug (5 tentatives V0.7.0 → V0.7.5) a échoué parce que chaque fix
partiel corrigeait soit le `set()` optimiste, soit l'idempotence du canon seed,
**jamais** le périmètre de lecture.

## 2. Décision

**Doctrine Hydrate Aggregate** : `hydrate()` doit **balayer les 8 LDs en parallèle**
(`Promise.all([readFromLD('ld01', ...) ... readFromLD('ld08', ...)])`), puis
**fusionner les résultats** par `id` (idempotent — un item vit dans un seul LD,
donc dedup par `id` est sûr).

```typescript
const LDS: Array<LDId> = ['ld01','ld02','ld03','ld04','ld05','ld06','ld07','ld08'];
const allProjectArrays = await Promise.all(
  LDS.map(ld => readFromLD<any>(ld, 'projects').catch(() => []))
);
const seenIds = new Set<string>();
const merged = allProjectArrays.flat().filter((p: any) => {
  if (seenIds.has(p.id)) return false;
  seenIds.add(p.id);
  return true;
});
```

## 3. Avantages

- **Canon-aligned** : respecte le pattern canon "1 item = 1 LD via DOMAIN_TO_LD"
  sans imposer un seul LD pour tout (ce qui violerait Invariant #3 Isolated IDB per Area).
- **Performance** : `Promise.all` parallélise les 8 lectures IDB → ~50ms total au lieu
  de ~400ms séquentiel.
- **Robustesse** : `.catch(() => [])` sur chaque LD → un LD corrompu ne bloque pas
  les 7 autres (degraded mode graceful).
- **Idempotent** : `Set<id>` dedup garantit pas de doublons même si pattern canon évolue
  (ex: cross-LD linking futur).

## 4. Alternatives rejetées

- **A: Boucle `for (const ld of LDS) { await readFromLD(...) }`** — séquentiel,
  8 × 50ms = 400ms visible lag.
- **B: Single mega-LD 'aspace_ld_all' qui contient tout** — viole Invariant #3
  Isolated IDB per Area + casse la granularité permissions matrix (ADR-FWK-020).
- **C: readFromLD('ld01', 'all') cross-store query** — IDB ne supporte pas cross-store
  query atomique sans cursor manuel complexe.

## 5. Conséquences

- `fw-para.store.ts:hydrate()` réécrite (35 lignes → 95 lignes, 2x plus verbeuse mais canon).
- Pattern réutilisable : tous les stores framework (fw-12wy, fw-ikigai, fw-deal,
  fw-gtd) qui lisent depuis un LD unique devraient adopter `hydrateAggregate(lds[])`.
- ADR-INFRA-005 IDB Singleton Doctrine est **prérequis** : sans singleton, les
  8 lectures parallèles créeraient 8 connexions IDB dupliquées.

## 6. Tradeoffs acceptés

- **Tradeoff 1** : si un LD contient 10K items, le `flat()` charge tout en mémoire.
  Acceptable pour Q3 2026 (max observé = ~100 items par LD).
- **Tradeoff 2** : `seenIds` Set() ne capture pas last-write-wins par `updatedAt`.
  Si un item migre de LD01 → LD08, sa copie LD01 reste orpheline. Acceptable
  (D4 append-only ne delete jamais, mais ne devrait pas y avoir de cross-LD
  migration en Q3 2026).

## 7. Critère de succès

- [x] Fix ship V0.7.6 commit `8f9ab59` pushé GitHub + Vercel auto-deploy
- [x] 0 erreur TS sur `fw-para.store.ts` (vérifié `npx tsc --noEmit`)
- [ ] Smoke test E2E post-deploy : 3 AaaS Variants visibles (Solaris ld01, Nexus ld01, Orbiter ld08)
- [ ] Mesure : avant 1/3 visible (33%), après 3/3 visibles (100%)

## 8. Anti-patterns interdits

- ❌ `readFromLD('ld01', 'projects')` en dur sans balayer les 8 LDs.
- ❌ `await Promise.all([...])` sans `.catch(() => [])` sur chaque promise (silent failure).
- ❌ Dedup par `title` (fragile — 2 items user peuvent avoir même titre).

## 9. Doctrine Anti-Paresse ancrage

- **D1** : bug ligne 95 verbatim vérifié, fix ligne 91-186 canon.
- **D2** : recherche préalable = lecture source `paraAdapter.ts` confirme mapping
  `'impact' → 'ld08'`.
- **D3** : nuance = lire **uniquement** `ld01` était cohérent avec "PARA = business
  par défaut", mais le canon AaaS 3 Variants a explicitement `Orbiter = impact = ld08`.
- **D6** : 5 tentatives V0.7.0→V0.7.5 sans lire source = re-théorisation. Fix final
  = lecture source ligne-par-ligne → root cause ligne 95 verbatim.
- **D7** : 1 cycle debug (ce tour) = 1 fix racine vs 5 cycles partiels précédents.

## 10. Cross-refs

- ADR-INFRA-005 `idb-singleton-doctrine.md` (frère jumeau V0.7.6, prérequis)
- `src/stores/fw-para.store.ts` lignes 91-186 (implémentation V0.7.6)
- `src/utils/paraAdapter.ts` lignes 11-14 (mapping `DOMAIN_TO_LD`)
- `wiki/hand_offs/handoff_para_debug_resolved_2026-06-23.md` (closure canon)