---
type: Playbook
title: Une 404 de Vercel n'est pas une 404 de l'app
description: Sans règle de repli dans vercel.json, tout chemin profond d'une SPA rend le 404 de la plateforme avant que le code ne s'exécute — ce qui a bloqué la connexion Google de Coach OS.
tags: [vercel, spa, oauth, routage, coach-os, 404]
generated: { by: claude-opus-5, at: 2026-08-17T16:20:00Z }
verified:
  - { by: process:curl-prod, at: 2026-08-17T16:18:00Z }
sources:
  - id: mesure-avant
    resource: "curl sur omk-desktop-web-os.vercel.app — /, /auth/callback, /api/agent/roster, avant correctif"
    author: process:curl-prod
    last_modified: 2026-08-17
  - id: mesure-apres
    resource: "mêmes trois chemins après déploiement du correctif"
    author: process:curl-prod
    last_modified: 2026-08-17
  - id: correctif
    resource: "coach-os — vercel.json + src/lib/vercel-spa-fallback.test.ts"
    title: Règle de repli et son verrou
    last_modified: 2026-08-17
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Les deux mesures sont des
> appels HTTP réels sur l'URL de production, avant et après.

# Le symptôme

La connexion Google de Coach OS échouait sur une page `404: NOT_FOUND` portant
un identifiant `cle1::…`.

Cet identifiant est la signature de Vercel. **La 404 venait de la plateforme,
pas de l'application** — la requête n'a jamais atteint le code.

# La mesure

| Chemin | Avant | Après |
|---|---|---|
| `/` | 200 | 200 |
| `/api/agent/roster` | 200 `application/json` | 200 `application/json` |
| `/auth/callback` | **404** | 200 `text/html` |

# La cause

`vercel.json` déclarait `buildCommand` et `outputDirectory`, mais **aucune
règle `rewrites`**. Sur une SPA construite en fichiers statiques, Vercel cherche
un fichier réel pour chaque chemin : il trouve `dist/index.html` pour `/`, ne
trouve rien pour `/auth/callback`, et rend son propre 404.

```json
"rewrites": [
  { "source": "/((?!api/).*)", "destination": "/index.html" }
]
```

L'exclusion de `/api` est nécessaire : sans elle, les fonctions serverless
rendraient du HTML au lieu de leur JSON.

# Pourquoi c'était difficile à voir

**Rien n'était cassé côté applicatif.** Le composant `OAuthCallback.tsx`
existait, `App.tsx` l'aiguillait sur le bon chemin, et son commentaire d'en-tête
décrivait même le symptôme mot pour mot — sans que personne fasse le lien.

Surtout : la page d'accueil répondait 200, et les fonctions `/api/*` aussi.
Seuls les **chemins profonds** tombaient. Or le seul chemin profond du produit
est justement le retour OAuth. Le défaut était donc invisible partout sauf à
l'endroit exact où il coûtait une connexion.

# Le piège de diagnostic, plus large

La panne a longtemps été attribuée à Google — un `redirect_uri_mismatch`, qui
était réel et a été corrigé côté Google Cloud Console. Une fois corrigé,
l'écran de consentement Google s'affichait normalement… et l'échec persistait,
un cran plus loin dans la chaîne.

**Deux défauts en série sur un même parcours se ressemblent de l'extérieur.**
Corriger le premier ne fait pas disparaître le symptôme, ce qui donne
l'impression que le correctif n'a pas marché. Ce qui tranche est la capture :
l'écran Google affichait bien `ndvqwcapwcnpdvknxcjw.supabase.co`, donc le
premier maillon fonctionnait, et le suivant était en cause.

# Le verrou

`src/lib/vercel-spa-fallback.test.ts` verrouille quatre propriétés : une règle
existe, elle couvre `/auth/callback`, elle couvre `/`, elle ne capture pas
`/api/*`.

Vérifié par falsification — 3 échecs sur 4 quand on retire la règle, 4
réussites quand elle est là. **Ce test lit une configuration, pas une réponse
HTTP** : il empêche une régression d'écriture, pas une régression de
plateforme. La vérification qui tranche reste un `curl` sur la production.

# Le geste, pour toute SPA sur Vercel

Après chaque déploiement, mesurer **trois** chemins et pas un seul :

```bash
for p in / /une/route/profonde /api/une-fonction; do printf "%-24s " "$p"; curl -s -o /dev/null -w "%{http_code} %{content_type}\n" "https://<domaine>$p"; done
```

Tester uniquement `/` laisse passer exactement ce défaut-là.
