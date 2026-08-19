# Tech OS — Index des concepts (couche 10_Tech_OS)

15 concepts extraits du corpus 10_Tech_OS de la V2 (97 fichiers `.md` écrits à la main, classés en 5 zones).

## Files

- [Loi L0 — Souveraineté, anti-fragilité, sobriété, idempotence](loi-l0.md) — Quatre principes fondateurs qui cadrent toute doctrine Rick's Verse. Axiome 0 qui justifie ou refuse tout autre choix.
- [Caste Doctor Who — A1 Rick / A2 Doctors / A3 Companions](caste-doctor-who.md) — Hiérarchie des agents Tech OS dérivée du lore Doctor Who. Un Visionnaire, trois Managers, neuf Compagnons spécialisés.
- [TARDIS Inversé — ordre d'invocation Kernel d'abord](tardis-inverse.md) — L0.3 Kernel Core (13ème Doctor) avant L0.2 Forge (12ème) avant L0.1 Life Core (11ème). Correction architecturale SDD-001 §3.
- [Doctrine MCP — six serveurs canoniques production](mcp-doctrine-six.md) — hostinger, github, dokploy, vercel, supabase, graphify. DOX framework AGENTS.md hiérarchique comme contrat de travail.
- [Vault-tier pattern — secrets en env vars Windows](vault-tier-pattern.md) — Toutes les clés MCP et tokens vivent dans les variables d'environnement Windows User scope, jamais versionnés. Rotation policy trimestrielle.
- [DOX — AGENTS.md hiérarchique comme contrat de travail](dox-framework.md) — Framework d'AGENTS.md immuable. Root > Child > Leaf. Anti-panique par lecture obligatoire avant édition.
- [Capabilities A3 — Yaz / Ryan / Graham / Bill / Clara / Nardol / Amy / Rory / River](capabilities-doctors-13-12-11.md) — Neuf agents compagnons Tech OS en trois triades, leurs MCP et leurs outils interdits.
- [Symphony bus remplace N8N](symphony-bus-replace-n8n.md) — Orchestration L0 file-based. Tick 8 phases (WAKE → SLEEP). N8N legacy depuis 2026-05-26.
- [Trois axiomes antifragiles — RAW, dégradation gracieuse, mémoire procédurale](axiomes-antifragilite-k1-k4.md) — Axiome 1 Read-After-Write, Axiome 2 mode dégradé, Axiome 3 Pattern × 3 → Skill.
- [Taxonomie des 8 paniques Framework + Kernel](paniques-k1-k4-kernel.md) — 4 Framework (approval, budget, DM pairing, WS timeout) + 4 Kernel (filesystem, hallucination, secret leak, dead kernel). Chaque panique a un antidote.
- [Junction-based aliasing — un owner, N vues](junction-aliasing-fs001.md) — Architecture filesystem souveraine via NTFS Junctions (mklink /J). 3 couches : sentinelles `_\`, drives subst, junctions fonctionnelles.
- [Loi des 3 — pyramide documentaire SDD/PRD/ADR/DDD/TDD](loi-des-3-pyramide-documentaire.md) — Cascade : 1 SDD → 3 PRDs → 3 ADRs → N DDDs → 1 TDD par DDD avant code.
- [Shadow L0 manuel — triade Claude / GPT-Codex / Gemini](shadow-l0-triade-ia.md) — Avant l'automatisation Hermes, A0 opère via 3 IA par capability, pas par couche. Capability routing, pas model routing.
- [Doctrine de la 13ème Semaine](13eme-semaine-doctrine.md) — Pause méta entre cycles 12WY. 5 critères de déclenchement d'exception. Veto SDD 90 jours jusqu'au 2026-08-11.
- [Pyramide de souveraineté L0 ≥ L1 > L2 + ratio 50/30/20](sovereignty-tier-pyramid.md) — Hiérarchie d'autorité et règle de répartition temporelle d'Amadeus. Beth Veto. 3 lois fondamentales.

## Sources canoniques

- `C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/`
  - `00_Governance_Rick/` — Loi L0, Sobriété, VPS Audit, VPS Keys, Drivers A1/A2 × 3
  - `11_Infra_13th_Doctor/` — 16 fichiers, dont `06_MCP_Mastery/` (DOX) et `06_MCP_Mastery_dox/` (framework)
  - `12_Interface_11th_Doctor/` — 5 fichiers (Amadeus, Rory, River, Amy, IDENTITY)
  - `13_Data_12th_Doctor/` — 6 fichiers (Clara, Nardol, Missy, Bill, Clara_ETL)
  - `12_Blueprints/` — 26 fichiers (SDD canoniques + ADR filesystem)
- Carte : `C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat_domaines/CARTE_10_Tech_OS.md`
- Substrat : `C:/Users/amado/ASpace_OS_V3/50_Distillation/_substrat_domaines/10_Tech_OS.jsonl`

## Méthode et triplets

- Méthode : [`60_Implementation_Méthodologiques/domaines/tech.md`](../../../60_Implementation_Méthodologiques/domaines/tech.md)
- Triplets : [`70_Onthologies/triplets/dom-tech.jsonl`](../../../70_Onthologies/triplets/dom-tech.jsonl)