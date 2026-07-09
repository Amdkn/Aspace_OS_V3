---
id: YT-Wv3ARXImFUg
title: "J'ai tracké tous les salaires des dev"
channel: "cocadmin"
duration: "8:29"
date: "2026-06-18"
category: "Salaires Dev / Méthode Scraping / Infra Statique Cloudflare"
status: DISTILLED_L1_PREMIUM
domain: "04_Finance"
ld: LD02_Finance_Saru  # E1 fix (était: LD04_Cognition_Tilly) — bijection D3
ld_owner: "Tilly"
video_id: Wv3ARXImFUg
url: https://www.youtube.com/watch?v=Wv3ARXImFUg
transcript_source: TranscriptAPI.com MCP (D6 #43)
b2_owner: wonderwoman-finance
sister_b1: jerry-prime
---

# 📖 J'ai tracké tous les salaires des dev

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour le Domaine 04_Finance — Salaires Dev / Méthode Scraping / Infra Statique Cloudflare. Standard Antigravity Premium (D6 #48).

---

## 🧠 Concepts Clés à Haute Densité Sémantique

- **<Méthode Scraping Éthique Multi-Régions>** : Bright Data MCP pour scraper Indeed/LinkedIn/FreeWork × 15 régions FR (vs 1 avant), proxies résidentiels pour éviter bans IP, multi-sites (3) × multi-régions (15) = beaucoup de calls parallélisés. Pattern = ethical scraping assumé (pas de bypass agressif) + observability (métrique de bans).
- **<Stack Infra 'Infaillible + Fragile'>** : Scraping et génération page statique via GitHub Actions quotidien, DB SQLite commit dans repo + Git LFS pour dépasser 100 MB (limite GitHub), site statique servi par Cloudflare Pages (redondant mondial, gratuit). Pattern = minimal ops cost + max durability.
- **<Stats Freelance vs CDI — Signal vs Bruit>** : PHP #1 en CDI mais dernier en freelance (statistiquement significatif sur 1000+ offres) — phénomène régional/niche à creuser. C++ mieux payé tous langages (~15% d'écart avec PHP). Python = sweet spot (correct salaire + beaucoup d'offres). Lesson = lire 2 dimensions (salaire × volume d'offres) avant décision carrière.
- **<Skill Stacks à +Value — Mesure ROI>** : Java + CI/CD DevOps = +3% salaire mais +36% d'offres accessibles. Python + DevOps = +0% salaire mais +40% d'offres. Lesson = choisir skills pour ouvrir accès au marché, pas pour optimiser salaire nominal. ROI ≠ salaire direct.
- **<Power Purchase Parity — Décision Géo>** : Paris 453€/j freelance vs Occitanie 425€ (~5% diff salaire). Mais coût vie Marseille -20/30% vs Paris = ratio pouvoir achat favorable hors Paris. Lesson = optimiser ratio revenu / coût vie local, pas revenu absolu.

---

## 🛠️ Outillage Stratégique & Matrice d'Alignement

| Outil / Technologie / Approche | Rôle Stratégique | Alignement Souverain A'Space |
| :--- | :--- | :--- |
| **<Bright Data MCP>** | Service de scraping éthique avec proxies résidentiels, MCP natif pour Claude. | A'Space : déjà utilisé par plusieurs A3 twins pour veille concurrentielle. |
| **<Cloudflare Pages>** | Hosting statique gratuit, redondance mondiale. | A'Space : canon pour sites publiques (Geordi vault, openclaw.dev). |
| **<GitHub Actions + SQLite + Git LFS>** | Pipeline scraping quotidien, DB versionnée, site statique servi. | A'Space : pattern pour le Geordi aggregator Geordi-public. |
| **<Git LFS>** | Dépassement limite 100MB fichiers dans repo. | A'Space : applicable pour tout binaire > 100MB (modèles LoRA, datasets). |

---

## 🪐 Perspective Souveraine A'Space 04_Finance

Le tracker salaires de cocadmin est un cas d'usage canonique pour A'Space : observabilité du marché tech FR + infra minimale + scraping éthique. (1) **Niveau architecture** : le pattern 'site statique servi par Cloudflare Pages + scraping quotidien via GitHub Actions' est exactement l'architecture canonique A'Space pour les ressources publiques (cf. `00_Amadeus/05_OSS_Twin/` canon OpenSource). Applicable au sister-skill `/youtube-to-guide` — générer des `_BATCH_<date>_INDEX.md` quotidiens via GitHub Actions. (2) **Niveau doctrine** : la doctrine 'skill stacks à +value' valide l'approche A'Space d'enrichir les A3 twins avec des compétences transverses (Tilly + Spock = H30 cognition + doctrine = +36% 'd'offres' d'utilisation). (3) **Niveau action A0 (H3 Saru)** : (a) benchmarker le pattern 'Cloudflare Pages + GitHub Actions + SQLite LFS' pour le sister-skill `area-domain-doctrine-distill`, (b) si A0 est en recherche emploi/freelance, appliquer le ratio pouvoir achat (Paris vs Marseille = -20% coût vie = décision géographique). Doctrine Anti-Paresse D6 : un tracker de salaire n'a de valeur que si l'analyse corrèle salaire × volume d'offres × pouvoir achat, pas une dimension isolée.

---

## 🕹️ Protocole d'Exécution D.E.A.L

| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | Cartographier les 'skill stacks à +value' pour les A3 twins : Tilly × Spock = +36% offres, Saru × Culber = +X% ? | Identifier synergies transverses. |
| **Éliminer** | Skills stacks obsolètes dans A3 twins (ex: A3 twin calé sur une techno dépréciée depuis 2 ans). | Maintenir pertinence canon. |
| **Automatiser** | Implémenter scraping quotidien Geordi aggregator via Cloudflare Pages + GitHub Actions + SQLite LFS pattern. | Observabilité continue. |
| **Libérer** | Créer 1 dashboard A'Space 'salaires A3 twins' pour benchmarker les salaires d'agents IA (vs devs humains) sur le marché. | Nouveau livrable canonique. |

---

## 🔬 Annexes Détaillées de l'Audit Sémantique & Technique

### Note Note A3-01 : Calcul ROI Skill Stack pour A3 twins

Java + CI/CD = +3% salaire / +36% offres. Pattern transposable : A3 twin Tilly + Spock doctrine = ?% valeur ajoutée sur missions Symphony. Sister-skill `area-domain-doctrine-distill` peut scorer cette synergie transversement.

### Note Note A3-02 : Architecture 'Infaillible + Fragile' appliquée A'Space

Cocadmin : scraping quotidien via GitHub Actions + SQLite + Git LFS + Cloudflare Pages = 0 ops manual. Pattern transposable : A'Space `/youtube-to-guide` batch quotidien pourrait suivre le même pipeline.

### Note Note A3-03 : Power Purchase Parity appliqué aux décisions A'Space

Paris 453€/j vs Marseille -20% coût vie = ratio favorable hors Paris. Décision géographique A0 (où vivre) = optimiser ratio qualité vie / coût, pas revenu absolu. Doctrine Saru H3 (runway review).

---

*Fiche de connaissances souveraine d'04_Finance générée sous A'Space OS V2 — Standard Antigravity Premium (D6 #48).*
