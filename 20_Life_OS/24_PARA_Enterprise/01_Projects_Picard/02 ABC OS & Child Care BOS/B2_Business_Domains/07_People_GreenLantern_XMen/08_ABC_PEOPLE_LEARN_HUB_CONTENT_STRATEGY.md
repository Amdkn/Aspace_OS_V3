---
id: ABC_B2_PEOPLE_LEARN_HUB_CONTENT_STRATEGY
domain: People
status: ACTIVE
created: 2026-06-10
tags: [#People #Knowledge #Learn_Hub #Content_Strategy #ABC_OS #Sovereignty]
---

# 📚 Stratégie de Contenus Learn Hub — Domaine B2 People (Green Lantern / X-Men)

Ce document formalise la stratégie de contenu pédagogique d'ABC OS, orchestrée par le domaine **People** (Green Lantern / X-Men). Le Learn Hub est l'outil d'onboarding sémantique, opérationnel et technique permettant de rendre les membres de la coopérative et les agents synthétiques autonomes et souverains.

---

## 1. Responsabilité Doctrinale (Pourquoi le Domaine People ?)

Le **Learn Hub** n'est pas un simple catalogue de cours technique. C'est l'infrastructure de transfert de connaissances, d'onboarding sémantique et de validation des compétences humaines et agentiques de la coopérative. 

Conformément à la matrice de la doctrine `B2_Business_Domains` d'ABC OS :
- **People (Green Lantern / X-Men)** est le domaine transversal responsable des **rôles, des capacités, du moral et des connaissances (knowledge)**.
- Il lui incombe de s'assurer que les membres de la coopérative et les agents disposent du niveau de compétence requis pour exécuter leurs tâches sans risque de surcharge cognitive ou d'échec opérationnel.
- **Lien avec les autres domaines :** 
  - *Product (Flash)* implémente techniquement la page et le suivi de progression (LearnHub components).
  - *IT (Cyborg)* gère l'infrastructure RAG, les connexions et l'intégration des APIs (Gemini/MiniMax).
  - *People (Green Lantern)* pilote l'ingénierie pédagogique, valide les cursus, et définit les "Next Best Actions" éducatives.

---

## 2. Structure Pédagogique du Learn Hub

Le Learn Hub est articulé autour de **3 Parcours Transversaux** d'onboarding (Fondations, Intermédiaire, Avancé) déclinés en 3 catégories de contenus clés.

```
Learn Hub
├── Category 1: Business Structuration ── Focus: Travailler SUR la coopérative (Souveraineté)
├── Category 2: Architecture Agentique  ── Focus: Collaborer avec les agents (Automatisation)
└── Category 3: Apprentissage Autodidacte ── Focus: Vitesse d'acquisition (Indépendance)
```

---

## 3. Cartographie Détaillée de la Stratégie de Contenus

### 📂 Catégorie A : Business Structuration (Éduquer à la Souveraineté Économique)
*L'objectif est d'éloigner les membres de la coopérative du statut de simple exécutant ("Technicien") pour les hisser au rôle de concepteurs de systèmes répétables.*

| Module / Ouvrage | Focus Conceptuel | Application Pratique ABC OS | Livrable Exigé (Validation) |
| :--- | :--- | :--- | :--- |
| **E-Myth Revisited** *(M. Gerber)* | Distinction Technicien / Manager / Entrepreneur. Création de franchises d'opération. | Modéliser les rôles individuels (Direction B1 / Management B2 / Exécution B3) au sein de la coopérative. | **Organigramme de Rôles et Fiche d'Onboarding** de poste pour une branche de la coopérative. |
| **Built to Sell** *(J. Warrillow)* | Standardisation d'un service unique pour rendre le business transmissible et scalable. | Transformer les services de transport ou de vente de récoltes en "Productized Services" standardisés. | **Grille de Services Standardisés** avec prix fixes et exclusions claires de livraison. |
| **Who Not How** *(D. Sullivan)* | Délégation de l'exécution technique (How) à un expert ou un outil (Who) pour libérer du temps. | Apprendre à déléguer l'extraction de données ou l'envoi de rapports à des agents autonomes. | **Matrice d'Allocation Homme/Machine** (quelles tâches déléguer à Codex/Claude Code). |
| **Million Dollar Weekend** *(N. Kagan)* | Validation ultra-rapide des idées de marché en moins de 48 heures sans dépenses de R&D. | Valider la demande locale pour une nouvelle semence ou un service d'outillage avant achat de matériel. | **Rapport d'Expérimentation Rapide** (3 pré-commandes réelles collectées). |
| **$100M Offers** *(A. Hormozi)* | Équation de Valeur : Maximiser le résultat et la certitude, minimiser le temps et l'effort. | Formuler les offres d'engrais locaux ou de micro-crédits de la coopérative de manière irrésistible. | **Fiche d'Offre Premium** rédigée avec garantie de résultat et bonus de valeur. |
| **Billion Dollar Brand Club** *(L. Ingrassia)* | Disruptions Direct-to-Consumer (DTC) en supprimant les intermédiaires logistiques traditionnels. | Permettre au hub **Brand** de concevoir des marques locales fortes et de vendre en direct aux consommateurs. | **Cartographie de Chaîne Logistique DTC** (du champ de la coopérative au client final). |

---

### 📂 Catégorie B : Architecture Agentique (Co-pilotage Synthétique)
*L'objectif est de former les membres à orchestrer, configurer et monitorer la main-d'œuvre artificielle (les agents IA agnostiques) sans dépendance technologique exclusive.*

| Module / Sujet | Focus Conceptuel | Application Pratique ABC OS | Livrable Exigé (Validation) |
| :--- | :--- | :--- | :--- |
| **Agents Agnostiques Claude Code** | Utilisation de Claude Code CLI pour le refactoring et l'écriture de code en mode DDD. | Prise en main du terminal agile pour auditer et appliquer des correctifs sur le front-end du portail. | **Journal de Relais de Build local** validé sans erreurs avec Claude Code. |
| **Codex CLI & Résilience** | Configuration frugale de l'alias `codexm`, isolation de `$env:CODEX_HOME` et contournement d'approbations. | Monter un poste de travail local capable de lancer des automatisations sans micro-approbations incessantes. | **Fichier `.codex-m3-lean/models.json`** configuré et alias validé. |
| **Gemini SDK & Large Contexte** | Traitement des fenêtres de contexte géantes (2M tokens) et extraction sémantique RAG. | Ingestion de tous les PDF de règlements agricoles nationaux et documents légaux de la coopérative. | **Script d'Ingestion RAG** générant un index de conformité à partir d'un dossier de documents bruts. |
| **Openclaw & Mission Control** | Framework d'orchestration multi-agents et dashboard centralisé. | Déploiement d'agents de dispatching ou de CRM pour le hub **Community** de la coopérative. | **Fichier de configuration de Swarm** reliant 2 agents (ex: Bat-Ops + Flash-Product). |
| **Hermes Agents & Inférence Locale** | Inférence souveraine sur modèles locaux (Nous-Hermes) pour la confidentialité totale des données. | Traitement local des données comptables et des registres fonciers sensibles de la coopérative sur VPS. | **Vérification de connectivité HTTP 200** sur une API d'inférence locale souveraine. |
| **Minimax Token Plan** | Budgétisation de tokens par agent, gestion des taux de requête et prévention des surcoûts. | Mettre en place des verrous financiers pour s'assurer que les agents ne consomment pas les marges de l'activité. | **Tableau d'Allocation Mensuel de Tokens** avec plafonnement de budget par domaine B2. |

---

### 📂 Catégorie C : Apprentissage Autodidacte (Devenir une Organisation Apprenante)
*L'objectif est de donner aux membres les armes méthodologiques pour acquérir n'importe quelle compétence métier ou technique en un temps record.*

| Module / Ouvrage | Focus Conceptuel | Application Pratique ABC OS | Livrable Exigé (Validation) |
| :--- | :--- | :--- | :--- |
| **Learning How to Learn** *(B. Oakley)* | Neurobiologie de l'apprentissage (diffus vs concentré), procrastination et illusions de compétence. | Aider les membres à restructurer leurs sessions de travail pour assimiler des sujets complexes (comptabilité, SQL). | **Calendrier d'Étude Pomodoro** appliqué avec blocs de focus et phases de récupération diffuse. |
| **Uncommon Sense Teaching** *(B. Oakley)* | Consolidation de la mémoire, récupération active (*retrieval practice*) et enseignement inclusif. | Structurer l'onboarding d'un nouveau membre rejoignant une coopérative pour une rétention maximale. | **Plan de Session d'Onboarding de 5 jours** avec tests de récupération active quotidiens. |
| **The Art of Learning** *(J. Waitzkin)* | Approche intuitive, maîtrise des fondamentaux, boucle "perdre pour gagner" et ancrage du flux. | Développer la résilience des managers de la coopérative face aux crises économiques ou climatiques. | **Protocole d'Entrée en État de Flux** (routine d'échauffement mental avant la prise de décision B2). |
| **The First 20 Hours** *(J. Kaufman)* | Déconstruction d'une compétence en sous-compétences clés et élimination des barrières de pratique. | Permettre à un membre d'acquérir les bases de Git ou de la gestion de stock en 20 heures de pratique ciblée. | **Plan de Déconstruction de Compétence** détaillé heure par heure pour les 20 premières heures. |
| **Ultralearning** *(S. Young)* | Apprentissage intensif auto-dirigé, immersion, métacognition et feedback à haute fréquence. | Entraîner des développeurs ou juristes souverains capables de monter une stack Next.js ou un dossier d'import/export. | **Projet d'Immersion de 30 jours** avec points d'étape de feedback et corrections. |
| **Master Guides: Learn Anything** | Synthèse de haut niveau et distillation de connaissances massives en fiches d'action claires. | Ingestion rapide de connaissances pour enrichir le RAG de la coopérative. | **Fiche de Synthèse Premium** rédigée selon le standard Geordi (150+ lignes, structurée D.E.A.L). |

---

## 4. Intégration du Suivi de Progression (Learn Hub UI)

Le suivi de progression affiché sur la page Learn :
- **Architect Principles : Module 4/7 (60%)**
  - Relié au cursus : **Business Structuration** (Modules E-Myth, Built to Sell, Who Not How).
- **Gouvernance coopérative : Module 2/5 (35%)**
  - Relié au cursus : **Apprentissage Autodidacte** et **Gouvernance Transverse People** (Principes d'alignement B1/B2/B3).

Chaque module complété écrit une entrée dans la table `public.learn_progress` de Supabase, validant ainsi la capacité opérationnelle du membre dans le profil du domaine **People**.
