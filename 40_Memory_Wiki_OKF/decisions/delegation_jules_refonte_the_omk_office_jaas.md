---
type: Decision
title: Delegation Jules — Refonte Multi-Tenant & Back-Office The OMK Office
description: Lancement de la session d orchestration autonome Jules #9673642540723156850 sur The-OMK-Office-V1-JaaS-Landing-Site-Web.
tags: [jules, delegation, jaas, omk-office, multi-tenant, agency-garden, coursera-portal]
generated: { by: antigravity, at: 2026-09-09T03:41:00Z }
verified:
  - { by: human:amdkn, at: 2026-09-09T03:41:00Z }
sources:
  - id: target-repo
    resource: "https://github.com/Amdkn/The-OMK-Office-V1-JaaS-Landing-Site-Web.git"
    author: human:amdkn
    last_modified: 2026-09-09
okf_version: "0.2"
---

# Delegation Jules — Refonte Multi-Tenant & Back-Office The OMK Office

## 1. Contexte & Diagnostic de la Dette
- **Origine** : Prototype genere sous Google AI Studio ayant compresse la Landing Page et les ecrans Back-Office dans un flux unique non cloisonne.
- **Repository Cible** : `Amdkn/The-OMK-Office-V1-JaaS-Landing-Site-Web`.

## 2. Actions Realisees par Antigravity (Chef d Orchestre)
1. Synchronisation locale sous `C:\\Users\\amado\\The-OMK-Office-V1-JaaS-Landing-Site-Web`.
2. Creation du dossier de delegation canonique `delegation-a-jules/` avec `PRD-MultiTenant-Auth-BackOffice-Garden.md` et `README.md`.
3. Push sur GitHub `main` (commit `0c5ada3`).
4. Declenchement de la session Jules autonome (Session ID : `9673642540723156850`).

## 3. Specifications Deleguees
- Sas de connexion/inscription (`AuthModal.tsx` / `AuthPage.tsx`).
- Back-Office Staff & Administrateur inspire de `00-AaaS-Agency-Garden` (Kanban, suivi des dossiers, RLS).
- Portail Client Apprenant guide par etapes inspire de plateformes type Coursera/Udemy.
- Validation automatique `tsc` par Jules avant emission de la Pull Request.