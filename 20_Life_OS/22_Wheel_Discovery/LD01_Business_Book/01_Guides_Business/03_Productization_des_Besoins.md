---
okf_version: "0.1"
type: guide-distillation
title: "03 · Productization des Besoins"
description: "Distillation du corpus Product Geordi : Supply Chain Awareness (compute ownership), Skill vs MCP, Anti-AI Slop, Functional vs Marketing UI, 3 chaînes canoniques, dépendance Anthropic/Vercel/Supabase."
timestamp: 2026-08-02T16:40:00-04:00
domain: LD01_Career_Business
agent: A3_Book
squad: Avengers (B3-3 Captain America lead, Iron Man, Thor, Hulk, Black Widow, Hawkeye, Scarlet Witch)
vp: Flash
sources_count: 907
note_doublon: "`01_Product/` + `01_Product_Product/` = doublonnage structurel hérité d'une reclassification antérieure. À signaler, pas à fusionner (corpus en lecture seule)."
note_pollution: "Le canon réel tient sur ~10 fichiers ; les 900 autres sont du noise détecté par mots-clés `product|feature|ux|design|niche|icp|pmf`."
---

# 03 · Productization des Besoins

Le domaine 3 porte la **productisation des besoins utilisateurs** en assets déployables :
transformer un insight en skill, un skill en composant, un composant en produit. Le canon
est étonnamment petit (~10 fichiers) mais stratégique : il porte la doctrine **Supply
Chain Awareness** (qui possède le compute que tu consommes) et la séparation
**Skill/MCP**. Propriétaire canonique : **B2 Flash** (LD04 Cognition Tilly ↔ LD01
Business ↔ LD01 Picard), squad **Avengers** avec **Captain America** en lead.

⚠️ **Doublonnage structurel** : `01_Product/` (7 fichiers canon) + `01_Product_Product/`
(900 fichiers Geordi_YT, 3 chaînes canoniques). Héritage d'une reclassification antérieure
— à signaler, pas à fusionner (corpus source en lecture seule, cf. brief §5).

## 1. Ce que le corpus dit

### Thèse 1 — Supply Chain Awareness : auditer le compute ownership de chaque dépendance critique

SpaceX entre en bourse +75 Md$, rachète Cursor 60 Md$ 4 jours après, paie en actions (cash
intact). Mécanique : **convertir valorisation papier en revenu réel via narratif IA**.
Cursor entraînait ses modèles sur **Colossus** (1M GPUs Memphis, absorbé via xAI fév
2025). SpaceX possède déjà calcul + modèle (Grok) + distribution (X, Starlink) — il
manquait juste le canal utilisateur pro. **Leçon** : la chaîne de valeur AI se consolide
au niveau **compute**, pas modèle. Risque régulatoire : contrat 4 Md $ indemnité si
opération bloquée anti-trust ; Anthropic loue 25 Md $/an de Colossus (contrats résiliables
3 mois) — Musk contrôle le compute de ses concurrents code.
Sources : `01_Product/2026-06-18_musk-rachete-cursor-compute-ownership-supply-chain.md`
(Le SamourAI, 25:39, 2026-06-18).

### Thèse 2 — 4 dépendances critiques A'Space à auditer : Anthropic + Vercel + Supabase + Stripe

Pour chaque dépendance critique, **2 questions vitales** : (1) Sur quel moteur de calcul
tourne mon outil ? (2) Le propriétaire est-il en concurrence directe avec mon écosystème ?
Si oui = vulnérabilité. Sister canon : **ADR-OMK-004** (Pivot Supabase Cloud + Vercel)
adresse partiellement la doctrine, mais reste dépendant d'Anthropic pour les modèles, qui
dépend du compute de Musk via contrats résiliables 3 mois. **Doctrine Anti-Paresse** : la
dépendance compute = D7 cost-of-escalation potentiel — anticiper maintenant.
Sources : `01_Product/2026-06-18_musk-rachete-cursor-compute-ownership-supply-chain.md`.

### Thèse 3 — Skill = rulebook chargé à la demande, MCP = live connection permanente

Dans l'écosystème Claude, un **skill** est un *rulebook* (fichier `skill.md` avec
instructions, patterns, règles de projet) que l'agent charge **à la demande**. Le **MCP**
(Model Context Protocol) est une *live connection* à un registre distant qui reste **dans
le context window en permanence**. Verbatim : *« The skill only loads when it's actually
needed instead of being in the context window all the time like MCP does. »* **Conséquence
opérationnelle** : la skill donne le **jugement**, le MCP donne les **composants**.
Sources : `01_Product/2026-06-25_design-skills-that-actually-work-Ot582-E61ac.md`
(AI Labs, 16 853 chars, 2026-06-25).

### Thèse 4 — Anti-AI Slop : commit to a real design direction before it writes anything

L'**AI slop** = ensemble des patterns safe que le modèle produit par défaut quand il n'a
aucune contrainte directionnelle : mêmes fonts, mêmes gradients violet-sur-blanc, mêmes
composants génériques. Lutter contre l'AI slop = forcer le modèle à **commit to a real
design direction before it writes anything**. Un B3 doit forcer un agent freelance à
respecter cette discipline (sister canon : `book_routing: skill` × `b3_captain`).
Sources : `01_Product/2026-06-25_design-skills-that-actually-work-Ot582-E61ac.md`.

### Thèse 5 — Functional UI vs Marketing UI : deux skills séparés, jamais l'un pour l'autre

Distinction explicite : (a) **Functional skill** = UI que les gens utilisent vraiment
(dashboards) ; (b) **Marketing UI skill** = landing pages, portfolios où le design est
partie du produit. Dans AI Labs Pro, la landing page artistique et la couche fonctionnelle
**cohabitent volontairement** : la landing a un design language artistique, le fonctionnel
reste *boring and plain just like any other web interface*. Cette dissociation est
canonique : **ne jamais appliquer un skill marketing à un dashboard**.
Sources : `01_Product/2026-06-25_design-skills-that-actually-work-Ot582-E61ac.md`.

### Thèse 6 — Discipline : 1 taste-preset pické, jamais stacké

Anti-AI-slop en pratique : choisir **un seul taste-preset** par projet, jamais stacker.
« Ne jamais appliquer un skill marketing à un dashboard » vaut aussi côté preset : un
preset marketing + un preset dashboard = drift vers le générique. Sister canon : `book_routing:
skill` × `b3_captain` (B1 FILTER GREEN LANTERN).
Sources : `01_Product/2026-06-25_design-skills-that-actually-work-Ot582-E61ac.md`.

### Thèse 7 — Dashboard vs landing : deux problèmes différents, deux skills différents

Pour une app classique : problème = *keeping components consistent*. Pour un dashboard :
problème = *how all the information is arranged on the screen, how to group the data and
how much can live on one screen before it gets too cluttered*. Le **Dashboard Skill**
dédié raisonne d'abord sur l'arrangement avant de produire — résultat *feels like a real
analytics tool instead of being cluttered*.
Sources : `01_Product/2026-06-25_design-skills-that-actually-work-Ot582-E61ac.md`.

### Thèse 8 — Shadcn : registry + skill + MCP = clean output first time

Shadcn = bibliothèque de composants **professional grade déjà construits**. Architecture
double : (a) **Shadcn skill** = règles + patterns + contexte projet, (b) **Shadcn MCP**
= live connection au registre qui browse et pull les composants réels. Bénéfice : *« clean
output the first time instead of having to go back and fix the same mistakes over and over. »*
Le modèle assemble au lieu de générer.
Sources : `01_Product/2026-06-25_design-skills-that-actually-work-Ot582-E61ac.md`.

### Thèse 9 — 3 chaînes canoniques : Leo Grindarss (30), Sachmoney (19), Romain Brunel Affiseo (88)

Audit `PRODUCT_CHANNELS_AUDIT.md` : **137 vidéos** classifiées sur 8 domaines B2 :
Product 71, Ops 40, Growth 17, Finance 6, IT 2, Legal 1. Distribution : **71 % Product**
+ **29 % Ops** = essentiellement de la productisation opérationnelle. Romain Brunel
(Affiseo, SEO/Affiliation) = 88 vidéos = chaîne la plus grosse du corpus Product.
Sources : `01_Product/PRODUCT_CHANNELS_AUDIT.md` (audit classification).

### Thèse 10 — Skill vs MCP en pratique : choix d'architecture selon le contexte

Trade-off canonique : **Skill** quand le rulebook est stable et le coût de rechargement est
acceptable (UI design, content voice) ; **MCP** quand le contexte doit rester live et
actualisé (data warehouse, CRM live, browser automation). Le corpus ne tranche pas
quantitativement mais l'orientation est claire : **par défaut skill, MCP seulement si
justifié**.
Sources : `01_Product/2026-06-25_design-skills-that-actually-work-Ot582-E61ac.md`.

## 2. Ce qui est actionnable maintenant

- [ ] Auditer ses **4 dépendances critiques** (modèle, hosting, DB, paiement) avec les 2 questions Supply Chain Awareness (compute ownership + concurrence propriétaire).
- [ ] Pour chaque skill A3, vérifier qu'elle est **load-on-demand** (skill.md) et non un MCP permanent. Refactor si besoin.
- [ ] Choisir **un seul taste-preset** par projet en cours. Documenter dans le frontmatter de la skill.
- [ ] Si landing page : utiliser **Marketing UI skill** + skill Shadcn ou Anthropic Front-end. Si dashboard : utiliser **Functional UI skill** + Dashboard skill dédié. Jamais croiser.
- [ ] Implémenter un **anti-AI slop checklist** dans la convention B3 freelance : *« commit to a real design direction before it writes anything »*.
- [ ] Lire **le `_INDEX.md` B2 sister** : `02_Ops/_INDEX.md` (Operations ↔ Product sister-symétrie).
- [ ] Veille mensuelle sur **SpaceX/xAI/Cursor/Colossus** pour anticiper les mouvements de consolidation.

## 3. Ce que le corpus contredit

- **Skill vs MCP** : Anthropic promeut les skills load-on-demand ; mais l'écosystème MCP continue de croître. Le corpus tranche pour les skills par défaut, MCP justifié — pas un consensus fort.
- **AI slop vs AI default** : Lutter contre l'AI slop = forcer un design direction. Mais certains auteurs défendent l'AI default comme « assez bon pour 80 % des cas ». Pas d'arbitrage.
- **Compute ownership vs Open source** : la doctrine Supply Chain Awareness prône l'audit, mais open-source-first ne garantit pas l'indépendance (un projet OSS peut dépendre d'un compute Musk-backed). Tension implicite.
- **Design direction vs Discovery produit** : anti-AI-slop impose un design direction ; mais discovery produit (cross-référence Sales 4) impose d'écouter le client avant de figer le design. Tension non arbitrée.
- **Premium AI tool (Cursor 60 Md $) vs Open source alternative (Cody + Claude Code + VSCode)** : la doctrine A'Space prône l'alternative open-source ; mais Cursor reste dominant chez les devs pros. Pas de bascule franche observée.

## 4. Les 10 guides de tête

| Chemin | Titre | Pourquoi celui-ci |
|---|---|---|
| `01_Product/_INDEX.md` | 01_Product — Index (Roadmap · UX · Spec · Founder-grade) | Canon du domaine, sister B2/B3 |
| `01_Product/2026-06-18_musk-rachete-cursor-compute-ownership-supply-chain.md` | Pourquoi Musk rachète un éditeur de code ? | Doctrine Supply Chain Awareness, risque compute Musk |
| `01_Product/2026-06-25_design-skills-that-actually-work-Ot582-E61ac.md` | Design Skills That Actually Work (AI Labs) | Skill vs MCP, Anti-AI slop, Functional vs Marketing UI |
| `01_Product/PRODUCT_CHANNELS_AUDIT.md` | PRODUCT_CHANNELS_AUDIT — Analyse du gisement Product | 3 chaînes canoniques, 137 vidéos classifiées |
| `01_Product/_KaFS4Dxs5k.md` | EUform mirror (cross-référence Ops) | Sister canon — Micro-SaaS scopé |
| `01_Product/djYKi28hL_8.md` | G7 Leaders Meet Sam Altman (mirror) | Sister canon — AI strategy |
| `01_Product/Geordi_YT-01_Product/Geordi_YT-_kIxjlEf_0U.md` | On a réuni 200 founders SaaS FR (mirror) | Sister canon — sister Sales 4 |
| `01_Product/Dan_Martell/` (subdir) | Dan Martell 5 vidéos Product | Source sister — Product scaling |
| `01_Product/Leo_Grindarss/` (subdir) | Leo Grindarss 30 vidéos (mirror) | Source sister — TikTok monétisation |
| `01_Product/Romain_Brunel/` (subdir) | Romain Brunel (Affiseo) 88 vidéos | Source sister — SEO/affiliation |

## 5. Angles morts

- **Product discovery opérationnelle** : aucun guide sur les méthodologies discovery (Jobs To Be Done, Design Sprint, continuous discovery). Renvoie au domaine 4 Sales (SPIN/Gap).
- **Product analytics** : pas de guide sur les métriques produit (DAU/MAU, retention cohorts, feature adoption, North Star Metric).
- **Pricing produit** : ADR-AAAS-PRICING-001 est sister, mais aucun guide canonique sur le pricing des features (price elasticity, willingness-to-pay).
- **UX research** : aucun guide sur les interviews utilisateurs, les tests d'usage, le recueil de feedback qualitatif.
- **Roadmap prioritization** : pas de framework documenté (RICE, ICE, MoSCoW). Sister présumée dans ADR canon non listé ici.
- **Feature flagging & canary release** : aucun guide opérationnel, sister implicite avec domaine 7 R&D/IT.
- **Accessibility (a11y)** : aucun guide sur WCAG, screen reader, contraste. Anti-AI-slop adjacent mais non couvert.
- **Internationalization (i18n) & localization (l10n)** : aucun guide sur les conventions locales (formats date/nombre, devise, langue).
- **Open source product management** : sister Shadcn + Cody mentionnés mais pas de canon dédié.
- **Hardware / physical product** : 100 % du corpus est software/SaaS. Le hardware/IoT n'est pas couvert.

## 6. Notes canoniques

- **Doublonnage structurel `01_Product` + `01_Product_Product`** : héritage d'une reclassification antérieure. Le brief §1 note que « Traite les deux comme un seul domaine, et **signale les doublons de contenu** plutôt que de les fusionner toi-même ». C'est fait ici. Le sister `01_Product_Product/` est essentiellement des mirrors des guides Ops/Sales/Finance reclassés — 95 % de noise (Geordi_YT-*).
- **Pollution ~90 %** : sur 907 fichiers classés en domaine 3, ~850 sont du noise capté par mots-clés `product|feature|design|niche|icp|pmf`. Le canon réel tient sur ~10 fichiers.
- **Premium L1** : 2 fichiers DISTILLED_L1_PREMIUM (Musk Cursor 25:39 + Design Skills 16 853 chars).
- **B1 FILTER GREEN LANTERN** sur le guide Design Skills — utile pour le routage, pas pour les thèses.
- **Cross-référence forte avec domaine 7 (R&D & IT)** : la doctrine Supply Chain Awareness est **opérationnelle** côté IT (qui possède l'infra), **stratégique** côté Product (qui dépend de l'infra). Pattern : doubler la lecture IT + Product pour tout audit dépendance.
- **Sister canon critique** : `ADR-OMK-004` (Pivot Supabase Cloud + Vercel) et `ADR-L2-BDLD-001` (Product ↔ LD04 Cognition Tilly bijection). Toute modification d'un guide Product doit citer au moins l'un.
- **Frontmatter manquant** : Picard A3 doit appendre `sister_b1: jerry-prime` + `ld_owner: Tilly` dans chaque frontmatter des fichiers canon (D6 2026-07-03 action gated).
