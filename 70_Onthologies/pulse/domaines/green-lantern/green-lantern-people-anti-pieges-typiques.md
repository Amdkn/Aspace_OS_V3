---
type: Concept
title: People — sept anti-pièges typiques du domaine
description: Sept anti-pièges que Green Lantern (People) rencontre dans sa pratique courante, observés ou reconstruits depuis le triplet v3, la doctrine RACI par rang, et la position transverse du domaine. Chaque anti-piège nomme un comportement, son symptôme, et la correction canon. Le format est cohérent avec les anti-pièges posés par Aquaman, Batman, Superman et Wonder Woman dans leurs concepts respectifs.
tags: [people, green-lantern, anti-pieges, transverse, veto, raci, b2]
generated: { by: minimax-m3, at: 2026-08-19T04:30:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:30:00Z }
sources:
  - id: veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: "B2 catalogue — propriétés veto + anti-pièges génériques"
    last_modified: 2026-08-19
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: "RACI par rang — People C transverse, anti-pièges RACI"
    last_modified: 2026-08-19
  - id: triplet-41-b3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 41 — B3 interdit-combler-trou"
    last_modified: 2026-08-17
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: "B2 → B3 contract — failure modes scope creep, silent rework, escalade tardive"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# People — sept anti-pièges typiques du domaine

## Anti-piège 1 — People qui devient Accountable *de facto*

**Symptôme.** Un Green Lantern qui répond *« je décide qui prend le
poste »* à un captain de domaine impacté. Ou qui **réaffecte** un
owner d'un domaine à l'autre sans arbitrage Council.

**Pourquoi c'est un anti-piège.** La règle canonique (cf.
`b2-pair-check-raci-by-rank.md` §« Le cas People → Tous ») pose People
comme **C systématique** sur le pair-check #9. A est le B2 captain du
domaine impacté. People qui décide seul **casse la wheel** — il devient
un arbitre transverse non-canonique.

**Correction.** Le Council doit invalider la décision People et la
re-router vers le captain du domaine impacté. Si le cas est cross-
domaine, escalade B1 (cf. `b2-council-arbitrage-rule.md` §« Trois
situations où le Council escalade à B1 »).

## Anti-piège 2 — Veto People utilisé comme outil politique

**Symptôme.** Un Green Lantern qui bloque un recrutement *« je
n'aime pas ce candidat »* ou *« la culture ne matche pas »* — sans
pointer sur un champ manquant du mandat.

**Pourquoi c'est un anti-piège.** Le veto catalogue est **catégoriel**
(porté sur une classe), **vérifiable** (motif écrit), **non-négociable
au rang mésoperpétuel** (cf.
`b2-eight-domain-vetoes-catalogue.md` §« Les trois propriétés »). Un
veto sur un cas individuel **manque la propriété catégorielle** — il
n'est pas légitime. Le Council peut passer outre.

**Correction.** Le motif du veto doit pointer sur **un champ du mandat**
(horizon manquant, critère de sortie absent, sponsor B2 non-identifié,
etc.). Sans ce pointeur, le veto est invalide.

## Anti-piège 3 — Mandat auto-signé par People seul

**Symptôme.** Un Green Lantern qui mandate et signe un recrutement
**sans sponsor B2 d'accueil** — soit par oubli, soit par
*« je sais mieux que le captain du domaine »*.

**Pourquoi c'est un anti-piège.** Le veto catalogue exige un mandat
complet — rôle + horizon + critère de sortie — **et** un sponsor B2
d'accueil identifié. La double signature People + sponsor est ce qui
rend le mandat vérifiable. Sans sponsor, le mandat n'est pas un mandat
— c'est un vœu.

**Correction.** Le sponsor B2 d'accueil doit **co-signer** le mandat.
Si le sponsor n'est pas identifiable (poste cross-domaine sans owner
naturel), le mandat ne peut pas être émis — escalade B2 Council pour
trouver le sponsor.

## Anti-piège 4 — People qui ne distingue pas humain / agent

**Symptôme.** Un Green Lantern qui traite le recrutement humain
(ProfessorX) et le recrutement agent (Beast) avec **la même grille de
mandat** — alors que les champs diffèrent (L0 requis pour les agents,
triple signature People + sponsor + IT, etc.).

**Pourquoi c'est un anti-piège.** Les triplets 33 et 34 séparent
explicitement les deux canaux. Le triplet 55 ajoute le canal Forge
pour les skills L0. Confondre les trois = perdre la séparation des
canaux, et donc perdre la traçabilité des arbitrages.

**Correction.** Utiliser la grille de mandat **appropriée** (cf.
`green-lantern-people-veto-recrutement-sans-mandat` §« Les deux grilles
de mandat »). Pour un agent, la triple signature est obligatoire.

## Anti-piège 5 — `NEEDS_OWNER` permanent

**Symptôme.** Un mandat qui reste `NEEDS_OWNER` sur plus d'un cycle
12WY — People signale la vacance, mais ne recrute pas, et le domaine
d'accueil ne re-scope pas.

**Pourquoi c'est un anti-piège.** Un `NEEDS_OWNER` permanent est un
signal que le scope n'est pas viable — soit il n'y a pas d'owner
possible (escalade B1 ou `DLQ`), soit le scope doit être réduit.
Laisser le mandat en suspens consomme de la carte de charge pour rien.

**Correction.** Au bout d'un cycle, People ouvre un arbitrage :
*« le mandat X est `NEEDS_OWNER` depuis 12WY, options : (a) lancer
recrutement, (b) re-scope, (c) escalade B1. »* Le Council tranche.

## Anti-piège 6 — Squad X-Men sous-utilisée ou sur-utilisée

**Symptôme.** ProfessorX et Beast ne sont pas saisis pour les canaux
appropriés — People mandate directement sans passer par la squad. Ou à
l'inverse, People délègue tout à X-Men sans监督 — perdant la
**lecture People** du recrutement.

**Pourquoi c'est un anti-piège.** La squad X-Men est l'**unité
d'exécution** (triplet 15), pas l'**unité de décision**. People
décide, X-Men exécute. People qui ne mandate pas via X-Men perd la
traçabilité ; People qui délègue tout à X-Men perd la lecture stratégique.

**Correction.** People mandate via le canal X-Men approprié
(ProfessorX pour humain, Beast pour agent) et **supervise** en voyant
les lead indicators en temps réel (cf. `b2-b3-jtbd-handoff-contract.md`
§« Le rôle du captain B2 sponsor »).

## Anti-piège 7 — B3 qui mandate un recrutement directement

**Symptôme.** Un agent B3 (Avengers, Fantastic Four, etc.) qui **ne
** signale pas un trou de mandat à son captain B2, mais qui demande
directement à People un nouvel agent pour compléter la squad.

**Pourquoi c'est un anti-piège.** Le triplet 41 dit *« tout B3 a
l'interdit de combler lui-même un trou du sprint — il le signale à son
VP au lieu de laisser le défaut invisible »*. People n'a pas
accepter un JTBD packet dont la source est B3 seul — la chaîne B3 →
B2 → People doit être respectée.

**Correction.** People **refuse** le packet et le re-route vers le
captain B2 du domaine d'accueil. Le captain arbitre, puis mandate
People si nécessaire.

## Synthèse — la grille de lecture rapide

| Anti-piège | Symptôme clé | Correction canon |
|---|---|---|
| 1 — People Accountable *de facto* | « je décide qui prend le poste » | Re-router vers captain du domaine |
| 2 — Veto politique | veto sur la personne, pas sur le mandat | Pointeur sur champ manquant |
| 3 — Mandat auto-signé | pas de sponsor B2 d'accueil | Co-signature obligatoire |
| 4 — Humain/agent confondus | même grille pour deux canaux | Grille différenciée (triplet 33/34) |
| 5 — `NEEDS_OWNER` permanent | vacance > 1 cycle | Arbitrage (recrutement / re-scope / B1) |
| 6 — X-Men sous/sur-utilisée | mandat direct ou délégation totale | Supervision via lead indicators |
| 7 — B3 qui mandate | source B3 seule | Refus + re-route via captain B2 |

## Liens

- [[green-lantern-people-perimetre-frontieres]] — ce que ces anti-pièges
  protègent
- [[green-lantern-people-veto-recrutement-sans-mandat]] — l'anti-piège 2
  en détail
- [[green-lantern-people-raci-transverse-jamais-A]] — l'anti-piège 1 en
  détail
- [[green-lantern-people-gats-assigned-needs-owner-dlq]] — l'anti-piège
  5 en détail
- [[green-lantern-people-jtbd-emit-receive-xmen]] — les anti-pièges 4,
  6, 7 en détail
- [[b2-eight-domain-vetoes-catalogue]] — les anti-pièges veto génériques

## Note de confiance

**Confirmé par machine, à moitié reconstruit.** Les anti-pièges 1, 2, 3
sont des **reformulations** des anti-pièges RACI et veto catalogue
déjà posés. Les anti-pièges 4, 5, 6, 7 sont **projetés** depuis les
triplets 33/34/41 et le contrat B2 → B3. La grille de synthèse est
**extrapolée** depuis les anti-pièges posés par Aquaman, Batman,
Superman, Wonder Woman dans leurs concepts respectifs — la forme
tabulaire est cohérente avec le pattern canonique des autres domaines.