# RAPPORT — escouade de domaine Cyborg (IT)

**Tour** : 1
**Date** : 2026-08-19
**Périmètre IT** : identifié par lecture du canon (triplet 21, Avengers
Wheel, triplet 29 veto), confirmé par 6 concepts OKF posés.

---

## Ce que j'ai produit

6 concepts OKF v0.2 dans
`70_Onthologies/pulse/domaines/cyborg/` :

1. `cyborg-domain-it-perimetre-frontieres.md` — **Q1**. Surface
   canonique (runtime, accès, déploiement, backup, technical
   boundaries), squad Kang Dynasty 6 agents, 3 frontières poreuses
   (Batman, Flash, Wonder Woman), divergence numérotation Coach OS
   7 vs canonique 5.
2. `cyborg-veto-cloud-only-sortie.md` — **Q2**. Triple motif
   (souveraineté, réversibilité, coût caché), renforcements
   ADR-OMK-004 + ADR-L2-AAAS-001, 3 cas de déclenchement légitime,
   4 cas d'abus, amplification candidate (date de revue + métrique
   réversibilité).
3. `cyborg-jtbd-emit-receive-kang-dynasty.md` — **Q3**. Pipeline
   5 étapes Rock→DoD→JTBD, autonomy contract B3, 6 formes
   canoniques de dispatch, 6 archétypes de paquets émis
   (3 pérennes + 3 épisodiques), 3 failure modes hérités du
   contrat B2→B3.
4. `cyborg-couplages-l0-rick-river-song-pyramide.md` — **Q4** (le
   plus utile). Triplet 38 (River Song médiation), pyramide SDD-006
   §1.1:59 (L0≥L1>L2), Sobriété Rick kernel/infra, A0 HITL,
   absorption IT présumée à L0 Rick (W40 §M1+M2).
5. `cyborg-pair-checks-product-it-fantastic-four.md` — RACI #4
   (Cyborg A, Kang Dynasty R), chaîne Product→IT→Ops, dépendance
   Batman sur Cyborg, 3 exceptions qui retournent A à B1.
6. `cyborg-doctrine-5-principes-dispatch.md` — P2 Decompose-or-die,
   P3 TDD, P11+P13 Sovereignty, P14+P17 IaC, P18 Observability.
   5 gates qui changent le dispatch, anti-patterns #1-3 cités
   verbatim (SSH manuel prod, deploy sans CI/CD, DNS sans propagation
   check).

**Append ETAT_DOMAINES.md** : section `## Cyborg (IT)` ajoutée à
la fin du fichier, une seule ligne.

---

## Ce que j'ai lu

### Sources canoniques lues

- `50_Distillation/projets/eight-domain-avengers-wheel.md`
  (mapping 8 domaines B2/B3, IT = 05)
- `50_Distillation/areas/business-wheel-harmonization-matrix.md`
  (5 red flags, dont #1 *Product green, Ops/IT red*)
- `70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md`
  (veto Cyborg verbatim)
- `50_Distillation/projets/fifty-three-b3-agent-roster.md`
  (squad Kang Dynasty ~7, W40 patch hint)
- `70_Onthologies/triplets/v3-business.jsonl` (62 triplets, dont
  triplet 21 Cyborg/Kang, 28/29 cloud-only veto, 38 River Song,
  39 pyramide L0/L1/L2, 56/57 Batman remonte-fait)
- 6 règles B2 : `b2-council-arbitrage-rule.md`,
  `b2-harmonization-matrix-exploitable.md`,
  `b2-pair-check-raci-by-rank.md`,
  `b2-b3-jtbd-handoff-contract.md`,
  `b2-meso-decision-packet-spec.md`,
  et relecture de `b2-council-arbitrage-rule.md` (confirmée)
- `70_Onthologies/pulse/ETAT.md` (rendez-vous B1/B2/B3)
- `70_Onthologies/pulse/domaines/ETAT_DOMAINES.md` (rendez-vous 8
  escouades — lu 2 fois pour cause de modifications concurrentes)

### Sources OMK IT lues

- `V2/.../01-omk-business-os/B2_Business_Domains/05_IT_Cyborg_KangDynasty/00_B2_DOMAIN_CONTROL_ROOM.md`
- `.../02_B3_SWARM_SUPERVISION_PROTOCOL.md`
- `.../01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md`
- `V2/.../B3_Warp_Core_Execution/05_IT_Cyborg_KangDynasty/01_B3_AGENT_ROSTER.md`
- `V2/.../06_Claude_Code_Bare/agents/b2-06-cyborg-it.md`
- `V2/.../06_Claude_Code_Bare/mindsets/B2_Cyborg_IT_Dispatch.md`

### Sources SDD citées (sans lecture intégrale)

- SDD-004 (Rick's Verse Governance) — cité triplet 38 §7.2 pour
  River Song.
- SDD-006 (Business Pulse L2 Pyramide) — cité triplet 39 §1.1:59.
- SDD-006 vs SDD-006_DEAL collision documentée par
  `concept-sdd-006-collision.md` (lu).
- ADR-OMK-004 + ADR-L2-AAAS-001 — cités verbatim par
  `b2-06-cyborg-it.md`, mais **contenu non lu** (chemin non
  trouvé dans cette vague).

### Sources format et conventions lues

- `pulse/domaines/batman/batman-doctrine-remonte-fait-non-decision.md`
  (frontmatter OKF v0.2, structure « triplets qui ancrent /
  reconstruction / anti-pièges / liens / note de confiance »)
- `pulse/domaines/batman/batman-couplage-ops-it.md` (couplage
  cross-domaine)
- `pulse/domaines/aquaman/aquaman-veto-engagement-sans-perimetre.md`
  (veto — calqué pour Cyborg)

### Sources **non lues** (manque)

- Les 18 principes IT complets
  (`02_Areas_Spock/.../03_CYBORG_IT_PRINCIPLES.md`) — j'ai lu
  la sélection de 5 dans `B2_Cyborg_IT_Dispatch.md`, pas la liste
  intégrale.
- Les 7 autres packets JTBD-001 Areas (B3 a signalé « 7 packets
  non lus »).
- Le W40 V4 patches original — j'ai lu la **présomption** qu'il
  absorbe IT à L0 Rick dans `fifty-three-b3-agent-roster.md`, pas
  le SDD original.
- ADR-OMK-004 + ADR-L2-AAAS-001 (corps, pas seulement citation).
- Les profils individuels `L2_A3_KangPrime.md` etc. — seul le
  roster a été lu.
- Ownerbook T1 OMK (cité mais non lu intégralement).

---

## Ce que je n'ai pas couvert

- **Sprint hebdo concret de Cyborg** — aucun corpus ne donne un
  SPRINTS.md effectif pour le domaine IT. Les 6 archétypes de
  paquets sont **projetés** depuis le dispatch doctrine, pas
  observés en cycle.
- **Cas réel de veto cloud-only opposé** — 0 packet mésoperpétuel
  IT enregistré dans la vague 2 (convergence avec Batman, Aquaman,
  Wonder Woman, Superman, Flash, Green Lantern, John Jones — tous
  rapportent 0 packet mésoperpétuel).
- **W40 patches originaux** — la mutation IT → L0 Rick est
  présumée mais non vérifiée. **Remontée B1.**
- **Couplage People × IT transverse** — Green Lantern cite
  *« couplages invisibles People×IT »* dans son rapport. J'ai posé
  que Cyborg est C sur #9, mais l'intersection People × IT sur la
  charge Kang Dynasty (6 agents × tenure × spécialité) reste à
  creuser.
- **Couplage Aquaman × Cyborg** — Aquaman cite
  *« couplages invisibles Legal × IT »* (chemin de sortie
  contractuel = clause de réversibilité). J'ai noté que Cyborg
  alerte parfois Aquaman sur les clauses (#7 #8), mais je n'ai
  pas posé un concept dédié.

---

## Niveau de confiance

- **Confirmé par machine** : surface canonique (runtime, accès,
  déploiement, backup), squad Kang Dynasty 6 agents, pipeline
  5 étapes Rock→DoD→JTBD, autonomy contract, veto cloud-only
  verbatim, triplet 38 River Song, triplet 39 pyramide L0/L1/L2,
  RACI #4 Cyborg A. ~12 affirmations confirmées par ≥2 sources.
- **Reconstruit** : 3 frontières poreuses (Batman/Flash/Wonder
  Woman), triple motif du veto (souveraineté/réversibilité/coût
  caché), chaîne Product→IT→Ops, 3 cas de déclenchement légitime,
  4 cas d'abus, distinction OMK infra pure vs Coach OS
  code/architecture. ~15 affirmations reconstruites à partir
  d'indices canoniques, étiquetées « mon raisonnement » dans les
  concepts.
- **Présumé** : absorption IT à L0 Rick (W40 §M1+M2), ADR-OMK-004
  et ADR-L2-AAAS-001 (contenu), amplification candidate Cyborg
  *« date de revue + métrique de réversibilité »*. **3 remontées
  vers B1.**

---

# CE QUE LE CORPUS NE DIT PAS SUR Cyborg (le plus important)

## 1. L'absorption W40 §M1+M2 IT → L0 Rick est une présomption, pas un fait

Le concept OKF `fifty-three-b3-agent-roster.md` (2026-08-17) note
*« W40 §M1+M2 patches — l'IT infra absorbé à L0 Rick (Cyborg
devient R&D External Discovery) »*. Cette affirmation est
**répétée** dans le triplet 21 (Cyborg pairedWith Kang Dynasty,
*« R&D & IT »*) mais **non étayée** par :

- Aucun SDD ou triplet qui définit ce qu'est *« R&D External
  Discovery »* dans le périmètre Cyborg.
- Aucune décision Council explicite qui acte l'absorption.
- Aucun sprint ou JTBD qui démontre que Cyborg n'opère plus
  l'IT infra aujourd'hui.

**Conséquence opérationnelle** : je ne sais pas, en lisant le
corpus, si l'IT infra est encore sous Cyborg ou déjà sous L0
Rick. Le concept `cyborg-domain-it-perimetre-frontieres.md`
assume que Cyborg tient **les deux** (IT + R&D). Si Summers a déjà
absorbé l'IT à L0 Rick, le périmètre IT de Cyborg est **vide** —
ce qui serait une découverte majeure, pas un détail.

**Remontée B1** : trancher canoniquement l'absorption W40, et
mettre à jour le triplet 21 en conséquence. **Statut : bloqué
en attente.**

## 2. La divergence OMK � Coach OS sur le périmètre Kang Dynasty

Deux lectures coexistent sans arbitrage :

- **OMK (B3_Warp_Core_Execution/05_IT_Cyborg_KangDynasty/01_B3_AGENT_ROSTER.md)** :
  Kang Dynasty = **infra pure** (VPS, Dokploy, Hostinger DNS,
  Supabase, backup, CI/CD).
- **Coach OS (triplet 21 + triplet dispatch doctrine)** :
  Kang Dynasty = **code/architecture** (architecture prime,
  greenfield, legacy migration, capacity planning,
  documentation, refactor/review).

Les deux ne sont pas mutuellement exclusives — un même agent peut
tenir les deux — mais **l'effectif et la spécialisation** sont
différents. Le triplet 21 compte 6 agents (KangPrime, IronLad,
ScarletCenturion, Immortus, VictorTimely, RamaTut). Le roster
OMK compte 6 charges différentes (Kang Prime lead infra, Iron Lad
provisioning, Scarlet Centurion sécurité réseau, Immortus
capacity, Victor Timely CI/CD, Rama-Tut backup).

**Convergence partielle** : Kang Prime = architecture (les deux
côtés), Iron Lad = greenfield/provisioning (les deux côtés), Rama-Tut
= backup/review (les deux côtés). **Divergence** : Scarlet
Centurion = alt-stack (Coach OS) vs sécurité réseau (OMK).
Immortus = legacy code (Coach OS) vs capacity planning (OMK).

**Statut : non arbitré.** Si l'arbitrage existe, il n'est pas
dans le corpus lu.

## 3. La chaîne de causalité triplet 38 → River Song → L0 n'est pas expliquée

Le triplet 38 pose *« Cyborg dépend de River Song (SDD-004 §7.2),
médiation agentique imposée »*. Je n'ai pas lu SDD-004 §7.2 — je
cite la section mais je n'ai pas vérifié ce qu'elle dit. La nature
exacte de la médiation n'est pas claire :

- River Song est-il un agent L0 stable, ou un canal de
  routage ?
- Que se passe-t-il si River Song refuse une demande Cyborg ?
- Cyborg escalade-t-il à Beth (L1) ou à Summers (B1) ?
- La médiation est-elle symétrique (Cyborg → L0 uniquement) ou
  aussi descendante (L0 → Cyborg) ?

Ces quatre questions sont **ouvertes**. La pyramide L0≥L1>L2
(triplet 39) suggère que L1 (Beth) tranche, mais le canal n'est
pas explicité.

**Remontée B1** : faire lire SDD-004 §7.2 en cycle.

## 4. La distinction Green Lantern → Bill → River Song vs Cyborg → River Song n'est pas expliquée

Triplet 37 (Green Lantern → Bill L0.2 Forge → River Song Inject)
vs triplet 38 (Cyborg → River Song directement). Pourquoi cette
différence ? **Hypothèse non vérifiée** : Green Lantern est People,
sa médiation passe par Bill (skills/process), Cyborg est IT, sa
médiation passe directement par River Song (infra). Mais cette
hypothèse n'est pas canonique.

**Conséquence** : si un canal est légitime et l'autre pas, c'est
un arbitrage Council. Si les deux sont légitimes mais pour des
raisons non explicitées, c'est un manque doctrinal.

## 5. Le coût IT récurrent et le triplet 58

Triplet 58 (cité par Wonder Woman) étend la doctrine veto-dépense
de Wonder Woman *« avec ROI à 30 jours »*. Le rapport Wonder Woman
a posé une amplification candidate symétrique chez Cyborg (date
de revue + métrique de réversibilité). Mais ce parallèle **n'a
pas été soumis au Council**. Si 5/8 capitaines l'adoptent, c'est
une règle ; sinon, c'est une coïncidence.

**Statut : amplification candidate non tranchée.**

## 6. ADR-OMK-004 + ADR-L2-AAAS-001 — cités mais non lus

Les deux ADR sont sister à `b2-06-cyborg-it.md` et
`B2_Cyborg_IT_Dispatch.md`. **Je n'ai pas lu leur contenu.** Si
leur contenu précise les cas de souveraineté, les seuils de
réversibilité, ou les exceptions, mes concepts Cyborg sont
**incomplets** sur ces dimensions.

**Remontée B1** : localiser et lire ces deux ADR en cycle.

---

# REGLES B2 QUI ME PARAISSENT MAL AJUSTEES POUR Cyborg

## 1. Le RACI par rang met Cyborg A sur un seul pair-check (#4 Product→IT)

La matrice 9 pair-checks place Cyborg **A** uniquement sur #4. Mais
Cyborg est **Impliqué** (en dépendance ou en C) sur au moins 6
pair-checks : #2 Sales→Ops, #3 Product→Ops (dépendance), #4
Product→IT (A), #5 Finance→Growth (C indirect), #7 Legal→Growth
(C indirect), #8 Legal→Product (C indirect), #9 People→Tous (C
transversal).

C'est **plus que Batman A sur 2 pair-checks (#2 #3)**. Cyborg est
le **deuxième capitaine le plus couplé** de la wheel, après
Wonder Woman (3 pair-checks) et Batman (2 pair-checks). La règle
RACI minimise Cyborg en le déclarant A sur un seul — alors qu'il
tient le **système** dont la matrice entière dépend.

**Suggestion** : assumer Cyborg **A transverse léger** sur les
pair-checks qui touchent un système IT (par parallélisme avec
Wonder Woman A transverse léger sur les pair-checks qui touchent
la dépense récurrente). Sans décision Council, c'est une
**observation**, pas une proposition formelle.

## 2. Le veto catalogue ne capture pas la Sobriété Rick kernel/infra

Le triplet 29 dit *« Cyborg bloque tout fournisseur cloud-only
sans chemin de sortie documenté »*. Mais la doctrine de dispatch
ajoute deux gates **non-veto** :

- **Sobriété Rick** sur kernel/infra (A1, pas B2).
- **A0 HITL** sur cron (B1, pas B2).

Ces deux gates sont **plus contraignants** que le veto catalogue
pour certaines décisions IT. Mais le veto est **la règle
canonique** — une Sobriété Rick qui s'oppose n'a pas de mécanisme
de pair-check RACI. C'est une asymétrie : Cyborg peut bloquer par
veto, mais ne peut pas bloquer par Sobriété (Rick tranche seul).

**Conséquence** : un Cyborg qui veut **bloquer** un dispatch
kernel/infra peut invoquer le veto (si cloud-only sans sortie) ou
**escalader** à Rick Sobriété. Mais Rick Sobriété n'est pas un
mécanisme Council — c'est un fait remonté à Summers.

**Suggestion** : étendre le catalogue pour inclure une
**catégorie Sobriété** (Rick pour kernel/infra, A0 pour cron) qui
donne au Cyborg un droit de **pair-Consulted obligatoire** sur ces
mêmes décisions. C'est une **remontée vers B2** (catégoriel +
vérifiable + non-négociable = trois propriétés du veto), pas une
décision d'escouade.

## 3. Le format packet mésoperpétuel ne prévoit pas de motif de dépendance L0

Un packet mésoperpétuel standard (cf. `b2-meso-decision-packet-spec.md`)
a 7 champs : `meso_decision_id`, `source_mandate`, `mode`,
`impacted_domains`, `tradeoff`, `decision`, `proof_expected`,
`next_review`. **Aucun** champ ne mentionne *« River Song
médiation »*, *« L0 dépendance »*, *« Sobriété Rick ack »*.

C'est un trou. Cyborg qui escalade un blocker L0 persistant
devrait pouvoir documenter la cause dans un champ `l0_dependency`
ou `mediation_actor`. Sinon, le packet Council ne voit qu'un veto
IT sans voir la **cause structurelle**.

**Suggestion** : étendre le format packet avec deux champs
optionnels (catégoriel : tout domaine peut les utiliser, pas
seulement IT) — `mediation_actor` et `l0_dependency_ref`. À
soumettre au Council B2 (tour suivant).

## 4. Le triplet 39 (pyramide L0≥L1>L2) n'a pas de mécanisme d'arbitrage B2 → L0

La pyramide pose L2 (Cyborg et Kang Dynasty) sous L1 (Beth veto)
sous L0 (autorité absolue). Mais **aucun mécanisme B2** ne
formalise la remontée d'un blocker L0 vers B1 (Summers). Le
triplet 56/57 de Batman (remonte-fait) est un précédent — mais
il n'est pas étendu à L0.

**Suggestion** : poser que toute dépendance L0 bloquée >24h ouvrées
donne lieu à un packet mésoperpétuel avec un champ
`l0_blocker_acknowledged`. Summers tranche si B1 (et pas le
Council B2) peut amender la pyramide. C'est un précédent à créer.

---

# CONCLUSION

J'ai produit **6 concepts OKF** sur Cyborg/IT, couvrant les 4
questions du brief (périmètre, veto, JTBD émis/reçus, dépendances)
et ajoutant deux concepts annexes (pair-checks RACI, doctrine 5
principes de dispatch). Tous citent des sources réelles ; aucun
n'invente un triplet ou un SDD.

**3 remontées vers B1** :

1. Absorption W40 §M1+M2 IT → L0 Rick — **présumée non vérifiée**.
2. ADR-OMK-004 + ADR-L2-AAAS-001 — **cités non lus**.
3. SDD-004 §7.2 (médiation River Song) — **cité non lu**.

**4 remontées vers B2 (Council)** :

1. RACI Cyborg transverse léger sur les pair-checks système.
2. Catégorie Sobriété Rick kernel/infra dans le catalogue veto.
3. Champs optionnels `mediation_actor` et `l0_dependency_ref` dans
   le packet mésoperpétuel.
4. Mécanisme d'arbitrage B2 → L0 sur blocker persistant >24h
   ouvrées.

**0 packet mésoperpétuel IT** enregistré en corpus vague 2
(convergence avec Batman, Aquaman, Wonder Woman, Superman, Flash,
Green Lantern, John Jones). La wheel 8-domain est **posée** mais
**non encore exercée**.

---

*Standing : 6 concepts posés, 1 ligne ETAT ajoutée, 3+4
remontées vers B1 et B2, 0 cycle réel.*
