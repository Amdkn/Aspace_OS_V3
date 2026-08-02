# Paperclip — installation et garde-fous (L2)

**Statut au 2026-08-02 :** binaire installé et vérifié. Serveur **non
démarré** dans cette passe (décision de l'opérateur). Aucune boucle
autonome activée.

## Binaire

| | |
|---|---|
| Version | `paperclipai@2026.722.0` |
| Provenance | npm (`paperclipai` sur le registre officiel) |
| Install | `npm install -g paperclipai` — 330 paquets, peer deps `zod` warning (non fatal) |
| PATH | `/c/Users/amado/AppData/Roaming/npm/paperclipai` |
| `which paperclipai` | OK |
| `paperclipai --version` | `2026.722.0` |

## Instance existante

Une instance configurée existait avant la passe :

| | |
|---|---|
| `~/.paperclip/instances/default/config.json` | `local_trusted`, port 3100, postgres embarqué 54329 |
| `~/.paperclip/instances/default/.env` | `PAPERCLIP_AGENT_JWT_SECRET=…` (secret, hors V3) |
| `~/.paperclip/instances/default/db/` | Postgres embarqué (PG_VERSION, etc.) |
| `~/.paperclip/instances/default/secrets/master.key` | Présent (encryption locale) |
| `~/.paperclip/instances/default/skills/<uuid>/` | 1 skill installée |
| `~/.paperclip/instances/default/logs/server.log` | Présent |
| `~/.paperclip/instances/default.bak-2026-08-02/` | **Sauvegarde** faite avant install |

L'install npm n'a **pas** touché `~/.paperclip/instances/default/`. La
sauvegarde `default.bak-2026-08-02` est intacte et constitue le filet de
sécurité en cas d'erreur de configuration future.

## Les cinq garde-fous

| # | Garde-fou | Commande | Configuré ? | Vérifié ? |
|---|---|---|---|---|
| 1 | Plafond de dépense (par exécution + cumulé) | `paperclipai budget policy:upsert --payload-json ...` et `budget agent:update --payload-json ...` | non | non — nécessite serveur démarré |
| 2 | Garde-fous d'action (approbation humaine) | `paperclipai approval {list,get,create,approve,reject}` | non | non |
| 3 | Bypass de permissions et son périmètre | `paperclipai agent permissions:update <id> --payload-json ...` | non | non |
| 4 | Comportement en cas d'échec répété — doit finir chez Donna | `paperclipai run cancel <runId>`, `run watchdog-decision <runId>` | non | non — le branchement vers `dlq.py` de V3 n'est pas câblé |
| 5 | Autres réglages de sécurité (telemetry, secrets, storage) | `config.json` (serveur), `PAPERCLIP_TELEMETRY_DISABLED=1` | partiel — `telemetry.enabled: true` (par défaut) ; `secrets.provider: local_encrypted` ; `storage.provider: local_disk` | partiel — visible en `config.json`, non modifié |

**Aucun agent n'a été embauché.** L'instance n'a pas de `companies` /
`agents` actifs au démarrage. Sans agent hired, aucune boucle ne tourne,
et le budget cumulé est de 0 par construction.

## Ce que je n'ai pas fait

- `paperclipai run` (démarrage du serveur). Pas de boucle = pas de démarrage.
- `paperclipai agent hire` (embauche d'un agent). Pas de boucle = pas
  d'embauche.
- Configuration effective des budgets par agent. Fait uniquement le
  constat que les commandes existent et que les payloads sont du JSON.

## Pour activer

L'opérateur qui veut démarrer doit, dans cet ordre :

1. `paperclipai run` (démarre serveur + UI sur http://127.0.0.1:3100)
2. Créer une company, embaucher les 3 agents L2 de `ORG.json` (doctor_12,
   bill, nardole, missy) avec budget = 0 par défaut.
3. Câbler `paperclipai run cancel` (échec répété) vers `dlq.py` (V3) — pas
   documenté, à scripter.
4. Activer `PAPERCLIP_TELEMETRY_DISABLED=1` dans `.env` (privacy).
5. Confirmer que `telemetry.enabled: false` en `config.json` aussi.

Tant que les 5 garde-fous ne sont pas **vérifiés sur instance active**,
**aucune boucle n'est lancée**.
