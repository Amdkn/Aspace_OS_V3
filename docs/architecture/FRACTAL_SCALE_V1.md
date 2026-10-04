# Fractal Scale Contract v1

Status: CANONICAL
Origin: #513
Program: #512 / Project V2 #8

## Principle

M0/M1/M2 are **relative to the boundary of an object**, not absolute global ranks.

- **M0 — Macro**: the whole organism, world, product, or capability family at its own boundary.
- **M1 — Meso**: organs, districts, workflows, bounded subsystems inside that organism.
- **M2 — Micro**: primitives, cells, actions, components, effect-level units.

A whole M0 object may be consumed as M1 or M2 inside another M0 object.

Therefore:

```
IntrinsicScale != ProjectedScale
```

## Projection contract

```yaml
FractalProjection:
  object_id:
  object_type:
  intrinsic_scale: M0|M1|M2
  projected_into:
  projected_scale: M0|M1|M2
  relation_type:
  parent_projection_ref:
  evidence_refs: []
```

## Examples

- CubeFarm intrinsic M0 → projected into StarNet as M1 Factory District.
- StarNet Room intrinsic M1 → projected into CubeFarm as M2 Portal/Crew Habitat.
- Reflex Fabric intrinsic M0 capability family → projected into an S3 holon as an M2 fast-decision primitive.
- Agent OS intrinsic M0 product → projected into Life/Business as an M1 capability/projection membrane.

## Invariants

1. Scale never determines institutional rank or authority.
2. Projection never changes identity.
3. Projected scale may change without rewriting the source object.
4. One object may have several simultaneous projections.
5. Consequential cross-surface effects preserve correlation, authority, evidence and return routing.
6. "Macro", "Meso" and "Micro" are architectural coordinates, not identity ontology.

## Use

Every cross-product composition should state both:
- intrinsic scale;
- projected scale.

Avoid shorthand such as "CubeFarm is M1" without a projection context.
