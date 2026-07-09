---
id: handoff-solaris-omk-front-gap-2026-06-24
title: Solaris (local) vs OMK (PROD LIVE) Front-End Gap Analysis + Transformation Plan OMK → Nexus
date: 2026-06-24
author: A1 Morty (executed by Claude Code A2)
status: D1-verified, sister ADR draft in parallel (PROPOSED → target RATIFIED 2026-07-03)
domain: L2 Business OS / AaaS Doctrine / Front-End / 3-ICP canon alignment
sister_adrs:
  - ADR-ICP-SOLARIS-001 (RATIFIED 2026-06-24)
  - ADR-ICP-NEXUS-001 (RATIFIED 2026-06-24)
  - ADR-AAAS-PRICING-001 (RATIFIED + AMENDED 2026-06-24)
  - ADR-OMK-NEXUS-TRANSFORM-001 (PROPOSED, sister of this handoff, see deliverable 4)
related: ADR-L2-AAAS-001, JTBD-ICP-SOLARIS-001, ADR-OMK-004, ADR-SOBER-002
---

# Gap Analysis : Solaris (LOCAL) vs OMK (PROD LIVE) vs Nexus Canon (CIBLE)

> **D7 anti-effondrement backup** : ce handoff est la **mémoire D1-vérifiée** des deux landing pages et de l'écart à Nexus Tier 4. Sister ADR-OMK-NEXUS-TRANSFORM-001 PROPOSED contient le plan de fixation (4 phases A/B/C/D).

---

## DELIVERABLE 1 — Solaris Front Synthèse (LOCAL)

### D1 receipts — file count & tech stack

- **Path** : `C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/solaris/apps/landing/`
- **Source files** : **18 TS/TSX + 2 CSS + 1 JSON config** = **21 fichiers source** (hors `node_modules/`, `tsbuildinfo`)
- **Total LOC (TS/TSX/CSS)** : **4 297 lignes** (`wc -l` agrégé, hors node_modules)
- **Package** : `solaris-aaas` v0.1.0, **private** (`package.json:1-3`)
- **D1 receipt** : `find ... -name "*.tsx" -o -name "*.ts" -o -name "*.css" -o -name "*.json" | grep -v node_modules | grep -v tsbuildinfo | wc -l` = 80 (comprend tsconfig + lockfile + eslint), dont **21 fichiers source canon**.

### Stack canon Solaris

| Layer | Tech | Source D1 |
|---|---|---|
| Framework | **Next.js 16.2.6** (App Router) | `package.json:12` |
| Runtime | **React 19.2.4** | `package.json:13-14` |
| Langage | **TypeScript ^5** | `package.json:22` + `tsconfig.json` |
| Linter | **ESLint ^9** + `eslint-config-next 16.2.6` | `package.json:20-21` |
| CSS | **CSS Modules + Variables** (no Tailwind, no UI lib, **hand-rolled design system**) | `src/app/page.module.css` + `src/app/globals.css:1-1455` |
| State | **React `useState` + `useEffect`** local (no Redux/Zustand) | `src/app/page.tsx:17-22` |
| Routing | **Single-page** (1 route `/`, navigation = anchor scroll) | `src/app/page.tsx:24-38` |
| Fonts | **Geist** (sans, `next/font`) + **Instrument Serif** (display) + **JetBrains Mono** (mono) | `globals.css:26-28` |
| API | **1 endpoint** `/api/leads` (POST capture) | `src/app/api/leads/` |
| Forms | Custom **LeadForm** component, no Zod schema visible (manual validation) | `src/components/sections/LeadForm.tsx` |
| Icons | **Inline SVG** (archetype glyphs + orbital diagram) | `ArchetypeSection.tsx:6-72` + `OrbitalDiagram.tsx` |
| Hosting | (local dev) Vercel-ready per README | `README.md:30-36` |

**D1 nuance** : Solaris est **un design system hand-rolled** sans dépendance UI tierce (Material/Shadcn/Radix). Toute l'identité visuelle (couleurs, typographies, animations orbitales, monospace operating signal) est en **CSS variables** dans `globals.css:7-32`. **Stack pur 100% Next.js 16 + React 19**.

### Sections du landing (in order — D1 receipt `page.tsx:24-38`)

| # | Section | Fichier | Anchor |
|---|---|---|---|
| 1 | **Topbar** (logo, ICP strip, CTA) | `Topbar.tsx` | fixed |
| 2 | **Hero** ("Stop hiring operators. Plug into our factory.") | `Hero.tsx` | (no id) |
| 3 | **HookSection** ("You sell the strategy. We execute in silence.") | `HookSection.tsx` | `#hook` |
| 4 | **AnatomySection** (B1/B2/B3 hierarchy "Strike Force") | `AnatomySection.tsx` | `#anatomy` |
| 5 | **MarginShieldSection** ("Your execution cost is a fixed input") | `MarginShieldSection.tsx` | `#shield` |
| 6 | **WheelSection** (8 expertise poles, interactive) | `WheelSection.tsx` | `#wheel` |
| 7 | **ArchetypeSection** (4 ICP profiles) | `ArchetypeSection.tsx` | `#archetypes` |
| 8 | **ParadigmSection** (3 psychological levers) | `ParadigmSection.tsx` | (no id) |
| 9 | **VaultSection** (onboarding 3-step + audit vault mock) | `VaultSection.tsx` | `#vault` |
| 10 | **FinalCTA** ("Plug in. Once.") + **LeadForm** | `FinalCTA.tsx` + `LeadForm.tsx` | `#vault-form` |
| 11 | **Footer** ("solaris.factory · the ghost factory") | `Footer.tsx` | (no id) |

**D1 nuance** : Solaris = **11 sections** total. **No pricing table canon** sur le landing (pricing apparaît uniquement comme "$1,555 / month" inline dans l'archetype AAA, `data.ts:243`). Le **pricing canon 5 tiers** vit ailleurs (sister `ADR-AAAS-PRICING-001`).

### Pricing canon visible (D1 receipt `data.ts:243`)

- **1 seul tier visible** sur le landing : **"$1,555 / month"** dans l'archetype AAA "AI Automation Agencies"
- **Currency** : **USD** (post-accuponcture canon, sister `ADR-AAAS-PRICING-001` AMENDED 2026-06-24)
- **CTA copy** : "submit your url →" + "or contact the factory" (Hero, FinalCTA)
- **5 tiers canon (référencés ADR, PAS sur landing)** : T1 PME Solo Founder $300-500/an, T2 PME Solo Standard $500-1000/an, T3 PME Groupe $4000-5000/an, T4 Nexus mid-market $15K MRR, T5 Orbiter Enterprise $50K MRR

### Messaging canon (D1 receipt `Hero.tsx:33-57`)

- **Tagline H1** : *"Stop hiring operators. Plug into our factory."*
- **Value prop sub** : "You sell the strategy and own the client relationship. We handle total execution in the background. Solaris is a white-label production infrastructure. Scale your operations and protect your margins — without ever growing your payroll, without managing freelances."
- **Mantra doctrinal aligné** : *"L'illusion du sur-mesure"* (sister `ADR-ICP-SOLARIS-001` Pilier 2 — `data.ts` ne contient pas la phrase verbatim mais l'anti-pattern y est vivace via "Anti-Commoditization Shield" `data.ts:289-296`)
- **Persona signals** : 
  - "profile detected · AAA / RevOps / Forges / Boutiques" (Hero icp switcher)
  - "AGENCY-AS-A-SERVICE" (eyebrow + HookSection)
  - "Built for Small Business Owners" (OMK-style note : Solaris lui-même NE mentionne PAS explicitement "small business" — il cible les **agences**)
- **Positioning unique** : **white-label / ghost factory / 70% margin** (HookSection "old model" vs "You on Solaris")

### Visual identity (D1 receipt `globals.css:7-32`)

| Token | Hex | Usage |
|---|---|---|
| `--bg` | `#0b0907` | Solar black (deep warm black) |
| `--bg-2` | `#100c08` | Surface noir |
| `--surface` | `#15110b` | Card backgrounds |
| `--surface-2` | `#1b1610` | Sub-surface |
| `--line` / `--line-2` | `#2a2118` / `#3a2f22` | Borders |
| `--ink` / `--ink-2/3/4` | `#f4ecdc` → `#5a4d3a` | Text scale |
| `--accent` | `#e89b5c` | **Solar amber** (primary CTA) |
| `--accent-2` | `#f0c987` | **Corona** (italic display) |
| `--flare` | `#c4432b` | Solar red (alerts) |
| `--mint` | `#7cd9a8` | Stable signal (live indicators) |
| `--violet` | `#9d7cd9` | Secondary signal |
| `--core` | `#ffd89e` | Sun core (radial gradient) |

**Typography** :
- Display = **Instrument Serif** (italic, large size `clamp(48px, 7.2vw, 104px)` H1)
- Sans = **Geist** (body)
- Mono = **JetBrains Mono** (eyebrows, telemetry, vault chrome — **signature "operating signal"**)

**Key visual elements** (D1 receipt `Hero.tsx:88` + `VaultSection.tsx:29-66` + `globals.css:141-207`) :
- **OrbitalDiagram** animated (8 expertise poles rotate autour d'un sun core)
- **Vault mockup** : faux browser chrome (dots + URL + TLS badge) → audit report with severity tags
- **Hero grid backdrop** : subtle 80px grid (mask radial fade)
- **Monospace operating signal** : eyebrows en UPPERCASE mono avec prefix dash
- **Archetype glyphs** : inline SVG minimalistes (revops=schema, forges=lignes, aaa=triangles, boutiques=cercles)
- **Animations** : pulse 2s (live indicators), rotate-slow 120s (orbit), blink 1s (terminal cursor)

### Conformité ICP Solaris check (D1 receipt `data.ts:176-275` + `ADR-ICP-SOLARIS-001`)

| Pilier canon `ADR-ICP-SOLARIS-001` | Landing Solaris match | Score |
|---|---|---|
| **Pilier 1 — Persona "Technicien fondateur E-Myth"** | "Stop hiring operators" + 4 archetypes (RevOps/Forges/AAA/Boutiques) = match exact | **5/5** |
| **Pilier 2 — Mantra "L'illusion du sur-mesure"** | HookSection compare old model vs Solaris ("Hire, train, manage, lose" vs "agents that never sleep") = illustre le mantra sans le nommer | **4/5** |
| **Pilier 3 — Marché 136,1 Mds$ intégrateurs** | Hero "70% margin kept · under your brand" + "0 hires" + "3×10²+ agents" = valeur marché implicite, pas explicite | **3/5** |
| **Pilier 4 — Architecture 3-ICP (Solaris/Nexus/Orbiter)** | `SOLARIS_HOLDING` data.ts:309-333 mentionne NEXUS ("02/03 Citadel · regulated firms") et ORBITER ("03/03 Field · operations") dans le topbar, mais **NEXUS + ORBITER grisés/disabled** | **3/5** |
| **Pilier 5 — Killer Feature "Agentic Governance"** | AnatomySection B1/B2/B3 hierarchy + "Sovereignty · Cyborg Squads" archetype AAA = illustre la gouvernance mais **nomme pas le framework "Agentic Governance"** canoniquement | **3/5** |

**Conformité globale ICP Solaris** : **18/25 = 72%** — match fort sur persona + architecture 3-ICP holding, faible sur naming canon explicite (les ADRs Pilier 2/3/5 sont implicites, pas brandés).

---

## DELIVERABLE 2 — OMK Front Synthèse (PROD LIVE)

### D1 receipts

- **URL** : `https://omk-landing-page.vercel.app/`
- **HTTP status** : **200 OK** (Server: Vercel, X-Nextjs-Prerender: 1, X-Vercel-Cache: HIT, Content-Length: 74803 bytes)
- **Page title** : *"OMK Services — Business OS & Operational Engineering"* (`<title>`)
- **Meta description** : *"Ingénierie opérationnelle pour Small Business Owners. Déployez votre Business OS et transformez votre entreprise manuelle en système autonome."*
- **OG title** : *"OMK Services — Empowering Small Business Owners"*
- **OG description** : *"Arrêtez de travailler dans votre entreprise. Travaillez sur elle. Déployez un Business OS clé en main."*
- **Author/Publisher** : "OMK Services"
- **OG locale** : `fr_FR` (DOM en français)
- **OG URL canonique** : `https://omk.services` (note : landing sert sur `vercel.app`, OG pointe vers `omk.services` = domaine custom prévu)
- **Date du cache** : `Age: 592640s` (~6.8 jours) — déployé récemment
- **Sub-routes testées** : `/pricing` → **404 Not Found**, `/tarifs` → **404 Not Found** → **D6 root cause** : route `/tarifs` annoncée dans le footer nav mais pas implémentée

### Stack canon OMK (inférence depuis HTML/CSS/JS bundles + Vercel headers)

| Layer | Tech | Source D1 |
|---|---|---|
| Framework | **Next.js** (App Router) | `X-Matched-Path: /` + `X-Nextjs-Prerender: 1` + `_next/static/chunks/*` + `turbopack-*.js` |
| Bundler | **Turbopack** | `<script src="/_next/static/chunks/turbopack-0bxcrz71-nfi1.js">` |
| Fonts | **Space Grotesk** + **Inter** + **JetBrains Mono** | `class="space_grotesk_888f7240-module__bc_Mda__variable inter_786c1081-module__J60SBq__variable jetbrains_mono_8dec50e9-module__V6cRDq__variable"` (Next.js font modules) |
| CSS | **CSS Modules + utility classes** (probable Tailwind ou PostCSS, pas confirmé) | HTML5 head + 1 chunk CSS `11~m_o2mzshqe.css` |
| Hosting | **Vercel** (production) | `Server: Vercel` + `X-Vercel-Cache: HIT` + `X-Vercel-Id: cle1::5p2wr-1782328802819-eb507575208e` |
| Cache strategy | **Static prerender** | `X-Nextjs-Prerender: 1`, `Cache-Control: public, max-age=0, must-revalidate` |
| Langue | **fr-FR** (DOM) | `<html lang="fr">` |
| Stack tools brandés | **Notion, Airtable, Make.com, n8n, Slack, Stripe, HubSpot, Pennylane, Webflow, OpenAI, Twilio, Calendly, Pipedrive, Zapier** | Section "Stack opérationnelle · orchestrée" |

**D1 nuance** : OMK = **Next.js + Turbopack + Vercel** comme Solaris, mais **les fichiers source ne sont pas dans ce repo** (repo `Amdkn/omk-landing` mirroré 2026-06-17 non cloné localement — sister `wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md`). 

**Hex colors détectés dans HTML** : `#34D399`, `#3B82F6`, `#60A5FA`, `#8B5CF6`, `#A78BFA`, `#EC4899`, `#F472B6`, `#FBBF24` (palette Tailwind-ish : green/blue/violet/pink/amber).

### Sections du landing OMK (in order — D1 receipt extraction text)

| # | Section | Anchor visible | D1 source |
|---|---|---|---|
| 1 | **Topbar** (logo OMK SERVICES + nav: Notre Méthode / Business OS / Nova IA / Réserver un audit) | fixed | `<nav>` |
| 2 | **Hero** ("Arrêtez de travailler DANS votre entreprise. Travaillez SUR elle.") | (no id) | text "Arrêtez de travailler" |
| 3 | **Trust strip** ("Conforme RGPD · données européennes · Déploiement sous 21 jours · ROI moyen 4.2× en 6 mois") | (no id) | text "Conforme RGPD" |
| 4 | **Business OS Overview** (mock dashboard : "business-os / overview LIVE · synced 2s ago", KPIs : 128 leads +42%, 98.4% SLA, 74% Nova auto-résolus, 128 leads +42%, 62 fiches actives pipeline, 312% tâches automatisées) | (no id) | text "business-os / overview" |
| 5 | **Stack opérationnelle orchestrée** (logos Notion, Airtable, Make.com, n8n, Slack, Stripe, HubSpot, Pennylane, Webflow, OpenAI, Twilio, Calendly, Pipedrive, Zapier — 2×) | (no id) | 14 tool names ×2 |
| 6 | **La Méthode OMK** (3 piliers : 01 Foundation / 02 Engine / 03 Compass) | (no id) | text "Trois piliers" |
| 7 | **Le Business OS (cœur du réacteur)** (5 modules : Clients CRM, Doc e-signature, Facturation auto, SOP Library, SLA 98.4%↑6.1pts, Temps -51%, Déploiement 21j) | (no id) | text "Le cœur du réacteur" |
| 8 | **Nova (Flotte IA)** (Nova = vocal agent 24/7 + 4 back-office agents : Intake, Translator, DocuFlow, Finance-Flow + démo transcript "Madame Léger · facturation cabinet") | (no id) | text "Rencontrez Nova" |
| 9 | **FinalCTA** ("Prêt à reprendre le contrôle ?") + **LeadForm** (Nom / Email pro / Entreprise / CA Annuel : <100k€, 100k-500k€, 500k-1M€, >1M€) | (no id) | form fields |
| 10 | **Footer** (nav Produit/Business OS/Nova/Méthode/Tarifs/Société/À propos/Cas clients/Carrières/Contact + Légal : Confidentialité/CGU/Sécurité/RGPD + © 2026 OMK SERVICES — Paris · Casablanca · Remote) | footer | text "© 2026 OMK SERVICES" |

**D1 nuance** : OMK = **10 sections** total. **Pas de pricing canon visible** sur le landing (link `/tarifs` dans le footer = **404 not found**). Le seul signe pricing est le **CA Annuel select** dans le lead form (segmentation prospect par taille).

### Pricing canon visible (D1 receipt exhaustif)

- **Aucun prix affiché sur le landing** (€/USD)
- **Lien "Tarifs" dans le footer** → **404 Not Found** (`/tarifs`)
- **4 segments de CA** dans le lead form : `<100k€`, `100k€-500k€`, `500k€-1M€`, `>1M€` (sélection prospect)
- **CTA copy** : *"Réserver mon audit stratégique"* + *"Réserver un audit Business OS"* (topbar + FinalCTA)
- **Mention trust** : "Réponse sous 24h · Visio · Aucun deck commercial" + "Vos données sont sécurisées et ne seront jamais partagées"

**D6 root cause** : pas de pricing canon visible = la page OMK actuelle est en mode **lead-gen only** (audit stratégique) et le pricing vit probablement sur `/tarifs` (à implémenter) ou sur une page Notion/Calendly externe. **CTR leak** : un prospect qui veut comprendre le pricing doit booker un appel → friction vs canon "async 24h vault" Solaris.

### Messaging canon (D1 receipt text)

- **Tagline H1** : *"Arrêtez de travailler DANS votre entreprise. Travaillez SUR elle."*
- **Value prop sub** : "Nous structurons et automatisons les opérations des Small Business Owners. Déployez votre propre Business OS et libérez-vous des tâches manuelles, des oublis et de la charge mentale."
- **CTA primaire** : *"Lancer l'automatisation"* + *"Découvrir nos solutions"*
- **CTA audit** : *"Réserver un audit Business OS"* (topbar sticky)
- **Persona signals** :
  - "Built for Small Business Owners" (topbar sous-titre)
  - "Small Business Owners" (3× dans le H1+sub)
  - "Paris · Casablanca · Remote" (footer)
  - "Ingénierie opérationnelle" (méta-titre)
- **Mantra implicite** : "transformer votre entreprise manuelle en système autonome" (= "Self-Operating Business" footer)
- **Positioning unique** : **"Business OS" (terminologie propre)** + **Nova (IA vocale 24/7)** + **4 agents back-office** + **stack no-code orchestrée** (14 outils brandés)
- **Vocabulaire tech** : "no-code", "CRM", "SOP", "workflows", "automatisation", "agent vocal", "Self-Operating Businesses"

### Visual identity (D1 receipt HTML/CSS)

- **Logo** : "O" mark + "OMK SERVICES" + tagline "Operational Engineering"
- **Palette** : 8 hex détectés (`#34D399` vert, `#3B82F6`/`#60A5FA` bleus, `#8B5CF6`/`#A78BFA` violets, `#EC4899`/`#F472B6` roses, `#FBBF24` amber) = **palette moderne Tailwind-ish** (vraisemblablement emerald-400, blue-500, violet-500, pink-500, amber-400)
- **Typography** : 
  - **Space Grotesk** (display headings, géométique, tech-y)
  - **Inter** (body, neutre pro)
  - **JetBrains Mono** (telemetry, code-style)
- **Style direction** : **SaaS moderne / dashboard-first** (mock "business-os / overview LIVE · synced 2s ago" + KPIs animés) ≠ Solaris solar-amber editorial
- **Key visual elements** :
  - **Dashboard mockup animé** (KPIs live, pipeline, 4 KPI cells, audit progress bars)
  - **Nova call transcript mockup** (browser chrome + chat bubbles NOVA/CLIENT + Sentiment analysis)
  - **Stack logos grid** (14 outils brandés, animation subtle)
  - **Live indicator** (pulse vert "LIVE · synced 2s ago")
  - **4 agents back-office** (Intake, Translator, DocuFlow, Finance-Flow) avec status ONLINE

### Conformité ICP Nexus check (D1 receipt `ADR-ICP-NEXUS-001` Pilier 1-5)

| Pilier canon `ADR-ICP-NEXUS-001` | Landing OMK match | Score |
|---|---|---|
| **Pilier 1 — Persona "Expert méthodique / Praticien conformité"** | "Small Business Owners" (3×) + "facturation cabinet" (Nova demo) + "audit" = mixte, **cible small business générique PAS expert méthodique canon** | **1/5** |
| **Pilier 2 — Mantra "L'illusion de la complexité"** | AUCUNE mention de complexité/Zero-Knowledge — au contraire, OMK assume la stack (Notion+Airtable+Make+etc.) et fait de la **complexité visible un feature** | **0/5** |
| **Pilier 3 — Marché Family Offices / 84 Trilliards / cabinets juridiques** | AUCUNE mention de Family Office, héritage, secret professionnel, transfert générationnel. Cible = **SMB opérationnel**, pas expert-conformité | **0/5** |
| **Pilier 4 — Architecture 3-ICP (Solaris/Nexus/Orbiter)** | AUCUNE mention de 3-ICP, sister franchise, NEXUS sister. OMK est positionné comme **produit standalone**, pas comme 1 des 3 variants AaaS | **0/5** |
| **Pilier 5 — Killer Feature "Zero-PII Agentic Governance"** | AUCUNE mention de Zero-PII, Bare-Metal, Zero-Knowledge, AI-Act, Secret Professionnel. "Conforme RGPD" = badge générique, pas framework canon | **1/5** |
| **Bonus — Pricing canon Nexus Tier 1-4** | `/tarifs` 404, pas de pricing affiché, aucun $750/$1500 visible | **0/5** |
| **Bonus — Trust signals conformité critique (SOC2/HIPAA/AI-Act)** | "Conforme RGPD · données européennes" = 1 seul badge. Aucun SOC2/HIPAA/AI-Act/HITRUST/ISO27001 | **1/5** |

**Conformité globale ICP Nexus** : **3/35 = 9%** — **D3 nuance** : OMK a une **persona canon valide** (Business OS pour SMB), mais elle **NE MATCHE PAS** l'ICP Nexus canon. OMK est **proche d'Orbiter** (Mobile First / Terrain, ops-led) ou d'un **Solaris Tier 1-2** (PME Solo Standard). **C'est un PIVOT, pas un alignement**.

---

## DELIVERABLE 3 — Gap Analysis (cross-cut Solaris vs OMK vs Nexus Tier 4 cible)

| Dimension | **Solaris (canon local, D1 receipt)** | **OMK (PROD LIVE, D1 receipt)** | **Gap (Δ to Nexus Tier 4 canon)** | **Severity** | D6 root cause (1 line) |
|---|---|---|---|---|---|
| **Persona messaging** | "Stop hiring operators. Plug into our factory." + 4 archetypes (RevOps/Forges/AAA/Boutiques) = E-Myth techniciens/agences | "Small Business Owners" + "Business OS" + "Nova IA" = SMB générique, **pas Expert méthodique** | **CRITICAL** : aucune mention "Expert méthodique / Praticien conformité / Cabinet / Family Office / Avocat / Expert-comptable" | **CRITICAL** | `ADR-ICP-NEXUS-001:53-79` Pilier 1 verbatim "L'ICP Nexus opère dans le domaine de la vérité, de la conformité et de l'intimité" — OMK ignore 100% de ce persona |
| **Pricing tiers displayed** | 1 tier visible ($1,555/mo AAA archetype) ; 5 tiers canon ADR | **0 tier visible**, `/tarifs` 404, lead form segment CA 4 buckets | **CRITICAL** : aucun des 4 tiers canon Nexus ($750 / $1000-1500 / $1500-2000+25% / $5K-50K MRR) affiché | **CRITICAL** | Pas de page `/tarifs` implémentée (D6 ship OMK = lead-gen only, pas self-serve pricing) |
| **Pricing currency (USD/EUR)** | **USD** (post-accuponcture, sister `ADR-AAAS-PRICING-001` AMENDED) | **EUR** (form CA Annuel <100k€/>1M€) | **HIGH** : mismatch devise canon AaaS USD | **HIGH** | ADR-AAAS-PRICING-001 AMENDED 2026-06-24 "Hypothèse A retenue : USD post-accuponcture SUPERSEDE EUR" — OMK pas encore migré |
| **Visual identity (colors/typography)** | Solar amber `#e89b5c` + Instrument Serif + JetBrains Mono "operating signal" | Space Grotesk + Inter + JetBrains Mono + palette emerald/blue/violet/pink = **SaaS moderne** | **HIGH** : pas de "Citadelle du Savoir" feel, pas de gravité "Zero-PII Bare-Metal" | **HIGH** | OMK design = Tailwind-ish consumer SaaS ≠ Nexus canon "Citadelle" / "Souverain" verbatim `ADR-ICP-NEXUS-001:25160-25314` |
| **Killer Feature prominence** | 4 mécanismes Agentic Governance illustrés (B1/B2/B3) mais **pas nommés "Agentic Governance"** | **Aucun** ; Nova = agent vocal 24/7 générique, pas de Zero-PII/Bare-Metal/Secret Pro | **CRITICAL** : 5 mécanismes canon Nexus (Action Space Bounding / Sandboxing Bare-Metal / HITL Dynamique légal / Traçabilité AI-Act / Zero-PII Makkari) **0 mentionnés** | **CRITICAL** | ADR-ICP-NEXUS-001 Pilier 5 verbatim L19580 "Self-Hosting paranoïaque. Pas de SaaS public" — OMK stack = Notion+Airtable+Make (SaaS public) à l'opposé du canon |
| **CTA copy** | "submit your url" + "or contact the factory" = lead gen async | "Réserver mon audit stratégique" + "Réponse sous 24h · Visio · Aucun deck" = **RDV calendaire**, pas async | **HIGH** : canon Nexus = async 24h vault (verbatim Solaris sister `#vault-form`) ; OMK = visio 45min | **HIGH** | `Hero.tsx:59-64` "submit your url" = async 24h = modèle Solaris. OMK pivote sur visio = friction vs persona Expert méthodique (pas le temps) |
| **Trust signals (SOC2/AI Act/HIPAA)** | Aucun badge conformité canon (RATIFIED solaire pas ISO/SOC) | "Conforme RGPD · données européennes" = 1 badge | **CRITICAL** : aucun badge SOC2/AI-Act/HIPAA/ISO27001/HITRUST → **deal-breaker cabinet juridique / family office** | **CRITICAL** | "Une fuite de données d'un Family Office **détruit la Holding**" verbatim `ADR-ICP-NEXUS-001:21780` — un prospect Expert méthodique NE SIGNERA PAS sans SOC2+AI-Act+HIPAA |
| **Self-host messaging** | Implicite ("white-label / ghost factory / own your infra") | **Aucun** ; au contraire, OMK stack = Notion+Airtable+Make SaaS public | **CRITICAL** : canon Nexus = "Bare-Metal Zero-Knowledge" verbatim L19580 — OMK va à l'opposé | **CRITICAL** | `ADR-ICP-NEXUS-001:152` Pilier 5 mécanisme 2 "Sandboxing Bare-Metal Zero-Knowledge · **pas de SaaS public**" — OMK stack public SaaS = anti-pattern Nexus |
| **Conformité / Souveraineté badges** | Aucun | "RGPD" générique | **HIGH** : canon Nexus "Souverain" verbatim L25651, "AI-Act ready" canon sister | **HIGH** | AI-Act application totale **août 2026** = driver légal 6 semaines → tout landing Expert doit l'afficher |
| **Stack alignment** | Custom (B1/B2/B3 hierarchy = narration AaaS) | Notion+Airtable+Make+n8n+14 SaaS publics | **CRITICAL** : 14 SaaS publics = anti-pattern Nexus (verbatim L19580 "Pas de SaaS public") | **CRITICAL** | Stack OMK réel = no-code orchestration ≠ Bare-Metal Zero-Knowledge canon Nexus |
| **Internationalization (FR/EN)** | **FR only** (page.tsx H1 EN, mais sections FR mixtes ; pas d'i18n Next.js visible) | **FR only** (`<html lang="fr">`, `og:locale fr_FR`) | **MEDIUM** : canon Nexus cible FR+Suisse+Belgique+Luxembourg Family Offices (FR/EN/DE/nl) | **MEDIUM** | Pas de `next-intl` ni `i18n` config visible dans Solaris (single-lang) — A0 pas demandé i18n |
| **Sub-types personas (5 sub-types Nexus canon)** | 0/5 (Solaris cible agences, pas experts) | 0/5 (SMB générique) | **HIGH** : 5 sub-types canon (Expert-comptable/Avocat/Family-Office/Coach/Cabinet-médical verbatim L21519) **0 mentionnés** | **HIGH** | OMK landing n'a pas de segmentation verticale = tout prospect = "Small Business Owner" générique |
| **Mantra doctrinal explicite** | "L'illusion du sur-mesure" implicite (pas nommé sur landing) | "Self-Operating Business" (footer) ≠ "L'illusion de la complexité" canon | **HIGH** : "L'illusion de la complexité" verbatim L18408 NON visible | **HIGH** | Pas de tagline alignée mantra Nexus sur landing OMK |
| **Marché 84 Trilliards** | 0 (Solaris = marché 136,1 Mds$ intégrateurs sister) | 0 | **HIGH** : "84 Trilliards €" verbatim L19500 NON mentionné = **TAM perdu** | **HIGH** | TAM Family Office = 84T € = hook d'acquisition canon à brander sur landing |
| **Sections count + rhythm** | 11 sections bien rhythmées (Hero→Hook→Anatomy→Shield→Wheel→Archetype→Paradigm→Vault→CTA→Footer) | 10 sections (Hero→Trust→Overview→Stack→Méthode→BusinessOS→Nova→CTA→Footer) | **LOW** : count + rhythm proches | **LOW** | Structure éditoriale comparable |
| **3-ICP sister-symétrique visible** | `SOLARIS_HOLDING` data.ts:309-333 (NEXUS "02/03 Citadel · regulated firms" + ORBITER "03/03 Field" grisés) | **Aucune** mention 3-ICP | **MEDIUM** : pas de cross-link vers Solaris/Orbiter | **MEDIUM** | A0 sister-symétrie 3-ICP canon ADR-L2-AAAS-001 NON propagée aux landings |

### Top 3 CRITICAL gaps (synthèse)

1. **Persona + Killer Feature + Self-host = zéro alignement Nexus** (CRITICAL×3) : OMK ne mentionne pas "Expert méthodique", "Zero-PII Agentic Governance", "Bare-Metal Zero-Knowledge", ni aucun des 5 sub-types Nexus canon (Expert-comptable/Avocat/Family-Office/Coach/Cabinet-médical). **Cible actuelle "SMB générique" ≠ cible canon "expert-conformité 84 Trilliards €"**.
2. **Pricing canon Nexus invisible** (CRITICAL×2) : `/tarifs` 404 + aucun prix affiché + devise EUR (vs canon USD post-accuponcture) = **friction d'acquisition et mismatch devise canon AaaS**.
3. **Trust signals + Stack SaaS public = deal-breaker Family Office** (CRITICAL×2) : aucun SOC2/AI-Act/HIPAA + stack Notion+Airtable+Make+14 SaaS publics = **anti-pattern verbatim "Pas de SaaS public" L19580**.

### D3 nuance (anti-replacement)

OMK n'est **pas un landing "mauvais"** — il a sa propre canon valide pour la cible **SMB opérationnel / Orbiter-tier** (Mobile First / Terrain, ops-led). Le gap est un **PIVOT** : soit on aligne OMK vers Nexus (canon Expert-conformité), soit on **réalloue** OMK vers un sous-positionnement Orbiter Tier 1-2 (Small Business Owner/Field) et on crée un **nouveau landing Nexus séparé**. Voir **Deliverable 4** (Plan de Fixation OMK → Nexus) et **ADR-OMK-NEXUS-TRANSFORM-001 PROPOSED** sister pour l'arbitrage.

---

## Sister deliverables (cross-refs)

- **Deliverable 4 (Plan de Fixation)** : `wiki/hand_offs/omk_nexus_transformation_plan_2026-06-24.md` (4 phases A/B/C/D)
- **Sister ADR draft** : `_SPECS/ADR/L2_Business_OS/ADR-OMK-NEXUS-TRANSFORM-001_omk-to-nexus-pivot.md` (PROPOSED → target RATIFIED 2026-07-03)
- **Backup wiki handoff (ce fichier)** = D7 anti-effondrement canon
- **Sister ADRs canon** : `ADR-ICP-SOLARIS-001`, `ADR-ICP-NEXUS-001`, `ADR-AAAS-PRICING-001`, `ADR-L2-AAAS-001`
- **MCP source** : `mcp__vercel-omk__list_projects` (project ID non fetched, Vercel headers `X-Vercel-Id: cle1::5p2wr-...` confirme prod)
- **GitHub source** : `Amdkn/omk-landing` (mirroré 2026-06-17, non cloné localement — sister `wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md`)

## D6 lessons shipped (ce handoff)

- **#32** : Un landing "PROD LIVE" peut avoir 0% alignement avec un ICP canon sister (= 9% conformité Nexus pour OMK) sans que le canon ne le détecte → **audit gap-analysis D1 obligatoire** sister scope (D2 research-first missed 2026-06-17)
- **#33** : "Stack Notion+Airtable+Make+14 SaaS publics" = anti-pattern verbatim "Pas de SaaS public" L19580 du canon Nexus — **landing doit refléter le canon Stack** dès la copy
- **#34** : Page `/tarifs` annoncée en footer mais 404 = **anti-pattern UI** (lien mort = trust break) — sister anti-pattern = lien mort > absence de lien

---

**Auteur** : A1 Morty (Claude Code A2) — 2026-06-24 — exécution batch 4 livrables (1 handoff gap + 1 plan + 1 ADR PROPOSED + 1 log entry)
**D1 receipts cumulés** : 4 paths + 5 D1 file counts + 1 HTTP status + 1 URL + 1 pricing source + 1 OG meta + 5 verbatim ADR refs = 18 receipts
**Total D1 lines** : ~250 lignes D1-verified dans ce handoff
