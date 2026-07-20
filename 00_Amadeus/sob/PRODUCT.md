# PRODUCT.md — définition DISTILLÉE DU CANON (v2, sourcée — corrige la v1 écrite de mémoire)

> **v2 du 20/07/2026.** Chaque bloc cite son ADR ratifié. La v1 (non-sourcée) est supersédée : le travail de définition des niches et de l'ICP n'était ni perdu ni inutile — il était RATIFIÉ et la v1 l'ignorait (violation D2, corrigée ici). Toute copie (landing, outreach, démo, contrat) dérive de CE fichier.

## Le nom et le variant
**OMK Nexus** — variant **Data-First / Conformité** de l'architecture 3-ICP (Solaris = flux/image · **Nexus = donnée froide, critique, confidentielle** · Orbiter = terrain).
*Source : ADR-ICP-NEXUS-001 Pilier 4 (RATIFIED 2026-06-24) · ADR-L2-AAAS-001 §D2.*

## La niche (VERROUILLÉE par arbitrage direct A+)
> **Niche = l'intersection {Cabinets de Coaching Premium} × {Agences de Business Development}.**
Business/Sales coaching B2B haut de gamme. **Ni médical, ni psy** — rejet explicite des niches régulées (HIPAA/FDA, leçon Medvi : extraire la puissance des agents à coût écrasé, rejeter l'exposition réglementaire).
*Source : ADR-NEXUS-NICHE-001 §D1 (RATIFIED, arbitrage A+) + §Medvi.*

## L'ICP (le persona ratifié — pas une invention)
**« Expert méthodique / Praticien conformité »**, sous-type #4 : **Coachs/Consultants seniors** — pratiques haut de gamme, **facturation 500-2000 €/h**, programmes **$7.5-25K**, livrables = notes structurées + IP intellectuelle.
Sa douleur canonique n'est pas le manque de créativité : c'est le **débordement informationnel** — et des marges compressées par la facturation à l'heure (la force brute humaine).
*Source : ADR-ICP-NEXUS-001 Pilier 1 (L25160-25314 verbatim) · MANIFEST omk-nexus-coaching-premium (spearhead $7.5-25K).*

## Le mantra doctrinal (l'angle de TOUTE la copie)
**« L'illusion de la complexité. »** Le cabinet croit que son back-office exige son cerveau ; il exige un système. On ne vend pas des heures d'agents — on vend la **« Détention de Système »** : le coach passe de vendeur d'heures à détenteur d'un système qui produit.
*Source : ADR-ICP-NEXUS-001 Piliers 2 + 3 (verbatim L25304).*

## Le produit
**La Citadelle du Savoir du coach** : une instance privée d'agents IA, dédiée, qui traite sa donnée froide, critique et confidentielle — et fait tourner 4 fonctions en continu :

| # | Fonction | Concrètement | Ancrage canon |
|---|---|---|---|
| 1 | **Contenu dans sa voix** | newsletters, LinkedIn, frameworks — depuis SES notes/sessions, prêts à valider | livrables = IP intellectuelle (Pilier 1) |
| 2 | **Client ops** | Session 0, préparation de sessions, suivis inter-sessions | débordement informationnel (Pilier 1) |
| 3 | **Conformité productisée** | notes, RGPD, contrats tenus à jour, auditables en 1 query | « productiser la conformité » (Pilier 3) |
| 4 | **Pipeline qualifié** | quiz d'audit qui diagnostique + relances autonomes | axe Business Development (NICHE-001) |

## La Killer Feature (le différenciateur ratifié)
**Zero-PII Agentic Governance** — le secret professionnel est une hard constraint du marché (Pilier 3) et il n'y a **aucun dominant player Zero-PII** sur ce segment fragmenté. Instance privée par coach : ses données ne nourrissent personne d'autre, gouvernance agentique durcie (5 mécanismes).
*Source : ADR-ICP-NEXUS-001 Piliers 3 + 5.*

## Ce que ce N'EST PAS
- **Pas un chatbot qui coache** — l'instance fait le back-office ; la conversation reste au coach.
- **Pas un SaaS mutualisé** — Citadelle privée, Zero-PII (Pilier 5, pas un slogan).
- **Pas une niche santé/psy** — hors périmètre par arbitrage ratifié (NICHE-001).

## Le pricing (baseline ratifiée)
**1 000 $/mois** par cabinet — baseline NICHE-001 §D2 : **× 100 clients premium = 1,2 M$ ARR**, structure humaine minimale.
Offre fondateur Cycle 1 : **3 places · 1 000 $/mois · configuration incluse · résiliable · données au coach**.
(Grille complète 5 tiers : ADR-AAAS-PRICING-001 — $300-500/an intro → Tier 5 $50K MRR ; le spearhead coach entre par la baseline 1000$/mois, l'expansion multi-tenant vient au Cycle 3.)

## La preuve
Démo live 15 min sur l'instance `demo-coach` (framework 4-Quadrant, Session 0, programme 12 semaines, registre RGPD — `serve_instance.py`).

## Le funnel (officiel, unique)
```
outreach → LANDING → QUIZ D'AUDIT (8 questions → diagnostic) → DÉMO 15 min (instance live)
→ OFFRE fondateur → contrat (pack Legal, 1 scrum/Run) → onboarding (R3)
```

## La ligne de fond
Le coach garde les conversations. La Citadelle fait tout le reste — et ne parle à personne d'autre.

---
### Δ v1 → v2 (traçabilité)
Ajouté depuis le canon : la niche-intersection verrouillée + rejet médical/psy (NICHE-001) · le persona ratifié et ses chiffres exacts (Pilier 1) · le mantra « illusion de la complexité » + « Détention de Système » (Piliers 2-3) · la Killer Feature Zero-PII (Pilier 5) · la baseline 100 clients = 1,2 M$ ARR (NICHE-001 §D2) · le positionnement 3-ICP (Pilier 4). Conservé de v1 : les 4 fonctions, l'offre fondateur, le funnel, la démo.
**TODO landing (1 scrum Flash)** : injecter le mantra en hero-adjacent, renommer l'anti-objection données en « Zero-PII by design », vérifier zéro promesse santé/psy.
