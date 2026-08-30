---
okf_version: "0.1"
type: guide-distillation
title: "02 · Opérations en Loops"
description: "Distillation du corpus Ops Geordi : LWAS framework (Nate Herkelman), Micro-SaaS undercut (Abhishek EUform), Harness Engineering (Matt Pocock), AI-First Business (Hormozi), 7 KPIs canon, stack souverain n8n/Docker/Obsidian."
timestamp: 2026-08-02T15:20:00-04:00
domain: LD01_Career_Business
agent: A3_Book
squad: Fantastic Four (B3-2 Mr Fantastic lead, Invisible Woman, Human Torch, The Thing)
vp: Batman
sources_count: 348
---

# 02 · Opérations en Loops

Le domaine 2 porte l'**exécution systématisée** : transformer une opération manuelle en
boucles auto-alimentées, mesurer ce qui compte, déployer le moins de stack possible pour
le plus d'effet. Le canon est dense : 30 guides premium + sous-dossiers Dan Martell. Le
propriétaire canonique est **B2 Batman** (LD02 Finance Saru ↔ LD01 Business), squad
**Fantastic Four** avec **Mr Fantastic** en lead (process elasticity, R&D runbooks).

Le corpus est aligné sur l'**ADR-AAAS-ACQUISITION-DOCTRINE-001** (RATIFIED 2026-06-24,
25 455 chars) et **ADR-AAAS-PRICING-001** (5 Tiers USD, RATIFIED + AMENDED).

## 1. Ce que le corpus dit

### Thèse 1 — LWAS (Learn, Wire, Automate, Scale) est le framework canonique pour systématiser une opération

Nate Herkelman (AI-First Agency Model) impose la séquence : (1) **Learn** = comprendre le
flux manuel existant, (2) **Wire** = connecter les briques existantes, (3) **Automate** =
déléguer les étapes répétitives à l'IA, (4) **Scale** = augmenter la charge sans embauche.
**Cible** : marges brutes de 60-75 % (historiquement réservées aux éditeurs de logiciels)
dans une agence de services, en réduisant les coûts de prestation jusqu'à 80 % via IA.
Sources : `02_Ops/ai-first-agency-model.md` (Nate Herkelman, 30:00, 2026-05-31).

### Thèse 2 — Micro-SaaS discipliné vs cathédrale TAM-complète : scope ou rien

Abhishek (EUform, 11K$ MR / 35K users / 500 paying) incarne le **Micro-SaaS scopé** :
un produit tenu sur **une seule** catégorie d'usage, bâti par un indie hacker, qui ne
tente pas de servir le TAM complet. EUform ne fait que des formulaires de collecte
(name/email/star/export CSV) — pas de landing pages, pas de logique conditionnelle
complexe. Sister canon A'Space : on ne construit pas la cathédrale, on construit **une
niche validée** dans la cathédrale d'un leader.
Sources : `02_Ops/2026-06-24_i-copied-a-100m-saas-undercut-prices-hit-10k-month_KaFS4Dxs5k.md`
(Starter Story × Abhishek, 8:42, 2026-06-24).

### Thèse 3 — Undercut pricing = canal d'acquisition, pas margin erosion (ADR-SOBER-002)

L'undercut pricing chez Abhishek n'est **pas** une stratégie de margin erosion : c'est
une **stratégie d'acquisition**. Typeform a augmenté ses prix → pricing devenu pain point
→ EUform entre par la porte du prix comme preuve de valeur. **Doctrine critique**
(ADR-SOBER-002 Anti-Paperclip, RATIFIED 2026-06-21) : le prix bas **doit refléter une
vraie efficience opérationnelle** (coût marginal bas, scope réduit, pas de feature creep).
Pas de dumping insoutenable qui se transforme en churn massif à M+6.
Sources : `02_Ops/2026-06-24_i-copied-a-100m-saas-undercut-prices-hit-10k-month_KaFS4Dxs5k.md`,
`02_Ops/_INDEX.md` (sister ADRs).

### Thèse 4 — LTV:CAC ≥ 25:1 minimum viable, sister directe ADR-AAAS-PRICING-001

35 000 visiteurs/mois, ~1.5-2 % conversion premium, ~500 paying customers, 11 000$ MR.
~22$ ARPU/mois, ~264$ LTV annualisé. Sister A'Space : chaque tier canon doit être calibré
pour que **LTV ≥ 25× CAC blended** (paid + organic + referral). Le pricing n'est pas un
chiffre arbitraire — c'est l'inverse d'une fonction de coût d'acquisition viable.
Sources : `02_Ops/2026-06-24_i-copied-a-100m-saas-undercut-prices-hit-10k-month_KaFS4Dxs5k.md`.

### Thèse 5 — Harness Engineering > raw model : investis 10-20 % upfront, économise 100K tokens / 6 mois

Matt Pocock : « People are focused on the wrong thing. They're looking at the big shiny
new thing when in fact just focus on the stuff that's been working for 30-40 years. » Le
modèle change tous les 6 mois, les bonnes pratiques d'ingénierie logicielle durent 30-40
ans. **Tactical vs Strategic programming** (Ousterhout) : Tactical = écrire vite, debug
vite, ship vite. Strategic = investir 10-20 % upfront pour rendre la code base plus
facile à modifier ensuite. **Token Economics** : 1 jour de doc = 100K tokens économisés
sur 6 mois. ROIs du harness engineering sous-estimés par les devs qui optimisent
uniquement les models.
Sources : `02_Ops/2026-06-19_matt-pocock-harness-engineering-agentic-workflow.md` (62:24,
2026-06-19).

### Thèse 6 — Matt Pocock Skills (130K stars) = standard de facto pour harness TypeScript

Approche : **skills déclaratives + commands structurées**, pas prompts ad-hoc. Bon
niveau d'abstraction — assez structuré pour la cohérence, assez flexible pour s'adapter.
**D11 Fable Score** = métrique quantitative du harness : **coverage + token economy +
speed + quality**. Doctrine A'Space : tout A3 twin doit avoir un score mesurable. Sans
métrique, le harness dérive vers l'over-engineering ou le sous-engineering.
Sources : `02_Ops/2026-06-19_matt-pocock-harness-engineering-agentic-workflow.md`.

### Thèse 7 — Skill Stacking + Règle des 20 heures (Hormozi)

Hormozi : la valeur sur le marché provient de l'**accumulation de compétences
complémentaires** combinées à la maîtrise de l'IA. L'IA agit comme **multiplicateur** sur
un socle de compétences existant (Copywriting, Sales, Tech). La **règle des 20 heures** :
la barrière à l'adoption de l'IA n'est pas intellectuelle mais psychologique. 20 heures
d'expérimentation pratique suffisent pour surpasser 90 % des concurrents qui restent en
observation passive. Lean Team Structure = organisation ultra-réduite assistée par IA.
Sources : `02_Ops/alex-hormozi-ai-first-business-strategy.md` (Alex Hormozi, 22:00,
2026-05-31).

### Thèse 8 — Les 7 KPIs canon + anti-pattern du Manual Reporting Ritual

Le guide ProcessDriven (20 529 chars) ancre les **7 KPIs canon** + l'anti-pattern
*Manual Reporting Ritual*. Doctrine : les KPIs ne se construisent pas dans un tableur
mensuel, ils sont **câblés en continu** et **lus sans friction**. Sister canon A'Space :
A3 Chapel H10 (lead/lag scorecard) + Book H1 (weekly P&L pulse). Le reporting manuel est
le signe d'une stack mal configurée — chaque KPI doit être auto-collecté.
Sources : `02_Ops/_INDEX.md` (sister ADR canon), guide `tov_Xe5xZmU` cité (corpus).

### Thèse 9 — Process Mapping → SOP → Feedback Loops → Delegation → Scaling → Resilience

Shan Hanif (Business is hard until you build systems like this) impose la chaîne :
(a) **Cartographie As-Is** (process mapping, état actuel documenté), (b) **SOP** comme
« langage machine » pour les agents, (c) **Boucles de rétroaction intégrées** (auto-
optimisation continue), (d) **Délégation technique par abstraction** (humain = architecte,
agent = exécutant), (e) **Scalabilité horizontale** (indépendance des nœuds), (f)
**Résilience et exceptions** (retry + notification d'urgence). Le protocole **D.E.A.L** :
Définir → Éliminer → Automatiser → Libérer.
Sources : `02_Ops/business-is-hard-until-you-build-systems-like-this.md` (Shan Hanif, 10:49,
2026-04-20).

### Thèse 10 — Stack souverain : n8n self-hosted + Docker Compose + Obsidian (Vault Ops)

Le canon Ops prescrit un stack 100 % local : (a) **n8n** (Community Edition) — orchestration
centralisée des workflows, connectivité API, déclencheurs complexes ; (b) **Docker Compose**
— conteneurisation pour reproductibilité et isolation ; (c) **Obsidian** (Vault Ops) —
base de connaissances et documentation vivante, chiffrement natif, accès hors-ligne
garanti. Sister canon A'Space : aucune dépendance cloud tiers pour les process critiques.
L'opérateur passe de « exécutant » à « architecte système ».
Sources : `02_Ops/business-is-hard-until-you-build-systems-like-this.md`,
`02_Ops/claude-code-just-got-a-life-os-personal-ai-infrastructure.md`.

## 2. Ce qui est actionnable maintenant

- [ ] Lister ses **5 processus manuels critiques** ; pour chacun, exécuter **L-W-A-S** dans l'ordre (Learn → Wire → Automate → Scale).
- [ ] Calculer son **LTV:CAC blended** ce mois-ci. Si < 25, le pricing n'est pas viable — réviser le tier ou couper un canal d'acquisition.
- [ ] Investir **10-20 % du temps dev** dans le harness engineering (strategic programming Ousterhout). Mesurer l'économie de tokens sur 6 mois.
- [ ] Câbler un **D11 Fable Score** par A3 twin : coverage + token economy + speed + quality.
- [ ] **Bloquer manuellement** les 7 KPIs canon : leads → conversion → ARPU → churn → runway → CAC payback → opex/MR. Aucun ne doit être collecté à la main.
- [ ] Appliquer la **règle des 20 heures** sur 1 outil IA non-maîtrisé cette semaine.
- [ ] **Self-host n8n** sur Docker Compose local ; connecter au moins **3 agents A3** à des déclencheurs réels.

## 3. Ce que le corpus contredit

- **Lever du capital vs bootstrap** : le corpus Ops est massivement bootstrap-friendly (1 200 $/mois stack pour 11K$ MR). Mais les sous-dossiers Dan Martell promeuvent la scale via SaaS venture. Tension non arbitrée.
- **Undercut vs premium pricing** : Abhishek (undercut = acquisition) vs Hormozi (premium = valeur). Le corpus porte les deux doctrines simultanément sans donner de seuil de bascule.
- **Process Mapping d'abord vs DBM monitoring direct** : Hanif prescrit la cartographie As-Is exhaustive avant automatisation ; Deya prescrit le DBM qui monitore sans cartographie. Deux visions opposées du même problème.
- **AI-First Agency (Herkelman) vs Solo AI Business (Abhishek)** : agence = client-serving scalé, solo = produit scopé. Le canon Ops porte les deux comme variantes d'un même archétype.
- **Tactical vs Strategic programming** : Pocock tranche pour Strategic, mais le Y Combinator moderne ship-it vite. Le corpus ne tranche pas le moment de basculer de l'un à l'autre.

## 4. Les 10 guides de tête

| Chemin | Titre | Pourquoi celui-ci |
|---|---|---|
| `02_Ops/_INDEX.md` | 02_Ops — Index (Systématisation · KPIs · Pricing · Business OS) | Canon du domaine, sister ADRs |
| `02_Ops/ai-first-agency-model.md` | The AI-First Agency Model (Nate Herkelman) | LWAS framework canon, marges 60-75 % |
| `02_Ops/2026-06-19_matt-pocock-harness-engineering-agentic-workflow.md` | Matt Pocock Skills, Clearly Explained (130K stars) | Harness > raw model, D11 Fable Score |
| `02_Ops/2026-06-24_i-copied-a-100m-saas-undercut-prices-hit-10k-month_KaFS4Dxs5k.md` | I Copied a $100M SaaS, Undercut Their Prices (Abhishek) | Micro-SaaS, LTV:CAC 25:1, capital-efficient |
| `02_Ops/alex-hormozi-ai-first-business-strategy.md` | Alex Hormozi on AI-First Business Strategy | Skill Stacking, règle des 20 heures |
| `02_Ops/business-is-hard-until-you-build-systems-like-this.md` | Business is hard until you build systems like this | D.E.A.L + n8n + Docker + Obsidian |
| `02_Ops/2026-06-18_gregory-projets-ia-organisation-frontiere-contexte.md` | Projets IA · Organisation · Frontière · Contexte (Grégory) | Frontière organisationnelle agent |
| `02_Ops/2026-06-24_7-metrics-all-small-businesses-should-be-tracking-tov_Xe5xZmU.md` | 7 Metrics All Small Businesses Should be Tracking | 7 KPIs canon + anti-pattern reporting |
| `02_Ops/claude-code-just-got-a-life-os-personal-ai-infrastructure.md` | Claude Code Just Got a Life OS | Personal AI Infrastructure canon |
| `02_Ops/solopreneur-ai-agent-business-BI-MNjm1tTQ.md` | The $1M+ Solo AI Agent Business (Full Course) | 5 sub-types persona Structuration-First |

## 5. Angles morts

- **Opérations B2C grand public** : tout le corpus Ops est B2B ou B2B2C. Pas de guide sur le retail, le e-commerce physique, la logistique.
- **Conformité_ops sectorielle** : HIPAA, PCI-DSS, FedRAMP, HDS — non traités. Renvoie au domaine 8.
- **Gestion de crise / BCP** : pas de guide sur le plan de continuité d'activité (PCA), la gestion de crise cyber, ou le disaster recovery.
- **Vendor management** : aucun guide sur la sélection / négociation / sortie d'un fournisseur critique.
- **Capacity planning & forecasting** : la dimension prévision de charge / staffing / infra n'est pas couverte séparément.
- **SRE / on-call rotation** : aucun guide sur les astreintes, les SLO/SLA engineering, l'observabilité production.
- **Processus de vente-ops / RevOps** : frontière floue avec Sales (domaine 4). Pas de canon Ops dédié.
- **International ops / multi-juridiction** : pas de guide sur les opérations distribuées (timezone, langue, contract local).

## 6. Notes canoniques

- **Doublon 02_Ops + 02_Ops_Ops** : même domaine canonique, dossiers jumeaux hérités d'une reclassification antérieure. Pollution structurelle.
- **30 guides canon dans `_INDEX.md`** + ~280 fichiers Geordi_YT-* = 348. Forte proportion de noise (shorts, hashtags, musique, ASMR).
- **Sous-dossier Dan Martell** : 3 vidéos Ops reclassifiées (9w0INwjTYdU, eY9gpdaXW7w, y5jL8KsUwaI) — « Business is Hard Until You Build Systems », « How to Build Systems with AI », « How to Make Time For Everything ».
- **Sister canon critique** : `_INDEX.md` cite 6 ADRs ratifiées (Acquisition Doctrine, Pricing 5 Tiers, Nexus Transform, ICP Orbiter, SOBER-002, META-001). Toute modification d'un guide Ops doit citer au moins l'ADR-AAAS-PRICING-001.
- **ADR-OMK-NEXUS-TRANSFORM-001 (PIVOT OMK → Nexus)** ratifié 2026-06-24 — toute mesure d'impact Ops doit distinguer l'ancien périmètre OMK du nouveau Nexus.
- **Premium L1** : 3 fichiers DISTILLED_L1_PREMIUM (BI-MNjm1tTQ 22 708 chars, tov_Xe5xZmU 20 529 chars, _KaFS4Dxs5k 21 717 chars). Le reste = CANON standard ~6-7K chars.
