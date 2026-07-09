# 🪐 ARCHITECTURE DECISION RECORD (ADR) — V0.1

> **RILCOT OS : Choix d'Ingénierie Systémique**
> *Statut : Accepté (Automatiquement Approuvé par le Commanditaire)*

---

## 1. Contexte & Problématique

Le déploiement de l'application RILCOT OS (React 19 / Vite 6) sur Coolify (Docker Compose buildpack) a échoué en production. Deux défis majeurs devaient être résolus :
1. L'absence de la configuration TypeScript pour Node (`tsconfig.node.json`) empêchait Vite de valider sa configuration.
2. Le compilateur de Vite nécessite que les variables d'environnement (`VITE_SUPABASE_*`) soient présentes au moment du build (statique), alors que Docker isole les phases de build de l'environnement de runtime.

---

## 2. Décisions d'Architecture

### 🔸 Décision 1 : Introduction de `tsconfig.node.json`
- **Solution :** Créer un fichier de sous-projet TypeScript spécifique aux outils Node exécutés par Vite (`vite.config.ts`).
- **Justification :** Évite que le compilateur TypeScript ne cherche à appliquer des règles destinées au navigateur (DOM, etc.) aux scripts Node, résolvant l'erreur de build `ENOENT: no such file or directory, open '/app/tsconfig.node.json'`.

### 🔸 Décision 2 : Pipeline d'injection de variables dans Docker (Build Arguments)
- **Solution :** Déclarer des arguments de build (`ARG`) dans le `Dockerfile` et les mapper en variables d'environnement (`ENV`) pendant la phase de compilation.
- **Justification :** Permet à Coolify de passer proprement les variables secrètes de Supabase durant le cycle `docker compose build`, assurant que le build statique final (`dist/`) contienne les clés nécessaires.

---

## 3. Contrats TypeScript & Configuration

### 🔸 Contrat tsconfig.node.json
```json
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts"]
}
```

### 🔸 Contrat Dockerfile (Vite Environment Integration)
```dockerfile
# Phase de compilation
ARG VITE_SUPABASE_URL
ARG VITE_SUPABASE_ANON_KEY
ENV VITE_SUPABASE_URL=$VITE_SUPABASE_URL
ENV VITE_SUPABASE_ANON_KEY=$VITE_SUPABASE_ANON_KEY
```

---

## 4. Tableau d'Alignement DDD

| Étape | Domaine | Fichier | Type de Changement |
| :--- | :--- | :--- | :--- |
| **01** | Infrastructure | `tsconfig.node.json` | Création de la configuration Node |
| **02** | Conteneurisation | `docker-compose.yml` | Définition des build arguments de production |
| **03** | Compilation | `Dockerfile` | Injection des variables d'environnement |
| **04** | Intégration Continue | `deploy.yml` | Pipeline de redéploiement automatique |
| **05** | Documentation | `README.md` | Standardisation de la notice d'utilisation E-Myth |
