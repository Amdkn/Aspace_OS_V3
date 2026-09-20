# 00_Gatekeepers_Beth_Morty

|> Layer: L1 Life OS
|> Status: IMPLEMENTATION_IN_PROGRESS
|> Last updated: 2026-09-09
|> Canonical sources: A1_Beth_Spec.md, A1_Morty_Spec.md, fancy-hugging-bengio.md §4, SDD-005 life-os-l1-integration
|
This folder implements the A1 layer gatekeeper system for Life OS.

## Current State

**Implementation 5D** in progress per `EXECUTION_CONTRACT.md`. Livrables:

1. `life_gate.py` — Module gatekeeper A1 pivotant entre Beth et Morty.
   - **read-only evaluation (`eval`)** : extrait état numérique LD03/LD04 source-sécurisé, frais, numérique fini ; vérifie GTD inbox manquant/invalide ; rend ordonnance beth_green_authorized ; structure distincte vs état mesuré, provenance machine.
   - **capture (`capture <file>`)** : saisie GTD markdown locale via chemin déterministe et exclusif ; préserve littéralement ; hash content ; rejette même chemin / trace de traversal ; idempotent.
   - **validation (`validate`)** : fait passer tout JSON Context Pack (9 champs canon) et vérifie clearance Beth par rapport à contenu/hash ; rejette bool/NaN/non-numeric observations ; bloque les shell arbitraires.

2. `test_life_gate.py` — Paire de tests stdlib pour validations négatives, timestamps futurs/stalés, données booléennes/NaN, manquants, couleurs fabriquées, payloads modifiés, captures duplicates, chemins dangereux, snapshot invalide.

3. **README implémentation section** : précisément l'ajout ci-dessus.

## Files

| File | Purpose |
|------|---------|
| `life_gate.py` | Gatekeeper module avec CLI eval/capture/validate |
| `test_life_gate.py` | Tests unitaires pour le module gatekeeper |
| `A1_Beth_Spec.md` | Spécification stratégique/veto Beth |
| `A1_Morty_Spec.md` | Spécification exécuteur/routage Morty |
| `ContextPack.template.yml` | Contrat de handoff requis pour Morty |
| `README_Governance.md` | Règle de gouvernance compacte |
| `Beth_Alignment_Log/` | Enregistrements de décisions et veto Beth |
| `Morty_Global_Queue/` | File d'attente exécutable et dry-runs |
| `Sunday_Uplink_Protocols/` | Revues hebdo et rituels uplink ZORA |

## Operating Law

Beth lit le filesystem et la télémétrie de vie avant d'autoriser le travail. Morty route seulement les Context Packs validés.

Aucune action L1 n'est valide à moins qu'elle ne puisse répondre à :

1. Quel domaine ou framework est affecté ?
2. Quel A2 ship possède la décision ?
3. Quel A3 crew member possède la prochaine action ?
4. Quel evidence path prouve la requête ?
5. Did Beth clear l'exécution ?

## Module Usage

```bash
# Évaluation beth-ordonnée machine (aujourd'hui en GREEN si santé/cognition OK)
python life_gate.py eval

# Capture GTD markdown source (source repo)
python life_gate.py capture /chemin/vers/inbox.md

# Valider context pack depuis stdin
cat > cp.json <<EOF
{"ship": "USS Cerritos", "crew_member": "Spock", "next_action": "capture GTD", "framework": "GTD", "domain_impact": "life", "l0_skill_required": "terminal", "beth_clearance": "GREEN", "evidence_paths": ["path/to/ev1.json"], "output_artifact": "path/to/out.md"}
EOF
cat cp.json | python life_gate.py validate
```

## Purpose

Ce module implémente les gates de décision au niveau A1 qui protègent les 6 ships A2 :
- **USS Orville** (Ikigai)
- **USS Discovery** (Life Wheel / ZORA)
- **USS SNW** (12WY)
- **USS Enterprise** (PARA)
- **USS Cerritos** (GTD)
- **USS Protostar** (DEAL)

Il applique les règles verrouillées du plan `fancy-hugging-bengio.md` §3.5-3.8, y compris les seuils SDD-005:

```yaml
beth_thresholds:
  LD03_minimum: 4.0
  LD04_minimum: 3.5
  multi_domain_alert: 3
```

Le module est **fail-closed**, utilisant uniquement le stdlib Python, sans exécution shell arbitraire, et mettant en œuvre une gestion de fichier sécurisée et déterministe.

## Evidence & Integration

- `SDD-005_life-os-l1-integration.md` : Beth comme Life Core Guardian, HALT authority, PRD-L1 validator.
- `SDD-008_shadow-L1-life-os.md` : Shadow L1 tool mapping.
- `SDD-010_meta-cloture-scope-13eme-semaine.md` : Beth split stratégique et L2 nested dans L1 PARA.
- `.openclaw/workspace/agents_runtime/L1/L1_A1_Beth.md` : historical minimal Beth.
- `Shadow_L1/03_life-os-baserow-database-analysis-20260517.md` : concrete `Veto Beth` and `Morty Routing` fields.

## Self-Consistency

> **Règle d'or 1 : Le Gate Inviolable (`50_Distillation/`)**
>   Aucun fichier brut, aucune note non triée n'entre en direct dans la mémoire ou le graphe.
>
> **Règle d'or 2 : Les 4 Organes Souverains au-dessus de tout**
>   `70_Onthologies/`, `40_Memory_Wiki_OKF/`, `60_Implementation_Méthodologiques/` et `90-self-evolution/` gouvernent les 3 OS applicatifs (`10_Tech_OS`, `20_Life_OS`, `30_Business_OS`).
>
> **Règle d'or 3 : Le Couplage Déterministe (Hooks & Webhooks)**
>   Les agents ne s'exécutent jamais sans intercepteurs runtime (`10_Tech_OS/kernel/hooks/`).

Ce module respecte ces invariants tout en implémentant les gates concret de niveau A1 pour Life OS.