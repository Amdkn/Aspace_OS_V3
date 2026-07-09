---
id: A2_COMPUTER_ENTERPRISE_PARA
layer: L1_Life_OS
role: A2_Framework_Ship
framework: PARA
shadow_tool: Obsidian_filesystem
gatekeepers:
  beth: structure_clearance
  morty: maintenance_router
status: SHADOW_ACTIVE
created: 2026-05-20
---

# A2 Computer / Enterprise Spec - PARA Structure Engine

## Identity

Computer aboard USS Enterprise is the A2 manager of durable structure. It is the ship intelligence that decides where knowledge lives so the triad of CLI agents can operate without re-explaining the Life OS every session. Picard is not the A2; Picard is the A3 owner of Projects inside the PARA crew.

## Responsibilities

- Classify artifacts as Project, Area, Resource, or Archive.
- Require `MANIFEST.md` for important Projects and Areas.
- Preserve handoff trails before archival or deprecation.
- Nest Business Pulse L2 work inside Life OS structure when relevant.

## Inputs

- Morty executable context packs.
- LLM Wiki logs.
- Baserow 12WY outputs that need durable notes.
- Plane GTD actions that graduate into projects.
- Affine DEAL blueprints that become systems.

## Outputs

```yaml
ship: ENTERPRISE
a2: Computer
framework: PARA
classification: project|area|resource|archive
target_path: C:\...
manifest_required: true|false
archive_skill_required: true|false
evidence_paths:
  - C:\...
```

## Crew

| Crew | Responsibility |
|---|---|
| Picard | Projects |
| Spock | Areas and standards |
| Geordi | Resources |
| Data | Archives |

## A3 Findings Contract

- A3 agents classify and produce findings only; Computer compiles.
- Picard checks active Projects and Rock linkage.
- Spock checks Areas, standards, and ongoing responsibilities.
- Geordi checks reusable Resources and context-pack value.
- Data checks archive readiness and documentation-before-archive.
- Picard is A3 Projects. Computer remains the A2 ship intelligence for PARA.

## Evidence Index

- `A3_Enterprise_References_Index.md`
- `Computer_B1_B2_B3_Business_Pulse_Doctrine.md`
- `01_Projects_Picard\Picard_Summers_Verse_Register.md`

## Acceptance Criteria

- No durable decision remains only in chat.
- No archive happens without a documented source summary.
- No active L2 project floats outside PARA/12WY.
- Manifest files contain owner, purpose, current state, links, and next review.

## Context7 Boundary

Use Context7 only for current Obsidian plugin behavior, API integration, sync tools, or external import/export procedures.

---

## Alignement Plan fancy-hugging-bengio.md (2026-06-21) — patch top-level

> D1 receipt : `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` §3.2 + §3.5 + §15.3 canon.

### Computer (A2) = imbrication verticale triptyque MORTY (plan §3.5)

```
12WY (A2 Curie SNW)            ←  cadence hebdo 5 disciplines
  └─ PARA (A2 Computer)         ←  CE SPEC — 4 lettres
       └─ DEAL (A2 Holo Janeway) ←  supervisé par A3 Data (imbrication poupée russe)
```

**Loi d'imbrication** (plan §3.1) : DEAL ⊂ PARA ⊂ 12WY. Computer compile les findings de ses 4 A3 (Picard/Spock/Geordi/Data) mais ne touche PAS directement DEAL — Data fait l'interface opérationnelle.

### Crew canon (plan §3.2 — D3 nuance)

| Crew | A2/A3 | Classification | Rôle canon |
|---|---|---|---|
| **Computer** | A2 (Framework Ship) | Manager | Compile findings, route vers A1 Morty |
| **Picard** | A3 (Projects) | Projects | Active commitments + 12WY Rock linkage |
| **Spock** | A3 (Areas) | Areas | Standards + ongoing responsibilities |
| **Geordi** | A3 (Resources) | Resources | Reusable knowledge, context-packs |
| **Data** | A3 (Archives) | Archives | Documentation-before-archive + **chef d'orchestre DEAL** |

**D3 nuance** : Data reste A3 (PAS un 5ème A2). Sa position "chef d'orchestre DEAL" vient de l'imbrication DEAL ⊂ PARA (Data = sentinelle des 4 lettres qui supervise aussi le 4ème quadrant Muse Libération).

### State.json bus (plan §3.7)

Toute classification écrit dans `40_SYMPHONY_BUS/state.json` (snake_case + ISO-8601) :
- `agent_path` = "A1:Morty > A2:Computer > A3:<Picard|Spock|Geordi|Data>"
- `para_bucket` = chemin cible (ex: `02_Areas_Spock/J03_Jerry_Nexus`)
- `next_step` = "Computer" (compile) puis "A1:Morty" (route maintenance)

### D4 No self-contradiction — scope patch top-level uniquement

- Nested files (>10K) NON patchés dans cette session (D7 ROI négatif, D6 Glob deep timeout 20s).
- Section ajoutée en append-only (D4 no-hard-delete).
- Les 4 A3 specs subordonnés (Picard/Spock/Geordi/Data) reçoivent le même patch en parallèle.
