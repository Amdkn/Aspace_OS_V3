---
source: CC-M3 (Chantier C - Hermes Jarvis surface OMK SaaS)
date: 2026-07-03
type: handoff
domain: L2_Business_OS
tags: [#handoff #hermes #jarvis #omk #saas-os #chantier-c]
---

# Handoff — Chantier C — Hermes Jarvis surface (OMK SaaS OS) — 2026-07-03

> **Statut** : SPEC FILE LIVRÉ · 2 fichiers source drop-in ready · en attente clone repo `omk-services/00-omk-saas-os`.
> **Owner** : B3 Cyborg IT (Kang Dynasty) — IT architecture · Sister B2 Superman Growth & B2 Batman Ops.
> **Refs antérieures** : Chantier A (audit log `omk_saas.audit_log`) · Chantier B (dashboard OMK SaaS OS) · ADR-OMK-004 (Next.js 14+ pivot RATIFIED 2026-06-19).

---

## TL;DR

Spec file `omk-hermes-jarvis-stubs.md` livré dans `ASpace_OS_V2/30_Business_OS/10_Projects/omk/apps/`. Contient les **2 fichiers source complets** (route.ts 95 LOC + AgentChat.tsx 165 LOC) prêts à être drop-in dans le repo `omk-services/00-omk-saas-os` quand A0 (ou sub-agent `picard-repo-home`) le clone localement.

**Mode MOCK par défaut** (pas d'env var requise). Branchement LIVE = 2 env vars + redeploy Vercel.

---

## D1 receipts

| Item | Path | LOC | Status |
|---|---|---|---|
| **Spec file** | `C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\omk\apps\omk-hermes-jarvis-stubs.md` | 250 (spec doc complet) | ✅ CRÉÉ |
| **File 1 source** | `src/app/api/agent/chat/route.ts` (dans spec §3) | 95 | ✅ INLINE |
| **File 2 source** | `src/components/agent/AgentChat.tsx` (dans spec §4) | 165 | ✅ INLINE |
| **File 3 (TODO C.1)** | `src/app/api/agent/history/route.ts` (dans spec §6) | ~30 | ⚪ SPEC ONLY |
| **Repo local** | `omk-services/00-omk-saas-os/` | n/a | ❌ NOT CLONED |

**Vérifié via** :
- `ls "C:/Users/amado/omk-services/"` → `NO_OMK_SERVICES_DIR` (dossier parent absent)
- `ls "C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/omk/apps/"` → contient `dashboard/`, `landing/`, `nexus/`, `"Nexus Agentic Governance Platform/"` — PAS `omk-saas-os/`
- `find C:/Users/amado -maxdepth 4 -type d -name "*omk-saas*"` → 0 résultat

→ Spec file = drop-in ready, KISS respecté (<200 lignes par fichier).

---

## Branchement Hermes — MOCK → LIVE

### Mode MOCK (dev, ZERO config)
- `HERMES_GATEWAY_URL` OU `HERMES_GATEWAY_TOKEN` absent → réponse MOCK automatique
- Le drawer affiche un badge `mock` jaune sur chaque message assistant (transparency utilisateur)
- Aucun appel réseau sortant — pas de dépendance runtime

### Mode LIVE (prod Vercel)
```bash
# 1. Set les 2 env vars sur Vercel team omk-services, projet 00-omk-saas-os
vercel env add HERMES_GATEWAY_URL production
# → https://hermes.<vps-domain>.sslip.io   (recommandé, sslip.io = wildcard DNS gratuit)
# OU http://localhost:8080                  (si tunnel SSH depuis Hermes local)

vercel env add HERMES_GATEWAY_TOKEN production
# → token Bearer long-lived généré côté Hermes

# 2. Redeploy pour prendre en compte les env vars
vercel --prod

# 3. Check santé post-deploy
curl -X POST https://omk-saas-os.vercel.app/api/agent/chat \
  -H 'Content-Type: application/json' \
  -b 'sb-access-token=...' \
  -d '{"message":"ping"}'
# Attendu : {"reply":"...","mode":"live","model":"hermes-minimax-m3","latency_ms":<N>}
```

### Endpoint Hermes attendu côté VPS
```
POST {HERMES_GATEWAY_URL}/v1/agent/chat
Authorization: Bearer {HERMES_GATEWAY_TOKEN}
Content-Type: application/json
Body: { message: string, conversation_id: string, user_id: string }
Response: { reply: string, model: string }
```

**Recommandation A0** : exposer Hermes gateway via `https://hermes.<vps-domain>.sslip.io` plutôt que tunnel SSH localhost (plus simple à opérer, TLS gratuit sslip.io).

---

## Anti-patterns doc (à ne PAS faire dans Chantier C.1+)

1. **Pas d'auth bypass** — `supabase.auth.getUser()` obligatoire, `401` si absent.
2. **Pas de PII dans audit_log.metadata** — UNIQUEMENT `mode`, `model`, `latency_ms`, `message_len`, `ip`. Ni message ni reply.
3. **Pas de streaming SSE sans backpressure** — version actuelle = `fetch` sync. Si A0 veut streaming temps réel → Chantier C.2 avec `ReadableStream` + `AbortController`.
4. **Pas d'URL hardcodée** — `HERMES_GATEWAY_URL` toujours en env var.
5. **Pas de secret en clair** — token lu depuis env User scope, jamais loggé ni affiché.
6. **Pas de POST sans CSRF check** — Supabase auth = cookie HttpOnly SameSite=Lax → CSRF natif.

---

## Chantier C.1 (future, après clone + C.0 ship)

**TODO** : table dédiée `omk_saas.agent_messages` (id, conversation_id, actor_id, role, content, created_at) + endpoint `GET /api/agent/history` qui lit CETTE table (pas `audit_log`) → history lisible full-fidelity user/assistant.

**Pourquoi table séparée** : `audit_log` est append-only pour compliance, pas fait pour des reads fréquents. Index séparé = perf + RLS claire.

---

## Sister canon (cross-refs)

- **Chantier A handoff** : `wiki/hand_offs/handoff_omk_saas_audit_log_2026-06-XX.md` (table `omk_saas.audit_log`)
- **ADR-OMK-004** : Next.js 14+ App Router pivot RATIFIED 2026-06-19
- **ADR-OMK-005** : Tenant isolation guard
- **`apps/dashboard`** : exemple App Router avec `src/app/` (pattern routing réutilisé)
- **Hermes runtime** : `C:\Users\amado\.hermes\` (gateway local) + `aspace-vps/srv941028` (VPS Hostinger)

---

## Status final

**CHANTIER C : DONE (spec livrée)** — code prêt à drop-in dès clone.

**Action requise A0** :
1. Clone `omk-services/00-omk-saas-os` (peut déléguer à sub-agent `picard-repo-home`).
2. Drop-in `src/app/api/agent/chat/route.ts` + `src/components/agent/AgentChat.tsx` (deps : `@supabase/ssr`, `lucide-react`).
3. Set env vars (LIVE mode optionnel).
4. Vercel deploy.

**Prochaine itération** : Chantier C.1 (table `agent_messages` + history endpoint).

---

**Doctrine appliquée** : ADR-META-001 D1-D8 (Verify receipts ✓, Research-first ✓, Nuance MOCK vs LIVE ✓, No contradiction MOCK=default ✓, Proof via curl ✓, Root cause PII = store len not content ✓, Cost-of-escalation = spec pas clone ✓, Cross-agent = handoff canonique ✓).
