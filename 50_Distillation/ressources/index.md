---
type: Bundle index
title: ressources — Concepts distillés de 03_Resources_Geordi
description: Sous-bundle de la distillation d'ASpace OS V3. 26 concepts OKF v0.2 couvrant la racine KB Geordi, la Constitution 2026-07-12, l'architecture L0/L1/L2, le routage 6 branches, les jonctions NTFS et doctrines opérationnelles. Couverture partielle déclarée (47 lus / 48 378 disponibles).
tags: [distillation, okf, ressources, geordi, kb]
generated: { by: minimax-m3, at: 2026-08-17T21:40:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T21:40:00Z }
sources:
  - id: rapport
    resource: "50_Distillation/_briefs/RAPPORT_ressources.md"
    title: "Rapport obligatoire de la passe"
    last_modified: 2026-08-17
  - id: substrat
    resource: "50_Distillation/_substrat/03_Resources_Geordi.jsonl"
    title: "Substrat JSONL du seau"
    last_modified: 2026-08-17
  - id: methode
    resource: "50_Distillation/METHODE.md"
    title: "Méthode de distillation"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# ressources — Concepts distillés de 03_Resources_Geordi

> **Couverture partielle déclarée** : 47 fichiers `.md` lus en profondeur sur 48 378
> disponibles (0,097 %). Voir le [rapport obligatoire](../_briefs/RAPPORT_ressources.md)
> pour la liste exacte de ce qui n'a pas été couvert et les contradictions sans arbitrage.

## Files

### Backend — piliers KB, registres, infra

- [OKF v0.1 — standard de format d'un bundle mémoire](okf-v0-1-format-standard.md) - Le 4ᵉ pilier : ce qu'est un bundle valide (frontmatter, fichiers réservés, consommation permissive).
- [Wiki schema LLM — trois couches raw/wiki/schema.md](wiki-schema-llm-wiki.md) - Trois couches physiques, six types de pages, trois workflows (ingest/query/lint), conventions de nommage et cross-refs Obsidian.
- [Geordi KB — quatre piliers OKF/Wiki/Graphify/Dox](geordi-kb-quatre-piliers.md) - Carte d'accès canonique depuis la racine Geordi + algorithme de routage à 5 branches + correctif OKF du 2026-08-01.
- [Second Brain PARA — 14 sous-dossiers de Geordi](second-brain-14-sous-dossiers.md) - Cartographie mesurée 2026-08-02 (table de vérité 14 ↔ PARA ↔ strate S0→S4 + décisions D-2026-08-01-#1..4).
- [Rot-rates S0→S4 — politique de péremption par strate](rot-strates-s0-s4.md) - Opérer le rot ligne à ligne ; règles de transition S1→S2→S3→S4 ; cardinalités mesurées par strate.
- [Wiki routing par question — 6 branches canoniques](wiki-routing-by-question.md) - Algorithme de routage déterministe (OKF/Wiki/Graphify/Dox/Index/ROT) + pourquoi OKF a été oublié puis rétabli.
- [TAGS — registres Owner (Star Trek) + Shelf (Doctor Who)](tags-registres-owner-shelf.md) - 8 tags totaux ; Owner v2 = 6 valeurs, Shelf = 10 valeurs scoped aux guides `00_KERNEL_OS/`. `description:` est bloquant pour `RESOURCES_INDEX.md`.
- [Supabase Sovereign — multi-tenant RLS par JWT custom claim](supabase-rls-multi-tenant.md) - Topologie Caddy↔Kong, custom_access_token_hook, fonction `current_org_id()`, politiques RLS déterministes.

### Concept — notions pivots

- [Constitution A'SPACE v1.0 — loi suprême](constitution-aspace-v1.md) - 8 articles ratifiés 2026-07-12 (orientation, maximiseur, superviseur, auto-amélioration, GC doctrinal, blocage interdit, réversibilité, version append-only).
- [Souveraineté — trois niveaux (infra, code, mémoire)](sovereignty-3-niveaux.md) - Principe directeur L0 (Rick) ; Trust Zone ADR-007 + ADRs immuables + TARDIS ; loi du checkpoint profond.
- [Matryoshka A'Space OS — L0/L1/L2 emboîtés](matryoshka-l0-l1-l2.md) - Architecture poupée russe : grammaire A1/A2/A3 partagée, adaptée au registre de souveraineté ; A0 = Pilot.
- [Life OS — six vaisseaux L1 et leurs frameworks](life-os-six-vaisseaux.md) - Orville (Ikigai) · Discovery (Life Wheel) · SNW (12WY) · Enterprise (PARA) · Cerritos (GTD) · Protostar (DEAL).
- [L2 Fractal B1/B2/B3 — Command Stack](l2-fractal-b1-b2-b3.md) - Direction (Jerry/Summer) · Domaines (8 héros) · Exécution (8 squads Marvel) ; miroir fractal macro↔micro ; ruling A0 2026-06-02.
- [Shadow L1/L2 Homologie 4-méthodes](shadow-l1-l2-homologie.md) - Mesmo grammaire PARA/12WY/GTD/DEAL projetée sur instruments cloud (Notion/Airtable/ClickUp) vs souverains (Obsidian/Baserow/Plane).
- [Compounding Knowledge — pourquoi un wiki LLM bat RAG](compounding-knowledge-wiki.md) - Le principal reste, les rendements sont réinvestis, le temps amplifie ; LLM élimine le goulot de maintenance.

### Identity + Doctrine canonique

- [AGENTS.md — canon absolu d'identité](agents-md-identity-canon.md) - Gouverne l'identité (vs Constitution qui gouverne le comportement) ; registre Owner arbitré 2026-08-01.
- [A3 Geordi — Resources Officer (spec & mission)](a3-geordi-resources-officer.md) - Spec A3, registres Owner, anchoring plan fancy-hugging-bengio, état canonique 14 sous-dossiers.
- [ADR — Architecture Decision Records (Rick's Law)](adr-immutability-ricks-law.md) - Canon juridique Rick ; immuable ; nouvelles décisions = nouveaux ADRs. Tension avec Constitution Article 5.
- [SDD — System Design Documents (couche design)](sdd-system-design-documents.md) - 10 SDDs canoniques (SDD-000..007 + 000b/c) ; format SDD ; localisation VPS/local/wiki raw.
- [Canon Tripartite des Blueprints (ADR-FWK-021)](blueprints-canon-tripartite.md) - 3 canons isomorphes L0/L1/L2 (12_Blueprints\28_Blueprints\09_Blueprints\), 4 sous-dossiers identiques, _SPECS\ devient inbox.

### Relation — gouvernance opérationnelle

- [A'Space Governance Dashboard — console unifiée VPS](aspace-governance-dashboard.md) - `aspace-dashboard.148.230.92.235.sslip.io` (Next.js / Caddy) ; règle canonique « plus de dashboards isolés ».

### Entity — acteurs canoniques

- [Roster canon 8 Domaines L2 — Notion prime AGENTS.md (ADR-CANON-001)](l2-8-domaines-roster-canon.md) - 53 membres sur 8 squads B3 (Growth/Sales/Product/Ops/IT/Finance/People/Legal) ; ruling A0 2026-06-02 sur les divergences.

### Playbook — guides outillés

- [Geordi — cartographie des 159 jonctions NTFS](geordi-junctions-map-159.md) - 10 catégories de risque ; 3 classes de danger concrètes pour la migration V3 ; recommandations walk.
- [NotebookLM Bridge — contourner DBSC par Chromium persistant](notebooklm-bridge-dbsc.md) - Solution validée Antigravity 2026-05-20 ; pourquoi `notebooklm-mcp.exe` ne marche PAS ; commandes bridge.
- [Loi du harvest — wiki evergreen depuis artefact shippé](loi-du-harvest-wiki.md) - Sister artifact obligatoire ; skill canon `/harvest` ; anti-patterns ; tension Constitution Article 6 (pas de blocage).

### Filesystem

- [NTFS Junction Aliasing (ADR-FS-001) — short-path operability](ntfs-junction-aliasing.md) - PARA = SSOT exposé via junctions ; 3 couches d'aliasing (sentinelles `_\`, drives subst, junctions sectorielles) ; pièges filesystem.

# Directories

- Ce sous-bundle se lit en deux temps : (1) `geordi-kb-quatre-piliers.md` puis
  `wiki-routing-by-question.md` donnent la carte, (2) les autres concepts sont les
  noeuds réutilisables dans un graphe RDF ultérieur.
