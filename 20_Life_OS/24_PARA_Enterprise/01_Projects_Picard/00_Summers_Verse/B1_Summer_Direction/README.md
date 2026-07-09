---
id: B1_SUMMER_DIRECTION
layer: L2_Business_Pulse
role: B1_Project_Direction
status: SHADOW_ACTIVE
created: 2026-05-21
---

# B1 Summer Direction

B1 Summer Direction is the local project CEO layer. It translates a clarified Jerry idea into a project charter that the B2 DC managers and B3 Marvel squads can execute.

## Required Fields

```yaml
summer_id: <project_slug>
parent_jerry_area: <path>
icp_variant: Solaris|Nexus|Orbiter|Other
rock_link: <12WY rock or NEEDS_ROCK>
week_range: W1-W12
beth_status: GREEN|ORANGE|HALT
definition_of_done: <artifact-based DoD>
forbidden_actions:
  - bypass_beth
  - create_work_without_artifact
  - mutate_provider_config_without_signoff
```

## Output Packet

```yaml
agent: Summer
layer: B1
decision: open|pause|route_to_domain|needs_a0|needs_beth
target_domain: Growth|Sales|Product|Ops|IT|Finance|People|Legal
artifact_required: true
proof_path: C:\...
```

## Boundaries

- Summer does not own ongoing Areas; that is Jerry/Spock.
- Summer does not archive; completed Projects route to Data after documentation.
- Summer does not launch growth if Batman/Ops is red or Beth is HALT.
