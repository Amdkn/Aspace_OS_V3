---
title: Alykaly OS — Deployment Runbook
date: 2026-05-20
status: ACTIVE
domain: L1 / Project Picard / Deployment
related:
  - ../SUPABASE_STRATEGY.md
  - ../picard_audit.md
tags: [#Deployment, #Supabase, #Hostinger, #Runbook]
---

# Deployment Runbook — Alykaly OS

Ce runbook décrit le flow complet **local Supabase → Hostinger Business → self-hosted Supabase**.

---

## Phase A — Vérification locale (avec Supabase Docker)

### A.1 Prérequis

- ✅ Docker Desktop **démarré** (`docker info` doit répondre)
- ✅ Supabase CLI installé (`supabase --version` ≥ 1.150)
- ✅ Node 22 (`node --version`)
- ✅ Cloned/local repo `alykaly-os-V2`

### A.2 Bootstrap local

```powershell
cd "C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\Alikaly Bana Holding OS\alykaly-os-V2"
powershell -ExecutionPolicy Bypass -File .\deploy\bootstrap-local-supabase.ps1
```

Le script :
1. Vérifie Docker + Supabase CLI
2. `supabase init` (idempotent)
3. `supabase start` (download ~2GB la 1ère fois, ~30s ensuite)
4. `supabase db reset` → applique les 10 migrations + seed.sql
5. Affiche les credentials API URL / anon key / service_role key

### A.3 Configurer `.env.local`

Copier les valeurs printées par `supabase status` :

```
NEXT_PUBLIC_SUPABASE_URL=http://127.0.0.1:54321
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...
SUPABASE_SERVICE_ROLE_KEY=eyJ...
N8N_WEBHOOK_URL=                  # optional
DOCUSIGN_WEBHOOK_SECRET=          # optional
```

### A.4 Lancer Next.js en dev

```powershell
npm install
npm run dev
```

→ http://localhost:4444

### A.5 Smoke tests locaux

```bash
# Edge function appelée via API Next.js
curl http://localhost:4444/api/engine/status

# Intake test (anon path)
curl -X POST http://localhost:4444/api/intake \
  -H "Content-Type: application/json" \
  -d '{"full_name":"Test","email":"t@example.com","case_number":"X 1234"}'

# Supabase Studio
start http://127.0.0.1:54323
```

Vérifier dans Studio :
- 5 schemas (`app`, `crm`, `identity`, `ops`, `audit`)
- 15+ tables
- RLS activée sur toutes les tables business
- Seed data présent (cases, agents, knowledge docs)

---

## Phase B — Premier user + role

### B.1 Créer un user admin

Via Supabase Studio → Auth → Users → "Add user" :
- Email : `admin@kalybana.com`
- Password : (à définir)

Le trigger `handle_new_user` crée automatiquement le profile avec `role='viewer'`, `clearance='level_1_internal'`.

### B.2 Promouvoir en admin (SQL Editor Studio)

```sql
UPDATE identity.profiles
SET role = 'admin', clearance = 'level_5_sovereign'
WHERE email = 'admin@kalybana.com';
```

### B.3 Login depuis l'app

http://localhost:4444/auth/login → email + password.

Le middleware redirige vers `/` (Dashboard) après login.

---

## Phase C — Build production check

```powershell
npm run build
```

Doit produire `.next/standalone/server.js` sans erreur TypeScript ni lint blocker.

Tester en mode standalone localement :

```powershell
$env:NEXT_PUBLIC_SUPABASE_URL="http://127.0.0.1:54321"
# ... autres env vars
node .next/standalone/server.js
```

→ http://localhost:4444 doit fonctionner identique au mode `dev`.

---

## Phase D — Migration vers Supabase self-hosted

### D.1 Prérequis self-host

A0 confirme :
- `supabase.kalybana.com` UP (ADR existant)
- Connexion psql possible : `psql postgres://postgres:<pwd>@supabase.kalybana.com:5432/postgres`
- Auth admin créé (dashboard self-host)

### D.2 Push migrations + edge functions

```powershell
$env:SUPABASE_DB_URL="postgres://postgres:PASSWORD@supabase.kalybana.com:5432/postgres"
powershell -ExecutionPolicy Bypass -File .\deploy\push-to-selfhost.ps1
```

Le script applique les 10 migrations puis déploie les 5 edge functions.

### D.3 Configurer secrets Supabase self-host

Via dashboard Supabase ou CLI :

```bash
supabase secrets set N8N_WEBHOOK_URL=https://n8n.kalybana.com/webhook/bana --db-url $SUPABASE_DB_URL
supabase secrets set DOCUSIGN_WEBHOOK_SECRET=<hmac-secret>
```

### D.4 Activer Realtime sur tables critiques

(Déjà fait par migration 010, mais vérifier via Studio :)

Database → Replication → vérifier que `supabase_realtime` publication contient :
- app.cases
- app.transactions
- crm.sales_pipeline_items
- crm.court_filings
- crm.feed_events
- ops.wind_direction_alerts

### D.5 Smoke tests prod Supabase

```bash
# Replace <ANON_KEY> with self-host anon key
curl https://supabase.kalybana.com/functions/v1/sob-engine-simulate \
  -H "apikey: <ANON_KEY>" \
  -H "Authorization: Bearer <ANON_KEY>"

# Doit retourner JSON {status: ONLINE, global_exposure: ..., source: edge-fn}
```

---

## Phase E — Deploy Hostinger Business

### E.1 hPanel — créer le sous-domaine

1. hPanel → **Websites** → **Add Website** → **Subdomain**
2. Subdomain : `alykaly`
3. Parent domain : `kalybana.com`
4. SSL : Let's Encrypt auto

### E.2 hPanel — configurer Node.js App

1. hPanel → Websites → `alykaly.kalybana.com` → **Advanced** → **Node.js**
2. **Create application** :
   - Node.js version : 22
   - Application mode : **Production**
   - Application root : `/home/uXXX/domains/kalybana.com/public_html/alykaly` (noter le path exact, `uXXX` varie)
   - Application URL : `https://alykaly.kalybana.com`
   - Application startup file : `server.js`
3. **Environment variables** (Add one by one) :
   ```
   NODE_ENV=production
   PORT=4444
   HOSTNAME=0.0.0.0
   NEXT_TELEMETRY_DISABLED=1
   NEXT_PUBLIC_SUPABASE_URL=https://supabase.kalybana.com
   NEXT_PUBLIC_SUPABASE_ANON_KEY=<anon-key>
   SUPABASE_SERVICE_ROLE_KEY=<service-role>
   N8N_WEBHOOK_URL=https://n8n.kalybana.com/webhook/bana
   DOCUSIGN_WEBHOOK_SECRET=<hmac-secret>
   ```
4. Ne pas démarrer encore — l'app root est vide.

### E.3 Build local + upload

**Option A : SSH + script** (recommandé) :

```bash
# Depuis ta machine locale
APP_ROOT=/home/uXXX/domains/kalybana.com/public_html/alykaly \
  ./deploy/hostinger.sh
```

Avec ssh-agent ou rsync over ssh pointant vers Hostinger.

**Option B : Git deploy** :

1. Push le repo vers GitHub privé
2. hPanel → Application Manager → **Git** : clone url + branch `main`
3. **Deploy** → hPanel exécute `git pull` + `npm ci` + `npm run build` automatiquement
4. Veiller à ce que startup file pointe vers `.next/standalone/server.js` ou faire le rsync manuel

**Option C : FTP/SFTP** :

1. `npm ci && npm run build` localement
2. Upload via SFTP :
   - `.next/standalone/*` → app root
   - `.next/static/` → `<app_root>/.next/static/`
   - `public/` → `<app_root>/public/`

### E.4 Démarrer l'app

hPanel → Node.js → **Restart Application**.

Logs accessibles via hPanel → Application Manager → **Logs**.

### E.5 Smoke tests prod

```bash
curl https://alykaly.kalybana.com/api/engine/status
# → JSON avec source: "edge-fn"

curl https://alykaly.kalybana.com/bana
# → landing page Bana

# Auth check (devrait redirect vers /auth/login)
curl -i https://alykaly.kalybana.com/
```

---

## Phase F — Post-deploy

### F.1 DNS

Vérifier `dig alykaly.kalybana.com` → A record vers Hostinger IP.
TTL recommandé : 300s pour iterer rapidement les premiers jours.

### F.2 Cron jobs edge functions

Supabase self-host : ajouter dans `pg_cron` (si dispo) ou via GitHub Actions :

```sql
-- Recalc confidence daily 06:00 UTC
SELECT cron.schedule(
  'case-confidence-recalc',
  '0 6 * * *',
  $$SELECT net.http_post(
    url := 'https://supabase.kalybana.com/functions/v1/case-confidence-recalc',
    headers := jsonb_build_object('Authorization', 'Bearer ' || current_setting('app.service_role_key'))
  )$$
);

-- Audit rotation weekly Monday 03:00
SELECT cron.schedule(
  'audit-rotate',
  '0 3 * * 1',
  $$SELECT net.http_post(
    url := 'https://supabase.kalybana.com/functions/v1/audit-rotate',
    headers := jsonb_build_object('Authorization', 'Bearer ' || current_setting('app.service_role_key'))
  )$$
);
```

### F.3 Monitoring

- Supabase Studio → Logs → Edge Functions
- hPanel → Logs (Node.js stdout/stderr)
- `audit.log` review hebdo (script à venir)

---

## Phase G — Acceptance criteria (per SUPABASE_STRATEGY.md §14)

| AC | Vérification |
|---|---|
| AC-01 | Schema déployé — 15+ tables visibles en `supabase db diff --linked` |
| AC-02 | RLS — `select * from app.cases` en role `viewer` ne PEUT PAS INSERT |
| AC-03 | Clearance — user level_1 ne voit pas une row marquée `clearance_required = 'level_5_sovereign'` |
| AC-04 | Intake — `curl POST /api/intake` anon réussit, INSERT visible Studio |
| AC-05 | Edge function — `sob-engine-simulate` retourne `global_exposure` calculé live |
| AC-06 | Refactor — `getActiveCases()` retourne ≥ 5 rows (seed) |
| AC-07 | Realtime — modifier `app.cases.status` via Studio → Dashboard refresh sans reload |
| AC-08 | Deploy — `https://alykaly.kalybana.com` répond 200, login fonctionne |
| AC-09 | Audit — DELETE sur `app.cases` génère une row dans `audit.log` |
| AC-10 | Backup — `pg_dump` du schema réussit, restore sur DB test passe |

---

## Troubleshooting

### "Cannot connect to Docker daemon"
Docker Desktop non lancé. Lancer manuellement, attendre ~60s.

### `supabase start` échoue avec port conflict
`supabase stop` puis vérifier `netstat -ano | findstr 54321` — un autre process bloque les ports 54321-54329.

### Build Next.js : "Module not found: @supabase/ssr"
`npm install @supabase/ssr @supabase/supabase-js` puis re-build.

### Edge function 401 en local
`config.toml` : vérifier `verify_jwt = false` sur les functions publiques (intake-handler, sob-engine-simulate).

### Hostinger app ne démarre pas
- Vérifier startup file = `server.js` (pas `.next/standalone/server.js`)
- Vérifier que `.next/standalone/*` est bien à la **racine** de l'app root (pas dans un sous-dossier)
- Vérifier env vars
- Logs hPanel → erreurs Node.js stderr
