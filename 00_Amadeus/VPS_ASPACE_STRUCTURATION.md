# Structuration VPS A'Space — Business OS en instances Coolify, 1 Hermes Agent isolé par client

> **Cible** : le VPS Hostinger (Coolify v4.1.2 installé, serveur `srv941028`, projet `OMK > production` vide au 20/07/2026 — vérifié terminal Coolify).
> **Chaîne** : `sob/` local (SQLite, léger) → **déclencheur = 1er client payant** (`subscribed AND mrr>=1000`) → VPS.
> **Principe** : Coolify orchestre des ISOLATIONS PAR CLIENT ; l'AaaS est l'interface ; Supabase Cloud (MCP OMK) est la DB multi-tenant ; Hermes Agent exécute les workflows Business OS DU client, DANS le périmètre du client, rien d'autre.

## 1. L'architecture (3 étages)

```
COOLIFY (VPS srv941028)
├── Projet "ASpace-Core"                        ← le méta (1 seul)
│   ├── app: aaas-interface   (front AaaS — dashboard clients, Next.js/Vite)
│   └── app: sob-runner       (cron 0 6 */2 * * → le Run /2 jours, boot HANDOVER_EXECUTOR §1)
│
├── Projet "client-<slug-coach-1>"              ← 1 PROJET COOLIFY PAR CLIENT
│   ├── app: hermes-agent-<slug>   (l'exécuteur isolé du client — workflows Business OS)
│   └── volume: /data/<slug>/       (sob-instance du client : config.json + data.db + artefacts)
├── Projet "client-<slug-coach-2>"
│   └── ... (même forme — le clone du projet Coolify EST le provisioning)
└── ...
        │
        ▼ (toutes les apps parlent à)
SUPABASE CLOUD (MCP OMK — projet omk_saas existant, JWT hook + RLS live)
  schéma omk_saas : 1 tenant = 1 client coach · RLS par tenant · l'AaaS lit/écrit ici
```

## 2. Le mapping — qui vit où

| Élément local (`sob/`) | Équivalent VPS | Notes |
|---|---|---|
| `instances/<slug>/` (dossier isolé) | Projet Coolify `client-<slug>` + volume `/data/<slug>/` | l'isolation par dossier devient isolation par projet/conteneur |
| `deploy_instance.py <slug>` | « Clone » du projet Coolify template + `deploy_instance.py` dans le conteneur | le script reste la source de vérité du provisioning ; Coolify l'emballe |
| `aspace.db` (SQLite pilotage) | reste SQLite dans `~/sob/` du VPS (le pilotage global n'est PAS multi-tenant) | migration Postgres SEULEMENT au Cycle 3 (multi-tenant du pilotage) |
| `data.db` par instance | schéma tenant dans **Supabase Cloud OMK** (`omk_saas`, RLS par client) | les DONNÉES CLIENTS vont dans Supabase, pas dans SQLite |
| exécuteur (Hermes local) | `hermes-agent-<slug>` : 1 conteneur Hermes PAR client | clé API via env Coolify (Shared Variables), JAMAIS en dur |
| `RUN_LOG.md` / cadence | `sob-runner` cron `0 6 */2 * *` | même mécanique, mêmes fichiers |

## 3. L'isolation par client (la règle dure)

1. **1 client = 1 projet Coolify = 1 conteneur Hermes = 1 tenant Supabase (RLS)**. Un Hermes client ne voit QUE : son volume `/data/<slug>/`, son tenant RLS, son runbook client. Il ne voit ni les autres clients, ni le pilotage global, ni le disque hôte.
2. **Les credentials par client** vivent dans les env vars du projet Coolify (Keys & Tokens / Shared Variables scoped au projet) — rotation possible client par client sans toucher les autres.
3. **Le pilotage global** (`sob/` du VPS : aspace.db, RUN_LOG, forecasts) appartient au projet `ASpace-Core` seulement. Les Hermes clients n'y ont AUCUN accès.
4. **Blast radius** : un client compromis/cassé = son projet Coolify se stoppe/se redéploie sans toucher le reste. C'est l'antifragilité par cloisonnement.

## 4. Séquence de mise en place (dans l'ordre, sur le terminal Coolify)

1. **Pré-requis** (projet ASpace-Core) : `git clone https://github.com/Amdkn/Aspace_OS_V3 ~/aspace` puis `scp` du `sob/` local (avec aspace.db — le git public ne porte PAS les données) vers `~/sob/`.
2. **sob-runner** : app "scheduled task" Coolify → `cd ~/sob && python3 tools/deploy_instance.py --verify-all && <boot HANDOVER_EXECUTOR §1>` — cron `0 6 */2 * *`.
3. **aaas-interface** : déployer le front AaaS (repo omk) → pointe Supabase Cloud OMK (env : URL + anon key via Shared Variables).
4. **Template client** : créer le projet `client-_template` (1 app Hermes + 1 volume) — le provisioning d'un vrai client = clone de ce template + `deploy_instance.py <slug>` + création du tenant Supabase (`omk_saas`, RLS).
5. **1er client réel** : cloner le template avec son slug. C'est l'acte de naissance du multi-instance — il n'arrive QUE quand le client a payé.

## 5. Ce qui ne monte JAMAIS sur le VPS

Gardefous locaux, hooks, doctrines, wiki, wargames, canon (volonté explicite A+, 19/07/2026). Le VPS reçoit : `Aspace_OS_V3` (ce repo — doctrines d'exécution seulement) + `sob/` (par scp) + les apps. Rien d'autre. Anti-Paperclip = fonction H30-H90 (backups, snapshots Coolify) — jamais un gate H1-H10.

## 6. Les documents de référence (dans ce repo)

| Doc | Rôle |
|---|---|
| `START_HERE_2026-07-19.md` | L'allumage — cadence, compression, compact, budget |
| `ROADMAP_DEAL_12WY_2026-2027.md` | Les 4 cycles, 12 Rocks, métriques SQL |
| `INTEGRATION_CEOBENCH_SPECLOOP.md` | Les 18 composants d'exécution (mémoire hebdo, forecast, if-then, E.1-E.4, information hiding) |
| `sob/HANDOVER_EXECUTOR.md` | Le contrat d'exécution agnostique (tout harness) — §0 IGNITION |
| `sob/RUNBOOK_C1-R1/R2/R3.md` | Les 3 Rocks du Cycle 1 |
| `sob/tools/sob.py` + `deploy_instance.py` | L'interface unique + le provisioning léger idempotent |

---
*Local léger prouve le business (SQLite, zéro Docker). Le VPS industrialise l'isolation (Coolify, 1 projet/client). Supabase Cloud porte les données clients (RLS/tenant). Le déclencheur reste le même : un client qui paie. — A.S. 2026-07-20*
