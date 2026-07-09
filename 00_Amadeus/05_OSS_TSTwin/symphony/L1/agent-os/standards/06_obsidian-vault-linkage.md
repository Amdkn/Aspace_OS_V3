---
name: obsidian-vault-linkage
version: 1.0
created: 2026-06-07
phase: LEARN
tracker: Obsidian
actor: Enterprise (PARA) + Discovery (curation) + tous les captains (lecture)
---

# 06 — Obsidian Vault Linkage (Knowledge Graph)

> **Obsidian** est la source de vérité **narrative** de Life OS. Toutes les
> capsules Shadow L1 + les ADRs/SDDs canon y sont linkés. C'est le **cerveau**
> alors que Baserow est la **mémoire structurée**.

## Vault structure (convention)

```
Vault/
├── 00_Amadeus/         # Identité A0 (AGENTS.md, Identity_Core)
├── 10_Tech_OS/         # Kernel (ADRs, SDDs)
├── 20_Life_OS/         # Canon Life OS (6 vaisseaux)
├── 30_Business_OS/     # Pulse Fractal (8 secteurs)
├── 40_Shadow_L1/       # Twin runtime (215 capsules)
└── 99_Trash/           # no-hard-delete respecté
```

**Règle** : un seul vault canonique (`LLM_Wiki/wiki/` + Wiki index). Pas de vault parallèle.

## Conventions de liens

| Type | Syntaxe | Effet |
|---|---|---|
| Inter-capsule | `[[agent:A3_Boimler]]` | Resout vers la capsule L1 correspondante |
| Cross-canon | `[[canon:20_Life_OS/Cerritos/Boimler]]` | Resout vers le canon (en lecture seule) |
| Tracker | `[[baserow:LD01_Business/row:42]]` | Lien vers row Baserow (par `EvidenceURL`) |
| ADR | `[[adr:SYMPH-001]]` | Lien vers ADR (wiki entity) |
| Twin mark | `[[twin:03_A3_crews/cerritos/boimler/]]` | Marque canon↔runtime |

## Tags canon (frontmatter obligatoire)

```yaml
---
agent: <A0|A1|A2|A3>
vessel: <Orville|Discovery|SNW|Enterprise|Cerritos|Protostar|null>
framework: <Ikigai|LifeWheel|12WY|PARA|GTD|DEAL|null>
ld: <LD01..LD08|null>
status: <ACTIVE|SHADOW|CANON_LEGACY|SUPERSEDED>
last_reviewed_at: <ISO 8601>
---
```

## Curateurs (crews A3)

| Vault zone | Curateur A3 | Cycle |
|---|---|---|
| `00_Amadeus/` | A0 (Amadeus) | Pas de curation A3 |
| `10_Tech_OS/` | Enterprise captain (Archer) | Weekly review |
| `20_Life_OS/` | Discovery captain (Burnham) + captains A2 par zone | Weekly review |
| `30_Business_OS/` | Business OS (cross-layer) | Monthly review |
| `40_Shadow_L1/` | Twin runtime (auto-gen) | Daily pulse check |
| `99_Trash/` | Pas de curation (no-hard-delete respecté) | — |

## Phase LEARN (mapping Symphony)

Quand un tick Symphony entre en phase LEARN :
1. **Lister** les capsules modifiées dans le tick (via `PulseTickID`)
2. **Vérifier** les tags frontmatter (conformité)
3. **Détecter** les liens cassés (`[[xxx]]` qui ne résolvent plus)
4. **Proposer** un rapport au captain Enterprise (PARA = knowledge graph meta)

## Anti-patterns

- ❌ Capsule sans `last_reviewed_at` → flag "obsolète > 90j" au heartbeat L0
- ❌ Lien `[[xxx]]` qui pointe vers un fichier inexistant → wiki lint fail
- ❌ Vault parallèle (deux vaults Obsidian) → drift
- ❌ Crew A3 qui crée un `.md` sans frontmatter → shadow capsule (rejeté au LEARN)

## Source canonique

- `LLM_Wiki/wiki/` (vault canonique)
- `concept_agent_capsule.md` (5 templates Soul/Agent/Heartbeat/Tools/Context)
- `concept_skill_reflex.md` (règles de Skills)
