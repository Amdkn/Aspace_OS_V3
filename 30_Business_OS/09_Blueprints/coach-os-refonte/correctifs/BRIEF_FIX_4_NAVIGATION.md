# FIX-4 — Navigation cassée, titres qui se replient, signaux muets

Lis d'abord `COMMUN.md`, dans ce même dossier. Il fait partie de ce brief.

Ton rapport : `correctifs/RAPPORT_FIX_4.md`

---

## 1 · Welcome — quatre pages sur neuf sont inatteignables

Le plus grave de ton lot.

Le bandeau `PAGES` du canvas, juste sous le fil d'Ariane, n'affiche que **5 onglets sur 9**.
`Finance`, `IT`, `Legal` et `Coach Demo` sont hors du bandeau, sans indicateur de scroll
horizontal : le bandeau est coupé net, rien ne signale qu'il continue. Pour atteindre ces
quatre pages il faut passer par la barre latérale — un utilisateur qui se fie au bandeau
conclut qu'elles n'existent pas.

Constaté sur `OMK RH`, `OMK Operations`, `OMK Growth`, `OMK Cognition`, `OMK People`.

Le bandeau doit rendre ses neuf pages atteignables. Un défilement horizontal **qui se voit**
(dégradé de bord, chevrons, barre visible), ou un repliement sur deux lignes, ou des onglets
plus compacts. Ce qui est exclu : un débordement muet.

## 2 · Welcome — la page active surlignée n'est pas la bonne

Sur `OMK Coach Demo` : la barre latérale marque bien `OMK Coach Demo` comme section active,
mais le bandeau `PAGES` du canvas surligne `OMK RH` en cyan.

Deux sources de vérité pour une seule notion. Le bandeau lit probablement un état local
initialisé au premier onglet, au lieu de lire la section réellement active. Fais-le lire la
même source que la barre latérale.

## 3 · Sales — le titre se replie sur deux lignes

`Sales OS Control Center` passe sur deux lignes (`Sales OS Control` / `Center`) dans les
sections `Context` et `Cognition`, alors qu'il tient sur une seule dans `Today`, `Pipeline`,
`Stack` et `Capabilities`.

La différence vient du bloc de méta à droite, plus large dans ces deux sections
(`Source · The single-source brief · 7 living documents`). Il mange la largeur du titre.

Deux pièges déjà payés sur cette app :

- **`vw` ne mesure pas la carte mais la fenêtre** — un `clamp()` en `vw` ne se déclenche
  jamais dans un conteneur. Utilise des container queries (`containerType: 'inline-size'`
  puis `cqw`) si tu as besoin d'une taille adaptative.
- **`overflow-wrap: anywhere` a coupé `$486k` en `$48` / `6k`.** À proscrire là où il y a des
  chiffres.

Le plus simple ici est sans doute de contraindre la largeur du bloc de méta, pas de rétrécir
le titre.

## 4 · Legal — une échéance dépassée qui ne le dit pas

`legal > Compliance` affiche `Deadline 2026-08-02`, soit quatre jours dans le passé, sans
aucun signal visuel. La règle associée est cochée à 3/5.

Une échéance passée doit se voir : couleur d'alerte, mention explicite (`en retard de N
jours`), icône. Calcule le retard par rapport à la date du jour, pas en dur — cette date
avancera.

## 5 · Audit — un bloc coupé par le bas

`audit > Maturité` : le bloc `03 Déléguer` est coupé en bas de la fenêtre en 1440×900. Il faut
scroller pour voir les trois niveaux (`Discuter`, `Connecter`, `Déléguer`) — alors que les
trois forment un tout qui ne se comprend qu'ensemble.

Resserre le cadrage pour que les trois tiennent à la taille standard, ou rends le fait qu'on
puisse scroller évident.

## 6 · Audit — un titre tronqué dans la barre latérale

`Manuel de Diagnostic IA` devient `Manuel de Diagno…` sur les sept sections. Si la troncature
vient du composant partagé de barre latérale, **c'est FIX-5 qui le possède** : signale-le et
n'y touche pas. Si c'est propre à Audit, corrige.

## Ton périmètre exclusif

```
src/apps/welcome/**
src/apps/sales/**
src/apps/legal/**
src/apps/audit/**
```

Rien d'autre. Pas `src/components/` (FIX-5), pas `src/apps/_ui/` (FIX-1), pas
`src/lib/themes/` (FIX-2), pas `src/apps/finance/` ni `src/apps/product/` (FIX-3).

## Une chose à ne pas défaire dans Welcome

Le contenu de Welcome suit **délibérément** le thème global, à l'inverse des autres apps —
c'est le `GlobalThemedCanvas`, demandé explicitement parce que Welcome n'a pas de pages de
détail où le thème du bandeau supérieur pourrait s'appliquer. La QA a confirmé que ça marche
(« le hero d'Arrivée est noir sur dark-oled, crème sur warm-paper »). Ne touche pas à ce
mécanisme.

## Preuve attendue

Dans `correctifs/preuves/fix4/`, avant et après pour chaque point.

Pour Welcome, la capture après doit montrer les neuf pages atteignables depuis le bandeau, et
une capture sur `OMK Coach Demo` où c'est bien `OMK Coach Demo` qui est surligné.

Pour Legal, la capture doit montrer l'échéance marquée comme dépassée.
