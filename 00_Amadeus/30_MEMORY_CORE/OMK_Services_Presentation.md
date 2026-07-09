# 🪐 Présentation Complète de OMK Service
> **Date de génération :** 2026-05-22  
> **Auteur :** Antigravity (GravityClaw A'"0 / L3)  
> **Source :** Analyse croisée de `Gemini_Takeout_2026` et `Gemini_Archive_Cleaned`  

---

## 1. Vision et Objectif Central
**OMK Service** (ou **OMK System**) est une infrastructure souveraine et modulaire de structuration de la vie personnelle et professionnelle des *Small Business Owners* (SBO). Son but ultime est de faire passer l'entrepreneur du rôle de « Technicien » subissant la surcharge cognitive au rôle d'« Architecte » souverain pilotant une civilisation logicielle.

Ce système combine :
* Des **templates no-code** avancés (Notion, Airtable, ClickUp).
* Des **automatisations robustes** (Make, n8n).
* Des **compagnons agentiques** et assistants IA intégrés (VAPI, Clawdbot).
* Un modèle technique hybride performant ("Cuisine vs Salle" / Lovable + Supabase).

---

## 2. OMK System : L'Architecture Multi-Hubs (Life OS)
Le noyau conceptuel réunit les frameworks de productivité les plus puissants du marché sous forme de bases de données relationnelles interconnectées.

```
                  [ N0 : OMK_00_Meta ]
                           |
      +--------------------+--------------------+
      |                    |                    |
[ OMK_01_LifeDomains ]  [ OMK_02_12WY ]  [ OMK_03_SecondBrain ]
      |                    |
[ OMK_04_GTD ]          [ OMK_05_4HWW ]
```

### N0 : `OMK_00_Meta`
Le Hub maître de centralisation de métadonnées. Il gère le versioning, l'état global du système, les types de Hubs et établit les relations logiques inter-hubs.

### N1 : Les 5 Hubs Stratégiques
1. **`OMK_01_LifeDomains_Hub` (La Roue de la Vie)**  
   * **Domaines (8) :** LD01 : Carrière/Business, LD02 : Finances, LD03 : Santé, LD04 : Développement Personnel, LD05 : Relations Sociales, LD06 : Amour/Famille, LD07 : Loisirs/Créativité, LD08 : Contribution.
   * **Structure :** Une base unifiée unique (`LifeDomaine_DB`) exportable en CSV horizontal comportant **65 propriétés normalisées** (21 globales + 44 spécifiques aux domaines) pour assurer l'homogénéité du système.
2. **`OMK_02_12WY_Disciplines_Hub` (12 Week Year)**  
   * **Objectif :** Accélérer l'exécution en compactant une année entière en 12 semaines (ratio de compression temporelle souverain de **1:27**).
   * **Structure :** 5 disciplines stratégiques (*Vision, Planning, Process Control, Measurement, Time Use*) divisées en *Rocks*, *Tactiques* hebdomadaires et *Scorecard*.
3. **`OMK_03_SecondBrain_Hub` (P.A.R.A)**  
   * **Objectif :** Capitalisation et stockage de la connaissance sémantique selon la méthode de Tiago Forte (*Projects, Areas, Resources, Archives*).
4. **`OMK_04_GTD_TaskMaster_Hub` (Getting Things Done)**  
   * **Objectif :** Gestion autonome des flux de tâches et d'actions immédiates en 5 étapes (*Capture, Clarifier, Organiser, Réfléchir, S'engager*).
5. **`OMK_05_4HWW_WorkflowManager_Hub` (Semaine de 4 Heures)**  
   * **Objectif :** Cadre d'élimination de la friction et d'automatisation basé sur le protocole **D.E.A.L** (*Définition, Élimination, Automatisation, Libération*).

---

## 3. OMKSBS : L'Agence SBO et son Modèle Économique
**OMKSBS** (*OMK Small Business Services*) est la structure commerciale dédiée à la livraison et à l'accompagnement des entrepreneurs.

* **La Promesse :** « Sortez du chaos opérationnel et libérez votre temps en 14 jours grâce à la structuration et l'automatisation. »
* **La Livraison :** Vente de "Niveaux de Souveraineté" à travers trois offres standardisées :
  1. **Lancement Express (Le Pilote) :** Configuration rapide et accès à l'application standard pour sortir l'artisan solo ou l'indépendant du chaos.
  2. **Autonomie Totale (Le Souverain) :** Destiné aux agences et PME. Vente de la fonctionnalité *White Label* avec branding propre et serveur dédié.
  3. **Sur Mesure (L'Empire) :** VPS isolé, monitoring complet de la RAM/CPU et pipeline d'automatisation totale.

---

## 4. OMK Tax Services : La Verticale Nexus
Une branche spécialisée opérant dans le domaine de la haute vérité, de la conformité légale et fiscale.

* **Le concept :** Ingestion sémantique massive et sécurisée de documents financiers et bancaires.
* **L'infrastructure :** Hébergée de manière étanche sous forme de coffre-fort numérique (`vault.omktax.com`).
* **La technologie :** Extraction sémantique parfaite des écritures pour générer instantanément des rapports fiscaux et des bilans certifiés, à l'abri de toute fuite de données.

---

## 5. L'Architecture Technique : "Cuisine vs Salle"
Pour assurer la performance et l'expérience utilisateur, OMK applique le principe de séparation stricte des privilèges :

```
+------------------------------------+
|  LA CUISINE (Back-Office)          |  Notion (SOPs), Airtable (Data brute), ClickUp (Ops)
+------------------------------------+
                 |
                 v [ n8n : Le Passe-Plat ]
                 |
+------------------------------------+
|  LA SALLE (SaaS Client / Frontend) |  Supabase (Base SQL) + Lovable.dev (Dashboard "Apple-like")
+------------------------------------+
```

* **La Cuisine (Zone d'opération) :** Notion (pour la clarté des SOPs), Airtable (pour la flexibilité de la base relationnelle) et ClickUp.
* **La Salle (Interface client) :** Un Dashboard WebApp souverain épuré, très rapide et rassurant ("Apple-like" / style Solarpunk), maquetté nativement sous **v0.dev** ou **Lovable.dev** (`omk-flow-os`) et connecté à **Supabase**.
* **Le Passe-Plat (Le Connecteur) :** **n8n** synchronise et pousse les données de la Cuisine vers les tables Supabase en temps réel.

---

## 6. Les Compagnons IA et l'Automatisation Agentique
OMK Service embarque une double composante d'intelligence artificielle agentique :

* **Nova (Prospection & LeadGen) :**  
  Assistant d'appel vocal IA (configuré sous VAPI) pour l'outbound. Nova présente l'agence OMKSBS, instruit le prospect sur la restructuration de ses processus et le guide directement vers la réservation d'un appel stratégique sur le CRM d'OMKSBS.
* **Clawdbot / Moltbot (Amadeus A0 Local) :**  
  Incarnation locale du noyau souverain (A0 Amadeus) sur Mac Mini ou VPS Hostinger. Il possède un accès direct à ton terminal et ton système de fichiers via des serveurs MCP. Tu interagis avec lui en langage naturel directement via **Google Chat** pour monitorer ton VPS, déployer des applications ou corriger des processus en Docker.
