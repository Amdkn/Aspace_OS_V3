|# Dashboard de Gouvernance d'Infrastructure — A'Space OS V2

> Layer: L0 Tech OS
> Date: 2026-06-04
> Status: PLANNED

## Overview

Ce dashboard de gouvernance d'infrastructure centralise la gestion des secrets, des tokens, des configurations et des intégrations pour A'Space OS V2. Il permet de surveiller, gérer et auditer tous les secrets et configurations de manière centralisée.

## Architecture

### Stack Technique

| Composant | Description |
|-----------|-------------|
| **Frontend** | React / Next.js |
| **Backend** | Node.js / Express |
| **Base de données** | PostgreSQL |
| **Authentification** | OAuth2 / JWT |
| **Sécurité** | Hashage bcrypt, chiffrement AES-256 |

### Structure des Données

```sql
-- Secrets
CREATE TABLE secrets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    value TEXT NOT NULL,
    category VARCHAR(100) NOT NULL,
    environment VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_used_at TIMESTAMP,
    expires_at TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    metadata JSONB
);

-- Tokens
CREATE TABLE tokens (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    token TEXT NOT NULL,
    type VARCHAR(100) NOT NULL,
    environment VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_used_at TIMESTAMP,
    expires_at TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    metadata JSONB
);

-- Configurations
CREATE TABLE configurations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    value TEXT NOT NULL,
    category VARCHAR(100) NOT NULL,
    environment VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    metadata JSONB
);

-- Audit Logs
CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    action VARCHAR(100) NOT NULL,
    entity_type VARCHAR(100) NOT NULL,
    entity_id INTEGER NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    old_value TEXT,
    new_value TEXT,
    ip_address VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Endpoints API

### Authentification

| Endpoint | Méthode | Description |
|----------|---------|-------------|
| `/api/auth/login` | POST | Connexion utilisateur |
| `/api/auth/logout` | POST | Déconnexion utilisateur |
| `/api/auth/refresh` | POST | Rafraîchir le token |

### Secrets

| Endpoint | Méthode | Description |
|----------|---------|-------------|
| `/api/secrets` | GET | Lister tous les secrets |
| `/api/secrets/:id` | GET | Obtenir un secret |
| `/api/secrets` | POST | Créer un secret |
| `/api/secrets/:id` | PUT | Mettre à jour un secret |
| `/api/secrets/:id` | DELETE | Supprimer un secret |
| `/api/secrets/:id/reveal` | POST | Révéler un secret |
| `/api/secrets/:id/revoke` | POST | Révoquer un secret |

### Tokens

| Endpoint | Méthode | Description |
|----------|---------|-------------|
| `/api/tokens` | GET | Lister tous les tokens |
| `/api/tokens/:id` | GET | Obtenir un token |
| `/api/tokens` | POST | Créer un token |
| `/api/tokens/:id` | PUT | Mettre à jour un token |
| `/api/tokens/:id` | DELETE | Supprimer un token |
| `/api/tokens/:id/reveal` | POST | Révéler un token |
| `/api/tokens/:id/revoke` | POST | Révoquer un token |

### Configurations

| Endpoint | Méthode | Description |
|----------|---------|-------------|
| `/api/configurations` | GET | Lister toutes les configurations |
| `/api/configurations/:id` | GET | Obtenir une configuration |
| `/api/configurations` | POST | Créer une configuration |
| `/api/configurations/:id` | PUT | Mettre à jour une configuration |
| `/api/configurations/:id` | DELETE | Supprimer une configuration |

### Audit

| Endpoint | Méthode | Description |
|----------|---------|-------------|
| `/api/audit/logs` | GET | Lister les logs d'audit |
| `/api/audit/logs/:id` | GET | Obtenir un log d'audit |
| `/api/audit/stats` | GET | Statistiques d'audit |

## Pages du Dashboard

### 1. Dashboard Principal

- Vue d'ensemble des secrets, tokens et configurations
- Alertes de sécurité
- Statistiques d'utilisation
- Graphiques de tendance

### 2. Secrets

- Liste de tous les secrets
- Recherche et filtrage
- Création, édition, suppression
- Révélation des secrets
- Expiration et révocation

### 3. Tokens

- Liste de tous les tokens
- Recherche et filtrage
- Création, édition, suppression
- Révélation des tokens
- Expiration et révocation

### 4. Configurations

- Liste de toutes les configurations
- Recherche et filtrage
- Création, édition, suppression
- Validation des configurations

### 5. Audit Logs

- Liste des logs d'audit
- Filtrage par action, utilisateur, date
- Recherche dans les logs
- Export des logs

### 6. Settings

- Configuration de l'application
- Gestion des utilisateurs
- Paramètres de sécurité
- Intégrations externes

## Sécurité

### Authentification

- OAuth2 / JWT pour l'authentification
- Refresh tokens pour la persistance
- Session timeout configurable

### Chiffrement

- Chiffrement AES-256 pour les secrets stockés
- Hashage bcrypt pour les mots de passe
- Chiffrement TLS pour les communications

### Audit

- Logs d'audit pour toutes les actions
- Notification d'alertes de sécurité
- Rapports d'audit réguliers

### Limitations

- Masquage des secrets dans l'interface
- Logs d'activité pour chaque action
- Limitation du nombre de révélations par secret/token

## Intégrations

### Hermes Desktop

- Intégration avec la configuration Hermes Desktop
- Synchronisation des secrets et tokens
- Validation des configurations

### Baserow

- Intégration avec Baserow pour les données de Life OS
- Synchronisation des domaines et métriques
- Validation des données

### Obsidian

- Intégration avec Obsidian pour la documentation
- Synchronisation des notes
- Validation des liens

### Plane

- Intégration avec Plane pour la gestion de projet
- Synchronisation des tâches
- Validation des données

## Configuration

### Variables d'Environnement

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/aspace_dashboard

# JWT
JWT_SECRET=your-secret-key
JWT_EXPIRES_IN=7d

# OAuth2
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret

# Email (optionnel)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-email-password

# Security
BCRYPT_ROUNDS=12
AES_KEY=your-aes-key
```

### Docker Compose

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: aspace_dashboard
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build: ./backend
    environment:
      DATABASE_URL: postgresql://user:password@postgres:5432/aspace_dashboard
      JWT_SECRET: your-secret-key
      JWT_EXPIRES_IN: 7d
      GOOGLE_CLIENT_ID: your-google-client-id
      GOOGLE_CLIENT_SECRET: your-google-client-secret
    ports:
      - "3000:3000"
    depends_on:
      - postgres

  frontend:
    build: ./frontend
    environment:
      NEXT_PUBLIC_API_URL: http://localhost:3000
    ports:
      - "3001:3000"
    depends_on:
      - backend

volumes:
  postgres_data:
```

## Déploiement

### VPS (Production)

```bash
# Cloner le repository
git clone https://github.com/your-repo/aspace-dashboard.git
cd aspace-dashboard

# Configurer les variables d'environnement
cp .env.example .env
nano .env

# Construire et démarrer
docker-compose up -d

# Configurer le reverse proxy (Nginx)
sudo nano /etc/nginx/sites-available/aspace-dashboard
```

### Configuration Nginx

```nginx
server {
    listen 443 ssl http2;
    server_name aspace-dashboard.148.230.92.235.sslip.io;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Accès

### URL

- **Production**: https://aspace-dashboard.148.230.92.235.sslip.io/tokens
- **Développement**: http://localhost:3001

### Authentification

- Connexion via Google OAuth2
- JWT tokens pour l'authentification API
- Session timeout configurable

## Maintenance

### Sauvegardes

- Sauvegardes automatiques quotidiennes
- Sauvegardes manuelles sur demande
- Sauvegardes chiffrées

### Mises à jour

- Mises à jour automatiques
- Mises à jour manuelles
- Rollback en cas d'échec

### Monitoring

- Logs d'activité
- Alertes de sécurité
- Statistiques d'utilisation

## Références

- `10_Tech_OS/12_Blueprints/01-SDD/SDD-009_dashboard-governance.md` — SDD Dashboard de Gouvernance
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/concepts/concept_dashboard.md` — Concept Dashboard
- `CLAUDE.md` — Context7 Boundary pour L0 Tech OS