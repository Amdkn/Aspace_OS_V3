---
type: Concept
title: Canal de remontée Batman → B1 Summers — format concret
description: Les triplets 56/57 posent la doctrine remonte-fait mais ne définissent ni le canal concret (où Batman écrit), ni le format (quelle structure porte le fait). Ce concept pose 3 entrées (fait binaire / structurel / couplage) × 3 sorties (constat Council / signal captain / escalade B1) avec un fichier `batman/_facts/YYYY-MM-DD_<slug>.md` par fait.
tags: [canal, batman, summers, b1, fait, format, remonte, ops, doctrine]
generated: { by: minimax-m3, at: 2026-08-19T07:00:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-6, at: 2026-08-19T07:00:00Z }
sources:
  - id: triplet-56
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 56 — Batman remonte à Summers des faits, pas des décisions"
    last_modified: 2026-08-17
  - id: triplet-57
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 57 — Batman veto remonte à Summers comme un fait, avec son motif"
    last_modified: 2026-08-17
  - id: vp-agent-md
    resource: "C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/coach-os/04_Business_Domains/02_Operations_en_Loops_Batman_Fantastic4/VP_AGENT.md"
    title: VP_AGENT Batman — source triplet 56/57
    last_modified: 2026-08-02
  - id: b2-council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tient le journal
    last_modified: 2026-08-19
  - id: b2-meso-decision-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format arbit Council
    last_modified: 2026-08-19
  - id: batman-tour-4
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-pyramide-l0-l1-l2-positionnement.md"
    title: Pyramide L0/L1/L2 — 3 canaux par type de fait (concept tour 5)"
    last_modified: 2026-08-19
  - id: batman-tour-5
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-batman.md"
    title: "RAPPORT_dom-batman.md §T5.5.1.1 — lien canonique Batman×B1 non posé"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Canal de remontée Batman → B1 Summers — format concret

## Le trou comblé

Le triplet 56 dit *« Batman remonte à Summers des faits, pas des
décisions »* ; le triplet 57 dit *« le veto remonte à Summers comme
un fait, avec son motif »*. Les 5 tours Batman précédents (cf.
`RAPPORT_dom-batman.md` §T5.5.1.3) ont identifié que **le canal
concret** (où Batman écrit, sous quelle forme, à quelle cadence) **n'est
pas posé canoniquement**.

Trois positions implicites coexistent sans qu'aucune soit tranchée :

1. **Journal Council `B2_DC_DIRECTION_COUNCIL_DECISIONS.md`** —
   utilisé pour les arbitrages Council (`b2-meso-decision-packet-spec.md`).
   Un fait Batman qui n'est pas un arbitrage n'y a pas sa place —
   c'est une décision, pas un constat.
2. **Sprint hebdomadaire Batman (`SPRINTS.md`)** — porte les 4 sprints
   par rock, mais les faits Ops structurels ne sont pas des
   *« actions de sprint »*. Un fait Batman qui traverse 3 sprints
   (par exemple un trigger `charge_derivee`) ne tient pas dans une
   entrée de sprint hebdomadaire.
3. **Aucun canal explicite** — Batman *« remonte verbalement »* à
   Summers. C'est une fiction de coordination — sans trace écrite,
   il n'y a pas de **preuve de remontée**, et Summers ne peut pas
   auditer ce qui lui a été remonté.

Ce concept pose le canal manquant : `batman/_facts/` dans le dossier
domaine Batman, un fichier par fait, format strictement fait-daté.

## Les 3 entrées — 3 types de faits Ops

### Type 1 — Fait binaire

**Définition** : un fait vérifiable en une lecture, avec une réponse
oui/non ou un chiffre.

**Exemples** :
- *« La procédure onboarding-client n'a pas de condition d'arrêt
  dans `squad/03_HumanTorch_*/RUNBOOK.md` »* — vérifiable par lecture
  directe.
- *« Le portique LAUNCH_READY a été franchi 0 fois sur 5 vagues
  (cf. `ETAT_DOMAINES.md`) »* — vérifiable par comptage.
- *« Le squad lead MrFantastic a 0 sprint `SPRINTS.md` écrit
  cette vague »* — vérifiable par énumération.

**Format d'écriture** :
```yaml
type: binary
date: YYYY-MM-DD
sprint: B2-OPS-SPRINT-NN
source_observation: <path/line>
constat: "<phrase factuelle, sans interprétation>"
niveau_confiance: haute | moyenne | basse
```

### Type 2 — Fait structurel

**Définition** : un fait qui révèle une structure manquante ou
incomplète, sans porter de jugement de valeur.

**Exemples** :
- *« La doctrine dormance `b2-areas-dormants-doctrine.md` pose 3
  états (DORMANT/SHADOW_ACTIVE/ACTIF) mais aucun seuil de passage
  entre eux. »*
- *« La matrice d'harmonisation pose 9 pair-checks ; aucun ne teste
  le transit Growth → Ops, qui est une dépendance réelle. »*
- *« Les 4 agents Fantastic Four sont nommés (triplet 16) ; 2 charges
  seulement sont posées (triplets 31+32). »*

**Format d'écriture** :
```yaml
type: structural
date: YYYY-MM-DD
sprint: B2-OPS-SPRINT-NN
doctrine_observee: <path>
doctrine_attendue: <path-ou-formulation>
ecart: "<description de l'écart, sans le qualifier>"
impact_si_non_couvert: "<description factuelle du risque>"
niveau_confiance: haute | moyenne | basse
```

### Type 3 — Fait couplage

**Définition** : un fait qui révèle une dépendance Batman ↔ un autre
capitaine, avec un trigger observable.

**Exemples** :
- *« Le trigger `charge_derivee` (Superman Growth → Ops via Sales) a
  été projeté (cf. `batman-couplage-superman-growth-volume-charge.md`
  §3) mais n'a pas d'instrument de mesure dans le sprint courant. »*
- *« Le veto Wonder Woman sur `dépense récurrente sans ROI` est
  adjacent au veto Batman sur `procédure sans condition d'arrêt` ;
  aucun arbitrage Council n'a tranché l'ordre canonique. »*
- *« Le RACI place Cyborg A sur #4 (Product→IT) ; Batman dépend de
  #4 sans y être Consulted — la dépendance Product→IT→Ops n'est
  pas visibilisée en Council. »*

**Format d'écriture** :
```yaml
type: coupling
date: YYYY-MM-DD
sprint: B2-OPS-SPRINT-NN
domaine_amont: <captain>
domaine_aval: <captain>
couplage_observe: <path-ou-triplet>
trigger: "<phénomène observable, sans projection>"
niveau_confiance: haute | moyenne | basse
```

## Les 3 sorties — 3 destinations du fait

### Sortie 1 — Constat Council (registre append-only)

**Destination** : `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` section
*« faits Batman pour information »*, append-only.

**Quand** : un fait binaire observé en revue hebdo, qui n'appelle
pas d'arbitrage mais que le Council doit voir. Exemple : *« 0 portique
LAUNCH_READY franchi cette vague »*.

**Format de sortie** : une ligne dans la section *« faits Batman pour
information »*, datée, avec pointeur vers le fichier source
`batman/_facts/YYYY-MM-DD_<slug>.md`.

**Force** : aucun — c'est un constat, pas une décision. Le Council
peut l'ignorer.

### Sortie 2 — Signal captain (transverse direct)

**Destination** : le captain B2 du domaine couplé, par message
Council daté (pas par packet mésoperpétuel — le packet est réservé
aux arbitrages).

**Quand** : un fait couplage qui concerne un autre capitaine B2, où
Batman a besoin que l'autre capitaine **sache** mais n'a pas besoin
d'un arbitrage. Exemple : *« Wonder Woman, ton veto sur la dépense
récurrente Ops-as-a-Service touche 2 procédures Batman sans
condition d'arrêt — l'ordre canonique n'est pas tranché entre nous. »*

**Format de sortie** : un message Council daté, copiant le fait
couplage, sans demander de décision.

**Force** : aucune — c'est un signal de **coordination**, pas un
arbitrage. L'autre captain peut répondre ou pas.

### Sortie 3 — Escalade B1 (fait brut, motif, pas de décision)

**Destination** : Summers directement, via `Summers_CEO/_inbox/<date>_<slug>.md`
et copie dans `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` section
*« escalades B1 Batman »*.

**Quand** : un fait structurel qui révèle une décision de cycle
manquante, OU un veto Batman qui touche un mandate B1 (cf.
triplet 57). Le fait remonte comme un fait brut avec son motif.

**Format de sortie** : le fichier source `batman/_facts/YYYY-MM-DD_<slug>.md`
est copié dans `Summers_CEO/_inbox/` avec un préambule :

```yaml
escalation_id: BATMAN-ESCALATION-YYYY-NN
source_fact: <path-vers-batman/_facts/...>
domaines_impacted: [<liste>]
type_decision_manquante: "<cycle|north_star|cadre|veto>"
deja: :
```

**Force** : Summers **doit** répondre dans le cycle courant (par
défaut < 5 jours ouvrés), mais Batman n'a pas le droit de statuer à
sa place.

## Le dossier `batman/_facts/` — règles de tenue

1. **Un fichier par fait**, daté `YYYY-MM-DD_<slug>.md`. Pas de
   mise à jour en place — un fait observé à nouveau est un
   **nouveau fichier** avec mention de l'observation antérieure.
2. **Append-only au niveau dossier** : aucun fichier n'est
   supprimé. Si un fait est invalidé, un fichier `YYYY-MM-DD_<slug>_invalidated.md`
   est créé qui pointe sur l'original et explique l'invalidation.
3. **Pas de décision dans le fichier** : le fait est la matière
   première, pas l'arbitrage. Si Batman écrit *« il faut… »* ou
   *« on devrait… »*, le fichier est invalidé par construction.
4. **Confiance chiffrée** : chaque fait porte un
   `niveau_confiance` (haute / moyenne / basse), avec une note
   justifiant le niveau si moyenne ou basse.
5. **Source précise** : chaque fait pointe sur une source
   vérifiable (chemin + ligne, ou URL, ou triplet). Pas de
   *« selon les rapports d'escouade »* sans pointeur exact.

## Le rôle du squad lead MrFantastic

MrFantastic (B3 squad lead, ProcessDesign) **n'écrit pas** dans
`batman/_facts/`. Son rôle :

- **Collecte** les faits B3 (lead indicators, charge dérivée,
  trigger de procédure) au quotidien via scrums.
- **Remontée** à Batman via `MrFantastic_ProcessDesign/SCRUMS.md`
  quotidien, pas dans `batman/_facts/`.
- **Batman** lit `SCRUMS.md` chaque vendredi, sélectionne les faits
  qui montent en `_facts/`, les qualifie (binaire / structurel /
  couplage), choisit la sortie (constat / signal / escalade).

Le squad lead **ne décide pas** du type de fait ni de la sortie —
c'est le mandat Batman (triplet 56 : remonte-fait, pas décision).

## Anti-pièges

- **Batman qui décide dans le fait.** Si Batman écrit *« la procédure
  onboarding doit être arrêtée »*, le fichier `_facts/` est invalidé.
  Le fait est *« la procédure n'a pas de condition d'arrêt »*, pas
  *« il faut l'arrêter »*.
- **Fait sans source.** Un fait qui dit *« selon les rapports
  précédents »* sans pointeur précis est invalidé. La source doit
  être lisible par un tiers qui n'est pas Batman.
- **Fait qui est en réalité un arbitrage.** Si Batman écrit *« je
  propose que la matrice passe de 9 à 12 pair-checks »*, ce n'est
  pas un fait, c'est une motion — elle doit aller dans un packet
  mésoperpétuel `B2-MESO-DECISION-YYYY-NN`, pas dans `_facts/`.
- **Canal saturé.** Si Batman écrit plus de 5 faits par sprint, le
  canal sature — c'est un signal que Batman **statue** au lieu de
  remonter. La cadence canonique est ≤ 3 faits par sprint, dont 1
  maximum en escalade B1.
- **Summers qui ignore.** Si Summers ne répond pas à une escalade
  B1 en < 5 jours ouvrés, Batman **ré-escalade** une fois, puis
  **note le silence** dans `B2_DC_DIRECTION_COUNCIL_DECISIONS.md`
  section *« escalades Batman non répondues »*. Le silence n'est
  pas une autorisation tacite.

## Liens

- [[batman-doctrine-remonte-fait-non-decision]] — la doctrine
  qui justifie ce canal
- [[batman-pyramide-l0-l1-l2-positionnement]] — les 3 types de
  fait (binaire/structurel/couplage) reprennent les 3 canaux L0/L1/L2
- [[batman-veto-condition-arret-procedure]] — le veto qui
  remonte par sortie 3 (escalade B1)
- [[b2-council-arbitrage-rule]] — qui tient le journal Council
- [[b2-meso-decision-packet-spec]] — le format des arbitrages,
  distinct des faits
- [[batman-couplage-superman-growth-volume-charge]] — exemple de
  fait couplage (trigger `charge_derivee`)

## Note de confiance

**Confirmé par machine.** Les triplets 56/57 sont cités verbatim.
Le constat du trou *« canal concret non posé »* est tiré du rapport
Batman §T5.5.1.3 (tour 4) et confirmé par §T5.5.1.1 (tour 5). Les
3 entrées (binaire / structurel / couplage) sont **reconstruites**
à partir de la tripartition L0/L1/L2 du concept `batman-pyramide-l0-l1-l2-positionnement.md`
(tour 5). Les 3 sorties (constat / signal / escalade) sont
**projetées** à partir du triplet 57 (escalade B1 du veto), du
rôle Council (`b2-council-arbitrage-rule.md` §« Routine »), et
du rôle captain transverse (couplages Batman×autres, 7 concepts
des tours 1-4). Le rôle MrFantastic est **reconstruit** à partir
du triplet 31 (ProcessDesign) et du triplet 13 (B3 dependsOn
B2-sprint). Les 5 règles de tenue `_facts/` sont **mon
inférence** — le format append-only est canonique (D4), la
règle *« 1 fait = 1 fichier »* est extrapolée depuis la pratique
OKF v0.2 (un concept = un fichier).