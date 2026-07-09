Volume du code source : 16 462 lignes (src/) + ~70K Agent Portal composants

Version courante : 0.9.x (The Nexus Convergence — Agent Portal Alpha, Phase C en cours)

V0.9	The Nexus Convergence	Agent Portal Alpha (Poste de Commandement Unifié)	🔧 En Cours

---

## 7.3 V0.9 — "The Nexus Convergence" (Agent Portal Profond)

### 7.3.1 Vision Stratégique
L'Agent Portal V0.9 est la **convergence** entre le prototype **ClaudeClaw Agent** (UI haute-fidélité, 17 composants, standalone) et le **Web OS souverain** (infrastructure IndexedDB/Zustand). L'objectif : un **poste de commandement total** capable d'orchestrer la Flotte à travers les dimensions temporelles (Crons), spatiales (Skill Tree) et exécutives (Scorecard), avec synchronisation temps-réel sur les données humaines (PARA, GTD, Ikigai, LD01-LD08).

### 7.3.2 Pipeline Spec-Driven V0.9 (Statut)
Document	Fichier	Statut
SDD	_SPECS/SDD/SDD-V0.9_AgentPortal_Nexus.md	✅ Rédigé (GravityClaw)
PRD	_SPECS/PRD/PRD-V0.9_AgentPortal_Product.md	✅ Rédigé (7 User Stories, 3 Phases)
ADR	_SPECS/ADR/ADR-V0.9_AgentPortal_Architecture.md	✅ Rédigé (3 décisions : Flat Root, LD-Nexus, Strategic Hub)
DDD	_SPECS/DDD/DDD-V0.9_AgentPortal_Execution.md	✅ Rédigé (3 étapes avec Build Gates)

### 7.3.3 Architecture du Portal (État Construit)
Le Portal intégré au Web OS est opérationnel en version V0.2.0 interne. Il réside dans :
`src/apps/agent-portal/`

**Layout Triple-Panel** (AgentPortalApp.tsx — 200 lignes) :
```
┌──────────────┬──────────────────────────────┬──────────────┐
│  SideNav     │  Main Content (Pepites)      │  AgentStats  │
│  (Frameworks │  ┌──────────────────────┐    │  (Armada     │
│   + Methods) │  │ Header (Pepite Nav)  │    │   Telemetry) │
│              │  ├──────────────────────┤    │              │
│              │  │ Active View:         │    │              │
│              │  │ - ScoreCard (default)│    │              │
│              │  │ - SkillsView         │    │              │
│              │  │ - CronsView          │    │              │
│              │  │ - RelationDiagram    │    │              │
│              │  │ - Framework Drilldown│    │              │
│              │  └──────────────────────┘    │              │
└──────────────┴──────────────────────────────┴──────────────┘
```

### 7.3.4 Composants Principaux (7 Core)
Composant	Fichier	Taille	Rôle
SideNav	components/SideNav.tsx	10 030 B	Navigation Frameworks + Methods + Footer stratégique
Header	components/Header.tsx	7 851 B	Sélecteur Pepites (Scorecard/Skills/Crons) + breadcrumbs
AgentStats	components/AgentStats.tsx	14 669 B	Panel Armada Telemetry (hiérarchie plate A0→A3)
SkillsView	components/SkillsView.tsx	13 210 B	Quantum Canvas SVG infini zoomable (Frameworks Tree)
CronsView	components/CronsView.tsx	6 023 B	Grille 7×24 d'orchestration Drones/automatisations
RelationDiagram	components/RelationDiagram.tsx	10 439 B	Diagramme de relations inter-Frameworks
AgentChatbot	components/AgentChatbot.tsx	8 064 B	Interface Chat IA intégrée au Portal

### 7.3.5 Dashboards Framework (9 portés depuis ClaudeClaw)
Dashboard	Fichier	Taille	Framework Cible
ScoreCard	dashboards/ScoreCard.tsx	11 015 B	Sprint Kanban (Todo/InProgress/Review/Done)
FrameworkOverview	dashboards/FrameworkOverview.tsx	8 710 B	Vue macro d'un Framework sélectionné
IkigaiPillars	dashboards/IkigaiPillars.tsx	13 985 B	USS Orville — Passion/Vocation/Mission/Profession
IkigaiHorizons	dashboards/IkigaiHorizons.tsx	20 929 B	USS Orville — H1/H3/H10/H30/H90
LifeWheelDomains	dashboards/LifeWheelDomains.tsx	16 923 B	USS Discovery — 8 Domaines de vie
TwelveWeekYear	dashboards/TwelveWeekYear.tsx	15 032 B	USS SNW — Vision/Planning/Process/Measurement/Time
ParaFramework	dashboards/ParaFramework.tsx	14 271 B	USS Enterprise — Projects/Areas/Resources/Archive
GtdFramework	dashboards/GtdFramework.tsx	14 967 B	USS Cerritos — Capture/Clarify/Organize/Reflect/Engage
DealFramework	dashboards/DealFramework.tsx	14 321 B	USS Protostar — Definition/Elimination/Automation/Liberation

### 7.3.6 Convergence ClaudeClaw → Web OS (Matrice de Portage)
La source de vérité pour la fidélité visuelle est le prototype `ClaudeClaw Agent` dans :
`20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/ClaudeClaw Agent/src/`

Composant CC Agent	Taille CC	Composant Web OS	Statut
Layout.tsx	8 040 B	AgentPortalApp.tsx	✅ Porté (adapté triple-panel)
SideNav.tsx	10 640 B	SideNav.tsx	✅ Porté
Header.tsx	3 762 B	Header.tsx	✅ Porté (enrichi Pepites)
AgentStats.tsx	16 840 B	AgentStats.tsx	✅ Porté
SkillsView.tsx	17 970 B	SkillsView.tsx	✅ Porté (Quantum Canvas)
CronsView.tsx	6 013 B	CronsView.tsx	✅ Porté
RelationDiagram.tsx	10 429 B	RelationDiagram.tsx	✅ Porté
AgentChatbot.tsx	8 048 B	AgentChatbot.tsx	✅ Porté
ScoreCard.tsx	9 176 B	dashboards/ScoreCard.tsx	✅ Porté (enrichi Sprint)
FrameworkOverview.tsx	8 694 B	dashboards/FrameworkOverview.tsx	✅ Porté
IkigaiPillars.tsx	13 969 B	dashboards/IkigaiPillars.tsx	✅ Porté
IkigaiHorizons.tsx	20 913 B	dashboards/IkigaiHorizons.tsx	✅ Porté
LifeWheelDomains.tsx	16 907 B	dashboards/LifeWheelDomains.tsx	✅ Porté
TwelveWeekYear.tsx	15 016 B	dashboards/TwelveWeekYear.tsx	✅ Porté
ParaFramework.tsx	14 255 B	dashboards/ParaFramework.tsx	✅ Porté
GtdFramework.tsx	14 951 B	dashboards/GtdFramework.tsx	✅ Porté
DealFramework.tsx	14 305 B	dashboards/DealFramework.tsx	✅ Porté

### 7.3.7 Pages Héritées (V0.1.8)
Page	Fichier	Lignes	Rôle
Dashboard V0.1.8	pages/Dashboard.tsx	157	Fleet Status + Neural Bridge Console + Task Injector

### 7.3.8 Plan de Développement V0.9 (Phases)

**Phase A — La Matrice de Commandement** (Layout + Armada)
- S-P-A-D 01 : Layout `AgentPortalApp.tsx` triple-panel ✅ Construit
- S-P-A-D 02 : Panel `Armada Telemetry` hiérarchie plate (A0→A3) ✅ Construit

**Phase B — Les Moteurs de Réalité** (Trinité Stratégique)
- S-P-A-D 03 : Port du `SkillsView` (Frameworks Tree / Quantum Canvas) ✅ Porté
- S-P-A-D 04 : Port du `CronsView` (Calendrier 7×24 d'orchestration) ✅ Porté
- S-P-A-D 05 : Port du `ScoreCard` (Kanban PARA synchronisé) ✅ Porté

**Phase C — Le Bridge Transversal** (Zustand/IndexDB)
- S-P-A-D 06 : Câblage des sélecteurs transversaux (Filtrage par LDxx) 🔧 En cours
- S-P-A-D 07 : Synchronisation `fw-deal.store` et `fw-wheel.store` (ROI) 🔧 En cours

### 7.3.9 Décisions Architecturales V0.9 (ADR)
ID	Décision	Justification
ADR-01	Flat Root Armada Panel	Tous les dossiers agents (A0, A1, A2) à la racine — accès One-Click pour l'OVERSEER
ADR-02	Transversal DB Routing (LD-Nexus)	Les agents Discovery (A3) mappés 1:1 sur LD01-LD08 (Book→LD01, Saru→LD02...)
ADR-03	Strategic Hub State Management	L'état `activePepite` est global au Portal — switch de vue sans perdre le filtre LDxx

### 7.3.10 Contrats TypeScript V0.9
typescript
// Armada Panel Context (ADR-01)
interface ArmadaTelemetryProps {
  allFolders: ArmadaFolder[];        // Dossiers à la racine (flat)
  activeAgentId: string | null;
  groups: { label: string; ids: string[] }[];  // Cadres visuels (A1, A2)
}

// Agent Entity (DDD)
interface Agent {
  name: string;
  role: string;
  status: 'Active' | 'Idle' | 'Busy';
  ld?: string;  // Domaine transversal (LD01-LD08)
}

// Armada Folder (DDD)
interface ArmadaFolder {
  id: string;
  label: string;
  icon: any;
  status: 'Active' | 'Idle' | 'Busy';
  agents: Agent[];
}

### 7.3.11 Métriques de Succès V0.9
Métrique	Cible	Statut
Zéro Latence (switch Pepites)	< 100ms	✅ Atteint (AnimatePresence mode="wait", transition 0.1s)
Zéro Dette TypeScript	tsc --noEmit clean	🔧 En cours
Wow Effect (fidélité ClaudeClaw)	1:1 avec prototype	✅ 17/17 composants portés
Volume de code Agent Portal	> 4000 lignes TSX	✅ ~200L layout + ~70K composants

---

Agent Portal	Flotte Stellaire	Amiral (A0 Overseer)
Ce document est un snapshot factuel. Il ne remplace pas les specs détaillées dans _SPECS/. Pour toute modification architecturale, consulter CONTRACTS.md en priorité.