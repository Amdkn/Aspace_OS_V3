# Intentions, besoins, problématiques, désirs — 2 307 sessions, mars→août 2026

> **Méthode.** Le champ `titre` de `_substrat/05_Sessions.jsonl` est le **premier
> message humain** de chaque session : l'intention au moment où elle est formulée,
> avant toute négociation avec la machine. 2 307 sessions retenues sur 2 325
> (18 écartées : moins de 12 caractères).
>
> Le découpage en 10 tranches a été **délégué à `claude-glm`** — 10 passes, ~1 h
> de temps machine, hors quota Anthropic. Les **comptages sont scriptés**, pas
> inférés : le délégué a produit une hypothèse (« la duplication domine »), le
> script l'a tranchée. C'est l'application du principe que tu as tiré de
> CEO-Bench.
>
> **Confiance : machine.** Rien ici n'a été relu par un humain.

---

## 0. Le chiffre qui commande tous les autres

| Mois | Sessions | Intentions **uniques** | % unique |
|---|---:|---:|---:|
| 2026-03 | 2 | 2 | 100 % |
| 2026-04 | 5 | 4 | 80 % |
| 2026-05 | 57 | 47 | 82,5 % |
| 2026-06 | 241 | 220 | 91,3 % |
| 2026-07 | 1 123 | 904 | 80,5 % |
| **2026-08** | **879** | **284** | **32,3 %** |
| **Total** | **2 307** | **1 461** | **63,3 %** |

**En août, deux sessions sur trois rejouent une intention déjà formulée.** Le
taux tenait entre 80 et 91 % pendant cinq mois ; il s'effondre en un seul.

Les briefs les plus rejoués, tous mois confondus :

| Rejeux | Brief |
|---:|---|
| 132× | `you are running as a chat assistant for a multica workspace…` |
| 83× | `you are running as a local coding agent for a multica workspace…` |
| 69× | `LES SEPT CADENCES — table de vérité de l'ordonnanceur…` |
| 65× + 31× | `GARDE-FOU — vague de revue, tu exécutes ce brief toi-même…` |
| 60× | `MODE FABLE — la manière de travailler…` |
| 45× | `tu exécutes cette critique toi-même, avec tes propres outils…` |
| 27× | `tu es le worker WF1 (Morty)…` |

**978 sessions sur 2 307 (42,4 %) portent une intention déjà vue.**

---

## 1. Intentions — ce que tu cherches à obtenir

Sur les **1 453 intentions uniques** (après dédoublonnage), par volume :

| Thème | Uniques | mai | juin | juil | août | État en août |
|---|---:|---:|---:|---:|---:|---|
| **Agents, sous-agents, cadences** | **700** | 3 | 92 | **484** | 120 | en reflux |
| **Coach OS / Life OS / Agent OS** | 195 | 18 | 55 | 59 | **62** | **en croissance continue** |
| Business, PARA, projets | 183 | 24 | 57 | 67 | 34 | en reflux |
| Vérification, audit, revue | 150 | 8 | 15 | 93 | 33 | en reflux |
| Quota, coût, modèle | 60 | 1 | 3 | **53** | 3 | **éteinte** |
| Outillage, harness, MCP | 56 | 4 | 21 | 20 | 11 | stable bas |
| Distillation, migration V3 | 37 | 0 | 5 | 18 | 14 | active |
| **Mémoire, ontologie, RDF** | **22** | 5 | 1 | 5 | **11** | **émergente** |

Trois lectures que ce tableau impose :

**I1 — Orchestrer des agents est ton intention dominante** (48 % des intentions
uniques), et elle culmine en juillet. Elle ne disparaît pas en août, elle change
de forme : elle passe de « comment faire tourner des agents » à des **rejeux
automatiques** de briefs déjà écrits. D'où l'effondrement du §0.

**I2 — Les applications sont la seule intention qui ne recule jamais.** 18 → 55
→ 59 → 62. Coach OS, Life OS, Agent OS. C'est le seul thème dont la courbe
monte sur les quatre mois. Tu demandes des agents ; tu reviens aux **surfaces
visibles**.

**I3 — L'ontologie est ton intention la plus récente, pas la plus mûre.** Tu la
déclares comme ton stade actuel (« j'ai dépassé le contexte engineering pour me
retrouver en ontology engineering »), et c'est vrai : 22 intentions uniques au
total, mais **la moitié en août**. C'est un virage en cours, pas un acquis.

**I4 — La crise de quota était en juillet et elle est réglée.** 53 intentions
uniques sur le sujet en juillet, **3 en août**. Les routeurs, OpenRouter et
`claude-glm` ont éteint le sujet. Ce n'est plus le problème.

---

## 2. Besoins révélés — ce que la répétition trahit

Un besoin exprimé est ce que tu demandes. Un besoin révélé est ce que la
répétition dit malgré toi.

**B1 — Tu as besoin qu'un mandat survive à la reprise de session.**
`GARDE-FOU` relancé 96 fois, `LES SEPT CADENCES` 69 fois, `MODE FABLE` 60 fois.
Ces briefs disent tous la même chose : *exécute toi-même, n'invoque personne,
voici la table de vérité*. **Tu les réécris parce qu'ils ne tiennent pas.**
Chaque reprise sur résumé efface l'autorisation et garde les réflexes de
prudence — c'est exactement la panne du governor module, déjà consignée, et
c'est le besoin non satisfait le plus coûteux du corpus.

**B2 — Tu as besoin de voir l'état, pas de le reconstituer.**
Les 195 intentions « apps » ne demandent pas des fonctionnalités : elles
demandent des **vues**. Agent OS, les schémas, l'arborescence, les points
d'accès. Et jusqu'à aujourd'hui, `CLAUDE.md` ne portait **aucune cartographie de
V3** — chaque session redécouvrait 10 734 fichiers à l'aveugle.

**B3 — Tu as besoin que la vérification soit scriptée, pas déléguée à un jugement.**
150 intentions « audit / revue », et le mot qui revient est *toi-même*.
Tu ne demandes pas un avis, tu demandes une **exécution vérifiable**. Le
délégué de cette session l'illustre : il a affirmé « la duplication domine »,
il avait raison, mais c'est le script qui l'a établi.

**B4 — Tu as besoin de moins de systèmes, pas de plus.**
Les 700 intentions « agents » produisent 8 cadences, 3 frameworks, des
gatekeepers, des workers. Aucune n'a pour objet de **retirer** quelque chose.

---

## 3. Problématiques — classées par coût réel

**P1 — La boucle du rejeu.** 67,7 % des sessions d'août rejouent un brief.
Le système construit pour travailler seul **se relance plutôt qu'il ne produit**.
Coût : la majorité du volume d'août.

**P2 — La boucle du mandat perdu.** Chaque compaction efface l'autorisation
d'agir et conserve les faits. L'agent repart prudent, redemande, et tu réécris
le brief. C'est la cause de P1.

**P3 — La boucle du point d'entrée.** Le `CLAUDE.md` désignait
`40_Memory_Wiki_OKF/` comme « la mémoire ». Mesure du jour : **38 `.md` sur
6 534, soit 0,6 % du corpus**. Suivre la consigne garantissait de manquer
99,4 % de ce qui est écrit, donc de conclure « non documenté », donc de
redemander. *Corrigé aujourd'hui — `CARTOGRAPHIE.md` + pointeur en tête.*

**P4 — La boucle de l'instrument qui ment.** Jonctions NTFS comptées 13,8 M au
lieu de 14 613 ; filtres qui se comptent eux-mêmes ; scripts sans arrêt sur
erreur qui annoncent un succès. Récurrent, et chaque occurrence coûte une
conclusion fausse.

**P5 — Le plancher de contexte.** 127 000 tokens chargés avant ton premier mot,
dont ~5 000 seulement de `CLAUDE.md`. Le reste est du schéma d'outils MCP et de
greffons. Mesuré ce soir : ce plancher **a fait échouer le délégué** deux fois
(`Prompt is too long`) jusqu'à ce que je le coupe avec `--strict-mcp-config`.

**P6 — La production dépasse la vérification.** 423 fichiers produits en deux
vagues, zéro relu par un humain. Le goulot n'est plus d'écrire.

---

## 4. Désirs — ce qui oriente sans être demandé

**D1 — Un jumeau qui tient sans toi.** Jamais formulé comme tel, présent partout :
« perpetual Events Runtime », « pas une boîte noire », « observabilité profonde ».
Tu ne veux pas un assistant qui répond — tu veux un système qui **continue**.

**D2 — Que la distinction entre ce qui est mesuré et ce qui est supposé soit
structurelle.** C'est tout OKF, toute la Silver Gate, tout le `A SOURCER`. Le
désir n'est pas d'avoir raison : c'est que **l'erreur soit visible**.

**D3 — Ne pas construire un second cerveau de plus.** Dit explicitement
(« contrairement à la masse qui conçoivent des second cerveau inutile »). Le
refus d'Obsidian n'est pas technique : le corpus **est** la source, l'app n'en
est qu'une vue.

**D4 — Reproduire sans réexpliquer.** La franchise, les ownerbooks, les SOP qui
deviennent des skills, D.E.A.L. Le désir est que **le système se réplique**,
pas qu'il grossisse.

---

## 5. Trajectoire mars → août

| | |
|---|---|
| **mars–mai** | V2 vivant, audits VPS, exploration. Faible volume, forte unicité. |
| **juin** | Fondation V3 (07-09), explosion des sous-agents A3. 91,3 % d'unicité — le sommet. |
| **juillet** | Le pic absolu : 1 123 sessions, 484 intentions « agents », 53 sur le quota. Wargames, ADR, EXPANSION MODE, D7 FULL BURN. |
| **août** | **La bascule.** Volume −22 %, unicité −60 %. La machine tourne, elle se relance. |

**Point de bascule : première quinzaine d'août.** Deux signaux concordants —
le quota cesse d'être un sujet (53 → 3) et l'unicité s'effondre (80,5 % →
32,3 %). Tu as résolu le coût et perdu la nouveauté dans le même mouvement.

**Ce qui n'a jamais bougé :** les applications (18→55→59→62) et l'exigence de
vérifiabilité.

---

## 6. Ce que la migration V3 doit porter

| # | Exigence | Rattachée à |
|---|---|---|
| E1 | Le **mandat d'autonomie vit dans un fichier lu au démarrage**, pas dans l'historique. C'est la seule correction qui casse P1 à la racine. | B1, P2 |
| E2 | Un **compteur de rejeu** : si une intention est déjà vue, le dire avant d'exécuter. Un système qui ne sait pas qu'il se répète ne peut pas s'arrêter. | P1 |
| E3 | La **cartographie régénérée**, pas rédigée, en tête des points d'entrée. | B2, P3 |
| E4 | Tout chiffre affiché est **lu à chaud** ; aucune mesure figée dans le code. | P4, D2 |
| E5 | **Dégraisser le plancher de contexte.** Chaque 10k retiré rend $0,05/appel sur Opus, sur *tous* les appels. | P5 |
| E6 | La **vérification est scriptée**, l'inférence propose, le script tranche. | B3, D2 |
| E7 | Le passage `machine → humain` reste **manuel et explicite**. Aucun script ne le pose. | P6, D2 |
| E8 | Les **surfaces visibles sont un livrable de premier rang**, pas un habillage. C'est la seule intention qui n'a jamais reculé. | I2, B2 |
| E9 | Toute nouvelle cadence exige de **nommer celle qu'elle remplace**. | B4, D4 |
| E10 | La **franchise se réplique par générateur**, jamais par copie. Deux exemplaires d'un standard divergent en silence. | D4 |

---

## 7. Ce que je n'ai pas pu déterminer

1. **Les premiers messages ne disent pas les résultats.** Je mesure ce que tu as
   demandé, pas ce que tu as obtenu. Un thème très demandé peut être très
   satisfait — ou pas du tout. Le corpus des 4 647 transcriptions complètes le
   dirait ; il n'a pas été analysé ici.

2. **Le seuil de duplication est un choix.** « Même intention » = 120 premiers
   caractères normalisés identiques. Un brief reformulé compte comme unique.
   Le taux réel de rejeu est donc **au moins** 42,4 %, probablement plus.

3. **Mars et avril sont vides** (7 sessions). L'origine de la trajectoire est
   invisible : soit tu ne travaillais pas ainsi, soit ces sessions ont été
   perdues avant la désactivation de la rétention.

4. **Je n'ai pas mesuré le coût par intention.** Savoir quelles intentions
   consomment le plus demanderait de croiser avec les compteurs d'usage.
   C'est faisable et ce n'est pas fait.

5. **Les 10 analyses partielles déléguées sont inégales.** Plusieurs ont produit
   un inventaire chronologique au lieu d'une analyse. Elles ont servi de matière
   première ; les conclusions ci-dessus reposent sur les **comptages scriptés**,
   reproductibles, pas sur leur jugement.

---

*Reproduire les mesures : `_substrat/05_Sessions.jsonl` est l'entrée, les
scripts de comptage sont dans le corps de cette session. Les 10 analyses
partielles sont dans `50_Distillation/_partiels/`, les tranches dans
`50_Distillation/_tranches/`.*
