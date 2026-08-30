---
type: Concept
title: Flash pacte de coordination inter-escouades — dépendances externes formalisées avec deadlines et escalade
description: Formalisation des 4 dépendances externes Flash identifiées en vagué 2-5 (Batman pour vérification sister canon Captain America/MrFantastic concept 27 tour 5, Aquaman pour clause sunset contractuelle Scarlet Witch concept 28 tour 5, Captain America pour livraison brief J+0 programme T-30j concept 26 tour 5, Council pour agenda séance hebdomadaire packet agrégé concept 29 tour 5) en un **pacte de coordination** explicite. 4 capsulaires × 5 colonnes (capitaine, livrable attendu, deadline, statut au 2026-08-19, mécanisme escalade) + 3 mécanismes de désenclavement (escalade B1, founder rotation, vacation owner) + 1 gabarit YAML `pacte_coordination_flash` Council-ready + 3 cas Council-ready A1/A2/A3.
tags: [flash, product, coordination, inter-escouades, dependances, batman, aquaman, captain-america, council, escalade-deadline]
generated: { by: minimax-m3, at: 2026-08-19T13:30:00Z }
verified:
  - { by: process:synthese-escouade-flash-tour-6, at: 2026-08-19T13:30:00Z }
sources:
  - id: flash-sister-canon-captain-america-mrfantastic-verification-protocol
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-sister-canon-captain-america-mrfantastic-verification-protocol.md"
    title: "Sister canon Captain America/MrFantastic concept 27 tour 5 — dépendance Batman"
    last_modified: 2026-08-19
  - id: flash-scarlet-witch-4d-test-coherence-validation
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-scarlet-witch-4d-test-coherence-validation.md"
    title: "Scarlet Witch Issue A amendée concept 28 tour 5 — dépendance Aquaman"
    last_modified: 2026-08-19
  - id: flash-j0-brief-captain-america-t30j-content
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-j0-brief-captain-america-t30j-content.md"
    title: "Brief J+0 Captain America concept 26 tour 5 — dépendance Captain America"
    last_modified: 2026-08-19
  - id: flash-aggregated-pair-check-dod-packet-unique-seance
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-aggregated-pair-check-dod-packet-unique-seance.md"
    title: "Packet agrégé concept 29 tour 5 — dépendance Council agenda"
    last_modified: 2026-08-19
  - id: b2-pair-check-raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: "RACI par rang — A = B2 en aval"
    last_modified: 2026-08-19
  - id: b2-council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: "B2 Council arbitrage — escalade B1 si 3 exceptions"
    last_modified: 2026-08-19
  - id: b2-veto-amplification-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: "Amplification vetos — procédure 5/8 + D4"
    last_modified: 2026-08-19
  - id: b1-stop-conditions-escalier
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-stop-conditions-escalier.md"
    title: "B1 stop conditions + escalier canonique 5 échelons"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Flash pacte de coordination inter-escouades

## Le problème que ce pacte ferme

Le rapport tour 5 (`RAPPORT_dom-flash.md` §5.5 recommandation 4 + 5 vague 5) liste **4 dépendances externes Flash** qui bloquent l'activation de doctrines saisissables :

| # | Dépendance | Concept source | Statut au 2026-08-19 |
|---|---|---|---|
| 1 | **Batman Ops** — lecture fiche MrFantastic pour vérification sister canon Captain America/MrFantastic | concept 27 tour 5 | non coordonné |
| 2 | **Aquaman Legal** — clause sunset contractuelle Scarlet Witch H90 | concept 28 tour 5 | non coordonné |
| 3 | **Captain America** (squad lead Avengers) — livraison brief J+0 programme T-30j | concept 26 tour 5 | brief saisissable, livraison dépend |
| 4 | **Council** — agenda séance hebdomadaire pour packet agrégé | concept 29 tour 5 | séance à convoquer |

Ces 4 dépendances ont en commun :
- **Aucun mécanisme d'escalade** défini si le capitaine externe refuse ou tarde.
- **Aucune deadline chiffrée** — les concepts disent « saisissable », pas « attendu avant T+X ».
- **Aucun tracking** — les 7 autres escouades (Aquaman, Batman, etc.) ont leur propre charge, le brief J+0 Captain America peut être oublié.

Sans pacte, ces 4 dépendances **dormantes** transforment les doctrines Flash saisissables en projections théoriques. Le pacte de coordination **ferme cette asymétrie** en formalisant 4 capsulaires × 5 colonnes.

## Le tableau 4 × 5 — capsulaires de dépendance

| # | Capitaine externe | Livrable attendu | Deadline | Statut au 2026-08-19 | Mécanisme escalade |
|---|---|---|---|---|---|
| 1 | **Batman** (B2 Ops) | Fiche MrFantastic lue + gabarit `verification_sister_canon` rempli | 2026-09-15 (T+27j) | non démarré | Batman pair-check #3 captain sponsor sister squad (concept 27) — escalade B1 si 30j sans réponse |
| 2 | **Aquaman** (B2 Legal) | Clause sunset ≤ 2026-12-31 dans contrat Scarlet Witch H90 | 2026-09-30 (T+42j) | non démarré | Aquaman pair-check #8 Legal → Product A (cf. RACI par rang) — escalade Council si 14j sans réponse |
| 3 | **Captain America** (B3 squad lead Avengers) | Brief J+0 livré aux 7 agents Avengers dans section `scrums.md` | 2026-08-25 (T+6j) | brief saisissable, livraison dépend | triplet 41 (B3 interdit combler trou) — Captain America signale à Flash au plus tard 5j avant deadline |
| 4 | **Council** (B2) | Séance hebdomadaire convoquée avec packet agrégé B2-MESO-DECISION-2026-42-aggregated à l'agenda | 2026-09-01 (T+13j) | non démarré | chair saisissant (cf. `b2-council-cadence-and-chair.md`) — escalade B1 si 2 séances sans agenda |

**Lecture du tableau** : chaque livrable a une **deadline**, un **statut**, et un **mécanisme d'escalade** distinct. Le pattern est cohérent avec `b2-pair-check-raci-by-rank.md` §« Le RACI par rang » — A = B2 en aval, ici Flash est Consulted ou Accountable selon la transition.

## Le gabarit YAML — pacte de coordination Flash

```yaml
pacte_id: B2-PEER-2026-13  # pacte coordination Flash
generated_by: B2 captains Flash + Batman + Aquaman + Captain America
mode: parallel  # 4 capsulaires indépendantes
tradeoff: "Formalisation 4 dépendances externes Flash (Batman / Aquaman /
  Captain America / Council) en pacte de coordination explicite. 4 capsulaires
  × 5 colonnes (capitaine / livrable / deadline / statut / escalade).
  Le coût : 1 séance de cadrage + 4 relances. Le gain : 4 dépendances
  dormantes transformées en 4 livrables tracés, avec escalade B1 possible
  si 2 deadlines manquent."
decision: accepted
capsules:
  - id: C1
    capitaine_externe: Batman
    livrable: fiche_mrfantastic_lue + gabarit_verification_sister_canon_rempli
    deadline: 2026-09-15
    statut_2026_08_19: non_demarre
    escalade: batman_pair_check_3_captain_sponsor_sister_squad
    seuil_temps: 30j
  - id: C2
    capitaine_externe: Aquaman
    livrable: clause_sunset_2026_12_31_dans_contrat_scarlet_witch_h90
    deadline: 2026-09-30
    statut_2026_08_19: non_demarre
    escalade: aquaman_pair_check_8_a_legal_to_product
    seuil_temps: 14j
  - id: C3
    capitaine_externe: Captain_America
    livrable: brief_j0_livre_7_agents_avengers_section_scrums_md
    deadline: 2026-08-25
    statut_2026_08_19: brief_saisissable_livraison_depend
    escalade: triplet_41_b3_interdit_combler_trou
    seuil_temps: 5j
  - id: C4
    capitaine_externe: Council
    livrable: seance_hebdomadaire_agenda_packet_agrege_2026_42
    deadline: 2026-09-01
    statut_2026_08_19: non_demarre
    escalade: chair_saisissant_b2_council_cadence_and_chair
    seuil_temps: 2_seances_sans_agenda
proof_expected:
  - B2 gate coordination update (4_capsules_suivies_hebdomadaire)
  - B3 proof path (capsule_C3_brief_j0_livre_avant_2026_08_25)
  - B3 proof path (capsule_C1_verification_sister_canon_remplie_2026_09_15)
next_review: 2026-09-30
```

## Les 3 mécanismes de désenclavement

Quand une capsule est bloquée (refus, retard, silence), **3 mécanismes** permettent de désenclaver sans escalade destructrice :

### M1 — Escalade B1 si 2 deadlines manquent

Si **2 capsules** sur 4 dépassent leur deadline sans livrable, Flash demande **escalade B1** via un packet mésoperpétuel `decision: escalate_to_B1`. B1 arbitre en Summers sur la base du tradeoff : *« 4 dépendances Flash dans 4 domaines distincts — confirmer que les mécanos actuels tiennent, ou réallouer. »*

**Coût** : 1 packet mésoperpétuel, 1 séance Council, 1 escalade B1 (rare).
**Bénéfice** : débloque 4 capsules en 1 cycle.

### M2 — Founder rotation (capitaine suppléant)

Si un capitaine externe refuse explicitement (ex. Batman refuse de lire la fiche MrFantastic), Flash demande **founder rotation** : un autre B2 captain (par ordre alphabétique du domaine) prend la capsule. Batman refusé → Superman Growth prend la capsule C1.

**Coût** : 1 renegociation Council, 1 nouveau calendrier.
**Bénéfice** : la capsule avance, pas de blocage durable.

### M3 — Vacation owner (capsule en vacance)

Si une capsule est **dormante** (le capitaine externe ne répond pas et n'est pas explicitement en refus), elle passe en **vacance owner** : un capitaine B2 volontaire (différent du capitaine externe) prend la capsule par défaut. La vacance est consignée D4 append-only.

**Coût** : 1 captain volontaire, traçabilité D4.
**Bénéfice** : la capsule ne bloque pas le packet mésoperpétuel agrégé.

## Les 3 cas A1/A2/A3 Council-ready

| Cas | Adoption | Conséquence |
|---|---|---|
| **A1** — 4 capsules tenues dans les délais | calendrier respecté | Pacte tenu, doctrines Flash activées |
| **A2** — 2 capsules tenues, 2 manquées | escalade B1 mécanisme M1 | 1 packet mésoperpétuel escalade, founder rotation M2 sur les manquées |
| **A3** — 1 capsule tenue, 3 manquées | escalade B1 + vacation owner M3 sur 2 | Pacte partiellement actif, doctrines en partie saisissables |

**Cas A2 partiel** : 2 capsules manquées → M1 activé, B1 arbitre. Le tradeoff Council est alors : *« faut-il maintenir le pacte, ou remanier les 4 capsulaires en 2 cycles séparés ? »*

**Cas A3 critique** : 3 capsules manquées → 1 seule doctrine Flash s'active (celle qui dépend de la capsule tenue). Le pacte devient **Shotgun** (1 capsule tient, 3 ratent) — recommendable seulement si la capsule tenante est critique (ex. Council agenda, qui ouvre les 3 autres).

## Anti-pièges identifiés

1. **Confondre pacte et contrat B2 → B3**. Le pacte de coordination **n'est pas** un contrat B2 → B3 (cf. `b2-b3-jtbd-handoff-contract.md` §« Le contrat bilatéral »). Le pacte est **horizontal** (Flash ↔ capitaine externe), pas vertical (B2 sponsor ↔ B3 squad lead). La signature conjointe est différente.
2. **Pacte saisi sans consultation des capitaines externes**. Si Flash saisit le pacte **seul**, les 4 capitaines externes peuvent le refuser en séance. Le pacte doit être **pré-consulté** par Captain America (relais Avengers) avant saisine Council.
3. **Mécanisme M1 systématique**. Si Flash escalade B1 à la **première** deadline manquée, l'escalade devient **disproportionnée**. Le seuil de 2 capsules manquées protège contre l'overreach.
4. **M2 founder rotation sur Batman Superman Aquaman**. Les 3 B2 captains Batman/Superman/Aquaman sont **capitaines pivots** (cf. `b2-council-arbitrage-rule.md`). La founder rotation doit éviter de les remplacer par défaut — préférer M3 vacation owner pour ces 3-là.
5. **Ignorer la deadline Captain America (C3)**. 6 jours est très court. Si brief J+0 n'est pas livré avant 2026-08-25, le programme T-30j (concept 23 vague 4) ne démarre pas, et l'amplification veto Flash (concept 5 tour 3) reste saisissable.

## Liens

- [[flash-sister-canon-captain-america-mrfantastic-verification-protocol]] — concept 27 tour 5 source C1
- [[flash-scarlet-witch-4d-test-coherence-validation]] — concept 28 tour 5 source C2
- [[flash-j0-brief-captain-america-t30j-content]] — concept 26 tour 5 source C3
- [[flash-aggregated-pair-check-dod-packet-unique-seance]] — concept 29 tour 5 source C4
- [[flash-packet-format-extended-consolide-4-champs]] — concept 31 tour 6 saisie dépendante C4
- [[flash-veto-amplification-observation-protocole-T-30j]] — concept 23 vague 4 dépendance C3
- [[b2-pair-check-raci-by-rank]] — RACI par rang, base des mécanismes d'escalade
- [[b2-council-arbitrage-rule]] — escalade B1 si 3 exceptions, base mécanisme M1
- [[b2-veto-amplification-cycle]] — procédure 5/8 + D4, base adoption pacte
- [[b1-stop-conditions-escalier]] — escalier canonique 5 échelons, base mécanisme M1

## Note de confiance

**Confirmé par machine, saisissable mais pas Council-adopté.** Les 4 dépendances externes sont tirées verbatim des concepts sources (27, 28, 26, 29). Le tableau 4 × 5 est **projeté** par symétrie avec `b2-pair-check-raci-by-rank.md` (5 colonnes : capitaine externe, livrable, deadline, statut, escalade). Les 3 mécanismes M1/M2/M3 sont **projetés** depuis la doctrine d'escalade canonique (escalade B1 = M1, founder rotation = extension RACI par rang, vacation owner = extension doctrine dormance `b2-areas-dormants-doctrine.md`). Les 3 cas A1/A2/A3 sont **projetés** par symétrie avec la matrice d'amplification. Les deadlines 2026-08-25 / 2026-09-01 / 2026-09-15 / 2026-09-30 sont **arbitraires par construction** — Captain America dépendant du calendrier T-30j (concept 23 vague 4), Aquaman aligné sur Issue A T-30j (Aquaman effectif Eternals). À vérifier en cycle : (1) Batman accepte de lire la fiche MrFantastic, (2) Aquaman accepte la clause sunset contractuelle, (3) Captain America livre avant 6j, (4) Council convoque une séance avant 13j.
