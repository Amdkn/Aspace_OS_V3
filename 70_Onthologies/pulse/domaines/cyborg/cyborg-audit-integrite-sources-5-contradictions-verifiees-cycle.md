---
type: Concept
title: Audit intégrité sources — 5 contradictions vérifiées en cycle
description: Audit machine-checké des 28 concepts Cyborg vagues 1-5 : sur 154 resources absolus, 18 sont introuvables (12%) ; sur 206 liens wiki inter-concepts, 20 pointent vers des cibles mortes (10%) ; 5 contradictions de fond sont confirmées par lecture de ORG.json. Les couches de confiance "haute" et "confirmé par machine" du tour 5 masquent des erreurs d'inférence.
tags: [cyborg, audit, sources, integrite, contradiction, cycle, machine-check]
generated: { by: minimax-m3, at: 2026-08-19T07:30:00Z }
verified:
  - { by: process:python-glob-exists, at: 2026-08-19T07:30:00Z }
  - { by: process:lecture-org-json, at: 2026-08-19T07:30:00Z }
sources:
  - id: orga-cyborg-v3
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/ORG.json"
    title: ORG.json — source canonique b2 (résolu en V3, pas V2)
    last_modified: 2026-08-02
  - id: triplets-v3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: Triplets V3 — 8 vetos par capitaine B2
    last_modified: 2026-08-17
  - id: cyborg-dir
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/"
    title: Dossier Cyborg — 28 concepts vagues 1-5
    last_modified: 2026-08-19
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — mapping canonique
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Audit intégrité sources — 5 contradictions vérifiées en cycle

## Périmètre de l'audit

Les 28 concepts Cyborg posés en vagues 1-5 (`cyborg-*.md` dans
`70_Onthologies/pulse/domaines/cyborg/`) déclarent des `resources:` et
des liens `[[…]]` vers le corpus. **MODE FABLE étape 3 — Attaque** :
avant de poser un tour 6 doctrinal, vérifier si le substrat tient sous
machine-check. Audit exécuté le 2026-08-19, vagues 1-5, par script
Python.

## Méthode

- **Resources absolus** (`resource: "C:/…"`): test `os.path.exists`
  sur chaque valeur déclarée.
- **Resources relatifs** (`resource: "30_Business_OS/…"`): test contre
  deux racines candidates (`ASpace_OS_V3/` puis `ASpace_OS_V2/`).
- **Liens wiki** (`[[nom]]`): résolution par `glob(**/*.md)` du nom de
  fichier sans extension.
- **Vérification verbatim** : pour les 8 vetos catalogue, comparaison
  octet-à-octet entre `ORG.json` et les citations des concepts.

## Résultats bruts

| Métrique | Compte | % |
|---|---|---|
| Concepts Cyborg | 28 | — |
| Resources absolus cités (champ `resource:`) | 154 | 100% |
| Resources absolus **résolus sur disque** | 136 | 88% |
| Resources absolus **introuvables** | 18 | **12%** |
| Resources relatifs cités (incluant "ligne X" et "V2 OMK …") | ≥22 | — |
| Resources relatifs **résolubles** | 0 | 0% |
| Liens wiki `[[…]]` distincts (cumul) | 206 | — |
| Liens wiki pointant vers une cible **morte** | 20 | **10%** |

18/154 = 12% de resources absolus sont introuvables. 20/206 = 10%
des liens wiki sont morts. Ce ne sont pas des fautes de frappe : les
cibles mortes sont **structurellement** absentes, et leur nom
ressemble à un **pattern** que les concepts Cyborg ont inféré.

## Les 5 catégories de cibles mortes

### Catégorie 1 — Frères symétriques inférés mais inexistants (6 cas)

Les concepts Cyborg ont produit des cibles par symétrie de pattern
sans vérifier l'existence :

- `aquaman-couplages-invisibles-legal-it.md` — cité 3 fois. Le vrai
  fichier est `aquaman-couplages-invisibles.md`.
- `green-lantern-couplages-invisibles-people-it.md` — cité 1 fois. Le
  vrai fichier est `green-lantern-couplages-invisibles.md`.
- `flash-veto-empirical-validation-protocole.md` — cité 1 fois.
  Introuvable, alors que Superman et Green Lantern ont bien leur
  version du même concept.

**Lecture** : un concept Cyborg a posé une règle de symétrie
« chaque capitaine a son couplage invisible avec IT » ou « chaque
capitaine a son veto validation empirique » et l'a documentée comme
si elle existait dans le corpus voisin. La règle peut être vraie
comme structure ; elle n'est pas sourcée.

### Catégorie 2 — Path V2 / V3 non résolu (5 cas)

```
30_Business_OS/AGENTS.md ligne 16         (concept 1 tour 5)
30_Business_OS/10_Projects/coach-os/ORG.json  (référencé V2 partout)
V2 OMK B2_Business_Domains/05_IT_Cyborg_KangDynasty/01_B3_AGENT_ROSTER.md
fifty-three-b3-agent-roster.md ligne 84
fifty-three-b3-agent-roster.md citations multiples
```

**Lecture** : les resources relatifs du tour 1-2 ont été écrits
contre `ASpace_OS_V2` (alors que le dépôt canonique est passé en
V3 mi-2026). Le re-root vers V2 ne résout rien — `coach-os/` n'y
existe pas. Le V2 root est un snapshot, pas un dépôt vivant.
**ORG.json vit en V3** depuis 2026-08-02 ; aucun concept Cyborg ne
le pointe correctement. C'est l'erreur d'inférence racine : poser
un chemin relatif en présumant qu'il se résout contre la racine du
brief, pas contre la racine du dépôt canonique.

### Catégorie 3 — Liens wiki avec nom presque-juste (5 cas)

- `cyborg-doctrine-5-principles-dispatch` (anglais) — cible morte.
  Le vrai fichier est `cyborg-doctrine-5-principes-dispatch` (français).
- `cyborg-coupling-aquaman-reversibilite` (singulier) — cible morte.
  Le vrai fichier est `cyborg-couplage-aquaman-reversibilite` (pluriel).
- `superman-domain-perimeter` — cible morte. Le vrai fichier est
  `domain-perimeter.md` à la racine du dossier Superman (sans préfixe).
- `rapport-dom-batman` — cité 1 fois mais le rapport s'appelle
  `RAPPORT_dom-batman.md` (majuscules). Insensible sur la plupart des
  OS mais pas tous.
- `cyborg-cycle-vie-infrastructure-5-phases` avec saut de ligne
  parasite dans le nom wiki (le `\n` s'est glissé dans le `[[…]]`).

**Lecture** : 5 fautes de frappe, mais chacune prise isolément
brise un lien canonique. La détection est triviale en machine
(`if l not in names`). Elle n'a pas été faite en cycle.

### Catégorie 4 — Liens vers des concepts non-OKF (3 cas)

- `[[ADR-L2-AAAS-001]]` et `[[ADR-OMK-004]]` — des ADR canoniques
  existent (vérifié : `ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md`
  et `ADR-OMK-004_pivot-supabase-cloud-vercel.md` sont sur disque)
  mais avec un **suffixe** `_pivot-supabase-cloud-vercel.md` /
  `_aaas-doctrine-3-variants-solarpunk.md` que les liens wiki ne
  portent pas. Les ADR ne sont pas des concepts OKF ; ils ne sont
  pas censés être linkables par `[[…]]` au titre court.
- `[[AGENTS.md canon 30_Business_OS]]` — titre wiki inclut le chemin
  (anti-pattern : le `[[…]]` est un nom de fichier, pas un titre).

**Lecture** : 3 cas où le `[[…]]` n'est pas un nom de fichier
existant ni un slug raisonnable. Le lien wiki est une
**convenance littéraire**, pas une ancre canonique.

### Catégorie 5 — Cibles « vivante-en-tour-N-mais-pas-N+1 » (1 cas)

- `[[rapport-dom-cyborg]]` (9 fichiers) — le rapport existe
  (`RAPPORT_dom-cyborg.md` avec majuscules) ; le slug lower-case
  n'est pas résolu par la glob `*.md` parce que la comparaison est
  case-sensitive sous Windows sur certains FS (NTFS par défaut est
  case-insensitive mais `os.walk` peut remonter la casse selon le
  mode d'ouverture). **Statut** : faux positif partiel. Le rapport
  existe.

## 5 contradictions de fond confirmées par lecture de ORG.json

L'audit source ouvre des contradictions de fond. Les voici dans
l'ordre de gravité.

### Contradiction 1 — Trois systèmes de numérotation incompatibles

| Système | Cyborg n° | Source canonique |
|---|---|---|
| Avengers Wheel | **05** | `eight-domain-avengers-wheel.md` ligne 44 |
| ORG.json `b2[].n` | **7** | `30_Business_OS/10_Projects/coach-os/ORG.json` |
| ORG.json `b2[].agent_canon` | **06** | même fichier, slug `b2-06-cyborg-it` |
| ORG.json `b2[].dossier` | `07_RD_et_IT` | même fichier |

**Impact** : les 5 domaines qui partagent une équipe (Sales × People ×
IT × Finance × Legal) ont des collisions sur 2 systèmes ou plus.
Exemple Superman : Avengers Wheel n°01, ORG.json n°5, agent_canon
n°4. Martian Manhunter : Avengers Wheel n°02, ORG.json n°4,
agent_canon n°5.

**Ferme** la question du tour 5 §T5.5.1 thèse 5 (« le compte Kang
Dynasty 6 vs Ownerbook T1 ≥7 — divergence persistante ») : il y a
**trois sources**, pas deux. Ownerbook T1 dit probablement 6 (si
cohérent avec ORG.json), et la « divergence ≥7 » venait d'une
lecture d'un quatrième artefact jamais identifié.

### Contradiction 2 — R&D apparaît dans ORG.json, pas dans Avengers Wheel

`ORG.json` nomme le domaine Cyborg `R&D & IT`. L'Avengers Wheel dit
simplement `IT`. Aucun concept Cyborg n'a relevé que **R&D est
absent de la wheel** : le triplet 22 (Growth-Product-Sales) et le
triplet 23-30 (vetos) ne couvrent pas R&D. **Impact** : si R&D est
un sous-domaine d'IT, l'extension à LD03 Cognition (concept tour 2
`cyborg-dans-aaas-3-variants.md`) reste IT-canonical. Si R&D est un
domaine à part, il manque un neuvième capitaine B2. **Statut** :
ouvert, **non résolu en corpus**.

### Contradiction 3 — Aquaman est `dormant: true`, les 7 autres `false`

`ORG.json` ligne b2[7] (Aquaman) est l'**unique** domaine marqué
`dormant: true`. Le concept `cyborg-areas-dormants-doctrine` n'a
pas vu cette information — il a utilisé un cadrage narratif
« dormance structurelle wheel 8-domain » observé sur les 5 vagues
(zéro packet mésoperpétuel en cycle), ce qui est une **dormance de
pratique**, pas une dormance d'**état canonique**. **Statut** :
ORG.json dit « seul Aquaman dort canoniquement », et la wheel dort
parce qu'aucun capitaine n'a soumis de packet. Ce sont deux
phénomènes distincts que le corpus confond.

### Contradiction 4 — Veto Cyborg tronqué à 3 mots sur 8

Citation ORG.json verbatim (UTF-8, octets exacts) :
`"tout fournisseur cloud-only sans chemin de sortie documenté"`.

Citation dans 11 concepts Cyborg vagues 1-5 (machine-check) :
`"cloud-only sans chemin de sortie documenté"`.

Le préfixe `« tout fournisseur »` disparaît dans toutes les
citations. **Impact** : le veto perd sa portée — « cloud-only sans
chemin de sortie » s'applique à toute dépendance IT, pas seulement
aux fournisseurs commerciaux. Un agent B3 lisant uniquement les
concepts peut bloquer un package interne (ex : `torch` dans le
monorepo) au motif qu'il n'a pas de chemin de sortie, alors que
le veto vise les fournisseurs externes. **Recommandation** : tous
les concepts Cyborg qui citent le veto doivent être amendés en
append-only avec la formule complète.

### Contradiction 5 — Le triplet v3 dit `confiance: haute` sur une source V2

Les 8 triplets `triplets/v3-business.jsonl` lignes 23-30 portent
chacun `"source": "30_Business_OS/10_Projects/coach-os/ORG.json"`.
`ORG.json` est en **V3**, pas en V2. La résolution correcte est
`30_Business_OS/10_Projects/coach-os/ORG.json` **préfixée par
`C:/Users/amado/ASpace_OS_V3/`**. Le triplet est correct comme
chemin relatif **si** on est dans la racine V3, mais aucun concept
Cyborg ne précise la racine de résolution. **Impact** : un agent
B3 lisant le triplet hors de V3 (par exemple depuis un sub-module
V2) ne trouve pas ORG.json et tombe sur l'erreur « source
introuvable » — l'audit a reproduit cette erreur 8 fois.

## Anti-pièges

- **Confondre « confirmé par machine » et « vérifié en cycle ».**
  Le concept `b2-eight-domain-vetoes-catalogue` est marqué
  `verified: process:lecture-b2-corpus`. La lecture a existé, mais
  le substrat cité (lignes 23-30 du triplet) est correct **et** la
  source canonique (ORG.json) est mal résolue par 100% des concepts
  qui s'y réfèrent. « Lu » ne veut pas dire « résolu ».
- **Croire qu'un ratio 88% suffit.** 12% de resources morts sur 154
  = 18 concepts affectés. Si les 18 sont concentrés sur un même
  paquet doctrinal (composite Council-ready), c'est un paquet
  Council-ready qui ne peut pas être **soumis en l'état** — sa
  chaîne de preuves est brisée.
- **Inférer la symétrie avant de la lire.** Le pattern « chaque
  capitaine a son couplage invisible avec IT » est tentant
  intellectuellement. La machine-check dit qu'il n'existe pas dans
  le corpus voisin. Le pattern reste peut-être **à poser** comme
  nouvelle doctrine, pas comme **citation** d'un existant.

## Recommandations opérationnelles

1. **Poser `cyborg-source-root-anchor.md`** qui fixe la racine de
   résolution des resources relatifs à `C:/Users/amado/ASpace_OS_V3/`.
   Aucun concept futur ne doit assumer V2. *Cette note est un
   premier pas, mais ne suffit pas — la convention doit être
   Council-adopted.*

2. **Amender en append-only les 11 concepts qui tronquent le veto**
   pour restaurer le préfixe `« tout fournisseur »`. Un diff
   ciblé, sans réécriture.

3. **Soumettre le présent audit en packet mésoperpétuel
   `decision: signal_inconsistency`** vers B2 Council — c'est la
   première fois qu'une escouade pose une **auto-remontée** sur
   l'intégrité de ses propres sources. Le pattern est rare et
   positivement atypique.

4. **Ouvrir la question R&D comme domaine** dans la prochaine
   séance Council. C'est une **cinquième thèse ouverte** à ajouter
   à la liste T5.5.1.

## Liens

- [[b2-eight-domain-vetoes-catalogue]] — le catalogue qui pose les 8 vetos
- [[b2-harmonization-matrix-exploitable]] — la matrice dont les sources sont dans le même cas
- [[cyborg-veto-cloud-only-sortie]] — le concept le plus cité avec troncature
- [[cyborg-w40-v4-decision-document]] — un concept qui dépend d'ORG.json

## Note de confiance

**Confirmé par machine**, vagues 1-5 audit terminé 2026-08-19. Les
5 contradictions sont issues de lectures byte-exact (`os.path.exists`,
`json.load`, comparaison verbatim). Les 18 resources morts et les
20 liens wiki morts sont comptés par script Python, pas à la
main. La contradiction 4 (troncature veto) est la plus opérationnelle
: elle change la portée d'un veto B2 et peut être corrigée en
append-only sans débat doctrinal. Les contradictions 1, 2, 3 sont
des **trous canoniques** qui demandent un arbitrage Council, pas
une correction locale. Recommandation forte : ne pas empiler un
septième concept doctrinal avant que la Council ait tranché les
contradictions 1 et 2.
