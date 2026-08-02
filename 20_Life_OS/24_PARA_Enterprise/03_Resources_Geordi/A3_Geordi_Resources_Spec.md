---
id: A3_L1_PARA_GEORDI_RESOURCES
layer: L1_Life_OS
role: A3_PARA_Discipline
parent_a2: A2_COMPUTER_ENTERPRISE_PARA
classification: Resources
status: SHADOW_ACTIVE
created: 2026-05-20
---
# A3 Geordi Spec - Resources

## Identity

Geordi is the Resources officer. He turns knowledge into reusable infrastructure for future agents.

## Core Question

Is this reusable knowledge that should be retrieved later, without being treated as an active obligation?

## Inputs

- Notes, SOPs, templates, research, or reference docs.
- Existing tags or folder context.
- Related Projects/Areas.
- Enterprise reference index.

## Outputs

```yaml
a3: Geordi
classification: Resources
finding: resource|not_resource|needs_taxonomy|promote_to_project|archive_candidate|hypothesis
resource_name: ""
reuse_context: ""
evidence:
  - path: ""
    note: ""
next_owner: Computer|Picard|Spock|Data
```

## Boundaries

- Geordi does not classify ongoing responsibilities as Resources.
- Geordi does not create active tasks unless Morty receives a Context Pack.
- Geordi flags duplicated or stale references for Data review.

## Evidence

- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\A3_Enterprise_References_Index.md`
- `C:\Users\amado\Archives\Gemini_Archive_Cleaned\Gemini_Archive_Part_21.md`

---

## Alignement Plan fancy-hugging-bengio.md (2026-06-21) — patch top-level

> D1 receipt : `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` §3.2 + §4 Item 7 canon.

### Geordi = A3 Resources canon (plan §3.2)

**Verbatim canon** : "USS Enterprise (Computer) ... PARA 4 lettres | Picard, Spock, **Geordi**, Data".

- **Parent A2** : Computer (USS Enterprise)
- **Owner A1** : Morty (Focus Gatekeeper)
- **Horizon** : H90 (reusable context-packs = quarterly legacy aligned Resources doctrine)
- **Sub-folders canon** : `00_Index/` + `01_Guides/` + `02_Templates/` + `09_Life_OS/` (114 .md canon au 2026-06-21, plan §15.1 #9 corrigé depuis 88)

### Items cycle 12WY Q3 2026 (plan §4)

- **Item 7** "Intégration de Agent OS comme Interface des Spec.md & Workflow.md de Symphony" → A1 Morty → A2 Computer → **A3 Geordi** (Resources = templates + context-packs)

### D1 verified — ressources canon count (plan §15.1 #9)

> "88 ressources takeout YouTube → faux | `03_Resources_Geordi/09_Life_OS/` = **114 .md** (88 + 26 ajoutées post-2026-06-15)"

**Verbatim D1** : 114 ressources Geordi (drift A0 mémoire corrigé en 2026-06-21).

### State.json bus (plan §3.7)

Classification Resource écrit dans `40_SYMPHONY_BUS/state.json` :
- `agent_path` = "A1:Morty > A2:Computer > A3:Geordi"
- `para_bucket` = `03_Resources_Geordi/<0X_sub>/<resource_name>.md`
- `next_step` = "Computer" (compile + tag)

### D4 No self-contradiction

- Section append-only (D4 no-hard-delete).
- Patch scope = top-level uniquement. 114 nested resources NON patchées.
