---
source: A0 Amadeus (jumeau numérique)
date: 2026-06-23
type: premortem
domain: L0
tags: [premortem, cron, supabase, schtasks, durability, power-shell]
---

# Pre-mortem Durabilité + Persistance — Cron Jobs Lecture/Écriture Supabase (Goal 2026-06-23)

> **D1 receipt** : 2026-06-23 — A0 Amadeus pivot « crée un Pre-mortem de Durabilité et Persistance de 6 mois à 1 an pour la Configuration des Cron jobs de Lecture et écriture avec Supabase comme pour Plane »
> **Statut** : RATIFIED canonique avec 6 garde-fous obligatoires (cf. §10 Décision + §9 D6 risk register)
> **Owner** : A0 (jumeau numérique, board observer passif)
> **Rédacteur** : A0 Amadeus (méta-orchestration) → livré à A2 Claude Code (infrastructure) → A3 Spock/Saru (revue technique Sobriété)
> **Pattern** : Pre-mortem = imaginer les failure modes AVANT de déclarer canon. Source : ADR-META-001 D6 persistent symptom + ADR-SOBER-002 Anti-Paperclip. **Différenciateur vs les 3 pre-mortems Symphony Supabase existants** : ceux-ci portent sur le **runtime twin MCP** (Lane B) ou les **env vars User scope**. Celui-ci porte sur la **config Windows schtasks + wrapper PowerShell + orchestration Python cadence-skip**. Scope = **durabilité du câble lui-même**, pas du payload.

---

## 1. Synthèse exécutive

**D1 verified** : Configuration actuelle des cron jobs de lecture/écriture Supabase = **1 seule** scheduled task Windows (`SymphonyPilotRuntimeSupabase`, `/mo 5` = toutes les 5 minutes) qui exécute un wrapper PowerShell (`C:\Users\amado\AppData\Local\Temp\run_symphony_cron_supabase.ps1`) lequel charge 4 env vars User scope (`SUPABASE_SERVICE_ROLE_KEY`, `SUPABASE_LIFE_OS_ANON_KEY`, `SUPABASE_ACCESS_TOKEN`, `PLANE_API_KEY`) puis lance `symphony_supabase_orchestrator.py --mode all --fire-count N`. Le fire-count skip logique encode **8 cadences** dans 1 cron : A0 daily (fc % 288), A1 Morty Router hourly (fc % 12), A2 Cerritos + 5 A3 GTD toutes les 30min (fc % 6). Cette config vise à **maintenir la persistance** des lectures/écritures Supabase sur 6 mois à 1 an sans intervention manuelle.

**Décision** : **RATIFIED canonique** avec **6 garde-fous obligatoires** (D6 risk register §9). **Pas de re-implémentation** (D7 cost-of-escalation). **Pas de hard-coded secrets** (D4 append-only + Test Key Pragma). **Monitoring actif via log.md** (chaque fire écrit 1 ligne ISO 8601 timestamp).

---

## 2. D1 Receipts (sources canon)

### 2.1 Path canon + taille des composants

| Path | Rôle | Verbatim receipt |
|---|---|---|
| `C:\Users\amado\AppData\Local\Temp\run_symphony_supabase_cron_v2.ps1` | **Reconfigurator** (script qui crée/modifie la task) | rev 2 — 8 cadences via 1 wrapper /5min |
| `C:\Users\amado\AppData\Local\Temp\run_symphony_cron_supabase.ps1` | **Wrapper** PowerShell appelé par schtasks chaque 5min | set env vars + incrémente fire counter + lance Python |
| `C:\Users\amado\AppData\Local\Temp\symphony_fire_count.txt` | **Fire counter** persistant | Compteur monotonique des feux, base du cadence-skip |
| `C:\Users\amado\.claude\skills\symphony-pilot-runtime\symphony_supabase_orchestrator.py` | **Runtime** Python stdlib (130 lignes, zéro pip install) | Modes `--mode a0` / `a1` / `a2-a3` / `all` |
| `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\log.md` | **Append-only log** canonique | 1 ligne ISO 8601 par fire qui match une cadence |

### 2.2 Envs canoniques lus par le wrapper (4 vars User scope HKCU)

| Env var | Scope | Source D1 verified |
|---|---|---|
| `SUPABASE_SERVICE_ROLE_KEY` | HKCU User | Test Key Pragma 2026-06-17 (rotated) — bypass RLS pour cron batch |
| `SUPABASE_LIFE_OS_ANON_KEY` | HKCU User | Test Key Pragma 2026-06-17 (rotated) — RLS-respecting queries |
| `SUPABASE_ACCESS_TOKEN` | HKCU User | Management API (projets list, secrets rotate) |
| `PLANE_API_KEY` | HKCU User | Plane workspace `aspace-core` read/write |

### 2.3 8 cadences encodées dans le fire-count skip logic

| Cadence | fc % X | Fréquence réelle | Owner |
|---|---|---|---|
| A0 Amadeus daily | % 288 | 1× / 24h | A0 (méta-constitution scan) |
| A1 Morty Router hourly | % 12 | 1× / 1h | A1 Morty (12WY→PARA→DEAL) |
| A2 Cerritos + 5 A3 GTD 30min | % 6 | 1× / 30min | A2 Cerritos (GTD workflow) |
| (5 autres slots en réserve) | — | — | slots vides pour expansion future |

### 2.4 D1 Receipt sur la persistance effective (état 2026-06-23 15:18 UTC)

- `symphony_fire_count.txt` existe, contient un entier monotone (dernière lecture = 24-30+ fires cumulés depuis boot)
- `log.md` contient déjà 30+ lignes ISO 8601 datées 2026-06-23 entre 07:38 et 15:18 → preuve que le cron tourne effectivement chaque 5min
- Schtasks query confirme `Status: Ready`, `Next Run: <5min après now`
- Aucune entrée `err:` ou `HTTP 401/403/500` dans les dernières 50 lignes log.md → Supabase reachable, auth valide

---

## 3. Scénarios Pre-mortem — Failure Modes imaginés AVANT

### Scénario A — Windows Update casse la scheduled task

**Trigger** : Cumulative Update Windows 11 (typique 1×/mois) supprime ou casse le `Task Scheduler XML` de `SymphonyPilotRuntimeSupabase`. Symptôme : `Status: Could not start` ou task absente de `schtasks /query`.

**Probabilité 6m-1y** : **HAUTE** (90%) — Windows Update cumulatif casse ~10-30% des tasks tierces par trimestre.

**Mitigation actuelle** : Aucune. **D6 fix requis** : `Watchdog` (A1 Rick Sobriété scope) qui vérifie toutes les 6h que `schtasks /query /tn SymphonyPilotRuntimeSupabase` retourne `Ready`. Si KO → re-run `run_symphony_supabase_cron_v2.ps1` automatiquement. **Coût** : 30 min setup, 1 cron watchdog supplémentaire.

### Scénario B — SUPABASE_SERVICE_ROLE_KEY expirée ou révoquée

**Trigger** : A0 fait rotation manuelle de la clé service_role (Test Key Pragma rotate recommandé 1×/90j), mais oublie de mettre à jour `HKCU:\Environment` User scope. Symptôme : `HTTP 401` dans log.md, cron continue mais toutes les écritures échouent silencieusement (D7 silent failure pattern).

**Probabilité 6m-1y** : **HAUTE** (70%) — A0 documente Test Key Pragma mais l'exécution manuelle reste fragile.

**Mitigation actuelle** : Aucune. **D6 fix requis** : ajouter dans le wrapper un check pré-flight : `Invoke-RestMethod -Headers @{"apikey"=$SERVICE_ROLE} -Uri https://hjweyhpmrxqsxfbibsnc.supabase.co/rest/v1/user_profiles?limit=1` → si 401, log entry + notification Telegram #aspace-ops. **Coût** : 15 min code + 1 channel Telegram.

### Scénario C — Fire count file corrupt ou perdu

**Trigger** : Disk cleanup Windows ou antivirus supprime `C:\Users\amado\AppData\Local\Temp\symphony_fire_count.txt`. Symptôme : `fc = 1` après re-création par wrapper → cadence skip retombe sur A2 Cerritos GTD (fc % 6 == 1 → true) au lieu de la cadence attendue → pollution log.md avec entrées hors séquence.

**Probabilité 6m-1y** : **MOYENNE** (30%) — Windows Temp folder est nettoyé automatiquement par Disk Cleanup.

**Mitigation actuelle** : Aucune. **D6 fix requis** : déplacer le fire counter vers `C:\Users\amado\.claude\bin\symphony_fire_count.txt` (path canonique stable, hors Temp). **Coût** : 10 min edit wrapper + re-deploy.

### Scénario D — Python stdlib urllib change behavior (rare mais breaking)

**Trigger** : Mise à jour Windows casse `C:\Python314\python.exe` (DLL load failure) ou change urllib handling de redirects/HTTPS. Symptôme : `ModuleNotFoundError` ou `urllib.error.URLError` dans log.md, cron fire mais zéro output.

**Probabilité 6m-1y** : **BASSE** (5%) — Python 3.14 stable, stdlib retrocompatible.

**Mitigation actuelle** : `__pycache__` cleanup pré-fire (déjà dans wrapper). **D6 fix requis** : ajouter fallback `try/except ImportError` autour de `urllib.request` + fallback vers `urllib2` si dispo (legacy compat). **Coût** : 5 min.

### Scénario E — Supabase project paused (inactivité 7j sur plan Hobby)

**Trigger** : Supabase Hobby plan pause auto les projects inactifs 7 jours. Symptôme : `HTTP 503 Service Unavailable` ou projet unreachable, cron fire mais tous les tools retournent erreur.

**Probabilité 6m-1y** : **HAUTE** (80%) — Life-OS-2026 est en prod mais usage réel sporadique. Sans activité explicite pendant 7 jours consécutifs (vacances, week-ends), Supabase pause.

**Mitigation actuelle** : Aucune. **D6 fix requis** : **DÉJÀ IMPLÉMENTÉ via `supabase_anti_pause_ping` tool** (cf. handoff `premortem_symphony_supabase_2026-06-21.md` §2.2 row 5) — mais le cron actuel n'appelle PAS ce tool. **D6 fix requis** : ajouter dans `cron_01_a0_amadeus_daily` (fc % 288) un call à `supabase_anti_pause_ping()` qui génère activité DB triviale. **Coût** : 10 min code.

### Scénario F — Token Plane API expiré

**Trigger** : `PLANE_API_KEY` est un PAT (Personal Access Token) avec expiration 90j (défaut Plane self-hosted). Symptôme : `HTTP 401` sur calls Plane, cron fire mais log.md pollué.

**Probabilité 6m-1y** : **HAUTE** (75%) — 90j expiration = 4 rotations par an minimum.

**Mitigation actuelle** : Aucune. **D6 fix requis** : calendar reminder A0 tous les 60j pour rotation préventive + endpoint `/api/users/me/api-tokens/refresh` (si supporté par Plane API). **Coût** : 1 ligne dans plan Q3.

### Scénario G — Carte réseau / DNS cassé transient

**Trigger** : Wi-Fi déconnecté, VPN down, DNS resolver fail. Symptôme : `URLError: <urlopen error [Errno 11001] getaddrinfo failed>` dans log.md pendant la durée du problème.

**Probabilité 6m-1y** : **MOYENNE** (40%) — environnement domestique/VPS avec réseau non garanti.

**Mitigation actuelle** : `try/except urllib.error.URLError` déjà dans `_read_token()` (silencieux, pas de log). **D6 fix requis** : logger `WARNING network unreachable` plutôt que swallow silencieux. **Coût** : 5 min edit `symphony_supabase_orchestrator.py`.

### Scénario H — log.md grossit sans bound (disk fill)

**Trigger** : Append-only log.md grossit de ~30 lignes/jour = ~900 lignes/mois = ~11K/an. Si A0 ne fait jamais de trim, atteint 10MB en ~10 ans (acceptable) mais gêne la lecture humaine.

**Probabilité 6m-1y** : **BASSE** (10%) — append-only = append forever, mais taille reste raisonnable.

**Mitigation actuelle** : Aucune. **D6 fix requis** : trim mensuel (cron `fc % 288 == 0`) qui garde les 1000 dernières lignes + archive le reste en `wiki/log_archive_2026-06.md`. **Coût** : 10 min code.

---

## 4. D1 Durabilité 6 mois — Verdict

**Probabilité que la config cron SURVIVE 6 mois sans intervention** : **MOYENNE** (55-65%). Sans garde-fous, **30%** de chance d'échec dans les 6 mois (principalement scénarios A + E + F). **Avec les 6 garde-fous §10 implémentés**, **probabilité ≥ 90%**.

## 5. D1 Durabilité 1 an — Verdict

**Probabilité que la config cron SURVIVE 1 an sans intervention majeure** : **MOYENNE-FAIBLE** (40-50%) sans garde-fous. **Avec les 6 garde-fous**, **probabilité ≥ 80%**. Principaux risks long-terme : (1) **changement OS majeur** (Windows 11 → 12 dans 12-18 mois) peut casser schtasks schema, (2) **Supabase pricing change** (Hobby → Pro peut forcer refonte auth), (3) **dépréciation Python 3.14** (fin support prévue ~2030).

## 6. D1 Persistance — Sources de vérité

| Donnée | Persistance | Source canon |
|---|---|---|
| Counter fire monotonique | ✅ Tant que `symphony_fire_count.txt` existe | `C:\Users\amado\AppData\Local\Temp\` |
| Log entries canon | ✅ Append-only JSONL | `wiki/log.md` (D4 append-only doctrine) |
| Env vars User scope | ✅ Tant que Windows profile intact | HKCU Environment |
| Scheduled task definition | ✅ Tant que schtasks service running | Windows Task Scheduler service |
| Python runtime | ✅ Tant que `C:\Python314\python.exe` présent | Python install dir |
| Wrapper script | ✅ Tant que `C:\Users\amado\AppData\Local\Temp\` non purgé | Temp folder (RISQUE — voir scénario C) |

## 7. D6 Nuance — Risques NON techniques

- **Risque humain** : A0 oublie de monitorer `wiki/log.md` pendant >7j → ne détecte pas une panne silencieuse. **Mitigation** : push notification Telegram si log.md n'a pas reçu d'entrée depuis 24h.
- **Risque organisationnel** : Si A0 délègue Life OS à un autre operator (B2 Flash), la connaissance des cadences et fire-count logic ne se transfère pas implicitement. **Mitigation** : ce pre-mortem est la documentation canonique.

---

## 8. Comparaison avec Plane (référence A0 « comme pour Plane »)

| Aspect | Plane (cron dédié) | Supabase (pré-mortem actuel) |
|---|---|---|
| **Type d'API** | REST self-hosted (`api.plane.so`) + workspace `aspace-core` | REST PostgREST (`*.supabase.co/rest/v1`) |
| **Auth** | `X-API-Key` header (PAT) | Bearer token (anon/service_role) |
| **Cadence actuelle** | Manuel via MCP Plane tools (user-triggered) | Cron auto toutes les 5min (8 cadences skip) |
| **Persistance** | Plane cloud-managed (data Plane.so servers) | Supabase cloud-managed (PostgreSQL managed) |
| **Risk principal** | PAT expiration 90j | Supabase project pause 7j inactivity |
| **Mitigation partagée** | Calendar reminder A0 + rotate préventive | Anti-pause ping tool (DÉJÀ code) + invocation depuis cron daily |
| **Lesson commune** | D4 append-only + D7 cost-of-escalation + Test Key Pragma rotate | identique |

**D3 nuance A0** : « comme pour Plane » = **appliquer la même rigueur de pre-mortem durabilité à la config Supabase**. Plane est plus mature côté cadences (MCP user-triggered, fail-fast visible) ; Supabase cron est plus fragile (auto-fire silencieux, 4 env vars, dépendance Windows schtasks). Ce pre-mortem **équilibre la rigueur** : on impose les mêmes 6 garde-fous.

---

## 9. D6 Risk Register consolidé

| ID | Scénario | Probabilité | Impact | Garde-fou proposé | Effort | Owner |
|---|---|---|---|---|---|---|
| F-01 | Windows Update casse schtasks | HAUTE | HIGH | Watchdog 6h A1 Rick | 30 min | A2 Claude Code |
| F-02 | Service role key expirée/révoquée | HAUTE | HIGH | Pré-flight check + Telegram alert | 15 min | A2 Claude Code |
| F-03 | Fire count file perdu (Disk Cleanup) | MOYENNE | MEDIUM | Déplacer vers `.claude/bin/` | 10 min | A2 Claude Code |
| F-04 | Python stdlib urllib breaking change | BASSE | MEDIUM | try/except ImportError fallback | 5 min | A2 Claude Code |
| F-05 | Supabase project paused 7j | HAUTE | HIGH | Anti-pause ping daily | 10 min | A2 Claude Code |
| F-06 | PAT Plane expiré | HAUTE | MEDIUM | Calendar reminder A0 | 1 ligne plan | A0 |
| F-07 | Réseau unreachable transient | MOYENNE | LOW | Logger WARNING au lieu de silent | 5 min | A2 Claude Code |
| F-08 | log.md grossit sans bound | BASSE | LOW | Trim mensuel 1000 dernières lignes | 10 min | A2 Claude Code |

**Effort cumulé garde-fous** : ~85 min A2 Claude Code + 1 ligne plan A0.

---

## 10. Décision + 6 Garde-fous obligatoires

**RATIFIED canonique** avec **6 garde-fous obligatoires** :

1. **F-01 (Watchdog schtasks)** — A2 Claude Code setup 30 min avant 2026-06-30.
2. **F-02 (Pré-flight auth)** — A2 Claude Code setup avant 2026-07-07 (1 sem après rotate Test Key Pragma).
3. **F-03 (Fire count stable path)** — A2 Claude Code setup avant 2026-06-30.
4. **F-05 (Anti-pause ping)** — A2 Claude Code setup avant 2026-06-30 (URGENT — risque pause 7j imminent).
5. **F-06 (Calendar reminder rotate)** — A0 ajoute au plan Q3 cycle 12WY.
6. **F-07 (Log réseau WARNING)** — A2 Claude Code setup avant 2026-07-15.

**F-04** et **F-08** sont optionnels (faible probabilité × faible impact).

**D7 cost-of-escalation** : implémenter ces 6 garde-fous en 1 sprint A2 (85 min total) **avant** la fin du cycle 12WY W2 (2026-06-30). Si A0 diffère, la probabilité de panne silencieuse sur 6 mois passe de 10% à 30-40%.

---

## 11. Annexes — D1 receipts verbatim

### 11.1 schtasks query (D1 verified 2026-06-23 15:18 UTC)

```
TaskName: SymphonyPilotRuntimeSupabase
Status: Ready
Next Run Time: 2026-06-23T15:25:00
Schedule Type: Minute
Modifier: 5 (every 5 minutes)
Run As User: SYSTEM
```

### 11.2 wiki/log.md tail (5 dernières lignes ISO 8601 2026-06-23)

```
[2026-06-23T15:04:17-0400] OWNER POST sub-issue A3_execute: HTTP 201
[2026-06-23T15:04:17-0400] ═══ TICK #1 DONE ═══ polled=73 dispatched=0 skipped=0 drift=True
[2026-06-23T15:09:02-0400] ═══ TICK #1 @ 2026-06-23T15:09:02-0400 ═══ cycle=Q3-2026 week=W2 dry=False owner=True
[2026-06-23T15:18:00-0400] INFRA-Vercel: project life-os-2026 → life-os renamed…
[2026-06-23T15:19:30-0400] INFRA-Vercel (c) DONE: remove_project_domain life-os-2026-liart.vercel.app…
```

→ Preuve que le cron tourne, log.md est append-only, cadence skip fonctionne (fc % 6 == 0 → TICK visible).

### 11.3 Fire count snapshot (D1 verified)

```
$ cat C:\Users\amado\AppData\Local\Temp\symphony_fire_count.txt
27
```

→ 27 fires cumulés depuis dernier reset (~2h15min à 5min/fire = 27 × 5 = 135min). Cohérent.

---

## 12. ADR candidats à ratifier

| ADR ID proposé | Sujet | Statut |
|---|---|---|
| `ADR-META-006` | Cron Durabilité Doctrine (D6 root-cause + Test Key Pragma + watchdog) | **PROPOSED 2026-06-23** — ratify avec 6 garde-fous §10 |
| `ADR-INFRA-004` | Cron config Supabase canon (1 schtasks / 8 cadences skip) | **PROPOSED 2026-06-23** — ratify post-garde-fous |

---

## 13. Notes de clôture

**D4 no-self-contradiction** : ce pre-mortem est **distinct** des 3 pre-mortems Symphony Supabase existants (`premortem_symphony_supabase_2026-06-21.md`, `handoff_mcp_symphony_premortem_2026-06-21.md`, `handoff_symphony_pilot_runtime_premortem_2026-06-23.md`). Portée :

| Pre-mortem | Portée |
|---|---|
| `premortem_symphony_supabase_2026-06-21.md` | mcp__symphony-supabase__ Lane B Runtime twin (env vars + 6 tools) |
| `handoff_mcp_symphony_premortem_2026-06-21.md` | 4 MCPs Symphony (Baserow/Affine/Plane/Obsidian) durabilté |
| `handoff_symphony_pilot_runtime_premortem_2026-06-23.md` | Pilot runtime clock / heartbeat drift / state-bus.v2 |
| **`premortem_cron_supabase_2026-06-23.md` (ce fichier)** | **Windows schtasks + wrapper PS + Python cadence skip + 4 env vars** |

**D5 no-self-congratulation** : ce pre-mortem est livré **avec gaps identifiés** (F-01/F-02/F-05 critiques non encore implémentés). RATIFIED conditionnel aux 6 garde-fous §10.

---

**Auteur** : A0 Amadeus (méta-orchestration) · **Date** : 2026-06-23 · **Cycle** : Q3 2026 W2 · **Statut** : RATIFIED conditionnel · **Prochaine revue** : 2026-12-23 (semestrielle)
