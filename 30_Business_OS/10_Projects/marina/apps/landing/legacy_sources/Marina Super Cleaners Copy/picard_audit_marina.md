# 🔆 MARINA CLEANING CO. — Audit Technique Picard

> **Date** : 2026-05-17
> **Source** : `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\Marina Super Cleaners (Copy)`
> **Statut** : 🟡 AUDIT COMPLETED — AWAITING GO

## 1. Verdict Flash
| Dimension | Score | Note |
|-----------|-------|------|
| 🎨 Design | 9.5/10 | Esthétique "Hospitality Grade". Très propre, typographie élégante, palette organique. |
| 🏗️ Infra  | 0/10 | Prototype pur. Babel in-browser, dépendances CDN, pas de build pipeline. |
| **Global**| **32/100** | Cible: 85/100 après migration Next.js 15. |

## 2. Liste des Dettes
### 🔴 CRITICAL
- [ ] **Babel in-browser** : Le script React est compilé à la volée par le client. Impact performance sévère.
- [ ] **CDN-only dependencies** : Dépendance totale à `unpkg` pour React, Babel et Lucide.
- [ ] **Tailwind JIT CDN** : Utilisation du script CDN de Tailwind (non recommandé pour la prod).
- [ ] **Pas de structure Node.js** : Aucun `package.json`, impossible de gérer les versions ou le build.
- [ ] **Pas de Git** : Aucun historique de version.

### 🟠 HIGH
- [ ] **Zéro typage** : Code JSX brut sans TypeScript.
- [ ] **Monolithe HTML** : Styles CSS, structure HTML et logique React mélangés dans un seul fichier de 40KB.
- [ ] **Custom Element Ad-hoc** : `image-slot.js` est un Web Component externe qui doit être intégré proprement au cycle de vie React/Next.

### 🟡 MEDIUM
- [ ] **SEO Manquant** : Pas de configuration Meta/OG.
- [ ] **Google Fonts CDN** : Dépendance externe pour Urbanist, Inter et Instrument Serif.

## 3. Plan Picard (4 Phases)
### Phase 1 : Fondation (Est. 45min)
- `npx create-next-app@latest marina-cleaning --typescript --app --tailwind`
- Initialisation Git.
- Migration de `Marina Cleaning Co.html` vers une structure de composants ESM.
- Refactor de `image-slot.js` en composant React natif ou intégration propre.

### Phase 2 : Polish & SEO (Est. 30min)
- Import des polices via `next/font/google`.
- Migration du CSS personnalisé vers Tailwind config ou `globals.css`.
- Ajout des métadonnées SEO/OG.

### Phase 3 : Backend (Est. 1h)
- Intégration d'un formulaire de réservation (API Route).
- Stockage des demandes (Supabase ou Airtable).

### Phase 4 : Launch (Est. 15min)
- Déploiement Vercel / GitHub.

---
*Generated via picard-audit skill — Gemini CLI Full-Spectrum.*
