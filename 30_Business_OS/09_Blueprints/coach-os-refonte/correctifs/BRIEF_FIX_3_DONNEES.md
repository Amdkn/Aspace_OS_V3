# FIX-3 — Ce que l'interface affiche et qui est faux

Lis d'abord `COMMUN.md`, dans ce même dossier. Il fait partie de ce brief.

Ton rapport : `correctifs/RAPPORT_FIX_3.md`

---

Les défauts de cette famille se ressemblent : l'interface montre quelque chose qui n'est pas
vrai. Un `undefined`, un compteur qui ne compte pas ce qu'il affiche, un graphique vide alors
que les données existent. C'est la famille la plus grave — une troncature se voit, un chiffre
faux se croit.

## 1 · `undefined` affiché à l'écran — bloquant

**clients > IP Vault**, les deux thèmes. Les quatre fiches portent `undefined` en guise de
titre, à la place du titre de la note de session.

**operations > Knowledge Base**, les deux thèmes. Sous chaque fiche : `citations undefined
this month`.

Deux causes possibles à trancher, et elles n'appellent pas le même correctif :

- le champ est **absent du seed** → complète le seed avec une valeur plausible ;
- le champ existe mais **le binding vise le mauvais nom** → corrige le binding.

Ne te contente pas de masquer le `undefined` derrière un `?? ''`. Un champ vide silencieux
remplace un bug visible par un bug invisible. Si la donnée n'existe vraiment pas, affiche une
absence assumée (`—`, ou pas de ligne du tout), et dis-le dans ton rapport.

## 2 · Compteurs qui mentent

**product > Backlog** : le badge d'en-tête annonce `3`, la grille affiche `6` cartes — et ces
six viennent de tous les stages confondus (NOW ×2, NEXT ×2, LATER ×1, BACKLOG ×1). Le compteur
appelle `byStage('backlog').length`, la grille ne filtre pas. Un commentaire dans le code
(`emptyMessage="No backlog items yet."`) montre que le filtre était prévu.

**product > Specs** : badge `8`, six cartes visibles. Même famille.

Tranche dans le bon sens : **la grille doit être filtrée**, et le compteur compter ce qui est
affiché. L'inverse — gonfler le compteur pour qu'il colle à six cartes non filtrées — donnerait
une section Backlog qui montre des items déjà livrés.

## 3 · Titres vides

**product > Releases** : les trois cartes SHIPPED affichent `—` en titre, sans date de
livraison. Seul `version v0.X` apparaît. Le seed ne porte probablement ni titre ni date.
Complète-le : une release a un nom et une date.

## 4 · Graphique entièrement vide — le plus visible

**finance > Runway**, les deux thèmes. Douze mois en abscisse, la légende `Cash on hand`
présente, **aucune barre rendue**. Les données sont pourtant dans le code :
`[42, 40, 39, 37, 36, 34, 33, 31, 30, 28, 27, 25]`.

Le conteneur est dessiné, le contenu est absent. Cherche du côté d'une hauteur de conteneur à
zéro, d'une échelle mal calculée (division par un maximum indéfini), ou d'un SVG sans
`viewBox`. Un graphique vide qui affiche sa légende est presque toujours un problème de
dimensionnement, pas de données.

## 5 · Deux détails de texte, même dossier

**finance > Formes** : le titre affiche `Formesde prix` — l'espace manque entre `Formes` et
`de prix`. Probablement une concaténation sans séparateur.

**finance > Overview** : le sous-titre `Wonder Woman Domain` est tronqué en
`WONDER WOMAN DOM…` dans la barre latérale. Il manque cinq caractères. Si c'est le composant
partagé de barre latérale qui tronque, **c'est hors de ton périmètre** (il appartient à FIX-5)
— signale-le dans ton rapport et n'y touche pas. Si c'est propre à Finance, corrige.

## Ton périmètre exclusif

```
src/apps/finance/**
src/apps/product/**
src/apps/clients/**
src/apps/operations/**
```

Rien d'autre. Attention en particulier :

- `src/apps/_ui/FleetItemCard.tsx` appartient à **FIX-1**. Tu vas le croiser (clients et
  operations le consomment). N'y touche pas — si un `undefined` vient de lui, dis-le.
- `src/components/` appartient à **FIX-5**.
- Les troncatures de titres de cartes dans operations et clients appartiennent à **FIX-1**.
  Toi, tu ne t'occupes que des données.

## Preuve attendue

Une capture après pour chaque point, dans `correctifs/preuves/fix3/`. Sur celle d'IP Vault,
les quatre titres réels doivent être lisibles. Sur celle de Runway, les douze barres doivent
être dessinées, avec une décroissance visible de 42 à 25.

Pour les compteurs, la capture doit montrer le badge **et** la grille dans le même cadre — un
badge `3` au-dessus de trois cartes.
