---
type: OKF-0.2
date: 2026-09-01
titre: Arbitrage final des 3 Docteurs — renommages profils + cahier des charges Workspace
mandat: Reprise session 20260901_075739_62fa0f (interrompue à 60/60 itérations)
statut: ARBITRÉ
---

# ARBITRAGE DOCTEURS — 2026-09-01

## 1. Propositions (mesuré — sessions Hermes réelles)

- **L0 (doctor13_review_l0**, session 20260901_090731_761d0d) : renommage cosmétique "Prénom - Rôle Lx", slug inchangé ; Workspace = point d'accès unique sur uc.db, cycle von Neumann affiché, claims/leases horodatés (vivants/expirés/doubles), panneau DLQ → Donna, toute valeur non sourcée affichée A SOURCER.
- **L1 (doctor11_review_l1**, session 20260901_090613_bec61f — répondu après 2 silences, sans correction config nécessaire) : renommage OUI si slug inchangeant (rename de dossier = interdit, casse sessions/skills) ; Workspace L1 = bandeau HALT rouge Beth, champ confiance machine|humain non-mutable depuis l'app, portes irréversibles absentes ou double-confirm humain, métriques lues depuis uc.db jamais inventées.
- **L2 (doctor12_review_l2**, session 20260901_090819_f4904c, complétait proposition partielle 20260901_080411_bda452) : UN seul mapping slug→nom relu par le code ; Workspace = embed gateway 127.0.0.1:8642 multi-tenant (F1 persistance par tenant, F2 reprise instantanée, F3 identité dynamique, F4 observabilité tokens/coût par tenant, F5 cycle de vie gateway health/restart) + onglets Projets/Squads/Métriques business.

## 2. Arbitrage — table des renommages confirmée

Consensus unanime 3/3 : **libellé seul change, slug de dossier inchangé** (clé stable du runtime). Un mapping JSON unique (`Prenom - Role Lx`), relu par le code.

| Slug (inchangé) | Libellé affiché | Niveau |
|---|---|---|
| yaz_spec_l0 | Yaz - Spec L0 | φ Ruban L0 |
| ryan_build_l0 | Ryan - Build L0 | A Constructeur L0 |
| graham_spawn_l0 | Graham - Spawn L0 | B Copieur L0 |
| doctor13_review_l0 | 13e Docteur - Review L0 | C Contrôleur L0 |
| amy_spec_l1 | Amy - Spec L1 | φ Ruban L1 |
| rory_build_l1 | Rory - Build L1 | A Constructeur L1 |
| river_spawn_l1 | River - Spawn L1 | B Copieur L1 |
| doctor11_review_l1 | 11e Docteur - Review L1 | C Contrôleur L1 |
| clara_spec_l2 | Clara - Spec L2 | φ Ruban L2 |
| nardole_build_l2 | Nardole - Build L2 | A Constructeur L2 |
| bill_spawn_l2 | Bill - Spawn L2 | B Copieur L2 |
| doctor12_review_l2 | 12e Docteur - Review L2 | C Contrôleur L2 |
| rick_governance_l0 | Rick - Gouvernance L0 | Gouvernance |
| kernel_builder_a | Kernel - Build A | Kernel |
| kernel_copier_b | Kernel - Spawn B | Kernel |
| kernel_controller_c | Kernel - Review C | Kernel |
| donna_dlq | Donna - DLQ | DLQ |

Les noms humains des 3 kernel_* (Build A / Spawn B / Review C) restent génériques : A SOURCER un mapping nommé canonique pour ces 4 profils si Amadou en veut un.

## 3. Cahier des charges Workspace final (fusion L0+L1+L2)

- **Architecture** : embed du gateway local 127.0.0.1:8642, tenant = profil Hermes, aucun backend distant, aucune source parallèle (l'app est une vue, D3).
- **Vue L0 (mécanisme)** : cycle Fetch→Decode→Execute→Writeback depuis uc.db ; claims/leases (vivants, expirés→récupérables, doubles bloqués) ; panneau DLQ avec motif + re-jouabilité.
- **Vue L1 (conscience)** : bandeau HALT rouge Beth (travail détaché masqué si HALT) ; champ confiance machine|humain visible, passage à humain impossible depuis l'app ; portes irréversibles absentes ou double-confirm.
- **Vue L2 (business)** : onglets Projets / Squads (13 compagnons, rôles Lx visibles) / Métriques (coût/token par tenant, cadences, taux de rejeu P1).
- **Multi-tenant** : F1 persistance isolée, F2 reprise instantanée, F3 identité dynamique (titre + accent par profil, applique le mapping §2), F4 observabilité par tenant, F5 cycle de vie gateway (health, restart, dégradé).
- **Règle transversale** : toute valeur affichée provient d'une lecture uc.db/disque/gateway, sinon A SOURCER. Interdit : cumul Build+Review.

## 4. MESURE / SUPPOSÉ

- MESURÉ : les 3 sessions de propositions (ids ci-dessus), profils présents via `hermes profile list` (17, tous GLM-5.3-flash).
- SUPPOSÉ / A SOURCER : schéma exact des tables uc.db (à lire avant implémentation des vues) ; mapping nommé pour kernel_* ; coût/token par tenant (source gateway à confirmer).
