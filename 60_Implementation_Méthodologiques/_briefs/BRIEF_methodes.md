# BRIEF — convertir les deux methodes en concepts OKF appliques

## Ton perimetre EXCLUSIF en ecriture

```
C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/prompt-systeme/
C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/autonomie-agents/
C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_briefs/RAPPORT_methodes.md
```

**Aucun autre fichier.** Tu ne touches ni a `50_Distillation/`, ni aux
`CLAUDE.md` du poste, ni a quoi que ce soit dans `ASpace_OS_V2/`.

## Ce que tu lis

```
C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_sources/indydevdan-prompt-systeme.md     (extraction video 1)
C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_sources/echelle-autonomie-agents.md      (extraction video 2)
C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/index.md                                  (ce que le bundle vise)
C:/Users/amado/CLAUDE.md                      (le canon du poste — LECTURE SEULE)
C:/Users/amado/.claude/CLAUDE.md              (le canon global — LECTURE SEULE)
```

## Le travail

Les deux fichiers de `_sources/` portent deja les principes. **Ton travail
n'est pas de les resumer** — ils sont deja denses. Ton travail est de les
**convertir en concepts appliques a ce poste**.

Un concept utile ici repond a trois questions :

1. **Quel principe** — avec sa source, videe de son emballage marketing.
2. **Quel est l'ecart** entre ce principe et ce que fait le poste aujourd'hui —
   les deux fichiers `_sources/` contiennent chacun un tableau d'ecart mesure,
   pars de la.
3. **Quel geste** comble l'ecart — concret, verifiable, faisable sans acheter
   ni installer quoi que ce soit.

Un concept qui s'arrete a la question 1 est un resume de video. On n'en veut
pas.

## Priorites, dans cet ordre

Les deux extractions nomment ce qui manque. Le plus rentable d'abord :

- **L'examen** (video 2, chantier 2). Le poste a `vitest`, deux `tsc` et
  `oxlint`, mais **aucune commande unique ne les enchaine**, et rien n'oblige un
  agent a la lancer avant de rendre. C'est le chantier le plus rentable :
  ecris le concept qui le specifie, y compris la commande exacte et ce qu'elle
  doit rendre en cas d'echec.
- **Les quatre sections manquantes du prompt systeme** (video 1) : patterns
  positifs/negatifs, points de reference, alias, exemples. Un concept par
  section, avec le contenu propose pour ce poste — pas une description de ce
  que serait la section.
- **L'agent relecteur** (video 2, chantier 4). Absent ici : c'est Opus qui
  relit, et il a parfois ecrit le code. Specifie le mandat d'un relecteur neuf.
- **Les bacs a sable** (video 2, chantier 3). Le cloisonnement actuel tient a la
  discipline du brief, pas a l'outil. Dis ce que `git worktree` changerait, et
  ce qu'il couterait.
- **Goodhart et le compteur de jetons** (video 2). Le poste a une doctrine
  d'economie de quota. Elle risque exactement le travers decrit : une mesure
  devenue objectif. Ecris le garde-fou.

## Ce qu'on attend

**12 concepts OKF v0.2 au minimum**, repartis entre les deux sous-bundles selon
leur nature, en `kebab-case.md`.

Mets a jour l'`index.md` de chaque sous-bundle : une ligne par concept.

## Une exigence particuliere

Les deux videos **ne tirent pas dans le meme sens** : l'une optimise la qualite
d'une reponse, l'autre la quantite de travail delegue. Un prompt systeme tres
contraint coute du temps a ecrire ; un essaim lance vite produit plus, moins
bien.

**Ne lisse pas cette tension.** Au moins un de tes concepts doit la traiter de
front et dire comment on tranche, cas par cas.

## Ton rapport

`C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_briefs/RAPPORT_methodes.md`. Il dit ce que tu as ecrit, ce que tu as
laisse de cote et pourquoi, et les endroits ou les deux sources se contredisent.
