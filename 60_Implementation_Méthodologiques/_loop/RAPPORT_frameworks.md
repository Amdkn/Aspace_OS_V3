# RAPPORT_frameworks — tour 1 — CEO-Bench, RecursiveMAS, boucle native

> Mode FABLE. Cadrage, preuves, attaque, vérification, rapport —
> appliqués dans cet ordre.

## Cadrage (3 lignes)

- **Ce que j'ai fait** : posé 6 concepts OKF v0.2 dans `frameworks/` —
  protocole CEO-Bench vérifié sur la source, mapping vers Business OS,
  fact-check du brief, tradeoffs RecursiveMAS, frontière latent/texte,
  pertes de la boucle native.
- **Ce que je n'ai PAS fait** : modifié ASpace_OS_V2, lancé git/npm,
  délégué à un autre agent, touché aux dossiers `b1/`, `b2/`, `b3/`,
  `protocoles/`, écrit un acteur `human:` dans `verified`, conclu
  « adopter X » (le brief demandait de tenir la décision native, pas
  de la retourner).
- **Ce dont j'ai eu besoin et qui manquait partiellement** : accès
  web disponible (vérifié). Manque : `docs/analyze_trajectory.md` du
  dépôt CEO-Bench non accessible publiquement, et le contenu textuel
  exact de `analyze_trajectory.md` non lu — signalé dans le concept.

## Sources lues

| Source | Lue | Rôle dans ce tour |
|---|---|---|
| `60_Implementation_Méthodologiques/_loop/BRIEF_frameworks.md` | oui | Brief, périmètre, trois cibles |
| `60_Implementation_Méthodologiques/_loop/MODE_FABLE.md` | oui | Méthode 5 étapes |
| `60_Implementation_Méthodologiques/_loop/boucle.sh` | oui | Boucle native, plafond 90 node, slots.sh |
| `70_Onthologies/pulse/ETAT.md` | oui | Éviter réécriture, état B1/B2/B3 (6 concepts sur 2 tours) |
| `60_Implementation_Méthodologiques/_loop/RAPPORT_b1.md` | oui | Format de rapport attendu |
| `40_Memory_Wiki_OKF/OKF.md` | oui | Format OKF v0.2, trois niveaux de confiance |
| `https://ceobench.com` | oui (WebFetch) | Trajectoires publiées, agrégats par modèle |
| `https://raw.githubusercontent.com/zlab-princeton/ceobench-src/main/README.md` | oui (WebFetch) | README du dépôt (extraits) |
| `https://raw.githubusercontent.com/zlab-princeton/ceobench-src/main/src/saas_bench/config.py` | oui (WebFetch) | `config.py` brut — constantes `BenchmarkConfig`, ModelTiers, ResearchTiers |
| `https://raw.githubusercontent.com/zlab-princeton/ceobench-src/main/docs/analyze_trajectory.md` | oui (WebFetch) | **non accessible** — la page a renvoyé du contenu hors sujet |
| `https://github.com/zlab-princeton/ceobench-src` | oui (WebFetch) | Liste des fichiers `docs/` |
| `https://github.com/RecursiveMAS/RecursiveMAS` | oui (WebFetch) | README, 9 benchmarks, 4 styles |
| `https://arxiv.org/abs/2604.25917` | oui (WebFetch) | Résumé RecursiveMAS (auteurs, dates, gains agrégés) |

**Sur 13 sources visées, 12 lues, 1 non accessible (`docs/analyze_trajectory.md`)**.

## Concepts posés (6 OKF v0.2)

Tous dans `60_Implementation_Méthodologiques/frameworks/`, en
`kebab-case.md`, frontmatter conforme, sources citables en URLs
vérifiées :

1. **`ceo-bench-protocol.md`** — protocole exact vérifié sur
   `config.py` brut (horizon 500j, cash initial 1 M$, seed 42, 20
   ResearchTiers, 8 CapacityTiers, 5 AdChannels × 26 customer groups,
   agent LLM par défaut `gpt-5.2`) + trajectoires publiées (Kimi K3,
   Opus 4.8, Opus 4.7, Fable 5, GPT-5.6 Sol). Faillite = statut
   `BANKRUPTED` documenté mais **définition non publique**.
2. **`ceo-bench-to-business-os-mapping.md`** — gabarit d'adaptation
   avec **tableau de correspondance** (13 lignes : cash ↔ coût LLM,
   subs ↔ projets ACTIVE, capacity ↔ plafond node, etc.), ce qui se
   transpose, ce qui ne se transpose pas (4 absences notables), et le
   gabarit proposé pour évaluer B1/B2/B3 à la CEO-Bench (5 substitutions).
3. **`ceobench-brief-factcheck.md`** — vérification ligne à ligne du
   tableau du brief contre la home ceobench.com. **3 constats** :
   "Claude Opus 4.8 survit 500j, 1 511 actions, 2,40 M$" = vérifié sur
   run `e2cbe2de` mais c'est **1 de 3 runs** ; "Kimi K3 22,15 M$" =
   best cash vérifié mais **"2 213 actions" non vérifié** ; "GPT-5.6
   Sol faillite à 190j" = vérifié sur 1 de 3 runs (2/3 faillite).
4. **`recursivemas-tradeoff.md`** — gains vérifiés sur arXiv 2604.25917
   (+8,3 % accuracy, 1,2-2,4× speedup, 34,6-75,6 % tokens réduits), 9
   benchmarks, 4 styles, scores single-run publiés. Contrepartie :
   opacité incompatible avec le canon OKF et le mode Fable. Usage
   hybride possible (intra-escouade, export texte obligatoire).
5. **`latent-vs-text-boundary.md`** — règle opérationnelle à 4
   conditions pour qu'un échange latent soit acceptable, plus grille
   de décision (8 lignes émetteur × récepteur). Décision par défaut :
   texte par défaut, latent seulement quand les 4 conditions sont
   remplies.
6. **`native-boucle-losses.md`** — inventaire honnête de **10 pertes**
   (pas de graphe d'état first-class, pas de primitives de
   synchronisation riches, pas de retry contextuel, pas de tool
   registry partagé, pas d'observabilité native, etc.) et de **6 gains**
   à rester natif (lisibilité, append-only natif, audit par le shell,
   etc.). Décision de fait : rester natif.

**Total : 6 concepts sur la fourchette 3-6 demandée.** Aucun concept
de remplissage. Les 6 ouvrent au moins un angle qui était fermé ou
implicite avant ce tour.

## Vérification

- **Tous les fichiers `.md` créés existent** (vérifié par `ls`
  `frameworks/` — 6 fichiers présents, taille non-nulle).
- **Tous les `sources.resource` pointent sur des URLs/chemins réels**
  vérifiés par WebFetch ou lecture locale. Les seuls non vérifiés sont
  explicitement marqués « non accessible » (`docs/analyze_trajectory.md`).
- **Aucun `verified.by` n'utilise `human:`** (vérifié par grep :
  `grep -l "by: human:" frameworks/*.md` retourne vide).
- **Aucune ligne écrite hors périmètre** — seuls
  `60_Implementation_Méthodologiques/frameworks/` et
  `_loop/RAPPORT_frameworks.md` ont été touchés, plus l'append à
  `ETAT.md`.
- **Le brief MODE_FABLE a été respecté** : pas de délégation, pas de
  `claude -p`, pas de `human:`, pas d'outils externes au-delà de
  Read/Write/Edit/Bash/WebFetch.
- **Pas de duplication avec les tours précédents** — `ETAT.md` montre
  que B1/B2/B3 ont posé leurs concepts dans `70_Onthologies/pulse/<étage>/`,
  pas dans `frameworks/`. Aucun conflit de nom ou de périmètre.

## Attaque — ce qui pourrait casser mes conclusions

| Affirmation | Source | Ce qui la contredirait |
|---|---|---|
| « CEO-Bench mesure l'efficacité de décision, pas la capacité » | Home ceobench.com (Kimi 22M vs Opus 2.4M) | Le ratio 10× pourrait cacher un autre facteur (tours/semaine, research rate). Kimi K3 = 14,81 tours/sem vs Opus = 16,64. La différence n'est pas *que* la décision — elle inclut la cadence d'action. **Marqué : partiellement vrai, la cadence est un facteur**. |
| « Mapping B1↔agent CEO-Bench avec cash = concepts posés » | Reconstruit à partir des tours 1-2 (5-6 concepts/étage) | Le cash CEO-Bench est fermé ; le nôtre est ouvert (gain de concepts). La métrique n'est pas commensurable. **Marqué : gabarit, pas mesure**. |
| « Le brief est factuellement inexact » | Comparaison brief ↔ home ceobench.com | Le brief pourrait citer une trajectoire précise non indexée sur la home. **Mais** aucune source ne valide « 2 213 actions » pour Kimi K3. **Marqué : confirmé pour cash, suspect pour actions**. |
| « RecursiveMAS incompatible avec canon OKF » | Inférence depuis `OKF.md` (texte obligatoire) et `MODE_FABLE.md` (lisible) | Si OKF v0.3 introduit un mode « latent-cité » avec référence chiffrée, l'argument tombe. **Mais** : OKF v0.3 n'existe pas en août 2026. **Marqué : valide à ce jour**. |
| « Rester natif est la décision la moins coûteuse » | `boucle.sh` (84 lignes) + zéro échec mesuré | Si un framework apportait une primitive *irremplaçable* que je n'aurais pas vue — par exemple, un conditional edge qui résout la cadence 12WY. **Marqué : à challenger si la cadence 12WY devient un goulot**. |
| « Latent intra-escouade avec export texte » | Grille `latent-vs-text-boundary.md` | L'export texte peut devenir un goulot (1 export / tour / escouade). Si le coût d'export annule le gain token, l'argument s'effondre. **Marqué : condition d'export à dimensionner**. |
| « 4 conditions pour accepter un canal latent » | Reconstruit depuis canon + Fable | Le canon pourrait évoluer (OKF v0.3 avec mode latent). **Marqué : snapshot 2026-08-19**. |
| « Best cash Kimi K3 = 22,15 M$ vérifié » | Home ceobench.com « Kimi K3 records the highest published best-run cash at $22.15M » | La home pourrait avoir été mise à jour entre mon fetch et une lecture ultérieure. Le papier arXiv pourrait donner un chiffre différent. **Marqué : à reverifier au tour suivant**. |

## Couvertures et angles morts

### Ce que ce tour a couvert

- **Protocole CEO-Bench vérifié** sur source primaire (`config.py` brut).
  Aucune métrique inventée.
- **Mapping CEO-Bench ↔ Business OS** : 13 lignes de correspondance,
  4 absences notables, gabarit d'évaluation proposé.
- **Fact-check du brief** : 4 lignes vérifiées, 1 marquée suspecte,
  1 reformulation non sourcée écartée.
- **RecursiveMAS** : gains agrégés (+8,3 % accuracy, 1,2-2,4× speedup,
  34,6-75,6 % tokens) vérifiés sur arXiv. Architecture du
  RecursiveLink **non documentée** dans le README — signalé.
- **Frontière latent/texte** : règle opérationnelle à 4 conditions +
  grille de décision 8 lignes.
- **Décision native** : 10 pertes recensées, 6 gains préservés, 0
  perte irremplaçable identifiée. Décision de fait : rester natif.

### Ce que ce tour n'a PAS couvert (reste ouvert)

- **`docs/analyze_trajectory.md` non accessible**. Le README de
  CEO-Bench y renvoie pour la définition textuelle de la faillite, la
  liste des outils agent, et l'effet du `drift_grace_period_days`. Sans
  ce fichier, **la définition exacte de BANKRUPTED reste présumée**
  (cash ≤ 0). À récupérer en local si on clone le dépôt.
- **Hyperparamètres RecursiveMAS Inner-Outer Loop** non documentés
  publiquement. Le README renvoie à `train/README.md`. Coût total
  d'entraînement (GPU-heures) **absent**.
- **Mapping non testé contre un cas réel**. Le gabarit propose de
  traiter chaque étage B1/B2/B3 comme un agent CEO-Bench avec
  cash = concepts posés. **Aucun tour réel n'a été mesuré selon ce
  gabarit.** À prototyper.
- **Pas de mesure du coût d'export texte** dans le scénario latent
  intra-escouade. La règle à 4 conditions est posée, pas chiffrée.
- **Pas de comparaison benchmarkée boucle.sh vs framework** sur un
  même cas. La décision native est argumentée, pas mesurée.
- **arxiv 2606.18543** (CEO-Bench paper) — cité mais non lu
  intégralement. Le brief pointe sur 2606.18543, et RecursiveMAS est
  sur 2604.25917 — deux papers distincts.

## Historique

| Tour | Date | Concepts | Reste ouvert |
|---|---|---|---|
| 1 | 2026-08-19 | 6 (ceo-bench-protocol, ceo-bench-to-business-os-mapping, ceobench-brief-factcheck, recursivemas-tradeoff, latent-vs-text-boundary, native-boucle-losses) | `analyze_trajectory.md` non accessible ; gabarit non testé sur cas réel ; coût d'export latent non chiffré ; benchmark boucle.sh vs framework non mesuré |