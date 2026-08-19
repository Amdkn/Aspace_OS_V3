---
type: Concept
title: People — sept couplages invisibles avec les autres domaines
description: People (Green Lantern) est le domaine le plus transverse — il touche les sept autres domaines B2 par des couplages qui ne sont pas tous explicites dans la matrice d'harmonisation canonique. Trois couplages sont canoniques (charge People × Ops, ownership vacant × tous, succession × tous). Quatre couplages sont reconstruits depuis la pratique et le triplet v3 : People × IT (skills L0), People × Legal (double signature), People × Finance (charge comme coût récurrent), People × Growth (rotation vs continuité de la marque).
tags: [people, green-lantern, couplages, invisibles, transverse, b2, matrice]
generated: { by: minimax-m3, at: 2026-08-19T04:25:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:25:00Z }
sources:
  - id: harmonization-canonique
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: "Harmonisation — pair-check #9 People → Tous (canonique)"
    last_modified: 2026-08-17
  - id: avengers-wheel-coordinateur
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: "Eight Domain Avengers Wheel — coordinateur transverse People"
    last_modified: 2026-08-17
  - id: triplet-37-55-forge
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplets 37 + 55 — Green Lantern ↔ Bill L0.2 Forge"
    last_modified: 2026-08-17
  - id: veto-aquaman
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: "B2 catalogue — veto Aquaman Legal × veto Green Lantern People (double clef)"
    last_modified: 2026-08-19
  - id: veto-wonder-woman
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: "B2 catalogue — veto Wonder Woman Finance sur dépense récurrente"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# People — sept couplages invisibles avec les autres domaines

## Le principe : pourquoi People est *le plus* transverse

D'après `eight-domain-avengers-wheel.md` §« Le coordinateur transverse —
People » : *« pour qu'une motion B3 passe à l'Ops launch readiness,
People doit avoir émis `ASSIGNED` / `NEEDS_OWNER` / `DLQ`. »*

C'est la **même règle** que pour IT (`SYSTEM_READY` /
`NEEDS_SYSTEM_OWNER` / `QUARANTINE`) et Legal (`LEGAL_READY` /
`NEEDS_REVIEW` / `BLOCKED_RISK`) — sauf que People est **le seul** des
trois à toucher **les sept autres domaines** simultanément par
construction. IT et Legal ont des périmètres plus contenus.

Conséquence : la matrice d'harmonisation canonique (9 pair-checks) ne
couvre pas tous les couplages People. **Quatre couplages sont
invisibles** dans le canon — ils se révèlent dans la pratique, ou sont
reconstitués depuis le triplet v3.

## Les trois couplages canoniques

### 1. People × Ops (Batman) — charge de livraison

**Source canonique.** Red flag matrice #3 : *« Sales green / Ops+People
red — risque de charge de livraison »*. Pair-check #2 *Sales → Ops* et
pair-check #9 *People → Tous* se croisent ici.

**Mécanisme.** Ops tient la livraison, People tient la carte de charge
des owners Ops. Si Ops est `READY` mais que People émet `NEEDS_OWNER`
sur un owner Ops critique, Ops ne peut pas tenir la cadence de livraison.

**Effet visible.** Le red flag matrice déclenche le B2 Council. People
est C, Batman Ops est A. People remonte la carte de charge, Batman
arbitre.

### 2. People × Tous — ownership vacant

**Source canonique.** Pair-check #9 *People → Tous* : *« la propriété et
la charge sont-elles tenables ? »*

**Mécanisme.** Tout owner qui part (fin de mandat, démission, rotation)
laisse un poste vacant. People signale `NEEDS_OWNER`, le domaine
d'accueil (Batman Ops, Flash Product, etc.) statue.

**Effet visible.** Trois issues : (a) recrutement lancé par People,
(b) `DLQ` si pas d'owner possible, (c) re-scope du mandat par le
domaine d'accueil (réduction de périmètre).

### 3. People × Tous — succession

**Source canonique.** Implicite dans le pair-check #9 — la rotation est
un cas particulier de ownership vacant.

**Mécanisme.** Quand un owner quitte, People doit **préparer la
succession** (cartographie des candidats internes, lancement du
recrutement externe, transition de connaissance). Le captain du domaine
d'accueil arbitre le choix final.

**Effet visible.** Le délai de succession est un **lag indicator** People
qui n'est pas posé dans le canon V4. À poser.

## Les quatre couplages invisibles

### 4. People × IT (Cyborg) — skills L0 et TechRecruiting

**Source.** Triplets 37 et 55 — Green Lantern sollicite Bill (L0.2
Forge) pour les injections de skills. Triplet 34 — Beast tient le
TechRecruiting.

**Mécanisme.** Quand People mandate un agent technique, deux questions se
croisent :

- *« les skills L0 sont-ils disponibles ? »* — People ↔ Bill Forge.
- *« l'agent peut-il tourner dans le système IT ? »* — People ↔ IT Cyborg.

La matrice canonique pose Product × IT (pair-check #4), mais **pas**
People × IT. Le couplage est **invisible**.

**Effet visible.** Un recrutement agent qui passe le mandat People peut
être bloqué par IT (système non-prêt) ou par Forge (skill L0 manquant).
Le Council doit traiter le blocage comme un **arbitrage à trois** :
People + IT + Forge.

### 5. People × Legal (Aquaman) — double clef People + Legal

**Source.** Veto Aquaman : *« engagement démarré sans accord écrit sur
le périmètre et la propriété du livrable »*. Veto People : *«
recrutement sans mandat écrit + critère de sortie »*. Les deux vetos
portent sur la **même signature**.

**Mécanisme.** Pour démarrer une prestation, il faut :

1. People mandate le recrutement (rôle + horizon + critère de sortie).
2. Legal acte l'accord de prestation (périmètre + propriété +
   résiliation).

Sans les deux, pas de démarrage. La matrice canonique pose Legal ×
Growth (pair-check #7) et Legal × Product (pair-check #8), mais **pas**
Legal × People. Le couplage est **invisible**.

**Effet visible.** Un recrutement qui passe People mais pas Legal est
**bloqué**. Inversement, un accord Legal sans mandat People n'a pas de
**sujet** (qui est recruté ?). Le Council doit exiger la double clef.

### 6. People × Finance (Wonder Woman) — charge comme coût récurrent

**Source.** Veto Wonder Woman : *« dépense récurrente sans date de
revue et sans métrique de retour »*. Le People mandate des owners qui
**coûtent** (salaires, mandats agents facturés). La charge People est un
**coût récurrent** au sens Finance.

**Mécanisme.** Wonder Woman peut opposer son veto sur un recrutement
**récurrent** (CDI, agent permanent) sans date de revue ni métrique de
ROI. Inversement, People peut signaler qu'un owner est sous-employé,
ce qui justifie la dépense.

La matrice canonique pose Finance × Growth (pair-check #5) et Finance ×
Product (pair-check #6), mais **pas** Finance × People. Le couplage est
**invisible**.

**Effet visible.** Un recrutement qui passe People mais qui n'a pas de
date de revue Finance peut être bloqué par Wonder Woman. Le Council
doit traiter le conflit comme un arbitrage croisé.

### 7. People × Growth (Superman) — rotation vs continuité de la marque

**Source.** Coach OS cite *« People & Brand »* comme intitulé local du
domaine People, et *« Superman (People & Brand) »* comme intitulé local
de Growth. Cette **double casquette** People × Brand n'est pas dans le
canon V4 — c'est une lecture Coach OS.

**Mécanisme.** Quand un owner People quitte (rotation), la **continuité
de la marque** (voix, ton, position) est en jeu. Superman Growth tient
le brand, People tient les owners qui portent le brand. Les deux
peuvent se contredire : People dit *« on remplace »*, Superman dit *«
on perd la voix »*.

**Effet visible.** Une rotation d'un owner *porte-parole* peut être
**arbitrée par Superman** (maintien de la marque) ou par **People**
(disponibilité de l'owner). Le Council tranche — pas de règle par
défaut.

## Le cas asymétrique : People × tous vs Legal × Growth/Product

Legal Aquaman a **deux** pair-checks canoniques (Legal × Growth,
Legal × Product). People n'en a **qu'un** (People × Tous), mais ce pair-
check **englobe les sept autres domaines** par construction. La matrice
canonique **sous-représente People** par rapport à son rôle effectif.

C'est une **observation** sur la matrice, pas une critique : la matrice
traite les transitions **binaires** (A → B). People → Tous est une
**famille** de transitions, pas une transition unique. La matrice ne
peut pas la granulariser davantage sans perdre sa lisibilité.

**Conséquence pour le Council** : un arbitrage People doit **toujours**
préciser **quel sous-domaine** est impacté (People × Ops, People × IT,
etc.). Sans cette précision, le pair-check #9 est ambigu.

## Anti-pièges

- **Couplage ignoré puis découvert tard** — un arbitrage qui révèle un
  couplage People × X non posé dans le packet mésoperpétuel est un
  signal que le scan initial a été incomplet. Le Council doit **retourner
  au scan**, pas trancher avec une information manquante.
- **Couplage People × IT traité comme People × Legal** — les deux
  couplages ont des veto et des mécanismes différents. Le premier passe
  par Forge (skills L0), le second par la double clef. Confondre les
  deux = invoquer le mauvais veto.
- **Couplage People × Finance négligé** — Wonder Woman peut bloquer un
  recrutement récurrent sans date de revue. People doit intégrer cette
  grille **avant** de lancer le recrutement, pas après.
- **Couplage People × Growth utilisé comme veto de marque** — la
  rotation d'un owner *porte-parole* n'est pas un cas de veto People.
  C'est un arbitrage Council. People peut signaler, Superman peut
  arbitrer, mais aucun des deux n'a de veto sur l'autre.

## Liens

- [[green-lantern-people-perimetre-frontieres]] — les trois frontières
  qui cristallisent ces couplages
- [[green-lantern-people-raci-transverse-jamais-A]] — pourquoi People
  est C, pas A, sur ces arbitrages
- [[green-lantern-people-veto-recrutement-sans-mandat]] — le veto qui
  double celui d'Aquaman
- [[b2-harmonization-matrix-exploitable]] — la matrice qui ignore certains
  de ces couplages
- [[b2-eight-domain-vetoes-catalogue]] — les veto Aquaman et Wonder
  Woman qui couplent People

## Note de confiance

**Reconstruit, à moitié étayé.** Les trois couplages canoniques sont
tirés verbatim de la matrice d'harmonisation canonique. Les quatre
couplages invisibles sont **reconstruits** à partir des triplets 34,
37, 55 (People × IT), du couple veto Aquaman × veto People (People ×
Legal), du veto Wonder Woman sur dépense récurrente (People × Finance),
et de l'intitulé Coach OS *« People & Brand »* (People × Growth). Aucun
de ces quatre couplages n'est nommé dans la matrice canonique. Le cas
asymétrique *People × Tous* vs *Legal × Growth/Product* est une
**observation directe** sur la matrice, pas une projection.