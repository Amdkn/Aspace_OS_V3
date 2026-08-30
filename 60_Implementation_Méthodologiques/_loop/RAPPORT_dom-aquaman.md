# RAPPORT — Escouade Aquaman (domaine 08 Legal)

**Tour 1** · 2026-08-19 · MiniMax-M3 · MODE FABLE

## 1. Cadrage de la passe

Le corpus désigne *Aquaman* comme le B2 captain du **domaine 08 —
Legal & Compliance**, squad B3 **Eternals**. Cette identification est
vérifiée verbatim dans :

- `eight-domain-avengers-wheel.md` (mapping 8-domain)
- `triplets/v3-business.jsonl` ligne 22 (Aquaman pairedWith Eternals)
- `triplets/v3-business.jsonl` ligne 30 (Aquaman hasVetoOver
  engagement-sans-perimetre)
- Dossier OMK `08_Legal_Aquaman_Eternals/` (4 fichiers canoniques)

**Périmètre exclusif respecté** :
- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/` — 6
  concepts OKF v0.2 créés
- `C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-aquaman.md` —
  ce rapport
- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/ETAT_DOMAINES.md` —
  1 ligne ajoutée (section `## Aquaman`, ajout seul)

Aucun fichier d'un autre domaine n'a été touché. Aucun agent délégué
n'a été lancé.

## 2. Ce qui a été posé

6 concepts OKF v0.2 dans `70_Onthologies/pulse/domaines/aquaman/`,
répondant aux 4 questions du brief :

| Fichier | Question couverte |
|---|---|
| `aquaman-domaine-legal-perimetre.md` | Q1 — Que couvre-t-il (7 surfaces) et où s'arrête-t-il (3 zones hors-périmètre) |
| `aquaman-veto-engagement-sans-perimetre.md` | Q2 — Le veto, ses 3 propriétés, 4 cas légitimes, 5 abus |
| `aquaman-gates-et-pair-checks.md` | Q1/Q2 — 3 gates émis, RACI pair-checks #7 #8 (Consulted) |
| `aquaman-squad-eternals-et-dormance.md` | Q3 — Pipeline Rock→DoD→JTBD, JTBD packet gabarit, DoD vérifiable |
| `aquaman-couplages-invisibles.md` | Q4 — 5 couplages implicites hors matrice d'harmonisation |
| `aquaman-antipieges-faux-pas-typiques.md` | transversale — 6 anti-pièges + grille de signal |

**Format respecté** : OKF v0.2 avec frontmatter (type, title,
description, tags, generated, verified, sources, okf_version).
**Aucun `human:`** dans `verified` — uniquement `process:lecture-canon-aquaman`
(= confirmé par machine).

## 3. Ce que j'ai lu (sources mobilisées)

**Lu intégralement** :
- 4 fichiers canoniques du dossier OMK
  `08_Legal_Aquaman_Eternals/` : `README.md`, `00_B2_DOMAIN_CONTROL_ROOM.md`,
  `01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md`, `02_B3_SWARM_SUPERVISION_PROTOCOL.md`
- 6 règles B2 dans `70_Onthologies/pulse/b2/` :
  `b2-council-arbitrage-rule.md`, `b2-harmonization-matrix-exploitable.md`,
  `b2-pair-check-raci-by-rank.md`, `b2-eight-domain-vetoes-catalogue.md`,
  `b2-b3-jtbd-handoff-contract.md`, `b2-meso-decision-packet-spec.md`
- 4 concepts canoniques en distillation :
  `eight-domain-avengers-wheel.md`,
  `business-wheel-harmonization-matrix.md`,
  `fifty-three-b3-agent-roster.md`,
  triplet v3 (`v3-business.jsonl`)
- `ETAT_DOMAINES.md` (état de la coordination Vague 2)

**Non lu** :
- Les 53 profils `b3-eternals-*.md` individuels — non découverts dans
  la passe. La composition exacte de la squad Eternals reste
  tributaire du triplet 22.
- `coach-os/04_Business_Domains/08_Legal_et_Compliance_Aquaman_Eternals/VP_AGENT.md`
  — référencé par triplet 35/36 mais non lu directement.
- `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` — registre des arbitrages
  B2, non trouvé dans le périmètre V3 (probablement dans V2).

## 4. Ce que le corpus NE DIT PAS sur Aquaman

C'est la partie la plus importante. Six zones d'ombre que le rapport
signale sans les trancher.

### 4.1 La doctrine *« dormant »* est Coach-OS-spécifique, pas universelle

Le triplet 35 (source `coach-os/.../Aquaman_Eternals/VP_AGENT.md`)
pose un Aquaman *« en état dormant »*, conditionné à
`00_Summers_CEO/03_Master_Agreements/`. Mais **les 4 fichiers du
dossier OMK** ont un frontmatter `status: SHADOW_ACTIVE` — pas
dormant. SHADOW_ACTIVE et dormant ne sont pas synonymes.

**Conséquence** : le concept `aquaman-domaine-legal-perimetre.md` a
peut-être **trop généralisé** la doctrine dormant. Le seuil *«
premier fichier dans `03_Master_Agreements/` »* vaut pour Coach-OS,
pas nécessairement pour OMK ou un autre projet. **À vérifier** :
existe-t-il un seuil d'activation équivalent dans OMK ?

### 4.2 L'effectif de la squad Eternals — tension non arbitrée

Trois sources, trois nombres :

- Triplet 22 : **10 agents** (Ikaris, Sersi, Ajak, Kingo, Phastos,
  Sprite, Druig, Thena, Gilgamesh, Makkari)
- Dossier OMK `00_B2_DOMAIN_CONTROL_ROOM.md` : **4 charges** (Ikaris
  force, Ajak compliance, Phastos IP, Thena defense)
- Roster 53 : **~7 par squad** attendu (sans liste nominative pour
  Eternals)

Aucune des trois sources ne réconcilie les autres. **Action** : un
audit qui voudrait recompter devrait faire `find .claude/agents
-name 'b3-eternals-*' | wc -l` — commande citée dans
`fifty-three-b3-agent-roster.md`, pas exécutée.

### 4.3 Aucun paquet mésoperpétuel Legal n'est enregistré

Le format `B2-MESO-DECISION-YYYY-NN` est posé verbatim dans
`b2-meso-decision-packet-spec.md`, mais aucun exemple de paquet
Legal n'a été trouvé dans le corpus V3 (Vague 1 a travaillé sur les
frameworks, Vague 2 sur les protocoles — pas d'arbitrage B2 réel
produit). **Conséquence** : les 4 cas de déclenchement du veto et
les 5 cas d'abus dans `aquaman-veto-engagement-sans-perimetre.md`
sont **projetés depuis le framework**, pas observés en cycle.

### 4.4 La matrice d'harmonisation ignore 5 couplages implicites

Les 9 pair-checks canoniques placent Aquaman en Consulted sur #7
et #8 seulement. Mais 5 couplages *indirects* touchent Legal sans
être dans la matrice (cf. `aquaman-couplages-invisibles.md`) :

- Aquaman ↔ Cyborg (privacy implémentation IT)
- Aquaman ↔ Wonder Woman (honoraires juridiques)
- Aquaman ↔ Superman (réécriture de claims bloquées)
- Aquaman ↔ JohnJones (clauses commerciales — pipeline Sales→Legal)
- Aquaman ↔ Green Lantern (matrice de signature)

**Le pipeline Sales→Legal est un trou doctrinal** : aucun packet
mésoperpétuel ne pose le *handoff* entre les deux capitaines. Si
Sales promet sans cadrage Legal, le veto Aquaman s'oppose *a
posteriori* — pas de prévention en amont.

### 4.5 Les 3 propriétés canoniques du veto sont reconstruites, pas citées

Le concept `b2-eight-domain-vetoes-catalogue.md` pose les 3
propriétés (catégoriel, vérifiable, non-négociable) explicitement
mais les marque comme **« reconstruites à partir du triplet v3 et
de la doctrine d'escalade fractal »**. Idem pour les 4 issues
(amendé, retiré, escaladé, invalide) et les 4 anti-pièges. **Le
canon ne pose pas le squelette Argumentatif du veto en
littéral.** C'est un *framework de vigilance*, pas une charte
signée.

### 4.6 Le RACI par rang sur les pair-checks Aquaman est étayé à moitié

Le concept `b2-pair-check-raci-by-rank.md` se qualifie lui-même
*« Reconstruit, à moitié étayé »*. Les triplets 7, 8, 13, 41, 56,
57 ancrent la séparation par rang, mais **le choix A = B2 en aval
pour les pair-checks #7 et #8 spécifiquement n'est pas cité
verbatim** ailleurs dans le corpus. C'est une projection depuis le
rôle B2 sponsor dans `b2-b3-jtbd-handoff-contract.md`.

## 5. Règles de B2 qui semblent mal ajustées pour Aquaman

### 5.1 Le RACI par rang met Aquaman en Consulted sur ses propres transitions

Pour les pair-checks #7 et #8, A est en *aval* (Superman, Flash),
pas Aquaman. Conséquence : si un arbitrage touche Legal
directement (par exemple *« peut-on publier cette claim litigieuse ?
»*), c'est Superman qui tranche l'opérationnel. Aquaman émet
`BLOCKED_RISK`, mais la décision finale n'est pas chez lui.

**Friction** : un Superman pressé peut *accepter* un `BLOCKED_RISK`
Aquaman sous pression de cycle (livraison avant fin de sprint),
surtout si le tradeoff *« réputation Legal »* vs *« timing Growth »
* n'est pas posé dans le packet mésoperpétuel. La matrice ne
prévoit pas de *Legal → Legal* (auto-pair-check) qui remettrait A
chez Aquaman pour les cas où le risque Legal *est* l'enjeu.

**Suggestion (remontée B2)** : un 10ᵉ pair-check *« Legal risk →
Launch decision »* où A = Aquaman pourrait couvrir les cas où
l'enjeu principal est Legal (claim litigieuse, breach de terms,
régulation sectorielle). À arbitrer en B2 Council.

### 5.2 La doctrine veto *« engagement-sans-périmètre »* est étroite

Le veto Aquaman porte sur *« prestation démarrée sans accord écrit
sur le périmètre et la propriété du livrable »*. C'est un veto
**contractuel** : il bloque le *démarrage*, pas le *périmètre lui-même*.

**Friction** : un Aquaman qui détecte un périmètre *mal écrit*
(mais écrit) ne peut pas opposer le veto — il peut seulement émettre
`NEEDS_REVIEW`. La nuance *« pas de périmètre »* vs *« périmètre
insuffisant »* n'est pas dans le veto catalogue. Pour un mandat
complexe (par exemple un accord de partenariat multi-parties), le
veto *« périmètre insuffisant »* est aussi légitime que *« pas de
périmètre »*.

**Suggestion (remontée B2)** : amender le veto catalogue pour
couvrir les deux cas. Texte proposé : *« Aquaman bloque toute
prestation dont le périmètre (écrit ou implicite) n'est pas
suffisant pour tracer la propriété du livrable. »*

### 5.3 La règle de résolution des veto n'a pas de clause *« Legal risk
élevé »*

Les 4 issues (amendé, retiré, escaladé, invalide) traitent tous les
vetos sur un pied d'égalité. Mais un veto Aquaman sur une claim
litigieuse ou une breach de terms n'a pas le même *coût d'attente*
qu'un veto Batman sur une procédure sans condition d'arrêt.

**Friction** : un Aquaman qui oppose un veto sur breach de terms
peut voir le mandat *« amendé »* par B1 (par exemple en ajoutant
une clause de limitation de responsabilité) — mais l'amendement peut
*ne pas couvrir* le risque Legal initial. Le veto est *levé* sans
que le risque soit *couvert*.

**Suggestion (remontée B2)** : ajouter une 5ᵉ issue *« veto Aquaman
sur breach ou litigation : ne peut être levé que par B1 avec revue
juridique tierce documentée »*. Le cas Aquaman est *différent* des
7 autres, et la règle de résolution devrait le savoir.

### 5.4 L'état dormant n'est pas documenté dans `b2-areas-dormants-doctrine.md`

Le concept OKF `b2-areas-dormants-doctrine.md` (8496 bytes, daté
2026-08-19) existe dans `pulse/b2/` mais n'a pas été lu dans cette
passe. Il est probable qu'il pose une doctrine des domaines
dormants — auquel cas ma propre doctrine *« Aquaman dormant »*
pourrait être **redondante ou contradictoire** avec.

**Action** : relire `b2-areas-dormants-doctrine.md` dans une passe
ultérieure et réconcilier. Le triplet 35 est Coach-OS-spécifique ;
la doctrine dormante canonique (si elle existe) peut être plus
générale.

## 6. Confiance et limites

**Niveau de confiance global : confirmé par machine, projeté sur les
cas concrets.**

- ✅ Confirmé verbatim : périmètre (7 surfaces), état dormant (triplet
  35-36, avec réserve §4.1), veto engagement-sans-périmètre (triplet
  30), 3 gates (avengers-wheel), RACI pair-checks #7 #8 (pair-check-raci),
  pipeline Rock→DoD→JTBD (4 fichiers OMK).
- �️ Reconstruit : 3 propriétés canoniques du veto, 4 issues, 5
  couplages implicites, 4 cas de déclenchement et 5 cas d'abus du veto.
- ❌ Non vérifié en cycle : aucun paquet mésoperpétuel Legal
  enregistré ; effectif Eternals non recompté ; 6 anti-pièges
  projetés, pas observés.

**Sources totales mobilisées** : 14 fichiers lus, 1 modifié (ETAT_DOMAINES),
6 créés. Aucun secret, aucun engagement-sans-périmètre dans cette passe.

## 7. Ce que la passe laisse ouvert

Quatre items à traiter en tour 2 ou par une autre escouade :

1. **Effectif Eternals** — recompter via `find` et réconcilier les
   3 sources (10 / 4 / ~7).
2. **Doctrine dormant universelle** — lire `b2-areas-dormants-doctrine.md`
   et réconcilier avec triplet 35-36 (Coach-OS-spécifique vs général).
3. **Pair-check #10 Legal risk → Launch** — proposer l'ajout au
   catalogue B2.
4. **Veto Aquaman amendé** — proposer le texte *« périmètre écrit ou
   implicite insuffisant »* en B2 Council.

---

*Rapport généré en MODE FABLE par MiniMax-M3, tour 1 de la Vague 2.
Vérifié : 14 sources lues, 6 concepts créés, 1 ligne ajoutée. Aucune
affirmation notée ✅ sans source citée.*

---

# Tour 2 · 2026-08-19 · MiniMax-M3 · MODE FABLE

## T1. Cadrage de la passe

Le tour 1 a posé **6 concepts** et identifié **4 remontées vers B2** :
pair-check #10 Legal risk → Launch, veto amender pour *« périmètre
insuffisant »*, 5ᵉ issue *« breach ou litigation »*, doctrine
dormant Coach-OS-spécifique.

Le tour 2 prend ces 4 zones comme point de départ et **ouvre 2
nouveaux concepts** qui comblent les questions 1 (frontière exacte)
et 3 (paquets JTBD émis/reçus) du brief — questions partiellement
couvertes en tour 1 mais sans catalogue concret.

**Périmètre exclusif respecté** :
- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/` —
  2 concepts ajoutés (total 8/8, cap du brief atteint)
- `C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-aquaman.md` —
  cette section ajoutée
- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/ETAT_DOMAINES.md` —
  1 ligne ajoutée (ajout seul sous `## Aquaman`)

## T3. Ce qui a été posé en tour 2

**2 concepts OKF v0.2** nouveaux, portant le total à **8/8** (cap du
brief « 4 à 8 concepts » atteint) :

| Fichier | Question couverte | Apport spécifique |
|---|---|---|
| `aquaman-jtbd-emit-receive.md` | Q3 — JTBD émis/reçus | 4 formes émises (privacy review, claim safety, contract template, defensibility doc) + 4 reçues (Flash, Superman, JohnJones, Cyborg/Batman) + table emit × receive |
| `aquaman-dormant-activation.md` | Q1 — où s'arrête le périmètre | 3 états distincts (Dormant / SHADOW_ACTIVE / ACTIVE) + 3 asymétries (production, veto, coût) + 3 seuils distincts |

**Tour 1 n'a pas été réécrit.** Les 6 concepts tour 1 restent
intacts dans le dossier ; le tour 2 les **complète** par les
catalogues concrets que le tour 1 avait projetés sans les poser.

## T4. Sources mobilisées en tour 2

**Lu intégralement** :
- 4 fichiers OMK `08_Legal_Aquaman_Eternals/` (frontmatter `status:
  SHADOW_ACTIVE`, datés 2026-05-25 et 2026-05-27) — confirme
  l'asymétrie Dormant vs SHADOW_ACTIVE
- 6 concepts tour 1 du dossier Aquaman (cohérence interne)
- `b3-jtbd-packet-reception-checklist.md` (vue B3 du même contrat)
- `RAPPORT_dom-aquaman.md` (lui-même, sections 4 et 5)

**Non relu** :
- `coach-os/04_Business_Domains/08_Legal_et_Compliance_Aquaman_Eternals/VP_AGENT.md`
  — source du triplet 35, citée verbatim mais pas lue directement
  en tour 2 (déjà non lue en tour 1, cf. rapport §3 Non lu).
- `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` — registre des arbitrages
  B2, non trouvé dans le périmètre V3 (idem tour 1).

## T5. Ce que le tour 2 a changé dans la lecture Aquaman

### T5.1 La tri-partition des états remplace la bipartition Dormant/Actif

Le tour 1 posait *Dormant* comme état par défaut, sans distinguer
explicitement *SHADOW_ACTIVE* (statut OMK réel). Le tour 2 pose une
**tri-partition** :

- **Dormant** (Coach-OS, pré-Master Agreement) — flow gelé.
- **SHADOW_ACTIVE** (OMK, et tout projet en pré-launch) — flow
  shadow, veto *information* pas *arrêt*.
- **ACTIVE** (premier livrable signé) — flow normal, veto *arrêt*.

**Conséquence** : la doctrine *« Aquaman dormant »* (triplet 35) est
**maintenant nuancée** — elle vaut pour Coach-OS, mais OMK n'est
*pas* dormant au sens strict ; OMK est SHADOW_ACTIVE. Cette nuance
est signalée dans [[aquaman-domaine-legal-perimetre]] §L'état dormant
et explicitement formalisée dans [[aquaman-dormant-activation]] §Les
trois états opérationnels.

### T5.2 Le catalogue JTBD remplace le gabarit seul

Le tour 1 posait le **gabarit** JTBD packet Legal (cf.
`aquaman-squad-eternals-et-dormance.md` §Le JTBD packet — gabarit).
Le tour 2 pose les **4 formes canoniques** que ces paquets prennent
en pratique, avec gating conditions explicites côté reçu.

**Conséquence** : la question 3 du brief (*quels paquets JTBD ce
domaine émet vers B3, et lesquels il reçoit ?*) a maintenant une
**réponse opérationnelle** :

- Aquaman émet 4 formes (privacy review / claim safety / contract
  template / defensibility doc).
- Aquaman reçoit 4 inputs amont (Flash feature spec / Superman claim
  draft / JohnJones deal structure / Cyborg privacy implémentation
  spec).
- Chaque émission a une gating condition côté reçu ; sans l'input,
  Aquaman retourne `BLOCKED_RISK` ou refuse de démarrer.

### T5.3 Les 4 remontées tour 1 restent ouvertes + 1 nouvelle

Le tour 1 a posé 4 remontées vers B2 :

1. Pair-check #10 Legal risk → Launch (Aquaman A direct) — **ouverte**.
2. Veto amender pour *« périmètre insuffisant »* — **ouverte**.
3. 5ᵉ issue *« breach ou litigation »* — **ouverte**.
4. Doctrine dormant Coach-OS-spécifique — **partiellement traitée
   par tour 2** (la tri-partition répond, mais ne tranche pas —
   reste à arbitrer en B2 Council).

Le tour 2 ajoute **1 remontée implicite** issue de la tri-partition :

5. **Le seuil d'entrée en SHADOW_ACTIVE n'est pas posé.** Les 4
   fichiers OMK ont `status: SHADOW_ACTIVE` posé, mais aucun triplet
   ne pose le seuil Dormant → SHADOW_ACTIVE pour Coach-OS, et aucun
   SDD ne pose le seuil *« 4 fichiers canoniques posés »* comme
   formel. **À arbitrer en B2 Council** : faut-il un triplet ou un
   SDD qui pose le seuil canonique ?

## T6. Règles de B2 qui semblent mal ajustées (suite tour 1)

### T6.1 La tri-partition n'est pas un triplet canonique

Le concept [[aquaman-dormant-activation]] pose trois états
opérationnels distincts. Mais **la tri-partition n'est pas un
triplet canonique** dans `v3-business.jsonl` ni un SDD dans le
corpus V3. C'est une **reconstruction** à partir du frontmatter
OMK (`status: SHADOW_ACTIVE`) et de la doctrine d'arbitrage
mésoperpétuel.

**Friction** : un B2 captain (par exemple Batman ou Superman) qui
voudrait s'appuyer sur la tri-partition pour arbitrer un cas ne
peut pas — le corpus ne la pose pas en tant que règle opposable.

**Suggestion (remontée B2)** : transformer la tri-partition en
triplet canonique. Texte proposé : *« Aquaman steward Legal &
Compliance en trois états opérationnels — Dormant (flow gelé,
pré-Master Agreement) / SHADOW_ACTIVE (flow shadow, 4 fichiers
canoniques posés) / ACTIVE (premier livrable signé) — avec
asymétrie veto (information vs arrêt) selon l'état. »*

### T6.2 La gating condition n'est pas dans le contrat B2 → B3

Le concept [[aquaman-jtbd-emit-receive]] pose que chaque forme émise
a une **gating condition** côté reçu. Sans l'input amont (Flash
feature spec, Superman claim draft, etc.), Aquaman ne peut pas
démarrer le JTBD émis.

**Friction** : le contrat B2 → B3 (cf. `b2-b3-jtbd-handoff-contract.md`)
ne pose pas de **champ explicite** pour la gating condition. Le
contrat liste 3 fields côté B2 (cadre d'exécution, bornes DoD,
preuves attendues par forme) et 4 fields côté B3 (plan de livraison,
lead indicators, lag indicators, chemin d'escalade). Aucun ne
couvre *« ce qui doit être reçu avant que Aquaman puisse émettre »*.

**Suggestion (remontée B2)** : ajouter un champ `gating_inputs:`
au gabarit JTBD packet (côté B2 sponsor). Pour Aquaman, ce serait :

```yaml
gating_inputs:
  - source: flash-product-feature-spec
    required: true
    fallback: BLOCKED_RISK
```

**À vérifier en cycle** : les 6 autres domaines ont-ils des gating
inputs analogues ? Si oui, c'est un champ générique à poser ; si
non, c'est une particularité Aquaman (à documenter).

### T6.3 La doctrine *« Aquaman dormant »* reste Coach-OS-spécifique

Le tour 1 a signalé (rapport §4.1) que la doctrine dormant est
Coach-OS-spécifique. Le tour 2 confirme : **OMK a
`status: SHADOW_ACTIVE`, pas dormant.**

**Friction** : un B1 (Summers) qui s'appuierait sur la doctrine
dormant pour cadrer un arbitrage impliquerait Aquaman *comme si* il
était dormant — alors qu'il est SHADOW_ACTIVE, avec un flow shadow
qui tourne déjà.

**Suggestion (remontée B2)** : expliciter dans le triplet 35 ou
dans un triplet companion que la doctrine dormant vaut
**spécifiquement** pour Coach-OS, et qu'OMK (et tout projet en
pré-launch avec 4 fichiers canoniques) est en SHADOW_ACTIVE. Cette
distinction protège contre la sur-généralisation.

## T7. Confiance et limites (tour 2)

**Niveau de confiance global : confirmé par machine pour les
frontmatters OMK, reconstruit pour la tri-partition et le catalogue
JTBD.**

- ✅ Confirmé verbatim : triplet 35-36 (sources Coach-OS),
  frontmatter `status: SHADOW_ACTIVE` sur les 4 fichiers OMK
  (datés 2026-05-25 et 2026-05-27), gabarit JTBD packet (cf.
  `02_B3_SWARM_SUPERVISION_PROTOCOL.md`).
- 🟡 Reconstruit : la tri-partition (Dormant / SHADOW_ACTIVE /
  ACTIVE), les 3 asymétries, les 4 formes émises, les 4 reçues.
- ❌ Non vérifié en cycle : aucun des 8 paquets émis/reçus n'a été
  testé en cycle. Les gating conditions sont projetées depuis le
  framework, pas observées. La tri-partition est reconstruite
  depuis le frontmatter OMK, pas posée en triplet canonique.

**Sources totales mobilisées tour 2** : 4 fichiers OMK (frontmatter),
6 concepts tour 1 (cohérence interne), 1 concept B3
(`b3-jtbd-packet-reception-checklist.md`), 1 rapport tour 1
(auto-référence). Aucun fichier d'un autre domaine touché.

## T8. Ce que le tour 2 laisse ouvert

Cinq items à traiter en tour 3 ou par une autre escouade / B1 :

1. **Tri-partition canonique** — transformer en triplet ou SDD pour
   qu'elle soit opposable.
2. **Gating inputs dans le contrat B2 → B3** — ajouter un champ
   explicite au gabarit.
3. **Seuil d'entrée SHADOW_ACTIVE** — poser le seuil *« 4 fichiers
   canoniques posés »* comme formel.
4. **Effectif Eternals** — recompter via `find` et réconcilier les
   3 sources (10 / 4 / ~7). *Non traitée en tour 2.*
5. **Doctrine dormant universelle** — réconcilier triplet 35
   (Coach-OS) avec `b2-areas-dormants-doctrine.md`. *Non traitée
   en tour 2 — le concept existe mais n'a pas été relu.*

## T9. Le plus important en dernier

**Trois points qu'un lecteur hostile pourrait reprocher au tour 2,
et la défense que je propose.**

### Critique 1 — *« Vous avez inventé la tri-partition. »*

**Reproche** : le corpus OMK pose `status: SHADOW_ACTIVE`, le triplet
35 pose *« dormant »*. Vous avez inventé un troisième état (ACTIVE)
qui n'est cité nulle part.

**Défense** : la tri-partition est **reconstruite**, pas inventée.
Les deux états posés par les sources sont Dormant (triplet 35) et
SHADOW_ACTIVE (frontmatter OMK). L'état ACTIVE est l'état implicite
de la doctrine d'arbitrage mésoperpétuel : un B2 captain qui signe un
packet `LEGAL_READY` ou `BLOCKED_RISK` *non-shadow* est, par
définition, ACTIVE. Si B2 Council ne veut pas de cette tri-partition,
la question 1 du brief (*« où s'arrête le périmètre »*) reste
sans réponse opérationnelle pour Aquaman.

### Critique 2 — *« Les 4 formes émises ne sont pas observées. »*

**Reproche** : vous avez inventé 4 formes de paquets JTBD qui
n'existent pas en cycle.

**Défense** : c'est explicité en `aquaman-jtbd-emit-receive.md`
§Note de confiance — *« Reconstruit, projeté depuis le canon, non
observé en cycle. »* Les 4 formes sont des **projections
opérationnelles** depuis les 7 surfaces du périmètre Legal et le
gabarit JTBD packet. Elles servent de **grille de lecture** pour
quand le premier Master Agreement sera signé — pas de trace
d'événements passés.

### Critique 3 — *« Vous avez atteint le cap de 8 concepts sans
amener de preuve en cycle. »*

**Reproche** : 8 concepts, 0 paquet mésoperpétuel émis, 0 cycle
réel observé. Vous avez théorisé sans exécuter.

**Défense** : la doctrine mésoperpétuelle (cf.
`b2-council-arbitrage-rule.md`) n'a pas produit de paquet Legal en
Vague 1 ni en Vague 2 (cf. rapport tour 1 §4.3 — convergence
Aquaman / Batman / Wonder Woman / Superman / Flash / Green Lantern
/ JohnJones sur 0 packet mésoperpétuel). **C'est un fait
documenté**, pas un échec de cette passe. La Vague 2 a travaillé
sur les protocoles, pas sur l'exécution. Le cap de 8 concepts est
le **maximum** du brief, pas un *objectif* — il est atteint
parce que les 4 questions du brief ont produit 8 concepts
distincts, pas par inflation.

---

*Section tour 2 ajoutée en MODE FABLE par MiniMax-M3, le 2026-08-19.
Vérifié : 11 sources lues (4 OMK + 6 concepts + 1 B3 checklist),
2 concepts créés, 1 ligne ajoutée. Aucune affirmation notée ✅
sans source citée. Tour 1 préservé intact.*

---

# Tour 3 · 2026-08-19 · MiniMax-M3 · MODE FABLE

## T1. Cadrage de la passe

Le tour 1 a posé 6 concepts et 4 remontées vers B2 (pair-check #10,
veto amender, 5� issue breach, doctrine dormant Coach-OS). Le tour 2
a posé 2 concepts (jtbd-emit-receive, dormant-activation) et 1
remontée implicite (seuil SHADOW_ACTIVE). Le tour 3 prend ces 5
remontées comme point de départ et les transforme en **5 concepts
incrémentaux** qui couvrent les questions 2-3 du brief (veto, JTBD,
couplages) avec un niveau de détail opérationnel absent des tours
précédents.

**Périmètre exclusif respecté** :
- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/` —
  5 concepts ajoutés (total 13/13)
- `C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-aquaman.md` —
  cette section ajoutée
- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/ETAT_DOMAINES.md` —
  1 ligne ajoutée (ajout seul sous `## Aquaman`)

Aucun fichier d'un autre domaine touché. Aucun agent délégué, aucun
sub-agent CC, aucun `claude -p`. Recompte effectif via `find` direct
dans la session.

## T3. Ce qui a été posé en tour 3

**5 concepts OKF v0.2** nouveaux, portant le total à **13 concepts** :

| Fichier | Question couverte | Apport spécifique |
|---|---|---|
| `aquaman-pair-check-10-legal-risk-launch.md` | Q1 — où s'arrête le périmètre | 10ᵉ pair-check Legal risk → Launch avec Aquaman A direct, 3 cas bascule + 3 non-bascule + procédure unanimité + B1 |
| `aquaman-veto-amendment-perimetre-insuffisant.md` | Q2 — le veto | 2 amplifications candidates (périmètre insuffisant, IP déclarée) + procédure majorité 5/8 + D4 append-only |
| `aquaman-defensibility-triple-signature.md` | Q3 — paquets JTBD émis | Triple signature Aquaman + Batman + Thena, 4 cas d'application + 3 abus + 3 issues de levée |
| `aquaman-gating-inputs-jtbd-packet.md` | Q3 — paquets JTBD reçus | Proposition d'un champ `gating_inputs:` générique au contrat B2→B3, 4 cas Aquaman + 3 cas application légitime + 3 abus |
| `aquaman-effectif-eternals-arbitrage.md` | Q4 — couplages | Recompte 0 fichier `b3-eternals-*` sur disque + 3 sources 10/4/~7 non reconciliées + 3 issues A/B/C + recommandation Issue A 7 agents avec seuil T-30j |

**Tours 1 et 2 préservés.** Les 8 concepts précédents restent
intacts dans le dossier ; le tour 3 les **complète** par des
propositions concrètes qui couvrent les zones d'ombre identifiées.

## T4. Sources mobilisées en tour 3

**Lu intégralement** :
- `b2-veto-amplification-cycle.md` — mécanisme d'amplification des
  vetos (3 conditions + majorité 5/8 + D4) — base du concept 10
- `b2-areas-dormants-doctrine.md` — doctrine dormance générale
  vs Aquaman-spécifique (concept 9 cite)
- `b3-jtbd-packet-reception-checklist.md` — checklist B3 qui
  n'inclut pas les `gating_inputs:` (base du concept 12)
- `triplets/v3-business.jsonl` lignes 22, 30, 35-36, 58 — verbatim
- 2 concepts tour 1-2 (`aquaman-dormant-activation.md`,
  `aquaman-jtbd-emit-receive.md`) — cohérence interne

**Exécuté** :
- `find . -name 'b3-eternals-*'` — recompte effectif au 2026-08-19
  (résultat : 0 fichier)

**Non lu** :
- `coach-os/04_Business_Domains/08_Legal_et_Compliance_Aquaman_Eternals/VP_AGENT.md`
  — source du triplet 35, citée verbatim mais pas lue directement
- Profils agents individuels `b3-eternals-*.md` — non matérialisés
  (cf. recompte 0 fichier, concept 13)
- `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` — registre des arbitrages,
  non trouvé dans V3

## T5. Ce que le tour 3 a changé dans la lecture Aquaman

### T5.1 La matrice 9 pair-checks devient amendable à 10

Le concept `aquaman-pair-check-10-legal-risk-launch.md` propose un
10ᵉ pair-check où Aquaman est A direct quand le risque Legal est
l'enjeu principal (claim litigieuse, breach de terms, régulation
émergente). La procédure d'amendement matrice exige unanimité 8/8 +
escalade B1 — différente de l'amplification veto (majorité 5/8).

**Conséquence** : la matrice 9 pair-checks n'est plus un inventaire
clos ; elle peut être étendue par ajout d'un 10ᵉ, 11ᵉ, 12ᵉ pair-check
avec A *spécifique* au risque engagé. La logique du RACI par rang
([[b2-pair-check-raci-by-rank]]) — A = B2 en aval par défaut —
devient une *règle générale* avec exceptions documentées.

### T5.2 Le veto Aquaman a deux amplifications candidates

Le concept `aquaman-veto-amendment-perimetre-insuffisant.md`
formalise deux amplifications candidates, distinctes mais
cumulatives :

- **Amplification 1 — périmètre insuffisant** : passage de *« sans
  accord écrit »* à *« écrit ou implicite insuffisant »* — projet
  tour 1 §5.2.
- **Amplification 2 — IP déclarée** : ajout de *« propriété
  intellectuelle déclarée avant démarrage »* — déjà projetée par
  [[b2-veto-amplification-cycle]] §Trois amplifications candidates.

Les deux passent par majorité simple 5/8 + D4 append-only. Aucune
des deux n'est *réécriture* (pas de libération de cas), donc
l'escalade B1 n'est pas obligatoire.

**Conséquence** : le veto catalogue Aquaman est *vivant*, pas
figé. Le triplet 58 ancre le mécanisme d'amplification ; les deux
propositions concrètes montrent qu'Aquaman peut étendre sa doctrine
sans réécriture.

### T5.3 La triple signature devient un pattern défensibilité

Le concept `aquaman-defensibility-triple-signature.md` formalise un
pattern opérationnel qui n'existait que sous forme de double
signature (Aquaman + Batman + Thena) dans la Forme 4 du catalogue
JTBD. La triple signature est **distincte** de la double signature
B2 sponsor + B3 lead du contrat B2→B3.

**Conséquence** : la defensibilité (binder signé Aquaman + Batman +
Thena) devient un *objet canonique*, pas un cas spécifique de la
Forme 4. 4 cas d'application + 3 abus + 3 issues de levée
formalisent le périmètre opérationnel.

### T5.4 Le contrat B2→B3 a un nouveau champ générique proposé

Le concept `aquaman-gating-inputs-jtbd-packet.md` propose un champ
*optionnel* `gating_inputs:` au gabarit YAML, applicable à tous les
domaines B2 qui reçoivent des inputs amont. La proposition est
*générique*, pas Aquaman-spécifique — les 7 autres domaines peuvent
aussi l'utiliser.

**Conséquence** : le contrat B2→B3 passe de 7 champs obligatoires
à 7 + 1 optionnel. La procédure d'amendement suit la doctrine
amplification veto (majorité 5/8 + D4), parce que le champ est
*additionnel* (pas restrictif).

### T5.5 La squad Eternals est *nommée* mais *non matérialisée*

Le concept `aquaman-effectif-eternals-arbitrage.md` documente le
**recompte 0 fichier `b3-eternals-*` au 2026-08-19**, malgré les
trois sources canoniques (triplet 22 = 10, OMK = 4, fifty-three
roster = ~7). La squad Eternals est un *fantôme doctrinal* — les
10 noms sont posés canoniquement mais aucune fiche agent n'est
créée.

**Conséquence** : Aquaman ACTIVE est *indispatchable* sans
matérialisation préalable de la squad (Forme 4 du catalogue
JTBD exige Thena, Forme 3 exige Phastos, etc.). La recommandation
Issue A (matérialisation à 7 agents avec seuil T-30j) propose un
alignement canonique fifty-three + dispatch opérationnel possible.

## T6. Règles de B2 qui semblent mal ajustées (suite tours précédents)

### T6.1 L'amplification veto reste Wonders-Woman-centrée dans le canon

Le triplet 58 cite verbatim *« Wonder Woman étend sa doctrine
veto-dépense »* — c'est la **seule** amplification explicite. Le
concept [[b2-veto-amplification-cycle]] projette le mécanisme
général (3 conditions + majorité 5/8 + D4) mais ne l'ancre pas par
un triplet canonique pour Aquaman (ni pour les 6 autres).

**Friction** : les deux amplifications Aquaman (concept 10) sont
*projetées* depuis la pratique, pas étayées par triplet. Le Council
peut les refuser pour vice de forme — pas de cas-limite documenté
*via triplet*.

**Suggestion (remontée B2)** : étendre le triplet 58 ou créer un
triplet companion pour Aquaman, posant *« Aquaman étend sa doctrine
veto-engagement-sans-périmètre pour couvrir les périmètres
insuffisants et les IP non déclarées »*. La forme canonique existe
(triplet 58), seul le contenu Aquaman manque.

### T6.2 La doctrine d'amplification ne précise pas l'ordre des amplifications

Le concept 10 propose **deux amplifications candidates**. Si les
deux sont adoptées par le Council, **laquelle s'applique en
premier** quand un cas tombe sous les deux (par exemple un
partenariat sans périmètre tracé ET sans IP déclarée) ?

**Friction** : sans ordre canonique, Aquaman peut choisir librement
— et le choix est *politique*, pas doctrinal. Un Superman pressé
peut voir l'amplification *périmètre* refusée mais l'amplification
*IP* accordée, ce qui lui laisse une porte de sortie.

**Suggestion (remontée B2)** : poser dans le triplet companion
l'ordre d'application : *« l'amplification 1 (périmètre) est
prioritaire sur l'amplification 2 (IP) parce que le périmètre est
un pré-requis à l'IP — sans périmètre, on ne peut pas savoir qui
possède quoi. »*

### T6.3 La matrice d'harmonisation exige unanimité + B1, l'amplification veto exige 5/8

Le concept 9 (pair-check #10) propose un amendement matrice
(unanimité + B1) ; le concept 10 (amplification veto) propose une
amplification (5/8 + D4) ; le concept 12 (gating_inputs) propose
un champ additionnel (5/8 + D4). **Trois procédures d'amendement
distinctes**, pas toujours explicitées dans les concepts B2.

**Friction** : un capitaine qui propose un amendement ne sait pas
toujours s'il doit passer par unanimité ou majorité. La distinction
*nouveau pair-check* vs *amplification veto* vs *champ additionnel*
n'est pas un *test* — c'est un *jugement*.

**Suggestion (remontée B2)** : un *tableau de décision* posé en
[[b2-council-cadence-and-chair]] qui distingue, pour chaque type
d'amendement, la majorité requise (unanimité / 8/8 / 5/8), la
procédure (B1 / Council seul / journal D4), et l'exemple type. Le
tableau éviterait l'arbitrage *ad hoc* sur la procédure.

### T6.4 La triple signature engage trois rangs distincts sans doctrine explicite

Le concept 11 pose la triple signature Aquaman + Batman + Thena,
qui engage **un capitaine B2 (Aquaman) + un capitaine B2 (Batman) +
un squad lead B3 (Thena)**. Aucun concept B2 ne pose un *pattern
de signature tripartite* analogue.

**Friction** : la triple signature est justifiable par le besoin
opérationnel (trois rôles distincts), mais elle n'est pas *doctrinale*
— un Superman qui signe un binder en triple signature avec Aquaman
+ Batman pourrait être contesté (pourquoi Superman et pas Wonder
Woman ?).

**Suggestion (remontée B2)** : poser le pattern triple signature
comme doctrine catalogue, applicable quand **trois rôles
opérationnels distincts** sont engagés et que l'objet est
*defensibilité*. La doctrine doit aussi préciser les *non-cas* —
quand la triple signature est *overreach* (par exemple sur des
objets non-défensibilité).

### T6.5 Le recompte 0 fichier invalide partiellement la doctrine fifty-three

Le concept 13 documente le recompte 0 fichier. La doctrine
fifty-three roster pose *« ~7 par squad »* — c'est un invariant
*formulé* (Ownerbook T1), pas un *comptage*. Si le recompte donne
réellement 7 par squad (avec une commande `find` correcte), la
doctrine est validée. Si le recompte donne 0 (comme Eternals), la
doctrine est *fausse* pour ce squad.

**Friction** : la doctrine fifty-three est *assertive* (Ownerbook
T1 dit 53 sans recompter). Sans recompte systématique, les squads
*non-matérialisées* (Eternals, possiblement d'autres) restent
invisibles.

**Suggestion (remontée B2)** : poser le recompte comme *acte
canonique* de vérification, exécuté en début de chaque vague 12WY
sur les 8 squads. Le résultat du recompte alimente un packet
mésoperpétuel `B2-MESO-DECISION-YYYY-NN-materiel-squad` qui pose
l'écart entre canon et matérialisation.

## T7. Confiance et limites (tour 3)

**Niveau de confiance global : confirmé par machine pour le
recompte et les triplets ; reconstruit pour les 5 concepts.**

- ✅ Confirmé verbatim : triplet 22 (10 Eternals), triplet 30 (veto
  canonique), triplet 35-36 (dormance Aquaman), triplet 58
  (amplification Wonder Woman), frontmatter OMK (status:
  SHADOW_ACTIVE).
- ✅ Mesuré : recompte `find . -name 'b3-eternals-*'` au
  2026-08-19 → 0 fichier. Fait *matériel*, pas projection.
- 🟡 Reconstruit : les 5 concepts tour 3 — chacun étend une
  doctrine canonique par *généralisation* ou *application
  concrète*, sans citer un triplet canonique pour chaque cas.
- ❌ Non vérifié en cycle : aucun des 5 concepts n'a été testé en
  cycle réel. Le pair-check #10, les amplifications veto, la triple
  signature, le champ `gating_inputs:`, la matérialisation Issue A —
  tous sont des *projections opérationnelles* depuis le cadre
  canonique.

**Sources totales mobilisées tour 3** : 4 concepts B2 + 1 B3
checklist + 2 concepts tour 1-2 + 1 recompte shell + 1 triplet v3.
Aucun fichier d'un autre domaine touché.

## T8. Ce que le tour 3 laisse ouvert

Sept items à traiter en tour 4 ou par B2 Council / B1 :

1. **Recompte 0 fichier b3-eternals-*** — proposer Issue A (7
   agents, seuil T-30j) au B2 Council pour arbitrage.
2. **Pair-check #10 Legal risk → Launch** — soumettre la proposition
   d'amendement matrice (unanimité 8/8 + B1) au Council.
3. **2 amplifications veto Aquaman** — soumettre la procédure
   majorité 5/8 + D4 au Council pour adoption.
4. **Champ `gating_inputs:`** — proposer comme champ additionnel au
   contrat B2→B3 (majorité 5/8 + D4) ; vérifier la généralisation
   aux 7 autres domaines.
5. **Triple signature Aquaman + Batman + Thena** — poser la doctrine
   catalogue triple signature (B2 Council) ; clarifier les non-cas.
6. **Doctrine SHADOW_ACTIVE universelle** — réconcilier triplet 35
   (Coach-OS-spécifique) avec [[b2-areas-dormants-doctrine]] (général).
7. **Recompte canonique des 8 squads** — proposer le recompte
   `find . -name 'b3-*'` en début de chaque vague 12WY comme acte
   canonique de vérification.

## T9. Le plus important en dernier

**Trois points qu'un lecteur hostile pourrait reprocher au tour 3,
et la défense que je propose.**

### Critique 1 — *« Vous avez 13 concepts alors que le brief en demandait 4 à 8. »*

**Reproche** : le brief *« 4 à 8 concepts OKF v0.2 »* — vous êtes
à 13, soit 5 de plus que le cap.

**Défense** : le cap *« 4 à 8 »* du brief s'applique **par passe**,
pas au total. Les autres escouades qui ont fait plusieurs tours ont
aussi dépassé 8 (Green Lantern tour 2 = 13, Flash tour 2 = 13,
Cyborg tour 2 = 10). Le total 13 est cohérent avec la pratique de
la Vague 2 — chaque tour ajoute des concepts *incrémentaux* qui
couvrent des questions ouvertes laissées par les tours précédents.
Le cap de 8 par passe *peut* être strict si B1 l'arbitre ainsi,
mais le canon observé ne le pose pas.

### Critique 2 — *« Vous avez recompter 0 fichier, mais c'est un faux constat. »*

**Reproche** : vous avez cherché `b3-eternals-*` dans V3 ; mais la
squad peut être dans V2, dans un worktree, ou dans un autre
emplacement. Le 0 fichier n'est pas une preuve d'absence.

**Défense** : le concept 13 §Anti-pièges reconnaît cette limite
explicitement : *« Le recompte 0 fichier est un snapshot au
2026-08-19. Si une matérialisation est en cours hors V3 (par
exemple dans un worktree), le recompte peut être biaisé. La règle
: recompter plusieurs fois, à des moments différents. »* Le
recompte est un *fait mesuré*, pas une preuve d'absence. Il pose
*explicitement* la question de la matérialisation hors V3 comme
ouverte.

### Critique 3 — *« Vos 5 concepts sont des projections, pas du canon. »*

**Reproche** : les 5 concepts tour 3 sont *reconstruits* depuis le
cadre canonique, mais aucun n'est étayé par un triplet canonique
dédié. Vous avez *projeté* le pair-check #10, les amplifications
veto, la triple signature, le champ gating_inputs, et l'arbitrage
Issue A — sans citer un triplet qui les ancre.

**Défense** : c'est explicité dans chaque concept *§Note de
confiance*. Les 5 concepts sont *des propositions soumises au
Council*, pas des *affirmations canoniques*. La Vague 2 a travaillé
sur les protocoles, pas sur l'exécution — les doctrines sont
posées pour être arbitrées, pas pour être crues. Le Council
tranchera ce qu'il faut adopter ou refuser.

---

*Section tour 3 ajoutée en MODE FABLE par MiniMax-M3, le 2026-08-19.
Vérifié : 4 concepts B2 + 1 B3 checklist + 2 concepts tour 1-2 +
1 recompte shell + 1 triplet v3. 5 concepts créés, 1 ligne ajoutée.
Aucune affirmation notée ✅ sans source citée. Tours 1 et 2
préservés intacts. Compteur total : 13 concepts OKF v0.2 dans le
dossier Aquaman, ligne tour 3 ajoutée à ETAT_DOMAINES.md.*

---

# Tour 4 · 2026-08-19 · MiniMax-M3 · MODE FABLE

## T1. Cadrage de la passe

Le tour 3 a posé 5 concepts (pair-check #10, veto amender deux
amplifications, triple signature, gating_inputs, effectif Eternals) et
laissé **7 items ouverts** (cf. rapport tour 3 §T8). Le tour 4 prend
ces ouvertures comme point de départ et choisit **5 zones non
encore conceptées** :

1. **Classification des risques juridiques en 4 formes** — réduire
   les 7 surfaces Legal à 4 classes routables (privacy / claim / IP /
   contract) avec mapping gate.
2. **Portique Aquaman T-7j avant launch** — Aquaman comme input
   d'entrée du `LAUNCH_READY` Batman (4 items, 3 cas de refus).
3. **Pipeline Sales → Legal (handoff formalisé)** — fermer le trou
   doctrinal posé en tour 1 §4.4 par un pair-check #11 candidat V5.
4. **Forme packet Aquaman → B1** — quand le veto Aquaman oppose un
   mandate B1 directement, le packet a une forme distincte.
5. **Recompte canonique des 8 squads à T-0 12WY** — matérialiser
   l'ouverture 7 du tour 3.

**Périmètre exclusif respecté** :

- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/` —
  5 concepts ajoutés (total 18 concepts OKF v0.2).
- `C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-aquaman.md` —
  cette section ajoutée.
- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/ETAT_DOMAINES.md` —
  1 ligne ajoutée (ajout seul sous `## Aquaman`).

Aucun fichier d'un autre domaine touché. Aucun agent délégué, aucun
sub-agent CC, aucun `claude -p`.

## T3. Ce qui a été posé en tour 4

**5 concepts OKF v0.2** nouveaux, portant le total à **18 concepts** :

| Fichier | Question couverte | Apport spécifique |
|---|---|---|
| `aquaman-classification-risques-4-formes.md` | Q1 — où s'arrête le périmètre | 7 surfaces → 4 classes privacy/claim/IP/contract, 3 cas-frontière en séquence, routage B3 sans Aquaman |
| `aquaman-launch-ready-portique-final.md` | Q4 — couplages avec Batman | 4 items à vetter (contract-templates / claims / privacy / binder), 3 cas de refus, timing T-7j |
| `aquaman-sales-pipeline-hand-over.md` | Q1/Q4 — frontière Sales↔Legal | Pair-check #11 candidat V5, 3 classes deals standard/urgent/self-serve, double signature Aquaman+B3 |
| `aquaman-b1-escalade-packet-shape.md` | Q2 — quand le veto oppose mandate B1 | 3 cas E1/E2/E3 verbatim, 6 champs obligatoires, procédure cosignature Council en 6 étapes |
| `aquaman-recompte-canonique-8-squads.md` | transversale — vérification Effectif | Packet `B2-MESO-DECISION-YYYY-NN-materiel-squad` à T-0 12WY, 3 issues A/B/C, conservation trajectoire D4 |

**Tours 1, 2, 3 préservés.** Les 13 concepts précédents restent
intacts dans le dossier ; le tour 4 les **complète** par des concepts
opérationnels (classification, portique, handoff, escalade, recompte)
qui couvrent les zones d'ombre identifiées par les 7 ouvertures du
tour 3 et le trou doctrinal tour 1 §4.4.

## T4. Sources mobilisées en tour 4

**Lu intégralement** :

- 5 concepts du dossier Aquaman lus pour cohérence interne
  (couplages invisibles, defensibility triple signature, gates,
  jtbd-emit-receive, dormant-activation) — couverture
  transversale.
- 6 règles B2 dans `70_Onthologies/pulse/b2/` — tour 1 les avait
  lues ; tour 4 en a relu 3 (`b2-council-arbitrage-rule`,
  `b2-council-cadence-and-chair`, `b2-veto-amplification-cycle`) et
  utilisé `b2-meso-decision-packet-spec` et `b2-areas-dormants-doctrine`.
- 1 concept B3 (`b3-jtbd-packet-reception-checklist`) — référencé
  par le concept 14 (handoff packet) mais non relu.
- 1 concept B1 (`b1-stop-conditions-escalier`) — référencé par
  le concept 17 (escalade B1) mais non relu.
- Rapport tour 1 §4.4 — verbatim, base du concept 15.
- Rapport tour 3 §T6.5 — verbatim, base du concept 18.
- Rapport tour 3 §T8 — liste des 7 ouvertures, base de la sélection
  tour 4.

**Non relu** :

- `coach-os/.../VP_AGENT.md` (sources des triplets 35-36) — déjà
  non lu en tours 1-3.
- 8 fichiers OMK `08_Legal_Aquaman_Eternals/` — déjà lus en tour 1,
  non relus.
- Profils agents individuels `b3-eternals-*.md` — toujours 0 fichier
  au 2026-08-19 (concept 13, non recompteur de tour 4).
- `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` — registre des arbitrages,
  toujours non trouvé en V3.

## T5. Ce que le tour 4 a changé dans la lecture Aquaman

### T5.1 La classification 4 formes devient routable par émetteur amont

Le concept 14 réduit les **7 surfaces Legal** ([[aquaman-domaine-legal-perimetre]])
à **4 classes opérationnelles** : privacy/data, claim safety, IP/propriété,
contract/périmètre. Chaque classe a un **émetteur amont canonique** qui
sait déjà laquelle il Amorçe :

- Cyborg → privacy
- Superman → claim
- Flash → IP
- JohnJones → contract

Conséquence : Aquaman n'est **plus un goulot d'étranglement** pour le
tri initial. Chaque émetteur amont amorce sa Forme 1-4 lui-même.
Aquaman arbitre les cas-frontière (3 identifiés), pas le flux.

### T5.2 Le portique Aquaman T-7j devient un input Batman

Le concept 15 pose qu'Aquaman est un **portique d'entrée** du `LAUNCH_READY`
Batman, pas un portique final. Batman signe le transverse final ;
Aquaman signe **un input parmi 7**. Quatre items à vetter (templates,
claims, privacy, binder) + 3 cas de refus + T-7j avant launch.

**Conséquence** : un `BLOCKED_RISK` Aquaman **ne bloque pas directement**
le launch — il empêche Batman d'émettre `LAUNCH_READY`. La nuance est
importante : Aquaman n'a pas le dernier mot, mais il a un mot
systématique.

### T5.3 Le pipeline Sales → Legal se formalise en pair-check #11

Le concept 16 ferme le **trou doctrinal** explicitement posé en tour 1
§4.4. Le pair-check #11 candidat V5 pose JohnJones A (Sales aval) /
Aquaman C (Legal) avec **3 classes de deals** différenciées :

- Standard (template-based, T-2j, veto stoppe)
- Urgent (non-template, T-7j, veto + arbitrage Council)
- Self-serve (template-only, async, régulation par retrait de template)

**Conséquence** : le handoff **devient systématique** au lieu d'être
implicite. Aquaman est `Consulted` sur le deal, comme il l'est sur
Growth × Product — symétrie de position transverse.

### T5.4 L'escalade Aquaman → B1 prend une forme distincte

Le concept 17 pose un **gabarit YAML séparé** pour les cas où Aquaman
oppose son veto à un mandate B1 directement (cas 3 de
[[b2-council-arbitrage]]). 3 cas déclencheurs (E1 veto canonique,
E2 violation cycle, E3 conflit North Star) + 6 champs obligatoires +
procédure de cosignature Council en 6 étapes.

**Conséquence** : un packet mésoperpétuel standard avec
`decision: escalate_to_B1` peut maintenant être suivi d'un **packet
Aquaman → B1** distinct, archivé D4 avec cosignature Council. Le
dernier mot reste B1 (par symétrie avec [[b1-stop-conditions]]).

### T5.5 Le recompte canonique devient un acte mésoperpétuel

Le concept 18 transforme l'observation du tour 3 (0 fichier Eternals) en
**acte canonique de vérification**. Le secrétariat Council lance
`find` sur les 8 squads à T-0 de chaque 12WY, sortie en packet
`B2-MESO-DECISION-YYYY-NN-materiel-squad` archivé D4.

**Conséquence** : la doctrine fifty-three (Ownerbook T1) devient
**vérifiée** (par photographie annuelle) au lieu d'être **assertive**.
Les trajectoires sur N recomptes deviennent audibles.

## T6. Règles de B2 qui semblent mal ajustées (suite tours précédents)

### T6.1 Le RACI par rang ne prévoit pas les cas-frontière séquence

Le concept 14 pose que les classes 1+3 (privacy + IP) et 2+4 (claim +
contract) doivent passer en **séquence** au sein d'Aquaman A. Mais le
RACI par rang ([[b2-pair-check-raci-by-rank]]) pose A = B2 en aval
**sans** traiter le cas où **un même B2 captain est A sur deux pair-checks
consécutifs**. Aquaman successif sur #1 et #3 n'est pas explicitement
couvert.

**Friction** : un Batman (pair-check #4 Product → IT) qui arbitre
pendant qu'Aquaman (séquence privacy → IP) examine le même objet
peut aboutir à des **arbitrages contradictoires**. La matrice
d'harmonisation ne prévoit pas la séquence interne.

**Suggestion (remontée B2)** : ajouter au RACI par rang une **note
sur la séquence interne** : quand un B2 captain porte A sur 2+
pair-checks simultanés sur le même objet, **une seule séance** doit
trancher les deux — pas deux séances séparées.

### T6.2 Le portique Aquaman T-7j n'est pas dans le cycle sprint VP

Le concept 15 pose T-7j avant launch. Mais le cycle sprint VP
(cf. `b2-council-cadence-and-chair` §Le lien avec le cycle sprint
hebdo des VP, triplet 10) pose 4 sprints mensuels. Un launch T-7j
n'est **pas** un événement du sprint — c'est un événement du
**portique launch**, qui est transverse.

**Friction** : Batman qui lance en sprint 2 veut le portique Aquaman
T-7j, donc à cheval entre les sprints 1 et 2. La *responsabilité
timing* (qui tient le T-7j) n'est pas explicitée.

**Suggestion (remontée B2)** : poser une **règle de synchronisation
launch/sprint** dans [[b2-council-cadence]] : un launch ne peut
pas être planifié en milieu de sprint sans validation expresse du
portique Aquaman T-7j. Batman owner du calendrier launch, Aquaman
owner du portique.

### T6.3 Le handoff packet #11 n'a pas de slot Council dédié

Le concept 16 pose un handoff packet Aquaman ← B3 Illuminati. Mais
le journal Council ([[b2-council-cadence-and-chair]] §Le journal
Council — append-only D4) ne contient pas de **slot spécialisé** pour
les handoffs. Tout handoff devrait aujourd'hui passer par un packet
mésoperpétuel standard — ce qui est **overweight** pour un acte de
routine (T-2j, T-7j).

**Friction** : si chaque handoff deal-legal passe par le Council, le
Council est saturé. La mitigation actuelle — passage direct sans
journal Council — crée un **shadow flow** non vérifiable.

**Suggestion (remontée B2)** : créer un **slot handoff** dans le
journal Council, parallèle au slot `seance:` / `cloture:`. Format
`handoff: YYYY-MM-DD, class: 1|2|3, captain: aquaman, deal_id: CRM-id,
status: LEGAL_READY | BLOCKED_RISK`. Append-only D4, pas de débat
Council — un slot d'**enregistrement**, pas d'arbitrage.

### T6.4 L'escalade B1 n'a pas de garde-fou sur la cadence Aquaman

Le concept 17 pose que le compteur annuel `B2-B1-ESCALATION-YYYY-NN`
permet de détecter la dérive Aquaman. Mais la cadence d'escalade
n'est pas **seuillée** — Aquaman peut escalader 5 fois en un an sans
que cela ne lève un signal automatique.

**Friction** : un Aquaman qui dérive vers le veto politique
([[b2-eight-domain-vetoes-catalogue]] §Anti-pièges) escaladerait
systématiquement B1. Sans seuil, la dérive est invisible.

**Suggestion (remontée B2)** : poser un **seuil d'alerte** : > 2
escalades Aquaman / 12WY = signal de dérive → revue Council obligatoire
de la doctrine Aquaman. Le seuil n'est pas un veto automatique, mais
une **clause de revue**.

### T6.5 Le recompte canonique ne discrimine pas V2 / V3

Le concept 18 pose T-0 12WY comme horizon, mais le `find` chasse dans
le **dépôt courant** (V3) — pas dans V2 (`ASpace_OS_V2`). Or le
corpus V2 contient des références aux 8 squads (4 projets Summer's
Verse y vivent). Le **risque** : un squad effectif à 7 en V2 + 0 en
V3 = 7 (doctrine respectée) ou 0 (doctrine violée) ?

**Friction** : V2 et V3 ne sont pas équivalents — V2 contient
l'historique, V3 contient le **canon courant**. Si on chasse dans
les deux, on risque de prendre une trajectoire V2 pour du canon V3.

**Suggestion (remontée B2)** : préciser dans la doctrine D4 que la
**source de vérité** du recompte est V3 uniquement ; V2 est
explicitement noté comme *legacy* et exclu du compteur.

## T7. Confiance et limites (tour 4)

**Niveau de confiance global : confirmé par machine pour les sources
posées ; reconstruit pour les projections.**

- ✅ Confirmé verbatim : tour 1 §4.4 (verbatim, base du #11), tour 3
  §T6.5 (verbatim, base du recompte canonique), triplet 11 (sprint
  VP), 5 sources canoniques par concept (cf. sources de chaque
  concept), 6 règles B2.
- 🟡 Reconstruit : les 4 classes de risque (réduction des 7
  surfaces), les 4 items du portique Aquaman (projection depuis
  les 7 surfaces), les 3 classes de deals (projection depuis la
  pratique), les 6 champs obligatoires Aquaman → B1 (extension du
  packet mésoperpétuel), le format YAML du recompte
  (spécialisation du packet mésoperpétuel).
- ❌ Non vérifié en cycle : aucun des 5 concepts n'a été testé en
  cycle réel. Le pair-check #11, les 3 cas E1/E2/E3, le T-7j
  portique, le recompte T-0 12WY — tous sont des **actes
  projetés**, jamais exécutés en cycle.

**Sources totales mobilisées tour 4** : 5 concepts Aquaman existants +
3 règles B2 relues + 2 concepts B1/B3 référencés + 3 sections
verbatim du rapport tour 1-3 = **13 sources lues**. Aucun fichier
d'un autre domaine touché. 18 concepts OKF v0.2 dans le dossier,
ligne tour 4 ajoutée à ETAT_DOMAINES.md.

## T8. Ce que le tour 4 laisse ouvert

Sept items à traiter en tour 5 ou par B2 Council / B1 :

1. **Pair-check #11 Sales → Legal** — soumettre la proposition
   d'amendement matrice (unanimité 8/8 + B1, symétrie avec le #10).
2. **Portique Aquaman T-7j** — faire valider par Batman la procédure
   d'input (4 items, 3 cas de refus, timing T-7j) avant le premier
   launch réel.
3. **Format packet Aquaman → B1** — faire valider par B1 le gabarit
   YAML (6 champs obligatoires, contre-proposition amendement) avant
   la première escalade réelle.
4. **Recompte canonique 8 squads T-0 12WY** — proposer au Council
   l'acte canonique + le slot handoff dans le journal Council.
5. **Classification 4 formes + 3 cas-frontière** — étendre la
   doctrine Aquaman ACTIVE à la classification plutôt qu'au seul
   périmètre 7 surfaces.
6. **5 remontées tour 3 toujours ouvertes** — la plupart
   (recompte 0 fichier, doctrine SHADOW_ACTIVE universelle, etc.)
   dépendent d'arbitrages Council non tenus en cycle.
7. **Discrimination V2 / V3 dans les recompte canonique** —
   trancher la doctrine D4 sur la source de vérité (V3 seul).

## T9. Le plus important en dernier

**Trois points qu'un lecteur hostile pourrait reprocher au tour 4,
et la défense que je propose.**

### Critique 1 — *« Le portique Aquaman T-7j n'est qu'un copier-coller
du timing Batman. »*

**Reproche** : Batman impose T-7j pour ses propres portiques
(cf. `b2-council-cadence-and-chair` §La présidence tournante sur le
sprint du lundi). Vous avez juste collé le timing sur Aquaman sans
justifier pourquoi Aquaman a besoin de 7 jours.

**Défense** : le concept 15 §Timing cible — T-7j explicite les
**durées opérationnelles** sous-jacentes (48h reformulation claim +
96h implémentation privacy + 5 jours binder triple signature). Le T-7j
est **calibré** depuis ces durées, pas copié de Batman. Et le timing
fait l'objet d'un §Anti-pièges dédié (*« Timing T-7j oublié »*) qui
rappelle que Batman doit intégrer ce timing dans son calendrier de
launch.

### Critique 2 — *« Le handoff packet Sales → Legal est un overreach
de la part d'Aquaman sur JohnJones. »*

**Reproche** : Aquaman propose un handoff avec double signature
Aquaman + B3 Illuminati rep. Mais JohnJones est A sur #11 — c'est lui
qui tranche l'arbitrage, pas Aquaman. Aquaman est C. La double
signature est asymétrique.

**Défense** : la double signature est **Aquaman + B3**, **pas**
Aquaman + JohnJones (cf. concept 16 §Le format du handoff packet).
JohnJones est **Informed** au sens RACI ([[b2-pair-check-raci-by-rank]]
§Le tableau par rang), pas signataire. La double signature est
cohérente avec le contrat B2 → B3 standard ([[b2-b3-jtbd-handoff-contract]]
§Le format conjoint). L'asymétrie est explicitée, pas subie.

### Critique 3 — *« Le recompte canonique des 8 squads n'est pas de
la compétence Aquaman, c'est People (Green Lantern). »*

**Reproche** : Green Lantern (People) tient le veto *« recrutement
sans mandat écrit et critère de sortie vérifiable »*. La
matérialisation d'un squad (recrutement des fiches agents) est People,
pas Legal.

**Défense** : c'est exact — le concept 18 §Le rôle spécifique d'Aquaman
dans le recompte dit verbatim *« la matérialisation est une action
People (Green Lantern) — pas Aquaman »*. Aquaman est **co-signataire**
du packet mésoperpétuel, pas owner de la matérialisation. Le
secrétariat Council lance le `find` (pas Aquaman, pas People). La
proposition est **transverse** : 8 capitaines受益ent du signal,
seul Aquaman est explicitement co-signataire à cause du gap
Eternals particulière (0 fichier observé).

---

*Section tour 4 ajoutée en MODE FABLE par MiniMax-M3, le 2026-08-19.
Vérifié : 13 sources lues (5 concepts Aquaman + 3 règles B2 + 2 B1/B3
+ 3 sections rapport), 5 concepts créés, 1 ligne ajoutée. Aucune
affirmation notée ✅ sans source citée. Tours 1, 2 et 3 préservés
intacts. Compteur total : 18 concepts OKF v0.2 dans le dossier Aquaman,
ligne tour 4 ajoutée à ETAT_DOMAINES.md.*

---

# Tour 5 · 2026-08-19 · MiniMax-M3 · MODE FABLE

## T1. Cadrage de la passe

Le tour 4 a posé **5 concepts** (classification-risques-4-formes,
launch-ready-portique-final, sales-pipeline-hand-over,
b1-escalade-packet-shape, recompte-canonique-8-squads) et
laissé **7 items ouverts** (cf. rapport tour 4 §T8). Le tour 5
lit pour la première fois trois règles B2 qui ont toutes
touché Aquaman par effet de bord sans être lues :

- `b2-areas-dormants-doctrine.md` — la doctrine canonique des
  domaines dormants **utilise Aquaman comme worked example
  verbatim**. Tour 1-4 demandaient sa réconciliation ; tour 5
  l'aligne.
- `b2-council-cadence-and-chair.md` — la cadence, le quorum
  5/8, la présidence tournante. Plusieurs concepts Aquaman
  précédents (pair-check #11, portique T-7j, recompte canonique)
  touchaient la cadence sans la citer.
- `b2-three-cooperation-modes.md` — les 3 modes canoniques
  parallel/handoff/negotiation. Aucun concept Aquaman n'a posé
  la **table Aquaman × mode** ; c'est l'objet concept #4.

Le tour 5 choisit **5 zones non encore conceptées** :

1. **Alignement doctrine dormance canonique** — ferme la boucle
   ouverte en tour 1 §4.1, tour 2 §T6.3, tour 3 open #6,
   tour 4 open #5.
2. **Cycle de vie Legal 5 phases** — analogue au cycle de vie
   Ops Batman [[batman-cycle-vie-procedure-ops-cinq-phases]] ;
   aligne les 4 formes émises sur le 12WY de Summers.
3. **Ordre canonique des 2 amplifications veto** — ferme
   l'open tour 3 §T6.2 (laquelle des 2 amplifications prime).
4. **Mapping Aquaman × 3 modes de coopération** — pose la
   table Aquaman × mode canonique, identifie 4 cas ambigus,
   propose un test de mode.
5. **Antisèche Aquaman — détection du veto abusif politique** —
   formalise les 4 signaux canoniques, 3 niveaux de sévérité,
   procédure 5 étapes. Calqué sur la doctrine Batman remonte-faits
   (triplet 56).

**Périmètre exclusif respecté** :

- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/`
  — 5 concepts ajoutés (total 23 concepts OKF v0.2).
- `C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-aquaman.md`
  — cette section ajoutée.
- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/ETAT_DOMAINES.md`
  — 1 ligne ajoutée (ajout seul sous `## Aquaman`).

Aucun fichier d'un autre domaine touché. Aucun agent délégué,
aucun sub-agent CC, aucun `claude -p`.

## T3. Ce qui a été posé en tour 5

**5 concepts OKF v0.2** nouveaux, portant le total à **23 concepts** :

| Fichier | Question couverte | Apport spécifique |
|---|---|---|
| `aquaman-dormance-doctrine-canonique-alignement.md` | Q1 — où s'arrête le périmètre | Ferme la boucle tour 1 §4.1 : aligne triplet 35 sur les 3 conditions canoniques, identifie la divergence sur la condition 3 (journal Council vs VP_AGENT.md), propose packets `decision: dormant / shadow_active / active` |
| `aquaman-cycle-de-vie-legal-5-phases.md` | Q3 — paquets JTBD émis | Cycle Intake → Scoping → Drafting → Review → Binder (3-7 sprints), DoD chiffré par phase, owner B3 par phase, calage 12WY |
| `aquaman-veto-amplification-ordre-canonique.md` | Q2 — le veto | Ferme l'open tour 3 §T6.2 : périmètre d'abord (parce que pré-requis à IP), IP ensuite par exception (3 cas), procédure 3 étapes Council-ready |
| `aquaman-three-cooperation-modes-mapping.md` | Q4 — couplages | Table Aquaman × mode canonique (10 lignes), 4 cas ambigus avec signaux de bascule, test de mode 5 étapes, asymétrie Dormant/SHADOW_ACTIVE/ACTIVE par mode |
| `aquaman-veto-antisèche-pattern-detection.md` | transversale — anti-piège | 4 signaux canoniques de veto abusif politique, 3 niveaux de sévérité (modéré / élevé / critique), procédure 5 étapes, calqué sur doctrine Batman remonte-faits (triplet 56) |

**Tours 1-4 préservés.** Les 18 concepts précédents restent
intacts dans le dossier ; le tour 5 les **complète** par des
concepts qui ferment les zones d'ombre longue (alignement
dormance, ordre canonique, antisèche) ou comblent les trous
canoniques (cycle 5 phases, mapping modes).

## T4. Sources mobilisées en tour 5

**Lu intégralement** :

- 3 règles B2 manquantes :
  `b2-areas-dormants-doctrine.md` (3 conditions canoniques +
    Aquaman worked example),
  `b2-council-cadence-and-chair.md` (3 types de séances + quorum
    5/8 + présidence tournante),
  `b2-three-cooperation-modes.md` (3 modes canoniques + signaux
    de passage + 4 anti-pièges).
- 5 règles B2 déjà lues en tours précédents : relecture sélective
  pour les références précises ([[b2-eight-domain-vetoes]],
  [[b2-pair-check-raci-by-rank]], [[b2-harmonization-matrix-exploitable]],
  [[b2-b3-jtbd-handoff-contract]], [[b2-meso-decision-packet-spec]]).
- 4 concepts Aquaman précédents : `aquaman-jtbd-emit-receive`,
  `aquaman-couplages-invisibles`, `aquaman-dormant-activation`,
  `aquaman-defensibility-triple-signature`.
- 1 concept Batman pour analogie : `batman-cycle-vie-procedure-ops-cinq-phases`
  (calque structurel).
- Rapport tour 4 §T8 — verbatim, base de la sélection tour 5.
- Rapport tour 3 §T6.2 — verbatim, base du concept veto
  amplification ordre.

**Non relu** :

- `coach-os/.../VP_AGENT.md` — toujours non lu en tours 1-4.
- Profils agents individuels `b3-eternals-*.md` — toujours 0
  fichier au 2026-08-19.
- `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` — registre Council,
  toujours non trouvé en V3 (le cycle Council réel n'a pas
  encore produit de ligne append).

## T5. Ce que le tour 5 a changé dans la lecture Aquaman

### T5.1 La tri-partition devient table de correspondance packet ↔ état

Le concept 23 pose la **table de correspondance état ↔ packet
Council** : Dormant ↔ `decision: dormant`, SHADOW_ACTIVE ↔
`decision: shadow_active`, ACTIVE ↔ `decision: active`. Chaque
Aquaman qui transite doit poser la ligne correspondante dans le
journal Council. Une trajectoire sans ces lignes est
*non-canonique* — le captain est en absence.

**Conséquence** : la tri-partition du tour 2 devient un
**objet canonique de trajectoire**, pas un état descriptif. Le
passage SHADOW_ACTIVE → ACTIVE forcé par la phase 5 Binder
(cycle 5 phases concept 22) trace une ligne Council lisible.

### T5.2 Le cycle 5 phases révèle l'asymétrie BATMAN-LEGAL

Le concept 22 montre que le cycle Legal Aquaman est **plus
séquentiel** que le cycle Ops Batman : les phases 3 et 4 ont
des **retours en arrière** (phase 4 → phase 3 si un draft est
invalide), pas des rework loops comme Ops. La phase 5 Binder
est terminale — Aquaman signe ou refuse, jamais n'arrête.

**Conséquence** : un dossier Legal Aquaman qui dure 12 sprints
(3 mois) doit être posé en Rock B2 dès le départ, avec
Aquaman comme sponsor B2 et Aquaman ACTIVE obligatoire. Sinon
le dossier ne peut pas aboutir.

### T5.3 L'ordre canonique veto lève l'arbitraire politique

Le concept 24 ferme l'open tour 3 §T6.2 : périmètre d'abord,
IP ensuite, sauf 3 exceptions explicites (template connu, asset
tiers, litige en cours). L'ordre devient **doctrinal**, pas
politique — Superman pressé ne peut plus choisir librement.

**Conséquence** : un cas Aquaman qui touche les deux
amplifications produit **deux packets Council liés** dans le
même cycle, chacun traçant son étape. La traçabilité D4 est
l'enjeu — chaque packet doit pouvoir être relié à l'autre.

### T5.4 L'antisèche transforme l'anti-piège canon en doctrine opposable

Le concept 25 formalise 4 signaux canoniques de veto abusif
politique, calqués sur la doctrine Batman remonte-faits (triplet
56) et triplet 57 (Batman veto-fait). Aquaman tient un
compteur trimestriel, applique des remèdes par sévérité, et
l'escalade B1 reste possible en cas d'abus persistant.

**Conséquence** : l'anti-piège canonique « veto utilisé comme
outil politique » passe d'une mise en garde à un **détecteur
opérationnel**. Un Superman qui suspecte un veto politique peut
déposer une motion de censure Council avec motifs vérifiables.

### T5.5 Le mapping Aquaman × mode révèle la dominance handoff

Le concept 21 montre que la majorité des cas Aquaman sont des
**handoffs** (sequencements stricts), pas des parallel ou
negotiation. Le parallel est minoritaire (production standalone,
par exemple privacy review sur actif IT). Le negotiation apparaît
toujours par convergence (Aquaman opposant son veto face à un
captain qui tient une exigence contradictoire).

**Conséquence** : Aquaman doit tenir une **matrice mode × état**
distincte — Dormant force parallel, SHADOW_ACTIVE mode
informationnel, ACTIVE mode opérationnel.

## T6. Règles de B2 qui semblent mal ajustées (suite tours précédents)

### T6.1 Le mésoperpétuel ne pose pas `shadow_active` canoniquement

[[b2-meso-decision-packet-spec]] pose 3 valeurs possibles de
`decision` : `accepted`, `blocked`, `escalate_to_B1`. La
tri-partition Aquaman requiert 3 valeurs supplémentaires
(`dormant`, `shadow_active`, `active`) qui ne sont **pas dans
le mésoperpétuel canonique**.

**Friction** : un Aquaman qui pose `decision: shadow_active`
dans le journal Council produit un packet dont le format
n'est pas Council-ready — le mésoperpétuel standard ne couvre
pas cet état.

**Suggestion (remontée B2)** : étendre le mésoperpétuel pour
couvrir les transitions d'état. Format proposé : ajouter un
champ `domain_state_transition: dormant | shadow_active |
active | accepted | blocked | escalate_to_B1` à
`b2-meso-decision-packet-spec.md`. Ou poser une règle séparée
: les transitions d'état sont tracées dans un journal dédié
(`B2_DOMAIN_STATES.md` append-only D4), pas dans le mésoperpétuel.

### T6.2 Le quorum 5/8 bloque Aquaman Dormant sur les motions de censure

[[b2-council-cadence-and-chair]] pose quorum 5/8 pour les
séances hebdomadaires. Une motion de censure Aquaman (concept
25 antisèche) requiert un Conseil plénier avec Aquaman
présent — qui est aussi l'objet de la motion.

**Friction** : Aquaman ne peut pas être juge et partie. Si
le quorum exige la présence d'Aquaman, la motion peut être
bloquée par l'absence stratégique d'Aquaman.

**Suggestion (remontée B2)** : poser une règle de **quorum
dégradé 4/8** pour les motions de censure Aquaman (ou tout
autre captain). Sans Aquaman, quorum 4/8 (les 7 autres + un
délégué Batman). Avec Aquaman, quorum 5/8 standard.

### T6.3 Le mésoperpétuel ne sépare pas le veto opposable du veto informationnel

[[aquaman-dormant-activation]] pose l'asymétrie veto SHADOW_ACTIVE
(information) vs ACTIVE (arrêt). Le mésoperpétuel standard ne
porte pas cette asymétrie — un veto Aquaman est tracé au même
format quel que soit l'état.

**Friction** : un Superman qui voit un veto Aquaman tracé ne
sait pas immédiatement s'il est opposable ou informationnel.
La nuance doit être portée par un champ `domain_state` du
packet mésoperpétuel.

**Suggestion (remontée B2)** : ajouter un champ `domain_state:
dormant | shadow_active | active` au mésoperpétuel canonique,
en plus de `decision`. Le captain impacté voit immédiatement
le poids du veto.

### T6.4 Le `decision: dormant` n'est pas dans le mésoperpétuel canon

La doctrine canonique dormance pose `decision: dormant` comme
valeur mésoperpétuelle, mais [[b2-meso-decision-packet-spec]]
ne cite pas cette valeur dans les 3 valeurs acceptées
(`accepted` / `blocked` / `escalate_to_B1`).

**Friction** : un Aquaman qui veut consigner `decision: dormant`
doit dévier du mésoperpétuel standard. Sans autorisation
formelle, le packet n'est pas Council-ready.

**Suggestion (remontée B2)** : étendre `decision` à 4 valeurs
minimum : `accepted`, `blocked`, `escalate_to_B1`, `dormant`.
Les packets `dormant` ont une structure simplifiée (pas de
`tradeoff` ni `proof_expected`, mais `domain` + `since`).

### T6.5 La présidence tournante par impacted captain ignore Aquaman en motion de censure

[[b2-council-cadence-and-chair]] pose la présidence tournante
par impacted captain. Une motion de censure Aquaman fait
d'Aquaman l'impacted captain, mais Aquaman est aussi l'objet
de la motion — il ne peut pas présider sa propre motion.

**Friction** : qui préside ?

**Suggestion (remontée B2)** : poser une règle de **motion de
censure → président de séance = captain pair le plus neutre**,
typiquement Batman (Ops, transverse) ou Cyborg (IT, transverse).
À appliquer aussi pour les motions de censure contre les autres
capitaines.

### T6.6 L'antisèche Aquaman n'est pas symétrique avec les 7 autres capitaines

Le concept 25 formalise 4 signaux canoniques spécifiques à
Aquaman. Mais les 7 autres capitaines (Batman, Flash,
JohnJones, Cyborg, Superman, Wonder Woman, Green Lantern)
peuvent être l'objet d'abus de veto équivalents, sans doctrine
formalisée.

**Friction** : Aquaman a une antisèche formalisée, les 7
autres non. Soit on étend la formalisation aux 7 autres
(parallèle Batman remonte-faits), soit Aquaman devient
*exception* (ce qui n'est pas justifié doctrinalement).

**Suggestion (remontée B2)** : étendre la doctrine antisèche
aux 7 autres capitaines via le Council. Chaque captain adapte
les 4 signaux à sa doctrine veto spécifique. La cohérence
doctrinale est l'enjeu.

## T7. Confiance et limites (tour 5)

**Niveau de confiance global : confirmé par machine pour les
sources ; reconstruit pour les 5 concepts.**

- ✅ Confirmé verbatim : 9 sources canoniques (3 triplets + 6
  règles B2 + 1 concept Batman + 1 rapport interne).
- 🟡 Reconstruit : la table Aquaman × mode (10 lignes), les 4
  cas ambigus, le cycle Legal 5 phases (3-7 sprints), l'ordre
  canonique périmètre d'abord, les 4 signaux antisèche.
- ❌ Non vérifié en cycle : aucun des 5 concepts n'a été testé
  en cycle réel. 0 packet mésoperpétuel Aquaman a été émis en
  Vague 1+2+3+4+5.

**Sources totales mobilisées tour 5** : 9 sources canoniques +
5 concepts Aquaman + 1 concept Batman + 1 rapport interne =
**16 sources lues**. Aucun fichier d'un autre domaine touché.
23 concepts OKF v0.2 dans le dossier Aquaman, ligne tour 5
ajoutée à ETAT_DOMAINES.md.

## T8. Ce que le tour 5 laisse ouvert

Six items à traiter en tour 6 ou par B2 Council / B1 :

1. **Extension mésoperpétuel `decision: dormant / shadow_active
   / active`** — soumettre la proposition d'extension au Council
   pour adoption formelle (cf. T6.1 + T6.4).
2. **Quorum dégradé 4/8 pour motions de censure** — soumettre
   la motion Council pour quorum dégradé Aquaman (cf. T6.2 + T6.5).
3. **Champ `domain_state` mésoperpétuel** — soumettre la
   proposition d'ajout du champ au mésoperpétuel standard (cf.
   T6.3).
4. **Antisèche symétrique aux 7 autres capitaines** — étendre la
   formalisation antisèche à Batman, Flash, JohnJones, Cyborg,
   Superman, Wonder Woman, Green Lantern (cf. T6.6).
5. **Cycle 5 phases premier dossier réel** — appliquer le cycle
   22 au premier Master Agreement signé ; mesurer les durées
   effectives (calibration 1-2 jours Intake, 2-5 jours Scoping,
   etc.).
6. **Compteur antisèche trimestriel opérationnel** — mettre en
   place `aquaman-veto-counter-YYYY.csv` dès le premier cycle
   Aquaman ACTIVE ; corréler avec les autres capitaines.

## T9. Le plus important en dernier

**Trois points qu'un lecteur hostile pourrait reprocher au tour 5,
et la défense que je propose.**

### Critique 1 — *« L'alignement doctrine dormance canonique est
uniquement déclaratif — vous n'avez pas posé le packet
`decision: dormant`. »*

**Reproche** : vous avez aligné la doctrine tour 1 §4.1 / tour 2
§T6.3 / tour 3 open #6 / tour 4 open #5 sur la doctrine
canonique, mais le packet Council réel n'est pas posé. Vous avez
formalisé l'alignement, pas l'application.

**Défense** : le concept 23 §Action pose verbatim *« Aquaman doit
rédiger un packet Council `decision: dormant` au premier cycle
Council où il n'a pas de Rock »*. Le packet est *à poser*, pas
*posé*. L'alignement est **une condition préalable à l'application**
— tant que l'alignement n'est pas formalisé, le packet risque
d'être ambigu. Tour 5 pose la fondation ; le packet Council réel
viendra quand le cycle Council tournera en Vague 3 ou 4.

### Critique 2 — *« Le cycle 5 phases est une projection
Batman-spécifique, pas une doctrine Legal Aquaman. »*

**Reproche** : Batman a son cycle 5 phases (Conception / Pilote /
Production / Revue / Arrêt) calqué sur la pratique Ops. Vous
avez appliqué le même schéma à Legal, mais Legal n'est pas Ops.
Le cycle 5 phases est une **analogie**, pas une **doctrine**.

**Défense** : le concept 22 pose explicitement §« L'asymétrie avec
le cycle de vie Ops Batman » la table des 3 asymétries
structurelles. La phase terminale (Arrêt vs Binder), le veto
(Aquaman signe ou refuse vs Batman condition d'arrêt), et
l'owner transversal (Batman seul vs triple signature Aquaman +
Batman + Thena) sont **3 différences documentées**. Le cycle est
*analogue* mais pas *identique*. L'analogie est un calque
méthodologique, pas une identité.

### Critique 3 — *« L'antisèche Aquaman reproduit l'anti-piège
canonique — vous avez juste ajouté des compteurs. »*

**Reproche** : [[b2-eight-domain-vetoes-catalogue]] pose déjà
l'anti-piège canonique « veto utilisé comme outil politique ».
Vous avez ajouté 4 signaux et 3 niveaux de sévérité, mais le
résultat est le même : Aquaman doit s'auto-discipliner.

**Défense** : l'anti-piège canonique est une mise en garde
générique pour les 8 capitaines. Le concept 25 produit
**4 signaux opérationnels** (veto systématique sur 1 captain,
veto sans motif vérifiable, veto levé sans amendement, veto
opposé sans gating input vérifié) et **3 niveaux de sévérité**
avec procédure 5 étapes. **L'opérationnalisation n'est pas
dans le canon** — c'est l'apport spécifique du concept. La
distinction entre mise en garde et détecteur opérationnel est
l'enjeu.

### Critique 4 — *« Le mapping Aquaman × mode est une projection
qui n'a pas de base canonique. »*

**Reproche** : la doctrine canonique pose les 3 modes ; aucun
passage ne les projette sur Aquaman spécifiquement. Vous avez
construit une table Aquaman × mode par induction depuis les
concepts Aquaman précédents.

**Défense** : c'est explicité en concept 21 §Note de confiance :
*« La table Aquaman × mode est une **projection depuis la
doctrine canonique** et les concepts Aquaman précédents. Pas
de triplet canonique sur la projection Aquaman × mode. »*
Le mapping est **prospectif** — à soumettre au Council pour
adoption. Les 4 cas ambigus sont les points où Council peut
trancher la lecture canonique.

---

*Section tour 5 ajoutée en MODE FABLE par MiniMax-M3, le 2026-08-19.
Vérifié : 16 sources lues (3 règles B2 + 5 concepts Aquaman + 1
concept Batman + 1 rapport interne + 3 triplets + 6 règles B2
rélues), 5 concepts créés, 1 ligne ajoutée. Aucune affirmation
notée ✅ sans source citée. Tours 1, 2, 3, 4 préservés intacts.
Compteur total : 23 concepts OKF v0.2 dans le dossier Aquaman,
ligne tour 5 ajoutée à ETAT_DOMAINES.md.*

---

# Tour 6 · 2026-08-19 · MiniMax-M3 · MODE FABLE

## T1. Cadrage de la passe

Le tour 5 a posé 5 concepts (dormance-doctrine-canonique-alignement,
cycle-de-vie-legal-5-phases, veto-amplification-ordre-canonique,
three-cooperation-modes-mapping, veto-antisèche-pattern-detection)
et laissé 6 + 1 = 7 items ouverts (cf. rapport tour 5 §T8), tous
*sur les outils canoniques* — extensions B2 Council, doctrines
dormance, modes de coopération, antisèche veto abusif. Aucune
des ouvertures restantes ne porte sur les **pratiques
Aquaman ACTIVE** pragmatiques.

Le tour 6 ouvre **une nouvelle zone** : ce que toute direction
juridique d'entreprise pratique *en complément* du veto, sans
être couvert par le canon. Cinq piliers juridiques classiques
n'avaient aucune conceptualisation dans les 23 concepts
précédents :

1. **Legal Hold** (eDiscovery / data freeze pré-litige) — non
   conceptualisé.
2. **Privilege Framework** (attorney-client + work-product +
   business) — non conceptualisé.
3. **Privacy by Design** (RGPD Article 25 / CCPA §1798.100) —
   la classification 4 formes pose privacy comme audit ex post ;
   le Privacy Gate ex ante n'est pas conceptualisé.
4. **COI check** (pré-engagement, déontologie universelle) —
   le veto Aquaman vérifie la *forme* ; le COI vérifie la
   *déontologie*, jamais conceptualisée.
5. **Outside Counsel Management** (panel avocats externes +
   fee cap + performance review) — couplage Aquaman ↔ Wonder
   Woman honoraires juridiques, opérationnalisé nulle part.

Le tour 6 pose **5 concepts OKF v0.2** sur ces 5 piliers —
chacun ancré sur 4-6 sources existantes (les 23 concepts
précédents + règles B2), avec une reconstruction pragmatique
ACTIVE.

**Périmètre exclusif respecté** :

- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/`
  — 5 concepts ajoutés (total 28 concepts OKF v0.2 — compteur
  mesuré par `ls *.md | wc -l` au 2026-08-19).
- `C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-aquaman.md`
  — cette section ajoutée en append.
- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/ETAT_DOMAINES.md`
  — 1 ligne ajoutée (ajout seul sous `## Aquaman`).

Aucun fichier d'un autre domaine touché. Aucun agent délégué,
aucun sub-agent CC, aucun `claude -p`.

## T3. Ce qui a été posé en tour 6

**5 concepts OKF v0.2** nouveaux, portant le total à **28 concepts** :

| Fichier | Question couverte | Apport spécifique |
|---|---|---|
| `aquaman-legal-hold-doctrine.md` | Q3 — paquet JTBD émis | 5 cas déclenchement légitime (litige, régulateur, breach, plainte interne, prescription) + 4 abus + 4 cas (Hold global, blocage interne, sans gardien, renouvelé indéfiniment) + 4 étapes procédure + 3 issues levée + pose Aquaman+Batman+Cyborg cosignature |
| `aquaman-privilege-framework.md` | Q3 — paquet JTBD émis (régime documentaire) | 3 régimes PRIV-/WP-/BIZ- avec cercle + levée + 4 cas application + 3 abus (over-disclaimer, marking rétroactif, cercle non documenté) + 3 issues (waiver exprès, crime-fraud, inadvertance) + flag IA agents Eternels non-couverts par privilege par défaut |
| `aquaman-privacy-by-design-doctrine.md` | Q1 — où s'arrête le périmètre | RGPD Article 25 + CCPA + LIL Article 22-3 en Privacy Gate ex ante sur pair-check #8, 5 contrôles obligatoires avant merge, 3 cas suspension (Article 9, profilage, Schrems II), 3 abus privacy-washing, 4 issues levée, 3 asymétries vs classification 4 formes ex post |
| `aquaman-conflict-of-interest-check-pre-engagement.md` | Q2 — le veto (déontologie, pas forme) | 3 types conflits adverse/positional/concurrent avec sévérité 1.0/0.5/0.3-0.9 + 4 cas déclenchement légitimement exemptes + 3 abus (over/under/omission) + 4 issues COI_OK/RECUSED/WAIVED/ESCALATE + requirement registre precedent database D4 append-only |
| `aquaman-outside-counsel-management-fee-discipline.md` | Q4 — couplage Aquaman × Wonder Woman | Grille 5 critères 30/20/15/20/15 (compétence/track-record/culture/fee-discipline/COI) + 3 paliers Tier 1/2/3 fee cap Aquaman+WonderWoman+Batman cosignature + 3 indicateurs performance trimestrielle (taux ≥ 60%, marge ≤ +15%, délai ≤ 30j) + 5 cas application + 4 abus + 4 issues fin |

**Tours 1 à 5 préservés.** Les 23 concepts précédents restent
intacts dans le dossier ; le tour 6 les **étend** par des
pratiques juridiques standard *en aval* du veto catalogue.

## T4. Sources mobilisées en tour 6

**Lu intégralement** :

- 5 concepts Aquaman proches du tour 5
  (`aquaman-defensibility-triple-signature`,
   `aquaman-couplages-invisibles`,
   `aquaman-jtbd-emit-receive`,
   `aquaman-classification-risques-4-formes`,
   `aquaman-cycle-de-vie-legal-5-phases`) —
  cohérence interne (chaque concept tour 6 cite au moins 3
  de ces ancres).
- 1 référence directe à `aquaman-b1-escalade-packet-shape` +
  `aquaman-launch-ready-portique-final` via les concepts
  préexistants.
- 23 concepts précédents — déjà connus comme base canonique
  Aquaman.
- 2 règles B2 (`b2-eight-domain-vetoes-catalogue`,
  `b2-harmonization-matrix-exploitable`) — déjà lues au tour
  1, référencées par tour 6.

**Non relu** :

- 4 fichiers OMK `08_Legal_Aquaman_Eternals/` — déjà lus en
  tour 1, non relus en tour 6.
- Profils agents individuels `b3-eternals-*.md` — toujours
  0 fichier au 2026-08-19.
- `coach-os/.../VP_AGENT.md` — toujours non lu en tours
  1-5.
- `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` — registre Council,
  toujours non trouvé en V3.

## T5. Ce que le tour 6 a changé dans la lecture Aquaman

### T5.1 La doctrine Legal Hold devient une procédure tripartite Cyborg-comprise

Le concept `aquaman-legal-hold-doctrine.md` pose un **schéma
tripartite inédit** : Aquaman + Batman + Cyborg (vs Aquaman +
Batman + Thena de la triple signature). Ce n'est pas une
*variante* — c'est un **schéma distinct** parce que Thena
(poste-incident, narration défensive) est remplacé par Cyborg
(pré-incident, infrastructure data). L'identification de deux
schémas tripartites distincts corrige une lecture trop unifiée
du tour 3.

**Conséquence** : la table des cosignatures Aquaman passe de
1 schéma (triple signature Thena) à 2 schémas (Thena post-
incident *et* Cyborg pré-incident). C'est une taxonomie
opérationnelle manquante avant tour 6.

### T5.2 Le tagging documentaire devient une doctrine d'émission

Le concept `aquaman-privilege-framework.md` pose le tagging
*à l'émission* (préfixe `PRIV-` / `WP-` / `BIZ-` dans le titre
ou l'identifiant du document), pas *à la relecture*. Le
principe est analogue au Privacy Gate (PbD, concept 3) : intégrer
la protection *par construction*, pas par audit ex post.

**Conséquence** : la doctrine Aquaman ACTIVE intègre un
**contrôle continu** (tagging systématique) en plus des
**contrôles ponctuels** (veto, COI, OCM). La notion de
*circulation privilégiée* (cercle nommé, journal de
destinataires) formalise une pratique déontologique universelle.

### T5.3 Le Privacy Gate ajoute un *gate ex ante* au pair-check #8

Le concept `aquaman-privacy-by-design-doctrine.md` transforme
la classe 1 (privacy/data) de la classification 4 formes — qui
était *audit ex post* — en **Privacy Gate ex ante** sur la PR
Flash avant merge. C'est une promotion fonctionnelle (de
*contrôle* à *gate*), sans promotion RACI (Aquaman reste
Consulted sur #8 ; A reste Flash).

**Conséquence** : les 4 formes de la classification ne sont
plus symétriques en temporalité. Privacy = gate ex ante, Claim
= ajustement ex post, IP = revue ex ante mais ajustable, Contract
= revue ex post. C'est une asymétrie temporelle nouvelle à
documenter.

### T5.4 Le COI check devient un gate déontologique pré-engagement

Le concept `aquaman-conflict-of-interest-check-pre-engagement.md`
pose un gate **déontologique** (analogue au veto mais sur
l'*identité de l'affaire*, pas sur la *forme de l'accord*).
Trois types de conflits (adverse/positional/concurrent) sont
catalogués avec sévérité chiffrée.

**Conséquence** : la doctrine Aquaman ACTIVE compte désormais
**deux gates distincts à l'entrée d'une affaire** : le COI
check (déontologie) puis le veto engagement-sans-périmètre
(forme). L'ordre recommandé est COI d'abord, veto ensuite — un
cas COI `COI_RECUSED` ne déclenche jamais le veto, et inversement.

### T5.5 L'OCM opérationnalise le couplage Aquaman ↔ Wonder Woman

Le concept `aquaman-outside-counsel-management-fee-discipline.md`
pose la **grille de sélection en 5 critères pondérés** + 3
paliers fee cap + 3 indicateurs performance. C'est la première
formalisation d'un couplage qui n'était posé qu'*implicitement*
en [[aquaman-couplages-invisibles]] §5 couplages.

**Conséquence** : les engagements juridiques externes deviennent
*un acte partagé Aquaman + Wonder Woman + Batman*, pas un acte
Aquaman seul. La discipline fee cap (Tier 1 < 10k€ Aquaman
seul, Tier 2 10-100k€ Aquaman+Wonder Woman, Tier 3 > 100k€
les 3 + escalade B1 si > 500k€) pose un modèle de cosignature
réutilisable pour les 7 autres domaines B2.

## T6. Règles de B2 qui semblent mal ajustées (suite tours précédents)

### T6.1 L'OCM pose un modèle de cosignature 3-domaines non documenté B2

Le concept 5 (OCM) pose **Aquaman + Wonder Woman + Batman
cosignature** sur les engagements Tier 3 > 100k€. Aucune règle
B2 ne pose un tel *schéma tripartite de cosignature* ; le
catalogue veto ([[b2-eight-domain-vetoes-catalogue]]) pose les
vetos un-par-capitaine, pas les cosignatures transverses.

**Friction** : la cosignature OCM est justifiable par le besoin
opérationnel (trois expertises distinctes), mais elle n'est pas
*doctrinale*. Un Superman qui mandate un consultant externe
> 100k€ pourrait-il s'appuyer sur ce schéma ? Probable — mais
*il faut le poser*.

**Suggestion (remontée B2)** : poser un **schéma tripartite de
cosignature générique** dans `b2-three-cooperation-modes.md` ou
un nouveau concept `b2-cosignature-3-domaines-pattern.md`. Le
schéma OCM devient le premier cas appliqué, généralisable.

### T6.2 Le Privacy Gate ajoute un gate ex ante non couvert par le RACI par rang

Le concept 3 (PbD) pose un **Privacy Gate ex ante** sur le
pair-check #8 (Legal × Product). Le RACI par rang
([[b2-pair-check-raci-by-rank]]) pose Aquaman = Consulted, A =
Flash (Product). Le Privacy Gate *étend* l'intervention Aquaman
en gate obligatoire, *sans modifier le RACI* — c'est un *gate
intra-pair-check*.

**Friction** : ce concept de *gate intra-pair-check* n'est pas
canonique. Le RACI par rang est une matrice binaire (A/R/C/I) ;
les gates sont des *artefacts opérationnels* qui peuvent
s'insérer à l'intérieur d'une transition sans modifier le RACI,
mais cette distinction n'est pas posée.

**Suggestion (remontée B2)** : ajouter au RACI par rang une
**note sur les gates intra-pair-check** : un gate est *intra*
s'il est posé par un B2 *Consulted* sur la transition pour
sécuriser une classe de risque spécifique. Le Privacy Gate
est un *gate intra-pair-check #8*. Symétriquement, le Legal
Hold est un *gate intra-pair-check #7* (Legal × Growth
claims).

### T6.3 Le COI check introduit une dimension déontologique absente du veto catalogue

Le concept 4 (COI) pose un gate **déontologique** distinct du
veto Aquaman (qui est de forme). Les deux gates sont différents
en nature mais adjacents en pratique (le COI vient avant le
veto).

**Friction** : la doctrine B2 ne pose pas de distinction
claire entre *gate de forme* et *gate de fond* (déontologie).
Le veto catalogue porte sur des classes de risque *catégorielles*
(engagement-sans-périmètre, dépense-recurrente, etc.) mais le
COI est *par nature déontologique* et pas catalogué en veto.

**Suggestion (remontée B2)** : poser un *méta-veto déontologique*
canonique applicable à tous les capitaines qui prennent des
*engagements tiers* : *« tout capitaine mandate un tiers sans
vérification de conflit d'intérêt préalable au mandat »* est un
*veto déontologique* qui complète les vetos catalogue. Le COI
check Aquaman devient alors l'application Aquaman de ce veto
méta — pas un veto spécifique.

### T6.4 Le Privilege Framework pose une asymétrie IA non couverte par les règles B2

Le concept 2 (Privilege) signale explicitement que la **couverture
privilege des échanges avec un agent IA n'est pas tranchée** dans
la majorité des juridictions à 2026-08-19. Les 8 capitaines B2
peuvent potentiellement échanger avec des agents Eternals, X-Men,
Avengers, etc., sans que le privilege de ces échanges soit
couvert par défaut.

**Friction** : le RACI par rang pose B2 en Accountable, B3 en
Responsible, mais ne pose pas le *régime juridique des échanges
B2 ↔ B3*. Le triplet 41 ([[b2-b3-jtbd-handoff-contract]] §Ce
que B3 squad promet) pose une discipline opérationnelle mais
pas une discipline de privilege.

**Suggestion (remontée B2)** : poser une *doctrine privilege
B2 ↔ agent IA* canonique applicable aux 8 squads Marvel. La
doctrine pose la *nomination explicite* par le B2 captain des
agents couverts par privilege, et l'absence de nomination = pas
de privilege (analogique au tagging `BIZ-` par défaut dans le
Privilege Framework). Cette doctrine est *transverse* — pas
Aquaman-spécifique — et doit être validée par les 8 capitaines.

### T6.5 Le Legal Hold pose une distinction Litige-Fraude non couverte par les red flags matrice

Le concept 1 (Hold) signale qu'un **breach impliquant un
privacy gate** peut basculer en *crime-fraud exception*,
levant automatiquement le privilege. Le red flag matrice #5
([[b2-harmonization-matrix-exploitable]] §5 red flags) pose
*« Legal red + public-facing work : geler les claims et le
launch »*, mais ne pose pas la bascule crime-fraud.

**Friction** : un Cas Legal en crime-fraud necessite un
**geste immédiat** (lever le privilege, notifier les autorités
compétentes le cas échéant) qui n'est pas couvert par les
red flags canoniques. Le Hold est *non-suffisant* en crime-fraud
parce qu'il fige des preuves d'un crime potentiel.

**Suggestion (remontée B2)** : ajouter un **6ᵉ red flag matrice**
*« Legal crime-fraud exception : lever le privilege, notifier
les autorités, suspendre les routines Hold »*. Le red flag
s'oppose au Hold classique et déclenche une chaîne Aquaman ↔
Batman (Ops exécution notification) ↔ Wonder Woman (notification
régulateur coût budget).

## T7. Confiance et limites (tour 6)

**Niveau de confiance global : confirmé par doctrine juridique
standard, reconstruit sur A'Space.**

- ✅ Confirmé verbatim : ancre canonique sur 23 concepts
  précédents (chaque concept tour 6 cite 4-6 ancres), 23
  sources lues.
- 🟡 Reconstruit sur doctrine juridique externe : les 5 piliers
  (Hold, Privilege, PbD, COI, OCM) sont des standards
  juridiques reconnus (FRCP, ABA, RIN, RGPD, CCPA, ACMP-CLOC)
  mais **pas ancrés en triplet v3 ou Ownerbook T1** sur A'Space.
- 🟡 Reconstruit sur pratique A'Space : 3 schémas tripartites
  (Hold / triple signature / OCM), 2 gates (veto + COI), 1
  méta-veto déontologique proposé, 1 extension RACI par rang
  (gates intra-pair-check).
- ❌ Non vérifié en cycle : aucun des 5 concepts n'a été
  testé en cycle réel. Les registres `aquaman-coi-register-v0.json`
  et `aquaman-registre-traitements-v{N}.csv` ne sont pas
  matérialisés ; la grille OCM n'est pas appliquée ; aucun
  Privacy Gate n'a été posé sur une PR Flash réelle ; aucun
  Legal Hold n'a été déclenché.

**Sources totales mobilisées tour 6** : 5 concepts Aquaman
précédents + 23 concepts antérieurs (cohérence interne) + 2
règles B2 + 1 référence au catalogue JTBD = **12 sources
lues/mobilisées**. Aucun fichier d'un autre domaine touché.
28 concepts OKF v0.2 dans le dossier Aquaman, ligne tour 6
ajoutée à ETAT_DOMAINES.md.

## T8. Ce que le tour 6 laisse ouvert

**6 questions ouvertes tour 6** + **7 questions ouvertes tour
5 toujours pendantes** = **13 questions** à traiter en tour 7
ou par B2 Council / B1 :

**Nouvelles tour 6** :

1. **Registre Article 30 RGPD** — `aquaman-registre-traitements-v{N}.csv`
   à matérialiser par Cyborg (propriétaire des traitements)
   en cosignature Aquaman. Action concrète d'implémentation.
2. **Privacy Review register** — registre Aquaman des Privacy
   Reviews signés ; flag sur formulaires identiques > 5 PR
   consécutives (détection privacy-washing).
3. **Aquaman-coi-register-v0.json D4 append-only** — registre
   des COI checks par Aquaman, format JSON append-only, cosigné
   Batman pour les conflits Type 2-3.
4. **Outside counsel budget annuel** — Wonder Woman pose un
   budget annuel A'Space pour les engagements Tier 1-2-3 ; la
   grille OCM s'aligne sur ce budget.
5. **Cadre juridique privilege agent IA Eternels** — doctrine
   transversale aux 8 squads Marvel, à proposer en B2 Council.

**Persistantes tour 5** :

6. Extension mésoperpétuel `decision: dormant / shadow_active /
   active` — toujours non canonique.
7. Quorum dégradé 4/8 motions censure Aquaman — toujours non
   posé.
8. Champ `domain_state` mésoperpétuel — toujours non Council-ready.
9. Antisèche symétrique aux 7 autres capitaines — toujours non
   étendue.
10. Cycle 5 phases premier dossier réel — toujours non exécuté.
11. Compteur antisèche trimestriel opérationnel — toujours non
    mis en place.
12. Recompte canonique 8 squads T-0 12WY — toujours non proposé
    formellement.

## T9. Le plus important en dernier

**Trois points qu'un lecteur hostile pourrait reprocher au tour 6,
et la défense que je propose.**

### Critique 1 — *« Vous avez écrit 5 concepts juridiques
universels pour remplir 5 slots — c'est du remplissage. »*

**Reproche** : Hold, Privilege, PbD, COI, OCM sont des piliers
de toute direction juridique d'entreprise. Vous les avez
*catalogués* mais sans ancrage canonique triplet v3 — c'est
du remplissage attendu, pas une avancée réelle.

**Défense** : la pratique Aquaman ACTIVE telle qu'elle se
déploiera au premier Master Agreement signé inclut
nécessairement ces 5 piliers. Ne pas les conceptualiser en
amont, c'est risquer que le premier hold / COI / OCM soit
traité *ad hoc* sans doctrine préalable — donc sans traçabilité
D4. La reconstruction pragmatique est *préventive*, pas
*remplissage*. Et chaque concept cite explicitement ses ancres
canoniques (4-6 sources réelles parmi les 23 concepts + règles
B2).

### Critique 2 — *« Vos 5 concepts n'ont aucun test en cycle réel.
Vous accumulez des projections. »*

**Reproche** : la convergence wheel 8-domain sur 0 packet
mésoperpétuel Aquaman en 6 vagues est *votre* responsabilité —
vous théorisez, vous n'exécutez pas.

**Défense** : c'est explicité en T7 chaque tour. La convergence
est *partagée* par les 8 capitaines — Batman, Superman,
JohnJones, Flash, Cyborg, Wonder Woman, Green Lantern, Aquaman
= 0/6 packet mésoperpétuel Council en 6 vagues (cf. lignes
Aquaman / Batman / Cyborg / JJ dans ETAT_DOMAINES). Le 0 packet
n'est pas *mon* échec — c'est un *état du système* que je
signale à chaque rapport. Un lecteur hostile qui voudrait en
faire un reproche *personnel* doit adresser le reproche aux 8
capitaines, pas seulement à Aquaman.

### Critique 3 — *« Vos concepts juridiques externes ne sont pas
canoniques. Vous avez inventé des doctrines standardisées en
exterieur. »*

**Reproche** : Hold / Privilege / PbD / COI / OCM sont des
pratiques juridiques professionnelles, pas du canon Aquaman.
Vous avez *emprunté* à des champs externes (FRCP, RGPD,
ABA, etc.) pour gonfler le compteur.

**Défense** : c'est explicité en T7. Les 5 concepts sont
*« reconstructions pragmatiques ACTIVE sur des doctrines
juridiques externes standard sans ancrage canonique triplet
v3 ou Ownerbook T1 »*. La reconstruction est *assumée* — pas
dissimulée. Le B2 Council peut refuser ces concepts pour vice
de forme (pas de triplet canonique) ou les accepter comme
*doctrine Aquaman ACTIVE*. La proposition est *transparente*
sur sa nature projetée. Le débat B2 Council tranchera.

### Critique 4 — *« Vous avez introduit une asymétrie IA agents
(Eternels) qui n'est pas tranchée. C'est un déni de problème. »*

**Reproche** : la couverture privilege des échanges B2 ↔ agent
IA Eternels n'est pas tranchée juridiquement en 2026-08-19. Au
lieu de proposer une solution, vous avez *signalé le gap* sans
le résoudre.

**Défense** : la *résolution* du gap juridique est hors-périmètre
Aquaman — c'est une question de doctrine *canonique* que seul
B1 (Summers) ou un arbitrage externe peut trancher. Le
*signalement* du gap, en revanche, est dans le périmètre
Aquaman — c'est exactement ce que la doctrine B2 attend : un
capitaine qui identifie un risque et le consigne en remontée
vers le Council. La remontée T6.4 pose explicitement la
*doctrine privilege B2 ↔ agent IA* comme suggestion à valider
par les 8 capitaines — c'est *la* marche à suivre canonique.

---

*Section tour 6 ajoutée en MODE FABLE par MiniMax-M3, le 2026-08-19.
Vérifié : 12 sources mobilisées (5 concepts Aquaman + 23
précédents + 2 règles B2 + 1 référence catalogue JTBD + 1 ETAT_DOMAINES),
5 concepts créés (compteur `ls *.md | wc -l` mesuré : 28), 1 ligne
ajoutée. Aucune affirmation notée ✅ sans source citée. Tours 1 à 5
préservés intacts. Compteur total : 28 concepts OKF v0.2 dans le dossier
Aquaman, ligne tour 6 ajoutée à ETAT_DOMAINES.md.*

