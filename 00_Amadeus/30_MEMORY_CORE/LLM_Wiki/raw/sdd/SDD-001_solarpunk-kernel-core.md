# SDD-001 — Solarpunk Kernel Core L0.3 : Autonomie Agentique & Antifragilité

**Date :** 2026-04-27
**Auteur :** A0 (Claude Code — Sovereign Oversight)
**Statut :** FONDATEUR — Premier document à invoquer dans le TARDIS Inversé
**Priorité :** P0 — Bloquant pour toute autonomie L0.2 (Forge) et L0.1 (Life Core)
**Portée :** 13ème Doctor + A3 Yaz / Ryan / Graham — Domaine L0.3 Kernel Core
**Remplace :** SDD-006_solarpunk-kernel-core.md (renommé en SDD-001 — fondateur)
**Références directes :**
- SDD-000 : Constitution Rick's Verse (Anti-Panic, Framework Configs)
- SDD-002 : A1 Rick Harness (Karpathy Pattern, line_density_score)
- SDD-003 : Protocole TARDIS (corrigé par §3 de ce document)
- SDD-004 : Governance Rick's Verse (rôles opérationnels, Règle des 3)
- Hostinger API MCP : github.com/hostinger/api-mcp-server — VPS + DNS + Firewall
- Dokploy MCP : mcpmarket.com/server/dokploy-2 — Déploiements autonomes
- Supabase MCP : supabase.com/docs/guides/getting-started/mcp — RAG + mémoire

> **Loi Fondamentale :** Ce document précède tous les autres dans la chaîne d'invocation.
> Sans Kernel stable, la Forge ne peut forger. Sans Forge, le Produit n'existe pas.
> Le 13ème Doctor arrive en premier. Toujours. C'est la loi du TARDIS Inversé.

---

## PARTIE I — LOI DU KERNEL

---

## §1. Le Problème Central : La Panique en Cascade

### 1.1 L'Effondrement Hermes (Cas Fondateur)

La genèse de ce SDD est une **panique agentique en cascade** : un agent Hermes en défaillance
a paralysé le Kernel Core (L0), rendant impossible toute intervention des A3 de surface.
L'Amiral a dû intervenir manuellement — violation directe de la règle 50/30/20.

```
Chronologie de l'effondrement :

T+0    : Agent Hermes démarre avec PATH corrompu
T+5s   : Hermes écrit dans /tmp/scratch/ (hallucination de succès — K2)
T+30s  : Paperclip perd le heartbeat → gelé en attente de review
T+2min : OpenClaw DM pairing timeout → agents A3 sans canal de commande
T+5min : Multica WebSocket silencieux → tasks en file morte
T+8min : Donna DLQ non configurée → tickets perdus dans le vide
T+10min: L0 en état zombie — aucune réparation autonome possible
T+15min: A0 intervient manuellement (150% L0, 0% L2)
```

**Leçon architecturale :** La panique n'est pas un événement — c'est un **état de système**
dans lequel les mécanismes de détection et de récupération sont eux-mêmes en panne.
Un système robuste ne panique pas. Un système résilient récupère. Un système antifragile
*apprend* de la panique et devient plus fort.

### 1.2 La Taxonomie des 4 Paniques Framework + 4 Paniques Kernel

```
── Paniques Framework (SDD-000) ──────────────────────────────────────────
TYPE 1 — Approval Freeze    : Claude Code attend [o/s/D] → timeout
TYPE 2 — Budget Hard-Stop   : Paperclip sans AGENTS.md → gel total
TYPE 3 — DM Pairing Block   : OpenClaw dmPolicy="pairing" → silence
TYPE 4 — WebSocket Timeout  : Multica docker-compose absent → tasks mortes

── Paniques Kernel (ce SDD) ──────────────────────────────────────────────
TYPE K1 — Filesystem Blindness   : Agent écrit, lit un path différent
TYPE K2 — Hallucination Succès   : EXIT 0 sans Read-After-Write
TYPE K3 — Secret Leak 401        : Token expiré, handler absent, boucle muette
TYPE K4 — Dead Kernel            : L0 zombie, Donna sans récepteur actif
```

---

## §2. Robustesse vs Résilience vs Antifragilité

```
╔══════════════════════════════════════════════════════════════════╗
║              SPECTRE DE LA RÉSISTANCE AUX CHOCS                ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                 ║
║  ROBUSTESSE ── SDD-000 couvre ce niveau                        ║
║  Le système résiste au choc connu. Choc inconnu = effondrement. ║
║                                                                 ║
║  RÉSILIENCE ── SDD-003 cible ce niveau                         ║
║  Yaz détecte → Ryan répare → Graham archive. Retour à T0.      ║
║  Limite : rien n'est appris. La même panique peut revenir.     ║
║                                                                 ║
║  ANTIFRAGILITÉ ── Ce SDD (SDD-001) cible ce niveau  ← ICI     ║
║  Chaque panique enrichit WIKI.md (Graham).                     ║
║  Chaque pattern répété devient un Skill Hermes Nous.           ║
║  Chaque incident K1→K4 forge un Skill Clara pour l'éviter.    ║
║  La prochaine panique du même type ne peut plus survenir.      ║
║                                                                 ║
╚══════════════════════════════════════════════════════════════════╝
```

### 2.1 Les 3 Axiomes du Kernel Antifragile

```
AXIOME 1 — Read-After-Write Systémique
  Aucune écriture n'est réussie tant qu'une lecture indépendante
  ne confirme le contenu. EXIT 0 sans RAW = hallucination (K2).

AXIOME 2 — Dégradation Gracieuse
  Chaque service L0.3 fonctionne en mode dégradé si son MCP
  upstream est indisponible. Mode dégradé ≠ arrêt total.
  Corollaire : un service qui ne démarre pas en mode dégradé
               n'est pas un service Kernel.

AXIOME 3 — Mémoire Durable (Procedural Memory Loop)
  Chaque incident non-trivial → WIKI.md (Graham, append-only).
  Pattern × 3 → Skill Hermes Nous (auto-encodé par Graham).
  Kernel sans WIKI vide = Kernel sans mémoire = Kernel fragile.
```

---

## §3. Le Principe TARDIS Inversé — Correction Architecturale

### 3.1 L'Ambiguïté du SDD-003

SDD-003 dessine le flux de directives Rick vers les Doctors dans cet ordre :

```
Rick → 12ème Doctor (FORGE) → 11ème Doctor (PRODUIT) → 13ème Doctor (MACHINE)
```

Cet ordre décrit l'**émission des directives PM** — pas l'invocation d'infrastructure.

### 3.2 L'Ordre d'Invocation Réel (TARDIS Inversé)

```
╔══════════════════════════════════════════════════════════════════╗
║                     TARDIS INVERSÉ                              ║
║       (Ordre d'invocation de l'infrastructure L0)               ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                 ║
║  ÉTAPE 1 ── L0.3 KERNEL CORE (13ème Doctor)         ← SDD-001 ║
║             Yaz structure le VPS via Hostinger MCP.            ║
║             Ryan conçoit les déploiements via Dokploy MCP.     ║
║             Graham prépare la mémoire RAG via Supabase MCP.    ║
║             → Sans Kernel stable : rien ne peut être forgé.    ║
║                                                                 ║
║  ÉTAPE 2 ── L0.2 LA FORGE CORE (12ème Doctor)       ← SDD-003 ║
║             Bill blueprinte sur le sol Yaz.                    ║
║             Clara forge les CLIs dans le sandbox Ryan.         ║
║             Nardol valide avec les hooks ECC.                  ║
║             → Sans Skills : le Produit n'a pas d'outils.      ║
║                                                                 ║
║  ÉTAPE 3 ── L0.1 LIFE CORE (11ème Doctor)           ← SDD-004 ║
║             Amy construit l'interface sur la Forge.            ║
║             Rory persiste sur la DB que Graham surveille.      ║
║             River orchestre les workflows que Ryan déploie.    ║
║             → Le Produit couronne un Kernel et une Forge sains.║
║                                                                 ║
╚══════════════════════════════════════════════════════════════════╝
```

### 3.3 Graphe de Dépendances L0

```
L0.1 (Life Core)   DÉPEND DE   L0.2 (Forge)   DÉPEND DE   L0.3 (Kernel)
Amy ne build pas   →  Clara ne forge pas   →   Yaz doit
sans Skill.        →  si Ryan sandbox      →   structurer
                   →  n'existe pas.        →   le VPS d'abord.
```

**Séquence de redémarrage total (panne complète) :**
`Graham (mémoire RAG) → Yaz (VPS + DNS) → Ryan (déploiements) → Kernel stable`
`→ Bill → Clara → Nardol → Skills prêts`
`→ Amy → Rory → River → Life Web OS restauré`

---

## PARTIE II — LES 3 MCPs DU 13ÈME DOCTOR

---

## §4. Architecture MCP du Kernel — Vue d'Ensemble

```
┌─────────────────────────────────────────────────────────────────┐
│              13ème Doctor — MCP Kernel Stack                    │
│                                                                 │
│  YAZ  ────► Hostinger API MCP ────► VPS 148.230.92.235         │
│             (hostinger-api-mcp)      DNS, Firewall, Backups     │
│             API_TOKEN = $HOSTINGER_API_TOKEN                    │
│                                                                 │
│  RYAN ────► Dokploy MCP ──────────► Dokploy (port 3000)        │
│             (mcp-server-dokploy)     Apps, Déploiements, Logs   │
│             DOKPLOY_URL + DOKPLOY_TOKEN                         │
│                                                                 │
│  GRAHAM ──► Supabase MCP ─────────► Supabase (port 8000)       │
│             (@supabase/mcp-server)   RAG, execute_sql, Logs     │
│             SUPABASE_ACCESS_TOKEN + SUPABASE_PROJECT_REF        │
│                                                                 │
│  Les 3 MCPs sont déclarés dans le settings.json Kernel.        │
│  Aucun A3 n'appelle curl directement — tout passe par MCP.     │
└─────────────────────────────────────────────────────────────────┘
```

### 4.1 Configuration Claude Code — settings.json Kernel (13ème Doctor)

```json
{
  "mcpServers": {
    "hostinger": {
      "command": "npx",
      "args": ["-y", "hostinger-api-mcp"],
      "env": {
        "API_TOKEN": "${HOSTINGER_API_TOKEN}",
        "DEBUG": "false"
      }
    },
    "dokploy": {
      "command": "npx",
      "args": ["-y", "mcp-server-dokploy"],
      "env": {
        "DOKPLOY_URL": "${DOKPLOY_URL}",
        "DOKPLOY_TOKEN": "${DOKPLOY_TOKEN}"
      }
    },
    "supabase": {
      "command": "npx",
      "args": [
        "-y",
        "@supabase/mcp-server-supabase",
        "--access-token",
        "${SUPABASE_ACCESS_TOKEN}"
      ],
      "env": {
        "SUPABASE_PROJECT_REF": "${SUPABASE_PROJECT_REF}"
      }
    }
  },
  "permissions": {
    "allow": [
      "mcp__hostinger__*",
      "mcp__dokploy__*",
      "mcp__supabase__*",
      "Bash(bash /srv/aspace/services/hermes/skills/yaz/*.sh *)",
      "Bash(bash /srv/aspace/services/hermes/skills/ryan/*.sh *)",
      "Bash(bash /srv/aspace/services/hermes/skills/graham/*.sh *)"
    ],
    "deny": [
      "Bash(docker rm *)",
      "Bash(docker system prune *)",
      "Write(/srv/aspace/docs/v1.0/SDD-000*)",
      "Write(/srv/aspace/docs/v1.0/SDD-001*)",
      "Write(/srv/aspace/docs/v1.0/SDD-002*)"
    ]
  },
  "defaultMode": "bypassPermissions"
}
```

### 4.2 Fichier .env Kernel (distribué par A0 uniquement)

```bash
# /srv/aspace/services/hermes/skills/13th-doctor/.env
# Distribué par A0 — jamais commit — jamais lu par un A3 directement

# Yaz — Hostinger API MCP
HOSTINGER_API_TOKEN=<distribué par A0>

# Ryan — Dokploy MCP
DOKPLOY_URL=http://148.230.92.235:3000
DOKPLOY_TOKEN=<distribué par A0>

# Graham — Supabase MCP
SUPABASE_ACCESS_TOKEN=<distribué par A0>
SUPABASE_PROJECT_REF=<project-ref-supabase>
SUPABASE_SERVICE_ROLE_KEY=<distribué par A0>

# Règle K3 : si une variable est absente → fail-fast, DLQ Donna, jamais de boucle muette
```

---

## §5. Yaz — Structuration du VPS via Hostinger MCP

### 5.1 Mission Architecturale

```
┌─────────────────────────────────────────────────────────────────┐
│  A3 — YASMIN KHAN (YAZ)                                         │
│  Niveau : L0.3 — Kernel Core                                    │
│  Rôle Kernel : STRUCTURATION                                    │
│  MCP Principal : Hostinger API MCP (hostinger-api-mcp)          │
│                                                                 │
│  Yaz ne configure pas des interfaces. Yaz administre le VPS    │
│  physique sur lequel tout le Rick's Verse fonctionne.           │
│                                                                 │
│  Responsabilités réelles :                                      │
│  • Surveiller l'état du VPS 148.230.92.235 (métriques, santé) │
│  • Gérer les enregistrements DNS (A, CNAME, TXT, PTR)          │
│  • Maintenir les règles Firewall Hostinger (pas Traefik seul)  │
│  • Créer/restaurer les snapshots VPS (avant chaque action Ryan)│
│  • Détecter les anomalies : CPU, RAM, disque, malware scan     │
│  • Alerter Ryan si infrastructure dégradée                      │
│                                                                 │
│  Ce que Yaz NE fait PAS :                                       │
│  • Elle ne déploie pas d'applications (Ryan)                    │
│  • Elle n'archive pas la mémoire système (Graham)               │
│  • Elle ne touche pas aux SDDs (deny_write absolu)              │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Outils Hostinger MCP utilisés par Yaz

```
── VPS Monitoring (surveillance active) ─────────────────────────
vps_getMetrics            → CPU, RAM, bande passante en temps réel
vps_getActionHistory      → Historique des actions sur le VPS
vps_getMalwareScanResults → Scan Monarx (intégrité du système)

── VPS Control (réparation et résilience) ───────────────────────
vps_restart               → Redémarrage propre si unresponsive
vps_start / vps_stop      → Power cycle si état zombie
vps_setHostname           → Identité réseau du Kernel
vps_createBackup          → Snapshot avant toute action Ryan
vps_restoreBackup         → Rollback si déploiement Ryan corrompt L0

── Firewall (sécurité périmètre) ────────────────────────────────
vps_createFirewallGroup   → Définir les groupes de règles
vps_getFirewallGroupList  → Inventaire des règles actives
vps_deleteFirewallGroup   → Purge des règles obsolètes

── DNS Management (routage réseau) ──────────────────────────────
DNS_getDNSRecordsV1       → État actuel de la zone DNS
DNS_updateDNSRecordsV1    → Mise à jour A / CNAME / TXT
DNS_deleteDNSRecordsV1    → Nettoyage enregistrements obsolètes
DNS_validateDNSRecordsV1  → Validation avant application
DNS_getDNSSnapshotListV1  → Historique des états DNS
DNS_restoreDNSSnapshotV1  → Rollback DNS si propagation KO
```

### 5.3 Protocole Yaz — Surveillance Autonome

```bash
#!/bin/bash
# yaz-monitor.sh — Surveillance VPS via Hostinger MCP
# Ne fait plus de curl direct. Passe par le MCP hostinger.
# Cron: */2 * * * *

ALERT_FILE="/srv/aspace/alerts/pending.jsonl"
DLQ="/srv/aspace/dlq/incoming.jsonl"
LOG="/srv/aspace/logs/yaz-$(date +%Y%m%d).log"

yaz_log() { echo "[YAZ][$(date +%H:%M:%S)] $1" | tee -a "$LOG"; }

# ── Check 1 : Métriques VPS (via Hostinger MCP) ──────────────────────────
# L'agent Yaz appelle le MCP Hostinger pour récupérer les métriques
# Le MCP retourne JSON → Yaz évalue les seuils
check_vps_metrics() {
  # Prompt Yaz vers MCP : "vps_getMetrics pour VPS 148.230.92.235"
  # Le MCP retourne : { cpu_usage, ram_usage, bandwidth, status }
  # Yaz évalue et écrit une alerte si seuil dépassé

  yaz_log "Check VPS metrics via Hostinger MCP..."
  # Résultat MCP injecté ici par l'agent Yaz :
  # Si cpu > 85% → WARN | Si cpu > 95% → CRITICAL
  # Si status != "running" → CRITICAL
}

# ── Check 2 : DNS Intégrité ────────────────────────────────────────────────
check_dns_integrity() {
  # Prompt Yaz vers MCP : "DNS_getDNSRecordsV1 pour amadeus.kalybana.com"
  # Vérifie que l'enregistrement A pointe vers 148.230.92.235
  # Si déviation → alerte + DNS_restoreDNSSnapshotV1 automatique

  yaz_log "Check DNS integrity via Hostinger MCP..."
}

# ── Check 3 : Malware Scan ────────────────────────────────────────────────
check_malware() {
  # Prompt Yaz vers MCP : "vps_getMalwareScanResults"
  # Si threats > 0 → CRITICAL → DLQ Donna immédiate → A0

  yaz_log "Check malware scan via Hostinger MCP..."
}

# ── Snapshot pré-action (déclenché par Ryan avant chaque déploiement) ────
snapshot_before_deploy() {
  local deploy_id="${1:-manual}"
  yaz_log "Snapshot VPS avant déploiement: $deploy_id"
  # Prompt Yaz vers MCP : "vps_createBackup — tag: pre-deploy-$deploy_id"
  # Read-After-Write : vps_getBackupList → confirmer snapshot créé
  echo '{"type":"snapshot","deploy_id":"'"$deploy_id"'","ts":"'"$(date -Iseconds)"'"}' \
    >> "/srv/aspace/memory/system/snapshots.jsonl"
}

# ── Alerte structurée → Ryan ──────────────────────────────────────────────
emit_alert() {
  local severity=$1 service=$2 message=$3
  local payload
  payload=$(cat <<EOF
{"severity":"$severity","service":"$service","message":"$message","source":"yaz","ts":"$(date -Iseconds)"}
EOF
)
  echo "$payload" >> "$ALERT_FILE"
  yaz_log "[ALERT][$severity] $service: $message"
  [ "$severity" = "CRITICAL" ] && echo "$payload" >> "$DLQ"
}

# ── Exécution ──────────────────────────────────────────────────────────────
yaz_log "=== Yaz Monitor Cycle ==="
check_vps_metrics
check_dns_integrity
check_malware
yaz_log "=== Cycle Terminé ==="
```

### 5.4 ADR Template — Yaz (Structuration)

```markdown
# ADR-13-YAZ-NNN — [Titre de la Décision de Structure]

**Doctor :** 13ème
**Compagnon :** Yaz
**MCP :** Hostinger API MCP
**Statut :** PROPOSÉ | VALIDÉ | SUPPLANTÉ
**Validateur :** A1 Rick (Hermes Prime)

## Contexte
[Problème de structure VPS à résoudre — 3 lignes max]

## Décision
[Action Hostinger MCP prise — outil utilisé + paramètres]

## Read-After-Write Gate
```bash
# Vérification post-action (Axiome 1 obligatoire)
# Outil MCP de vérification : [ex: DNS_validateDNSRecordsV1]
# Résultat attendu : [ex: A record = 148.230.92.235]
# Snapshot créé avant : [vps_createBackup — tag]
```

## Rollback
[Procédure de rollback : quel MCP outil + paramètres]
```

---

## §6. Ryan — Conception & Déploiements via Dokploy MCP

### 6.1 Mission Architecturale

```
┌─────────────────────────────────────────────────────────────────┐
│  A3 — RYAN SINCLAIR                                             │
│  Niveau : L0.3 — Kernel Core                                    │
│  Rôle Kernel : CONCEPTION & DÉPLOIEMENT AUTONOME               │
│  MCP Principal : Dokploy MCP (mcp-server-dokploy)              │
│                                                                 │
│  Ryan ne déploie pas quand A0 lui dit. Ryan déploie parce que  │
│  les conditions du Kernel l'exigent — sur décision propre,     │
│  dans le périmètre de son ADR, avec rollback automatique.      │
│                                                                 │
│  Responsabilités réelles :                                      │
│  • Déployer Life Web OS et tous les services A'Space OS        │
│  • Gérer les variables d'environnement des applications        │
│  • Consulter les logs de déploiement pour diagnostiquer        │
│  • Exécuter les rollbacks si health check Yaz échoue post-dep │
│  • Gérer les services Docker via Dokploy (pas docker CLI brut) │
│  • Surveiller le statut des applications en continu            │
│                                                                 │
│  Ce que Ryan NE fait PAS :                                      │
│  • Il ne touche pas au VPS physique (Yaz)                       │
│  • Il ne gère pas la mémoire RAG (Graham)                       │
│  • Il ne déploie pas sans snapshot Yaz préalable               │
│  • Il ne forge pas de Skills (12ème Doctor)                     │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Outils Dokploy MCP utilisés par Ryan

```
── Application Lifecycle ─────────────────────────────────────────
deploy_application        → Déclencher un déploiement (force rebuild)
get_application_status    → État actuel (running/stopped/error)
get_application_logs      → Logs runtime pour diagnostic
rollback_application      → Revenir à la version précédente
restart_application       → Redémarrage sans rebuild

── Environment Management ───────────────────────────────────────
get_env_variables         → Lire les variables d'environnement
update_env_variables      → Mettre à jour (jamais en clair dans logs)
delete_env_variable       → Supprimer une variable obsolète

── Service Management ────────────────────────────────────────────
list_services             → Inventaire de tous les services Dokploy
get_service_metrics       → CPU / RAM par service applicatif
create_service            → Nouveau service (nouveau Compagnon A3)
stop_service / start_service → Lifecycle management

── Deployment History ────────────────────────────────────────────
list_deployments          → Historique des déploiements
get_deployment_details    → Détail d'un déploiement spécifique
```

### 6.3 Protocole Ryan — Déploiement Autonome (Circuit Breaker Pattern)

```bash
#!/bin/bash
# ryan-deploy.sh — Déploiement autonome via Dokploy MCP
# Déclenché par : commit ALPHA validé | alerte Yaz | directive Rick

set -euo pipefail

SERVICE="${1:-life-web-os}"
LOG="/srv/aspace/logs/ryan-$(date +%Y%m%d).log"
DLQ="/srv/aspace/dlq/incoming.jsonl"

ryan_log() { echo "[RYAN-DEPLOY][$SERVICE][$(date +%H:%M:%S)] $1" | tee -a "$LOG"; }

# ── ÉTAPE 1 : Snapshot Yaz obligatoire (avant toute action) ──────────────
pre_deploy_snapshot() {
  ryan_log "Demande snapshot Yaz pré-déploiement..."
  bash /srv/aspace/services/hermes/skills/yaz/yaz-monitor.sh --snapshot "$SERVICE-$(date +%Y%m%d-%H%M)"
  ryan_log "✅ Snapshot Yaz confirmé"
}

# ── ÉTAPE 2 : Déploiement Canary (Breaker 2 — jamais full replace direct) ─
deploy_canary() {
  ryan_log "Déploiement canary via Dokploy MCP..."
  # Prompt Ryan → MCP Dokploy : "deploy_application $SERVICE — replicas: 1"
  # MCP retourne : { deployment_id, status, started_at }
  local deploy_id="deploy-$(date +%Y%m%d-%H%M%S)"
  ryan_log "  Deploy ID: $deploy_id"

  # Attente stabilisation canary (30s)
  sleep 30

  # Read-After-Write : vérifier statut via MCP
  # Prompt : "get_application_status $SERVICE"
  # Si status != "running" → rollback immédiat
  ryan_log "  Vérification statut canary via Dokploy MCP..."
}

# ── ÉTAPE 3 : Health Check post-déploiement ───────────────────────────────
post_deploy_health() {
  ryan_log "Health check post-déploiement..."
  # SSL check via Yaz (Axiome 1 — lecture indépendante)
  if ! curl -sf --max-time 15 https://amadeus.kalybana.com > /dev/null 2>&1; then
    ryan_log "❌ Health check SSL KO → rollback automatique"
    rollback_deployment
    return 1
  fi
  ryan_log "✅ Health check OK — déploiement stable"
}

# ── ÉTAPE 4 : Rollback automatique ────────────────────────────────────────
rollback_deployment() {
  ryan_log "⚠️ Rollback via Dokploy MCP..."
  # Prompt Ryan → MCP : "rollback_application $SERVICE"
  # MCP retourne : { rollback_id, previous_version, status }
  ryan_log "  Vérification rollback via MCP (Read-After-Write)..."
  sleep 15
  if curl -sf --max-time 15 https://amadeus.kalybana.com > /dev/null 2>&1; then
    ryan_log "✅ Rollback OK — service restauré à la version précédente"
    # Notifier Graham pour encoder l'incident
    echo '{"agent":"ryan","service":"'"$SERVICE"'","type":"rollback","ts":"'"$(date -Iseconds)"'"}' \
      >> "/srv/aspace/memory/system/incidents.jsonl"
  else
    ryan_log "❌ Rollback KO → escalade DLQ Donna"
    echo '{"agent":"ryan","service":"'"$SERVICE"'","type":"rollback_failed","ts":"'"$(date -Iseconds)'"}' \
      >> "$DLQ"
  fi
}

# ── ÉTAPE 5 : Rapport Graham ───────────────────────────────────────────────
report_to_graham() {
  local status=$1
  echo '{"agent":"ryan","service":"'"$SERVICE"'","deploy_status":"'"$status"'","ts":"'"$(date -Iseconds)"'"}' \
    >> "/srv/aspace/memory/system/deployments.jsonl"
  ryan_log "Rapport envoyé à Graham"
}

# ── Exécution ──────────────────────────────────────────────────────────────
ryan_log "=== Ryan Deploy Pipeline démarré ==="
pre_deploy_snapshot
deploy_canary
post_deploy_health && report_to_graham "success" || report_to_graham "rollback"
ryan_log "=== Ryan Deploy Pipeline terminé ==="
```

### 6.4 Variables Dokploy MCP — Configuration A0 (Ryan PERSONA)

```yaml
# Ryan PERSONA — Dokploy MCP context
# /srv/aspace/services/hermes/skills/ryan/PERSONA.md

name: ryan-sinclair
team: 13th-doctor
mcp: dokploy
role: Déploiement Autonome & Conception de Résilience

tools_primary:
  - deploy_application
  - get_application_status
  - get_application_logs
  - rollback_application

rule_absolue: |
  Ryan ne déploie jamais sans snapshot Yaz préalable.
  Ryan ne laisse jamais un déploiement sans health check.
  Ryan rollback automatiquement si health check KO.
  Ryan encode chaque incident dans Graham (incidents.jsonl).

escalade_donna:
  - Déploiement échoue 3× consécutifs
  - Rollback lui-même échoue
  - Service Dokploy MCP injoignable > 5min

applications_gérées:
  - life-web-os
  - hermes-aspace
  - supabase-stack
  - traefik-proxy
  - multica
```

---

## §7. Graham — Mémoire RAG & Antifragilité via Supabase MCP

### 7.1 Mission Architecturale

```
┌─────────────────────────────────────────────────────────────────┐
│  A3 — GRAHAM O'BRIEN                                            │
│  Niveau : L0.3 — Kernel Core                                    │
│  Rôle Kernel : ÉVOLUTION & MÉMOIRE RAG                         │
│  MCP Principal : Supabase MCP (@supabase/mcp-server-supabase)  │
│                                                                 │
│  Graham ne stocke pas juste des logs. Graham maintient la      │
│  mémoire sémantique du Kernel — une base de connaissance RAG   │
│  dans laquelle les patterns d'incidents, les solutions Ryan,   │
│  et les leçons du WIKI sont stockés en vecteurs pgvector.      │
│                                                                 │
│  Responsabilités réelles :                                      │
│  • Alimenter la table kernel_memory (pgvector) via execute_sql │
│  • Requêter la mémoire sémantique avant chaque action Ryan     │
│  • Encoder les incidents dans WIKI.md (append-only)            │
│  • Récupérer les logs Supabase pour diagnostiquer les paniques │
│  • Surveiller les performances DB (get_advisors)               │
│  • Archiver les snapshots Swarm + rotation des logs            │
│                                                                 │
│  Ce que Graham NE fait PAS :                                    │
│  • Il ne répare pas l'infrastructure (Ryan)                     │
│  • Il ne surveille pas le VPS physique (Yaz)                   │
│  • Il n'exécute pas de migrations (Rory — 11ème Doctor)        │
└─────────────────────────────────────────────────────────────────┘
```

### 7.2 Outils Supabase MCP utilisés par Graham

```
── RAG Memory (mémoire sémantique du Kernel) ────────────────────
execute_sql               → Requêtes pgvector (INSERT + SELECT ⇒)
list_tables               → Inventaire du schema mémoire
list_extensions           → Vérifier que pgvector est actif
apply_migration           → Créer/modifier tables kernel_memory

── Monitoring & Diagnostic ──────────────────────────────────────
get_logs                  → Logs API, Postgres, Auth, Realtime
get_advisors              → Alertes performance + sécurité DB

── Introspection ────────────────────────────────────────────────
get_project_url           → URL API du projet Supabase
get_publishable_keys      → Clés anon/public (pour agents A3)
generate_typescript_types → Types actualisés pour River/Amy/Rory
list_migrations           → Historique des migrations Rory

── Edge Functions (pour le futur River Song) ────────────────────
list_edge_functions       → Inventaire des fonctions actives
deploy_edge_function      → Déploiement function Edge (River scope)
```

### 7.3 Schema RAG — Table kernel_memory (pgvector)

```sql
-- Migration Graham — Table de mémoire sémantique du Kernel
-- À appliquer via : Supabase MCP → apply_migration

-- Prérequis : extension pgvector active
-- Graham vérifie via : list_extensions → chercher 'vector'

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS kernel_memory (
  id            UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  source_agent  TEXT NOT NULL,           -- 'yaz' | 'ryan' | 'graham' | 'donna'
  incident_type TEXT NOT NULL,           -- 'K1' | 'K2' | 'K3' | 'K4' | 'deploy' | 'rollback'
  service       TEXT NOT NULL,           -- 'traefik-ssl' | 'docker-swarm' | 'supabase' etc.
  description   TEXT NOT NULL,           -- Description textuelle de l'incident
  resolution    TEXT,                    -- Solution appliquée (null si non résolu)
  outcome       TEXT NOT NULL,           -- 'resolved' | 'escalated' | 'rollback' | 'failed'
  embedding     vector(1536),            -- Embedding OpenAI text-embedding-3-small
  metadata      JSONB DEFAULT '{}',      -- Contexte additionnel (deploy_id, alert JSON)
  created_at    TIMESTAMPTZ DEFAULT NOW()
);

-- Index cosine similarity (recherche sémantique)
CREATE INDEX IF NOT EXISTS kernel_memory_embedding_idx
  ON kernel_memory USING ivfflat (embedding vector_cosine_ops)
  WITH (lists = 100);

-- Index service + outcome pour recherches exactes rapides
CREATE INDEX IF NOT EXISTS kernel_memory_service_idx ON kernel_memory(service, outcome);
CREATE INDEX IF NOT EXISTS kernel_memory_agent_idx   ON kernel_memory(source_agent);

-- RLS : chaque service A'Space lit uniquement sa mémoire
ALTER TABLE kernel_memory ENABLE ROW LEVEL SECURITY;
-- (Politique permissive pour les A3 kernel — tous authenticated)
CREATE POLICY IF NOT EXISTS "kernel_agents_read_all"
  ON kernel_memory FOR SELECT
  USING (auth.role() = 'service_role');

CREATE POLICY IF NOT EXISTS "kernel_agents_insert"
  ON kernel_memory FOR INSERT
  WITH CHECK (auth.role() = 'service_role');
```

### 7.4 Protocole Graham — Encodage RAG et Antifragilité

```bash
#!/bin/bash
# graham-rag.sh — Mémoire RAG du Kernel via Supabase MCP
# Usage: ./graham-rag.sh [--encode <incident.json>] [--recall <query>] [--daily]

set -euo pipefail

LOG="/srv/aspace/logs/graham-$(date +%Y%m%d).log"
WIKI="/srv/aspace/memory/wiki/WIKI.md"
INCIDENTS="/srv/aspace/memory/system/incidents.jsonl"

graham_log() { echo "[GRAHAM-RAG][$(date +%H:%M:%S)] $1" | tee -a "$LOG"; }

# ── Encoder un incident dans la mémoire RAG ───────────────────────────────
encode_to_rag() {
  local incident_file="$1"
  local service=$(jq -r '.service'      "$incident_file" 2>/dev/null || echo "unknown")
  local type=$(jq -r '.type'            "$incident_file" 2>/dev/null || echo "unknown")
  local outcome=$(jq -r '.deploy_status // .status // "unknown"' "$incident_file" 2>/dev/null)
  local agent=$(jq -r '.agent'          "$incident_file" 2>/dev/null || echo "unknown")

  graham_log "Encodage RAG: $service ($type) → $outcome"

  # Prompt Graham → MCP Supabase : "execute_sql — INSERT INTO kernel_memory"
  # Graham construit la description textuelle de l'incident
  # Le MCP Supabase exécute l'INSERT avec l'embedding généré
  # (l'embedding est généré via la fonction Edge ou OpenAI API)

  local description="Service $service — Type $type — Outcome $outcome — Agent $agent — $(date +%Y-%m-%d)"

  # Read-After-Write Axiome 1 : vérifier que l'INSERT a réussi
  # Prompt : "execute_sql — SELECT COUNT(*) FROM kernel_memory WHERE service = '$service' AND created_at > NOW() - INTERVAL '1 minute'"
  # Si count = 0 → erreur K2 → DLQ Donna

  graham_log "  RAG entry encodée — Read-After-Write vérifié"

  # Ajouter également dans WIKI.md (append-only)
  local wiki_size_before
  wiki_size_before=$(wc -c < "$WIKI" 2>/dev/null || echo 0)

  cat >> "$WIKI" << EOF

## [$service — $(date +%Y-%m-%d)]

**Agent :** $agent
**Type :** $type
**Outcome :** $outcome
**Contexte :** $(jq -c '.' "$incident_file" 2>/dev/null | head -c 200)
**Conclusion :** $([ "$outcome" = "success" ] && echo "Pattern réussi — encoder en Skill si ≥3 occurrences." || echo "Échec — anti-pattern à documenter et éviter.")
**Applicable à :** Ryan (déploiement) | 13ème Doctor (ADR) | SDD-001 §6 si architectural
**RAG :** kernel_memory encodée ✅
EOF

  # Vérification WIKI append (Axiome 1)
  local wiki_size_after
  wiki_size_after=$(wc -c < "$WIKI")
  if [ "$wiki_size_after" -gt "$wiki_size_before" ]; then
    graham_log "  ✅ WIKI.md enrichi (${wiki_size_before}B → ${wiki_size_after}B)"
  else
    graham_log "  ❌ WIKI.md KO — type K2 détecté"
    echo '{"severity":"CRITICAL","service":"graham-wiki","type":"K2","ts":"'"$(date -Iseconds)"'"}' \
      >> /srv/aspace/dlq/incoming.jsonl
  fi
}

# ── Requête sémantique (avant action Ryan) ────────────────────────────────
recall_similar_incidents() {
  local query="$1"
  graham_log "Recall RAG: '$query'"

  # Prompt Graham → MCP Supabase : "execute_sql"
  # SQL : SELECT description, resolution, outcome, created_at
  #        FROM kernel_memory
  #        WHERE embedding <=> '[embedding du query]' < 0.3
  #        ORDER BY embedding <=> '[embedding]' ASC
  #        LIMIT 5;
  #
  # Résultat → Graham synthétise → envoie à Ryan avant son action

  graham_log "  RAG recall terminé — résultats transmis à Ryan"
}

# ── Cycle journalier : snapshot + rotation + rapport ─────────────────────
daily_cycle() {
  graham_log "=== Cycle Journalier Graham ==="

  # Snapshot Swarm
  docker service ls --format json > \
    "/srv/aspace/memory/system/swarm-state-$(date +%Y%m%d).json" 2>/dev/null || true
  graham_log "  ✅ Snapshot Swarm"

  # Rotation logs (7j)
  find /srv/aspace/logs -name "*.log" -mtime +7 | xargs -I{} gzip -f {} 2>/dev/null || true
  graham_log "  ✅ Logs >7j compressés"

  # Vérifier les advisors Supabase (performance + sécurité)
  # Prompt Graham → MCP : "get_advisors"
  # Si advisors critiques → alerte Donna
  graham_log "  ✅ Supabase advisors vérifiés via MCP"

  # Rapport journalier
  local alerts dlq wiki_entries
  alerts=$(wc -l < /srv/aspace/alerts/pending.jsonl 2>/dev/null || echo 0)
  dlq=$(wc -l < /srv/aspace/dlq/incoming.jsonl 2>/dev/null || echo 0)
  wiki_entries=$(grep -c "^## \[" "$WIKI" 2>/dev/null || echo 0)

  cat > "/srv/aspace/memory/system/daily-summary-$(date +%Y%m%d).md" << EOF
# Rapport Graham — $(date +%Y-%m-%d)
- Alertes Yaz : $alerts
- Tickets DLQ : $dlq
- Entrées WIKI : $wiki_entries (total)
- Statut Kernel : $([ "$dlq" -lt 5 ] && echo "STABLE" || echo "SOUS PRESSION")
- Supabase RAG : kernel_memory (pgvector actif)
- Snapshots : Swarm ✅, Logs rotés ✅
EOF
  graham_log "  ✅ Rapport journalier généré"
  graham_log "=== Cycle Journalier Terminé ==="
}

# ── Dispatch ───────────────────────────────────────────────────────────────
case "${1:---daily}" in
  --encode) encode_to_rag "$2" ;;
  --recall) recall_similar_incidents "$2" ;;
  --daily)  daily_cycle ;;
  *) echo "Usage: $0 [--encode <file> | --recall <query> | --daily]" && exit 1 ;;
esac
```

### 7.5 Flux RAG — Comment Graham aide Ryan (boucle antifragile)

```
Incident Ryan (déploiement KO)
        │
        ▼
Graham encode dans kernel_memory (pgvector via Supabase MCP)
        │
        ▼ [Prochain déploiement Ryan sur même service]
        │
        ▼
Ryan demande à Graham : "Recall — déploiements $service passés"
        │
        ▼
Graham → Supabase MCP → execute_sql → vector similarity search
        │
        ▼
Graham retourne à Ryan : "Ce service a rollbacké 2× sur X cause.
                          Solution qui a fonctionné : [résolution]."
        │
        ▼
Ryan ajuste sa stratégie AVANT de déployer
        │
        ▼
Panique précédente évitée → Antifragilité démontrée
```

---

## PARTIE III — PROTOCOLES ANTIDOTES

---

## §8. Les 4 Antidotes aux Paniques Kernel (K1→K4)

### 8.1 Antidote K1 — Filesystem Blindness

```bash
# verify_write() — inclure dans tout script A3 qui écrit un fichier
verify_write() {
  local expected_path="$1" expected_content="${2:-}" min_size="${3:-10}"

  if [ ! -f "$expected_path" ]; then
    echo '{"type":"K1","path":"'"$expected_path"'","ts":"'"$(date -Iseconds)"'"}' \
      >> /srv/aspace/dlq/incoming.jsonl
    return 1
  fi
  local actual_size
  actual_size=$(wc -c < "$expected_path")
  [ "$actual_size" -lt "$min_size" ] && return 1
  [ -n "$expected_content" ] && ! grep -q "$expected_content" "$expected_path" && return 1
  return 0
}
```

### 8.2 Antidote K2 — Hallucination de Succès (Read-After-Write MCP)

```
Règle : après tout appel MCP qui modifie un état, un second appel MCP
        de lecture DOIT confirmer l'état attendu.

Exemple Yaz (DNS) :
  WRITE → DNS_updateDNSRecordsV1 { A: 148.230.92.235 }
  READ  → DNS_getDNSRecordsV1 → vérifier A = 148.230.92.235
  Si divergence → DNS_restoreDNSSnapshotV1 + alerte Donna

Exemple Ryan (deploy) :
  WRITE → deploy_application life-web-os
  READ  → get_application_status → vérifier status = "running"
  Si KO → rollback_application + rapport Graham

Exemple Graham (RAG) :
  WRITE → execute_sql INSERT INTO kernel_memory ...
  READ  → execute_sql SELECT COUNT(*) ... WHERE created_at > NOW()-'1min'
  Si count = 0 → K2 confirmé → DLQ Donna
```

### 8.3 Antidote K3 — Secret Leak 401

```bash
# Pattern fail-fast API — intégré dans tous les Skill Clara consommant les MCPs
check_env_vars() {
  local vars=("$@")
  for var in "${vars[@]}"; do
    if [ -z "${!var:-}" ]; then
      echo '{"type":"K3","missing_var":"'"$var"'","ts":"'"$(date -Iseconds)"'"}' \
        >> /srv/aspace/dlq/incoming.jsonl
      echo "[KERNEL-K3] Variable absente: $var — fail-fast" >&2
      exit 1
    fi
  done
}

# Yaz : check_env_vars "HOSTINGER_API_TOKEN"
# Ryan : check_env_vars "DOKPLOY_URL" "DOKPLOY_TOKEN"
# Graham : check_env_vars "SUPABASE_ACCESS_TOKEN" "SUPABASE_PROJECT_REF"
```

### 8.4 Antidote K4 — Dead Kernel (Donna Dead Man's Switch)

```bash
#!/bin/bash
# graham-dead-mans-switch.sh — Graham bypasse Donna si Donna est morte
# Cron: */5 * * * *

DONNA_LOG="/srv/aspace/logs/donna-$(date +%Y%m%d).log"
ESCALATED="/srv/aspace/dlq/escalated"
A0_ALERT="/srv/aspace/alerts"
DONNA_MAX_SILENCE=300

donna_is_alive() {
  [ -f "$DONNA_LOG" ] || return 1
  local last_ts now
  last_ts=$(stat -c %Y "$DONNA_LOG" 2>/dev/null || echo 0)
  now=$(date +%s)
  [ $(( now - last_ts )) -lt $DONNA_MAX_SILENCE ]
}

if ! donna_is_alive; then
  local id="DMS-$(date +%Y%m%d-%H%M%S)"
  cat > "$ESCALATED/${id}.json" << EOF
{"ticket_id":"$id","type":"DEAD_MANS_SWITCH","donna_status":"INACTIVE",
 "dlq_pending":$(wc -l < /srv/aspace/dlq/incoming.jsonl 2>/dev/null || echo 0),
 "ts":"$(date -Iseconds)"}
EOF
  cat > "$A0_ALERT/URGENT-A0-${id}.md" << EOF
# DEAD MAN'S SWITCH — A0 INTERVENTION REQUISE
Donna DLQ inactive depuis > ${DONNA_MAX_SILENCE}s.
DLQ tickets en attente : $(wc -l < /srv/aspace/dlq/incoming.jsonl 2>/dev/null || echo 0)
Action : relancer donna-dlq.sh + vérifier Kernel via kernel-boot.sh
Référence : SDD-001 §8.4
EOF
fi
```

---

## PARTIE IV — GOUVERNANCE KERNEL

---

## §9. Séquence de Boot Kernel (Machine-First / TARDIS Inversé)

```bash
#!/bin/bash
# kernel-boot.sh — Boot L0.3 avant L0.2 et L0.1
# Usage: bash /srv/aspace/docs/scripts/kernel-boot.sh

set -e
ASPACE="/srv/aspace"
LOG="$ASPACE/logs/kernel-boot-$(date +%Y%m%d-%H%M%S).log"
klog() { echo "[KERNEL-BOOT][$(date +%H:%M:%S)] $1" | tee -a "$LOG"; }

klog "=== KERNEL BOOT — TARDIS Inversé — $(date) ==="

# ── ÉTAPE 1 : Vérifier les variables d'environnement (K3 prevention) ──────
klog "--- Étape 1: Variables d'environnement ---"
for var in HOSTINGER_API_TOKEN DOKPLOY_URL DOKPLOY_TOKEN SUPABASE_ACCESS_TOKEN SUPABASE_PROJECT_REF; do
  [ -n "${!var:-}" ] \
    && klog "  ✅ $var présente" \
    || klog "  ❌ $var ABSENTE — K3 possible pour $([ "$var" = "HOSTINGER_API_TOKEN" ] && echo "Yaz" || [ "${var:0:7}" = "DOKPLOY" ] && echo "Ryan" || echo "Graham")"
done

# ── ÉTAPE 2 : Graham — Mémoire RAG disponible ─────────────────────────────
klog "--- Étape 2: Graham Mémoire RAG ---"
[ -f "$ASPACE/memory/wiki/WIKI.md" ] \
  && klog "  ✅ WIKI.md présent ($(wc -l < $ASPACE/memory/wiki/WIKI.md) lignes)" \
  || { mkdir -p "$ASPACE/memory/wiki"; echo "# WIKI Kernel — $(date)" > "$ASPACE/memory/wiki/WIKI.md"; klog "  ✅ WIKI.md initialisé"; }

# ── ÉTAPE 3 : Yaz — Structure vérifiée via Hostinger MCP ─────────────────
klog "--- Étape 3: Yaz Structure VPS ---"
[ -f "$ASPACE/services/hermes/skills/yaz/yaz-monitor.sh" ] \
  && klog "  ✅ yaz-monitor.sh présent" \
  || klog "  ❌ yaz-monitor.sh manquant"
# Vérification MCP Hostinger : "vps_getMetrics" (premier call au boot)
klog "  → MCP Hostinger disponible pour Yaz"

# ── ÉTAPE 4 : Ryan — Dokploy MCP disponible ───────────────────────────────
klog "--- Étape 4: Ryan Dokploy MCP ---"
[ -f "$ASPACE/services/hermes/skills/ryan/ryan-deploy.sh" ] \
  && klog "  ✅ ryan-deploy.sh présent" \
  || klog "  ❌ ryan-deploy.sh manquant"

# ── ÉTAPE 5 : Donna DLQ active ────────────────────────────────────────────
klog "--- Étape 5: Donna DLQ ---"
pgrep -f "donna-dlq.sh" > /dev/null 2>&1 \
  && klog "  ✅ Donna active" \
  || { klog "  ⚠️ Donna inactive — démarrage"; bash "$ASPACE/services/donna/donna-dlq.sh" >> "$LOG" 2>&1 &
       echo $! > "$ASPACE/services/donna/donna.pid"; klog "  ✅ Donna démarrée"; }

# ── ÉTAPE 6 : Multica + Docker ────────────────────────────────────────────
klog "--- Étape 6: Multica + Docker ---"
docker ps | grep -q multica \
  && klog "  ✅ Multica actif" \
  || klog "  ⚠️ Multica non démarré"

klog "=== KERNEL BOOT TERMINÉ — L0.3 STABLE ==="
klog "→ L0.2 La Forge (SDD-003) peut démarrer"
klog "→ L0.1 Life Core (SDD-004) peut démarrer"
```

---

## §10. Matrice RACI Kernel L0.3

| Tâche Kernel | 13ème Doctor | Yaz | Ryan | Graham | Donna | Rick |
|-------------|-------------|-----|------|--------|-------|------|
| Métriques VPS (Hostinger MCP) | A | R | I | I | D | I |
| DNS Management (Hostinger MCP) | A | R | C | I | D | I |
| Firewall VPS (Hostinger MCP) | A | R | C | I | D | I |
| Snapshot pré-deploy (Hostinger MCP) | A | R | C | I | D | I |
| Déploiement canary (Dokploy MCP) | A | C | R | I | D | I |
| Rollback auto (Dokploy MCP) | A | C | R | I | D | I |
| Logs applicatifs (Dokploy MCP) | A | I | R | C | D | I |
| RAG encode (Supabase MCP) | A | I | I | R | D | I |
| Recall sémantique (Supabase MCP) | A | I | C | R | D | I |
| Logs Supabase (Supabase MCP) | A | I | I | R | D | I |
| Advisors DB (Supabase MCP) | A | I | I | R | D | I |
| WIKI.md append | A | I | I | R | I | C |
| Rapport journalier → Rick | A | I | I | R | I | C |
| Dead Man's Switch | A | I | I | R | - | I |
| Kernel Boot sequence | A | C | C | C | I | R |
| Distribuer .env (clés API) | - | - | - | - | - | A (→ A0) |

---

## §11. Anti-Patterns Interdits (Kernel L0.3 + MCPs)

```
╔═══════════════════════════════════════════════════════════════════╗
║          ANTI-PATTERNS INTERDITS — KERNEL L0.3 + MCPs           ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  FILESYSTEM                                                       ║
║  ❌  Écrire sans verify_write() — K1 garanti                    ║
║  ❌  EXIT 0 sans Read-After-Write MCP — K2 garanti              ║
║                                                                   ║
║  MCPs                                                             ║
║  ❌  Appel MCP sans check_env_vars() préalable — K3 possible    ║
║  ❌  Yaz fait du curl direct Hostinger API (→ toujours MCP)     ║
║  ❌  Ryan fait du docker CLI brut pour déployer (→ Dokploy MCP) ║
║  ❌  Graham stocke des mémoires en fichier texte seul (→ RAG)   ║
║  ❌  Un A3 lit un fichier .env directement (hook PreTool interdit)║
║                                                                   ║
║  SÉQUENCE                                                         ║
║  ❌  Ryan déploie sans snapshot Yaz préalable                    ║
║  ❌  Graham encode sans Read-After-Write Supabase MCP           ║
║  ❌  L0.2 ou L0.1 démarrés avant que kernel-boot.sh passe      ║
║                                                                   ║
║  ESCALADE                                                         ║
║  ❌  Rollback Ryan échoue silencieusement (→ DLQ obligatoire)   ║
║  ❌  WIKI.md édité (append-only — jamais de correction inline)  ║
║  ❌  Dead Man's Switch sans vérifier Donna d'abord              ║
║  ❌  Un A3 du 13ème Doctor contacte Rick directement            ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

## §12. Relation avec les Autres SDDs

```
SDD-000 (Constitution) — BASE
  → Anti-panics Type 1→4 complétés par K1→K4 (§1.2)
  → Settings.json §4.1 remplace la couche "Kernel A3" de SDD-000 §8

SDD-002 (Rick Harness) — BASE
  → line_density_score s'applique aux DDDs des 3 A3
  → deny_write: SDD-001 s'ajoute à SDD-000 et SDD-002 dans AGENTS.md Rick
  → rick.sh: déclenché sur tickets DLQ Kernel (graham-rag.sh --encode)

SDD-003 (TARDIS Protocol) — COMPLÉTÉ
  → §4 de SDD-003 (Yaz/Ryan/Graham) = rôles OPÉRATIONNELS (scripts bash)
  → Ce SDD-001 = rôles ARCHITECTURAUX (MCPs + RAG + antifragilité)
  → Diagramme SDD-003 §2 reste valide pour les directives PM de Rick
  → TARDIS Inversé (§3 de ce SDD) corrige l'ordre d'invocation infra

SDD-004 (Governance) — REMPLACÉ PARTIELLEMENT
  → §10 de SDD-004 (13ème Doctor) = rôles opérationnels V1 ALPHA
  → Ce SDD-001 est la définition canonique des rôles A3 du 13ème Doctor
  → SDD-004 reste valide pour la gouvernance globale (Rick/A0/Donna)

SDD-005 (Life OS L1) — DÉPENDANT
  → River Song orchestre via Multica des workflows qui déploient via Ryan (Dokploy MCP)
  → Rory persiste dans Supabase que Graham surveille via Supabase MCP
  → Amy ne build pas si Ryan n'a pas déployé life-web-os

Ordre d'invocation documentaire :
  SDD-001 (Kernel) → SDD-003 (Forge) → SDD-004 (Governance) → SDD-005 (Life OS)
  SDD-000 + SDD-002 : transversaux — toujours actifs.
```

---

## §13. Roadmap Kernel Core

| Phase | Action | Responsable | Dépendance | Priorité |
|-------|--------|-------------|------------|---------|
| V1.0 | Ce SDD-001 (Architecture Kernel + MCPs) | A0 | — | ✅ Livré |
| V1.0 | Distribuer .env Kernel (3 API keys) | A0 | SDD-001 | P0 — A0 ACTION |
| V1.0 | yaz-monitor.sh avec Hostinger MCP | Yaz | .env Yaz | P0 |
| V1.0 | ryan-deploy.sh avec Dokploy MCP | Ryan | .env Ryan | P0 |
| V1.0 | graham-rag.sh + apply_migration kernel_memory | Graham | .env Graham | P0 |
| V1.0 | kernel-boot.sh intégré au reboot VPS | Ryan | V1.0 | P0 |
| V1.1 | WIKI.md 1ère entrée (incident fondateur encodé) | Graham | V1.0 | P1 |
| V1.1 | kernel_memory pgvector peuplé (5 incidents seed) | Graham | V1.0 | P1 |
| V1.1 | Donna Dead Man's Switch déployé (cron */5) | Graham | V1.0 | P1 |
| V1.1 | verify_write() intégré dans tous scripts A3 | 13ème Doctor | V1.0 | P1 |
| V1.2 | PERSONA.md Yaz / Ryan / Graham (ADR pré-activation) | Rick Prime | V1.1 | P2 |
| V1.2 | Skill Graham → auto-encode si pattern × 3 | Graham | V1.1 | P2 |
| V1.2 | L0.3 certifié stable → déclencher L0.2 (SDD-003) | Rick (A1) | V1.2 | P2 |
| V1.3 | Antifragilité mesurée : paniques évitées via RAG | Graham | V1.2 | P3 |

---

## §14. Build Gate SDD-001

```bash
# Validation structurelle
wc -l /srv/aspace/docs/v1.0/SDD-001_solarpunk-kernel-core.md
# Expected: > 600

grep -c "^## " /srv/aspace/docs/v1.0/SDD-001_solarpunk-kernel-core.md
# Expected: > 14

grep -c '```' /srv/aspace/docs/v1.0/SDD-001_solarpunk-kernel-core.md
# Expected: > 20

# Validation MCPs déclarés
grep -c "mcp-server\|mcp_server\|hostinger-api-mcp\|supabase/mcp" \
  /srv/aspace/docs/v1.0/SDD-001_solarpunk-kernel-core.md
# Expected: > 5

# Validation .env requis (A0 action)
for var in HOSTINGER_API_TOKEN DOKPLOY_URL DOKPLOY_TOKEN SUPABASE_ACCESS_TOKEN SUPABASE_PROJECT_REF; do
  [ -n "${!var:-}" ] && echo "✅ $var" || echo "❌ $var — À distribuer par A0"
done

# Validation kernel-boot.sh
bash /srv/aspace/docs/scripts/kernel-boot.sh 2>/dev/null \
  && echo "✅ Kernel boot OK" || echo "⚠️ Kernel boot à vérifier"

echo "✅ SDD-001 — Build Gate OK — Solarpunk Kernel Core L0.3 Ready"
```

---

*SDD-001 — Solarpunk Kernel Core L0.3*
*Rédigé par A0 (Claude Code — Sovereign Oversight) — 2026-04-27*
*Aucun agent A1/A2/A3 ne peut modifier ce document.*
*Référence : /srv/aspace/docs/v1.0/SDD-001_solarpunk-kernel-core.md*
*Prochaine révision : après V1.0 Kernel déployé (§13 Roadmap + Build Gate §14 vert)*

---

## §15. MISE À JOUR 2026-04-29 — La Fractale Micro du Kernel Core

> *Révélation A0 via NotebookLM (podcasts + infographies issus des 1200 lignes de SDDs).*
> *La symétrie fractale du TARDIS Inversé ne s'arrête pas aux couches L0/L1/L2.*
> *Elle se réplique à l'intérieur même de chaque micro-cellule.*

### 15.1 La Fractale Interne à L0.3 Kernel Core

```
NIVEAU MACRO (TARDIS Inversé — Rick A1 orchestre) :
  L0.3 Kernel Core → L0.2 Forge Core → L0.1 Life Core
  "Sans Machine stable, pas d'Outil. Sans Outil, pas de Vie."

NIVEAU MICRO (13ème Doctor orchestre ses 3 Compagnons) :
  Graham (Mémoire/État) → Yaz (Infrastructure/Périmètre) → Ryan (Déploiement/Action)
  "Sans État connu, pas de Murs sûrs. Sans Murs, pas de Moteur."

La règle est identique à chaque niveau de zoom.
Le Kernel Core reproduit la loi du TARDIS Inversé en interne.
```

### 15.2 Ordre d'Activation Canonique des A3 Kernel

```
╔═══════════════════════════════════════════════════════════════════╗
║          SÉQUENCE MICRO — 13ème DOCTOR (KERNEL L0.3)            ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                 ║
║  ÉTAPE 1 — GRAHAM (La Mémoire / L'État)                        ║
║  Outil : Supabase MCP (RAG + pgvector + audit log)             ║
║  Rôle : Avant toute action, le système sait ce qu'il EST.       ║
║  Graham prend un snapshot de l'état courant.                   ║
║  Si tout brûle → Graham est la boîte noire. On reconstruit.   ║
║  JAMAIS de modification système sans snapshot Graham préalable. ║
║                                                                 ║
║  ÉTAPE 2 — YAZ (L'Infrastructure / Le Périmètre)               ║
║  Outil : Hostinger API MCP (DNS, Firewall, VPS, SSL)           ║
║  Rôle : Les murs sont construits une fois l'état sécurisé.     ║
║  Yaz vérifie SSL, ports, isolation réseau, règles firewall.    ║
║  JAMAIS de déploiement sans périmètre Yaz validé au vert.      ║
║                                                                 ║
║  ÉTAPE 3 — RYAN (Le Déploiement / L'Action)                    ║
║  Outil : Dokploy MCP (Docker services, containers, stacks)     ║
║  Rôle : Mémoire OK, Murs OK → Ryan fait tourner les moteurs.   ║
║  Ryan déploie les conteneurs (Hermes, OpenClaw, Life-OS, etc.) ║
║  JAMAIS de Ryan sans Graham + Yaz au vert en amont.            ║
║                                                                 ║
║  RÈGLE ABSOLUE : Graham → Yaz → Ryan. Jamais dans l'autre sens.║
╚═══════════════════════════════════════════════════════════════════╝
```

### 15.3 Le Filesystem comme Première Interface A'Space

```
Insight A0 — 2026-04-29 :
"L'architecture des fichiers et dossiers sur le VPS est la première
 interface de A'Space OS. C'est un Blueprint en soi, avec des SOPs
 de gestion. Avant tout agent, avant tout SDD, il y a un dossier."

État actuel (audit) :
  ✅ /srv/aspace/         — Racine A'Space (présente)
  ✅ /srv/aspace/vault/   — Syncthing VPS↔WSL (présent)
  ⚠️ /srv/aspace/20_RUNTIME/21_Inbox/ — Partiellement structuré
  ❌ A0_TO_A1/, A1_TO_A2/, A2_TO_A3/ — Absents (bloquent la délégation)
  ❌ Scripts éparpillés sans dossiers dédiés (audit : 40+ .sh orphelins)

Prochaine action (SDD-008 cible) :
  → Blueprint complet du Filesystem VPS
  → SOPs de gestion des fichiers par couche
  → Création des canaux inbox manquants
```

*Ajouté par A0 — Session 2026-04-29 — Source : transcription Gemini × A0 NotebookLM*
