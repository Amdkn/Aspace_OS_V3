---
type: Concept
title: Position Superman sur le 7ᵉ agent Guardians — Peter_Quill_Orchestrator proposé comme candidat principal
description: Le substrat OMK carto liste 6 agents B3 Guardians (StarLord_Story, Rocket_Auto, Gamora_Target, Drax_Closing, Groot_Content, Mantis_VoC). Le compte canonique squad est ~7 par `fifty-three-b3-agent-roster.md`. Superman Growth propose Peter_Quill_Orchestrator comme 7ᵉ agent : coordinateur transverse des 6 autres, tenant le sprint Guardians et le DoD partagé. Nebula_Analytics est écarté car la frontière IT (couplage Superman↔IT) doit être arbitrée séparément, pas absorbée dans la squad Growth.
tags: [superman, growth, guardians, 7th-agent, peter-quill, orchestrator, omk, squad]
generated: { by: minimax-m3, at: 2026-08-19T05:20:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-2, at: 2026-08-19T05:20:00Z }
sources:
  - id: carto-substrat-omk
    resource: "C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/carto/01_picard_w2_unread.txt"
    title: Carto substrat OMK — 6 agents B3 Guardians
    last_modified: 2026-08-17
  - id: fifty-three-roster
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: Fifty-three B3 agent roster — ~7 par squad
    last_modified: 2026-08-17
  - id: triplet-line-19
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet v3 ligne 19 — Superman pairedWith Guardians (6 techniciens)"
    last_modified: 2026-08-17
  - id: jtbd-emit-receive-tour1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/jtbd-emit-receive.md"
    title: Superman JTBD emit/receive — 6 agents + 3 lectures du 7ᵉ
    last_modified: 2026-08-19
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — B3 Guardians = R sur Finance→Growth et Legal→Growth
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Position Superman sur le 7ᵉ agent Guardians

## L'asymétrie observée

Le substrat OMK carto (`01_picard_w2_unread.txt` lignes 63-77) liste
**6 agents B3 Guardians** :

| # | Agent | Spécialisation | Pair-check matrice dominant |
|---|---|---|---|
| 01 | StarLord_Story | manifeste, brand storytelling | (Brand transverse) |
| 02 | Rocket_Auto | automation marketing, séquences | Finance → Growth |
| 03 | Gamora_Target | ciblage, segmentation, ICP | Growth → Sales |
| 04 | Drax_Closing | closing, dernière étape funnel | Sales → Ops |
| 05 | Groot_Content | content production, blog, SEO | Legal → Growth |
| 06 | Mantis_VoC | voice of customer, témoignage | Legal → Growth |

Le triplet v3 ligne 19 confirme le compte de 6. Le compte canonique
par squad est **~7** selon `fifty-three-b3-agent-roster.md`.

**Asymétrie** : 6 observés / 7 attendus. Le Ownerbook T1 OMK
(DoD-1 *« ≥ 7 par squad »*) n'est pas tenu pour Guardians. Trois
lectures sont possibles (cf. `jtbd-emit-receive.md` §« Le 7ᵉ agent
manquant — projection ») :

1. **Peter_Quill_Orchestrator** — coordinateur transverse des 6
   autres, dispatch des JTBD entre eux, sprint Guardians.
2. **Nebula_Analytics** — analytics stack (Mixpanel, Amplitude,
   PostHog), frontière #3 Superman↔IT.
3. **Compte exact 6** — canon ajusté à 6, Ownerbook T1 DoD-1
   non-tenu pour Guardians.

Cette note tranche : **Peter_Quill_Orchestrator est le candidat
principal**.

## Pourquoi Peter_Quill_Orchestrator plutôt que Nebula_Analytics

Trois raisons :

### 1. Symétrie avec les autres squads

Chaque squad B3 a un **squad lead** qui orchestre les autres agents :

- **Avengers** (Flash) → Captain America (squad lead cité triplet
  v3 ligne 17)
- **Fantastic Four** (Batman) → MrFantastic (triplet 31 : *«
  MrFantastic tient la charge ProcessDesign »*)
- **Illuminati** (Sales) → MrFantastic ou ProfessorX (squad
  lead non explicite canoniquement, plusieurs candidats)
- **X-Men** (Green Lantern) → ProfessorX (triplet 33 : *«
  ProfessorX tient le recruiting »*)
- **Thunderbolts** (Wonder Woman) → BuckyBarnes (squad lead
  canonique Coach OS)
- **Kang Dynasty** (Cyborg) → KangPrime (squad lead canonique
  Coach OS)
- **Eternals** (Aquaman) → Ikaris (squad lead canonique Coach OS)

Sept squads sur 8 ont un squad lead explicite. **Seuls les Guardians
n'en ont pas**. La symétrie pointe Peter_Quill_Orchestrator.

### 2. La frontière IT ne doit pas être absorbée dans Growth

Nebula_Analytics absorberait la frontière #3 Superman↔IT
(analytics stack) dans la squad Growth. Mais le couplage est
**asymétrique** (Superman dépend de Cyborg pour l'infra, Cyborg ne
dépend pas de Superman pour la doctrine analytics — cf.
`pair-checks-dependencies.md` §« Couplage Superman ↔ IT »). Si
Nebula_Analytics devient B3 Growth, la frontière IT est **dissoute
par absorption** plutôt qu'arbitrée par Council.

Mieux : la frontière IT reste un **arbitrage Council** (mode
negotiation, cf. `cooperation-mode-patterns.md` §« Negotiation 1 »),
et l'analytics stack reste en **infrastructure partagée Cyborg**.
Peter_Quill_Orchestrator peut consommer les analytics (lecture des
données) sans les posséder.

### 3. Le compte 6 ajusté est la lecture la moins défendable

Le compte 6 ajusté brise la symétrie 8 squads / 7 agents sans
justification canonique. Le Ownerbook T1 OMK DoD-1 est **un
engagement de compte** : il a été posé, il n'a pas été re-tranché
pour Guardians. Le respecter est l'attribution par défaut.

## Le rôle proposé pour Peter_Quill_Orchestrator

### Mission canonique

Peter_Quill_Orchestrator tient **trois charges** explicitement
distinguées des 6 charges spécialisées :

1. **Sprint Guardians** — `SCRUMS.md` consolidé des 6 agents,
   5 scrums/semaine (cf. triplet 11). Vue d'ensemble des blockers
   inter-agents (Groot × Mantis contradiction, Rocket × Gamora
   targeting).
2. **Dispatch inter-agents** — séquencement des JTBD entre les
   6 agents. Ex : Mantis recueille un témoignage (VoC) → Groot
   produit le case-study → Mantis valide la version finale →
   Groot publie.
3. **DoD partagé** — agent qui tient les DoDs qui ne sont la
   responsabilité d'aucun agent seul (ex : lead indicator
   cross-canal, vue funnel consolidée).

### Ce que Peter_Quill_Orchestrator n'est PAS

- **Pas un B2 captain** — le rang B2 est Superman seul. Peter est
  B3 squad lead, pas VP.
- **Pas un ICP** — la qualification ICP reste Gamora_Target.
  Peter ne se substitue pas à Gamora.
- **Pas un arbitre B2** — les arbitrages restent Council. Peter
  signale, ne tranche pas (cf. triplet 41 : *« B3 interdit-combler-trou »*).
- **Pas une 7ᵉ spécialité** — Peter n'a pas de pair-check
  matrice dominant propre. Sa valeur est la coordination, pas
  l'exécution.

## Le format du compte squad Guardians — proposition

Avec Peter_Quill_Orchestrator, la squad Guardians passe de 6 à 7
agents, alignée sur le Ownerbook T1 OMK DoD-1. Le mapping devient :

| # | Agent | Spécialisation | Rang |
|---|---|---|---|
| 01 | StarLord_Story | manifeste, brand storytelling | B3 spécialisé |
| 02 | Rocket_Auto | automation marketing, séquences | B3 spécialisé |
| 03 | Gamora_Target | ciblage, segmentation, ICP | B3 spécialisé |
| 04 | Drax_Closing | closing, dernière étape funnel | B3 spécialisé |
| 05 | Groot_Content | content production, blog, SEO | B3 spécialisé |
| 06 | Mantis_VoC | voice of customer, témoignage | B3 spécialisé |
| 07 | **Peter_Quill_Orchestrator** | sprint + dispatch + DoD partagé | **B3 squad lead** |

**Compte final** : 7. Symétrie 8 squads / 7 agents rétablie.

## La procédure d'adoption

Trois étapes, append-only D4 :

### Étape 1 — Vérification Ownerbook T1 OMK

Le compte canonique Ownerbook T1 OMK est la source de vérité. Si
Ownerbook pose ≥ 7 par squad, l'adoption est mécanique. Si Ownerbook
pose un autre compte (6, 8, autre), Superman escalade B2 Council
pour arbitrage.

**Statut vague 2** : Ownerbook T1 OMK **non lu** (hors périmètre
de cette escouade — V2/V3 exclusivement). Vérification Ownerbook
est une **tâche d'arbitrage** à effectuer en Council, pas une
déduction de cette escouade.

### Étape 2 — Création du fichier B3 Peter_Quill_Orchestrator

Si l'adoption est confirmée Ownerbook, le fichier
`04_Business_Domains/01_Growth_Superman_Guardians/squad/00_PeterQuill_Orchestrator/AGENT.md`
est créé par Meta-Factory (cf. triplet 54), pas par Superman. La
structure 4 fichiers canoniques (`AGENT.md`, `SOUL.md`, `SCRUMS.md`,
`JTBD.md`) doit être tenue.

### Étape 3 — Premier dispatch B2 → B3

Le premier JTBD packet B3 Guardians qui inclut Peter_Quill_Orchestrator
doit avoir Peter en **squad lead** signataire (cf.
`b2-b3-jtbd-handoff-contract.md` §« Le rôle du B3 squad lead »).
La double signature B2 sponsor (Superman) + B3 squad lead (Peter) est
canonique.

## L'alternative Nebula_Analytics — pourquoi écartée

Nebula_Analytics reste une **possibilité** dans deux cas :

1. **Si l'arbitrage Council frontière #3 (Superman↔IT) tranche que
   l'analytics est Growth**, Nebula_Analytics devient B3 spécialisé
   *analytics*, pas squad lead. Le compte reste 7 (Peter +
   Nebula), mais la spécialisation change.
2. **Si Peter_Quill_Orchestrator est refusé en Council** (parce
   que la symétrie n'est pas un argument canonique, par exemple),
   Nebula_Analytics peut être proposé comme 7ᵉ agent alternatif.

Mais dans les deux cas, **Peter_Quill_Orchestrator reste le candidat
par défaut** proposé par Superman.

## L'alternative compte exact 6 — pourquoi écartée

Le compte exact 6 brise :

- La symétrie 8 squads / 7 agents.
- Le Ownerbook T1 OMK DoD-1 (≥ 7 par squad).
- Le triplet 11 (5 scrums/semaine, un par jour ouvré — un agent
  sans squad lead manque un scrum).

Aucun des trois n'est arbitré canoniquement contre 6. La lecture 6
est **défendable** mais **non-défendue** par le canon.

## Anti-pièges

- **Peter_Quill_Orchestrator créé sans Ownerbook vérifié.** Cette
  escouade propose Peter comme candidat principal mais **ne crée
  pas** le fichier B3. La création est Owner / Meta-Factory après
  vérification Ownerbook T1 OMK.
- **Nebula_Analytics absorbant la frontière IT.** La frontière
  Superman↔IT reste un arbitrage Council, pas une absorption
  Growth.
- **Compte 6 sans déclaration explicite.** Si Superman adopte 6
  sans consigner dans le journal Council, c'est une décision hors
  D4. Le Council doit refuser ou exiger la consigne.
- **Peter_Quill_Orchestrator comme 7ᵉ spécialité.** Peter est
  squad lead (orchestration), pas une 7ᵉ spécialisation. Confondre
  les deux rôles casse la cohérence.

## Liens

- [[jtbd-emit-receive]] — les 6 agents listés et le débat 7ᵉ
- [[b2-b3-jtbd-handoff-contract]] — la double signature B2 sponsor + B3 lead
- [[fifty-three-b3-agent-roster]] — le compte ~7 attendu
- [[domain-perimeter]] — la frontière #3 Superman↔IT (Nebula)
- [[pair-checks-dependencies]] — couplage Superman↔IT

## Note de confiance

**Projets, à moitié étayé.** La symétrie squad lead est
**observée** dans 7 squads sur 8 (Avengers, Fantastic Four, X-Men,
Thunderbolts, Kang Dynasty, Eternals, et le candidat Illuminati).
La lecture Peter_Quill_Orchestrator est **projetée** par analogie
avec les squad leads des 7 autres squads. Le compte Ownerbook T1
OMK DoD-1 est **non vérifié** par cette escouade (hors périmètre).
Le rôle proposé (sprint + dispatch + DoD partagé) est **reconstruit**
par lecture critique du triplet 11 (5 scrums/semaine) et du triplet
41 (B3 interdit-combler-trou). L'écartement de Nebula_Analytics est
**projeté** par lecture critique de la matrice d'harmonisation
(coupleplage asymétrique Superman↔IT).