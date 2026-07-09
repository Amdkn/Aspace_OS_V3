# ADR-INFRA-001 — Tmux (WSL Dev) + PM2 (VPS Prod) : Base de Persistance Opérationnelle

**Date :** 2026-05-26
**Auteur :** A0 Amadeus + A2 Claude Code
**Statut :** RATIFIÉ
**Type :** Architecture Decision Record (Tech OS / L0 / Infra)
**Portée :** Tout service ou agent devant survivre à un disconnect, reboot, ou crash
**Ancré sur :** SDD-001 §1.2 (taxonomie paniques) + §2.1 Axiome 2 (Dégradation Gracieuse) · ADR-HEART-002 (anti-panique tick) · ADR-SYMPH-001 (bus orchestration)
**Amende :** `Shadow_L0/SPEC.md` §1 point 1 — la formule *"no daemons"* est précisée : interdiction = composants daemon **custom Windows-natif**, autorisation = process managers **standards éprouvés** Tmux (WSL) + PM2 (VPS Linux)

---

## Contexte

L'effondrement Hermes d'avril 2026 (cf. SDD-001 §1.1) a démontré que les composants custom de gestion de process (Hermes, OpenClaw gateway, Paperclip Node process) sont **fragiles par construction** sur Windows natif. SPEC.md a réagi en bannissant tous les daemons.

A0 a depuis identifié (2026-05-26) la **bonne couche** : utiliser les **process managers standards éprouvés industriellement** :

- **Tmux** (Terminal Multiplexer, 2007) — standard Unix, dans tous les serveurs Linux. Pour le **développement** dans WSL.
- **PM2** (Process Manager 2, 2013) — standard Node.js, utilisé par Netflix/IBM/millions de devs. Pour la **production** sur VPS Linux.

Ces deux outils ne sont **pas** des daemons custom — ce sont des binaires upstream avec >10 ans de production scale-up et aucune classe de panique documentée comparable aux composants interdits.

## Décision

### D1 — Séparation stricte dev / prod

| Contexte | Plateforme | Process Manager | Rôle |
|----------|-----------|-----------------|------|
| **Dev local** | WSL2 Ubuntu (sur Windows A0) | Tmux | Sessions persistantes attachables/détachables pour les agents CLI et scripts en cours |
| **Prod** | VPS Hostinger Ubuntu 24.04 | PM2 | Services Node.js/Python long-running (sync Notion↔Supabase, Stripe listeners, etc.) |

**Règle d'or** : aucun service qui doit survivre à une fermeture de terminal ne tourne hors Tmux (dev) ou PM2 (prod). Pas d'exception.

### D2 — Stack Dev : WSL + Tmux

#### Layout canonique session Tmux "aspace"

```
tmux new-session -s aspace
  ├── Window 0 "heartbeat"
  │     ├── pane 0.0 : heartbeat-tick.ps1 Codex_CLI (loop 15min)
  │     ├── pane 0.1 : heartbeat-tick.ps1 Gemini_CLI
  │     └── pane 0.2 : heartbeat-tick.ps1 Claude_Code_CLI
  ├── Window 1 "logs"
  │     ├── pane 1.0 : tail -F LLM_Wiki/wiki/log.md
  │     └── pane 1.1 : tail -F Shadow_L0/watchdog.log
  ├── Window 2 "agents-interactive"
  │     ├── pane 2.0 : Claude Code interactive session
  │     └── pane 2.1 : Codex CLI interactive session
  └── Window 3 "scratch"
        └── pane 3.0 : bash libre pour A0
```

Bootstrap via `aspace-tmux-session.sh` à créer dans `10_Tech_OS/11_Infra_13th_Doctor/02_Ryan_SysAdmin/`. Idempotent (vérifie session existante, attach si déjà créée).

Detach : `Ctrl+B d`. Reattach : `tmux attach -t aspace`.

### D3 — Stack Prod : VPS + PM2

#### Fichier canonique `ecosystem.config.js` par projet

Chaque projet déployé sur le VPS contient un `ecosystem.config.js` au format PM2 :

```javascript
module.exports = {
  apps: [
    {
      name: 'symphony-sync-notion-supabase',
      script: './src/sync.js',
      instances: 1,
      autorestart: true,
      max_restarts: 5,
      min_uptime: '60s',
      max_memory_restart: '500M',
      restart_delay: 5000,
      env: { NODE_ENV: 'production' },
      error_file: '/var/log/pm2/symphony-sync-err.log',
      out_file: '/var/log/pm2/symphony-sync-out.log',
      time: true
    }
  ]
};
```

Lifecycle commands canoniques (documentées dans chaque README projet) :

```bash
pm2 start ecosystem.config.js          # démarre les apps
pm2 save                                # persiste la liste pour reboot
pm2 startup                             # active auto-start au boot VPS
pm2 status                              # liste l'état
pm2 logs <name>                         # tail logs
pm2 restart <name>                      # restart manuel
pm2 monit                               # monitoring temps réel
```

### D4 — Mapping anti-panique SDD-001

| Panique SDD-001 | Mitigation Tmux/PM2 |
|-----------------|---------------------|
| TYPE 1 — Approval Freeze | Tmux `detach` permet quitter sans tuer la session — pas de timeout |
| TYPE 2 — Budget Hard-Stop | PM2 `max_memory_restart` + `max_restarts: 5` empêche les boucles infinies |
| TYPE 3 — DM Pairing Block | N/A (concerne OpenClaw qui reste désactivé en mode `lean`) |
| TYPE 4 — WebSocket Timeout | PM2 health-check via `pm2-health` plugin (optionnel) + restart auto |
| TYPE K1 — Filesystem Blindness | Inchangé (couvert par `Write-AndVerify` de HEART-002) |
| TYPE K2 — Hallucination Succès | Inchangé (couvert par RAW de HEART-002) |
| TYPE K3 — Secret Leak 401 | PM2 `--no-autorestart` sur exit code 401 + alerting webhook |
| TYPE K4 — Dead Kernel | Tmux survit aux SSH disconnects · PM2 `pm2 startup` survit aux reboots VPS |

→ **5 paniques sur 8** sont mitigées structurellement par cette couche. Les 3 autres (K1, K2, et TYPE 3 si jamais activé) restent gouvernées par ADR-HEART-002.

### D5 — Doctrine d'allocation (qui tourne où)

| Service | Runner | Rationale |
|---------|--------|-----------|
| `heartbeat-tick.ps1` capsules CLI | Tmux pane (dev) | Sessions interactives + visibilité humaine |
| Yaz Watchdog (5min sweep) | Windows Task Scheduler (inchangé) | Reste léger, Windows-natif, déjà fonctionnel |
| `symphony-sync-notion-supabase` | PM2 (VPS) | Doit survivre H24/365 indépendamment du PC A0 |
| Stripe webhook listener | PM2 (VPS) | Webhook = doit toujours répondre |
| Airtable sync workers | PM2 (VPS) | Long-running, prod-grade |
| Dokploy-managed client apps | Dokploy (qui utilise PM2 sous le capot) | Multi-tenant client deployments |
| Symphony dev exploration | Tmux pane (dev) | Itération rapide A0 |

### D6 — Coexistence avec Windows Task Scheduler (décision par défaut)

Migration choisie : **coexistence**. Heartbeat-tick.ps1 reste sur Task Scheduler Windows pour Yaz Watchdog + ticks légers. Tmux/PM2 prennent les services lourds (Symphony sync, listeners webhooks).

**Pourquoi pas migration totale** : Task Scheduler Windows fonctionne. Yaz Watchdog n'a pas besoin de Linux. La migration brutale créerait du risque sans bénéfice immédiat. À ré-évaluer dans 30 jours via un ADR-INFRA-002 si pertinent.

### D7 — Amende SPEC.md

`Shadow_L0/SPEC.md` §1 point 1 dit actuellement :

> *"Run on Windows without daemons — no Hermes service, no OpenClaw gateway, no Paperclip Node process. Past attempts created fragile WSL/systemd dependencies that broke on reboot."*

Lecture **amendée** par cet ADR :

> *"Run on Windows without **custom** daemons — no Hermes service, no OpenClaw gateway, no Paperclip Node process. Past attempts at custom daemons created fragile dependencies that broke on reboot. **Tmux (WSL dev) and PM2 (VPS prod) are explicitly authorized** as industry-standard process managers (20+ and 12+ years respectively) with no panic class equivalent to the banned custom components. Their use is governed by ADR-INFRA-001."*

## Conséquences

### Positives
- **Persistance dev** acquise : A0 peut fermer son PC, le rouvrir 3 jours plus tard, `tmux attach -t aspace` et tout est là.
- **Durabilité prod** acquise : VPS reboot → services redémarrent seuls via `pm2 startup` + `pm2 save`.
- **5/8 paniques SDD-001** mitigées structurellement sans code custom.
- **Standard industrie** : zéro innovation risquée, adoption d'outils battle-tested.
- **Dokploy** (utilisé pour les client deployments Nexus) repose lui-même sur PM2 — alignement naturel.

### Négatives
- Apprentissage A0 : commandes Tmux (Ctrl+B + lettre) + commandes PM2. **Antidote** : cheatsheet dans `Ryan_SysAdmin/CHEATSHEETS/` à créer.
- Dépendance WSL pour le dev — si A0 veut un jour migrer sur Mac/Linux natif, le layout Tmux reste portable, PM2 aussi.
- 2 process managers à monitorer (Tmux + PM2) au lieu d'un. **Antidote** : Yaz Watchdog peut sweep les deux dans son tick 5min.

### Risques tracés
- PM2 sur VPS peut se corrompre si OOM kill. Mitigation : `max_memory_restart` + monitoring Hostinger.
- Tmux session "aspace" peut accumuler des panes morts. Mitigation : Yaz Watchdog inclut une vérif `tmux ls` et alert si > 20 panes.

## Plan d'implémentation

### Phase 1 — Bootstrap Tmux dev (~30 min)
- [ ] Vérifier WSL2 Ubuntu installé
- [ ] `apt install tmux`
- [ ] Créer `10_Tech_OS/11_Infra_13th_Doctor/02_Ryan_SysAdmin/aspace-tmux-session.sh` (idempotent)
- [ ] Premier lancement : `bash aspace-tmux-session.sh` → vérifier les 4 windows
- [ ] Documenter cheatsheet Tmux pour A0 (Ctrl+B navigation)

### Phase 2 — Bootstrap PM2 VPS (~1h, premier déploiement)
- [ ] SSH VPS → `npm install -g pm2`
- [ ] `pm2 startup` (génère commande systemd)
- [ ] Créer template `ecosystem.config.js` canonique dans `10_Tech_OS/11_Infra_13th_Doctor/02_Ryan_SysAdmin/templates/`
- [ ] Premier service déployé : `symphony-sync-notion-supabase` (quand Phase 2 NOTION débloquée)
- [ ] `pm2 save` après stabilisation

### Phase 3 — Documentation A0 (~30 min)
- [ ] Cheatsheet Tmux 1 page
- [ ] Cheatsheet PM2 1 page
- [ ] Schéma d'allocation services (D5) maintenu à jour

## Références

- Tmux : https://github.com/tmux/tmux (créé 2007)
- PM2 : https://pm2.keymetrics.io (créé 2013)
- SDD-001 §1.2 — taxonomie 4+4 paniques
- ADR-HEART-002 — couche tick anti-panique (complémentaire)
- ADR-SYMPH-001 — bus orchestration (compatible avec Tmux/PM2 runners)
- `Shadow_L0/SPEC.md` §1 — amendé par cet ADR
