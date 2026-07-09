# 🪐 Picard Audit : RILCOT_OS

**Verdict Flash**
- **Design Score** : 8.5/10 (UI propre, cohérente, inspirée de l'expérience mobile-first).
- **Infrastructure Score** : 6/10 (Vite + React 19 est moderne, mais le routage interne est rudimentaire).

---

## 📝 Liste des Dettes

### 🔴 CRITIQUE (Bloquants pour la mise en production)
- **Routage Monolithique** : La navigation est gérée par un simple `useState` dans `App.tsx`. Cela casse le bouton "Précédent" du navigateur, empêche le deep linking (partage d'URL spécifique) et nuit gravement au SEO.
- **Contrainte de Layout** : Forçage systématique du `max-w-md` à la racine, ce qui rend l'expérience médiocre sur desktop.

### 🟡 HAUTE (Risques structurels)
- **Typage Partiel** : Utilisation de `any` pour certains composants critiques (ex: `NavItem` icons).
- **Gestion des Assets** : Dépendance à des services externes comme `picsum.photos` pour les avatars, au lieu d'assets locaux ou gérés par Supabase.
- **Dette de Synchro** : Les composants comme `Dashboard` ou `Projects` re-fetchent les données via `useEffect` sans cache global performant (SWR ou React Query).

### 🟢 MOYENNE (Améliorations de confort)
- **SEO & Metadata** : Pas de gestion dynamique des balises Title/OG par page.
- **Validation** : Les formulaires (ex: Création de projet) manquent de validation robuste côté client (Zod/Hook Form).

---

## 🚀 Plan d'Action (The 4-Phase Blueprint)

### Phase 1 : Foundation (Migration Next.js 15)
- **Initialisation** : Setup d'un projet Next.js 15 avec App Router et TypeScript strict.
- **Routage** : Conversion des `screens/*.tsx` en routes réelles (`/app/dashboard`, `/app/projects`, etc.).
- **Auth** : Portage du `AuthProvider` vers les Server/Client Components de Next.js.
- **Temps estimé** : 2h.

### Phase 2 : Polish & Layout
- **Layout Responsive** : Remplacement du `max-w-md` par un layout adaptatif (Sidebar sur desktop, Bottom Nav sur mobile).
- **Metadata API** : Implémentation des fichiers `layout.tsx` et `page.tsx` avec gestion SEO.
- **Icons & Assets** : Consolidation du composant `Icons` et remplacement des placeholders.
- **Temps estimé** : 1.5h.

### Phase 3 : Backend & Data
- **API Routes** : Sécurisation des appels Supabase via des API routes si nécessaire.
- **Validation** : Intégration de **Zod** pour le schéma des données `Project` et `Profile`.
- **Cache** : Mise en place d'une stratégie de cache efficace via Server Components ou `next/cache`.
- **Temps estimé** : 2h.

### Phase 4 : Deployment & CI/CD
- **Docker** : Optimisation du `Dockerfile` pour Next.js (multi-stage build).
- **Dokploy/Vercel** : Configuration du pipeline de déploiement automatique.
- **Health Check** : Mise en place de scripts de validation `npm run gate`.
- **Temps estimé** : 1h.

---

## ⚖️ Verdict Final
Le projet est un excellent prototype fonctionnel. La logique métier est bien isolée, ce qui rend la migration vers une infrastructure souveraine (Picard/Solaris) simple et rapide.

**Action recommandée** : Lancer la **Phase 1** immédiatement pour stabiliser le routage.

---
*Audit réalisé par Gemini CLI Full-Spectrum — Skill picard-audit activé.*
