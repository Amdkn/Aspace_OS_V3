---
type: Concept
title: Les 8 domaines sont en absence, pas en dormance — spécifié à 100 %, exécuté à 0 %
description: SPRINTS.md des 8 domaines B2 est entièrement rempli (livrables nommés, chemins exacts, dates), mais 53/53 SCRUMS.md sont des gabarits vierges, 0 fichier dans dossiers/, 0/11 paquets Council signés. La colonne « Tenu ? » vide ne distingue pas « pas encore échu » de « jamais exécuté » — le système ne peut pas se déclarer en échec, seulement se taire.
tags: [b2, dormance, absence, sprints, scrums, council, wonder-woman, execution, mesure]
generated: { by: claude-opus-5, at: 2026-08-26T07:30:00Z }
verified:
  - { by: process:mesure-directe-repo, at: 2026-08-26T07:30:00Z }
sources:
  - id: sprints-finance
    resource: "coach-os-app/04_Business_Domains/06_Finance_et_ROI_WonderWoman_Thunderbolts/SPRINTS.md"
    title: 4 sprints d'août, livrables nommés, colonnes Tenu ?/Motif vides
    last_modified: 2026-08-26
  - id: scrums-echantillon
    resource: "coach-os-app/04_Business_Domains/01_RH_Meta_Gouvernance_GreenLantern_XMen/squad/01_ProfessorX_Recruiting/SCRUMS.md"
    title: Gabarit non rempli, 35 lignes, <AAAA-Sxx> jamais remplace
    last_modified: 2026-08-26
  - id: mesure-scrums
    resource: "find 04_Business_Domains -name SCRUMS.md | wc -l && wc -l chacun"
    title: 53 fichiers, tous exactement 35 lignes
    author: process:claude-opus-5
    last_modified: 2026-08-26
  - id: mesure-dossiers
    resource: "find 04_Business_Domains/*/dossiers -type f"
    title: 0 fichier sur les 8 domaines
    author: process:claude-opus-5
    last_modified: 2026-08-26
  - id: council-non-signe
    resource: "coach-os-app/04_Business_Domains/B2_DC_DIRECTION_COUNCIL_DECISIONS.md"
    title: 11 paquets, 0 signature
    last_modified: 2026-08-26
  - id: doctrine-anterieure
    resource: "70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: Les 3 conditions cumulatives de la dormance — absence ≠ dormance
    last_modified: 2026-08-19
  - id: diagnostic-anterieur
    resource: "70_Onthologies/pulse/domaines/batman/batman-rupture-dormance-structurelle-wheel-8-domain.md"
    title: "0 packet mésoperpétuel sur 175 concepts OKF, daté 2026-08-19"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Les 8 domaines sont en absence, pas en dormance

## La question posée

Le capitaine avait supposé que la dormance de Legal, et l'inertie des 7
autres domaines, venaient du non-enregistrement d'un client de niveau
zéro. Cette hypothèse a été écartée par mesure (voir
`002_ARCHITECTE_NIVEAU_ZERO.md` dans `03_Master_Agreements/`) : le seuil
d'activation de Legal — le premier fichier déposé dans
`03_Master_Agreements/` — était déjà franchi. La vraie cause restait à
établir. Elle l'est ici, par mesure directe du dépôt Coach OS.

## Mesure, couche par couche

| Couche | État | Preuve |
|---|---|---|
| B1 `ROCKS.md` | rempli | 86 lignes, 28 lignes de tableau |
| B2 `SPRINTS.md` | **spécifié à 100 %, 8/8** | 40–81 lignes chacun ; le cas Finance nomme 4 livrables (`COST_MODEL.md`, `PRICING.md`, `ROI_METRIC.md`, trio `REPRO/FINANCIAL_DOSSIER/COMPLIANCE_NOTE`), avec chemin exact, techniciens assignés, dates du 3 au 28 août |
| B3 `SCRUMS.md` | **53 gabarits vierges** | tous exactement 35 lignes, `<AAAA-Sxx>` jamais remplacé, les 5 cases jour/preuve vides |
| Livrables `dossiers/` | **0 fichier** | mesuré sur les 8 domaines sans exception |
| Journal Council | **0/11 signé** | `grep -c "^decision:"` = 11, `grep "^signé:"` = 11 lignes, toutes vides |

**Le système a été intégralement spécifié et n'a jamais été exécuté une
seule fois.** La couche de spécification (B1→B2) est de bonne qualité —
chiffrée, datée, avec chemins de fichiers exacts. La couche d'exécution
(B3→livrable) n'a jamais tourné.

## Pourquoi la doctrine existante classe ça en « absence », pas en dormance

`b2-areas-dormants-doctrine` pose trois conditions **cumulatives** pour
qu'un domaine soit légitimement dormant. Deux échouent ici :

**Condition 2 — le DoD est vide.** La doctrine distingue explicitement :

> « Le DoD du cycle est vide — pas "non rempli", **vide**. La différence
> compte : un DoD non rempli appelle une action ; un DoD vide appelle la
> dormance. »

Ici le DoD (`SPRINTS.md`) n'est ni vide ni exécuté : il est **rempli et
ignoré**. Ce troisième état n'a pas de nom dans la doctrine — ce concept
lui en donne un : l'**absence**.

**Condition 3 — consigné au journal Council.** 0/11 signatures.

> « Sans cette ligne, le captain est en absence, pas en dormance.
> L'absence est un défaut opérationnel ; la dormance est un acte
> documenté. »

**Verdict de la doctrine appliquée aux 8 domaines : absence, pas
dormance.** Y compris Legal, dont le seuil d'activation est franchi mais
dont le paquet Council n'est pas non plus signé.

## Pourquoi ça n'a pas été détecté pendant un mois

C'est le défaut structurel, pas anecdotique. Le seul artefact censé
enregistrer un échec est la colonne **« Tenu ? »** de `SPRINTS.md`. Elle
est vide sur les 4 sprints des 8 domaines — **personne n'a écrit
« non »**.

Une case vide se lit exactement comme « pas encore échu ». **Le mode de
défaillance produit le même artefact que « pas encore commencé ».** Le
système ne signale pas l'échec, il ne dit rien du tout.

C'est le même défaut que celui corrigé sur `_runtime/kernel.mjs` le
2026-08-24 : un noyau qui se déclarait dormant alors qu'il était mort.
Le correctif appliqué là (`--sante` distingue DORMANT de MORT selon l'âge
du dernier battement) n'a pas d'équivalent au niveau B2/B3 — rien ne
calcule l'âge d'un sprint échu et non coché.

## Ce diagnostic n'est pas nouveau — il était déjà écrit

`batman-rupture-dormance-structurelle-wheel-8-domain.md`, daté du
2026-08-19, mesurait déjà : *« 175 concepts OKF cumulés, 0 packet
mésoperpétuel réel. Aucun des 8 capitaines n'a franchi le seuil ACTIF. »*
et concluait : *« 0 application = 0 motif d'arbitrage. »*

Ce concept-ci confirme la même conclusion sept jours plus tard, avec une
mesure plus fine (au niveau sprint/scrum plutôt qu'au niveau packet), et
ajoute le mécanisme précis de non-détection (la case vide silencieuse).
La doctrine ne manquait pas — **l'exécution manquait**.

## La sortie choisie, pas seulement diagnostiquée

Le capitaine a choisi de rompre l'absence par le chemin le plus court :
un run réel sur le domaine dont la spécification était déjà la plus
actionnable (Finance, sprint 1), plutôt que produire un 176e concept de
doctrine. Résultat déposé dans le dépôt Coach OS, pas dans ce corpus :

- `coach-os-app/04_Business_Domains/06_Finance_et_ROI_WonderWoman_Thunderbolts/dossiers/2026-08/COST_MODEL.md`
- `coach-os-app/04_Business_Domains/06_Finance_et_ROI_WonderWoman_Thunderbolts/SPRINTS.md`,
  ligne S1 marquée « Oui (partiel) »

Un seul poste de coût confirmé ($50/mois), trois marqués explicitement
non confirmés plutôt que devinés — même discipline mesure-contre-suppose
que ce concept applique à la doctrine.
