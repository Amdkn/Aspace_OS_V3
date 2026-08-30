---
id: ONTOLOGIE_V1
statut: PROPOSITION D'ARCHITECTE — a valider, amender ou rejeter
date: 2026-08-13
---

# L'ontologie des trois couches — version 1

## Ce que ce document est, et ce qu'il n'est pas

**Ce n'est pas un recensement.** Quatre passes d'agents ont recense le canon et
le corpus ; la derniere a rendu 49 entites, 2 relations, 14 trous. C'etait
previsible : on lui demandait de trouver des liens que personne n'avait jamais
poses.

Le canon DC/Marvel, les cadres Star Trek, les 96 sessions, Geordi — **c'est de
la matiere, pas une structure**. Une ontologie ne se retrouve pas dans ses
sources : elle se decide, puis on verifie qu'elle tient contre elles.

Ce document decide. Chaque choix est marque **DECISION** et peut etre rejete.

---

## §1 · Le principe : trois couches, un sens de service

Les trois couches ne sont pas trois dossiers. Elles ont un **ordre de
subordination**, et c'est lui qui fait l'ontologie plutot qu'un catalogue.

```
   TECH OS      sert      BUSINESS OS      sert      LIFE OS
   (comment)              (avec quoi)                (pourquoi)
```

**DECISION 1 — le sens est unique et ne se renverse pas.** Un agent sert un
domaine ; un domaine sert une vision. Jamais l'inverse. Une vision qui
« servirait » un agent est le signe qu'on a construit l'outil avant le but —
c'est exactement la faute que le corpus documente en boucle.

Consequence testable : **toute chaine doit remonter a une Vision.** Un objet
qui ne remonte pas est soit orphelin, soit inutile. C'est ce que mesure
`pct_rattachable`, aujourd'hui a 0 %.

---

## §2 · Les entites, couche par couche

**DECISION 2 — on garde peu d'entites et beaucoup de relations.** Le reflexe
inverse (49 entites, 2 relations) produit un catalogue, pas un modele. Une
entite se merite : elle existe si quelque chose pointe vers elle.

### LIFE OS — le pourquoi (5 entites)

| Entite | Ce que c'est | Realite mesuree |
|---|---|---|
| **Vision** | une intention declaree, a un horizon | 20 lignes dans `ikigai_visions` |
| **Pilier** | craft · mission · passion · vocation | 4, fermes |
| **Horizon** | H1 · H3 · H10 · H30 · H90 | 5, fermes |
| **Ambition** | un engagement sur un domaine de vie | 8 lignes, LD01→LD08 |
| **Rock** | un livrable de semaine | 15 lignes, W1→W12 |

`Pilier` et `Horizon` sont des entites, pas des chaines. **DECISION 3** : une
valeur fermee sur laquelle on veut compter, filtrer et rattacher est une entite.
C'est ce qui fait la difference entre « H10 » ecrit dans deux tables et un
horizon qui relie reellement deux objets.

### BUSINESS OS — le avec quoi (6 entites)

| Entite | Ce que c'est | Realite mesuree |
|---|---|---|
| **Domaine** | un des 8 domaines du Business Pulse | 8, canon Lore Index |
| **Proprietaire** | le stratege DC qui en repond | 8 : Superman, Martian Manhunter, Flash, Batman, Cyborg, Wonder Woman, Green Lantern, Aquaman |
| **Escouade** | l'unite Marvel qui execute | 8 : Guardians, Illuminati, Avengers, Fantastic4, KangDynasty, Thunderbolts, XMen, Eternals |
| **Offre** | ce qui se vend | `Offering`, deja livree |
| **Client** | qui l'achete | `Client`, deja livree |
| **Procedure** | SOP et Runbook | deja livrees |

**DECISION 4 — `Proprietaire` et `Escouade` sont deux entites, pas deux
attributs du Domaine.** Un stratege peut changer de domaine ; une escouade a des
membres nommes (Invisible Woman, Jean Grey sont dans le Lore Index). Les aplatir
en chaines rendrait impossible de dire « qui, dans les X-Men, tient ce Rock ».

### TECH OS — le comment (5 entites)

| Entite | Ce que c'est |
|---|---|
| **Agent** | un executant, humain ou modele |
| **Cadence** | un rythme d'execution (1m, 5m, 10m, 15m, 20m, 25m, 30m) |
| **Garde-fou** | une regle qui refuse |
| **Incident** | une chute observee |
| **Sonde** | ce qui mesure un garde-fou |

**DECISION 5 — `Garde-fou` et `Sonde` sont distincts.** La journee du
2026-08-13 en donne la raison : onze faux verdicts, tous produits par des sondes
mal formees mesurant des garde-fous corrects. Confondre la regle et son
instrument, c'est ne pas pouvoir dire lequel des deux a menti.

---

## §3 · Les relations — ce qui manquait, et c'est tout le sujet

L'ontologie livree dans coach-os a 27 relations. Jusqu'a aujourd'hui, **toutes
etaient structurelles** : `has`, `binds`, `manages`, `executes`, `runs`,
`acquires`, `incarnates`, `projects`, `guides`, `requires`, `mitigates`,
`triggers`, `engages`.

Aucune ne disait **pourquoi**. C'est la cause de `pct_rattachable = 0 %`, et
aucun recensement ne pouvait la reveler : il n'y avait rien a recenser.

### Les quatre verbes qu'on ajoute

**DECISION 6 — `sert` : l'axe de finalite.**

```
Rock        --sert-->  Vision
Ambition    --sert-->  Vision
Domaine     --sert-->  Vision        ← traverse Business → Life
Agent       --sert-->  Domaine       ← traverse Tech → Business
Cadence     --sert-->  Domaine
```

C'est le verbe absent. Il transforme cinq seaux d'horizon partage en une chaine
reelle : `Agent → Domaine → Vision`. Techniquement c'est une colonne
(`vision_id`) ; ontologiquement c'est ce qui fait exister les trois couches
comme un tout plutot que comme trois dossiers.

**DECISION 7 — `repond de` : l'axe d'autorite.**

```
Proprietaire --repond de--> Domaine
Escouade     --execute-->   Domaine
Domaine      --possede-->   SOP · Runbook · Routine · Incident · Offre
```

Pose dans le code le 2026-08-13. Sans lui, aucune SOP n'a de responsable.

**DECISION 8 — `remplace` et la validite : l'axe temporel.**

```
Objet --remplace--> Objet
Objet .valide_de / .valide_jusqu_a / .statut ∈ {actif, deprecie}
```

L'ontologie ne savait pas dire qu'une chose en perime une autre. Cout mesure le
2026-08-13 : `ARCHITECTURE_V1.md` du 7 aout affirmait « `createItem` n'existe
pas » alors que le code l'avait depuis des jours — 4 lignes sur 6 perimees. Et
`SDD-006` decrivait 7 domaines quand le canon en a 8, ce qui a fait ecrire une
mauvaise version de ce registre le matin meme.

**Un document sans date de validite est un document qui ment avec confiance.**

**DECISION 9 — `atteste` : l'axe de preuve.**

```
Sonde     --atteste-->  Garde-fou
Incident  --revele-->   Garde-fou manquant
Capture   --atteste-->  Correctif
```

Onze faux verdicts en une journee. Un garde-fou jamais vu se declencher est un
garde-fou suppose ; un correctif sans capture n'est pas verifie. L'ontologie doit
pouvoir porter la difference entre « affirme » et « constate ».

---

## §4 · Ce qui se teste

Une ontologie qui ne se mesure pas est une opinion. Trois metriques :

| Metrique | Definition | Aujourd'hui |
|---|---|---|
| `pct_rattachable` | objets qui remontent a une Vision par `sert` | **0 %** |
| `pct_avec_proprietaire` | objets Business ayant un `repond de` | 0 % |
| `pct_atteste` | garde-fous vus se declencher | 2 sur ~8 |

**DECISION 10 — la premiere vaut pour toutes.** Tant qu'elle est a zero, les
trois couches sont trois dossiers.

---

## §5 · Les choix qui te reviennent

Ce ne sont pas des trous dans les sources. Ce sont des **decisions non prises**,
et elles ne peuvent pas l'etre par un agent :

1. **Sales / Illuminati / John Jones — B2 a part entiere, ou sous-ensemble de
   Growth ?** Le Lore Index le liste en propre. Le SDD ne le connait pas. Le
   dossier `src/apps/sales/` existe. Trois sources, trois etats.
2. **Les 4 Variants de Jerry — Postures d'une meme entite, ou 4 entites ?**
   S'ils ont des plafonds differents (`max_active_summers`), ce sont 4 entites.
3. **Summer's Verse — canonique, ou artefact d'un SDD perime ?** Meme doute que
   pour SDD-006. Verifier dans V3 avant de modeliser.
4. **L'horizon s'applique-t-il aux objets Business ?** Aujourd'hui il vit en Life
   OS. S'il traverse, il devient l'axe commun ; sinon `sert` porte seul la
   jointure.
5. **Une Vision peut-elle etre servie par plusieurs domaines ?** Si oui, `sert`
   est n-n et le rattachement se dilue. Si non, chaque domaine a une seule
   raison d'etre — plus dur, plus clair.

---

## §6 · Ce que je propose comme suite

**Une seule chose : la DECISION 6.** Ajouter `vision_id` sur `Rock` et
`Ambition`, et exposer `sert` dans `relations.ts`.

C'est une colonne et une relation. Apres ca, `pct_rattachable` cesse d'etre 0 %
et devient un nombre qui bouge — et une ontologie qui bouge peut se corriger,
alors qu'un catalogue ne le peut pas.

Le reste de ce document attend tes cinq arbitrages.
