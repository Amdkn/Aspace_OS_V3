---
session: agent-aa6408c9dcf7acc1f
projet: wf_bdced047-a27
debut: 2026-08-09T06:41:11.557Z
fin: 2026-08-09T06:43:56.763Z
messages_utilisateur: 1
reponses_assistant: 0
---

## >>> UTILISATEUR #1

Audit tous les apps de Coach OS. Le dépôt est à C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os.

LIVRABLE OBLIGATOIRE : écris C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os/AUDIT_FINAL.md.

ÉTAPE 1 — Lire l'architecture existante :
  - src/lib/cms/cms.store.ts (CRUD déjà en place : registerCollection, addItem, updateItem, removeItem)
  - src/lib/cms/types.ts (CmsCollectionDef, CmsItem, CmsField)
  - src/components/cms/* (CollectionRepeater, DynamicPageView, AppDetailOverlay, itemDetailRegistry)
  - src/stores/* (Zustand stores)
  - src/lib/app-registry.ts, src/lib/app-discovery.ts

ÉTAPE 2 — Auditer chaque app sous src/apps/ (19 apps : audit, clients, cognition, dashboard, design, finance, growth, it-rd, legal, marketplace, onboarding, ontology, operations, people, product, sales, settings, tasks, welcome + _ui partagé).

Pour chaque app, classe dans une catégorie :
  - "STUB" : juste App.tsx, pas de CMS, pas de mutations, données en dur → DoD 0/9
  - "PARTIAL" : a un App + DetailPage mais TODOs non branchés, mutations partielles → DoD 3-6/9
  - "NEAR-DONE" : structure complète, 1-2 trous → DoD 6-8/9
  - "DONE" : passe les 9 critères → DoD 9/9

Pour chaque app, donne :
  - fichiers lus
  - TODOs et hardcoded arrays trouvés (avec chemin:ligne)
  - boutons morts identifiés
  - DoD score actuel
  - tâches précises pour passer à 9/9 (liste de courses)

ÉTAPE 3 — Définir le CONTRAT DE STORE MULTI-TENANT.

Le store actuel (cms.store.ts) est mono-tenant. Le contrat doit :
  - ajouter un champ tenant_id partout (CmsItem, CmsCollectionDef)
  - exposer un useTenant() hook qui retourne le tenant actif depuis un store global tenant.store.ts
  - filtrer TOUTES les lectures/écritures par tenant_id (row-level côté front)
  - avoir une méthode seedFor(tenantId) qui hydrate un tenant neuf avec ses données par défaut
  - ne PAS modifier le comportement actuel tant qu'il n'y a qu'un tenant (rétro-compat)

Écris le contrat dans AUDIT_FINAL.md sous forme de signatures TypeScript :
  interface TenantContext { ... }
  interface CmsItem { id; tenant_id; ... }
  interface CmsState { collections; items (par tenant); ...; seedFor(tenantId): Promise<void>; }
  function useTenant(): TenantContext

ÉTAPE 4 — Donner la table de vérité finale :
  | App | Catégorie actuelle | Tâches pour 9/9 | Périmètre de fichiers exclusif |

Garde le rapport FACTUEL. Pas de promesses. Si tu ne peux pas lire un fichier, dis-le. Si tu n'arrives pas à lancer shot.mjs, dis-le.

Tu ne modifies AUCUN fichier de app (audit seulement). Tu peux créer AUDIT_FINAL.md et un nouveau fichier src/lib/tenant/contract.ts (signature uniquement, sans implémentation — c'est l'étape Phase 3).
