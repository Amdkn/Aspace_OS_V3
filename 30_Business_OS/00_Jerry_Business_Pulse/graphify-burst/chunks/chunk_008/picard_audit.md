# 🎯 Rapport d'Audit Picard — ABC OS Community-01

Ce document constitue la **Phase 1 (Deep Ingestion & Audit)** du workflow Picard appliqué au prototype statique de tableau de bord communautaire **ABC OS Community-01**.

---

## 1. Cartographie du Prototype Legacy

Le projet analysé est un prototype interactif statique conçu pour simuler une application mobile sur navigateur.

### Structure des Fichiers Source
- **Racine du projet** :
  - [ABC OS Dashboard.html](file:///C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/abc/apps/ABC%20OS%20Community-01/ABC%20OS%20Dashboard.html) : Contient la structure HTML globale, le simulateur de terminal mobile iOS (notch, statusbar, navigation) ainsi qu'une mise en page Bento alternative pour le mode Desktop.
  - [app.js](file:///C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/abc/apps/ABC%20OS%20Community-01/app.js) : Contient l'état global mocké (`DATA`), les configurations des hubs, les générateurs de composants HTML (avatars, barres de progression, jauge SVG) et la logique d'interactivité du dock de réglages.
- **Dossier `hubs/`** :
  - Quatre pages HTML dupliquées ([community.html](file:///C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/abc/apps/ABC%20OS%20Community-01/hubs/community.html), [learn.html](file:///C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/abc/apps/ABC%20OS%20Community-01/hubs/learn.html), [build.html](file:///C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/abc/apps/ABC%20OS%20Community-01/hubs/build.html), [brand.html](file:///C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/abc/apps/ABC%20OS%20Community-01/hubs/brand.html)) servant de coquilles vides. Elles portent un attribut `data-hub` sur le `body` et délèguent le rendu à `hub.js`.
- **Dossier `assets/`** :
  - `abc-os.css` : Thèmes (couleurs CSS variables sombres/claires), police Space Grotesk, et styles génériques.
  - `hub.css` : Mise en page spécifique aux écrans intérieurs des hubs.
  - `hub.js` : Moteur de rendu dynamique vanilla. Injecte le HTML des écrans intérieurs en fonction du hub actif (discussions pour Community, cours pour Learn, jalons pour Build, jauge SVG pour Brand).

---

## 2. Évaluation Picard & Scores

| Métrique | Score | Justification |
| :--- | :---: | :--- |
| **Design / Esthétique** | **8.5/10** | Excellente direction artistique. Design moderne de type "Bento", dégradés harmonieux, gestion des thèmes clairs/sombres via tokens CSS, jauge SVG dynamique bien calculée et micro-interactions simulées convaincantes. |
| **Infrastructure / Code** | **0.0/10** | Aucun framework ni linter. Rendu entièrement dépendant de l'injection sauvage de chaînes de caractères HTML dans le DOM (`innerHTML`). Aucune gestion d'API ou persistance réelle (tout est dans un objet `DATA` codé en dur). Polices chargées via CDN externe. |
| **Score Global Picard** | **42.5/100** | Prototype esthétique de haute fidélité, mais nécessitant une réécriture complète sous forme de Web App moderne. |

---

## 3. Registre de la Dette Technique

### Dette Critique (Bloquante pour la Production)
- **Injection XSS potentielle** : Rendu dynamique basé sur l'interpolation de chaînes de caractères non désinfectées injectées via `innerHTML`.
- **Zéro connectivité API & Persistance** : Aucune persistance d'état. Les interactions de base (comme simuler une erreur ou recharger) réinitialisent simplement l'état mémoire ou écrivent superficiellement dans `localStorage`.
- **Duplication de coquilles HTML** : Quatre fichiers HTML distincts sous `hubs/` recopiant exactement le même squelette de simulateur de téléphone.
- **Vanilla JS non typé** : Pas de build, pas de validation à la compilation, aucune protection contre les propriétés indéfinies au runtime.

### Dette Haute
- **Cibles de liens en dur** : Redirections complètes du navigateur (`location.href`) provoquant un rechargement complet de la page à chaque changement de hub ou retour au dashboard, ce qui brise l'expérience Single Page App (SPA).
- **Dépendances CDN tierces** : Les Google Fonts et Material Symbols sont importés directement depuis les CDN de Google, créant des délais de chargement (FCP/CLS) et une dépendance réseau externe.
- **Mélange des responsabilités visuelles** : Le prototype embarque à la fois la mise en page mobile physique simulée (notches, statusbars) et les écrans réels de l'application, polluant la mise en page.

### Dette Moyenne
- **SSR-unsafe theme toggling** : Le basculement sombre/clair repose sur une classe injectée côté client via `localStorage` au démarrage du script, ce qui provoquera un flash visuel (FCP blanc avant passage en sombre) sous SSR.
- **Absence de SEO structuré** : Balises Meta rudimentaires et statiques.

---

## 4. Plan de Migration cible (Next.js 15 TypeScript)

Pour transformer ce prototype en application de production sous le chemin court canonique `30_Business_OS/10_Projects/abc/apps/abc-os-community` :

### Étape 1 : Initialisation & Born-Shorting
1. Scaffold d'un nouveau projet Next.js 15 strict TypeScript :
   ```powershell
   npx -y create-next-app@15 abc-os-community --ts --tailwind --app --src-dir --eslint --no-src-dir
   ```
2. Configuration de l'architecture propre :
   - `src/app/` : App Router pour le routage natif (`/`, `/community`, `/learn`, `/build-hub`, `/brand`).
   - `src/components/` : Composants réutilisables (ex: `BentoLayout`, `MobileWrapper`, `HubCard`, `ActivityFeed`, `ActionList`, `SvgGauge`).
   - `src/design/` : Centralisation des tokens de couleur dans `tokens.ts` et styles globaux.

### Étape 2 : Extraction de la Simulation
- Séparer la maquette en deux modes d'affichage gérés par media-queries natifs ou une route de prévisualisation dédiée :
  - **Mode App Réel** : L'application s'adapte à la fenêtre (Responsive CSS mobile-first). Le frame physique de téléphone et le dock de réglages sont exclus du build final de production.
  - **Mode Sandbox (Optionnel)** : Une page de démo `/sandbox` qui enrobe l'application dans le frame iOS simulé pour le client ou la démonstration.

### Étape 3 : Refactoring TypeScript & ESM
- Traduction de `DATA` en schémas de données typés (`Member`, `Cooperative`, `HubConfig`, `ActionItem`, `ActivityFeedItem`, `SpotlightProject`).
- Intégration du client SDK Supabase pour brancher ces structures de données sur les tables relationnelles définies lors de la phase d'architecture.

### Étape 4 : Optimisation & SEO
- Hébergement local des polices (Space Grotesk, Fraunces) pour supprimer l'appel CDN de Google.
- Configuration du routeur et des transitions animées (Framer Motion ou CSS transitions légères).
- Métadonnées SEO structurées par route.
