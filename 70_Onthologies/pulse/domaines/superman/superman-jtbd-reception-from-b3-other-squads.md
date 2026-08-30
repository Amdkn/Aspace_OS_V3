---
type: Concept
title: Superman Growth — paquets JTBD reçus des 7 autres B3 squads (pas Guardians)
description: jtbd-emit-receive.md (vague 1) couvre Superman émetteur vers B3 Guardians (6 agents) et Superman récepteur de B1/B2 amont (mandates, pair-checks Legal×Growth + Finance×Growth). Ce concept ferme le vide canonique : Superman reçoit aussi des 7 autres B3 squads (Illuminati, Avengers, Fantastic Four, Thunderbolts, Kang Dynasty, Eternals, X-Men) — chaque squad émet un signal amont qui touche Growth. 7 réceptions B3 typées, 4 sources d'alerte (scope drift, claim drift, capacity drift, ICP drift), 3 asymétries structurelles (squads verticaux vs Superman horizontal).
tags: [superman, growth, jtbd-reception, b3, cross-squad, illuminati, avengers, fantastic4, signal-amont]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-5, at: 2026-08-19T12:00:00Z }
sources:
  - id: jtbd-emit-receive
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/jtbd-emit-receive.md"
    title: Superman Growth — paquets JTBD émis vers B3 Guardians et reçus de B1/B2 amont
    last_modified: 2026-08-19
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — 8 squads B3 Marvel
    last_modified: 2026-08-17
  - id: fifty-three-roster
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: 53 B3 Agent Roster — 8 squads
    last_modified: 2026-08-17
  - id: b2-pair-check-raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — réception B3 vers B2 sponsor
    last_modified: 2026-08-19
  - id: pair-checks-dependencies
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/pair-checks-dependencies.md"
    title: Superman — pair-checks canoniques + couplages hors matrice
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Superman Growth — paquets JTBD reçus des 7 autres B3 squads

## Le vide canonique comblé

`jtbd-emit-receive.md` (vague 1) pose Superman Growth :

- **Émetteur** vers B3 Guardians (6 agents — StarLord/Rocket/Gamora/Drax/Groot/Mantis, plus 7ᵉ candidat Peter_Quill ou Nebula).
- **Récepteur** de B1 (mandates) et B2 amont (Legal × Growth Aquaman, Finance × Growth Wonder Woman).

Ce concept complète le **récepteur B3** — Superman reçoit aussi des **7 autres squads B3** Marvel, pas seulement des B3 Guardians. C'est un vide canonique signalé par `pair-checks-dependencies.md` (vague 1) §« Les 3 couplages hors matrice » mais non documenté en réception.

## Pourquoi Superman reçoit des B3 pairs

Trois raisons structurelles :

### 1. Le triplet 13 (B3 dependsOn B2-sprint) crée une boucle de dépendance

`b2-b3-jtbd-handoff-contract.md` §« triplet 13 » pose *« B3 dependsOn B2-sprint »*. La dépendance va de B3 vers B2 — mais elle est **bilatérale** en pratique : B3 signale au B2 sponsor, qui redistribue aux B3 pairs impactés.

Superman est B2 sponsor des B3 Guardians, mais aussi **B2 aval** sur les pair-checks #5 (Finance → Growth) et #7 (Legal → Growth) où il est Accountable. Il redistribue donc des informations amont vers les B3 pairs impactés.

### 2. Les 9 pair-checks canoniques ont chacun un B3 Responsible

`b2-pair-check-raci-by-rank.md` pose **R = B3** sur chaque pair-check. Pour les 4 pair-checks impliquant Growth (cf. §« Pair-checks Superman » ci-dessous), il y a **4 squads B3 Responsible** qui émettent vers Superman via leur captain B2 amont ou aval.

### 3. Le signal cross-squad est un anti-pattern scope creep

Sans réception B3 structurée, Superman découvre les dérives cross-squad **après** que le B3 pair ait déjà bougé. C'est un **scope creep silencieux** (cf. `b2-b3-jtbd-handoff-contract.md` §« Scope creep »). La réception structurée permet à Superman de **détecter en amont** les dérives qui toucheront Growth.

## Pair-checks impliquant Growth — 4 transitions

Croisement de `pair-checks-dependencies.md` (vague 1) et `b2-pair-check-raci-by-rank.md` :

| # | Pair-check | B2 aval (A) | B2 amont (C) | B3 Responsible | B3 Consulted |
|---|---|---|---|---|---|
| 1 | Growth × Sales | Sales (JohnJones) | Growth (Superman) | Illuminati | Guardians |
| 5 | Finance × Growth | Growth (Superman) | Finance (Wonder Woman) | Guardians | Thunderbolts |
| 7 | Legal × Growth | Growth (Superman) | Legal (Aquaman) | Guardians | Eternals |
| V5 #11 | People × Growth (Brand) | Growth (Superman) | People (Green Lantern) | Guardians | X-Men (Brand) |
| V5 #12 | IT × Growth (Analytics) | Growth (Superman) | IT (Cyborg) | Guardians | Kang Dynasty |

**Note V5** : les pair-checks #11 et #12 sont proposés dans `superman-pair-check-v5-brand-and-analytics.md` (vague 3) mais non canoniques (unanimité 8/8+B1 non obtenue). Ils sont listés ici comme **candidats Council-ready**, pas comme réceptions effectives.

## Les 7 réceptions B3 typées — une par squad

### Réception 1 — B3 Illuminati (Sales) — signal SQL qualifié

**Source** : `fifty-three-b3-agent-roster.md` ligne 43 — squad Illuminati, ~7 agents (MrFantastic, ProfessorX, IronMan, DoctorStrange, BlackBolt, Namor, +1).

**Signal émis** : *« X SQL qualifiés ICP Y sur la semaine, avec Y fermés / Z en pipeline / W en attente »*.

**Mode** : signal **quotidien** via scrums.md du squad lead Illuminati (Captain lead non nommé, candidat ProfessorX ou MrFantastic — cf. `superman-domain-perimeter.md` frontière #1).

**Ce que Superman en fait** : ajuste les **claims publics** (veto Superman catalogue) pour ne pas promettre plus que ce que Sales ferme. Si SQL < 5/sem et que Superman claim "50 SQL/sem", c'est un **veto bloquant** (cas-type 1 US premium post-mortem delivery).

**Type d'alerte** : **capacity drift** — Sales ne suit pas la cadence attendue par Growth.

### Réception 2 — B3 Avengers (Product) — signal scope change

**Source** : squad Avengers, ~7 agents (Captain America, IronMan, Thor, Hulk, BlackWidow, Hawkeye, ScarletWitch).

**Signal émis** : *« scope feature F ajoutée/retirée/reformulée sur le cycle »*.

**Mode** : signal **hebdomadaire** via Captain America scrums.md (mandat spécifié vague 3 `flash-captain-america-roster-fiche-canon.md`).

**Ce que Superman en fait** : ajuste les **claims publics** (veto Superman) parce qu'un scope change (ex : feature promise non livrée) déclenche un veto bloquant. Si Captain America annonce scope retreat J+5, Superman doit retirer les claims sur cette feature avant J+7.

**Type d'alerte** : **scope drift** — Product ne livre pas ce qui est claimé.

### Réception 3 — B3 Fantastic Four (Ops) — signal delivery capacity

**Source** : squad Fantastic Four, ~4 agents (MrFantastic, InvisibleWoman, TheThing, HumanTorch — Batman Ops B3 canonique).

**Signal émis** : *« charge de livraison actuelle / backlog / incidents ouverts »*.

**Mode** : signal **hebdomadaire** via MrFantastic scrums.md (mandat pas explicitement spécifié, symétrique Captain America Flash).

**Ce que Superman en fait** : ajuste les **promesses de scaling** (claims volume) parce qu'une charge Ops saturée déclenche le **red flag #3** (Sales green, Ops/People red — la promesse ne pourra pas être tenue, cf. `b2-harmonization-matrix-exploitable.md` §« 5 red flags »). Si Ops charge > 80% et que Superman claim "scale to 10k accounts", Batman doit bloquer.

**Type d'alerte** : **capacity drift** — Ops ne suit pas la cadence promise par Growth.

### Réception 4 — B3 Thunderbolts (Finance) — signal ROI réalisé

**Source** : squad Thunderbolts, ~7 agents (Bucky/Yelena/RedGuardian/Ghost/Taskmaster/USAgent + 1, cf. Wonder Woman tour 2 — divergences squad canon non-arbitré).

**Signal émis** : *« ROI 30j sur la dépense récurrente Growth »* (cf. triplet 58 extension Wonder Woman).

**Mode** : signal **mensuel** via squad lead Thunderbolts scrums.md (squad lead pas nommé — candidat Bucky ou Yelena).

**Ce que Superman en fait** : ajuste le **budget paid media** (Rocket_Auto) pour maximiser le ROI. Si ROI < cible triplet 58 (typiquement 3x), Wonder Woman étend le veto-dépense, Superman doit **geler le scaling**.

**Type d'alerte** : **ROI drift** — la dépense récurrente n'atteint pas la métrique de retour.

### Réception 5 — B3 Kang Dynasty (IT) — signal analytics stack

**Source** : squad Kang Dynasty, 6 agents (cf. `cyborg-kang-dynasty-effectif-canon-recompte.md` — recompte V3 0 fichier b3-*kang* sur disque au 2026-08-19, recommandation Issue A 7ᵉ agent).

**Signal émis** : *« stack analytics disponibilité / incidents / schema drift »* (Mixpanel, Amplitude, PostHog, GA4).

**Mode** : signal **temps réel** via monitoring IT (cf. Cyborg pair-check #4 Product → IT).

**Ce que Superman en fait** : ajuste la **mesure de DoD** — si l'analytics stack est en panne, le compteur MQL/reach/trafic n'est pas mesurable. C'est un **trigger DoD caduque** (le DoD est verrouillé, l'instrument de mesure est cassé). Superman escalade B2 Council pour ré-arbitrage.

**Type d'alerte** : **measurement drift** — l'instrument de mesure du DoD n'est pas fiable.

### Réception 6 — B3 Eternals (Legal) — signal claims boundary

**Source** : squad Eternals, ~7 agents (Ajak, Sersi, Thena, Ikaris, Kingo, Sprite, Druig — Aquaman Legal B3 canonique).

**Signal émis** : *« périmètre claims autorisés / interdits / conditions »*.

**Mode** : signal **par cas** (chaque claim public Growth passe par Aquaman revue), pas un signal périodique.

**Ce que Superman en fait** : applique le **veto Superman préventif** (mode reformulation amont, cf. `superman-dod-cas-type-2-awareness-prelaunch-verrouille.md` §« Levier 3 ») sur les claims qui touchent une boundary Aquaman (régulation, propriété intellectuelle, claims commerciaux).

**Type d'alerte** : **claim drift** — un claim Superman déborde du périmètre Aquaman autorisé.

### Réception 7 — B3 X-Men (People) — signal brand voice + ICP

**Source** : squad X-Men, 8 agents (ProfessorX, Cyclops, Wolverine, Storm, JeanGrey, Nightcrawler, Rogue, Gambit — recompte canon vague 4 `xmen-effectif-canon-recompte-disk.md`).

**Signal émis** : *« brand voice updates / ICP shifts / capacity People assignée à Growth »*.

**Mode** : signal **mensuel** ou **par cas** (chaque campagne majeure Growth co-signée People, cf. cas-type 2 awareness prelaunch).

**Ce que Superman en fait** : applique la **co-signature People×Growth** sur les campagnes brand voice (pair-check #11 Brand V5 candidat). Si People refuse la co-signature, Superman doit amender les claims.

**Type d'alerte** : **ICP drift** — le segment ICP Y défini par Growth ne correspond plus au segment validé par People.

## Les 4 sources d'alerte cross-squad

| Alerte | Type | Squad émettrice | Veto Superman déclencheur |
|---|---|---|---|
| **scope drift** | feature promise non livrée | B3 Avengers (Flash) | Veto bloquant post-delivery |
| **claim drift** | claim hors périmètre Aquaman | B3 Eternals (Aquaman) | Veto préventif reformulation amont |
| **capacity drift** | Ops/Sales/People surchargés | B3 Fantastic Four / Illuminati / X-Men | Red flag #2 / #3 matrice |
| **ICP drift** | segment ICP Growth ≠ segment People | B3 X-Men | Co-signature People refusée |

## Les 3 asymétries structurelles

### Asymétrie 1 — Squads verticaux vs Superman horizontal

Les 7 autres B3 squads sont **verticales** à leur capitaine B2 — Illuminati sous JohnJones, Avengers sous Flash, etc. Superman est **horizontal** parce qu'il est Accountable sur les pair-checks #5 et #7 (Finance → Growth, Legal → Growth) et Consulted sur #1 (Growth × Sales). Superman reçoit donc des **6 squads verticales** (toutes sauf Guardians) en plus d'être capitaine de la 7ᵉ (Guardians).

C'est une **asymétrie de rang** — Superman est à la fois B2 sponsor (vertical Guardians) et B2 coordinateur cross-squad (horizontal). Les B3 pairs traitent Superman comme un capitaine standard, pas comme un coordinateur. **Risque** : Superman absorbe trop de signaux sans mandat explicite de coordination.

### Asymétrie 2 — Squads B3 sans contrat bilatéral Superman

Le contrat B2 → B3 canonique (`b2-b3-jtbd-handoff-contract.md`) est bilatéral entre B2 sponsor et B3 squad lead. Superman signe le contrat avec les B3 Guardians (6 agents). **Il n'a pas de contrat bilatéral avec les B3 Illuminati/Avengers/FF/Thunderbolts/Kang/Eternals/X-Men** — il est Accountable sur leur transition, pas sponsor.

**Conséquence** : Superman reçoit des signaux de squads B3 sans avoir signé de contrat. C'est un **trou contractuel** — Superman est en position de réception sans engagement formel. **Remontée vers B2** : la matrice RACI par rang ne pose pas de contrat bilatéral entre B2 Accountable et B3 Responsible quand ils ne sont pas dans la même chaîne verticale.

### Asymétrie 3 — Squad lead pas nommé

`superman-peter-quill-7th-agent-mandate-spec.md` (vague 4) signale que le **squad lead Guardians** n'est pas nommé dans le substrat OMK. C'est un **trou canonique persistant** vague 1-2-3-4-5.

**Mais** les autres squads B3 ont aussi un squad lead manquant ou non-arbitré :

- B3 Illuminati : squad lead candidat ProfessorX/MrFantastic/DoctorStrange (3 hypothèses).
- B3 Avengers : Captain America mandat spécifié (vague 3 Flash) mais fiche roster non lue.
- B3 Fantastic Four : MrFantastic mandat implicite.
- B3 Thunderbolts : squad lead candidat Bucky/Yelena (Wonder Woman tour 2).
- B3 Kang Dynasty : squad lead pas nommé (Cyborg vague 1-4).
- B3 Eternals : squad lead pas nommé (Aquaman tour 1-4).
- B3 X-Men : ProfessorX vs Beast nomination en suspens (Green Lantern tour 4).

**7 trous de squad lead** sur 8 squads. Superman est le **capitaine qui mandate le sien** (Peter_Quill spec vague 4) mais les 6 autres squads qu'il réceptionne ont aussi le **même trou**. **Asymétrie de maturité** : Superman est en avance sur ses propres récepteurs.

## Anti-pièges

- **S'auto-coordonner sans mandat B1.** Refusé — Superman absorbe les signaux B3 pairs mais ne peut pas initier une coordination cross-squad sans mandat B1 explicite. Sinon il bascule en B2 coordinateur transversal, ce qui n'est pas son rôle canonique (People Green Lantern est le coordinateur transverse, cf. `eight-domain-avengers-wheel.md` §« Le coordinateur transverse — People »).
- **Ignorer les signaux B3 pairs.** Refusé — sans réception structurée, Superman découvre les dérives après que le dommage est fait. La réception est un **acte de vigilance**, pas de coordination.
- **Signer un contrat bilatéral avec un B3 pair sans mandat B2 sponsor.** Refusé — Superman est Accountable sur la transition, pas sponsor. Seul le B2 sponsor signe. Superman reçoit en mode `Consulted`, pas `Accountable`.
- **Confondre réception et arbitrage.** Refusé — Superman arbitre les **pair-checks #5 et #7** où il est Accountable. Sur les autres pair-checks (#1, V5 #11, V5 #12), il est Consulted et ne peut pas arbitrer seul.
- **Escalader B2 Council sur chaque signal.** Refusé — Superman escalade si le signal déclenche un veto catalogue ou un red flag matrice. Sinon il consigne en scrums.md et poursuit.

## Liens

- [[superman-jtbd-emit-receive]] — émetteur B3 Guardians + récepteur B1/B2 amont
- [[superman-pair-checks-dependencies]] — 3 pair-checks canoniques + 2 hors matrice
- [[superman-pair-check-v5-brand-and-analytics]] — V5 #11 Brand + #12 Analytics
- [[superman-dod-cas-type-1-us-premium-verrouille]] — scope drift Avengers
- [[superman-dod-cas-type-2-awareness-prelaunch-verrouille]] — claim drift Eternals
- [[superman-domain-perimeter]] — asymétrie Superman horizontal vs B3 vertical
- [[b2-pair-check-raci-by-rank]] — Superman A/C sur 4 pair-checks
- [[b2-b3-jtbd-handoff-contract]] — contrat bilatéral B2 sponsor + B3 lead
- [[b2-harmonization-matrix-exploitable]] — red flags #2 et #3 déclenchés par capacity drift

## Note de confiance

**Reconstruit — vide canonique comblé par projection.** Les 7 réceptions B3 typées sont **projetées** à partir des pair-checks canoniques (`b2-pair-check-raci-by-rank.md`), du triplet 13 (B3 dependsOn B2-sprint), et du contrat B2 → B3 (`b2-b3-jtbd-handoff-contract.md`). Les 4 sources d'alerte (scope/claim/capacity/ICP drift) sont **extrapolées** depuis les failure modes canoniques (scope creep, silent rework, escalation tardive) + les red flags matrice. Les 3 asymétries sont **reconstruites** depuis la position RACI de Superman (Accountable sur #5/#7, Consulted sur #1) + le trou squad lead persistant vagues 1-4. **Confiance moyenne** sur la structure des 7 réceptions, *basse* sur la capacité B3 pairs à émettre ces signaux en l'absence de squad lead nommé (les 7 squads ont le même trou que Superman).
