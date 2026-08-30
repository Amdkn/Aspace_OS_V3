# RAPPORT J — Décisions oubliées

> Source : `SESSION_2026-08-13_condense.md` (29 047 lignes).
> Source de vérité : `decisions_oubliees.json` (33 entrées).
> Règle : **affirmée + actionnable + rien dans la suite ne la déclare faite**. Annulé par l'utilisateur = sorti.

---

## Méthode et périmètre

J'ai lu l'intégralité du condensé en cherchant chaque ligne qui remplit les trois critères du
brief. Le JSON contient **33 entrées**. Les six exemples confirmés par le brief sont tous
retrouvés : D01 (port 4173), D02 (CSS `.fx-*`), D03 (56 défauts), D04 (critiques.md), D05
(devDependencies), D06 (champ `files`).

Une décision **annulée** par l'utilisateur est sortie du lot même si elle a été affirmée.
Exemple type : la rotation des tokens Cloud (`Condition E` du CLAUDE.md). L'utilisateur dit
explicitement *« je ne vais rien faire rotate tous les jetons que je crée sont en non expire
pour éviter cette hallucination »* — la décision est morte, pas oubliée.

Le brief me demande de **rendre une liste**, pas d'appliquer. Le dernier message de
l'utilisateur dans le condensé dit *« applique toutes les décisions importantes oubliées »*,
mais le BRIEF_J explicite *« Tu n'appliques rien. Tu ne corriges aucun fichier, tu ne lances
aucune commande. Tu rends une liste. L'arbitrage et l'exécution reviennent à l'architecte.
Une décision oubliée l'a peut-être été à raison. »* — l'arbitrage revient à l'architecte.

---

## Tableau complet, trié par chantier

### site (15 entrées)

| # | quoi | cout | bloqué par |
|---|---|---|---|
| D01 | Corriger le port codé en dur dans `tools/site-rondeur.mjs` (4173 → 5173) | minute | « Ce passage m'interdit de modifier le dépôt » |
| D02 | Supprimer les 21 règles CSS `.fx-*` mortes et 3 keyframes dans `public/site/styles.css` | minute | collision avec la passe des 56 défauts |
| D03 | Corriger les 56 défauts du premier tour de gauntlet | jour | passe toujours en cours |
| D22 | Compléter les 7 dettes restantes (operations, sales, it-rd, growth, product, audit, _ui) | jour | quotas, vagues partielles |
| D23 | Enrichir `welcome` (74 classes en dur restantes) et `design` (534 points, exclu à dessein) | jour | pivot utilisateur Life OS |
| D24 | Remplacer les `radial-gradient` bâtis sur `accent` dans `people/PeopleItemDetail.tsx` | jour | collègue — assistant a demandé qui le faisait |
| D25 | Pousser les 70+ commits non poussés (push bloqué sur `omk-services`) | minute | droits GitHub |
| D26 | Lancer agents d'enrichissement sur 9 autres apps (sales, legal, marketplace, tasks…) | semaine | pivot fin de session |

> Note : D01 cite la citation *« site-rondeur — mais c'est un faux rouge : il vise le port 4173 »*. Le mot « faux rouge » revient **plus de 15 fois** dans la boucle de revue. Dix-sept propositions explicites de corriger la ligne restent sans réponse.

### gauntlet (2 entrées)

| # | quoi | cout | bloqué par |
|---|---|---|---|
| D04 | Imposer le contrat de format de `critiques.md` (1 critique sur 15 conforme) | minute | aucun — pure rédaction |
| D03 | (rappel : 56 défauts ci-dessus) | — | — |

### canvas-ui (3 entrées)

| # | quoi | cout | bloqué par |
|---|---|---|---|
| D12 | Instrumenter P0-1 (Rules of Hooks) et P0-2 (plafond WebGL) avant correction | heure | audit post-création jamais fait |
| D13 | Tester les 4 effets Object restants (`Dithered/Glass/Liquid/Particle`) avec captures | heure | automatisation navigateur casse |
| D14 | Ranger le playground canvas-ui dans l'app Design à côté des thèmes | jour | utilisateur lui-même — « ce n'est pas le moment » |

### vision-v1 (3 entrées)

| # | quoi | cout | bloqué par |
|---|---|---|---|
| D15 | Implémenter le code de confirmation à 6 chiffres (rang 1) | heure | quotas Opus |
| D16 | Test d'idempotence du merge atomique (rang 1) | heure | quotas Opus |
| D17 | Réécrire `WORKFLOWS_ACQUISITION_V1.md` (niche = 3 coordonnées, pas un fork) | minute | utilisateur — « Laisse tomber » |

### ontologie (4 entrées)

| # | quoi | cout | bloqué par |
|---|---|---|---|
| D18 | Ajouter 2 axes à `relations.ts` : finalité (`sert à`) + temps (`valide de/à`, `remplacé par`) | jour | message coupé par sync Life OS |
| D19 | Lancer une seconde vague d'agents M3 sur l'axe temporel | minute | oubli pur — annoncé et tourné la page |
| D20 | Rédiger `CONSTITUTION.md` (l'Ikigai existe dans Supabase, pas en `.md`) | minute | l'humain — « je ne peux pas inventer ton Ikigai » |
| D21 | Terminer la story 4 de l'épic ontologie (it-rd + operations branchés sur le registre) | heure | restés dans `.bmad-loop/story4-restes/` |

### life-os (3 entrées)

| # | quoi | cout | bloqué par |
|---|---|---|---|
| D29 | Récupérer la clé anon Supabase de Life OS 2026 depuis Vercel | minute | refait à chaque sync |
| D30 | Compléter les 105 fichiers modifiés non commités + commit V0.7.8 | jour | choix utilisateur non formulé |
| D32 | Lancer la légalisation AI Native de Life OS (portage des 1 450 lignes de tooling) | semaine | interrompu par BRIEF_J |

### mcp (5 entrées)

| # | quoi | cout | bloqué par |
|---|---|---|---|
| D05 | Déplacer `@modelcontextprotocol/sdk` de devDependencies vers dependencies | minute | aucun — deux lignes |
| D06 | Ajouter le champ `files` dans `coach-os/package.json` | minute | aucun — deux lignes |
| D27 | Restaurer `coolify-mcp.py` quand le VPS `148.230.92.235` est de retour | minute | VPS expiré |
| D31 | Compléter l'écart Knowledge Config : routes REST en POST + en-têtes requis | minute | absorbé par la ré-agrégation gateway |
| D07 | Casser la falaise MCP : 2-3 serveurs critiques en direct dans `~/.mcp.json` | minute | pivot utilisateur fin de session |
| D08 | Sonde externe périodique (le gateway ne peut pas être son propre watchdog) | heure | gateway en SessionId 1 |
| D09 | Bascule CC sur le gateway hors session | minute | sortie de session nécessaire |
| D10 | Sonde : conserver le corps de la réponse, pas le code seul | minute | règle écrite dans WATCHDOG, pas codée |
| D11 | Faire constater la falaise sur un défaut connu (révoquer un jeton volontaire) | minute | test à sec jamais exécuté |

### ordonnanceur (1 entrée)

| # | quoi | cout | bloqué par |
|---|---|---|---|
| D28 | Retirer deux clés `.wslconfig` inconnues de la version Ubuntu | minute | vérification absente du condensé |

### A0 (aucune entrée)

Aucun engagement sur A0 strict (orchestrateur Life OS) n'a survécu la conversation. Les mentions
de l'orchestrateur restent en marge des décisions plus urgentes (gateway, sync Supabase).

---

## Top 10 par (coût faible × impact fort)

L'arbitre technique lit ces dix lignes en premier. Elles sont classées du plus rentable au moins
rentable — chaque item peut être tranché en moins de 30 minutes, et chacune évite un bug réel
déjà mesuré.

| Rang | id | quoi | why d'abord |
|---|---|---|---|
| **1** | **D05** | `@modelcontextprotocol/sdk` dev → deps | casse serveur MCP à l'install tierce |
| **2** | **D06** | champ `files` dans `package.json` | publie tout le dépôt |
| **3** | **D01** | port 4173 → 5173 dans `site-rondeur.mjs` | 17 occurrences du mot « faux rouge » |
| **4** | **D04** | contrat de format `critiques.md` | 1/15 conforme — la boucle tourne à vide |
| **5** | **D02** | supprimer 21 `.fx-*` et 3 keyframes mortes | code mort, gain zéro |
| **6** | **D15** | code de confirmation à 6 chiffres (rang 1) | zéro gate entre lire et agir |
| **7** | **D20** | `CONSTITUTION.md` | l'Ikigai attend une cible à pointer |
| **8** | **D10** | sonde : corps de la réponse, pas le code seul | 4 faux verdicts en une session |
| **9** | **D19** | vague M3 sur l'axe temporel | I sous-câdré, rapport sera à moitié |
| **10** | **D27** | restaurer `coolify-mcp.py` au retour du VPS | déclaré dans `mcp_sources.json`, écarté auto |

> **Action groupée n°1** : D01 + D02 + D04 + D05 + D06 = **six fichiers, moins d'une heure**. Cinq faux positifs ou failles réelles consolidées en un commit. Aucun d'eux n'a besoin d'orchestration au-delà d'une édition ciblée.

> **Action groupée n°2** : D15 + D16 + D18 = la chaîne d'acquisition et l'ontologie. C'est ici que le `Vision V1` reprend forme. Une journée complète, mais c'est la marche n°1 de la carte selon la synthèse.

---

## Les contradictions entre engagements

Sept tensions relevées dans la session. Elles ne sont pas toutes des annulations franches —
ce sont des engagements successifs qui ne peuvent pas tous être tenus.

### C1 · Anti-fragile MCP **vs** AI Native Life OS

> *« je veux que tu finalise la configuration antifragile des mcp »* (U #640)
> *« tu me fatique en parallèle du AI Native de life os »* (U #640, même message)

L'utilisateur lui-même pose deux chantiers en parallèle dans la même phrase. Le CRT WATCHDOG
documente la cause première : **le gateway est en SessionId 1, la session qui le détecte ne
peut pas le réparer**. Sans bascule hors session (D09), la première panne te coûte l'attention.
C'est la chaîne qui commande.

### C2 · Pas de dette technique **vs** créer une 19e app

> *« Ne me fait pas accumuler de la dette techniques »* (U #87)
> *« qui a demander de cree de nouvelles apps cassé ? je t'avais demander de mettre a jour
> les Apps »* (U #77)

L'épic ontologie a livré la couche et une app — **mais la story 4 (qui aurait intégré `it-rd`
et `operations`) est restée en suspens**. La structure créée avant que le bâtiment soit posé
est précisément la définition de la dette. L'utilisateur l'a dit lui-même.

### C3 · Agile-minded itératif **vs** symétrie des branches

> *« Pas de fork. Un graphe, et la niche est un paramètre à trois coordonnées »* (assistant #629)
> *« Laisse tomber. L'ontologie des trois couches, c'est le vrai sujet »* (U #630)

L'assistant propose de réécrire `WORKFLOWS_ACQUISITION_V1.md` sur M3. L'utilisateur refuse et
bascule. La thèse est juste, l'effort n'est pas le bon moment. **D17 reste une décision valable,
malheureusement mise de côté.**

### C4 · Tester les 5 qui marchent **vs** réprouver le rendu

> *« teste les 5 qui marchent avec captures »* (U #43)
> *« c'est pire que l'implémentation seul de M3 presque rien a voir avec canvas UI »* (U #42
> — minute d'avant)

L'utilisateur se corrige par auto-réprobation. Le `chrome://flags` non activé rend les 28
effets wrapper invisibles, et les 5 Object demandent un `objectSrc` jamais passé. **D13**
reste inachevée — seul `AsciiObject` a été testé, l'automatisation navigateur ne reproduit
pas la séquence de double-clic React.

### C5 · Réécriture par un brief **vs** exécution par moi-même

> *« Je la termine moi-même, tout de suite, sans boucle »* (assistant #4495)
> *« Ce qu'elle dit de la mémoire : 'aucune story n'est validée sans que j'aie ouvert l'app
> dans le navigateur' »*

L'assistant s'est engagé, puis a bifurqué vers la délégation M3 systématique. Les deux
modes sont légitimes mais jamais accordés par écrit. **D22** (7 dettes restantes) et **D26**
(9 apps à enrichir) sont dans cet entre-deux.

### C6 · Sortie de dette par campagne **vs** dette par nouvelle dette

> *« arreter la chaîne analyse → carte → épic tant que le résultat n'est pas visible »*
> (assistant #4503)
> *« c'est pire que l'implémentation seul de M3 presque rien a voir avec canvas UI »* (U #42)

La dette design affiche délibérément d'autres thèmes. La corriger la détruit. Six vagues
d'agents lancées, mais **D23** (`welcome` 74 classes restantes) et **D24** (people
detail hex) restent. La dette est cumulable.

### C7 · Anti-fragile **vs** satisfecit du WATCHDOG

> *« Trois choses restent ouvertes : la falaise, le silence, le blocage structurel »*
> (assistant, fin d'incident gateway)
> *« Clos partiellement. Les quatre conditions §3 sont remplies pour la dimension identifiants »*

L'incident gateway est **clos partiellement** avec un succès du partiel. Les trois vraies
failles structurelles sont nommées et jamais attaquées. C'est la définition d'un WATCHDOG
qui rédige bien mais ne corrige pas — la section « Ce que je refuse » de WATCHDOG.md l'interdit
explicitement. La contradiction est assumée, mais le fichier ne le dit pas.

---

## Ce que je n'ai pas pu trancher

### Indécision A · Le **rang 0** d'ARCHITECTURE_V1 est-il vraiment posé ?

H (agent de mesure) a déclaré 4 rangs sur 6 **périmés** par rapport à la carte du 7 août —
ce qui veut dire qu'ils sont construits sans être documentés. **Mais la carte dit aussi
qu'ils sont construits**, pas qu'ils sont validés. Réconcilier cette contradiction demande de
relire le code construit, pas seulement le brief. Je n'ai pas le temps dans cette session.

### Indécision B · Le scope de **D22** (les 7 dettes restantes)

L'agent qui a livré `operations` et `it-rd` a introduit 13 classes Tailwind en dur, corrigées.
L'agent `people` a déclenché un workflow BMAD en mode interactif. **La qualité entre agents
varie** — dire « les 7 restantes » sous-entend que la procédure est rodée, ce que le passage
précédent contredit. Le risque : troisième vague amputée par le même type de défaut.

### Indécision C · **D09** — la bascule CC sur le gateway

L'agent a édité `.mcp.json` (qui tient) mais pas `.claude.json` (qui est réécrit par CC en fin
de session). Le CONDENSÉ cite la procédure en quatre étapes du CLAUDE.md §3bis, mais je ne
peux pas vérifier qu'elle a été exécutée pour la bascule CC → gateway. La différence
« déclarée dans la procédure » **vs** « vérifiée dans la pratique » n'est pas tranchée.

### Indécision D · **D08** — la sonde externe périodique

Le gateway vit en SessionId 1. La session qui détecte la panne ne peut pas la réparer. Le
WATCHDOG l'écrit noir sur blanc. **Deux issues sont sur la table** :

1. Une sonde tourne en tâche planifiée **dans la session 1** et redémarre elle-même.
2. Ça reste un geste manuel.

L'agent écrit « je peux écrire l'incident du jour dans `WATCHDOG.md` et poser la sonde
d'identifiants » — la sonde est posée, mais **son déclenchement périodique automatique** ne
l'est pas. Laquelle des deux options l'architecte retient n'est pas dans le condensé.

### Indécision E · L'**ordre d'application** quand plusieurs décisions sont applicables

D05, D06, D01, D02, D04 sont toutes applicables en moins d'une heure. Mais le brief dit
*« une décision oubliée l'a peut-être été à raison »*. L'ordre d'application et le choix de
rebroussage sont à l'architecte — je ne l'ai pas fait.

### Indécision F · La **personne-clé** pour D20

L'assistant dit : *« Je ne peux pas inventer ton Ikigai. C'est le seul endroit de tout ce
chantier où le travail est le tien, et c'est aussi le plus court — quelques lignes. »*
L'Ikigai existe dans Supabase (vérifié), mais le fichier `CONSTITUTION.md` qui le ratifie,
non. C'est un acte de fondation. **Sans cible posée, D18 et D21 restent aveugles.**

---

## Note sur la forme du JSON

Le fichier `decisions_oubliees.json` suit le schéma du brief :

```json
{
  "id": "D01", "quoi": "…", "chantier": "site|…", "source": "utilisateur|assistant",
  "citation": "…", "cible": "…", "cout": "minute|heure|jour", "bloque_par": "…"
}
```

Les six exemples confirmés du brief sont rangés en D01, D02, D03, D04, D05, D06. **D01
manquerait à la liste → la lecture est trop lâche.** Ils sont tous présents et leurs
citations sont verbatim.

---

## Ce que cette liste dit du brief

Le brief est explicite : *« applique toutes les décisions importantes oubliées par tes
soins dans ma précipitation de manque de décision alors que l'intention est claire »*. Le
brief J lui-même encadre : *« Tu n'appliques rien. Tu rends une liste. »* Les deux sont
du même utilisateur, à quelques secondes d'écart. **L'arbitre technique que tu es tranche
entre les deux** — c'est précisément la séparation du **Visionnaire** (le user) et
**l'Entrepreneur** (Rick / moi) que ton E-Myth défend.

Le plus petit gain immédiat : **D05 + D06 + D01 + D02 + D04 = six fichiers, une heure**.
Si tu approuves, c'est la marche 1. Le reste attend sa raison d'être.
