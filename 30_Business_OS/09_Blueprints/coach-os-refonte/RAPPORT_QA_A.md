# RAPPORT_QA_A — Dashboard · Sales · Welcome · Settings · Design

Testeur : session isolée, lecture seule. Outil : `node tools/shot.mjs` (Playwright + chromium, viewport 1440×900, devicePixelRatio 2). 132 captures sur 132 attendues (5 apps × 22 + 14 + 10 + 7 + 21 sections, deux thèmes globaux — `warm-paper` et `dark-oled`). Toutes stockées dans `qa/A/` et copiées dans le présent dossier.

Périmètre : `dashboard`, `sales`, `welcome`, `settings`, `design`. Le reste (people, operations, it-rd, clients, tasks, marketplace, product, growth, finance, legal, ontology, audit, onboarding) n'a pas été ouvert.

---

## Défauts trouvés — tableau trié du plus grave au plus bénin

`gravite` :
- `bloquant` : on ne peut pas s'en servir
- `visible` : ça se voit et ça décrédibilise
- `mineur` : à corriger un jour

| # | app | section | theme | gravite | ce qui ne va pas | capture |
|---|-----|---------|-------|---------|-----------------|---------|
| 1 | dashboard | Integrations | dark-oled | **visible** | Les 6 cartes ont TOUTES leur nom tronqué à 1-2 lettres + `…` (`M…`, `S…`, `G…`, `V…`, `G…`, `S…`) et toutes les descriptions coupées net (`Passerelle unique des outils MCP d…`, `Données tenant, authentification …`, `Dépôts, issues et changelogs du…`, `Déploiements et journaux de…`, `Documents partagés du…`, `Canal d'équipe non autorisé sur…`). Le contenu textuel est rendu inutilisable par la troncature. | `qa/A/dash_Integrations_do.png` |
| 2 | dashboard | Integrations | warm-paper | **visible** | Même troncature que ci-dessus (1-2 lettres + `…` par carte). Reproduit sur l'autre thème → c'est la grille, pas le thème. | `qa/A/dash_Integrations_wp.png` |
| 3 | dashboard | Wind Direction | dark-oled | **visible** | Titre « Wind Direction » et sous-titre « Things requiring your validation » quasi invisibles sur fond sombre. Contraste texte insuffisant. Les 3 cartes ont leur titre tronqué `Validation devi…`, `Retard livrais…`, `Mise à jour Stri…`. | `qa/A/dash_Wind_Direction_do.png` |
| 4 | dashboard | Wind Direction | warm-paper | **visible** | Titre et sous-titre quasi invisibles sur le fond crème chaud (même symptôme, autre thème). Cartes tronquées. | `qa/A/dash_Wind_Direction_wp.png` |
| 5 | dashboard | Client Pipeline | dark-oled | **visible** | Titre « Client ledger » et sous-titre quasi invisibles. Sous-titres des 6 cartes tronqués : `Citadelle — high tic…`, `Programme — 12 w…`, `Atelier Bric…`, etc. | `qa/A/dash_Client_Pipeline_do.png` |
| 6 | dashboard | Client Pipeline | warm-paper | **visible** | Même faible contraste des titres et même troncature des sous-titres. | `qa/A/dash_Client_Pipeline_wp.png` |
| 7 | dashboard | CEO Cockpit | dark-oled | **visible** | Titre « CEO Cockpit » et son sous-titre « Interconnected view across core business domains… » quasi illisibles sur le fond sombre (gris foncé sur fond noir). | `qa/A/dash_CEO_Cockpit_do.png` |
| 8 | dashboard | Sessions | dark-oled | **mineur** | Le tableau déborde à droite : la dernière colonne (un `D…` tronqué) est coupée par le bord droit de la zone de contenu. Pas de scroll horizontal visible. | `qa/A/dash_Sessions_do.png` |
| 9 | dashboard | Kill Switches | dark-oled | **mineur** | La 3ᵉ carte `COST CONTROLS` est tronquée : `cost cap per s…` (il manque `session` ou équivalent). | `qa/A/dash_Kill_Switches_do.png` |
| 10 | dashboard | Usage | dark-oled | **mineur** | La carte `TRAJECTOIRE` (bandeau du bas) est coupée à droite — le titre du graphique, `Dépense horaire · 12 h glissantes`, est visible mais le picto/légende à droite `MIX…` est tronqué hors fenêtre. | `qa/A/dash_Usage_do.png` |
| 11 | dashboard | Knowledge | dark-oled | **mineur** | Le panneau étroit `QUESTION AU DOCUMENT` à droite fait wrapper le titre du document sur 3 lignes (`Playbook / — / première séance`) au lieu d'une seule. Le texte de la question est aussi tronqué : `Quel est le point essen… / retenir pour la prochai… / séance ?` | `qa/A/dash_Knowledge_do.png` |
| 12 | sales | Context | dark-oled | **visible** | Le titre `Sales OS Control Center` wrappe sur 2 lignes (`Sales OS Control / Center`) à cause du meta de droite plus large (`Source · The single-source brief · 7 living documents`). Dans les autres sections de Sales (`Today`, `Pipeline`, `Stack`, `Capabilities`), le titre tient sur 1 ligne. | `qa/A/sales_Context_do.png` |
| 13 | sales | Cognition | dark-oled | **visible** | Même wrap du titre que `Context`. | `qa/A/sales_Cognition_do.png` |
| 14 | welcome | OMK RH, OMK Operations, OMK Growth, OMK Cognition, OMK People | dark-oled | **visible** | Le bandeau `PAGES` du canvas (juste sous le breadcrumb) ne montre que **5 onglets sur 9**. Finance / IT / Legal / Coach Demo sont inaccessibles depuis ce bandeau — pas d'indicateur de scroll horizontal, le bandeau est coupé sec. Pour naviguer vers ces 4 pages, l'utilisateur est obligé de passer par la sidebar. | `qa/A/welcome_OMK_RH_do.png`, `qa/A/welcome_OMK_Operations_do.png`, `qa/A/welcome_OMK_Legal_do.png` |
| 15 | welcome | OMK Coach Demo | dark-oled | **visible** | Surbrillance incohérente : la section active dans la sidebar est `OMK Coach Demo` mais le bandeau `PAGES` du canvas surligne en cyan `OMK RH`. Mauvais marqueur de page active. | `qa/A/welcome_OMK_Coach_Demo_do.png` |
| 16 | settings | Canvas FX | dark-oled | **mineur** | Les tuiles d'effet sont trop étroites : les noms à 8 caractères sont tous tronqués à 6, perdant 1-2 lettres (`BUBBL`, `FORCEF`, `DECRYP`, `DISPLA`, `DROPLE`, `FLAMEW`, `HEXFLO`, `MAGNIF`, `PARTIC`, `PARTIC`). Les `…` de fin manquent, on dirait des noms raccourcis à la main. | `qa/A/settings_Canvas_FX_do.png` |

---

## Sections capturées et jugées saines

### Dashboard (warm-paper + dark-oled) — 22 sections
- Overview (KPIs du jour, TLDR), Chat, Playground, Jarvis, Sessions, Usage, Cost, Audit Log, Security Posture, DLP & Exfil, Rate Limits, Panic, Compliance, Kill Switches (cartes 1 et 2), Memories, Members — pas de défaut visible au viewport.
- Le fond d'écran (wallpaper `paper-garden`) reste visible derrière la fenêtre du Dashboard dans les deux thèmes.

### Sales (warm-paper + dark-oled) — 6 sections
- Today, Pipeline, Capabilities, Stack, Cognition (hormis le wrap du titre noté en #13). Les onglets-puces `Today / Pipeline / Context / Capabilities / Stack` fonctionnent comme attendu visuellement.

### Welcome (warm-paper + dark-oled) — 10 sections
- Arrivée (hero magnétique), OMK RH, OMK Operations, OMK Growth, OMK Cognition, OMK People, OMK Finance, OMK IT, OMK Legal, OMK Coach Demo — toutes rendent leur hero dédié et leurs sous-sections.
- Le contenu Welcome applique le thème global (override GlobalThemedCanvas) — le hero d'Arrivée est noir sur dark-oled, crème sur warm-paper, comme attendu.

### Settings (warm-paper + dark-oled) — 7 sections
- General, Themes, Wallpaper, Privacy, Integrations, Help — propres.
- `Themes` montre les 12 aperçus dans une grille 4 colonnes (les 8 premiers visibles au viewport, les 4 autres sont en dessous).

### Design (warm-paper + dark-oled) — 21 sections
- Overview (roster 9 cartes), Glass, Clay, Brutalism, Cyberpunk, Soft UI, Editorial, Y2K, Memphis, Vapor, Bauhaus, Art Deco, Bento, Retro 57, Aurora, Terminal, Wabi-sabi, GenZ, Drawn, Neo-brutal, Liquid — toutes les showcases rendent leur identité visuelle. Defauts de troncature minimes sur Overview (palette de certaines cartes qui wrappe sur 2 lignes) et sur Brutalism (stat `[STAT_02]` `256k JS BUNDLE,` coupé au bord droit).

---

## Ce que je n'ai pas pu tester, et pourquoi

1. **Dashboard · Agents** — la capture `dash_Agents_*.png` montre en réalité la section `Overview` (breadcrumb `DASHBOARD > OVERVIEW`). Le sélecteur `--section "Agents"` de `tools/shot.mjs` tape le bouton `People / Agents` du rail gauche du desktop (parce que l'attribut `data-section` n'est jamais posé sur les boutons de section dans `AppFrame.tsx`, et le sélecteur de repli `button:has-text("Agents")` matche le premier bouton contenant « Agents », qui est dans le rail). Donc la section `Agents` interne n'a pas été capturée. Aucun défaut visible côté dashboard — défaut côté outil, mentionné ici pour qu'on sache.
2. **Sales · Today** — même problème de collision de sélecteur (et en plus timeout Playwright). `sales_Today_*.png` a été capturée en relançant le script sans `--section` (la section par défaut de Sales étant `Today`, ça a fonctionné). Donc `Today` a bien été capturée par chance, mais je n'ai pas pu confirmer via le sélecteur normalisé.
3. **Aucun drill-down / page de détail** ouvert : je n'ai cliqué sur aucun item d'aucune section. Je n'ai donc pas testé `DashboardItemDetail`, `SalesDetailPage`, `SettingsItemDetail`, `ThemeDetailPage`, les agents overlay, les skills/routines en drill, etc. Hors-périmètre mais à signaler.
4. **Le tour RGPD Privacy** aurait dû se déclencher automatiquement à l'ouverture de `Settings > Privacy` (cf. `settings_Privacy_do.png`). Je n'ai pas pu vérifier visuellement s'il apparaît (la capture montre déjà le contenu Privacy, sans tooltips visibles).
5. **Aucun drag, hover, focus clavier, screen-reader, mobile / viewport réduit, ni interaction avec les toggles / dropdowns / sliders**. Le brief demandait des captures, pas des interactions.
6. **Aucun test de performance** (rendu, scroll, lazy-load). Hors-périmètre.
7. **Aucun test de contraste texte par formule WCAG**. J'ai regardé à l'œil ; pour qu'un testeur de contraste puisse valider formellement, il faudrait extraire les paires foreground/background depuis le DOM, pas juste l'œil sur PNG.

---

## Bilan de santé global

- 132 captures propres, aucun crash, aucune erreur de console remontée par le script (le script logge les erreurs de console rencontrées pendant la navigation ; `tools/shot.mjs` ne rapporte `ERREURS CONSOLE (N)` que si `N > 0`).
- 16 défauts trouvés, dont **2 majeurs** (troncature Integrations sur les deux thèmes, contraste des titres Wind Direction / Client Pipeline / CEO Cockpit) et **5 visibles** restants. Les 9 autres sont des débordements partiels ou des wraps contextuels.
- Les thèmes `warm-paper` et `dark-oled` ne produisent pas toujours les mêmes défauts visuels : la troncature Integrations est présente sur les deux, mais le wrap de titre Sales et le bandeau PAGES de Welcome sont des défauts structurels qui n'ont pas de dépendance au thème.
- Aucun défaut bloquant (`bloquant`) au sens strict : tout reste utilisable, mais la troncature Integrations rend la grille illisible.