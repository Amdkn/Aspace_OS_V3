---
name: p3-point-entree
description: Vérifie qu'un document produit est atteignable depuis ce qui est lu au démarrage. Répond à P3 — 117 rapports sur 130 étaient hors de portée sans être orphelins.
version: 1.0.0
platforms: [windows, linux, macos]
author: amadou-kone
metadata:
  hermes:
    tags: [atteignabilite, index, routeur, corpus]
    category: self-evolution
    requires_tools: [terminal]
    ancrage:
      problematiques: [P3]
      besoins: [B2]
      desirs: [D3]
      mesure: "520/4 625 documents atteignables (11,2 %) ; 117/130 rapports hors de portée ; bundle OKF = 0,6 % du corpus"
      source: "50_Distillation/RAPPORT_INTENTIONS_V3.md §3 P3"
---

# Quand l'utiliser

**Après avoir produit tout document destiné à être relu.** Un rapport écrit et
inatteignable a coûté des jetons pour rien — ce n'est pas un problème de
rangement, c'est du travail mort.

# Pourquoi elle existe

Mesure du 2026-08-30, avant correction :

| | Avant | Après |
|---|---:|---:|
| Documents atteignables depuis les `CLAUDE.md` | 520 / 4 625 — **11,2 %** | 1 395 — 30,2 % |
| Rapports de distillation atteignables | 13 / 130 — **10 %** | 140 / 140 — 100 % |

**Aucun de ces 130 rapports n'était orphelin** : ils se citaient entre eux. Ils
étaient enfermés dans une boucle fermée qu'aucun point d'entrée n'atteignait.
2,6 Mo produits, jamais relus.

Le même défaut à l'étage au-dessus : le `CLAUDE.md` désignait le bundle OKF
comme « la mémoire du poste ». Il porte **38 `.md` sur 6 557 — 0,6 %**. Suivre
la consigne garantissait de manquer 99,4 % de ce qui est écrit, donc de
conclure « non documenté », donc de redemander.

**La bonne question n'est pas « ce fichier est-il cité ? » mais « est-il
atteignable depuis ce qui est réellement lu au démarrage ? »**

# Procédure

1. **Mesurer l'atteignabilité**, pas les liens entrants.

   ```bash
   python 90-self-evolution/skills/p3-point-entree/scripts/portee.py
   ```

   Le script part des `CLAUDE.md` et propage sur 4 sauts.

2. **Si le document neuf n'y est pas**, l'ajouter à un index déjà atteignable
   — `CARTOGRAPHIE.md`, `INDEX_DISTILLATIONS.md` — plutôt que de créer un
   nouveau point d'entrée. (B4 : moins de systèmes, pas plus.)

3. **Préférer un index régénéré à une liste écrite.** Une liste tenue à la main
   est périmée dès le document suivant.

4. **Ne jamais poser un lien `[[nom]]` vers un concept inexistant.** Un lien
   mort ment à l'avenir.

# Pièges

- **« Zéro orphelin » n'est pas une preuve.** Les 130 rapports se citaient
  mutuellement et affichaient 0 orphelin, alors que 90 % étaient hors de
  portée. Une boucle fermée est indétectable par comptage de liens entrants.

- **Le compte direct d'un dossier n'est pas son cumul.** Le bundle OKF mesuré
  en direct donnait 0,1 % ; les concepts vivent dans les sous-dossiers, le
  cumul donne 0,6 %.

- **Ajouter un index coûte.** `CLAUDE.md` est passé de 162 à 320 lignes, soit
  ~2 000 tokens par session. Le dire, et vérifier que ça vaut le prix. (P5)

# Vérification

```bash
python 90-self-evolution/skills/p3-point-entree/scripts/portee.py --auto-test
```

Le test **échoue si la part de rapports atteignables descend sous 95 %**.
Cette borne est le seuil au-delà duquel un rapport produit redevient du travail
mort.
