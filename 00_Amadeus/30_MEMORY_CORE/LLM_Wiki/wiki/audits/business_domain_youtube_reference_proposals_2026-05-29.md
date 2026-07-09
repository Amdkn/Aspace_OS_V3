---
source: backfilled 2026-06-06 (hygiene lint remediation)
date: 2026-05-29
type: audit
domain: audit
title: Business Domain YouTube Reference Proposals
tags: [#audit #audits #backfilled]
---

# Business Domain YouTube Reference Proposals

Date: 2026-05-29

Source locale principale:
`C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv`

Scan local:
- 25,463 lignes YouTube Takeout/RAG.
- 7,137 chaines uniques.
- Categories dominantes: `Regular` 15,632, `AI` 9,285, `Business` 542.
- Status dominants: `SKIPPED` 16,069, `CAPTURED` 8,700, `CLARIFIED_PLANE` 690.

Lecture: le Takeout contient deja un fort signal Growth/AI/Ops, mais Sales, People et Legal sont sous-alimentes. Il faut donc distinguer:
- `Corpus local a miner`: chaines deja presentes dans ton historique.
- `Seed externe a ajouter`: chaines a consommer volontairement pour combler un domaine faible.

## 01 Growth - Superman / Guardians

Role reference: acquisition, marque, positionnement, contenu, SEO, offre, go-to-market.

Corpus local prioritaire:
- Yann Leonardi - 86 occurrences. Deja canonise comme source Growth principale. Exemples: PNL marketing, Nike vs On, doudoune virale.
- Julian Goldie SEO - 55 occurrences. Bon pour SEO, agents MCP, croissance organique et experimentation IA.
- Marketing Mania - 3 occurrences. Bon pour psychologie marketing, narration de marche, persuasion.
- SchoolMaker - 4 occurrences. Bon pour formation, offre educative, vente de connaissance.
- StrategeMarketing - 6 occurrences. Bon comme base pedagogique marketing generaliste.
- Scalezia - 2 occurrences. Bon pour SEO process et croissance B2B.
- Little Bit Better - 10 occurrences. Bon pont vers `Million Dollar Weekend`, `Built to Sell`, `100M Offers`.

Seed externe propose:
- Ahrefs - SEO tactique et contenu organique.
- Lenny's Podcast - pont Product/Growth/PMF.
- Alex Hormozi - offre, pricing, acquisition, sales enablement.

Decision: garder Yann comme constitution Growth, puis ouvrir deux sous-corpus: `SEO_Growth` avec Julian/Ahrefs/Scalezia et `Offer_Growth` avec Hormozi/Little Bit Better/SchoolMaker.

## 02 Sales - Martian Manhunter / Illuminati

Role reference: prospection, closing, discovery, pipeline, CRM, objection handling.

Corpus local prioritaire:
- Bastien Pelissier - 6 occurrences. Signal clair vente/closing. Exemple: repondre a "j'ai besoin de temps avant de me decider".
- Valentin Heinly - 8 occurrences. Signal agence/SMMA: onboarding client, prospection a froid, tarifs d'agence.
- Tom & Harry | SMMA (Unfiltered) - 1 occurrence. Signal cold call et collecte contacts business.
- Nathan Levallois - 3 occurrences. Signal acquisition premiers clients + automatisation business.
- Natalie Dawson - 2 occurrences. Signal croissance business, marketing et execution commerciale.

Seed externe propose:
- Josh Braun - B2B sales, cold outreach, objection handling.
- Patrick Dang - sales training simple et systematique.
- HubSpot - CRM, pipeline, inbound sales.

Decision: domaine sous-alimente mais recuperable. Bastien + Valentin peuvent former le noyau francophone; Josh Braun/HubSpot deviennent la source de standardisation B2B.

## 03 Product - Flash / Avengers

Role reference: MVP, interface, UX, product strategy, build, QA, shipping.

Corpus local prioritaire:
- Y Combinator - 6 occurrences. Tres bon pour design review, startup product thinking, validation.
- Melvynx - 109 occurrences. Fort signal build/front-end/product engineering.
- WorldofAI - 128 occurrences. Fort signal demos, agents, produit IA, prototypes.
- Fireship - 36 occurrences. Bon pour vulgarisation stack, shipping rapide, patterns dev.
- Labo Des Reseaux - 24 occurrences. Signal outils/design/Canva et production de surfaces.

Seed externe propose:
- Product School - product management structure.
- Lenny's Podcast - product strategy, growth loops, PMF.
- Nielsen Norman Group - UX research et heuristiques.

Decision: ici il faut eviter que Product devienne seulement "build". Y Combinator/Lenny/Product School doivent tirer la couche strategie; Melvynx/WorldofAI/Fireship tirent la couche execution.

## 04 Ops - Batman / Fantastic4

Role reference: SOP, systemisation, workflow, delegation, automation, delivery.

Corpus local prioritaire:
- Julien Sanson | Automatisation & AI - 69 occurrences. N8N, webhooks, MCP, automatisation.
- Nate Herk | AI Automation - 26 occurrences. N8N, agents, RAG, no-code automation.
- Ousmane Automatise - 10 occurrences. N8N/Make en francais, assistants IA operationnels.
- Layla at ProcessDriven - 4 occurrences. Business systems, process, systemisation.
- EOS Worldwide - 3 occurrences. Entrepreneurial Operating System, VTO, operating cadence.
- n8n - 6 occurrences. Source officielle execution workflow.
- UpSys - ClickUp Consulting - 7 occurrences. Structuration ClickUp/agence.

Seed externe propose:
- Process Street - SOP et checklists operationnelles.
- Make - automatisation visuelle.
- Zapier - integration ops generaliste.

Decision: Ops est le domaine le plus pret pour devenir une raffinerie SOP. Layla/EOS donnent la doctrine; Julien/Nate/Ousmane/n8n donnent l'execution technique.

## 05 IT - Cyborg / Kang Dynasty

Role reference: infrastructure, code, cloud, agents, securite, self-hosting.

Corpus local prioritaire:
- Cole Medin - 57 occurrences. Agents, Supabase local, workflows agentiques.
- OpenAI - 86 occurrences. Source primaire produit/agents/research.
- Google for Developers - 24 occurrences. Gemini, ADK, MCP, developer tooling.
- Google Cloud Tech - 42 occurrences. Cloud, agents, AI Studio.
- WorldofAI - 128 occurrences. Demos agents et outils IA.
- Melvynx - 109 occurrences. Stack front, Shadcn/UI, Codex, dev product.
- Fireship - 36 occurrences. Vulgarisation dev rapide.
- TechWorld with Nana - 1 occurrence. Source externe solide deja presente faiblement.

Seed externe propose:
- TechWorld with Nana - DevOps pedagogique.
- NetworkChuck - reseau, homelab, securite.
- ByteByteGo - architecture systeme.

Decision: IT a beaucoup de volume, mais il faut le scinder en `Agentic IT`, `Dev Product`, `Infra/Security`. Cole/OpenAI/Google = agentic; Melvynx/Fireship = build; Nana/ByteByteGo = infra propre.

## 06 Finance - Wonder Woman / Thunderbolts

Role reference: pricing, marge, budget, unit economics, cashflow, finance d'entreprise.

Corpus local prioritaire:
- Thami Kabbaj - 32 occurrences. Finance/marches/investissement.
- BFM Business - 25 occurrences. Actualite business et macro.
- MoneyRadar - 79 occurrences. Finance, tech, marche, analyse d'actifs.
- Bloomberg Television - 2 occurrences. Macro et signaux CEO/market.
- NextGenVC - 2 occurrences. VC, bootstrap vs levee, fundraising.
- Little Bit Better - 10 occurrences. Built to Sell, Million Dollar Weekend, 100M Offers.

Seed externe propose:
- Accounting Stuff - comptabilite claire pour entrepreneurs.
- The SaaS CFO - SaaS metrics, MRR, CAC, LTV.
- Acquisition.com / Hormozi - pricing, marge, offre.

Decision: Finance manque encore de comptabilite operationnelle. Thami/MoneyRadar = culture financiere; Accounting Stuff/SaaS CFO = operating finance; Hormozi = pricing/offre.

## 07 People - Green Lantern / X-Men

Role reference: hiring, leadership, culture, communication, management, charge cognitive.

Corpus local prioritaire:
- Ali Abdaal - 3 occurrences. Productivite, systemes personnels, business solo.
- Natalie Dawson - 2 occurrences. Croissance equipe/business execution.
- Deya - 7 occurrences. Business systems, daily checklist, business without me.
- Notion - 31 occurrences. Documentation et collaboration equipe.
- Anthropic - 19 occurrences. Travail avec agents/Claude, moins People pur mais utile pour culture AI-native.

Seed externe propose:
- Harvard Business Review - leadership, management, culture.
- Patrick Lencioni / The Table Group - team health, execution leadership.
- Manager Tools - management cadence, one-on-ones, delegation.
- Simon Sinek - leadership, mission, communication.

Decision: People est sous-alimente dans le Takeout. Il faut une phase seed volontaire pour eviter que People soit confondu avec productivite personnelle.

## 08 Legal - Aquaman / Eternals

Role reference: contrats, compliance, IP, privacy, conditions, risques.

Corpus local prioritaire:
- Aucun noyau local fiable detecte. Les hits `legal/law/contract` sont surtout du bruit musical, politique ou culture internet.
- Legal doit donc etre seed depuis des sources externes avant extraction SOP.

Seed externe propose:
- LegalEagle - vulgarisation juridique et contrats grand public.
- LegalBytes - analyse legal/media/IP.
- TermsFeed - privacy policy, terms, compliance web.
- Wilson Sonsini / startup legal resources - startup incorporation, financing, IP.

Decision: Legal est le domaine le plus vide. Ne pas promouvoir les resultats locaux actuels en doctrine; creer d'abord un corpus seed `Legal_Startups_Compliance`.

## Prochaine action conseillee

1. Creer un dossier `Reference_Channels` sous chaque domaine B2 avec `CHANNEL_MAP.md`.
2. Pour chaque domaine, selectionner:
   - 1 source canonique,
   - 2 sources tactiques,
   - 1 source externe a consommer volontairement.
3. Ajouter un pipeline de promotion:
   `YouTube Takeout -> Resources/Geordi Guide -> B2 Domain Principle -> B3 SOP / JTBD`.
4. Creer ou reutiliser un skill de mapping `youtube-takeout-domain-channel-map` si cette analyse doit etre relancee apres chaque nouveau Takeout.

