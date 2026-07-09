# Supervision de l'Orchestration — introduire Symphony + Hermes Agent

> **Statut** : Shadow A0 — DRAFT — hors-canon SDD, hors-Airlock (veto 90j respecté).
> **Date** : 2026-06-05 · **Auteur** : Claude Code (A2) sur intention A0.
> **Hérite** : `symphony-base.spec.md` + `L0/open-hermes-runtime.md` (ÉTAT 3) + `L0/shadow-ai-capability-routing.md` (ÉTAT 1).
> **Ancre** : ADR-RICK-001 (OpenHarness/Donna), ADR-RICK-002 (Hermes promotion), ADR-INFRA-001 (console unifiée).
> ⚠ Ce document **n'active rien**. Il décrit *comment superviser* Symphony + Hermes Agent quand ils tourneront.

---

## 1. La question, précisée
"Introduire Symphony et Hermes Agent dans le plan de supervision de l'orchestration" = répondre à :
**qui surveille l'orchestrateur, comment on sait qu'il est vivant/sain, comment on suit ses SLA,
et comment une défaillance remonte — sans qu'A0 devienne le watchdog manuel.**

Deux sujets **distincts** à superviser (ne pas confondre) :
| Composant | Nature | Rôle | Port/Proc |
|---|---|---|---|
| **Symphony** | daemon headless (printingpress.dev) | B1 Router : poll tracker → workspace/issue → lance l'agent. *Lit ; n'écrit pas.* | service long-running |
| **Hermes Agent** | gateway Kanban (state machine) | runtime A1 (Rick incarné) : reçoit, triage SLA/SOC, dispatch vers A2, Donna DLQ | `hermes-agent.service` :3101 |

> Open Hermes (ÉTAT 3) = **OpenHarness (moteur) + Hermes Agent (gateway) + Donna DLQ + Yaz/Ryan/Graham**.
> Symphony est le **routeur d'entrée** B1 ; Hermes Agent est le **cœur d'orchestration** A1.

---

## 2. Le tissu de supervision existant (où les brancher)
A'Space a déjà 3 organes de supervision — il ne faut **rien réinventer**, juste y connecter Symphony + Hermes :

1. **Yaz (Watchdog, L0/13e Docteur A3)** — monitor + restart. → *propriétaire des health-checks et du redémarrage.*
2. **Donna (DLQ, ADR-RICK-001)** — dead-letter queue + escalade A0 (Telegram MCP). → *propriétaire de l'escalade après N retries.*
3. **Console de gouvernance unifiée (ADR-INFRA-001)** — un seul dashboard
   (`aspace-dashboard.148.230.92.235.sslip.io`), apps sous `/srv/aspace/dashboard/app/<domain>/`. → *propriétaire de la surface d'état.*
   - Doc-ownership rappel : **Codex documente en local Windows ; Hermes documente dans le VPS ; Claude Code réconcilie.**

Plus le **mesh Shadow L0 heartbeat** (ticks éphémères, *no-daemon*) pour les 3 opérateurs CLI.

---

## 3. La tension à résoudre : "no-daemon" vs daemons long-running
Doctrine Shadow L0 = **« plus de Task Scheduler entries, jamais un daemon »** pour les opérateurs CLI
(Codex/Gemini/Claude) — ticks éphémères. **Mais** Symphony et Hermes Agent **SONT** des daemons (ÉTAT 3).

**Résolution (proposée)** : pas de contradiction si on sépare les rôles —
- Les **ticks éphémères ne FONT pas le travail** ; ils **SUPERVISENT** les daemons (probe → reportent → relancent si mort).
- Symphony/Hermes = les **daemons autonomes V1** ; le tick Yaz est leur **watchdog externe sans état**.
- Donc : `Task Scheduler → heartbeat-tick.ps1 yaz` (every 5m always) **probe** `hermes-agent:3101/health` + le PID Symphony, et `restart` si besoin. Le daemon vit ; le tick le veille. Cohérent avec ADR-006 (watchdog natif PS) + la doctrine no-daemon-pour-les-CLI.

---

## 4. Contrat de supervision par composant (le cœur du plan)

### 4.1 Symphony (B1 Router)
| Dimension | Mécanisme proposé |
|---|---|
| **Liveness** | PID + un fichier `last_poll.touch` horodaté à chaque cycle de poll ; Yaz alerte si âge > 3× cadence. |
| **Progress** | compteur `issues_dispatched` + `runs_active` dans un log structuré (déjà prévu : "Status Surface"). |
| **Eligibility/stop** | Symphony stoppe un run si l'issue devient inéligible (déjà spec). Surveillance = log des stops. |
| **Coût (SLA financier)** | tokens × tarif (MiniMax/GLM) agrégés par run → panneau Finance du dashboard (slot Thunderbolts). |
| **Échec transient** | backoff exponentiel interne ; si dépasse N → **déborde vers Donna DLQ**. |
| **Frontière** | *Symphony lit, l'agent écrit.* La supervision vérifie que Symphony **ne fait aucune écriture** (audit). |

### 4.2 Hermes Agent (gateway A1 :3101)
| Dimension | Mécanisme proposé |
|---|---|
| **Health** | endpoint `:3101/health` (Uptime Kuma + probe Yaz). Restart `hermes-agent.service` si down (Ryan = clés/connexions). |
| **State machine** | exposer l'état Kanban (queue depth, in-flight, blocked) → panneau dashboard "Orchestration". |
| **SLA triade (SDD-009)** | Temporel (durée run vs max), Financier (coût vs budget), Qualitatif (Build Gates humains) — trackés par issue. |
| **SOC validation** | chaque payload validé Zod ; rejets loggés → si récurrent, alerte People/Ethics (X-Men) + Donna. |
| **Escalade** | retry > N → Donna DLQ → A0 via Telegram MCP (asynchrone, sleep-safe). |
| **Sécurité** | tokens gateway en plaintext = risque connu (cf. memories) ; supervision inclut un scan "zero leaked secret" (Yaz). |

---

## 5. Plan d'introduction phasé (respecte le veto 90j)
**Phase 0 — Observe-only (maintenant, hors-canon)** : Symphony/Hermes tournent en *dry-run* ; la supervision
ne fait que **lire** (health, logs, coût). Aucun write, aucun bi-sync (cohérent BRIDGE draft). Surface : un
panneau read-only "Orchestration" dans la console unifiée.
**Phase 1 — Supervised activation (post-levée veto / graduation MUSE 3 semaines)** : Yaz watchdog branché
(probe+restart), Donna DLQ câblée, SLA triade active, dashboard live.
**Phase 2 — Autonome ÉTAT 3** : Open Hermes pilote 24/7, intervention A0 < 5%, premium Anthropic réservé
aux arbitrages Rick A1 critiques.

> Promotion en canon (PRD/ADR) seulement après **3 semaines d'usage continu prouvé** (critère MUSE SDD-008).

---

## 6. Crochets concrets à câbler (quand activation autorisée)
1. **Health endpoints** : `hermes-agent:3101/health` + Symphony `last_poll.touch` → Uptime Kuma + tick Yaz.
2. **Panneau dashboard** : `/srv/aspace/dashboard/app/orchestration/` (queue depth, runs actifs, coût, DLQ count) — ADR-INFRA-001.
3. **Watchdog** : `heartbeat-tick.ps1 yaz` (every 5m) probe + restart `hermes-agent.service` ; log dans `pulse.log` (noms de var seulement, jamais de secrets).
4. **Donna DLQ** : table/queue d'escalade + canal Telegram MCP ; chaque run failed-after-N y atterrit avec son payload SOC.
5. **SLA tracker** : par issue, 3 colonnes (max_time, max_cost, build_gate) — déjà amorcé côté Baserow Rock L2 (cf. BRIDGE draft).
6. **Audit frontière** : test périodique "Symphony n'a fait aucun write tracker" (la frontière lit/écrit est la garantie de sûreté).

---

## 7. Frontières & garde-fous (non négociables)
- **Symphony lit, l'agent écrit** — la supervision *vérifie* cette frontière, ne la franchit pas.
- **Donna est l'unique chemin d'escalade** — pas d'alerte sauvage hors DLQ.
- **Un seul dashboard** (ADR-INFRA-001) — pas de console isolée par composant.
- **Frugalité** : MiniMax 2.7 / GLM 4.7 Flash par défaut ; premium Anthropic réservé Rick A1.
- **Veto 90j** : ce plan est une *carte*, pas un activable. Rien ne démarre sans accord A0 + levée veto.

---
*Shadow A0 draft — supervision map for Symphony + Hermes Agent. 2026-06-05. Aucun write, aucun activable.*
