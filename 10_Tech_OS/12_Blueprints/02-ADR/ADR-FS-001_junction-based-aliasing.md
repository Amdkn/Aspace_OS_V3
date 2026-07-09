# ADR-FS-001 — Junction-Based Aliasing for Short-Path Agent Operability

**Date de décision :** 2026-05-22
**Auteur :** A0 Amadeus + A2 Claude Code (Architecte)
**Statut :** RATIFIÉ
**Type :** Architecture Decision Record (Filesystem / L0)
**Portée :** Filesystem souverain `C:\Users\amado\ASpace_OS_V2\` — gouverne les vues L1 et L2
**Ancré sur :** ADR-007 (Trust Zone V2) · ADR-002 (Portabilité) · ADR-FWK-021 (Canon Blueprints) · `AGENTS.md`

---

## Contexte

PARA/Enterprise est la **source de vérité** pour Projects (Picard), Areas (Spock), Resources (Geordi), Archives (Data). Business OS expose ces données par **secteur DC**. Sans aliasing :

1. **Chemins très longs** : `…\24_PARA_Enterprise\01_Projects_Picard\04 Alikaly Bana Holding to LLC\B2_Business_Domains\03_Product_Flash_Avengers\02_alykaly-os-v2\` = **143 caractères**. Windows MAX_PATH = 260 ; npm/pnpm/cargo/uv et watchers cassent bien avant.
2. **Risque de drift par copie** : robocopy/rsync 2-way garantit race conditions et conflits.
3. **Agents A3 perdus** : agents Marvel/DC ne savent pas si la source de vérité est Business OS ou PARA pour un dossier donné.
4. **Audit 2026-05-22** : 4 junctions existantes, dont 1 (`30_Business_OS\00_Links\alykaly-front`) configurée avec target auto-référentiel cassé (corrigée le 2026-05-22 vers la vraie cible PARA).

## Décision

**Trois couches d'aliasing filesystem complémentaires, basées sur les NTFS Junctions, jamais sur la copie.**

### Couche 1 — Junctions sentinelles racine `_\`

Création à la racine de `ASpace_OS_V2\` d'un dossier `_\` (underscore court, trié en haut, agent-friendly) :

```
ASpace_OS_V2\_\
├── biz\    → 30_Business_OS\
├── para\   → 20_Life_OS\24_PARA_Enterprise\
├── proj\   → 24_PARA_Enterprise\01_Projects_Picard\
├── area\   → 24_PARA_Enterprise\02_Areas_Spock\
├── res\    → 24_PARA_Enterprise\03_Resources_Geordi\
├── arch\   → 24_PARA_Enterprise\04_Archives_Data\
├── snw\    → 20_Life_OS\23_12WY_SNW\
├── gtd\    → 20_Life_OS\25_GTD_Cerritos\
└── deal\   → 20_Life_OS\26_DEAL_Protostar\
```

Gain : `…\_\proj\` = 38 caractères vs 70+. Le Canon reste à sa place — `_\` n'est qu'une **vue**.

### Couche 2 — Drives PowerShell (`subst` / `PSDrive`)

Pour les outils CLI/agents (npm/cargo/uv/git), ergonomie maximale via lettres de drive :

```powershell
subst B: C:\Users\amado\ASpace_OS_V2\30_Business_OS
subst P: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise
```

Persistance via profil PowerShell ou script `Setup-ASpace-Junctions.ps1` (livré en ADR-FS-002 / script B).

### Couche 3 — Junctions fonctionnelles Business OS ↔ PARA

| Type de contenu | Source de vérité (propriétaire) | Vue (junction) |
|-----------------|----------------------------------|----------------|
| **Projects B3** (code, repos actifs) | `PARA\01_Projects_Picard\<projet>\…\<repo>\` | `30_Business_OS\<secteur>\<repo>` (junction) |
| **Areas B2** (process, SOP, dashboards) | `PARA\02_Areas_Spock\Business_Pulse\` | `30_Business_OS\00_Jerry_Business_Pulse\` (junction) |
| **Resources B3** (templates, guides) | `PARA\03_Resources_Geordi\` | `30_Business_OS\00_Links\res\` (junction unique) |
| **Archives** (gelé, read-only) | `PARA\04_Archives_Data\` | `30_Business_OS\00_Links\arch\` (junction unique) |
| **12WY / GTD / DEAL** (transversaux) | `20_Life_OS\23_12WY_SNW\` etc. | `30_Business_OS\00_Links\snw\` `\gtd\` `\deal\` (junctions uniques racine) |

### Règles d'or

1. **Chaque dossier n'a qu'UN propriétaire réel.** L'autre côté est toujours une junction. Aucune copie, aucun robocopy, aucun rsync 2-way.
2. **NTFS Junctions uniquement** (`mklink /J`). Symlinks (`mklink /D`) interdits sauf cross-volume justifié — ils demandent Developer Mode et cassent silencieusement sur certains outils.
3. **Junctions = même volume.** Si cross-volume requis (rare), exception documentée case par case.
4. **`node_modules` jamais junctionnés.** Watchers (nodemon, vite, esbuild, webpack) deviennent fous. `node_modules` reste local au repo réel.
5. **Variables d'environnement portables** : `$env:ASPACE_ROOT`, `$env:ASPACE_BIZ`, `$env:ASPACE_PARA`. Jamais de chemin hardcodé dans un script agent (cf. ADR-002).

### Réponses aux questions architecturales (2026-05-22)

- **Geordi (Resources) et Data (Archives) doivent-ils passer dans Business OS ?** Oui, mais en lecture via **une junction unique** (`00_Links\res\` et `00_Links\arch\`). PARA reste propriétaire. Pas de junction par secteur DC — overhead inutile.
- **12WY / GTD / DEAL doivent-ils être junctionnés par secteur DC ?** **Non.** Une seule junction par OS, au niveau `30_Business_OS\00_Links\`. Si junction par secteur (8 secteurs), on multiplie le bruit sans bénéfice.
- **B3 vivent dans PARA ou Business OS ?** **PARA/Picard** est la propriété (un projet a un cycle de vie → P de PARA). Business OS expose les B3 actifs via junctions sectorielles. Pattern déjà éprouvé sur `alykaly-front` après correction.

## Conséquences

### Positives
- Path length réduit ~60% pour les usages agents
- Drift impossible par construction (1 propriétaire, N vues)
- Git voit un seul fichier (pas de duplication)
- Aucun script de sync à maintenir
- Stratégie testable : `Test-Path` sur target = audit complet en 1 commande

### Négatives
- Junctions invisibles dans Explorer Windows (icône identique aux dossiers) → besoin d'audit régulier
- Outils legacy ignorant les junctions peuvent suivre 2 fois (rare, ex : antivirus mal configuré)
- Création de junction nécessite shell admin OU mklink (non-admin OK pour `/J`)

### Anti-patterns explicitement interdits
- `robocopy /MIR` en mode 2-way
- `mklink /D` (symlinks) hors cas cross-volume documenté
- Junction vers `node_modules`, `.next\`, `.git\` ou tout dossier avec watcher actif
- Hardcoder un chemin long dans un script agent au lieu d'utiliser `$env:ASPACE_*`

## Implémentation

- **Script associé** : `Setup-ASpace-Junctions.ps1` (livré sous ADR-FS-002), idempotent, dry-run par défaut, audit + create + verify
- **Variables d'env** à exporter dans le profil PowerShell utilisateur :
  ```powershell
  $env:ASPACE_ROOT = 'C:\Users\amado\ASpace_OS_V2'
  $env:ASPACE_BIZ  = "$env:ASPACE_ROOT\30_Business_OS"
  $env:ASPACE_PARA = "$env:ASPACE_ROOT\20_Life_OS\24_PARA_Enterprise"
  $env:ASPACE_SHORT = "$env:ASPACE_ROOT\_"
  ```

## Audit initial (2026-05-22)

- 4 junctions existantes : 3 OK, 1 cassée (`alykaly-front` self-référence) → **corrigée**
- 0 symlink détecté
- 0 junction orpheline post-correction

## Références

- ADR-007 — Paradigm Shift V2 / Trust Zone (fondateur)
- ADR-002 — Portabilité Multiverse / `ASPACE_ROOT` env var
- ADR-FWK-021 — Canon Tripartite des Blueprints (parent doctrinal)
- `AGENTS.md` § Trust Zone absolue
