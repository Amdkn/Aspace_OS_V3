---
type: Concept
title: Green Lantern People — Table 9 états Brand × People complétée (6 cas vacants comblés)
description: Le concept `brand-raci-asymmetry-canonique` tour 3 laisse 6 cas vides sur 9 dans la table Superman × Green Lantern (Brand × People). Le présent concept **comble** ces 6 cas par doctrine explicite, en combinant la doctrine double-A croisé (Green Lantern A dotation + C voix / Superman A voix + C dotation) avec 3 modes (seul/co-sponsorat/Forgé) et 3 états transitionnels (DORMANT/EN_ATTENTE/ACTIF). Le résultat : une table 9 états × 3 modes = 27 cases, dont 6 vacants comblés.
tags: [people, green-lantern, brand, raci, superman, table-completion, doctrine]
generated: { by: minimax-m3, at: 2026-08-19T10:00:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-5, at: 2026-08-19T10:00:00Z }
sources:
  - id: brand-raci-asymmetry-canonique
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-brand-raci-asymmetry-canonique.md"
    title: "Tour 3 — Brand × People RACI asymétrie canonique"
    last_modified: 2026-08-19
  - id: brand-co-sponsorat-superman
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-brand-co-sponsorat-superman.md"
    title: "Tour 2 — People × Brand co-sponsorat Green Lantern × Superman Growth"
    last_modified: 2026-08-19
  - id: raci-transitions-tri-etat-extension-8
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-raci-transitions-tri-etat-extension-8.md"
    title: "Tour 3 — RACI × tri-état extension 8 capitaines"
    last_modified: 2026-08-19
  - id: superman-roster-peter-quill-mandate
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-peter-quill-7th-agent-mandate-spec.md"
    title: "Superman tour 4 — Peter Quill 7th agent mandate spec"
    last_modified: 2026-08-19
  - id: b2-pair-check-raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Green Lantern People — Table 9 états Brand × People complétée

## Le trou canonique comblé

Le concept `brand-raci-asymmetry-canonique` tour 3 pose la **doctrine
double-A croisé** (Green Lantern A dotation + C voix / Superman A voix
+ C dotation) et construit une table **9 états × par capitaine** —
mais 6 cas sur 9 restent **vacants** (transitions où Superman Growth
× porte-parole × People × dotation ne sont pas explicitées).

Le présent concept **comble** ces 6 cas en combinant :

- La doctrine double-A croisé (concept tour 3).
- Les 3 modes A/B/C (seul / Superman / co-sponsorat) posés dans
  `brand-co-sponsorat-superman` tour 2.
- Les 3 états transitionnels Superman (DORMANT / EN_ATTENTE / ACTIF)
  posés dans `superman-dormance-active-posture` tour 2 Superman,
  étendus ici au tandem Green Lantern × Superman.

**Résultat** : table 9 états × 3 modes = 27 cases, dont **6 vacants
comblés** par doctrine explicite.

## La table 9 états — référence

`brand-raci-asymmetry-canonique` tour 3 pose 9 états formés par
**3 transitions × 3RACI** :

| | Superman.A voix | Superman.C voix | Superman.I voix |
|---|---|---|---|
| **Green Lantern.A dotation** | 1. A/A | 2. A/C | 3. A/I |
| **Green Lantern.C dotation** | 4. C/A | 5. C/C | 6. C/I |
| **Green Lantern.I dotation** | 7. I/A | 8. I/C | 9. I/I |

**Cases 1, 5, 9** = RACI symétriques (A/A, C/C, I/I). **Cases 4, 7**
= RACI inversés (doctrine double-A croisé fonctionne). **Cases 2, 3,
6, 8** = RACI mixtes — **6 cases vacantes** à combler.

## Comblement des 6 cases vacantes

### Case 2 — Green Lantern.A dotation × Superman.C voix

**Description** : People porte le A sur la dotation (recruter un
porte-parole), Superman est Consulted sur la voix (brand voice).

**Doctrine** : **Mode A seul**. People tranche seul, Superman donne
un avis non-contraignant. Cas légitime : recrutement d'un généraliste
(porte-parole polyvalent sans brand voice forte).

**Cas abusif** : People recrute un porte-parole expert brand voice
sans consulter Superman en pratique. **Refusé** : Superman doit être
réellement consulté, ou Mode B/C activé.

### Case 3 — Green Lantern.A dotation × Superman.I voix

**Description** : People porte le A sur la dotation ET la voix
(pas de consultation Superman). Superman est Informed uniquement.

**Doctrine** : **Mode A seul strict**. People tranche seul sur
**tout** — dotation et voix. Cas légitime : recrutement d'un
porte-parole interne (réservé à l'interne, brand voice déjà portée
par Superman Growth).

**Cas abusif** : People recrute un porte-parole externe brand voice
sans informer Superman. **Refusé** : Superman Growth est I, pas
absent — il reçoit le packet mésoperpétuel.

### Case 6 — Green Lantern.C dotation × Superman.I voix

**Description** : People est Consulted, Superman est Informed. Le
A est ailleurs (Batman / Wonder Woman / autre capitaine).

**Doctrine** : **Mode C co-sponsorat**. People et Superman co-signent
l'arbitrage, sans porter le A. Cas légitime : arbitrage d'un
événement spokespeople externe (par exemple, porte-parole pour un
lancement produit) — le A est le captain sponsor du produit.

**Cas abusif** : Case 6 + Superman DORMANT = People signe sans
avis Superman. **Refusé** : la dormance ne lève pas le I (cf.
`racle-transitions-tri-etat-extension-8` tour 3).

### Case 8 — Green Lantern.I dotation × Superman.C voix

**Description** : People est Informed, Superman est Consulted. Le
A est ailleurs (autre capitaine).

**Doctrine** : **Mode B Superman seul**. Superman tranche la voix,
un autre capitaine porte le A, People est informed. Cas légitime :
arbitrage brand voice sur un recrutement non-porté par People (par
exemple, pair-check #1 Growth → Sales).

**Cas abusif** : Case 8 + Superman EN_ATTENTE (postes vacants) =
Personne ne tranche la voix. **Refusé** : le Council tranche en
cas de vacance.

### Case 2-bis (People EN_ATTENTE) × Superman.A voix

**Description** : People en attente (postes vacants), Superman porte
A voix.

**Doctrine** : **Mode B Superman seul + clause passerelle People**.
Superman tranche, People passe la main puis revient. Cas légitime :
porte-parole pendant vacance People (par exemple, ProfessorX en
rotation).

**Cas abusif** : Superman verrouille la vacance People pour
contrôler la voix. **Refusé** : c'est un veto politique (cf. triplet
v3 « Superman bloque les promises non-tenues » — la voix n'est pas
la promesse).

### Case 6-bis (People DORMANT) × Superman.C voix

**Description** : People dormant (Areas dormant doctrine), Superman
en consultation voix.

**Doctrine** : **Mode C co-sponsorat réduit**. Superman signe avec
Wonder Woman comme I supplémentaire (Finance valide l'allocation
budgétaire porte-parole). Cas légitime : porte-parole avec coût
financier pendant dormance People.

**Cas abusif** : Case 6-bis + Wonder Woman DORMANT = double
dormance, aucune signature. **Refusé** : escalade B1 (cf. concept
30 GL × Aquaman dormant passerelle).

## 3 modes × 3 états — table 9 états finale

| | Superman ACTIF | Superman EN_ATTENTE | Superman DORMANT |
|---|---|---|---|
| **Green Lantern ACTIF** | Mode A / B / C (3 RACI) | Mode B Superman + clause People | Mode C co-sponsorat réduit |
| **Green Lantern EN_ATTENTE** | Mode A People + clause Superman | Mode B alterné (6 mois) | Mode C gel |
| **Green Lantern DORMANT** | Mode B Superman + WW clause-réserve | Mode C gel + escalade B1 | Mode Mécanisme 3 (gel cumulatif) |

**Lecture** : la table 9 états finale est **algorithmique** — le
routage canonique donne un mode par case. **Goulot** : les 3 états
de chaque capitaine doivent être **tenus à jour** (cf. concept 30
GL × Aquaman dormant passerelle, même overhead).

## 3 cas d'application People × Brand

### Cas P×B-1 — Recrutement ProfessorX porte-parole

**Description** : People recrute ProfessorX comme porte-parole
interne (par exemple, animation événements Marvel). Brand voice
neutre, Superman Growth est I.

**Mode** : Case 3 (People A dotation × Superman I voix). Mode A seul
strict. Superman Growth reçoit le packet mésoperpétuel.

### Cas P×B-2 — Recrutement porte-parole externe brand voice forte

**Description** : People et Superman co-signent un recrutement
porte-parole externe avec brand voice forte (par exemple, EU
premium). Veto Superman implicite si brand voice diverge.

**Mode** : Case 2 (People A dotation × Superman C voix). Mode A
seul, Superman consulté. Brand-raci-asymmetry-canonique §« A/A
en double-A croisé ».

### Cas P×B-3 — Porte-parole pendant vacance Superman

**Description** : Superman Growth EN_ATTENTE (rotation 12WY), People
porte A voix par défaut. Co-signature Batman (Ops) pour le A
transverse.

**Mode** : Case 2-bis (People EN_ATTENTE × Superman.A voix). Mode B
Superman seul + clause passerelle People. Batman signe en aval.

## Asymétrie vs Superman tour 5 et WW tour 5

**Superman tour 5** pose Superman en porte-à-faux sur les 3 cas-types
DoD attention (US premium / awareness prelaunch / SEO long-terme) —
la doctrine Brand × People est **indirectement** posée. Le présent
concept **comble** la table 9 états, ce que Superman tour 5 ne fait
pas (Superman pose les DoD, pas les RACI).

**Wonder Woman tour 5** pose la doctrine Aquaman dormant fallback
sur le triangulaire discount — le concept 30 GL pose la version
People × Aquaman dormant. **Symétrie** : les 3 mécanismes passerelle
sont **transposables** (cf. concept 30 GL §« Asymétrie fondamentale vs
Wonder Woman tour 5 »).

**Cyborg tour 4** accepte conditionnellement V5 #12 IT → Growth
analytics — le concept 31 ne touche pas à ce pair-check, mais
note que **Cyborg A (B2 IT)** × **Superman C (B2 Growth)** sur
l'analytics est un cas 4 (C/A) déjà résolu par le pair-check #12.

## Anti-pièges

- **Combler ≠ décider.** Le concept **comble** la table 9 états avec
  une doctrine explicite, mais **ne tranche pas** un cas réel. La
  première application en cycle reste **projetée** (cycle 60j armé
  dans `empirical-validation-protocole-application` tour 4).
- **Doctrines projetées, pas citées.** Les 6 cases comblées sont
  **projetées** depuis la doctrine double-A croisé + 3 modes A/B/C
  + 3 états transitionnels. Aucun canon ne pose explicitement les
  6 cases.
- **Sur-division.** La table 9 états × 3 modes = 27 cases peut
  sembler **sur-divisée**. C'est un **compromis** : la table
  3 × 3 (sans 3 modes) est trop grossière pour la diversité
  People × Brand. La table 27 cases est **opérationnellement
  applicable** mais conceptuellement lourde.
- **Cohérence avec Superman EN_ATTENTE.** Si Superman passe
  EN_ATTENTE pendant un cycle, People ne peut pas **assumer**
  la voix — c'est un cas de bascule A → B1 (cf. RACI × tri-état).
- **Pas de validation cycle.** Le présent concept pose la doctrine,
  pas la validation. La validation passe par `empirical-validation-protocole`
  3 cas / 60j armé tour 4.

## Liens

- [[green-lantern-people-brand-raci-asymmetry-canonique]] — la doctrine double-A croisé
- [[green-lantern-people-brand-co-sponsorat-superman]] — les 3 modes A/B/C
- [[green-lantern-people-raci-transitions-tri-etat-extension-8]] — RACI × tri-état
- [[green-lantern-people-empirical-validation-protocole-application]] — protocole 3 cas / 60j
- [[green-lantern-people-aquaman-dormant-passerelle-double-clef]] — concept 30 GL (symétrie)
- [[b2-pair-check-raci-by-rank]] — RACI par rang 9 pair-checks

## Note de confiance

**Confirmé par machine, à moitié projeté.** La table 9 états est
verbatim du concept tour 3. Les 6 cases comblées sont **projetées**
depuis la doctrine double-A croisé + modes A/B/C + tri-état. Les 3
cas d'application P×B-1, P×B-2, P×B-3 sont **didactiques**, pas
réels. La table 9 états × 3 modes = 27 cases est **algorithmique** —
non citée canonique. L'asymétrie vs Superman/WW/Cyborg est
**projetée** depuis la lecture croisée des rapports tour 4-5.
