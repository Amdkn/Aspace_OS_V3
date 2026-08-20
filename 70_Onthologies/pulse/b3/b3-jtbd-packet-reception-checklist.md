---
type: Concept
title: JTBD packet — checklist de réception côté B3
description: Le point de vue B3 sur le paquet JTBD-001 : qu'est-ce qu'un agent doit cocher pour dire "oui, je peux travailler sans revenir poser de question" ? Checklist de complétude à 8 champs dérivés du canon Areas, augmentée des interdits B1 (pas de travail B3 sans DoD/JTBD source) et des 5 méthodes autonomie-agents.
tags: [jtbd, b3, packet, reception, checklist, dod, canonical, area-level]
generated: { by: minimax-m3, at: 2026-08-19T02:05:00Z }
verified:
  - { by: process:lecture-b3-jtbd-packet-grammar, at: 2026-08-19T02:05:00Z }
  - { by: process:synthese-pulse-b3-tour-1, at: 2026-08-19T02:05:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: jtbd-grammar-canonical
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/b3-jtbd-packet-grammar.md"
    title: JTBD-001 packet grammar — la grammaire B3 canonique (Area-level)
    last_modified: 2026-08-17
  - id: fractal-b1b2b3
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/fractal-b1b2b3-architecture.md"
    title: Le fractal B1/B2/B3 — Areas perpétuelles vs Summer's Verse datées
    last_modified: 2026-08-17
  - id: b1-mandate-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-mandate-packet-spec.md"
    title: B1 mandate packet — la grammaire du paquet B1 vers B2
    last_modified: 2026-08-19
  - id: triplet-scrums
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets (lignes 7-13 — B3 cadence et interdits)
    last_modified: 2026-08-17
  - id: autonomie-5-methodes
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/autonomie-agents/index.md"
    title: autonomie-agents — index des 5 méthodes
    last_modified: 2026-08-17
okf_version: "0.2"
---

# JTBD packet — checklist de réception côté B3

> Priorité du tour 1 B3. Le gabarit JTBD-001 existe au niveau Area
> (`JTBD-GROWTH-001_GUARDIANS_AAAS_GTM_PACKET.md` et 7 autres JTBD-001
> canoniques par domaine). Ce concept prend le point de vue **réception** :
> qu'est-ce qu'un B3 doit cocher dans le paquet qu'il reçoit pour
> commencer à travailler sans revenir poser de question ?

## Le paquet qu'un B3 doit recevoir

Le JTBD-001 canonique (Areas §1) impose déjà 9 sections en prose + un
frontmatter obligatoire. Le B3 qui le reçoit applique la **checklist de
complétude** suivante, dans cet ordre. Si un seul item manque, l'agent
**refuse** de démarrer et escalade en B2 (voir `b3-hole-signaling-doctrine.md`).

### 1. Frontmatter (8 champs minimum)

| Champ | Présence requise | Si manquant |
|---|---|---|
| `id` / `jtbd_id` | obligatoire | refus — pas d'identité = pas de traçabilité |
| `source_rock` | obligatoire | refus — pas de rattachement = drift autorisé |
| `layer` (`B3_AREA_WARP_CORE`) | obligatoire | refus |
| `surface` (Area parente) | obligatoire | refus |
| `scope` (Area / Project) | obligatoire | refus |
| `b2_owner` + `guardian_lead` | obligatoire | refus — qui escalader ? |
| `principles_ref` (P# doctrines援) | obligatoire | refus sans P# — le B3 n'a pas de doctrine à appliquer |
| `evidence_grade` | obligatoire | refus si `HYPOTHESIS` *sans* validation §5 explicite |

**Source** : `b3-jtbd-packet-grammar.md` §« Frontmatter obligatoire ». Le
roster fait foi sur les assignations — un packet qui s'en écarte n'est
pas invalide, mais le B3 documente l'écart dans son `SCRUMS.md`.

### 2. Job statement (1 phrase)

Le « when X needs Y, the squad produces Z so <B2 owner> can… ».

**Critère B3** : si le B3 ne peut pas le reformuler en une phrase sans
ajouter de contexte implicite, le job statement est trop flou. Refus
avec motif.

### 3. Squad roster (aligné au roster canonique)

Le `b3-jtbd-packet-grammar.md` §« Le Squad Roster prime sur les tags
inline » est explicite : **le roster fait foi**. Si le packet assigne un
agent qui n'est pas dans le roster (ou omet un agent du roster), le B3
n'agit pas avant d'avoir signalé l'écart à B2.

### 4. North Star + cadre AARRR (ou équivalent domaine)

Pour Growth : NSM + AARRR. Pour les autres domaines : équivalent
canonique. Si le packet n'ancre pas le job dans une métrique de domaine,
le B3 ne sait pas comment prioriser ses arbitrages.

### 5. ICP / VOC / painkiller hypotheses

**3 sections** : ICP filter (3 critères de rejet + scoring), VOC (5
pains génériques déclinés par mode), painkiller hypotheses (3 variants
canoniques + Drax kill-gate pour Growth, équivalent pour les autres
domaines).

**Critère B3** : sans VOC, le B3 ne sait pas à qui parle le job. Sans
ICP, le B3 ne sait pas qui exclure. Sans painkiller, le B3 ne sait pas
quoi construire.

### 6. Premier experiment RICE + lead/lag indicators + build gates

**RICE** : Reach × Impact × Confidence / Effort. **Lead indicators** :
ce qui se mesure en cours de route (leading). **Lag indicators** : ce
qui se mesure en fin (outcome). **Build gates** : conditions d'arrêt /
ship / itération.

Sans RICE : pas de priorisation des sous-tâches. Sans lead/lag : pas de
mid-course correction. Sans build gates : pas de critère d'arrêt.

### 7. Handoff & autorité (Area vs Project)

Le packet doit dire explicitement ce qui est **hérité** de l'Area
(doctrine canonique) et ce qui est **calibré** par le Project (mode
Solaris / Nexus / Orbiter). Sans cette séparation, un Project qui
re-dérive un ICP viole la doctrine Area.

### 8. DoD auto-check + Acceptance <Hero>

Le packet finit par une checklist d'acceptance avec un item réservé
`[ ] Acceptance <Hero>`. Tant que cet item est unchecked, le packet
n'est pas canonique et le B3 **n'agit pas**.

## Ce que le B3 refuse d'inventor

Le fractal B1/B2/B3 pose l'invariant : *« Pas de travail B3 sans une
source DoD ou JTBD de B2. »* Le B3 qui reçoit un packet incomplet n'a
pas le droit de **deviner** les champs manquants. Il a trois issues,
classées par coût croissant :

1. **Demander à B2** (peer ou owner du domaine) — preferred.
2. **Escalader via le squad lead** (`guardian_lead`) si B2 ne répond pas.
3. **Refuser le démarrage** et poser le motif dans `SCRUMS.md` — dernier recours.

L'inventaire (le B3 qui patche en silence ce qui manque dans le packet)
est le **premier anti-pattern** de la discipline B3. Il est documenté en
`b3-hole-signaling-doctrine.md`.

## Les 5 méthodes autonomie-agents appliquées à la réception

Chaque champ de la checklist est aussi un point où les 5 méthodes
s'appliquent :

| Méthode | | Application à la réception B3 |
|---|---|---|
| Examen préalable | | Avant de commencer, le B3 a lancé `tools/examen.sh` sur son périmètre (si périmètre code). Sortie jointe au SCRUM. |
| Agent relecteur | | Le SCRUM rendu est accompagné d'un peer-relecteur qui n'a pas écrit le code. |
| Bacs à sable | | Si le chantier croise un périmètre B2 voisin, bac à sable (worktree) — voir `bacs-a-sable-worktree.md`. À l'étape 1, cloisonnement par brief suffit. |
| Goodhart | | Les SCRUMS ne sont pas comptés pour la métrique « nombre de scrums ». L'output est la preuve inspectable, pas le compteur. |
| Tension Q/Q | | Le B3 tranche cas par cas : un SCRUM long et vérifié > 5 micro-SCRUMS. Voir `tension-qualite-quantite.md`. |

## Anti-pieges côté réception

- **Paquet trop court** : un packet sans ICP/VOC/painkiller n'est pas un
  JTBD-001, c'est une intention. Refus.
- **Paquet trop long** : un packet qui dépasse 4 pages est un plan B2, pas
  un JTBD. Refus et renvoi en B2 pour distillation.
- **Acceptance `<Hero>` déjà cochée à la réception** : c'est un faux
  canon. Le B3 signale l'irrégularité à B2 et **n'agit pas** tant que
  l'acceptance n'est pas re-signée.
- **Re-dérivation d'un ICP canonique** : si le Project re-dérive l'ICP
  de l'Area, le B3 remonte l'écart au squad lead et au B2 owner.

## Source de la checklist

- `b3-jtbd-packet-grammar.md` §« Le packet canon — section par section »
  — les 9 sections canoniques (Areas, perpetual doctrine).
- `b1-mandate-packet-spec.md` §« Ce que B2 recoit et fait » — la
  traduction amont B1→B2→B3 et le rôle de B2 en distillation.
- `fractal-b1b2b3-architecture.md` §« Les stop conditions (durs) » —
  l'invariant *« pas de B3 sans DoD/JTBD »*.

## Liens

- [[b3-peer-unblock-protocol]] — quand un champ manque, qui le B3 tente de débloquer en premier
- [[b3-hole-signaling-doctrine]] — l'anti-pattern du B3 qui comble un trou en silence
- [[b3-proof-path-4-formes]] — ce que le B3 rend, une fois le paquet accepté
- [[b3-cycle-scrums-five-per-week]] — le grain temporel minimal, post-réception
- [[b3-veto-and-signal-vocabulary]] — le vocabulaire signal pour escalader à B2
- [[fifty-three-b3-agent-roster]] — qui consomme ces paquets
- [[eight-domain-avengers-wheel]] — qui les émet (les 8 B2)

## Note de confiance

**Confirmé par machine.** La checklist de complétude est dérivée
verbatim du concept Areas `b3-jtbd-packet-grammar.md`, qui cite lui-même
le packet source `JTBD-GROWTH-001_GUARDIANS_AAAS_GTM_PACKET.md`
(non lu dans cette passe). Les 5 méthodes autonomie-agents sont lues.
L'invariant *« pas de B3 sans DoD/JTBD »* est dans le fractal.

**Écart signalé** : le corpus donne 7 domaines dans un SDD ancien et
8 dans le canon à jour (cf. `eight-domain-avengers-wheel.md`). Le code
(8 squads, 8 JTBD-001 canoniques) est en avance sur le document ancien.
Cette checklist utilise 8.