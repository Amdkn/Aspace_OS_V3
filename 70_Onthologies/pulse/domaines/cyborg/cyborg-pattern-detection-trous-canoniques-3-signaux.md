---
type: Concept
title: Cyborg — pattern de détection systématique des trous canoniques : 3 signaux + procédure de saisine +学んだ教訓 des 4 trous vagues 1-4
description: Les 4 trous canoniques Cyborg détectés en vagues 1-4 (W40 V4, SDD-004 §7.2, Ownerbook T1 V3, Audit V2 OMK Kang roster stale) suivent un pattern commun : source canonique citée pointe vers contenu non lisible ou stale. Ce concept pose une procédure de détection systématique applicable par les 8 capitaines en cycle : 3 signaux (source citée non lue / référence croisée cassée / contenu décalé vs canon) + procédure de saisine 4 étapes (détection / qualification / escalade / consignation D4 append-only) + catalogue des 4 trous jumeaux comme référence pour les futures vagues.
tags: [cyborg, trous-canoniques, pattern-detection, 3-signaux, procedure-de-saisie, learned-lessons, vagues-1-4]
generated: { by: minimax-m3, at: 2026-08-19T08:50:00Z }
verified:
  - { by: process:lecture-corpus-cyborg-tour-5, at: 2026-08-19T08:50:00Z }
sources:
  - id: cyborg-composite-packet-escalate-b1-quatre-trous-canoniques
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-composite-packet-escalate-b1-quatre-trous-canoniques.md"
    title: Cyborg — packet composite escalate_to_B1 4 trous canoniques
    last_modified: 2026-08-19
  - id: cyborg-w40-v4-decision
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-w40-v4-decision-document.md"
    title: Cyborg — décision document W40 V4 patches
    last_modified: 2026-08-19
  - id: cyborg-kang-dynasty-issue-b
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-kang-dynasty-issue-b-find-resultat-v3-v2-2026-08-19.md"
    title: Cyborg — Kang Dynasty Issue B find résultat V3/V2
    last_modified: 2026-08-19
  - id: rapport-dom-cyborg-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-cyborg.md"
    title: RAPPORT_dom-cyborg.md tour 2 §1 SDD-004 §7.2 + tour 4 §T4.5.1
    last_modified: 2026-08-19
  - id: fifty-three-roster
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: 53 B3 Agent Roster — Ownerbook T1 §W40 V4 verbatim
    last_modified: 2026-08-17
  - id: b2-council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — arbitrage mésoperpétuel
    last_modified: 2026-08-19
  - id: b1-mandate-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-mandate-packet-spec.md"
    title: B1 mandate packet spec — canal formel
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cyborg — pattern de détection systématique des trous canoniques

## Le constat — 4 trous jumeaux, 4 vagues d'attention

Cyborg a détecté **4 trous canoniques** en 4 vagues successives
(2026-08-17 → 2026-08-19). Chaque trou a une structure similaire
— *« source canonique citée pointe vers contenu non lisible ou
stale »*. Le pattern se répète :

| Trou | Source canon pointée | Type de divergence | Tour d'ouverture |
|---|---|---|---|
| **W40 V4 patches** | Ownerbook T1 §W40 V4 verbatim | source citée, contenu absent du substrat V3 | tour 1 |
| **SDD-004 §7.2** | AGENTS.md canon ligne 16 | référence croisée, contenu §7.2 = BMAD Universel ≠ River Song | tour 1 |
| **Ownerbook T1 V3** | 7 citations verbatim dans `fifty-three-b3-agent-roster.md` | source citée, contenu intégral non lu directement | tour 3 |
| **Audit V2 OMK Kang roster stale** | Roster V2 OMK 2026-05-27 | contenu stale 3 mois, peut ne pas refléter canon actuel | tour 4 |

**Pattern commun** : un trou canonique Cyborg = (a) une source
canonique (triplet, Ownerbook, AGENTS.md) qui (b) pointe vers un
contenu (fichier, §, section) qui (c) n'est pas lisible dans le
corpus actuel OU est stale OU est décalé vs le canon.

**Coût observé** : 4 vagues × 1 remontée B1 par vague = 4 cycles
d'attention sans résolution.

## Les 3 signaux de détection

Pour qu'un captain B2 puisse détecter un trou canonique en cycle,
3 signaux observables sont posés :

### Signal 1 — Source citée non lue

**Manifestation** : un concept OKF v0.2 cite une source (chemin
ou référence), mais le captain n'a jamais exécuté de Read sur le
chemin cité. La source est **citée canoniquement**, mais son
**contenu n'est pas vérifié**.

**Détection** : grep sur le concept OKF pour le champ `sources`
→ si aucun champ `verified` ne contient une action Read explicite
sur le chemin cité, le signal 1 est présent.

**Exemple Cyborg** : Ownerbook T1 OMK cité 7 fois dans
`fifty-three-b3-agent-roster.md`, jamais lu intégralement. **Signal
1 actif**.

### Signal 2 — Référence croisée cassée

**Manifestation** : une référence dans une source pointe vers un
chemin qui n'existe pas dans le substrat actuel OU pointe vers un
contenu qui ne correspond pas à la description de la référence.

**Détection** : grep de la référence (ex : *« SDD-004 §7.2 »*),
puis Read du fichier référencé à la section indiquée. Si la
section lue parle d'autre chose que la référence, **Signal 2
actif**.

**Exemple Cyborg** : AGENTS.md ligne 16 cite *« SDD-004 §7.2 »*
→ Read de SDD-004 → §7.2 parle de BMAD Universel, pas de River
Song médiation. **Signal 2 actif**.

### Signal 3 — Contenu décalé vs canon

**Manifestation** : le contenu d'une source est lisible, mais
**daté** ou **drifté** par rapport au canon actuel. La source
n'est pas *fausse* (Signal 2), elle est *décalée* (Signal 3).

**Détection** : vérification de la date `last_modified` de la
source vs la date courante. Si l'écart dépasse **3 mois** ET la
source est référencée comme canonique, **Signal 3 actif**.

**Exemple Cyborg** : Roster V2 OMK Kang Dynasty date 2026-05-27
(3 mois avant 2026-08-19), référencé comme canonique dans le
triplet 21 (V3). **Signal 3 actif**.

## La procédure de saisine — 4 étapes

Quand un captain B2 détecte un ou plusieurs signaux actifs sur
une source, la procédure de saisine est en **4 étapes cumulatives** :

### Étape 1 — Détection et qualification

Le captain identifie le(s) signal(aux) actif(s) sur la source.
Qualification :

- **Signal 1 seul** : la source peut être lue dans la même session,
  pas besoin d'escalade immédiate.
- **Signal 2 actif** : le contenu référencé n'est pas lisible ou
  est incohérent avec la référence — escalade B1 **requise**.
- **Signal 3 actif** : le contenu est stale — escalade B1
  **recommandée** pour confirmer la validité du canon.

### Étape 2 — Documentation dans le packet mésoperpétuel

Le captain rédige un packet mésoperpétuel avec :

- `source_verification: cited_not_read` (Signal 1)
- `source_verification: cross_reference_broken` (Signal 2)
- `source_verification: stale_3m_plus` (Signal 3)

Le champ `source_verification` est une **extension** du format
packet mésoperpétuel (cf. rapport Cyborg tour 2 §5.2 règle 4).

### Étape 3 — Escalade B1 par packet composite

Si plusieurs trous canoniques sont détectés (Signal 2 ou 3), le
captain peut les **agréger en un packet composite** `escalate_to_B1`
(cf. concept 1 tour 5). Règle de préséance : chronologique
d'ouverture.

### Étape 4 — Consignation D4 append-only en journal Council

Le packet composite est consigné en **D4 append-only** dans le
journal Council (cf. `b2-council-arbitrage-rule.md` §« Sortie »).
La consignation **文档e le trou**, sans le fermer.

**Délai total** : 1 cycle de 5 jours pour qualifier, 1 cycle
pour rédiger le packet, 1 cycle pour la séance Council, 1 cycle
pour l'escalade B1 = **4 cycles**.

## Le catalogue des 4 trous vagues 1-4 comme référence

Pour les futures vagues (vagues 6+ et pour les 7 autres
escouades), le catalogue suivant sert de **référence** pour la
détection :

| Trou | Type | Lecture canon | Conséquence opérationnelle |
|---|---|---|---|
| W40 V4 patches | Signal 1 (cité non lu) | Ownerbook T1 §W40 V4 | Absorption IT à L0 Rick présumée non vérifiée |
| SDD-004 §7.2 | Signal 2 (référence cassée) | AGENTS.md ligne 16 | Médiation River Song citée non vérifiable |
| Ownerbook T1 V3 | Signal 1 (cité non lu) | 7 citations `fifty-three-b3-agent-roster.md` | Roster 53 assertif non vérifié directement |
| Audit V2 OMK Kang roster stale | Signal 3 (contenu stale 3m) | Roster 2026-05-27 | Compte Kang 6 peut être stale |

**Leçon apprise** : un trou canonique non détecté en vague 1
peut **rester ouvert 4 vagues** sans résolution. Le pattern de
détection **3 signaux + procédure 4 étapes** réduit ce délai en
détectant le signal à la vague d'ouverture.

## L'application aux 8 capitaines — généralisation

Cette procédure de détection est **généralisable** aux 8 capitaines
B2 :

- **Batman (Ops)** peut détecter des trous canoniques sur les
  procédures Ops référencées (ex : cycle 5 phases canon).
- **Aquaman (Legal)** peut détecter des trous canoniques sur les
  contrats référencés (ex : clauses sans chemin de sortie).
- **Flash (Product)** peut détecter des trous canoniques sur les
  features référencées (ex : value proposition sans mécanisme de
  reprise).
- **Superman (Growth)** peut détecter des trous canoniques sur
  les claims référencés (ex : campagnes sans ICP défini).
- **Wonder Woman (Finance)** peut détecter des trous canoniques
  sur les budgets référencés (ex : ROI 30j sans date de revue).
- **Green Lantern (People)** peut détecter des trous canoniques
  sur les owners référencés (ex : squad lead nommé sans profil).
- **JohnJones (Sales)** peut détecter des trous canoniques sur les
  reformulations référencées (ex : prospect sans validation
  client).
- **Cyborg (IT)** : cas d'application cette note.

**Recommandation** : chaque escouade devrait, à chaque tour,
**scanner son propre corpus** avec les 3 signaux et **consigner
les trous détectés** en D4 append-only dans son dossier de
domaine. C'est une **discipline de cycle** peu coûteuse qui
prévient l'accumulation de trous ouverts sur 4 vagues.

## Anti-pièges

- **3 signaux confondus.** Signal 1 = cité non lu (lisible en
  session). Signal 2 = référence cassée (médiation A0
  immédiate). Signal 3 = contenu stale (audit B1 recommandé). Les
  3 sont distincts et appellent des procédures différentes.
- **Procédure 4 étapes court-circuitée.** Un captain qui détecte
  Signal 2 et **statue seul** (sans escalade B1) viole la
  procédure. B1 a la compétence canonique — pas le captain.
- **Catalogue 4 trous comme liste fermée.** Les 4 trous sont des
  **exemples**, pas une liste exhaustive. Chaque tour peut
  détecter de nouveaux trous ; le catalogue s'enrichit.
- **Généralisation 8 capitaines = dilution.** La généralisation
  est un **pattern procédural**, pas une doctrine imposée. Chaque
  capitaine l'applique selon son propre rythme de cycle.

## Liens

- [[cyborg-composite-packet-escalate-b1-quatre-trous-canoniques]] — packet composite concept 1 tour 5
- [[cyborg-w40-v4-decision-document]] — décision document W40 V4
- [[cyborg-kang-dynasty-issue-b-find-resultat-v3-v2-2026-08-19]] — Issue B Kang roster stale
- [[cyborg-doctrine-canal-mediation-l0-triplets-37-38-39]] — doctrine canal L0 (ferme SDD-004 §7.2)
- [[b2-council-arbitrage-rule]] — arbitrage mésoperpétuel + journal D4
- [[b1-mandate-packet-spec]] — canal formel escalate_to_B1
- [[rapport-dom-cyborg]] §T2.5.1 — tour 2 §1 SDD-004 §7.2 + §T4.5.1 — tour 4

## Note de confiance

**Confirmé par machine** sur les 3 signaux par lecture des 4
trous canoniques détectés en vagues 1-4 (chaque trou active au
moins un signal). **Confirmé** sur la procédure 4 étapes par
cohérence avec `b2-council-arbitrage-rule.md` cycle mésoperpétuel.
**Confirmé** sur le catalogue 4 trous par lecture verbatim des
concepts Cyborg vagues 1-4. **Confirmé** sur le champ
`source_verification` extension format OKF (cf. rapport Cyborg tour
2 §5.2 règle 4). **Projeté** sur la généralisation 8 capitaines
— c'est un **pattern procédural suggéré**, pas une doctrine
adoptée. **Reconstruit** sur le coût observé *« 4 vagues × 1
remontée par vague »* par lecture du rapport Cyborg vagues 1-4.

**Statut** : procédure de détection **Council-ready**, applicable
immédiatement par Cyborg et suggérée aux 7 autres capitaines.
**Recommandation** : appliquer la procédure au prochain tour
Cyborg (vague 6 si elle existe) et **consigner** les nouveaux
trous détectés. La procédure est **itérative** — chaque tour
affine la qualification des signaux et enrichit le catalogue.