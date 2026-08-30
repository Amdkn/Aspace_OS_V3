---
type: Concept
title: Mode Fable appliqué à Batman — cadre d'input vers B2 Council
description: Le mode Fable (cadrage / preuves / attaque / vérification / rapport) est un cadre de travail personnel, pas une doctrine B2. Ce concept propose 4 propriétés que Batman doit respecter pour que son input vers le Council soit Council-arbitrable : (1) fait daté, (2) source précise, (3) confiance chiffrée, (4) zéro décision. C'est ce qui distingue un *« fait »* d'une *« projection Batman »*.
tags: [mode-fable, batman, ops, fait, source, confiance, decision, council, arbitre]
generated: { by: minimax-m3, at: 2026-08-19T07:00:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-6, at: 2026-08-19T07:00:00Z }
sources:
  - id: mode-fable-brief
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-batman.md"
    title: "MODE FABLE — le cadre de travail posé en tête de brief Batman vague 2"
    last_modified: 2026-08-19
  - id: triplet-56
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 56 — Batman remonte à Summers des faits, pas des décisions"
    last_modified: 2026-08-17
  - id: b2-council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — instance d'arbitrage
    last_modified: 2026-08-19
  - id: b2-meso-decision-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Format packet mésoperpétuel
    last_modified: 2026-08-19
  - id: batman-canal
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-canal-remonte-b1-summers-format-concret.md"
    title: Canal de remontée Batman → B1 — format concret
  -3: 2026-08-19
  - id: batman-asymetrie
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-asymetrie-remonte-fait-formalisee-3-lectures.md"
    title: Asymétrie remonte-fait — 3 lectures en compétition
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Mode Fable appliqué à Batman — cadre d'input vers B2 Council

## Ce que le mode Fable est, ce qu'il n'est pas

Le mode Fable est posé en tête du brief de chaque escouade (cf.
`RAPPORT_dom-batman.md` §T1.1 — *« MODE FABLE — la manière de
travailler, avant la tâche »*) : **cadrage**, **preuves**,
**attaque**, **vérification**, **rapport**. C'est un cadre de
travail **personnel** (celui qui écrit s'engage à le respecter),
pas une doctrine B2.

Batman applique ce mode depuis 5 tours. Mais le rapport tour 5
§T5.5.1.2 a montré que les 3 lectures sur l'asymétrie remonte-fait
sont **en compétition sans arbitrage** — Batman défend Lecture C
(doctrine cycle) mais **ne l'a pas formalisée dans un format que le
Council peut trancher**. C'est précisément l'écart que ce concept
essaie de combler : **formaliser l'output Batman en format
Council-arbitrable**, pas en projection Batman-brute.

Le concept s'applique à deux niveaux :

1. **Pour Batman en interne** — quand Batman (ou un sub-agent qui
   écrit pour Batman) pose un concept OKF, le concept respecte 4
   propriétés minimales.
2. **Pour le Council en réception** — quand le Council arbitre une
   motion Batman, il teste ces 4 propriétés en premier filtre. Un
   input Batman qui manque une propriété est **rejeté en
   pré-arbitrage**, pas discuté.

## Les 4 propriétés que Batman doit respecter

### 1. Fait daté

**Définition** : le fait porte une date d'observation explicite,
distincte de la date d'écriture.

**Pourquoi** : un fait sans date d'observation est **non
audit-able**. Si Batman remonte *« la procédure X n'a pas de
condition d'arrêt »*, le Council doit pouvoir vérifier **quand**
Batman a observé ça. Une observation datée 2026-07-15 est
**différente** d'une observation datée 2026-08-19 — le premier
peut être devenu obsolète, le second est actuel.

**Test Council** : *« la date d'observation est-elle posée ? »*
Si non, rejet en pré-arbitrage avec mention *« fait non daté »*.

**Format** : `date_observation: YYYY-MM-DD` dans le frontmatter
du concept (distinct de `generated:`, qui est la date d'écriture).

### 2. Source précise

**Définition** : chaque fait pointe sur une source vérifiable
(chemin + ligne, ou URL, ou triplet), avec une **lecture
référençable**.

**Pourquoi** : sans source précise, le fait est un *« selon
Batman »* — non-falsifiable. Le Council ne peut pas trancher un
fait qu'il ne peut pas vérifier. Le triplet 56 parle de *« faits »*,
pas de *« intuitions »* ou *« projections »* — la source est la
garantie que le fait est **falsifiable**.

**Test Council** : *« la source est-elle lisible par un tiers ? »*
Si non, rejet en pré-arbitrage avec mention *« source non
vérifiable »*.

**Format** : section `sources:` dans le frontmatter OKF v0.2,
avec `resource:` (chemin / URL), `title:`, `last_modified:`.

### 3. Confiance chiffrée

**Définition** : chaque fait porte un niveau de confiance
explicite (haute / moyenne / basse), avec une note justifiant le
niveau si moyenne ou basse.

**Pourquoi** : un fait sans confiance chiffrée force le Council à
**deviner** la fiabilité. C'est exactement ce que le mode Fable
interdit (étape 3 — *« Attaque »* : *« Ce que tu ne peux pas
défendre sous attaque, tu le marques confiance:moyenne ou tu ne
l'écris pas »*). Le Council peut arbitrer plus vite si la
confiance est déjà posée.

**Test Council** : *« le niveau de confiance est-il posé ET
justifié ? »* Si confiance haute sans justification → OK.
Si confiance moyenne/basse sans justification → rejet en
pré-arbitrage avec mention *« confiance non justifiée »*.

**Format** : `niveau_confiance: haute|moyenne|basse` dans le
frontmatter du fait, avec note de justification dans le corps.

### 4. Zéro décision

**Définition** : le fait ne contient **aucune** formulation
décisionnelle. Batman décrit **ce qui est**, pas **ce qu'il faut
faire**.

**Pourquoi** : le triplet 56 est explicite *« Batman remonte des
faits, pas des décisions »*. Une formulation décisionnelle
(*« il faut… »*, *« on devrait… »*, *« je propose… »*, *« je
décide… »*) **transforme le fait en motion**, qui doit aller
dans un packet mésoperpétuel `B2-MESO-DECISION-YYYY-NN`, pas
dans un fait remonté.

**Test Council** : *« le fait contient-il une formulation
décisionnelle ? »* Si oui, rejet en pré-arbitrage avec mention
*« fait contaminé par décision — requalifier en motion »*.

**Format** : revue de chaque fait par Batman avant écriture, avec
suppression ou déplacement des formulations décisionnelles.

## Les 3 cas où Batman produit une motion (pas un fait)

Le mode Fable permet 3 cas où Batman **doit** produire une motion,
pas un fait — et où le format est Council-arbitrable :

### Motion 1 — Proposition d'amplification canonique

**Exemple** : *« La typologie 4 formes de condition d'arrêt (cf.
`batman-stop-condition-typologie-quatre-formes.md`) devrait être
**amplifiée** dans le catalogue 8 vetos — c'est l'équivalent
Batman du triplet 58 Wonder Woman. »*

**Format** : packet mésoperpétuel `B2-MESO-DECISION-YYYY-NN` avec
mode `negotiation`, impacted_domains incluant Batman + tous les
capitaines qui peuvent être impactés (ici : tous, parce que
l'amplification touche le catalogue 8).

### Motion 2 — Proposition d'amendement RACI / matrice

**Exemple** : *« Batman devrait être en Informed sur le pair-check
#4 Product→IT pour visibiliser la chaîne Product→IT→Ops (cf.
`batman-raci-i-sur-4-packet-council-ready.md`). »*

**Format** : packet mésoperpétuel `B2-MESO-DECISION-YYYY-NN` avec
mode `handoff`, impacted_domains Batman + Cyborg (+ les capitaines
qui peuvent être impactés par l'extension V5).

### Motion 3 — Demande d'arbitrage sur Lecture C

**Exemple** : *« Batman défend Lecture C (doctrine cycle) sur
l'asymétrie remonte-fait. Demande au Council de trancher entre
Lecture A (doctrine commune), Lecture B (oubli canonique) et
Lecture C (doctrine cycle). »*

**Format** : packet mésoperpétuel `B2-MESO-DECISION-YYYY-NN` avec
mode `negotiation`, impacted_domains Batman + les capitaines dont
la doctrine est en jeu.

## La règle de tri — fait ou motion

Trois questions que Batman (ou un sub-agent qui écrit pour Batman)
doit se poser **avant** d'écrire :

1. *« Est-ce que ce que je veux écrire décrit **ce qui est** ou
   **ce qui devrait être** ? »* Si c'est **ce qui est**, c'est un
   fait → format `_facts/`. Si c'est **ce qui devrait être**, c'est
   une motion → format packet mésoperpétuel.
2. *« Est-ce que ce que je veux écrire a besoin d'être arbitré ? »*
   Si non, c'est un fait (à mettre dans `_facts/` avec sortie
   constat ou signal). Si oui, c'est une motion (à mettre dans
   packet mésoperpétuel).
3. *« Est-ce que ce que je veux écrire engage une décision de
   cycle ? »* Si non, c'est un fait (Batman peut l'écrire seul). Si
   oui, c'est une motion qui doit escalader B1 (triplet 57).

## L'output côté Council — ce que le Council voit

Quand Batman remonte un fait, le Council voit :

- **Type** : binaire / structurel / couplage.
- **Date d'observation** : YYYY-MM-DD.
- **Source** : chemin précis.
- **Confiance** : haute / moyenne / basse, justifiée.
- **Zéro décision** : pas de formulation prescriptive.

Le Council a alors 3 options :

1. **Accepter** le fait comme constat (sortie 1 — append au journal).
2. **Tester** le fait (vérifier la source, reproduire
   l'observation) — peut prendre 1-3 jours.
3. **Rejeter** en pré-arbitrage (manque une des 4 propriétés).

Quand Batman propose une motion, le Council voit un packet
mésoperpétuel `B2-MESO-DECISION-YYYY-NN` qui respecte les 8 champs
canoniques (`b2-meso-decision-packet-spec.md`).

## Anti-pièges

- **Fait contaminé par décision.** Batman écrit *« la procédure X
  n'a pas de condition d'arrêt, il faut l'arrêter »*. La première
  phrase est un fait, la seconde est une motion. Batman doit
  **scinder** : le fait va dans `_facts/`, la motion va dans un
  packet mésoperpétuel distinct.
- **Motion déguisée en fait.** Batman écrit *« la procédure X
  n'a pas de condition d'arrêt, ce qui pose un problème de
  sécurité »*. La première phrase est un fait, la seconde est une
  **interprétation** (pas une décision, mais déjà une projection).
  Le Council peut la requalifier en motion.
- **Confiance non justifiée.** Batman marque *« confiance haute »*
  sur un fait sans preuve — c'est un signal de **projection
  déguisée**. Le Council rejette en pré-arbitrage.
- **Source qui n'existe pas.** Batman cite un triplet ou un
  fichier qui n'existe pas (typo, chemin mort) — le Council rejette
  en pré-arbitrage.
- **Date d'observation = date d'écriture.** Si les deux sont
  identiques et que le fait porte sur un phénomène lent (par
  exemple *« 0 packet mésoperpétuel Batman en 5 vagues »*), c'est
  suspect : un fait lent a une date d'observation ancienne. Le
  Council peut demander la distinction.

## Liens

- [[batman-canal-remonte-b1-summers-format-concret]] — le format
  concret `_facts/` où les faits Batman sont posés
- [[batman-doctrine-remonte-fait-non-decision]] — la doctrine qui
  impose zéro décision
- [[batman-veto-condition-arret-procedure]] — exemple de veto
  qui remonte comme un fait (sortie 3 escalade B1)
- [[batman-asymetrie-remonte-fait-formalisee-3-lectures]] —
  exemple d'arbitrage Lecture C à formaliser en motion
- [[b2-council-arbitrage-rule]] — qui arbitre les motions
- [[b2-meso-decision-packet-spec]] — le format des motions

## Note de confiance

**Confirmé par machine.** Le mode Fable est posé verbatim en tête
de brief Batman vague 2 (cf. `RAPPORT_dom-batman.md` §T1.1). Le
triplet 56 *« remonte des faits, pas des décisions »* est cité
verbatim. Les 4 propriétés (fait daté, source précise, confiance
chiffrée, zéro décision) sont **reconstruites** à partir du mode
Fable (5 étapes) et du triplet 56 (doctrine remonte-fait). Les
3 cas de motion (amplification / amendement RACI / arbitrage
Lecture C) sont **projetés** à partir des concepts Batman tour 4-5
qui ont posé ces motions sans les formaliser en packets. La règle
de tri (3 questions) est **mon inférence** à partir du triplet 56
+ du format mésoperpétuel canonique. Le pré-arbitrage Council
(3 options : accepter / tester / rejeter) est **reconstruit** à
partir de la routine Council §« Intake » (`b2-council-arbitrage-rule.md`)
qui pose déjà un scan des domaines impactés — j'étends le scan
aux 4 propriétés du fait Batman.