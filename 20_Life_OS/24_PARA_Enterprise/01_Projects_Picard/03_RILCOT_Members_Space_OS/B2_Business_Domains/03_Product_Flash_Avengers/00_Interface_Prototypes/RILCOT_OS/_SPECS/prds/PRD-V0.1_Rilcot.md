# 🪐 PRODUCT REQUIREMENTS DOCUMENT (PRD) — V0.1

> **RILCOT OS : Consolidation de Déploiement & Purge API**
> *Header TVR : T = Faisabilité Technique (Élevée), V = Valeur Business (Cruciale), R = Réutilisabilité (Élevée)*

---

## 1. Description & Objectifs

Ce PRD formalise la stabilisation de l'infrastructure de **RILCOT OS V0** et l'achèvement de la migration vers une architecture 100% souveraine, en résolvant le crash de build Coolify et en garantissant l'intégrité de la sécurité des données.

---

## 2. User Stories (US)

### 🔹 Phase A : Résolution du Build Vite/TypeScript
- **US-01 :** En tant que SysAdmin (A2/A3), je veux que le build TypeScript de Vite n'échoue pas sur les références manquantes afin que Coolify puisse compiler les actifs sans erreur.
- **US-02 :** En tant que Développeur, je veux que la configuration TypeScript pour Node (`tsconfig.node.json`) soit présente et isolée pour compiler proprement `vite.config.ts`.

### 🔹 Phase B : Intégrité & Sécurité (Purge API)
- **US-03 :** En tant que Commanditaire (A0), je veux qu'aucune clé API ou trace de modèle Gemini ne soit présente dans le code de production pour garantir l'indépendance technologique.
- **US-04 :** En tant qu'utilisateur, je veux que mes variables d'environnement pour Supabase soient chargées dynamiquement lors du build conteneurisé.

### 🔹 Phase C : Déploiement Souverain (Coolify)
- **US-05 :** En tant que SysAdmin, je veux un fichier `docker-compose.yml` et un `Dockerfile` optimisé acceptant les build arguments pour automatiser le déploiement sur VPS 1.
- **US-06 :** En tant que DevOps, je veux un fichier `coolify.yaml` et un workflow GitHub Actions pour déclencher des builds automatisés dès la fusion dans `main`.

---

## 3. Anti-Patterns (Tableau Comparatif)

| Anti-Pattern ❌ | Pratique Recommandée ASpace OS V2 ✅ |
| :--- | :--- |
| Injecter des clés d'API (Gemini, Supabase) en dur dans `App.tsx` | Charger toutes les variables depuis `import.meta.env` compilé par le PaaS. |
| Laisser des fichiers d'outils Vite non configurés en TypeScript | Ajouter `tsconfig.node.json` et référencer les fichiers de build. |
| Servir une SPA en production avec un serveur Node dev | Compiler le build statique et le servir via Nginx Alpine ultra-léger. |
| Ignorer les variables d'environnement lors de la phase docker build | Déclarer `ARG` et `ENV` dans le Dockerfile pour que le compilateur injecte les valeurs. |

---

## 4. Fichiers Impactés

- `tsconfig.node.json` *(Créé)*
- `docker-compose.yml` *(Créé)*
- `coolify.yaml` *(Créé)*
- `.dockerignore` *(Créé)*
- `.env.example` *(Créé)*
- `.github/workflows/deploy.yml` *(Créé)*
- `Dockerfile` *(Mis à jour)*
- `README.md` *(Mis à jour)*
