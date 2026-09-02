# Audit RILCOT — cohérence ontologie V3 (work 3, uc.db)

> Audit LECTURE SEULE. Aucune correction appliquée aux sources. Ruban :
> `00_Amadeus/60_Tape_Specs/2026-09-01-spec-audit-rilcot.md` (l2-spec-003).
> Date : 2026-09-01. Harness : ryan_build_l0. Prédiction antérieure : uc.db prediction_id=23.

## Methodologie

Outils réellement exécutés (chemin + code retour) :

| Commande | rc | Usage |
|---|---|---|
| `cd /c/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel && python uc.py claim --work 3 --harness ryan_build_l0 --lease 3600` | 0 | claim work 3 |
| `python uc.py predict --work 3 --claim '...' --confidence 0.7` | 0 | prédiction antérieure id=23 |
| `grep -n "JTBD-002 RILCOT Transverse" 70_Onthologies/sujets/01_Projects_Picard.ttl` | 0 | listing gates |
| `grep -n "Manifest — RILCOT" 70_Onthologies/sujets/30_Business_OS.ttl 70_Onthologies/sujets/05_From_V2_Domains.ttl` | 0 | manifests l.63 |
| `sed -n '740,770p' 70_Onthologies/triplets/aspace-os.ttl` + `grep -n "picard-audit"` | 0 | triplets LD01 |
| `python -` (script de comptage/comparaison de blocs TTL) | 0 | comptes exacts |

Méthode : comptage par correspondance exacte de chaîne sur les fichiers TTL
sources (lecture seule), extraction des blocs sujet complets des deux
Manifests (du `<sujet>` au ` .` final) et comparaison attribut par attribut.

Fichiers d'entrée (lus intégralement aux lignes citées) :
- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/sujets/01_Projects_Picard.ttl`
- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/sujets/30_Business_OS.ttl`
- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/sujets/05_From_V2_Domains.ttl`
- `C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/aspace-os.ttl`
- Référence croisée : `C:/Users/amado/ASpace_OS_V3/30_Business_OS/AGENTS.md` (l.16 : règle des 8 domaines B2 / 8 squads B3).

## Verifications

### Verification 1 — Gates transverses complets (attendu : 8)

Comptage exact `JTBD-002 RILCOT Transverse * Gate` dans `01_Projects_Picard.ttl` :
**7 gates trouvés, 8 attendus** (commande : grep exact + comptage Python).

| # | Gate | Ligne |
|---|---|---|
| 1 | JTBD-002 RILCOT Transverse Legal Risk Gate | 2500 |
| 2 | JTBD-002 RILCOT Transverse People Agent Governance Gate | 2596 |
| 3 | JTBD-002 RILCOT Transverse Finance Money Gate | 2680 |
| 4 | JTBD-002 RILCOT Transverse IT Systems Gate | 2752 |
| 5 | JTBD-002 RILCOT Transverse Ops Gate | 2824 |
| 6 | JTBD-002 RILCOT Transverse Product Offer Gate | 2884 |
| 7 | JTBD-002 RILCOT Transverse Sales Revenue Gate | 2962 |

Domaines couverts : Legal, People, Finance, IT, Ops, Product, Sales — **Growth
absent** en tant que JTBD-002 RILCOT. Le domaine Growth est couvert en amont par
`JTBD-005 RILCOT Transverse Growth Signal Gate` (l.3052) — un JTBD-005, pas un
JTBD-002 — et par les nœuds Growth `RILCOT Growth Transverse Demand Signal OS`
(l.3562), `RILCOT B2/B3 Growth Experiment Protocol` (l.3568). Référence
`30_Business_OS/AGENTS.md` l.16 : les 8 domaines attendus sont Growth / Sales /
Product / Ops / IT / Finance / People / Legal.

**Résultat : ÉCHEC du critère « exactement 8 » — 7 mesurés.** Aucun
`JTBD-002 ... Growth` n'existe pour RILCOT (vérification inverse : les seuls
`JTBD-002 * Growth` du fichier, lignes 466/1636/2884/4096, sont MARINA,
ALIKALY, le label Product RILCOT citant « Sales/Growth », et ABC).

### Verification 2 — JTBD cibles et JTBD-001 RILCOT de projet

JTBD-001 RILCOT de projet trouvés (lignes) :
- 2494 `JTBD-001 - RILCOT Claims Data IP Boundary`
- 2590 `JTBD-001 - RILCOT Owner and Agent Handoff Map`
- 2674 `JTBD-001 - RILCOT Price Margin Model`
- 2746 `JTBD-001 - RILCOT Runtime And Data Boundary`
- 2818 `JTBD-001_RILCOT_DELIVERY_SOP`
- 2878 `JTBD-001 - RILCOT MVP Demo Boundary`
- 2956 `JTBD-001 - RILCOT Diagnostic To Proposal`

Chacun précède immédiatement (2-6 lignes) le gate JTBD-002 correspondant du
même domaine — chaîne JTBD-001 → gate vérifiée pour les 7 gates mesurés.

JTBD-001..005 cibles (Nexus / Growth) trouvés (lignes 3028-3052) :
- 3028 `JTBD-001 - NEXUS VOC Packet`
- 3034 `JTBD-002 — Nexus Member-ICP Filter (signal-density rejection) — RILCOT Members Space`
- 3040 `JTBD-003 — Nexus Painkiller Message Variants (belonging / Expert Secrets) — RILCOT`
- 3046 `JTBD-004 — Nexus Non-Paid Experiment + RICE — RILCOT Members Space`
- 3052 `JTBD-005 RILCOT Transverse Growth Signal Gate`

Les 5 cibles JTBD-001..005 sont présentes. Remarque : le libellé l.3028 est
`NEXUS VOC Packet`, pas littéralement « Nexus VOC Packet » en casse mixte —
divergence de casse mineure, non bloquante, non comptée comme incohérence.

### Verification 3 — Manifests RILCOT (l.63 des deux fichiers)

Blocs sujets complets extraits et comparés :

`30_Business_OS.ttl` l.61-65 (sujet `<urn:aspace:30-business-os-10-projects-rilcot-manifest-md>`) :
```
a aspace:Document ;
rdfs:label "Manifest — RILCOT Members Space & OS" ;
aspace:seau <urn:aspace:30-business-os> ;
dct:modified "2026-07-13" ;
aspace:mots 475 .
```

`05_From_V2_Domains.ttl` l.61-65 (sujet `<urn:aspace:05-from-v2-domains-30-business-os-10-projects-rilcot-manifest-md>`) :
```
a aspace:Document ;
rdfs:label "Manifest — RILCOT Members Space & OS" ;
aspace:seau <urn:aspace:05-from-v2-domains> ;
dct:modified "2026-07-13" ;
aspace:mots 475 .
```

Attributs comparés ligne par ligne : label identique, `dct:modified`
identique (2026-07-13), `aspace:mots` identique (475). Seuls le sujet URN et
`aspace:seau` diffèrent — ce qui est structurellement attendu (le nœud
`05_From_V2_Domains` est une projection du nœud `30_Business_OS` dans un
seau différent ; l'URN encode le chemin source). **Aucune divergence de
contenu mesurée.**

### Verification 4 — Chaîne LD01 / 6 vs 9 livres

`70_Onthologies/triplets/aspace-os.ttl` :
- l.743 : commentaire `#   LD01 Book Alignment mappe 6 livres vers 8 B2 domains`
  (au-dessus du triplet l.742 `<urn:aspace:entity:ld01-book-alignment> aspace:appliesTo <urn:aspace:entity:b2-domains> .`)
- l.746 : triplet `<urn:aspace:entity:rilcot> aspace:refines <urn:aspace:entity:ld01-book-alignment> .`
- l.747 : commentaire `#   RILCOT refine le LD01 Book Alignment avec 9 livres (ajout Expert Secrets + Group Genius)`

La chaîne `rilcot → refines → ld01-book-alignment` est confirmée (l.746). Les
chiffres 6 et 9 sont des commentaires de provenance (`src:
projets/ld01-book-alignment.md`), non des triplets — le fichier TTL ne permet
pas de compter les livres lui-même : **6 et 9 confirmés comme énoncés
cohérents entre eux** (9 = 6 + Expert Secrets + Group Genius, cohérence
arithmétique interne du commentaire l.747), la valeur réelle des livres reste
A SOURCER dans `projets/ld01-book-alignment.md` (hors périmètre de ce ruban).

### Verification 5 — Triplet picard-audit

`70_Onthologies/triplets/aspace-os.ttl` l.763 :
`<urn:aspace:entity:picard-audit> aspace:appliesTo <urn:aspace:entity:rilcot> .`
avec commentaire l.764 : `#   Le Picard Project Pattern a été appliqué à l'audit RILCOT Master Interface (2026-05-20)`.
**Confirmé.**

## Incoherences

1. **[I-1] Gate Growth manquant sous la dénomination JTBD-002.**
   `01_Projects_Picard.ttl` porte 7 gates `JTBD-002 RILCOT Transverse * Gate`
   (l.2500, 2596, 2680, 2752, 2824, 2884, 2962) au lieu des 8 attendus par le
   ruban et par `30_Business_OS/AGENTS.md` l.16 (8 domaines B2). Le domaine
   Growth n'a pas de `JTBD-002 RILCOT Transverse Growth Gate` ; sa couverture
   passe par `JTBD-005 RILCOT Transverse Growth Signal Gate` (l.3052) — un
   niveau JTBD différent, sans doute délibéré (Growth est traité comme signal,
   pas comme gate d'exécution), mais le comptage du ruban attendait 8.

## Corrections proposees

### Patch pour I-1 — Gate Growth JTBD-002 RILCOT (NON appliqué, lecture seule)

Fichier : `C:/Users/amado/ASpace_OS_V3/70_Onthologies/sujets/01_Projects_Picard.ttl`

Deux options, selon l'intention réelle (le patch texte exact est proposé, pas appliqué) :

**Option A — si Growth doit être un gate JTBD-002** : insérer avant l.3052
(bloc JTBD-005), un nœud frère des 7 autres, dans le même style :

```ttl
    rdfs:label "JTBD-002 RILCOT Transverse Growth Signal Gate" ;
```

(via un nouveau sujet `<urn:aspace:entity:jtbd-002-rilcot-growth-gate>` calqué
sur le bloc Ops l.2824-2876, avec les readiness checks Growth : signal source,
ICP fit, coût d'acquisition, canal non payant, seuil de passage JTBD-005).

**Option B — si le JTBD-005 l.3052 EST le gate Growth (intention actuelle)** :
corriger le comptage attendu dans le ruban source, ou renommer l.3052 pour
expliciter la double appartenance :

Ancien extrait (l.3052) :
```ttl
    rdfs:label "JTBD-005 RILCOT Transverse Growth Signal Gate" ;
```
Nouvel extrait proposé :
```ttl
    rdfs:label "JTBD-005 RILCOT Transverse Growth Signal Gate (8e domaine transverse RILCOT — remplit le rôle JTBD-002 Growth)" ;
```

L'option B est recommandée : elle ne duplique rien (B4 — moins de systèmes) et
rend visible la couverture des 8 domaines.

## Verdict

**INCOHERENT** — 1 incohérence mesurée (I-1), 1 correction proposée (non
appliquée). Tout le reste est cohérent : manifests identiques, chaîne LD01
confirmée, triplet picard-audit confirmé, JTBD-001..005 cibles présents.
