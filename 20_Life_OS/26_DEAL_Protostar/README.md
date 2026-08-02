# 26_DEAL_Protostar - Handoff A2

> Layer: L1 Life OS  
> A2: Holo Janeway aboard USS Protostar  
> Framework: DEAL / MUSE liberation  
> Shadow tool: Affine Edgeless and filesystem blueprints  
> Gatekeepers: Beth validates liberation; Morty routes implementation only after proof  
> Status: SHADOW_ACTIVE

## Mission

Protostar turns repeated friction into liberation blueprints. It defines the outcome, eliminates waste, automates only what is safe, and liberates time without creating invisible complexity.

## Resume Protocol

1. Read Beth/Morty specs.
2. Read `A2_HoloJaneway_Protostar_Spec.md`.
3. Identify the DEAL stage: Define, Eliminate, Automate, or Liberate.
4. Produce a blueprint before implementation.
5. Route implementation to Morty only when the automation boundary is explicit.

## A2 Spec

- `A2_HoloJaneway_Protostar_Spec.md`
- `A3_Protostar_References_Index.md`

## Crew Map

| Folder | A3 role | DEAL stage |
|---|---|---|
| `01_Definition_Dal` | Dal | Define |
| `02_Elimination_RokTahk` | Rok-Tahk | Eliminate |
| `03_Automation_Zero` | Zero | Automate |
| `04_Liberation_Gwyn` | Gwyn | Liberate |

## A3 Rule

Protostar A3 agents produce narrow DEAL findings only. Holo Janeway compiles the liberation blueprint and Morty routes implementation only after the stage, risk, and expected proof are explicit.

## Outputs

- DEAL blueprint.
- Elimination list.
- Automation candidate with risk class.
- Liberation metric for Beth/Sunday Uplink.

## Handoff Rules

- Protostar does not automate by default; it eliminates first.
- Risky automation routes to Beth, then Morty, then the appropriate technical owner.
- Affine is the Shadow L1 canvas, but current API/plugin behavior is `NEEDS_CONTEXT7`.
- Generated blueprints belong in PARA if they become durable systems.

## Evidence

- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\symphony-affine.spec.md`
- `C:\Users\amado\ASpace_OS_V2\10_Tech_OS\12_Blueprints\01-SDD\SDD-008_shadow-L1-life-os.md`

## Context7 Boundary

No Context7 lookup is required to read or update this local handoff. Use Context7 before Affine API, Edgeless integration, MCP, plugin, or provider configuration.

---

## Alignement Plan fancy-hugging-bengio.md (2026-06-21)

> **D1 receipt** : patch canonique Round 1 alignant `26_DEAL_Protostar/` sur le plan `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` (§3.1, §3.2, §3.5, §25) — Doctrine Anti-Paresse ADR-META-001 D1-D8 appliquée (verify-before-assert, no-self-contradiction, proof-before-claim).

### Matrice 4 stages DEAL × A3 canon (plan §25.1)

| Étape | A3 | Rôle canon | Output canon (plan §25.1) | Output local (DEAL dossier) |
|---|---|---|---|---|
| **D**efine | Dal | Pattern detection + outcome specification | `pattern_definition.md` | `01_Definition_Dal/A3_Dal_Definition_Spec.md` |
| **E**liminate | Rok-Tahk | NO-GO propositions + permission de delete | `elimination_proposal.md` | `02_Elimination_RokTahk/A3_RokTahk_Elimination_Spec.md` |
| **A**utomate | Zero | Skill creation + sub-agent deployment | `skill_<name>/SKILL.md` + risk_class + D1 proof | `03_Automation_Zero/A3_Zero_Automation_Spec.md` |
| **L**iberate | Gwyn | D11 bandwidth measurement + maintenance tax | `d11_score.json` | `04_Liberation_Gwyn/A3_Gwyn_Liberation_Spec.md` |

### Data (PARA Archives) — chef d'orchestre DEAL (plan §3.1, §3.5)

**D3 nuance** : **DEAL ⊂ PARA ⊂ 12WY** (imbrication poupée russe triptyque Morty, plan §3.1). A3 **Data** (`20_Life_OS/24_PARA_Enterprise/04_Archives_Data/`, parent A2 Computer Enterprise) supervise opérationnellement Holo-Janeway A2 DEAL et **libère A1 Beth (Ikigai Centrée) de la supervision opérationnelle de Protostar**. A1 Beth conserve le **veto d'alignement Ikigai** ; A3 Data porte la **supervision DEAL courante**.

### Affine shadow tool + state.json bus (plan §23.1, §25.3)

- **Affine Edgeless** = shadow L1 canvas pour blueprints DEAL (spec ligne 6 + handoff lignes 51-52). Local blueprint writing ne nécessite pas Context7 (spec ligne 81).
- **`state.json`** = bus sémantique inter-agents. Chaque stage DEAL persiste sa transition (`captured → clarified → eliminated → automated → liberated`) pour traçabilité Karpathy loop (plan §25.3).

### Karpathy loop appliqué D→E→A→L (plan §25.3)

```
D Define ───► A3 Dal capture pattern friction (Mariner inbox upstream)
    │
E Eliminate ──► A3 Rok-Tahk NO-GO propose (Tendi review upstream)
    │
A Automate ─► A3 Zero crée skill canon (skill-reflex-detect.ps1)
    │
L Liberate ─► A3 Gwyn mesure D11 (heartbeat-tick.ps1)
    │
Karpathy retest ─► si val_score < target → amend → re-D Define
```

**D11 bandwidth metric = output Gwyn** : gain bande passante cognitive (minutes libérées/semaine) vs maintenance tax (minutes upkeep/semaine). Upkeep > gain → route back to Zero/Rok-Tahk.

### Loi d'héritage DEAL (plan §25.2)

- Un PRD DEAL ne peut pas contredire son ADR parent (`_SPECS/ADR/ADR-DEAL-001` ratifié cible fin Item 11 Q3 2026).
- Un DDD skill ne peut pas contredire son ADR parent.
- Le CODE doit implémenter le DDD, pas l'interpréter.

### Cycle 12WY Q3 2026 — DEAL Item 11

**Item 11** : "Transfert du Memory core local sur VPS pour reconstruction A'Space OS en D.E.A.L de Muse de Libération 4H Workweek" → A1 Beth → A2 Protostar → A3 Rok-Tahk + Zero · H30 · 🔄 In progress.
