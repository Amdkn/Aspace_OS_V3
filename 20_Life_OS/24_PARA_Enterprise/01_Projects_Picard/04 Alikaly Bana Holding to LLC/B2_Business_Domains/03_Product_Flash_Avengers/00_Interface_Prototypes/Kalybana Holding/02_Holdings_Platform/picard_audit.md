# Projet Picard — Rapport d'Audit Technique & Plan de Modernisation
## Plateforme : Kalybana Holdings

> **Rapport d'Audit Établi par :** Antigravity IDE (GravityClaw Layer 3)
> **Statut :** En attente de validation A0
> **Date de l'Audit :** 20 mai 2026

---

## ⚡ Verdict Flash

| Dimension | Note | Description |
| :--- | :---: | :--- |
| **Design & Esthétique** | **9.5 / 10** | Un travail visuel exceptionnel. Style brutaliste/futuriste immersif, palette HSL harmonieuse avec accent émeraude (`#06b77f`), typographie forte, grilles filaires (`wireframe-grid`), et micro-interactions haut de gamme. |
| **Infrastructure & Architecture** | **3.0 / 10** | Vitrine SPA purement statique déguisée en tableau de bord technique. Pas d'intégration de base de données (Supabase simulé), pas d'authentification réelle, routes injectées directement dans `main.tsx` en contournant `App.tsx`, aucune couverture de test, et du code mort (Express, Gemini API non exploités). |

---

## 🔍 Classification de la Dette Technique

### 🚨 1. Dette CRITICAL (Bloquants de Production)
* **Simulations Textuelles sans Backend (Fake Data) :** Les mentions de base de données ("Supabase Pro Tier", "Engine Core v4") sont de purs affichages textuels codés en dur dans le JSX. Aucun stockage persistant, API ou flux dynamique n'existe.
* **Investor Portal Non Fonctionnel :** Le bouton d'accès au portail investisseur et les liaisons d'authentification sont des liens morts (`#` ou sans action). Il n'y a aucun mécanisme de sécurité, de session ou de gestion d'identité.
* **Scripts de Build Non Portables :** Le script `"clean": "rm -rf dist"` dans `package.json` provoquera des erreurs sur les environnements Windows natifs n'ayant pas d'alias Bash pour `rm`.
* **Absence d'Historique Git Local :** Aucun dépôt Git n'est initialisé à la racine du projet, rendant impossible la traçabilité des modifications et l'intégration CI/CD continue.

### ⚠️ 2. Dette HIGH (Risques Structurels & Qualité)
* **Architecture de Routage Inversée :** Les routes de l'application sont déclarées directement dans `main.tsx`, tandis que `App.tsx` est un composant vide et inutilisé. Cela brise la structure conventionnelle de React et complique l'implémentation de fournisseurs de contexte globaux (Auth, Theme, Query Client).
* **Données et Logiques Métier Mélangées :** Les listes de Holdings, les étapes d'ingestion et les données financières sont injectées directement dans les composants de présentation (`Portfolio.tsx`, `Engine.tsx`, `Compliance.tsx`) au lieu d'être structurées sous forme de modèles de données, d'interfaces TypeScript et de hooks personnalisés.
* **Zéro Couverture de Tests (0% TDD) :** Absence totale de suite de tests unitaires, d'intégration ou de bout en bout (E2E), violant directement le protocole standard d'alignement ECC (Everything Claude Code) qui exige 80%+ de couverture.

### 📝 3. Dette MEDIUM (Polissage, SEO & Optimisations)
* **SEO et Métadonnées Basiques :** Le fichier `index.html` contains des métadonnées génériques. Aucun système de gestion dynamique des balises SEO (ex. React Helmet ou React Router 7 framework capabilities) n'est en place pour adapter les titres et descriptions par page.
* **Dépendances Inactives & Code Mort :** Les dépendances `express`, `@types/express`, `dotenv` et `@google/genai` sont présentes dans le `package.json` et la configuration Vite (`process.env.GEMINI_API_KEY`), mais ne sont importées nulle part.

---

## 🛠️ Le Plan de Modernisation en 4 Phases

Ce plan propose de transformer la plateforme Kalybana d'une simple maquette esthétique en une application souveraine ultra-sécurisée, robuste et dynamique.

### 🛰️ Phase 1 : Consolidation des Fondations (Est. 4h)
* **Objectif :** Rétablir un environnement de développement standardisé et robuste.
* **Actions :**
  1. Initialiser le dépôt Git (`git init`) et configurer proprement le `.gitignore`.
  2. Remplacer `"clean": "rm -rf dist"` par une solution cross-platform via `rimraf` ou script Node.
  3. Nettoyer les dépendances inutilisées ou configurer un fichier de serveur Express indépendant si un backend local est requis.
  4. Restructurer le routage : Déplacer le `<BrowserRouter>` et les routes de `main.tsx` vers `App.tsx` pour restaurer la hiérarchie React standard.

### 💎 Phase 2 : Typage, Données & SEO (Est. 6h)
* **Objectif :** Typage strict, isolation du contenu et optimisation du référencement.
* **Actions :**
  1. Extraire toutes les données codées en dur (Holdings, Statuts, Membres de l'équipe) dans un dossier `src/data/` ou des constantes typées avec TypeScript.
  2. Définir des interfaces strictes pour les modèles financiers et les entités (`Holding`, `SystemStatus`, `ComplianceOfficer`).
  3. Mettre en œuvre une gestion dynamique du SEO avec des balises méta adaptées à chaque page (titres descriptifs, descriptions uniques, balises OpenGraph pour le partage).
  4. S'assurer de la conformité totale aux directives d'accessibilité et de performance.

### ⚡ Phase 3 : Intégration Dynamique & Base de Données (Est. 12h)
* **Objectif :** Rendre l'application vivante grâce à une intégration Supabase active et sécurisée.
* **Actions :**
  1. Configurer l'intégration de Supabase (ou d'une base de données PostgreSQL souveraine).
  2. Créer les schémas de base de données : table `holdings`, table `system_logs` et table `compliance_records`.
  3. Implémenter des services d'API ou des hooks React Query / Supabase Client pour récupérer dynamiquement les données financières en temps réel (ex. les `$248,192,004.00` d'exposition globale et les rendements YTD).
  4. Rendre le module "Engine Ingestion" fonctionnel en simulant ou connectant de vrais flux de données (Flux RSS, API publiques de cadastres, etc.) intégrés en arrière-plan.

### 🔒 Phase 4 : Authentification, Sécurité & TDD (Est. 10h)
* **Objectif :** Sécuriser les accès investisseurs et garantir la stabilité via les tests.
* **Actions :**
  1. Implémenter le système d'authentification Supabase Auth pour l'accès "Investor Portal" (accès sécurisé par e-mail/mot de passe ou SSO).
  2. Mettre en place des Politiques de Sécurité au niveau des lignes (RLS) sur Supabase pour protéger les données confidentielles des investisseurs.
  3. Rédiger les tests unitaires et d'intégration (Vitest/React Testing Library) pour atteindre les 80%+ de couverture de tests exigés par le protocole ECC.
  4. Préparer le déploiement sur une infrastructure souveraine (Dokploy ou Vercel de production) avec pipelines de build automatisés.

---

## 🚦 Grille d'Approbation (Verification Gate)

Avant d'entamer la Phase 1 du plan d'action, merci de donner vos instructions ou d'approuver l'approche.

- [ ] **Approuver et lancer la Phase 1 (Fondations & Routage)**
- [ ] **Demander des ajustements sur le Plan de Modernisation**
- [ ] **Définir des priorités spécifiques (ex. Connexion immédiate à Supabase)**

---
*Rapport généré avec rigueur sous protocole Picard.*
