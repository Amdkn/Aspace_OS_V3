|# Shadow Tools Guide — L1 Life OS

> Layer: L1 Life OS
> Date: 2026-06-04
> Status: ACTIVE

## Overview

L1 Life OS utilise 6 shadow tools différents pour gérer la mémoire, l'exécution et la structure. Ce guide documente les conventions d'utilisation pour chaque tool.

## Règle d'Or

**Une information n'a qu'un seul propriétaire.** Si dupliquée, c'est un pointeur (URL/ID), pas une copie.

---

## Ship 1: 21_Ikigai_Orville — Obsidian / Filesystem Knowledge Base

### Rôle
**Meaning Engine** — Structure de vie, objectifs, exécution quotidienne.

### Shadow Tool
**Obsidian** + **Filesystem** — Knowledge base locale

### Convention de Nommage

```
21_Ikigai_Orville/
├── 01_Pillars_Identity/
│   ├── 01_Profession_Mercer/
│   │   └── README.md
│   ├── 02_Mission_Grayson/
│   │   └── README.md
│   ├── 03_Passion_Malloy/
│   │   └── README.md
│   └── 04_Vocation_Finn/
│       └── README.md
└── 02_Horizons_Time/
    ├── 01_H1_Isaac/
    │   └── README.md
    ├── 02_H3_Lamarr/
    │   └── README.md
    ├── 03_H10_Bortus/
    │   └── README.md
    ├── 04_H30_Alara/
    │   └── README.md
    └── 05_H90_Klyden/
        └── README.md
```

### Convention de Fichier

Chaque A3 produit un fichier `README.md` avec :
- **Mission** : Rôle de l'A3
- **Handoff Protocol** : 5 étapes
- **Output** : Ce que l'A3 produit
- **Boundaries** : Ce que l'A3 ne fait pas
- **Spec** : Fichier de spécification

### Convention de Chemin

```
C:\Users\amado\ASpace_OS_V2\20_Life_OS\21_Ikigai_Orville\
├── 01_Pillars_Identity\
│   └── 01_Profession_Mercer\
│       └── README.md
└── 02_Horizons_Time\
    └── 01_H1_Isaac\
        └── README.md
```

### Convention de Handoff

Chaque handoff A2/A3 suit ce format :
```markdown
|# <Folder Name> - Handoff <A2/A3>

> Layer: L1 Life OS
> Parent A2: <Parent A2 Name>
> <A2/A3> Role: <Role>
> Status: SHADOW_ACTIVE

## Mission
<Description>

## Handoff Protocol
1. Read <File 1>
2. Read <File 2>
3. <Step 3>
4. <Step 4>
5. <Step 5>

## Output
<What is produced>

## Boundaries
<What is not done>

## Spec
<Specification file>
```

### Convention de Context7 Boundary

**No Context7 lookup is required for local Ikigai pillar/handoff writing. Use Context7 before any provider, plugin, API, MCP, or CLI mutation.**

---

## Ship 2: 22_Wheel_Discovery — Baserow

### Rôle
**Observation Engine** — Observe les 8 domaines de vie et convertissent la charge subjective en signaux ZORA.

### Shadow Tool
**Baserow** — Base de données relationnelle

### Convention de Nommage

```
22_Wheel_Discovery/
├── LD01_Business_Book/ (Book)
├── LD02_Finance_Saru/ (Saru)
├── LD03_Health_Culber/ (Culber)
├── LD04_Cognition_Tilly/ (Tilly)
├── LD05_Social_Stamets/ (Stamets)
├── LD06_Family_Burnham/ (Burnham)
├── LD07_Creativity_Reno/ (Reno)
└── LD08_Impact_Georgiou/ (Georgiou)
```

### Convention de Table Baserow

Chaque domaine correspond à une table Baserow :

| Domain | Table Name | Columns |
|--------|------------|---------|
| Business | LD01_Business_Book | client_id, task, status, priority |
| Finance | LD02_Finance_Saru | client_id, amount, category, date |
| Health | LD03_Health_Culber | client_id, metric, value, date |
| Cognition | LD04_Cognition_Tilly | client_id, metric, value, date |
| Social | LD05_Social_Stamets | client_id, connection, quality, date |
| Family | LD06_Family_Burnham | client_id, relationship, quality, date |
| Creativity | LD07_Creativity_Reno | client_id, project, quality, date |
| Impact | LD08_Impact_Georgiou | client_id, impact, metric, date |

### Convention de Chemin

```
C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\
├── LD01_Business_Book\
│   └── README.md
├── LD02_Finance_Saru\
│   └── README.md
└── ...
```

### Convention de Handoff

Chaque handoff A2/A3 suit ce format :
```markdown
|# <Folder Name> - Handoff <A2/A3>

> Layer: L1 Life OS
> Parent A2: <Parent A2 Name>
> <A2/A3> Role: <Role>
> Domain: <Domain Name>
> Status: SHADOW_ACTIVE

## Mission
<Description>

## Handoff Protocol
1. Read <File 1>
2. Read <File 2>
3. <Step 3>
4. <Step 4>
5. <Step 5>

## Output
<What is produced>

## Boundaries
<What is not done>

## Spec
<Specification file>
```

### Convention de Context7 Boundary

**No Context7 lookup is required to read or update this local handoff. Use Context7 before Baserow API, schema, rollup, MCP, or provider configuration.**

---

## Ship 3: 23_12WY_SNW — Baserow

### Rôle
**Execution Engine** — Convertir la direction de Life OS validée en exécution 12WY.

### Shadow Tool
**Baserow** — Base de données relationnelle

### Convention de Nommage

```
23_12WY_SNW/
├── 01_Vision_Pike/ (Pike)
├── 02_Planning_Una/ (Una)
├── 03_Focus_MBenga/ (M'Benga)
├── 04_Metrics_Chapel/ (Chapel)
└── 05_Execution_Ortegas/ (Ortegas)
```

### Convention de Table Baserow

Chaque discipline correspond à une table Baserow :

| Discipline | Table Name | Columns |
|------------|------------|---------|
| Vision | 01_Vision_Pike | quarter_intent, north_star, deadline |
| Planning | 02_Planning_Una | rock, decomposition, dependencies |
| Focus | 03_Focus_MBenga | strategic_focus, process_control, metrics |
| Metrics | 04_Metrics_Chapel | scorecard, measurement, KPIs |
| Execution | 05_Execution_Ortegas | weekly_execution, tasks, status |

### Convention de Chemin

```
C:\Users\amado\ASpace_OS_V2\20_Life_OS\23_12WY_SNW\
├── 01_Vision_Pike\
│   └── README.md
├── 02_Planning_Una\
│   └── README.md
└── ...
```

### Convention de Handoff

Chaque handoff A2/A3 suit ce format :
```markdown
|# <Folder Name> - Handoff <A2/A3>

> Layer: L1 Life OS
> Parent A2: <Parent A2 Name>
> <A2/A3> Role: <Role>
> 12WY Discipline: <Discipline Name>
> Status: SHADOW_ACTIVE

## Mission
<Description>

## Handoff Protocol
1. Read <File 1>
2. Read <File 2>
3. <Step 3>
4. <Step 4>
5. <Step 5>

## Output
<What is produced>

## Boundaries
<What is not done>

## Spec
<Specification file>
```

### Convention de Context7 Boundary

**No Context7 lookup is required to read or update this local handoff. Use Context7 before Baserow API, schema, rollup, MCP, Symphony adapter, or CLI configuration.**

---

## Ship 4: 24_PARA_Enterprise — Obsidian / Filesystem Knowledge Base

### Rôle
**Structure Engine** — Keep projects, areas, resources, and archives from collapsing into chat residue.

### Shadow Tool
**Obsidian** + **Filesystem** — Knowledge base locale

### Convention de Nommage

```
24_PARA_Enterprise/
├── 01_Projects_Picard/ (Picard)
├── 02_Areas_Spock/ (Spock)
│   └── J01_Jerry_Prime_LD01_Business/
│       ├── 12WY_Area_Cadence/
│       └── B2_Area_Domains/
│           ├── 01_Growth_Superman_Guardians/
│           ├── 02_Sales_MartianManhunter_Illuminati/
│           ├── 03_Product_Flash_Avengers/
│           ├── 04_Ops_Batman_Fantastic4/
│           ├── 05_IT_Cyborg_KangDynasty/
│           ├── 06_Finance_WonderWoman_Thunderbolts/
│           ├── 07_People_GreenLantern_XMen/
│           └── 08_Legal_Aquaman_Eternals/
├── 03_Resources_Geordi/ (Geordi)
└── 04_Archives_Data/ (Data)
```

### Convention de Fichier

Chaque A3 produit un fichier `README.md` avec :
- **Mission** : Rôle de l'A3
- **Handoff Protocol** : 5 étapes
- **Output** : Ce que l'A3 produit
- **Boundaries** : Ce que l'A3 ne fait pas
- **Spec** : Fichier de spécification

### Convention de Chemin

```
C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\
├── 01_Projects_Picard\
│   └── README.md
├── 02_Areas_Spock\
│   └── J01_Jerry_Prime_LD01_Business\
│       └── B2_Area_Domains\
│           └── 01_Growth_Superman_Guardians\
│               └── README.md
└── ...
```

### Convention de Handoff

Chaque handoff A2/A3 suit ce format :
```markdown
|# <Folder Name> - Handoff <A2/A3>

> Layer: L1 Life OS
> Parent A2: <Parent A2 Name>
> <A2/A3> Role: <Role>
> PARA Domain: <Domain Name>
> Status: SHADOW_ACTIVE

## Mission
<Description>

## Handoff Protocol
1. Read <File 1>
2. Read <File 2>
3. <Step 3>
4. <Step 4>
5. <Step 5>

## Output
<What is produced>

## Boundaries
<What is not done>

## Spec
<Specification file>
```

### Convention de Context7 Boundary

**No Context7 lookup is required to read or update this local handoff. Use Context7 before Obsidian plugin, sync, API, MCP, or import/export configuration.**

---

## Ship 5: 25_GTD_Cerritos — Plane

### Rôle
**Chaos Engine** — Capture loose inputs, clarify, organize, review, execute.

### Shadow Tool
**Plane** — Project management tool

### Convention de Nommage

```
25_GTD_Cerritos/
├── 01_Inbox_Mariner/ (Mariner)
├── 02_Clarify_Boimler/ (Boimler)
├── 03_Organize_Rutherford/ (Rutherford)
├── 04_Review_Tendi/ (Tendi)
└── 05_Engage_Freeman/ (Freeman)
```

### Convention de Table Plane

Chaque stage GTD correspond à une table Plane :

| Stage | Table Name | Columns |
|-------|------------|---------|
| Capture | 01_Inbox_Mariner | input, source, timestamp, category |
| Clarify | 02_Clarify_Boimler | input, definition, next_action |
| Organize | 03_Organize_Rutherford | input, location, dependencies |
| Review | 04_Review_Tendi | input, status, next_review_date |
| Engage | 05_Engage_Freeman | input, next_action, owner |

### Convention de Chemin

```
C:\Users\amado\ASpace_OS_V2\20_Life_OS\25_GTD_Cerritos\
├── 01_Inbox_Mariner\
│   └── README.md
├── 02_Clarify_Boimler\
│   └── README.md
└── ...
```

### Convention de Handoff

Chaque handoff A2/A3 suit ce format :
```markdown
|# <Folder Name> - Handoff <A2/A3>

> Layer: L1 Life OS
> Parent A2: <Parent A2 Name>
> <A2/A3> Role: <Role>
> GTD Stage: <Stage Name>
> Status: SHADOW_ACTIVE

## Mission
<Description>

## Handoff Protocol
1. Read <File 1>
2. Read <File 2>
3. <Step 3>
4. <Step 4>
5. <Step 5>

## Output
<What is produced>

## Boundaries
<What is not done>

## Spec
<Specification file>
```

### Convention de Context7 Boundary

**No Context7 lookup is required to read or update this local handoff. Use Context7 before Plane API, project schema, MCP, webhook, or provider configuration.**

---

## Ship 6: 26_DEAL_Protostar — Affine Edgeless

### Rôle
**Liberation Engine** — Turn repeated friction into liberation blueprints.

### Shadow Tool
**Affine Edgeless** — Canvas for blueprints

### Convention de Nommage

```
26_DEAL_Protostar/
├── 01_Definition_Dal/ (Dal)
├── 02_Elimination_RokTahk/ (Rok-Tahk)
├── 03_Automation_Zero/ (Zero)
└── 04_Liberation_Gwyn/ (Gwyn)
```

### Convention de Table Affine

Chaque stage DEAL correspond à une table Affine :

| Stage | Table Name | Columns |
|-------|------------|---------|
| Define | 01_Definition_Dal | friction, outcome, source, pipeline |
| Eliminate | 02_Elimination_RokTahk | friction, elimination, impact |
| Automate | 03_Automation_Zero | friction, automation, risk |
| Liberate | 04_Liberation_Gwyn | friction, liberation, metric |

### Convention de Chemin

```
C:\Users\amado\ASpace_OS_V2\20_Life_OS\26_DEAL_Protostar\
├── 01_Definition_Dal\
│   └── README.md
├── 02_Elimination_RokTahk\
│   └── README.md
└── ...
```

### Convention de Handoff

Chaque handoff A2/A3 suit ce format :
```markdown
|# <Folder Name> - Handoff <A2/A3>

> Layer: L1 Life OS
> Parent A2: <Parent A2 Name>
> <A2/A3> Role: <Role>
> DEAL Stage: <Stage Name>
> Status: SHADOW_ACTIVE

## Mission
<Description>

## Handoff Protocol
1. Read <File 1>
2. Read <File 2>
3. <Step 3>
4. <Step 4>
5. <Step 5>

## Output
<What is produced>

## Boundaries
<What is not done>

## Spec
<Specification file>
```

### Convention de Context7 Boundary

**No Context7 lookup is required to read or update this local handoff. Use Context7 before Affine API, Edgeless integration, MCP, plugin, or provider configuration.**

---

## Convention de Handoff Standardisée

Tous les handoffs A2/A3 suivent ce format standard :

```markdown
|# <Folder Name> - Handoff <A2/A3>

> Layer: L1 Life OS
> Parent A2: <Parent A2 Name>
> <A2/A3> Role: <Role>
> <Framework> Discipline: <Discipline Name>
> Status: SHADOW_ACTIVE

## Mission
<Description>

## Handoff Protocol
1. Read <File 1>
2. Read <File 2>
3. <Step 3>
4. <Step 4>
5. <Step 5>

## Output
<What is produced>

## Boundaries
<What is not done>

## Spec
<Specification file>
```

---

## Convention de Context7 Boundary Standardisée

Tous les ships suivent cette convention :

**No Context7 lookup is required to read or update this local handoff. Use Context7 before <Shadow Tool> API, schema, MCP, webhook, or provider configuration.**

---

## Anti-Patterns

1. **Copier le texte d'un README local** → Inutile et coûteux
2. **Modifier un shadow tool sans Context7** → Risque de bugs ou de perte de données
3. **Ignorer les claims externes** → Risque de sécurité ou de conformité
4. **Marquer `NEEDS_CONTEXT7` sans vérifier** → Risque de drift doctrinal

---

## Risques

1. **Drift doctrinal** : Si Context7 n'est pas utilisé, les conventions peuvent diverger
2. **Bugs de configuration** : Si Context7 n'est pas utilisé, les configurations peuvent être incorrectes
3. **Perte de données** : Si Context7 n'est pas utilisé, les données peuvent être perdues
4. **Risque de sécurité** : Si Context7 n'est pas utilisé, les secrets peuvent être exposés

---

## Mitigation

1. **Standardiser les handoffs** → Chaque ship a son propre format
2. **Standardiser les Context7 Boundary** → Chaque ship a sa propre Boundary
3. **Marquer `NEEDS_CONTEXT7`** → Tous les claims externes doivent être marqués
4. **Utiliser Context7 avant toute mutation** → Vérifier le provider/plugin/API/MCP/CLI
5. **Documenter la preuve** → Toujours documenter la preuve dans le fichier local

---

## Références

- `AGENTS.md` — Canon Absolu A'Space OS
- `10_Tech_OS/12_Blueprints/01-SDD/SDD-008_shadow-L1-life-os.md` — Shadow L1 Life OS
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/concepts/concept_life_os.md` — Concept Life OS
- `20_Life_OS/00_Context7_Boundary_L1.md` — Context7 Boundary L1
- `CLAUDE.md` — Context7 Boundary pour L0 Tech OS