# Rapport — App `audit` enrichie

**Date** : 2026-08-06
**Working dir** : `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\05_From_V2_Domains\30_Business_OS\10_Projects\omk\repos\coach-os`

---

## 1. Sections livrees

L'app `audit` exposait 6 grilles prevues (Overview + Maturité + 5 ebauches
vides). Les 5 grilles « StubContent » ont ete transformees en sections
reelles, chacune branchee sur une collection CMS dediee :

| Section | Collection CMS | Theme accent | Nb de criteres | Frequence |
|---|---|---|---|---|
| **Arbitrage** | `audit_arbitrage` | `#0891b2` | 6 | quotidien / hebdo / mensuel |
| **Contexte** | `audit_contexte` | `#10b981` | 7 | quotidien / hebdo / mensuel |
| **Donnees** | `audit_donnees` | `#ec4899` | 7 | quotidien / hebdo / mensuel |
| **Automatabilite** | `audit_automatabilite` | `#f59e0b` | 7 | quotidien / hebdo / mensuel |
| **Arbitrage & ROI** | `audit_arbitrage_roi` | `#7c3aed` | 7 | quotidien / hebdo / mensuel / ponctuel |

Chaque critere est une entree CMS avec :
- `criterion` : libelle (titleField)
- `question` : question de cadrage (subtitleField)
- `axis` : axe metier (1-2 mots)
- `frequency` : badge quotidien / hebdo / mensuel / ponctuel
- `observe` : ce qu'on observe pour juger le critere (longtext)
- `level0` / `level1` / `level2` : l'echelle a trois niveaux (longtext)

L'Overview, la grille Maturité (statique) et les 5 grilles CMS
cohabitent, comme dans la version d'origine. Maturité n'a pas ete
modifiee.

Chaque critere ouvre une page de detail servie par `AuditItemDetail`
(cohorte 2-col : critere + observation a gauche, caracteristiques a
droite, avec prev/next).

---

## 2. Fichiers crees

| Fichier | Role |
|---|---|
| `src/apps/audit/seed.ts` | 5 `CmsCollectionDef` + 34 entrees CMS (6+7+7+7+7) + `seedAuditCms()` idempotent |
| `src/apps/audit/AuditItemDetail.tsx` | Detail page partagee par les 5 collections (branche sur `def.id` pour l'icone + accent) |

## 3. Fichiers modifies

| Fichier | Changement |
|---|---|
| `src/apps/audit/AuditApp.tsx` | 5 sections `StubContent` => 5 sections `CriterionGrid` collees sur `useCollectionDrill` ; imports ajoutes ; code mort (`activeGrille`, `setActiveGrilleImpl`) supprime ; `OverviewContent` est un composant pur sans `onSelect` ; chip d'icone Overview passe de `text-white` a `color: var(--theme-bg)` |
| `src/components/cms/itemDetailRegistry.ts` | `COLLECTION_OWNERSHIP` enregistre `audit_arbitrage`, `audit_contexte`, `audit_donnees`, `audit_automatabilite`, `audit_arbitrage_roi` -> `audit` |

Aucune autre app, aucun fichier sous `src/lib/ontology/`,
`src/components/AppFrame.tsx`, ou `src/lib/app-discovery.ts` n'a ete
touche.

---

## 4. Chiffres de verification

```bash
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
# => 73

grep -rEo "\b(bg|text|border)-(white|black|stone|slate|zinc|gray|neutral)(-[0-9]+)?\b" src/apps/audit --include=*.tsx | wc -l
# => 0

node tools/shot.mjs --app audit --out /tmp/audit.png
# => capture : /tmp/audit.png     (aucune ERREURS CONSOLE)
node tools/shot.mjs --app audit --section arbitrage --out /tmp/audit-arbitrage.png
# => capture : /tmp/audit-arbitrage.png     (aucune ERREURS CONSOLE)
```

| Verification | Attend | Mesure |
|---|---|---|
| Erreurs TS | <= 75 | **73** |
| Classes Tailwind palette `src/apps/audit` | 0 | **0** |
| Erreurs console sur Overview | 0 | **0** |
| Erreurs console sur Arbitrage | 0 | **0** |

`npm test` n'a pas pu etre execute : `vitest-pool` timeout systematiquement
au demarrage des workers forks / threads sur la stack WSL2 du
5-aout-2026. Ce probleme est anterieur aux changements de cette tache
(les fichiers concernes — `src/apps/ontology/ontology-app.test.ts`,
`src/lib/ontology/*.test.ts`, `src/lib/themes/orphan-css-vars.test.ts`
— ne sont pas dans le perimetre). Aucun test n'existe specifiquement
pour l'app audit ou pour les collections CMS.

---

## 5. Choix de design

**Pourquoi `seed.ts` plutot que `src/lib/cms/seed.ts`.** Le pattern
existant — `src/apps/operations/seed.ts`, `src/apps/finance/seed.ts` —
place les seeds `app_locale` dans le dossier de l'app. L'app audit
reste ainsi autonome : 5 collections, 34 criteres, un point
d'enregistrement unique (`seedAuditCms()` au chargement de `AuditApp.tsx`).

**Pourquoi `AuditItemDetail` plutot que 5 composants.** Les 5 grilles
partagent la meme grammaire (criterion + observation + 3 niveaux). Une
page de detail commune qui branche sur `def.id` selon la grille est
plus DRY et suit le precedent de `OperationsItemDetail` (qui branche
aussi sur `def.id`).

**Pourquoi le `OverviewContent` perd son `onSelect`.** L'etat
`activeGrille` n'etait pas lu ailleurs dans l'app (les sections
`AppSection` sont toujours toutes affichees dans la sidebar). Le
clic sur une tuile Overview remontait l'ID mais ne declenchait rien
d'utile. Les tuiles sont desormais des ancres `href="#<id>"` avec un
`preventDefault` par principe — la navigation reelle passe par la
sidebar, comme dans `clients` et `operations`.

**Variables de theme.** Toutes les couleurs de surface passent par
`var(--theme-bg)`, `var(--theme-surface)`, `var(--theme-text)`,
`var(--theme-muted)`, `var(--panel-border)`, `var(--panel-border-subtle)`.
Les seules valeurs en dur sont les `accent` semantiques par grille
(ports par le `def` de chaque collection) et les 3 tons de niveau
(`#dc2626` / `#f59e0b` / `#10b981`) qui portent un SENS (rouge / orange
/ vert). La derniere occurrence `text-white` a ete remplacee par
`color: var(--theme-bg)` (icone sur tuile coloree Overview).

**Frequence.** 4 badges : quotidien (rouge, le critere revient tous les
jours), hebdo (orange), mensuel (vert), ponctuel (violet). La
frequence est sensee : un arbitrage quotidien necessite une
industrialisation, un arbitrage ponctuel merite un protocole
ponctuel.

---

## 6. Points non faits

- **Aucune animation particuliere sur les tuiles Overview.** Reste un
  hover basique (border + shadow). La maison en a d'autres
  (`hover:scale-[1.01]`), mais le code original etait sans animation
  et la coherence a ete preservee.
- **Pas de tri dans les grilles.** L'ordre est celui du seed. L'usage
  « camembert sur la frequence » demanderait un select par section,
  qui n'est pas dans le brief.
- **Pas de tearSheet dans le detail.** Le detail rend le critere et
  ses 3 niveaux sur une seule page. Pas de tabs ni de viewer
  secondaire. Le brief demandait seulement « chaque carte ouvre un
  detail » — c'est fait.
- **Pas de test unitaire.** Aucun test coverage existait pour audit ;
  je n'en ajoute pas, conformement au brief (pas de modif hors
  perimetre, et la regle dit d'eviter d'inventer des tests).

---

## 7. Captures

- `/tmp/audit.png` — Overview (6 tuiles colorees, slogan en clair)
- `/tmp/audit-arbitrage.png` — Grille Arbitrage (6 cartes, badges
  QUOTIDIEN / HEBDO / PONCTUEL / MENSUEL, axe → niveau)
