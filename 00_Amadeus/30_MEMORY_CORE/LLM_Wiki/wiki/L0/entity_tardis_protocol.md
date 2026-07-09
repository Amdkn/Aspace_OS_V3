---
source: LLM_Wiki_A0
date: 2026-05-10
type: entity
domain: Tech_OS / L0_Infra / Agent_Runtime
tags: [#entity #TARDIS_Protocol #Version_Control #Agent_History #A0_Memory #Trust_Zone #Anti-Technicien]
---

# Entity: TARDIS Protocol

> Canon: `A'Space_OS_V2/00_Amadeus/01_Identity_Core/AGENTS.md` (A0/Rick)

**TARDIS** = **T**ime **A**nd **R**elative **D**imension **I**n **S**pace

Le TARDIS Protocol est le **système de contrôle de version pour agents** dans A'Space OS. Inspiré du TARDIS de Doctor Who (qui voyage dans le temps et préserve l'historique), ce protocole exige que toute modification d'agent soit **historisée**, jamais écrasée.

---

## Origine

Née de la perte de `A0_Memory` lors de la purge de `C:\Aspace00` le **2026-03-05**. Un agent avait été modifié sans保存历史 → perte de mémoire contextuelle.

**Loi du Checkpoint Profond (Anti-Technicien):**
> Un technicien automatise. Un Architecte vérifie ce qu'il laisse derrière.

---

## Principes

1. **Jamais de `git reset --hard`** sur un agent modifié
2. **Jamais de `Remove-Item`** sans checkpoint préalable
3. **Tout agent modifié** = nouvelle version avec historique
4. **ADR referencing** — chaque version doit référencer l'ADR qui la gouverne

---

## Implementation

```python
# Exemple: avant de modifier un agent
def checkpoint_agent(agent_name: str, version: str, adr_ref: str):
    """
    Sauvegarde l'état actuel avant modification.
    Throw: si checkpoint échoue, modification interdite.
    """
    path = f"00_Amadeus/11_Teams/{agent_name}/versions/"
    timestamp = datetime.now().isoformat()
    save(f"{path}v{version}_{timestamp}.md", current_state)
    log(f"TARDIS checkpoint: {agent_name} v{version} @ {timestamp}")
```

---

## Checklist Av任何 modification

- [ ] Inventaire: lister TOUS les dossiers exclus
- [ ] Checkpoint: dossiers > 100 MB = STOP + validation explicite
- [ ] Inventaire avant purge: rapport de ce qui Ne sera Pas dans la destination
- [ ] Commentaire obligatoire: `# EXCLU — validé par Amadeus le [date]`

---

## Relationship

- **[[entity_rick]]**: Rick enforce le TARDIS Protocol comme standard L0
- **[[entity_amadeus]]]]: A0 a créé ce protocole après la perte de A0_Memory
- **[[entity_13th_doctor]]**: Doc infra implémente les checkpoints scripts

---

## Stats

- **Mentions dans 2026-05**: 245
- **Domain**: L0 Infra / Agent Runtime
- **Source**: [[sources/source_gemini-takeout-2026-05]]

---

*Last updated: 2026-05-11*
*Source: [[sources/source_gemini-takeout-2026-05]] | AGENTS.md (canon)*

---

## Inbounds

- [[sources/source_gemini-takeout-2026-05]] — TARDIS Protocol émerge comme solution à la perte de A0_Memory
- [[concept_sovereignty]] — TARDIS = instrument de la souveraineté mémoire
- [[concept_e-myth]] — TARDIS = E-Myth en action (Manager vérifie le Technician)