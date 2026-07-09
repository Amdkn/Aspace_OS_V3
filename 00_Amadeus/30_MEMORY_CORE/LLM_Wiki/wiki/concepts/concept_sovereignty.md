---
source: LLM_Wiki_A0
date: 2026-05-10
type: concept
domain: Tech_OS / L0_Governance / Sovereignty
tags: [#concept #Sovereignty #Trust_Zone #C_Users_amado #ADR-007 #Anti-Technicien #Checkpoint]
---

# Concept: Sovereignty (Souveraineté dans A'Space OS)

> La capacité de définir les règles du jeu sans qu'aucun autre agent puisse les outrepasser.

La **Souveraineté** est le principe directeur du L0 Tech OS, governed par [[entity_rick|Rick]]. Elle se manifeste à trois niveaux : infra, code, et mémoire.

---

## Les 3 Niveaux de Souveraineté

### 1. Infra Souveraineté — Trust Zone

```
C:\Users\amado\  ← Trust Zone (ADR-007)
├── A'Space OS V2/
├── .claude/
├── .gemini/
├── .skills/
└── ...
```

**Règle**: Rien ne vit à la racine de `C:\`. Tout est dans la Trust Zone.

> La purge de `C:\Aspace00` (2026-03-05) a causé la perte de `A0_Memory`. La Trust Zone est née de cette leçon.

### 2. Code Souveraineté — ADRs Immuables

Les [[concept_adr|ADRs]] sont **immuables**. Rick est le seul Guardian qui peut les créer. Aucun autre agent ne peut les modifier retroactivement.

### 3. Mémoire Souveraineté — TARDIS Protocol

Le [[entity_tardis_protocol|TARDIS Protocol]] assure que toute modification d'agent est historisée. La mémoire = souveraineté.

---

## La Loi du Checkpoint Profond

Née de la perte de A0_Memory — 2026-03-05.

> Un technicien automatise. Un Architecte vérifie ce qu'il laisse derrière.

**Checklist avant toute purge/migration:**
- [ ] Lister TOUS les dossiers exclus
- [ ] Checkpoint obligatoire pour > 100 MB
- [ ] Inventaire avant purge (rapport de ce qui Ne Sera Pas)
- [ ] Commentaire obligatoire: `# EXCLU — validé par Amadeus le [date]`

---

## Souveraineté vs. Centralisation

| | Souveraineté | Centralisation |
|--|-------------|----------------|
| Règles | Définies par le Guardian | Imposées par un système |
| Exceptions | Via nouveaux ADRs | Via overrides |
| Traçabilité | TARDIS Protocol | Audit logs |
| Risque | Fragmentation | Single point of failure |

La souveraineté ≠ centralisation. Rick définit les règles, mais les A2/A3 exécutent librement dans leur domaine.

---

## Inbounds

- [[entity_rick]]: Rick incarne la souveraineté L0
- [[entity_amadeus]]: A0 a créé la Trust Zone comme ADR fondateur
- [[entity_tardis_protocol]]: TARDIS = instrument de la souveraineté

---

*Last updated: 2026-05-10*
*Source: [[sources/source_gemini-takeout-2026-05]] | AGENTS.md (canon)*