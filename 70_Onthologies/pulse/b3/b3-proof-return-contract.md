---
type: Concept
title: B3 proof return contract — le miroir B3 → B2 de la handoff
description: Le contrat B2 → B3 (B2 sponsor) promet un périmètre et un DoD. Le contrat B3 → B2 retourne la livraison : 4 formes de preuve (capture, log, diff, output reproductible), 5 acceptance checks B2, 3 failure modes B3 (silent acceptance, proof inflation, premature DONE). Le format conjoint YAML est l'inverse de `b2-b3-jtbd-handoff-contract.md`.
tags: [b3, proof, return, contract, accept, done, b2, mirror, handoff]
generated: { by: minimax-m3, at: 2026-08-19T03:10:00Z }
verified:
  - { by: process:lecture-b3-corpus-tour-1, at: 2026-08-19T03:10:00Z }
  - { by: process:synthese-pulse-b3-tour-2, at: 2026-08-19T03:10:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: handoff
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — quand une décision mésoperpétuelle devient un JTBD packet
    last_modified: 2026-08-19
  - id: proof-path
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-proof-path-4-formes.md"
    title: B3 proof path — la preuve inspectable
    last_modified: 2026-08-19
  - id: veto-signal
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-veto-and-signal-vocabulary.md"
    title: B3 veto and signal vocabulary
    last_modified: 2026-08-19
  - id: sprint-close
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-sprint-close-mechanics.md"
    title: B3 sprint close — la mécanique du vendredi
    last_modified: 2026-08-19
  - id: agent-relecteur
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/autonomie-agents/agent-relecteur-mandat.md"
    title: Agent relecteur — mandat unique, contexte vierge
    last_modified: 2026-08-17
  - id: examen-prealable
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/autonomie-agents/examen-prealable.md"
    title: L'examen préalable — une commande unique qui prouve avant de rendre
    last_modified: 2026-08-17
okf_version: "0.2"
---

# B3 proof return contract — le miroir B3 → B2 de la handoff

> Le contrat B2 → B3 (`b2-b3-jtbd-handoff-contract.md`) pose ce que B2
> promet : cadre, DoD bornée, captain sponsor, contract_signed à
> double signature. Ce concept pose **ce que B3 rend** : la preuve
> dans l'une des 4 formes canoniques, le format conjoint YAML, les
> 5 acceptance checks que B2 applique pour valider, et les 3 failure
> modes côté B3 (silent acceptance, proof inflation, premature
> `DONE`).

## Le principe du miroir

Un contrat bilatéral a deux faces. Si B2 promet sans que B3 ne
s'engage à prouver, B2 ne peut pas distinguer une livraison
honnête d'un placeholder. Le format conjoint du packet
(`contract:` block dans le JTBD packet, cf. handoff §« Le format
conjoint ») porte un second bloc `delivery:` que B3 remplit au
moment du `DONE`.

L'invariant : **un `DONE` sans bloc `delivery:` rempli n'est pas un
`DONE`** — c'est un `AT_RISK` qui s'ignore. Le B2 sponsor peut
refuser de marquer la gate à `READY` si le bloc est vide ou
lacunaire (cf. `b3-veto-and-signal-vocabulary.md` §« Anti-patterns »
— *« B3 qui émet `DONE` sans preuve »*).

## Le bloc `delivery:` — format conjoint

À l'inverse du bloc `contract:` qui contient les promesses B2, le
bloc `delivery:` contient les **constats B3** au moment du `DONE`.
Le format est verrouillé à 6 champs :

```yaml
delivery:
  by:                <b3-handle>          # qui rend
  at:                <YYYY-MM-DDTHH:MM>   # horodatage précis
  proof_forms:       # 1 à 4 formes, cf. b3-proof-path-4-formes.md
    - forme:         capture | log | diff | output_reproductible
      chemin:        <path-or-url>
      consommateur:  b2_owner | b2_council | squad_lead | futur_b3
  proof_acceptance:  # 5 checks B2 applique (cf. infra)
    scope_respected:    true | false
    dod_seuil_atteint:  true | false
    lead_indicators:    true | false | n/a
    lag_indicators:     true | false | n/a   # lag = mesuré après, peut être n/a
    no_violation:       true | false         # aucun veto enfreint
  examen_prealable:   # sortie de tools/examen.sh, si périmètre code
    run:               OK | N/A | FAIL_<etape>
    journal:           <path vers le journal d'examen>
  relecteur:          # pair-relecteur en contexte vierge, si livré > 200 lignes
    run:               OK | N/A | NÉANT
    journal:           <path ou néant>
  holes_open:         [<hole_id>, ...]   # HOLE non résolus à la livraison
  sprint_outcome:     CLEAN | DRAGGED | CANCELLED
  next_recommendation: <1 phrase — ce que B3 suggère pour la suite>
```

## Les 5 acceptance checks B2

Quand le B2 sponsor reçoit un bloc `delivery:`, il applique 5
vérifications avant de marquer la gate à `READY` (cf. handoff §« Rôle
du capitaine B2 sponsor »). Chaque check est binaire, sauf
`lead_indicators` et `lag_indicators` qui admettent `n/a` quand le
domaine ne s'y prête pas.

### Check 1 — `scope_respected`

Le scope livré correspond au scope contracté. Le B2 compare la
**diff** entre `jtbd_packet.received` (champ `dod_bornee`) et
`jtbd_packet.delivered` (champ `proof_forms` + artefacts). Si la
diff est non vide, c'est du **scope creep** (cf. handoff §« Les
trois failure modes — 1. Scope creep »).

### Check 2 — `dod_seuil_atteint`

Pour chaque critère du DoD borné (handoff §« Ce que B2 Council
promet — 2. Bornes DoD explicites »), le seuil chiffré est
atteint. Un DoD *« NPS ≥ 40 »* est `true` si NPS mesuré = 42, et
`false` si NPS = 35. Pas d'arrondi optimiste.

### Check 3 — `lead_indicators`

Les lead indicators (handoff §« Ce que le B3 squad promet — 2.
Lead indicators ») ont été suivis en cours de sprint, et leur
tendance était verte ou a été escaladée. Le B2 sponsor compare
avec ce qu'il a vu en temps réel via le DISPATCH.md (cf.
`b3-squad-lead-dispatch-protocol.md`).

### Check 4 — `lag_indicators`

Les lag indicators (handoff §« 3. Lag indicators ») sont mesurés à
la livraison. Pour un outcome à J+30 (rétention), `n/a` est
accepté à la livraison — le lag sera mesuré plus tard, et le
B3 s'engage à le remonter.

### Check 5 — `no_violation`

Aucun des 8 vetos B2 (cf. `b3-veto-and-signal-vocabulary.md`
§« Couche 1 ») n'a été enfreint pendant le sprint. Si un veto a
été escaladé puis assoupli (handoff §« Quand un veto s'applique »),
le B2 vérifie que l'assouplissement est documenté.

## Les 3 failure modes côté B3

Le handoff contract pose 3 failure modes côté B2 (scope creep,
silent rework, escalation tardive). Le miroir côté B3 a 3 failure
modes distincts :

### Failure mode 1 — Silent acceptance

**Symptôme** : le B2 sponsor accepte tacitement la livraison sans
passer les 5 acceptance checks. La gate passe à `READY` par
inertie. Le B3 ne s'en rend pas compte — la livraison est
officiellement acceptée, mais aucun des checks n'a vraiment été
appliqué.

**Détection** : le `SPRINT_SUMMARY.md` (cf.
`b3-sprint-close-mechanics.md`) ne porte pas de `B2_RECEIPT` signé.
Le B3 qui voit sa close acceptée sans accusé **relance** le B2
sponsor.

**Remède** : le format conjoint impose un `B2_RECEIPT` signé en
réponse au bloc `delivery:`. Sans signature, la livraison est
**en attente d'acceptance**, pas acceptée.

### Failure mode 2 — Proof inflation

**Symptôme** : le B3 joint 4 formes de preuve pour signaler
qu'il a « tout fait », alors que le job n'en demandait que 2.
L'agent relecteur passe plus de temps à lire les preuves
qu'à valider le job.

**Détection** : le nombre de `proof_forms` dépasse 2 sans
justification dans `next_recommendation`. Le B2 sponsor peut
refuser les preuves excédentaires et demander une distillation.

**Remède** : le B3 cite, pour chaque forme, son **consommateur
canonique** (cf. `b3-proof-path-4-formes.md` §« Les 4 formes
canoniques »). Une forme sans consommateur cité est de
l'inflation.

### Failure mode 3 — Premature `DONE`

**Symptôme** : le B3 émet `DONE` alors qu'un `HOLE_OPEN` est
encore dans `holes_open`. Le `DONE` est invalide (cf.
`b3-hole-signaling-doctrine.md` §« Lien avec la preuve et
l'examen »).

**Détection** : `holes_open` est non vide dans le bloc
`delivery:`. Le bloc est rejeté par le B2 sponsor.

**Remède** : le B3 classifie le sprint en DRAGGED (cf.
`b3-sprint-close-mechanics.md` §« Issue 2 ») et laisse B2
arbitrer la suite. Un HOLE_OPEN à la livraison est un HOLE à
escalader, pas un HOLE à taire.

## Le B2_RECEIPT — la signature retour

Le B2 sponsor répond au bloc `delivery:` par un `B2_RECEIPT` signé,
dans un format verrouillé à 4 champs :

```yaml
b2_receipt:
  by:                <b2-sponsor>
  at:                <YYYY-MM-DDTHH:MM>
  acceptance:        ACCEPTED | ACCEPTED_WITH_RESERVE | REJECTED
  proof_check:       # écho des 5 acceptance checks
    scope_respected:    true | false
    dod_seuil_atteint:  true | false
    lead_indicators:    true | false | n/a
    lag_indicators:     true | false | n/a
    no_violation:       true | false
  next_step:         <TRIGGER_SPRINT_NEXT | HOLD | ROLLBACK | RETRY>
  notes:             <1 paragraphe — ce que B2 a vu, ce qu'il a demandé>
```

`ACCEPTED_WITH_RESERVE` est une issue valide : le scope est tenu
mais un lag indicator sera mesuré plus tard, ou un HOLE a été
classé `WONT_FIX` (cf. `b3-hole-signaling-doctrine.md` §« Le cycle
de vie du trou »). Le B2 consigne la réserve et date la
**levée de réserve** prévue.

## Anti-patterns

1. **`DONE` sans bloc `delivery:`** — un signal `DONE` (cf.
   `b3-veto-signal-vocabulary.md` §« Couche 3 ») émis sans
   livraison du bloc est un faux `DONE`. Le B2 peut le refuser.
2. **`DONE` avec `holes_open` non vide** — invalidant (failure
   mode 3).
3. **Preuve sans consommateur cité** — inflation (failure mode 2).
4. **Pas de `B2_RECEIPT` après 24h** — le B3 escalade au B2
   sponsor puis au B2 Council si pas de réponse. Le sprint reste
   **en attente d'acceptance** entre temps.
5. **B3 qui accepte un `REJECTED` sans contester** — un rejet
   sans motif dans `notes` est un veto de fait, et le B3 peut
   contester par un ping pair (cf. `b3-peer-unblock-protocol.md`).

## Lien avec l'agent relecteur et l'examen

`agent-relecteur-mandat.md` §« Pourquoi ne pas automatiser » pose
que la preuve couvre les défauts **sémantiques**. Le bloc
`delivery:` rend cette preuve **explicite** :

- **Forme 1 (capture)** : le bord visuel.
- **Forme 2 (log)** : le défaut temporel.
- **Forme 3 (diff)** : le défaut mécanique.
- **Forme 4 (output reproductible)** : le défaut de dépendance.

L'agent relecteur **consomme** le bloc `delivery:` — il ne le
produit pas. Le champ `relecteur.run: OK` dans le bloc est la
**trace** que la relecture a eu lieu, pas la relecture elle-même.

`examen-prealable.md` §« L'obligation côté brief » impose
`tools/examen.sh` avant la livraison. Le champ
`examen_prealable.run: OK` est la trace que l'examen a passé.
Sans cette trace, le bloc `delivery:` est **incomplet** sur les
périmètres code.

## Source du concept

- `b2-b3-jtbd-handoff-contract.md` §« Le format conjoint » — le
  bloc `contract:` parent, dont `delivery:` est le miroir.
- `b3-proof-path-4-formes.md` §« Les 4 formes canoniques » — la
  nomenclature des preuves.
- `b3-sprint-close-mechanics.md` §« Issue 1 — CLEAN » — le
  contexte dans lequel le bloc est typiquement émis.
- `b3-hole-signaling-doctrine.md` §« Le cycle de vie du trou » —
  la cohérence `DONE` ↔ `holes_open` vide.
- `agent-relecteur-mandat.md` §« Pourquoi ne pas automatiser » —
  la séparation preuve mécanique / preuve sémantique.

## Liens

- [[b2-b3-jtbd-handoff-contract]] — le bloc `contract:` parent
- [[b3-proof-path-4-formes]] — les 4 formes canoniques
- [[b3-sprint-close-mechanics]] — l'issue CLEAN qui porte le bloc
- [[b3-veto-and-signal-vocabulary]] — le signal `DONE` qui ouvre le bloc
- [[b3-hole-signaling-doctrine]] — failure mode 3
- [[b3-squad-lead-dispatch-protocol]] — le B2 sponsor qui consomme le bloc

## Note de confiance

**Confirmé par machine.** Le format `contract:` du handoff est
verrouillé ; son miroir `delivery:` est **projeté** à partir de
la pratique et des 4 formes canoniques de preuve. Les 3 failure
modes (silent acceptance, proof inflation, premature DONE) sont
**reconstruits** à partir des anti-patterns分散 dans
`b3-proof-path-4-formes.md` et `b3-hole-signaling-doctrine.md`.

**Limite signalée** : le format conjoint YAML à 6 champs
`delivery:` + 4 champs `B2_RECEIPT` est **proposé**, pas
**validé** par un cycle B3 réel. Le critère « 24h sans
B2_RECEIPT = escalade » est indicatif — à calibrer au premier
sprint documenté.
