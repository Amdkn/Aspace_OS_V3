# ADR-CK-FREE-001 — Contraintes ClickUp Free → Choix 12-Sectors + Zéro Custom Field

**Date :** 2026-05-27
**Auteur :** A0 Amadeus + A2 Claude Code
**Statut :** RATIFIÉ (documentation rétroactive d'un choix déjà appliqué)
**Type :** Architecture Decision Record (Business OS / L2 / Plateforme)
**Portée :** Toute structuration ClickUp tant que l'organisation reste sur le plan gratuit
**Ancré sur :** ADR-MESH-L2-001 §D3 (ClickUp = layer exécution) · ADR-ID-001 §D5 (préfixe `[SOP_ID]` dans titres) · Shadow_L2/11 (peuplement Solaris II/III)

---

## Contexte

ClickUp est la couche **WHEN/WHO** du mesh L2 tri-plateforme. A0 opère sur **plan Free** par choix de souveraineté économique : pas d'engagement financier récurrent tant que le mesh n'est pas auto-générateur de revenus.

Le plan Free impose des contraintes majeures :

| Ressource | Limite Free | Impact |
|-----------|-------------|--------|
| Spaces | **5 max** | Force une hiérarchie 2-niveaux Space > Folder > List |
| Custom Fields | **Quota "ClickApps uses" très limité** (60 utilisations cumulées avant lock) | Empêche workspace-wide tagging via Custom Fields |
| Stockage fichiers | **100 MB total** | Assets lourds doivent vivre ailleurs (S3, Drive, Airtable) |
| Gantt / Mind Maps / Timeline | Locked | Visualisations avancées indisponibles |
| Dépendances avancées | Locked | Garder uniquement les liens simples task↔task |
| Automations | **100 runs/mois** | Pas de wiring lourd ClickUp natif |
| Goals / Sprints | Locked | Pas de cérémonie Scrum native |
| Time tracking | **Disponible (gratuit, illimité)** | Bonus — utiliser à fond |
| Threaded comments | **Disponible** | Bonus — utiliser pour exécution opérationnelle |
| Chat | **Disponible** | Bonus — éviter Slack/Discord pour discussions tasks |
| Tags | **Illimités** | Vector de cross-référencement principal |

## Décision

### D1 — Architecture 5 Spaces forcée

Les 5 spaces sont **strictement attribués** :

| # | Space | Rôle | Justification anti-pollution |
|---|-------|------|-------------------------------|
| S1 | 🏛️ AaaS Holding (Jerry) | Direction B1, KPI cross-domaines | Jerry doit voir sans naviguer |
| S2 | ☀️ Solaris I Front-Office | Stage 1 production (acquisition, conversion, onboarding, triage) | 4 squads pré-prod |
| S3 | ☀️ Solaris II Factory | Stage 2 production (forge texte/visuel, publication, infra) | 4 squads production |
| S4 | ☀️ Solaris III Back-Office | Stage 3 (legal, finance, analytics, templates) | 4 squads gouvernance |
| S5 | 🧪 SandBox | R&D, expérimentation, anti-pollution | Test sans contaminer S2/S3/S4 |

**Règle d'or** : aucun space ne sera créé hors de ces 5. Si un besoin émerge, refactor d'un space existant.

### D2 — Adaptation 8 squads doctrinaux → 12 sectors physiques

ClickUp Free + contrainte 5-spaces force la projection des 8 squads doctrinaux sur 12 folders physiques (4 par space workflow) :

| Squad doctrinal | Sectors ClickUp | Raison du split |
|------------------|------------------|------------------|
| Guardians (Growth) | S2-1 | 1:1 |
| Illuminati (Sales) | S2-2 | 1:1 |
| XMen (People/RAG) | S2-3 | 1:1 |
| Fantastic4 (Ops) | **S2-4 + S3-7** | Ops = pré-prod (Triage Build Gate) + prod (Tisserand Publication) |
| Avengers (Product) | **S3-5 + S3-6** | Product = texte (Forge Textuelle) + visuel (Forge Visuelle) |
| KangDynasty (IT) | S3-8 | 1:1 |
| Eternals (Legal) | S4-9 | 1:1 |
| Thunderbolts (Finance) | S4-10 | 1:1 |
| *(meta Analytics)* | S4-11 | Transverse mesure 8 squads |
| *(meta Templates)* | S4-12 | Réplique opérationnelle SOPs Notion |

**Ce n'est pas un drift doctrinal mais une adaptation contrainte**. Le 12-fold ClickUp doit toujours être lu à travers la grille 8-fold Notion.

### D3 — Zéro Custom Field workspace-wide

**Décision** : NE PAS créer de Custom Fields tant qu'on est sur Free.

Raisons :
- Quota ClickApps strict — un Custom Field workspace-wide consomme à chaque task créée
- Risque de lock partiel imprévisible si quota dépassé
- Pattern `[SOP-L2-{DOMAIN}-{NN}]` **dans le titre** de la task remplace fonctionnellement le Custom Field
- Cross-référencement Notion↔ClickUp passe par **Symphony worker** (Phase 2) qui matche par regex titre

**Exception autorisée** : Custom Fields **list-level** (1-2 lists critiques uniquement) sont OK car comptés différemment du quota workspace. Ex : sur la list S4-10 "Émission Factures Stripe", un field `Invoice_Amount` (currency) est tolérable.

### D4 — Tags comme vector principal de cross-référencement

Les tags ClickUp sont **illimités** sur Free. Les utiliser pour :

| Catégorie | Pattern | Exemple |
|------------|---------|---------|
| Client | `cl:{slug}` | `cl:acme-corp` |
| Domaine | `dom:{domain}` | `dom:sales` |
| Sprint | `sp:{YYYY-WW}` | `sp:2026-22` |
| Priorité | `p0`, `p1`, `p2`, `p3` | `p0` |
| État (au-delà du natif) | `st:{state}` | `st:waiting-client`, `st:blocked-billing` |
| Brief Airtable | `br:{BRIEF_ID}` | `br:BR-CL-acme-corp-20260527-01` |

Les tags doivent **toujours être lowercase + tirets**, jamais d'espaces.

### D5 — Time tracking utilisé à fond

ClickUp Free a 8 endpoints API time tracking gratuits :
- `start_time_tracking` · `stop_time_tracking` · `get_current_time_entry`
- `add_time_entry` · `get_time_entries` · `get_task_time_entries`
- `get_task_time_in_status` · `get_bulk_tasks_time_in_status`

Doctrine : **tout task qui prend >15 min doit avoir un time entry**. Cela alimente :
- ADR-ID-001 + scoring du burn par squad
- Postmortems (S4-11 Boucles Fermées)
- Future calibration des SOPs Notion (réalité vs estimation)

### D6 — Threaded comments + Chat = canal d'exécution

Les commentaires threadés ClickUp remplacent Slack/Discord/Teams pour la **discussion opérationnelle attachée à une task**. Avantages :
- Contexte ne quitte jamais la task (anti-fragmentation)
- Mention `@squad-member` natif
- Historique permanent attaché à l'exécution

Doctrine : **toute conversation qui concerne une task spécifique vit dans le thread de cette task**. Pas dans email, pas dans Slack, pas dans WhatsApp.

### D7 — Anti-patterns ClickUp Free

- ❌ Créer un 6e Space → refactor obligatoire d'un existant
- ❌ Activer un Custom Field workspace-wide pour le "confort"
- ❌ Stocker des fichiers >5 MB dans ClickUp (uploader sur S3, coller URL)
- ❌ Câbler une Automation pour synchroniser avec Airtable (Symphony s'en charge, hors quota CK)
- ❌ Acheter une licence Business "pour les Goals" — d'abord prouver via Free
- ❌ Créer des Custom Statuses elaborate par list (rester sur les defaults : Open, In Progress, Closed)

### D8 — Critères de migration vers payant

Bascule vers **ClickUp Unlimited** (le moins cher payant) déclenchée **uniquement** si **AU MOINS 2 critères** réunis pendant 30 jours consécutifs :

1. MRR > 5 k€/mois (cf. Airtable 🛡️ Finance & Compute)
2. >50 tasks créées/semaine
3. >3 collaborateurs humains actifs (Espace Agent +1 collaborateur humain min)
4. Besoin réel de Custom Fields workspace-wide identifié 3+ fois en postmortem
5. Stockage natif >50% de la limite Free

Ré-évaluation : 2026-Q3 ou +30 j post-1er client réel.

## Conséquences

### Positives
- **Économie immédiate** : 0€/mois ClickUp pour 97 lists + time tracking + chat + tags illimités
- **Discipline forcée** : moins de features = plus de doctrine respectée
- **Portabilité** : si bascule vers Linear/Plane/Asana un jour, les conventions tag + titre se transposent
- **Time tracking gratuit** = data réelle pour calibrer SOPs Notion

### Négatives
- **Pas de Gantt** : planification longue durée se fait dans Airtable ou un autre outil
- **Pas de Goals** : OKRs vivent ailleurs (Notion ou doc dédié)
- **Quota Automations 100/mois** : suffit largement tant que Symphony fait le gros
- **Visualisation moins riche** : compensée par dashboards Notion + Airtable

### Risques tracés
- **Quota ClickApps imprévisible** : Anthropic ne documente pas le décompte. Mitigation : éviter tout Custom Field jusqu'à upgrade.
- **Migration de tags si bascule plateforme** : Symphony peut scripter une réécriture si besoin

## Plan d'implémentation

### Phase 1 — Audit existant (immédiat)
- [x] 56 lists Solaris II/III créées (Shadow_L2/11)
- [ ] Vérifier qu'aucun Custom Field n'a été activé par accident
- [ ] Documenter convention tags D4 dans cheatsheet `Ryan_SysAdmin/CHEATSHEETS/clickup-free-conventions.md`

### Phase 2 — Premiers usages réels
- [ ] Première task créée respectant convention titre `[SOP-L2-XXX-NN] {CLIENT_ID} — action` (cf. ADR-ID-001)
- [ ] Premier time tracking enclenché
- [ ] Premier tag `cl:{slug}` appliqué

### Phase 3 — Surveillance quota
- [ ] Hebdo : vérifier dashboard usage ClickUp Free (UI Settings > Plan & Usage)
- [ ] Si quota Automations >70%, désactiver les moins critiques
- [ ] Si stockage >50 MB, audit des assets

## Références

- ADR-MESH-L2-001 — Doctrine tri-plateforme L2
- ADR-ID-001 — Conventions identifiants universels
- ADR-NOTION-001 — Back-office Solaris template
- Shadow_L2/11 — ClickUp Solaris II/III peuplement
- ClickUp Free plan : https://clickup.com/pricing (référence externe)
