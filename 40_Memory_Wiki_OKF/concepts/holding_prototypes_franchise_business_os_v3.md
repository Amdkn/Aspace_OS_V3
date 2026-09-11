---
type: Concept
title: Holding de Prototypes de Franchise — Matrice V2/V3 (Picard, Spock, Geordi)
description: Cadre d'unification et de distillation de Business OS en une holding de prototypes de franchise multi-locataires (OMK, ABC OS, Marina, Alikaly, Rilcot) opérant sur le runtime Coach OS V3.
tags: [business-os, franchise, holding, picard, spock, geordi, okf, v3-migration]
generated: { by: gemini-pro, at: 2026-09-11T05:43:00Z }
verified:
  - { by: human:amdkn, at: 2026-09-11T05:43:00Z }
sources:
  - id: v2-h10-projects
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects"
    author: system:aspace-os-v2
    last_modified: 2026-08-19
  - id: v2-picard-projets
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard"
    author: system:aspace-os-v2
    last_modified: 2026-08-30
  - id: v2-spock-canon
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/franchise"
    author: system:aspace-os-v2
    last_modified: 2026-08-30
  - id: script-franchise-v3
    resource: "C:/Users/amado/ASpace_OS_V3/scripts/franchise_ownerbooks.py"
    author: human:amdkn
    last_modified: 2026-08-30
okf_version: "0.2"
---

# Holding de Prototypes de Franchise — Matrice V2/V3

## 1. Vision et Problématique Résolue

Dans l'architecture V2 (`24_PARA_Enterprise`), les initiatives entrepreneuriales étaient fragmentées en trois couches :
1. **01_Projects_Picard (La Forge Lourde) :** 485 000 fichiers (10,74 Go), saturés de `node_modules`, builds et dépôts imbriqués, mais abritant les véritables répertoires doctrinaux (`01-omk-business-os`, `02 ABC OS`, `03 RILCOT`, `04 Alikaly`, `05 Marina`).
2. **02_Areas_Spock (Le Canon Perpétuel) :** Le standard invariable de franchise (`B0_Self_Operating_Business_Doctrine/franchise/`), articulé autour des 3 Triptyques (T1 People/Ops/Product, T2 Growth/Sales/Finance, T3 Legal/R&D) et des 8 domaines B2 / 8 escouades B3.
3. **03_Resources_Geordi / 30_Business_OS / 10_Projects (La Couche de Dispatch Relocalisée) :** Une collection de 10 dossiers projets où les jonctions NTFS (`_doctrine`) vers Picard s'étaient en partie rompues ou figées sous forme de dossiers réels.

**Le Pivot V3 : La Holding de Prototypes de Franchise.**
Au lieu de maintenir 5 ou 10 codebases dispersées qui dupliquent le shell OS, A'Space OS V3 fédère toutes ces expérimentations au sein d'une **Holding de Franchises Multi-Tenants** hébergée dans le cockpit applicatif vivant `coach-os-app` (port 5174).

---

## 2. État des Lieux Mesuré des Jonctions et Doctrines (10 Projets H10)

L'audit physique approfondi de `03_Resources_Geordi/.../30_Business_OS/10_Projects` révèle la topologie exacte suivante :

| Projet H10 | Jonction NTFS `_doctrine` | Cible Réelle dans Picard | Doctrine Présente / Statut | Mode Franchise Lu (North Star) |
|---|---|---|---|---|
| **omk** | `JUNCTION` OK | `01_Projects_Picard/01-omk-business-os` | Complète (T1/T2/T3, chartes, runbooks) | **Prototype Fondateur** (Nexus + US Coach) |
| **abc** | `JUNCTION` OK | `01_Projects_Picard/02 ABC OS & Child Care BOS` | Complète (B1 Direction, B2 Domaines, B3) | **Orbiter + Compliance** (Coopérative & Garderie) |
| **marina** | `JUNCTION` OK | `01_Projects_Picard/05 marina Cleaning BOS & SOP` | Complète (B1 Direction, B2 Domaines, B3) | **Orbiter primary, Nexus secondary** (Cleaning BOS) |
| **alikaly** | `JUNCTION` OK | `01_Projects_Picard/04 Alikaly Bana Holding to LLC` | Complète (B1 Direction, B2 Domaines, B3) | **Nexus + Finance/Legal** (Holding to LLC) |
| **rilcot** | `JUNCTION` OK | `01_Projects_Picard/03_RILCOT_Members_Space_OS` | Complète (B1 Direction, B2 Domaines, B3) | **Nexus + Community Ops** (Espace Membres) |
| **ceo-desktop** | `REAL_DIR` (Divergence) | `None` (dossier local figé) | Partielle (B1/B2/B3 sans runbooks) | Shell Desktop Expérimental |
| **solaris** | `MISSING` (Rompue) | `None` (dossier `_doctrine` absent) | Absente (`_pulse.log` résiduel, apps vides) | Ingestion Registre W111 / Sources |
| **cerritos-gtd-dispatch** | `MISSING` (Rompue) | `None` (dossier `_doctrine` absent) | Absente (Plans GTD locaux, app spock-wf0) | Dispatch GTD W108 |
| **wargames** | `MISSING` (Rompue) | `None` (dossier `_doctrine` absent) | Absente (Simulations Mirofish Markdown) | Études Stratégiques Sob |
| **graphify-out** | `MISSING` (Rompue) | `None` (dossier `_doctrine` absent) | Graphe statique HTML/JSON | Artefact de cartographie visuelle |

### Constat d'Intégrité :
- **Le noyau des 5 vraies franchises (`omk`, `abc`, `marina`, `alikaly`, `rilcot`) possède 100% de ses doctrines intactes**, reliées sans perte à Picard.
- Les autres dossiers (`solaris`, `cerritos`, `ceo-desktop`, `wargames`) n'étaient pas des entreprises complètes mais des briques transversales (GTD, graphes, audits) ou des modules de support.

---

## 3. Architecture Canonique de Franchise (Spock & OMK)

Chaque franchise de la holding s'articule autour des **3 Triptyques invariants** :

1. **T1 — People / Ops / Product (Le Mur Porteur) :**
   - **B2 Dirigeants :** Green Lantern (RH Méta) + Batman (Opérations/SOP) + Flash (Produit/Agences).
   - **B3 Escouades :** X-Men (Recrutement, Onboarding) + Fantastic Four (SOPs, Process) + Avengers (Spécifications).
   - **Rôle :** Construit l'actif vendable. Tout SOP répété devient une Skill.

2. **T2 — Growth / Sales / Finance (Le Moteur Économique) :**
   - **B2 Dirigeants :** Superman (Acquisition/Growth) + John Jones (Offre/Vente) + Wonder Woman (Trésorerie/Finance).
   - **B3 Escouades :** Guardians of the Galaxy + Illuminati + Thunderbolts.
   - **Rôle :** Monétisation, conversion, facturation et distribution de dividendes.

3. **T3 — Legal & Compliance / R&D (Le Bouclier & la Vigie) :**
   - **B2 Dirigeants :** Aquaman (Juridique & RGPD) + Cyborg (R&D & IT).
   - **B3 Escouades :** Eternals + Kang Dynasty.
   - **Rôle :** Conformité dès la conception (365 jours) et absorption des innovations de pointe.

---

## 4. Stratégie de Migration V3 : L'Usine à Franchises Multi-Tenants

Pour respecter la loi **L0 (Rick)** et l'anti-dette structurelle, la migration vers V3 applique le protocole suivant :

```
[V2 Picard & Geordi Doctrines]
        │
        ▼ (Filtrage sémantique & exclusion de 10 Go de node_modules)
[50_Distillation/projets/] ──> [40_Memory_Wiki_OKF/concepts/] (Certification OKF)
        │
        ▼
[Coach OS V3 Template Reproductible (30_Business_OS/10_Projects/coach-os-app)]
        │
        ├── Tenant 1 : OMK Nexus Premium (US Coach / Mid-Market B2B)
        ├── Tenant 2 : ABC OS & Child Care BOS (Coopérative & Garderie)
        ├── Tenant 3 : Marina Cleaning BOS & SOP (Services Entretien B2B/B2C)
        ├── Tenant 4 : Alikaly Bana Holding to LLC (Holding Foncière & Patrimoniale)
        └── Tenant 5 : RILCOT Members Space OS (Communauté & Espace Membres)
```

### Règles d'or d'exécution :
1. **Zéro Copie Brutale :** Ne jamais copier `apps/` ou les builds obsolètes de V2. Seules les chartes, Ownerbooks, Runbooks et manifestes entrent dans `50_Distillation/`.
2. **Tenant Configuration Déterministe :** Chaque franchise devient un profil `ORG.json` / `tenant.config.json` dans l'application `coach-os-app`.
3. **Ségrégation des Rôles :**
   - `02_Areas_Spock` reste le modèle universel abstrait.
   - Les projets instancient ce modèle avec un `mode_franchise` et un `icp` ciblés.
   - L'interface unique `http://localhost:5174` bascule dynamiquement d'une franchise à l'autre via le sélecteur d'organisation (Multi-Tenant Workspace).
