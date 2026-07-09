# Shadow A0 — Symphony Adapters

> **Lieu** : `00_Amadeus/05_OSS_Twin/symphony/` (Shadow A0)
> **Date** : 2026-05-13
> **Statut** : Pré-configuration A0 — **hors canon SDD, hors Airlock**
> **Veto** : Aucun de ces documents ne sera promu en SDD. Les 12+1=13 SDDs sont scellés.

---

## 1. Pourquoi ce dossier existe

Ces documents sont des **Shadow Frameworks pré-configurés** au sens strict de SDD-000c :

> *"Le système ne peut pas se lancer lui-même. A0 existe en dehors du système, équipé de Shadow Frameworks pré-configurés, pour allumer la machine avant qu'elle soit auto-hébergée."*

Ce sont les **outils personnels d'A0** pour piloter A'Space OS sans devenir lui-même technicien. Ils n'appartiennent ni à L0 (Rick), ni à L1 (Beth/Morty), ni à L2 (Jerry/Summer). Ils appartiennent à **A0 hors-univers**.

## 2. Contexte stratégique — SDD-010 et la fin de la souveraineté absolue

SDD-010 = **le méta-SDD de cette session**, la 13ème semaine de l'année des 12 semaines. Sa leçon :

> *"J'en ai fini avec mon souhait de Souveraineté Absolue, même si j'ai manqué de construire un empire sur du sable mouvant — mon Serveur qui est toujours à 100% plus de 2 jours maintenant."* — Amadeus, 2026-05-13

**Conséquence opérationnelle** :
- Cycle H1 = **12 semaines + 1** (la 13ème = revue Meta / promotion V0→V1 Muse)
- V0 = ce qui existe actuellement (sable mouvant compris)
- V1 cible = Antifragile + Souverain (sans le "Absolu") + Durable
- **Plus aucun nouveau SDD ne sera créé pendant 90 jours.** Veto absolu. 12+1 SDDs scellés.

## 3. Doctrine Symphony dans A'Space OS

Symphony (`printingpress.dev`) remplace n8n post-SaaSApocalypse. Différence clé :
- **n8n** = workflow visuel rigide, self-host pénible
- **Symphony** = orchestrateur agentique frugal, OpenAI open-source compatible

### Position dans la pyramide A'Space

```
A0 (Shadow A0 — ce dossier)
    │
    ▼
B1 — Symphony Router (Jerry-niveau)
    │ Lit les trackers + génère le Payload JSON SOC
    │ Outils possibles : Symphony OSS, MiniMax 2.7, GLM 4.7 Flash
    ▼
B2 — Hermes Kanban (Justice League DC + Marvel orchestration)
    │ Découpe en pipelines, gère Circuit Breakers
    ▼
B3 — Paperclip Execution (Marvel Squads — exécutants Clean Slate)
    │ Skills MCP → conversion en CLI par la Forge de Clara (12ème Doctor)
    │ via CLI Printing Press + CLI Anything
    ▼
Trackers (les 7 adapters de ce dossier)
    L0 : tooling open (KE, Tines, etc.) — possibilités à évaluer
    L1 : Plane / Baserow / Obsidian / Affine (Shadow L1 de SDD-008)
    L2 : Airtable / ClickUp / Notion (Shadow L2)
```

### Principe de frugalité (Sobriété Intelligente)
- **OpenHarness ne doit pas devenir le goulot d'étranglement** — c'est Rick A1 + Donna DLQ, point.
- **Symphony en B1 = Jerry-niveau** (orchestration commerciale), mais NE remplace pas la fractal Summers.
- **B2 et B3 doivent rester commodity** — communication par CLI (Clara forge), pas par MCP lourd.
- **Coût compute cible** : MiniMax 2.7 ($20/4500/5h = 10% touché en usage manuel intensif) ou GLM 4.7 Flash sur OpenRouter (100× moins cher que Claude/GPT).

## 4. Protocole TARDIS Inversé pour le lancement L1 (rappel)

Ordre de boot pour activer L1 Life OS de Beth :

```
1. 13ème Doctor (L0.3 Kernel Core)  — Yaz/Ryan/Graham stabilisent VPS
2. 12ème Doctor (L0.2 Forge Core)   — Clara forge MCP → CLI
                                      Bill architecture BMAD
                                      Nardol everything-claude-code
3. 11ème Doctor (L0.1 Life Core)    — Amy UI + Rory SQL + River Agent Portal
                                      ↓
4. A1 Beth                          — A2 Ikigai (4 Piliers & 5 Horizons)
   A1 Morty                         — A2/A3 : 12WY, PARA, GTD, DEAL
                                      ↓
5. L2 = poupée russe (3ème couche)  — Dans Areas/Projects PARA
                                      Directive 12WY sous Ikigai+LifeWheel
                                      8 Domaines roue de la vie
                                      Décomposition 1/4 H1 → H90
                                      Airlock d'Organisation
                                      Objectif Muse V0 → V1 en S13
```

## 5. Roadmap des 8 Adapters

| # | Tier | Tool | Statut | Complexité | Notes |
|---|------|------|--------|------------|-------|
| 1 | L1 | **Plane.so** | ✅ Spec écrite | Faible | Linear-compatible, GraphQL similaire, **proof of concept** |
| 2 | L1 | Baserow | ✅ Spec écrite | Faible | API REST simple, 3 tables 12WY canoniques, Token auth |
| 3 | L1 | Obsidian | ✅ Spec écrite | Moyenne | Local REST API plugin + MANIFEST.md frontmatter + Tasks mode |
| 4 | L1 | Affine | ✅ Spec écrite | Moyenne | GraphQL + Database Blocks, Edgeless Blueprints DEAL, API WIP |
| 5 | L2 | Airtable | ✅ Spec écrite | Faible | REST + webhooks (7j expiration), Growth/Sales/Finance slot |
| 6 | L2 | ClickUp | ✅ Spec écrite | Moyenne | API v2 + Build Gates + custom fields SLA, Ops/Product/IT slot |
| 7 | L2 | Notion | ✅ Spec écrite | Moyenne | Database Query + compound filters, polling-only, People/Legal slot |
| 8 | L2 | **Google Sheets** | ✅ Spec écrite | Faible | GWS CLI natif (gws), **Capture brute & Serendipity (YouTube Pipeline)** |

**Priorité de production** (proposé) :
1. **Google Sheets (GWS)** (Vague 2) — Ingestion et capture brute YouTube.
2. **Plane** (fait) — modèle de référence pour le raffinage GTD.
3. **Obsidian** — organisation en fichiers Markdown.
4. **Affine** — revue visuelle des idées et des workflows.
5. **Airtable** — webhook natif = polling moins coûteux, slot Lead/Sales/Finance.
6. **ClickUp** — slot Ops/Product/IT.
7. **Notion** — slot People/Legal.
8. **Baserow** — fait nativement le 12WY Warp Core (Curie).

## 6. Spécification Master

Tous les adapters héritent de `symphony-base.spec.md` qui généralise la spec Symphony de `printingpress.dev` :
- Garde l'architecture (WORKFLOW.md, Orchestrator, Workspace Manager, Agent Runner)
- Remplace les hypothèses Linear-spécifiques par des abstractions Tracker
- Ajoute les hooks A'Space : SLA/SOA/SOC, Donna DLQ, TARDIS Inversé, Skills MCP→CLI Clara

Chaque adapter = `symphony-<tool>.spec.md` qui ne documente QUE :
- Les spécificités de l'API du tracker
- Les états du tracker mappés aux états Symphony
- Les hooks particuliers (par exemple : Plane Cycles → Baserow Weeks)
- Le coût d'exploitation (polling fréquence × tarification API)

## 7. Hors-scope explicite

Ce dossier ne contient pas :
- ❌ **Pas de SDD** (veto absolu — les 13 sont scellés)
- ❌ **Pas d'ADR** (les ADRs canon vivent dans `_SPECS/ADR/`)
- ❌ **Pas de Airlock pipeline** (Plane → Obsidian → Affine est de SDD-008, pas d'ici)
- ❌ **Pas de PRD ou DDD ou TDD** (ceux-là viendront en Phase 2 quand un adapter est validé en usage)

## 8. Critère de promotion (si jamais)

Un adapter Shadow A0 peut un jour devenir :
- Un **PRD** dans `_SPECS/PRD/` si son usage prouve qu'il mérite d'être codifié dans le canon
- Un **plugin** OpenHarness si son code mérite d'être partagé
- Un **ADR** si une décision d'architecture émerge de son usage

**Critère** : minimum 3 semaines d'usage continu en production (graduation MUSE de SDD-008).
Tant que ce critère n'est pas atteint, ces docs vivent dans Shadow A0 sans pression.
