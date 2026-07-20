# Runbook C1-R2 — Pipeline : 100 coachs contactés, 10 démos, 3 signés (mois 2 : 17/08 → 13/09)
## Objectif (métrique SQL)
`SELECT count(*) FROM subscriptions WHERE mrr>=1000 AND status='subscribed'` ≥ 3.
Intermédiaires : pipeline ≥100 contacted · ≥10 demo · outreach_log ≥100 lignes direction='out'.
## Entrées
Ce runbook + aspace.db + ICP : coachs premium B2B ($7.5K-25K programmes, facturation 500-2000€/h). Offre : 1000$/mois, l'usine de contenu+conformité+prospection clé en main.
## Sorties
1. 100 lignes `pipeline` (prospects nommés, réels, trouvés — LinkedIn/annuaires/podcasts).
2. 100 messages sortants loggés `outreach_log` (personnalisés : 1 détail spécifique du prospect chacun).
3. 10 démos bookées (l'instance R1). 3 signés à 1000$/mois → `subscriptions` + `ledger(revenue)`.
## Procédure
S1 : constituer la liste 100 (recherche réelle, pas de noms inventés — un prospect sans URL vérifiable n'entre pas en base). S2 : vague outreach 1-50 + relances. S3 : vague 51-100 + démos. S4 : closing + mémo.
## Cadence
Chaque scrum : 5-10 prospects recherchés OU 10-15 messages OU 1 démo préparée/débriefée. Delta SQL obligatoire.
## Notes
Réponses humaines = asynchrones : le Run produit le sortant, le Run suivant ramasse l'entrant (§2 START_HERE). 10 conversations découverte/mois SANS vente (source='research') pour C6.
