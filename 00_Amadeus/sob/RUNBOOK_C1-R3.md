# Runbook C1-R3 — Onboarding + facturation récurrente automatiques (mois 3 : 14/09 → 11/10)
## Objectif (métrique SQL)
`SELECT SUM(mrr) FROM subscriptions WHERE status='subscribed'` ≥ 10000 ET zéro intervention manuelle d'onboarding sur le dernier client signé.
## Entrées
Ce runbook + aspace.db + les clients R2 + l'instance R1.
## Sorties
1. Flow onboarding : signature → instance provisionnée → accès livré, sans étape manuelle.
2. Facturation récurrente live (Stripe ou équivalent) → chaque paiement = `INSERT INTO ledger(revenue)`.
3. 1er client onboardé par le flow automatique (receipt : timestamps du flow dans experiments).
## Procédure
S1 : cartographier l'onboarding manuel des 3 clients R2 (le SOP émerge du réel, pas l'inverse). S2 : automatiser les étapes répétées 2×+. S3 : brancher facturation. S4 : test bout-en-bout + mémo.
## Notes
E-Myth : on n'automatise QUE ce qui a été fait manuellement au moins 2 fois. Un churn ce mois = contre-exemple E.3 prioritaire → issues + amendement de ce runbook.
