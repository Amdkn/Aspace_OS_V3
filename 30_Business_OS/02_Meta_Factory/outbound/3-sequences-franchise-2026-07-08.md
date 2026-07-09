---
id: OMK-OUTBOUND-2026-07-08
title: 3 Séquences Outbound — Pitch Franchise-First (reframe des séquences Gemini : token-first → franchise-first)
type: Outbound Playbook (réutilisable, AIDA + AAARR, aligné ADR-OMK-PRODUCTS-001)
status: DRAFT (prêt meeting Abdaty mercredi ; ratification A0 pending)
date: 2026-07-08
deciders: [A0 Amadeus]
drafted_by: A0-Amodei (Murderbot méta-coach) sur GO A0 "GO séquences et GO séquences"
domain: L2 Business OS / OMK / OMK Meta Factory (P2) / 3 Variants ICP / $100M Offer
doctrine_anchors: [ADR-OMK-PRODUCTS-001, ADR-L2-AAAS-001, ADR-ICP-SOLARIS-001, ADR-ICP-NEXUS-001, ADR-ICP-ORBITER-001, ADR-AAAS-PRICING-001, ADR-MARKET-STUDY-001_the-builders-2026]
related: [Life-OS-2026 (Solaris prod), omk-services/00-omk-saas-os (Nexus prod), ABC-OS-COMMUNITY (Orbiter prod), Cibles Gemini (30 comptes B1/B2/B3), Wargames W03 CEO-Bench + W28 RunPane + W29 chain Mirofish]
provenance: |
  Née 2026-07-08 du GO A0 "GO séquences et GO séquences" après ratifier ADR-OMK-PRODUCTS-001
  (ligne verticale P1 BOS / P2 Meta Factory / P3 R&D, variants nichés dans P2). Reframe
  surgical des 3 séquences de l'étude Gemini qui vendaient la tuyauterie (Arbitrage de
  Jevons, RLS, équations vectorielles) en pitch FRANCHISE-FIRST (Built-to-Sell, souveraineté,
  déterminisme Mirofish/CEO-Bench). Tout ancrage prix sur ADR-AAAS-PRICING-001 (5 tiers
  USD post-accuponcture). Mapping Axe1↔Axe2 conservé de Gemini (hypothèse), RECON flaggée
  sur B2↔Nexus dans l'ADR-OMK-PRODUCTS-001 §"Matrice d'Offre".
supersedes: [les 3 séquences outbound token-first de l'étude Gemini 2026-07-08]
---

# 3 Séquences Outbound OMK — Pitch Franchise-First (Abdaty-ready)

> **Doctrine** (D3) : on ne vend pas la **tuyauterie** (« –90% de tokens », « RLS », « cache local ») — c'est la **preuve technique**, pas le désir. On vend la **franchise** : *transformer ton agence de main-d'œuvre en usine logicielle souveraine, scalable et revendable (Built-to-Sell)*. Le token-cost est un **effet**, pas l'offre. Source : `ADR-OMK-PRODUCTS-001` §D2.

> **Tarification** (D1) : ancré sur `ADR-AAAS-PRICING-001` (5 tiers canon USD post-accuponcture, 2026-06-24) :
> T1 PME Solo Founder **$300-500/an** · T2 PME Solo Standard **$500-1000/an** · T3 PME Groupe **$4000-5000/an** · T4 Nexus Pro **$30000-50000/an** · T5 Orbiter Enterprise **$100000-250000/an**.
> Les **3 séquences** ci-dessous s'addressent aux **3 segments $100M** (T3-T5 surtout) : l'outbound ROI justifie l'effort sur les comptes à ticket $30K+/an.

> **AIDA + AAARR** (mappés sur les 3 axes de `ADR-OMK-PRODUCTS-001`) :
> A = **signaux 2026** (recrutements Prompt Eng, stack Gong/Clay, post SaaS-pocalypse) ·
> I = **franchise vs main-d'œuvre** (vs le piège utilitaire) ·
> D = **Built-to-Sell + souveraineté** (matière noire sémantique locale = propriété revendable) ·
> A = **POC 30j / install <10j**.
> AAARR : Acquisition (signaux 2026) → Activation (install Docker <10j) → Rétention (**gravité des données**, matière noire = attrition ≈ 0) → Referral (affiliation Clay/Rev-Arch) → Revenue (forfait récurrent + $150/tenant/mois RLS — *à confirmer pricing canon*).

---

## Séquence 1 — B1 Outbound × **Solaris** (L'usine d'outreach autonome à haute intensité)

**Cibles primaires** (10 comptes Gemini, marché US) : Leadium (Las Vegas, ~60 emp.) · Whistle (Wilmington, 10-49) · SalesPipe (Miami) · SalesCaptain (Austin) · Outbound Sales Pro · Cleverly (LA) · OutboundFlow · Growthonics · Leadle · Reachly (Bangkok).

**Décideur** : CEO / Founder / VP of Sales Operations (Apollo/LinkedIn — matter noire = données d'enrichissement contacts manuelles, logs validation téléphone, séquences multicanal non indexées).

**Objet email** : *« De l'agence de services SDR à l'usine logicielle : rendre votre matière noire revendable »*

**Structure (8 phrases max, neutralité pronominale, CTO-grade)** :

> L'analyse du marché outbound US 2026 met en évidence une convergence structurelle : la **matière noire sémantique** (enrichissement, validation téléphone, séquencement multicanal) accumulée par les agences leaders devient leur **actif le plus difficile à répliquer** — et paradoxalement le plus exposé à la disruption LLM cloud. Les agences qui survivent en 2026-2027 ne sont pas celles qui négocient le forfait token au rabais ; ce sont celles qui transforment leur matière noire en **prototype de franchise industrialisable**.
>
> L'architecture **OMK Meta Factory** (sister canon d'OMK BOS, ratifiée 2026-06-21 — `ADR-OMK-PRODUCTS-001`) installe chez vous en moins de 10 jours une **usine d'outreach autonome à haute intensité** : déterminisme structuré par les simulations Mirofish + wargames CEO-Bench, gravité des données locale (R&D souverain, ADR-AAAS-PRICING-001), orchestration des 3 Variants (Solaris = cette configuration). Vous passez d'un modèle économique **vente d'heures de SDR** (risque marge, attrition) à un modèle **vente d'une plateforme franchisable** (Built-to-Sell, exit option).
>
> Variant **Solaris** taillé pour votre segment : tier d'entrée PME **$300-500/an** (POC 30 jours) jusqu'au tier Groupe **$4000-5000/an** (10+ clients simultanés), avec isolation RLS par tenant **$150/tenant/mois** si vous grandissez vers les grands comptes. La souveraineté de la donnée (Docker hermétique, RLS PostgreSQL, anti-réentraînement tiers) est une **condition de votre revente**, pas un bonus.
>
> Un échange de 20 minutes la semaine prochaine pour examiner votre funnel de qualification actuel et le POC.

**Pourquoi ça marche** : le « rêve » (Built-to-Sell) + la **preuve** (déterminisme Mirofish, pas une promesse) + l'**offre** (5 tiers ancrés) + l'**action** (POC 30j, install <10j). Aucune phrase ne parle d'« optimisation de token » — l'agent qui lira cette offre et qui négocie sur les tokens a déjà perdu la bataille : il se positionne comme un acheteur d'utilitaire, pas comme un acquéreur de franchise.

---

## Séquence 2 — B2 Growth × **Nexus** (Le hub multi-tenant souverain — piloter un empire à 2 personnes)

**Cibles primaires** : MeghRoop (10-49, USA) · Avenue Z (Miami, 51-200, **AEO/brand-visibility**) · NoGood (NYC, 50-100) · SaaS Hero · L&L Growth Agency · GrowthAssist (HIPAA) · OnDigi Solutions · Forge · Growth Division · LeadGem (Amsterdam).

**Décideur** : Founder / CEO / Lead Growth Engineer. **Matter noire** : WhatsApp/n8n payloads, AEO brand-visibility scores, multi-tenant conversion payloads, **PHI** (pour GrowthAssist HIPAA).

> ⚠️ **RECON flaggée** (D1) : `ADR-ICP-NEXUS-001` canon positionne Nexus sur **Expert méthodique / Conformité** (avocats, experts-comptables, family offices, cliniques) — pas sur Growth marketing. La séquence 2 ci-dessous **conserve l'hypothèse Gemini** (B2-Growth → Nexus) mais doit être **re-testée**. Si tu confirmes le mapping après cette campagne, ratifier ; sinon, remapper B2 sur un autre variant (ou créer un variant 4).

**Objet email** : *« Centralisez 100% de vos expériences de croissance en coffre-fort souverain — sans l'emploi d'un seul data engineer »*

**Structure** :

> Les agences de croissance gérant en parallèle les comptes de dizaines de startups (SaaS grand public, conformité CCPA/HIPAA) accumulent une **matière noire unique** : des milliers d'expériences d'acquisition validées ou invalidées, des payloads d'agents, des scores de visibilité AEO, des bases de reciblage. Cette matière noire est à la fois votre **actif le plus précieux** (ce qui vous distingue d'une agence Clay/n8n jetable) et votre **risque existentiel** (fuites cross-tenant, réentraînement non consenti, perte de clients grands comptes à la première fuite PII).
>
> OMK Meta Factory (sister canon d'OMK BOS — `ADR-OMK-PRODUCTS-001`) installe en moins de 10 jours le **hub multi-tenant souverain** qui transforme une équipe de 2 personnes en plateforme gérant 100+ clients en parallèle, **avec isolation cryptographique stricte par tenant** (PostgreSQL RLS, Docker hermétique, anti-réentraînement tiers garanti). Variant **Nexus** taillé pour ce segment : **Zero-PII Agentic Governance** + Safe Harbor sémantique, conforme AI-Act 2026-08-02 + RGPD + HIPAA selon le tenant. La matière noire de chaque client reste **son actif exclusif** ; votre agence passe du statut **d'exécutant Make/n8n jetable** à **partenaire d'infrastructure souverain**.
>
> Tier **Nexus Pro** ancré à **$30000-50000/an** (ADR-AAAS-PRICING-001 T4), avec isolation RLS par tenant additionnelle à **$150/tenant/mois** (cohérent avec le mode SaaS multi-client que vous gérez). Le POC 30 jours sur un seul tenant vous permet de mesurer la **gravité des données** : la matière noire s'accumule localement, la base sémantique se densifie, l'attrition client tombe vers zéro (le coût de switching du client devient prohibitif).
>
> 20 minutes la semaine prochaine pour examiner le tenant le plus sensible de votre portefeuille (généralement un compte HIPAA ou AEO-grand compte) et chiffrer la migration.

**Pourquoi ça marche** : « piloter un empire à 2 personnes » (dream outcome) + RLS/Safe Harbor (perceived likelihood — c'est un pattern canon, pas un hack) + $30K-50K/anchored tier (price credible) + isolation $150/tenant (expansion model, not discount). Le piège « coût API » est absent — l'offre n'est jamais en concurrence avec « attendre que les prix baissent ».

---

## Séquence 3 — B3 Enablement × **Orbiter** (Logicieliser votre méthodo MEDDICC/SPICED dans le CRM client)

**Cibles primaires** : Force Management (Charlotte, 51-200) · Winning by Design (Mountain View, 114) · Janek Performance · RAIN Group (Boston, 163) · Challenger · ValueSelling Associates · JB Sales (John Barrows) · Sandler Training (200-500) · Richardson Sales · The Brooks Group.

**Décideur** : CRO / Managing Director / VP of Sales Enablement. **Matter noire** : transcriptions d'appels, scripts de re-framing Challenger, value stories ValueSelling, plans d'action VP Sales, diagnostics de compétences — **tous sous NDA** (hautement confidentiel).

**Objet email** : *« Logicieliser votre méthode de vente dans le CRM de chaque client — sans qu'un seul octet stratégique quitte leur réseau »*

**Structure** :

> Les cabinets d'enablement vendent aujourd'hui des **heures de formation** et des **audits manuels** — un modèle qui plafonne dès que le cabinet refuse de croître (le fondateur sature, les consultants seniors partent, la méthodologie fuit). Le cabinet qui survit en 2026-2027 est celui qui **logicielise sa propre méthodologie** dans un auditeur sémantique que le client installe directement dans son CRM, sans dépendance continue sur le cabinet.
>
> OMK Meta Factory (sister canon d'OMK BOS — `ADR-OMK-PRODUCTS-001`) installe en moins de 10 jours **l'usine d'audit sémantique Orbiter** : vos grilles MEDDICC / SPICED / Challenger / ValueSelling deviennent des **modèles sémantiques locaux** dans une instance Docker hermétique par client. L'auditeur se couple aux **étapes réelles du CRM** (Discovery vs. Closing), note les comportements de vente **selon la grille attendue à cette étape**, et apprend à partir de **votre** base de transcriptions (pas d'un LLM tiers qui réentraînerait sur vos données confidentielles). **Aucune transcription, aucun plan d'action, aucune value story ne quitte le pare-feu du client** : la souveraineté NDA est une condition de la revente, pas un bonus.
>
> Tier **Orbiter Enterprise** ancré à **$100000-250000/an** (ADR-AAAS-PRICING-001 T5) : c'est le segment qui paye pour la **propriété intellectuelle logicielisée** (MEDDICC-as-a-Service, SPICED-as-a-Service), pas pour des heures. Le cabinet vend ensuite à chaque client une **prothèse cognitive de direction commerciale** — Built-to-Sell, exit option par acquisition de la stack logicielle.
>
> POC 30 jours sur **une** méthodologie propriétaire (MEDDICC chez Force Management, SPICED chez Winning by Design) pour mesurer l'alignement grille-CRM et la qualité de l'audit.
>
> 20 minutes la semaine prochaine pour examiner votre méthodologie la plus standardisée et chiffrer la logicielisation.

**Pourquoi ça marche** : « logicieliser MA méthodologie » (Built-to-Sell + IP-as-software) + « prothèse cognitive de direction commerciale » (descriptif précis vs. générique) + NDA + tier $100K-250K (seul segment à 6-7 chiffres). On ne vend pas un auditeur — on vend **un actif que le client peut revendre**.

---

## 3 séquences, ce qui est commun (D4)

1. **Aucune mention du coût API.** Pas une fois, pas comme effet. C'est une **preuve technique**, pas le pitch. Si un prospect le demande en réplique, c'est un signal d'achat d'utilitaire — on le relit ensemble.
2. **Tier canon ancré** sur `ADR-AAAS-PRICING-001` (D1 receipts). Pas de chiffre inventé.
3. **POC 30 jours, install <10 jours** = AIDA-Action. Le « 20 minutes » est calibré pour 30 cibles / semaine en SDR semi-automatisé.
4. **3 Variants distincts, 1 prototype de franchise** (D1) : P2 Meta Factory = la même usine configurée différemment. La cohérence du discours est l'anti-pitch-dégénéré.
5. **Liens canon présents** : `ADR-OMK-PRODUCTS-001`, `ADR-L2-AAAS-001`, `ADR-AAAS-PRICING-001`, `ADR-ICP-{SOLARIS,NEXUS,ORBITER}-001` (les 3 sisters ratifiées). Le prospect qui creuse trouve le canon, pas une promesse.
6. **RECON B2↔Nexus flaggée** explicitement dans l'ADR-OMK-PRODUCTS-001. Si la campagne invalide ce mapping, remapper ; sinon ratifier dans l'ADR-ICP-NEXUS-001 §"Targeting".

## Ratification & next

- **A0 ratifier** ce draft avant le meeting Abdaty.
- **Vétos possibles** : (a) nom P2 (« Meta Factory »), (b) mapping B2↔Nexus, (c) pricing $150/tenant (à confirmer ADR-AAAS-PRICING-001), (d) tonalité CTO-grade (ajuster voix).
- **Next, après ratification** : dry-run sur les 3 premières cibles B1 (Leadium/Whistle/SalesPipe) avec les Replies attendues comme outcome mesurable (Book H1, SARU H3).
