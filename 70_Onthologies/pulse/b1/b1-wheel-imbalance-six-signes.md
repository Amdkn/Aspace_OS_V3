---
type: Concept
title: B1 wheel imbalance scan — les six signes qu'un mandat est du
description: Six signes que B1 scanne sur la wheel 8-domain avant d'emettre un mandat : domaine vide, surcharge, gate bloquee, derive produit-only, conflit cross-domaine, preuve manquante. Chaque signe a un remede standard.
tags: [b1, wheel, scan, imbalance, huit-domaines, signaux]
generated: { by: minimax-m3, at: 2026-08-19T01:35:00Z }
verified:
  - { by: process:lecture-fractal-b1b2b3, at: 2026-08-19T01:35:00Z }
  - { by: process:synthese-pulse-b1-tour-1, at: 2026-08-19T01:35:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: fractal-arch
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md"
    title: L2 Business — The B1 / B2 / B3 Fractal Architecture
    last_modified: 2026-06-02
  - id: eight-domain
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel
    last_modified: 2026-08-17
okf_version: "0.2"
---

# B1 wheel imbalance scan — les six signes qu'un mandat est du

B1 ne decide pas d'emettre un mandat sur une intuition. Il scanne la wheel 8-domain et agit sur un **signe**. Six signes canoniques, tires du fractal.

## La wheel 8-domain (rappel)

Les 8 domaines B2 — Growth, Sales, Product, Ops, IT, Finance, People, Legal — chacun avec un B2 captain et un B3 squad Marvel. Chaque domaine emet un gate (READY / NEEDS_X / BLOCKED_X). La wheel tourne quand **tous** les gates sont dans un etat exploitable, et que les **transitions** entre domaines marchent.

La matrice d'harmonisation teste les transitions deux a deux (Growth×Sales, Sales×Ops, etc.) et bloque un lancement quand une combinaison de red flags rend l'ensemble inoperant. Voir [[b2-business-wheel-harmonization-matrix]].

## Les six signes

### Signe 1 — Domaine vide

Un domaine n'a pas de B2 captain actif, ou le captain n'a pas emis de gate depuis plus d'un 12WY. **Diagnostic** : ownership perdu, ou domaine declares sans squelette.

**Remede standard** : mandat B1 → B2 owner vacant + escalation A0 si pas de candidat interne. Ne pas *« laisser le domaine se reposer »* — un domaine vide laisse une transition aveugle.

### Signe 2 — Surcharge

Un domaine cumule plus de 3 mandates B1 actifs simultanement, ou le B2 captain remonte des `BLOCKED_*` repetes. **Diagnostic** : la cadence d'execution depasse la capacite du captain, ou les mandates ne sont pas assez precis et se chevauchent.

**Remede standard** : geler les nouveaux mandates B1 vers ce domaine jusqu'a ce que la backlog descende sous 2. Prioriser dans la handoff queue. Si la surcharge est structurelle (domaine sous-dote en B3), escalade A0 pour renforcer la squad.

### Signe 3 — Gate bloquee

Un B2 captain reste sur `BLOCKED_*` plus d'un cycle sans que le B2 Council ait tranche. **Diagnostic** : le blocage est cross-domaine (le captain ne peut pas le resoudre seul) ou la wheel scannee a un domaine adverse qui bloque la transition.

**Remede standard** : forcer un arbitrage B2 Council. Si le Council ne peut pas preserver la wheel, c'est une escalade vers B1 — un mandat refrant les contraintes.

### Signe 4 — Derive produit-only

Trois domaines ou plus emettent des signaux OK, mais le reste de la wheel est silencieux (les autres domaines n'ont pas emis de signal depuis plus d'un 12WY). **Diagnostic** : le projet s'est focalise sur le livrable, l'operabilite et la soutenabilite n'avancent pas.

**Remede standard** : pause des nouveaux mandates Product / IT. Mandat B1 vers Ops, Legal, People pour ramener la wheel en equilibre. C'est le signe le plus insidieux : la wheel affiche du vert sur 3/8 et tout le monde pense que c'est OK.

### Signe 5 — Conflit cross-domaine

Le B2 Council remonte un arbitrage en mode *negotiation* qui ne se resout pas en un cycle. **Diagnostic** : deux DoD ou plus sont en conflit et necessitent un tradeoff de cycle ou de North Star.

**Remede standard** : arbitrage B1 (avec A0 si North Star en jeu). C'est le seul moment ou B1 tranche un conflit cross-domaine directement. Avant ce seuil, le Conseil arbitre.

### Signe 6 — Preuve manquante

Un B3 a execute un JTBD, mais la preuve (lead/lag indicator, peer-review, screenshot, log) est absente ou non-inspectable. **Diagnostic** : la boucle de verification est cassee, ou l'auteur de la preuve est le seul a pouvoir la lire.

**Remede standard** : exiger une preuve externe (agent relecteur, capture outillage, log exporte) avant que B2 ne passe le gate. Tant que la preuve manque, le JTBD est `BLOCKED_DELIVERY`.

## Lecture en grille — pas en silos

Les six signes ne sont pas exclusifs. Une wheel peut en montrer deux ou trois. La regle : **un seul signe suffit pour justifier un scan plus profond**, pas forcement un mandat immediat.

| Combinaison observee | Lecture |
|---|---|
| Surcharge + gate bloquee | Le domaine n'arrive pas a sortir ; risque de burnout captain |
| Domaine vide + conflit cross-domaine | Une transition est aveugle ET en conflit ; escalade A0 |
| Derive produit-only + preuve manquante | Les 3 domaines visibles n'ont pas de preuve ; pas de wheel reellement verte |
| Gate bloquee + preuve manquante | Le captain bloque sur un signal qu'il ne peut pas verifier ; verifier d'abord |

## Quand le scan est *negatif*

Six signes absents ne veut pas dire wheel saine — cela veut dire qu'aucun signe canonique n'est visible. La wheel peut etre :

- **Operante mais sans cadence** — les domaines tournent, mais sans rythme mesurable. B1 cadence alors par 12WY rocks, pas par mandat.
- **Verte par defaut** — tous les domaines emettent `READY` sans qu'aucun proof path n'ait ete ouvert. Suspect : le B2 Council peut etre en *groupthink*. B1 doit alors poser une question derangeante, pas un mandat.

Le scan negatif est un signal de **manque de visibilite**, pas de sante. Voir [[b1-decision-rights-frontieres]] pour ce que B1 peut faire d'autre.

## Sources

- `00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` — liste verbatim des six signes dans le flux de commandement etape 2.
- `B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md` §« Domain Pair Checks » — les 9 pair checks qui valident les transitions.
- `eight-domain-avengers-wheel.md` — la wheel 8-domain et ses gates.

## Liens

- [[b1-decision-rights-frontieres]] — ce que B1 peut faire quand un signe est detecte
- [[b1-mandate-packet-spec]] — la forme du mandat qui remedie au signe
- [[b2-business-wheel-harmonization-matrix]] — la matrice que B2 applique au signe

## Note de confiance

**Confirme par machine.** Liste des six signes verbatim depuis le fractal. Lecture en grille : extrapolation motivee, pas une doctrine ecitee — a surveiller dans le prochain tour si une pair-check matrix est ajoutee.