---
type: Concept
title: Superman Growth — paquets JTBD émis vers B3 Guardians et reçus de B1/B2 amont
description: Superman Growth dispatche vers 6 B3 Guardians identifiés (StarLord_Story, Rocket_Auto, Gamora_Target, Drax_Closing, Groot_Content, Mantis_VoC). Le 7ᵉ agent attendu (~7 par squad canonique) n'est pas présent dans le substrat OMK. Superman reçoit des mandates B1 et des handoffs B2 amont (Legal × Growth, Finance × Growth). Le format bilatéral signé B2 sponsor + B3 lead (cf. b2-b3-jtbd-handoff-contract) s'applique à chaque paquet.
tags: [superman, growth, jtbd, b3, guardians, packet, handoff, omk, squad]
generated: { by: minimax-m3, at: 2026-08-19T04:02:00Z }
verified:
  - { by: process:lecture-corpus-superman, at: 2026-08-19T04:02:00Z }
sources:
  - id: carto-substrat-omk
    resource: "C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/carto/01_picard_w2_unread.txt"
    title: Carto substrat OMK — 6 agents B3 Guardians listés
    last_modified: 2026-08-17
  - id: triplet-v3-line-19
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet v3 ligne 19 — Superman pairedWith Guardians (6 techniciens)"
    last_modified: 2026-08-17
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — quand une décision mésoperpétuelle devient un JTBD packet
    last_modified: 2026-08-19
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Superman Growth émet GROWTH_READY/NEEDS_SIGNAL/BLOCKED_PROMISE
    last_modified: 2026-08-17
  - id: b3-reception-checklist
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-jtbd-packet-reception-checklist.md"
    title: B3 JTBD packet reception checklist (réception côté B3)
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Superman Growth — paquets JTBD émis vers B3 Guardians et reçus de B1/B2 amont

## Ce que Superman émet vers B3 — 6 agents Guardians identifiés

Le substrat OMK (carto `01_picard_w2_unread.txt` lignes 63-77) liste
**6 agents B3** dans la squad Guardians of the Galaxy. Le triplet v3
ligne 19 confirme le compte de 6 :

| # | Agent B3 | Spécialisation | Pair-check matrice dominant |
|---|---|---|---|
| 01 | **StarLord_Story** | narrative, manifeste, brand storytelling | (Brand transverse — voir `domain-perimeter.md` frontière #2) |
| 02 | **Rocket_Auto** | automation marketing, séquences, paid ops | Finance → Growth (dépense récurrente) |
| 03 | **Gamora_Target** | ciblage, segmentation, ICP, account selection | Growth → Sales (qualification amont) |
| 04 | **Drax_Closing** | closing, conversion, dernière étape funnel | Sales → Ops (handoff closing) |
| 05 | **Groot_Content** | content production, blog, SEO, social | Legal → Growth (claims publics) |
| 06 | **Mantis_VoC** | voice of customer, case-study, témoignage | Legal → Growth (autorisation publication) |

**Le 7ᵉ agent attendu** (~7 par squad selon `fifty-three-b3-agent-roster.md`)
n'est pas présent dans le substrat OMK visible. Candidat plausible :
un **Peter_Quill_Orchestrator** (coordinateur transverse des 6
agents), ou un **Nebula_Analytics** (analytics/mixpanel —
correspond à la frontière #3 Superman vs IT, voir
`domain-perimeter.md`). **À confirmer** par lecture du Ownerbook T1
OMK (DoD-1 : `ls .claude/agents/b3-1-* | wc -l` ≥ 7).

## Ce que Superman émet — trois signaux canoniques

Le triplet ligne 27 et `eight-domain-avengers-wheel.md` posent trois
émissions canoniques de Superman Growth vers l'aval :

| Signal | Sens | Émis par | Reçu par |
|---|---|---|---|
| `GROWTH_READY` | « l'attention est qualifiée, le signal est stable » | Superman | B1 (Summers) via handoff queue |
| `NEEDS_SIGNAL` | « l'attention est insuffisante ou mal orientée » | Superman | B1 + Sales (JohnJones) |
| `BLOCKED_PROMISE` | « la parole publique est bloquée par veto Superman » | Superman | B2 Council + Aquaman (Legal) cross-veto possible |

Ces trois signaux correspondent à trois états du **DoD amont** :
*Growth est prêt à scaler* / *Growth attend un signal externe*
(segment, ICP, marché) / *Growth est bloqué par sa propre doctrine*.

## Ce que Superman reçoit — trois sources

### Source 1 — Mandates B1 (Summers)

Le B1 mandate packet (cf. `b1-mandate-packet-spec.md`) vise un
domaine. Si le mandate vise Growth (ex : *« pivoter US premium »*,
*« scaler paid media EU »*), Superman reçoit dans la handoff queue et
produit un Rock + DoD. **Le DoD doit être chiffré** (cf.
`b2-b3-jtbd-handoff-contract.md` §`dod_bornee`) : *« 1,000 MQL
qualifiés en 90 jours »*, pas *« scaler l'attention »*.

### Source 2 — Pair-checks B2 amont (Legal → Growth, Finance → Growth)

Le RACI par rang (`b2-pair-check-raci-by-rank.md`) pose Superman en
**Accountable** sur les pair-checks #5 (Finance → Growth) et #7
(Legal → Growth). Superman reçoit donc :

- **Finance** (Wonder Woman) — une dépense récurrente Growth
  (paid media, content production) qui doit porter une métrique de
  retour chiffrée (cf. triplet 58 extension Wonder Woman). Superman
  arbitre l'allocation dépense ↔ apprentissage attendu.
- **Legal** (Aquaman) — un périmètre de claims (parfois dormant,
  réveillé par un mandat Growth). Superman arbitre la portée
  publique ↔ risque juridique.

Les deux pair-checks amont sont **Receivable** par Superman en
**mode parallel ou handoff**, rarement negotiation (cf.
`cooperation-mode-patterns.md`).

### Source 3 — Pair-check B3 aval (B3 Guardians → Superman)

Le triplet 13 pose *« B3 dependsOn B2-sprint »*. Les 6 B3 Guardians
émettent vers Superman en **mode scrums.md** (5 scrums/semaine par
squad lead, cf. triplet 11). Superman reçoit en J+1 ouvré le
journal d'exécution et arbitre les blockers cross-B3 (ex : Groot et
Mantis qui se contredisent sur un case-study).

## Le contrat bilatéral B2 → B3 — Superman côté sponsor

`b2-b3-jtbd-handoff-contract.md` pose le contrat signé conjointement.
**Superman est le captain B2 sponsor** de chaque paquet JTBD émis
vers un B3 Guardians. Son rôle :

1. **Signe le contrat** conjointement avec le B3 squad lead
   (StarLord pour Story, Rocket pour Auto, etc.).
2. **Voit les lead indicators** en temps réel — pas seulement à la
   livraison. Une dérive à J+2 d'un sprint Groot_Content doit être
   visible à Superman à J+2, pas à J+7.
3. **Décide de l'escalade** au Council si la dérive dépasse le
   seuil. L'escalade tardive est sanctionnée par le Council.

Pour chaque agent B3, le contrat précise :

```yaml
jtbd_packet_id: B3-JTBD-YYYY-NN
source_meso_decision: B2-MESO-DECISION-YYYY-NN
contract_signed:
  b2_sponsor: superman
  b3_squad_lead: <starLord|rocket|gamora|drax|groot|mantis>
  signed_at: YYYY-MM-DD
cadre:
  duree: <weeks>
  squad: guardians
  captain_b2: superman
dod_bornee:
  - critere: <ex: "MQL qualifies ICP US premium">
    seuil: <ex: 1000>
    fenetre: <ex: 90j>
proof_expected:
  forme: capture|log|metrique|temoignage
  chemin: <path-or-url>
indicators:
  lead: [<metrique>, <metrique>]
  lag: [<metrique>, <metrique>]
escalade:
  first_stop: superman (captain_b2_sponsor)
  seuil_temps: 24h
```

## Les trois failure modes — particularités Superman

`b2-b3-jtbd-handoff-contract.md` pose 3 failure modes. Pour
Superman :

### Scope creep — Groot_Content qui produit du Brand work

**Risque** : Groot_Content est dans la squad Growth, mais StarLord_Story
est aussi dans la squad. Un scope qui déborde du contenu Growth vers
le brand manifeste est tentant — *« c'est plus simple, on a déjà
l'équipe »*. Superman doit refuser la livraison excédentaire et
consigner le scope creep dans le journal Council.

### Silent rework — Rocket_Auto qui re-tente sans signaler

**Risque** : Rocket_Auto travaille sur des séquences paid media.
Quand une séquence sous-performe, Rocket peut re-tenter sans
escalader Superman, en se disant *« je vais corriger »*. Le rework
non signalé consomme du budget paid media (dépense récurrente
Wonder Woman) sans que Superman ne le sache. **C'est un veto
Wonder Woman indirect** — la dépense récurrente non revue est une
violation de classe Finance → Growth.

### Escalade tardive — Mantis_VoC qui attend pour escaler un case-study

**Risque** : Mantis_VoC recueille un témoignage client. Le client
retire son accord **J-2**, mais Mantis attend J+1 pour escaler. Le
case-study a été publié (par Groot) entre J-2 et J+1. C'est un
**veto Aquaman + Superman** — case-study publié sans autorisation
(frontière #2 du `veto-catalogue-concrete.md`).

## Le 7ᵉ agent manquant — projection

L'asymétrie 6 observés / 7 attendus a trois lectures :

1. **Lecture 1 — Peter_Quill_Orchestrator** : un agent qui orchestre
   les 6 autres, dispatche les JTBD entre eux, et tient le sprint
   Guardians au niveau squad lead. C'est la lecture la plus
   défendable par symétrie avec les autres squads (Avengers ont un
   Captain America, Fantastic Four ont MrFantastic, etc.).
2. **Lecture 2 — Nebula_Analytics** : un agent qui tient l'analytics
   stack (Mixpanel, Amplitude, PostHog) — la frontière #3
   Superman vs IT, voir `domain-perimeter.md`.
3. **Lecture 3 — compte exact 6** : le canon ajusté à 6, pas 7.
   Ownerbook T1 DoD-1 *« ≥7 par squad »* n'est pas tenu pour
   Guardians. Lecture minoritaire mais possible.

**Recommandation** : vérifier Ownerbook T1 OMK verbatim avant de
trancher. Le Ownerbook est hors périmètre V2/V3 de cette escouade.

## Anti-pièges

- **6 agents comme limite dure.** Émettre un JTBD vers un 7ᵉ agent
  inexistant casse le contrat B2 → B3. Toujours vérifier que le B3
  squad lead existe avant de signer.
- **Confondre signal et DoD.** Un signal `NEEDS_SIGNAL` n'est pas un
  DoD — c'est un état amont qui demande une action. Le DoD est
  produit quand le signal est levé.
- **Pair-check amont sans sponsor.** Si Superman reçoit un handoff
  Finance → Growth sans que Wonder Woman ait signé le contrat, le
  paquet est invalide. Le captain sponsor doit refuser.
- **7ᵉ agent supposé.** Si un brief OMK mentionne un agent
  Guardians qui n'est pas dans le substrat (ex : Rocket_X, StarLord_Y),
  c'est une **erreur de canon** — Superman doit escalader B2 Council
  pour mise à jour.

## Liens

- [[b2-b3-jtbd-handoff-contract]] — le contrat bilatéral
- [[b2-pair-check-raci-by-rank]] — Superman A sur Finance→Growth et
  Legal→Growth
- [[b3-jtbd-packet-reception-checklist]] — vue B3 du même contrat
- [[domain-perimeter]] — frontières qui modifient les paquets
- [[pair-checks-dependencies]] — qui dépend de qui
- [[cooperation-mode-patterns]] — mode parallel/handoff/negotiation
  typique
- [[veto-catalogue-concrete]] — veto `BLOCKED_PROMISE` consigné dans
  le paquet

## Note de confiance

**Confirmé par machine pour les 6 agents ; reconstruit pour le 7ᵉ.**
La liste des 6 B3 Guardians est extraite verbatim du substrat OMK
carto (`01_picard_w2_unread.txt`). Le compte 6 vs 7 attendu est
**reconstruit** par comparaison avec `fifty-three-b3-agent-roster.md`
(~7 par squad) et Ownerbook T1 DoD-1 (≥7 par squad). Les trois
projections du 7ᵉ agent sont **empiriques** par analogie avec les
autres squads (Avengers Captain America, etc.). Les trois failure
modes particularisés à Superman sont **reconstruits** à partir du
contrat canonique + les frontières du `domain-perimeter.md`.
