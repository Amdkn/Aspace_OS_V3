---
type: Concept
title: B1 success signal — mesurable ou observable, et la règle de choix
description: Distingue success_signal mesurable (compteur, seuil, ratio chiffré) de success_signal observable (signal qui tombe sous les yeux, vérifiable sans instrument) ; pose la règle de choix B1→B2 et le mécanisme de substitution quand B2 ne peut pas tenir le signal émis.
tags: [b1, success-signal, mesurable, observable, mandate, interface, b2]
generated: { by: minimax-m3, at: 2026-08-19T02:15:00Z }
verified:
  - { by: process:synthese-pulse-b1-tour-2, at: 2026-08-19T02:15:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: b1-mandate-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-mandate-packet-spec.md"
    title: B1 mandate packet — la grammaire du paquet B1 vers B2
    last_modified: 2026-08-19
  - id: decision-charter
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/03_DECISION_CHARTER.md"
    title: B1 Decision Charter — Who decides what
    last_modified: 2026-05-31
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable
    last_modified: 2026-08-19
okf_version: "0.2"
---

# B1 success signal — mesurable ou observable, et la règle de choix

Le `success_signal` est le seul champ du mandat B1 qui sert de **contrat
ex post**. L'intent peut être reformulé ; les contraintes peuvent être
amendées ; le signal, lui, est ce sur quoi B1 tranche *après coup* que le
mandat a réussi ou échoué. C'est pourquoi son format mérite sa propre page.

## Le format canon (rappel)

`b1-mandate-packet-spec.md` pose le gabarit :

```yaml
success_signal: |
  <observation qui prouvera que le mandat a reussi>
  <delai ou cycle de mesure>
```

Deux phrases. Pas un rapport. Le format est libre à l'intérieur — et c'est
précisément le problème : un signal « le client doit être satisfait » ou
« la wheel doit être verte » n'est pas un signal, c'est un voeu.

## Mesurable vs observable — la distinction qui tranche

Deux familles de signaux, mutuellement exclusifs dans leur source de
vérité :

| Type | Source de vérité | Coût de vérification | Latence | Exemple |
|---|---|---|---|---|
| **Mesurable** | Un compteur (CRM, billing, log, MRR) | Instrument + accès lecture | Définie par le cycle de mesure | « NPS ≥ 40 sur 30 réponses du segment cible, fin de 12WY » |
| **Observable** | Un fait qu'un tiers peut attester sans instrument dédié | Témoin + convention d'observation | Immédiate à la prochaine revue | « 3 sign-offs Legal Aquaman citent dans le rapport de fin de cycle » |

**Mesurable** = la réalité devient un chiffre. **Observable** = la réalité
reste un fait, mais ce fait est public.

## La règle de choix — quand préférer l'un à l'autre

Cinq critères, dans l'ordre. Le premier qui tranche suffit :

1. **Le signal a-t-il un compteur naturel ?** Si oui et que le compteur est
   lisible par B2 sans intervention B1 → **mesurable**. (Exemples : MRR,
   adoption %, churn, runway.)
2. **Le signal touche-t-il un domaine sans instrument de mesure ?** Si oui →
   **observable**, parce qu'inventer un instrument pour le mandat est un
   projet en soi, pas une clause de mandat.
3. **Le signal touche-t-il un veto catalogue ?** (cf. `b2-eight-domain-vetoes-catalogue`)
   → **observable**, parce que les vetos sont des faits publics (motif
   dans le packet Council) et le B1 les valide comme tels.
4. **Le signal est-il temporel et binaire ?** (Exemples : « batiment
   livré », « contrat signé ») → **observable**, parce qu'un compteur
   n'apporte rien et le témoin suffit.
5. **Sinon** → **mesurable**, en gardant la porte ouverte à un substitut
   observable si B2 ne peut pas tenir le compteur (voir § suivant).

## Le mécanisme de substitution — quand B2 ne peut pas tenir le signal

`b1-mandate-packet-spec.md` dit : *« B2 remonte avec 'ce signal n'est pas
atteignable, voici un substitut' »*. Le substitut est légitime ssi trois
conditions sont remplies :

- **Substitut dans la même famille.** Un signal mesurable ne se remplace
  pas par un signal observable — ce serait baisser la barre de mesure
  *et* la barre de vérification. Substitut = mesurable → mesurable ;
  observable → observable.
- **Substitut corrélé au intent.** Le nouveau signal doit porter sur la
  même intention ; un signal qui mesure un proxy facile n'est pas un
  signal, c'est une dérive.
- **Substitut accepté par B1 dans les 72 h.** Sans acceptation B1, le
  substitut n'a pas de force — c'est une discussion, pas un contrat.

Le mécanisme de substitution est **le seul moment** où B1 réécrit le
contrat d'un mandat qu'il a lui-même émis. C'est pourquoi le substitut
doit être *tracé* — logué dans la même handoff queue, daté, et indexé
contre le `b1_b2_mandate_id` d'origine.

## Pourquoi pas les deux (mesurable + observable)

Un mandat qui cumule les deux types de signaux a deux problèmes :

- **Coût de vérification doublé.** B2 doit tenir un compteur ET publier
  un fait. Pour un mandat tactique, c'est de la bureaucratie.
- **Risque de contradiction.** Si les deux signaux désalignent (compteur
  vert, fait absent, ou inversement), B1 doit arbitrer — et le mandat
  bascule en arbitrage B1 au lieu d'être évalué mécaniquement.

La règle : **un seul signal par mandat**, le plus contraint des deux
candidats. La contrainte gagne, pas la commodité.

## Trois signaux mal écrits (anti-patterns)

| Anti-pattern | Lecture | Reformulation |
|---|---|---|
| « Le client doit être satisfait » | Observable sans témoin | « NPS ≥ 40 sur 30 réponses, fin 12WY » (mesurable) |
| « MRR doit croître » | Mesurable sans seuil | « MRR ≥ $X, soit +Y% vs début de cycle » (mesurable) |
| « La wheel doit être verte » | Observable sans moment | « 8/8 domaines B2_READY au rollover, audit Council signé » (observable) |

Les trois sont des voeux. La règle : **pas de seuils = pas de signal** ;
**pas de témoin = pas de signal** ; **pas de délai = pas de signal**.

## L'articulation avec la matrice B2

Le signal B1 ferme le contrat. La matrice B2 (cf. `b2-harmonization-matrix-exploitable`)
ouvre le test des transitions. Si le signal B1 ne dépend pas d'une
transition (ex. : adoption produit), B2 doit quand même valider que la
transition Product→Ops tient — sinon le signal arrive avec un support
effondré derrière.

La règle d'usage : **le signal B1 et la matrice B2 sont complémentaires,
pas redondants.** Le signal teste le *what* ; la matrice teste le *how*.

## Sources

- `b1-mandate-packet-spec.md` — le gabarit et la règle de substitution.
- `03_DECISION_CHARTER.md` §« Les escalation thresholds » — exemples de
  signaux mesurables (MRR decline > 5%, runway < 9 mois).
- `b2-harmonization-matrix-exploitable.md` — l'aval matrice.

## Liens

- [[b1-mandate-packet-spec]] — le gabarit qui contient le signal
- [[b1-mandate-acceptance-check]] — la face miroir (B2 valide en 24h)
- [[b2-harmonization-matrix-exploitable]] — l'aval qui teste les transitions
- [[b1-omk-t2-pivot-us-mandate]] — application au pivot US OMK T2

## Note de confiance

**Confirmé par machine.** Distinction mesurable/observable reconstruite
à partir du gabarit mandat + de la doctrine matrice + des seuils
d'escalade du Decision Charter. Mécanisme de substitution : reformulé
à partir de la note du `b1-mandate-packet-spec.md` (« B2 remonte avec
'ce signal n'est pas atteignable, voici un substitut' »), pas une section
explicite du canon.