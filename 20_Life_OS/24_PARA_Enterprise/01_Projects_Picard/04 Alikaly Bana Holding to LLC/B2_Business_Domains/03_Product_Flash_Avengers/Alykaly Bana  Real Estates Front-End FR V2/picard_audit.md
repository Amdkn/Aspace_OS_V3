# Projet Picard — Rapport d'Audit Technique & Plan de Modernisation
## Plateforme : Alykaly Holding — Front-End FR V2

> **Rapport d'Audit Établi par :** Antigravity IDE (Gemini CLI Full-Spectrum)
> **Statut :** En attente de validation A0
> **Date de l'Audit :** 20 mai 2026

---

## ⚡ Verdict Flash

| Dimension | Note | Description |
| :--- | :---: | :--- |
| **Design & Esthétique** | **9.5 / 10** | Une exécution visuelle exceptionnelle. Thème "Slate & Emerald" avec des accents "Old-Money/Legal". Utilisation de textures de grain, d'animations de marquee, et d'un widget d'audit ("StitchWidget") extrêmement immersif. |
| **Infrastructure & Architecture** | **1.0 / 10** | **Dette Technique Critique.** L'ensemble de l'application (React, Tailwind, Babel) est chargé via CDN et transpilé directement dans le navigateur. Aucun build system, aucune gestion de dépendances, aucune modularité. |

---

## 🔍 Classification de la Dette Technique

### 🚨 1. Dette CRITICAL (Bloquants de Production)
*   **Babel Standalone :** L'usage de `@babel/standalone` dans le navigateur est un "anti-pattern" de production. Cela cause des lenteurs au chargement (FOUC) et consomme inutilement des ressources client.
*   **CDN-Only :** Toutes les librairies (React 18.3, Lucide, Tailwind) dépendent de serveurs tiers (`unpkg.com`, `cdn.tailwindcss.com`). Une panne de CDN paralyse le site.
*   **Code Monolithique :** L'intégralité de la logique UI et métier (Header, Hero, Widget d'Audit, Ticker) réside dans un seul fichier HTML de 50 Ko.

### ⚠️ 2. Dette HIGH (Risques Structurels & Qualité)
*   **Helper d'Icônes Custom :** Utilisation d'un composant `Icon` qui manipule le DOM manuellement (`ref.current.innerHTML`) pour injecter des SVGs Lucide, au lieu d'utiliser le package npm officiel.
*   **Données en Dur :** Les statistiques de récupération ($4.72M) et les dossiers récents du ticker sont codés en dur dans le JSX.
*   **Zéro Modularité :** Aucun système d'import/export (ESM). Impossible de tester les composants isolément.

### 📝 3. Dette MEDIUM (Polissage, SEO & Optimisations)
*   **SEO Limité :** Pas de gestion dynamique des métadonnées par route (bien que le projet soit une SPA).
*   **Performance Assets :** Utilisation d'images distantes via `lh3.googleusercontent.com` sans optimisation (WebP, srcset).

---

## 🛠️ Le Plan de Modernisation en 4 Phases

### 🛰️ Phase 1 : Extraction & Fondation (Est. 4h)
*   **Objectif :** Établir un environnement de développement professionnel (Souveraineté).
*   **Actions :**
    1.  Initialiser un projet **Next.js 15 (App Router)** ou **Vite + React + TS**.
    2.  Découper le monolithe en composants fonctionnels (`/components/ui/`, `/components/marketing/`).
    3.  Migrer les styles CSS custom et Tailwind v4 vers un fichier global propre.

### 💎 Phase 2 : Typage & Polish (Est. 3h)
*   **Objectif :** Sécuriser la logique et améliorer le SEO.
*   **Actions :**
    1.  Définir les interfaces TypeScript pour les `AuditCase`, `StatBlock` et `ExpertiseCard`.
    2.  Implémenter le hook `useSEO` pour les balises OpenGraph et Meta.
    3.  Remplacer le helper d'icônes par les composants `lucide-react` natifs.

### ⚡ Phase 3 : Dynamisation (Est. 8h)
*   **Objectif :** Rendre l'audit interactif et le dashboard vivant.
*   **Actions :**
    1.  Connecter le `StitchWidget` à une API (Supabase) pour valider réellement les numéros de dossier.
    2.  Rendre le `RecoveryTicker` dynamique (fetch des dernières victoires en base).
    3.  Mettre en place une validation de formulaire avec **Zod**.

### 🔒 Phase 4 : Déploiement & TDD (Est. 5h)
*   **Objectif :** Garantir la stabilité et la disponibilité.
*   **Actions :**
    1.  Mise en place de tests unitaires (Vitest) pour la logique de formatage des dossiers Ohio.
    2.  Configuration Docker et pipeline de déploiement (Dokploy/Vercel).
    3.  Audit de performance Lighthouse pour viser le 100/100.

---

## 🚦 Grille d'Approbation (Verification Gate)

L'interface est visuellement prête pour la production, mais l'infrastructure est au stade de "bac à sable".

- [ ] **Approuver la Phase 1 (Extraction vers Next.js/Vite)**
- [ ] **Lancer une session de prévisualisation locale (SANS build)**

---
*Rapport généré avec rigueur sous protocole Picard.*
