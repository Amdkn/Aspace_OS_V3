---
type: Concept
title: X-Men effectif canon — recompte disque 8 agents, divergence 53-roster ~7
description: Recompte exhaustif sur disque au 2026-08-19 : 8 agents X-Men polymorphes (AGENT.md + SCRUMS.md + SOUL.md) sous `coaching-os/04_Business_Domains/01_RH_Meta_Gouvernance_GreenLantern_XMen/squad/`. Le triplet 15 (8 techniciens) gagne, le fifty-three-b3-agent-roster (~7) est inexact pour X-Men. Le canon V4 est confirmé par le disque ; la 53-roster n'est pas un recomptage mais une estimation. 4 asymétries X-Men vs autres squads documentées + 3 issues A/B/C + recommandation Issue A.
tags: [people, green-lantern, xmen, effectif, recompte, 8-agents, 53-roster, disk-verified, b2, b3]
generated: { by: minimax-m3, at: 2026-08-19T08:00:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-4, at: 2026-08-19T08:00:00Z }
  - { by: process:recompte-disk-find-bash, at: 2026-08-19T08:00:00Z }
sources:
  - id: triplet-15-xmen-8
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 15 — Green Lantern VP B2 commande X-Men (8 techniciens)"
    last_modified: 2026-08-17
  - id: vp-agent-greenlantern
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/04_Business_Domains/01_RH_Meta_Gouvernance_GreenLantern_XMen/VP_AGENT.md"
    title: "VP Green Lantern — 8 techniciens X-Men (verbatim)"
    last_modified: 2026-08-02
  - id: fifty-three-roster
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: "53 B3 Agent Roster — estimation par squad"
    last_modified: 2026-08-17
  - id: recompte-disk-bash
    resource: "for d in squad/0*; do test -f $d/AGENT.md && echo OK $(basename $d); done"
    title: "Recompte disk 2026-08-19 — 8 dossiers 01_*_..08_*_ avec AGENT.md"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# X-Men effectif canon — recompte disque 8 agents

## Le fait nouveau : 8 agents confirmés sur disque

Au 2026-08-19, recompte exhaustif du répertoire
`C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/04_Business_Domains/01_RH_Meta_Gouvernance_GreenLantern_XMen/squad/`
produit **8 dossiers**, chacun contenant un triplet `AGENT.md` +
`SCRUMS.md` + `SOUL.md` :

| # | Dossier | Spécialité (cf. VP_AGENT.md) | AGENT.md |
|---|---|---|---|
| 01 | `01_ProfessorX_Recruiting` | Recruiting — sourcing, lecture profils, décision d'entrée | 881 B |
| 02 | `02_Cyclops_Onboarding` | Onboarding — 30 premiers jours, opérationnel | 892 B |
| 03 | `03_JeanGrey_Culture` | Culture — rituels, langue commune | 889 B |
| 04 | `04_Wolverine_PerfReviews` | PerfReviews — revue de performance, sans ménagement | 899 B |
| 05 | `05_Storm_OpsLeadership` | OpsLeadership — arbitrages charge, encadrement quotidien | 906 B |
| 06 | `06_Beast_TechRecruiting` | TechRecruiting — recrutement technique et agentique | 906 B |
| 07 | `07_Nightcrawler_DistributedOnboarding` | DistributedOnboarding — intégration à distance et asynchrone | 917 B |
| 08 | `08_Rogue_SkillTransfer` | SkillTransfer — cessation du tacite | 905 B |

Triplet 15 verbatim cité dans `green-lantern-people-jtbd-emit-receive-xmen.md`§« La squad X-Men : 8 agents (pas 7) ». Verbatim `VP_AGENT.md` :
> *« Squad : **X-Men** · 8 techniciens »*

**Le disque confirme le triplet 15, pas le fifty-three-roster.**

## Divergence avec fifty-three-b3-agent-roster

Le `fifty-three-b3-agent-roster.md` pose X-Men à **~7 agents** dans la
table de répartition (§« Répartition par squad »), avec une note
*« compte exact 53 vient du Ownerbook T1 (DoD-1) »* — assertion non
recomptée. Le ownerbook T1 attend `≥ 7 agents par squad` (DoD-1) ;
8 satisfait, mais le compte exact 53 reste assertif.

**Trois positions possibles** sur la divergence disque (= 8) vs roster
(estimé ~7) :

- **Lecture A — Le disque fait foi**. Huit fichiers AGENT.md existent,
  huit triplets (AGENT+SCRUMS+SOUL) existent, le VP_AGENT.md est
  cohérent. Le fifty-three-roster est une **estimation** (le fichier
  le dit : *« Agent count (estimé) »*) ; la réalité disque est **8**.
  → Recommandation : mettre à jour la fifty-three-roster avec le
  compte exact 8 à la ligne X-Men, et garder l'estimation ~7 comme
  baseline obsolète pour traçabilité.
- **Lecture B — Le roster fait foi**. Le fifty-three-roster est issu
  d'une vague de documentation Ownersbook T1 (2026-05-27) et le
  triplet 15 est canonique. Huit sur disque ne contredit pas le
  triplet 15 — le compte 8 est **canonique** ; la fifty-three-roster
  est **désynchronisée** et doit être mise à jour.
- **Lecture C — Divergence non arbitrée**. Le Council doit trancher
  entre A et B. L'absence de recomptage depuis 2026-05-27 (3 mois sans
  changelog d'effectif) entretient l'ambiguïté.

**Recommandation Issue A** : recompte canonique = 8, mettre à jour le
fifty-three-roster, sans toucher au triplet 15 (qui est correct).

## Quatre asymétries X-Men vs les autres squads

Contrairement aux 7 autres squads Marvel, X-Men présente **quatre
asymétries de structure** :

### 1. Composition par rôles opérationnels, pas par angle Marvel

Les 8 X-Men sont définis par **rôle opérationnel** (Recruiting, Onboarding,
Culture, PerfReviews, OpsLeadership, TechRecruiting, DistributedOnboarding,
SkillTransfer) — pas par **angle Marvel narratif** (CaptainAmerica lead,
BlackBolt closer, etc.). L'asymétrie est **fonctionnelle** : X-Men
couvre un **spectre People** (recrutement → intégration → performance →
transférabilité) que les autres squads ne couvrent pas.

Conséquence : la **substituabilité** entre X-Men agents est **faible**.
ProfessorX (Recruiting) ne peut pas remplacer Cyclops (Onboarding)
sans coût de transition. Les autres squads (Avengers, Fantastic4) ont
une substituabilité plus haute entre agents d'un même angle.

### 2. Squad leadership non explicite

Les 7 autres squads ont un **squad lead explicite** (CaptainAmerica
Avengers, MrFantastic Fantastic4, BlackBolt Illuminati, StarLord
Guardians, Yelena Thunderbolts, Kang Dynasty, Thena Eternals). X-Men
n'a **aucun squad lead nommé** dans `VP_AGENT.md` (§« Mon squad » liste
8 agents, sans lead). Les 8 sont au même niveau hiérarchique.

**Note de confiance** : projection. Le concept `green-lantern-people-jtbd-emit-receive-xmen.md`
mentionne un *« squad lead People DoctorStrange »* projeté — pas
vérifié sur disque. Le constat empirique est : **pas de squad lead
nommé** dans VP_AGENT.md, ni dans le canon V4, ni dans le triplet 15.

### 3. Quote-part Ownerbook T1 ≠ disque

Le fifty-three-roster pose X-Men = ~7 agents, total 8 squads × ~7 = ~56.
Mais 53 < 56 → le Ownerbook T1 attend **53 agents totaux**, pas 56.
Si X-Men est en réalité 8 (et non 7), et si les autres squads ont
leur compte exact, le total canon peut être **53 - 7 + 8 = 54** —
soit **un de plus** que l'assertion Ownerbook T1.

**Hypothèse** : le compte Ownerbook T1 inclut Originaux X-Men fondateur
**comme squad à 7**, et un **8ᵉ agent a été ajouté post-canon** (peut-être
Nightcrawler — DistributedOnboarding répond à un besoin apparu après la
vague 2026-05-27). Sans date de création par agent, l'hypothèse reste
invérifiable.

### 4. Granularité des fichiers AGENT.md (taille ~880-920 B)

Les 8 AGENT.md X-Men sont **émimétriques** (881 à 917 octets, écart
4%). Les 7 autres squads Marvel ont des fichiers AGENT.md moins
regularisés. C'est un signal de **vague de documentation commune** pour
X-Men (création simultanée), pas d'évolution organique sur 3 mois.

## Trois issues A/B/C + recommandation

L'**ouverture 7** signalée par le rapport tour 3 (*« divergence X-Men
8 (triplet 15) vs ~7 (fifty-three-b3-agent-roster) non arbitrée »*)
trouve ici sa **clôture empirique** :

- **Issue A (recommandée)** — recompte canon = 8 ; mise à jour fifty-three-roster
  ligne X-Men de `~7` à `8`. Le triplet 15 + VP_AGENT.md + disque convergent.
- **Issue B** — recompte canon = 7 ; suppression du 8ᵉ agent sur disque
  (Nightcrawler ou un autre) pour aligner sur la fifty-three-roster.
  Demande **une décision Scott Summers** que je ne peux pas prendre.
- **Issue C** — divergence maintenue ; le fifty-three-roster reste
  estimé, le canon V4 reste 8. La divergence est **documentée mais
  pas tranchée**.

**Recommandation Issue A** : la **convergence triplet 15 + VP_AGENT.md
+ disque** est un signal fort. Le fifty-three-roster est explicitement
*« Agent count (estimé) »* dans son titre — l'estimation est fausse
pour X-Men. Corriger l'estimation ne touche pas au canon.

## Anti-pièges

- **Compter les fichiers avant de recompter les agents.** Le comte 8
  sur disque **inclut** les fichiers triplet (AGENT + SCRUMS + SOUL),
  pas un unique AGENT.md. Confondre les deux = surcompte.
- **Récupérer un compte canonique 53 comme exact.** Le Ownverbook T1
  DoD-1 attend `≥ 7 agents par squad` — 53 n'est pas un compte
  recompté, c'est une **invariance formulée avant vérification**.
- **Ignorer le VP_AGENT.md comme source.** Le VP_AGENT.md Green Lantern
  est **verbatim** (« Squad : X-Men · 8 techniciens »). Il prime sur
  toute estimation tant que le canon n'est pas réécrit.
- **Décréter un squad lead sans citer le triplet canon.** Les 7 autres
  squads ont un lead canon ; X-Men n'en a pas. **L'inventer** viole
  le canon. La projection tour 1 *« DoctorStrange squad lead People »*
  est **non vérifiée** et **non canonique**.

## Liens

- [[green-lantern-people-jtbd-emit-receive-xmen]] — le périmètre X-Men
- [[green-lantern-people-veto-recrutement-sans-mandat]] — ProfessorX/Beast canoniques
- [[fifty-three-b3-agent-roster]] — la roster à mettre à jour
- [[triplet-15-verbatim]] — la source canonique 8 agents

## Note de confiance

**Confirmé par machine, à moitié reconstruit.** Verbatim triplet 15 =
cité. Verbatim VP_AGENT.md = cité. Recompte disque = mesuré ce tour 4
(8 dossiers, 8 AGENT.md, 8 SCRUMS.md, 8 SOUL.md). 4 asymétries
X-Men = **observées** par lecture de VP_AGENT.md, pas **citées** dans
le canon. Asymétrie 3 (quote-part Ownerbook) = **hypothèse** à valider
par dates de création fichiers. Issue A recommandée = **ma lecture**,
non tranchée par Council.
