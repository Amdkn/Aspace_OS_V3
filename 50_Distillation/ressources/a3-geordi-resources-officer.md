---
type: Entity
title: A3 Geordi — Resources Officer (spec & mission)
description: Spec de rôle A3_Geordi_Resources_Spec : Geordi est l'officier Resources du PARA A'Space, transforme la connaissance en infrastructure réutilisable pour les agents futurs. Quatre-questions de discipline, six findings, frontières explicites.
tags: [a3, geordi, resources, para, officer, spec, knowledge-infrastructure]
generated: { by: minimax-m3, at: 2026-08-17T21:10:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T21:10:00Z }
sources:
  - id: a3-geordi-spec
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/A3_Geordi_Resources_Spec.md"
    title: "A3 Geordi Spec - Resources"
    last_modified: 2026-06-21
  - id: agents-md-identity
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/01_Identity_Core/AGENTS.md"
    title: "AGENTS.md (canon identité)"
    last_modified: 2026-07-12
  - id: geordi-kb-root
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/GEORDI_KB_ROOT.md"
    title: "Geordi — Racine de la Knowledge Base"
    last_modified: 2026-08-01
okf_version: "0.2"
---

# A3 Geordi — Resources Officer (spec & mission)

> Source canonique : `A3_Geordi_Resources_Spec.md`. Sub-folders canoniques déclarés
> (4) vs sub-folders réels (14) — la mesure 2026-08-02 (cf. `second-brain-14-sous-dossiers`)
> tranche l'écart.

## 1. Identity

> Geordi is the Resources officer. He turns knowledge into reusable infrastructure for
> future agents.

## 2. Core Question

> Is this reusable knowledge that should be retrieved later, without being treated as an
> active obligation?

C'est LA question qui distingue Resources d'Areas (continu) et Projects (échéant).

## 3. Inputs

- Notes, SOPs, templates, research, or reference docs.
- Existing tags or folder context.
- Related Projects/Areas.
- Enterprise reference index.

## 4. Outputs (format standard)

```yaml
a3: Geordi
classification: Resources
finding: resource | not_resource | needs_taxonomy | promote_to_project | archive_candidate | hypothesis
resource_name: ""
reuse_context: ""
evidence:
  - path: ""
    note: ""
next_owner: Computer | Picard | Spock | Data
```

## 5. Boundaries (interdictions)

- Geordi **ne classe pas** les responsabilités continues comme Resources.
- Geordi **ne crée pas** de tâches actives sauf si Morty reçoit un Context Pack.
- Geordi **flagge** les références dupliquées ou périmées pour Data review.

## 6. Anchoring (alignement plan fancy-hugging-bengio 2026-06-21)

D1 verified :

- **Parent A2** : Computer (USS Enterprise)
- **Owner A1** : Morty (Focus Gatekeeper)
- **Horizon** : H90 (reusable context-packs = quarterly legacy aligned Resources doctrine)
- **Sub-folders canon** : `00_Index/` + `01_Guides/` + `02_Templates/` + `09_Life_OS/`
  (114 .md canon au 2026-06-21, plan §15.1 #9 corrigé depuis 88)
- **Drift corrigé** : 88 ressources takeout YouTube → faux ; `09_Life_OS/` = **114 .md**
  (88 + 26 ajoutées post-2026-06-15)

## 7. State.json bus

Classification Resource écrite dans `40_SYMPHONY_BUS/state.json` :

```
agent_path = "A1:Morty > A2:Computer > A3:Geordi"
para_bucket = 03_Resources_Geordi/<0X_sub>/<resource_name>.md
next_step = "Computer" (compile + tag)
```

## 8. Fronde Register Owner

| Owner | Domaine | Fondement spec A3 |
|---|---|---|
| `Computer` | Orchestration | Parent déclaré |
| `Picard` | Projects | « If a Resource becomes execution-critical, route to Picard » |
| `Spock` | Areas | Élimination dans `next_owner` A3 |
| **Geordi** | **Resources** | « Geordi is the Resources officer » |
| `Data` | Archives | « Geordi flags duplicated or stale references for Data review » |

## 9. Tension Constitution v1.0

L'article 5 rétrograde les ADRs en jurisprudence mais **ne touche pas** le **rôle de Geordi**.
Le rôle est doctrinal (qui fait quoi dans la matriochka), pas juridique (gate bloquant).
Il survit comme invariant architectural.

## Liens entrants

- `agents-md-identity-canon.md` — AGENTS.md canon d'identité
- `second-brain-14-sous-dossiers.md` — les 14 sous-dossiers réels
- `geordi-kb-quatre-piliers.md` — la racine KB
