# FIX-5 — La coquille et l'instrument de mesure

Lis d'abord `COMMUN.md`, dans ce même dossier. Il fait partie de ce brief.

Ton rapport : `correctifs/RAPPORT_FIX_5.md`

**Tu passes en premier, seul sur l'arbre.** Les quatre autres correctifs attendent que tu
aies fini, parce qu'ils ont besoin de ton point 1. Sois rapide et net.

---

## 1 · L'outil de capture vise le mauvais bouton — priorité absolue

Les quatre testeurs QA ont buté sur la même chose, chacun de son côté.

`tools/shot.mjs` sélectionne une section avec
`[data-section="X"], button:has-text("X")`. Deux échecs distincts :

- **`data-section` n'est jamais posé.** L'attribut n'existe sur aucun bouton de section dans
  `AppFrame.tsx`. La première branche du sélecteur ne matche donc jamais rien.
- **Le repli textuel attrape le fil d'Ariane.** `Breadcrumbs.tsx` rend le segment actif avec
  `disabled`. Playwright le trouve en premier et échoue sur *element is not enabled*. Pire,
  sur `dashboard --section "Agents"`, il a cliqué le bouton `People / Agents` du rail du
  bureau : la capture montrait la section `Overview` en croyant montrer `Agents`.

Ce dernier point est le plus coûteux : **l'instrument a accusé la mauvaise app.** Une capture
qui montre autre chose que ce qu'elle prétend montrer invalide silencieusement toute une
campagne de QA.

Ce que je te demande :

- Pose un `data-section="<label>"` sur les boutons de section de la barre latérale dans
  `AppFrame.tsx`, et **seulement** sur eux — ni sur le fil d'Ariane, ni sur le rail du bureau.
- Restreins le sélecteur de `shot.mjs` à `[data-section="X"]`, sans repli textuel. Si la
  section n'est pas trouvée, **le script doit échouer bruyamment**, pas capturer autre chose.
  Une capture muette qui montre la mauvaise page est pire qu'une erreur.
- Vérifie sur les trois cas qui ont échoué : `dashboard --section "Agents"`,
  `sales --section "Today"`, `marketplace --section "Browse"`. Les trois doivent produire la
  bonne section, et le fil d'Ariane de la capture doit le confirmer.

## 2 · Les libellés tronqués dans les barres latérales

`AppFrame.tsx` pose `truncate` aux lignes 219, 225, 273, 276 et 319. Conséquences relevées
par la QA :

- `audit` : `Manuel de Diagnostic IA` → `Manuel de Diagno…`, sur les sept sections.
- `finance` : `Wonder Woman Domain` → `WONDER WOMAN DOM…`, cinq caractères manquants.

Le titre d'app dans sa barre latérale doit tenir. Deux lignes valent mieux qu'une amputation.

**Ne touche pas à `src/apps/_ui/FleetItemCard.tsx`** : les troncatures de cartes appartiennent
à FIX-1, qui travaille dessus.

## 3 · `Onboarding (demo)` se casse en deux lignes

Dans la barre latérale du bureau, ce libellé passe sur deux lignes (`Onboarding` puis
`(demo)`) alors que les sept autres (`Dashboard`, `People / Agents`, `Operations`, `IT / R&D`,
`Clients`, `Tasks`, `Marketplace`) tiennent sur une. Incohérence visuelle dans un même menu.

Raccourcir le libellé est sans doute plus sain que d'élargir le rail pour un seul item.

## 4 · L'app `cognition` affiche un écran d'erreur

Ouvrir `cognition` donne : *« 🚧 cognition — This app is not registered. »*

C'est exact et c'est voulu : `CognitionApp` a été supprimée en Phase 39b, sa logique vit
désormais dans la section `Cognition` de Sales. Mais deux choses ne vont pas.

**a.** L'écran est rendu avec des couleurs Tailwind figées — `Desktop.tsx:157` porte
`text-stone-400`, et le titre `text-stone-700`. Sous un thème sombre, c'est illisible :
un message d'erreur qu'on ne peut pas lire. Branche ces couleurs sur les variables de thème.

**b.** L'app reste atteignable alors qu'elle n'existe plus. Soit tu retires son entrée de
`CANONICAL_APP_THEMES` et de tout ce qui la rend ouvrable, soit — mieux — ouvrir `cognition`
redirige vers `sales`, section `Cognition`. Choisis, applique, justifie en une phrase dans ton
rapport.

Si tu retires l'entrée `'cognition'` de `CANONICAL_APP_THEMES`, c'est la **seule** modification
autorisée à cette table, et elle doit être mentionnée explicitement dans ton rapport.

## Ton périmètre exclusif

```
tools/shot.mjs
src/components/**
src/lib/app-discovery.ts
src/lib/themes/tokens.ts     (uniquement pour retirer l'entrée 'cognition', si tu choisis a)
```

Rien dans `src/apps/`.

## Preuve attendue

Dans `correctifs/preuves/fix5/` :

- les trois captures des sections qui échouaient, fil d'Ariane lisible et conforme ;
- une capture de la sortie du script quand on lui demande une section inexistante — l'échec
  doit être explicite ;
- barre latérale d'`audit` et de `finance`, titre entier ;
- le rail du bureau, `Onboarding (demo)` sur une ligne ;
- l'écran `cognition`, lisible sous `dark-oled`, ou la redirection vers Sales si tu as choisi
  cette voie.

Et lance `npx vitest run` : la suite était à 60/60 avant toi, elle doit y rester.
