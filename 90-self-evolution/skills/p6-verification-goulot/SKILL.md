---
name: p6-verification-goulot
description: Fait passer un livrable machine par une vérification exécutable avant de le déclarer bon. Répond à P6 — 423 fichiers produits, zéro relu par un humain.
version: 1.0.0
platforms: [windows, linux, macos]
author: amadou-kone
metadata:
  hermes:
    tags: [verification, okf, confiance, revue, goulot]
    category: self-evolution
    requires_tools: [terminal]
    ancrage:
      problematiques: [P6]
      besoins: [B3]
      desirs: [D2]
      mesure: "423 fichiers produits en 2 vagues, 321 concepts OKF, 0 relu par un humain"
      source: "50_Distillation/RAPPORT_INTENTIONS_V3.md §3 P6"
---

# Quand l'utiliser

**Avant de déclarer qu'un livrable est bon**, et systématiquement sur toute
sortie d'agent délégué. C'est la skill qui empêche de confondre *produit* et
*vérifié*.

# Pourquoi elle existe

> Mesure du 2026-08-18 : deux vagues d'agents ont produit **423 fichiers**,
> dont 321 concepts OKF, zéro échec sur 60 lancements — **et aucun relu par un
> humain**. Tous en `confiance: machine`.

**Produire davantage n'aide plus. Le goulot est la vérification.**

Le rapport d'intentions le confirme d'un autre côté : 150 intentions
« audit / revue », et le mot qui revient dans ces briefs est *toi-même*. La
demande n'est pas un avis — c'est une **exécution vérifiable**.

# Procédure

1. **L'inférence propose, le script tranche.** Le 2026-08-30, un délégué a
   affirmé « la duplication domine ». C'était vrai, et c'est un script de
   comptage qui l'a établi. Une affirmation d'agent n'est pas une mesure.

2. **Faire tourner la vérification du livrable.**

   ```bash
   python 90-self-evolution/skills/p6-verification-goulot/scripts/verifier.py <fichier>
   ```

   Contrôle : frontmatter OKF présent, `verified` cohérent, aucun lien `[[…]]`
   mort, aucun `A SOURCER` résiduel non déclaré.

3. **Rendre le niveau de confiance explicite.** Le format OKF le déduit de
   `verified` — absent = non vérifié, acteurs machine = confirmé par machine,
   au moins un `human:` = revu par un humain.

4. **S'arrêter à la porte.** `machine → humain` ne se franchit **jamais** sans
   le propriétaire. C'est le seul verrou qu'aucun script ne peut poser à sa
   place.

# Pièges

- **Un `exit 0` n'est pas une vérification.** Ni un journal vide, ni un
  rapport d'agent qui dit avoir réussi.

- **Zéro échec sur 60 lancements ne dit rien de la qualité.** 423 fichiers ont
  été produits sans une seule panne et sans une seule relecture.

- **Ne jamais s'auto-attribuer `human:`.** C'est la falsification la plus
  coûteuse possible dans ce corpus : elle rend la distinction mesuré/supposé
  inutilisable, et c'est **D2** qui s'effondre.

- **Un lien `[[nom]]` vers un concept inexistant ment à l'avenir.** Vérifier
  la cible avant d'écrire.

# Ce que cette skill remplace

- **La revue par jugement d'agent**, retirée au profit de `--auto-test`. Un
  agent qui déclare avoir réussi ne prouve rien ; 60 lancements sans échec
  n'ont produit aucune relecture.
- **Les 150 briefs d'audit réémis** (`tu exécutes cette critique toi-même`,
  45×) : leur contenu devient un script qu'on lance, pas un brief qu'on
  recolle.
- **Le `exit 0` comme preuve.** Remplacé par la lecture de la sortie réelle.

# Vérification

```bash
python 90-self-evolution/skills/p6-verification-goulot/scripts/verifier.py --auto-test
```

Le test balaie le bundle OKF et rend la répartition réelle des niveaux de
confiance. Il **échoue si un fichier porte un `human:` non attribuable** — la
seule anomalie qui compte ici, parce qu'elle fait passer du supposé pour du
mesuré.
