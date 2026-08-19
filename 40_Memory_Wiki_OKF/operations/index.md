---
type: Bundle index
title: operations — playbooks et gestes de remise en route
description: Sous-bundle en attente de sa première page. Il portera les procédures répétables : redémarrages, migrations, vérifications.
tags: [okf, operations, index]
generated: { by: claude-opus-5, at: 2026-08-17T15:10:00Z }
okf_version: "0.2"
---

Ce sous-bundle porte les **procédures répétables** : redémarrer un service,
appliquer une migration, vérifier qu'un jeton est encore vivant.

Un playbook utile dit aussi **comment on sait que ça a marché**. Une procédure
qui se termine sans critère de succès se rejoue à l'aveugle, et c'est ainsi
qu'un `exit 0` trompeur passe pour une réussite.

# Files

- [NotebookLM en assistance de revue humaine](notebooklm-revue-humaine.md) - Quand la production n'est plus le goulot : 423 fichiers produits en une nuit, aucun relu. Regroupement en 26 sources chargeables, et la règle qui ne se délègue pas — rien ne passe de `machine` à `humain` sans le propriétaire du produit.
- [Une 404 de Vercel n'est pas une 404 de l'app](vercel-repli-spa-404.md) - Sans règle de repli dans `vercel.json`, tout chemin profond d'une SPA rend le 404 de la plateforme avant que le code ne s'exécute. C'est ce qui bloquait la connexion Google de Coach OS, après que le `redirect_uri_mismatch` de Google eut été corrigé. Contient le geste de vérification à trois chemins.
