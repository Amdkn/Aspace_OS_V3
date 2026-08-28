---
type: Backend
title: La couche B (B1 Summers / B2 Conseil / B3 Swarms) n'existe plus dans le runtime Multica
description: L'ontologie et les concepts des 8 domaines existent, mais les agents B1/B2/B3 sont absents du workspace vivant — ce n'est pas de la dormance, c'est une disparition.
tags: [multica, agents, couche-b, ontologie, coach-os, business-os, 8-domaines, rdf]
generated: { by: "claude-opus-5", at: "2026-08-21T08:10:00Z" }
verified:
  - { by: "claude-opus-5", at: "2026-08-21T08:10:00Z" }
sources:
  - id: multica-live
    resource: "https://api.multica.ai/api/agents?workspace_id=1ae43c2b-…"
    title: "API Multica — inventaire des agents du workspace, mesure directe"
    last_modified: 2026-08-21
  - id: multica-snapshot
    resource: "ASpace_OS_V3/00_Amadeus/20_Harness/multica_export_2026-08-02/agents.json"
    title: "Export Multica du 2026-08-02 (112 agents)"
    last_modified: 2026-08-02
  - id: ontologie-ttl
    resource: "ASpace_OS_V3/70_Onthologies/triplets/, _structure/"
    title: "Cinq fichiers Turtle décrivant les 8 domaines"
    last_modified: 2026-08-21
  - id: concepts-domaines
    resource: "ASpace_OS_V3/70_Onthologies/pulse/domaines/"
    title: "258 concepts markdown répartis sur 8 domaines"
    last_modified: 2026-08-21
okf_version: "0.2"
---

# La couche B n'est pas dormante, elle est absente

## La mesure qui tranche

Deux inventaires du même workspace Multica
(`1ae43c2b-c443-4896-8afe-b15bec691b9e`) :

| | Export 2026-08-02 | API vivante 2026-08-21 |
|---|---|---|
| Agents totaux | 112 | **57** |
| B1 (Summers, Jerry) | 6 | **0** |
| B2 (Conseil des 8 champions DC) | 8 | **0** |
| B3 (Swarms Marvel) | 12 | **0** |
| A1 / A2 / A3 | 3 / 6 / 26 | 2 / 6 / 35 |
| Couche S (Rick, Doctor, Yaz…) | — | 14 |

Recherche par mot-clé sur les 57 agents vivants — `summers`, `jerry`, `batman`,
`superman`, `cyborg`, `aquaman`, `flash`, `lantern`, `wonder`, `jones`,
`manhunter` : **zéro correspondance**.

La formulation « rester en dormance par manque d'opérateurs autonomes » suppose
des agents inactifs qu'il suffirait de réveiller. Ce n'est pas l'état mesuré :
**il n'y a rien à réveiller.** La couche A a grossi pendant ce temps
(26 → 35 en A3), donc le workspace a bien vécu.

**Cause, donnée par l'utilisateur le 2026-08-21 :** l'archivage est
**délibéré**. Croyant que Multica n'était plus le runtime du Business OS, il a
archivé tout ce qui y vivait pour expérimenter Tech OS. Ce n'est donc ni une
perte, ni un incident — c'est une décision, réversible. Ne pas la traiter comme
une panne à réparer.

Cette distinction n'est pas rhétorique : réveiller coûte une commande,
reconstruire coûte 26 définitions d'agents.

## Ce qui existe bel et bien

L'absence est côté runtime, pas côté matière. Trois actifs sont mesurés présents.

**L'ontologie RDF** — cinq fichiers Turtle, ~2 520 triplets terminaux :

| Fichier | Lignes | Triplets |
|---|---|---|
| `_structure/aspace-v3-structure.ttl` | 9 167 | 1 518 |
| `triplets/aspace-domaines.ttl` | 1 155 | 385 |
| `triplets/aspace-v3.ttl` | 981 | 327 |
| `triplets/aspace-os.ttl` | 834 | 278 |
| `triplets/aspace-vague2.ttl` | 36 | 12 |

Le motif d'appariement est en place, par exemple :

```turtle
<urn:aspace:entity:sales-domain> aspace:pairedWith  <urn:aspace:entity:illuminati> .
<urn:aspace:entity:sales-domain> aspace:instantiates <urn:aspace:entity:martian-manhunter-owner> .
```

**Le corpus de concepts** — 258 fichiers markdown dans `pulse/domaines/` :
flash 35, green-lantern 35, wonder-woman 35, batman 33, superman 32,
cyborg 30, john-jones 30, aquaman 28.

## Deux défauts du graphe

**Product/Flash n'a pas de triplet `instantiates`.** Sept domaines sur huit
déclarent leur propriétaire B2 (`aquaman-owner`, `batman-owner`, `cyborg-owner`,
`green-lantern-owner`, `martian-manhunter-owner`, `superman-owner`,
`wonder-woman-owner`). Il n'existe aucun `flash-owner`, et
`product-domain` n'instancie personne. Le domaine est apparié à sa squad
(`product-domain pairedWith the-avengers`) mais orphelin de champion.

**Le nœud Avengers est dédoublé.** Le graphe contient à la fois
`entity:the-avengers` (depuis `product-domain`) et `entity:avengers` (depuis
`entity:flash`). Deux URI pour une seule squad : toute requête qui suit l'une
rate l'autre.

**Piège de lecture — John Jones n'est pas manquant.** Une recherche sur `Jones`
rend zéro occurrence dans les cinq `.ttl` et donne l'illusion d'un trou. Le
domaine Sales est bien couvert, sous `martian-manhunter-owner` : J'onn J'onzz,
John Jones et Martian Manhunter sont le même personnage. Chercher un champion
par son alias humain produit un faux négatif.

## Couverture B3 : cinq squads sur huit, même dans le snapshot

Avant même la disparition, les swarms n'étaient pas complets. Les 12 agents B3
du 2 août se répartissaient ainsi :

| Squad | Domaine | B3 |
|---|---|---|
| Gardiens de la Galaxie | Growth (Superman) | 6 |
| Fantastic Four | Ops (Batman) | 2 |
| Illuminati | Sales (John Jones) | 1 |
| Avengers | Product (Flash) | 1 |
| X-Men | People (Green Lantern) | 1 |
| Kang Dynasty | IT (Cyborg) | **0** |
| Thunderbolts | Finance (Wonder Woman) | **0** |
| Eternals | Legal (Aquaman) | **0** |

Un douzième agent, `B3 Doctor Strange`, n'est rattaché à aucune des huit squads.

## Le pont qui n'a jamais été construit

Dans `projects.json`, le projet **« WF2 — Pont Business L2 (A3 Picard → B1 Jerry
→ B1 Summers) »** porte le statut `planned`. C'est exactement le chaînon qui
relierait la couche A (vivante, 43 agents) à la couche B (absente). Il n'a
jamais démarré.

## Revue humaine : 1 domaine sur 8

`70_Onthologies/_revue/` ne contient qu'un rendu :
`REVUE_70_Onthologies-pulse-domaines-aquaman.md`. Les sept autres domaines sont
en `confiance: machine`. La vague de revue du 2026-08-21 au matin s'est
effondrée sans rien produire — 429 sur tous les fournisseurs gratuits, puis
épuisement du commit mémoire Windows (`MEM_COMMIT failed, Win32 error 1455`).

## Correction du 2026-08-21 — la matérialisation est en aval d'un seuil

La première rédaction de cette note traitait l'absence des 26 agents B comme un
défaut à réparer. La doctrine `b2-areas-dormants-doctrine.md` (revue
`human:amdkn`, 2026-08-20) dit l'inverse : la matérialisation d'une squad B3
n'est exigée qu'au passage à l'état `ACTIVE`, planifiée à `T-30j`. En
`SHADOW_ACTIVE`, une squad non matérialisée est l'état **attendu**.

Les agents manquants ne sont donc pas une perte à combler en urgence. Ils sont
en aval d'un seuil client qui n'a pas été franchi.

**Le seuil, mesuré :** `30_Business_OS/10_Projects/coach-os/00_Summers_CEO/03_Master_Agreements/`
ne contient qu'un `README.md`. Aucun contrat signé. Le portail est
légitimement fermé, et Aquaman légitimement dormant sur les conditions 1 et 2.

**Le CEO Micro Fractal est installé** — `AGENT.md`, `ROCKS.md`, `SOUL.md` et
trois sous-dossiers (`01_Vision_Strategy`, `02_Global_Dashboard`,
`03_Master_Agreements`), chacun réduit à son `README.md`. Ce n'est pas lui qui
manque.

## Ce qui manque réellement : le journal Council

La condition 3 de la doctrine exige que le captain consigne sa dormance dans
`B2_DC_DIRECTION_COUNCIL_DECISIONS.md` via un paquet `decision: dormant`.

**Recherche sur ASpace_OS_V3 et ASpace_OS_V2 : le fichier n'existe nulle part.**
Zéro occurrence, sous ce nom ou un équivalent.

Et sur les huit `VP_AGENT.md` des domaines, **un seul déclare un état** :

| Domaine | État déclaré dans `VP_AGENT.md` |
|---|---|
| 08 Legal · Aquaman · Eternals | `dormant` |
| Les 7 autres | *(aucun état déclaré)* |

La doctrine tranche elle-même le cas, ligne 80 : *« Sans cette ligne, le captain
est en **absence**, pas en dormance. L'absence est un défaut opérationnel ; la
dormance est un acte documenté. »* Et ligne 121 : *« Un capitaine B2 qui ne
consigne pas sa dormance **devient** un capitaine absent. »*

**Sept capitaines sur huit sont donc en absence, pas en dormance.** Ce n'est pas
un jugement extérieur : c'est le verdict du texte appliqué à l'état du disque.

Le journal Council est l'artefact le moins coûteux de toute la chaîne — un
fichier markdown — et c'est le seul qui convertisse un défaut opérationnel en
état légitime, auditable et armé de déclencheurs.

**Posé le 2026-08-21** :
`30_Business_OS/10_Projects/coach-os/04_Business_Domains/B2_DC_DIRECTION_COUNCIL_DECISIONS.md`,
dix entrées, **aucune signée**.

## Le renversement : sept domaines ne sont pas éligibles à la dormance

En préparant ce journal, la condition 2 a été mesurée plutôt que supposée — et
elle contredit l'hypothèse d'une roue dormante.

`00_Summers_CEO/ROCKS.md` porte un **rock actif pour le cycle 2026-08** :
*« À la fin du mois, une première offre Coach OS a été rendue démontrable,
livrable et pilotable de bout en bout sans dépendre d'une personne nommée. »*

**Sept `SPRINTS.md` sur huit portent une ligne « rock hérité » remplie et
substantielle.** Seul `08_Legal` conserve le gabarit `<recopier ici…>`.

| Domaine | Rock hérité 2026-08 | Éligible dormance |
|---|---|---|
| 01 Green Lantern · RH | mandat écrit + titulaire + critère de sortie par rôle | non |
| 02 Batman · Ops | parcours de livraison exécuté une fois, bout en bout | non |
| 03 Flash · Product | offre spécifiée comme produit reproductible | non |
| 04 Martian Manhunter · Sales | un problème client reformulé et validé | non |
| 05 Superman · Growth | démonstration conforme à ce que la delivery a prouvé | non |
| 06 Wonder Woman · Finance | coût, prix, marge et métrique de retour chiffrés | non |
| 07 Cyborg · IT | environnement reproductible et observable | non |
| **08 Aquaman · Legal** | *(gabarit vide)* | **oui** |

Un rock hérité rempli invalide la condition 2. La doctrine est explicite : *« Un
domaine qui manque une seule [condition] n'est pas dormant — il est en attente,
et le captain doit produire. »*

**La roue n'est donc pas dormante.** Sept capitaines ont une cause de travail
reçue de Summers, non close. C'est de l'absence sous mandat, ce qui est un
diagnostic très différent — et bien plus actionnable — qu'une dormance
structurelle.

Corollaire pour l'outillage : pré-remplir huit paquets `decision: dormant`
aurait inscrit un mensonge dans le journal de gouvernance, et déclenché
exactement l'anti-piège nommé par la doctrine (*« dormance déclarée sans
signal »*). Mesurer la condition 2 avant d'écrire a évité cela.

**Il ne peut pas être rédigé par un tiers.** Doctrine, ligne 154 : *« B1 ne peut
pas déclarer dormant un domaine B2 sans l'accord du captain. La dormance est un
acte du captain, pas une décision B1 — B1 peut *demander* la dormance, pas
l'imposer. »* Le squelette du journal est outillable ; les huit paquets
`decision: dormant` sont un acte humain.

## Deux défauts de la doctrine elle-même

**Contradiction interne sur la condition 3.** Le corps du texte nomme
`B2_DC_DIRECTION_COUNCIL_DECISIONS.md` comme lieu de consignation. Le tableau
de l'exemple travaillé (ligne 135) coche pourtant la condition 3 en citant
`VP_AGENT.md`. Deux artefacts différents pour une même condition : selon la
ligne qu'on lit, Aquaman est dormant ou absent.

**La généralisation aux 7 autres domaines est une projection déclarée.** La note
de confiance du document le dit : *« seul Legal a un triplet dormant
explicite. »* Les trajectoires d'activation détaillées pour Green Lantern
(DORMANT / EN_ATTENTE / ACTIF) ou le `NON_FORCED` de John Jones sont des
extrapolations cohérentes, pas des triplets sourcés. Une synthèse qui les
présente au même niveau que la doctrine Aquaman surestime leur assise.

## Le graphe RDF et la distillation OKF ne se parlent pas

Trouvé par la revue Sonnet 5 du domaine Flash le 2026-08-21, 35 concepts sur 35 :

> *« Le corpus Flash ne mentionne à aucun moment le graphe RDF, les fichiers
> Turtle, ni le prédicat `instantiates`. Les 35 concepts s'appuient
> exclusivement sur `70_Onthologies/triplets/v3-business.jsonl` et sur des
> documents Markdown de synthèse — jamais sur une représentation Turtle/RDF
> explicite. »*

Les deux anomalies du graphe soumises à vérification — `product-domain` sans
triplet `instantiates`, et la squad sous deux URI (`entity:the-avengers` /
`entity:avengers`) — ne sont **ni confirmées ni contredites** par le corpus :
elles lui sont **invisibles**.

Le diagnostic de la revue va plus loin que la question posée :

> *« C'est un trou de traçabilité entre les deux couches (graphe Turtle vs
> distillation OKF), pas juste une lacune Flash. »*

**Conséquence pratique.** Vérifier une assertion du graphe en lisant les
concepts ne prouve rien, dans un sens comme dans l'autre. Les deux couches se
développent sans se citer : le `.ttl` peut dériver du markdown, ou l'inverse,
sans qu'aucune relecture ne le voie. Toute vérification de cohérence doit se
faire **directement sur les fichiers `.ttl`**.

Corollaire sur la source : les concepts citent `triplets/v3-business.jsonl`
(JSON Lines) alors que le graphe mesuré vit dans `triplets/*.ttl` (Turtle).
Deux formats de triplets coexistent, et la distillation n'en lit qu'un.

**Second trou, même revue.** Toute la description de la squad Avengers —
spécialités, effectif à 7, appariement avec Fantastic4 — repose sur des
projections à partir de noms canon Marvel et d'un patron générique
(`fifty-three-b3-agent-roster.md`). **Aucune fiche d'agent B3 individuelle n'a
jamais été lue.** Ce qui est cohérent avec la mesure du runtime : ces agents
n'existent pas dans le workspace vivant.

## Anti-pièges

- **Ne jamais conclure sur l'export du 2026-08-02.** Il a 19 jours et décrit un
  workspace qui a perdu la moitié de ses agents depuis. Interroger l'API.
- **`multica_export_*/` est un instantané daté, pas un état.** Le nom du dossier
  porte la date : la lire avant de s'en servir.
- **Un champion cherché par son alias humain donne un faux négatif** (cas John
  Jones / Martian Manhunter). Chercher par `*-owner` ou par `*-domain`.
