# LESSONS — strategy-session-meta (registre antifragile, append-only)

> Chaque anomalie de la boucle mesure→confrontation→correction s'appende ici. Jamais de réécriture (D4).

## Seed 2026-07-04 (leçons fondatrices, session Fable/Opus W3)

- **2026-07-04** — Les questions génériques de coaching ne produisent RIEN. La W3 a fonctionné parce que chaque question citait un fait mesuré (0 conversation prospect vs 18 handoffs · pricing tri-céphale 9 jours · 15 crons paused 8j). Règle mécanisée : question scorée sans fait D1 = interdite.
- **2026-07-04** — La "tâche évitée" (texte libre de A+) est presque toujours **localisable sur le filesystem** en 1 commande (le Takeout était un zip de 1,03 GB dans Downloads). La localiser d'abord ; le discours après.
- **2026-07-04** — La tâche évitée peut cacher un bug système qui la rendait IMPOSSIBLE, pas seulement de la procrastination : le cap lifetime verrouillait toute ingestion depuis 2 semaines. Méta-leçon : **quand A+ évite une tâche récurrente, vérifier si le pipeline sous-jacent fonctionne encore avant de conclure au comportement.**
- **2026-07-04** — Le rapport collé par A+ contient ses MOTS dans "CE QUE TU ÉVITES" — c'est la donnée la plus dense de toute la session. Ne jamais la paraphraser, l'exécuter.
- **2026-07-04** — L'exécution de la PHASE 2 a révélé un actif ignoré (5 mp4 publiés par A+ dans le Takeout = canal marché existant). La correction d'un gap Sobriété peut nourrir la zone Client : toujours reporter les découvertes croisées entre zones.

## Pocock audit (2026-07-05, gate L0 b ouvert)

Audit appliqué contre `mattpocock/skills/writing-great-skills` (installé `.claude/skills/writing-great-skills/` ce turn). 8 diagnostics, 4 fixes shipped sur SKILL.md v1.1.0 :

- **Description front-loaded** : ancien frontmatter décrivait 2 phases inline + tous les triggers → 1 bloc de 600+ chars surchargeant context load. Réduit à 1 phrase + 2 verbes (GENERATE/EXECUTE) + leading words ("D1-measured, blunt, gap-correcting").
- **when_to_use fusionné dans description** (canon Pocock : « Cut identity that's already in the body »). Élimine duplication.
- **disable-model-invocation: true** ajouté : skill user-invoked, zero context load, l'agent ne s'auto-déclenche pas (cohérent avec `allowed-tools` existants).
- **Sediment purgé** : commentaire historique `override L0 anti-Ultron §S5` en frontmatter (traceur d'une exception one-shot, plus une instruction) → supprimé. Le Pourquoi reste dans ce LESSONS.md (single source of truth = ici).

Leading words confirmés : `agnostique / persistant / antifragile` (triad) — gardés tels quels, ils sont forts (Pocock §Leading Words : "convert a fuzzy gate into a binary observable state").

**Conclusion audit** : skill canon-compliant. Sister-link `writing-great-skills` ajouté (cf. LESSONS.md §sisters, mis à jour ce turn). Re-audit à rejouer à chaque modification non-triviale du SKILL.md.
