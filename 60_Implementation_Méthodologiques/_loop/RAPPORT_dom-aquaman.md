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
