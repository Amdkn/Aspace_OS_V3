---
type: Concept
title: Aquaman — pipeline Sales → Legal : fermer le trou doctrinal
description: Le rapport tour 1 §4.4 a explicitement identifié *« Le pipeline Sales→Legal est un trou doctrinal : aucun packet mésoperpétuel ne pose le handoff entre les deux capitaines »*. Le tour 4 formalise ce handoff comme un pair-check #11 candidat V5 : JohnJones A (Sales aval, fermé au moment du deal), Aquaman C (Legal), Aquaman veto sur périmètre (classe 4) en cas d'amendement impossible. Trois classes de deals (standard / urgent / template-based) avec timing T-X différent, sans补 déroger au veto catalogue.
tags: [b2, aquaman, johnjones, sales, legal, handoff, pipeline, trou-doctrinal, pair-check-11]
generated: { by: minimax-m3, at: 2026-08-19T06:00:00Z }
verified:
  - { by: process:lecture-canon-aquaman-tour-4, at: 2026-08-19T06:00:00Z }
sources:
  - id: rapport-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-aquaman.md"
    title: "Rapport tour 1 §4.4 — Le pipeline Sales→Legal est un trou doctrinal"
    last_modified: 2026-08-19
  - id: aquaman-couplages
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-couplages-invisibles.md"
    title: "Aquaman couplages invisibles §Couplage 4 — Aquaman ↔ JohnJones (clauses commerciales)"
    last_modified: 2026-08-19
  - id: aquaman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-veto-engagement-sans-perimetre.md"
    title: Aquaman veto — engagement-sans-périmètre
    last_modified: 2026-08-19
  - id: aquaman-pair-check-10
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-pair-check-10-legal-risk-launch.md"
    title: Aquaman pair-check #10 Legal risk → Launch (proposition V5)
    last_modified: 2026-08-19
  - id: b2-harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable (9 pair-checks canoniques)
    last_modified: 2026-08-19
  - id: b2-pair-check-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: "RACI par rang §Pourquoi A = B2 en aval, pas B1"
    last_modified: 2026-08-19
  - id: triplet-vp-sprint
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 11 — VP ne peut pas amender un scope qui change de domaine"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Aquaman — pipeline Sales → Legal : fermer le trou doctrinal

## Le trou, tel que posé en tour 1

Le rapport tour 1 ([[rapport-tour-1]]) §4.4 dit verbatim :

> *« Le pipeline Sales→Legal est un trou doctrinal : aucun packet
> mésoperpétuel ne pose le handoff entre les deux capitaines. Si
> Sales promet sans cadrage Legal, le veto Aquaman s'oppose a posteriori
> — pas de prévention en amont. »*

Le couplage Aquaman ↔ JohnJones (Sales) est documenté en
[[aquaman-couplages-invisibles]] §Couplage 4, mais sans procédure de handoff
formelle. Le **risque opérationnel** est asymétrique : Aquaman ne voit la
promesse qu'après l'envoi — et son veto canonique *engagement-sans-périmètre*
(cf. [[aquaman-veto-engagement-sans-perimetre]]) devient un **blocage rétroactif**
au lieu d'une **prévention amont**.

## Le pair-check #11 candidat V5

Le tour 3 a déjà proposé le pair-check #10 `Legal risk → Launch` (cf.
[[aquaman-pair-check-10-legal-risk-launch]]). Le pipeline Sales→Legal est
**distinct** : il porte sur le **moment du deal**, pas sur le **moment du
launch**. La V5 peut accueillir les deux comme deux pair-checks
supplémentaires, avec procédure d'amendement unanimité 8/8 + B1 (cf.
[[b2-pair-check-raci-by-rank]] §Pourquoi A = B2 en aval, pas B1).

### Le tableau RACI du pair-check #11

| # | Pair-check | A (Accountable) | R (Responsible) | C (Consulted) | I (Informed) |
|---|---|---|---|---|---|
| 11 | Sales → Legal (deal-close) | B2 Sales (JohnJones) | B3 Illuminati | B2 Legal (Aquaman) | B1, B3 Eternals |

**Justification A = Sales (JohnJones)** : par application du principe
*« A est toujours le B2 captain en aval de la transition »* ([[b2-pair-check-raci-by-rank]]
§Le tableau par rang). Sales est en aval du deal — c'est lui qui porte la
responsabilité opérationnelle du closing. Aquaman ne tranche pas l'opportunité
commerciale, il cadre la conformité du livrable.

**Justification R = Illuminati (B3 squad)** : par application de la règle
*« B3 est Responsible au sens d'exécution opérationnelle du transfert »*
([[b2-pair-check-raci-by-rank]] §Pourquoi R = B3, pas B2). L'équipe Sales
construit le deal ; c'est elle qui produit la documentation contractuelle.

**Justification C = Aquaman** : Aquaman est **Consulted** pendant le cycle
de vente, mais c'est un **veto d'input** qu'il émet au closing, pas un veto
de la décision commerciale.

**Distinction avec le pair-check #10** : le #10 porte sur le **launch**
(risque Legal avant publication), le #11 porte sur le **deal** (cadrage
Legal avant signature client). Les deux sont nécessaires mais déclenchés à
des moments différents.

## Les 3 classes de deals — procédures différenciées

### Classe 1 — Deal standard (template-based)

**Description** : deal qui suit un template Aquaman (Forme 3 du catalogue
JTBD — cf. [[aquaman-jtbd-emit-receive]] §Forme 3). Le contrat est
essentiellement **pré-écrit**, Aquaman n'intervient que pour la validation
finale.

**Timing handoff** : T-2j avant closing. B3 Illuminati soumet le deal
complet à Aquaman ; Aquaman émet `LEGAL_READY` ou `BLOCKED_RISK` en 24h.

**Veto** : `BLOCKED_RISK` Aquaman **stoppe le closing** — c'est le veto
canonique. Le Sales doit amender (clause, périmètre, propriété) avant de
re-soumettre. Pas de court-circuit possible (cf. *Anti-pièges* §Court-circuit
template).

### Classe 2 — Deal urgent (non-template, hors-template)

**Description** : deal qui **déroge** aux templates Aquaman — clauses
personnalisées, juridiction exotique, livrable complexe (par exemple
partenariat multi-parties, marché régulé).

**Timing handoff** : T-7j avant closing. Aquaman doit produire une revue
*forensic* — pas seulement un coup d'œil au template. Le délai T-7j est
cohérent avec [[aquaman-launch-ready-portique-final]] §Timing cible T-7j.

**Veto** : `BLOCKED_RISK` Aquaman **stoppe le closing** et **ouvre un arbitrage
B2 Council** si JohnJones conteste. Le mode Council est `negotiation` (cf.
[[b2-harmonization]] §Trois modes) parce que deux DoDs domain sont en conflit :
Sales (clore le deal) et Legal (cadrer le livrable).

### Classe 3 — Deal self-serve (template-only, automated)

**Description** : deal **100% template**, clos par le client sans
intervention Sales (par exemple self-serve SaaS avec terms of service
figés). Aquaman n'intervient **pas** au closing — la validation template a
eu lieu au moment de la mise en ligne du template.

**Timing handoff** : aucun, par construction. La validation Aquaman est
**asynchrone** et périodique (revue de templates une fois par sprint).

**Veto** : Aquaman peut bloquer un self-serve **rétroactivement** en
retirant un template défectueux — mais c'est un acte de **régulation**, pas
un veto de deal. La procédure est distincte (cf. [[aquaman-classification-risques-4-formes]]
§Les 4 gates comme discipline).

## La coordination avec le naming W40 V4

Le captain Sales a changé de nom en W40 V4 — *Martian Manhunter* (legacy)
vers *JohnJones* (canon). Cf. [[eight-domain-avengers-wheel]] §Note sur la
nomenclature Sales. Le pair-check #11 utilise le nom courant **JohnJones**,
pas Martian Manhunter. Trois projets sur quatre utilisent encore l'ancien
nom (cf. [[aquaman-couplages-invisibles]] §Couplage 4 source commentaires) —
la migration est **inachevée**.

**Conséquence** : un B2 captain qui oppose le #11 par le nom *JohnJones*
risque de ne pas être reconnu par un B3 squad encore sur *Martian Manhunter*.
La mitigation : le packet mésoperpétuel utilise le **rang** (*B2 Sales*)
avec le **nom** entre parenthèses, jamais le nom seul.

## Le format du handoff packet

Le B3 Illuminati produit un **handoff packet** au moment du closing, qui
contient :

```yaml
jtbd_id: B3-LEGAL-HANDOFF-YYYY-NN
source_deal: CRM-opportunity-id
class: 1 | 2 | 3
deal_owner: <B3 Illuminati rep>
template_used: <template-id>  # Class 1 + 3 only
custom_clauses: [<clause-id>, ...]  # Class 2 only
deliverable:
  type: <artifact>
  owner_to_be: <role>
  perimeter: <text>
  property: <clause-ref>
closing_target: YYYY-MM-DD
gating_inputs:
  - source: johnjones-reformulation
    required: true
    fallback: BLOCKED_RISK (Aquaman)
  - source: aquaman-template-review
    required: true (Class 1) | n/a (Class 2) | not_required (Class 3)
```

**Aquaman signe** le handoff packet conjointement avec le B3 Illuminati rep
(double signature B2 sponsor / B3 lead — cf. [[b2-b3-jtbd-handoff-contract]]
§Le format conjoint). Sans cette double signature, le closing peut être
contesté rétroactivement.

## Anti-pièges

- **Court-circuit template.** Un Sales qui ferme un deal Classe 2 (urgent)
  avec un template Classe 1 sans passer par le handoff T-7j est en violation
  de procédure. Le `BLOCKED_RISK` rétroactif Aquaman est légitime — le Sales
  a contourné le circuit. La mitigation : Batman et Superman sont
  *Informed* en temps réel par le handoff packet.
- **Veto Aquaman sur l'opportunité commerciale.** Aquaman **ne tranche pas**
  l'opportunité commerciale (deal bon ou mauvais pour l'entreprise) ; il
  tranche la **conformité du livrable**. Confondre les deux transforme
  Aquaman en CMO-bis. La séparation est explicite dans le RACI : A = Sales,
  C = Aquaman.
- **T-2j insuffisant pour Classe 2.** Un deal non-template qui passe par
  le handoff T-2j est probablement déjà signé avant le retour Aquaman.
  La mitigation : la Classe 2 **exige** T-7j, jamais T-2j. Si Sales
  presse, c'est un arbitrage B2 Council (Sales peut-il se passer de
  T-7j pour ce deal ? — la réponse canonique est non).
- **Aquaman ACTIVE absent.** Si Aquaman est en Dormant ou SHADOW_ACTIVE
  (cf. [[aquaman-dormant-activation]]), la validation Classe 2 doit
  escalader B1 pour activation — ou le deal **ne se fait pas** jusqu'à
  activation Aquaman. C'est l'application directe du triplet 36 : *« Legal
  & Compliance ne s'active qu'au premier fichier déposé dans
  00_Summers_CEO/03_Master_Agreements/ »*.
- **Self-serve sans revue périodique.** Un template Classe 3 qui n'a pas
  été revu depuis 6 mois peut être obsolète sans qu'Aquaman le sache.
  La mitigation : revue de tous les templates **une fois par sprint**, pas
  par deal.

## Liens

- [[aquaman-couplages-invisibles]] §Couplage 4 — la surface Aquaman ↔
  JohnJones qui motive le #11
- [[aquaman-veto-engagement-sans-perimetre]] — le veto canonique Aquaman
  qui sous-tend les Classes 1, 2, 3
- [[aquaman-launch-ready-portique-final]] — le portique Aquaman T-7j qui
  fait écho au handoff Classe 2 T-7j
- [[aquaman-classification-risques-4-formes]] §Classe 4 — la classe
  contract/limite de périmètre qui sous-tend les 3 classes de deals
- [[aquaman-jtbd-emit-receive]] §Forme 3 — les templates qui sous-tendent
  Classe 1 et 3
- [[aquaman-pair-check-10-legal-risk-launch]] — le pair-check #10 sur le
  launch, distinct du #11 sur le deal
- [[b2-pair-check-raci-by-rank]] §Le cas People → Tous — par symétrie, le
  #11 reste transverse (Aquaman C, jamais A)
- [[b2-harmonization-matrix-exploitable]] §Trois modes — le mode
  `negotiation` qui tranche Classe 2 en cas de désaccord
- [[eight-domain-avengers-wheel]] §Note sur la nomenclature Sales — la
  migration JohnJones / Martian Manhunter qui impacte le handoff packet

## Note de confiance

**Reconstruit, projeté depuis un trou explicitement posé.** Le besoin est
**confirmé verbatim** par [[rapport-tour-1]] §4.4. La procédure de
pair-check #11 est **projetée** par application des principes du
[[b2-pair-check-raci-by-rank]] (A = aval, C = émetteur de veto, R = squad
B3) — c'est une **généralisation** d'une matrice qui a 9 entrées, pas 10.
Les 3 classes de deals sont **projetées** depuis la pratique courante des
templates / non-templates / self-serve — pas observées en cycle. Le
format YAML du handoff packet est **empiré** de [[b2-b3-jtbd-handoff-contract]]
§Le format conjoint et de [[aquaman-classification-risques-4-formes]]
§Routage B3 — c'est une **combinaison** de deux sources canoniques.
**À vérifier en cycle** : (1) JohnJones accepte-t-il la Classe 2 T-7j ou
veut-il compresser ?, (2) Aquaman a-t-il la bande passante pour la revue
self-serve par sprint ?, (3) le pair-check #11 doit-il rester Consulted
(Aquaman C) ou passer Accountable pour les Classes 2 (non-template) ?
