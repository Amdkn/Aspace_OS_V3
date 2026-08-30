---
type: Concept
title: Flash — test de continuité de la doctrine « valeur d'artefact »
description: La doctrine valeur-d-artefact reste reconstruite après 13 concepts (tour 1 + tour 2). Ce concept pose un test concret en 4 dimensions + 5 critères d'acceptance qui transforme la doctrine en grille vérifiable. Le test sépare trois failure modes typiques et distingue la lecture stricte de la lecture large du périmètre Flash (cf. flash-domain-perimeter §« Pourquoi ces frontières existent »).
tags: [flash, product, doctrine, valeur-artefact, test-of-continuity, verification, build, run, sunset, pivot]
generated: { by: minimax-m3, at: 2026-08-19T08:00:00Z }
verified:
  - { by: process:lecture-corpus-flash-tour-3, at: 2026-08-19T08:00:00Z }
sources:
  - id: doctrine-valeur-artefact
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-doctrine-valeur-artefact.md"
    title: Flash Product — la doctrine « valeur d'artefact », contraste avec les 3 autres docteurs
    last_modified: 2026-08-19
  - id: veto-offre-depersonnalisee
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-veto-offre-depersonnalisee.md"
    title: Veto Flash — l'offre dépersonnalisée, 5 cas légitimes, 3 cas abusifs
    last_modified: 2026-08-19
  - id: domain-perimeter
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-domain-perimeter.md"
    title: Périmètre du domaine Flash — Product (03) et ses quatre frontières floues
    last_modified: 2026-08-19
  - id: batman-doctrine
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-doctrine-remonte-fait-non-decision.md"
    title: Batman doctrine — Flash parle en valeur d'artefact (l. 91-108)
    last_modified: 2026-08-19
  - id: triplet-v3-line-25
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet v3 ligne 25 — Flash hasVetoOver offre-depersonnalisee"
    last_modified: 2026-08-17
  - id: b2-veto-amplification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — triplet 58 (Wonder Woman)
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Flash — test de continuité de la doctrine « valeur d'artefact »

## Pourquoi un test, pas un énoncé

`flash-doctrine-valeur-artefact.md` pose la doctrine en 4 unités de parole (état, promesse, retour, valeur). `flash-veto-offre-depersonnalisee.md` pose le veto catalogue avec 5 cas légitimes. Mais aucun des deux ne donne un **test** qui distingue un artefact conforme d'un artefact qui ne l'est pas.

Le rapport tour 2 (`RAPPORT_dom-flash.md` §5.2) signale explicitement : *« Doctrine valeur d'artefact reste reconstruite sans cas pratique, malgré les 13 concepts posés. »* Le présent concept ferme cette lacune — un test vérifiable par un tiers qui n'est pas Flash.

## Le test en 4 dimensions

La doctrine « valeur d'artefact » se teste sur **4 dimensions** distinctes. Un artefact qui passe les 4 dimensions a une valeur indépendante de son créateur. Un artefact qui en manque une est **non-conforme** au veto canonique.

### Dimension 1 — Continuité de build (qui produit si l'opérateur part ?)

**Question** : si l'opérateur principal (l'agent Avengers qui a écrit le code, rédigé le livrable, ou porté la méthode) part demain, **qui produit la prochaine itération sans escalade ?**

Trois verdicts :
- ✅ **Continuité build OK** — un autre agent Avengers peut prendre sans formation spécifique (squad back-up formée, documentation de la méthode, pair programming pratiqué)
- ⚠️ **Continuité build partielle** — un autre agent peut prendre mais avec une formation de 2-4 semaines
- ❌ **Continuité build KO** — personne ne peut reprendre, l'artefact meurt avec l'opérateur

### Dimension 2 — Continuité de run (qui maintient si l'opérateur part ?)

**Question** : si l'opérateur principal part, **qui maintient la boucle de run** (support, monitoring, runbook, dépendances) ?

Trois verdicts :
- ✅ **Run OK** — Batman Ops peut maintenir avec la SOP standard, le runbook est documenté, le squad Fantastic Four a été formé
- ⚠️ **Run partiel** — Batman Ops maintient avec une exception documentée (formation, dette technique connue)
- ❌ **Run KO** — Batman Ops refuse de maintenir, l'artefact devient inutilisable

### Dimension 3 — Continuité de pivot (qui re-scope si le marché change ?)

**Question** : si la proposition de valeur doit pivoter (ex : client demande une évolution majeure du scope), **qui pilote la transformation ?**

Trois verdicts :
- ✅ **Pivot OK** — ScarletWitch (H90 transformation scope) peut piloter sans dépendance à l'opérateur originel
- ⚠️ **Pivot partiel** — la transformation nécessite une re-négociation avec l'opérateur originel
- ❌ **Pivot KO** — seul l'opérateur originel peut piloter le pivot

### Dimension 4 — Continuité de sunset (qui décommissionne proprement ?)

**Question** : le jour où l'artefact est retiré du catalogue, **qui gère la dépréciation sans casser les clients qui en dépendent ?**

Trois verdicts :
- ✅ **Sunset OK** — la dépréciation est documentée (date de fin, message client, archivage code)
- ⚠️ **Sunset partiel** — la dépréciation dépend d'un script connu d'un seul opérateur
- ❌ **Sunset KO** — aucun plan de dépréciation, le retrait casse les clients

## Les 5 critères d'acceptance combinés

Un artefact conforme au veto canonique **passe les 4 dimensions** ET respecte les **5 critères d'acceptance**. Un critère raté = veto applicable.

| # | Critère | Quand il est rempli |
|---|---|---|
| 1 | Runbook documenté et versionné | Le runbook existe dans `B3_Avengers_*/runbooks/` (ou équivalent) avec date, version, owner |
| 2 | Squad back-up identifiée et formée | Au moins 1 autre agent Avengers peut prendre le build sans formation spécifique |
| 3 | Run prêt à être absorbé par Batman | Le run est conforme à la SOP support standard OU une exception documentée existe |
| 4 | Pivot reproductible | La méthode de re-scope est documentée (pas dans la tête de ScarletWitch uniquement) |
| 5 | Sunset planifié | Une date de fin de vie est posée OU un signal de sunset est défini (ex : adoption < seuil) |

## Les 3 failure modes — ce qui rend le test rouge

### Failure mode 1 — Documentation-théâtre

**Symptôme** : le runbook existe, mais il ne couvre pas les incidents réels. CaptainAmerica produit un document pour le test, mais l'opérateur reste le seul à savoir débugger un cas de production.

**Détection** : un test en double-aveugle (deuxième agent Avengers exécute le runbook pendant que l'opérateur est indisponible 30 jours). Si le double-aveugle échoue → documentation-théâtre.

**Remède** : le runbook est réécrit par le double-aveugle qui a échoué, pas par l'opérateur originel.

### Failure mode 2 — Squad back-up fictive

**Symptôme** : IronMan est listé comme « squad back-up de CaptainAmerica » dans la fiche roster, mais IronMan n'a jamais lu le code ni participé à une itération.

**Détection** : IronMan doit livrer un patch trivial sur l'artefact dans les 48h. S'il échoue → squad back-up fictive.

**Remède** : la squad back-up doit faire au moins une itération complète par trimestre (rotation forcée).

### Failure mode 3 — Sunset jamais planifié

**Symptôme** : l'artefact est en production depuis 3+ ans sans aucune date de fin de vie ni signal de sunset.

**Détection** : un audit cron cherche les artefacts > 24 mois sans signal de sunset. Si > 5 trouvés → sunset-backlog.

**Remède** : chaque artefact > 24 mois doit déclarer un signal de sunset (adoption < seuil, breaking change upstream, dette technique > N jours-homme) ou une date de fin explicite.

## Distinction lecture stricte vs lecture large

`flash-domain-perimeter.md` §« Pourquoi ces frontières existent » pose deux lectures vivantes du périmètre Flash :

- **Lecture stricte** : la productisation uniquement (build). Le test couvre les dimensions 1+2.
- **Lecture large** : la maintenance transverse (build + run + sunset). Le test couvre les 4 dimensions.

**Recommandation** : la doctrine valeur-d-artefact, telle que posée par `flash-doctrine-valeur-artefact.md`, inclut implicitement la dimension 3 (pivot) et la dimension 4 (sunset) — c'est cohérent avec la lecture large. Le présent test applique donc la lecture large par défaut, et un artefact qui passe les 4 dimensions est conforme.

**Escalade B2 Council** : si un capitaine (Batman Ops, Cyborg IT, etc.) conteste l'application de la lecture large à son domaine, l'arbitrage se fait en mode **negotiation** (cf. `b2-three-cooperation-modes.md`). Le packet mésoperpétuel documente le tradeoff entre lecture stricte (moins de friction, plus de risque Sunset KO) et lecture large (plus de friction, moins de risque).

## Le test comme outil de veto

Quand Flash oppose son veto catalogue, le test devient la **grille de justification**. Le motif du veto n'est plus *« cette offre me semble nominative »* — il est *« dimension 2 rouge, run KO, pas de squad back-up formée. Cf. matrice 4D test-de-continuité, dimension 2. »*

C'est conforme à la propriété 2 du veto (vérifiable) — cf. `b2-eight-domain-vetoes-catalogue.md` §« Propriété 2 — Vérifiable ».

## Pourquoi ce test n'est pas une checklist

Trois différences entre ce test et une checklist projet-management classique :

1. **Le test mesure la disparition, pas la présence.** Un artefact qui a une documentation n'est pas conforme — il faut que la documentation permette à un tiers de prendre sans l'opérateur. La présence ne dit rien sur l'utilisabilité réelle.
2. **Le test accepte le partiel, pas le tout-ou-rien.** Un artefact en ⚠️ sur 1 dimension peut être commercialisé si les 4 autres sont en ✅. Le veto catalogue se déclenche sur **2+ dimensions rouges** ou **1 dimension rouge + 1 critère d'acceptance raté**.
3. **Le test distingue l'opérateur de l'organisation.** Une équipe stable ne prouve pas la continuité — c'est la **rotabilité** des rôles qui prouve la continuité. Un artefact porté par 7 agents qui ne sont pas rotés échoue le test.

## Anti-pièges

- **Test utilisé comme blocage systématique.** Si Flash oppose son veto sur chaque artefact qui rate 1 dimension, il bloque excessivement. Le veto catalogue ne s'applique qu'aux **cas où l'offre est commercialisée**. Un artefact interne (runbook, outil interne) peut rater 1 dimension sans veto.
- **Test qui confond rotation et remplacement.** La rotation (un agent change, un autre prend) n'est pas la réversibilité (le squad peut absorber le départ sans recrutement). Le test mesure la rotation effective, pas la fiche RH.
- **Test exécuté une seule fois.** Le test doit être **récurrent** (tous les 6 mois) pour détecter la dérive. Un artefact conforme en 2026-Q1 peut ne plus l'être en 2026-Q4 si l'opérateur originel est parti sans rotation.
- **Sunset-backlog non escaladé.** Un artefact > 24 mois sans signal de sunset est un Sunset KO. Si Flash ne remonte pas le sunset-backlog au B2 Council, le test devient un artefact administratif.

## Liens

- [[flash-doctrine-valeur-artefact]] — la doctrine dont le test est la grille
- [[flash-veto-offre-depersonnalisee]] — le veto qui s'appuie sur le test
- [[flash-domain-perimeter]] — les lectures stricte vs large du périmètre
- [[flash-pair-checks-dependencies]] — les pair-checks où le test s'applique
- [[flash-jtbd-emit-receive]] — CaptainAmerica squad lead, premier acteur du test
- [[b2-eight-domain-vetoes-catalogue]] — la propriété 2 (vérifiable) que le test sert
- [[b2-veto-amplification-cycle]] — l'amplification « mécanisme de reprise » que le test prépare
- [[batman-doctrine-remonte-fait-non-decision]] — le contraste avec l'unité de parole Batman (état)
- [[twelve-weeks-year-cycle]] — la récurrence 6 mois pour ré-exécuter le test

## Note de confiance

**Reconstruit, à moitié étayé.** Le triplet v3 ligne 25 et la doctrine Batman (l. 91-108) sont cités verbatim. Le contraste des 4 unités de parole est verbatim. Les 4 dimensions du test sont **projetées** à partir du cycle de vie d'un artefact (build → run → pivot → sunset) et de la pratique projet-management — pas une catégorie canonique du corpus. Les 5 critères d'acceptance combinent le RACI par rang (A = B2 en aval) avec les 4 formes canoniques de preuve (`b3-proof-path-4-formes`) — extrapolation assumée. Les 3 failure modes sont **reconstruits** à partir des erreurs typiques observées (documentation-théâtre citée dans `b3-cycle-scrums-five-per-week.md`, squad-back-up-fictive citée dans `flash-jtbd-emit-receive.md` §« Anti-pièges »). Le seuil de veto (2+ dimensions rouges OU 1 rouge + 1 critère raté) est **projeté** — pas de seuil canonique équivalent dans le corpus. Standing : draft d'outillage, à tester en cycle réel.