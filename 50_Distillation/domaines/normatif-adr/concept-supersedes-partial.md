---
type: Concept
title: Supersedes partiel — quand un ADR invalide seulement une section d'un autre
description: Certains ADR supersedent partiellement un autre (ex : ADR-OMK-004 supersede §Deploy de ADR-OMK-001 mais laisse vivre §runtime amendé). Le triplet supersedes exige une portée explicite.
tags: [adr, supersedes, partiel, amend, omk]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-OMK-004
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-OMK-004_pivot-supabase-cloud-vercel.md"
    title: OMK 004 — supersedes partiel canon
    last_modified: "2026-06-19"
  - id: ADR-ABCOS-002
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-ABCOS-002_pivot-supabase-cloud-vercel.md"
    title: ABCOS 002 — supersedes partiel
    last_modified: "2026-06-19"
okf_version: "0.2"
---

# Supersedes partiel — quand un ADR invalide seulement une section d'un autre

## Résumé

Un **supersedes partiel** est un ADR qui **invalide une section précise** d'un autre ADR, sans toucher au reste. C'est une opération courante dans le canon A'Space, mais elle exige une discipline rigoureuse pour éviter la perte d information.

## Les deux exemples canon

### Exemple 1 : `ADR-OMK-004` supersede `ADR-OMK-001` (partiel)

Le frontmatter de `ADR-OMK-004` dit explicitement :

> `supersedes: "ADR-OMK-001 (deploy section D1-D4: Dokploy → Vercel) + ADR-SUPABASE-001 (hosting: self-host VPS → Supabase Cloud). OMK-001 §runtime AMENDED 2026-06-19 : single-mode SaaS only (VITE_APP_MODE=saas), internal mode retired per Condition A = A1 (A0 directive)."`

Ce que cela signifie :

| Section de OMK-001 | Verdict OMK-004 |
|---|---|
| §Deploy D1-D4 (Dokploy) | **supersedé** par OMK-004 |
| §Runtime (VITE_APP_MODE baked) | **amendé** (internal mode retiré) |
| Autres sections | **inchangé** |

OMK-001 reste canonique, mais son §Deploy est mort et son §runtime est amendé.

### Exemple 2 : `ADR-ABCOS-002` supersede `ADR-ABCOS-001` (partiel)

Le frontmatter de `ADR-ABCOS-002` :

> `supersedes: "ADR-ABCOS-001 (hosting: self-host VPS → Supabase Cloud). Does NOT supersede ABCOS-001 §multi-tenant (org_id + RLS) which is still valid; nor D10 mixed-tenancy model."`

Ici la discipline est encore plus stricte : **ce qui n'est pas supersedé est explicitement nommé**. La liste négative est plus informative que la liste positive.

## Le piège pour les triplets RDF

Le verbe `supersedes` au sens strict affirme qu'un document en invalide un autre **en entier**. Un supersedes partiel exige :

1. Soit un champ `portée` dans le triplet (`"objet_portee": "§Deploy D1-D4"`),
2. Soit un triplet séparé avec un verbe `amends` ou `partialSupersedes`,
3. Soit un document de référence qui explicite le périmètre.

Le format OKF v0.2 triplets admet l'option `objet_portee` en champ additionnel (hors verbes canoniques).

## Statut vis-à-vis de V3

**canon**. Le supersedes partiel est une doctrine appliquée. Aucun cas n'a été trouvé où elle aurait été mal gérée (la lecture du corps confirme toujours la portée).

## Le verdict de cette distillation

**canon**. Le pattern est sain. La discipline d'explicitation de la portée est l'élément clé.

## Liens

- Voir aussi : `concept-amend-pattern.md` (les AMEND)
- Voir aussi : `concept-adr-format.md` (le format général)