# ADR-MESH-L2-001 — Doctrine Tri-Plateforme L2 (Notion / ClickUp / Airtable)

**Date :** 2026-05-27
**Auteur :** A0 Amadeus + A2 Claude Code
**Statut :** RATIFIÉ
**Type :** Architecture Decision Record (Business OS / L2 / Mesh)
**Portée :** Toute donnée, tâche ou doctrine vivant dans la couche L2 Business Pulse
**Ancré sur :** ADR-NOTION-001 (back-office Solaris template) · cartographie Shadow_L2/10 + 11 · audit Airtable AaaS Solaris Marketing
**Amende :** rien (premier ADR du namespace MESH)

---

## Contexte

L'audit du 27 mai 2026 a établi que A0 opère **3 plateformes SaaS distinctes** pour la couche L2, chacune avec un rôle naturel et des contraintes propres :

- **Notion** : la doctrine — workspace `Business Pulse ∞ AMADEUS`, 38 SOPs MASTER_SOP_DB, 8 squads AGENT_REGISTRY_DB, 8 portails. Auth via Internal Integration Bearer post-bascule du 27 mai (cf. handoff Notion). Free tier.
- **ClickUp** : l'exécution opérationnelle — workspace `90141225938`, 5 spaces (contrainte Free), 12 folders productifs, 97 lists. Restriction Custom Fields → pattern de nommage `[SOP-L2-...]` dans titre.
- **Airtable** : les données quantitatives — base `AaaS Solaris Marketing` (`appmWf5Xm7w9Ae0ky`), 9 tables relationnelles hub-and-spoke autour de 🌞 Clients & Workspaces. Modèle 1:1 avec les 8 squads doctrinaux.

Sans doctrine de séparation, le risque est triple : duplication de données entre plateformes (drift de vérité), confusion des responsabilités (où vit quoi ?), explosion des coûts si plusieurs plans payants.

## Décision

### D1 — Séparation des couches sémantiques

| Plateforme | Rôle sémantique | Question répondue | Granularité |
|------------|------------------|----------------------|-------------|
| **Notion** | **WHAT** (Doctrine) | "Comment doit-on faire ?" | 8 domaines plats |
| **ClickUp** | **WHEN/WHO** (Exécution) | "Quelle étape, qui agit, quelles deps ?" | 8 domaines × 3 stages = 12 sectors |
| **Airtable** | **HOW MUCH** (Données) | "État réel — qui, combien, statut ?" | 8 tables = 8 squads + 1 hub |

**Règle d'or** : une information **n'a qu'un seul propriétaire**. Si dupliquée, c'est un pointeur (URL/ID), pas une copie.

### D2 — Notion = source de vérité doctrinale

- Toute SOP, KPI, anti-pattern, identité agent vit **uniquement dans Notion**.
- ClickUp peut contenir des **templates de tasks** (S4-12 Masters & Modèles) mais ne stocke jamais le texte canonique de la SOP — uniquement un pointeur (URL Notion).
- Airtable ne contient pas de SOPs. Les briefs (🦇 table) référencent une SOP par son `SOP_ID`.

### D3 — ClickUp = layer exécution opérationnelle

- Chaque task ClickUp **doit** comporter dans son titre le préfixe `[SOP-L2-{DOMAIN}-{NN}]` qui pointe vers la SOP Notion qui la régit.
- Convention titre canonique : `[SOP_ID] {CLIENT_ID} — {action courte}`.
  - Exemple : `[SOP-L2-SALES-001] CL-acme-corp — Qualifier lead inbound`
- Les **dépendances entre tasks** restent dans ClickUp (gratuit).
- Le **time tracking** vit dans ClickUp (gratuit, 8 endpoints API).
- Les **threads de discussion** opérationnelle vivent dans ClickUp Chat (gratuit).

### D4 — Airtable = layer données quantitatives

- Table 🌞 Clients & Workspaces = **spine relationnelle**. Tous les autres records (briefs, leads, assets, contrats…) lient vers un `CLIENT_ID` 🌞.
- Pipeline `airtable-enrich` (skill maison) consomme 🦸 Leads & Audits, jamais ClickUp.
- Les **formules anti-panique** (`Filtre Invisible Woman`, `Marge Nette`, `Alerte Dépassement`) restent dans Airtable — c'est où elles sont déjà optimales.

### D5 — Flux unidirectionnels (anti-spaghetti)

```
Doctrine évolue            : Notion (humain) → Symphony worker → ClickUp Templates (S4-12)
Lead enrichi               : Airtable 🦸 (skill enrich) → ClickUp S2-1 task
Brief approuvé             : Airtable 🦇 (Build_Gate OK) → ClickUp S2-4 + S3 chain
Asset livré                : ClickUp task Done → Airtable ⚡ statut "Livré"
Paywall hit                : Airtable 🛡️ checkbox → ClickUp S1 Holding alert (manuel sinon, worker à terme)
Postmortem deal            : ClickUp S4-11 task → Notion lessons learned (manuel)
```

Aucun flux bidirectionnel simultané. Si bidirectionnel nécessaire, médiation **obligatoire** par Symphony bus (ADR-SYMPH-001).

### D6 — Anti-patterns proscrits

1. **Copier le texte d'une SOP Notion dans ClickUp ou Airtable**. Seul un lien/ID est autorisé.
2. **Stocker des leads dans ClickUp** ou des tasks dans Airtable. Mauvaise plateforme = drift garanti.
3. **Recréer le Build Gate ailleurs qu'Airtable 🦇**. La formule `Filtre Invisible Woman` est canonique.
4. **Activer un Custom Field ClickUp en plan Free**. Cf. ADR-CK-FREE-001 (à créer).
5. **Dupliquer le scoring de marge dans ClickUp**. Reste en Airtable 🛡️, exporté en alerte si dépassement.

### D7 — Identifiants universels (relai vers ADR-ID-001)

Tous les croisements de données utilisent les identifiants définis dans `ADR-ID-001` :
- `SOP_ID` · `SQUAD_ID` · `CLIENT_ID` · `BRIEF_ID` · `ASSET_ID`

## Conséquences

### Positives
- **Clarté absolue** sur où chercher quoi : 3 plateformes, 3 rôles, zéro ambiguïté.
- **Robustesse à l'audit** : aucune donnée orpheline, chaque record a un propriétaire identifié.
- **Économie plan Free** : ClickUp Custom Fields évités, Notion Internal Integration gratuit, Airtable Free 1000 records/base suffisant tant que <1000 leads/base.
- **Compatibilité Symphony** : workers à venir n'ont qu'à respecter les 5 flux D5 unidirectionnels.

### Négatives
- **Coût cognitif initial** : A0 doit assimiler "où vit quoi" pendant ~2 semaines.
- **Pas de vue unifiée native** : impossible de voir Notion+ClickUp+Airtable dans un seul écran sans dashboard custom (différé Phase 3).
- **Risque de glissement** : tentation de "vite mettre dans X" parce que c'est ouvert. Antidote : checklist mentale "WHAT/WHEN/HOWMUCH" avant chaque ajout.

### Risques tracés
- **Notion auth Bearer rotation** : si token `ntn_...` revoke, Symphony Phase 2 cassé. Mitigation : rotation documentée, fallback sur new token via Test Key Pragma.
- **ClickUp Free quotas** : 100 MB stockage. Mitigation : assets restent en URL externe.
- **Airtable Free 1000 records** : surveiller table 🦸 Leads & Audits. Auto-archive >6 mois (formule à coder).

## Plan d'implémentation

### Phase 1 — Conventions seules (immédiat, ~2h)
- [x] Cartographie cross-plateforme (Shadow_L2/10 + 11)
- [ ] Ajouter dans Notion MASTER_SOP_DB une propriété `ClickUp_Template_URL`
- [ ] Ajouter dans Airtable 🌞 un champ `ClickUp_Client_Tag` (slug unique = CLIENT_ID)
- [ ] Documenter ADR-ID-001 (en cours, ce sprint)

### Phase 2 — Symphony workers (bloqué sur cluster A2 AntiPanicGuards.psm1)
- [ ] Worker `notion-to-clickup-templates.js` (PM2 VPS)
- [ ] Worker `airtable-to-clickup-tasks.js` (PM2 VPS)
- [ ] Worker `clickup-to-airtable-feedback.js` (PM2 VPS)

### Phase 3 — Dashboard unifié (différé)
- [ ] Vue Streamlit/Next.js qui agrège les 3 sources via leurs APIs

## Références

- ADR-NOTION-001 — back-office Solaris template (canon Business OS)
- ADR-SYMPH-001 — Symphony bus orchestration
- ADR-INFRA-001 — Tmux/PM2 process managers
- Shadow_L2/10 — Notion bootstrap complete + ID reference
- Shadow_L2/11 — ClickUp Solaris II/III populated
- ADR-ID-001 — Conventions identifiants universels (créé en parallèle)
- ADR-CK-FREE-001 — Contraintes ClickUp Free (à créer)
