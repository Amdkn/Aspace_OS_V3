# RUBAN φ — ASP-951 M4 : AsyncMessages.create monkey-patch

> Work 11 (uc.db, layer L0). Ruban complet — test binaire : un constructeur
> peut exécuter ce travail de bout en bout **sans poser une seule question**.

## 1. Contexte mesuré

- `AsyncMessages` n'existe nulle part sur le disque `C:/Users/amado` (vérifié
  par ripgrep global le 2026-09-02, zéro résultat). Le projet ASP-951 M4
  n'existait pas localement.
- Le ruban d'origine (`C:/Users/amado/AppData/Local/Temp/multica-task-396254240/spec-loop__nodejs-port.md`,
  tape_id=4) est disparu — Temp purgé.

## 2. Décision : projet autonome minimal

Le ruban cible le projet autonome **`C:/Users/amado/ASpace_OS_V3/30_Business_OS/asp951-m4/`**,
créé le 2026-09-02, qui implémente AsyncMessages (sync + async) avec tests
Vitest. Fichiers :

| Chemin | Rôle |
|---|---|
| `src/async-messages.js` | classe `AsyncMessages` : `createSync()` (version synchrone préservée) + `create()` (asynchrone) |
| `src/monkey-patch.js` | exporte `IDEMPOTENCY_KEY` (Symbol) et `installIdempotentCreate(instance)` |
| `tests/async-messages.test.js` | couverture Vitest (5 tests) |
| `package.json` | `npm test` → `vitest run`, vitest ^2.1.9 |

## 3. Spécification du monkey-patch

1. **Symbole d'idempotence distinct** : `Symbol('AsyncMessages.didempotence')`.
   Non énumérable, non sérialisable, impossible à entrer en collision avec une
   propriété métier. Vérifiable par import : `IDEMPOTENCY_KEY`.
2. **Idempotence du patch** : `installIdempotentCreate(instance)` retourne
   `false` et ne ré-applique pas si `instance[IDEMPOTENCY_KEY] === true`.
3. **Coexistence avec la version synchrone** : `createSync()` n'est **jamais
   touché** — aucune modification de sa signature, de son retour, ni de son
   comportement. Le patch ne remplace que `create()`.
4. **Le `create` patché reste asynchrone** : il retourne une promesse qui
   résout le message (délégation à l'original lié avant remplacement).

## 4. Couverture Vitest requise (toutes obligatoires)

- `createSync` retourne un message avec `id` et `created_at` (préservation).
- `create` non patché retourne une promesse qui résout un message.
- `IDEMPOTENCY_KEY` est un symbole, `instance[IDEMPOTENCY_KEY] === true` après
  patch, et absent de `Object.keys(instance)`.
- `create` patché reste asynchrone et fonctionnel.
- Double application du patch : aucune duplication, retour `false` la 2e fois.

## 5. Critères de réussite exécutables

```bash
cd C:/Users/amado/ASpace_OS_V3/30_Business_OS/asp951-m4 && npm test
# Attendu : vitest run — 1 fichier, 5 tests passés, code de sortie 0

# Vérification du symbole distinct (rc 0 attendu) :
node -e "const {AsyncMessages}=require('./src/async-messages.js');const {IDEMPOTENCY_KEY,installIdempotentCreate}=require('./src/monkey-patch.js');const m=new AsyncMessages();console.assert(typeof IDEMPOTENCY_KEY==='symbol');installIdempotentCreate(m);console.assert(m[IDEMPOTENCY_KEY]===true);console.assert(!installIdempotentCreate(m));console.log('OK')"
```

**État au moment de l'écriture du ruban (mesuré, 2026-09-02)** : les deux
critères sont déjà satisfaits — `npm test` : 5/5 passés, rc=0 ; vérification
du symbole : OK, rc=0.

## 6. Défaire

```bash
rm -rf C:/Users/amado/ASpace_OS_V3/30_Business_OS/asp951-m4
```
puis rétablir `tape_id=4` sur le work 11 dans `uc.db` (le ruban disparu).
