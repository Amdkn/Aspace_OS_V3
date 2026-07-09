# SDD-009 — Shadow L2 Business OS : La Matrice Souveraine 3×8

**Date :** 2026-05-13
**Auteur :** A0 Amadeus (via Claude Architect) — direct ratifié sans brainstorm
**Statut :** RATIFIÉ — 9ème SDD de la pyramide A'Space OS V0
**Numéro :** SDD-009 (préparé par libération du slot SDD-008 → ADR-RICK-001)
**Portée :** L2 Business Pulse — Jerry & Summer fractal — Justice League DC + Marvel Squads
**Source matière :** Gemini Takeout 2026-05-07 (lignes 6280–7720) + doctrine Amadeus 2026-05-13
**Relation amont :** SDD-005 (Life OS L1 — cible) + SDD-006 (Business Pulse L2 — pyramide) + SDD-007 (SOB Factory ICP Variants) + SDD-008 (Shadow L1 — moyen)
**Relation aval :** SDD-010 (Meta — clôture scope)

---

## 0. Le Théorème de SDD-009 en une phrase

> **"Le L2 Business souverain se construit en Shadow Cloud avant le self-hosted, sur 3 outils (Airtable / ClickUp / Notion) qui structurent chacun les 8 domaines de la Roue Business mais n'en utilisent pleinement qu'un sous-ensemble — les autres restent structurés et dormants pour assurer la continuité contextuelle et l'antifragilité."**

C'est l'application **inverse mais symétrique** de SDD-008 (Shadow L1) au niveau Business.

---

## 1. Contexte et Bootstrap Paradox du L2

### 1.1 Le problème que SDD-009 résout

SDD-005 décrit la cible (Life Web OS souverain). SDD-006 décrit la pyramide L2 abstraite (Jerry/Summer, 8 secteurs DC, Marvel squads). SDD-007 décrit les 3 ICPs commerciaux (Solaris/Nexus/Orbiter).

**Mais aucun de ces 3 SDDs ne dit COMMENT démarrer la production de valeur L2 SANS attendre que le bare metal soit prêt.**

→ **SDD-009 fournit le chemin Shadow** : démarrer immédiatement avec Airtable + ClickUp + Notion comme **substrate cloud du L2**, calibré par les contraintes SOA/SOC/SLA, en mode Shadow Mode (Phase Gamma — cf. SDD-007).

### 1.2 La leçon Beth Veto

Du 4 au 12 mai 2026, l'Amiral a passé son temps en L0 (bedrock) au lieu de L2 (production de valeur). Le serveur VPS est resté à 100% CPU pendant 32+ heures (cf. ADR-RICK-001 historique). **Beth Veto Absolu** a été déclenché : "Produis maintenant en Cloud, code après quand tu sais que ça marche."

→ SDD-009 est l'**autorisation architecturale** de produire en cloud sans honte ni dette technique implicite.

---

## 2. La Trinité Stratégique SLA / SOA / SOC

(Extrait verbatim du Gemini Takeout 2026-05-07 17:02 — ligne 6294)

### 2.1 Le Théorème Fondamental

| Couche | Nature | Définition exacte |
|---|---|---|
| **SOA** (Service-Oriented Architecture) | **L'Espace** | Les 8 Domaines de la Roue Business sont des **forteresses isolées**. Aucune DB partagée. Chaque domaine a son propre schéma Supabase avec RLS strict. Superman (Growth) ne peut PAS lire les tables de Wonder Woman (Finance). |
| **SOC** (Service-Oriented Communication) | **Le Langage** | Les domaines ne se "parlent" pas. Ils s'échangent des **Payloads JSON auto-porteurs** via Symphony Router (B1). Format strict, schema validé par Zod/Pydantic à chaque frontière. |
| **SLA** (Service Level Agreement) | **Le Temps & l'Énergie** | Chaque Payload SOC embarque ses propres **contraintes mathématiques** : `max_execution_time_minutes`, `max_compute_budget_usd`, `max_retry_loops`. Pas un rapport mensuel a posteriori — un **disjoncteur actif** au runtime. |

### 2.2 Format canonique du Payload SOC

```json
{
  "mission_id": "PRD-904",
  "target_soa_domain": "Product_Forge",
  "context_pack_url": "urn:solaris:rag:client_42_brandbook",
  "soc_instructions": {
    "goal": "Générer 3 articles SEO Biomimétiques",
    "forbidden_lexicon": ["synergie", "disrupter", "innover"]
  },
  "sla_constraints": {
    "max_execution_time_minutes": 120,
    "max_compute_budget_usd": 1.50,
    "max_retry_loops": 2
  },
  "trace_id": "uuid-v4-pour-Panopticon-Ops",
  "source_tracker": "clickup://t/abc123",
  "priority": 2
}
```

### 2.3 Les 3 SLA Sentinelles

| Type | Gardien (Marvel/DC) | Règle |
|---|---|---|
| **SLA Temporel** | The Thing (Ops/Fantastic 4) | Dépassement 80% `max_execution_time` → freeze worker + escalade A0 via ClickUp ticket |
| **SLA Financier** | Wonder Woman (Finance/Thunderbolts) | API Costs Paperclip à chaque Heartbeat → kill instance si proche `max_compute_budget` → **éradique le Margin Bleed** |
| **SLA Qualitatif** | Captain America (Product QA/Avengers) | Évalue contre `forbidden_lexicon` + DoD → après 2 rejets → admet que prompt/SOP défectueuse, bloque |

---

## 3. L'Architecture Tri-Tier B1 / B2 / B3

### 3.1 Diagramme de flux complet

```
┌─────────────────────────────────────────────────────────────────────┐
│  Source événement externe                                            │
│  (Stripe payment, formulaire Airtable, brief ClickUp, etc.)         │
└─────────────────────────────────┬────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│  B1 — Symphony Router (Jerry-niveau)                                │
│  Outil : Symphony (printingpress.dev) + MiniMax 2.7 / GLM 4.7 Flash │
│  Rôle : Capter événement → forger Payload SOC → router vers B2     │
│  Note : Remplace n8n post-SaaSApocalypse. Self-hostable, frugal.    │
└─────────────────────────────────┬────────────────────────────────────┘
                                  │
                                  ▼ Payload JSON SOC validé Zod
┌─────────────────────────────────────────────────────────────────────┐
│  B2 — Hermes Kanban Workspace (Summer-fractal)                      │
│  Outil : Instances locales Hermes par domaine (port 3101+N)        │
│  Rôle : DC Justice League Managers — découpent en pipelines,       │
│  appliquent Circuit Breakers, gèrent Structured Handoff            │
│                                                                     │
│  Superman │ Flash │ Batman │ Wonder Woman │                        │
│  John Jones │ Cyborg │ Green Lantern │ Aquaman                     │
└─────────────────────────────────┬────────────────────────────────────┘
                                  │
                                  ▼ Sub-Payloads SOC + Skills MCP/CLI
┌─────────────────────────────────────────────────────────────────────┐
│  B3 — Paperclip Execution Clean Slate (Squad Marvel)                │
│  Outil : Paperclip Org Structure                                    │
│  Rôle : Exécutants éphémères, workspaces temporaires destructibles, │
│  Skills MCP→CLI strictes (via Clara/12th Doctor), Heartbeats       │
│                                                                     │
│  Gardiens de la Galaxie │ Illuminati │ Avengers │ Fantastic 4 │     │
│  Kang Dynasty │ Thunderbolts │ X-Men │ Eternals                    │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Non-goulot : OpenHarness reste Rick (A1), pas l'orchestre B1

(Conformément à la doctrine 2026-05-13 d'Amadeus)

| Couche | Rôle | Outil | Doit éviter |
|---|---|---|---|
| Rick (A1) | Souveraineté + Donna DLQ | OpenHarness (cf. ADR-RICK-001) | Devenir l'orchestrateur de toute la stack |
| Jerry (A1 L2) | Orchestration Business | **Symphony Router B1** | Devenir un goulot d'étranglement |
| Summer (A1 L2) | Fractal Marvel/DC | Hermes B2 + Paperclip B3 | Charger trop sur un seul vaisseau |
| Clara (A3, 12ème Doctor) | Forge MCP → CLI | CLI Printing Press + CLI Anything | Garder les MCP en transport lourd |

**Principe** : la communication B2 ↔ B3 doit être **commodité de transport** (comme l'électricité par cable), pas MCP lourd. Clara forge chaque MCP en CLI pour réduire le coût de transport et la latence.

---

## 4. Les 8 Domaines de la Roue Business (Matrice DC × Marvel)

(Extrait Gemini Takeout 7 mai + référence SDD-006)

| # | Domaine | A2 Justice League (Manager) | A3 Marvel Squad | Mission unique |
|---|---|---|---|---|
| 1 | **Growth** | Superman | **Gardiens de la Galaxie** (Groot, Mantis, Rocket, Star-Lord, Drax) | Scraping, scoring, copywriting, lead nurturing |
| 2 | **Sales** | John Jones (Martian Manhunter) | **Illuminati** | Margin Bleed Calculator, Demo Space Agent, Contract Generation |
| 3 | **Product** | Flash | **Avengers** (Spider-Man, Captain America QA, Iron Man) | Forge de contenu, SEO/Social, QA contre `forbidden_lexicon` |
| 4 | **Ops** | Batman | **Fantastic 4 + Doom** (Invisible Woman, The Thing, Human Torch, Mr Fantastic, Dr Doom) | Bouclier Build Gates, surveillance SLA, relances, audit |
| 5 | **IT/Infra** | Cyborg | **Kang Dynasty** | Dokploy MCP/CLI, Transcodage S3, Load Balancing |
| 6 | **Finance** | Wonder Woman | **Thunderbolts** (Taskmaster pricer, Baron Zemo token auditor + 3 TBD) | Margin Protection, Compute Budget Killer, Stripe sync |
| 7 | **People** | Green Lantern | **X-Men** | RAG Manager, Brand Books vectorisés, lexicons interdits |
| 8 | **Legal** | Aquaman | **Eternals** | Contrats, compliance, WHOIS, GDPR |

> **Note SDD-010 anticipée** : la constitution complète et détaillée des Marvel Squads (noms exhaustifs de chaque A3, leurs Skills MCP/CLI, leurs Bounded Contexts DDD) **n'entre PAS dans SDD-009**. C'est une dette explicitement reconnue, à traiter dans un PRD ultérieur (PRD-MARVEL-001) hors veto SDD.

---

## 5. La Matrice Shadow L2 3×8 (Doctrine Amadeus 2026-05-13)

### 5.1 Le principe

Les **3 outils cloud SaaS** du Shadow L2 :
- **Airtable** — relational, formulaires, webhooks natifs
- **ClickUp** — task tracking, QA Build Gates, statuts terminaux
- **Notion** — knowledge base, PARA, SOPs

…structurent **chacun les 8 domaines complets** de la Roue Business. Mais **chaque outil n'en utilise pleinement qu'un sous-ensemble** ; les autres restent **structurés et dormants** prêts à être réactivés contextuellement.

### 5.2 La matrice complète

| Domaine | Airtable | ClickUp | Notion |
|---|---|---|---|
| **Growth** | 🟢 PLEIN (Lead capture, scoring) | 🌙 dormant | 🌙 dormant |
| **Sales** | 🟢 PLEIN (CRM, pipeline) | 🌙 dormant | 🌙 dormant |
| **Finance** | 🟢 PLEIN (Margin, Stripe sync) | 🌙 dormant | 🌙 dormant |
| **Ops** | 🌙 dormant | 🟢 PLEIN (Panopticon, Build Gates) | 🌙 dormant |
| **Product** | 🌙 dormant | 🟢 PLEIN (QA workflow, DoD validation) | 🌙 dormant |
| **IT** | 🌙 dormant | 🟢 PLEIN (Incident, Infra tickets) | 🌙 dormant |
| **People** | 🌙 dormant | 🌙 dormant | 🟢 PLEIN (RAG sédimentaire, Brand Books) |
| **Legal** | 🌙 dormant | 🌙 dormant | 🟢 PLEIN (Contrats, compliance) |

### 5.3 Pourquoi cette redondance n'est PAS du gaspillage

1. **Antifragilité L2** : si Airtable tombe → ClickUp et Notion ont la structure miroir dormante prête à activer
2. **Continuité contextuelle** : selon ton mode de travail (Sales-Lun, Ops-Mar, People-Mer), tu vois TOUS les 8 domaines depuis l'outil principal — pas de switch
3. **Préparation migration** : quand le self-hosted est prêt (NocoDB / Plane / Affine ou Supabase native), la structure ×3 est déjà testée
4. **Symétrie fonctionnelle** : chaque outil garde aussi son **rôle fonctionnel** propre (DB / QA / Mémoire) — cf. §5.4

### 5.4 Architecture matricielle à 2 axes — superposition fonction × domaine

C'est la **double lecture** :

```
                    Axe Fonction (rôle de l'outil)
                    Airtable=DB │ ClickUp=QA │ Notion=Mémoire
              ┌─────────────────┼────────────┼────────────────┐
   Growth  →  │     PLEIN       │  dormant   │    dormant      │
   Sales   →  │     PLEIN       │  dormant   │    dormant      │ ← Axe
   Finance →  │     PLEIN       │  dormant   │    dormant      │   Domaine
   Ops     →  │    dormant      │   PLEIN    │    dormant      │   (sujet
   Product →  │    dormant      │   PLEIN    │    dormant      │   business)
   IT      →  │    dormant      │   PLEIN    │    dormant      │
   People  →  │    dormant      │  dormant   │     PLEIN       │
   Legal   →  │    dormant      │  dormant   │     PLEIN       │
              └─────────────────┴────────────┴─────────────────┘
```

### 5.5 Règles de "dormance"

Un domaine est **dormant** dans un outil quand :
- ✅ La structure (tables, vues, schémas) **existe** dans l'outil
- ✅ Les Symphony Adapters peuvent **lire** sans écrire pleinement
- ❌ Pas de routine quotidienne A3 sur cet outil pour ce domaine
- ❌ Pas de SLA actif

Un domaine est **plein** quand :
- ✅ A3 Squad Marvel correspondante a sa routine d'exécution dans cet outil
- ✅ SLA Sentinelles actives (Temporel, Financier, Qualitatif)
- ✅ Symphony Adapter dispatch des Payloads SOC vers Hermes B2 du domaine
- ✅ Webhook/polling configuré pour réagir aux events

---

## 6. Pré-Symphony Adapters (les 3 spec.md Shadow A0)

Les 3 outils Shadow L2 ont **déjà** leurs spec.md Symphony en cours de rédaction dans `00_Amadeus/05_OSS_Twin/symphony/L2/` (voir Shadow A0 doctrine). Chaque adapter :

- Hérite de `symphony-base.spec.md`
- Définit le `tracker.kind`, endpoint, auth
- Mappe les états SOA spécifiques à l'outil
- Précise les Custom Fields qui portent les SLA constraints
- Implémente le `TrackerAdapter` Python

### 6.1 Référence rapide des 3 adapters L2

| Adapter | Status | Complexité | Slot primaire |
|---|---|---|---|
| `symphony-airtable.spec.md` | À écrire | 🟢 facile (webhooks natifs) | Lead/Sales/Finance |
| `symphony-clickup.spec.md` | À écrire | 🟡 moyen (Build Gates) | Ops/Product/IT |
| `symphony-notion.spec.md` | À écrire | 🟡 moyen (DB API rate-limited) | People/Legal |

> **Note** : ces 3 specs vivent en **Shadow A0**, pas dans les SDD canon. SDD-009 les référence sans les remplacer.

---

## 7. Stratégie de Déploiement — Phases Alpha → Delta

(Source : Gemini Takeout 7 mai 19:28 — ligne 2370)

| Phase | Nom | Action concrète | Durée H1 |
|---|---|---|---|
| **Alpha** | Amorçage Terre | Coolify/Dokploy + Supabase (PostgreSQL + pgvector) + Symphony Router sur VPS | W1-W2 |
| **Beta** | Acupuncture | **UN seul Self-Operating Hub** (le plus douloureux — Growth si pipe vide / Product si Margin Bleed) avec Clean Slate + Anti-Corruption Layer | W3-W6 |
| **Gamma** | Shadow Mode | **Double exécution** : humain (Airtable/ClickUp) + IA (Symphony → Hermes B2) en parallèle silencieux. Audit de Doom compare outputs → calibration SLA | W7-W10 |
| **Delta** | Fractal | Activation des 7 autres domaines successivement → SOB clonable (Solaris/Nexus/Orbiter de SDD-007) | W11-W12 + 13ème semaine |

**Critère MUSE de graduation Phase Gamma → Delta** :
- 3 semaines consécutives Shadow Mode stable
- Audit Doom : > 80% concordance humain ↔ IA
- < 5% incidents SLA Financier (Margin Bleed contrôlé)
- A0 valide la signature finale

---

## 8. Stack OpenSource Chinoise — Frugal LLM Stack

(Doctrine Amadeus 2026-05-13)

| LLM | Token plan | Usage A'Space | Économie vs Claude |
|---|---|---|---|
| **MiniMax 2.7** | $20 = 4500/5h | **Default A3 Compagnons** (95% des appels) — API Anthropic-compatible → Claude Code native | ~70x moins cher |
| **GLM 4.7 Flash** (OpenRouter) | ~$0.05/M tokens | Fallback ultra-frugal pour Symphony Router B1 + Donna DLQ | ~100x moins cher |
| **Claude Opus/Sonnet** | $20/M+ | **Réservé Rick A1** + tâches critiques de souveraineté (SDDs, ADRs, arbitrages) | Référence |

**Règle** : par défaut Symphony route vers MiniMax. Promotion vers GLM Flash si budget tendu. Promotion vers Claude **uniquement** si Donna escalade vers Rick A1 (max 5% des tâches).

→ Budget compute mensuel A'Space cible : **< $30/mois en cruise** (vs $300+ all-Claude).

---

## 9. Conformité aux SDDs Antérieurs

| SDD | Lien | Comment SDD-009 le respecte |
|---|---|---|
| SDD-000 | Constitution Rick's Verse | Anti-Panic appliquée — Symphony B1 ne remplace pas Rick |
| SDD-000c | Shadow Frameworks A0 | Symphony adapters L2 vivent en `05_OSS_Twin/` Shadow A0 |
| SDD-001 | Solarpunk Kernel L0.3 | Symphony self-hosted sur Dokploy = bedrock L0.3 antifragile |
| SDD-002 | Rick Harness | Rick délègue à Jerry Symphony, garde le veto via Donna DLQ |
| SDD-003 | TARDIS Protocol | Inversé pour L2 : Donna → 13ème Doctor → 12ème Doctor → Rick |
| SDD-005 | Life OS L1 cible | SDD-009 NE TOUCHE PAS au L1 — pas de débordement |
| SDD-006 | Business Pulse pyramide | SDD-009 = **exécution pratique** de la pyramide SDD-006 |
| SDD-007 | SOB Factory ICP | SDD-009 fournit le substrate Shadow où les 3 ICPs vont être testés |
| SDD-008 | Shadow L1 | SDD-009 = **symétrie L2** parfaite (matrice 3×4 outils L1 ↔ matrice 3×8 domaines L2) |
| ADR-RICK-001 | OpenHarness | OpenHarness reste Rick — ne sert PAS de B1 Symphony |

---

## 10. Anti-Goals (verrous explicites)

- ❌ **Ne pas faire** d'OpenHarness l'orchestrateur B1 — il reste Rick (A1) avec Donna DLQ
- ❌ **Ne pas charger** Symphony en MCP — Clara forge CLI commodité pour B2↔B3
- ❌ **Ne pas activer** les 8 domaines simultanément en phase Beta — UN seul hub d'abord
- ❌ **Ne pas mixer** les couches SOA — chaque domaine reste forteresse isolée Supabase RLS
- ❌ **Ne pas exécuter** sans Payload SOC validé Zod — frontière infranchissable
- ❌ **Ne pas implémenter** la constitution complète Marvel Squads dans SDD-009 — c'est un PRD séparé
- ❌ **Ne pas négocier** les SLA après dispatch — `max_compute_budget` est mathématique, pas social
- ❌ **Ne pas créer** de nouveau SDD au-delà de SDD-010 pendant 90 jours — veto Amadeus 2026-05-13

---

## 11. Definition of Done de SDD-009

Pour considérer SDD-009 "Done" (= conditions du critère MUSE de graduation L2) :

1. ✅ Trinité SLA/SOA/SOC documentée et schématisée
2. ✅ Tri-tier B1/B2/B3 mappé sur Symphony/Hermes/Paperclip
3. ✅ Matrice 3×8 Shadow L2 documentée avec règles de dormance
4. ✅ 3 specs Symphony adapters Shadow A0 en cours (Airtable/ClickUp/Notion)
5. ✅ Stratégie déploiement Alpha→Delta avec critères de transition
6. ✅ Stack LLM frugale documentée (MiniMax/GLM/Claude réparti)
7. ⏳ Premier ICP Solaris testé en Phase Gamma Shadow Mode (futur — pas dans SDD-009 lui-même)
8. ⏳ PRD-MARVEL-001 rédigé pour constitution complète squads (futur — PRD, pas SDD)

---

## 12. Follow-ups (hors SDD, dans le veto)

Listés ici **pour mémoire** — à traiter via PRD/ADR/DDD/TDD, **pas** via nouveaux SDDs :

| ID | Type | Sujet | Priorité |
|---|---|---|---|
| PRD-009a | PRD | Symphony Router déploiement Dokploy | P1 |
| PRD-009b | PRD | Premier Hub Acupuncture (Growth ou Product) | P1 |
| PRD-MARVEL-001 | PRD | Constitution complète des 8 Marvel Squads | P2 |
| ADR-LLM-001 | ADR | MiniMax 2.7 comme default + bascule GLM/Claude | P1 |
| ADR-CLI-001 | ADR | Clara MCP→CLI conversion strategy (Printing Press + CLI Anything) | P1 |
| DDD-009a | DDD | Bounded Contexts des 8 SOA domaines | P2 |
| DDD-009b | DDD | Payload SOC schema versioning (Zod contracts) | P1 |
| TDD-009a | TDD | Tests d'idempotence Symphony Router | P1 |
| TDD-009b | TDD | Tests SLA Sentinelles (Temporel/Financier/Qualitatif) | P1 |

---

## 13. Signature & Ratification

| Champ | Valeur |
|---|---|
| **Auteur SDD** | A0 Amadeus (Claude Architect interface) |
| **Date ratification** | 2026-05-13 |
| **Versioning** | V0 (sera promu V1 en 13ème semaine après validation Muse — cf. SDD-010) |
| **Veto Amadeus** | Aucun nouveau SDD au-delà de SDD-010 pendant 90 jours |
| **Hash conceptuel** | trinity_SLA_SOA_SOC + matrix_3x8_dormance + tri-tier_B1B2B3 + stack_frugal_chinois |
| **Statut** | RATIFIÉ — immutable selon Règle d'Or n°3 du Canon |

---

*SDD-009 — Shadow L2 Business OS : La Matrice Souveraine 3×8 — Amadeus & Claude Architect — Ratifié 2026-05-13*
*Aucun agent A1/A2/A3 ne peut modifier ce document sans nouveau SDD ou ADR de supersedure.*
*Prochain SDD : SDD-010 — Meta : Clôture du Scope et 13ème Semaine.*
