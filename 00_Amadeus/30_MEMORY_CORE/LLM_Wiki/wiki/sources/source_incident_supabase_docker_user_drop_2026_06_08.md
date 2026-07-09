---
source: incident
date: 2026-06-08
type: source
domain: L0 Tech_OS / Infra / Supabase / Docker networking
tags: [#incident #supabase #docker #iptables #DOCKER-USER #postgrest #vps #resolved]
related: [ADR-SUPABASE-001, ADR-OMK-001, ADR-META-001]
severity: high
status: RESOLVED
---

# Incident — Supabase PostgREST "Database connection timed out" (DOCKER-USER DROP)

## Symptôme
Après la Phase E (CLI MiniMax) sur le Supabase self-hosted VPS (`aspace-vps`), PostgREST (`supabase-rest`) bouclait sur :
`connection to server at "db" (172.19.0.x), port 5432 failed: Operation timed out`.
`pooler` en Restarting, `auth`/`storage` unhealthy, `kong`/`studio`/`functions` en Created. API REST KO.

## Root cause (confirmée, pas supposée)
La chain iptables **`DOCKER-USER`** contenait une règle de durcissement :
```
-A DOCKER-USER -s 174.102.16.12/32  ... --dports 5432,6543,8000,8001,8443 -j ACCEPT   # IP A0
-A DOCKER-USER -s 127.0.0.1/32      ... --dports 5432,6543,8000,8001,8443 -j ACCEPT   # localhost
-A DOCKER-USER                          --dports 5432,6543,8000,8001,8443 -j DROP      # tout le reste
```
Cette règle (verrouiller les ports Supabase à l'IP A0 + localhost) **droppait aussi le trafic interne container→container** : les conteneurs (172.19.0.x) ne sont ni l'IP A0 ni localhost → leurs connexions vers `db:5432` (et pooler `6543`, kong `8000/8001/8443`) tombaient dans le DROP.

### Pourquoi le diagnostic était trompeur (matrice de preuves)
- `host → db:5432` = OK → trafic host = chain OUTPUT, **pas** FORWARD/DOCKER-USER.
- `db → rest:3000` = OK → port 3000 **absent** de la liste droppée.
- `meta → db:5432`, `rest → db:5432`, `pooler → db:6543` = **DROP** (container→container, FORWARD).
- conntrack 12/262144 (pas plein) ; bridge OK ; db healthy. → ce n'était NI conntrack, NI bridge, NI PostgREST.

Un `docker compose down/up` (tenté) n'a rien changé (la règle DROP est indépendante du réseau) — il a juste confirmé que le redémarrage n'était pas la solution.

## Fix appliqué (chirurgical, réversible, blast radius = supabase ports only)
Autoriser le sous-réseau Docker interne vers ces ports, **avant** le DROP (sécurité externe préservée) :
```
sudo iptables -I DOCKER-USER 1 -s 172.16.0.0/12 -p tcp -m multiport --dports 5432,6543,8000,8001,8443 -j ACCEPT
```
- Live : appliqué → `meta→db OK`, rest a rechargé son schema cache (31 relations), 13/13 conteneurs healthy, `kong/rest` = 401 (attendu, kong→rest OK).
- Persistance : ligne ajoutée dans `/etc/iptables/rules.v4` (ligne 65, avant la règle IP-A0), `iptables-restore --test` = VALID. Backup : `/etc/iptables/rules.v4.bak.20260608-supabase-fix`. netfilter-persistent enabled → survit au reboot.

## Leçon (anti-récurrence)
Toute règle de durcissement `DOCKER-USER` qui DROP un port **doit** d'abord ACCEPT le range Docker interne (`172.16.0.0/12`), sinon elle casse le trafic inter-conteneurs. Si la règle DROP est un jour régénérée par un script de durcissement, ré-ajouter l'ACCEPT interne en tête.

## Reste / non-régression
- `supabase.148.230.92.235.sslip.io` (REST API HTTPS) **n'existe pas** dans Caddy (seul `supabase-studio.148.230.92.235.sslip.io` est routé, cookie-gate). Le `.env.example` OMK qui pointait là était une supposition erronée → corrigé. Pour exposer l'API REST en HTTPS (SaaS), ajouter un bloc Caddy → `kong:8000`.
- Phase E exposure (`PGRST_DB_SCHEMAS=...,solaris_internal,solaris_saas`) reste à ré-appliquer maintenant que la connectivité est rétablie (schémas déjà créés par le CLI).
