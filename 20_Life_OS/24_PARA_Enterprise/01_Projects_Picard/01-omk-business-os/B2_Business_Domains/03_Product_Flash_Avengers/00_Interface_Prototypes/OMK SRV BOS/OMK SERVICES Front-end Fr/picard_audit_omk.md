# 🔆 OMK SERVICES — Audit Technique Picard

> **Date** : 2026-05-17
> **Source** : `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\OMK SRV BOS\Oussoumane Malamine Kounta Service\OMK SERVICES Front-end Fr`
> **Statut** : 🟡 AUDIT COMPLETED — AWAITING GO

## 1. Verdict Flash
| Dimension | Score | Note |
|-----------|-------|------|
| 🎨 Design | 9.5/10 | Visuel ultra-premium. Glassmorphism, Mesh gradients, animations fluides. Prêt pour le marché. |
| 🏗️ Infra  | 0/10 | Prototype pur. Babel in-browser, React via CDN, Tailwind JIT CDN. Aucun pipeline de build. |
| **Global**| **32/100** | Cible: 85/100 après migration Next.js 15. |

## 2. Liste des Dettes
### 🔴 CRITICAL
- [ ] **Babel in-browser** : Le fichier `omk-app.jsx` est compilé à la volée par le client. Performance catastrophique en prod.
- [ ] **CDN-only dependencies** : React, ReactDOM et Tailwind sont chargés via unpkg/cdn. Risque de coupure et latence.
- [ ] **Pas de structure de build** : Aucune trace de `package.json` ou d'environnement Node.js.
- [ ] **Pas de Git** : Versioning inexistant sur le dossier source.

### 🟠 HIGH
- [ ] **Zéro typage** : Code JSX brut sans TypeScript. Risque élevé de régressions lors du refactor.
- [ ] **Global state as bus** : Utilisation implicite de variables globales pour les icônes et composants.
- [ ] **Fichier géant** : `omk-app.jsx` fait 43KB et contient toute la logique de page. Inmaintenable.

### 🟡 MEDIUM
- [ ] **SEO Inexistant** : Pas de balises Meta, OG ou Favicon configurées proprement.
- [ ] **Polices externes** : Dépendance directe à Google Fonts (latence/privacy).

## 3. Plan Picard (4 Phases)
### Phase 1 : Fondation (Est. 45min)
- `npx create-next-app@latest omk-services --typescript --app`
- Initialisation Git.
- Migration de `omk-app.jsx` vers une structure de composants ESM (`/components/`).
- Découpage du fichier géant en sections atomiques.

### Phase 2 : Polish & Performance (Est. 30min)
- Import des fonts via `next/font/google` (Space Grotesk, Inter, JetBrains Mono).
- Extraction du CSS global vers `globals.css`.
- Configuration des métadonnées SEO/OG.

### Phase 3 : Backend Integration (Est. 1h)
- Mise en place de la table de leads.
- API Route Next.js pour le formulaire "Réserver un audit".
- Branchement de Nova (IA) si nécessaire.

### Phase 4 : Launch (Est. 15min)
- Push GitHub.
- Déploiement Vercel.

---
*Generated via picard-audit skill — Gemini CLI Full-Spectrum.*
