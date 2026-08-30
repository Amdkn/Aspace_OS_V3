---
type: Concept
title: People — protocole de validation empirique 3 cas / 60 jours sur les concepts tour 2
description: Le tour 2 a posé 6 concepts OKF — méta gouvernance, formule de charge, lag indicator succession, seuil vacance tolérable, dormance vs attente, co-sponsorat People × Brand — qui sont tous des **projections** depuis la doctrine existante. Le présent concept pose un **protocole de validation empirique** : cible 3 cas / 60 jours sur l'ensemble des 6 concepts, 5 critères d'acceptance par cas, 3 indicateurs de couverture / distribution / vitesse, conditions de mise à jour de la doctrine (confirmée / amendée / invalidée), et procédure d'observation Council-ready. Le protocole est **non destructif** : il observe sans modifier la doctrine existante.
tags: [people, green-lantern, validation-empirique, protocole, doctrine, 60-jours, b2, council, observation]
generated: { by: minimax-m3, at: 2026-08-19T06:45:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-3, at: 2026-08-19T06:45:00Z }
sources:
  - id: meta-gouvernance-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-meta-gouvernance-skills-l0.md"
    title: "Tour 2 — People × IT × Forge — Méta Gouvernance"
    last_modified: 2026-08-19
  - id: formule-charge-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-formule-charge-carte.md"
    title: "Tour 2 — People formule de calcul de charge"
    last_modified: 2026-08-19
  - id: lag-indicator-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-lag-indicator-succession.md"
    title: "Tour 2 — People lag indicator succession"
    last_modified: 2026-08-19
  - id: seuil-vacance-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-seuil-vacance-tolerable.md"
    title: "Tour 2 — People seuil vacance tolérable"
    last_modified: 2026-08-19
  - id: dormance-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-dormance-attente-active.md"
    title: "Tour 2 — People dormance vs attente vs actif"
    last_modified: 2026-08-19
  - id: brand-co-sponsorat-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-brand-co-sponsorat-superman.md"
    title: "Tour 2 — People × Brand co-sponsorat"
    last_modified: 2026-08-19
  - id: flash-empirical-validation-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-veto-empirical-validation-protocole.md"
    title: "Flash — protocole de validation empirique 3 cas / 60 jours"
    last_modified: 2026-08-19
  - id: superman-empirical-validation-tour-3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-veto-empirical-validation-protocole.md"
    title: "Superman — protocole de validation empirique 3 cas / 60 jours"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# People — protocole de validation empirique 3 cas / 60 jours sur les concepts tour 2

## Le constat — 6 concepts posés, 0 cas observé

Le tour 2 de l'escouade Green Lantern a posé 6 concepts OKF v0.2,
chacun traitant un gap canonique identifié en tour 1 :

1. `meta-gouvernance-skills-l0.md` — 3 lectures + 4 critères de tri.
2. `formule-charge-carte.md` — formule `C(o) = Σ poids / capacité` + 3 modes + 3 seuils (0.7 / 1.0 / 1.3).
3. `lag-indicator-succession.md` — 3 indicateurs (délai médian, taux bouclage, taux rollback 90j) + grille par type.
4. `seuil-vacance-tolerable.md` — grille criticité × horizon 14/30/45/60/90/120j + procédure 3 étages.
5. `dormance-attente-active.md` — tri-état DORMANT / EN ATTENTE / ACTIF + sous-état People × IT permanent.
6. `brand-co-sponsorat-superman.md` — 3 modes A/B/C + 3 triggers d'arbitrage + format `brand_specific`.

**Mais** : aucun de ces 6 concepts n'a été **observé en cycle réel**.
Le rapport tour 2 l'admet explicitement : *« les 6 concepts n'ont pas
été testés les uns contre les autres. »* Et le bilan vague 2 signale
*« 0 packet mésoperpétuel People enregistré en vague 2 (convergence
8/8 domaines Batman/Aquaman/WW/Superman/Flash/GL/JJ/Cyborg) »*.

C'est le **risque d'inertie** : 6 concepts **posés** mais pas
**vérifiés**, qui peuvent rester lettre morte jusqu'à ce qu'un cycle
les invalide implicitement (par exemple, un People en DORMANCE
permanente qui n'a jamais appliqué la tri-état).

Le présent concept pose un **protocole de validation empirique** —
une cible chiffrée, des critères mesurables, des indicateurs de
suivi, et des conditions de mise à jour de la doctrine.

## La cible — 3 cas / 60 jours

L'objectif chiffré : **observer au moins 3 cas réels** sur
l'ensemble des 6 concepts tour 2, dans une **fenêtre de 60 jours**.

**Pourquoi 3 cas** : c'est le minimum pour distinguer un pattern
d'un bruit. 1 cas = anecdote, 2 cas = début de pattern, 3 cas =
pattern confirmé. C'est la convention OMK / Ownerbook T1 (cf. DoD-1
*« verify ≥ 7 agents par squad »* — la vérification se fait sur
plusieurs cas, pas un seul).

**Pourquoi 60 jours** : c'est ~1 cycle 12WY / 2, soit la moitié
d'un trimestre. Une fenêtre plus courte (30 jours) rate les cas
lents (succession, dormance). Une fenêtre plus longue (90 jours)
**perd** la réactivité — les concepts peuvent dériver pendant
l'observation.

**Sur quoi compter les 3 cas** : tout **événement** où un des 6
concepts est **appliqué** ou **référencé** dans un arbitrage réel :

- Une sollicitation Forge tranchée par la tri-état People (concept
  #5).
- Un calcul de charge `C(o)` produit par People pour un arbitrage
  Council (concept #2).
- Un lag indicator succession produit après un départ (concept #3).
- Un escalade de vacance à 1 des 3 étages (concept #4).
- Une décision de co-sponsorat People × Brand prise en A, B, ou C
  (concept #6).
- Une demande de Méta Gouvernance tranchée par les 3 lectures (concept
  #1).

**3 cas sur 6 concepts**, c'est une cible **distribuée**, pas
**concentrée**. Le protocole accepte 1 cas par concept (3 cas sur
3 concepts différents) ou 3 cas sur 1 seul concept. La distribution
sera mesurée par l'indicateur **distribution** (cf. §« Les 3
indicateurs »).

## Les 5 critères d'acceptance par cas

Pour qu'un cas compte dans la cible 3/60j, il doit remplir **5
critères cumulatifs** :

### Critère 1 — Cas réel, pas projeté

Le cas doit être **observé** dans un arbitrage Council, un journal
People, un packet mésoperpétuel, ou un sprint B3 X-Men. Un cas
**projeté** (par exemple, *« si Storm part, Gambit reprendrait son
poste »*) ne compte pas — c'est une projection, pas un cas.

### Critère 2 — Concept explicitement référencé

Le cas doit **référencer** explicitement le concept tour 2 (par son
titre ou son numéro dans le dossier `green-lantern/`). Une
application **implicite** (par exemple, People passe en
EN_ATTENTE sans citer le concept #5) ne compte pas — le protocole
veut tester **les concepts**, pas seulement les pratiques.

### Critère 3 — Issue tranchée ou refus motivé

Le cas doit avoir une **issue** tranchée (mode parallel/handoff/
negotiation choisi) ou un **refus motivé** (par exemple, *« le
co-sponsorat Mode A est refusé car People n'a pas de sponsor Brand
»*). Un cas **sans issue** (par exemple, *« la vacance dure depuis
45 jours, pas d'escalade »*) compte **seulement** si le motif de
non-escalade est documenté — c'est un cas de **non-application** qui
a autant de valeur qu'un cas d'application.

### Critère 4 — Documenté en format canonique

Le cas doit être documenté en format **Council-ready** :
`meso_decision_id`, `mode`, `impacted_domains`, `decision`, et
référence explicite au concept source. Un cas **non documenté** est
un cas **non-valide** pour le protocole.

### Critère 5 — Au moins un capitaine B2 **autre que Green Lantern** est témoin

Le cas doit impliquer au moins un capitaine B2 **autre que Green
Lantern** (Batman Ops typiquement, ou Cyborg IT). Un cas **purement
People interne** (par exemple, People en DORMANT sans impact sur un
autre domaine) ne compte pas — le protocole teste les
**interactions inter-domaines**, pas les états People seuls.

## Les 3 indicateurs de suivi

### Indicateur 1 — Couverture

**Définition.** Ratio du nombre de concepts **testés** (au moins 1
cas) sur le nombre total de concepts tour 2 (6).

**Cible** : ≥ 50% après 60 jours (≥ 3 concepts sur 6 testés).

**Calcul** : `couverture = concepts_testés / 6`.

### Indicateur 2 — Distribution

**Définition.** Écart-type du nombre de cas par concept testé.

**Cible** : ≤ 1.5 (distribution raisonnable — pas 3 cas sur 1 seul
concept, pas 1 cas sur 3 concepts).

**Calcul** : `distribution = std_dev(cas_par_concept)`. Si
distribution > 1.5, le protocole signale une **concentration**
excessive.

### Indicateur 3 — Vitesse

**Définition.** Délai médian (en jours) entre le **besoin** (par
exemple, un owner part) et l'**application** du concept (par
exemple, le lag indicator succession est produit).

**Cible** : ≤ 14 jours (2 semaines) pour 80% des cas.

**Calcul** : `vitesse = median(délai_application - délai_besoin)`.

## Les 3 conditions de mise à jour de la doctrine

À la fin de la fenêtre 60 jours, **3 issues possibles** pour chaque
concept testé :

### Condition 1 — Doctrine confirmée

**Critère** : ≥ 3 cas observés, **tous** cohérents avec le concept,
**aucun** cas contradictoire.

**Action** : le concept passe de *« projection »* à *« doctrine
confirmée »*. Le frontmatter `verified` est mis à jour avec un
acteur `human:` (un B1 ou B2 humain qui confirme). Le concept est
**ajouté au canon** par append-only dans le dossier source.

### Condition 2 — Doctrine amendée

**Critère** : ≥ 3 cas observés, **majorité** cohérente mais ≥ 1 cas
**contradictoire** identifié.

**Action** : le concept est **amendé** pour intégrer le cas
contradictoire. Un concept amendé garde son titre, mais son corps
est **réécrit** (pas append-only — c'est une révision, pas un
ajout). La date d'amendement est consignée. Le concept amendé est
**re-soumis** au Council pour validation.

### Condition 3 — Doctrine invalidée

**Critère** : ≥ 3 cas observés, **majorité** contradictoires avec
le concept.

**Action** : le concept est **invalidé**. Le fichier concept est
**marqué** `status: invalidated` dans son frontmatter, mais
**conservé** dans le dossier (D4 append-only — l'invalidation est
une trace, pas un effacement). Le dossier `green-lantern/` contient
une note *« concept invalidated 2026-XX-XX, motif : [raison] »*.

## La procédure d'observation Council-ready

### Étape 1 — Cadre d'observation

Green Lantern (People) tient un **journal d'observation** dans
`green-lantern/observations-2026-Q3.md` (ou équivalent), append-only,
qui consigne chaque cas observé avec :

- Date d'observation
- Concept référencé (#1 à #6)
- Cas réel (résumé en 2-3 phrases)
- Issue tranchée ou refus motivé
- Délai besoin → application
- Capitaine B2 témoin (nom, pas rang)
- Référence au packet mésoperpétuel source (si Council)

### Étape 2 — Revue hebdomadaire

Chaque semaine, Green Lantern produit un **bulletin d'observation**
de 5 lignes maximum, ajout au journal Council. Le bulletin liste
les cas de la semaine, sans interprétation.

### Étape 3 — Bilan 60 jours

À J+60, Green Lantern produit un **bilan** (1-2 pages) avec :

- Nombre de cas observés (cible : 3)
- Couverture (cible : ≥ 50%)
- Distribution (cible : ≤ 1.5)
- Vitesse (cible : ≤ 14 jours pour 80% des cas)
- Condition de mise à jour par concept testé (confirmée / amendée /
  invalidée)

Le bilan est **soumis** au B2 Council pour validation. Si le
protocole n'a pas atteint la cible, le bilan signale les
**obstacles observés** (par exemple, *« 0 cas sur la Méta
Gouvernance parce que 0 sollicitation Forge n'a été reçue »*).

### Étape 4 — Mise à jour de la doctrine

Pour chaque concept testé, le bilan conclut sur la condition de mise
à jour (1, 2, ou 3). Les **actions** correspondantes (append canon /
amendement / invalidation) sont entreprises dans la semaine qui suit
le bilan.

## Trois cas où le protocole serait inadapté

### Cas 1 — 0 cas observé après 60 jours

Si **0 cas** est observé en 60 jours, le protocole est **inopérant**
— pas de cible, pas de mesure. **Action** : étendre la fenêtre à
90 jours, ou **abandonner** le protocole (les concepts restent
lettre morte). Recommandation projetée : **étendre** à 90 jours,
parce que les concepts People sont **lents par nature** (succession,
dormance — pas des événements quotidiens).

### Cas 2 — 5+ cas observé en 30 jours

Si **5 cas ou plus** sont observés en **30 jours**, le protocole est
**sous-dimensionné** — la cible 3/60j est atteinte trop vite.
**Action** : ré-évaluer les critères d'acceptance (trop souples ?)
ou ajouter un **6ᵉ critère** (par exemple, *« cas diffusé à au
moins 2 capitaines B2 »*). Recommandation projetée : **durcir** les
critères, pas étendre la cible.

### Cas 3 — Distribution très concentrée

Si **distribution > 2** (3 cas sur 1 seul concept, 0 sur les 5
autres), le protocole **biaise** la doctrine vers 1 concept.
**Action** : sélectivement **abandonner** les concepts non-testés
(les marquer `status: untested` dans le frontmatter, sans les
invalider), et **concentrer** la fenêtre 60j sur les concepts
testés. Recommandation projetée : ne **jamais** invalider un
concept sans cas — l'invalidation requiert **contradiction**.

## Anti-pièges

- **Compter les cas projetés comme cas réels**. Un cas qui n'est pas
  observé en cycle ne compte pas. C'est le critère 1 — strict.
- **Cibler 6 cas au lieu de 3**. La cible 3/60j est **suffisante**,
  pas **plafond**. Viser 6 force à inventer des cas — c'est
  l'anti-piège *« speed over substance »*.
- **Confirmer un concept avec 1 seul cas**. La condition 1 exige ≥ 3
  cas, **tous** cohérents. 1 cas = anecdote.
- **Invalider un concept sans 3 cas contradictoires**. La condition
  3 exige ≥ 3 cas, **majorité** contradictoires. 1 cas contradictoire
  = signal d'amendement (condition 2), pas d'invalidation.
- **Oublier le bilan 60 jours**. Sans bilan, pas de mise à jour de
  la doctrine. Le protocole est **auto-fermant** à 60 jours.
- **Référence implicite au concept**. Un cas qui applique la tri-état
  People sans citer le concept #5 ne compte pas — le protocole teste
  les **concepts**, pas seulement les pratiques (critère 2).

## Liens

- [[green-lantern-people-meta-gouvernance-skills-l0]] — concept #1 testé
- [[green-lantern-people-formule-charge-carte]] — concept #2 testé
- [[green-lantern-people-lag-indicator-succession]] — concept #3 testé
- [[green-lantern-people-seuil-vacance-tolerable]] — concept #4 testé
- [[green-lantern-people-dormance-attente-active]] — concept #5 testé
- [[green-lantern-people-brand-co-sponsorat-superman]] — concept #6 testé
- [[flash-veto-empirical-validation-protocole]] — un précédent du même type
- [[superman-veto-empirical-validation-protocole]] — un autre précédent
- [[b2-council-arbitrage-rule]] — l'instance qui valide le bilan
- [[b2-meso-decision-packet-spec]] — le format Council-ready

## Note de confiance

**Reconstruit, à moitié étayé.** Le protocole cible 3 cas / 60 jours
est **calqué** sur les précédents Flash (tour 2) et Superman (tour
3) du même type — c'est une convention B2 en formation, pas une
règle catalogue. Les 5 critères d'acceptance sont **reconstitués**
depuis la pratique RACI (cas réel, concept référencé, issue
tranchée, format canonique, témoin externe) — pas cités
canoniquement. Les 3 indicateurs (couverture, distribution, vitesse)
sont **projetés** depuis les indicateurs de succès typiques (3
indicateurs = couverture + distribution + vitesse). Les 3 conditions
de mise à jour (confirmée / amendée / invalidée) sont **reconstituées**
depuis la doctrine Council (D4 append-only, validation Council).
La procédure 4 étapes est **projetée** depuis le fractal B1/B2/B3.
Les 3 cas d'inadaptation sont **projetés** depuis la pratique
protocolaire. Le protocole est **non-destructif** par construction —
il observe sans modifier la doctrine existante.