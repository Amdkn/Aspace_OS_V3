# 🔆 [PROJECT NAME] — Audit Technique Picard & Prod Workflow

> **Date** : [DATE]
> **Source** : `[PATH]`
> **Statut** : 🔴 PENDING AUDIT (En attente d'approbation A0 pour Phase 3)

## 1. Verdict Flash
| Dimension | Score | Note |
|-----------|-------|------|
| 🎨 Design | ?/10 | [Feedback visuel, textures, CSS] |
| 🏗️ Infra  | 0/10 | Prototype pur sans package.json / TS / bundler. |
| **Global**| **?/100** | Cible: 85/100 |

## 2. Liste des Dettes
### 🔴 CRITICAL
- [ ] [Issue, ex: Babel CDN, pas de Git, pas de package.json]

### 🟠 HIGH
- [ ] [Issue, ex: pas de typage, inline CSS styles, variables globales]

### 🟡 MEDIUM
- [ ] [Issue, ex: pas de SEO/OG meta, magic numbers, pas de tests]

## 3. Plan Picard Souverain d'Implémentation et Déploiement (7 Phases)

- **Phase 1 : Diagnostic & Audit** (Création de ce document, gel des sources)
- **Phase 2 : Approbation A0** (Attente du GO explicite de l'utilisateur)
- **Phase 3 : Born-Short Repo Migration (ADR-INFRA-002)**
  - Initialisation Git local
  - Initialisation du squelette Next.js 15 sous `30_Business_OS/10_Projects/[PROJET]/apps/[APP]`
  - Création du lien de jonction symbolique (Junction Link) depuis PARA `_verse` vers le dossier court.
- **Phase 4 : Réfactorisation ESM & TypeScript**
  - Conversion `.jsx` -> `.tsx`
  - Suppression des liaisons globales au profit de modules ESM propres
  - Remplacement des polices CDN par `next/font` locales
  - Ajout des balises SEO & OpenGraph métadonnées
  - Remplacement de `postMessage` par un hook client `useLocalStorage` autonome.
- **Phase 5 : Vérification de Build Stricte**
  - Validation typecheck `npx tsc --noEmit`
  - Validation du build production `npm run build`
  - Lancement local sur `localhost:3000` et test HTTP
- **Phase 6 : Livraison GitHub & Déploiement VPS Dokploy**
  - Envoi vers le dépôt distant GitHub
  - Création de l'application dans Dokploy VPS (`https://dokploy.148.230.92.235.sslip.io/`)
  - Configuration du sous-domaine et des variables d'environnement
  - Déploiement et test final en production
- **Phase 7 : Capitalisation Digital Twin**
  - Entrée de log dans `README.md` et `log.md` de la Memory Core

---
*Généré via picard-audit-and-prod-workflow.*
