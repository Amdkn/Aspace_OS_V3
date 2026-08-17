---
type: Project
title: Marina Cleaning BOS & SOP
description: Business OS et système SOP pour Marina Super Cleaners (opérations de nettoyage de marinas), mode Orbiter primary, status GRADUATED depuis 2026-05-21.
tags: [projet, summer-verse, gradue, field-services, sop, marina, ld01]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraire_substrat_rdf, at: 2026-08-17T19:50:00Z }
  - { by: process:lecture_concepts_picard, at: 2026-08-17T21:00:00Z }
sources:
  - id: manifest-canon
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/05 marina Cleaning BOS & SOP/SUMMERS_VERSE_MANIFEST.md"
    title: Manifest (status GRADUATED, 2026-05-21)
    last_modified: 2026-05-21
  - id: handover-canon
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/05 marina Cleaning BOS & SOP/CERRIROS_HANDOVER.md"
    title: Handover Cerritos (status GRADUATED, 2026-05-21)
    last_modified: 2026-05-21
  - id: b2-matrix
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/05 marina Cleaning BOS & SOP/B2_Business_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md"
    title: B2 Business Wheel Harmonization Matrix (status SHADOW_ACTIVE, 2026-06-02)
    last_modified: 2026-06-02
okf_version: "0.2"
---

# Marina Cleaning BOS & SOP

## Synthèse

**Business OS et système SOP pour Marina Super Cleaners** — opérations
terrain de nettoyage de marinas (mode Orbiter primary, exécution / logistique).
Status **GRADUATED** depuis 2026-05-21. Différence vs les autres projets
du seau : ici, l'unité de succès est l'**SOP documentée et exécutée par
un crew sans owner**, pas le client signé. Le projet vise une franchise
SOP-as-a-service.

## Trois questions — ce qu'il visait, ce qui a été livré, ce qui ne l'a pas été

**Ce qu'il visait.** Établir un BOS opérationnel avec 3 SOPs core (safety,
quality inspection, client walkthrough) en Year 1, 2 contrats marina
embarqués, métriques baseline (on-time >90%). Vision 3 ans (2029) : 6+
clients marina, franchise-ready, $100K ARR depuis SOP-as-a-service. Vision
10 ans (2036) : marina BOS comme standard industry, $500K ARR.

**Ce qui a été livré.** L'armature Summer's Verse, avec un **plan 12WY
différent des autres projets** : W1 (21 jours) au lieu de 84 jours — la
livraison SOP est rapide par nature, pas une campagne annuelle. Quatre
SOPs documentées : safety, quality inspection, client walkthrough,
scheduling. Le manifeste introduit des **lag metrics spécifiques operations
terrain** (weather dependency tracker, NPS per job, on-time rate) qui
n'existent pas dans les autres projets — signal que le mode Orbiter
demande ses propres indicateurs.

**Ce qui ne l'a pas été.** Comme les autres Summer's Verse, **aucun
artefact Lead/Lag ou Artifact_Proof** n'a été déposé dans le corpus. La
différence est dans la nature du livrable : les SOPs sont des **fichiers
de procédure** marqués 2026-05-21, et le code n'expose pas de trace
d'exécution au-delà de la documentation. Le status GRADUATED est donc
ici plus légitime que pour les projets B2B : il marque "les SOPs sont
rédigés", pas "les SOPs sont exécutés".

## Signaux faible mais distinct

Marina est le seul projet où le `Lead_Lag_Logs/` est thématiquement
approprié (logs weather-buffered, lags per job) — et il est absent. Le
projet est **architecturalement complet, opérationnellement non documenté**.

## Liens

- [[cerritos-gtd-pipeline]] — la chaîne de routage
- [[b2-business-wheel-harmonization-matrix]] — la matrice 8-domaines
- [[summers-verse-framework]] — la structure canonique
- [[twelve-weeks-year-cycle]] — la cadence 12WY (W1=21j ici)

## Note de confiance

**Confirmé par machine.** Le HUD GRADUATED vient du frontmatter. L'absence
d'artefacts Lead/Lag est lue dans l'inventaire substrat. La cohérence
plan/sources est vérifiée : W1=21 jours est annoncé dans le manifeste
ligne 62.

*Standing : GRADUATED en documentation SOP, exécution terrain non documentée.*
