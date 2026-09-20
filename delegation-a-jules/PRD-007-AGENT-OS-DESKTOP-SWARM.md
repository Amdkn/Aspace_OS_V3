# PRD-007 — Agent-OS-Desktop Swarm Navigation & Shell Robustness

## 1. Objectif
Améliorer et consolider l'application Shell `agent-os/desktop` (Dashboard React/Vite sur port 5555) :
1. Intégrer une vue synthétique ou un onglet pour le suivi du **Swarm Sémantique Hermes** (10 profils : orchestrator, km-agent, builder, reviewer, qa, researcher, ops-watch, maintainer, strategist, inbox-triage) en complément des 3 Doctor Apps.
2. Vérifier et garantir l'accessibilité a11y (labels ARIA sur les boutons du Dock, TopBar et WindowFrame).
3. S'assurer que le build TypeScript (`pnpm build` ou `npm run build`) passe sans la moindre erreur (`0 error`).
4. Préserver l'empreinte mémoire légère et l'absence de re-renders inutiles.

## 2. Directives d'Exécution pour Jules
- Exécuter `pnpm install` / `npm install`.
- Vérifier `src/components/Dock.tsx`, `src/components/TopBar.tsx`, et les apps dans `src/apps/`.
- Lancer le linter et le compilateur TypeScript : `pnpm build` ou `npx tsc --noEmit`.
- Créer une PR automatiquement (`AUTO_CREATE_PR`).
