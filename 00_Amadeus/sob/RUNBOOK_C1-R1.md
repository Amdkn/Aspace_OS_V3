# Runbook C1-R1 — Instance AaaS déployable en 1 commande (mois 1 : 20/07 → 16/08)
## Objectif (métrique SQL)
`SELECT count(*) FROM subscriptions WHERE status IN ('trial','subscribed')` ≥ 1 avec une instance live.
## Entrées (ce que le B3 reçoit)
Ce runbook seul + accès repo omk-nexus + aspace.db. Rien d'autre (information hiding).
## Sorties (deltas attendus)
1. Script `deploy_instance.py` : 1 commande = 1 instance coach isolée (zéro Docker, config.json + data.db SQLite privée). Testé 2× (idempotence prouvée). [amendé 2026-07-20 §4.2 : design Docker initial remplacé par design léger fichier pour portabilité VPS sans service]
2. 1 instance de démo live, URL fonctionnelle, utilisée dans les démos R2.
3. Chaque déploiement loggé : `INSERT INTO experiments(ts,domain,segment,hypothesis,status)`.
## Procédure
S1 : inventaire de l'existant (omk-nexus repo, landing live) → gap list. S2 : script deploy + instance test.
S3 : durcissement (redéploiement idempotent, backup). S4 : doc 1 page + mémo if-then.
## Cadence
4 sprints × 5 scrums. Scrum = query état → 1 action produit → delta loggé → uplink 1 ligne.
## Notes (cas limites)
Pas de multi-tenant ce cycle (C3). Pas de perfection : l'instance sert la DÉMO, elle s'améliore par contre-exemples clients (E.3).
