# RAPPORT QA C — finance · growth · product · legal · audit

**Testeur :** C
**Date :** 2026-08-06
**Apps du groupe :** finance (7 sections) · growth (7) · product (9) · legal (3) · audit (7)
**Themes testes :** `warm-paper` (clair) et `dark-oled` (sombre)
**Captures :** `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/qa/C/<app>/<theme>/<section>.png`

---

## Defauts trouves

| app | section | theme | gravite | ce qui ne va pas | capture |
|-----|---------|-------|---------|------------------|---------|
| finance | Runway | warm-paper | **visible** | Graphique en barres 100% vide : 12 mois affiches en abscisse, legende "Cash on hand" presente, mais **aucune barre** rendue pour les 12 mois. Donnees dans le code : `[42, 40, 39, 37, 36, 34, 33, 31, 30, 28, 27, 25]`. Container dessine, contenu absent. | `qa/C/finance/warm-paper/runway.png` |
| finance | Runway | dark-oled | **visible** | Meme defaut que warm-paper : 12 barres absentes. Theme en plus incoherent (cf. ligne theme finance ci-dessous). | `qa/C/finance/dark-oled/runway.png` |
| finance | Formes | warm-paper | **mineur** | Le titre de section affiche "**Formesde prix**" sans espace entre "Formes" et "de prix" — bug d'affichage, devrait etre "Formes de prix". | `qa/C/finance/warm-paper/formes.png` |
| finance | Formes | dark-oled | **mineur** | Meme bug "Formesde prix" colle, + canvas qui ne suit pas le theme sombre. | `qa/C/finance/dark-oled/formes.png` |
| finance | (toutes) | dark-oled | **visible** | Le **canvas Finance ne suit pas le theme global** : la barre du haut et le dock de gauche sont bien DARK OLED, mais toute la fenetre Finance (sidebar + contenu) reste sur fond **blanc**. Theme incoherent — l'app fait exception sans raison visible. | `qa/C/finance/dark-oled/overview.png` (et toutes les autres sections finance/dark-oled) |
| finance | Overview | warm-paper | **mineur** | Le sous-titre "Wonder Woman Domain" est tronque en "WONDER WOMAN DOM…" dans la sidebar. Manque ~5 caracteres. | `qa/C/finance/warm-paper/overview.png` |
| growth | (toutes) | dark-oled | **visible** | Le **canvas Growth ne suit pas le theme global** : topbar DARK OLED, mais la fenetre Growth reste sur fond blanc. Meme symptome que Finance, meme defaut. | `qa/C/growth/dark-oled/funnel.png` (et toutes les autres) |
| product | Backlog | warm-paper | **visible** | Le badge du header annonce "**3**" (compteur `byStage('backlog').length`) mais la grille affiche **6 cartes** issues de tous les stages (NOW × 2, NEXT × 2, LATER × 1, BACKLOG × 1). Le filtre "backlog only" documente en commentaire (`emptyMessage="No backlog items yet."`) n'est pas applique — incoherence nombre vs contenu visible. | `qa/C/product/warm-paper/backlog.png` |
| product | Specs | warm-paper | **mineur** | Le badge du header affiche "**8**" mais on ne voit que **6 cartes** dans la fenetre. Meme pattern que Backlog : le compteur et le rendu ne s'accordent pas. | `qa/C/product/warm-paper/specs.png` |
| product | Releases | warm-paper | **mineur** | Trois cartes SHIPPED : titre affiche "**—**" (vide) pour chacune. Aucun sous-titre (date de livraison). Seul "version v0.X" apparait. Cartes tres pauvres en information, alors qu'un seed structurerait sans doute un titre et une date. | `qa/C/product/warm-paper/releases.png` |
| product | (toutes) | dark-oled | **visible** | Le **canvas Product ne suit pas le theme global** : topbar DARK OLED, canvas reste clair. Meme defaut que Finance / Growth. | `qa/C/product/dark-oled/roadmap.png` (et toutes les autres) |
| legal | Compliance | warm-paper | **mineur** | Le bandeau affiche "Deadline 2026-08-02" — 4 jours dans le passe (date du jour : 2026-08-06). Pas de signal visuel "deadline depassee" alors que la regle est cochee partiellement (3/5). | `qa/C/legal/warm-paper/compliance.png` |
| legal | (toutes) | dark-oled | **visible** | Le **canvas Legal ne suit pas le theme global** : topbar DARK OLED, canvas Legal reste clair. Meme defaut systemique que les 3 apps precedentes. | `qa/C/legal/dark-oled/contracts.png` (et toutes les autres) |
| audit | Maturite | warm-paper | **mineur** | Le bloc "03 Deleguer" est coupe en bas de la fenetre visible (1440×900). Pour voir les 3 niveaux (Discuter, Connecter, Deleguer) en entier il faut scroller. Defaut de cadrage a la taille standard. | `qa/C/audit/warm-paper/maturite.png` |
| audit | (sidebar) | warm-paper + dark-oled | **mineur** | Le titre "Manuel de Diagnostic IA" est tronque en "**Manuel de Diagno…**" dans la sidebar, sur les 7 sections (Overview, Maturite, Arbitrage, Contexte, Donnees, Automatabilite, ROI). | `qa/C/audit/warm-paper/overview.png` |
| audit | (toutes) | dark-oled | **visible** | Le **canvas Audit (Glassmorphism interne) ne suit pas le theme global** : topbar DARK OLED, canvas reste en mode Glassmorphism clair (palette lavande/bleu pale). Theme incoherent. Cas legerement different de Finance/Growth/Legal/Product car Audit utilise son propre theme canvasNuance=1, mais l'effet visuel est le meme : topbar sombre ≠ canvas clair. | `qa/C/audit/dark-oled/overview.png` (et toutes les autres) |

---

## Sections capturees et jugees saines

**Finance (warm-paper) :** Overview, Planchers, Courbes, Tokens, Invoices.
**Finance (dark-oled) :** memes 7 sections ont ete capturees mais TOUTES presentent le meme defaut theme (cf. ligne dediee ci-dessus).
**Growth (warm-paper) :** Funnel, Channels, Experiments, Acquisition, Strategie, Partenariats, AEO — toutes OK.
**Growth (dark-oled) :** memes 7 sections capturees mais toutes presentent le defaut theme.
**Product (warm-paper) :** Roadmap, Backlog (defaut compteur), Classement, Lancement, MVP, Ideation, Channels. Specs et Releases ont des defauts mineurs signales.
**Product (dark-oled) :** memes 9 sections, defaut theme generalise.
**Legal (warm-paper) :** Contracts, Compliance (defaut deadline passe), Policies.
**Legal (dark-oled) :** memes 3 sections, defaut theme.
**Audit (warm-paper) :** Overview, Maturite (defaut cadrage), Arbitrage, Contexte, Donnees, Automatabilite, ROI.
**Audit (dark-oled) :** memes 7 sections, defaut theme (legerement attenue par le canvasNuance Glassmorphism).

---

## Ce que je n'ai pas pu tester

1. **Aucun detail de carte.** Les ToolTips m'ont dit "cartes ouvrent un detail", mais je n'ai pas clique sur une carte (risque de faire muter l'app). Les defauts d'ouverture / rendu en overlay sont donc hors perimetre de cette QA.

2. **Aucun test fonctionnel (toggle, drag, search).** Brief demande capture visuelle, pas interaction. Compliance a des toggles, Backlog affiche "drag to Roadmap", Legal a une search box : aucune interaction testee.

3. **Erreurs console :** le script `shot.mjs` n'a remonte **aucune erreur console** sur les 70+ captures effectuees (le rapport "ERREURS CONSOLE" du script est reste vide). Console propre cote navigateur.

4. **Theme "Trust and Authority" / "Vibrant Block" / "Brutalism" / "Glassmorphism"** affiches dans la sidebar des apps sont des libelles de theme par app — comportement attendu, pas un defaut.

5. **Les couleurs semantiques** (rouge, orange, vert, jaune sur badges status) ne suivent pas le theme sombre parce que les apps ne rechargent pas leur canvas en dark — c'est une consequence du defaut theme principal, pas un defaut supplementaire.

6. **Audit app est marque `hidden: true` dans `src/lib/app-discovery.ts`.** Il n'apparait pas dans la sidebar en navigation normale. Il est cependant accessible via `--app audit` dans l'outil, et affiche les 7 sections. Pas teste en navigation naturelle.

---

## Resume

- **1 defaut visible tres fort** : graphique Runway vide (finance), affecte le sens de la section.
- **4 defauts visibles themes** : canvas Finance / Growth / Product / Legal / Audit qui ne suivent pas le theme global `dark-oled`. Meme symptome, meme cause probable (le theme est pose via `localStorage.coach-os-themes-v1.globalTheme` puis recharge, mais l'app canvas ne lit pas ce signal). Systemique, pas isole.
- **3 defauts mineurs** : troncature de titres (Finance "Wonder Woman Domain", Audit "Manuel de Diagnostic IA"), bug "Formesde prix" colle (espace manquant).
- **3 defauts mineurs d'incoherence** : badge compteur Backlog (3 vs 6 cartes), badge Specs (8 vs 6 cartes), titres Releases vides.
- **1 defaut de cadrage** : Audit Maturite coupe au tiers inferieur en 1440×900.
- **1 defaut de signal** : Legal Compliance deadline affichee comme si elle etait a venir alors qu'elle est passee.

Aucun defaut bloquant : toutes les sections sont utilisables.