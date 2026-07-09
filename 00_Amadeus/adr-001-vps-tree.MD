# ADR-001 : Arborescence du VPS Hostinger

> **Statut :** DRAFT — En attente de validation par A-Amadou
> **Date :** 2026-04-07
> **Core :** Kernel (L0) — 13th Doctor
> **Décideur :** Rick (A1)

---

## Contexte

VPS Hostinger KVM 2 — Ubuntu 24.04 bare metal (Coolify désinstallé).
2 vCores, 8GB RAM, 100GB disque.
User unique : `amadeus` (non-root, sudoer).
Gestion des services : systemd.
Reverse proxy : différé (Caddy/Nginx/Traefik — choix contextuel futur).

## Décisions

1. **Bare metal** — pas de Docker, pas de PaaS. Tout est installé nativement.
2. **`/srv/aspace/`** = données servies par le système (backupable en une commande).
3. **`/home/amadeus/`** = config user + dotfiles agents (reconstructible par script).
4. **Séparation stricte** — les agents lisent/écrivent dans `/srv/aspace/`, mais leurs configs et binaires vivent dans `/home/amadeus/`.

---

## Arborescence complète

```
/srv/aspace/                          # RACINE SERVEUR — tout ce qui est "servi"
│
├── vault/                            # 🔄 AMADEUS_VERSE (Syncthing P2P)
│   ├── .stignore                     # Exclut logs chauds, .git, node_modules
│   │
│   ├── 00_ORIGIN/                    # 👑 Source biologique + Méta-Conscience
│   │   ├── a_amadou_core.md          # Limites biologiques, Ikigai, entropie
│   │   ├── a0_reasoning_map.md       # Filtre A0 (Clarify → Score → Route)
│   │   ├── ikigai_master.md          # IKIGAI 2.0 vivant
│   │   └── life_wheel_baseline.md    # Snapshot des 8 domaines
│   │
│   ├── 10_FORGE/                     # 🏗️ Stratégie & Architecture
│   │   ├── 11_Manifestos/            # Constitutions L0, L1, L2
│   │   │   ├── l0_kernel.md
│   │   │   ├── l1_life.md
│   │   │   └── l2_buz.md
│   │   ├── 12_Blueprints/            # PRDs et ADRs
│   │   │   ├── adr-001-vps-tree.md   # CE DOCUMENT
│   │   │   └── ...
│   │   └── 13_Templates/             # Modèles Markdown standardisés
│   │       ├── ticket_template.md
│   │       ├── adr_template.md
│   │       └── prd_template.md
│   │
│   ├── 20_RUNTIME/                   # ⚡ Le Markdown-as-API
│   │   ├── 21_Inbox/                 # Tickets déposés → en attente d'exécution
│   │   ├── 22_Active_WIP/            # Travaux en cours (scripts, brouillons)
│   │   └── 23_DLQ_Donna/             # Dead Letter Queue — crashs et erreurs
│   │
│   └── 30_MEMORY_CORE/               # 📚 Le Second Brain
│       ├── 31_Raw_Logs/              # Transcripts bruts (NON synchronisé P2P)
│       └── 32_Compiled_Wiki/         # Savoir distillé, leçons apprises
│
├── services/                         # 🛠️ DONNÉES RUNTIME des agents
│   ├── openclaw/                     # Sessions .jsonl, heartbeats, profils
│   │   ├── sessions/
│   │   ├── heartbeat.json
│   │   └── agents/                   # Profils des agents A3
│   ├── hermes/                       # Skills locaux, boucles de feedback
│   │   ├── skills/
│   │   └── feedback/
│   ├── paperclip/                    # DB runtime (si SQLite externe au dotfile)
│   │   └── runtime.db
│   ├── n8n/                          # Workflows, credentials (si installé)
│   │   └── data/
│   └── ollama/                       # Modèles LLM locaux (si installé)
│       └── models/
│
├── web/                              # 🌐 HÉBERGEMENT PUBLIC
│   ├── amadeuspace.com/              # Life Web OS — site principal
│   │   └── public/                   # Fichiers servis (HTML/CSS/JS/assets)
│   ├── agency/                       # Agency as a Service
│   │   └── public/
│   └── sob-hub/                      # SOB Hub
│       └── public/
│
└── backups/                          # 💾 SAUVEGARDES LOCALES
    ├── vault-snapshots/              # Snapshots périodiques du Vault
    │   └── YYYY-MM-DD/
    ├── services-snapshots/           # Snapshots des données agents
    │   └── YYYY-MM-DD/
    └── db-dumps/                     # Dumps de bases de données
        └── YYYY-MM-DD/


/home/amadeus/                        # CONFIG USER — reconstructible par script
│
├── .ssh/                             # Clés SSH
│   ├── authorized_keys
│   └── config
│
├── .openclaw/                        # Config OpenClaw (pointant vers /srv/aspace/services/openclaw/)
├── .hermes/                          # Config Hermes
├── .claude.json                      # Config Claude Code (permissions, hooks)
├── .paperclip/                       # Config Paperclip (SQLite UI interne)
│
├── .local/bin/                       # Scripts d'invocation rapide
│   ├── aspace-backup.sh              # Backup one-liner
│   ├── aspace-status.sh              # Health check de tous les services
│   └── aspace-sync-check.sh          # Vérifier état Syncthing
│
├── .bashrc                           # Aliases et PATH
├── .profile                          # Variables d'environnement
│
└── setup/                            # 🔧 Scripts de reconstruction
    ├── bootstrap.sh                  # Script maître : recrée tout le VPS from scratch
    ├── install-agents.sh             # Installe OpenClaw, Hermes, Paperclip, Claude Code
    ├── install-syncthing.sh          # Configure Syncthing + peers
    ├── install-runtime.sh            # n8n, Ollama (optionnel)
    └── systemd/                      # Fichiers .service pour chaque agent
        ├── openclaw.service
        ├── hermes.service
        ├── paperclip.service
        └── syncthing.service
```

---

## Conventions

### Nommage
- Dossiers : `snake_case` en minuscules
- Fichiers Markdown : `kebab-case.md` pour les documents, `snake_case.md` pour les configs
- Préfixes numériques (`00_`, `10_`, `20_`, `30_`) uniquement dans le Vault pour l'ordre de lecture

### Permissions
- `/srv/aspace/` : propriétaire `amadeus:amadeus`, droits `755` (dossiers) / `644` (fichiers)
- `/srv/aspace/vault/` : droits restreints `700` (données personnelles synchronisées)
- `/srv/aspace/web/*/public/` : lisible par le serveur web (`644`)
- `/home/amadeus/.ssh/` : `700` (standard SSH)

### Syncthing
- Le dossier synchronisé est `/srv/aspace/vault/` (pas la racine `/srv/aspace/`)
- Le `.stignore` exclut : `31_Raw_Logs/`, `*.tmp`, `*.lock`, `.git/`, `node_modules/`
- Les dossiers `services/`, `web/`, `backups/` ne sont PAS synchronisés — ils sont locaux au VPS

### Backups
- `aspace-backup.sh` fait un `rsync` snapshot de `/srv/aspace/` vers `backups/`
- Rotation : 7 jours glissants, 4 semaines, 3 mois
- Un `rsync /srv/aspace/` vers un stockage externe = disaster recovery complet

### systemd
- Chaque agent a un fichier `.service` dans `~/setup/systemd/`
- Installé via symlink dans `/etc/systemd/system/`
- Pattern : `ExecStart=`, `Restart=on-failure`, `WorkingDirectory=/srv/aspace/services/<agent>/`
- Le working directory pointe vers `/srv/aspace/services/` — les agents travaillent sur les données serveur, pas dans le home

---

## Ce que cette arborescence garantit

1. **Un seul `rsync` backup tout** — `rsync -a /srv/aspace/ destination/` = Vault + données agents + sites web + backups
2. **Le VPS est reconstructible** — `~/setup/bootstrap.sh` sur un Ubuntu vierge recrée l'intégralité
3. **Séparation config/données** — Le home brûle ? Réinstalle les agents. Le `/srv/` brûle ? Restaure le backup.
4. **Syncthing ne synchronise que le Vault** — les données locales du VPS (services, web, backups) ne polluent pas le triangle P2P
5. **Chaque agent sait où travailler** — OpenClaw scanne `/srv/aspace/vault/20_RUNTIME/21_Inbox/`, pas un chemin arbitraire

---

*Dernière mise à jour : 2026-04-07*
*Mainteneur : 13th Doctor (A2 Kernel) — validé par Rick (A1)*
