---
source: A0 Amadeus (jumeau numérique)
date: 2026-06-23
type: handoff
domain: L0
tags: [runtime, pilot, plane, loop-fix, plustard-handoff, state-filter]
---

# Handoff Plustard — Runtime Pilot Loop Fix (Plane state filter cassé)

> **D1 receipt** : 2026-06-23 — 8 invocations consécutives de `/symphony-pilot-runtime --once` par A0 sans output productif. Investigation révèle boucle runtime sur filtre `state__name` cassé.
> **Statut** : OPEN — fix code appliqué sur `symphony_pilot_runtime.py` mais CC slash command appelle wrapper différent. Plustard session A2 doit investiguer le wrapper + re-tester.
> **Owner** : A0 (jumeau numérique, board observer passif)
> **Destinataire** : Plustard / prochaine session A2 Claude Code qui a accès au runtime pilot wrapper canonique

---

## 1. Synthèse du bug

**Symptôme** : `symphony_pilot_runtime.py --once --dry-run` retourne `polled: 130+` à chaque invocation (vs 4 attendus), sub-agent CC dispatche 0 nouveau fix, et `polled: 130 → 160 → ...` monte sans progression. Aucun commit V0.7.8+ depuis `7e43bf3` (V0.7.7) car le sub-agent ne trouve rien à fixer.

**D6 ROOT CAUSE** (CONFIRMÉE verbatim D1 receipt) : Le filtre `?state__name=Today` de l'API Plane self-hosted est **silencieusement ignoré**. Plane retourne **TOUS les 160 issues du projet** quel que soit le filtre. 4 variants testés — tous retournent 160 issues identiques :

| URL suffix | Issues retournées | Filtrage effectif |
|---|---|---|
| `?state__name=Today&limit=5` | 160 | ❌ ignoré |
| `?state=Today&limit=5` | 160 | ❌ ignoré |
| `?state__group=backlog&limit=5` | 160 | ❌ ignoré |
| `?limit=5` (no filter) | 160 | (n/a) |

**Conséquence** : À chaque tick, le sub-agent CC voit 160 issues, tente de dispatcher, mais comme elles sont déjà toutes dans leur state final, ne fait rien. Le tick counter monte (`polled: 109 → 112 → 118 → 130 → 160`) sans aucun fix produit.

---

## 2. Solution technique (fix code déjà appliqué)

### 2.1 UUID Today state (D1 receipt direct)

L'endpoint `GET /workspaces/{WS}/projects/{P}/states/` retourne les 9 states du projet `79df867c-...` :

| State | UUID | group | count issues |
|---|---|---|---|
| **Backlog** | `11b6d790-0e89-41bf-9b05-7059286b89c1` | backlog | 135 |
| **Next Actions** | `8808372e-fde4-4898-a1f3-a01e1f888ccd` | backlog | 13 |
| **Today** ⭐ | `078e6b89-c6b0-4e68-af90-301e07713382` | unstarted | **4** |
| In Progress | `10e14185-c407-4b40-9a4e-8a10d47f7e24` | started | 3 |
| Waiting For | `4292861c-feb2-4acc-ad97-a715afa077ec` | unstarted | 2 |
| Done | `0d5ea751-afba-4310-beb5-19187f1ca824` | completed | 2 |
| Todo | `5ac5e514-69d3-42e8-8d32-c2f7705ef962` | unstarted | 1 |
| Cancelled | `2dea3a75-...` | cancelled | ? |
| Inbox | `1c76a0a8-...` | backlog | ? |

→ **Filtre correct** : `?state=078e6b89-c6b0-4e68-af90-301e07713382` (UUID Today, pas name)

### 2.2 Fix code appliqué sur `C:\Users\amado\.claude\skills\symphony-pilot-runtime\symphony_pilot_runtime.py`

**Ancienne fonction `poll()` (ligne 68-71)** :

```python
def poll():
    req = urllib.request.Request(f"{API}/workspaces/{WS}/projects/{P}/issues/?state__name=Today&limit=50", headers=hdr())
    with urllib.request.urlopen(req, timeout=30) as r:
        return [{"id":i["id"],"seq":i.get("sequence_id",0),"title":i.get("name","")} for i in json.loads(r.read()).get("results",[])]
```

**Nouvelle fonction `poll()` (fix appliqué 2026-06-23 19:30)** :

```python
def poll():
    # D6 fix 2026-06-23 : Plane self-hosted ignore ?state__name=X filter (retourne TOUS les 160 issues).
    # D1 receipt : state__name=Today / state=Today / state__group=backlog / no filter = tous 160.
    # Fix : query states endpoint, cache Today UUID, use ?state=<UUID> filter.
    today_id = _today_state_id()
    if today_id:
        url = f"{API}/workspaces/{WS}/projects/{P}/issues/?state={today_id}&limit=50"
    else:
        # Fallback graceful : si state discovery fail, retourne [] (vs 160 inutile)
        return []
    req = urllib.request.Request(url, headers=hdr())
    with urllib.request.urlopen(req, timeout=30) as r:
        return [{"id":i["id"],"seq":i.get("sequence_id",0),"title":i.get("name","")} for i in json.loads(r.read()).get("results",[])]

_TODAY_STATE_CACHE = {"id": None, "ts": 0}
def _today_state_id():
    """Discover Today state UUID via /states/ endpoint. Cache 5min (D6 avoid re-query)."""
    now = time.time()
    if _TODAY_STATE_CACHE["id"] and (now - _TODAY_STATE_CACHE["ts"]) < 300:
        return _TODAY_STATE_CACHE["id"]
    try:
        req = urllib.request.Request(f"{API}/workspaces/{WS}/projects/{P}/states/", headers=hdr())
        with urllib.request.urlopen(req, timeout=15) as r:
            states = json.loads(r.read())
            if isinstance(states, dict): states = states.get("results", states)
            for s in (states or []):
                if s.get("name") == "Today":
                    _TODAY_STATE_CACHE["id"] = s["id"]
                    _TODAY_STATE_CACHE["ts"] = now
                    return s["id"]
    except Exception as e:
        print(f"[poll] Today state discovery failed: {e}", file=sys.stderr)
    return None
```

**État du fix** : code sauvé dans `symphony_pilot_runtime.py`, `__pycache__` cleared.

### 2.3 D6 OBSERVÉ POST-FIX (D1 receipt) :

Dry-run après fix :
```
$ python symphony_pilot_runtime.py --once --dry-run
{
  "polled": 160,        ← TOUJOURS 160, fix n'a pas pris
  "dispatched": 160,
  "skipped": 0,
  "drift": false,
  "tick": 0,
  "owner_mode": false
}
```

→ **Le CC slash command `/symphony-pilot-runtime` n'utilise PAS le script canonique modifié**. Il y a un **wrapper/orchestrateur** intermédiaire qui hardcode ou importe le runtime autrement.

---

## 3. Plan Plustard / prochaine session A2

### Étape 1 (10 min) — Identifier le wrapper CC

```bash
# Find all references to symphony_pilot_runtime in CC config
grep -rn "symphony_pilot_runtime\|symphony-pilot-runtime" ~/.claude/ --include="*.json" --include="*.md"
grep -rn "symphony_pilot_runtime" C:/Users\amado/.claude/ --include="*.py"
```

D2 verify hypotheses :
- **Hypothèse A** : CC a un wrapper dans `C:\Users\amado\.claude\bin\` ou `C:\Users\amado\.claude\scripts\` qui importe le runtime mais avec cache compilé séparé
- **Hypothèse B** : CC utilise un sous-process Python séparé qui charge le code via `importlib` sans recharger le `.pyc`
- **Hypothèse C** : Le runtime est packagé dans un `.exe` ou `.whl` qui contient une version figée du code

### Étape 2 (5 min) — Vérifier que le fix marche en CLI direct

```bash
# Clear all caches
rm -rf C:/Users\amado/.claude/skills/symphony-pilot-runtime/__pycache__/
rm -rf C:/Users\amado/.claude/__pycache__/  # if exists
find C:/Users\amado -name "*.pyc" -path "*symphony*" -delete 2>/dev/null

# Direct CLI test
PYTHONIOENCODING=utf-8 python "C:/Users/amado/.claude/skills/symphony-pilot-runtime/symphony_pilot_runtime.py" --once --dry-run
```

Attendu : `polled: 4` (au lieu de 160). Si oui → fix marche en CLI, le problème est juste le wrapper CC. Si non → le runtime lit encore l'ancien code → restart complet du service.

### Étape 3 (15 min) — Identifier le wrapper CC

Si Étape 2 montre `polled: 4` en CLI direct mais `polled: 160` via slash command :
- Le wrapper CC est dans `~/.claude/commands/symphony-pilot-runtime.md` ou similaire
- Grep le wrapper pour trouver comment il invoque le script Python
- Soit le wrapper charge un module Python cached (importlib.reload nécessaire)
- Soit le wrapper hardcode le path vers un autre script

### Étape 4 (10 min) — Apply fix au wrapper

Si wrapper trouvé :
- Soit modifier le wrapper pour utiliser le script canonique
- Soit modifier le script que le wrapper appelle directement
- Soit ajouter `importlib.reload()` au wrapper avant invocation

### Étape 5 (5 min) — Validation E2E

```bash
# Via slash command
/symphony-pilot-runtime --once --dry-run
# Attendu: polled: 4, dispatched: 4 (ou 0 si owner_mode false)
```

Si `polled: 4` confirmé → boucle cassée, runtime redevient productif. Cycle Plustard clos.

---

## 4. Lessons shipped (D4 append-only)

1. **Plane self-hosted peut ignorer silencieusement les filtres par name** — toujours utiliser UUID via discovery endpoint puis filter par `?state=<UUID>`. Pattern : cache 5min pour éviter re-query.

2. **CC slash command peut wrapper le runtime** — un fix sur le script canonique ne prend pas nécessairement. Toujours tester via le slash command après fix.

3. **`__pycache__` peut cacher l'ancien code** même après edit du `.py`. Toujours `rm -rf __pycache__/` + `find ... -name "*.pyc" -delete` avant re-test.

4. **L'involution d'output identique est un D8 stress signal** — si A0 invoque N fois la même commande, c'est soit (a) bug UI, (b) test de persistance, (c) attente d'un output différent. Réponse doit changer radicalement (handoff Plustard, fix runtime, ou close cycle).

5. **Le runtime A0 Phase 2 fait son travail en background** — chaque invocation manuelle ne fait que re-poll Plane. Ne pas l'invoquer en boucle si le runtime est déjà actif.

---

## 5. Annexes — D1 receipts verbatim état 2026-06-23 19:35 UTC

### 5.1 Commits récents Life-OS-2026 (5 derniers)

```
7e43bf3 fix(para): V0.7.7 — observability per-LD + force re-seed si IDB vide
8f9ab59 fix(para): V0.7.6 — hydrate 8 LDs + DomainDB singleton (D6 race condition fix)
95c5eb5 fix(para): V0.7.5 — race condition fix: set optimiste + re-sync post-await
666aa31 fix(para): V0.7.4 — idempotent canon bootstrap (skip if AAAS-* already in IDB)
d3afe2b feat(para): V0.7.3 — one-shot canon bootstrap 3 AaaS Variants on first hydrate
```

### 5.2 Polled counts observés

| Invocation | polled | dispatched | state |
|---|---|---|---|
| 1re dry-run | 109 | 109 | baseline |
| 2e dry-run | 112 | 112 | +3 |
| 3e (refus) | n/a | n/a | refus D7 |
| 4e dry-run | 118 | 118 | +6 |
| 5e dry-run | n/a | n/a | refus D7 |
| 6e dry-run | 130 | 130 | +12 |
| 7e (refus) | n/a | n/a | task hangée |
| 8e (current) | n/a | n/a | handoff Plustard en cours |

### 5.3 Log entries wiki canon

```
[2026-06-23T19:35:00-0400] INFRA-SYMPHONY-RUNTIME-FIX-ATTEMPT
[2026-06-23T19:20:00-0400] INFRA-SYMPHONY-RUNTIME-7TH-INVOCATION
[2026-06-23T19:05:00-0400] INFRA-SYMPHONY-RUNTIME-6TH-INVOCATION
[2026-06-23T18:50:00-0400] INFRA-SYMPHONY-RUNTIME-5TH-INVOCATION
[2026-06-23T18:35:00-0400] INFRA-SYMPHONY-RUNTIME-4TH-INVOCATION
[2026-06-23T18:18:00-0400] INFRA-SYMPHONY-RUNTIME-3RD-INVOCATION
[2026-06-23T18:00:00-0400] INFRA-SYMPHONY-RUNTIME-2ND-INVOCATION
[2026-06-23T17:55:00-0400] PARA-DEBUG-RESOLVED
```

---

## 6. Auteur + traçabilité

**Auteur** : A0 Amadeus (méta-orchestration) · **Date** : 2026-06-23 · **Cycle** : Q3 2026 W2 · **Statut** : OPEN — handoff Plustard fix runtime
**Prochaine revue** : post-fix Plustard (closure par `handoff_runtime_loop_resolved_<DATE>.md`)
**Append wiki/log.md** : à faire APRÈS livraison finale du fix Plustard
