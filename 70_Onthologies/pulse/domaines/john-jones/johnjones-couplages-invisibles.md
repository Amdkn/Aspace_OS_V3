---
type: Concept
title: JohnJones — couplages invisibles avec Product, Finance, Legal (hors matrice 9 pair-checks)
description: La matrice d'harmonisation pose 9 pair-checks canoniques, mais JohnJones a 3 couplages cross-domaine hors matrice : Product→Sales pour la forme de la promesse, Finance→Sales pour prix/marge, Legal→Sales pour terms/claims. Ces couplages sont documentés dans SPRINTS.md mais pas dans la matrice canonique. Ils révèlent une limite de la matrice 9-pair-checks.
tags: [b2, johnjones, sales, couplages, invisibles, matrice, produit, finance, legal, hors-piste]
generated: { by: minimax-m3, at: 2026-08-19T04:20:00Z }
verified:
  - { by: process:lecture-corpus-sales, at: 2026-08-19T04:20:00Z }
sources:
  - id: sprints-sales
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/04_Business_Domains/04_Sales_et_Cognition_MartianManhunter_Illuminati/SPRINTS.md"
    title: SPRINTS — Pourquoi BlackBolt/Namor pas dans le tableau, lien reformulation-offre
    last_modified: 2026-08-02
  - id: harmonization-exploitable
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable (9 critères)
    last_modified: 2026-08-19
  - id: aquaman-couplages
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-couplages-invisibles.md"
    title: Aquaman — couplages invisibles (analogue pour Legal)
    last_modified: 2026-08-19
okf_version: "0.2"
---

# JohnJones — couplages invisibles

## Pourquoi cette notion existe

La matrice d'harmonisation pose 9 pair-checks canoniques
(`b2-harmonization-matrix-exploitable.md` §« Les 9 critères — forme
tabulaire »). Mais l'expérience d'un arbitrage B2 Council montre
que des couplages **transverses** apparaissent, qui ne sont ni
directement amont-aval ni dans la matrice. Le concept analogue pour
Legal (Aquaman) est documenté dans
`aquaman-couplages-invisibles.md`. Pour Sales, ces couplages sont
**3** et ils sont critiques : Sales dépend de Product, Finance, et
Legal pour pouvoir promettre — sans eux, la reformulation validée
reste une vue de l'esprit.

## Couplage #1 — Product → Sales (forme de la promesse)

**Sens** : Flash (Product, B2 captain, domaine 03) doit avoir
formalisé une promesse reproductible avant que JohnJones puisse
relier la reformulation validée à une offre.

**Source verbatim** (`SPRINTS.md` §« Pourquoi BlackBolt et Namor ne
sont pas dans le tableau ») :

> *« BlackBolt et Namor entreront en jeu lorsque le domaine 6
> (Finance & ROI) aura prix et marge, et que le domaine 3
> (Productization) aura une promesse reproductible. »*

Et Sprint 4 §« Résultat vérifiable le vendredi » :

> *« table à 2 colonnes (problème reformulé validé · promesse de
> l'offre Coach OS citée) avec ≥ 3 lignes, et la phrase d'ouverture
> de la promesse de l'offre citée mot pour mot depuis l'artefact du
> domaine 3. »*

**Mécanique** : Sales doit citer la promesse Coach OS **mot pour
mot** dans son `LINK_TO_OFFER.md`. Si Product (Flash) n'a pas
produit cette phrase d'ouverture (par exemple, parce que Coach OS
n'a pas encore de produit reproductible), Sales ne peut pas tenir
Sprint 4 — le critère DoD est invérifiable.

**Pourquoi hors matrice 9** : la matrice pose un pair-check #6
(Finance → Product — *« Le coût de build protège-t-il la marge ? »*),
mais pas de pair-check Product → Sales. Le couplage est implicite :
Product stabilise la promesse, Sales la cite.

**Qui dépend de qui** :

- Sales **dépend** de Product (sans promesse reproductible, pas de
  reformulation-validée-liée-offre).
- Product **dépend faiblement** de Sales (la promesse est définie
  sans input commercial, mais Flash consulte JohnJones sur ce qui
  esttenable en discovery).

**Couplage réciproque latent** : Product consulte JohnJones pour
calibrer ce qui est promettable. C'est un couplage **faible mais
nécessaire** — sans input commercial, Product risque de promettre
ce que Sales ne peut pas tenir.

**Failure mode projeté** : Product livre une promesse que Sales ne
peut pas tenir en discovery → le client signe sur une promesse
invendable → Ops ne peut pas la livrer → red flag #3 (Sales green,
Ops red) en cascade.

## Couplage #2 — Finance → Sales (prix, marge, structure)

**Sens** : Wonder Woman (Finance, B2 captain, domaine 06) doit
avoir calibré prix et marge avant que JohnJones puisse activer
Closer (BlackBolt) et Negotiation (Namor).

**Source verbatim** (`SPRINTS.md` §« Pourquoi BlackBolt et Namor ne
sont pas dans le tableau ») :

> *« BlackBolt et Namor entreront en jeu lorsque le domaine 6
> (Finance & ROI) aura prix et marge. »*

**Mécanique** : Closer et Negotiation ont besoin d'un plancher
(Namor) et d'une valeur de signature (BlackBolt). Sans prix et
marge calibrés par Finance, le commercial ne peut pas défendre un
plancher ni calculer une remise.

**Pourquoi hors matrice 9** : la matrice pose un pair-check #5
(Finance → Growth — *« La dépense est-elle justifiée par
l'apprentissage ou la traction ? »*) mais pas de pair-check Finance
→ Sales. Le couplage est implicite : Finance calibre le prix, Sales
le pratique.

**Qui dépend de qui** :

- Sales **dépend** fortement de Finance (sans prix, pas de closer ;
  sans marge, pas de plancher).
- Finance **dépend faiblement** de Sales (Finance calibre sans input
  commercial direct, mais peut consulter JohnJones sur la résistance
  du marché à un prix).

**Couplage réciproque latent** : Finance consulte JohnJones pour
calibrer la résistance prix du segment ciblé. C'est un couplage
**fort mais asynchrone** — Finance calibre une fois par cycle,
Sales pratique quotidiennement.

**Failure mode projeté** : Sales signe à un prix non calibré par
Finance → la marge s'effondre → red flag #4 (Finance red +
Growth/Product green —) au cycle suivant. Wonder Woman oppose le
veto dépense récurrente (autre veto) en aval.

## Couplage #3 — Legal → Sales (terms, claims, périmètre contractuel)

**Sens** : Aquaman (Legal, B2 captain, domaine 08) doit avoir cadré
les terms-of-use et les claims safe avant que JohnJones puisse
envoyer une proposition engageante.

**Source** : aucun triplet canonique ne pose explicitement ce
couplage, mais la pratique documentée le suggère. Aquaman oppose
son veto catalogue *« engagement-sans-périmètre »* (cf.
`aquaman-veto-engagement-sans-perimetre.md`) — ce veto s'applique
à toute prestation démarrée sans accord écrit sur le périmètre et
la propriété du livrable. Une proposition commerciale
Sales **est** un engagement, au sens où elle prend acte d'un
problème reformulé.

**Mécanique** : Sales envoie une proposition → Aquaman oppose le veto
si la proposition engage sur un périmètre non cadré. Sans terms
safe, Sales peut promettre des claims qui engagent la
responsabilité de l'organisation.

**Pourquoi hors matrice 9** : la matrice pose deux pair-checks
Legal (#7 Legal → Growth, #8 Legal → Product), mais pas de pair-check
Legal → Sales. Le couplage est implicite : Legal cadre, Sales
engage.

**Qui dépend de qui** :

- Sales **dépend** de Legal (sans terms safe, Aquaman oppose le veto
  en aval, la proposition est caduque).
- Legal **dépend très faiblement** de Sales (Legal cadre sans input
  commercial direct).

**Couplage réciproque latent** : Legal consulte marginalement
JohnJones pour vérifier qu'une claim proposée par Growth est
commercialement tenable. C'est un couplage **faible et rare**.

**Failure mode projeté** : Sales pousse une propale avec une claim
non safe (par exemple, *« ROI en 30 jours »* non documenté) →
Aquaman oppose le veto engagement-sans-périmètre → la propale est
gelée, le client attend, le commercial perd la confiance.

## Le tableau des 3 couplages invisibles de Sales

| Couplage | Source verbatim | Dépendance Sales | Dépendance inverse | Failure mode projeté |
|---|---|---|---|---|
| Product → Sales | `SPRINTS.md` Sprint 4 + §Pourquoi BlackBolt/Namor | Forte (Sprint 4 impossible sans phrase d'ouverture) | Faible (consultatif) | Promesse invendable signée → Ops ne livre pas → red flag #3 |
| Finance → Sales | `SPRINTS.md` §Pourquoi BlackBolt/Namor | Forte (Closer/Negotiation inactifs sans prix) | Forte-asynchrone (calibrage résistance marché) | Marge effondrée → red flag #4 au cycle suivant |
| Legal → Sales | Pratique documentée (veto Aquaman aval) | Forte (veto engagement-sans-périmètre) | Très faible (claims safe) | Propale gelée par veto, client perd confiance |

**Trois couplages forts depuis Sales vers trois domaines amont**
(Product, Finance, Legal). Sales est **en position de dépendance
multiple** : sans la stabilisation de ses voisins, Sales ne peut
pas promettre. Le SPRINT 2026-08 montre un cas où Sales **travaille
**explicitement sans Finance (Closer/Negotiation désactivés) et sans
Legal (terms à cadrer plus tard), mais avec Product (Sprint 4 cite
la phrase d'ouverture).

## Limite de la matrice 9 pair-checks

La matrice 9 pair-checks est **nécessaire mais non suffisante**.
Trois constatations :

1. **Elle teste 9 transitions directes**, mais les couplages
   indirects (Product → Sales, Finance → Sales, Legal → Sales)
   échappent à son scan.
2. **L'amplification du veto catalogue** (cf.
   `b2-veto-amplification-cycle.md`) peut créer de nouveaux
   couplages : par exemple, si Wonder Woman étend son veto-dépense
   pour inclure *« Sales ne signe pas à un prix non calibré »*, le
   couplage Finance → Sales devient **explicite et bloquant**.
3. **L'escalade Council** (cf. `b2-council-arbitrage-rule.md`)
   reçoit des cas où le red flag matrice #2 (Growth green, Sales
   red) s'oppose mais où la cause est un couplage hors matrice
   (par exemple, Product n'a pas stabilisé la promesse). Le Council
   tranche, mais le packet ne marque pas la dépendance hors matrice.

**Conséquence opérationnelle** : un audit mésoperpétuel qui
n'examine que les 9 pair-checks manque **3 couplages critiques** de
Sales. Une proposition pour résoudre cette limite : étendre la
matrice à 12 pair-checks (ajout des 3 couplages Sales), mais cette
extension **n'est pas soumise au Council** dans le corpus visible.

## Anti-pièges

- **Activer Closer/Negotiation sans prix calibré.** C'est le failure
  mode #2 — Sales signe à un prix invendable, Finance s'effondre.
- **Faire Sprint 4 sans phrase d'ouverture Product.** C'est le
  failure mode #1 — Sales cite une promesse qui n'existe pas, le
  lien reformulation-offre est fictif.
- **Envoyer une propale sans terms safe.** C'est le failure mode #3 —
  Aquaman oppose son veto en aval, la propale est gelée.
- **Considérer les 9 pair-checks comme exhaustifs.** L'audit
  mésoperpétuel qui s'arrête aux 9 rate les couplages critiques. Une
 评审 honnête inclut les 3 couplages Sales (et probablement
  d'autres, par exemple Batman ↔ People sur les charges).

## Liens

- [[b2-harmonization-matrix-exploitable]] — les 9 pair-checks canoniques
- [[b2-council-arbitrage-rule]] — qui escalade quand un couplage
  hors matrice est en cause
- [[b2-veto-amplification-cycle]] — extension de veto qui peut
  expliciter un couplage
- [[johnjones-domaine-sales-perimetre]] — le périmètre Sales qui
  subit les couplages
- [[johnjones-jtbd-emit-receive]] — JTBD émis/reçus incluant ces
  couplages
- [[aquaman-couplages-invisibles]] — analogue pour Legal

## Note de confiance

**Confirmé par machine, à moitié.** Les 3 couplages sont **projetés**
depuis la pratique documentée dans `SPRINTS.md` (couplages Product
et Finance) et depuis la doctrine Aquaman (couplage Legal). Les
sources verbatim existent pour 2 couplages (Product, Finance) ; le
couplage Legal est inféré depuis le veto Aquaman aval. La
distribution des dépendances (forte/faible) est **projetée** depuis
le rôle de chaque domaine, pas étayée par des triplets canoniques.
La proposition d'étendre la matrice à 12 pair-checks est
**explicitement non soumise** — notée ici comme candidate.