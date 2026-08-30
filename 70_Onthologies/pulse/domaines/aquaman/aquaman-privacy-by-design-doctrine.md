---
type: Concept
title: Aquaman — Privacy by Design (RGPD Article 25, extend pair-check #8)
description: La Privacy by Design (PbD) est une doctrine juridique imposée par RGPD Article 25 + CCPA §1798.100 + Loi Informatique et Libertés. Elle exige que la protection des données personnelles soit intégrée au produit *à la conception*, pas ajoutée après. Aquaman étend ici la classification 4 formes ([[aquaman-classification-risques-4-formes]]) — la classe 1 (privacy/data) n'est plus traitée comme un *audit ex post* mais comme un *gate ex ante* sur le pair-check #8 (Legal × Product). 5 contrôles obligatoires avant merge, 3 cas de suspension Privacy Gate, 3 cas abusifs (privacy-washing), 4 issues de levée du gate.
tags: [b2, aquaman, privacy, rgpd, by-design, article-25, cyborg, flash, pair-check-8]
generated: { by: minimax-m3, at: 2026-08-19T07:00:00Z }
verified:
  - { by: process:lecture-canon-aquaman-tour-6, at: 2026-08-19T07:00:00Z }
sources:
  - id: aquaman-classification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-classification-risques-4-formes.md"
    title: Aquaman classification 4 formes (privacy/claim/IP/contract)
    last_modified: 2026-08-19
  - id: aquaman-pair-check-8
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-gates-et-pair-checks.md"
    title: Aquaman gates et pair-checks (Legal × Growth #7, Legal × Product #8)
    last_modified: 2026-08-19
  - id: aquaman-jtbd
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-jtbd-emit-receive.md"
    title: Aquaman catalogue JTBD émis et reçus
    last_modified: 2026-08-19
  - id: aquaman-couplages
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-couplages-invisibles.md"
    title: Aquaman couplages invisibles (Cyborg ↔ Aquaman privacy)
    last_modified: 2026-08-19
  - id: aquaman-portique
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-launch-ready-portique-final.md"
    title: Aquaman portique Batman T-7j
    last_modified: 2026-08-19
  - id: b2-harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman — Privacy by Design (RGPD Article 25, extend pair-check #8)

## La question que le corpus ne posait pas

Le pair-check #8 ([[aquaman-gates-et-pair-checks]]) pose que
« *les frontières IP/privacy/terms sont-elles claires ?* » entre
Legal (Aquaman) et Product (Flash). Tours 1 à 5 ont classé la
privacy comme un **risque parmi 4** ([[aquaman-classification-risques-4-formes]])
— privacy/data, claim safety, IP/propriété, contract/périmètre.
Chaque risque est géré par un *audit ex post* : le code est
*déjà écrit* quand Aquaman le voit, et la privacy est soit
*préservée par chance*, soit *corrigée en rattrapage*.

La doctrine Privacy by Design (RGPD Article 25 + CCPA §1798.100)
inverse ce dogme : la protection des données personnelles doit
être **intégrée dès la conception**, comme un *gate* sur le
pair-check #8, pas comme un *audit* après merge. C'est l'objet
de ce concept.

## Définition opérationnelle

Le **Privacy Gate** est une vérification Aquaman obligatoire,
déclenchée à la première PR Flash (Product) qui touche des
données personnelles. Le gate produit un Privacy Review (forme
privée du catalogue JTBD, cf. [[aquaman-jtbd-emit-receive]])
qui :

1. **Identifie les catégories de données personnelles** traitées
   (Article 4 RGPD : toute information relative à personne
   physique identifiée ou identifiable).
2. **Documente la base légale** du traitement (Article 6 RGPD —
   consentement, contrat, obligation légale, intérêt vital,
   mission publique, intérêt légitime).
3. **Choisit les contrôles proportionnés** (Article 25(1) RGPD —
   *data minimization*, *purpose limitation*, *storage
   limitation*, *accuracy*, *confidentiality*, *accountability*).
4. **Évalue les risques** (Article 35 — DPIA si haut risque,
   par exemple profilage à grande échelle, données sensibles,
   surveillance systématique).
5. **Prépare l'exercice des droits** (Articles 15-22 RGPD —
   accès, rectification, effacement, portabilité, opposition).

Le résultat est un **Privacy Review signé Aquaman** qui doit
accompagner la PR avant merge. Sans ce Privacy Review, Flash ne
peut pas merger vers le main.

## Les 5 contrôles obligatoires avant merge

| # | Contrôle | Standard | Output |
|---|---|---|---|
| 1 | **Privacy by Design checklist complétée** | RGPD Article 25 + EDPB Guidelines 4/2019 | Formulaire signé Flash + Aquaman |
| 2 | **DPIA si traitement à haut risque** | RGPD Article 35 + CNIL doctrine | Document complet ou décision motivée de non-DPIA |
| 3 | **Privacy notice UI** | RGPD Article 13-14 | Capture UI ou texte final visible utilisateur |
| 4 | **Registre des traitements mis à jour** | RGPD Article 30 | Entrée dans `aquaman-registre-traitements-v{N}.csv` |
| 5 | **Chiffrement at rest + in transit** | RGPD Article 32 + EDPB | Preuve technique Cyborg |

## Les 3 cas de suspension Privacy Gate

Le Privacy Gate suspend la PR dans les cas suivants :

1. **Données sensibles (Article 9)** — santé, biométrie, opinion
   politique, sexualité, etc. La suspension exige un Privacy
   Review élargi (DPIA complet, durée minimale 30 jours, cosig
   DPO si nommé, ou escalade B1 si conflit d'architecture).
2. **Profilage à grande échelle** — Article 35(3)(a) RGPD. La
   suspension exige un DPIA complet même si pas de données
   sensibles.
3. **Transfert hors UE/EEE** — Article 44 RGPD, *Schrems II*
   C-311/18, 16 juillet 2020. La suspension exige un *Standard
   Contractual Clauses* signé + *Transfer Impact Assessment*
   (TIA) Cyborg.

## Les 3 cas abusifs (privacy-washing)

Le Privacy Gate peut être utilisé abusivement dans les cas
suivants :

1. **Privacy-washing par formulaire vide**. Flash qui coche toutes
   les cases du Privacy Review sans analyse effective. Détection :
   Aquaman tient un *Privacy Review register* ; les formulaires
   identiques sur 5+ PR consécutives sont signalés.
2. **Privacy-washing par délai**. Aquaman qui signe un Privacy
   Review en < 1 heure pour des cas complexes (par exemple
   données sensibles). Le seuil est posé dans le Privacy Gate
   : < 5 jours ouvrés pour les cas standards ; < 30 jours pour
   les cas Article 9.
3. **Privacy-washing par DPO externe**. Un DPO externalisé qui
   signe systématiquement en 24h sans escalader. La motion de
   censure antisèche ([[aquaman-veto-antisèche-pattern-detection]])
   peut s'appliquer si le DPO signe > 5 PR / semaine sans
   renvoi à Aquaman.

## Les 4 issues de levée du Privacy Gate

Un Privacy Gate est levé par l'une des 4 issues suivantes :

1. **PRIVE_OK** — Privacy Review signé Aquaman ; Flash peut
   merger.
2. **PRIV_BLOCKED** — Privacy Review refuse la PR ; Flash doit
   amender avant re-soumission.
3. **PRIV_ESCALATE_B1** — La PR pose un conflit d'architecture
   (par exemple choix entre minimisation et observabilité) qui
   dépasse le périmètre Aquaman ; escalade B1 via packet
   mésoperpétuel (cf. [[aquaman-b1-escalade-packet-shape]]).
4. **PRIV_PARKED** — La PR est mise en attente pour Privacy
   Review H30 (échéance) ; Aquaman driver le sprint de revue.

## Liens avec les concepts existants

- **Classification 4 formes
  ([[aquaman-classification-risques-4-formes]])** : la classe 1
  (privacy/data, Cyborg upstream) est étendue d'« audit ex post »
  à « gate ex ante » sur le pair-check #8. Le *portique Batman
  T-7j* ([[aquaman-launch-ready-portique-final]]) devient Privacy
  Gate + portique launch.
- **Pair-check #8 ([[aquaman-gates-et-pair-checks]])** : le
  pair-check #8 avait Aquaman = Consulted (RACI par rang, A =
  Flash). Le Privacy Gate *étend* l'intervention Aquaman en gate
  obligatoire, sans modifier le RACI par rang — c'est un *gate
  intra-pair-check*, pas une promotion RACI.
- **Couplage Aquaman ↔ Cyborg ([[aquaman-couplages-invisibles]])** :
  Cyborg upstream sur privacy ; le Privacy Gate exige la preuve
  technique de chiffrement (contrôle #5), c'est la formalisation
  du couplage implicite.
- **Catalogue JTBD émis ([[aquaman-jtbd-emit-receive]])** : la
  Forme 1 du catalogue (Privacy Review) est étendue au Privacy
  Gate — la différence est la position temporelle (gate ex ante
  vs audit ex post).

## Les 3 asymétries avec la classification 4 formes

La classification pose des cas-frontière en séquence (cf.
[[aquaman-classification-risques-4-formes]] §3 cas-frontière).
Le Privacy Gate ajoute **3 asymétries** :

1. **Privacy est binaire, claim est gradient**. Une PR peut
   être *un peu* litigieuse (claim minor), mais *un peu* privacy
   *n'existe pas* : soit des données personnelles sont traitées,
   soit elles ne le sont pas. Le Privacy Gate est binaire ;
   les claims sont négociables.
2. **Privacy Gate bloque, claim ajuste**. Un Privacy Gate
   refusé bloque la PR. Un claim safety refusé ajuste la copie
   (rares cas de claim blocking complet). Conséquence : le
   Privacy Gate est *plus restrictif* qu'un claim review.
3. **Privacy Gate est public, claim est commercial**. Le
   Privacy Gate est documenté et opposable par un régulateur
   (CNIL, EDPB, FTC) ; un claim safety relève du seul régime
   commercial. Le Privacy Gate a une *traçabilité publique*
   qui n'existe pas pour le claim.

## Anti-pièges

- **Privacy by Design = checklist, pas analyse**. La doctrine
  RGPD attend une *analyse* proportionnée au risque, pas un
  *formulaire* systématique. Le Privacy Review doit adapter le
  niveau de détail à la complexité de la PR.
- **Privacy by Design = une fois**. La protection doit être
  *continue*, pas *one-shot*. Chaque PR successive doit
  reprendre l'analyse — un Privacy Review ancien n'est pas
  acquis pour une PR nouvelle, même sur le même domaine.
- **Privacy by Design = juridique, pas sécurité**. Le Privacy
  Gate traite le *régime juridique* des données personnelles,
  pas leur *sécurité technique* (qui relève Cyborg). Les deux
  sont complémentaires, mais distincts — confondre les deux fait
  reposer la conformité sur des contrôles inadaptés.
- **Privacy Gate sans DPO**. RGPD Article 37-39 impose un DPO
  pour certains traitements. Le Privacy Gate n'est pas un
  substitut — il est un *gate opérationnel*, pas une fonction
  de gouvernance. Sans DPO nommé, le Privacy Gate est
  *incomplet*.
- **Privacy Gate bloqué par habitude**. Un Aquaman qui refuse
  systématiquement les PR par *défiance*, sans analyser les
  contrôles, tombe sous le coup de la motion de censure
  antisèche ([[aquaman-veto-antisèche-pattern-detection]]).

## Liens

- [[aquaman-classification-risques-4-formes]] — la classe
  privacy/data, étendue ici en gate
- [[aquaman-gates-et-pair-checks]] — le pair-check #8, instrumenté
  ici en Privacy Gate
- [[aquaman-jtbd-emit-receive]] — Forme 1 Privacy Review, étendue
  en Privacy Gate ex ante
- [[aquaman-couplages-invisibles]] — couplage Cyborg ↔ Aquaman,
  formalisé via contrôle #5 (chiffrement)
- [[aquaman-launch-ready-portique-final]] — le portique T-7j, qui
  devient Privacy Gate + portique launch
- [[aquaman-b1-escalade-packet-shape]] — escalade B1 sur conflit
  privacy/architecture
- [[aquaman-veto-antisèche-pattern-detection]] — motion de censure
  applicable au Privacy Gate abusif

## Note de confiance

**Confirmé par doctrine juridique, reconstruit sur A'Space.** La
Privacy by Design est une doctrine juridique positive (RGPD
Article 25 ; CCPA §1798.100 ; LIL Article 22-3 ; UK GDPR
équivalent) — pas une projection. L'ancrage A'Space est cependant
indirect : aucun triplet v3, aucun Ownerbook T1, aucun des 23
concepts Aquaman existants ne pose le Privacy Gate comme *gate
obligatoire* sur le pair-check #8. Le concept est **reconstruit**
depuis les doctrines RGPD/CCPA + la classification 4 formes
Aquaman.

**Particularité A'Space** : A'Space manipule des données
personnelles à grande échelle (multi-tenants, observabilité
produit, logs utilisateur), ce qui place Aquaman en première
ligne pour les DPIA Article 35. Le Privacy Gate devient un
*acte de gouvernance* substantiel, pas un simple formulaire.

**À vérifier en cycle** :
- Le Ownerbook T1 / Ownerbook T2 pose-t-il un DPO ou un Privacy
  Lead ? Si oui, le DPO est-il Explicit Responsable Privacy Gate ?
- Cyborg a-t-il un registre des traitements (Article 30 RGPD) ?
  Si non, le concept propose implicitement
  `aquaman-registre-traitements-v{N}.csv` à matérialiser.
- Flash a-t-il un Privacy by Design checklist documenté ? Sinon,
  le concept propose un template à matérialiser.
- Les sous-traitants (Vercel, Supabase, etc.) sont-ils listés
  dans le registre Article 30 ? Sinon, une action Cyborg est
  ouverte.

**Limite** : la doctrine RGPD est dense (250+ pages de
règlement, milliers de pages de guidelines EDPB, multiples
arrêts C-311/18 *Schrems II*, C-25/21 *Planned*
Parenthood, etc.). Ce concept pose les 5 contrôles minimaux —
une implémentation complète demanderait un Privacy
Program séparé (registre Article 30, DPIA Article 35,
notifications Article 33-34, accord sous-traitant Article 28,
clauses contractuelles types Article 46, etc.).
