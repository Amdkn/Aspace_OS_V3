---
type: Concept
title: B1 stop conditions et escalier d'escalade
description: Trois stop conditions durs (pas de B2 sans mandat handoff queue, pas de B3 sans DoD/JTBD, pas de release Business Done sans passer la matrice B2) + l'escalier canonique B3->B2->B1->gatekeepers->A0, sans saut d'echelon.
tags: [b1, stop-condition, escalade, gatekeeper, amadeus, doctrine]
generated: { by: minimax-m3, at: 2026-08-19T01:35:00Z }
verified:
  - { by: process:lecture-fractal-b1b2b3, at: 2026-08-19T01:35:00Z }
  - { by: process:synthese-pulse-b1-tour-1, at: 2026-08-19T01:35:00Z }
sources:
  - id: fractal-arch
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md"
    title: L2 Business — The B1 / B2 / B3 Fractal Architecture
    last_modified: 2026-06-02
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md"
    title: B2 Business Wheel Harmonization Matrix
    last_modified: 2026-05-27
okf_version: "0.2"
---

# B1 stop conditions et escalier d'escalade

B1 tient trois **stop conditions durs** et un **escalier d'escalade** canonique. Les deux jouent le role de **garde-fou structurel** : ils n'ont pas besoin d'etre appliques par un humain pour tenir — ils tiennent par la grille.

## Les trois stop conditions durs

### Stop 1 — Pas de travail B2 sans un item dans la handoff queue B1

Tout travail B2 doit tracer jusqu'a un mandat B1 logue. Sans mandat, le B2 travaille *« a titre exploratoire »* — c'est un anti-pattern.

**Consequence si viole** : le travail B2 n'est pas couverte par la gouvernance B1. Si le travail echoue, B1 ne peut pas corriger la source — il doit assumer en arriere. Et le B2 suivant, qui voit son captain travailler sans mandat, perd la discipline de la handoff queue.

**Detection** : B1 scanne `04_B2_HANDOFF_QUEUE.md` a chaque rollover de 12WY. Tout Rock B2 actif sans mandat en amont est remonte comme *« dette de gouvernance »*.

### Stop 2 — Pas de travail B3 sans une source DoD ou JTBD de B2

Tout JTBD execute par B3 doit pointer vers un DoD packet B2 ou un JTBD packet B2. B3 n'agit pas sur intuition, meme si la tache parait evidente.

**Consequence si viole** : la preuve renduepar B3 n'est pas comparable a un DoD. Le B2 owner ne peut pas valider ou refuser. La boucle de verification est cassee a la source.

**Detection** : B2 scanne ses JTBD packs a chaque sprint. Tout JTBD execute sans DoD/JTBD parent est `BLOCKED_DELIVERY` et le travail est gele.

### Stop 3 — Pas de release « Product-only » comme « Business Done »

Une feature livree par Product ne devient pas **Business Done** tant qu'elle n'a pas passe la matrice B2 (les 9 pair checks + les 5 red flags). Le *« shipped is not done »*.

**Consequence si viole** : la wheel 8-domain affiche un Produit vert sans que Ops / Legal / People aient valide. C'est exactement le cas que la matrice d'harmonisation detecte — voir [[b2-business-wheel-harmonization-matrix]].

**Detection** : B2 Council refuse le label *« Business Done »* tant que les 9 pair checks n'ont pas ete valides. B1 n'a pas besoin d'intervenir — le Council tient le stop.

## L'escalier canonique

Cinq echelons, en ordre strict. **On ne saute jamais un echelon**, sauf emergency triggers explicites (voir section suivante).

```
B3 (peer-unblock d'abord)
  --> B2 owner du domaine
    --> B1 (Jerry ou Summer)
      --> B1 gatekeepers (Rick, Morty)
        --> A0 Amadeus
```

### Etape 1 — B3 peer-unblock d'abord

Un B3 qui bloque sur un autre B3 ne remonte pas tout de suite. Il tente d'abord le peer-unblock : *« qu'est-ce que je peux faire pour desamorcer, avant d'embeter le captain ? »*. Le Ownerbook T1 cite ce pattern : les squads Marvel s'entraident en interne avant d'escalader.

### Etape 2 — B2 owner

Si le peer-unblock echoue, l'agent B3 remonte au B2 owner du domaine. Le captain arbitre dans son domaine, sans impliquer B1.

### Etape 3 — B1 (Jerry ou Summer)

Le B2 owner remonte a B1 quand :
- le blocage touche plusieurs domaines (cross-domaine) ;
- le B2 owner ne peut pas tenir son DoD sans modifier le mandat B1 ;
- la wheel 8-domain est menacee.

B1 tranche dans le cadre du North Star et du 12WY courant. Il peut refrormuler un mandat, geler un mandat, ou remonter aux gatekeepers.

### Etape 4 — B1 gatekeepers (Rick, Morty)

Les gatekeepers arbitrent ce qui touche les **doctrines verrouillees** : D4 (append-only), D6 (no-self-contradiction), Spec-Loop, etc. Si B1 veut modifier une doctrine, il passe par les gatekeepers.

### Etape 5 — A0 Amadeus

L'autorite globale de l'OS. A0 tranche quand :
- le North Star est en jeu ;
- la structure (Areas vs Projects, rangs A vs B) est en jeu ;
- une doctrine verrouillee est menacee par une autre doctrine verrouillee.

## Emergency triggers (exception au non-saut)

Trois cas ou l'escalier peut sauter un echelon :

1. **Securite / legal critique.** Une fuite de donnees, une mise en public non-autorisee, un risque legal immediat. A0 direct.
2. **Doctrine verrouillee violee.** Quelqu'un a modifie un canon append-only ou a contredit une doctrine D4/D6. Gatekeepers direct.
3. **Systeme tombe.** L'infrastructure ne repond plus (Paperclip plafonne a 2-3 agents — *« fork: Resource temporarily unavailable »* deja observe 2026-08-02). A0 direct.

**En dehors de ces trois cas, le saut d'echelon est un anti-pattern** : il court-circuite la discipline et Cree une dette d'autorite.

## Anti-pieges

- **B3 qui appelle A0 directement.** Sauf emergency trigger, c'est un saut de 4 echelons. Le B3 doit passer par B2 owner. Si le B2 owner est indisponible, c'est au B2 de designer un remplacant — pas au B3 de court-circuiter.
- **B1 qui re-derive la doctrine dans un arbitrage.** Stop 1 et Stop 2 sont des consequenses directes de la doctrine fractale (Area perpetuelle vs Project calibre). Si B1 les modifie dans un arbitrage, il casse le DRY du fractal.
- **B2 qui demande a B1 d'arbitrer ce que le Council peut trancher.** Stop 3 depend du Conseil comme instance d'arbitrage. Si B1 accepte d'arbitrer ce que le Conseil peut traiter, le Conseil se met en sommeil.

## Sources

- `00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §« Les stop conditions (durs) » et §« L'escalier d'escalade (canonique) » — source verbatim.
- `B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md` §« Le B2 Council comme instance d'arbitrage » — la place du Conseil entre B2 et B1.

## Liens

- [[b1-decision-rights-frontieres]] — la frontiere d'autorite que les stops protègent
- [[b1-mandate-packet-spec]] — la grammaire qui alimente la handoff queue (Stop 1)
- [[b1-wheel-imbalance-six-signes]] — le scan qui detecte les seuils d'escalade

## Note de confiance

**Confirme par machine.** Stop conditions et escalier sont verbatim du fractal. Emergency triggers : extrapolation a partir des Ownerbooks OMK (Paperclip plafonne, doctrines verrouillees) — pas une section explicite du fractal. A verifier au prochain tour quand les Ownerbooks seront lus.