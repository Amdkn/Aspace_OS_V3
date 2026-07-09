# Shadow L0 — Tmux (WSL Dev) + PM2 (VPS Prod) : Persistance Opérationnelle

**Date :** 2026-05-26
**Niveau :** L0 Tech OS
**Source doctrinale :** `12_Blueprints/02-ADR/ADR-INFRA-001_tmux-wsl-dev-pm2-vps-prod.md`

## Insight A0 acté

Après l'expérience des paniques agentiques (effondrement Hermes/OpenClaw/Paperclip d'avril 2026), A0 a identifié la **bonne couche** : les process managers standards éprouvés industriellement.

- **Tmux** (2007, Unix std) pour le dev persistant dans WSL
- **PM2** (2013, Node std) pour la prod durable sur VPS

Ce ne sont **pas** des daemons custom (bannis par SPEC.md) — ce sont des binaires upstream avec >10 ans de production scale-up sans panique structurelle équivalente.

## Décisions clés (7)

1. D1 — Séparation stricte : Tmux=dev (WSL), PM2=prod (VPS). Aucune exception.
2. D2 — Layout Tmux canonique "aspace" : 4 windows (heartbeat, logs, agents-interactive, scratch). Bootstrap via `aspace-tmux-session.sh`.
3. D3 — Template `ecosystem.config.js` PM2 par projet (max_restarts:5, max_memory_restart, autorestart).
4. D4 — 5/8 paniques SDD-001 structurellement mitigées par cette couche.
5. D5 — Doctrine d'allocation : Yaz Watchdog reste Task Scheduler Windows (léger), services lourds (Symphony sync, Stripe listeners) sous PM2 VPS, exploration A0 sous Tmux dev.
6. D6 — Migration choisie : **coexistence**. Pas de bascule brutale. Re-évaluation 30j.
7. D7 — Amende SPEC.md : "no custom daemons" (pas "no daemons"). Tmux + PM2 explicitement autorisés.

## Mapping anti-panique

| Panique | Mitigation |
|---------|------------|
| Type 1 Approval Freeze | Tmux detach (pas de timeout) |
| Type 2 Budget Hard-Stop | PM2 max_restarts:5 + max_memory_restart |
| Type 4 WS Timeout | PM2 health-check + restart auto |
| K3 Secret Leak 401 | PM2 no-autorestart sur 401 + webhook alert |
| K4 Dead Kernel | Tmux survit SSH disconnect · PM2 startup survit reboot |

## Plan implémentation (3 phases)

| Phase | Durée | Status |
|-------|-------|--------|
| 1. Bootstrap Tmux dev (WSL + apt install + aspace-tmux-session.sh) | 30 min | À FAIRE |
| 2. Bootstrap PM2 VPS (npm i -g pm2 + pm2 startup + template) | 1h | À FAIRE (au 1er service prod) |
| 3. Cheatsheets A0 (Tmux + PM2 dans Ryan_SysAdmin/CHEATSHEETS/) | 30 min | À FAIRE |

## Conséquences pour le mesh

- Symphony bus (ADR-SYMPH-001) reste pattern files+Task Scheduler côté Yaz, mais les **services lourds** (Phase 2 Notion→Supabase sync) tourneront sous PM2 sur VPS.
- ADR-HEART-002 mode `lean` inchangé (OpenClaw/Paperclip restent désactivés — Tmux/PM2 résolvent les besoins sans eux).
- Capsules CLI (Codex/Gemini/Claude Code) peuvent enfin avoir un mode "always-on" via Tmux panes dédiées.

## SPEC.md à amender

Action requise (différée — pas dans cet ADR pour respecter immutabilité ADRs existants) : éditer `Shadow_L0/SPEC.md` §1 point 1 pour préciser "no custom daemons" au lieu de "no daemons", avec référence à ADR-INFRA-001.

## Références

- ADR-INFRA-001 (canon)
- SDD-001 (anchor paniques)
- ADR-HEART-002 (couche complémentaire)
- ADR-SYMPH-001 (compatible)
