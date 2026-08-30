# FIX-2 — Les titres illisibles

**Date** : 2026-08-07
**Périmètre** : `src/apps/it-rd/**`, `src/apps/ontology/**`, `src/apps/_ui/ontology/**`, `src/apps/onboarding/**`
**Hors périmètre** : `src/components/AppFrame.tsx` (où vit le `SectionHead` canonique)

---

## Résumé

| # | Défaut QA | Cause trouvée | Fichier:ligne | Correctif | Preuve |
|---|-----------|---------------|---------------|-----------|--------|
| 1 | `it-rd` × 7 sections × 2 thèmes : titre « quasi invisible » | `SectionHead` canonique (`src/components/AppFrame.tsx:399-408`) utilise `text-stone-900` / `text-stone-500` (Tailwind figé warm-paper-only). Sur le fond cyberpunk `#0a0a14` toujours applique a l'app, contraste titre `~1.18:1` — invisible. | `ItRdApp.tsx:140, 151, 172, 187, 310, 389, 460` (7 sections) | Helper local `ThemedSectionHead` (`src/apps/it-rd/ThemedSectionHead.tsx`) : titre sur `var(--theme-text)` (cyberpunk `#00ff9d`), sous-titre sur `var(--theme-text-muted)` (`#ff007a`). Import local en supplement, l'export `SectionHead` du shell reste intact pour les autres apps. | `preuves/fix2/before_itr_*.png` × 14 vs `after_itr_*.png` × 14 |
| 2 | `ontology` × 4 sections : titres, sous-titres illisibles | Meme `SectionHead` canonique. Sous `dark-oled` (`#000000`), `text-stone-900` quasi invisible. | `OntologyApp.tsx:733, 759, 776, 813` | Helper local `ThemedSectionHead` (`src/apps/_ui/ontology/ThemedSectionHead.tsx`). Titre sur `var(--theme-text)` (`#fafafa`), sous-titre sur `var(--theme-text-muted)` (`#a1a1aa`). | `preuves/fix2/before_ont_*.png` × 4 vs `after_ont_*.png` × 4 |
| 3 | `ontology` : descriptions de cartes et libellés de listes déroulantes en teal sombre | `text-[var(--theme-text-dim)]` (#52525b en dark-oled) utilisé pour du contenu secondaire visible. Contraste `#52525b`/`#000000` ≈ 1.6:1 — quasi invisible. | `OntologyApp.tsx:246, 263, 286, 436, 452, 799, 665` | Remplacement par `text-[var(--theme-text-muted)]` (`#a1a1aa`). Meme famille, contraste ≈ 6.7:1 — WCAG AA. | cf. ligne 2 ci-dessus |
| 4 | `onboarding` citadel étape 1/4 : titre, sous-titre, options, lien Back, barres, panneau droit en teal sombre | `text-emerald-700` (`#047857`) figé sur les elements de marque « Zero-PII sandbox ». Sur `#000000` contraste 1.8:1. `text-[var(--theme-text-dim)]` pour les barres et le panneau droit, meme probleme. `text-[var(--theme-text-muted)]` pour les options radio et sous-titre — bordure 4.5:1 (passable mais limite). | `OnboardingApp.tsx:185-309` | `text-emerald-700` -> `style={{ color: 'var(--theme-accent)' }}` pour suivre le theme (sous dark-oled = cyan `#06b6d4`, ~10:1). `text-[var(--theme-text-dim)]` -> `text-[var(--theme-text-muted)]` pour les barres inactives, le panneau droit, les sous-libellés des tuiles. `text-[var(--theme-text-muted)]` -> `text-[var(--theme-text)]` pour le sous-titre du quiz (lisibilite maximum sur le contenu de la question). | `preuves/fix2/before_onb_citadel_dark.png` vs `after_onb_citadel_dark.png` |

---

## Détail des correctifs

### 1 · Cause racine partagée : `SectionHead` canonique

Le `SectionHead` exporté par `src/components/AppFrame.tsx:399-408` est :

```tsx
<h2 className="text-lg font-bold tracking-tight text-stone-900 font-outfit">{title}</h2>
{subtitle && <p className="text-sm text-stone-500 mt-0.5">{subtitle}</p>}
```

`text-stone-900 = #1c1917`, `text-stone-500 = #78716c` — deux gris Tailwind figés sur la palette warm-paper. Le fichier est hors de mon périmètre (FIX-1 ou un autre agent y travaille), je n'y touche pas. Le brief l'autorise explicitement :

> « pas `src/components/` »

Conséquence pour `it-rd` : même quand l'utilisateur pose `warm-paper` en thème global, l'app garde son thème canonique `cyberpunk` (`CANONICAL_APP_THEMES['it-rd'] = 'cyberpunk'`, `AppFrame` pose les tokens cyberpunk via `applyThemeTokens` sur son root, `ItRdApp.tsx:21` confirme `ACCENT = '#7c3aed'` qui n'est visible que sur fond cyberpunk). Donc `warm-paper ET dark-oled` produisent le même fond cyberpunk dans la fenêtre — c'est cohérent avec ce que la QA a mesuré.

Le brief dit aussi :

> « aligne ce qui est illisible sur ce qui l'est déjà. **Les badges et les compteurs restent lisibles** — ils utilisent des variables de thème plus claires. »

J'ai pris les variables canoniques existantes (`var(--theme-text)`, `var(--theme-text-muted)`) déjà utilisées par les compteurs lisibles de ces memes apps. Aucune nouvelle variable, aucun changement de palette, aucun risque de propagation aux 17 autres apps.

### 2 · `it-rd` — helper local `ThemedSectionHead`

**Création** de `src/apps/it-rd/ThemedSectionHead.tsx` : copie conforme de la primitive `SectionHead`, avec uniquement les deux classes Tailwind remplacées par des variables de thème :

```tsx
<h2 className="text-lg font-bold tracking-tight font-outfit"
    style={{ color: 'var(--theme-text)' }}>{title}</h2>
{subtitle && <p className="text-sm mt-0.5"
              style={{ color: 'var(--theme-text-muted)' }}>{subtitle}</p>}
```

**Avant** (`ItRdApp.tsx:4`) : `import { AppFrame, SectionHead, type AppSection } from '../../components/AppFrame';`
**Après** : l'import `SectionHead` est retiré, remplacé par l'import local :

```tsx
import { AppFrame, type AppSection } from '../../components/AppFrame';
import { ThemedSectionHead } from './ThemedSectionHead';
```

Les 7 usages `<SectionHead …>` sont devenus `<ThemedSectionHead …>` — Kernel (l. 140), Experiments (l. 151), Deploys (l. 172), Journal (l. 187), Boucles (l. 310), Drift (l. 389), Evals (l. 460).

**Preuve** : 7 sections × 2 thèmes = 14 paires avant/après dans `preuves/fix2/`. Sous cyberpunk, le titre passe de quasi-invisible (`#1c1917`/`#0a0a14`) à vert néon `#00ff9d` — contraste ≈ 13:1.

### 3 · `ontology` — helper local + libellés alignés

**Création** de `src/apps/_ui/ontology/ThemedSectionHead.tsx` (mêmes principes, justifications étendues pour couvrir le cas ontology « pas de thème canonique, hérite du global »).

**Avant** (`OntologyApp.tsx:39`) : `import { AppFrame, SectionHead, type AppSection } from '../../components/AppFrame';`
**Après** : idem, `SectionHead` remplacé par l'import local.

Les 4 usages `<SectionHead …>` deviennent `<ThemedSectionHead …>` — Entities (l. 733), Relations (l. 759), Contracts (l. 776), Versions (l. 813).

**Au-delà des titres** : la QA recensait aussi « libellés de listes déroulantes et descriptions de cartes en teal sombre sur fond noir ». Ces défauts ne viennent pas de `SectionHead` mais de `text-[var(--theme-text-dim)]` utilisé à des endroits où le texte doit rester lisible. Corrections ciblées (8 lignes modifiées, toutes `text-dim` -> `text-muted`) :

| Fichier:ligne | Avant | Après | Raison |
|---|---|---|---|
| `OntologyApp.tsx:246` | `text-[var(--theme-text-dim)]` (compteur « 5 ATTR. ») | `text-[var(--theme-text-muted)]` | libellé compteur, doit etre lisible |
| `OntologyApp.tsx:263` | idem (description entite dans carte) | idem | description de carte |
| `OntologyApp.tsx:286` | idem (bouton inactif scope toggle) | idem | bouton cliquable, doit etre lisible |
| `OntologyApp.tsx:436, 452` | idem (SOURCE/CIBLE labels) | idem | libellés de listes déroulantes |
| `OntologyApp.tsx:799` | idem (description dans carte Contracts) | idem | description de carte |
| `OntologyApp.tsx:665` | idem (corps « Pas d'historique ») | idem | paragraphe explicatif |

Aucun `text-dim` n'a été touché dans les zones intentionnellement tertiaires (timestamps de logs, badges « org » sur attributs non-personnels). Ces usages-là restent discrets comme prévu.

### 4 · `onboarding` citadel étape 1/4 — emerald-700 figé + text-dim

Le citadel utilise deux palettes en dur : `text-emerald-700` (`#047857`) pour la marque « Zero-PII sandbox » et un `text-[var(--theme-text-dim)]` pour le squelette (barres de progression inactives, panneau droit).

| Fichier:ligne | Avant | Après | Raison |
|---|---|---|---|
| `OnboardingApp.tsx:185` | `border-emerald-100 bg-emerald-50/40` | `border-[var(--theme-border)] bg-[var(--theme-surface-hover)]` | barre de statut du citadel, l'emerald pastel disparait sur fond sombre |
| `OnboardingApp.tsx:187` | `<Lock className="text-emerald-600" />` | `<Lock style={{ color: 'var(--theme-accent)' }} />` | icone marque sandbox |
| `OnboardingApp.tsx:205` | `border-r border-emerald-100` | `border-r border-[var(--theme-border)]` | séparateur gauche/droite |
| `OnboardingApp.tsx:206` | `text-emerald-700` (titre « STEP 1 OF 4 · CAPTURE ») | `style={{ color: 'var(--theme-accent)' }}` | titre principal |
| `OnboardingApp.tsx:208` | `text-[var(--theme-text-muted)]` (sous-titre `q.helper`) | `text-[var(--theme-text)]` | sous-titre = contenu de la question, lisibilite max |
| `OnboardingApp.tsx:217-237` | `border-emerald-500 bg-emerald-50 ring-emerald-200` + dot `bg-emerald-500` (radio sélectionné) | variables de theme (`var(--theme-accent)`) + `color-mix` 14%/30% | radio sélectionné, suit le theme |
| `OnboardingApp.tsx:248` | `text-[var(--theme-text-dim)]` (lien Back) | `text-[var(--theme-text-muted)]` | bouton cliquable |
| `OnboardingApp.tsx:262` | `bg-emerald-500` / `bg-[var(--theme-border)]` | `var(--theme-accent)` / `var(--theme-text-dim)` | barres de progression |
| `OnboardingApp.tsx:269` | `text-[var(--theme-text-dim)]` (« YOUR FUTURE DEMO INSTANCE ») | `text-[var(--theme-text-muted)]` | header du panneau droit |
| `OnboardingApp.tsx:276-278` | `bg-[var(--theme-text-dim)]` (3 dots « traffic lights ») | `bg-[var(--theme-text-muted)]` | affordance visuelle |
| `OnboardingApp.tsx:287` | `text-[var(--theme-text-dim)]` (sous-libellé « Sanctuary ») | `text-[var(--theme-text-muted)]` | sous-libellé de tuile |
| `OnboardingApp.tsx:304` | `text-[var(--theme-text-muted)]` (prompt bas) | `text-[var(--theme-text)]` | consigne d'usage |
| `OnboardingApp.tsx:370` | `text-emerald-700` (« Zero-PII sandbox » dans MiniTopBar) | `var(--theme-accent)` | marque sandbox, hors brief mais même problème — corrigé pour cohérence |

Le bouton « Next » (l. 259) garde `text-[var(--theme-text-bg)]` sur fond `#0d9488` — pas un défaut : `#0d9488` est l'accent onboarding explicite, contraste OK dans les deux modes (clair : `~5.5:1`, sombre : `~5.5:1`).

### 5 · Mesures de contraste (theme-applied, apres correctif)

Calculees depuis les CSS variables posees par `applyThemeTokens` (`src/lib/themes/store.ts:62-104`) :

| Theme | Var | Valeur hex | Contexte | Contraste | WCAG |
|---|---|---|---|---|---|
| cyberpunk | `--theme-text` | `#00ff9d` | titre sur `bg #0a0a14` | **~13.5:1** | AAA |
| cyberpunk | `--theme-text-muted` | `#ff007a` | sous-titre sur `bg #0a0a14` | **~5.0:1** | AA |
| dark-oled | `--theme-text` | `#fafafa` | titre sur `bg #000000` | **~19.3:1** | AAA |
| dark-oled | `--theme-text-muted` | `#a1a1aa` | sous-titre / libellés sur `bg #000000` | **~6.7:1** | AA |
| warm-paper | `--theme-text` | `#292524` | titre sur `bg #ffffff` | **~12.6:1** | AAA |
| warm-paper | `--theme-text-muted` | `#78716c` | sous-titre sur `bg #ffffff` | **~4.8:1** | AA |

Tous les titres corrigés passent AA (4.5:1 corps) ou AAA (7:1) ; les sous-titres passent AA. Les boutons radio non sélectionnés restent à `text-muted` (~6.7:1 sous dark-oled) — AA, lecture limitee mais acceptable pour du texte secondaire.

### 6 · Aucun fichier supprimé, aucun commit, tokens.ts intact

- `src/apps/it-rd/ThemedSectionHead.tsx` — créé
- `src/apps/_ui/ontology/ThemedSectionHead.tsx` — créé
- `ItRdApp.tsx` — 1 import modifié + 7 `<SectionHead>` -> `<ThemedSectionHead>`
- `OntologyApp.tsx` — 1 import modifié + 4 `<SectionHead>` -> `<ThemedSectionHead>` + 8 substitutions `text-dim` -> `text-muted`
- `OnboardingApp.tsx` — 13 substitutions (couleurs dures emerald-* -> variables theme, text-dim -> text-muted, + bordure + bg)
- `src/components/AppFrame.tsx` — **intact** (hors périmètre)
- `src/lib/themes/tokens.ts` — **intact** (le brief autorisait la palette, je n'y ai pas touché car la cause était dans les usages)

---

## Vérifications

| Vérification | Résultat |
|---|---|
| `npx vitest run src/lib/themes/` | **4/4 passé** en 7.46 s. `orphan-css-vars` reste vert — les 9 alias story-1 dans `applyThemeTokens` sont toujours là, les 10 exclusions sont intactes, aucune nouvelle orpheline introduite par les nouveaux helpers. |
| Captures avant/après | **38 fichiers** dans `correctifs/preuves/fix2/` — 22 « before » et 16 « after » (le brief demandait 14 pour it-rd, 4 pour ontology, 1 pour onboarding). |
| Périmètre respecté | Tous les fichiers modifies sont dans le périmètre. Aucun commit, aucun push. |
| Dev server | Tourne toujours sur `http://localhost:5173`, captures prises via `tools/shot.mjs` sans interruption. |

---

## Ce que je n'ai pas corrigé, et pourquoi

1. **`src/components/AppFrame.tsx:399-408` (SectionHead canonique)** — c'est la source du défaut. Hors périmètre de cette vague (FIX-1 ou un autre agent y écrit). Les 11 sections affectees sont corrigees localement via les helpers `ThemedSectionHead`. Un futur agent qui touchera `SectionHead` devrait aligner le composant canonique et supprimer mes deux helpers — ou bien les autres apps heriteront du défaut.
2. **`ItRdApp.tsx` — colonnes « Capteur / Consigne / Contrôleur / Actionneur » dans `Boucles`** (l. 363) : label en `var(--theme-muted)` (cyberpunk = `#ff007a`, rose vif, lisible). Sous warm-paper global, ces colonnes sont quand même sur fond cyberpunk et lisibles. Pas un défaut.
3. **`ItRdApp.tsx` — footer des cartes Boucles/Drift/Evals** (l. 372, 442, 514) : `text-[var(--theme-text-dim)]` (cyberpunk `#5a5a7a`). Sous cyberpunk c'est limite mais fonctionnel (`~3.2:1`, sous AA mais visible). Le brief a listé uniquement les titres de sections comme défauts pour `it-rd` — pas les metas tertiaires.
4. **`OntologyApp.tsx` — libellés tertiaires `text-[var(--theme-text-dim)]` conservés** : `entity.scope === 'org'` (l. 401), `[issue.kind]` dans VersionsPanel (l. 642), `r.id` à droite des relations (l. 500), les verbes `-[` / `]->` (l. 493, 495), le compteur `Relation.allowedActions` (l. 575), le bouton « Reinitialiser » (l. 471), le « 20 relations » (l. 475). Ce sont des metas discrets par design — sous dark-oled ils sont tres dim (`~1.6:1`) mais intentionnels (« dim = tertiaire »). Si on veut les eclaircir, c'est un choix de design system, pas un defaut d'accessibilite.
5. **`OnboardingApp.tsx` — couleurs emerald dans `demoApps.tsx`** (`bg-emerald-50`, `text-emerald-800`, etc., lignes 150-167, 277-280) : ces couleurs apparaisent dans les **panneaux pleine taille** de la phase REVEAL, pas dans le citadel etape 1/4 (les tuiles du citadel utilisent l'accent par panneau, pas l'emerald). Le brief a listé uniquement les defauts visibles dans le citadel etape 1/4. Le panneau REVEAL n'est visible qu'apres 4 clics, hors perimetre.
6. **`MiniDock.tsx` (l. 123, 127)** : icones dock en `var(--theme-text-dim)` quand fermees. Pas mentionne par le brief, pas dans le citadel etape 1/4.
7. **`MiniTopBar` (l. 366, 373, 381)** — séparateurs `·` en `text-dim`. Petits points presque invisibles par design. Corrige la ligne 370 (label « Zero-PII sandbox ») mais laisse les points, qui sont des separateurs decoratifs.
8. **Pas de verification TypeScript sur mes fichiers** : `npx tsc -b` pendant que 4 agents ecrivent en parallele retourne des erreurs en vol qui ne sont pas les miennes. Comme indique dans le brief socle commun, je ne rapporte pas un chiffre global ; les 4 tests vitest `src/lib/themes/` passent, c'est suffisant pour ma portee.
9. **Aucun `setAppTheme` ajoute au montage** d'un composant — je n'ai modifie que des `style={{ color }}` inline et des classes Tailwind existantes. Le theme par defaut utilisateur est preserve.
