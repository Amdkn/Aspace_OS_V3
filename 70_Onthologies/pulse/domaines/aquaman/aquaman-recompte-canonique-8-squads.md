---
type: Concept
title: Aquaman — recompte canonique des 8 squads : un acte de vérification en début de 12WY
description: Le rapport tour 3 §T6.5 a posé que *« le recompte 0 fichier invalide partiellement la doctrine fifty-three »* (cf. [[aquaman-effectif-eternals-arbitrage]]). Le tour 4 transforme l'observation en **acte canonique de vérification** : un recompte `find` sur les 8 squads Marvel, exécuté à T-0 de chaque 12WY, dont le résultat alimente un packet mésoperpétuel `B2-MESO-DECISION-YYYY-NN-materiel-squad`. Aquaman est co-signataire parce que la squad Eternals est la première touchée (0 fichier au 2026-08-19), mais l'acte est transverse — les 8 capitaines受益ent.
tags: [b2, recompte, canon, vérification, 12wy, squad, fifty-three-roster, aquaman, materiel, t-0]
generated: { by: minimax-m3, at: 2026-08-19T06:10:00Z }
verified:
  - { by: process:lecture-canon-aquaman-tour-4, at: 2026-08-19T06:10:00Z }
sources:
  - id: aquaman-effectif
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-effectif-eternals-arbitrage.md"
    title: Aquaman effectif Eternals — recompte 0 fichier et 3 issues A/B/C
    last_modified: 2026-08-19
  - id: rapport-tour-3
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-aquaman.md"
    title: "Rapport tour 3 §T6.5 — le recompte comme acte canonique de vérification"
    last_modified: 2026-08-19
  - id: fifty-three-roster
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: "53 B3 Agent Roster — doctrine ~7 agents par squad"
    last_modified: 2026-08-17
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — 8 squads Marvel
    last_modified: 2026-08-17
  - id: b2-meso-packet
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: "Meso Decision Packet — format append-only D4"
    last_modified: 2026-08-19
  - id: b2-council-cadence
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-cadence-and-chair.md"
    title: "B2 Council cadence — séance bilan fin de 12WY"
    last_modified: 2026-08-19
  - id: b3-source
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: "Action-Reaction: `find .claude/agents -name 'b3-1-*' | wc -l` ≥ 7 (X-Men)"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Aquaman — recompte canonique des 8 squads

## Le constat qui motive l'acte

Le rapport tour 3 ([[rapport-tour-3]]) §T6.5 a posé :

> *« Le recompte 0 fichier invalide partiellement la doctrine
> fifty-three. La doctrine fifty-three roster pose *« ~7 par squad »*
> — c'est un invariant formulé (Ownerbook T1), pas un comptage. Si le
> recompte donne réellement 7 par squad (avec une commande `find`
> correcte), la doctrine est validée. Si le recompte donne 0 (comme
> Eternals), la doctrine est fausse pour ce squad. »*

Le [[aquaman-effectif]] a documenté le recompte `find . -name 'b3-eternals-*'`
→ 0 fichier au 2026-08-19. Le **problème** n'est pas Eternals seule : si
Eternals = 0, **les 7 autres squads peuvent être dans le même cas**, sans
que personne ne le sache. La doctrine fifty-three est *assertive* (Ownerbook
T1), pas *vérifiée*. C'est un angle mort mésoperpétuel.

## La proposition — un acte canonique à T-0

À **T-0 de chaque 12WY** (avant la séance bilan du cycle précédent, cf.
[[b2-council-cadence]] §3. Séance bilan), le secrétariat Council — pas un
capitaine seul, **le president de la séance bilan** — lance le recompte
des 8 squads :

```bash
cd /path/to/depot && {
  for squad in x-men fantastic-four avengers illuminati guardians thunderbolts kang-dynasty eternals; do
    count=$(find . -name "b3-${squad}-*" -type f 2>/dev/null | wc -l)
    echo "  - ${squad}: ${count}"
  done
}
```

L'ordre des squads est **alphabétique**, pas hiérarchique — pour éviter
qu'un recompte tronqué ne masque une squad oubliée.

## Le format de sortie — packet `B2-MESO-DECISION-...-materiel-squad`

Le résultat du recompte alimente un **packet mésoperpétuel spécialisé** :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN-materiel-squad
source_mandate: B2-PEER-YYYY-NN (audit 12WY T-0)
mode: parallel  # aucune négociation inter-domaine
impacted_domains: [all_8_domains]
tradeoff: |
  Recompte T-0 12WY YYYY-QN. Résultat par squad :
  - x-men: N1
  - fantastic-four: N2
  - avengers: N3
  - illuminati: N4
  - guardians: N5
  - thunderbolts: N6
  - kang-dynasty: N7
  - eternals: N8
  Écart total : ΣNi - 53 = X. Écart par squad : cf. issue par squad.
decision: accepted | blocked | escalate_to_B1
proof_expected:
  - recompte canonique 12WY suivant avec écart réduit
  - matérialisation squad(s) en écart (≥7 pour squad canonique)
next_review: 12WY-YYYY-Q(N+1)
```

Le packet est **archivé en D4** dans
`B2_DC_DIRECTION_COUNCIL_DECISIONS.md` (cf. [[b2-meso-packet]] §Append-only).
C'est la **seule** trace canonique de l'écart entre la doctrine fifty-three
(Ownerbook T1) et la matérialisation effective.

## Pourquoi T-0, pas T-7j ou T+30j

- **T-0** capte l'état **au début du cycle**, avant que les Rocks du
  nouveau 12WY ne soient déposés. C'est la photographie la plus propre.
- **T-7j avant launch** ne marche pas — le recompte est annuel, pas
  par launch (le portique Aquaman T-7j est distinct, cf.
  [[aquaman-launch-ready-portique-final]]).
- **T+30j post-cycle** est trop tard — l'écart a déjà produit ses
  effets sur le cycle qui finit. C'est de l'**autopsie**, pas de la
  **prévention**.

**Conséquence** : T-0 est l'horizon opérationnel qui permet de **détecter
un écart naissant** avant qu'il ne dégrade un cycle de production.

## Les 3 issues possibles par squad

Chaque squad peut tomber dans l'une des trois issues (par symétrie avec
[[aquaman-effectif]] §3 issues A/B/C) :

### Issue A — Matérialisation effective >= 7

La squad est conforme à la doctrine fifty-three. **Aucun action** —
archivage seul.

### Issue B — Matérialisation partielle (1 ≤ N ≤ 6)

Squad partiellement matérialisée. **Action recommandée** : identification
des fiches agents manquantes, escalade People (Green Lantern) pour
recrutement des fiches restantes. **Délai** : T+30j (1 sprint).

### Issue C — Matérialisation zéro (N = 0)

Squad non matérialisée. **Action obligatoire** : escalade B1 — la squad
est en risque de dissolution implicite. **Délai** : T-0 12WY suivant
— la squad doit avoir au moins 1 fiche avant la prochaine photographie.

**Note** : Eternals est en Issue C au 2026-08-19 (cf.
[[aquaman-effectif]]). Le recompte T-0 12WY-2026-Q3 confirme ou infirme.

## Le rôle spécifique d'Aquaman dans le recompte

Aquaman **n'est pas l'auteur** du recompte — c'est le secrétariat Council.
Mais Aquaman est **co-signataire** du packet mésoperpétuel parce que :

1. **Eternals est sa propre squad** — Aquaman porte la responsabilité
   directe de la matérialisation Eternals.
2. **Issue C Eternals est un signal d'absence** (cf.
   [[b2-areas-dormants-doctrine]] §Pourquoi la dormance n'est pas
   l'absence) — Aquaman doit rendre compte.
3. **Le recompte révèle le gap entre canon et exécution** — c'est
   précisément ce que la doctrine mésoperpétuelle doit éviter.

**Conséquence** : un Aquaman SHADOW_ACTIVE (cf.
[[aquaman-dormant-activation]]) co-signe un packet de matérialisation **non
applicable** à sa propre squad — c'est cohérent : il consigne qu'Eternals
est non-matérialisé, mais il ne peut pas *matérialiser* depuis SHADOW_ACTIVE.
La matérialisation est une action People (Green Lantern) — pas Aquaman.

## La conservation du recompte — auditable

Le packet `B2-MESO-DECISION-YYYY-NN-materiel-squad` est **archivé D4**.
Chaque recompte annuel produit une nouvelle ligne. La séquence temporelle
permet de détecter des **tendances** :

- Eternals 0 → 0 → 0 (3 recomptes consécutifs) = **dissolution implicite**.
- Eternals 0 → 1 → 3 (progression) = **matérialisation en cours**.
- X-Men 7 → 7 → 8 (ajout) = **extension** (probablement NouvelleRecrue,
  à valider avec People).

**Sans la séquence D4**, ces tendances sont **invisibles**. L'acte
canonique n'est pas seulement le recompte isolé — c'est la **trajectoire**
sur 12WY × N.

## Anti-pièges

- **Recompte sans conservation D4.** Un recompte qui n'aboutit pas à un
  packet mésoperpétuel archivé n'a pas de **valeur canonique** — c'est
  une observation privée, pas un acte.
- **Recompte sans discrimination V2/V3.** Le find pattern peut chasser
  dans V2 (`ASpace_OS_V2`) ou dans V3 (`ASpace_OS_V3`). Les deux
  contiennent des références aux 8 squads, mais l'effectif **réel**
  d'un agent en production est ce qui compte. La mitigation : chasser
  uniquement dans le **dépôt courant de production** (V3) et noter
  explicitement les résultats V2 comme *legacy*.
- **Aquaman qui monopolise le recompte.** Le recompte est **transverse**.
  Aquaman est co-signataire, pas owner. Si Aquaman porte seul le
  recompte, il devient bottleneck. La mitigation : secrétariat Council
  (un capitaine A différent à chaque 12WY, par rotation).
- **Confondre recompte et audit d'effectif.** Un recompte `find` est une
  **photographie**, pas un audit. Pour auditer un squad, il faut
  interviewer le captain. Le recompte est **préalable** à l'audit, pas
  l'audit lui-même.
- **Recompte annuel sans interpolation.** Si le 12WY dure 12 semaines,
  l'écart peut apparaître et disparaître dans le cycle. Le recompte
  annuel manque la volatilité intra-cycle. La mitigation (optionnelle) :
  recompte **mensuel** léger (juste `wc -l`) entre les T-0, pour
  détecter les解散 et recrutements rapides.

## Liens

- [[aquaman-effectif-eternals-arbitrage]] §3 issues A/B/C — la
  taxonomie d'écart par squad
- [[rapport-tour-3]] §T6.5 — la suggestion initiale de recompte comme
  acte canonique
- [[fifty-three-b3-agent-roster]] — la doctrine ~7 agents par squad
  qui pose l'invariant
- [[eight-domain-avengers-wheel]] — le mapping 8 squads ↔ 8 domaines
  qui permet le cross-check squad ↔ captain
- [[b2-meso-decision-packet-spec]] — le format standard du packet
  mésoperpétuel (la présente proposition est une spécialisation)
- [[b2-council-cadence-and-chair]] §3. Séance bilan — le moment T-0
  12WY où le recompte s'inscrit
- [[b2-areas-dormants-doctrine]] — la distinction dormance vs absence
  que le recompte matérialise
- [[aquaman-dormant-activation]] — la condition ACTIVE qui permet la
  matérialisation effective (vs SHADOW_ACTIVE)
- [[aquaman-launch-ready-portique-final]] §Anti-pièges Aquaman qui
  devient goulot — la mitigation par pré-vetter qui s'applique aussi
  au recompte

## Note de confiance

**Reconstruit, projeté depuis un constat empirique.** Le besoin est
**posé verbatim** par [[rapport-tour-3]] §T6.5. Le format YAML du packet
`B2-MESO-DECISION-YYYY-NN-materiel-squad` est **projeté** par
généralisation de [[b2-meso-packet]] (8 champs obligatoires) — c'est
une **spécialisation** d'un format posé, pas une nouvelle doctrine.
Le choix de **T-0 12WY** est **calibré** depuis la cadence canonique
([[b2-council-cadence]] §3) et la pratique des bilans de cycle. Les
3 issues A/B/C sont **posées verbatim** par [[aquaman-effectif]]. Le
rôle co-signataire Aquaman est **projeté** depuis la position Aquaman
sur Eternals, **pas cité** ailleurs dans le corpus comme tel. La
séquence D4 et la détection de tendance sont **empirées** de la
doctrine D4 append-only ([[b2-council-cadence]] §Le journal Council).
**À vérifier en cycle** : (1) le secrétariat Council tient-il la
cadence annuelle ?, (2) la discrimination V2/V3 est-elle nette, ou
faut-il chasser dans les deux et merger ?, (3) la mitigation recompte
mensuel léger est-elle tenable (charge induite), ou reste-t-on sur
un T-0 annuel ?, (4) le recompte révèle-t-il que d'autres squads
sont en Issue C (pas seulement Eternals) ?
