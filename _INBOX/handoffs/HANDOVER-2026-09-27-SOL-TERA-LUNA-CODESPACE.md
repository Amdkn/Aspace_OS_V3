# HANDOVER — SOL / TERA / LUNA / CODESPACE — 2026-09-27

## Canon
A'Space V3 reste un seul système. Les noms Sol, Tera et Luna désignent des mondes de travail fédérés, pas de nouveaux OS concurrents.

- **Sol** = filesystem souverain V3 : `C:/Users/amado/ASpace_OS_V3` → `Amdkn/Aspace_OS_V3`.
- **Tera** = monde Agent OS local : `C:/Users/amado/agent-os`.
- **Luna** = monde Life OS propre : `C:/Users/amado/ASpace_Worlds/Life_OS_2026` → `Amdkn/Life-OS-2026`.

## Junctions locales
Sol expose deux junctions à sens unique :
- `C:/Users/amado/ASpace_OS_V3/Agent_OS` → `C:/Users/amado/agent-os`.
- `C:/Users/amado/ASpace_OS_V3/Life_OS_2026` → `C:/Users/amado/ASpace_Worlds/Life_OS_2026`.

Ces deux chemins sont exclus uniquement via `.git/info/exclude` du checkout Sol. Ils ne doivent jamais être ajoutés comme contenu Git V3.

## Tera / Agent OS / port 5555
Le service 5555 correspond à `agent-os/desktop` (Vite, host 127.0.0.1, strictPort=true). Aucun listener 5555 n'était actif au moment du snapshot.

L'état local vivant du Desktop a été préservé sur GitHub :
- repo : `Amdkn/Agent-OS-Desktop`
- branche : `snapshot/tera-5555-2026-09-27`
- SHA : `9d5782868babb16e4477214dee0a40a8b6825e80`
- snapshot machine : `_INBOX/handoffs/TERA_AGENT_OS_5555_SNAPSHOT.json`.

Le parent local `Agent-OS` est sur le SHA `4b73326954b602134a51ed9bad147d187a9479b0`. Son push snapshot parent a été refusé par GitHub Push Protection à cause d'un ancien Supabase PAT dans l'historique. Aucun bypass n'a été effectué. Le parent ne doit pas être considéré comme clonable depuis GitHub tant que cet historique n'est pas assaini.

Tera Codespace est donc fédéré :
- Desktop → `Amdkn/Agent-OS-Desktop` snapshot 5555.
- HermesWorkspace → `outsourc-e/hermes-workspace`.
- Observatoire → local-only tant qu'aucun remote n'est défini.
- Parent Agent-OS → local-only jusqu'à assainissement.

## Luna + Business Skyhooks
Luna est un clone propre de `Amdkn/Life-OS-2026`, SHA local initial `3718ee652838eee498195b5dded83701fdb56aec`.

Dans Codespaces, Luna possède des Skyhooks vers les repos Business fédérés, sans les inclure dans son historique Git :
`BusinessOS`, `Business-Office-3-OS`, `01-OMK-Business-OS`, `The-OMK-Mobile-Back-Office`, `OMK-DESKTOP-WEB-OS`, `00-omk-saas-os`.

## Continuité partagée
- WHO → `ADE_REGISTRY`.
- WHERE → `ASPACE_WORKSPACE_REGISTRY`.
- NOW → Supabase `Aspace OS / Agent OS Backend / aspace`.
- Human Blackboard → Linear.
- Versioned worlds → GitHub.
- Federated cloud workspace → GitHub Codespaces.
- Living Desktop → Omarchy VM (planifié).

## Automatisation Codespace
Politique : `ASPACE_AUTOMATION_POLICY.json`.
Budget : 4 h/jour cumulées de runtime d'automatisation lorsque le Codespace est actif ; aucun horaire fixe n'est inventé.
Capacité additionnelle : >=80% Life + Business ; Kernel <=20%, sauf blocage Kernel critique qui débloque directement Life/Business.

Harness locaux vérifiés :
- Antigravity / `agy` 1.2.6
- Codex 0.153.4
- Hermes Agent 0.21.0

Dans Codespaces, aucun harness ne s'exécute tant qu'un adapter Linux explicite n'est pas fourni via `ASPACE_ANTIGRAVITY_CMD`, `ASPACE_CODEX_CMD` ou `ASPACE_HERMES_CMD`. Le budget controller refuse donc les faux lancements.

## GitHub / Codespace
Branche Registry : `feat/aspace-workspace-registry`.
PR : #168 sur `Amdkn/Aspace_OS_V3`.
Codespace principal : `a-space-federated-workspace-7g5grwqpgrxfvr`.

Prochaine reprise : valider le bootstrap fédéré dans le Codespace après rebuild, puis installer/configurer les adapters Linux des harness sans contourner les secrets ni fusionner les repos en un monorepo.
