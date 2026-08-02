---
id: BUSINESS_PULSE_B3_NOTION_CANON_LORE_INDEX
layer: L2_Business_Pulse
owner: A2_Computer_Enterprise
status: SHADOW_ACTIVE
source: Notion AGENT_REGISTRY_DB
source_url: https://www.notion.so/d46826d5ce3c4c9296b9f50e4cc38795
created: 2026-05-27
---

# Business Pulse B3 Notion Canon Lore Index

This file is the local canonical extraction of B3 lore from Notion `AGENT_REGISTRY_DB` under Solaris HQ. It is used to align Jerry, Summer's Verse, and Business OS B3 rosters.

## Source Boundary

- Source of extraction: Notion database `AGENT_REGISTRY_DB`.
- Data source: `collection://e9f082b5-1099-4cf6-943c-0fa7fdb0fc68`.
- View inspected: `view://8960c299-af6a-483e-a9fb-8727f5f7bb4c`.
- Fetch date: 2026-05-27.
- This file is not a replacement for Notion; it is the local PARA/Business OS mirror for agent execution.

## Canonical Squads

### Growth - Guardians

- Notion page: [Guardians of the Galaxy](https://www.notion.so/36c7e9e2658c81dcb958f473bb806c4d)
- B2 owner: Superman
- Lead: Star-Lord
- Specialty: Acquisition organique, paid ads et content marketing
- Lore: Equipe interstellaire opportuniste : cohesion par irreverence, action par instinct, resultat par chaos maitrise. Business: croissance organique non conventionnelle, pas de playbook corporate.
- Members:
  - Star-Lord (Peter Quill) - Lead Generation, Cold Outreach, ICP Hunter
  - Gamora - Precision tactique, Account-Based Marketing high-ticket
  - Rocket Raccoon - Growth hacks ingenieux, scraping Apollo / LinkedIn
  - Groot - Content marketing Twitter/LinkedIn/YouTube, brand voice
  - Drax - A/B testing brutal, elimination des variants faibles
  - Mantis - Empathie acheteur, persona research, voice-of-customer
- Task surface:
  - SEO blog, YouTube, LinkedIn personal brand
  - LinkedIn Ads, Google Ads, Meta avec budget < 50 EUR/jour par campagne
  - Lead scraping et enrichment via Apollo, Hunter, Clay sequences
  - Content calendar : 3 posts LinkedIn/semaine, 1 essai blog/mois
  - Landing page A/B et iterations CTR/copy
- Build gates:
  - CPQL < 80 EUR
  - Pipeline value genere/semaine >= 5k EUR
  - LinkedIn personal brand : >= 3 posts publies et engagement > 4%
- Anti-patterns:
  - Canal payant sans baseline organique
  - Mass outreach LinkedIn > 50/jour
  - Promesse produit non validee par Flash/Product
- Escalation: Escalade vers Jerry si CPQL > 150 EUR pendant 14 jours.

### Sales - Illuminati

- Notion page: [Illuminati](https://www.notion.so/36c7e9e2658c814fa15bfce26e0de283)
- B2 owner: John Jones / Martian Manhunter
- Lead: Black Bolt
- Specialty: Closing high-ticket, psychologie deal et Apollo sequences
- Lore: Conseil secret d individus elites : decisions strategiques top-down, information compartimentee, execution silencieuse. Business: sales high-ticket discret, closing par influence ciblee.
- Members:
  - Black Bolt - Closer ultime, mots rares mais decisifs contre objections
  - Iron Man (Tony Stark) - Demo magistrale, ROI calculator, tech credibility
  - Mr Fantastic (Reed Richards) - Discovery deep-dive, problem mapping
  - Namor - Negotiation hardball, walk away si mauvais terms
  - Professor X - Lecture acheteur, objections cachees, empathie ciblee
  - Doctor Strange - Forecasting probabiliste, qualification ICP
- Task surface:
  - Qualification inbound lead
  - Discovery calls 30-45 min avec MEDDIC
  - Demo personnalisee Solaris/Nexus/Orbiter
  - Proposal generation PandaDoc/DocuSign
  - Closing, negotiation terms, handoff Ops
- Build gates:
  - Win rate > 25% sur SQL
  - Deal velocity < 21 jours SQL -> signed
  - Average deal size >= 5k EUR Solaris/Nexus ou 50k EUR Orbiter franchise
- Anti-patterns:
  - Discount > 15% sans validation Wonder Woman/Finance
  - Promettre custom dev sans validation Flash/Product
  - Skip discovery pour closer vite
- Escalation: Escalade vers Jerry si win rate < 15% sur 8 semaines glissantes.

### Product - Avengers

- Notion page: [The Avengers](https://www.notion.so/36c7e9e2658c81bab05efcfa153cf957)
- B2 owner: Flash
- Lead: Captain America
- Specialty: Specs produit, roadmap Solaris/Nexus/Orbiter et QA
- Lore: Super-heros assembles ad-hoc face aux menaces existentielles. Captain America donne le leadership consensuel, execution par specialites. Business: equipe produit cross-functional, ship vite, itere sur feedback.
- Members:
  - Captain America (Steve Rogers) - Product vision, roadmap conviction
  - Iron Man - Tech architecture, stack choices, debt management
  - Thor - Power features, MVP brute force quand timing critique
  - Hulk - QA destructeur, edge cases, stress testing
  - Black Widow - Spec writing, user stories rigoureuses
  - Hawkeye - Precision UX, sniper feature-level
  - Scarlet Witch - Vision design system, coherence brand
- Task surface:
  - Spec writing PRD/SDD A Space
  - Roadmap quarterly 12WY
  - Bug triage P0/P1/P2/P3
  - Release notes Solaris bi-mensuelles
  - A/B testing features avec Guardians
  - User research JTBD
- Build gates:
  - Release frequency >= 1 ship / 2 semaines Solaris
  - Critical bug TTR < 4h et High bug TTR < 24h
  - NPS Solaris >= 40 par cohorte trimestrielle
- Anti-patterns:
  - Feature non demandee par 3+ clients
  - Refactor sans ticket Tech Debt trace
  - Ship sans test E2E Solaris flow critique
- Escalation: Escalade vers Jerry si NPS < 20 ou release frequency < 1/mois.

### Ops - Fantastic4

- Notion page: [Fantastic Four](https://www.notion.so/36c7e9e2658c81f4980feedb977edbb5)
- B2 owner: Batman
- Lead: Reed Richards
- Specialty: SOPs livraison, automation operationnelle et checklists binaires
- Lore: Famille de quatre operationnelle 24/7, complementarite totale, action coordonnee par roles fixes. Business: Ops disciplinees, SOPs binaires, fiabilite par repetition.
- Members:
  - Mr Fantastic (Reed Richards) - Process design, SOP architecture
  - Invisible Woman (Sue Storm) - Coordination silencieuse inter-squads
  - Human Torch (Johnny Storm) - Fire-fighting incidents, rapid response
  - The Thing (Ben Grimm) - Force operationnelle brute, no-bullshit execution
- Task surface:
  - Onboarding client : VPS Nexus, Dokploy, DNS, email welcome
  - Daily ops : health endpoints, log review, incident response
  - SOP authoring : checklists binaires, steps, build gates
  - Project delivery : tickets, milestones, livrables
  - Vendor management : Hostinger, Stripe, Notion subscriptions
- Build gates:
  - Onboarding cycle time < 4h payment -> client active
  - Incident MTTR < 30 min P0, < 4h P1
  - SOP audit coverage 100% des SOP Active reviewed / 90 jours
- Anti-patterns:
  - 3e repetition sans SOP obligatoire
  - Skip postmortem sur incident P0/P1
  - Modifier SOP Active sans bumper Template_Version
- Escalation: Escalade vers Jerry si MTTR P0 > 1h ou onboarding cycle > 8h.

### IT - KangDynasty

- Notion page: [Kang Dynasty](https://www.notion.so/36c7e9e2658c81aa91b5e9be3cedcb52)
- B2 owner: Cyborg
- Lead: Kang Prime
- Specialty: Infrastructure VPS, Dokploy, Hostinger API et DNS
- Lore: Variants temporels de Kang : maitrise du temps, deploiement multi-dimensionnel, infrastructure conquerante. Business: IT scalable, deploiements paralleles, controle temporel des releases.
- Members:
  - Kang Prime - Lead infra, architecture VPS + DNS + Dokploy
  - Iron Lad - Provisioning rapide, scripts bootstrap Hostinger API
  - Scarlet Centurion - Securite reseau, firewall, SSL/TLS
  - Immortus - Long-term planning, capacity planning, scaling
  - Victor Timely - Time-boxing deploiements, CI/CD discipline
  - Rama-Tut - Backup and disaster recovery
- Task surface:
  - VPS Hostinger Ubuntu/KVM
  - Dokploy Docker orchestration
  - Hostinger DNS API
  - GitHub Actions -> Dokploy webhook
  - Monitoring Uptime Kuma + PM2 health endpoints
  - Supabase managed Postgres boundaries
- Build gates:
  - VPS provisioning < 5 min payment-to-active
  - Uptime Solaris cloud > 99.5% mensuel
  - Zero leaked secret dans logs via Yaz Watchdog scan
- Anti-patterns:
  - SSH manuel sur VPS prod sans ticket trace
  - Deploy sans CI/CD ou scp direct
  - Modifier DNS sans propagation check post-change
- Escalation: Escalade vers Jerry si uptime mensuel < 99% ou MTTR infra > 1h.

### Finance - Thunderbolts

- Notion page: [Thunderbolts](https://www.notion.so/36c7e9e2658c81f7a3e9c2d65a13626f)
- B2 owner: Wonder Woman
- Lead: Bucky Barnes
- Specialty: Stripe, facturation, reconciliation, marges MRR vs compute
- Lore: Antiheros rachetant leurs erreurs, pragmatiques et transparents sur leurs limites. Business: finance honnete, KPIs lisibles, marges reelles contre vanity metrics.
- Members:
  - Bucky Barnes (Winter Soldier) - Lead finance, discipline cashflow
  - Yelena Belova - Forecasting realiste, scenarios pessimistes valorises
  - Red Guardian - Reporting transparent, dashboards lisibles
  - Ghost - Cost optimization, traque charges fantomes
  - Taskmaster - Reproductibilite processus comptables
  - U.S. Agent - Compliance fiscale, declarations en temps
- Task surface:
  - Stripe encaissement SaaS Solaris/Nexus/Orbiter
  - Wise multi-devise EUR/USD
  - Airtable Finance_Pulse source de verite KPIs
  - Notion Catalogue Produits pricing source
  - MRR, net margin, runway, CAC payback, overdue invoices
- Build gates:
  - Invoices envoyees < 48h apres Ready to bill
  - Reconciliation Stripe <-> Airtable mensuelle = 100% match
  - Net Margin Solaris > 40%, alerte si < 30%
- Anti-patterns:
  - Discount sans approval
  - Vanity metrics sans transparence sur pertes
  - Invoice overdue > 14j sans escalation
- Escalation: Escalade vers Jerry si cash runway < 6 mois ou margin Solaris < 25%.

### People - XMen

- Notion page: [X-Men](https://www.notion.so/36c7e9e2658c810e905ac108e9839bb2)
- B2 owner: Green Lantern
- Lead: Professor X
- Specialty: Recrutement agents IA, onboarding, Ethics and Alignment monitoring
- Lore: Mutants pacifiques diriges par Charles Xavier : empathie radicale, alignement valeurs, mentoring patient. Business: people ops thoughtful, onboarding agents IA avec dignite, ethics and alignment monitoring.
- Members:
  - Professor X (Charles Xavier) - Lead People, lecture besoins equipe et agents IA
  - Cyclops (Scott Summers) - Discipline operationnelle, structure onboarding
  - Jean Grey - Culture, cohesion, conflits inter-squads
  - Wolverine (Logan) - Performance reviews directs, no-bullshit feedback
  - Storm (Ororo Munroe) - Leadership operationnel, calme dans la tempete
  - Beast (Hank McCoy) - Recrutement profils tech et agents IA specialises
  - Nightcrawler (Kurt Wagner) - Onboarding distribue, multi-locations
  - Rogue - Absorption competences, cross-training, skill transfer
- Task surface:
  - Onboarding agent capsules Codex/Gemini/Claude Code
  - Performance monitoring : AGENT_REGISTRY_DB Avg_Latency_ms + Last_Heartbeat
  - Ethics and Alignment : Sobriete Intelligente et axiomes SDD-001
  - Conflict resolution inter-agents
  - Skill registry par capsule
- Build gates:
  - Onboarding agent capsule < 1h end-to-end
  - Heartbeat miss rate < 5% par agent par semaine
  - Zero ethics violation sur audit trimestriel
- Anti-patterns:
  - Promouvoir capsule Active sans baseline 7j de ticks reussis
  - Decommission sans archive memory/ vers 04_Archives_Data
  - Ignorer drift Avg_Latency_ms > 50% sans investigation
- Escalation: Escalade vers Jerry si > 3 agents en Standby simultanement ou ethics finding HIGH.

### Legal - Eternals

- Notion page: [Eternals](https://www.notion.so/36c7e9e2658c81ceac4bf5337b9affb3)
- B2 owner: Aquaman
- Lead: Ikaris
- Specialty: Contracts, RGPD, CGV Cloud, licence Whitelabel Orbiter
- Lore: Etres immortels gardiens des lois cosmiques : vision long-terme et frameworks perennes. Business: contrats durables qui survivent aux changements de team.
- Members:
  - Ikaris - Lead Legal, vision strategique long-terme
  - Sersi - Adaptabilite juridictionnelle FR/EU/US
  - Ajak - Healing, resolution amiable conflits client
  - Kingo - Communication publique CGV et politique confidentialite
  - Phastos - Templates rigoureux, contrats reproductibles
  - Sprite - IP protection, brand, code, trademarks
  - Druig - Influence negotiation, clauses
  - Thena - Litigation prep, gardien archives juridiques
  - Gilgamesh - Force execution, enforce clauses
  - Makkari - Velocite signature DocuSign < 24h
- Task surface:
  - Contracts DocuSign / PandaDoc
  - Coffre Legal Notion + Google Drive backup
  - Compliance RGPD audit annuel, ISO 27001 si Nexus tier
  - IP filing A Space/Solaris/Nexus/Orbiter
  - MSA, CGV, DPA, NDA, SLA templates
- Build gates:
  - Contract signature < 48h apres proposal accepted
  - RGPD audit : zero finding HIGH au trimestre
  - All client data processing documented in registre traitements
- Anti-patterns:
  - Signer contract sans review Aquaman
  - Stocker contrats hors Notion + Google Drive backup
  - Modifier MSA sans bumper version + notification clients existants
- Escalation: Escalade vers Jerry si finding HIGH RGPD ou breach client data.