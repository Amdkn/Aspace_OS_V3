# FIX-1 — La troncature des titres de cartes

Lis d'abord `COMMUN.md`, dans ce même dossier. Il fait partie de ce brief.

Ton rapport : `correctifs/RAPPORT_FIX_1.md`

---

## Ce que la QA a trouvé

Une trentaine de défauts répartis sur huit apps, tous de la même forme : le titre d'une carte
est coupé à quelques lettres suivies de `…`, ce qui rend la grille illisible sans cliquer.

| app | sections touchées | échantillon |
|-----|-------------------|-------------|
| dashboard | Integrations | `M…`, `S…`, `G…` — 6 cartes sur 6, titres réduits à **1 lettre** |
| dashboard | Wind Direction | `Validation devi…`, `Retard livrais…`, `Mise à jour Stri…` |
| dashboard | Client Pipeline | `Citadelle — high tic…`, `Programme — 12 w…`, `Atelier Bric…` |
| operations | Runbooks, Incidents, Processus, Benchmarks, Changements, Alertes | `Client onb…`, `Egress attemp…`, `Add tag-based se…` |
| tasks | Definition of Done, Comparateur, Actions exposées | `Onboarding to…`, `Voice-clone v2…` |
| clients | Directory | `Atelier Bric…` |
| settings | Canvas FX | `BUBBL`, `FORCEF`, `DECRYP` — coupés **sans** `…`, on dirait des noms mal saisis |
| dashboard | Sessions | le tableau déborde à droite, dernière colonne coupée, pas de scroll |
| dashboard | Kill Switches | `cost cap per s…` |
| dashboard | Usage | carte TRAJECTOIRE coupée à droite |
| dashboard | Knowledge | panneau étroit, titre sur 3 lignes, question tronquée |

Reproduit à l'identique sous `warm-paper` et sous `dark-oled` : **ce n'est pas le thème,
c'est la mise en page.**

## La cause, déjà localisée

`src/apps/_ui/FleetItemCard.tsx` — les lignes 79, 84, 144, 149 posent `truncate` sur le titre
et le sous-titre. `truncate` en Tailwind, c'est `overflow:hidden` + `text-overflow:ellipsis` +
**`white-space:nowrap`**. Une seule ligne, quoi qu'il arrive.

La grille (ligne 192) est en `sm:grid-cols-2` : à 1440 px de large, dans une fenêtre d'app qui
n'occupe pas tout l'écran, chaque colonne reçoit quelques centaines de pixels. Une carte porte
en plus une icône de 44 px, une pastille de statut et des gouttières. La largeur qui reste au
titre est dérisoire, et `nowrap` interdit d'aller à la ligne.

C'est ce fichier qui explique operations, tasks, clients, et la majeure partie du dashboard —
il est consommé par `CMSCardList`, lui-même utilisé par huit apps.

## Ce que je te demande

**Le titre d'une carte doit être lisible en entier, ou sur deux lignes, jamais amputé à une
lettre.** `line-clamp-2` plutôt que `truncate` sur les titres est la piste évidente ; à toi de
juger au cas par cas. Un sous-titre peut rester sur une ligne s'il en reste assez pour
comprendre.

Trois pièges déjà payés dans ce dépôt, ne les repaie pas :

- **`vw` ne mesure pas ce que tu crois.** Une unité `vw` mesure la fenêtre du navigateur, pas
  la carte. Un `clamp()` en `vw` posé dans une carte ne se déclenche jamais. Utilise les
  **container queries** (`containerType: 'inline-size'` sur le parent, puis `cqw`) si tu as
  besoin d'une taille qui suit la carte.
- **`overflow-wrap: anywhere` casse les nombres.** Appliqué à une carte, il a coupé `$486k`
  en `$48` / `6k`. À proscrire sur tout ce qui porte un chiffre.
- **Élargir la carte n'est pas la seule issue.** Passer une grille de 2 à 1 colonne rend la
  page interminable. Deux lignes de titre coûtent moins cher.

Pour `settings > Canvas FX`, le symptôme est différent et plus grave : les noms sont coupés
**sans ellipse**, ce qui fait passer une troncature pour une faute de frappe. Rends la tuile
assez large, ou mets le nom sur deux lignes.

Pour `dashboard > Sessions`, un tableau qui déborde sans scroll horizontal : soit tu rends le
conteneur scrollable et ça se voit, soit tu réduis le nombre de colonnes. Un débordement muet
est le pire des deux mondes.

## Ton périmètre exclusif

```
src/apps/_ui/FleetItemCard.tsx
src/apps/_ui/CMSCardList.tsx
src/apps/dashboard/**
src/apps/settings/**
```

Rien d'autre. En particulier : pas de `src/components/`, pas de `src/lib/themes/`, pas les
autres dossiers d'apps — même si tu y vois le même défaut. `FleetItemCard` étant partagé, le
corriger là suffit à réparer operations, tasks et clients sans y toucher.

Note aussi que `FleetItemCard` code en dur `bg-white`, `text-stone-900`, `text-stone-500`,
`text-stone-700`. Ces couleurs figées ignorent le thème. **Tu peux les brancher sur les
variables de thème** (`var(--theme-text)`, `var(--theme-text-dim)`, `var(--panel-bg)` — vérifie
les noms exacts dans `src/lib/themes/tokens.ts` avant d'écrire) : c'est le même fichier, c'est
ton périmètre, et ça règle une partie du défaut de contraste. Si tu le fais, capture les huit
apps consommatrices sous les deux thèmes pour prouver que tu n'as rien cassé ailleurs.

## Preuve attendue

Pour chaque ligne du tableau ci-dessus, une capture avant et une capture après, dans
`correctifs/preuves/fix1/`. Le titre complet doit être lisible sur la capture après.

Vérifie aussi les sections que la QA avait jugées saines et qui consomment `FleetItemCard`
(people, growth, product, audit, finance) : ton correctif les traverse, il ne doit pas les
abîmer. Une capture par app suffit.
