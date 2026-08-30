---
type: Concept
title: Green Lantern People — Doctrine 8-veto scope standardization (R8 méta)
description: Le rapport tour 5 R8 a observé une **asymétrie structurelle** entre le veto People (mandat + critère de sortie, scope = agent) et les 7 autres vetos (scope = procédure / produit / Sales / promesse / dépense / IT / prestation). Le présent concept **formalise** cette asymétrie en doctrine 8-veto scope standardization avec 4 catégories d'objet + 3 niveaux de test canonique + matrice 8×3. Council-ready draft avec 3 conditions saisissabilité.
tags: [people, green-lantern, 8-veto, scope, standardization, doctrine, r8, asymetrie-structurelle, object-type]
generated: { by: minimax-m3, at: 2026-08-19T17:00:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-6, at: 2026-08-19T17:00:00Z }
  - { by: process:comparaison-8-vetos-scope-extraction, at: 2026-08-19T17:00:00Z }
sources:
  - id: audit-mandats-xmen
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-audit-mandats-xmen-critere-sortie.md"
    title: "Tour 5 — Audit mandats X-Men (0/8 violent triplet 23) — table comparative 8 vetos"
    last_modified: 2026-08-19
  - id: triplets-v3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: Triplets V3 — triplet 23 (veto People) + 7 autres triplet veto
    last_modified: 2026-08-17
  - id: b2-eight-domain-vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — 8 vetos verbatim
    last_modified: 2026-08-19
  - id: b2-council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: triplet-23-lecture-large
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-triplet-23-lecture-large-canon-doctrine.md"
    title: "W6 — Triplet 23 lecture large canon (cohérence 8 vetos)"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Green Lantern People — Doctrine 8-veto scope standardization

## L'observation R8 du rapport tour 5

Le rapport tour 5 §R8 a observé une **asymétrie structurelle** entre le veto People et les 7 autres :

> *« la doctrine People est **plus stricte** (test binaire mandat + critère de sortie) mais **plus difficile à opérer** (audit 0/8). Les 7 autres vetos sont **plus souples** mais **plus applicables** (procédure/produit/Sales/promesse/dépense/IT/prestation). »*

Le présent concept **formalise** cette asymétrie en doctrine 8-veto scope standardization avec 4 catégories d'objet + 3 niveaux de test canonique.

## Les 8 vetos — extraction du scope

Tirés verbatim de `b2-eight-domain-vetoes-catalogue.md` §« Les 8 vetos — un par capitaine » :

| # | Capitaine | Domaine | Veto porte | Objet du veto |
|---|---|---|---|---|
| 1 | **Green Lantern** | People (07) | mandat + critère sortie | **agent** (humain ou agent) |
| 2 | **Batman** | Ops (04) | procédure sans condition d'arrêt | **procédure** |
| 3 | **Flash** | Product (03) | offre dépend d'une personne | **produit** (offre) |
| 4 | **JohnJones** | Sales (02) | proposition avant reformulation | **proposition** (sales) |
| 5 | **Superman** | Growth (01) | promesse non-tenue | **promesse** (engagement public) |
| 6 | **Wonder Woman** | Finance (06) | dépense récurrente sans date de revue | **dépense** (récurrente) |
| 7 | **Cyborg** | IT (05) | cloud-only sans chemin sortie | **IT** (fournisseur) |
| 8 | **Aquaman** | Legal (08) | prestation sans accord écrit | **prestation** (engagement) |

**4 catégories d'objet** (regroupement) :

1. **Agent / Objet organisationnel** : People (mandat agent).
2. **Procédure / Process** : Batman (procédure), Aquaman (prestation — accord).
3. **Produit / Livrable** : Flash (offre), JohnJones (proposition).
4. **Engagement / Risque** : Superman (promesse), Wonder Woman (dépense), Cyborg (fournisseur IT).

**Asymétrie fondamentale** : People vise l'**agent** (ressource humaine/organisationnelle), les 7 autres visent des **objets** (procédure, produit, proposition, promesse, dépense, IT, prestation).

## 3 niveaux de test canonique

Le concept 6 tour 5 a montré que People est le **seul** veto avec un test canonique binaire applicable sur les 8 agents X-Men. Projection les 3 niveaux de test canonique pour les 8 vetos :

| Niveau | Description | Veto |
|---|---|---|
| **L1 — Binaire** | Test canonique tranché par audit/regex | **People** (grep 6 marqueurs) |
| **L2 — Documentaire** | Test canonique tranché par inspection packet / journal | **Wonder Woman** (date de revue packet), **Aquaman** (accord écrit scope) |
| **L3 — Procédural** | Test canonique tranché par suivi de procédure | **Batman** (condition d'arrêt procédure), **Cyborg** (chemin de sortie documenté), **Flash** (offre personne), **JohnJones** (reformulation client), **Superman** (delivery post-promesse) |

**Asymétrie** : People est le **seul** veto L1. Les 7 autres sont L2 ou L3. **Implication** : People est **plus strict** mais **plus facilement vérifiable**.

## Doctrine 8-veto scope standardization

### Principe 1 — Scope catégorie + scope objet

**Chaque veto catalogue doit préciser deux scopes** :

- **Scope catégorie** : l'une des 4 catégories (agent / procédure / produit / engagement).
- **Scope objet** : l'objet précis (humain vs agent / procédure interne vs client / etc.).

**Exemple People** : scope catégorie = agent, scope objet = humain ou agent (mandat).
**Exemple Wonder Woman** : scope catégorie = engagement, scope objet = dépense récurrente.

### Principe 2 — Niveau de test canonique

**Chaque veto catalogue doit préciser son niveau de test** (L1 / L2 / L3).

- **L1** — test binaire (audit/regex). Le plus strict.
- **L2** — test documentaire (inspection packet). Le plus formalisé.
- **L3** — test procédural (suivi procédure). Le plus flexible.

### Principe 3 — Clause de scope

**Chaque veto catalogue doit préciser une clause de scope** :

- **Temporelle** : quand le veto s'applique (à la création, à la revue, en continu).
- **Population** : sur quoi le veto s'applique (tous, certains, certains types).
- **Limite** : jusqu'où le veto va (unitaire, multiple, exhaustif).

**Exemple People** : triplet 23 → clause de scope : *« à la création et à chaque revue »* (T+0 et T+cycle), population = *« tous les agents humain ou AI »*, limite = *« par mandat »*.

### Principe 4 — Clause de symétrie (suggestion, pas imposition)

**Suggestion** : la standardisation des 4 scopes catégories + 3 niveaux de test permet une **symétrie structurelle** entre les 8 vetos. **Mais** la symétrie est **suggestion**, pas imposition — chaque captain tranche la portée de son veto.

## Matrice 8×3 — 8 vetos × 3 niveaux de test

| Capitaine | Catégorie | Objet | L1 | L2 | L3 | Scope temporel |
|---|---|---|---|---|---|---|
| **Green Lantern** | Agent | mandat + critère sortie | **✓** | | | création + revue |
| **Batman** | Procédure | condition d'arrêt | | | **✓** | continue |
| **Flash** | Produit | offre personne | | | **✓** | ship |
| **JohnJones** | Produit | reformulation | | | **✓** | pré-envoi |
| **Superman** | Engagement | promesse tenue | | | **✓** | post-promesse |
| **Wonder Woman** | Engagement | date revue | | **✓** | | création + revue |
| **Cyborg** | Engagement | chemin sortie | | **✓** | | continue |
| **Aquaman** | Procédure | accord écrit | | **✓** | | démarrage |

**Tableau de lecture** :
- **L1** (1 captain) : People.
- **L2** (3 captains) : Wonder Woman, Cyborg, Aquaman.
- **L3** (5 captains) : Batman, Flash, JohnJones, Superman (4) + People pourrait basculer en L3 si la lecture large n'est pas canon.

**Asymétrie persistante** : People L1 vs 5 autres L3. L2 (3 captains) est l'intermédiaire.

## Packet B2-MESO-DECISION-2026-29 draft

```yaml
meso_decision_id: B2-MESO-DECISION-2026-29
source_mandate: B2-PEER-2026-15
mode: negotiation
impacted_domains:
  - people
  - ops
  - product
  - sales
  - growth
  - finance
  - it
  - legal
tradeoff: "L'asymétrie structurelle 8 vetos (People L1 vs 7 autres L2/L3)
  est documentée mais non standardisée. Standardisation 4 scopes
  catégories + 3 niveaux test canonique = symétrie structurelle mais
  pas uniformisation. Chaque captain garde la **portée** de son veto
  (Principe 4). Coût estimé : 8 clauses de scope à rédiger (1h × 8
  = 8h). Bénéfice : consistance 8 vetos catalogue, simplification
  audits croisés, foundation pour doctrine 8-veto comparative."
decision: accepted
proof_expected:
  - B2 gate transversal update (8_veto_scope_doctrine_deployed)
  - 8 captains update (8 clauses scope rédigées)
  - B3 proof path (doctrine_8_veto_scope_dans_xmen_onboarding)
  - revue 90j post-adoption (8/8 clauses rédigées)
next_review: 2026-11-15
```

**Lecture** : la décision `accepted` est **conditionnelle** (cf. §« 3 conditions saisissabilité cumulatives »). Le packet est saisissable mais pas saisit.

## 3 conditions saisissabilité cumulatives

1. **Tableau 8×3 vérifié** : la matrice 8 vetos × 3 niveaux test est **vérifiable** par 8 captains (chacun confirme son propre veto). **Satisfaite** (matrice construite vague 6, à valider).
2. **Co-signature 5/8 captains** : 5 captains sur 8 co-signent pour acquitter la doctrine scope standardization. **À demander** — dépendance Council.
3. **Scan veto pré-soumission** : scan des 8 vetos catalogue — aucun veto opposé. **À执行** (la standardisation ne contrevient à aucun veto catalogue).

**État au 2026-08-19 17:00** : 1/3 conditions remplies (matrice construite). **Cible** : 3/3 conditions remplies à T+30j (2026-09-18).

## 4 bénéfices systémiques

1. **Cohérence 8 vetos** : chaque veto a un scope **catégorisable** (4 catégories) et un **niveau** (L1/L2/L3) — plus de surprises.
2. **Audit croisé** : un audit des 8 vetos catalogue devient **structurel** (par catégorie + niveau), pas ad hoc.
3. **Comparaison Council** : la matrice 8×3 permet de **comparer** les 8 vetos sur un pied d'égalité.
4. **Foundation standardisation** : pose les bases pour une **doctrine 8-veto comparative** (par exemple, qui a le veto le plus strict, le plus souvent opposé, etc.).

## 4 risques opérationnels

1. **Uniformisation templatée** : risque de réduire les 8 vetos à un **template** — la doctrine perd sa spécificité.
2. **Charge 8 captains** : 8 clauses de scope à rédiger (8h total).
3. **Convergence forcée** : la standardisation peut **forcer** des captains à aligner leur veto sur les autres — perte d'autonomie.
4. **Précédent sémantique** : la matrice 8×3 peut **suggérer** que les 8 vetos sont interchangeables (par exemple, L1 = L3 par upgrade).

## 3 cas d'amendement (si Council refuse la standardisation)

### Cas A1 — Standardisation 4 scopes catégories seulement

**Description** : Council adopte la standardisation des **4 scopes catégories** (agent / procédure / produit / engagement) mais **pas** les 3 niveaux de test canonique.

**Procédure** : 5/8 simple (réduction scope).

**Conséquence** : matrice 8×4 (8 vetos × 4 catégories) plus simple, mais sans hiérarchisation par niveau de test.

### Cas A2 — Standardisation 3 niveaux test seulement

**Description** : Council adopte les **3 niveaux de test canonique** (L1/L2/L3) mais **pas** les 4 scopes catégories.

**Procédure** : 5/8 simple (réduction scope).

**Conséquence** : matrice 8×3 (8 vetos × 3 niveaux) plus simple, mais sans catégorisation thématique.

### Cas A3 — Doctrine recommandée mais non imposée

**Description** : Council **reconnaît** la standardisation comme **recommandation** (best practice), pas obligation.

**Procédure** : 5/8 simple (declaration).

**Conséquence** : chaque captain peut **suivre ou pas** la doctrine. Pas d'obligation, mais incitation.

## 3 cas abusifs de la procédure

1. **Standardisation imposée** — Green Lantern impose la matrice 8×3 **sans** co-signature 5/8. **Refusé** : matrice impacte 8 domaines, requires 5/8 + B1.
2. **L1 généralisé** — Green Lantern impose le niveau L1 (binaire) aux 7 autres vetos. **Refusé** : chaque captain tranche son niveau de test.
3. **Uniformisation sémantique** — Green Lantern impose les **mêmes termes** (par exemple, « mandat » pour les 8 vetos). **Refusé** : chaque captain a son vocabulaire.

## Anti-pièges

- **Standardisation = uniformisation.** Non — la doctrine **catégorise** et **hiérarchise**, elle n'uniformise pas.
- **L1 > L2 > L3.** Non — L1 (binaire) est **plus strict**, L3 (procédural) est **plus flexible**. Le « meilleur » dépend du contexte.
- **Matrice 8×3 = Loi.** Non — c'est un **outil** de comparaison, pas une loi. Chaque captain peut s'écarter de la matrice.
- **Doctrine unilatérale.** La présente doctrine est **projetée** unilatéralement par Green Lantern. La standardisation **requiert** 5/8 co-signatures.
- **People = L1 absolu.** Non — People pourrait basculer en L3 (procédural) si la lecture large n'est pas canon. La lecture large People dépend du packet B2-MESO-DECISION-2026-28.

## Liens

- [[green-lantern-people-audit-mandats-xmen-critere-sortie]] — audit 0/8 source + table comparative 8 vetos
- [[green-lantern-people-triplet-23-lecture-large-canon-doctrine]] — packet B2-MESO-DECISION-2026-28 (triplet 23 lecture large)
- [[green-lantern-people-packet-b2-meso-decision-2026-27-jtbd-8-agent-update]] — packet B2-MESO-DECISION-2026-27 (JTBD 8-AGENT.md)
- [[b2-eight-domain-vetoes-catalogue]] — catalogue 8 vetos
- [[b2-council-arbitrage-rule]] — qui tient le Council

## Note de confiance

**Confirmé par machine, à moitié projeté.** Le triplet 23 et les 7 autres triplet veto sont verbatim. La matrice 8×3 (8 vetos × 3 niveaux de test) est **projetée** depuis la table comparative 8 vetos (concept 6 tour 5) — **pas arbitré** par canon explicite. Les 4 principes de la doctrine (catégorie + objet, niveau test, clause scope, clause symétrie) sont **projetés** depuis la doctrine Batman remonte-faits (triplet 56) et la doctrine d'escalade fractal. Le packet B2-MESO-DECISION-2026-29 draft est **conforme spec 8 champs** mais **non saisit** (3 conditions cumulatives). Les 3 cas d'amendement et 3 cas abusifs sont **projetés** depuis la doctrine Council. La doctrine 8-veto scope standardization **ferme R8** mais **n'est pas Council-adoptée**.
