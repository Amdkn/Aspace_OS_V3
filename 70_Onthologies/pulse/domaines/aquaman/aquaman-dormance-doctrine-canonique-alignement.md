---
type: Concept
title: Aquaman — alignement avec la doctrine canonique des domaines dormants
description: Tour 1 §4.1, tour 2 §T6.3, tour 3 open #6 et tour 4 ont tous soulevé le même point : la doctrine "Aquaman dormant" (triplet 35) est Coach-OS-spécifique et n'est pas alignée avec `b2-areas-dormants-doctrine.md`. Ce concept ferme la boucle en alignant explicitement le triplet 35 sur les trois conditions canoniques d'entrée en dormance + les trois déclencheurs canoniques de réveil, et en marquant la portée Coach-OS-spécifique comme exception, pas comme défaut.
tags: [b2, aquaman, dormance, doctrine, alignement, triplet-35, canonical]
generated: { by: minimax-m3, at: 2026-08-19T05:50:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-5, at: 2026-08-19T05:50:00Z }
sources:
  - id: triplet-35
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 35 — Aquaman steward domaine dormant"
    last_modified: 2026-08-17
  - id: triplet-36
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 36 — Legal dependsOn premier contrat signé"
    last_modified: 2026-08-17
  - id: b2-areas-dormants-doctrine
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: B2 Areas-dormants — la doctrine Aquaman et ses trois conditions
    last_modified: 2026-08-19
  - id: aquaman-dormant-activation
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-dormant-activation.md"
    title: Aquaman — la transition dormant ↔ activation, trois états distincts
    last_modified: 2026-08-19
  - id: aquaman-domaine-legal-perimetre
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-domaine-legal-perimetre.md"
    title: Aquaman — domaine Legal périmètre
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman — alignement avec la doctrine canonique des domaines dormants

## La boucle ouverte depuis quatre tours

Les rapports tour 1 à tour 4 ont tous signalé la même zone
d'ombre :

- **Tour 1 §4.1** : la doctrine "Aquaman dormant" (triplet 35) est
  *Coach-OS-spécifique*. Les 4 fichiers OMK ont un frontmatter
  `status: SHADOW_ACTIVE`, pas dormant.
- **Tour 2 §T6.3** : la doctrine Aquaman-dormant n'est pas alignée
  avec `b2-areas-dormants-doctrine.md` (qui n'a pas été lue à
  l'époque).
- **Tour 3 open #6** : la doctrine SHADOW_ACTIVE universelle n'a
  pas été réconciliée avec [[aquaman-dormant-activation]].
- **Tour 4 open #5** : classification 4 formes + 3 cas-frontière
  — extension à la doctrine ACTIVE, pas encore réconciliée avec
  la doctrine dormante générale.

Le concept `b2-areas-dormants-doctrine.md` (tour 5 lu) **pose la
doctrine générale des domaines dormants**, et Aquaman est *l'exemple
travaillé* explicite de cette doctrine. La réconciliation est donc
non plus un open, mais un alignement à formaliser.

## L'alignement triplet 35 ↔ doctrine canonique

Le triplet 35 dit verbatim : *« Aquaman steward Legal & Compliance
en état dormant : ne produit rien tant que
`00_Summers_CEO/03_Master_Agreements/` reste vide — un domaine
dormant qui produit est un coût sans contrepartie. »*

La doctrine canonique pose **trois conditions cumulatives** d'entrée
en dormance (§« Les trois conditions d'entrée en dormance ») :

| Condition canonique | Lecture Aquaman triplet 35 | Verdict |
|---|---|---|
| Aucune ressource externe ne requiert sa doctrine | "Aucun contrat dans `00_Summers_CEO/03_Master_Agreements/`" | ✅ Aligné |
| DoD vide pour le cycle courant | "Aucun Rock Legal actif" (lecture projetée depuis triplet 35 + cycle 12WY) | ✅ Aligné |
| Captain a consigné l'état dans le journal Council | "L'état dormant est documenté dans `VP_AGENT.md`" (Coach-OS) | ⚠️ **Divergence** |

La **divergence sur la condition 3** est précisément la zone d'ombre
que les tours précédents ont signalée. `VP_AGENT.md` n'est pas le
*journal Council* (`B2_DC_DIRECTION_COUNCIL_DECISIONS.md`). La
doctrine canonique exige **explicitement** le journal Council :

> *« Sans cette ligne, le captain est en absence, pas en dormance.
> L'absence est un défaut opérationnel ; la dormance est un acte
> documenté. »*

**Conséquence** : tant qu'Aquaman n'a pas consigné `decision:
dormant` dans `B2_DC_DIRECTION_COUNCIL_DECISIONS.md`, Aquaman est
*en absence* (Captain dormant non documenté), pas *en dormance*
(canonique).

**Action** : Aquaman doit rédiger un packet Council `decision:
dormant` au premier cycle Council où il n'a pas de Rock. La ligne
est append-only — Aquaman peut la poser aujourd'hui sans rien
réécrire.

## La portée Coach-OS-spécifique devient exception, pas défaut

Le triplet 35 est sourcé verbatim depuis `coach-os/.../Aquaman_Eternals/
VP_AGENT.md`. **Cette source est Coach-OS**, pas OMK, pas Jerry
Prime.

La doctrine canonique pose trois déclencheurs de réveil : signal B1,
signal B3 pair, signal client. Pour Coach-OS, le déclencheur
canonique est *signal client* (premier contrat signé), parce que
le projet est en pre-launch.

Pour OMK (frontmatter `status: SHADOW_ACTIVE`), le déclencheur est
**déjà** parti : OMK a 4 fichiers canoniques posés et une squad
cataloguée. **OMK est en SHADOW_ACTIVE**, pas dormant au sens
canonique — il lui manque le packet `decision: dormant` (parce qu'il
n'a jamais été dormant, il a toujours été en pré-construction).

**Conséquence** :

- Coach-OS Aquaman = *doctrine Coach-OS-spécifique* (triplet 35
  verbatim), mais doit poser `decision: dormant` dans le journal
  Council pour passer de *absence* à *dormant*.
- OMK Aquaman = *doctrine canonique appliquée*, frontmatter
  `status: SHADOW_ACTIVE` maintenu, jusqu'au premier livrable
  signé.
- Jerry Prime Aquaman = *à vérifier* (projet non documenté
  canoniquement).

## L'entrée en SHADOW_ACTIVE comme transition mineure

Ni la doctrine canonique ni le triplet 35 ne posent une *transition
formelle* Dormant → SHADOW_ACTIVE. [[aquaman-dormant-activation]]
pose cette transition comme **mineure** (activation shadow sans
escalade B1), mais elle n'est pas ancrée par triplet.

**Action proposée** : ajouter au journal Council, à la première
activation shadow, un packet `decision: shadow_active` qui pointe
vers le domain Aquaman. Le packet documente :

- le passage de l'état Dormant (par décision antérieure) à
  SHADOW_ACTIVE ;
- les 4 fichiers canoniques posés (avec date et frontmatter) ;
- la squad cataloguée (membres et sièges) ;
- le passage vers ACTIVE sera conditionné au prochain
  `LEGAL_READY` ou `BLOCKED_RISK`.

Ce packet est *complémentaire* au packet `decision: dormant`, pas
*concurrent*. Les deux tracent la trajectoire Aquaman en
D4 append-only.

## L'alignement des trois déclencheurs de réveil

La doctrine canonique pose trois déclencheurs canoniques de réveil.
Leur application à Aquaman :

| Déclencheur canonique | Application Aquaman | Source / projection |
|---|---|---|
| Signal B1 | Aquaman réveille si un mandate B1 dans handoff queue vise Legal directement (ex : revue conformité réglementaire) | `b2-areas-dormants-doctrine.md` §A. Signal B1 |
| Signal B3 pair | Aquaman réveille si un autre capitaine B3 signale un blocker privacy, claim ou IP | `b2-areas-dormants-doctrine.md` §B. Signal B3 pair |
| Signal client | Aquaman réveille au premier contrat signé (triplet 36 verbatim) | triplet 36 |

**Subtilité** : pour Aquaman, le signal client est *plus fort* que
les deux autres. Un contrat signé brise la dormance **avant** que
B1 ou B3 n'aient à escalader. La doctrine canonique marque
explicitement le signal client comme le plus fort des trois.

## La table de correspondance état ↔ packet Council

Une fois l'alignement appliqué, voici la table de correspondance
que Aquaman doit tenir en D4 :

| État Aquaman | Packet Council correspondant | Frontmatter | Critère d'entrée |
|---|---|---|---|
| **Dormant** (canonique) | `decision: dormant, domain: legal, since: YYYY-MM-DD` | (pas de fichiers domain posés, ou tous `status: dormant`) | 3 conditions canoniques remplies |
| **SHADOW_ACTIVE** | `decision: shadow_active, domain: legal, since: YYYY-MM-DD, triggered_by: ...` | `status: SHADOW_ACTIVE` | 4 fichiers canoniques posés + squad cataloguée |
| **ACTIVE** | `decision: active, domain: legal, since: YYYY-MM-DD, first_livrable: ...` | `status: ACTIVE` | Premier `LEGAL_READY` ou `BLOCKED_RISK` signé |

**Cette table est l'objet canonique de la trajectoire Aquaman**.
Tout Aquaman qui transite d'un état à un autre doit poser la ligne
correspondante dans le journal Council. Une trajectoire sans ces
lignes est *non-canonique* — soit le captain est en absence, soit
les transitions sont silencieuses.

## L'anti-piège — la doctrine Coach-OS-spécifique comme défaut implicite

L'anti-piège principal : un Aquaman qui applique la doctrine
Coach-OS-spécifique (triplet 35 verbatim) **comme si elle était
universelle** produit deux erreurs :

- **Erreur 1** : un Aquaman OMK qui croit que sa doctrine est
  *dormant* alors que le frontmatter pose `SHADOW_ACTIVE`. Le
  triplet 35 ne s'applique pas.
- **Erreur 2** : un Aquaman Coach-OS qui croit qu'il est *en
  dormance* (au sens canonique) parce que le triplet 35 le pose,
  alors qu'il est en *absence* parce que `decision: dormant`
  n'a jamais été consigné.

**Remède** : avant d'invoquer le triplet 35, vérifier :

1. Le journal Council porte-t-il `decision: dormant` ?
2. Si non → Aquaman est en *absence* (pas dormance canonique).
3. Si oui → la doctrine triplet 35 s'applique.

Ce test est *peu coûteux* (lecture + grep) et tranche la confusion
en deux secondes.

## Les questions que ce concept laisse ouvertes

Trois zones restent ouvertes après alignement :

1. **Pas de cycle Council réel observé**. Les recommandations
   `decision: dormant`, `decision: shadow_active` supposent que le
   journal Council existe en V3 — or il n'est pas trouvé (rapport
   tour 1 §3). Action : vérifier existence en V2, créer
   l'équivalent en V3 si besoin.
2. **Aquaman Jerry Prime non documenté**. Le triplet 35 cite
   Coach-OS, mais Jerry Prime (projet V2) peut avoir sa propre
   doctrine. Action : lire `VP_AGENT.md` Jerry Prime si elle
   existe.
3. **Le packet `decision: shadow_active` ajoute un nouveau type
   au mésoperpétuel**. La doctrine canonique pose `decision:
   dormant`, mais ne pose pas `shadow_active` (qui est un état
   Aquaman-spécifique). Action : étendre le mésoperpétuel ou
   rebadger `shadow_active` sous le même régime que dormant.

## Liens

- [[b2-areas-dormants-doctrine]] — la doctrine canonique des domaines
  dormants, Aquaman worked example
- [[aquaman-dormant-activation]] — la tri-partition Dormant /
  SHADOW_ACTIVE / ACTIVE (tour 2)
- [[aquaman-domaine-legal-perimetre]] — le périmètre Legal, dont
  l'état dormant est posé (tour 1)
- [[aquaman-squad-eternals-et-dormance]] — la tension effectif
  Eternals, dont la matérialisation dépend de l'activation (tour 1)

## Note de confiance

**Confirmé par machine pour les sources ; reconstruit pour
l'alignement.**

- ✅ Triplet 35, triplet 36, frontmatters OMK : cités verbatim.
- ✅ `b2-areas-dormants-doctrine.md` : lu intégralement, doctrine
  canonique posée.
- 🟡 L'alignement triplet 35 ↔ doctrine canonique : reconstruit
  depuis les 3 conditions canoniques et le triplet 35, avec
  détection explicite de la **divergence sur la condition 3**
  (journal Council vs `VP_AGENT.md`).
- 🟡 Les packets `decision: dormant`, `decision: shadow_active`,
  `decision: active` : projetés depuis la doctrine canonique et
  la tri-partition tour 2. **Le mésoperpétuel canonique ne pose
  pas `shadow_active`** (cf. open #3) — extension proposée non
  Council-ready.
- ❌ Non vérifié : existence du journal Council en V3 (rapport
  tour 1 §3), VP_AGENT Jerry Prime, recompte Council réelle des
  états Aquaman.
