---
type: Rapport
title: Rapport Vague 2 — escouade Superman (Growth/01)
description: Rapport de l'escouade Superman après lecture du corpus canon (B2 Council, triplets v3, matrice d'harmonisation, RACI par rang) et production de 6 concepts OKF v0.2 dans le dossier superman/. Le rapport signale ce que le corpus ne dit pas sur Superman et identifie 2 règles B2 qui paraissent mal ajustées pour le domaine Growth.
tags: [rapport, vague-2, superman, growth, b2, corpus, lacunes, regles-a-revoir]
generated: { by: minimax-m3, at: 2026-08-19T04:10:00Z }
verified:
  - { by: process:lecture-corpus-superman, at: 2026-08-19T04:10:00Z }
sources:
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel
    last_modified: 2026-08-17
  - id: vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2
    last_modified: 2026-08-19
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2
    last_modified: 2026-08-19
  - id: triplets-v3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: Triplets v3 — 58 triplets, ligne 19 Superman People & Brand, ligne 27 veto, ligne 58 Wonder Woman extension
    last_modified: 2026-08-17
  - id: substrat-omk
    resource: "C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/carto/01_picard_w2_unread.txt"
    title: Carto substrat OMK — 6 B3 Guardians identifiés
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Rapport Vague 2 — escouade Superman (Growth/01)

## Cadrage (MODE FABLE — étape 1)

**Ce que j'ai fait** : 6 concepts OKF v0.2 dans
`70_Onthologies/pulse/domaines/superman/`, plus une ligne ajoutée
sous `## Superman (Growth)` dans `ETAT_DOMAINES.md`, plus ce
rapport.

**Ce que je n'ai PAS fait** : aucun contact avec les 7 autres
dossiers `domaines/` (aquaman, batman, cyborg, flash, green-lantern,
john-jones, wonder-woman). Aucune modification de `ASpace_OS_V2/`.
Aucun `git`, `npm install`, ou autre acte système. Aucun secret dans
les sorties. Aucun `human:` dans les champs `verified` (Garde-fou
respecté : un acteur `human:` exige une revue humaine).

**Ce dont j'avais besoin** : corpus canon B2 (5 fichiers
`pulse/b2/*.md`), 4 fichiers de référence (`50_Distillation/projets/
eight-domain-avengers-wheel.md`, `50_Distillation/projets/fifty-three-b3-agent-roster.md`,
`50_Distillation/areas/business-wheel-harmonization-matrix.md`,
`70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md`),
triplets v3 filtrés sur Superman/Growth, et le substrat OMK (carto
`01_picard_w2_unread.txt`). Tout a été trouvé sauf **le 7ᵉ agent
B3 Guardians** qui devrait exister par symétrie avec les autres
squads.

## Preuves (MODE FABLE — étape 2)

**Concepts produits** :

| Fichier | Lignes | Sources canoniques |
|---|---|---|
| `domain-perimeter.md` | ~140 | avengers-wheel, vetoes-catalogue, harmonization, triplet v3 ligne 19 |
| `veto-catalogue-concrete.md` | ~170 | vetoes-catalogue, triplet v3 ligne 27, org-json, veto-amplification |
| `jtbd-emit-receive.md` | ~155 | substrat-omk (6 B3), triplet v3 ligne 19, b2-b3-contract, avengers-wheel, b3-reception-checklist |
| `pair-checks-dependencies.md` | ~140 | harmonization, raci-by-rank, vetoes-catalogue, avengers-wheel |
| `veto-amplification-candidate.md` | ~150 | veto-amplification-cycle, triplet v3 ligne 58, vetoes-catalogue, council-cadence |
| `cooperation-mode-patterns.md` | ~175 | three-modes, harmonization, raci-by-rank, vetoes-catalogue, council-arbitrage |

**Lecture sur combien** : 11 fichiers canoniques lus
intégralement ou substantiellement (5 b2/* + 4 références +
triplets v3 filtrés + carto substrat OMK). 4 fichiers B2
secondaires mentionnés mais non lus en intégralité
(`b2-b3-jtbd-handoff-contract.md`, `b3-jtbd-packet-reception-checklist.md`,
`b2-council-cadence-and-chair.md`, `b2-council-arbitrage-rule.md`
lus ; `b2-failsafe-paperclip-recovery.md`,
`b2-areas-dormants-doctrine.md`, `b2-veto-amplification-cycle.md`,
`b2-three-cooperation-modes.md`, `b2-pair-check-raci-by-rank.md`,
`b2-meso-decision-packet-spec.md` lus).

**Ce que je n'ai pas couvert** : le Ownerbook T1 OMK (qui pose le
DoD-1 `ls .claude/agents/b3-1-* | wc -l` ≥ 7) — pas dans mon
périmètre V3. Le Coach OS V1 complet (`coach-os/04_Business_Domains/
05_People_et_Brand_Superman_Guardians/VP_AGENT.md` cité par triplet
19) — pas dans mon périmètre V3. Les 6 fichiers `01_B3_AGENT_ROSTER.md`
des autres squads (lus via le fifty-three concept, mais pas lus
directement).

## Attaque (MODE FABLE — étape 3) — trois réfutations tentées

### Réfutation 1 — Superman n'est PAS Growth, c'est People & Brand

Le triplet v3 ligne 19 dit verbatim *« Superman (VP B2 domaine 5 —
People & Brand) commande le squad Guardians (6 techniciens :
StarLord, Rocket, Gamora, Drax, Groot, Mantis) »*, source
`coach-os/04_Business_Domains/05_People_et_Brand_Superman_Guardians/VP_AGENT.md`.

**J'ai tenu compte de cette réfutation.** Le concept
`domain-perimeter.md` §« Pourquoi ces frontières existent dans le
canon » cite cette divergence et la traite comme un héritage de
version non re-tranché. Le triplet 27 (hasVetoOver promesse-non-tenue)
et le catalogue des 8 vetos positionnent Superman en **Growth** —
canon V4. Le triplet 19 est **legacy V1** (Coach OS). **Pas de
contradiction tranchée** — l'incohérence est signalée.

**Niveau de confiance** : *moyenne*. Le canon V4 est plus récent
(2026-07-15 ACTIVE) que Coach OS V1 (2026-05-27 daté). Mais le
triplet 19 est dans le substrat actuel (v3-business.jsonl daté
2026-08-17), donc **la divergence est vivante** — un arbitrage
B2 réel qui s'appuierait sur le triplet 19 serait défensable.

### Réfutation 2 — Le veto Superman est trop vague pour être vérifiable

Le veto canonique *« bloque toute prise de parole publique qui
promet un résultat que la delivery ne tient pas »* pose un
**critère de pratique**, pas un artefact documentaire. Sept autres
vetos catalogue portent sur des artefacts vérifiables (mandat
écrit, condition d'arrêt, accord, etc.). Superman seul porte sur
une **pratique de delivery** — quelque chose qui n'est pas un
document mais une trajectoire.

**J'ai tenu compte de cette réfutation.** Le concept
`veto-catalogue-concrete.md` §« Pourquoi le veto Superman est le
plus difficile à opérationnaliser » pose explicitement le tableau
comparatif des 8 vetos et identifie Superman comme **le seul à
critère non-documentaire**. L'amplification candidate
(`veto-amplification-candidate.md`) **restaure la vérifiabilité**
en exigeant une date ou un horizon mesurable.

**Niveau de confiance** : *haute* sur la difficulté, *moyenne*
sur l'amplification. Le canon Council-arbitrage note *« aucun
packet mésoperpétuel n'existe encore »* — donc l'amplification
n'a pas été testée en cycle réel.

### Réfutation 3 — La distribution 40/40/20 est une projection, pas une mesure

Le concept `cooperation-mode-patterns.md` projette 40% parallel /
40% handoff / 20% negotiation pour Superman. Aucun cycle OMK réel
n'a été mesuré (le canon Council-arbitrage note la même limite).
La projection est **invérifiable** — un cycle pourrait montrer
60/30/10 ou 25/45/30.

**J'ai tenu compte de cette réfutation.** Le concept marque
explicitement *« Projection, pas un comptage canonique »* et la
*« Note de confiance »* finale précise *« Projets, à moitié étayé »*.
La projection est basée sur la matrice + RACI + triplet 28/58, pas
sur des mesures.

**Niveau de confiance** : *basse* sur les pourcentages, *moyenne*
sur la tendance (handoff dominant à cause des pair-checks amont
Legal/Finance).

## Vérification (MODE FABLE — étape 4)

**Ce que j'ai vérifié** :

- **Existence des 6 fichiers .md** dans `superman/` — confirmé par
  `ls -la` (6 fichiers, 8.4-12.2 KB chacun, datés 2026-08-19
  03:32-03:35).
- **Cohérence frontmatter OKF v0.2** — 6 fichiers avec champs
  `type`, `title`, `description`, `tags`, `generated`, `verified`,
  `sources`, `okf_version`. Aucun champ `human:` dans `verified`
  (Garde-fou).
- **Append à ETAT_DOMAINES.md** — lu après modification, ligne
  Superman présente sous `## Superman (Growth)` après les sections
  Aquaman et Wonder Woman.
- **Triplet 19 vs canon V4** — vérifié par lecture du triplet
  ligne 19 et des sources `eight-domain-avengers-wheel.md` +
  `b2-eight-domain-vetoes-catalogue.md`. **Divergence confirmée**.
- **Compte 6 B3 Guardians dans substrat OMK** — vérifié par
  `carto/01_picard_w2_unread.txt` lignes 63-77. Six agents listés
  (StarLord_Story, Rocket_Auto, Gamora_Target, Drax_Closing,
  Groot_Content, Mantis_VoC).
- **Triplet 58 Wonder Woman extension** — vérifié verbatim.

**Ce que je n'ai PAS vérifié** :

- Le 7ᵉ agent B3 Guardians (Ownerbook T1 OMK hors périmètre V3).
- Le contenu réel des fichiers `B2_Business_Domains/01_Growth_Superman_Guardians/`
  dans OMK (`00_B2_DOMAIN_CONTROL_ROOM.md`,
  `01_B3_AGENT_ROSTER.md`, etc.) — chemin introuvable dans
  `ASpace_OS_V3/`, seulement `ASpace_OS_V2/`. ASpace_OS_V2 hors
  périmètre (Garde-fou).
- L'existence du cycle sprint hebdo avec un packet mésoperpétuel
  Superman réel — *« aucun packet mésoperpétuel n'existe encore »*
  dans le canon.
- La présidence tournante du B2 Council en pratique (5/8 quorum
  tenable ?) — *« À vérifier en cycle réel »* dans
  `b2-council-cadence-and-chair.md`.

## Rapport (MODE FABLE — étape 5) — ce que le corpus ne dit pas

C'est la section la plus importante. **Le canon B2 lus ne répond
pas à 5 questions sur Superman Growth** :

### 1. Qui tient l'ICP — Superman ou Sales (JohnJones) ?

Le pair-check #1 (Growth → Sales) teste *« l'attention devient-elle
opportunité qualifiée ? »*. Le RACI par rang pose Sales en A,
Superman en C, B3 Illuminati en R. **Mais qui définit l'ICP que
Superman applique pour qualifier l'attention ?** Le canon ne dit
pas.

Cas projeté : si l'ICP est défini par Sales, Superman est un
**exécutant** (apply ICP). Si l'ICP est défini conjointement,
Superman est un **co-auteur**. Si l'ICP est défini par Superman
(segmentation Gamora_Target), Sales devient exécutant.

Le canon n'a pas tranché. **C'est un arbitrage Council prévisible**.

### 2. Qui tient le Brand — Superman, People, ou les deux ?

Le triplet 19 cite Superman en People & Brand. Le canon V4
positionne Superman en Growth. La squad Guardians inclut
StarLord_Story (narrative de marque) et Groot_Content (content de
marque). Le canon ne dit pas si People (Green Lantern) mandate
StarLord ou si Superman mandate StarLord.

Cas projeté : si People mandate, le contrat B2 → B3 est signé par
Superman (sponsor B2) mais le DoD est fixé par People. Qui est
Accountable ? **Pas de réponse canonique**.

### 3. Qui tient l'analytics stack — Superman ou Cyborg ?

Le pair-check #4 (Product → IT) parle de déploiement et monitoring
de produit, pas d'analytics marketing. Mixpanel/Amplitude/PostHog
sont une dépendance IT **et** un livrable Growth. Le canon ne
tranche pas.

Cas projeté : si Cyborg déploie et Superman lit, c'est **handoff**
(Cyborg upstream, Superman downstream). Mais le contrat B2 → B3
n'est pas signé entre les deux — c'est un gap.

### 4. Quel est le DoD par défaut de l'attention qualifiée ?

Le signal `NEEDS_SIGNAL` est émis par Superman quand l'attention
est insuffisante. Mais **quel est le seuil** de l'attention
qualifiée ? *1000 MQL par trimestre* ? *10% de conversion en SQL* ?
Le canon n'a pas de valeur par défaut — chaque mandat B1 fixe
son propre seuil.

Conséquence : Superman doit obtenir un **DoD chiffré** de B1 à
chaque mandat (cf. `b2-b3-jtbd-handoff-contract.md` §`dod_bornee`).
Sans DoD chiffré, le pair-check #1 (Growth → Sales) n'a pas de
critère de passage.

### 5. Quel est le rôle de Superman en cas de B1 dormant ?

`b2-areas-dormants-doctrine.md` pose Aquaman (Legal) comme exemple
canonique de dormance — *« ne produit rien tant que
`00_Summers_CEO/03_Master_Agreements/` reste vide »*. Superman
**peut-il** être dormant ? Si B1 (Summers) ne mandate pas
Growth, Superman attend. Mais Superman émet `NEEDS_SIGNAL` — un
état actif qui dit *« j'attends un signal »*, pas un état dormant
qui dit *« je n'ai rien à faire »*.

Le canon ne pose pas la distinction *attente* vs *dormance* pour
Superman. **Cas projeté** : Superman en attente prolongée (B1 ne
mandate pas pendant 2 cycles 12WY) est-il dormant ou actif ?

## Les règles B2 qui paraissent mal ajustées pour Superman

Deux règles du canon B2 méritent une remontée à B2 (sans
contournement par cette escouade) :

### Règle mal ajustée #1 — La vérifiabilité du veto Superman

Le catalogue des 8 vetos pose **3 propriétés** (catégoriel,
vérifiable, non-négociable). Le veto Superman canonique *« bloque
toute prise de parole publique qui promet un résultat que la
delivery ne tient pas »* **manque la vérifiabilité** — c'est un
critère de pratique, pas un artefact documentaire.

**Remontée** : le catalogue 8 vetos pourrait compléter la
propriété *vérifiable* par un énoncé de défaut pour chaque veto.
Pour Superman, le défaut serait *« la promesse n'a pas de date ou
d'horizon mesurable »* (cf. `veto-amplification-candidate.md`).
Cette amplification candidate n'est pas tranchée — c'est une
suggestion à B2 Council, pas une adoption.

### Règle mal ajustée #2 — Le RACI par rang sur les couplages hors matrice

`b2-pair-check-raci-by-rank.md` pose un RACI sur les 9 pair-checks
canoniques. Mais Superman a **2 couplages hors matrice** (Brand
transverse People, analytics stack Cyborg) qui ne sont pas dans
les 9 critères.

**Remontée** : le RACI par rang pourrait s'étendre aux couplages
non-canoniques — soit en les nommant (devenir 11 ou 12 critères),
soit en posant une **matrice d'extension** pour les couplages
projetés. Sans extension, les couplages Superman ↔ People Brand et
Superman � IT analytics restent hors arbitrage explicite.

## Synthèse — ce que cette escouade a livré

6 concepts OKF v0.2 dans `superman/`, structurés autour des 4
questions du brief :

1. **Périmètre exact** → `domain-perimeter.md` — 3 frontières
   floues (Sales, Brand, IT) qui attendent un arbitrage Council.
2. **Veto catalogue** → `veto-catalogue-concrete.md` — 5 cas
   concrets où il bloque légitimement, 3 cas où il serait abusif,
   identification de la difficulté d'opérationnalisation.
3. **JTBD émis/reçus** → `jtbd-emit-receive.md` — 6 B3 Guardians
   identifiés (vs 7 attendus), 3 signaux canoniques émis, 3 sources
   de paquets reçus (mandates B1, pair-checks amont, pair-checks
   aval B3).
4. **Couplages cross-domaines** → `pair-checks-dependencies.md` —
   3 pair-checks canoniques + 2 couplages hors matrice + 3
   dépendances non-évidentes.

Plus **2 concepts transverses** :

- `veto-amplification-candidate.md` — amplification candidate
  *« date ou horizon mesurable »* projetée triplet 58.
- `cooperation-mode-patterns.md` — distribution 40/40/20
  parallel/handoff/negotiation projetée.

## Liens

- [[domain-perimeter]]
- [[veto-catalogue-concrete]]
- [[jtbd-emit-receive]]
- [[pair-checks-dependencies]]
- [[veto-amplification-candidate]]
- [[cooperation-mode-patterns]]

## Note de confiance

**Reconstruit pour les cas, confirmé pour le mapping.** Le mapping
Superman = 01 Growth = Guardians est confirmé par 4 sources
canoniques (avengers-wheel, vetoes-catalogue, triplet 27,
fifty-three-b3-agent-roster). Le triplet 19 (People & Brand) est
**incohérent** et signalé comme héritage V1 non re-tranché. Les 6
cas de veto légitime, les 3 cas abusifs, la distribution 40/40/20,
l'amplification candidate, et les 5 questions sans réponse canonique
sont **projetés** à partir du corpus — ce ne sont pas des
affirmations mesurées.
