---
type: Backend
title: Bloquer une app par son registre, pas par ses boutons d'entrée
description: Remplacer le composant dans le manifeste ferme toutes les portes d'un coup, retire la sidebar au passage, et sort le code du bundle livré.
tags: [coach-os, architecture, registre, feature-flag, bundle]
generated: { by: claude-opus-5, at: 2026-08-17T19:10:00Z }
verified:
  - { by: process:curl-bundle-prod, at: 2026-08-17T19:05:00Z }
sources:
  - id: mesure-bundle
    resource: "grep sur assets/index-B4Z47MoY.js servi par omk-desktop-web-os.vercel.app — présence/absence des libellés propres à chaque app"
    author: process:curl-bundle-prod
    last_modified: 2026-08-17
  - id: mise-en-oeuvre
    resource: "coach-os — src/lib/app-discovery.tsx, src/apps/en-construction/"
    title: Le blocage et son verrou
    last_modified: 2026-08-17
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** L'effet a été mesuré sur le
> bundle réellement servi en production, pas sur le code source.

# La décision

Pour rendre une app indisponible, **remplacer son `component` dans le manifeste
du registre** — pas masquer son icône, pas ajouter une garde dans l'app.

```ts
registerApp({ id: 'app-store', name: 'App Store', /* … */
  component: creerPageEnConstruction({ nom: 'App Store', raison: '…' }) });
```

# Pourquoi le registre et pas les boutons

Le registre est **le seul point de passage**. Une app s'ouvre depuis l'icône du
bureau, le dock, le menu Apps, ou un `openApp()` appelé par une autre app.

Masquer un bouton d'entrée ne ferme qu'une porte sur plusieurs — et la porte
oubliée est toujours celle qu'on ne connaissait pas. Ici, `SaaS Builder`
appelait `App Store` par `openApp` pour publier : une garde posée sur l'icône
aurait laissé ce chemin ouvert.

# Trois effets, dont deux qu'on n'a pas eu à programmer

**1. La sidebar disparaît d'elle-même.** Dans Coach OS, la colonne « Sections »
est rendue **à l'intérieur** de chaque app, pas par la coquille de fenêtre.
Remplacer le composant la retire donc sans traitement séparé. C'était la
demande explicite — « personne ne doit même accéder aux sidebar » — et elle
n'a coûté aucune ligne.

**2. Le code sort du bundle.** L'app n'étant plus importée, le *tree-shaking*
l'élimine. Mesure sur le bundle de production après déploiement :

| Libellé propre à l'app | Dans le bundle |
|---|---|
| `URL externe dans un iframe`, `Programmes installes` | **absent** |
| `Liste des engines`, `ALL-TIME SPEND`, `Publish to App Store` | **absent** |
| `est en construction` | présent |
| `App Store`, `SaaS Builder` (noms d'app) | présents — les icônes restent |

Ce n'est pas un masquage : **l'interface n'est plus livrée au navigateur**. Un
utilisateur curieux ne peut pas la rejoindre, parce qu'elle n'y est pas.

**3. Rouvrir tient en deux lignes** : l'import, et le composant sur la ligne
`registerApp`. Les fichiers source ne sont pas touchés.

# Le verrou, et ce qu'il doit vraiment mesurer

Un test qui cherche seulement le titre « en construction » passerait au vert sur
une page posée **par-dessus** une sidebar encore cliquable. Le verrou vérifie
donc l'inverse : que l'app **ne rend plus sa propre interface** — ni intitulé
« Sections », ni `<aside>`.

Il porte aussi une **app témoin** qui doit continuer de s'ouvrir. Sans elle, un
verrou qui casserait tout le registre serait vert.

Vérifié par falsification : 2 échecs sur 6 quand on rebranche le vrai
composant.

# Anti-piège de vérification

Le bureau n'ouvre pas ses fenêtres sur des événements souris synthétiques
(`dispatchEvent`). Plusieurs tentatives de clic scripté ont échoué **sans rien
casser** — et un verdict « la page ne s'affiche pas » en aurait été tiré à
tort.

**Quand l'interaction scriptée résiste, mesurer l'artefact plutôt que le
geste.** Ici, `grep` sur le bundle servi tranche mieux qu'un clic : il dit ce
qui est livré, indépendamment de la façon dont on y accède.

# Quand cette décision ne s'applique pas

Si l'app doit disparaître complètement du bureau, c'est `hidden: true` sur le
manifeste, pas une page de construction. Les deux ne disent pas la même chose à
l'utilisateur : la page annonce un chantier, l'absence n'annonce rien.
