---
source: A0_Amadeus_market_study (recovered) + SDD-007
date: 2026-06-03
type: icp_market_study
domain: L2_Business / Growth+Sales / Project 00 Agency as a Service / Mode Solaris
status: CONSOLIDATED
provenance:
  - Gemini_Takeout_2026/2026-05_conversations.md ("Topographie du Marché des Agences 2025-2026" + "Pressure Cooker")
  - LLM_Wiki/raw/sdd/SDD-007_sob-factory-icp-variants.md (§3 SOLARIS — formalized ICP)
tags: [#icp #solaris #aaas #agences #marketing #creative #market_study_2026 #voc #soc #sla #soa #picard #summer]
---

# 🌅 SOLARIS ICP & Market Study 2026 — Agency-as-a-Service flagship

> **Décision (tranchée par l'étude + SDD-007)** : l'ICP Solaris = **les agences marketing / créatives / web**,
> **PAS** le B2B SaaS / startups tech. L'étude 2026 ("🏆 Le Gagnant : Marketing Digital & Social Media =
> le Variant Solaris"). Dans la matrice SOB : Solaris = créatif/marketing · Nexus = cabinets juridiques ·
> Orbiter = BTP/chantiers. Cette fiche consolide l'étude éparpillée (dump conversation + SDD raw) en un
> socle exploitable pour l'offre. **Rien fabriqué — rapatriement + structuration de tes sources.**

---

## 1. La cible : 4 archétypes d'agences (Topographie 2025-2026)

Le marché des agences s'est scindé en 4 archétypes ; chacun a une douleur distincte et un angle Solaris.

| Archétype | Nouvelle offre | Douleur (l'entropie) | Angle d'attaque Solaris (le remède) |
|---|---|---|---|
| **1. RevOps / Performance** ("Ingénieurs du Revenu") | Growth-as-a-Service, attribution, CRM-Sales | **Fragmentation data** : réparer des zaps cassés (HubSpot/Stripe/régies) > optimiser | **SOC + Build Gates** : fin des silos, routing L0 à précision mathématique |
| **2. Content Forges / Brand Entities** ("Usines Média") | Domination multicanal, owned media | **Margin bleed** : les allers-retours de révision (prompt-fatigue) détruisent **80% de la marge** | **Content Forge (Flash) + RAG anti-hallucination** : ÷10 le QA humain, 500 assets sans polluer le contexte marque |
| **3. AAA (AI Automation Agencies)** | Agents internes, automatisation support | **Paradoxe du cordonnier** : vendent l'automatisation, back-office en chaos (Make qui explose les budgets API), zéro infra souveraine | **Bare Metal Dokploy (Cyborg)** : « deviens éditeur de logiciel, ton propre Control Plane » — **ticket franchise 1555 $** |
| **4. Boutiques stratégie high-ticket** ("Penseurs") | Fractional CMO, audits, positionnement | **Plafond de verre** : « qui exécute ? » → refuser = perdre la LTV ; accepter = enfer du management freelance | **AaaS marque blanche** : « reste la façade stratégique, branche tes clients sur notre exécution, garde **70% de marge** sans embaucher » |

---

## 2. ICP primaire formalisé (SDD-007 §3.1)

**ICP primaire :**
- Agences de design (UI/UX, branding, print)
- Studios de production vidéo & motion design
- Agences médias & content marketing
- Studios photo pro (> 50 projets/an)

**Critère d'entrée (qualification ICP) :**
- ≥ 3 membres d'équipe
- ≥ 15 projets clients actifs simultanément
- Douleur de versioning **documentée**
- Perd **≥ 5h/semaine** en allers-retours de validation

**Persona décideur :**
- Directeur créatif ou fondateur d'agence, **30-45 ans**
- Saturé par l'administration, veut « juste créer »
- A déjà essayé Notion / Figma / Monday **sans succès structurel**

---

## 3. Douleurs & Désirs transversaux (le "Pressure Cooker" 2026)

**🩸 Douleurs (Margin Bleed) :**
- **Épuisement créatif & turnover** — douleur n°1 ; remplacer un talent = **33% du salaire annuel**. L'agence est « un tourniquet à dépressions ».
- **Paradoxe post-clic & ROI** — budgets gelés (**54% des entreprises coupent la pub**) ; les clients exigent du CAC/revenu, plus des « clics ».
- **AI Overwhelm** — le FOMO IA paralyse ; bloqués dans l'exécution, pas le temps d'expérimenter.
- **Croissance toxique** — **37%** peinent à acquérir ; celles qui grandissent trop vite sans SOP → qualité ↓, churn ↑.

**🌟 Désirs (Quête de souveraineté) :**
- **Rentabilité, pas CA** — clients qualifiés long terme, marge nette, arrêter de justifier les honoraires chaque mois.
- **Statut de Challenger indépendant** — un **système propriétaire** qui les sort de la commoditisation.
- **Zero-Management** — le rêve 2026 : non plus 50 salariés (coûts fixes), mais **3 super-humains orchestrant 50 agents logiciels**.

---

## 4. Les 3 leviers de vente 2026 (ce qui ferme en Solaris)

Les agences ne répondent plus aux *promesses d'outils* (« on utilise l'IA la plus avancée ») mais aux **garanties de système** :

1. **La fin de la location de temps** — elles veulent tarifer à la valeur/au résultat → besoin d'un **coût de production fixe (le "Compute")** pour le sécuriser.
2. **La protection anti-commoditisation** — si le client final sait utiliser un LLM, l'agence justifie son prix par son **Système Propriétaire** (= acheter une instance Solaris le leur donne).
3. **Le Zero-Management** — vendre l'orchestration, pas l'effectif.

> Ces leviers se branchent direct sur la doctrine Sales v3 : **S15 Doctor Frame** (diagnostiquer la douleur
> versioning/margin-bleed avant de prescrire), **S4/S16** (prix-valeur, jamais au coût), **S20** (vendre la
> rétention via le système propriétaire).

---

## 5. Le backbone propriétaire — SOA / SOC / SLA (ce qui rend l'offre incommoditisable)

Le « Système Propriétaire » que les agences achètent n'est pas un slogan — c'est une **architecture contractuelle** à trois piliers (source : SDD-007 + Master SOC schema). C'est ce qui transforme Solaris d'une « presta agence » en **actif logiciel souverain**.

### SOA — *Sector/Service-Oriented Architecture* (l'isolation)
Les **8 domaines** (SOA01–SOA08 : People, IT, Ops, Product, Growth, Finance, Legal, Sales) sont **isolés** — chacun son orchestrateur B2, ses gates, sa Definition of Done. Pour l'agence cliente : pas de monolithe fragile ; chaque pôle (création, livraison, facturation…) est un module gouverné indépendamment. *C'est le remède direct à la « fragmentation data » de l'archétype RevOps.*

### SOC — *Service-Oriented Communication* (la douane / le contrat de message)
Le **Master SOC Schema** : un contrat **JSON à 3 couches (Header · SLA · Payload métier)**, validé par Zod, qui route **chaque** message inter-domaines avec une précision mathématique. C'est le « Harnais de Test » permanent de Solaris : aucune action ne traverse sans passer la douane → **immunité contre les hallucinations** et les silos. *Remède à l'archétype RevOps (zaps cassés) et Content Forge (dérive de contexte marque).*

### SLA — *Service Level Agreement* (l'engagement chiffré, Compute fixe)
La **couche d'engagement** *dans* le SOC payload : `contract_type: SLA_STRICT | CUSTOM_ENTERPRISE`, timeout global, gestion `SLA_BREACH`, et surtout un **budget de Compute fixe par mission** (traçable via `trace_id`). Traduit pour l'agence :
- **Coût de production fixe** → permet la tarification à la valeur (levier de vente n°1).
- **Révisions bornées contractuellement (max 2 rounds, SDD-007 §3.2)** → tue le margin-bleed des allers-retours (douleur n°1 des Content Forges).
- Livrables sous SLA strict (résolution/format/délai garantis).

> **En une phrase** : **SOA** isole, **SOC** route et vérifie, **SLA** garantit et chiffre. Ensemble =
> le système propriétaire qui justifie le premium et bloque la commoditisation (levier de vente n°2).

---

## 6. Architecture de livraison Asset-First (SDD-007 §3.2, résumé)

Ce que l'instance Solaris fait tourner pour l'agence :
- **Couche 0 — Mémoire des Assets (Agent Librarian)** : versionne/nomme/dé-doublonne chaque asset (n8n + Supabase Storage + Vector Search).
- **Couche 1 — Validation des livrables (Agent Art Director)** : pré-valide brief/résolution/format, génère le compte-rendu de révision (Claude Vision + n8n).
- **Couche 2 — Orchestration projet (Batman/Fantastic Four)** : pipeline Brief→Concept→Production→Validation→Livraison, SOP par type, révisions plafonnées (le SLA).
- **Couche 3 — Croissance (Superman/Guardians)** : acquisition ciblée (Gamora, agences similaires), referral, cas clients documentés.

---

## 7. Prochains pas (offre)
1. **Offre Grand Slam** ($100M Offers, S1-S4) : packager l'instance Solaris en offre core (setup + retainer, F23) pour l'archétype prioritaire — **proposition : commencer par les "Content Forges"** (margin-bleed le plus aigu + ROI démontrable via le SLA 2-rounds).
2. **Doctor Frame de diagnostic** (S15) : le script de qualification = les 4 critères d'entrée + la douleur versioning chiffrée (≥5h/sem).
3. **Modèle prix/marge** (Finance JTBD-001) : ancrer le Compute fixe → marge cible (F4/F24, sovereign-infra arbitrage).

---

## Sources & provenance
- **Étude brute** : `00_Amadeus/30_MEMORY_CORE/Gemini_Takeout_2026/2026-05_conversations.md`
  (« Topographie du Marché des Agences 2025-2026 » l.2189+ ; « Pressure Cooker » l.10960+ ; « Le Gagnant » l.18489).
- **ICP formalisé + Asset-First + SOC/SLA/SOA** : `LLM_Wiki/raw/sdd/SDD-007_sob-factory-icp-variants.md` §3 + Master SOC Schema.
- **Doctrine appliquée** : Sales v3 (S4/S15/S16/S20), Finance v4 (F4/F23/F24).
