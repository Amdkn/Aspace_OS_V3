---
source: A0 Amadeus (jumeau numérique)
date: 2026-06-23
type: handoff
domain: L1
tags: [para, debug, aaaS-variants, plustard-handoff, v0.7.5, life-os]
---

# PARA Debug Handoff — 3 AaaS Variants ne s'affichent pas (post V0.7.5)

> **D1 receipt** : 2026-06-23 — A0 Amadeus pivot « Ecrit le Handoff de debug de PARA pour Plustard ou une autre session car il n'affiche toujours pas mes 3 Projets »
> **Statut** : ⚠️ **RESOLVED par runtime A0 Phase 2 (2026-06-23 17:55 UTC)** — voir `handoff_para_debug_resolved_2026-06-23.md` et commit `8f9ab59` V0.7.6. Ce handoff est conservé comme **archive** des hypothèses + commands debug, mais le fix a été livré en parallèle par le sub-agent CC du runtime pilot.
> **Owner** : A0 (jumeau numérique, board observer passif)
> **Destinataire** : Plustard / prochaine session A2 Claude Code ou A3 Saru Sobriété
> **Pattern** : Debug handoff = transmettre le contexte COMPLET (état actuel, ce qui a été tenté, hypothèses non-testées, command de debug immédiat) pour qu'une autre session reprenne sans avoir à re-découvrir

---

## 1. Synthèse exécutive du bug

**Symptôme observé par A0** : Sur `https://life-os-2026-liart.vercel.app/` → onglet **PARA > PROJECTS**, l'empty state "NO ITEMS IDENTIFIED" s'affiche **même après** 5 itérations de fix (V0.7.0 → V0.7.5). Le bundle servi par Vercel contient bien le code canon (D1 vérifié par `curl + grep AAAS-SOLARIS` sur `assets/index-D8dxZR8D.js` puis `index-Bk4bc00H.js` puis `index-...js` après chaque deploy). Le code s'exécute mais les 3 cards n'apparaissent jamais de façon persistante.

**État actuel** : Build `dpl_86Z7U49SzvEEKSPkPegjbiSM8BeH` PROMOTED sur Vercel prod, code V0.7.5 servi, mais UI montre empty state. A0 a escaladé 5+ fois entre 2026-06-23 14:50 et 15:30 UTC, à chaque tour un fix différent a été tenté.

---

## 2. D1 Receipts — État du code V0.7.5 actuel

### 2.1 Store PARA — `src/stores/fw-para.store.ts` (205 lignes)

**Logique `hydrate()`** (lignes 91-142) :

```typescript
hydrate: async () => {
  try {
    const projectItems = await readFromLD<any>('ld01', 'projects');
    const resourceItems = await readFromLD<any>('ld01', 'resources');

    const idbProjects = (projectItems || []).filter((d: any) => d?.type === 'project' || d?.status);
    const CANON_IDS = ['AAAS-SOLARIS', 'AAAS-NEXUS', 'AAAS-ORBITER'];
    const missingCanon = CANON_IDS.filter(id => !idbProjects.some((p: any) => p.id === id));

    if (missingCanon.length > 0) {
      const canonSeeds: Project[] = [
        { id: 'AAAS-SOLARIS', title: 'Solaris AaaS — Solarpunk Kernel', status: 'active', domain: 'business', pillars: ['meta'], resources: [], progress: 30, updatedAt: now },
        { id: 'AAAS-NEXUS',   title: 'Nexus AaaS — OMK Business OS',    status: 'active', domain: 'business', pillars: ['operations', 'product'], resources: [], progress: 60, updatedAt: now },
        { id: 'AAAS-ORBITER', title: 'Orbiter AaaS — ABC Community OS', status: 'paused', domain: 'impact', pillars: ['people'], resources: [], progress: 25, updatedAt: now },
      ];
      for (const seed of canonSeeds) {
        await get().addProject(seed);
      }
      const refreshed = await readFromLD<any>('ld01', 'projects');
      const allIdbProjects = (refreshed || []).filter((d: any) => d?.type === 'project' || d?.status);
      set({
        projects: allIdbProjects as Project[],
        resources: (resourceItems || []).filter((d: any) => d?.type === 'resource') as Resource[],
        isHydrated: true
      });
      return;
    }
    set({ projects: idbProjects as Project[], ... });
  } catch (e) {
    console.error('[PARA Store] Hydration failed', e);
    set({ isHydrated: true });
  }
}
```

### 2.2 Lib IDB — `src/lib/idb.ts` (151 lignes) — **D6 ROOT CAUSE PROBABLE**

**Méthode `getAll()` lignes 41-75** :

```typescript
async getAll<T>(storeName: string): Promise<T[]> {
  await this.init();
  try {
    const { data: { session } } = await supabase.auth.getSession();
    const userId = session?.user?.id;

    if (!userId) throw new Error('Unauthenticated access');  // ⚠️ THROW silencieux

    const { data, error } = await supabase
      .from(this.tableName)
      .select('*')
      .eq('user_id', userId)
      .eq('type', storeName);
    
    if (!error && data) {
      // Push remote items to local IDB + return
      ...
      return data as T[];
    }
  } catch (e) {
    console.warn(`Sync failed for ${this.tableName}, falling back to local`, e);
  }
  // FALLBACK : IDB local seul
  return new Promise((resolve, reject) => {
    const transaction = this.db!.transaction(storeName, 'readonly');
    const store = transaction.objectStore(storeName);
    const request = store.getAll();
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}
```

**D6 ROOT CAUSE PROBABLE** : 

- `supabase.auth.getSession()` retourne `{ data: { session: null } }` si l'utilisateur frontend n'est pas authentifié (pas de flow login)
- `session?.user?.id` est donc `null`/`undefined`
- Le code throw `Error('Unauthenticated access')` AVANT d'écrire dans IDB
- Fallback IDB local retourne ce qui a été `put` (potentiellement vide ou en race window)

**Triple chaîne d'échecs** :

1. **Frontend non authentifié** → `userId = null` → throw `Unauthenticated` → fallback IDB local → retourne ce qui a été écrit localement
2. **Si IDB local n'a jamais reçu de `put` réussi** (par exemple `await this.init()` timeout) → retourne `[]`
3. **Même si `addProject → writeToLD → db.put` réussit localement**, le re-hydrate post-await via `readFromLD` peut avoir une race condition où `getAll` lit IDB avant que la transaction put soit commitée

### 2.3 Lib LD-Router — `src/lib/ld-router.ts` (152 lignes)

`readFromLD(ldId, store)` appelle `db.getAll<T>(store)` (ligne 114). `writeToLD(ldId, store, action, data, caller)` :

- Vérifie permissions `PERMISSIONS[caller]?.[ldId]?.includes('W')` — throw si non autorisé
- Pour `'para'` caller : `ld01..ld08` ont tous `['R', 'W']` ✅ (lignes 27-30)
- Appelle `db.put(store, data)` ou `db.delete(store, data.id)`

### 2.4 App PARA — `src/apps/para/ParaApp.tsx`

Lignes 53-58 :

```typescript
useEffect(() => {
  if (!isHydrated) {
    hydrate();
  }
}, [isHydrated, hydrate]);
```

Hydrate appelé UNE fois au mount si pas déjà hydraté.

### 2.5 Mapping domain → LD (vérifié D3 nuance)

`src/utils/paraAdapter.ts` lignes 11-15 :

```typescript
export const DOMAIN_TO_LD: Record<string, LDId> = {
  business: 'ld01', finance: 'ld02', health: 'ld03', cognition: 'ld04',
  relations: 'ld05', habitat: 'ld06', creativity: 'ld07', impact: 'ld08'
};
```

Donc :
- AAAS-SOLARIS (domain='business') → écrit dans `ld01` → DB `aspace_ld01_business`, store `projects`
- AAAS-NEXUS (domain='business') → idem ld01
- AAAS-ORBITER (domain='impact') → écrit dans `ld08` → DB `aspace_ld08_impact`, store `projects`

**D3 nuance critique** : `hydrate()` lit **uniquement `ld01`** (`readFromLD<any>('ld01', 'projects')`). Si l'IDB `ld01` contient AAAS-SOLARIS + AAAS-NEXUS mais l'IDB `ld08` contient AAAS-ORBITER, le re-hydrate **lit 2 items au lieu de 3** car Orbiter est dans une autre DB.

Mais le `set` final après amorce écrit `allIdbProjects` venant de `ld01` uniquement → **Orbiter manque du state Zustand même s'il existe en IDB**.

---

## 3. Historique des tentatives V0.7.0 → V0.7.5

### V0.7.0 (commit `c36a138`) — Pattern canon 12WY

**Intent** : Migrer store PARA du `zustand/middleware persist` (localStorage) vers pattern `isHydrated + hydrate() async` comme `useTwelveWeekStore`.

**Code livré** : `useParaStore` avec `hydrate()` qui lit IDB, plus aucun hardcoded seed. `ParaApp.tsx` useEffect appelle `hydrate()` au mount.

**Résultat** : Empty state honnête "NO ITEMS IDENTIFIED" (avant ça, des seeds hardcodés "Pépites" 3.5.0+ s'affichaient toujours).

### V0.7.1 (commit `bd7349d`) — Bouton Amorcer

**Intent (A0)**: "PARA est complètement vide" → ajout d'un bouton "+ AMORCER 3 AaaS Variants" dans l'empty state.

**Code livré** : Bouton qui appelle `addProject()` × 3.

**Rejeté par A0** : "je ne veux jamais appuyer de bouton dans GTD et DEAL" → cohérence canon → revert.

### V0.7.2 (commit `7fd754f`) — Revert bouton

**Code livré** : Empty state honnête sans bouton, identique GTD/DEAL.

**Résultat** : Mêmes symptômes.

### V0.7.3 (commit `d3afe2b`) — One-shot bootstrap avec flag localStorage

**Intent** : Auto-amorce invisible au premier load, jamais plus.

**Code livré** : `hydrate()` check `idbProjects.length === 0 && localStorage['aspace_para_canon_bootstrap_v1'] !== 'done'` → amorce 3 seeds via `addProject` + set flag.

**Bug A0 observé** : Bootstrap ne se déclenche pas (probablement parce que `idbProjects.length > 0` à cause d'un item user-created leftover, OU flag `done` set sans amorce effective).

### V0.7.4 (commit `666aa31`) — Bootstrap idempotent par ID

**Intent** : Changer condition de `idbProjects.length === 0` à `missingCanon.length > 0` (où missingCanon = AAAS-* absents).

**Code livré** : Bootstrap idempotent — déclenche si **n'importe lequel** des 3 IDs canon manque.

**Bug A0 observé** : "Après le hard refresh les projets se sont afficher l'espace d'1 second avant de disparaitre" → race condition.

### V0.7.5 (commit `95c5eb5`) — Race condition fix (loop addProject séquentiel + re-sync)

**Intent** : Éliminer race où re-hydrate post-await écrase avec IDB pas encore commité.

**Code livré** : `await addProject(seed)` séquentiel, puis re-sync final avec `readFromLD` post-loop.

**Bug A0 observé** : "Toujours Rien" → cards persistent pas.

---

## 4. D6 Hypothèses ordonnées (probabilité décroissante)

### H1 (probabilité 70%) — Session Supabase absente throw `Unauthenticated access` avant `db.put`

**Symptôme prédit** : Console browser affiche `[PARA Store] Unauthenticated access` ou `Sync failed for ld01_business`. IDB local jamais écrit. `set projects = []` (idbProjects vide).

**Test à faire** : Ouvrir DevTools Console sur `https://life-os-2026-liart.vercel.app/`, hard refresh, chercher `Unauthenticated access` ou warnings `Sync failed`.

**Fix proposé** : 
- Option A (court terme) : Dans `idb.ts:getAll()`, ne pas throw si `!userId`, juste skip la sync Supabase et retourner IDB local direct (sans le try/catch wrapper qui swallow les erreurs).
- Option B (moyen terme) : Ajouter un flow d'auth auto-anonyme Supabase (`supabase.auth.signInAnonymously()`) dans `App.tsx` mount.

### H2 (probabilité 50%) — DOMAIN_TO_LD split fait que Orbiter écrit dans ld08 mais `hydrate()` ne lit que ld01

**Symptôme prédit** : Seul 2 cards visibles (Solaris + Nexus depuis ld01) ou 0 cards (si ld01 vide + ld08 contient Orbiter mais non lu).

**Test à faire** : Inspecter IDB Chrome DevTools → Application → IndexedDB → `aspace_ld01_business` → `projects` store et `aspace_ld08_impact` → `projects` store. Compter combien d'items chacun.

**Fix proposé** : Changer `hydrate()` pour lire TOUS les 8 LDs et merger les items :

```typescript
const allDomains: LDId[] = ['ld01','ld02','ld03','ld04','ld05','ld06','ld07','ld08'];
const projectArrays = await Promise.all(
  allDomains.map(ld => readFromLD<any>(ld, 'projects'))
);
const idbProjects = projectArrays.flat().filter(d => d?.type === 'project' || d?.status);
```

### H3 (probabilité 30%) — Permissions `PERMISSIONS[caller]` throw pour 'para' caller

**Symptôme prédit** : Console affiche `Permission Denied: para cannot write to ldXX` (ou silencieux si `getAll` swallow).

**Test à faire** : Console browser, chercher `Permission Denied`.

**Fix proposé** : Vérifier que `'para'` caller a bien `W` sur tous les LDs. D1 vérifié dans §2.3 = OK.

### H4 (probabilité 15%) — Race condition entre addProject put + getAll

**Symptôme prédit** : Cards s'affichent 1 sec puis disparaissent (ce qu'A0 a observé à V0.7.4).

**Test à faire** : Network tab ralentir throttling à Slow 3G, observer si cards persistent plus longtemps.

**Fix proposé** : V0.7.5 devrait fix — si toujours présent, ajouter un `setTimeout(100)` avant re-hydrate post-amorce pour laisser IDB commit.

### H5 (probabilité 10%) — Domain `business` n'existe pas dans DOMAIN_TO_LD lookup

**Symptôme prédit** : `addProject` skip le writeToLD si `DOMAIN_TO_LD[p.domain]` est undefined. Mais V0.7.5 mapping inclut `'business'` → `'ld01'` ✅.

**Test à faire** : N/A, mapping OK.

### H6 (probabilité 5%) — Le composant utilise un autre store que `useParaStore`

**Symptôme prédit** : `useParaStore` n'est pas le store utilisé par ParaApp. D1 vérifié ParaApp.tsx ligne 3 `import { useParaStore, type Project } from '../../stores/fw-para.store'` ✅.

### H7 (probabilité 5%) — Le filtre `activeLdFilter !== 'all'` cache les items

**Symptôme prédit** : `domainMatch` filter ligne 62 exclut items si domain mismatch. Mais `activeLdFilter='all'` par défaut, et aucun user action sur le filter dans cette session.

---

## 5. D2 Commands de debug à exécuter IMMÉDIATEMENT

### 5.1 Ouvrir DevTools Console (30 sec)

1. Naviguer vers `https://life-os-2026-liart.vercel.app/`
2. Hard refresh (Ctrl+Shift+R)
3. F12 → Console tab
4. Filter sur `[PARA Store]` et `[LD-Router]` et `Unauthenticated`
5. **D1 receipts à copier-coller dans Plustard** :
   - Si `Unauthenticated access` apparaît → **H1 confirmée**, fix Option A ci-dessous
   - Si `Permission Denied: para` apparaît → H3 confirmée
   - Si aucun warning → H2/H4 plus probables, passer à §5.2

### 5.2 Inspecter IndexedDB Chrome DevTools (60 sec)

1. F12 → Application tab → Storage → IndexedDB → `https://life-os-2026-liart.vercel.app`
2. Chercher `aspace_ld01_business` et `aspace_ld08_impact`
3. Expand `aspace_ld01_business` → `projects` object store → lire entries
4. **D1 receipts** :
   - Si `AAAS-SOLARIS` et `AAAS-NEXUS` présents → amorce a marché, mais display fail
   - Si `AAAS-ORBITER` absent de ld01 et présent dans ld08 → **H2 confirmée**, fix ci-dessous
   - Si 0 entries partout → **H1 confirmée**, `db.put` n'a jamais écrit

### 5.3 Inspecter Supabase Auth state (45 sec)

1. F12 → Application tab → Local Storage → `https://life-os-2026-liart.vercel.app`
2. Chercher clé `sb-hjweyhpmrxqsxfbibsnc-auth-token`
3. **D1 receipts** :
   - Clé absente → **H1 confirmée**, frontend jamais authentifié
   - Clé présente mais `expires_at < now` → token expiré

### 5.4 Console eval direct (10 sec)

```javascript
// Console browser, taper:
await supabase.auth.getSession()
```

**D1 receipts** : `{ data: { session: null }, error: null }` → H1 confirmée.

---

## 6. Fix proposé (à valider avec §5 avant d'éditer)

### Fix A (H1, court terme, 10 min) — Skip auth dans `idb.ts:getAll`

```typescript
// AVANT (idb.ts lignes 41-75)
async getAll<T>(storeName: string): Promise<T[]> {
  await this.init();
  try {
    const { data: { session } } = await supabase.auth.getSession();
    const userId = session?.user?.id;
    if (!userId) throw new Error('Unauthenticated access');
    // ... supabase query
  } catch (e) {
    console.warn(...);
  }
  // fallback IDB
}

// APRÈS
async getAll<T>(storeName: string): Promise<T[]> {
  await this.init();
  // Si user_id connu, tente sync Supabase (best-effort)
  try {
    const { data: { session } } = await supabase.auth.getSession();
    const userId = session?.user?.id;
    if (userId) {
      const { data, error } = await supabase
        .from(this.tableName)
        .select('*')
        .eq('user_id', userId)
        .eq('type', storeName);
      if (!error && data) {
        // sync to IDB
        ...
        return data as T[];
      }
    }
    // Pas de user_id OU query Supabase fail → fallback IDB local
  } catch (e) {
    console.warn(`Sync failed for ${this.tableName}`, e);
  }
  return new Promise(...); // fallback IDB local
}
```

**D5 vérification** : Garantit que `getAll` retourne TOUJOURS ce qui est en IDB local, même sans auth Supabase.

### Fix B (H2, court terme, 5 min) — Lire TOUS les 8 LDs dans `hydrate()`

```typescript
// fw-para.store.ts hydrate() lignes 95-100
const allDomains: LDId[] = ['ld01','ld02','ld03','ld04','ld05','ld06','ld07','ld08'];
const projectArrays = await Promise.all(
  allDomains.map(ld => readFromLD<any>(ld, 'projects'))
);
const projectItems = projectArrays.flat().filter(d => d != null);
// idem pour resources
```

**D5 vérification** : Merge tous les projects depuis tous les LDs.

### Fix C (H1 long terme, 1h) — Auth anonyme Supabase dans App mount

Dans `App.tsx` ou `main.tsx`, au mount :

```typescript
import { supabase } from './lib/supabase';

useEffect(() => {
  supabase.auth.signInAnonymously().catch(console.warn);
}, []);
```

Crée un user anonyme Supabase avec UUID, persiste dans `localStorage` (`sb-*-auth-token`), toutes les `getAll` futures trouvent `userId`.

---

## 7. ADR candidats à ratifier post-fix

| ADR ID | Sujet | Statut |
|---|---|---|
| `ADR-INFRA-005` | IDB-first Offline Doctrine : IDB est source de vérité locale, Supabase sync best-effort | **PROPOSED 2026-06-23** — ratify après Fix A |
| `ADR-FEAT-002` | Auth Anonyme Auto-Supabase pour frontend Vite sans login | **PROPOSED 2026-06-23** — ratify après Fix C |

---

## 8. Lessons shipped (D4 append-only)

1. **IDB `db.put` est async mais IDBTransaction est sync** : `transaction.objectStore.put` est enqueue sur la transaction, mais le commit arrive à la fin du microtask. Si on appelle `getAll` dans le même microtask, il peut voir un état stale.

2. **Frontend sans auth → `getAll` swallow silencieux** : Le `try/catch` autour du bloc Supabase cache le throw `Unauthenticated`. Visible uniquement en console (warning `Sync failed`).

3. **Mapping `domain → LD` split l'état des projects** : Un item domain='business' va dans ld01, domain='impact' va dans ld08. Si `hydrate()` ne lit que ld01, les items domain='impact' sont invisibles. Faille design, pas bug isolé.

4. **LocalStorage vs IDB vs Supabase : 3 sources, 1 canon par contexte** : Pour mode local-first offline, IDB est canon. Pour mode cloud-first multi-device, Supabase est canon. Le code actuel mélange les 3 modes sans stratégie claire.

---

## 9. Plan d'action Plustard / prochaine session

**Étape 1** (5 min) : Exécuter §5 commands debug. Copier-coller console output ici.

**Étape 2** (selon résultat §5) :
- Si H1 confirmée → appliquer Fix A (10 min), build, deploy, verify A0
- Si H2 confirmée → appliquer Fix B (5 min), build, deploy, verify A0
- Si H1 + H2 → Fix A + Fix B ensemble (15 min)
- Si ni H1 ni H2 → investiguer §4 autres hypothèses (rare)

**Étape 3** (post-fix) : Écrire un post-mortem dans `wiki/hand_offs/handoff_para_debug_resolved_<DATE>.md` avec D1 receipts du fix effectif.

---

## 10. Annexes — D1 receipts verbatim état 2026-06-23 15:32 UTC

### 10.1 Git log PARA history (8 commits)

```
95c5eb5 fix(para): V0.7.5 — race condition fix: set optimiste + re-sync post-await
666aa31 fix(para): V0.7.4 — idempotent canon bootstrap (skip if AAAS-* already in IDB)
d3afe2b feat(para): V0.7.3 — one-shot canon bootstrap 3 AaaS Variants on first hydrate
68b4b91 chore: trigger Vercel redeploy to re-link production domain after liart re-add
1091877 chore: trigger Vercel redeploy after project rename life-os-2026 -> life-os
7fd754f revert(para): V0.7.2 — remove Amorcer button, follow GTD/DEAL canon (no buttons in empty state)
bd7349d feat(para): V0.7.1 — Amorcer 3 AaaS Variants button in empty state
c36a138 refactor(para): V0.7.0 — D6 fix migrate to 12WY pattern (isHydrated + hydrate from IDB)
```

### 10.2 Vercel deploys PARA history

| Deploy | Commit | Status | Alias |
|---|---|---|---|
| `dpl_86Z7U49SzvEEKSPkPegjbiSM8BeH` | `95c5eb5` V0.7.5 | READY+PROMOTED | `life-os-2026-liart.vercel.app` (aliasAssignedAt `1782242987927`) |
| `dpl_AekzMPdF1VidzAox7AcSs9uRQZUR` | `666aa31` V0.7.4 | READY+PROMOTED | idem |
| `dpl_ApaNT9B4yfBHgSAwyFvL3PuCnwg6` | `d3afe2b` V0.7.3 | READY+PROMOTED | idem |

### 10.3 Bundle Vercel vérifié contient AAAS-SOLARIS

```
$ curl -s "https://life-os-2026-liart.vercel.app/assets/index-Bk4bc00H.js" | grep -oE 'AAAS-SOLARIS'
AAAS-SOLARIS  ← code V0.7.5 servi
```

### 10.4 Pas de logs canon wiki pour ce debug

`wiki/log.md` ne contient **pas encore** d'entrée traçant ce debug spécifique (à ajouter post-fix). Recherche `grep "PARA.*debug\|PARA.*auth\|Unauthenticated" wiki/log.md` = 0 match.

---

## 11. Notes pour Plustard

**Contexte A0** : A0 est en mode méta-orchestration, ne debugge pas lui-même. Il attend que A2 Claude Code ou A3 Saru Sobriété applique les fixes proposés. D7 cost-of-escalation = ne PAS re-poser les questions, appliquer le fix basé sur §5 output.

**Préférence A0 confirmée** : "Plus de bouton" — ne pas ajouter de UI CTA. Fix backend uniquement.

**État émotionnel A0** : 5+ escalades successives sur le même bug. Frustration croissante. D8 cross-agent = work verified, pas de justification.

**Bonne pratique** : Commit + push + Vercel deploy doit être une opération atomique. Pas de "fix partiel" qui nécessite 3 retries pour confirmer.

---

## 12. Auteur + traçabilité

**Auteur** : A0 Amadeus (méta-orchestration) · **Date** : 2026-06-23 · **Cycle** : Q3 2026 W2 · **Statut** : OPEN DEBUG — fixation reportée à Plustard / prochaine session
**Prochaine revue** : post-fix (closure par `handoff_para_debug_resolved_<DATE>.md`)
**Append wiki/log.md** : à faire APRÈS livraison finale du fix
