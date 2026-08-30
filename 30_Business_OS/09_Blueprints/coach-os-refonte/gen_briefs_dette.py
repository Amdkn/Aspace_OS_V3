# -*- coding: utf-8 -*-
"""Un brief par app pour resorber la dette de style : couleurs en dur."""
import pathlib
P = pathlib.Path(__file__).parent
REPO = ("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/"
        "05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os")

# Mesure du 2026-08-05, hex + classes de palette Tailwind.
DETTE = {
 "people":     (74, 124), "welcome":  (1, 177), "onboarding": (48, 83),
 "finance":    (96, 13),  "operations": (85, 0), "sales":     (16, 67),
 "_ui":        (22, 55),  "it-rd":    (65, 7),  "growth":     (62, 10),
 "product":    (26, 20),  "audit":    (7, 30),
}

BRIEF = """# BRIEF — resorber la dette de style de l'app `{APP}`

Tu ne changes aucun comportement. Tu remplaces des couleurs codees en dur par les
variables du systeme de theme, pour que l'app suive enfin le theme choisi.

## Le probleme, mesure

L'app `{APP}` porte **{HEX} couleurs hexadecimales** et **{CLS} classes de palette
Tailwind** ecrites en dur. Total : **{TOT} points**.

Consequence visible : changer le theme d'une app ne change qu'une partie de son
apparence. Pire, les pages de detail semblent appartenir a une autre app que
leurs listes — c'est le constat du proprietaire du produit, et c'est ce qu'on
corrige.

Le depot : `{REPO}`
React 19 · TypeScript · Tailwind v4 · Zustand.

## Le systeme de theme

`src/lib/themes/store.ts` (`applyThemeTokens`) pose ces variables sur la racine
de chaque fenetre. Elles sont ta cible :

| role | variable |
|---|---|
| texte principal | `var(--theme-text)` |
| texte secondaire | `var(--theme-muted)` |
| texte tertiaire | `var(--theme-text-dim)` |
| fond de fenetre | `var(--theme-bg)` |
| fond exterieur | `var(--canvas)` |
| surface de carte | `var(--theme-surface)` · `var(--panel-solid)` |
| survol de surface | `var(--theme-surface-hover)` |
| bordure | `var(--panel-border)` · `var(--theme-border)` |
| bordure discrete | `var(--panel-border-subtle)` · `var(--hairline)` |
| ombre | `var(--shadow-panel)` · `var(--theme-shadow)` |
| accent | `var(--theme-accent)` |
| accent en rgb | `var(--theme-accent-rgb)` (pour `rgba(var(--theme-accent-rgb), .2)`) |

En Tailwind, la notation entre crochets accepte les variables :
`className="bg-[var(--theme-surface)] text-[var(--theme-text)]"`.

## Ce que tu NE dois PAS convertir

C'est la partie la plus importante du brief. Une couleur qui porte un **sens**
n'est pas un choix de style :

1. **Les etats semantiques** — vert = succes, rouge = erreur ou incident, orange
   = avertissement, bleu = information. Un badge « ONLINE » vert doit rester vert
   sur un theme qui n'a pas de vert.
2. **Les previsualisations de theme** — tout composant qui affiche les couleurs
   d'un AUTRE theme que le theme courant (`ThemePreview`, les vignettes de
   `settings`, les demonstrations de `design`). Les convertir casserait leur
   raison d'etre.
3. **Les identites de marque** — le logo, les couleurs propres a un partenaire
   ou a un outil tiers.
4. **Les accents par app** — la constante `ACCENT` en tete de chaque app est
   voulue : c'est l'identite de l'app. Tu ne la touches pas.

En cas de doute : **laisse la couleur et signale-la dans ton rapport.** Une
couleur laissee et signalee vaut mieux qu'un sens detruit.

## Le cas des degrades bâtis sur l'accent

Certains fichiers construisent leurs fonds ainsi :

```
background: `radial-gradient(60% 80% at 50% 0%, ${{accent}}26 0%, transparent 70%)`
```

Ce n'est pas a supprimer — c'est la signature visuelle de l'app. Mais le RESTE
de la page (surfaces, textes, bordures) doit suivre le theme, pour que le
degrade se pose SUR un fond correct au lieu de le remplacer. Verifie qu'une page
de detail et sa liste se ressemblent apres ton passage.

## Verification obligatoire

```
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
npm test
```

La reference est **75 erreurs TS**. Au-dela, tu as introduit une regression.

Puis compte ce qui reste :

```
grep -rEo "#[0-9a-fA-F]{{6}}" src/apps/{APP} --include=*.tsx | wc -l
grep -rEo "\\b(bg|text|border)-(white|black|stone|slate|zinc|gray|neutral)(-[0-9]+)?\\b" src/apps/{APP} --include=*.tsx | wc -l
```

Rapporte les deux chiffres avant et apres.

## Interdits

0. **N'invoque AUCUN workflow BMAD** (`bmad-spec`, `bmad-build-auto`,
   `bmad-advanced-elicitation`...). Ils ouvrent une porte « [A] Approve » que
   personne ne peut franchir — la session est non interactive. Tu implementes
   directement.
1. Tu ne touches qu'a `src/apps/{APP}/`. Aucune autre app, aucun composant
   partage, aucun fichier de `src/lib/` ou `src/components/`.
2. Tu ne changes **aucun comportement** : pas de logique, pas de structure JSX,
   pas de props. Seulement des valeurs de couleur.
3. N'ajoute aucune dependance. Pas de `git commit`.
4. Ne supprime aucune section, aucune donnee de demonstration.

## Rapport attendu

Les deux comptes avant/apres, la liste des couleurs que tu as **volontairement
laissees** avec la raison de chacune, et tout point non fait avec sa raison.
Un point non fait et signale vaut mieux qu'un point bacle en silence.
"""

for app, (hexn, cls) in DETTE.items():
    txt = (BRIEF.replace("{APP}", app).replace("{REPO}", REPO)
                .replace("{HEX}", str(hexn)).replace("{CLS}", str(cls))
                .replace("{TOT}", str(hexn + cls)))
    (P / ("BRIEF_APP_dette-%s.md" % app)).write_text(txt, encoding="utf-8")
    print("BRIEF_APP_dette-%-12s %4d points" % (app + ".md", hexn + cls))
