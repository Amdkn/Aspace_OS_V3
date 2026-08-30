---
type: Concept
title: People — lag indicator succession, taux et qualité de transition
description: Le délai de succession est un lag indicator People non posé dans le canon V4. Le concept propose trois indicateurs mesurables (délai median, taux de succession bouclée en ≤ N jours, qualité de transition mesurée par taux de rollback à 90 jours), avec des seuils différenciés par type de mandat (humain vs agent, junior vs senior, owner de marque vs owner de production). Format de remontée hebdomadaire, audit mensuel, et règle d'escalade si un lag franchit son seuil d'alerte.
tags: [people, green-lantern, lag-indicator, succession, delai, taux, qualite, transition, rollback, b2]
generated: { by: minimax-m3, at: 2026-08-19T05:10:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-2, at: 2026-08-19T05:10:00Z }
sources:
  - id: green-lantern-couplages-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-couplages-invisibles.md"
    title: "Tour 1 — People sept couplages invisibles, §3 succession"
    last_modified: 2026-08-19
  - id: green-lantern-gates-tour-1
    resource: "C:/Usersamado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-gats-assigned-needs-owner-dlq.md"
    title: "Tour 1 — People 3 états ASSIGNED / NEEDS_OWNER / DLQ"
    last_modified: 2026-08-19
  - id: green-lantern-jtbd-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-jtbd-emit-receive-xmen.md"
    title: "Tour 1 — People paquets JTBD émis et reçus"
    last_modified: 2026-08-19
  - id: triplet-33-prof
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 33 — ProfessorX tient le recruiting (sourcing, lecture profils, décision d'entrée)"
    last_modified: 2026-08-17
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — lag indicators comme promesse B3
    last_modified: 2026-08-19
okf_version: "0.2"
---

# People — lag indicator succession, taux et qualité de transition

## Le constat — un lag indicator manquant

`green-lantern-people-couplages-invisibles.md` §3 a posé la
**succession** comme couplage canonique People × Tous :

> *« Quand un owner quitte, People doit préparer la succession
> (cartographie des candidats internes, lancement du recrutement
> externe, transition de connaissance). Le captain du domaine
> d'accueil arbitre le choix final. »*

Le texte note explicitement :

> *« Le délai de succession est un lag indicator People qui n'est
> pas posé dans le canon V4. À poser. »*

Le B2 → B3 contract (`b2-b3-jtbd-handoff-contract.md` §« Ce que le
B3 squad promet ») impose au B3 squad des **lag indicators** — *«
les 1 à 2 métriques *après* l'exécution qui confirment que le
résultat a tenu »*. People, en tant que B2 captain qui mandate des
B3 squads, devrait donc lui-même **publier** des lag indicators
pour sa propre chaîne de succession. Le canon ne le fait pas.

Le présent concept pose **trois** lag indicators succession,
chacun avec sa métrique, son seuil, et son format de remontée. La
forme est **reconstituée** — le canon V4 ne pose aucun de ces
trois.

## Les trois lag indicators

### Lag 1 — Délai médian de succession

**Définition.** Le délai médian entre la **notification de départ**
(date à laquelle l'owner notifie son départ au captain du domaine
d'accueil) et la **prise de fonction** du successeur (date à laquelle
le nouveau owner est `ASSIGNED` et tenable).

**Mesure.** `mediane = médiane(délai_i)` sur les N successions des 12
derniers mois.

**Seuils (reconstitués)** :

| Type de mandat | Seuil vert | Seuil ambre | Seuil rouge |
|---|---|---|---|
| **Owner humain senior** (squad lead, B3 lead) | ≤ 60 jours | 60-90 jours | > 90 jours |
| **Owner humain junior** | ≤ 30 jours | 30-60 jours | > 60 jours |
| **Owner agent B3 squad** (X-Men, Avengers, etc.) | ≤ 14 jours | 14-30 jours | > 30 jours |
| **Owner agent générique** | ≤ 7 jours | 7-14 jours | > 14 jours |
| **Owner de marque** (porte-parole, content lead) | ≤ 90 jours | 90-120 jours | > 120 jours |

**Justification reconstruite.** Un owner de production peut être
remplacé en quelques jours si la documentation est à jour. Un
owner senior porte une **mémoire** qui prend du temps à
transférer. Un owner de marque porte une **voix** qui ne se
remplace pas — la transition peut être plus longue, ou plus
complexe (co-existence, content de transition).

### Lag 2 — Taux de succession bouclée en ≤ N jours

**Définition.** Pourcentage de successions bouclées dans le délai
cible (Lag 1 — seuil vert) sur les 12 derniers mois.

**Mesure.** `taux_bouclage = count(délai_i ≤ seuil_vert) / N × 100`.

**Seuils (reconstitués)** :

| Type de mandat | Seuil vert | Seuil ambre | Seuil rouge |
|---|---|---|---|
| Owner humain senior | ≥ 80% | 60-80% | < 60% |
| Owner humain junior | ≥ 85% | 70-85% | < 70% |
| Owner agent B3 | ≥ 90% | 75-90% | < 75% |
| Owner agent générique | ≥ 95% | 85-95% | < 85% |
| Owner de marque | ≥ 70% | 50-70% | < 50% |

**Justification.** Un taux de bouclage vert signifie que la
majorité des successions tiennent le délai. Un taux rouge indique
un **problème systémique** dans la chaîne People — pas une
succession individuelle manquée.

### Lag 3 — Taux de rollback à 90 jours

**Définition.** Pourcentage de successions où le successeur est
**remplacé** dans les 90 jours suivant sa prise de fonction. Le
**rollback** est un signal que la succession a échoué — le
successeur n'était pas la bonne personne, ou le mandat n'était pas
correctement scope.

**Mesure.** `taux_rollback = count(successions avec remplacement
< 90j) / N × 100`.

**Seuils (reconstitués)** :

| Type de mandat | Seuil vert | Seuil ambre | Seuil rouge |
|---|---|---|---|
| Owner humain | ≤ 10% | 10-20% | > 20% |
| Owner agent B3 | ≤ 5% | 5-10% | > 10% |
| Owner agent générique | ≤ 5% | 5-10% | > 10% |
| Owner de marque | ≤ 15% | 15-25% | > 25% |

**Justification.** Un taux de rollback vert signifie que les
successions **tiennent**. Un taux rouge indique que la chaîne de
sélection est défaillante — soit ProfessorX (recrutement humain,
triplet 33), soit Beast (recrutement agent, triplet 34) — pas
forcément People (la chaîne de décision). Mais People porte la
**carte de succession**, donc le signal lui revient.

## Le format de remontée hebdomadaire

Les trois lag indicators sont **remontés** chaque semaine dans le
journal Council. Format proposé :

```yaml
succession_lag_report:
  periode: 2026-W33
  people_captain: green-lantern
  successions_ouvertes: <count>
  successions_bouclees_30j: <count>
  lag_1_delai_median:
    par_type: {senior: 45j, junior: 22j, agent_b3: 9j, agent_gen: 4j, marque: 78j}
  lag_2_taux_bouclage:
    par_type: {senior: 82%, junior: 88%, agent_b3: 91%, agent_gen: 96%, marque: 65%}
  lag_3_taux_rollback:
    par_type: {humain: 8%, agent_b3: 4%, agent_gen: 5%, marque: 18%}
  alertes:
    - type: marque
      lag: lag_2_taux_bouclage
      valeur: 65%
      seuil: ambre
      action: revue_marque_30j
  next_review: 2026-W34
```

**Trois propriétés de ce format** :

1. **Période explicite** — chaque rapport est daté et versionné.
2. **Granularité par type** — un taux global masque les disparités
   (un owner de marque peut être à 50% de bouclage sans que la
   production ne le voie).
3. **Alertes actionnables** — chaque franchissement de seuil est
   rattaché à une **action** (revue, escalade, audit), pas juste
   constaté.

## L'audit mensuel — un garde-fou contre la dérive

Le format hebdomadaire peut **dériver** si People declare ses
propres seuils. Un audit mensuel croisé est proposé :

**Mécanisme.** Une fois par mois, deux capitaines B2 (autres que
People) **croisent** :

- le journal de charge People (cf.
  `green-lantern-people-formule-charge-carte.md` §« Gadget 2 »),
- le journal de succession (le présent concept),
- la carte de charge des owners **vue par leur captain d'accueil**.

Si un lag est franchi sans que People ait **réagi** (pas d'alerte
dans le journal hebdomadaire), le cas est porté en séance Council.
C'est un **garde-fou** contre l'auto-déclaration.

## La règle d'escalade aux seuils rouges

Quand un lag franchit le seuil rouge pendant deux périodes
consécutives (par exemple, taux de rollback humain > 20% deux mois
de suite), People **escalade** au B2 Council avec une **recommandation
d'action** — pas juste un constat. Trois actions possibles :

1. **Audit de la chaîne de sélection** — ProfessorX (humain) ou
   Beast (agent) revoit ses critères. People mandate l'audit, le
   captain d'accueil fournit la liste des successions ratées.
2. **Re-scope du mandat** — si le mandat est mal défini (scope trop
   large, ambigu, mal chiffré), le captain d'accueil revoit le
   mandat. People peut bloquer un re-mandat sans scope corrigé.
3. **Renfort de la squad People** — si la chaîne People est
   sous-effectif (X-Men 8 agents pour 53 mandates, taux
   d'occupation > 1.0 sur People), People mandate un renfort (un
   nouvel agent X-Men, par exemple — Wolverine ou Storm, dont le
   rôle canon n'est pas explicité, cf.
   `green-lantern-people-jtbd-emit-receive-xmen.md` §« La squad
   X-Men : 8 agents »).

## Le cas asymétrique — owner de marque

L'owner de marque (porte-parole, content lead) a un lag
**structurellement** plus long et un taux de rollback
**structurellement** plus haut. Le canon V4 ne pose pas cette
asymétrie — elle est **reconstituée** depuis la pratique Coach OS
et la notion de *« continuité de la marque »* (cf.
`green-lantern-people-couplages-invisibles.md` §7).

**Conséquence** : un lag rouge sur la marque n'est **pas** un
signal de défaillance People — c'est un signal de **dépendance
excessive à un owner individuel**. Le couplage People × Brand (cf.
concept #6 du présent tour 2) entre en jeu : la rotation d'un
owner de marque n'est pas un simple `ASSIGNED → DESASSIGNED`, c'est
un arbitrage Council avec Superman Growth.

## Anti-pièges

- **Confondre lag et lead.** Le délai de succession est un **lag**
  (mesure *après*), pas un lead (mesure *pendant*). People doit
  publier un **lead** aussi — par exemple, *« temps moyen entre
  notification de départ et premier sourcing actif »*. Le lead
  est plus réactif (signal en cours), le lag est plus définitif
  (constat après).
- **Prendre le lag vert comme cible, pas comme seuil.** Un lag
  vert ne veut pas dire *« la succession est parfaite »* — il
  veut dire *« la succession tient le seuil »*. Viser en-dessous
  du seuil vert n'est **pas** un objectif — c'est un signal que
  les seuils sont mal calibrés.
- **Cacher les roulettes sous le tapis.** Un lag rouge pendant un
  mois peut être **passé sous silence** par People si le format
  ne force pas l'alerte. Le format YAML ci-dessus force
  l'**alerte actionnable** — un lag rouge sans action proposée est
  un packet invalide.
- **Appliquer les seuils d'un type à un autre.** Les seuils
  humain / agent / marque sont **très différents**. Un agent
  générique à 14 jours est **rouge**, un humain senior à 60 jours
  est **vert**. Confondre les échelles = comparer des
  pommes et des oranges.
- **Oublier que le lag mesure People, pas le successeur.** Le
  taux de rollback à 90 jours mesure **la chaîne People de
  sélection** (ProfessorX, Beast), pas la compétence du
  successeur. Un successeur qui rate n'est pas un mauvais
  successeur — c'est une **mauvaise sélection**. People doit
  lire le lag comme un signal de **process**, pas de **personne**.

## Liens

- [[green-lantern-people-couplages-invisibles]] — §3 succession
  canonique + §7 couplage People × Brand
- [[green-lantern-people-formule-charge-carte]] — le journal de
  charge qui sert de point d'entrée à l'audit croisé
- [[green-lantern-people-jtbd-emit-receive-xmen]] — Type B
  (succession d'owner) déjà posé comme paquet JTBD reçu
- [[green-lantern-people-veto-recrutement-sans-mandat]] — la grille
  de mandat humain / agent que la chaîne de sélection doit tenir
- [[b2-b3-jtbd-handoff-contract]] — la doctrine B2 → B3 sur les
  lag indicators comme promesse B3

## Note de confiance

**Reconstruit, à moitié étayé.** Le gap canonique est posé (canon
V4 ne pose aucun lag indicator succession). Les trois lag
indicators (délai médian, taux de bouclage, taux de rollback) sont
**projetés** depuis la pratique RH classique et la doctrine B2 → B3
contract sur les lag indicators. Les seuils par type (humain
senior, humain junior, agent B3, agent générique, marque) sont
**reconstitués** avec référence implicite à la difficulté
structurelle de chaque type — pas de mesure canonique. Le format
YAML est **projeté** depuis le packet mésoperpétuel Council. La
règle d'escalade aux seuils rouges est **un ajout** : pas de
source canonique, mais aucune source ne l'interdit. **À arbitrer
par B2 Council.** Le concept propose une **forme**, pas une
**vérité**.
