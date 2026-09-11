---
type: Concept
title: Architecture Agent OS V3 — Template Reproductible de Web Desktop (Standard Business OS)
description: Spécification canonique de la montée en gamme d'Agent OS en V3 alignée sur les standards de conception Business OS (Amdkn/BusinessOS), transformant le bureau en un template reproductible ultra-avancé sans régression sur V1 et V2.
tags: [agent-os, v3, business-os, template-engine, web-desktop, tiling, command-palette, blueprints]
generated: { by: gemini-2.5-pro, at: 2026-09-07T20:45:00Z }
verified:
  - { by: human:amdkn, at: 2026-09-07T20:45:00Z }
sources:
  - id: business-os-repo
    resource: "Amdkn/BusinessOS — https://github.com/Amdkn/BusinessOS"
    author: Amadou Kone
  - id: business-os-agents-dox
    resource: "c:/Users/amado/ASpace_OS_V3/30_Business_OS/AGENTS.md"
    author: Amadou Kone
  - id: directive-agent-os-v3
    resource: "Directive Amadou Kone — Plan d'amélioration Agent OS en V3 par une refonte de mise à niveau au Standard de conception de Business OS en Template reproductible de Web Desktop le plus avancé sans rien casser de la V1 et V2 déjà construites"
    author: human:amdkn
    last_modified: 2026-09-07
okf_version: "0.2"
---

# Architecture Agent OS V3 : Template Reproductible de Web Desktop

## 1. Contexte & Alignement Stratégique

L'architecture d'**Agent OS V3** concrétise la fusion entre la souplesse du Web Desktop souverain et la rigueur industrielle du standard de conception **Business OS** (https://github.com/Amdkn/BusinessOS).

### Invariants Inviolables
1. **Loi L0 d'Auto-Réplication (Rick)** : Le bureau Web n'est pas un ensemble statique de fenêtres codées en dur, mais un **Template reproductible** capable d'être cloné, configuré et instancié instantanément pour n'importe quel tenant, franchise ou domaine (Tech L0, Life L1, Business L2, Client externe).
2. **Garantie Zéro Régression sur V1 & V2** :
   - Le moteur de fenêtrage flottant, dock et catalogue d'applications natives de la **V1** demeurent 100% opérationnels.
   - Le CMS sémantique à 7 niveaux, le deep linking bidirectionnel (payload.targetTab) et les passerelles inverses 'CMS' de la **V2** sont intégralement préservés et servent de couche de données universelle.
3. **Zéro Dette Technique** : Pas de mocks incomplets, pas de placeholders, typage strict TypeScript validé par compilation tsc --noEmit.

---

## 2. Les 5 Piliers Architecturaux de la V3

### Pilier 1 : Moteur de Fenêtrage Hybride (Tiling & Aero Snap)
- **Aero Snap Dynamique** : Glisser une fenêtre vers le bord gauche ou droit déclenche un ancrage à 50% de largeur d'écran ; glisser vers les 4 coins la positionne dans le quadrant correspondant (25%) ; glisser vers le haut la maximise.
- **Visual Ghost Preview** : Détection en temps réel de la zone d'ancrage avec prévisualisation en surbrillance acrylique semi-transparente.
- **Picture-in-Picture (PiP / Always-on-Top)** : Épinglage au premier plan pour les fenêtres de télémétrie critique ou d'agents actifs.

### Pilier 2 : Command Palette Universelle (Ctrl+K / Cmd+K)
- **Moteur Spotlight Global** : Indexation instantanée des 7 niveaux du CMS V2.
- **Recherche & Navigation Instantanée** : Permet de basculer vers n'importe quel onglet de n'importe quelle application en 2 frappes.
- **Exécution Directe d'Actions N6** : Lancement d'actions système (rechargement de baux, export de snapshot, bascule de workspace) directement depuis la barre de commande.

### Pilier 3 : Multi-Workspaces & Espaces Virtuels
- **Isolation Tri-OS** : Espaces de travail par défaut configurés pour Tech OS (L0), Life OS (L1) et Business OS (L2).
- **Workspaces Sur-Mesure** : Création d'espaces personnalisés pour des clients ou projets spécifiques.
- **Indépendance d'État** : Chaque espace retient ses propres fenêtres ouvertes, positions et géométries sans interférence.

### Pilier 4 : Business OS Template Engine & Widget SDK Reproductible
- **Spécification Déclarative d'Apps (AppBlueprint)** :
  Permet de générer une application complète en décrivant simplement sa structure (colonnes, KPIs, tables et flux d'actions) sans réécrire l'interface utilisateur.
- **Bibliothèque de Widgets Métier Réutilisables** :
  - MetricCard : Indicateurs de performance clés (valeur, delta, tendance, statut).
  - DataGrid : Tableaux opérationnels interactifs avec tri, filtrage, pagination et export CSV/JSON.
  - KanbanBoard : Gestion visuelle des flux de tâches et de sprints.
  - ActionConsole : Terminal interactif d'exécution et de journalisation des actions asynchrones.
- **Clonage & Exportation Clé en Main (Loi L0)** :
  Sérialisation complète d'une configuration de bureau en fichier JSON (desktop-template.json) pour un déploiement instantané pour tout nouveau client ou franchisé (ex. Coach OS).

### Pilier 5 : Design System & Ergonomie de Précision (12 Thèmes Canoniques)
- **12 Thèmes Portés de BusinessOS** : `dark-oled`, `warm-paper`, `glassmorphism`, `neumorphism`, `brutalism`, `aurora`, `cyberpunk`, `editorial`, `liquid-glass`, `claymorphism`, `trust`, `vibrant-block`.
- **Tokens Graphiques & CSS Variables** : Injection dynamique sur `:root` via `ThemeApplier` et `useThemeStore` (surfaces, accents, bordures, contrastes et typographies).
- **Centre de Notifications & Toasts ToastContainer** : Gestion des messages d'information, succès, avertissement et erreur avec persistance et badge non lu.
- **Framework d'Applications AppLayout** : Structure standardisée pour les applications avec barre latérale rétractable, onglets de navigation et synchronisation des breadcrumbs dans la barre de titre.
- **Launchpad AppDrawer** : Tiroir d'applications plein écran avec filtre de recherche et catégorisation par domaine.
- **Défense Anti-Écran Blanc & Migration Résiliente** : Décodeur d'enveloppe de session défensif (`migrationDefensive.ts`), gestionnaire d'erreurs global précoce dans `main.tsx`, et prise en charge du paramètre d'URL `?reset=1`.
- **Compatibilité Sonore & Vocale** : Intégration transparente avec le démon vocal certifié (`10_Tech_OS/kernel/antigravity_tts_daemon.py` / `edge-tts`).

---

## 3. Matrice de Rétrocompatibilité

| Composant | Statut V3 | Garantie Rétrocompatibilité |
| :--- | :--- | :--- |
| Window Manager V1 | Enrichi | 100% compatible. Les fenêtres existantes bénéficient automatiquement du snap et des breadcrumbs. |
| Dock & MenuBar V1 | Enrichis | 100% compatible. Ajout du Launchpad, centre de notifications, sélecteur de thème et ⌘K. |
| Catalogue Apps V1/V2 | Intact | Zéro régression. Toutes les 23 applications sont validées et fonctionnelles sans erreur. |
| CMS Hiérarchique V2 | Intact & Pivot | Les 7 niveaux Wix et le bouton CMS sont conservés et alimentent la V3. |
| Persistence Session | Étendue | Migration fluide défensive avec fallback V2 et validation d'enveloppe V3. |
| Dock V3 (BusinessOS standard) | Parachevé | 20 skins UI/UX Pro Max, placement réversible Droite/Bas, magnification fish-eye et sélecteur in-dock. |

---

## 4. Dock V3 aux Standards BusinessOS & Déploiement GitHub pour Jules

### Caractéristiques du Dock V3 :
1. **20 Habillages UI/UX Pro Max (`dockSkins.ts`)** : `glass`, `clay`, `brutalism`, `cyberpunk`, `retro`, `macos`, `win95`, `solarpunk`, `minimal-borderless`, `neumorphism-soft`, `frosted-neon`, `tokyo-night`, `nordic-frost`, etc.
2. **Placement Réversible à Droite** : Commutation instantanée entre barre horizontale en bas et colonne verticale ancrée à droite (`PanelBottom` / `PanelRight`), avec adaptation géométrique automatique de `cadreBureau()` dans `Window.tsx`.
3. **Magnification Croissante Fish-Eye** : Échelle progressive au survol (`scale(1.28)` au centre, `1.14` sur les voisins immédiats, `1.05` au deuxième rang), avec fluidité GPU (`transition-all duration-150`).
4. **Panneau de Réglages In-Dock** : Bouton `Settings2` ouvrant un popover complet permettant d'alterner la position et de choisir parmi les 20 skins avec aperçu visuel immédiat.

### Synchronisation GitHub & Hand-off Jules :
- **Dépôt GitHub public synchronisé** : [Amdkn/Agent-OS-Desktop](https://github.com/Amdkn/Agent-OS-Desktop)
- **Branche active** : `main`
- **Validation** : 0 erreur TypeScript (`tsc --noEmit`), build Vite de production réussi (`dist/` validé en 10.20s), serveur local HTTP 200 sur port 5555.


