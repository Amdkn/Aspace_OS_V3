---
type: Concept
title: People — dépendances actives vs passives, matrice asymétrique 7 domaines
description: Couple-check #9 *People → Tous* est le plus transverse de la matrice (9 critères). Mais la **dépendance inverse** — ce sur quoi People s'appuie pour exister — est implicite. Le concept isole **6 dépendances actives** (People attend un signal d'un autre domaine pour fonctionner) vs **1 dépendance passive** (les autres attendent People). 6 dépendances actives sont chiffrées (latence, criticité, fréquence), 1 nomination implicite (squad lead X-Men) est identifiée, et 3 asymétries fondamentales (transverse vs local, ownership vs consultation, temporalité People-2026) sont documentées.
tags: [people, green-lantern, dependances, asymetrie, actif-passif, 7-domaines, b2, matrice]
generated: { by: minimax-m3, at: 2026-08-19T08:30:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-4, at: 2026-08-19T08:30:00Z }
sources:
  - id: pair-checks-raci-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: "RACI par rang sur les 9 pair-checks"
    last_modified: 2026-08-19
  - id: couplages-invisibles-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-couplages-invisibles.md"
    title: "Tour 1 — 7 couplages invisibles People"
    last_modified: 2026-08-19
  - id: v5-pair-check-granularisation-9-tour-3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-v5-pair-check-granularisation-9.md"
    title: "Tour 3 — V5 pair-check granularisation 9 (7 sous-pair-checks)"
    last_modified: 2026-08-19
  - id: perimetre-frontieres-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-perimetre-frontieres.md"
    title: "Tour 1 — People périmètre et 3 frontières floues"
    last_modified: 2026-08-19
  - id: brand-co-sponsorat-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-brand-co-sponsorat-superman.md"
    title: "Tour 2 — People × Brand co-sponsorat Green Lantern × Superman Growth"
    last_modified: 2026-08-19
  - id: veto-recrutement-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-veto-recrutement-sans-mandat.md"
    title: "Tour 1 — Veto People recrutement sans mandat"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# People — dépendances actives vs passives, matrice asymétrique 7 domaines

## Le constat — People est transverse en émission, pas en réception

Le pair-check #9 *People → Tous* (cf. `b2-pair-check-raci-by-rank.md`)
pose People comme **C systématique** sur les 9 transitions canoniques,
avec Accountable = B2 captain du domaine impacté. C'est la **dépendance
émission** — People est transverse.

Mais la **dépendance réception** — ce sur quoi People s'appuie pour
délivrer — est **implicite**. People **reçoit** 6 signaux d'autres
domaines (cf. infra) avant de pouvoir émettre un avis C. Sans ces
signaux, People **ne peut pas** jouer son rôle de coordination.

**Asymétrie fondamentale** : People émet **1** pair-check transverse
(#9), mais **reçoit 6** signaux distincts d'autres domaines. Le ratio
1 / 6 fait de People un **concentrateur** : il agrège 6 signaux et
émet 1 avis.

## Les 6 dépendances actives — People attend un signal

| # | Source | Nature du signal | Latence | Criticité | Statut |
|---|---|---|---|---|---|
| 1 | **Aquaman Legal** | Signature de l'accord de prestation (double clef) | J+0 synchrone | **Critique** (cf. `green-lantern-people-couplages-invisibles.md` §« 5. People × Legal ») | **actif** |
| 2 | **Cyborg IT** | Disponibilité du système pour héberger l'agent | J+1 à J+7 | **Critique** (système non-prêt = recrutement bloqué) | **actif** |
| 3 | **Bill L0.2 Forge** | Confirmation skills L0 disponibles | J+5 à J+10 | **Critique** (triplets 37 + 55) | **actif** |
| 4 | **Wonder Woman Finance** | Date de revue + métrique de retour (recrutement récurrent) | J+30 mensuel | **Moyenne** (veto Wonder Woman conditionnel) | **semi-actif** |
| 5 | **Batman Ops** | Charge de livraison → seuil vacance / surcharge | J+7 hebdo | **Critique** (red flag #3 matrice) | **actif** |
| 6 | **Superman Growth** | Continuité de la voix de marque (porte-parole) | J+30 mensuel | **Moyenne** (co-sponsorat Brand) | **passif** |

**6 dépendances actives** : 1, 2, 3, 5 sont **critiques** (sans le
signal, People bloque). 4, 6 sont **moyennes** (le veto est
conditionnel, l'absence de signal est récupérable).

## La 1 dépendance passive — les autres attendent People

Le pair-check #9 *People → Tous* est la **dépendance passive** des 7
autres domaines. Sur les 9 pair-checks canoniques, **9 portent A =
un B2 captain en aval** (par exemple, A = B2 Sales sur Growth → Sales) ;
**6 portent C = People** (sur les 9 où People est pertinente). Les 7
autres domaines **attendent** l'avis C de People avant de statuer.

**Asymétrie d'attente** :
- People **attend** 6 signaux (concaténation).
- Chacun des 7 autres **attend** 1 avis C de People (déconcaténation).

Le ratio 6 / 1 fait de People un **goulot d'étranglement** potentiel :
si People tarde à émettre son avis C, les 7 autres pair-checks sont
gelés.

## 3 asymétries fondamentales

### Asymétrie 1 — Transverse vs local

People est **transverse** par construction (émission sur 7 domaines) ;
les 6 dépendances actives sont **locales** (1 source par dépendance).
**Conséquence** : la **dette de latence** de People est la **somme**
des 6 dépendances. Si Aquaman (J+0) tarde, et Cyborg (J+7) tarde, et
Forge (J+10) tarde, People est bloqué à J+10 au plus tôt.

### Asymétrie 2 — Ownership vs consultation

Sur les 6 dépendances actives, **People est Accountable** sur la
**synthèse** (émettre l'avis C final), mais **Consulted** sur
**chacune** des 6 sources. C'est la **différentiation RACI** : A sur
le résultat, C sur les inputs.

**Conséquence** : People **ne peut pas accélérer** une dépendance
bloquée. Si Aquaman tarde à signer, People ne peut pas forcer la
signature. Le Council doit trancher (escalade B1 si Aquaman oppose
un veto).

### Asymétrie 3 — Temporalité People-2026

Les 6 dépendances ne sont **pas simultanées** : la **dépendance 5
(Batman Ops, charge)** est hebdomadaire ; la **dépendance 4 (Wonder
Woman, finance)** est mensuelle. La temporalité People-2026 est **mixte** :
- **Hebdo** : 5 (charge) + 1 (double clef Legal) = 2 dépendances rapides.
- **Mensuel** : 4 (finance) + 6 (brand) = 2 dépendances lentes.
- **J+1 à J+10** : 2 (IT) + 3 (Forge) = 2 dépendances intermédiaires.

**Conséquence** : le **cycle People** est mixte (2 hebdo + 2 J+10 + 2
mensuel). Le cycle optimal est **T+10j** (pire des 2 + 3) — un
arbitrage People ne peut pas être Council-ready sous J+10.

## Comparaison avec les autres domaines (matrice 8 × 7)

Chaque domaine B2 a **1 dépendance principale** (le ou les captain en
amont de ses pair-checks) :

| Domaine | Émission (transverse) | Réception (active) |
|---|---|---|
| **People** | 1 pair-check #9 → 7 | **6 dépendances actives** |
| **Legal** | 2 pair-checks (#7, #8) | 3 (avant People #9, avant citation, avant Batman) |
| **Sales** | 0 (reçoit) | 2 (Growth en amont, Ops en aval) |
| **Finance** | 2 pair-checks (#5, #6) | 2 (B1 mandate + revue) |
| **Ops** | 3 pair-checks (#2, #3, #9 receveur) | 4 (Sales, Product, People delivery, support) |
| **Growth** | 1 pair-check (#1) | 3 (Sales aval, B1 mandate, public) |
| **Product** | 2 pair-checks (#6, #8) | 3 (Finance, IT, B2-Ops aval) |
| **IT** | 1 pair-check (#4) | 2 (Product amont, People codé) |

**People est dernier en ratio émission/réception** (1 / 6). C'est la
**trace** de la transversalité People — un capitaine transverse
**reçoit** plus qu'il n'émet.

## 1 nomination implicite — squad lead X-Men

La dépendance passive des 7 autres (People est C) pose une **question
de squad lead** : qui signe l'avis C de People au Council ?

- **Batman Ops** → compte sur MrFantastic (squad lead Fantastic4).
- **Aquaman Legal** → compte sur Thena (squad lead Eternals).
- **People** → **pas de squad lead nommé** (cf. `green-lantern-people-xmen-effectif-canon-recompte-disk.md`
  §« 4 asymétries X-Men »).

**Recommandation** : nommer un squad lead X-Men parmi les 8 (par exemple,
**ProfessorX** par primauté sur le canal recruiting, ou **Beast** par
primauté sur le canal TechRecruiting). Cette nomination est **une
dépendance Council**, pas People — le Council tranche.

C'est une **remontée B2** du présent concept.

## Anti-pièges

- **Confondre dépendance et couplage.** Un couplage (cf.
  `green-lantern-people-couplages-invisibles.md`) est une **interaction**
  entre 2 domaines. Une dépendance est un **signal** qu'un domaine
  attend d'un autre. Les deux sont liés, mais pas identiques.
- **People comme goulot d'étranglement supposé.** Le ratio 1 / 6
  fait de People un **concentrateur**, pas un goulot. La lenteur
  People n'est pas un défaut de People — c'est la **somme** des 6
  dépendances.
- **Squad lead auto-proclamé.** Le squad lead X-Men n'est **pas**
  nommé. Green Lantern ne peut pas le nommer seul — c'est un
  **arbitrage Council**.
- **Asymétrie 3 ignorée.** Le cycle People T+10j est un **plancher**,
  pas une cible. Un arbitrage People sous J+10 est **suspicious**
  (peut signaler un avis C bâclé).

## Liens

- [[b2-pair-check-raci-by-rank]] — la matrice RACI canonique
- [[green-lantern-people-couplages-invisibles]] — les 7 couplages
- [[green-lantern-people-v5-pair-check-granularisation-9]] — V5 granularisation
- [[green-lantern-people-perimetre-frontieres]] — les 3 frontières
- [[green-lantern-people-brand-co-sponsorat-superman]] — Brand × People
- [[green-lantern-people-veto-recrutement-sans-mandat]] — le veto People
- [[green-lantern-people-xmen-effectif-canon-recompte-disk]] — recompte 8

## Note de confiance

**Reconstruit, à moitié étayé.** Les 6 dépendances actives sont
**reconstruites** depuis les couplages-invisibles (tour 1) et les
triplets 37 + 55 (Forge). La 1 dépendance passive est tirée verbatim
du pair-check #9. Les 3 asymétries sont **projetées** depuis la
différentiation RACI et la temporalité Council. La matrice 8 × 7 est
**reconstituée** par observation sur les 9 pair-checks + projetée par
analogie. La nomination squad lead X-Men est une **remontée** —
décision Council, pas People.
