---
name: p4-instrument-honnete
description: Vérifie qu'un script mesure bien ce qu'il prétend avant de croire son chiffre. Répond à P4 — l'instrument qui ment, défaut le plus récurrent du poste.
version: 1.0.0
platforms: [windows, linux, macos]
author: amadou-kone
metadata:
  hermes:
    tags: [mesure, verification, ntfs, encodage, instrument]
    category: self-evolution
    requires_tools: [terminal]
    ancrage:
      problematiques: [P4]
      besoins: [B3]
      desirs: [D2]
      mesure: "jonctions NTFS 13,8 M au lieu de 14 613 ; isDirectory() faux sur lien ; tokens gonflés ×3,5"
      source: "50_Distillation/RAPPORT_INTENTIONS_V3.md §3 P4"
---

# Quand l'utiliser

**Avant de rapporter tout chiffre issu d'un script**, et impérativement quand
une mesure contredit l'observation directe. C'est la skill qui protège toutes
les autres : posée sur un instrument qui ment, `p1-anti-rejeu` produit des
verdicts faux avec conviction.

# Pourquoi elle existe

**La règle : quand la mesure contredit l'observation directe, on répare
l'instrument — jamais on n'ajuste le chiffre.**

Chaque ligne ci-dessous est un défaut réel, payé, sur ce poste :

| Défaut | Ce que l'instrument disait | La réalité |
|---|---|---|
| Jonction NTFS suivie | 13,8 M fichiers | 14 613 |
| `os.path.islink()` sur jonction | « pas un lien » | jonction |
| Compte direct au lieu du cumul | OKF = 0,1 % | 0,6 % |
| `isDirectory()` sur lien symbolique | 4 skills | 6 |
| Sonde `(Get-Item).LinkType` | « aucun lien » | 2 liens |
| Motifs non accentués | « introuvable » | présent |
| Somme de tout ce qui est atteignable | ~20 724 tokens/session | ~5 819 |
| Console cp1252 | plantage à l'affichage | mesure juste, perdue |
| Orphelins par liens croisés | 0 orphelin | 117/130 hors de portée |

Deux familles se dégagent : **la sonde qui ne voit pas ce qu'elle cherche**, et
**le total qui additionne ce qui ne s'additionne pas**.

# Procédure

1. **Faire tourner la liste de contrôle sur le script suspect.**

   ```bash
   python 90-self-evolution/skills/p4-instrument-honnete/scripts/auditer.py <script.py|.ts>
   ```

   Le script signale les motifs connus pour mentir sur ce poste.

2. **Croiser avec une seconde méthode.** Un compte n'est crédible que confirmé
   par un chemin indépendant. `find` contre `os.walk`, `Get-Item` contre
   `fs.statSync`. Si les deux divergent, **l'un des deux est l'instrument à
   réparer**, et ce n'est pas forcément celui qu'on soupçonne.

3. **Vérifier le sens du total.** Avant d'additionner : ces valeurs
   s'additionnent-elles vraiment ? Le coût de démarrage n'est pas la somme de
   tout ce qui est atteignable. Un total qui exagère pousse à couper ce qu'il
   faut garder.

4. **Regarder la sortie réelle, pas le code de retour.** Un `exit 0`, un
   journal vide, un rapport d'agent délégué ne prouvent rien.

# Pièges

- **`tsc` qui passe ne prouve rien.** Le 2026-08-30, `tsc --noEmit` est passé
  sans un mot pendant que la console criait `vue is not defined`. C'est la
  console qui a tranché.

- **La sonde qui confirme est la plus dangereuse.** `LinkType` a répondu
  « aucun lien », ce qui *confirmait* l'hypothèse — et c'était faux. Une sonde
  qui va dans le sens attendu mérite plus de méfiance, pas moins.

- **Ne jamais ajuster une constante pour faire passer un test.** Si
  `deja_vu.py --auto-test` sort de sa tolérance, la question est *qu'est-ce
  qui a bougé*, pas *comment élargir la tolérance*.

- **L'accent, l'encodage, la casse.** Sur ce poste : cp1252 en console, motifs
  non accentués face à du texte accentué. Normaliser des deux côtés.

# Vérification

```bash
python 90-self-evolution/skills/p4-instrument-honnete/scripts/auditer.py --auto-test
```

Le test s'audite lui-même : il applique ses propres motifs à son propre code
source. **Un auditeur qui ne se détecte pas est disqualifié** — il prouve
qu'il ne voit pas ce qu'il prétend chercher.
