---
type: Concept
title: Superman Growth — couplages cross-domaines révélés par les pair-checks
description: Superman Growth est Accountable sur Legal→Growth et Finance→Growth (entrant), Responsible via B3 Guardians sur Growth→Sales (sortant). La matrice d'harmonisation teste 3 pair-checks qui touchent Superman. La question 4 du brief — qui dépend de Superman, de qui Superman dépend — révèle deux couplages que la matrice ne montre pas : Superman ↔ People (Brand transverse) et Superman � IT (analytics stack).
tags: [superman, growth, pair-check, harmonization, raci, couplage, dependance]
generated: { by: minimax-m3, at: 2026-08-19T04:03:00Z }
verified:
  - { by: process:lecture-corpus-superman, at: 2026-08-19T04:03:00Z }
sources:
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — 9 critères cross-domaines
    last_modified: 2026-08-19
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks — A = B2 en aval
    last_modified: 2026-08-19
  - id: vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2
    last_modified: 2026-08-19
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Superman Growth (01)
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Superman Growth — couplages cross-domaines révélés par les pair-checks

## Les trois pair-checks canoniques qui touchent Superman

La matrice d'harmonisation (`b2-harmonization-matrix-exploitable.md`)
teste **9 transitions** cross-domaines. Trois touchent Superman
explicitement :

| # | Transition | Direction | Superman = | Question matrice |
|---|---|---|---|---|
| 1 | Growth → Sales | sortant | Aval (output de Superman) | *« L'attention devient-elle opportunité qualifiée ? »* |
| 5 | Finance → Growth | entrant | Aval (reçoit de Wonder Woman) | *« La dépense est-elle justifiée par l'apprentissage ou la traction ? »* |
| 7 | Legal → Growth | entrant | Aval (reçoit de Aquaman) | *« Les claims sont-ils safe ? »* |

Lecture RACI par rang (`b2-pair-check-raci-by-rank.md`) :

| Pair-check | A (Accountable) | R (Responsible) | C (Consulted) | I (Informed) |
|---|---|---|---|---|
| Growth → Sales (#1) | **B2 Sales** (JohnJones) | **B3 Illuminati** | **B2 Growth (Superman)** | B1, B3 Guardians |
| Finance → Growth (#5) | **B2 Growth (Superman)** | **B3 Guardians** | B2 Finance (Wonder Woman) | B1, B3 Thunderbolts |
| Legal → Growth (#7) | **B2 Growth (Superman)** | **B3 Guardians** | B2 Legal (Aquaman) | B1, B3 Eternals |

**Lecture clé** : Superman est **Accountable** sur 2 pair-checks
(Finance → Growth, Legal → Growth), **Consulted** sur 1
(Growth → Sales). Superman **n'est jamais Responsible** — c'est
toujours un B3 (Illuminati pour Growth→Sales, Guardians pour les
deux entrants).

## Qui dépend de Superman — la sortie Growth → Sales

Le pair-check #1 (Growth → Sales) est la **transition la plus
scrutée** de la wheel. Trois raisons :

1. **C'est le passage de l'attention à l'opportunité.** Avant
   cette transition, tout le travail upstream (paid media, content,
   outbound) est **coût sans contrepartie**. Après, c'est
   **potentiel de revenu**.
2. **Le B2 Sales (JohnJones) porte l'arbitrage.** Superman est
   Consulted, pas Accountable. Si la transition casse, c'est
   JohnJones qui escalade B2 Council — pas Superman. Superman porte
   le **fait** (cf. triplet 56 Batman remonte des faits) sur
   l'attention produite, mais ne décide pas de l'arbitrage.
3. **Le red flag #2 (Growth green, Sales red)** est *« valider
   l'offre avant de scaler l'attention »*. Si Superman monte en
   capacité sans que JohnJones ne valide l'offre, la wheel
   s'effondre. **C'est Superman qui détecte ce red flag** — il
   doit refuser d'accélérer quand Sales est red.

Conséquence : Superman **dépend** d'un signal JohnJones stable
pour scaler. Si JohnJones est dormant ou en blocker, Superman doit
escalader — pasScaler l'attention.

## Qui Superman dépend — les deux entrants

### Finance → Growth (Wonder Woman → Superman)

Wonder Woman veto *« bloque toute dépense récurrente sans date de
revue ni métrique de retour »* (triplet 28). Avec l'amplification
triplet 58 *« chaque ligne doit porter une métrique de retour
chiffrée »*.

**Le couplage** : Superman ne peut pas scaler l'attention sans
dépense récurrente (paid media, content, automation). Wonder Woman
peut bloquer cette dépense si la métrique de retour manque. **Si
Wonder Woman bloque**, Superman ne peut pas exécuter son Rock
sans escalader B1 (parce que le veto est non-négociable au niveau
mésoperpétuel, cf. `b2-eight-domain-vetoes-catalogue.md` §3).

**Cas concret** : un mandat B1 *« pivoter US premium »* déclenche
une dépense paid media récurrente (Rocket_Auto). Wonder Woman
veto si la métrique de retour (MQL qualifies ICP US) n'est pas
chiffrée. Superman doit **négocier** la métrique avec Wonder Woman
avant de démarrer — mode handoff ou negotiation selon
`cooperation-mode-patterns.md`.

### Legal → Growth (Aquaman → Superman)

Aquaman veto *« bloque toute prestation démarrée sans accord écrit
sur le périmètre et la propriété du livrable »* (cf. catalogue 8
vetos). Pour Superman, **toute prise de parole publique** est une
prestation — case-study (Mantis_VoC), claim produit (Groot_Content),
manifeste (StarLord_Story). Aquaman peut bloquer si l'accord
manque.

**Le couplage** : Superman produit la parole publique, Aquaman
doit avoir validé le périmètre en amont. **Si Aquaman est dormant**
(cf. `b2-areas-dormants-doctrine.md`), Superman **ne peut pas
publier** — Aquaman peut être réveillé par signal Superman (le
premier mandat Growth qui demande une prise de parole).

**Cas concret** : un mandat B1 *« annoncer une intégration avec
partenaire Z »* déclenche Groot_Content. Aquaman dormant — la
dormance est levée par le signal Superman, Aquaman consigne le
réveil dans le journal Council et statue sur le périmètre de
l'accord. Mode handoff obligatoire (cf.
`cooperation-mode-patterns.md`).

## Les couplages **non canoniques** que la matrice ne montre pas

La question 4 du brief — *« sur quoi dépend-il d'un autre domaine,
et lequel dépend de lui ? »* — révèle deux couplages **hors
matrice** :

### Couplage Superman ↔ People (Brand transverse)

Le triplet v3 ligne 19 cite Superman en *« People & Brand »* (cf.
`domain-perimeter.md` §« Pourquoi ces frontières existent »).
Brand est un travail transverse qui, dans le canon V4, relève de
People (Green Lantern) — pas de Superman.

**Mais** : la squad Guardians inclut StarLord_Story (manifeste de
marque) et Groot_Content (content de marque). Superman **exécute
de fait** du travail Brand sans que People ne l'ait formellement
arbitré.

Conséquence : People **dépend** de Superman pour la production
Brand, mais Superman ne dépend pas de People pour la doctrine
Brand. C'est un couplage **asymétrique** — Superman peut
produire sans People, People ne peut pas produire sans Superman.

**Cas-limite** : si People mandate un livrable Brand via
StarLord_Story, le contrat B2 → B3 est signé par Superman (sponsor
B2) mais le DoD est fixé par People. Qui est Accountable ?
Probablement Superman (la production), avec People en Consulted.
**À trancher en Council** — pas de triplet canonique.

### Couplage Superman ↔ IT (Cyborg)

L'analytics stack (Mixpanel, Amplitude, PostHog) est une dépendance
IT (déployée, monitorée, sauvegardée par Cyborg) **et** un
livrable Growth (qui regarde les données, qui décide sur leur
base). Cf. `domain-perimeter.md` §« Frontière 3 ».

Conséquence : Superman **dépend** de Cyborg pour l'infra
analytics, mais Cyborg **ne dépend pas** de Superman pour la
doctrine analytics. C'est le même couplage asymétrique.

**Cas-limite** : un dashboard PostHog est déployé par Cyborg,
interprété par Superman. Si le dashboard crashe, c'est Cyborg qui
escalade (veto IT). Si le dashboard est mal interprété, c'est
Superman qui escalade (veto Growth).

## Les trois dépendances non-évidentes

Au-delà des 3 pair-checks canoniques, Superman a **3 dépendances
non-évidentes** que les captains oublient souvent :

1. **Sales (JohnJones) sur l'ICP** — Superman qualifie l'attention
   selon un ICP. Si JohnJones n'a pas validé l'ICP, Superman
   qualifie dans le vide.
2. **Finance (Wonder Woman) sur la runway** — Superman peut
   scaler l'attention tant que la runway le permet. Wonder Woman
   tient la runway. Si la runway baisse, Superman doit ralentir —
   même sans veto explicite.
3. **People (Green Lantern) sur la capacité squad** — Les 6 B3
   Guardians ont une charge. Si People (X-Men squad) ne tient pas
   la capacité, Superman ne peut pas scaler le dispatch B3.

Ces 3 dépendances ne sont pas des pair-checks matrice. Elles sont
**reconstruites** par lecture des triplets et du RACI par rang —
le canon ne les nomme pas.

## Anti-pièges

- **Superman comme simple émetteur d'attention.** Le pair-check
  #1 (Growth → Sales) montre que Superman est aussi **récepteur**
  de l'output Sales (qui est-ce qui qualifie, quel ICP).
- **Couplage asymétrique ignoré.** Le couplage Superman ↔ People
  (Brand) et Superman ↔ IT (analytics) n'est pas dans la matrice.
  Un arbitrage qui l'ignore rate la moitié du couplage.
- **Dépendance non-évidente comme implicite.** Les 3 dépendances
  non-évidentes (ICP, runway, capacité squad) doivent être
  **explicites** dans le packet mésoperpétuel, pas sous-entendues.
- **Veto Wonder Woman ou Aquaman sans cross-veto Superman.** Le
  veto porte sur la classe (dépense récurrente, accord écrit). Si
  Superman accepte un mandat qui déclenche la classe, il porte
  **aussi** le veto (cf. `veto-catalogue-concrete.md` §« Cas 4 »).

## Liens

- [[b2-harmonization-matrix-exploitable]] — les 9 critères
- [[b2-pair-check-raci-by-rank]] — la matrice RACI par rang
- [[b2-eight-domain-vetoes-catalogue]] — les vetos catalogue
- [[b2-areas-dormants-doctrine]] — quand Aquaman est dormant
- [[domain-perimeter]] — les 3 frontières floues
- [[veto-catalogue-concrete]] — cas concrets de veto
- [[cooperation-mode-patterns]] — modes de coopération

## Note de confiance

**Confirmé par machine pour les 3 pair-checks canoniques ;
reconstruit pour les couplages hors matrice.** Les 3 pair-checks
sont tirés verbatim de la matrice d'harmonisation + RACI par rang.
Les 2 couplages non canoniques (People Brand, IT analytics) sont
**projetés** à partir du triplet ligne 19 (Superman People &
Brand) et de la lecture pratique du substrat OMK (Groot_Content
fait du brand, dashboards sont IT). Les 3 dépendances
non-évidentes sont **reconstruites** par lecture critique du RACI
par rang et des triplets 28/41/56/57.
