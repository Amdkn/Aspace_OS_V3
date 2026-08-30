# RAPPORT QA D — groupe `marketplace` / `onboarding` / `ontology` / `cognition`

**Date** : 2026-08-06
**Périmètre** : 4 apps, 18 captures (sections × 2 thèmes globaux).
**Thèmes testés** : `warm-paper` (clair), `dark-oled` (sombre).
**Cible** : repérer les défauts visuels, pas les corriger.

---

## 1. Défauts trouvés — triés du plus grave au plus bénin

| # | app | section | thème | gravité | ce qui ne va pas | capture |
|---|-----|---------|-------|---------|------------------|---------|
| D-01 | cognition | (toutes) | warm-paper | bloquant | L'app `cognition` a été supprimée de la barre latérale (Phase 39b). Sa logique vit désormais dans une section `Cognition` de Sales Sanctum (hors groupe). Quand on ouvre `cognition`, le shell affiche « 🚧 cognition — This app is not registered. ». La barre latérale de l'app ne contient aucune section à capturer. | `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/qa/D/cognition-warm-paper.png` |
| D-02 | cognition | (toutes) | dark-oled | bloquant | Même fenêtre « not registered », mais en plus le titre `cognition` et la phrase `This app is not registered.` sont rendus en `text-stone-400/700` (couleurs fixes Tailwind, non reliées au thème) sur fond sombre — quasi illisibles. | `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/qa/D/cognition-dark-oled.png` |
| D-03 | onboarding | citadel (étape 1 du quiz) | dark-oled | visible | Sous thème sombre global, le panneau gauche du citadel (titre `STEP 1 OF 4 · CAPTURE`, question `Where do your client session notes live today?`, sous-titre `One answer — closest to reality.`, options radio, lien `← Back`, barres de progression Q1/Q2/Q3/Q4) est rendu en teal sombre sur fond quasi noir — contraste trop faible pour être lu confortablement. Le panneau droit (`YOUR FUTURE DEMO INSTANCE` + 4 tuiles IP Vault / Mini-apps Library / QuizResult / Compliance) est dans le même état : titre presque invisible, libellés des tuiles à peine lisibles. | `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/qa/D/onboarding-dark-oled-default.png` |
| D-04 | ontology | Entities | dark-oled | visible | Sous thème sombre, le titre `Entites metier`, le sous-titre `Les 12 types du registre…`, l'interrupteur `Organisation seule / Tout`, et la plupart des textes des cartes d'entités (descriptions `Localiser racine…`, `Lien entre un Profil…`) sont en teal sombre sur fond noir — lecture très pénible. Seuls les badges `personnel` (jaune) et les compteurs `N attr.` (teal clair) restent lisibles. | `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/qa/D/ontology-dark-oled-entities.png` |
| D-05 | ontology | Relations | dark-oled | visible | Titre `Relations`, sous-titre `Verbes typés entre entites…`, libellés des listes déroulantes `Source` / `Cible`, bouton `Réinitialiser` et compteur `20 relations` sont rendus en couleurs sombres quasi invisibles sur fond noir. Les relations elles-mêmes (Organization -[has]-> Membership, etc.) restent lisibles parce qu'elles utilisent des variables de thème plus claires. | `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/qa/D/ontology-dark-oled-relations.png` |
| D-06 | ontology | Contracts | dark-oled | visible | Titre `Contrats semantiques` et sous-titre `Declencheurs et actions permises par entite.` quasi invisibles (teal sur noir). Les noms d'entités et leurs descriptions dans les cartes (`Persona morale ou…`, `Prestation catalogue…`, etc.) sont également très peu contrastés. | `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/qa/D/ontology-dark-oled-contracts.png` |
| D-07 | ontology | Versions | dark-oled | visible | Titre `Etat du registre` et sous-titre quasi invisibles. Les blocs `ETAT DU REGISTRE` et `Pas d'historique de versions` ont leur titre et corps de texte en couleurs sombres — lecture pénible. Seuls les compteurs `12 / 20 / 12` (en teal accentué) et la coche verte restent lisibles. | `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/qa/D/ontology-dark-oled-versions.png` |
| D-08 | (macro) | barre latérale (icône `Onboarding (demo)`) | warm-paper, dark-oled | mineur | Le libellé `Onboarding (demo)` de l'icône dans la barre latérale macro se casse sur deux lignes (`Onboarding` puis `(demo)`) tandis que les 7 autres libellés (`Dashboard`, `People / Agents`, `Operations`, `IT / R&D`, `Clients`, `Tasks`, `Marketplace`) tiennent sur une seule. Troncature/wrap incohérent entre items d'un même menu. | `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/qa/D/onboarding-warm-paper-default.png` (et toutes les autres captures, car la barre latérale est partagée) |

---

## 2. Sections capturées et jugées saines

Pour qu'on sache ce qui a été vu et pas seulement ce qui a échoué :

### marketplace
- `Browse` — warm-paper : grille 2×3 de cartes (Stripe Billing, Calendly Sync, LinkedIn Reach, Notion Export, DocuSign, Loom Recaps) avec états `Installed` (vert) et bouton `Install` (rose). Rendu cohérent.
- `Browse` — dark-oled : marketplace applique son thème canonique `glassmorphism` (cartes `bg-white` hardcodées, ligne 71 de `MarketplaceApp.tsx`), donc l'intérieur reste clair même quand le thème global est sombre. **Comportement constant entre les deux thèmes pour cette app** — à signaler comme une décision produit, pas un défaut.
- `Installed` — warm-paper, dark-oled : 2 cartes (Stripe Billing, Calendly Sync) avec badge vert `Installed`. OK.
- `Featured` — warm-paper, dark-oled : 3 cartes (Calendly Sync, LinkedIn Reach, Loom Recaps) avec badge rose `Featured`. OK.

### onboarding
- Vue par défaut (citadel quiz, étape 1/4) — warm-paper : citadel lisible, topbar `demo-coach · your Nexus preview`, dock 6 icônes (Q, V, L, D, shield, file), wallpaper `MiniWallpaper` (collines vert tendre) bien rendu. OK.

### ontology
- `Entities` — warm-paper : grille 3×2 de cartes d'entités (Organization, Membership, Profile, Client, Offering, SOP), interrupteur `Organisation seule / Tout`, badges `personnel` sur les entités concernées. OK.
- `Relations` — warm-paper : 2 listes déroulantes + bouton reset, 7 relations visibles (Organization -[has]-> {Membership, Client, Offering, SOP, Runbook, Agent, Routine}) avec cardinalité `1-n` et ID `org-has-*`. OK.
- `Contracts` — warm-paper : grille 3×4 de cartes d'entités (Organization, Membership, Profile, Client, Offering, SOP, Runbook, Skill, Agent, Routine, Incident, Persona) avec icône teal. OK.
- `Versions` — warm-paper : 3 StatCard (Entites 12, Relations 20, Contrats 12), bloc `ETAT DU REGISTRE` avec coche verte indiquant que les invariants sont respectés, encart `Pas d'historique de versions`. OK.

### cognition
- *Aucune section saine à reporter — l'app n'est plus dans la barre latérale.* Voir D-01 / D-02.

---

## 3. Ce que je n'ai pas pu tester, et pourquoi

### 3.1 — `cognition` : app supprimée de la barre latérale
Le brief m'a affecté 4 apps : `marketplace`, `onboarding`, `ontology`, `cognition`. Or la 4ᵉ n'existe plus comme entrée de `registerApp()` (cf. commentaire en tête de `src/apps/cognition/CognitionApp.tsx` : « CognitionApp (the standalone AppFrame wrapper) was deleted in Phase 39b. Cognition now lives ONLY as `<CognitionOverviewContent>` dwelled inside the Sales Sanctum app. The standalone `registerApp()` entry was removed from `src/lib/app-discovery.ts.` »).

**Pour tester les 4 sections `Cognition` (Knowledge sovereignty + Stat cards + Schema metadata + Routines), il faudrait ouvrir `sales` puis naviguer sur sa section `Cognition`** — mais `sales` est dans un autre groupe QA. Le brief interdit explicitement de toucher aux apps hors groupe : « Tu ne touches a aucune app hors de ton groupe. ». J'ai donc reporté D-01 / D-02 sur la base des seules captures de l'état « app non enregistrée ».

### 3.2 — `onboarding` : pas de barre latérale « standard »
`OnboardingApp` n'utilise pas `AppFrame` ; il rend `MiniDesktopShell` (citadel + dock + 4 panneaux + audit). Il n'y a donc pas de sections de sidebar au sens `AppSection[]` du brief. J'ai capturé l'état par défaut (citadel quiz étape 1). Je n'ai **pas** capturé :
- les états `reveal` du citadel (après réponse au quiz complet)
- chacun des 5 panneaux ouverts (IP Vault, Mini-apps Library, QuizResult, Compliance, Audit Simulation) — `tools/shot.mjs` n'a pas de moyen de cliquer une icône du dock ; il faudrait injecter du JS via `page.evaluate` pour `openApp('ip-vault', …)`, ce que le script ne fait pas et que je n'ai pas voulu improviser (mes consignes : pas de script custom qui toucherait à la pipeline de capture).

Si tu veux que je passe cette deuxième vague, il faut soit enrichir `tools/shot.mjs` d'un mode `--app <app> --open <window-id>` (clic interne sur le `MiniDock`), soit autoriser un script auxiliaire dans mon dossier de sortie.

### 3.3 — `marketplace` : `--section "Browse"` non capturable proprement
Le sélecteur `[data-section="Browse"], button:has-text("Browse")` du script `tools/shot.mjs` attrape d'abord le bouton **désactivé** du fil d'Ariane (`MARKETPLACE > BROWSE`, ligne 38 de `Breadcrumbs.tsx`) au lieu du bouton actif de la sidebar de l'app. Le script se plante alors sur « element is not enabled ». J'ai contourné en capturant `Browse` sans `--section` (état par défaut de l'`AppFrame`, qui démarre sur la première section = `Browse`). Pour `Installed` et `Featured`, le sélecteur fonctionne car le breadcrumb n'affiche pas leur libellé. **À signaler comme défaut du script de capture**, pas comme défaut visuel d'une app.

### 3.4 — Thèmes par-app : `marketplace` et `onboarding` ignorent le thème global
`CANONICAL_APP_THEMES` (`src/lib/themes/tokens.ts:251-271`) fixe :
- `marketplace → glassmorphism` (cartes translucides, light-mode par défaut)
- `onboarding → liquid-glass` (idem, light-mode)
- `ontology` → pas d'entrée (tombe sur le thème global)
- `cognition → editorial` (canon mais app supprimée, voir D-01)

Conséquence : poser `--theme dark-oled` sur ces apps ne change presque rien à leur intérieur — le chrome de l'app (sidebar, topbar de la fenêtre) reste clair. C'est par conception du mapping canonique, pas un défaut visuel isolé. Mais ça veut dire que mon test « dark-oled » pour `marketplace` et `onboarding` ne représente pas vraiment un stress-test en thème sombre — c'est juste l'app dans son thème canonique. **À garder en tête pour la suite** : pour stress-tester `marketplace`/`onboarding` en sombre, il faudrait soit surcharger le thème par-app via le panneau Settings > Themes, soit changer le mapping canonique.

### 3.5 — Pas d'erreurs de console détectées
Le script `tools/shot.mjs` loggue `ERREURS CONSOLE (N)` si la page émet des erreurs pendant la capture. Sur les 18 runs, **aucune** n'a imprimé ce bandeau. Les pages hurlent en silence, pas en console. (Cela dit : aucune interaction utilisateur n'a été simulée — l'app reste en mode lecture. Une navigation au clic pourrait en révéler ; le script ne les simule pas.)

---

## Annexe — inventaire des captures

Toutes les captures sont dans `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/qa/D/` :

```
marketplace-warm-paper-browse.png       marketplace-dark-oled-browse.png
marketplace-warm-paper-installed.png     marketplace-dark-oled-installed.png
marketplace-warm-paper-featured.png      marketplace-dark-oled-featured.png
onboarding-warm-paper-default.png       onboarding-dark-oled-default.png
ontology-warm-paper-entities.png        ontology-dark-oled-entities.png
ontology-warm-paper-relations.png       ontology-dark-oled-relations.png
ontology-warm-paper-contracts.png       ontology-dark-oled-contracts.png
ontology-warm-paper-versions.png        ontology-dark-oled-versions.png
cognition-warm-paper.png                cognition-dark-oled.png
```

Soit 18 fichiers PNG.