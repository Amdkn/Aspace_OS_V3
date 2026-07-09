# 🪐 Picard Audit: Kalybana Holding OS
**Status**: DRAFT | **Project**: `03_Kalybana_Production` | **Date**: 2026-05-20

## 🎯 Verdict Flash
- **Design Score**: 9/10 (Material Design 3 Sovereign Aesthetic, consistent, polished)
- **Infrastructure Score**: 4/10 (Static Vite SPA, basic SEO, hardcoded data)

---

## 🏗️ Dette List

### 🛑 CRITICAL (Blockers)
- **SEO/Metadata Zero**: Site de type "Holding" sans aucune optimisation SEO (SPA pure). Risque d'invisibilité institutionnelle.
- **Confusion Dépendances**: Présence de `express` et `@google/genai` dans un frontend Vite sans implémentation backend visible.

### ⚠️ HIGH (Structural)
- **Architecture SPA**: Routage uniquement côté client via `react-router-dom`. Manque de Server Components pour la performance et la sécurité.
- **Data Hardcoded**: Tout l' "Asset Manifest" est codé en dur dans les composants. Maintenance difficile et manque de dynamisme.

### ⚙️ MEDIUM (Polish)
- **Assets Locaux**: Dépendance aux fontes système/navigateur. Absence d'optimisation d'images.
- **PWA/Manifest**: Pas de support hors-ligne ni d'icônes d'application pour une expérience OS fluide.

---

## 🗺️ The 4-Phase Blueprint (Solaris Pattern)

### Phase 1: Foundation (Infrastructure) - *Est: 2 jours*
- Migration vers **Next.js 15 (App Router)**.
- Mise en place du mode strict TypeScript.
- Centralisation des layouts (Sovereign/Bana).

### Phase 2: Polish (SEO & Identity) - *Est: 1 jour*
- Implémentation de la **Metadata API** pour chaque page.
- Optimisation des polices (Next/Font) et des icônes (Lucide).
- Mise en place de `next-sitemap` et robots.txt.

### Phase 3: Backend (Data Sovereign) - *Est: 3 jours*
- Intégration d'un **Headless CMS (Sanity)** ou **Supabase** pour gérer le Portfolio et le "SOB Engine".
- Création de routes API pour les fonctions génératives (Gemini).
- Sécurisation des clés API via Server Actions.

### Phase 4: Deploy (Sovereign Launch) - *Est: 1 jour*
- Déploiement sur **Vercel** ou **Dokploy**.
- Configuration de l'environnement de staging.
- Mise en place du monitoring d'erreurs (Sentry).

---

## 🚦 Verification Gate
**Action requise :** Approbation du passage en Next.js (Phase 1) par l'utilisateur (A0).

*Codifié par l'Agent Picard — Gemini CLI Sovereign Protocol.*
