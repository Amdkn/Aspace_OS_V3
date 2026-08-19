---
type: Concept
title: Domaine Finance — couplages amont/aval vers les 7 autres domaines
description: Le domaine Finance (Wonder Woman) est le C des pair-checks #5 (Finance→Growth) et #6 (Finance→Product). En aval, Finance reçoit : deal value (Sales), CAC brut (Growth), compute cost (IT), delivery cost (Ops). En amont, Finance alimente : payback/cac (Growth), marge / coût build (Product), impact billing (Legal via CGV), runway/cashfloor (People via capacity). Les couplages les plus serrés sont avec Growth (CAC partagé) et IT (compute Sovereignty, F24). Le couplage People→Finance va dans les deux sens (rotation d'un owner financier ne doit pas dégrader la cadence).
tags: [b2, finance, couplage, pair-check, dependance, wonder-woman, raci]
generated: { by: minimax-m3, at: 2026-08-19T03:46:00Z }
verified:
  - { by: process:lecture-domaine-finance-corpus, at: 2026-08-19T03:46:00Z }
sources:
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: harmonization-matrix
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable
    last_modified: 2026-08-19
  - id: finance-principles
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/03_WONDERWOMAN_FINANCE_PRINCIPLES.md"
    title: Wonder Woman Finance Principles (v4)
    last_modified: 2026-06-25
  - id: omk-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: OMK Finance — B2 Domain Control Room
    last_modified: 2026-05-25
  - id: meso-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — le format canonique d'une décision B2
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Domaine Finance — couplages amont/aval vers les 7 autres domaines

## Le principe de couplage

La matrice d'harmonisation pose **9 pair-checks** entre domaines.
Pour le domaine Finance, **deux d'entre eux** le concernent
directement (#5 Finance→Growth, #6 Finance→Product) — Wonder
Woman y est **Consulted**, pas Accountable. Mais le couplage
réel dépasse ces deux pair-checks : Finance interagit avec les 7
autres domaines, soit par les pair-checks où elle apparaît en I
(Informed), soit par des dépendances opérationnelles hors matrice.

Le couplage est qualifié par **direction** :

- **Couplage amont** = un autre domaine produit une donnée ou une
  décision dont Finance a besoin pour opérer.
- **Couplage aval** = Finance produit une donnée ou un arbitrage
  dont un autre domaine a besoin pour opérer.
- **Couplage bilatéral** = les deux domaines dépendent l'un de
  l'autre dans les deux sens.

## Tableau des couplages

| # | Couplage | Direction | Intensité | Source canonique |
|---|---|---|---|---|
| 1 | Finance ↔ Growth | Bilatéral | Fort (pair-check #5, CAC payback partagé) | `b2-pair-check-raci-by-rank.md` ligne 5 + F6 |
| 2 | Finance ↔ Product | Bilatéral | Fort (pair-check #6, blocking authority) | `00_B2_DOMAIN_CONTROL_ROOM.md` §« Blocking Authority » + F4 |
| 3 | Finance ← Sales | Amont seul | Moyen (deal value → MRR) | ADR-MESH-L2-001 + pair-check implicite |
| 4 | Finance ← IT | Amont seul | Fort (compute cost → sovereignty F24) | F24 + IT P13 |
| 5 | Finance ← Ops | Amont seul | Moyen (delivery cost → marge brute) | F4 + ADR-MESH-L2-001 |
| 6 | Finance → Legal | Aval | Moyen (billing path → CGV) | Aquaman veto §08 + F10 |
| 7 | Finance ↔ People | Bilatéral (rotation) | Faible | `eight-domain-avengers-wheel.md` §« coordinateur transverse » |

Lecture : les deux couplages bilatéraux forts sont avec **Growth
(1)** et **Product (2)**. Trois couplages amont seul avec
**Sales (3)**, **IT (4)**, **Ops (5)**. Un couplage aval avec
**Legal (6)**. Un couplage bilatéral faible avec **People (7)**
sur la rotation du captain Finance.

## Couplage #1 — Finance ↔ Growth (le plus serré)

### Amont (Growth → Finance)

- **Source** : Growth fournit le **CAC brut** (Coût d'Acquisition
  Client), la dépense paid media, et les volumes de MQL → SQL.
- **Canal** : Airtable `Finance_Pulse` lit la donnée source depuis
  `Growth_*` (ADR-MESH-L2-001 — un datum, un owner).
- **Cadence** : Mensuelle pour la consolidation, quotidienne pour
  les dashboards Pulse.

### Aval (Finance → Growth)

- **Sortie** : Wonder Woman calcule le **CAC payback** (F6) et le
  communique à Superman. Le payback est un **KR partagé** :
  « Shared owner with Growth KR-4b » (`03_WONDERWOMAN_FINANCE_PRINCIPLES.md`
  §« Cluster B — F6 »).
- **Format** : Métrique chiffrée (mois pour récupérer le CAC),
  livrée dans le Pulse hebdo avec seuil d'alerte.
- **Décision qui en sort** : Growth arbitre la continuation ou
  l'arrêt de la dépense paid media selon le payback remonté par
  Finance. Pair-check #5 dans la matrice : « La dépense est-elle
  justifiée par l'apprentissage ou la traction ? »

### Le RACI canonique

`b2-pair-check-raci-by-rank.md` ligne 5 :

- A = B2 Growth (Superman)
- R = B3 Guardians
- C = B2 Finance (Wonder Woman)
- I = B1, B3 Thunderbolts

Wonder Woman est **Consulted** : elle dit si la dépense est
défendable, **Superman tranche**. Cela signifie concrètement que
Wonder Woman peut bloquer une métrique de payback trop optimiste
(motif vérifiable : « la métrique livrée est X, le payback réel
calculé est Y »), mais elle **ne peut pas** bloquer une décision
de continuer le paid media si Superman en prend la responsabilité.

### Le couplage symétrique sur F22 (Heavy-asset moat)

Quand Finance arbitre le reinvestissement (F19-F22), elle peut
recommander à Growth de pivoter vers une chaîne de valeur plus
lourde (asset-backed). C'est un couplage aval qui ne passe pas
par le pair-check #5 mais qui existe en doctrine.

## Couplage #2 — Finance ↔ Product (le blocker)

### Amont (Product → Finance)

- **Source** : Product fournit la **scope** d'une feature
  (utilisation attendue, coûts de build, support burden).
- **Canal** : Le control room OMK exige ces inputs en ouverture
  de sprint : « Requires Product to state feature scope, expected
  usage, provider costs, and support burden assumptions. »
  (`00_B2_DOMAIN_CONTROL_ROOM.md` §« Required Input From Product »).

### Aval (Finance → Product)

- **Sortie** : Wonder Woman calcule la **marge brute** réelle (F4,
  après Hostinger + LLM API + Stripe fees) et évalue la
  **marge nette** après coûts de delivery. Si la marge est
  négative, **bloque le produit** (control room §« Blocking Authority » :
  « Blocks Product when it creates hidden recurring cost, unclear
  pricing, or margin-negative delivery »).
- **Format** : Build gate Finance — le produit ne peut pas
  « graduate » sans passer le gate. C'est un blocage hard, pas
  un veto catalogue — voir [[wonder-woman-pair-check-consulted-role]].

### Le RACI canonique

`b2-pair-check-raci-by-rank.md` ligne 6 :

- A = B2 Product (Flash)
- R = B3 Avengers
- C = B2 Finance (Wonder Woman)
- I = B1, B3 Thunderbolts

Même RACI que #5 (Wonder Woman en C), **mais** Wonder Woman a un
droit de blocage B2 hard si la marge est négative. L'asymétrie est
notable : sur #6 le pair-check attribue A à Product, mais le
control room donne à Wonder Woman un **veto effectif**. Cela
vient du fait que la matrice pair-check teste la transition
(compatible avec A = Product), tandis que le control room Finance
teste la viabilité financière (le gate peut bloquer indépendamment).

### Le couplage symétrique sur F23 (Pricing)

Wonder Woman arbitre **le pricing**, qui est aussi un input
Produit (le pricing hook d'une feature est souvent porté par le
produit). Quand F23 (« setup + retainer ») est en jeu, Flash et
Wonder Woman négocient ensemble la structure de prix ; Flash porte
le « prix comme signal de positionnement », Wonder Woman porte le
« prix comme solvabilité ».

## Couplage #3 — Finance ← Sales (amont seul)

- **Source** : Sales (JohnJones) fournit le **deal value** signé
  (ACV, TCV, conditions de paiement).
- **Canal** : Reconnaissance en MRR par Finance. Pas de pair-check
  canonique Sales → Finance dans la matrice (qui teste surtout
  Sales → Ops, ligne 2).
- **Cadence** : À la signature d'un deal (temps réel) +
  consolidation mensuelle.
- **Décision qui en sort** : Finance reconnaîtdes MRR forecasts
  (F2 « Forecast pessimistically »), pas des promesses. Le
  forecast est **pessimiste par principe** (Yelena Belova).
- **Couplage aval** : Faible. Finance remontant à Sales le CAC
  payback et la capacité de financer des deals plus agressifs
  (par le surplus floor F19). Pas de pair-check structuré.

### Le veto Aquaman en amont

Le deal Sales a besoin d'un accord écrit sur le périmètre (Aquaman
veto §08). Sans accord écrit, **Wonder Woman ne peut pas
facturer** — c'est un blocker Aquaman qui se transmet à Finance.

## Couplage #4 — Finance ← IT (amont seul, fort)

- **Source** : IT (Cyborg) fournit le **compute cost** : LLM API,
  Hostinger, Vercel, Supabase, etc. (cf. stack ancrée
  `03_WONDERWOMAN_FINANCE_PRINCIPLES.md` §« Mesh anchoring »).
- **Canal** : Factures fournisseurs remontées dans `Finance_Pulse`
  (un datum, un owner — IT tient le coût brut).
- **Cadence** : Mensuelle (factures) + continue (avec F24).

### Le couplage F24 — Sovereign-infra arbitrage

Le principe **F24** (« Sovereign-infra arbitrage drives net margin
toward 90%+ ») est **un couplage bilatéral déguisé en amont seul** :

- IT (Cyborg) tient la souveraineté (veto §07 « Bloque tout
  fournisseur cloud-only sans chemin de sortie documenté »).
- Finance (Wonder Woman) calcule la marge nette qui résulte.
- Quand la marge se dégrade à cause d'un fournisseur SaaS
  tiers, **Wonder Woman demande** la migration vers infra
  souveraine (self-hosted n8n, local vector DB, OpenRouter
  gateway). C'est une décision conjointe B2, pas un arbitrage
  unilatéral.

### Le couplage F22 — Heavy-asset moat

F22 (« Heavy-asset moat over thin wrappers ») est l'endroit où
Finance et IT convergent sur la même doctrine : « When software
cost → 0, a thin AI wrapper has no moat. Prefer Halo businesses. »
Ce couplage se voit dans le pair-check #4 (Product → IT) où
Wonder Woman n'apparaît pas en RACI, mais sa doctrine F22
s'applique aux décisions IT.

## Couplage #5 — Finance ← Ops (amont seul, moyen)

- **Source** : Ops (Batman) fournit le **delivery cost** : support,
  onboarding, customer success.
- **Canal** : Consolidation en marge brute par Finance.
- **Cadence** : Mensuelle.
- **Couplage aval** : Faible. Finance remontant à Ops la capacité
  de delivery chiffrée (par les KRs runway). Pas de pair-check
  structuré.

### Le lien indirect via le red flag #3

Le red flag matrice #3 (« Sales green, Ops/People red — risque de
charge de livraison ») n'inclut pas Finance directement, mais le
principe F4 (« real net margin, never gross theatre ») **est** la
conséquence Finance d'un Ops red. Si Ops est saturé, le delivery
cost explose, la marge nette fond — Wonder Woman déclenche un
pair-check #6 renforcée sur Product.

## Couplage #6 — Finance → Legal (aval, moyen)

- **Sortie** : Finance produit le **billing path** et fournit à
  Aquaman les inputs pour les **CGV** (pricing, modalités de
  paiement, conditions de remboursement).
- **Canal** : Pas de pair-check canonique. Le veto Aquaman §08
  (« Bloque toute prestation démarrée sans accord écrit sur le
  périmètre et la propriété du livrable ») bloque en amont de
  Finance.
- **Cadence** : À chaque nouvelle offre ou changement de pricing.
- **Couplage amont** : Faible. Legal remontant à Finance les
  contraintes réglementaires fiscales qui affectent F10.

### Le cas spécifique du pricing

Le pricing >15% discount requiert Wonder Woman sign-off. Cela
signifie qu'une décision Sales/Illuminati de discount peut
déclencher une consultation Aquaman sur les CGV — c'est un
couplage triangulaire Sales-Finance-Legal qui n'est pas posé
comme tel dans une seule source.

## Couplage #7 — Finance ↔ People (bilatéral, faible)

- **Amont** : People (Green Lantern) tient la **charge** sur les
  owners Finance (Bucky, Yelena, etc.). Si People ne peut pas
  fournir un owner stable, la cadence de réconciliation
  mensuelle saute.
- **Aval** : Finance remontant à People la **capacité** de
  financer de nouveaux owners (chaque owner B3 a un coût).
- **Couplage** : Très indirect. Pas dans les pair-checks. Le
  coordinateur transverse (People) consulte Finance sur la
  capacité, mais la décision reste chez People.

## Le couplage manquant — Finance ↔ Growth × Product

Le **double couplage** Finance↔Growth ET Finance↔Product crée un
**couplage triangulaire** (Growth-Finance-Product) qui n'est pas
posé dans la matrice canonique. Il émerge quand :

- Growth demande une dépense pub pour un produit nouveau →
  Pair-check #5 (Finance est C sur « la dépense est-elle justifiée
  par l'apprentissage ? »).
- Product lance le produit avec coût caché → Pair-check #6
  (Finance est C sur « le coût de build protège-t-il la marge ? »).
- Growth et Product sont alignés sur le launch, **Finance
  n'arbitre pas** (Wonder Woman est C sur les deux pair-checks),
  mais son **droit de blocage hard** sur la marge négative peut
  torpiller le lancement après le pair-check.

Le **red flag #4** (« Finance red + Growth/Product green —
Ralentir ou re-pricer. Le cash ne suit pas. ») est précisément le
mécanisme qui protège contre ce piège. Voir
[[wonder-woman-red-flag-4-trigger]].

## Anti-pièges couplage

- **Traiter les 7 couplages comme symétriques**. Ils ne le sont
  pas. Growth et Product sont les couplages forts. People est
  faible. Voir l'intensité dans le tableau ci-dessus.
- **Confondre dépendance opérationnelle et dépendance pair-check**.
  Finance a 2 dépendances pair-check (#5 et #6) mais 7
  dépendances opérationnelles. Les 5 supplémentaires (Sales, IT,
  Ops, Legal, People) sont **aussi** des blocages potentiels, gérés
  par les ADR-MESH et les vetos, pas par la matrice d'harmonisation.
- **Ignorer les couplages en C**. Wonder Woman est Consulted, pas
  Accountable. C'est une position **faible dans la wheel** mais
  **forte en doctrine** (truth in numbers). Un capitaine qui lit le
  RACI peut croire qu'il n'a pas besoin de Wonder Woman pour
  décider — c'est faux sur les dépenses à blocker.

## Liens

- [[wonder-woman-finance-frontiers]] — le périmètre détaillé
- [[wonder-woman-pair-check-consulted-role]] — pourquoi C, pas A
- [[wonder-woman-red-flag-4-trigger]] — quand les deux pair-checks
  Courts-circuitent Superman/Flash
- [[b2-pair-check-raci-by-rank]] — la matrice RACI source
- [[b2-harmonization-matrix-exploitable]] — la matrice d'harmonisation

## Note de confiance

**Confirmé par machine.** Les 2 pair-checks (#5, #6) sont posés
verbatim dans `b2-pair-check-raci-by-rank.md`. Les couplages avec
Sales, IT, Ops, Legal sont **reconstruits** à partir des sources
ADR-MESH-L2-001, F4, F22, F24 et du veto Aquaman §08. Le
couplage triangulaire Growth×Finance×Product est **projeté** — il
n'est pas posé comme tel dans le corpus. Le couplage People est
**projeté** à partir du rôle transverse de People
(`eight-domain-avengers-wheel.md` §« coordinateur transverse »).
Les 7 anti-pièges sont des extrapolations depuis les doctrines
Finances (F4-F22).
