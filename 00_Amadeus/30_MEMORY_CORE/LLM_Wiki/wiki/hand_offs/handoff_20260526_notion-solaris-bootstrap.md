---
source: backfilled 2026-06-06 (hygiene lint remediation)
date: 2026-05-26
type: handoff
domain: handoff
title: Handoff — Notion Back Office Bootstrap Phase 1 (Solaris)
tags: [#handoff #hand_offs #backfilled]
---

# Handoff — Notion Back Office Bootstrap Phase 1 (Solaris)

**Date :** 2026-05-26
**Émetteur :** A2 Claude Code
**Destinataire :** A0 Amadeus (exécution manuelle OU via MCP Notion)
**Statut :** PRÊT — Auth Notion OK, ADR ratifié, plan d'exécution ci-dessous

## Pré-requis vérifiés

- [x] Workspace `Business Pulse ∞ AMADEUS` consenti via MCP (tokens.json valide)
- [x] ADR-NOTION-001 ratifié
- [x] Mapping Marvel/DC PARA J01 stabilisé (ADR-FWK-022)
- [ ] ADR-SYMPH-001 — **non bloquant** pour Phase 1 (sync différé)

## Plan d'exécution Phase 1 (≈ 3h cumulé)

### Étape 1 — Top-level page `Solaris HQ`  (5 min)

Via MCP : `notion-create-pages` avec `parent = workspace root`, `title = "Solaris HQ"`, icon = ☀️, cover = thème solaire.

Body initial (4 sections placeholder + 1 callout doctrine) :

```markdown
> **Doctrine** : Cette page est le prototype canonique du SOB Factory.
> TEMPLATE_VERSION : 1.0-draft
> SoT alignment : PARA\02_Areas_Spock\J01_Jerry_Prime_LD01_Business

## 🏛️ Dashboard d'Accueil
[à compléter]

## 📚 Bibliothèque SOPs TVR
[MASTER_SOP_DB ici — étape 2]

## 🧬 Hall des Agents
[à compléter — étape 4]

## 💰 Catalogue Produits
[à compléter — Solaris, Nexus, Orbiter specs]

## ⚖️ Coffre Légal
[à compléter — templates contrats]
```

### Étape 2 — `MASTER_SOP_DB` (30 min)

Via MCP : `notion-create-database` sous `Solaris HQ`, schema 14 propriétés (cf. ADR § D4) :

```yaml
properties:
  Title: title
  SOP_ID: formula  # "SOP-L2-" + prop("Domain") + "-" + format(prop("Number"))
  Number: number
  Domain: select [Growth, Sales, Product, Ops, IT, Finance, People, Legal]
  Owner_VP: person
  Executor_B3: multi_select [Fantastic4, KangDynasty, Illuminati, Thunderbolts, Eternals, Avengers, Guardians, XMen]
  Trigger: rich_text
  Steps_Checklist: (page body — pas une property)
  Build_Gate: rich_text
  Loom_URL: url
  Context_Pack_URL: url
  Status: select [Draft, Active, Deprecated, Under_Audit]
  Template_Version: text  # default "1.0"
  Last_Audited: date
  Created_At: created_time
```

Vues à créer :
- **Par Domaine** : Kanban grouped by `Domain` (8 colonnes)
- **Par Trigger** : Table sorted by `Trigger`
- **À auditer (>30j)** : Filter `Last_Audited` < 30 days ago OR null
- **Active uniquement** : Filter `Status = Active`

### Étape 3 — 8 Portails Domaines (30 min)

Sous `Solaris HQ`, créer 8 sub-pages (une par domaine) :

| Page name | Linked DB View |
|-----------|----------------|
| `01_Growth · Superman · Guardians` | MASTER_SOP_DB filtered Domain=Growth |
| `02_Sales · John Jones · Illuminati` | … Domain=Sales |
| `03_Product · Flash · Avengers` | … Domain=Product |
| `04_Ops · Batman · Fantastic4` | … Domain=Ops |
| `05_IT · Cyborg · KangDynasty` | … Domain=IT |
| `06_Finance · Wonder Woman · Thunderbolts` | … Domain=Finance |
| `07_People · Green Lantern · XMen` | … Domain=People |
| `08_Legal · Aquaman · Eternals` | … Domain=Legal |

Chaque page contient un Linked DB block (pas une nouvelle DB).

### Étape 4 — `AGENT_REGISTRY_DB` (15 min)

Sous section "Hall des Agents" :

```yaml
properties:
  Title: title  # ex: "Kang Dynasty"
  Squad: select [Fantastic4, KangDynasty, Illuminati, Thunderbolts, Eternals, Avengers, Guardians, XMen]
  Domain: select [Growth, Sales, Product, Ops, IT, Finance, People, Legal]
  Lead_Character: text  # ex: "Kang the Conqueror"
  Specialty: rich_text
  Status: select [Active, Standby, Deprecated]
  Avg_Latency_ms: number
  Last_Heartbeat: date
```

Peupler avec 8 rows initiaux (1 squad par domaine).

### Étape 5 — 3 SOPs P0 (1h)

Pour tester le format binaire, rédiger 3 SOPs :

1. **`Provision VPS Nexus`** (Domain=IT, Owner=Cyborg, Executor=KangDynasty)
   - Trigger : Stripe webhook `checkout.session.completed` avec product=Nexus
   - Steps : 8 étapes Hostinger API + Dokploy deploy
   - Build Gate : SSH actif + Dokploy dashboard accessible

2. **`Send Invoice Stripe`** (Domain=Finance, Owner=WonderWoman, Executor=Thunderbolts)
   - Trigger : ClickUp task status = "Ready to bill"
   - Steps : 5 étapes Stripe API
   - Build Gate : `invoice.paid` event reçu OU 7j timeout escalation

3. **`Qualify Inbound Lead`** (Domain=Sales, Owner=JohnJones, Executor=Illuminati)
   - Trigger : Airtable Leads new row status=New
   - Steps : 6 étapes (scoring ICP, enrichissement, premier contact)
   - Build Gate : Lead status=Qualified ou Inexploitable

## Outils MCP Notion disponibles

Une fois Claude Code redémarré (post fix A3), les outils suivants seront disponibles via ToolSearch :

- `notion-create-pages` — créer Solaris HQ + 8 sub-pages
- `notion-create-database` — créer MASTER_SOP_DB et AGENT_REGISTRY_DB
- `notion-update-page` — peupler le contenu
- `notion-create-view` — créer les vues filtrées
- `notion-search` — vérifier l'existant
- `notion-fetch` — lire pour propagation

A0 peut soit exécuter via Claude Code (MCP), soit faire à la main dans Notion UI puis demander à Claude Code de vérifier.

## Critères de passage Phase 1 → Phase 2

Phase 1 est verrouillée quand :
- [ ] Solaris HQ existe avec les 5 sections
- [ ] MASTER_SOP_DB peuplée avec 3 SOPs minimum (1 Ops + 1 Sales + 1 Finance)
- [ ] Chaque SOP a `Status=Active` + `Build_Gate` non vide
- [ ] AGENT_REGISTRY_DB peuplée avec 8 rows

→ Bump `Template_Version: 1.0-stable` sur Solaris HQ
→ Trigger Phase 2 (ADR-SYMPH-001 ratifié, sync Notion↔Supabase)

## Référence

ADR-NOTION-001_back-office-solaris-template.md
