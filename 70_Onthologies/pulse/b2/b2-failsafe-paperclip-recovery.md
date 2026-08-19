---
type: Concept
title: Fail-safe Paperclip — la récupération d'un B3 failed-run vers le B2 sponsor
description: Le triplet 53 dit « un 'failed' sur un agent Paperclip ne veut pas dire 'rien produit' — vérifier le fichier avant de relancer, sous peine d'écraser du travail valide ». Transposé au rang B2↔B3 : quand un B3 squad lead remonte un failed-run au B2 captain sponsor, le sponsor ne relance pas — il vérifie le livrable produit avant toute décision. La procédure distingue quatre états (vide / partiel / complet-non-vérifié / complet-vérifié) et quatre issues (relance / acceptation partielle / acceptation totale / escalade B2 Council).
tags: [b2, b3, fail-safe, paperclip, failed-run, recovery, sponsor, verification]
generated: { by: minimax-m3, at: 2026-08-19T03:40:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-3, at: 2026-08-19T03:40:00Z }
sources:
  - id: triplet-paperclip-failed
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 53 — paperclip failed-run = vérifier fichier avant relance"
    last_modified: 2026-08-17
  - id: triplet-paperclip-plafond
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 52 — Paperclip-Coach-OS plafonne à 2-3 agents claude_local simultanés"
    last_modified: 2026-08-17
  - id: triplet-b3-interdit-trou
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 41 — B3 interdit-combler-trou"
    last_modified: 2026-08-17
  - id: triplet-batman-fait
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 56 — Batman remonte à Summers des faits, pas des décisions"
    last_modified: 2026-08-17
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — quand une décision mésoperpétuelle devient un JTBD packet
    last_modified: 2026-08-19
  - id: b2-council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: examen-prealable
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/autonomie-agents/examen-prealable.md"
    title: L'examen préalable — une commande unique qui prouve avant de rendre
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Fail-safe Paperclip — la récupération d'un B3 failed-run vers le B2 sponsor

## Le signal canonique

Le triplet 53 dit verbatim :

> *« Un 'failed' sur un agent Paperclip ne veut pas dire 'rien produit'
> — vérifier le fichier avant de relancer, sous peine d'écraser du
> travail valide. »*

Le triplet 52 contextualise :

> *« Paperclip-Coach-OS plafonne à 2-3 agents claude_local simultanés :
> sept VP réveillés simultanément ont épuisé la table des process le
> 2026-08-02 (fork: Resource temporarily unavailable). »*

Les deux triplets ensemble posent une doctrine de **récupération après
échec d'infrastructure** : un agent qui sort en `failed` n'est pas un
agent qui n'a rien produit. Le relancer sans vérifier écrase le
travail valide déjà sur disque.

## La transposition au rang B2 ↔ B3

`b2-b3-jtbd-handoff-contract.md` pose le contrat bilatéral B2 → B3
avec trois failure modes (scope creep, silent rework, escalade
tardive). Le triplet 53 parle d'un **quatrième cas** : le B3 squad
lead remonte un failed-run au B2 captain sponsor. La cause n'est pas
un défaut de discipline B3 (scope creep, silent rework) — c'est un
**défaut d'infrastructure** (plafond Paperclip, fork épuisé, OOM,
timeout réseau, etc.).

Le triplet 41 dit *« B3 a l'interdit de combler lui-même un trou du
sprint — il le signale à son VP au lieu de laisser le défaut
invisible »*. Le failed-run est un trou d'un genre particulier : le
B3 a peut-être produit quelque chose, mais ne sait pas si c'est
complet. Le signal doit remonter au B2 sponsor **sans tentative de
relance locale**.

## La procédure de récupération

Quatre étapes, dans l'ordre. Le B2 sponsor ne décide rien avant
l'étape 2.

### Étape 1 — Constat

Le B3 squad lead remonte au B2 captain sponsor un packet
`failed-run` avec :

- `jtbd_packet_id` (le packet mésoperpétuel source)
- `squad` (la squad Marvel concernée)
- `horodatage` (date + heure de l'échec)
- `journal_erreur` (les 5-10 dernières lignes de la sortie d'erreur)
- **`livrable_existe_oui_non`** — la question binaire cruciale

Le champ `livrable_existe_oui_non` est **obligatoire**. Un packet
failed-run qui omet ce champ est invalide — le B2 sponsor **refuse**
de traiter et exige la complétion.

### Étape 2 — Vérification du livrable

Le B2 sponsor ne relance pas l'agent. Il lit le fichier
`scrums.md` du B3 squad lead (cf. triplet 8 : *« B3 produit SCRUMS.md
et rien d'autre »*) et le compare au scope du JTBD packet. Quatre
états possibles :

| État | Critère | Action B2 sponsor |
|---|---|---|
| **Vide** | aucun artefact produit, journal d'erreur uniquement | relancer le B3 squad lead (étape 3) |
| **Partiel** | artefact produit mais scope incomplet | acceptation partielle (étape 4) ou relance (étape 3) selon DoD |
| **Complet-non-vérifié** | artefact produit, scope complet, mais qualité non vérifiée | passer en revue B2 sponsor (examen préalable) |
| **Complet-vérifié** | artefact produit, scope complet, qualité vérifiée par le B3 squad lead | acceptation totale (étape 4) |

L'examen préalable (cf. `examen-prealable.md`) est l'outil canonique
de l'étape « complet-non-vérifié » : le B2 sponsor lance
`tools/examen.sh` (ou équivalent) sur le livrable avant de
décider.

### Étape 3 — Relance conditionnelle

L'état **Vide** ou **Partiel** peut justifier une relance. Trois
conditions cumulatives :

1. Le journal d'erreur indique une cause **transitoire** (timeout,
   OOM, fork épuisé), pas une cause **structurelle** (code qui ne
   compile pas, dépendance manquante).
2. La fenêtre de relance est **dans le cadre d'exécution** promis
   par le contrat B2 → B3 (cf. `b2-b3-jtbd-handoff-contract.md`
   §`cadre.duree`).
3. Le B2 sponsor consigne la relance dans une **ligne de journal
   Council** : `relance: <jtbd-id>, run: N+1, motif: <cause
   transitoire>`. D4 append-only.

Si une condition manque, **pas de relance**. Le packet mésoperpétuel
passe en `decision: blocked` (cf. `b2-meso-decision-packet-spec.md`)
et le sponsor escalade au Council pour ré-instruction.

### Étape 4 — Acceptation et clôture

L'état **Complet-vérifié** ou **Partiel-accepté** produit un packet
de retour (cf. `b2-b3-jtbd-handoff-contract.md` §`B2_RECEIPT`) avec :

- `decision: accepted` ou `decision: accepted_partial`
- `proof_path` (le chemin de l'artefact vérifié)
- `verification_log` (la sortie de l'examen préalable, le cas
  échéant)
- `next_action` (étape suivante du workflow, ou null si le packet
  est terminal)

L'acceptation partielle est **explicitement différente** d'un
échec. Le B3 squad lead a produit quelque chose de valide, même si
le scope est incomplet. La diff entre scope demandé et scope produit
est documentée — pas un trou, un **délai** (le reste est ré-arbitré
en Council ou reprogrammé dans un JTBD suivant).

## Pourquoi le B2 sponsor ne relance pas lui-même

Le triplet 56 dit *« Batman remonte à Summers des faits, pas des
décisions »*. Le B2 sponsor **remonte le fait** (état du livrable)
et **ne décide pas** de relancer sans passer par le B3 squad lead.
Trois raisons :

1. **Le B3 squad lead a le contexte de production.** Il sait ce qui
   a été tenté, ce qui a échoué, et ce qui reste à faire. Le B2
   sponsor qui relance à l'aveugle peut écraser un livrable
   partiellement valide (le piège nommé par le triplet 53).
2. **La discipline du signal.** Si le B2 sponsor peut relancer sans
   le B3 squad lead, le B3 squad lead n'a plus d'incitation à
   signaler — il peut attendre que le sponsor relance tout. Le
   triangle de responsabilité (B2 sponsor / B3 lead / Council) se
   rompt.
3. **L'escalier canonique reste respecté.** Le fractal
   §« L'escalier d'escalade (canonique) » dit *« on ne saute jamais
   un échelon »*. B2 sponsor qui relance B3 sans passer par le
   squad lead, c'est sauter le B3.

## Le cas Spécial — plafond Paperclip

Le triplet 52 dit que Paperclip-Coach-OS plafonne à 2-3 agents
simultanés. Quand le failed-run est causé par le plafond (fork:
Resource temporarily unavailable), la relance doit attendre la
**libération d'un slot**. Le B2 sponsor consigne dans le journal
Council : `pending_slot: <date-estimée>`. Le packet mésoperpétuel
reste ouvert jusqu'à la libération.

C'est le **seul cas** où la procédure de fail-safe accepte une
attente sans escalade B2 Council — la cause est **documentée et
transitoire**, et le slot se libère dans la journée en règle
générale.

## Les quatre issues possibles

```
failed-run remonté
   ↓
étape 1 — constat (5 champs obligatoires)
   ↓
étape 2 — vérification (4 états)
   ↓
   ┌─ vide ──────────────► relance conditionnelle (étape 3)
   ├─ partiel ───────────► acceptation partielle ou relance
   ├─ complet-non-vérifié ─► examen préalable (étape 3)
   └─ complet-vérifié ───► acceptation totale (étape 4)
   ↓
étape 4 — acceptation et clôture
   ↓
   ┌─ accepted ─────────► packet de retour normal
   ├─ accepted_partial ─► packet de retour avec diff documentée
   ├─ blocked ─────────► escalade B2 Council (motif = failed-run)
   └─ pending_slot ─────► attente libération slot Paperclip
```

Les quatre issues sont **mutuellement exclusives** : un packet
failed-run produit une seule issue, documentée en D4.

## Anti-pièges

- **Relancer sans vérifier.** Le B2 sponsor qui voit `failed-run` et
  lance immédiatement une relance applique le pattern explicitement
  interdit par le triplet 53. La discipline : étape 2 d'abord,
  étape 3 ensuite. Pas l'inverse.
- **B2 sponsor qui ne lit pas le livrable.** Un sponsor qui accepte
  l'état **Complet-non-vérifié** sur la foi du B3 squad lead
  contourne l'examen préalable. Le piège : un B3 squad lead qui
  déclare *« complet »* sans avoir lancé l'examen préalable. Le
  B2 sponsor doit **exiger** la sortie de l'examen.
- **Acceptation partielle silencieuse.** Un sponsor qui accepte un
  livrable partiel sans documenter la diff entre scope demandé et
  scope produit ouvre la porte au scope creep. La diff doit être
  dans le packet de retour.
- **Pending slot permanent.** Un B3 squad lead qui reste en
  `pending_slot` au-delà de 5 jours ouvrés n'est plus en fail-safe —
  il est en panne structurelle. Le B2 sponsor doit escalader B2
  Council pour dissolution ou ré-arbitrage.
- **Failed-run comme excuse.** Un B3 squad lead qui remonte
  failed-run pour masquer un silent rework (failure mode #2 dans
  `b2-b3-jtbd-handoff-contract.md`) contourne la discipline. Le
  B2 sponsor doit croiser le failed-run avec le journal d'exécution
  B3 — si le livrable est complet et le rework visible, c'est un
  silent rework, pas un failed-run.

## Liens

- [[b2-b3-jtbd-handoff-contract]] — le contrat bilatéral que le fail-safe protège
- [[b2-council-arbitrage-rule]] — l'instance qui reçoit l'escalade d'un failed-run non résolu
- [[b2-meso-decision-packet-spec]] — le format des packets de retour
- [[b2-pair-check-raci-by-rank]] — qui est Accountable quand un failed-run touche un pair-check
- [[b2-council-cadence-and-chair]] — la séance où le fail-safe est consolidé en doctrine
- [[examen-prealable]] — l'outil de vérification pour l'état « complet-non-vérifié »

## Note de confiance

**Projets, à moitié étayé.** Le triplet 53 est cité verbatim et ancre
la doctrine *« vérifier avant de relancer »*. Le triplet 52 fournit
la cause-type (plafond Paperclip). La transposition au rang B2 ↔ B3
est **projetée** : le triplet 53 parle d'agents Paperclip
(infrastructure), pas d'agents B3 logiques. Le saut est défendable
parce que le triplet 41 ancre le signalement B3 vers B2, mais il
doit être marqué projeté. La procédure en 4 étapes, les 4 états, et
les 4 issues sont **reconstruites** à partir de la doctrine
d'examen préalable (cf. `examen-prealable.md`) et du contrat B2 → B3.
Le cas Spécial « plafond Paperclip » est **empirique** — observé
dans la pratique documentée, pas dans un triplet canonique
d'arbitrage.
