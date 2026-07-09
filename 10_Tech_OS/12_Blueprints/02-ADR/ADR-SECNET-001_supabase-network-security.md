# ADR-SECNET-001 — Sécurité Réseau Supabase Self-Hosted + Mesh L2

**Date :** 2026-05-28
**Auteur :** A0 Amadeus + A2 Claude Code
**Statut :** RATIFIÉ (Phase 1 appliquée — iptables allowlist actif)
**Type :** Architecture Decision Record (Tech OS / L0 / Sécurité Réseau)
**Portée :** VPS Hostinger `aspace-vps` (148.230.92.235) — tout port exposé docker+host
**Ancré sur :** ADR-INFRA-001 (Tmux/PM2) · ADR-MESH-L2-001 (mesh tri-plateforme) · ADR-HEART-002 (anti-panique)

---

## Contexte

Le 27 mai 2026, lors du Stage 0 de la session "mesh L2 production-ready", l'inventaire du VPS Hostinger a révélé que **plusieurs ports critiques étaient exposés sur 0.0.0.0** :

| Port | Service | Risque |
|------|---------|--------|
| `5432` | Supavisor pooler (postgres) | Accès BDD complète, brute-force, leak données clients |
| `6543` | Supavisor transaction mode | Idem 5432 |
| `8000` | Kong API gateway (HTTP) | API publique sans auth visible |
| `8001` | Studio (UI admin) | Accès dashboard admin Supabase |
| `8443` | Kong HTTPS | Idem 8000 |
| `9081` | life-web-os-emergency | Service legacy à auditer |
| `3000` | obsidian-web | Edition notes — public |
| `80/443` | Caddy host | Reverse proxy général (OK, fronte les sous-domaines) |
| `22` | SSH | OK (Auth par clé ed25519 + StrictHostKeyChecking) |

Aucun firewall actif (`ufw: command not found`, iptables vide). VPS dans l'état "tout ouvert sauf SSH".

## Décision

### D1 — Architecture défense en profondeur (3 couches)

| Couche | Tool | Rôle |
|---------|------|------|
| **L1 Network filter** | `iptables` (DOCKER-USER chain) | Allowlist IP brute pour ports docker exposés |
| **L2 Reverse proxy + TLS** | `Caddy` (déjà installé host:80,443) | Subdomain routing + cert Let's Encrypt auto + IP allowlist HTTP |
| **L3 App auth** | Supabase JWT + RLS Postgres | Authent + row-level security par tenant |

Chaque couche bloque indépendamment. Compromettre 1 niveau ne donne pas accès à tout.

### D2 — Phase 1 — iptables allowlist (APPLIQUÉE 2026-05-27)

Règles dans la chain `DOCKER-USER` (s'applique aux ports docker-exposed avant docker forwarding) :

```
iptables -I DOCKER-USER 1 -s 174.102.16.12/32 -p tcp -m multiport --dports 5432,6543,8000,8001,8443 -j ACCEPT
iptables -I DOCKER-USER 2 -s 127.0.0.1/32     -p tcp -m multiport --dports 5432,6543,8000,8001,8443 -j ACCEPT
iptables -I DOCKER-USER 3                     -p tcp -m multiport --dports 5432,6543,8000,8001,8443 -j DROP
```

Persistance : `apt install iptables-persistent` + `netfilter-persistent save`. Rules rechargées au boot.

**IPs allowlistées (état initial)** :
- `174.102.16.12` — A0 Windows (sortie publique)
- `127.0.0.1` — localhost (workers PM2 sur VPS, accès docker exec)

**Pour ajouter une IP** (collaborateur futur, autre site, etc.) :
```
sudo iptables -I DOCKER-USER 1 -s <NEW_IP>/32 -p tcp -m multiport --dports 5432,6543,8000,8001,8443 -j ACCEPT
sudo netfilter-persistent save
```

**Pour retirer** : `sudo iptables -D DOCKER-USER -s <IP>/32 ... -j ACCEPT` puis `save`.

### D3 — Phase 2 — Caddy reverse proxy + TLS (À DÉPLOYER)

Caddy déjà installé sur host (`/etc/caddy/Caddyfile`). À étendre pour fronter Supabase Studio + Kong via subdomain :

```
# /etc/caddy/Caddyfile (extension à ajouter)

studio.aspace-vps.example.com {
    @allowlist {
        remote_ip 174.102.16.12 127.0.0.1
    }
    handle @allowlist {
        reverse_proxy 127.0.0.1:8001
    }
    handle {
        respond "Access denied — IP not allowlisted" 403
    }
    log { output file /var/log/caddy/studio.log }
}

api.aspace-vps.example.com {
    @allowlist {
        remote_ip 174.102.16.12 127.0.0.1
    }
    handle @allowlist {
        reverse_proxy 127.0.0.1:8000
    }
    handle {
        respond "Access denied" 403
    }
}
```

**Pré-requis Phase 2** :
1. Domaine acquis pointant vers VPS (ex: `aspace-vps.example.com`)
2. DNS A records `studio.*` `api.*` `*.tenant` → IP VPS
3. Caddy redémarre auto sur changement de Caddyfile (`sudo systemctl reload caddy`)
4. Une fois TLS Let's Encrypt actif, **fermer** iptables aux ports 8000/8001/8443 sauf `127.0.0.1` (puisque Caddy local proxy)

**Note Postgres** : 5432/6543 restent en iptables-only (TCP non-HTTP). Pour accès distant sécurisé : SSH tunnel ou pgbouncer + TLS cert.

### D4 — Phase 3 — Hardening RLS Postgres (par tenant)

Chaque schema `tenant_<slug>` reçoit RLS sur toutes ses tables (cf. ADR-MESH-L2-001 D2) :

```sql
ALTER TABLE tenant_<slug>.<table> ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation ON tenant_<slug>.<table>
  USING (current_setting('app.current_tenant', true) = '<slug>'
         OR current_user = 'postgres');
```

Worker PM2 connecté en `postgres` (superuser) bypasse RLS — pour ops. Connexion utilisateur final passe par `role_<slug>` (cf. supabase-schema-per-project.sql v2) qui respecte RLS.

### D5 — Anti-patterns proscrits

- ❌ Ouvrir un port sur 0.0.0.0 sans vérifier l'iptables DOCKER-USER
- ❌ Stocker un secret en clair dans `ecosystem.config.js` (cf. .env chmod 600)
- ❌ Commit d'un `.env` dans un repo (gitignore obligatoire)
- ❌ Désactiver iptables-persistent (perdrait rules au reboot)
- ❌ Utiliser le user `postgres` superuser dans une app cliente (toujours role-per-tenant)
- ❌ Caddy reverse_proxy sans `@allowlist` matcher (= public)

### D6 — Audit + monitoring

| Quoi | Fréquence | Comment |
|------|-----------|---------|
| Trafic DROP iptables | Hebdo | `sudo iptables -L DOCKER-USER -n -v` (compteurs pkts/bytes) |
| Logs SSH brute-force | Quotidien | `sudo lastb \| head -20` + fail2ban (à installer si attaques) |
| Studio access | Hebdo | `tail /var/log/caddy/studio.log` (après Phase 2) |
| Supabase Postgres connections | Hebdo | `SELECT * FROM pg_stat_activity WHERE datname='postgres';` |
| Workers PM2 panic | Temps réel | `pm2 monit` + Donna DLQ inspection |

### D7 — Plan de rotation secrets

| Secret | Lieu | Rotation |
|--------|------|----------|
| `POSTGRES_PASSWORD` | `/srv/aspace/supabase/docker/.env` + `~/symphony-workers/*/\.env` | Semestre (manuel) |
| `JWT_SECRET` Supabase | Idem | Annuel (manuel — invalide tous les anon/service keys) |
| `NOTION_TOKEN` Internal Integration | `~/symphony-workers/sync-notion-to-supabase/.env` | À chaque revoke Notion UI |
| SSH key `id_sovereign_amadeus` | `~/.ssh/` Windows | À chaque compromis suspect |
| API tokens externes (Stripe, etc.) | Vault à venir (Phase 4) | Selon politique fournisseur |

### D8 — Réponse à incident

1. **Compromis suspect** → exécuter `Test-RunnerHealth -RunnerType Both` + check `pg_stat_activity`
2. **Si confirmé** :
   - Rotation immédiate des secrets impactés
   - `iptables -F DOCKER-USER && netfilter-persistent save` puis re-apply allowlist propre
   - Audit log Donna DLQ
3. **Postmortem** dans ClickUp S4-11 list "Postmortems Deals Perdus" (ou créer "Postmortems Incidents")

## Conséquences

### Positives
- **Surface d'attaque réduite ~95%** : ports stratégiques accessibles uniquement depuis A0 + localhost
- **Données Supabase isolées** : tentatives brute-force depuis l'extérieur droppées au niveau kernel
- **Coût zéro** : iptables natif, Caddy déjà installé, pas de service tiers
- **Évolutif** : ajouter une IP = 1 commande, retirer = 1 commande

### Négatives
- **Manuel pour Phase 2 Caddy** : nécessite domaine + DNS configurés (différé)
- **iptables silencieux** : DROP sans log → ajouter `LOG` rules si suspicion (charge IO)
- **A0 doit IP allowlist depuis chaque réseau** (home, office, mobile hotspot…) — friction
  - Mitigation : VPN/WireGuard installé à terme

### Risques tracés
- **IP A0 dynamique** (FAI résidentiel) : si change, allowlist devient stale. Mitigation : monitoring + auto-update via script depuis Windows (à scripter)
- **Container recreate change IP Docker bridge** : `supabase-db` peut changer d'IP si re-créé. Mitigation : worker PM2 doit utiliser nom DNS docker (à ajouter Phase 2.1)
- **iptables-persistent + custom rules collision** : si quelqu'un édite rules manuellement sans `save`, perdues au reboot. Mitigation : doctrine "toujours `save` après modif"

## Plan d'implémentation

### Phase 1 — iptables allowlist (FAIT 2026-05-27)
- [x] Stop daemons banned (Hermes/OpenClaw)
- [x] Apply 3 rules DOCKER-USER (ACCEPT A0, ACCEPT localhost, DROP rest)
- [x] Install iptables-persistent + netfilter-persistent save
- [x] Verify : counters pkts/bytes augmentent sur DROP rule

### Phase 2 — Caddy reverse proxy + TLS (À FAIRE)
- [ ] Acquérir / configurer subdomain `*.aspace-vps.example.com`
- [ ] Étendre `/etc/caddy/Caddyfile` avec blocks `studio.*` `api.*`
- [ ] `systemctl reload caddy`
- [ ] Test Let's Encrypt cert auto-issuance
- [ ] Une fois OK : restreindre iptables 8000/8001/8443 à localhost seul

### Phase 3 — RLS Postgres (À FAIRE post-Phase 2)
- [ ] Pour chaque table tenant `sops`, `squads`, `symphony_log` : ENABLE RLS + policy
- [ ] Worker PM2 documenté comme bypass via `postgres` superuser
- [ ] Test connexion `role_aspace_solaris` avec RLS appliqué

### Phase 4 — Vault secrets management (À FAIRE Q3 2026)
- [ ] Installer `vault` ou `pass` ou `1password-cli` sur VPS
- [ ] Migrer `.env` files vers vault
- [ ] Workers chargent secrets via vault API au démarrage

## Références

- ADR-MESH-L2-001 — Doctrine mesh L2
- ADR-INFRA-001 — Tmux/PM2 process managers
- ADR-HEART-002 — Anti-panique guards
- ADR-RICK-001 — Donna DLQ
- Caddy docs : https://caddyserver.com/docs/caddyfile/matchers#remote-ip
- iptables DOCKER-USER : https://docs.docker.com/engine/network/packet-filtering-firewalls/
- Supabase RLS : https://supabase.com/docs/guides/auth/row-level-security
