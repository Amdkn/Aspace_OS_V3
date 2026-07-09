|# SDD-009 — Dashboard de Gouvernance d'Infrastructure

> Layer: L0 Tech OS
> A2: 13th Doctor — Manager of Infra
> Date: 2026-06-04
> Status: PLANNED

## Wishlist

Créer un Dashboard de Gouvernance d'Infrastructure centralisé pour A'Space OS V2 qui permet de :

1. **Gérer les secrets** : Stocker, chiffrer, révéler et révoquer tous les secrets (tokens, API keys, passwords)
2. **Gérer les tokens** : Créer, éditer, supprimer et révoquer tous les tokens (Telegram, Discord, etc.)
3. **Gérer les configurations** : Stocker, valider et synchroniser toutes les configurations de l'application
4. **Auditer les actions** : Enregistrer tous les actions effectuées sur les secrets, tokens et configurations
5. **Surveiller l'infrastructure** : Visualiser l'état de l'infrastructure et détecter les anomalies

## Specs

### Spécification Technique

**Stack Technique** :
- Frontend: React / Next.js
- Backend: Node.js / Express
- Base de données: PostgreSQL
- Authentification: OAuth2 / JWT
- Sécurité: Hashage bcrypt, chiffrement AES-256

**Architecture** :
```
┌─────────────────────────────────────────────────────────────┐
│                     Dashboard de Gouvernance                 │
├─────────────────────────────────────────────────────────────┤
│  Frontend (Next.js)                                          │
│  ├─ Dashboard Principal                                      │
│  ├─ Secrets Management                                       │
│  ├─ Tokens Management                                        │
│  ├─ Configurations Management                                │
│  ├─ Audit Logs                                               │
│  └─ Settings                                                 │
├─────────────────────────────────────────────────────────────┤
│  Backend (Express)                                           │
│  ├─ Auth API                                                 │
│  ├─ Secrets API                                              │
│  ├─ Tokens API                                               │
│  ├─ Configurations API                                       │
│  └─ Audit API                                                │
├─────────────────────────────────────────────────────────────┤
│  PostgreSQL Database                                         │
│  ├─ secrets (table)                                          │
│  ├─ tokens (table)                                           │
│  ├─ configurations (table)                                   │
│  └─ audit_logs (table)                                       │
└─────────────────────────────────────────────────────────────┘
```

### Spécification Fonctionnelle

**1. Authentification**
- Connexion via Google OAuth2
- JWT tokens pour l'authentification API
- Session timeout configurable (15 min)
- Refresh tokens pour la persistance

**2. Gestion des Secrets**
- Créer, éditer, supprimer des secrets
- Révéler les secrets (masqués par défaut)
- Révoquer les secrets expirés
- Configurer l'expiration des secrets
- Catégoriser les secrets (API, Database, etc.)
- Environnement (dev, staging, prod)

**3. Gestion des Tokens**
- Créer, éditer, supprimer des tokens
- Révéler les tokens (masqués par défaut)
- Révoquer les tokens expirés
- Configurer l'expiration des tokens
- Catégoriser les tokens (Telegram, Discord, etc.)
- Environnement (dev, staging, prod)

**4. Gestion des Configurations**
- Créer, éditer, supprimer des configurations
- Valider les configurations
- Synchroniser les configurations avec Hermes Desktop
- Catégoriser les configurations (App, Database, etc.)
- Environnement (dev, staging, prod)

**5. Audit Logs**
- Enregistrer toutes les actions (CRUD)
- Enregistrer les révélations de secrets/tokens
- Enregistrer les révocations
- Filtrer par action, utilisateur, date
- Exporter les logs

**6. Dashboard Principal**
- Vue d'ensemble des secrets, tokens et configurations
- Alertes de sécurité (secrets révélés, tokens expirés)
- Statistiques d'utilisation
- Graphiques de tendance

## Deliverables

### 1. Base de Données

- [ ] Schema PostgreSQL (secrets, tokens, configurations, audit_logs)
- [ ] Migrations
- [ ] Index pour les performances

### 2. Backend API

- [ ] Auth API (login, logout, refresh)
- [ ] Secrets API (CRUD, reveal, revoke)
- [ ] Tokens API (CRUD, reveal, revoke)
- [ ] Configurations API (CRUD, validate, sync)
- [ ] Audit API (logs, stats)
- [ ] Middleware d'authentification
- [ ] Middleware d'audit

### 3. Frontend

- [ ] Dashboard Principal
- [ ] Secrets Management
- [ ] Tokens Management
- [ ] Configurations Management
- [ ] Audit Logs
- [ ] Settings
- [ ] Authentification (Google OAuth2)
- [ ] Responsive design

### 4. Documentation

- [ ] README.md
- [ ] API Documentation (Swagger/OpenAPI)
- [ ] Guide d'utilisation
- [ ] Guide de déploiement
- [ ] Guide de sécurité

### 5. Déploiement

- [ ] Docker Compose
- [ ] Dockerfile (backend et frontend)
- [ ] Configuration Nginx
- [ ] Configuration SSL/TLS
- [ ] Scripts de déploiement

## Timeline

| Phase | Durée | Livrables |
|-------|-------|-----------|
| Phase 1: Planning | 1 jour | SDD, ADR |
| Phase 2: Database | 2 jours | Schema, Migrations |
| Phase 3: Backend | 5 jours | API, Middleware |
| Phase 4: Frontend | 7 jours | Dashboard, Auth |
| Phase 5: Intégration | 2 jours | Intégrations, Tests |
| Phase 6: Déploiement | 2 jours | Docker, Nginx, SSL |
| **Total** | **19 jours** | **Dashboard complet** |

## Risques

| Risque | Impact | Probabilité | Mitigation |
|--------|--------|-------------|------------|
| Sécurité des secrets | Haute | Moyenne | Chiffrement AES-256, audit logs |
| Performance de la base de données | Moyenne | Faible | Index, pagination |
| Intégration avec Hermes Desktop | Moyenne | Moyenne | Tests d'intégration |
| Déploiement sur VPS | Moyenne | Faible | Documentation détaillée |

## Success Criteria

- [ ] Dashboard accessible via https://aspace-dashboard.148.230.92.235.sslip.io/tokens
- [ ] Authentification via Google OAuth2 fonctionnelle
- [ ] Gestion complète des secrets (CRUD, reveal, revoke)
- [ ] Gestion complète des tokens (CRUD, reveal, revoke)
- [ ] Gestion complète des configurations (CRUD, validate, sync)
- [ ] Audit logs complets pour toutes les actions
- [ ] Dashboard principal avec statistiques et alertes
- [ ] Déploiement sur VPS avec SSL/TLS
- [ ] Documentation complète

## Context7 Boundary

No Context7 lookup is required to read or update this local handoff. Use Context7 before any live provider, plugin, API, MCP, or CLI configuration.

---

## Références

- `10_Tech_OS/11_Infra_13th_Doctor/00_Dashboard_Gouvernance.md` — Dashboard de Gouvernance
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/concepts/concept_dashboard.md` — Concept Dashboard
- `CLAUDE.md` — Context7 Boundary pour L0 Tech OS