# RAPPORT — Hiérarchie des entités d'A'Space

> **Statut** : LIVRÉ — 2026-08-17
> **Auteur** : agent brief `hierarchie_jsonl`
> **Livrables** : `ontologie/hierarchie.jsonl` (34 relations sourceées)
> **Règle d'or** : Aucune entrée sans source. META_ONTOLOGIE.md est une source, pas une vérité.

---

## 1. Couverture effective

| Mesure | Valeur |
|---|---|
| Fichier source `META_ONTOLOGIE.md` | lu intégralement (281 lignes) |
| Fichier source `meta_ontologie.json` | lu intégralement (1050+ lignes) |
| `LAW.md` (Tech OS) | lu intégralement (99 lignes) |
| `CASCADE.md` (Tech OS) | lu intégralement (115 lignes) |
| `SOUL.md` (Rick) | lu intégralement (59 lignes) |
| `aspace-entites.ttl` | lu intégralement (21 entités, alias et comptages) |
| `aspace-schema.ttl` | lu intégralement (11 prédicats disponibles) |
| Concept `beth-morty-safety-gatekeepers.md` | lu intégralement |
| Concept `four-jerry-fractal.md` | lu intégralement |
| Concept `spock-areas-canon.md` | lu intégralement |
| Concept `jerry-macro-steward.md` | lu intégralement |
| Concept `matryoshka-l0-l1-l2.md` | lu intégralement |
| `CATALOGUE.md` | lu (extrait 100 lignes pour vérifier les concepts référencés) |
| `relations.jsonl` | lu (30 premières lignes pour caler le format) |
| **Fichiers disponibles non lus** | 0 dans le périmètre demandé |
| **Fichiers lus en sus du périmètre** | concepts-areas (4 fichiers) pour ancrer Spock/Jerry/Geordi/Data et `matryoshka-l0-l1-l2.md` |

**Couverture** : 100 % des fichiers nommés dans le brief ont été lus. Les concepts area-spock, area-jerry, area-beth-morty, et ressource-matryoshka ont été lus **au-delà** du périmètre pour ancrer les relations qui parlent d'eux.

## 2. Ce qui a été écrit — `hierarchie.jsonl`

**34 relations**, toutes avec `source` et `confiance` :

### Répartition par prédicat

| Prédicat | Compte | Sens dominant |
|---|---|---|
| `governs` | 9 | autorité d'un rang sur un autre (Rick → Tech OS, Beth → Business OS, Spock → Jerry, etc.) |
| `partOf` | 16 | composition (les Docteurs dans Tech OS, A1/A2/A3 dans Life OS, Spock/Picard/Geordi/Data dans A3) |
| `pairedWith` | 5 | symétrie canonique (Beth / Morty, Spock / Picard, Geordi / Data, Jerry / Summer, A0 / Rick) |
| `instantiates` | 3 | production d'artefact (Doctor → OS, Picard → Summer, Tech OS → Life OS + Business OS) |
| `dependsOn` | 1 | dépendance productive (Summer → Beth pour le veto) |

### Répartition par confiance

| Confiance | Compte |
|---|---|
| `haute` | 34 |
| `moyenne` | 0 |

Aucun passage à `moyenne` n'a été nécessaire : **toutes les relations s'ancrent sur une source canonique** (LAW.md, SOUL.md, CASCADE.md, META_ONTOLOGIE.md, ou un concept OKF). Les sources sont principalement :
- `LAW.md:30-42` — le tableau des trois Cores ;
- `LAW.md:50-56` — cohabitation Rick/Docteurs dans 10_Tech_OS/ ;
- `CASCADE.md:24-32, 60-68, 71-83` — cascades amont (A1-A3) et aval (B1-B3) ;
- `meta_ontologie.json relations.inter_couches` — Veto, hôtes, instantiation ;
- concepts OKF de la distillation (beth-morty-safety-gatekeepers, four-jerry-fractal, spock-areas-canon, jerry-macro-steward).

### Couverture des questions du brief

| Question | Relations répondant |
|---|---|
| Q1 — Les trois OS et leur mécanisme | rick→tech-os, rick→docteur, docteur→{tech-os, life-os, business-os}, tech-os→{life-os, business-os}, compagnons→docteur, tech-os→rick |
| Q2 — Les Cores et les Docteurs | Les trois `docteur→{tech-os, life-os, business-os}` cartographient la triade Kernel/Life/Buzz Core |
| Q3 — A0, A1, A2, A3 | a0-amadeus→{rick, a1}, a1→life-os, a2→life-os, a3→life-os |
| Q4 — B1, B2, B3 | jerry→business-os, summer→business-os, b1→business-os, b2→business-os, b3→business-os |
| Q5 — Le veto | beth→business-os, life-os→business-os, beth→morty, summer→beth |
| Q6 — Les gardiens PARA | spock/picard/geordi/data → a3, spock→jerry, picard→summer, data↔geordi, spock↔picard |
| Q7 — Beth, Morty, Jerry, Summer | beth→life-os, morty→life-os, beth↔morty, jerry→business-os, summer→business-os, jerry↔summer, summer→beth |

## 3. La tension que je n'ai pas tranchée

**Pyramide stricte vs unification L2 dans L1.**

Le canon pose L0 >= L1 > L2 comme une **autorité verticale** (SDD-006 §1.1, META_ONTOLOGIE.md §1) — l'expression la plus brutale est le Beth HALT veto de L1 sur L2. Mais l'utilisateur a dit en session (314fae52:24820) que *« Business OS est en cours d'unification dans Life OS dont Coach OS est la 1ere Franchise Prototype »* — c'est une **intégration horizontale**, pas une subordination verticale.

Le concept `matryoshka-l0-l1-l2.md` renforce la lecture verticale (« poupée russe : chaque couche héberge la suivante »), tandis que le §5 du même concept note que la Constitution v1.0 fait *« disparaître le veto vertical »* au profit de la fonction cohérence vie/santé.

**Comment cette tension se reflète dans `hierarchie.jsonl`** :
- J'ai posé `life-os governs business-os` (polarité L1 → L2, descendante veto) en confiance haute, parce que **Beth HALT est mesurable et codifié** (Loi 1 SDD-006).
- Je n'ai PAS posé l'inverse (« Business OS instancie / fait partie de Life OS »), parce que ce mouvement (unification) est **declaratif et non codifié** — Coach OS est dit « 1ere Franchise Prototype » (L2 → L1), mais Coach OS ne porte aucune entité Life OS en code (cf. META_ONTOLOGIE.md §6 trou T01).

**Ce que ça laisse dans le graphe** : à la prochaine distillation, soit la relation `business-os partOf life-os` apparaîtra (si l'unification se code), soit la pyramide stricte restera seule (si l'utilisateur tranche en faveur de L0 ≥ L1 > L2). Je n'ai pas pré-jugé.

## 4. Les trois entités maigres — verdict

### 4.1 Les Compagnons (1 concept)

**Comptage** : 1 concept mentionne les Compagnons (`wiki-schema-llm-wiki`). META_ONTOLOGIE.md §2.1 cite pourtant **9 compagnons canoniques** : Yaz/Ryan/Graham (13e Kernel), Amy/Rory/River (11e Life), Clara/Bill/Nardole (12e Buzz). CASCADE.md:42-44 et 67-69 leur donnent un rôle technique explicite (Amy spécifie / Rory bâtit / River réplique pour L1 ; Clara spécifie / Nardole bâtit / Bill réplique pour L2).

**Verdict** : **trou de couverture.** Les quatre seaux PARA (Projects / Areas / Resources / Archives) portent des concepts Life OS et Business OS, pas les agents Tech OS. Les 9 compagnons sont sur disque (`sessions_md/.../bf0d8147-...:5192`), pas dans `AGENT_REGISTRY_DB` Notion (cf. META_ONTOLOGIE.md §6 trou T11). C'est l'information la plus utile de cette section : **la distillation a raté 9 acteurs techniques parce qu'aucun des 4 seaux PARA ne les porte**.

### 4.2 Les Docteurs (6 concepts)

**Comptage** : 6 concepts mentionnent `docteur`. META_ONTOLOGIE.md §1 et §2.1 leur donnent un rôle opérationnel structurant (Kernel Core 13e / Life Core 11e / Buzz Core 12e) — chaque Core est maître d'une couche.

**Verdict** : **trou de couverture**, moins sévère que les Compagnons. Les Docteurs apparaissent dans les concepts transverses (matrioshka, sovereign-ties, tags-registres, agents-md-identity-canon, l2-8-domaines-roster-canon, aspace-governance-dashboard) — 6 concepts, mais aucun n'est un concept « Docteur » en propre. La distillation a posé les Docteurs comme attribut d'un Core, pas comme sujet autonome.

### 4.3 Tech OS (8 concepts)

**Comptage** : 8 concepts mentionnent `tech-os`. À comparer aux 84 de Life OS et 41 de B2. META_ONTOLOGIE.md §3.3 conclut que Tech OS est **double** :
- actif (le constructeur universel, le replicator, le kernel) ;
- passif (le sol, le substrat, L0).

**Verdict** : **trou de couverture**, avec une nuance. Les 8 concepts qui mentionnent Tech OS sont des concepts transverses (matrioshka, sovereign-ties, sdd-system-design-documents, blueprints-canon-tripartite, adr-immutability-ricks-law, life-os-six-vaisseaux, archive-v3-structure-snapshot, concepts-ontologie). **Aucun n'est un concept Tech OS en propre.** Le seau Tech OS est occupé par 4 piliers transverses (Rick/SOUL, LAW, ADR, CASCADE), pas par des concepts. C'est la même pathologie que pour les Docteurs, amplifiée.

**Information utile** : la distillation a posé la **gouvernance** Tech OS (Rick, ADRs, sovereignty) comme attribut de concepts-canons, mais **les artefacts Tech OS** (les 3 Cores, les 9 compagnons, le replicator, les 4 organes du kernel) n'ont pas de concept dédié. Une prochaine passe pourrait créer :
- `tech-os/replicator.md` — le gabarit et le copieur ;
- `tech-os/kernel-4-organes.md` — file SQLite, adaptateur, portier, reviewer ;
- `tech-os/3-cores-moule-et-instances.md` — Kernel/Life/Buzz Core depuis le même gabarit.

### 4.4 Bilan des trois entités maigres

Les trois sont **marginales dans la distillation**, mais **structurantes dans le canon**. Aucune des trois n'est une notion périphérique d'A'Space : ce sont trois **acteurs du mécanisme** (Compagnons = S3 techniciens, Docteurs = S2 managers, Tech OS = L0 sol-mécanisme). Leur absence dans le graphe des concepts trahit un **biais de la distillation** : les 4 seaux PARA filtrent par couche applicative, pas par rang de souveraineté. Le L0 n'a pas de seau dans PARA ; c'est pourquoi la moitié de sa substance reste lettre morte dans le graphe.

## 5. Ce que je n'ai pas couvert

- **Les 8 domaines B2 individuellement** (Growth, Sales, Product, Ops, IT, Finance, People, Legal) et leurs 8 strates DC (Superman, John Jones, Flash, Batman, Cyborg, Wonder Woman, Green Lantern, Aquaman). Le brief ne les demande pas et le TTL ne les pose pas comme entités distinctes — ils sont des attributs de `b2`. Mentionnés dans 4 relations seulement (via `business-os` + `b2`).
- **Les 8 squads Marvel** (Guardians, Illuminati, Avengers, Fantastic4, KangDynasty, Thunderbolts, XMen, Eternals). Même raison.
- **Les 8 LD (Life Wheel)** (LD01-LD08). Le brief ne demande pas la relation LD → Business Domain — c'est le trou T02 de META_ONTOLOGIE.md §6.
- **Les 5 horizons 12WY** (H1, H3, H10, H30, H90) et le tag `horizon` partagé. Le canon le pose, mais aucune relation de hiérarchie d'entité ne le requiert — c'est un attribut (cf. trou T08).
- **Les 4 variantes de Jerry** (Prime, Bio, Nexus, Solarpunk). Une seule entité `jerry` est dans le TTL ; les 4 variantes sont des postures, pas des entités distinctes (cf. META_ONTOLOGIE.md §6 trou T04).

## 6. Auto-critique

**Ce qui m'a fait hésiter** : la relation `a0-amadeus → a1` (governs). META_ONTOLOGIE.md §2.1 dit « A0 subordonne 7 cadences » et la session 314fae52:25540 dit « A0 devient l'orchestrateur de Life OS ». Mais A0 → a1 n'est pas une relation universelle dans le canon — dans la lecture matrioshka, A0 est le Pilot qui **donne l'intention** à Rick (L0) ET à Beth/Morty (L1) AND à Jerry/Summer (L2), pas un gouverneur unique qui s'impose à a1. J'ai quand même retenu la relation parce que la session 314fae52:25540 et la note meta_ontologie.json entites.tech_os.A0 (`rang: au-dessus de A1, A2, A3 — orchestre le tout`) sont **conjointement** claires. Marge d'incertitude : « subordonne » plutôt que « pilote » ; le verbe `governs` est peut-être trop vertical pour ce que A0 fait. Aucun remplacement net à proposer — je signale.

**Ce qui manque et que je n'ai pas tenté d'écrire** : la relation `a2 → a3` (A2/Cerritos qualifie avant A3/Picard instancie). Elle est dans le canon (Cerritos/GTD filtre avant Picard/Project), mais elle parle de concepts (`cerritos-gtd-pipeline`, `picard-project-pattern`), pas d'entités du TTL. Hésitation légitime — j'ai préféré ne pas poser une relation d'entités dont la source ne parle que de concepts.

---
