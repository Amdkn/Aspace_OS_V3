---
type: Concept
title: Aquaman — couplages invisibles avec les autres domaines B2
description: Aquaman est Consulted sur les pair-checks #7 (Legal→Growth) et #8 (Legal→Product), mais la matrice d'harmonisation ne montre pas cinq couplages indirects : Aquaman↔Cyborg (privacy IT), Aquaman↔Wonder Woman (honoraires avocats), Aquaman↔Superman (réécriture de claims bloquées), Aquaman↔JohnJones (clauses commerciales), Aquaman↔Green Lantern (owners qui signent). Chacun peut déclencher un veto opposé ou un arbitrage implicite.
tags: [b2, aquaman, couplages, dependances, cyber, finance, growth, sales, people]
generated: { by: minimax-m3, at: 2026-08-19T03:50:00Z }
verified:
  - { by: process:lecture-canon-aquaman, at: 2026-08-19T03:50:00Z }
sources:
  - id: legal-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/README.md"
    title: 08 Legal - Aquaman / Eternals — Required Input From Product
    last_modified: 2026-05-25
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair checks et red flags
    last_modified: 2026-08-17
  - id: pair-check-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman — couplages invisibles

## Ce que la matrice d'harmonisation montre déjà

Sur les 9 pair-checks canoniques, Aquaman est **Consulted** sur deux
explicitement :

- **#7 Legal → Growth** : A = Superman (Growth), C = Aquaman (Legal)
- **#8 Legal → Product** : A = Flash (Product), C = Aquaman (Legal)

C'est la position visible. Aquaman cadre ces deux transitions sans
les piloter (cf. [[aquaman-gates-et-pair-checks]]). Mais ces deux
lignes ne capturent pas **cinq couplages indirects** que la matrice
ne nomme pas explicitement.

## Couplage 1 — Aquaman ↔ Cyborg (data privacy ↔ IT)

**Surface** : la privacy review Aquaman touche les choix IT
implémentation (chiffrement, IAM, retention). Un Aquaman qui émet
`BLOCKED_RISK` sur une feature parce que *« les données ne sont pas
chiffrées at rest »* formule une exigence que Cyborg doit traduire en
spec IT.

**Tension** : Cyborg a son propre veto (cloud-only sans chemin de
sortie, cf. `b2-eight-domain-vetoes-catalogue.md`). Un Aquaman qui
exige *« pas de cloud-only »* pour des raisons privacy rentre en
**convergence de vetos** — les deux capitaines bloquent le même
mandat pour des raisons différentes. C'est un cas de
`negotiation` mode (cf. `b2-council-arbitrage-rule.md` §Trois modes).

**Pair-check implicite** : aucun dans les 9 canoniques. C'est un
couplage qui se déclenche *par les veto*, pas par les transitions.

## Couplage 2 — Aquaman ↔ Wonder Woman (honoraires juridiques)

**Surface** : un Aquaman qui dit *« il faut un avocat externe pour
cette revue »* déclenche une dépense récurrente (ou ponctuelle
substantielle). Wonder Woman tient le veto *« dépense récurrente sans
date de revue et sans métrique de retour »*.

**Tension** : Aquaman cadre la qualité (privacy review tierce), Wonder
Woman cadre la viabilité économique. Un Aquaman qui exige un cabinet
new-yorkais à 600$/h pour un projet SMB rentre en conflit de
mandat — la qualité Legal est non-négociable pour Aquaman, le coût est
non-négociable pour Wonder Woman.

**Couplage** : Aquaman ne peut pas activer de la qualité Legal sans
consulter Wonder Woman sur le modèle de coût. Le triplet v3 ligne 58
cette logique pour Wonder Woman : *« corrélat direct avec la dette
récurrente — chaque ligne doit porter une métrique de retour
chiffrée »*.

## Couplage 3 — Aquaman ↔ Superman (réécriture de claims bloquées)

**Surface** : un Aquaman qui oppose son veto sur une claim (pair-check
#7) bloque la publication. Superman tient le canal de diffusion, mais
c'est *Superman* qui doit réécrire la claim pour qu'elle passe le
filtre Aquaman.

**Tension** : Aquaman cadre le contenu (claims safe, defensibility),
Superman tient la promesse publique. Un Aquaman qui dit *« cette
claim n'est pas safe, reformulez »* n'a pas le mandat de réécrire
lui-même — il cadre, il n'opère pas. Si Superman et Aquaman divergent
sur la *reformulation*, aucun des deux n'a de levier direct sur
l'autre : c'est un cas d'escalade au B2 Council.

**Couplage** : Aquaman émet `BLOCKED_RISK`, Superman doit
*consommer* le blocker et le traduire en claim corrigée. Si Superman
ne le fait pas, l'arbitrage remonte.

## Couplage 4 — Aquaman ↔ JohnJones (clauses commerciales)

**Surface** : un contrat client (Sales) doit passer par Aquaman pour
le périmètre + propriété du livrable (cf. veto catalogue). JohnJones
tient le veto *« proposition envoyée avant qu'un problème client ait
été reformulé et validé »* — un pré-filtre Sales.

**Tension** : les deux vetos se déclenchent en cascade.
JohnJones vérifie que le *problème* est reformulé. Aquaman vérifie que
le *périmètre du livrable* est écrit. Si les deux ne sont pas
coordonnés, un client peut recevoir une proposition qui passe le
filtre JohnJones mais échoue sur le filtre Aquaman — ou inversement.

**Couplage** : le pipeline Sales → Legal est un *handoff* implicite.
Aucun packet mésoperpétuel ne le pose aujourd'hui — c'est un trou dans
la doctrine.

## Couplage 5 — Aquaman ↔ Green Lantern (owners signataires)

**Surface** : un contrat signé par la mauvaise personne est un risque
Legal. Green Lantern tient le veto *« recrutement sans mandat écrit »*
mais aussi le roster des owners qui peuvent signer.

**Tension** : un Aquaman qui dit *« il faut un signataire autorisé sur
ce contrat »* déclenche un questionnement People sur *qui est
autorisé*. Si Green Lantern n'a pas posé la matrice de signature,
Aquaman ne peut pas émettre `LEGAL_READY`.

**Couplage** : Aquaman a besoin de la matrice de signature People
comme input. Si elle n'existe pas, Aquaman ne peut pas fonctionner en
cadre — il est forcé d'opérer (ce qui est hors-périmètre).

## Synthèse — qui dépend de qui

Tableau des dépendances croisées :

| Aquaman a besoin de | Pour | Sinon |
|---|---|---|
| **Flash (Product)** | Liste data + claims + third-party assets | `BLOCKED_RISK` par défaut |
| **Superman (Growth)** | Claim publique écrite | Pas de `LEGAL_READY` |
| **Cyborg (IT)** | Choix d'implémentation privacy | Convergence de veto |
| **Wonder Woman (Finance)** | Modèle de coût des revues | Veto Wonder Woman |
| **JohnJones (Sales)** | Reformulation client | Cascade de veto |
| **Green Lantern (People)** | Matrice de signature | Aquaman forcé d'opérer |

| Dépend de Aquaman | Pour | Sinon |
|---|---|---|
| **Flash (Product)** | Privacy review avant merge | Veto Aquaman implicite |
| **Superman (Growth)** | Claim safety avant publication | `BLOCKED_RISK` |
| **JohnJones (Sales)** | Périmètre + propriété avant signature client | Veto veto Aquaman |
| **Wonder Woman (Finance)** | Cadre contractuel pour assurance / provision | Risque non budgété |
| **People (Green Lantern)** | Validation contrat de travail / NDA | Recrutement non protégé |
| **Batman (Ops)** | Conditions d'arrêt contractuelles | Procédure sans cadre Legal |

## Anti-pièges

- **Ignorer un couplage parce qu'il n'est pas dans la matrice.** Les 9
  pair-checks sont une **base**, pas une **liste exhaustive**. Les 5
  couplages ci-dessus sont des points où Aquaman pèse *sans* être
  Accountable.
- **Croire qu'un couplage double le veto.** Aquaman et Cyborg peuvent
  bloquer le même mandat pour des raisons différentes — c'est un
  `negotiation` mode, pas un double veto. Le B2 Council tranche une
  fois.
- **Penser qu'Aquaman peut opérer sans les inputs amont.** Si Flash
  ne livre pas la liste data, Aquaman ne peut pas émettre de gate. Le
  blocker est sur Flash, pas sur Aquaman.

## Liens

- [[aquaman-domaine-legal-perimetre]] — les 7 surfaces qui
  déclenchent les couplages
- [[aquaman-veto-engagement-sans-perimetre]] — le veto qui
  se couple avec Cyborg et JohnJones
- [[aquaman-gates-et-pair-checks]] — les pair-checks canoniques
  où Aquaman est Consulted
- [[b2-harmonization-matrix-exploitable]] — la matrice qui ignore
  ces 5 couplages
- [[b2-council-arbitrage-rule]] — le `negotiation` mode qui tranche
  les conflits de couplage

## Note de confiance

**Confirmé par machine pour les pair-checks canoniques ; reconstruit
pour les couplages implicites.** Les pair-checks #7 et #8 sont
confirmés verbatim par `b2-pair-check-raci-by-rank.md`. Les 5
couplages implicites sont **reconstruits** à partir du périmètre
Legal (README), du veto catalogue, et de la doctrine d'arbitrage
Council. Aucun packet mésoperpétuel réel ne les observe — c'est une
projection depuis le framework, pas une trace de cycle.
