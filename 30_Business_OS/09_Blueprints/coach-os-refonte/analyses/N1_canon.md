# N1 — Carte du canon `01-omk-business-os`

**Périmètre lu** : `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\01-omk-business-os`
**Date du relevé** : 2026-08-05
**Jonctions écartées** : 1, à savoir `B2_Business_Domains\03_Product_Flash_Avengers\02-omk-services-business-os` (vers le dépôt de code). Non entré, conformément à la consigne.

---

## 1. Que déclare ce dépôt ?

Le dépôt n'a pas de `README.md`, de `CANON.md` ni de `NORTH_STAR.md` à la racine. Ce qui s'y présente comme des points d'entrée se devine par le format des fichiers : frontmatter typé, schéma constant, niveau d'autorité assumé.

| Mot | Désigne, en une phrase | Fichier qui le dit |
|---|---|---|
| **charte** | Spécification à 9 sections d'un livrable borné (Périmètre / Livrables / Gates / Aborts / DoD / Gaps), avec frontmatter `type: charte`, `rock_id`, `b2_owner`, `b3_squad`, `icp`, `doctrine_lock`. C'est le format canon W40 M3 — la *charte dit le QUOI*. | `chartes\phase_c_saas_auth.md` (9 sections numérotées, frontmatter complet) ; le format est imposé en miroir par les 25 fichiers de `chartes_cycle_2\`. |
| **runbook** | Plan d'exécution HITL-gated (M1-M5+), dérivé d'une charte source. Il transforme le QUOI en HOW — commandes bash, snippets code, gates runtime. Toujours ≤300 l. | `runbooks\runbook-C-saas-auth.md:11` (« transformer la chart `phase_c_saas_auth.md` en pattern d'exécution »). Sister : `runbooks\runbook-D-repositories.md`. |
| **ownerbook** | Document de *clôture* d'un Rock, produit par B1 Jerry en fin de cycle pour le owner. Il consolide mission, design, DoD, chartes à produire, runbooks à produire, aborts, red-team, et le spécifique marché (US/Euro). | `ownerbooks\ownerbook_T1_people_ops_product.md:9` (« B1 Jerry → A0 (T1 close) : 1 Ownerbook per Rock per cycle »). Trois ownerbooks pour T1/T2/T3. |
| **B2 (control room)** | Salle de supervision d'un domaine. Le captain B2 transforme la direction B1 en Rocks + DoD + JTBD pour le swarm B3, sans micro-manager. | `B2_Business_Domains\04_Ops_Batman_Fantastic4\00_B2_DOMAIN_CONTROL_ROOM.md` (mission explicite). Même gabarit pour `05/06/07/08`. |
| **B3 (swarm)** | Moteur d'exécution : squad d'agents qui exécute les paquets JTBD de B2 en autonomie, escalade uniquement quand le contrat ne peut être satisfait. | `B3_Warp_Core_Execution\README.md:11` (« Executes Rocks assigned by B2 managers within W1–W12 cycle »). Config par swarm dans `00_B3_SWARM_CONFIG.md`. |
| **Warp Core Execution** | Cycle de 12 semaines (12WY = W1–W12) avec Lead/Lag logs, artifact proofs, blocker protocol. Doctrine générique d'exécution par cycle. | `B3_Warp_Core_Execution\README.md:35` (cycle W1–W12 = 84-day quarters). |
| **Triptyque (T1/T2/T3)** | Découpage organisationnel en trois niveaux : T1 = operational core (people + ops + product) ; T2 = value-extraction (growth + sales + finance) ; T3 = governance + R&D (legal + rd). Chaque triptyque contient un Rock B1-1/B1-2/B1-3 et trois captains B2. | `ownerbooks\ownerbook_T1_people_ops_product.md:15` (mission T1) ; `ownerbook_T2_growth_sales_finance.md:15` (mission T2) ; `ownerbook_T3_legal_rd.md:15` (mission T3). |
| **graphify-out** | Cache de build (hastags + ast_hash + semantic_hash par fichier). Ce n'est pas du contenu source — c'est une trace d'indexation pour les wargames. | `graphify-out\.graphify_semantic_marker` (fichier marqueur) + `graphify-out\manifest.json` (clefs=valeurs chemins→hashes). |

**Vocabulaire transverse important** :

- **B1 = Summers** (vision, source de l'autorité) — référencé comme « B1 Summers » dans les ownerbooks et chartes.
- **A0 = l'humain (Amadeus)** ; la doctrine « A0 = IA » signifie *A0 doit être traité comme une Intelligence Artificielle* (automatisation d'abord, gates manuels exceptionnels). `chart_T1_product_spec_loop.md:38` (« A0 = IA, no manual UI gate »).
- **D4 append-only / D6 no-self-contradiction / D6 no-copy** : règles de doctrine omniprésentes dans les frontmatters. D4 = pas d'écrasement ; D6 = pas de contradiction dans le canon.
- **HITL** : Human-In-The-Loop gate — bloquant silencieux si skip (ex. `runbook-C-saas-auth.md:36` Condition B sur le JWT hook Cloud).
- **JTBD** : Job To Be Done — paquet de travail atomique donné par B2 à un agent B3, avec input/output/proof attendus (`B2_Business_Domains\04_Ops_Batman_Fantastic4\01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md:32`).
- **Spec-Loop Polivaev 2026** : discipline de planification locked-BEFORE-execution avec grill-me adversarial. Pattern récent, référencé partout dans les chartes_cycle_2 mais pas dans le `chartes/` racine.
- **AAAS** = Agency as a Service. Doctrine cardinale du produit : « 53 B3 agents ARE the product » (ownerbook T1 §2).
- **DoD Una 3-critères** : format de Definition of Done à exactement trois critères, vérifiables par grep/ls. Présent dans chaque charte_cycle_2.

**Deux strates temporelles coexistent** dans ce dépôt :

1. **Strate « omk-nexus-coaching-premium »** (mai 2026) : les fichiers `B2_Business_Domains/04-08/`, `B3_Warp_Core_Execution/01-08/`, et probablement l'état initial du `chartes/` — datés 2026-05-25 à 2026-05-27, status `SHADOW_ACTIVE`, frame encore en EUR et RGPD-first.
2. **Strate « SaaS-OS pivot US »** (juillet 2026) : `chartes/phase_c_*.md` + `chartes/phase_d_*.md` (15 juillet), `chartes_cycle_2/*` (juillet), `ownerbooks/*` (juillet), `runbooks/*` (15 juillet), avec icp = « US market — Coach premium + Enterprise mid-market », pricing USD strict, single-mode `'saas'` LOCKED 2026-06-19.

Le pivot est explicitement daté dans `ownerbook_T2_growth_sales_finance.md:18` (« US market pivot per A0 2026-07-15 »).

---

## 2. Les domaines métier

`B2_Business_Domains` déclare **cinq** domaines en propre dans ce dépôt — `03_Product_Flash_Avengers/` n'a aucun fichier hors jonction (cf. §5).

| # | Dossier | Domaine | B2 captain | B3 squad | Périmètre (core domain surface) | Source |
|---|---|---|---|---|---|---|
| 04 | `04_Ops_Batman_Fantastic4` | Ops | Batman | Fantastic Four (4 agents + 4 dossiers) | repeatable delivery, SOP, build gate, support path, operational reliability | `B2_Business_Domains\04_Ops_Batman_Fantastic4\00_B2_DOMAIN_CONTROL_ROOM.md:39` ; `01_B3_AGENT_ROSTER.md:39` |
| 05 | `05_IT_Cyborg_KangDynasty` | IT | Cyborg | Kang Dynasty (6 agents : Infra / Provisioning / Security / Capacity / CI-CD / Backup) | runtime, access, deployment, backup, technical boundaries | `B2_Business_Domains\05_IT_Cyborg_KangDynasty\00_B2_DOMAIN_CONTROL_ROOM.md:39` |
| 06 | `06_Finance_WonderWoman_Thunderbolts` | Finance | Wonder Woman | Thunderbolts (6 agents : Cashflow / Forecasting / Reporting / CostOpt / Repro / Compliance) | cost, price, margin, billing, model-usage & service-cost burn control | `B2_Business_Domains\06_Finance_WonderWoman_Thunderbolts\00_B2_DOMAIN_CONTROL_ROOM.md:39` |
| 07 | `07_People_GreenLantern_XMen` | People | Green Lantern | X-Men (8 agents) | ownership, training, load, delegation, continuity | `B2_Business_Domains\07_People_GreenLantern_XMen\00_B2_DOMAIN_CONTROL_ROOM.md:39` |
| 08 | `08_Legal_Aquaman_Eternals` | Legal | Aquaman | Eternals (10 agents) | claims, privacy, IP, terms, compliance boundaries | `B2_Business_Domains\08_Legal_Aquaman_Eternals\00_B2_DOMAIN_CONTROL_ROOM.md:39` |

**Domaines attendus mais absents** : `01_Growth_Superman_Guardians` et `02_Sales_MartianManhunter_Illuminati`. Ils sont référencés par leur path dans `ownerbook_T2_growth_sales_finance.md:23-25` (et `runbook-C-saas-auth.md:16` cite même « omk-nexus-coaching-premium/_doctrine/ » comme projet voisin), mais aucun fichier ne leur correspond dans ce dépôt. Les swarms B3 de ces deux domaines existent, eux (`B3_Warp_Core_Execution/01_Growth_Superman_Guardians/`, `…/02_Sales_MartianManhunter_Illuminati/`), mais leurs control rooms B2 ont été omis de l'extrait — soit perdus, soit jamais écrits pour ce miroir.

**Relations entre domaines** :

- Tous les B2 partagent le même gabarit de control room — seul change (a) le nom de domaine, (b) le B2 captain, (c) le B3 squad et ses agents, (d) la core domain surface listée dans `00_B2_DOMAIN_CONTROL_ROOM.md`.
- Le cross-domain passe par **handoffs B2↔B2** (la runbook-D appelle ça « meso swarm », `runbook-D-repositories.md:69`) et par **swarm overlaps** (ex. `chart_T1_people_b2b_saas_playbook.md:33` : « B3 Professor X … X-Men overlap with B3 Charles Xavier (Illuminati Sales) »).
- Les trois triptyques dessinent une chaîne de dépendance : T1 construit l'offre, T2 la vend, T3 la gouverne (`ownerbook_T1_people_ops_product.md:17` : « every other triptyque (T2 sells, T3 governs) consumes T1 output »).
- Le triptyque T3 a absorbé IT (Cyborg IT → R&D, `ownerbook_T3_legal_rd.md:15` « IT absorbed to L0 Rick »). C'est une décision doctrinale récente (W40 §M2 patch) qui **n'est pas reflétée dans `B2_Business_Domains/05_IT_Cyborg_KangDynasty/`** — le control room IT existe encore comme un domaine à part entière.

**Ce qui les relie** : le format de supervision lui-même. Les 5 control rooms sont des instances d'un même template, pas des créations indépendantes. C'est ce qui rend l'ensemble duplicable vers d'autres périmètres (Solaris, Orbiter) — voir §3.

---

## 3. Coach ou générique ? — la question centrale

Cette section est sévère. Je classe chaque artefact structurant selon qu'il porte du métier-de-coach, du positionnement-de-marché, ou du générique.

### 3.1 Verdict global

**Quasi tout est générique.** Le mot « coach » apparaît 50+ fois dans le corpus mais **toujours comme segment d'ICP** (« Coach premium B2B $7.5-25K ACV ») ou comme référence de persona acheteur. Le mot « coaching » (substantif) apparaît 2 fois — uniquement dans les runbooks C/D, et encore, dans des contextes neutres (« coaching-premium » comme ancien nom de projet, voir §5). Le mot « session » apparaît 17 fois — et **les 12 occurrences contextuelles** (runbook-C + Spec-Loop chart) réfèrent à *Spec-Loop sessions* ou *Spec-Loop session templates*, pas à des séances de coaching.

L'offre est donc : un Business OS B2B générique, positionné sur le segment « coach premium ». Rien dans l'architecture, la donnée, ou les processus ne présuppose le métier de coach.

### 3.2 Tableau — un artefact par ligne

| Artefact structurant | Fichier | Propre coaching | Générique | Ce qu'il faudrait pour généraliser |
|---|---|---|---|---|
| **B1/B2/B3 layered orchestration** | `B3_Warp_Core_Execution\README.md:13` | non | oui | rien — déjà général |
| **Lead/Lag / artifact-proof / blocker protocol** | `B3_Warp_Core_Execution\README.md:74` | non | oui | rien |
| **Charte (format W40 M3)** | `chartes\phase_c_saas_auth.md` | non | oui | rien |
| **Runbook (M1-M5 HITL-gated)** | `runbooks\runbook-C-saas-auth.md:14` | non | oui | rien |
| **Ownerbook (closing doc per Rock)** | `ownerbooks\ownerbook_T1_people_ops_product.md` | non | oui | rien |
| **Triptyque T1/T2/T3** | `ownerbook_T1_*.md:15` + T2 + T3 | non | oui | rien |
| **AAAS = Agency as a Service doctrine** | `ownerbook_T1_people_ops_product.md:17` | non | oui | déjà un méta-positionnement B2B |
| **Swarms B3 (53 agents)** | `B3_Warp_Core_Execution\01-08\` | non | oui | les noms sont des super-héros (F4 / GotG / Avengers / Illuminati / Thunderbolts / X-Men / Eternals / Kang Dynasty), aucun nom de coach |
| **Data model canon (5 entités)** | `runbook-D-repositories.md:21` : `clients / documents / agents / invoices / sops` | non | oui | déjà des entités B2B génériques ; pas de `program`, `session_note`, `coaching_package`, `intake_form`, `client_journey` |
| **B2 control room templates (×5)** | `B2_Business_Domains\04-08\` | non | oui | rien |
| **ADR-ICP-NEXUS-001 (5 piliers)** | cité `chartes\phase_c_saas_auth.md:24` (« ADR-ICP-NEXUS-001 Pilier 5 » — Zero-PII Auth) | non | oui | déjà général (Pilier 5 = conformité, pas coaching) |
| **ADR-AAAS-PRICING-001 (5 tiers USD)** | cité `ownerbook_T2_growth_sales_finance.md:22` (« PME Solo Founder $300-500/an → Orbiter $50K MRR ») | non | oui | rien — la palette de prix couvre PME solo à Enterprise |
| **ADR-NEXUS-NICHE-001 (Coach premium RATIFIED)** | cité `ownerbook_T1_people_ops_product.md:80` (« Coach premium (per ADR-NEXUS-NICHE-001 RATIFIED) ») | **oui (positionnement)** | non | Remplacer « Coach premium » par « {niche} premium » dans tous les artefacts |
| **« 60% mid-market + 25% Coach premium + 15% Fortune 500 »** | `chart_T2_growth_aaarr_funnel.md:24` ; `chart_T2_sales_100m_offers.md:13` (Boris Cherny deepscan, Devin Karns $100M archetype) | **oui (positionnement)** | non | Re-parameter l'ICP et la référence concurrentielle |
| **B3 Ops roster — Canonical Task Surface** | `B3_Warp_Core_Execution\04_Ops_Batman_Fantastic4\01_B3_AGENT_ROSTER.md:33` (« Onboarding client : VPS Nexus, Dokploy, DNS, email welcome ») | non | oui | « Onboarding client » désigne l'onboarding du client de l'agence (le coach), pas l'onboarding d'un coaché |
| **B3 Sales roster — Demo Solaris/Nexus/Orbiter** | `B3_Warp_Core_Execution\02_Sales_MartianManhunter_Illuminati\01_B3_AGENT_ROSTER.md:37` | non | oui | le mot « coach » est absent — la démo est par tier produit |
| **B3 Legal roster — licence Whitelabel Orbiter** | `B3_Warp_Core_Execution\08_Legal_Aquaman_Eternals\01_B3_AGENT_ROSTER.md:42` | non | oui | modèle franchise générique |
| **Pilier 5 Zero-PII Auth (ADR-ICP-NEXUS-001)** | `chartes\phase_c_saas_auth.md:24` | non | oui | conformité générique (GDPR Art. 15 / AI-Act §données-entraînement) |
| **Schema SQL `omk_saas`** | `runbook-D-repositories.md:21` (référencé aussi dans la jonction via `graphify-out\manifest.json` qui liste `sql/02_omk_saas_schema.sql`) | non | oui | aucune table ne porte de sémantique coaching |
| **3 produits Solaris / Nexus / Orbiter** | §4 ci-dessous | non (ce sont 3 tiers du même produit) | oui | rien — déjà générique |
| **Chartes « Coach premium » positioning** | `chart_T1_people_onboarding.md` (8 mentions) ; `chart_T2_growth_aaarr_funnel.md` (8 mentions) ; `chart_T2_sales_100m_offers.md` (4) ; `chart_T1_product_roadmap.md` (6) | **oui (positionnement)** | non | Tous les grep-tests `grep "Coach premium"` à réécrire |
| **TCPA / CAN-SPAM gates** | `chart_T2_growth_aaarr_funnel.md:30-31` | non | oui | juridique US générique |
| **Spec-Loop Polivaev 2026 + A0 = IA** | `chart_T1_product_spec_loop.md:14` | non | oui | déjà général |
| **DoD Una 3-critères** | toutes les chartes_cycle_2, §8 | non | oui | format générique |
| **Charte Phase C SaaS Auth** | `chartes\phase_c_saas_auth.md` | non | oui | code générique (Supabase Auth + JWT hook) |
| **Charte Phase D Repositories** | `chartes\phase_d_repositories_branches.md` | non | oui | code générique (5 repos + 7 views) |

### 3.3 Le seul vrai spécifique-coach est l'ICP

Si l'on cherche ce qui *contraint* la réutilisation vers une autre niche (Solaris, Orbiter, ou tout autre verticale), on ne trouve **que le segment ICP** :

- L'ADR **NEXUS-NICHE-001** (RATIFIED, mais **non présent dans ce dépôt** — seulement référencé par ownerbooks et chartes_cycle_2) est l'unique artefact qui pose le Coach premium comme choix stratégique.
- Les chartes T1/T2/T3 qui parlent de « Coach premium $7.5-25K ACV » sont dérivées de cet ADR.
- La référence concurrentielle **Boris Cherny deepscan / Devin Karns $100M AI Agency archetype** (citée `ownerbook_T2_growth_sales_finance.md:18`) est aussi niche-spécifique.

**Tout le reste est duplicable** sans renommage : noms de squad, schémas SQL, cycle 12WY, ownerbook format, chart format, doctrine D4/D6, Spec-Loop, AAAS, AAARR funnel, Hormozi 100M Offers, 1-Person/1-Billion unit economics — *rien* de tout cela ne touche au métier de coach.

### 3.4 Pièges à éviter en dupliquant

- **L'ADR NEXUS-NICHE-001 n'est pas copié** dans ce dépôt. Une duplciation vers Solaris ou Orbiter doit *refuser* le copiage et *produire* un nouveau NEXUS-NICHE-00X. Sinon on duplique aussi l'ICP coach — c'est exactement ce qu'interdit D6 no-copy.
- **`ADR-ICP-NEXUS-001` reste valide** (Pilier 5 Zero-PII Auth etc.) — c'est un ADR de *compliance*, pas de niche. Les piliers conformité dupliquent sans friction.
- **Le B3 roster Sales** mentionne « Solaris/Nexus/Orbiter » comme tiers — dupliquer Solaris vers un Solaris-bis impose de renommer la palette de tiers dans les 8 rosters.

---

## 4. Nexus, Solaris, Orbiter

**Les trois noms apparaissent dans le corpus. Ce ne sont pas trois produits, mais trois tiers d'un même produit.**

### 4.1 Preuves

- `B3_Warp_Core_Execution\03_Product_Flash_Avengers\01_B3_AGENT_ROSTER.md:21` : « Specs produit, roadmap **Solaris/Nexus/Orbiter** et QA ».
- `B3_Warp_Core_Execution\03_Product_Flash_Avengers\01_B3_AGENT_ROSTER.md:38` : « Release frequency >= 1 ship / 2 semaines **Solaris** » ; `B3_AGENT_ROSTER.md:46` : « NPS **Solaris** >= 40 par cohorte trimestrielle ».
- `B3_Warp_Core_Execution\02_Sales_MartianManhunter_Illuminati\01_B3_AGENT_ROSTER.md:37` : « Demo personnalisee **Solaris/Nexus/Orbiter** ».
- `B3_Warp_Core_Execution\02_Sales_MartianManhunter_Illuminati\01_B3_AGENT_ROSTER.md:45` : « Average deal size >= **5k EUR Solaris/Nexus** ou **50k EUR Orbiter franchise** ».
- `B3_Warp_Core_Execution\06_Finance_WonderWoman_Thunderbolts\01_B3_AGENT_ROSTER.md:35` : « Stripe encaissement SaaS **Solaris/Nexus/Orbiter** ».
- `B3_Warp_Core_Execution\06_Finance_WonderWoman_Thunderbolts\01_B3_AGENT_ROSTER.md:45` : « Net Margin **Solaris** > 40% ».
- `B3_Warp_Core_Execution\08_Legal_Aquaman_Eternals\01_B3_AGENT_ROSTER.md:21` : « licence Whitelabel **Orbiter** ».
- `B3_Warp_Core_Execution\08_Legal_Aquaman_Eternals\01_B3_AGENT_ROSTER.md:42` : « IP filing A Space/**Solaris/Nexus/Orbiter** ».
- `chartes_cycle_2\chart_T2_finance_unit_economics.md:14` : « 5 USD pricing tiers (PME Solo Founder T1 $300-500/an → **Orbiter** T5 $50K MRR → $500K Year 10) ».
- `ownerbooks\ownerbook_T2_growth_sales_finance.md:22` : « 5-tier canon `ADR-AAAS-PRICING-001` (T1 PME Solo Founder $300-500/an → T5 **Orbiter** Enterprise $50K MRR → $500K Year 10) ».

### 4.2 Hiérarchie probable (lecture par contexte)

- **Solaris** = entrée de gamme, périmètre resserré (release bi-mensuelle, marge cible 40%, NPS cible 40). Probable : T1-T2 de `ADR-AAAS-PRICING-001` (PME Solo).
- **Nexus** = tier du milieu, le **nom de produit** par défaut dans la doctrine (cf. `icp: Nexus (Data-First / Conformité)` dans `chartes\phase_c_saas_auth.md:6`, `ADR-ICP-NEXUS-001` Pilier 5, `ADR-NEXUS-NICHE-001`). « Nexus » est *à la fois* le nom de tier et le nom de la ligne-produit dans le canon le plus récent.
- **Orbiter** = haut de gamme (50K MRR, Whitelabel licence, modèle franchise, Fortune 500 ready, SOX §404 applicable). Probable : T5 de `ADR-AAAS-PRICING-001`.

`ADR-AAAS-PRICING-001` (référencé mais absent du dépôt) tranche la nomenclature exacte ; le dépôt n'en contient que les références.

### 4.3 Confusion à dissiper

Le brief demande si « Nexus, Solaris, Orbiter » sont trois produits séparés et quelle est leur relation. La réponse du canon est : **trois niveaux tarifaires d'un seul produit**, dans cet ordre d'entrée-de-gamme → premium :

- Solaris ≤ Nexus ≪ Orbiter
- Le « Business OS » est la **famille produit** ; Solaris/Nexus/Orbiter sont les **SKUs**.
- L'AAAS doctrine (« 53 B3 agents ARE the product ») couvre les trois ; l'offre ne change pas de nature entre les tiers, seulement de surface et de SLA.

---

## 5. Ce qui est mort

| Artefact | Signe de péremption | Source du constat |
|---|---|---|
| **Strate EUR / RGPD-first** des B2 control rooms et B3 rosters | Datés 2026-05-25 à 2026-05-27, citent « 5k EUR Solaris/Nexus » et « 50k EUR Orbiter franchise » (`B3_Warp_Core_Execution\02_Sales_MartianManhunter_Illuminati\01_B3_AGENT_ROSTER.md:45`) alors que les chartes_cycle_2 du 2026-07-15 imposent « USD strict, no EUR drift » et que `chart_T2_finance_unit_economics.md:52` exige littéralement `grep -F "EUR\|€\|SEPA" = 0`. Aucun chemin de migration EUR→USD n'est documenté dans ces fichiers B2/B3 de mai. | `chart_T2_finance_unit_economics.md:52` (DoD-3) ; `chart_T1_people_onboarding.md:49` (DoD-2) ; `chart_T2_sales_100m_offers.md:51` (DoD-2). |
| **Naming « MartianManhunter »** | Le B3 Sales swarm config et roster portent `b2_gatekeeper: Martian Manhunter / John Jones` (`B3_Warp_Core_Execution\02_Sales_MartianManhunter_Illuminati\00_B3_SWARM_CONFIG.md:7` ; `01_B3_AGENT_ROSTER.md:19`). Le T2 ownerbook dit explicitement « legacy naming MartianManhunter, W40 V4 rename JohnJones » — donc la doctrine courante est JohnJones. | `ownerbooks\ownerbook_T2_growth_sales_finance.md:24` (« legacy naming MartianManhunter, W40 V4 rename JohnJones »). |
| **B2 control rooms `01_Growth` et `02_Sales`** | Référencés par leur path exact dans `ownerbook_T2_growth_sales_finance.md:23-25` mais aucun fichier correspondant dans ce dépôt. Soit perdus, soit jamais écrits pour ce miroir. Le B3 swarm existe pour les deux, le B2 control room manque. | `ownerbook_T2_growth_sales_finance.md:23-25`. |
| **B2 control room `03_Product_Flash_Avengers`** | Le dossier existe mais ne contient rien hors la jonction vers le code repo. Aucun `00_B2_DOMAIN_CONTROL_ROOM.md`, aucun `01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md`, etc. alors que les autres 5 domaines (04-08) en sont tous équipés. | `ls B2_Business_Domains\03_Product_Flash_Avengers\` (retourne uniquement `02-omk-services-business-os` = jonction). |
| **Ancien nom de projet `omk-nexus-coaching-premium`** | Citée comme référence externe dans `runbook-C-saas-auth.md:16` (« Sister canon : aucun runbook sister dans `omk-nexus-coaching-premium/_doctrine/` »), mais le projet a pivoté vers `omk-services/00-omk-saas-os` (cf. `runbook-D-repositories.md` qui pointe vers ce nouveau path). | `runbook-C-saas-auth.md:16` ; `runbook-D-repositories.md:208` (« Sister MANIFEST : omk-nexus-coaching-premium/MANIFEST.md »). |
| **Custom hooks PG `aspace_admin` / `aspace_observer` self-host** | `ADR-OMK-002` est RATIFIED 2026-06-11 self-host, mais les chartes Phase C/D constatent : « **non re-provisionnés sur Cloud post-pivot** (D6 #orphelin) ». Mort à court terme, dormant à long terme. | `chartes\phase_c_saas_auth.md:50` (Gap-2). |
| **ADR-OMK-003 (MCP `supabase-aspace`)** | Rédigé « post-quota 429 », jamais terminé ; Phase C utilise le fallback `mcp__supabase-omk__*`. | `chartes\phase_c_saas_auth.md:49` (Gap-1). |
| **`@google/genai` installé mais unused** | CLAUDE.md gotcha #9 repris en Gap-3 par la Phase C charter. | `chartes\phase_c_saas_auth.md:51` (Gap-3). |
| **Custom domain `omk.kalybana.com`** | « non encore migré DNS vers CNAME Vercel (REBUILD_WORKFLOW §5 bloquant dormant) ». | `chartes\phase_c_saas_auth.md:52` (Gap-4). |
| **ADR-CRUD-VIEWS** | Référencé comme canon dans la charte Phase D, mais le runbook D constate « n'existe PAS en canon (`_SPECS/ADR/` absent confirmé 2026-07-15) ». | `runbook-D-repositories.md:148` (Gap-2). |
| **Graphify-out (cache de build)** | 165 fichiers JSON hash-nommés — ce n'est pas du contenu source. La trace existe ; la substantifique moelle du graphe ne se lit pas dans le dépôt. | `graphify-out\manifest.json` (clefs=valeurs chemins→hashes, aucune sémantique). |
| **Strate « multi-mode » (`'saas'` LOCKED 2026-06-19)** | Tout le canon Phase C/D suppose le single-mode `'saas'`. Une éventuelle strate antérieure `dev`/`self-host`/`on-prem` n'est pas documentée dans ce dépôt. | `chartes\phase_c_saas_auth.md:16` (« Single-mode 'saas' only (A1 LOCKED 2026-06-19) »). |
| **Chart `phase_d_repositories_branches.md` vs `apps/dashboard/AGENTS.md`** | Le runbook D ouvre sur une contradiction canon assumée : la chart Phase D dit RP3 = ❌ NOT STARTED, `apps/dashboard/AGENTS.md:28` dit Phase D = ✅ DONE 2026-06-20 (11/14 views wired). Le runbook tranche pour `AGENTS.md` (récent + receipts) et dénonce la chart comme stale. | `runbook-D-repositories.md:16`. |

**Thèse FDE / graphe de contexte — note de confrontation**

La couche manquante identifiée dans le travail amont est un *graphe de contexte versionné*. Ce dépôt en est **un embryon**, mais un embryon spécifique : `graphify-out/manifest.json` est bien un graphe (chemins → ast_hash + semantic_hash), mais c'est un graphe *de présence*, pas un graphe *de sens*. Il ne porte aucune notion d'entité, relation, ou règle du domaine. Le brief suggère que ce graphe devrait encoder clients/agents/sessions/règles du client du FDE — le dépôt actuel n'encode que l'arborescence de fichiers. C'est une ouverture, pas une fermeture.

---

## 6. Compte exact

### 6.1 Fichiers lus en entier (33)

1. `B3_Warp_Core_Execution\README.md`
2. `chartes\phase_c_saas_auth.md`
3. `chartes\phase_d_repositories_branches.md`
4. `ownerbooks\ownerbook_T1_people_ops_product.md`
5. `chartes_cycle_2\chart_T1_ops_sop_canon.md`
6. `ownerbooks\ownerbook_T2_growth_sales_finance.md`
7. `ownerbooks\ownerbook_T3_legal_rd.md`
8. `B2_Business_Domains\04_Ops_Batman_Fantastic4\README.md`
9. `B2_Business_Domains\04_Ops_Batman_Fantastic4\00_B2_DOMAIN_CONTROL_ROOM.md`
10. `B2_Business_Domains\04_Ops_Batman_Fantastic4\01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md`
11. `B2_Business_Domains\04_Ops_Batman_Fantastic4\02_B3_SWARM_SUPERVISION_PROTOCOL.md`
12. `B2_Business_Domains\05_IT_Cyborg_KangDynasty\00_B2_DOMAIN_CONTROL_ROOM.md`
13. `B2_Business_Domains\06_Finance_WonderWoman_Thunderbolts\00_B2_DOMAIN_CONTROL_ROOM.md`
14. `B2_Business_Domains\07_People_GreenLantern_XMen\00_B2_DOMAIN_CONTROL_ROOM.md`
15. `B2_Business_Domains\08_Legal_Aquaman_Eternals\00_B2_DOMAIN_CONTROL_ROOM.md`
16. `B3_Warp_Core_Execution\04_Ops_Batman_Fantastic4\00_B3_SWARM_CONFIG.md`
17. `B3_Warp_Core_Execution\04_Ops_Batman_Fantastic4\01_B3_AGENT_ROSTER.md`
18. `B3_Warp_Core_Execution\01_Growth_Superman_Guardians\00_B3_SWARM_CONFIG.md`
19. `B3_Warp_Core_Execution\02_Sales_MartianManhunter_Illuminati\00_B3_SWARM_CONFIG.md`
20. `B3_Warp_Core_Execution\03_Product_Flash_Avengers\01_B3_AGENT_ROSTER.md`
21. `B3_Warp_Core_Execution\02_Sales_MartianManhunter_Illuminati\01_B3_AGENT_ROSTER.md`
22. `runbooks\runbook-C-saas-auth.md`
23. `runbooks\runbook-D-repositories.md`
24. `chartes_cycle_2\chart_T1_product_roadmap.md`
25. `chartes_cycle_2\chart_T2_sales_100m_offers.md`
26. `chartes_cycle_2\chart_T1_people_onboarding.md`
27. `chartes_cycle_2\chart_T1_people_b2b_saas_playbook.md`
28. `chartes_cycle_2\chart_T2_finance_unit_economics.md`
29. `chartes_cycle_2\chart_T1_product_spec_loop.md`
30. `chartes_cycle_2\chart_T2_growth_aaarr_funnel.md`
31. `B3_Warp_Core_Execution\06_Finance_WonderWoman_Thunderbolts\01_B3_AGENT_ROSTER.md`
32. `B3_Warp_Core_Execution\08_Legal_Aquaman_Eternals\01_B3_AGENT_ROSTER.md`
33. `graphify-out\manifest.json` (JSON, pas .md, mais intégralement parcouru)

### 6.2 Dossiers ouverts sans y entrer

- `B2_Business_Domains\01_Growth_Superman_Guardians\` — n'existe pas dans ce dépôt.
- `B2_Business_Domains\02_Sales_MartianManhunter_Illuminati\` — n'existe pas dans ce dépôt.
- `B2_Business_Domains\03_Product_Flash_Avengers\02-omk-services-business-os\` — **jonction** vers le dépôt de code. **Non entré**, conformément à la consigne.
- `B3_Warp_Core_Execution\01-08\…\<dossiers d'agents>` — listés (53 sous-dossiers au total) mais non lus. Les noms d'agents seuls suffisent à la cartographie ; aucun fichier de ces sous-dossiers n'a été ouvert (lecture de leur README pour un échantillonnage ferait sens dans un brief ultérieur).
- `chartes_cycle_2\chart_T1_ops_perf_metrics.md`, `…runbook_v1.md`, `…sop_canon.md` — lus T1 SOP canon ; les deux autres non lus (couverture T1 Ops complète suffisante pour la question).
- `chartes_cycle_2\chart_T1_people_hr_ops.md` — non lu (couverture T1 People suffisante via `…onboarding.md` + `…b2b_saas_playbook.md`).
- `chartes_cycle_2\chart_T1_product_prd_template.md` — non lu (PRD template non central pour la question coach/générique).
- `chartes_cycle_2\chart_T2_finance_billing_stripe.md`, `…runway_runbook.md`, `…unit_economics.md` — lus ce dernier ; les deux autres Stripe/runway sont des facettes du même ADR-AAAS-PRICING-001 et n'ajoutent pas à la réponse.
- `chartes_cycle_2\chart_T2_growth_linkedin_abm.md`, `…producthunt_playbook.md`, `…sales_fortune500_msa.md`, `…sales_stripe_us_ach.md` — non lus (sous-canal du même triptyque T2, déjà couvert par `…aaarr_funnel.md` + `…100m_offers.md`).
- `chartes_cycle_2\chart_T3_legal_*.md` (3 fichiers : ai_act_eu_secondary, sec_ftc_compliance lu, us_ai_bill_of_rights) — lus ce dernier-tier (SEC/FTC), les deux autres non ; suffisant pour la question Solaris/Orbiter et la thèse Euro-vs-US.
- `chartes_cycle_2\chart_T3_rd_*.md` (3 fichiers : boris_cherny_archetypes, innovation_filter, youtube_last30days) — non lus (R&D externe, pas central pour les questions 1-5 du brief).
- `B3_Warp_Core_Execution\03_Product_Flash_Avengers\00_B3_SWARM_CONFIG.md`, `…\02_PEER_UNBLOCKING_AND_HANDOFFS.md`, `…\03_SHARED_CONTEXT_AND_PROOF_LOG.md` et leur symétrique dans les 7 autres swarms — non lus. Le `00_B3_SWARM_CONFIG.md` lu pour Ops/Growth/Sales suffit à établir le pattern template ; les fichiers 02/03 sont uniformes (à vérifier sur échantillon si une descente est nécessaire).
- `B3_Warp_Core_Execution\01-08\01_<agent>_*\README.md` (53 fichiers) — non lus.
- `graphify-out\graph.json`, `graphify-out\.graphify_analysis.json`, `graphify-out\.graphify_semantic_marker`, `graphify-out\cache\*` — non lus (cache de build, manifest.json suffit).

### 6.3 Budget

| Cible | Atteint |
|---|---|
| ≈100 fichiers lus en entier | 33 — bien en-deçà. Le corpus est petit et bien curé ; 33 fichiers suffisent à répondre aux 5 questions du brief. |
| Jonctions respectées (0 entrée) | OK — 1 jonction détectée, 0 entrée. |
| Pas de `node_modules` / `.git` / `.next` / `dist` / `build` / `__pycache__` / `.venv` | OK. |

---

## 7. Reste à couvrir (si un second brief prolonge celui-ci)

- Vérifier que les 5 dossiers d'agents `…\02_PEER_UNBLOCKING_AND_HANDOFFS.md` et `…\03_SHARED_CONTEXT_AND_PROOF_LOG.md` (8 swarms × 2 = 16 fichiers) sont bien des gabarits uniformes et n'apportent pas de spécifique-coach.
- Lire le `chart_T3_rd_boris_cherny_archetypes.md` pour valider la nature exacte de la référence concurrentielle (Devin Karns $100M archetype).
- Confirmer via un autre extrait du dépôt que `ADR-NEXUS-NICHE-001` et `ADR-AAAS-PRICING-001` portent bien les cinq tiers canon (actuellement non copiés dans ce miroir — seulement référencés).
- Si Solaris et Orbiter doivent être instanciés comme produits séparés, lire un échantillon de `B3_Warp_Core_Execution\01-08\01_<agent>_*\README.md` (au moins 8-10) pour s'assurer qu'aucun ne porte de sémantique métier-spécifique.

---

*Rapport N1 écrit 2026-08-05 par exploration en lecture seule. Aucune modification n'a été apportée au dépôt hormis la création de ce fichier `analyses/N1_canon.md`. Jonction NTFS `B2_Business_Domains\03_Product_Flash_Avengers\02-omk-services-business-os` non entrée.*