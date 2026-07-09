---
source: A0_Amadeus + Finance v4 (Hormozi-adjacent, Wright's law) + OFFER_GRANDSLAM_SOLARIS_CONTENT_FORGE + 5-segment SaaS lesson
date: 2026-06-03
type: price_margin_model
domain: L2_Business / Finance / Project 00 Agency as a Service / Mode Solaris
status: DRAFT_V1 (numbers = A0-tunable hypotheses, flagged)
tags: [#finance #pricing #margin #value_ladder #solaris #content_forge #compute_fixe #setup_retainer #sovereign_arbitrage #picard]
---

# 💰 Modèle Prix / Marge — Solaris (Content Forge + Lite)

> Pendant Finance du couple Growth(ICP)/Sales(offre). Chiffre le **price/margin boundary** des 2 tiers de la
> value ladder (S21). Doctrine : **F4** (vraie marge après Compute/API/Stripe), **F23** (setup+retainer),
> **F24** (arbitrage infra souveraine → marge vers 90%), **F25** (tailwind loi de Wright), **F13** (two-horizon).
> ⚠️ **Tous les montants = HYPOTHÈSES à calibrer par A0.** La structure est ferme, les chiffres non.
> Règle d'or : **prix à la valeur, jamais au coût (S4/F)** ; discount >15% = sign-off Wonder Woman.

---

## 1. La value ladder (2 tiers, 2 segments)

| | **Solaris Content Forge** (premium) | **Solaris Lite** (self-service) |
|---|---|---|
| Segment | Agence PME (≥3 membres, ≥15 projets) | Créateur/freelance contenu solo |
| **Setup** | ~5 000 – 8 000 $ (Genesis Sprint) | **~500 $ à l'inscription** |
| **Retainer** | ~2 000 – 3 000 $/mo | ~49 – 99 $/mo |
| **Deal annualisé** | ~30 000 – 40 000 $ | ~1 100 – 1 700 $ |
| Touch | High (orchestration humaine) | Low (self-service) |
| KR Sales | ASP ≥ 25K$ Solaris ✅ | volume / acquisition organique |

---

## 2. COGS (le coût réel à servir) — F4

Le coût des marchandises vendues d'une instance Solaris se résume à :
| Composant COGS | Nature | Levier de réduction |
|---|---|---|
| **Tokens LLM** (API) | variable / mission | routing cognitif : modèle local/cheap d'abord, frontier au besoin (F24) |
| **Hébergement / Compute** | semi-fixe (VPS/Dokploy) | infra souveraine vs SaaS tiers (F24) ; **Compute plafonné par le SLA** |
| **Stripe / paiement** | ~2-3% | incompressible |
| **Orchestration humaine** | élevé (premium) / ~0 (Lite) | le delta de touch EST le delta de marge entre les 2 tiers |

→ **Compute fixe par mission** (SLA budget/`trace_id`) : c'est ce qui permet la tarification à la valeur côté
vente (levier n°1) ET protège la marge côté Finance. La marge nette **réelle** se calcule *après* ces postes (F4),
jamais en marge brute théâtre.

## 3. Marge cible — F24 + F25
- **Lite** : COGS ≈ tokens + hébergement mutualisé + Stripe → marge nette visée **>90%** (self-service, ~0 humain). C'est le tier "machine".
- **Content Forge** : COGS + orchestration humaine (Genesis Sprint + suivi) → marge nette visée **>60%** (cible F North Star), montant vers >75% à mesure que les agents absorbent le high-touch.
- **Tailwind (F25)** : le coût d'inférence ÷2/an → à prix constant, la marge **monte mécaniquement** ; option de baisser le prix Lite pour tuer la concurrence low-cost sans sacrifier la marge.

## 4. Cash & paiement (F11/F1)
- **Lite** : prélèvement Stripe à l'inscription (setup) + abonnement mensuel auto → cash immédiat, CAC amorti au signup (F23).
- **Content Forge** : setup facturé à la signature (devis/bon de commande pour le segment PME — cf. leçon Tizi), retainer mensuel ou annuel ; relance >7j, escalade >14j (F11).
- Réconciliation Stripe ↔ `Finance_Pulse` 100% (F12).

## 5. Two-horizon (F13)
- **Plancher (survie)** : runway, marge réelle, MRR des 2 tiers (objectif flagship : **$10K MRR sans dépendance Jerry**).
- **Plafond (ambition)** : la value ladder est le mécanisme de scale — Lite fait le volume (acquisition organique), Content Forge fait la marge ; licences additionnelles par marque-client (share-of-wallet, S20) = expansion LTV.

## 6. Garde-fous (anti-patterns Finance)
- ❌ Lancer un tier sans marge connue (F : "ne scale pas une offre à marge inconnue").
- ❌ Enlever un zéro sur le premium pour le **même** segment (= sous-pricing, la leçon des 5 segments).
- ❌ Discount >15% sans sign-off Wonder Woman.
- ❌ Marge brute théâtre ignorant Compute/API/Stripe (F4).

---

## Prochains pas
1. **A0 calibre** : setup/retainer des 2 tiers, le seuil de Compute plafonné Lite, le segment exact du Lite.
2. **Mesurer le COGS réel** d'une mission-type (tokens + Compute) pour ancrer la marge — pas d'estimation en l'air.
3. **Legal** : la garantie 60j de l'offre + les CGV des 2 tiers (L25/L1).

## Sources
- Offre : `02_Sales.../OFFER_GRANDSLAM_SOLARIS_CONTENT_FORGE.md` (§4 + 4bis value ladder).
- Segmentation/pricing : `03_Resources_Geordi/01_Guides/06_Sales/resource_10saas_b2b_b2c_5segments.md`.
- Doctrine : Finance v4 `06_Finance.../03_WONDERWOMAN_FINANCE_PRINCIPLES.md` (F4/F13/F23/F24/F25) ; Sales S4/S21.
- One datum, one owner (ADR-MESH-L2-001) : Finance possède la vérité prix/marge ; Sales possède l'offre ; Growth l'ICP.
