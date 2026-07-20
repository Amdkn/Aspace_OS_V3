# Cartographie L2 — B1 Summers → 8 B2 (Triptyque V4) → 53 B3 canon : la délégation exécutive complète

> **Le principe** : Summers COMMANDE (Rocks mensuels, Runbooks Gstack, Down-Link WF2) · les 8 B2 DISPATCHENT (jamais ne codent — Sprint Dispatchers) · les 53 B3 EXÉCUTENT (Daily Scrums, delta SQL). Délégation, pas création : un besoin détecté se ROUTE au squad compétent (Paperclipai « delegation not creation »).
> Roster = ADR-CANON-001 (source of truth). Missions = Triptyques V4 (W40). Terrain Cycle 1 = SOB coach premium (`sob/`, Runbooks C1-R1/R2/R3).

## 1. La chaîne de commandement

```mermaid
graph TD
    Summers["B1 SUMMERS (CEO Gstack)<br>1 Rock/mois · Runbook 1 page · forecast J+28<br>reçoit la vision de B1 Jerry (E-Myth) via WF2"]
    subgraph T1 [T1 BUILD — construire la machine]
        GL["B2 GreenLantern PEOPLE<br>RH Agentique · H10"]
        BA["B2 Batman OPS<br>SOP & Skills · H3"]
        FL["B2 Flash PRODUCT<br>Agency as a Service · H10"]
    end
    subgraph T2 [T2 VALUE — extraire la valeur]
        SU["B2 Superman GROWTH<br>AAARR · H3"]
        JJ["B2 JohnJones SALES<br>100M Offers · H1+H3"]
        WW["B2 WonderWoman FINANCE<br>1P-1B Company · H3"]
    end
    subgraph T3 [T3 FOUNDATION — protéger et découvrir]
        AQ["B2 Aquaman LEGAL<br>365 Conformité · H90"]
        CY["B2 Cyborg R&D (ex-IT)<br>Découverte externe · H10"]
    end
    Summers --> T1 & T2 & T3
    GL --> XMen["X-Men ×8"] ; BA --> F4["Fantastic Four ×4"] ; FL --> AV["Avengers ×7"]
    SU --> GotG["Guardians ×6"] ; JJ --> IL["Illuminati ×6"] ; WW --> TB["Thunderbolts ×6"]
    AQ --> ET["Eternals ×10"] ; CY --> KD["Kang Dynasty ×6"]
    XMen & F4 & AV & GotG & IL & TB & ET & KD -.->|uplink au score 5 scrums DoD-PASS| Summers
```

**Comptage canon** : 8+4+7+6+6+6+10+6 = **53 B3**. L'infra technique n'appartient plus à Cyborg (pivot R&D) — elle descend à L0 sous Rick (sovereignty ladder).

## 2. Statut Cycle 1 (la cadence est un droit gate-PASS, pas une obligation — W40)

| Domaine | Statut C1 | Cause / Déclencheur de réveil |
|---|---|---|
| Flash Product | 🟢 **ACTIF** | porte R1 (instance AaaS démontrable) |
| JohnJones Sales | 🟢 **ACTIF** | porte R2 (outreach → démos → closing) |
| Superman Growth | 🟢 **ACTIF** | porte R2 amont (liste 100, canaux, AAARR) |
| Batman Ops | 🟢 **ACTIF** | porte R3 (SOP onboarding) + SOP émergents des scrums |
| WonderWoman Finance | 🟡 SEMI | ledger + forecast + unit economics — 1 scrum/sprint suffit |
| Aquaman Legal | ⚪ DORMANT | réveil au **1er contrat coach à signer** (CGV, RGPD, DPA) |
| GreenLantern People | 🟢 **ACTIF** | **RH AGENTIQUE = configurer les agents des autres B2/B3** (correction 20/07 : People ≠ RH humaine — les X-Men sont le squad qui STAFFE, INSTRUIT et OUTILLE tous les autres squads, déchargeant Summers de la gestion d'agents) |
| Cyborg R&D | 🟡 SEMI | 1 sweep découverte/mois, **≤3 propositions actionnables** max |

## 3. La délégation exécutive — les 53 B3, domaine par domaine

### T1 · B2-03 Flash PRODUCT — mission « Agency as a Service » — squad AVENGERS (7) 🟢
**Specs de design OBLIGATOIRES** (D1 vérifié 20/07) : tout livrable visuel respecte **[ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** (107 902★ — 161 reasoning rules, 84 UI styles) + **[impeccable](https://github.com/pbakaus/impeccable)** (48 159★ — `npx impeccable install`, `/impeccable init` → PRODUCT.md+DESIGN.md, 23 commandes : polish/audit/critique/animate, 46 detector rules anti-template-AI). Périmètre : le produit AaaS ET les assets Growth — **landing pages, quiz d'audit simulés, flows d'onboarding**.
| B3 | Rôle canon | Délégation exécutive Cycle 1 (R1 + assets Growth) |
|---|---|---|
| **Captain America** (LEAD) | vision produit, intégrité de spec | tient l'Ownerbook R1 ; **fait tourner `/impeccable init` (PRODUCT.md + DESIGN.md = la spec de design du SOB)** ; arbitre chaque livrable contre les 2 skills |
| Iron Man | tech produit, premium UX | l'instance démo au niveau « screenshot vendable » — **auditée `/impeccable audit` + styles ui-ux-pro-max (zéro tell AI : pas d'Inter-partout, pas de gradient violet-bleu, pas de cards-dans-cards)** |
| Thor | flagship, premium tiers | le paquet 1000 $/mois : ce que le coach VOIT — **la landing page de l'offre (design specs appliquées)** |
| Hulk | stress test, scale | casser l'instance : re-runs, données volumineuses, 2 instances en parallèle |
| Black Widow | intel concurrentielle, rétention | 3 AaaS/outils concurrents analysés → 1 page « pourquoi nous » |
| Hawkeye | traçabilité des specs | chaque sortie Runbook R1 a son receipt SQL ; **chaque asset visuel a son verdict audit design loggé** |
| Scarlet Witch | chaos engineering | les cas tordus + **le QUIZ D'AUDIT simulé** (l'asset Growth : le coach répond à 8 questions → son diagnostic → la démo) et le flow d'onboarding |

### T2 · B2-05 JohnJones SALES — mission « 100M Offers » — squad ILLUMINATI (6) 🟢
| B3 | Rôle canon | Délégation exécutive Cycle 1 (R2) |
|---|---|---|
| **Black Bolt** (LEAD) | closing complexe, silence-as-power | tient le pipeline ; dispatch ; ferme les démos (les 3 premiers signés) |
| Tony Stark | tech sales, comptes premium | le script de démo (instance live → valeur en 15 min) |
| Charles Xavier | mapping mental de l'acheteur | par prospect : le détail spécifique + l'angle du message personnalisé |
| Stephen Strange | deals internationaux | fuseaux/langues du batch US + variantes d'approche par géo |
| Namor | distribution, wholesale | canaux indirects : communautés de coachs, certifs ICF, podcasts |
| Reed Richards | pipeline d'innovation | l'offre Hormozi : valeur×certitude ÷ délai×effort — la page d'offre irrésistible |

### T2 · B2-04 Superman GROWTH — mission « AAARR » — squad GUARDIANS OF THE GALAXY (6) 🟢
| B3 | Rôle canon | Délégation exécutive Cycle 1 (R2 amont) |
|---|---|---|
| **Star-Lord** (LEAD) | top funnel, narrative | le hook : 1 phrase qui fait ouvrir le message d'un coach mid-tier |
| Gamora | tuer les mauvais canaux | après 50 envois : couper les canaux à 0 réponse (receipt outreach_log) |
| Rocket | analytics expérimentales | le tracking canal×segment dans `experiments` (l'allocation-efficiency CEO-BENCH) |
| Groot | evergreen, rétention lente | le contenu qui travaille seul : 1 asset/mois (article, template public) |
| Drax | A/B littéral, sans subtilité | 2 variantes de message, comptage brut des réponses, verdict mécanique |
| Mantis | empathie d'onboarding | les 10 conversations découverte/mois (source='research', non-vendantes) |

### T1 · B2-02 Batman OPS — mission « SOP & Skills » — squad FANTASTIC FOUR (4) 🟢
**Le pendant reproductible de la RH Agentique** : les X-Men CONFIGURENT (créent la config d'un agent), les F4 la rendent REPRODUCTIBLE (template + script — la 2e configuration ne se refait jamais à la main). C'est la boucle T1 : GreenLantern invente, Batman industrialise, Flash productise.
| B3 | Rôle canon | Délégation exécutive Cycle 1 (R3 + transverse) |
|---|---|---|
| **Mr Fantastic** (LEAD) | process élastiques | cartographie l'onboarding manuel des 3 premiers clients → le SOP émerge du réel ; **idem pour les configs X-Men : 2e config d'agent similaire = template** |
| Invisible Woman | privacy ops, incidents | les données coach cloisonnées (instance isolée) + réponse incident 1 page |
| Human Torch | hot fixes, déploiement urgent | le scrum de réparation quand un E.2 dépasse 3 retries |
| The Thing | process porteurs, durabilité | ce qui a marché 2× devient script (`tools/`) — **y compris les configs RH Agentique (template d'instruction, memory file type, checklist de staffing d'agent)** |

### T2 · B2-07 WonderWoman FINANCE — mission « 1-Person/1-Billion Company » — squad THUNDERBOLTS (6) 🟡
| B3 | Rôle canon | Délégation exécutive Cycle 1 (1 scrum/sprint) |
|---|---|---|
| **Bucky Barnes** (LEAD) | runway, résilience hiver | la vue `daily_cash` lue chaque sprint ; plancher 2 mois de burn surveillé |
| Yelena Belova | pricing affûté, unit econ | coût réel par client (tokens+infra) vs 1000 $ — la marge par tête |
| Ghost | actifs intangibles | l'IP qui s'accumule (Runbooks, templates) valorisée au bilan du cycle |
| Red Guardian | capex lourd, réserves | le budget VPS/outils : rien ne s'achète avant le déclencheur client |
| Taskmaster | CAC miroir, anti-pattern billing | coût d'acquisition par canal depuis ledger×outreach_log |
| U.S. Agent | conformité comptable | chaque € entré/sorti a sa ligne ledger — auditable en 1 query |

### T3 · B2-08 Aquaman LEGAL — mission « 365 Conformité par Conception » — squad ETERNALS (10) ⚪
| B3 | Rôle canon | Délégation au réveil (1er contrat à signer) |
|---|---|---|
| **Ikaris** (LEAD) | AI-Act lead | le pack conformité minimal : mentions IA, AI-Act applicable à l'AaaS |
| Sersi | alchimie contractuelle | LE contrat type coach (1000 $/mois, résiliable, IP claire) |
| Ajak | communion compliance | RGPD/DPA : registre + droits d'accès pour les données coach |
| Kingo | IP entertainment | le contenu généré pour le coach : qui possède quoi |
| Phastos | brevets/IP tech | l'IP des tools (`sob.py`, templates) : licence et protection |
| Sprite | narratif de responsabilité | disclaimers : l'AaaS assiste, le coach reste l'auteur |
| Druig | zones grises | ce qu'on ne PEUT PAS promettre (résultats clients, revenus) |
| Thena | clauses de guerre | indemnisation, limitation de responsabilité, litiges |
| Gilgamesh | gouvernance souveraine | la structure juridique porteuse (auto-entreprise → société, au seuil) |
| Makkari | recherche rapide | précédents et modèles : 1 h max par question, cite ses sources |

### T1 · B2-01 GreenLantern PEOPLE — mission « RH Agentique » — squad X-MEN (8) 🟢
**Le squad qui configure tous les autres.** RH Agentique = Harness Engineering + Context Engineering + Prompt Engineering des agents eux-mêmes. C'est lui qui décharge Summers : quand un domaine a besoin d'un agent (instructions, memory file, skill, accès), la demande va aux X-Men — jamais au CEO.
| B3 | Rôle canon | Délégation exécutive Cycle 1 (ACTIVE) |
|---|---|---|
| **Professor X** (LEAD) | stratégie, éthique | arbitre QUELLE configuration manque vraiment (anti-usine) ; tient le registre des agents configurés vs dormants |
| Cyclops | leadership tactique | **écrit les délégations exécutables** : chaque B3 actif a son instruction 1-page (rôle, Runbook source, format d'uplink) — ce document est son template |
| Jean Grey | résolution de conflits | frontières entre squads : 2 domaines sur la même tâche → 1 ligne de partage ; harmonise les formats d'uplink |
| Wolverine | profils difficiles | configure les agents des tâches ingrates : relances froides, nettoyage de données — et vérifie qu'ils tournent |
| Storm | culture, ton | **la voix du système** : prompts de messages sortants (outreach R2) relus — humain, pas robot ; 1 échantillon/sprint |
| Beast | L&D, rigueur | **la formation des agents** : les leçons des RUN_LOGs distillées dans les memory files et les prompts (l'agent du Run N+1 est plus intelligent) |
| Nightcrawler | mobilité | réaffectation : un agent/harness sous-utilisé (Multica idle, session morte) se re-route vers le squad qui déborde |
| Rogue | transfert de savoir | **anti-single-point** : tout savoir critique détenu par 1 seule config d'agent est copié dans un Runbook/template (le système survit à la perte de n'importe quel agent) |

### T3 · B2-06 Cyborg R&D — mission « Découverte externe » — squad KANG DYNASTY (6) 🟡
| B3 | Rôle canon | Délégation exécutive (1 sweep/mois, ≤3 propositions) |
|---|---|---|
| **Kang Prime** (LEAD) | architecture prime | arbitre les découvertes : max 3 candidats Rock remontés à Summers |
| Victor Timely | frontier civique | le sweep Last30days : nouveaux outils/repos/releases pertinents AaaS-coach |
| Iron Lad | greenfield véloce | prototype 1 découverte prometteuse en 1 scrum (jetable, prouvable) |
| Scarlet Centurion | pipelines alternatifs | teste l'alternative (autre canal, autre stack) en parallèle borné |
| Immortus | dépréciation long-horizon | ce qui doit MOURIR : outils/process obsolètes → liste de retrait |
| Rama-Tut | archéologie de code | ce que le disque contient DÉJÀ qui résout le besoin (avant tout achat) |

## 4. Les règles de délégation (les seules)

1. **Le LEAD dispatch, les membres exécutent.** Un LEAD qui exécute = un domaine sans dispatcher (signal WF1).
2. **Un B3 reçoit sa tâche du Runbook via son LEAD** — jamais en direct de Summers ni d'un autre domaine (le canal RH GreenLantern route les besoins inter-domaines).
3. **Un B3 dormant DORT** (règle des dormants, carte A3) : les Eternals ne produisent rien tant qu'aucun contrat n'est à signer. Zéro travail inventé.
4. **L'uplink monte au score** : 5 scrums DoD-PASS = sprint review du B2 → 4 sprints = dossier Rock pour Summers. Contre-exemples [E-type + ID SQL], jamais un PASS/FAIL sec.
5. **Besoin hors-domaine détecté en scrum** → route par la matrice RH : Skills/SOP → Batman F4 · produit → Flash Avengers · legal → Aquaman Eternals · découverte → Cyborg Kang. On ne crée pas, on route.

## 5. Scellé (state.json)

```json
{
  "layer": "L2_COMMAND_CHAIN", "topology_version": "3.1.FINAL",
  "b1": { "ceo": "SUMMERS_GSTACK", "vision": "JERRY_EMYTH", "canal": "WF2_97d332d5" },
  "b2": { "t1_build": ["greenlantern_people","batman_ops","flash_product"],
          "t2_value": ["superman_growth","johnjones_sales","wonderwoman_finance"],
          "t3_foundation": ["aquaman_legal","cyborg_rd"] },
  "b3_total": 53,
  "squads": { "xmen": 8, "f4": 4, "avengers": 7, "gotg": 6, "illuminati": 6, "thunderbolts": 6, "eternals": 10, "kang": 6 },
  "cycle1_gates": { "actifs": ["people","product","sales","growth","ops"], "semi": ["finance","rd"], "dormants": ["legal"] },
  "rule": "le LEAD dispatch, le membre execute, le dormant dort, l'uplink monte au score"
}
```

---
*Summers commande, 8 managers dispatchent, 53 exécutants livrent — et 4 domaines seulement sont éveillés, parce que le Cycle 1 n'a besoin que d'eux. La hiérarchie complète existe pour le jour où le MRR la remplira. — A.S. 2026-07-20*
