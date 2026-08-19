---
type: Concept
title: B1 mandate packet — la grammaire du paquet B1 vers B2
description: Format canonique d'un domain mandate emis par B1 : intent + contraintes + success signal (pas un plan). Logue dans 04_B2_HANDOFF_QUEUE.md. B2 traduit en Rock + DoD, puis en B3 JTBD. B1 tient le gabarit, B2 le remplit.
tags: [b1, b2, handoff, packet, mandat, grammaire, interface]
generated: { by: minimax-m3, at: 2026-08-19T01:35:00Z }
verified:
  - { by: process:lecture-fractal-b1b2b3, at: 2026-08-19T01:35:00Z }
  - { by: process:synthese-pulse-b1-tour-1, at: 2026-08-19T01:35:00Z }
sources:
  - id: fractal-arch
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md"
    title: L2 Business — The B1 / B2 / B3 Fractal Architecture
    last_modified: 2026-06-02
  - id: handover-abc
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/02 ABC OS & Child Care BOS/CERRIROS_HANDOVER.md"
    title: Handover ABC — B2 ownership domain mapping
    last_modified: 2026-05-21
okf_version: "0.2"
---

# B1 mandate packet — la grammaire du paquet B1 vers B2

> Priorite du tour 1. C'est le **contrat d'interface** entre l'etage direction et l'etage coordination.

## Le gabarit canonique

Tire verbatim du fractal : un domain mandate par B2 affecte contient trois champs. Pas quatre, pas cinq. Trois.

```yaml
b1_b2_mandate_id: B1-B2-MANDATE-YYYY-NN
issued_at: <ISO 8601>
issued_by: <jerry-area | summer-project>
cycle: <12WY courante>

intent: |
  <pourquoi ce mandat maintenant, dans le North Star, dans la wheel scannee>

contraintes:
  - <limite non negociable que B2 doit respecter>
  - <frontiere que B2 ne doit pas franchir>

success_signal: |
  <observation qui prouvera que le mandat a reussi>
  <delai ou cycle de mesure>
```

C'est tout. B1 **n'ecrit pas** le plan d'execution, le DoD, le JTBD. Ces trois champs-la sont le travail de B2.

## Pourquoi trois champs, pas un plan

La doctrine perpetuelle est claire : *« Areas never complete, Projects graduate »*. B1 est Jerry (Area, perpetuel) ou Summer (Project, date). Dans les deux cas, B1 fixe l'intention et la mesure du succes ; B2 choisit la route. La separation tient pour trois raisons :

1. **Le plan date.** Un plan ecrit au kickoff est deja faux trois semaines plus tard. L'intention reste vraie plus longtemps que le plan.
2. **B2 a l'expertise du gate.** B2 sait ce que son domaine peut promettre sans崩er. B1 ne sait pas — il n'a pas la pair-check matrix en tete au moment du mandat.
3. **Le retour remonte plus vite.** Si B1 ecrit le DoD, B2 ne peut pas le contester ; il l'applique. Si B1 ecrit le success signal, B2 remonte avec *« ce signal n'est pas atteignable, voici un substitut »*, et la conversation North Star se reengage.

## Le registre : 04_B2_HANDOFF_QUEUE.md

Chaque mandate emis est logue. Le registre est append-only (D4), daté, et jamais reecrit. Format d'entree :

```
- [YYYY-MM-DD] B1-B2-MANDATE-YYYY-NN → B2 <domaine> : <intent en une ligne>, success signal : <en une ligne>
```

Le registre est **la seule preuve** qu'un mandat B1 a ete emis. Sans log, il n'y a pas de mandat — il y a une discussion qui n'engage personne.

## Trois exemples calibres (depuis le corpus)

### Exemple 1 — Mandat Growth (T2, sprint)

```yaml
b1_b2_mandate_id: B1-B2-MANDATE-2026-19
issued_at: 2026-08-04T10:00:00Z
issued_by: summer-coach-os
cycle: 12WY-2026-Q3-Q4

intent: |
  Le pivot marche US (2026-07-15) demande une pression d'acquisition
  qualifiee sur le segment Coach premium B2B $7.5-25K ACV. Sans traction
  monetaire qualifiee avant fin 12WY, le pivot reste declare.

contraintes:
  - Pas de paid media non-mesure : chaque dollar doit porter une metrique
    de retour chiffree (doctrine Wonder Woman veto-depense).
  - Pas de claim public qui n'a pas passe Legal (Eternals review).

success_signal: |
  20 SQLs qualifies US segment premium B2B mesures sur 12WY,
  avec cout par SQL <= 1/4 du contrat moyen.
```

### Exemple 2 — Mandat Product (T1, refonte)

```yaml
b1_b2_mandate_id: B1-B2-MANDATE-2026-22
issued_at: 2026-08-15T09:00:00Z
issued_by: jerry-area
cycle: 12WY-2026-Q3-Q4

intent: |
  Coach OS tourne dans une societe Paperclip vivante (UUID
  1c6e1a3b-7cc0-49ec-8de4-a501e219f37c) plafonnee a 2-3 agents
  simultanes. Le chantier 1 (couche transversale + graphe ontologique)
  est pose comme premier chantier car sans lui les suivants sont aveugles.

contraintes:
  - Le moule est dans 02_Meta_Factory/, pas dans les fichiers engendres.
  - Le refactor n'invalide pas les profils agents deployes.

success_signal: |
  Chantier 1 livre et verifie en bout-en-bout par un agent externe
  au chantier ; aucun fichier engendre modifie a la main.
```

### Exemple 3 — Mandat Legal transverse (T3, conformite)

```yaml
b1_b2_mandate_id: B1-B2-MANDATE-2026-25
issued_at: 2026-08-18T14:00:00Z
issued_by: jerry-area
cycle: 12WY-2026-Q3-Q4

intent: |
  AI Bill of Rights + conformite 365 — avant toute mise en public
  US post-pivot, les claims et la privacy policy doivent passer
  une revue Legal Aquaman / squad Eternals.

contraintes:
  - Aucune mise en public sans `LEGAL_READY` d'Aquaman.
  - Toute decision Legal est loguee dans le registre B2 (Council output).

success_signal: |
  Zero `BLOCKED_RISK` Legal sur les livrables publiques du 12WY ;
  chaque `LEGAL_READY` cite dans le rapport de fin de cycle.
```

## Ce que B2 recoit et fait

A reception du mandat, B2 (le hero-manager du domaine affecte) :

1. **Convertit en Rock + DoD packet.** Format defini par `B2_DEFINITION_OF_DONE_SPEC.md` (cote B2, pas B1). B2 y ajoute le plan d'execution, les milestones, et la definition du DoD-Una (3 criteres minimum).
2. **Pousse au B2 Council** si le mandat touche plusieurs domaines. Le Council choisit le mode (parallel / handoff / negotiation).
3. **Dispatch en B3 JTBD packets.** Format defini par `B3_JOBS_TO_BE_DONE_SPEC.md` (cote B2).
4. **Remonte au B1** quand le success signal est observable, ou quand une contrainte ne peut pas etre tenue.

## Anti-pieges cote B1

- **Mandat trop long.** Si l'intent tient en trois lignes, c'est un mandat. Si l'intent tient en trois paragraphes, c'est un plan — c'est le travail de B2.
- **Contraintes qui sont des deliverables.** *« Le DoD est X »* est une contrainte de B2, pas une contrainte du mandat B1. La bonne forme : *« B2 doit me prouver X par un signal observable. »*
- **Success signal non-mesurable.** *« Le client doit etre satisfait »* est un voeu. La bonne forme : *« NPS ≥ 40 sur 30 reponses du segment cible, mesure fin de 12WY. »*

## Sources de l'interface

- `00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §« Le flux de commandement » — *« B1 ecrit un domain mandate par B2 affecte (intent + contraintes + success signal, pas un plan). Logue dans 04_B2_HANDOFF_QUEUE.md. »*
- `B2_Area_Domains/05_B2_DEFINITION_OF_DONE_SPEC.md` (reference, non lu dans cette passe) — la traduction B2.
- `B2_Area_Domains/06_B3_JOBS_TO_BE_DONE_SPEC.md` (reference, non lu dans cette passe) — la traduction B3.

## Liens

- [[b1-decision-rights-frontieres]] — la frontiere d'autorite de B1
- [[b1-wheel-imbalance-six-signes]] — ce qui declenche l'emission d'un mandat
- [[b1-stop-conditions-escalier]] — quand le mandat est revoque ou escalade
- [[b2-business-wheel-harmonization-matrix]] — la matrice que B2 applique enConseil

## Note de confiance

**Confirme par machine.** Le gabarit (intent + contraintes + success signal) est explicite dans le fractal, ligne par ligne. L'interdit *« pas un plan »* est la clause qui distingue ce gabarit d'un cahier des charges classique. La traduction B2→DoD et B2→JTBD est referencee mais non lue dans cette passe.