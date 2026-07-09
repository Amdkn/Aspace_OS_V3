# ADR-FS-002 — Script `Setup-ASpace-Junctions.ps1` (Sentinelles + Profile)

**Date :** 2026-05-22
**Auteur :** A0 Amadeus + A2 Claude Code (Architecte)
**Statut :** RATIFIÉ — EXÉCUTÉ
**Type :** Architecture Decision Record (Filesystem / L0)
**Portée :** Implémentation opérationnelle d'ADR-FS-001 (couche 1 sentinelles + env vars)
**Ancré sur :** ADR-FS-001 · ADR-FWK-021 · ADR-FWK-022

---

## Contexte

ADR-FS-001 a défini 3 couches d'aliasing (sentinelles `_\`, drives subst, junctions fonctionnelles). La couche 1 (sentinelles `_\`) et l'export des variables d'environnement portables n'avaient pas d'outil opérationnel. Ce ADR livre le script.

## Décision

Le script canonique vit dans `10_Tech_OS\11_Infra_13th_Doctor\02_Ryan_SysAdmin\Setup-ASpace-Junctions.ps1` (Ryan = Companion SysAdmin du 13th Doctor).

### Capacités

- **Idempotent** : skip si junction existe et target correct
- **Dry-run par défaut** : exécution réelle nécessite `-Apply`
- **Audit (`-Audit`)** : liste toutes les junctions du tree avec status OK/BROKEN
- **Patch profil (`-InstallProfile`)** : append les `$env:ASPACE_*` au PowerShell profile, marqué pour éviter doublons
- **Couvre 2 jeux** : 9 sentinelles racine `_\` + 5 sub-junctions Business OS Links (ce dernier = ADR-FS-003 ci-dessous absorbé)

### Sentinelles racine `_\` créées

```
ASpace_OS_V2\_\
├── biz  → 30_Business_OS
├── para → 20_Life_OS\24_PARA_Enterprise
├── proj → PARA\01_Projects_Picard
├── area → PARA\02_Areas_Spock
├── res  → PARA\03_Resources_Geordi
├── arch → PARA\04_Archives_Data
├── snw  → 20_Life_OS\23_12WY_SNW
├── gtd  → 20_Life_OS\25_GTD_Cerritos
└── deal → 20_Life_OS\26_DEAL_Protostar
```

### Variables d'environnement (patch profil PowerShell)

```powershell
$env:ASPACE_ROOT  = 'C:\Users\amado\ASpace_OS_V2'
$env:ASPACE_BIZ   = "$env:ASPACE_ROOT\30_Business_OS"
$env:ASPACE_PARA  = "$env:ASPACE_ROOT\20_Life_OS\24_PARA_Enterprise"
$env:ASPACE_SHORT = "$env:ASPACE_ROOT\_"
# Optionnel : subst B: $env:ASPACE_BIZ / subst P: $env:ASPACE_PARA
```

## Audit initial post-exécution

- **Total junctions ASpace_OS_V2** : 37 (toutes OK, 0 broken)
- Sentinelles `_\` : 9/9
- `_Inbox\B1/B2/B3` × 6 projets Picard : 18
- `00_Summers_QuickAccess\*` : 6
- Business OS `00_Links\*` : 8 (3 historiques + 5 ajoutées par ce script — voir ADR-FS-003)
- PARA `00_Links\30_Business_OS_Portal` : 1

## Usage

```powershell
.\Setup-ASpace-Junctions.ps1                  # dry-run (preview)
.\Setup-ASpace-Junctions.ps1 -Apply           # exécute
.\Setup-ASpace-Junctions.ps1 -Audit           # liste + status
.\Setup-ASpace-Junctions.ps1 -InstallProfile  # patch $PROFILE
```

## Conséquences

### Positives
- Toute machine A0 peut être reset/reinstall : un seul `-Apply` reconstruit l'aliasing complet
- Auditable en 1 commande
- Profil utilisateur portable (les `$env:ASPACE_*` partout disponibles)

### Négatives
- Script PowerShell uniquement (pas cross-platform — acceptable, A'Space est Windows)
- N'inclut pas (encore) les junctions par projet Picard (`_Inbox`) ni `00_Summers_QuickAccess` — à intégrer en v2 si besoin de reset complet

### Suivi
- v2 du script : intégrer les junctions Picard `_Inbox\B1/B2/B3` × 6 et `00_Summers_QuickAccess\*`
- Tester `-InstallProfile` sur le profil A0 réel

## Références

- ADR-FS-001 — Junction-Based Aliasing
- Script : `10_Tech_OS\11_Infra_13th_Doctor\02_Ryan_SysAdmin\Setup-ASpace-Junctions.ps1`
- Audit log inclus dans Shadow_L0/04 (ci-dessous)
