# ADR-ID-001 — Conventions Identifiants Universels Tri-Plateforme

**Date :** 2026-05-27
**Auteur :** A0 Amadeus + A2 Claude Code
**Statut :** RATIFIÉ
**Type :** Architecture Decision Record (Business OS / L2 / Identité)
**Portée :** Tout identifiant qui traverse au moins 2 plateformes parmi Notion / ClickUp / Airtable
**Ancré sur :** ADR-MESH-L2-001 §D7 · ADR-NOTION-001 · cartographie Shadow_L2/10–11

---

## Contexte

ADR-MESH-L2-001 a établi que les flux entre Notion, ClickUp et Airtable sont unidirectionnels et que chaque donnée a un propriétaire unique. Pour que les croisements fonctionnent, il faut des **identifiants stables, prévisibles et traçables** qui survivent aux migrations, refactorings et changements de plateforme.

Sans convention :
- Risque de collision (deux records avec même name)
- Impossibilité de matcher des records sans full-text search lourd
- Pas de continuité si on bascule vers une autre plateforme

## Décision

### D1 — Inventaire des identifiants canoniques

| ID | Pattern | Source de vérité | Exemple |
|----|---------|------------------|---------|
| `SOP_ID` | `SOP-L2-{DOMAIN}-{NN}` | Notion MASTER_SOP_DB | `SOP-L2-SALES-001` |
| `SQUAD_ID` | `SQUAD-{NAME}` | Notion AGENT_REGISTRY_DB | `SQUAD-Illuminati` |
| `CLIENT_ID` | `CL-{slug-agence}` | Airtable 🌞 Clients & Workspaces | `CL-acme-corp` |
| `BRIEF_ID` | `BR-{CLIENT_ID}-{YYYYMMDD}-{NN}` | Airtable 🦇 Briefs (formule) | `BR-CL-acme-corp-20260527-01` |
| `ASSET_ID` | `AS-{BRIEF_ID}-{NN}` | Airtable ⚡ Assets | `AS-BR-CL-acme-corp-20260527-01-03` |
| `LEAD_ID` | `LD-{slug-agence}-{YYYYMM}` | Airtable 🦸 Leads | `LD-acme-corp-202605` |
| `DEAL_ID` | `DL-{CLIENT_ID}-{NN}` | Airtable 💸 Sales Pipeline | `DL-CL-acme-corp-01` |
| `INVOICE_ID` | `INV-{CLIENT_ID}-{YYYYMM}` | Airtable 🛡️ Finance & Compute | `INV-CL-acme-corp-202605` |
| `KB_ID` | `KB-{CLIENT_ID}-{NN}` | Airtable 🏮 Knowledge & Brand Books | `KB-CL-acme-corp-01` |
| `INFRA_ID` | `IN-{CLIENT_ID}-{TYPE}` | Airtable 🤖 Infra & Media Logs | `IN-CL-acme-corp-s3bucket` |
| `LEGAL_ID` | `LG-{CLIENT_ID}-{TYPE}-{NN}` | Airtable 🔱 Compliance & Contrats | `LG-CL-acme-corp-DPA-01` |
| `TASK_ID` | natif ClickUp `9014...` | ClickUp tasks (URL) | `9014167...` (non-doctrinal) |

### D2 — Règles de slug pour `CLIENT_ID`

- ASCII uniquement, lowercase
- Mots séparés par tirets (`-`), pas d'underscores
- Max 24 caractères (économise l'écran ClickUp)
- Tronquer noms longs : "Acme Marketing Solutions Inc." → `acme-marketing` (drop "Solutions Inc.")
- Pas de chiffres en début (lecture humaine)
- Unicité vérifiée à la création (Airtable formule + alerte)

### D3 — Domaines canoniques pour `SOP_ID`

Les 8 domaines doctrinaux (cf. ADR-NOTION-001) :

| Domaine | Code court | Squad |
|---------|------------|-------|
| GROWTH | `GROWTH` | Guardians |
| SALES | `SALES` | Illuminati |
| PRODUCT | `PRODUCT` | Avengers |
| OPS | `OPS` | Fantastic4 |
| IT | `IT` | KangDynasty |
| FINANCE | `FINANCE` | Thunderbolts |
| PEOPLE | `PEOPLE` | XMen |
| LEGAL | `LEGAL` | Eternals |

Pas de domaine custom sans création préalable d'un ADR-NOTION-00X.

### D4 — Numérotation `NN`

- Toujours sur 2 chiffres minimum (`01`, `02`, … `99`)
- Si dépassement >99 dans un sous-ensemble, refactor du namespace (signal de stress doctrinal)
- Pas de réutilisation après archivage (une SOP archivée garde son numéro à vie)

### D5 — Préfixe `[SOP_ID]` dans les titres ClickUp

Format canonique titre ClickUp :

```
[SOP-L2-{DOMAIN}-{NN}] {CLIENT_ID} — {action courte impérative}
```

Exemples :
- `[SOP-L2-SALES-001] CL-acme-corp — Qualifier lead inbound`
- `[SOP-L2-FINANCE-001] CL-acme-corp — Émettre invoice Stripe février`
- `[SOP-L2-IT-002] CL-acme-corp — Déployer instance Solaris via Dokploy`

Validation : regex `^\[SOP-L2-(GROWTH|SALES|PRODUCT|OPS|IT|FINANCE|PEOPLE|LEGAL)-\d{2,}\] CL-[a-z0-9-]{1,24} — .+$`

### D6 — Génération automatique (Airtable formules)

Pour les IDs générés par Airtable, utiliser les formules :

```
BRIEF_ID    : "BR-" & {CLIENT_ID} & "-" & DATETIME_FORMAT(CREATED_TIME(), 'YYYYMMDD') & "-" & RIGHT("00" & {Brief Number}, 2)
ASSET_ID    : "AS-" & {BRIEF_ID} & "-" & RIGHT("00" & {Asset Number}, 2)
LEAD_ID     : "LD-" & {Agency Slug} & "-" & DATETIME_FORMAT(CREATED_TIME(), 'YYYYMM')
INVOICE_ID  : "INV-" & {CLIENT_ID} & "-" & DATETIME_FORMAT(CREATED_TIME(), 'YYYYMM')
```

Pour Notion (`SOP_ID`), formule SQL-style :
```
"SOP-L2-" + prop("Domain") + "-" + format(prop("Number"))
```

### D7 — Immutabilité

Une fois assigné, un ID **ne change jamais**. Renommer un client → garder l'ancien `CLIENT_ID`, ajouter un champ `Display_Name`.

### D8 — Anti-patterns

- ❌ Slugs avec espaces, majuscules, ou caractères spéciaux
- ❌ Réutilisation d'un numéro archivé
- ❌ IDs basés sur des hash (illisibles, impossibles à débugger)
- ❌ Préfixes redondants (`CL-CL-...`)
- ❌ Mixage langues dans les codes (toujours anglais : `LEGAL` pas `JURIDIQUE`)

## Conséquences

### Positives
- **Lookup cross-plateforme trivial** : grep `SOP-L2-SALES-001` retourne toutes les occurrences dans Notion + ClickUp + Airtable
- **Lecture humaine** : un ID est compréhensible sans contexte (`BR-CL-acme-corp-20260527-01` = brief client acme du 27 mai n°1)
- **Migration safe** : si un jour bascule vers Linear/Monday/etc., les IDs persistent
- **Audit trail** : traçabilité totale d'un brief depuis lead jusqu'à invoice

### Négatives
- **Verbosité** : `BR-CL-acme-marketing-solutions-20260527-01` = 36 caractères
  - Mitigation : règle slug max 24c sur la partie client
- **Apprentissage initial** : A0 doit retenir les patterns
  - Mitigation : cheatsheet dans Ryan_SysAdmin

### Risques tracés
- **Collision slug client** : deux "acme" dans deux secteurs différents. Mitigation : suffixe secteur si besoin (`acme-saas` vs `acme-corp`)
- **Drift de convention** : un humain crée à la main un ID non-conforme. Mitigation : validations regex Airtable + checks Symphony worker

## Plan d'implémentation

### Phase 1 — Documentation (immédiat)
- [x] Ce ADR
- [ ] Cheatsheet 1-page dans `Ryan_SysAdmin/CHEATSHEETS/identifiants-universels.md`

### Phase 2 — Application rétroactive
- [ ] Ajouter formule `BRIEF_ID` dans Airtable 🦇 (existe déjà cf. audit, vérifier conformité)
- [ ] Ajouter formule `LEAD_ID`, `ASSET_ID`, `INVOICE_ID` dans tables correspondantes Airtable
- [ ] Ajouter formule `SOP_ID` dans Notion MASTER_SOP_DB
- [ ] Renommer les tasks ClickUp existantes au format canonique (S4-12 Templates en priorité)

### Phase 3 — Enforcement Symphony
- [ ] Worker valide les IDs sur chaque flux unidirectionnel D5 du ADR-MESH-L2-001
- [ ] Donna DLQ (cf. ADR-RICK-001) reçoit les records non-conformes

## Références

- ADR-MESH-L2-001 — Doctrine tri-plateforme L2 (ratifié même date)
- ADR-NOTION-001 — Back-office Solaris template
- ADR-RICK-001 — OpenHarness Incarnation + Donna DLQ
- Shadow_L2/10 + 11 — Cartographie + peuplement ClickUp
- Audit Airtable AaaS Solaris Marketing 2026-05-27 (transcript session)
