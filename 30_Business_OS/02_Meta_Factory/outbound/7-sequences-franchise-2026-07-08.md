---
id: OMK-OUTBOUND-2026-07-08-v2
title: 7 Séquences Outbound (3 Strates × 10 ICPs canon) — Pitch Franchise-First, Abdaty-ready
type: Outbound Playbook (réutilisable, AIDA + AAARR, aligné ADR-OMK-PRODUCTS-001 v2 + ADR-NEXUS-10-ICP-001)
status: DRAFT v2 (amendement de 3-sequences-franchise-2026-07-08.md, étendu de 3 à 7 séquences par rectification scope L2 — Strate A + Strate C ajoutées)
date: 2026-07-08
deciders: [A0 Amadeus]
drafted_by: A0-Amodei (Murderbot méta-coach) sur GO A0 "t'as complètement oublié l'ICP et Niches des Coachs"
domain: L2 Business OS / OMK / OMK Meta Factory (P2) / 3 Strates × 10 ICPs / $100M Offer
doctrine_anchors: [ADR-OMK-PRODUCTS-001, ADR-NEXUS-10-ICP-001 (RATIFIED 2026-07-08), ADR-ICP-NEXUS-001, ADR-ICP-SOLARIS-001, ADR-ICP-ORBITER-001, ADR-L2-AAAS-001, ADR-AAAS-PRICING-001, ADR-MARKET-STUDY-001, ADR-SOBER-002, PRD-NEXUS-EVOLUTION-IA-001]
supersedes: [3-sequences-franchise-2026-07-08.md (3 séquences, Strate B uniquement)]
related: [plan-L2-business-os.md §13 (pricing $1000/mois gated), wargames 05-legal-dlp / 06-growth-aaarr / 07-sales-quiz / 08-picard-mirofish / 09-gstack, `ADR-NEXUS-LANDING-PERSONAS-001` (5 personas)]
provenance: |
  Née 2026-07-08 (v1) puis amendée 2026-07-08 (v2) du GO A0 rectifiant un oubli : les
  3 séquences v1 ne couvraient que la Strate B (B1/B2/B3) de l'étude Gemini, omettant
  la Strate A (Coachs C-Suite, leadership grand volume, M&A) ET la Strate C (Fractional
  COO, SOP vaulting, Patrimoine B2B, Conduite du changement). Or, la cible canon de
  Nexus per `ADR-ICP-NEXUS-001` RATIFIED pilier 3 inclut « coachs, experts-comptables,
  avocats, family offices » — c'est-à-dire précisément la Strate A. La v2 étend à 7
  séquences couvrant les 3 strates, sister canon `ADR-NEXUS-10-ICP-001`.
sign_off_a0: "pending"
---

# 7 Séquences Outbound OMK — 3 Strates × 10 ICPs (Franchise-First, Abdaty-ready)

> **Doctrine (D3)** : on ne vend pas la **tuyauterie** (« –90% de tokens », « RLS », « cache local ») — c'est la **preuve technique**, pas le désir. On vend la **franchise** : *transformer ta matière noire (savoir-faire, méthodologie, propriété intellectuelle) en usine logicielle souveraine, scalable et revendable (Built-to-Sell)*. Le token-cost est un **effet**, pas l'offre.
>
> **Tarification (D1)** : ancré sur `ADR-AAAS-PRICING-001` (5 tiers canon USD post-accuponcture, 2026-06-24) :
> T1 PME Solo Founder **$300-500/an** · T2 PME Solo Standard **$500-1000/an** · T3 PME Groupe **$4000-5000/an** · T4 Nexus Pro **$30000-50000/an** · T5 Orbiter Enterprise **$100000-250000/an**.
>
> **AIDA + AAARR** (mappés sur les 3 axes de `ADR-OMK-PRODUCTS-001`) :
> A = **signaux 2026** (recrutements Prompt Eng, stack Gong/Clay, post SaaS-pocalypse) ·
> I = **franchise vs main-d'œuvre** (vs le piège utilitaire) ·
> D = **Built-to-Sell + souveraineté** (matière noire sémantique locale = propriété revendable) ·
> A = **POC 30j / install <10j** (audit Sdiri + wargame process).
> AAARR : Acquisition (signaux) → Activation (POC) → Rétention (**gravité des données**, attrition ≈ 0) → Referral (affiliation Clay/Rev-Arch/Clara Sterling) → Revenue (forfait récurrent + $150/tenant/mois RLS — *à confirmer pricing canon*).

---

## Doctrine commune (7 séquences — ce qui ne change jamais, D4)

1. **Aucune mention du coût API.** Jamais. C'est un **effet**, pas le pitch. Si un prospect le demande en réplique, c'est un signal d'achat utilitaire — on le relit ensemble ou on l'écarte (T3-T5 ROI > T1-T2 « chasseur de rabais »).
2. **Le Pitch = la propriété intellectuelle du client, softwarelisée.** Toujours, sans exception. L'OS ne remplace pas le coach/l'agence/le COO — **il softwarelise ce qu'ils vendaient en heures**.
3. **Tier canon ancré** sur `ADR-AAAS-PRICING-001` (D1 receipts). Pas de chiffre inventé.
4. **POC 30 jours, install <10 jours** = AIDA-Action. Le « 20 minutes » est calibré pour 30 cibles / semaine en SDR semi-automatisé.
5. **3 Variants distincts, 1 prototype de franchise** (D1) : P2 Meta Factory = la même usine configurée différemment. La cohérence du discours est l'anti-pitch-dégénéré.
6. **Liens canon présents** : `ADR-OMK-PRODUCTS-001`, `ADR-NEXUS-10-ICP-001`, `ADR-ICP-NEXUS-001` (et sister Solaris/Orbiter), `ADR-AAAS-PRICING-001`, `PRD-NEXUS-EVOLUTION-IA-001` (les 5 modules).
7. **Filtre PRD §7 strict** : pas de pitch local-first 0,01$ (différé 2027), pas de chiffres non sourcés, pas de features inventées, pas de dissolution du veto Beth.

---

# Strate A — Cabinets de Coaching Exécutif & Alignement Organisationnel
*Persona-anchor : Marcus Vance — Managing Partner, coaching C-Suite*
*Iceberg : 12h/sem de comptes-rendus manuels + panique conformité (EU AI Act, fuite PII vers cloud grand public)*

## Séquence A1 — Coaching C-Suite haut de gamme → « Le Chef de Cabinet IA »
**Cibles (D1, marché US + EU)** : cabinets de coaching de partners (revenus > $500K/an) accompagnant VPs/directeurs ; « expertise méthodique » = ICP Nexus canon (pilier 1 verbatim).
**Variant (Axe 2)** : Nexus (Conformité, ZPAG) · **Tier** : T3 PME Groupe $4-5K/an → T4 Nexus Pro $30-50K/an (cabinets multi-partners)
**Objet email** : *« Le Chef de Cabinet IA : softwarelise ta synthèse qualitative, sans qu'un mot de tes sessions C-Suite quitte ton réseau »*

> L'analyse du coaching C-Suite 2026 met en évidence une **fuite structurelle** : la **synthèse qualitative** de chaque session (12h/sem par coach senior, valorisée $400-800/h) est le **capital intellectuel** le plus difficile à reconstruire — et paradoxalement le plus exposé à la disruption (L'IA générative, EU AI Act 2026-08-02, fuite PII vers cloud grand public, secret professionnel). Les cabinets qui survivent en 2026-2027 ne sont pas ceux qui négocient les prix LLM au rabais ; ce sont ceux qui **softwarelisent leur méthodologie de synthèse** dans une instance Docker hermétique, sous DLP bare-metal, livrée clé-en-main en moins de 10 jours.
>
> L'architecture **OMK Meta Factory** (sister canon d'OMK BOS, ratifiée 2026-06-21 — `ADR-OMK-PRODUCTS-001`) installe chez toi **le Chef de Cabinet IA** : Audit Sdiri de tes process de synthèse (Module 1 du pack) + Wargame Fable de chaque workflow critique (Module 2) + DLP bare-metal (Module 5, wargame 05 déjà validé 12/12). Tu passes d'un modèle **vente d'heures de synthèse** (plafond = 1 coach senior × 50h/sem × 4 clients) à un modèle **vente d'un OS de synthèse franchisable** (multi-clients, Built-to-Sell, exit option).
>
> Tier **PME Groupe $4-5K/an** (T3) pour un cabinet solo multi-partners, jusqu'à **Nexus Pro $30-50K/an** (T4) pour les cabinets à 10+ coaches opérant en parallèle sur des cohorts. ZPAG = **Zero-PII Agentic Governance** (extension des 4 mécanismes Agentic Governance sister Solaris, pilier 5 du canon Nexus) : aucun mot de session ne quitte ton Docker, conformité AI Act article 12 audit-ready.
>
> 20 minutes la semaine prochaine pour examiner ton process de synthèse actuel et chiffrer le POC 30 jours.

## Séquence A2 — Leadership Development grand volume → « L'Orchestrateur de Cohort »
**Cibles** : cabinets corporate à programmes managériaux (cohorts de 30-200 managers) qui ingèrent des historiques RAG massifs sur cloud public.
**Variant** : Nexus · **Tier** : T4 ($30-50K/an)
**Objet** : *« Arrête de payer l'inférence RAG à chaque cohort : softwarelise le pipeline d'ingestion »*

> Le cabinet de leadership development qui gère en parallèle 10+ cohorts (chacune 30-200 managers, 18-24 mois de programme) explose ses factures API cloud quand il tente d'injecter l'historique entier d'un cohort dans le RAG. La marge part en fumée à mesure que le cabinet grandit (le fameux **paradoxe de Jevons**). L'alternative n'est pas de baisser les coûts d'inférence (illusion 2027) — c'est de **softwareliser le pipeline d'ingestion une fois** et de le **réutiliser par franchise** sur chaque nouveau cohort.
>
> OMK Meta Factory installe l'**Orchestrateur de Cohort** : Audit + Wargame du pipeline d'ingestion RAG (Module 2) + **CEO-Bench** sur la qualité pédagogique de chaque cohort (Module 3, détecte les angles morts dans le curriculum avant qu'ils ne coûtent une promo). L'instance Docker hermétique te permet d'avaler l'historique entier d'un cohort sans payer le cloud au volume.
>
> Tier **Nexus Pro $30-50K/an** (T4). POC 30 jours sur un cohort (ingestion RAG + CEO-Bench du curriculum). La gravité des données (l'historique pédagogique s'accumule) verrouille l'attrition à ≈ 0.
>
> 20 minutes pour examiner ton cohort le plus actif.

## Séquence A3 — Coach M&A / Transition / Crise → « Le Sanctuaire de la Transaction »
**Cibles** : professionnels solos ou petits cabinets M&A/restructuration (revenus > $1M/an) — secret industriel, données fusions-acquisitions.
**Variant** : Nexus (secret professionnel, ZPAG maximal) · **Tier** : T4 → T5 ($30K-$250K/an)
**Objet** : *« Une fuite en M&A détruit la Holding : softwarelise le process, pas la promesse »*

> Le coach M&A travaille sur des dossiers où **une fuite détruit la Holding** (verbatim canon Nexus, pilier 1). Le risque n'est pas le coût d'inférence ; c'est l'**exposition NDA** d'un document stratégique à un LLM cloud tiers qui le réinjecte ailleurs. La panique conformité AI Act 2026-08-02 + secret professionnel avocat/notaire ne se gère pas par un **politique de sécurité** — elle se gère par une **garantie technique d'architecture** (Docker hermétique, DLP bare-metal, action-space bounding).
>
> OMK Meta Factory installe **le Sanctuaire de la Transaction** : **DLP bare-metal prioritaire** (Module 5, wargame 05) + Audit conformité AI Act article 12 (Module 1) + Wargame Fable de chaque process NDA (Module 2). Le coach vend ensuite à son client (banquier d'affaires, avocat, family office) la **garantie technique d'inviolabilité** comme un produit — Built-to-Sell, exit option, **mark-up competence** que le cloud ne peut pas donner.
>
> Tier **T4-T5** selon le portefeuille de clients. POC 30 jours sur un dossier de restructuration réelle (anonymisé).
>
> 20 minutes confidentiel (signé NDA).

---

# Strate B — Agences de Croissance, Prospection & Business Development
*Focus prioritaire A+ (PRD canon). Persona-anchor : Harrison Vance/Clara Sterling (B1) · Amara Sow (B2) · Christian Vance (B3).*
*Iceberg : matière noire = enrichissement contacts, séquences multicanal, expériences de croissance validées, transcriptions d'appels, scores de qualification.*

## Séquence B1 — Agences SDR/BDR as a Service → « L'Arbitrage Jevons »
**Cibles** : 10 comptes Gemini (Leadium/Las Vegas · Whistle/Wilmington · SalesPipe/Miami · SalesCaptain/Austin · Outbound Sales Pro · Cleverly/LA · OutboundFlow · Growthonics · Leadle · Reachly/Bangkok).
**Variant** : Solaris ou Nexus multi-tenant · **Tier** : T2-T3 ($500-$5K/an)
**Objet** : *« De l'agence de services SDR à l'usine logicielle : rends ta matière noire revendable »*

> L'analyse du marché outbound US 2026 met en évidence une convergence structurelle : la **matière noire sémantique** (enrichissement, validation téléphone, séquencement multicanal) accumulée par les agences leaders devient leur **actif le plus difficile à répliquer** — et paradoxalement le plus exposé à la disruption LLM cloud. Les agences qui survivent en 2026-2027 ne sont pas celles qui négocient le forfait token au rabais ; ce sont celles qui transforment leur matière noire en **prototype de franchise industrialisable**.
>
> L'architecture **OMK Meta Factory** installe chez toi en moins de 10 jours une **usine d'outreach autonome à haute intensité** : déterminisme structuré par les **simulations Mirofish** + **wargames CEO-Bench**, gravité des données locale, orchestration **Gstack** (wargame 09 déjà validé 12/12) des 3 Variants (Solaris = cette configuration). Tu passes d'un modèle **vente d'heures de SDR** (risque marge, attrition) à un modèle **vente d'une plateforme franchisable** (Built-to-Sell, exit option).
>
> Tier **PME Solo $500-1000/an** (T2) jusqu'au tier Groupe **$4-5K/an** (T3), avec isolation RLS par tenant **$150/tenant/mois** (à confirmer ADR-AAAS-PRICING-001) si tu grandis vers les grands comptes. La souveraineté de la donnée (Docker hermétique, RLS PostgreSQL, anti-réentraînement tiers) est une **condition de ta revente**, pas un bonus.
>
> 20 minutes la semaine prochaine pour examiner ton funnel de qualification actuel et le POC 30 jours.

## Séquence B2 — Agences Growth Marketing B2B native-IA → « Le Harnais Multi-Tenant »
**Cibles** : 10 comptes (MeghRoop · Avenue Z/Miami · NoGood/NYC · SaaS Hero · L&L Growth Agency · GrowthAssist/HIPAA · OnDigi · Forge · Growth Division · LeadGem/Amsterdam).
**Variant** : Nexus *(hypothèse à valider — voir RECON)* · **Tier** : T3-T4
**Objet** : *« Centralise 100% de tes expériences de croissance en coffre-fort souverain — sans data engineer »*

> Les agences growth gérant en parallèle les comptes de dizaines de startups accumulent une **matière noire unique** : des milliers d'expériences d'acquisition validées ou invalidées, des payloads d'agents, des scores de visibilité AEO, des bases de reciblage. Cette matière noire est à la fois ton **actif le plus précieux** et ton **risque existentiel** (fuites cross-tenant, réentraînement non consenti, perte de clients grands comptes à la première fuite PII).
>
> OMK Meta Factory installe en moins de 10 jours le **hub multi-tenant souverain** : **Audit étanchéité** (Module 1) + **Wargame RLS** (Module 2) + **orchestration Gstack** (Module 5) pour piloter 100+ clients en parallèle, **avec isolation cryptographique stricte par tenant** (PostgreSQL RLS, Docker hermétique, anti-réentraînement tiers garanti). La matière noire de chaque client reste **son actif exclusif** ; ton agence passe du statut **d'exécutant Make/n8n jetable** à **partenaire d'infrastructure souverain**.
>
> Tier **Nexus Pro $30-50K/an** (T4), avec isolation RLS par tenant additionnelle à **$150/tenant/mois**. POC 30 jours sur un tenant (généralement HIPAA ou AEO-grand compte) pour mesurer la **gravité des données**.
>
> 20 minutes pour examiner le tenant le plus sensible de ton portefeuille et chiffrer la migration.

## Séquence B3 — Cabinets Sales Enablement → « L'Évaluateur Stage-Aware »
**Cibles** : 10 comptes (Force Mgmt/Charlotte · Winning by Design/Mountain View · Janek · RAIN Group/Boston · Challenger · ValueSelling · JB Sales · Sandler · Richardson · Brooks Group).
**Variant** : Orbiter ou Nexus stage-aware · **Tier** : T3-T4
**Objet** : *« Logicielise MEDDICC/SPICED dans le CRM client — sans qu'un octet NDA quitte son réseau »*

> Les cabinets d'enablement vendent des **heures de formation** et des **audits manuels** — un modèle qui plafonne (le fondateur sature, les consultants seniors partent, la méthodologie fuit). Le cabinet qui survient en 2026-2027 **logicielise sa propre méthodologie** dans un auditeur sémantique installé directement dans le CRM du client, sans dépendance continue sur le cabinet.
>
> OMK Meta Factory installe en moins de 10 jours **l'usine d'audit sémantique** : tes grilles MEDDICC / SPICED / Challenger / ValueSelling deviennent des **modèles sémantiques locaux** dans une instance Docker hermétique par client. L'auditeur se couple aux **étapes réelles du CRM** (Discovery vs. Closing), note les comportements de vente **selon la grille attendue à cette étape** (Module 2 Wargame du pipeline de scoring + Module 3 CEO-Bench sur tes playbooks). **Aucune transcription, aucun plan d'action ne quitte le pare-feu du client** : la souveraineté NDA est une condition de la revente.
>
> Tier **T3-T4**. Le cabinet vend ensuite à chaque client une **prothèse cognitive de direction commerciale** — Built-to-Sell, exit option par acquisition de la stack logicielle.
>
> POC 30 jours sur une méthodologie propriétaire. 20 minutes pour examiner ta grille la plus standardisée.

---

# Strate C — Écosystèmes de Conseil Opérationnel & Systématisation
*Persona-anchor : David Kross — fractional COO ×15 PME*
*Iceberg : SOPs statiques jamais appliqués, onboarding client = conduite du changement manuelle.*

## Séquence C1-C2 — Fractional COO / SOP Vaulting → « SOPs → Skills exécutables »
**Cibles** : cabinets de Direction Opérationnelle Fractionnée gérant 10-20 PME en parallèle ; cabinets d'audit & standardisation des modes opératoires.
**Variant** : Solaris (Knowledge Bus) ou Nexus (systématisation) · **Tier** : T3-T4
**Objet** : *« Tes manuels SOP deviennent des Skills agentiques — exécutés par les clients, plus par toi »*

> Les cabinets de Fractional COO et de SOP vaulting détiennent un **actif dormant** : des années de méthodologie accumulée dans des manuels .pdf, des Notion, des Google Docs que **personne n'applique vraiment** chez les clients. Le cabinet facture des heures pour ré-expliquer la même procédure à chaque onboarding. L'attrition client est élevée (le client oublie le manuel, le cabinet re-facture). Le cabinet qui survient en 2026-2027 **convertit ses SOPs en Skills agentiques** : chaque procédure devient un exécutable local (Docker hermétique, audit-ready, traçable).
>
> OMK Meta Factory installe : **Wargame du portfolio-client** (Module 2) + **MiroFish** (Module 4, simulations de cohort d'onboarding avant déploiement) + conversion de tes manuels en Skills exécutables. L'orchestration **Gstack** (Module 5) te permet ensuite de **garder les lumières allumées** pour 20+ clients en parallèle, **sans embaucher**.
>
> Tier **T3-T4** selon le portefeuille. Le cabinet vend à chaque client un **OS de standardisation** (Built-to-Sell, exit option par acquisition de la stack). Le manuel mort devient une **prothèse cognitive de COO-augmented**.
>
> 20 minutes pour examiner un de tes SOPs les plus ré-expliqués.

## Séquence C3 — Gestion Patrimoine B2B / Planification Financière High-Ticket → « Le Coffre-Fort Patrimonial »
**Cibles** : cabinets de gestion de patrimoine pour dirigeants d'entreprise (revenus > $1M/an) ; **pilier 3 verbatim** du canon Nexus.
**Variant** : Nexus (secret professionnel) · **Tier** : T4-T5
**Objet** : *« RGPD + secret professionnel + secret bancaire : softwarelise la conformité du reporting »*

> Le cabinet de gestion patrimoine B2B traite des **données parmi les plus sensibles** du marché : identité des dirigeants, structures holdings, expositions fiscales, successions. La **récurrence** des process admin (reporting trimestriel, conformité, déclarations) est exactement le profil que l'**automatisation par cache sémantique local** sait absorber — sans qu'une seule donnée patrimoniale ne quitte le pare-feu du cabinet.
>
> OMK Meta Factory installe **le Coffre-Fort Patrimonial** : **DLP bare-metal** (Module 5, PRIORITÉ 1) + **Audit conformité** (Module 1) + **Wargame des process reporting** (Module 2). Le cabinet peut ensuite revendre à chaque client une **garantie technique d'inviolabilité** comme un produit — Built-to-Sell, exit option.
>
> Tier **T4-T5** selon AUM. POC 30 jours sur un process de reporting trimestriel (anonymisé).
>
> 20 minutes confidentiel (NDA).

## Séquence C4 — Conduite du Changement & Transformation Digitale → « L'Infrastructure Officielle de la Transformation » *(canal partenaire — Built-to-Sell par alliance)*
**Cibles** : cabinets de conseil prescrivant des solutions logicielles à leurs clients.
**Variant** : Solaris/Nexus/Orbiter selon le client final · **Tier** : T4 + **rev share partenaire**
**Objet** : *« Deviens prescripteur de l'OS que tu prescrivais déjà — avec rev share récurrent »*

> Les cabinets de conduite du changement prescrivent déjà des solutions logicielles à leurs clients. La friction : prescrire un SaaS tiers, c'est **remercier le client qui paie le SaaS, pas toi** ; prescrire un OS on-premise, c'est **devenir responsable de l'infra**. **OMK Meta Factory résout ce dilemme** : l'OS est livré en Docker hermétique clé-en-main, le cabinet le prescrit, **le client devient multi-tenant du cabinet** (rev share partenaire récurrent).
>
> Built-to-Sell **par alliance** : tu ne vends pas le logiciel — tu prescris l'infrastructure officielle de la transformation que tu vends déjà. Ton cabinet passe du statut **d'évangéliste de SaaS tiers** (revenu one-shot) à **de partenaire d'infrastructure souverain** (revenu récurrent, attribution du cabinet).
>
> Tier **T4 + rev share partenaire** (20-30% récurrent sur le forfait Nexus Pro). **4 simulations `/office-hours` (wargame 09 M4)** testent ta première prescription contre tes 3 personas cibles avant tout déploiement réel.
>
> 30 minutes — c'est un partenariat, pas une vente.

---

## Ce qui est commun (récap D4)

| # | Invariant | Source |
|---|---|---|
| 1 | **Aucun coût API mentionné** | Reframe A0 (D2) + ADR-OMK-PRODUCTS-001 §D2 |
| 2 | **Le Pitch = la propriété intellectuelle du client, softwarelisée** | PRD §1 pivot doctrinal + ADR-OMK-PRODUCTS-001 §D1 |
| 3 | **Tier ancré ADR-AAAS-PRICING-001** | D1 receipts |
| 4 | **POC 30j / install <10j** | PRD §2 value equation |
| 5 | **1 prototype de franchise (P2 Meta Factory)** | ADR-OMK-PRODUCTS-001 §D1 |
| 6 | **Liens canon présents** | ADR-NEXUS-10-ICP-001 + ADR-ICP-* + ADR-AAAS-PRICING-001 |
| 7 | **Filtre §7 PRD strict** (no local-first 0,01$, no fake features) | PRD §7 + ADR-SOBER-002 |

## Ratification & next

- **A0 ratifier** ce draft avant le meeting Abdaty mercredi.
- **Vétos possibles** : (a) nom P2 « Meta Factory », (b) mapping B2↔Nexus, (c) pricing $150/tenant, (d) tonalité CTO-grade, (e) ajout/retrait de séquences, (f) ordre des strates (focus prioritaire Strate B respecté per PRD §3).
- **Next, après ratification** : dry-run sur les 3 premières cibles **Strate A** (A1 cabinet C-Suite, A2 leadership grand volume, A3 M&A coach) — Book H1 measurement + SARU H3 conversion. La Strate A était la moins touchée par les drafts précédents, c'est l'angle mort à corriger en premier.
- **Sister à élever** : `PRD-NEXUS-EVOLUTION-IA-001` DRAFT v1 → v2 (intégrer l'ADR-NEXUS-10-ICP-001 ratifié).
