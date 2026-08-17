---
type: Reference
title: Les SaaS refusent l'embarquement en iframe — mesure du 2026-08-17
description: Sept cibles sur huit renvoient X-Frame-Options ou frame-ancestors restrictif ; aucun outil de travail visé ne s'affiche dans un iframe tiers.
tags: [iframe, x-frame-options, csp, coach-os, app-store]
generated: { by: claude-opus-5, at: 2026-08-17T13:45:00Z }
verified:
  - { by: process:curl-head, at: 2026-08-17T13:30:00Z }
sources:
  - id: mesure-directe
    resource: "curl -I -L sur 8 domaines — en-tetes X-Frame-Options et Content-Security-Policy"
    author: process:curl-head
    last_modified: 2026-08-17
  - id: rapport-m3
    resource: _briefs/2026-08-17_APPS_IFRAME/RAPPORT_ARCHITECTURE.md
    title: Rapport d'architecture (32 Ko, agent MiniMax-M3)
    last_modified: 2026-08-17
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Chaque ligne vient d'un
> appel HTTP réel, recoupé indépendamment du rapport qui l'a produit.

# Le tableau

| Cible | En-tête | Embarquable par un tiers ? |
|---|---|---|
| `macro.com` | `X-Frame-Options: DENY` | ❌ le plus strict — aucun site, jamais |
| Notion | `SAMEORIGIN` + `frame-ancestors 'self' app.notion.com …` | ❌ |
| Airtable | `X-Frame-Options: SAMEORIGIN` | ❌ |
| Figma | `X-Frame-Options: SAMEORIGIN` | ❌ |
| Google Docs | `SAMEORIGIN` + `frame-ancestors 'self'` | ❌ |
| ClickUp | `frame-ancestors 'self' clickup.com` | ❌ |
| Linear | `frame-ancestors 'self' cms.linear.app` | ❌ |
| `threejs.org` | aucun en-tête restrictif | ✅ |

**Sept sur huit refusent.**

# Ce que ça implique

Le niveau « Easy » de l'App Store de Coach OS embarque une **URL externe dans
un iframe**. Il ne peut donc fonctionner que sur de la documentation ou de la
démonstration — **aucun des outils de travail visés par les clients** ne
s'affichera.

Ce n'est pas une limite de Coach OS. C'est la politique de ces éditeurs, et
elle est unanime. **Aucun correctif côté client n'existe** : ni proxy, ni
sandbox, ni attribut d'iframe. Le navigateur refuse le rendu avant de charger.

# Le piège de diagnostic

Un embarquement refusé ne produit **aucune erreur exploitable** : pas de code
HTTP, pas de message console, juste un cadre vide ou un texte du navigateur.
Une app peut donc paraître cassée alors que rien ne l'est — et l'inverse.

Cas vécu le même jour : `Tearable UI` portait `?q=tearable` dans son URL.
Aucun exemple threejs ne s'appelle ainsi ; le filtre vidait la galerie et
l'app semblait morte alors qu'elle chargeait parfaitement.

**Toujours vérifier l'en-tête avant de conclure**, et prévenir l'utilisateur
*avant* qu'il publie une app qui ne s'affichera jamais.

# Le chaînon manquant, plus grave que l'iframe

Les AppSpec produites par le SaaS Builder pointent vers
`https://placeholder.invalid/<slug>.html`. `.invalid` est un TLD réservé
(RFC 2606) qui **ne résout jamais**.

Le SaaS Builder produit une **spécification**. Rien ne construit ni n'héberge
le HTML. **Aucune question de partage multi-tenant n'a de sens tant que ce
trou reste ouvert.**
