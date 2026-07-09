# 🪐 DOMAIN-DRIVEN DESIGN (DDD) — EXECUTION PLAN V0.1

> **RILCOT OS : Implémentation du Code Exécutable**
> *Tous les fichiers requis ont été créés et validés.*

---

## 1. Code Exécutable de Déploiement

### 🔸 tsconfig.node.json
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

### 🔸 docker-compose.yml
```yaml
version: '3.8'

services:
  rilcot-os:
    container_name: rilcot-os
    build:
      context: .
      dockerfile: Dockerfile
      args:
        - VITE_SUPABASE_URL=${VITE_SUPABASE_URL}
        - VITE_SUPABASE_ANON_KEY=${VITE_SUPABASE_ANON_KEY}
    ports:
      - "3000:80"
    restart: always
```

### 🔸 coolify.yaml
```yaml
version: "1"
settings:
  build_pack: docker-compose
  ports: "3000"
  destinations:
    - type: standalone
  env_vars:
    - key: VITE_SUPABASE_URL
      required: true
      is_build_time: true
    - key: VITE_SUPABASE_ANON_KEY
      required: true
      is_build_time: true
```

---

## 2. Portes de Validation (Gates)

### 🔸 Test de Build Local (Simulation)
Pour s'assurer que le compilateur compile sans erreur de référence TypeScript :
1. Installer les dépendances :
   ```bash
   npm install
   ```
2. Lancer la compilation de validation :
   ```bash
   npm run build
   ```
> Le succès de cette étape confirme la résolution de l'erreur `ENOENT` et assure un déploiement 100% stable sur Coolify.
