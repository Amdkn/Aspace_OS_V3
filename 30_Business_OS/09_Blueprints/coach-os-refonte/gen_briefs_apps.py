# -*- coding: utf-8 -*-
"""Genere un brief par app a enrichir. Contenu tire de CARTE.md section 3."""
import pathlib
P = pathlib.Path(__file__).parent

REPO = ("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/"
        "05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os")

COMMUN = """
## Ce qu'on corrige

Coach OS a 19 apps qui sont des **coquilles** : trois sections au nom vague, du
contenu de demonstration, aucun modele derriere. Le proprietaire du produit l'a
dit sans detour : « arreter d'avoir des apps basiques dans le projet le plus
ambitieux ».

Soixante-seize conferences ont ete analysees par dix-huit agents pour en tirer
la structure ci-dessous. Ce n'est pas une liste d'idees : c'est ce qui a survecu
a trois filtres — la primitive doit appauvrir les sections existantes si on la
retire, etre portee par au moins deux grappes d'analyse independantes, et
fonctionner pour un expert-comptable comme pour un coach.

**Ton travail : transformer cette structure en sections reelles.**

## Le depot

`{REPO}`

React 19 · TypeScript · Tailwind v4 · Zustand · Vite. Tests : `npm test`
(vitest + jsdom). Type-check : `npx tsc --noEmit -p tsconfig.app.json` — la
reference est **79 erreurs preexistantes**, ne la depasse pas.

## Le motif d'une app — a suivre exactement

Lis `src/apps/operations/OperationsApp.tsx` en entier avant d'ecrire une ligne.
Tu y verras :

- `const sections: AppSection[] = [{ id, label, icon, render }, ...]` passe a
  `<AppFrame title=... subtitle=... icon=... accent=... sections={sections} />` ;
- des composants de rendu locaux (`Runbooks`, `Knowledge`, `Incidents`) ;
- `CMSCardList` (`src/apps/_ui/CMSCardList.tsx`) pour les grilles de cartes ;
- `registerItemDetail('<appId>', <Composant>)` pour les pages de detail ;
- `useCmsStore` (`src/lib/cms/cms.store.ts`) pour les collections de contenu.

Un exemple de section moderne, deja branchee sur un registre reel :
`src/apps/_ui/ontology/OntologySection.tsx`, utilisee par `it-rd` et
`operations`. Elle montre comment lire une source unique plutot que de recopier
des donnees.

## Regles de contenu — c'est ici que tout se joue

1. **Aucune section vide.** Chaque section rend quelque chose de structure : une
   grille de cartes, un tableau, une liste d'etats. Une section qui affiche
   « bientot disponible » est un echec de cette tache.
2. **Des donnees de demonstration credibles et coherentes**, posees dans un
   fichier `<app>/seed.ts` a part — jamais melangees au composant. Entre 4 et 8
   entrees par section. Elles doivent raconter un metier plausible, pas
   `Lorem ipsum` ni `Item 1 / Item 2`.
3. **Chaque carte ouvre un detail.** Une grille qui ne mene nulle part est une
   image. Utilise le motif `registerItemDetail` deja en place dans l'app.
4. **Variables de theme, jamais de palette Tailwind en dur.** Utilise
   `var(--theme-text)`, `var(--theme-muted)`, `var(--panel-border)`,
   `var(--theme-surface)`, `var(--theme-surface-hover)`. Un epic precedent vient
   de corriger 385 usages ; ne reintroduis pas le defaut. Exception admise : une
   couleur qui porte un SENS (vert = succes, rouge = incident).
5. **Reutilise ce qui existe** — `CMSCardList`, `SectionHead`, les composants de
   `src/apps/_ui/`. N'invente pas un second systeme de cartes.

## Interdits

1. Ne modifie **aucune autre app** que la tienne, ni `src/lib/ontology/`, ni
   `src/components/AppFrame.tsx`, ni `src/lib/app-discovery.ts` (sauf si ta
   tache le dit explicitement).
2. N'ajoute **aucune dependance**.
3. Ne supprime aucune section existante. Tu ajoutes.
4. Pas de `git commit`, pas de `git push`.
5. Ne touche pas a `src/components/canvasui/`.

## Verification obligatoire avant de rendre

```
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
npm test
```

Rapporte les deux chiffres. Si le compte TS depasse **79**, tu as introduit une
regression : corrige-la avant de rendre.

## Rapport attendu

En fin de session, liste : les sections ajoutees, les fichiers crees, les deux
chiffres de verification, et tout point que tu n'as pas pu faire avec la raison.
Un point non fait et signale vaut mieux qu'un point bacle en silence.
"""

APPS = {
"operations": dict(
  fichier="src/apps/operations/OperationsApp.tsx",
  actuel="Runbooks · Knowledge Base · Incidents",
  accent="#4f46e5",
  cible="""
Ajoute ces **quatre** sections (garde les trois existantes) :

- **Processus** — la cartographie des processus de l'organisation et leurs
  dependances. Chaque processus : un nom, un proprietaire, ses entrees, ses
  sorties, les processus dont il depend. Une carte ouvre un detail montrant ses
  cas limites connus (« quand ca casse, on fait quoi »). C'est la primitive la
  plus corroboree du corpus : sans carte des processus, les runbooks sont des
  documents isoles.

- **Benchmarks** — les tests qui savent dire non. Chaque entree : ce qu'elle
  verifie, sa difficulte visee, son taux de reussite actuel, sa derniere
  execution. Un benchmark qui ne peut pas echouer n'est pas un benchmark : rends
  visible le statut `passe / echoue / instable`.

- **Changements** — la file des modifications proposees par les agents, en
  attente de decision humaine. Chaque entree : ce qui change, pourquoi, le
  risque estime, et la politique qui s'applique. Trois etats :
  `propose / approuve / rejete`.

- **Alertes** — les incidents **pre-enrichis a froid** : quand une alerte
  arrive, elle contient deja les traces, un extrait de code ou de log,
  l'hypothese de l'agent et son evaluation du risque. La personne d'astreinte
  n'ouvre plus un ticket vide. Distingue `enrichi / brut` sur chaque entree.
"""),

"it-rd": dict(
  fichier="src/apps/it-rd/ItRdApp.tsx",
  actuel="Kernel · Experiments · Deploys · Ontology (ajoutee ce jour, NE PAS LA TOUCHER)",
  accent="#7c3aed",
  cible="""
Ajoute ces **quatre** sections (garde les quatre existantes, dont `Ontology`
que tu ne modifies sous aucun pretexte) :

- **Journal** — un log en ajout seul, et l'etat qu'on en projette. Chaque entree
  : horodatage, acteur (humain ou agent), action, entite touchee. L'interet est
  qu'on peut rejouer : montre l'etat projete a cote du flux brut.

- **Boucles** — chaque boucle de retroaction du systeme, decrite par ses quatre
  organes : capteur (ce qui mesure), consigne (la valeur visee), controleur
  (ce qui decide), actionneur (ce qui agit). Plus son etat : `stable / derive /
  arretee`. Sans boucle, une metrique n'a personne pour la corriger.

- **Drift** — l'ecart entre le modele tel qu'il a ete specifie et tel qu'il se
  comporte. Chaque entree : la mesure, sa valeur de reference, sa valeur
  courante, la date de detection. Un seuil visible qui dit quand alerter.

- **Evals** — les evaluations du systeme : taux de reussite sur N essais,
  distribution des resultats, cas d'echec explicables. Distingue ce qui est
  mesure automatiquement de ce qui attend une revue humaine.
"""),

"people": dict(
  fichier="src/apps/people/PeopleApp.tsx",
  actuel="Overview · Team · Agents · Squads · Content · Cadence · Culture",
  accent="#0891b2",
  cible="""
Cette app a deja sept sections, dont `Cadence`. Ajoute ces **trois** :

- **Personas** — des profils synthetiques de premiere classe, pas des vues sur
  les personnes existantes. Chaque persona : son nom, ce qu'il veut, ce qui le
  bloque, son vocabulaire, et surtout son **ancrage** — la source reelle dont il
  est tire (entretien, appel, ticket). Un persona sans ancrage est une invention
  ; rends l'absence d'ancrage visible.

- **Memoire** — la memoire curee de l'organisation, avec son hygiene. Chaque
  entree : le fait retenu, sa provenance, sa date, et son statut de verification
  (`confirme / contredit / a verifier`). La memoire brute est un depotoir ; ce
  qui compte ici est ce qui a ete verifie.

- **Codex** — les motifs qui ont fait leurs preuves. Chaque entree : la
  situation, ce qu'on fait, pourquoi ca marche, et combien de fois ca a ete
  applique. C'est ce qui transforme une reussite ponctuelle en methode.

Ne touche pas aux sept sections existantes.
"""),
}

for app, a in APPS.items():
    txt = ("# BRIEF — enrichir l'app `%s`\n\n"
           "Tu es un developpeur front. Tu ajoutes des sections a UNE app existante,\n"
           "avec du contenu structure et une page de detail par element.\n\n"
           "**Ton fichier principal** : `%s`\n"
           "**Sections actuelles** : %s\n"
           "**Accent de l'app** : `%s`\n"
           % (app, a["fichier"], a["actuel"], a["accent"])
           + COMMUN.replace("{REPO}", REPO)
           + "\n## Les sections a ajouter\n" + a["cible"])
    (P / ("BRIEF_APP_%s.md" % app)).write_text(txt, encoding="utf-8")
    print("BRIEF_APP_%-12s %6d car." % (app + ".md", len(txt)))
