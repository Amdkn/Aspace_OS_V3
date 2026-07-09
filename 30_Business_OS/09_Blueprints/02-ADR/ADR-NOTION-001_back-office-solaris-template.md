# ADR-NOTION-001 — Notion Back Office : Solaris Prototype + Template Reproductible

**Date :** 2026-05-26
**Auteur :** A0 Amadeus + A2 Claude Code (Architecte)
**Statut :** RATIFIÉ — bootstrap en cours
**Type :** Architecture Decision Record (Business OS / L2)
**Portée :** Workspace Notion `Business Pulse ∞ AMADEUS` · Solaris (1er) puis clonage vers 5 projets Picard
**Ancré sur :** `AGENTS.md` · ADR-FWK-022 (SoT = PARA J01) · ADR-FS-001 (junctions short-path)
**Origine matière :** Conversations Gemini 2026-05 (citations doctrinales aux lignes 27840-27982, 211546-215482, 28396-28894)
**Dépendance externe :** ADR-SYMPH-001 (à venir) — bus orchestration pour sync Notion ↔ Supabase

---

## Contexte

Trois faits convergent :

1. **Gemini a accouché d'une doctrine Notion claire** entre avril 2025 et mai 2026 (cf. Takeout `2026-05_conversations.md`) : Notion est le "Livre de Loi" du *Self-Operating Business* (SOB), sous garde de Jerry (B1) + Green Lantern (B2-Agents). Pipeline canonique : `Airtable (CRM) ➔ Notion (SOP) ➔ ClickUp (Action)`.
2. **Airtable et ClickUp ont déjà été structurés** côté Shadow_L2 par A0 sur la base de ces mêmes conversations Gemini. **Notion a été procrastiné** — c'est le maillon manquant.
3. **L'auth MCP Notion vient d'être stabilisée** (2026-05-26, cf. fix A3) : `Business Pulse ∞ AMADEUS` est le workspace OAuth-consenti, persistance acquise via `tokens.json` + refresh_token.

**Intention A0 (2026-05-26)** : la structuration Notion vise d'abord **Solaris** (le produit-phare A'Space SaaS "Control Plane pour agences AaaS"), avec **objectif explicite de template reproductible** pour les 5 autres projets Picard (Agency aaS, OMK BOS, ABC OS, RILCOT, Alikaly, Marina) et — à terme — pour les clients franchisés.

## Décision

### D1 — Workspace canonique unique

`Business Pulse ∞ AMADEUS` est **le seul** workspace Notion du Back Office L2. Aucun second workspace ne sera créé pour les autres projets Picard — au lieu de ça, **chaque projet vit comme une top-level page** au sein du workspace unique. Rationale : multi-workspace = multi-auth = friction. Une page peut être dupliquée (template) sans changer de workspace.

### D2 — Solaris est le prototype canonique (TEMPLATE_VERSION:1.0)

La structure définie ci-dessous est **construite et validée d'abord pour Solaris**. Une fois Solaris green (SOPs binaires fonctionnelles + sync Symphony OK), la page Solaris devient un **template Notion natif** dupliqué vers les autres projets via le bouton "Duplicate" + relink. Chaque clone hérite de la `TEMPLATE_VERSION` du parent.

### D3 — Architecture en 5 sections (par projet)

Chaque top-level page projet (Solaris en tête) suit la structure canonique extraite du Takeout Gemini :

```
📄 Solaris HQ  (top-level page, owner: Jerry B1)
│
├── 🏛️ 1. Dashboard d'Accueil
│   ├── Vision & Mission  (callout — Type 4 Kardashev, alignement A'Space)
│   ├── Index 8 Portails Domaines  (linked database view filtered by domain)
│   └── Index Context Packs  (linked database view — prompts agents B3 lus par Symphony)
│
├── 📚 2. Bibliothèque SOPs TVR  ← LE CŒUR
│   └── MASTER_SOP_DB  (database, schema § D4)
│       Vues : "Par Domaine" (8 colonnes Kanban) · "Par Trigger" · "À auditer (>30j)"
│
├── 🧬 3. Hall des Agents  (Green Lantern / People)
│   ├── AGENT_REGISTRY_DB  (database — un row par essaim Marvel/DC actif)
│   ├── PERFORMANCE_LOG_DB  (database — rapports hebdo Green Lantern)
│   └── Ethics & Alignment  (page rich-text — Sobriété Intelligente)
│
├── 💰 4. Catalogue Produits  (Flash)
│   ├── PRODUCT_SPECS_DB  (Solaris / Nexus / Orbiter tier specs)
│   ├── MARKETING_COPY_DB  (utilisé par Superman/Guardians pour Growth)
│   └── PRICING_DB  (validé par Wonder Woman — marge MRR vs Compute)
│
└── ⚖️ 5. Coffre Légal  (Aquaman)
    ├── CONTRACT_TEMPLATES_DB  (Licence Whitelabel, CGV Cloud, MSA)
    └── COMPLIANCE_LOG_DB  (audits, RGPD, données clients)
```

### D4 — MASTER_SOP_DB : schema canonique (immuable v1.0)

**Database principale**, propriété de Batman (B2 Ops). Schema :

| Propriété | Type Notion | Contenu / Valeurs |
|-----------|-------------|-------------------|
| `Title` | Title | Nom court de la SOP, format "VERB OBJECT" (ex: "Provision VPS Nexus") |
| `SOP_ID` | Formula | `"SOP-L2-" + prop("Domain") + "-" + prop("Number")` |
| `Number` | Number | Auto-incrément manuel par domaine (001, 002, …) |
| `Domain` | Select | `Growth · Sales · Product · Ops · IT · Finance · People · Legal` (8 secteurs DC alignés PARA J01) |
| `Owner_VP` | Person | Batman, Cyborg, John Jones, Wonder Woman, Aquaman, Flash, Superman, Green Lantern |
| `Executor_B3` | Multi-select | `Fantastic4 · KangDynasty · Illuminati · Thunderbolts · Eternals · Avengers · Guardians · XMen` |
| `Trigger` | Rich text | Condition déclenchante (ex: "Statut ClickUp = To Do" ou "Stripe webhook = invoice.paid") |
| `Steps_Checklist` | Rich text (page body) | Étapes binaires 0/1 — pas de prose, pas d'ambiguïté |
| `Build_Gate` | Rich text | Critère de validation par Nardol (B3 QA) |
| `Loom_URL` | URL | Lien vidéo Loom 5 min max — démonstration de la SOP exécutée |
| `Context_Pack_URL` | URL | Lien vers le prompt système injecté dans Graham (mémoire agent) par Symphony |
| `Status` | Select | `Draft · Active · Deprecated · Under_Audit` |
| `Template_Version` | Text | `1.0` initial ; incrémenté sur changement breaking |
| `Last_Audited` | Date | Mis à jour à chaque revue (>30j = flag dans vue "À auditer") |
| `Created_At` | Created time | Auto |

**Règle d'or** : une SOP qui ne peut pas être exécutée par un agent B3 sans clarification humaine est `Draft`, jamais `Active`. Batman refuse les SOPs floues.

### D5 — 8 Portails Domaines (un par secteur DC, alignés PARA J01)

Conformément à ADR-FWK-022 (rename Marvel/DC), les 8 portails Notion miroir les 8 secteurs SoT :

| Portail Notion | Owner | Squad B3 | SoT PARA |
|----------------|-------|----------|----------|
| 01_Growth | Superman | Guardians of the Galaxy | `J01\B2_Area_Domains\01_Growth_Superman_Guardians` |
| 02_Sales | John Jones (Martian Manhunter) | Illuminati | `…\02_Sales_MartianManhunter_Illuminati` |
| 03_Product | Flash | Avengers | `…\03_Product_Flash_Avengers` |
| 04_Ops | Batman | Fantastic Four | `…\04_Ops_Batman_Fantastic4` |
| 05_IT | Cyborg | Kang Dynasty | `…\05_IT_Cyborg_KangDynasty` |
| 06_Finance | Wonder Woman | Thunderbolts | `…\06_Finance_WonderWoman_Thunderbolts` |
| 07_People | Green Lantern | X-Men | `…\07_People_GreenLantern_XMen` |
| 08_Legal | Aquaman | Eternals | `…\08_Legal_Aquaman_Eternals` |

Chaque portail est une page Notion qui filtre `MASTER_SOP_DB` sur son `Domain`. Pas de duplication de base.

### D6 — Pipeline canonique (rappel doctrinal)

```
Airtable (CRM Data, Pulse KPIs)
   ↓  bus orchestration
Notion (SOPs binaires + Context Packs + Specs Produits)
   ↓  bus orchestration
ClickUp (Tasks atomiques générées par les agents B3)
```

**Le bus d'orchestration est Symphony** (cf. ADR-SYMPH-001 à venir), pas N8N. N8N est marqué legacy dans `_Archives_Data\` au prochain ménage.

### D7 — Doctrine Cuisine / Salle (rappel ADR-FWK-022)

Notion = **Cuisine** (Back Office Amadeus + A3 techniciens). Le client final ne voit jamais Notion — il consomme une **App Client Next.js + Supabase** synchronisée par Symphony depuis Notion. Conséquence : on peut faire évoluer Notion librement sans casser l'UX client.

### D8 — Template Versioning & clonage

Quand Solaris atteint un état stable (toutes les SOPs P0 sont `Active`, build gates testés), A0 :
1. Marque la page racine `Solaris HQ` avec `Template_Version: 1.0-stable`
2. Duplique la page en `OMK_BOS HQ`, `ABC_OS HQ`, `RILCOT HQ`, `Alikaly HQ`, `Marina HQ`
3. Chaque clone hérite `Template_Version: 1.0-stable` et est marqué `Project: <name>` dans une propriété ajoutée
4. Toute évolution future Solaris bumpe la version (1.1, 2.0…) — un Linked View Master permettra de comparer divergences

Pour les clients franchisés (Orbiter tier), le clonage est automatisé par Symphony : Notion API `POST /pages` avec parent = template Solaris.

## Conséquences

### Positives
- **Une seule source Notion**, persistance MCP OAuth acquise, pas de prolifération workspace
- Schema SOP **immuable** — agents B3 peuvent compter sur `SOP_ID`, `Trigger`, `Build_Gate` sans deviner
- Alignement strict avec PARA J01 (canon Marvel/DC) → pas de drift naming
- Template clonable = scalabilité économique pour offre Orbiter (franchise white-label)

### Négatives
- 1 workspace = limite Notion de pages (~10000 — large mais pas infini). Si A'Space passe à 100+ clients franchisés, repenser le sharding.
- Couplage Symphony (ADR à venir) — Notion ne sert à rien sans bus de sync. Bootstrap Solaris peut commencer manuellement avant que Symphony soit prêt.

### Risques
- **Si A0 procrastine encore** sur la rédaction effective des SOPs (tentation : copier des templates Gemini sans les rendre binaires), Notion devient un musée. **Antidote** : Batman refuse `Active` sans Build_Gate testé.

## Plan de bootstrap (Phase 1 — Solaris seul)

1. **[Maintenant]** Créer top-level page `Solaris HQ` dans `Business Pulse ∞ AMADEUS` (via MCP Notion ou main UI)
2. **[+1h]** Créer `MASTER_SOP_DB` avec le schema § D4 — saisir les 14 propriétés
3. **[+30min]** Créer les 8 portails domaines avec Linked View filtrée
4. **[+30min]** Créer `AGENT_REGISTRY_DB` minimal — un row par squad B3 active
5. **[+1h]** Rédiger 3 SOPs P0 pour tester le format (1 Ops, 1 Sales, 1 Finance)
6. **[Phase 2]** Une fois ADR-SYMPH-001 ratifié → wire-up sync Notion → Supabase

## Références

- `Shadow_L0\03_quick-access-summers-and-inbox-20260522.md` (canon archivage legacy)
- `ADR-FWK-022_quick-access-summers-and-inbox-pattern.md` (alignement Marvel/DC)
- `Gemini_Takeout_2026\2026-05_conversations.md` lignes 27840-27982 (architecture 5 sections)
- `Gemini_Takeout_2026\2026-05_conversations.md` lignes 211546-215482 (cuisine/salle, MASTER_SOP_DB)
- `Gemini_Takeout_2026\2026-05_conversations.md` ligne 28396 (pipeline canonique Airtable→Notion→ClickUp)
- ADR-SYMPH-001 (à venir) — bus orchestration

## Propagation requise (post-ratification)

- [ ] `Shadow_L2\09_notion-back-office-solaris-bootstrap-20260526.md`
- [ ] `LLM_Wiki\wiki\entities\entity_adr_notion_001.md`
- [ ] `LLM_Wiki\wiki\log.md` (append)
- [ ] `LLM_Wiki\wiki\hand_offs\handoff_20260526_notion-solaris-bootstrap.md` (instructions exécution Phase 1)
