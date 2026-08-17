---
type: Bundle index
title: security — cloisonnements, modèles et failles
description: Modèles de sécurité, vulnérabilités mesurées et frontières d'isolation, avec la portée exacte de chaque mesure.
tags: [okf, security, index]
generated: { by: claude-opus-5, at: 2026-08-17T15:10:00Z }
okf_version: "0.2"
---

Ce sous-bundle porte les **frontières** : qui voit quoi, sur quelle base, et
comment on l'a vérifié.

Une page de sécurité qui ne dit pas ce qu'elle a mesuré ne vaut rien. La
portée — quel projet, quelle table, quel compte, à quelle date — fait partie de
l'affirmation, pas de son contexte.

# Files

- [Une policy RLS sans son GRANT ne s'applique jamais](policy-rls-sans-grant.md) - Postgres vérifie le privilège de table avant la policy. Une policy correcte sans GRANT a toutes les apparences d'une configuration valide et faisait échouer le hook JWT de Coach OS en 500, pour Google comme pour le courriel. Contient la requête de diagnostic et la cascade d'annulation de transaction.
- [Coach OS — un seul vocabulaire de tenant, `org_id uuid`](coach-os-canon-org-id.md) - Deux systèmes d'identifiant coexistaient, slug `text` et `uuid` ; le canon RLS l'emporte. Base et code alignés le 2026-08-17, marques de type pour empêcher la confusion de revenir. Mesure après : 0 colonne `text`, 128 policies, 0 table sans policy.
