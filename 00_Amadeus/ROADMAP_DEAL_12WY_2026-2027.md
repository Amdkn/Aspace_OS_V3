# ROADMAP D.E.A.L — 4 Cycles 12WY · 20/07/2026 → 20/07/2027

> **North Star H10** : $1B ARR — OMK BOS Nexus · ICP Coach premium · Produit AaaS de SOB à 1 000 $/mois par instance.
> **Fichier autonome, VPS-safe** : zéro import de doctrine, zéro gate, zéro flag. La cadence est le seul mécanisme.

## GOAL D.E.A.L (4HWW)

| | Définition |
|---|---|
| **D** | AaaS packagé OMK Nexus : hub clé en main (contenu + conformité + prospection) pour coachs premium. 1 000 $/mois/instance, expansion multi-tenant 150 $/mois/sous-segment. |
| **E** | Zéro validation humaine dans la boucle d'exécution. Zéro simulation. Le budget d'inférence va aux actions de conversion, rien d'autre. |
| **A** | Cascade Picard → Summers → 8 B2 → B3. SQL local (Supabase) = source de vérité. `next_week()` = pulsation. |
| **L** | Système lights-out : loops nocturnes, revenus récurrents, l'opérateur sort de l'opérationnel. |

## LES 4 CYCLES (dates réelles)

| Cycle | Fenêtre W1-W12 | W13 review | Thème | Cible MRR fin de cycle |
|---|---|---|---|---|
| **12WY-01 Fondations** | 20/07 → 11/10/2026 | 12-18/10 | Durcissement infra + premiers clients | **10 clients · $10K MRR** |
| **12WY-02 Prototype GTM** | 19/10/2026 → 10/01/2027 | 11-17/01 | Attaque Strate B US (30 comptes cibles) | **100 clients · $100K MRR** |
| **12WY-03 Multi-Tenant** | 18/01 → 11/04/2027 | 12-18/04 | Expansion RLS + viralité fondateurs | **1 000 clients · $1M MRR** |
| **12WY-04 Souveraineté** | 19/04 → 11/07/2027 | 12-18/07 | Franchise + R&D locale (réinvestissement) | **×10 + IP propriétaire** |

Échelle ×10 par cycle. Le milliard est l'asymptote H10 ; la trajectoire annuelle vit sur cette échelle.

## LES 3 ROCKS PAR CYCLE (Summers — 1 Rock/mois, métrique SQL observable)

### 12WY-01 Fondations (juillet-octobre)
| Rock | Moteur 3T | Livrable | Métrique de vérité |
|---|---|---|---|
| R1 (mois 1) | T1+T3 | Instance AaaS déployable en 1 commande (Docker + Supabase RLS) sur VPS | `SELECT count(*) FROM instances WHERE status='live'` ≥ 1 |
| R2 (mois 2) | T2 | Pipeline : 100 coachs contactés, 10 démos, 3 signés | `SELECT count(*) FROM subscriptions WHERE mrr>=1000` ≥ 3 |
| R3 (mois 3) | T3 | Onboarding automatisé + facturation récurrente sans intervention | `SELECT sum(mrr) FROM subscriptions WHERE status='active'` ≥ 10 000 |

### 12WY-02 Prototype GTM (octobre-janvier)
| Rock | Moteur 3T | Livrable | Métrique |
|---|---|---|---|
| R1 | T2 | 30 comptes Strate B US attaqués, 3 variants nichés live (Solaris Outbound · Nexus Conformité · Orbiter Sales-Enablement) | pipeline ≥ 30 comptes stage-aware |
| R2 | T1 | Templates d'exécution répliquables : 1 nouveau client provisionné < 1 h | `provisioning_time_p95 < 3600s` |
| R3 | T3 | Churn maîtrisé + expansion : NRR > 100 % | `SELECT churn_rate FROM cohorts` < 5 %/mois |

### 12WY-03 Multi-Tenant (janvier-avril)
| Rock | Moteur 3T | Livrable | Métrique |
|---|---|---|---|
| R1 | T1 | Isolation RLS par sous-compte, self-serve signup | sous-comptes actifs ≥ 200 |
| R2 | T2 | Boucle de referral fondateurs (viralité mesurée) | `viral_coefficient` ≥ 0.5 |
| R3 | T3 | Marge : coût d'inférence par client < 10 % du MRR | `SELECT avg(inference_cost/mrr) FROM unit_economics` < 0.10 |

### 12WY-04 Souveraineté (avril-juillet)
| Rock | Moteur 3T | Livrable | Métrique |
|---|---|---|---|
| R1 | T2 | Franchise : le playbook GTM vendable/licenciable à d'autres opérateurs | 1er contrat franchise signé |
| R2 | T3 | R&D : modèles locaux fine-tunés sur l'IP accumulée (indépendance API) | 1 workload prod migré local |
| R3 | T1+T3 | L'opérateur hors de la boucle : 4 semaines lights-out prouvées | `interventions_owner = 0` sur 28 jours |

## LA CADENCE (le métabolisme — descend puis remonte)

```
PICARD (A3)          1 vision/cycle    → décompose le cycle en 3 Rocks
   ▼
SUMMERS (B1)         1 Rock/mois       → traduit le Rock en directives par domaine
   ▼
8 B2 · 3T            4 Sprints/mois    → chaque manager tient le sprint de son domaine
   ▼
B3 SQUADS            5 Daily Scrums/sprint → exécution, receipts SQL
   ▲
UPLINK               5 scrums → 1 sprint review → 4 sprints → 1 Rock review
                     → 3 Rocks → 1 cycle review Picard → 4 cycles → bilan annuel
```

## LES 4 SPRINTS-TYPE DU MOIS (8 B2 × Triptyque V4)

| Sprint | T1 — RH Agentique · Operation · Product | T2 — Growth · Sales · Finance | T3 — Legal · R&D · Uplink |
|---|---|---|---|
| **S1 Build** | staffer agents du Rock · SOP du mois · feature AaaS prioritaire | liste de cibles fraîche · script d'approche · budget alloué | conformité de l'offre · veille (3 découvertes max) · prépa uplink |
| **S2 Push** | automatiser le répétitif détecté en S1 | outreach volume plein · démos bookées · relances auto | contrats types prêts · test découverte #1 |
| **S3 Close** | fiabiliser ce qui casse sous charge | closing · onboarding des signés · facturation | audit RLS/data des nouveaux clients |
| **S4 Harvest** | dette technique du mois purgée | métriques cohortes · NRR · pipeline du mois suivant | uplink consolidé → dossier Rock suivant pour Summers |

## LES 5 DAILY SCRUMS (B3 — chaque jour de sprint)

1. **Lire l'état** : requête SQL du domaine (pas de résumé narratif — le chiffre).
2. **1 action de conversion** : la tâche qui rapproche le MRR, en premier.
3. **1 action de système** : la tâche qui rend demain plus automatique.
4. **Receipt** : le delta SQL avant/après, loggé.
5. **Uplink 1 ligne** : au B2 du domaine. 5 lignes = matière du sprint review.

## RÈGLE UNIQUE

**Chaque niveau ne remonte que du chiffré.** Un scrum sans receipt SQL n'existe pas. Un sprint sans delta MRR/pipeline n'existe pas. Un Rock sans métrique atteinte se re-scope au mois suivant — la cadence, elle, ne s'arrête jamais.

---
*4 cycles. 12 Rocks. 48 sprints. 240 scrums. Départ : 20/07/2026. — A.S.*
