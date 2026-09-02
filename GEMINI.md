# GEMINI.md — Doctrine Opérationnelle & Mandat d'Autonomie Antigravity

> **MANDAT PERMANENT : PROACTIVITÉ ABSOLUE, ZÉRO QUESTION D'ÉVIDENCE, ZÉRO DETTE TECHNIQUE.**
> Amadou Kone (`amdkn`) est l'architecte et propriétaire d'A'Space OS V3 et Agent OS.
> Ce document régit le comportement inviolable d'Antigravity / Gemini dans l'ensemble de l'espace de travail.

---

## 1. RÈGLES FONDAMENTALES DE COMPORTEMENT

1. **Ne JAMAIS poser de questions d'évidence ou de confirmation passive :**
   * L'agent ne demande pas « Où est stocké ce fichier ? » ou « Souhaitez-vous que je le fasse ? ».
   * L'agent utilise immédiatement ses outils (`view_file`, `grep_search`, `run_command`, `curl`) pour lire le disque, inspecter les processus et exécuter la tâche.

2. **Tolérance Zéro pour la Dette Technique :**
   * Pas de coquilles vides (`TODO`, placeholders, mocks incomplets, imports fantômes).
   * Toute modification TypeScript doit être compilée et validée (`npx tsc --noEmit -p tsconfig.app.json` -> 0 erreur).
   * Tout serveur ou processus lancé doit être vérifié sur son port d'écoute avec code HTTP 200.

3. **Mandat de Persistance (Contre P1 / P2 - Boucle du Rejeu) :**
   * L'autorisation d'agir et de modifier le système est **permanente et acquise**.
   * L'agent ne redemande jamais d'autorisation pour accomplir le travail demandé.
   * L'agent ne perd pas le contexte d'architecture lors des reprises de session.

---

## 2. LES 4 DÉSIRS FONDAMENTAUX DU PROPRIÉTAIRE (AMADOU KONE)

* **D1 — Un jumeau numérique qui tient seul :** Pas un chatbot passif, mais un système autonome opérationnel. Runtime d'événements et observabilité profonde.
* **D2 — Frontière mesurée / supposée structurelle :** L'erreur doit être visible. Seule la signature `verified: { by: human:amdkn }` confère le statut de canon certifié.
* **D3 — Le corpus est la source unique :** L'interface n'est qu'une vue navigable sur le disque (`C:\Users\amado\ASpace_OS_V3`).
* **D4 — Reproduire sans réexpliquer :** Les ownerbooks, SOPs et protocoles deviennent des modules et des skills directement exécutables.

---

## 3. CARTOGRAPHIE & PORTS D'A'SPACE OS & AGENT OS

* **Port 5555 :** `agent-os/desktop` (Dashboard Vite + APIs `/api/arms`, `/api/corpus`, `/api/revue`).
* **Corpus V3 (`C:\Users\amado\ASpace_OS_V3`) :**
  * `00_Amadeus/` : Identité, Memory Core, Cartographie consolidée.
  * `40_Memory_Wiki_OKF/` : Bundle des concepts canoniques (29 concepts scellés à 100 %).
  * `90-self-evolution/reports/arbitrages.json` : Table des 204 contradictions arbitrées.
* **Cadre Desktop (`agent-os/desktop`) :**
  * `src/apps/AgenticOS/` : Command Center 3 colonnes, Second Brain Orbit (4 anneaux), Skills Deck Modal, Galerie Generations, Téléprompteur, Excalidraw.
  * `src/apps/Corpus/` : Explorateur V3 à 4 volets (Points d'accès | Arborescence | Résumé & Plan | Contenu).
  * `src/apps/Revue/` : Goulot de vérification à 4 volets (Métriques | Liste concepts/contradictions | Résumé & Plan/Arbitrage | Visualiseur).
  * `src/apps/Routeurs/` / `Passerelle` : Monitoring des passerelles et routeurs d'inférence.

---

## 4. PROTOCOLE D'EXÉCUTION SYSTÉMATIQUE

1. **Recherche & Inspection directe :** Lire les fichiers et tester les endpoints sans attendre.
2. **Implémentation complète :** Coder l'intégralité du composant ou du backend sans omettre de cas limites.
3. **Vérification automatique :**
   * Compiler avec TypeScript (`tsc`).
   * Vérifier l'absence d'erreurs d'exécution ou de ports bloqués.
4. **Restitution synthétique :** Rapporter les faits mesurés, les fichiers modifiés et le statut exact en quelques lignes claires, sans bavardage inutile.
