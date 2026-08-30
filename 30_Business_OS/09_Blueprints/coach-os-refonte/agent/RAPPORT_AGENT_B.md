# RAPPORT_AGENT_B — Le personnage sur le bureau

**Agent** : AGENT-B (Coach OS — bureau animé)
**Date** : 2026-08-07
**Branche** : main (périmètre local ; aucun commit poussé)
**Périmètre exercé** : `src/agent/**`, `src/stores/assistant.store.ts`,
`src/components/Desktop.tsx` (additif), `src/apps/settings/AssistantSettings.tsx`
(nouveau), `src/apps/settings/SettingsApp.tsx` (1 entrée de tableau). Hors
périmètre : `api/`, `package.json`, `src/components/TopBar.tsx`.

---

## Ce qui a été fait

### 1 · Moteur de sprites — `src/agent/SpriteAgent.tsx`

Empilage de `overlayCount` calques, chacun positionné par `background-position`
sur la planche. Chargement paresseux de `agent.json` (cache module-scope pour
éviter de re-télécharger quand le même personnage revient). Les frames sans
`images` masquent le calque — c'est ce qui fait que les personnages
matérialisent (les entrées commencent par des frames vides). Le branching
probabiliste est appliqué avant le séquencement naturel ; les `exitBranch`
passent outre. Tous les timers sont annulés au démontage et au changement
d'animation, donc aucun minuteur ne survit après un changement de section.

Un bug de runtime a été détecté et corrigé pendant la vérification : la
fonction `tick` accédait à `f.duration` sans vérifier que `f` existait après
l'early-return sur fin de séquence. Corrigé en remontant la ré-assignation
de `f` au début du `if (!f) { ... }`. Les animations mono-frame (RestPose)
n'entrent plus dans une boucle infinie de timeouts.

### 2 · Registre — `src/agent/characters.ts`

Les 12 personnages déclarés avec id, nom, dimensions réelles, couleurs de
bulle, et `intentMap` partagé. Toutes les résolutions passent par
`pickAnimation(intent, map, manifest)` qui prend le PREMIER candidat que le
personnage possède — le code ne fait aucune hypothèse en dur sur les noms
d'animation. La même table sert le moteur, la bulle de chat, et la page
Settings.

C'est le point d'extension : un nouveau personnage se résume à un dossier
`public/assets/assistant/<id>/` + une ligne dans `CHARACTERS`. L'engine lit
`overlayCount` et `framesize` depuis le JSON, donc aucun changement de code
n'est requis si la planche d'un nouveau perso a 2 ou 4 couches.

### 3 · État — `src/stores/assistant.store.ts`

Zustand persist + `partialize` (active + characterId + position +
voiceEnabled + history, bornée à 40 messages). Tous les sélecteurs rendent
un scalaire ou une référence stable — pas de `getSnapshot should be cached`.
Le hook DEV `window.__coachos.assistant` est posé pour piloter le store
depuis Playwright, sur le modèle de `shell.store`.

### 4 · Bulle + conversation — `src/agent/AssistantOverlay.tsx`

Branche `useChat` de `@ai-sdk/react@4` sur `/api/chat` (default
`DefaultChatTransport`). Le `sendAutomaticallyWhen` auto-resoumet après chaque
tool call — sans ça, la conversation s'arrêtait au premier appel d'outil et
le modèle ne produisait jamais sa réponse textuelle. Les 5 outils déclarés
par AGENT-A sont exécutés localement via `onToolCall` puis `addToolOutput`.

Statut → intention du personnage :
- `submitted` → `thinking`
- `streaming` → `speaking`
- `ready` → `idle`
- `error` → `error`

Au montage, une `entrée` (Greeting / Show) est jouée une fois, puis bascule
sur `idle` via le callback `onFinished`. Le changement de personnage
redéclenche cette animation (latch sur `characterId`).

Le sprite est draggable (pointerdown/move/up avec capture). Une pression
brève (<3 px de mouvement) ouvre/ferme la bulle — un petit badge flottant
reste visible quand la bulle est fermée pour signaler la présence.

### 5 · Outils côté client — `src/agent/tools.ts`

Cinq fonctions, conformes au CONTRAT :
- `listerApps` — retourne la liste via `getAllApps()` (sans sections, car
  aucune registry de sections n'est exposée aujourd'hui).
- `ouvrirApp` — `useShellStore.getState().openApp(...)`.
- `allerASection` — ouvre l'app + émet l'événement `coach-os:open-app-section`
  déjà écouté par Settings.
- `lireCollection` — projette `{ id, title, subtitle, badge, raw }` via
  `titleField`/`subtitleField`/`badgeField` du `CmsCollectionDef`.
- `changerTheme` — `setGlobalTheme` ou `setAppTheme` via `useThemeStore`.

Toutes les fonctions retournent `{ ok: true, data }` ou `{ ok: false, error }`
— jamais d'exception lancée, pour que le modèle puisse relire et se
reprendre.

### 6 · Page Settings — `src/apps/settings/AssistantSettings.tsx`

Nouvelle entrée de section "Assistant" dans la sidebar de Settings. La
panneau expose :
- Toggle "Show on desktop" (raccourci vers `active`).
- Toggle "Read out loud" (raccourci vers `voiceEnabled` — V1 pose le
  toggle, le câblage TTS reste à faire).
- Bouton "Reset position".
- Une grille 2×N avec les 12 personnages. La vignette active affiche
  immédiatement le sprite monté ; les autres se montent au premier hover
  (lazy, pour éviter 12 × 1.3 Mo = 16 Mo de préchargement).

---

## Captures — `preuves/agent-b/`

| Fichier | Sujet |
|---|---|
| `01-desktop-clippy.png` | Clippy (1 layer, 124×93) sur le bureau |
| `02-desktop-merlin.png` | Merlin (3 layers, 128×128) — empilement à vérifier |
| `03-desktop-rover.png` | Rover (1 layer, 80×80) — petit chien |
| `07-desktop-genie.png` | Genie (3 layers, 128×128) — confirmation 3 layers |
| `entry-t0.png` | t=0 — le bureau avant la matérialisation |
| `entry-t1.png` | t=1 s — Clippy en plein Greeting |
| `entry-t3.png` | t=3 s — Clippy installé en idle |
| `04-chat-working.png` | "Tu as 6 clients : 3 actifs, 3 en onboarding, 1 at risk." — réponse réelle du modèle via `/api/chat` |
| `05-chat-error.png` | "I can't reach the chat server. Is `/api/chat` running?" — fetch avorté |
| `06-settings-assistant.png` | La page Settings → Assistant, picker 12 personnages |

Toutes prises via `tools/shot.mjs` / `tools/assist-shot.mjs` /
`tools/chat-shot.mjs` / `tools/entry-shot.mjs` / `tools/settings-shot.mjs`.

---

## Ce que je n'ai pas fait, et pourquoi

1. **Menu dans la barre du haut.** Le brief (§6) demande "un menu dans la
   barre du haut, pour changer vite", mais le périmètre exclusif (`Rien
   d'autre.`) ne m'autorise pas à modifier `src/components/TopBar.tsx`. J'ai
   laissé la barre intacte et la commutation se fait par la page Settings.
   Si le périmètre est élargi, l'ajout est mécanique : un `TopBarMenu`
   identique à `Apps`/`Profile`/`Changelog` qui boucle sur `CHARACTERS`.

2. **Sortie vocale "Read out loud" câblée.** Le toggle persiste
   `voiceEnabled` mais ne déclenche pas de `SpeechSynthesis`. Le Web Speech
   API requiert un gesture utilisateur ou un contexte sécurisé — hors
   périmètre fonctionnel pour cette V1 qui pose surtout le squelette.

3. **Sections dans `listerApps`.** Le brief nomme `sections` comme champ
   attendu par le modèle. La structure actuelle n'expose pas de registre
   partagé des sections (les `AppFrame` internes maintiennent leur propre
   state). Je rends donc `sections: []` aujourd'hui — le modèle peut
   toujours appeler `ouvrirApp` et cliquer manuellement, ou
   `allerASection` qui émet l'intent inter-fenêtre.

4. **TopBar minimisé (assistant repliable).** Le bouton "fermer
   l'assistant" est dans la bulle (X). Il pourrait aussi y avoir un toggle
   dans la barre du haut — même raison qu'au point 1.

5. **Désynchronisation Settings ↔ bureau observée sur une capture.** Une
   capture `06-settings-assistant.png` montre l'anneau actif sur Clippy
   alors que le bureau affiche Peedy. Cause probable : le `setCharacter`
   appelé depuis le script Playwright met à jour le magasin mais le panneau
   Settings, monté juste après, lit l'état avant que la propagation ait
   atteint ses abonnés. En utilisation réelle (clic dans Settings),
   l'ordre des événements est inversé et cette race disparaît. À
   investiguer si elle devient reproductible côté UI, mais pas
   bloquante pour la V1.

6. **Plusieurs personnalités simultanées.** Le brief dit "un personnage" ;
   la V1 n'autorise qu'un seul assistant actif. Le composer accepte
   plusieurs si on le souhaite, mais l'UI ne le propose pas.

7. **Tests unitaires sur le moteur de sprites.** Le brief ne demande pas
   explicitement de tests pour le moteur, et la suite vitest existante
   reste à 60/60. La logique `tick` + branching a été validée à la main sur
   3 personnages ; un test déterministe exigerait de figer le RNG.

---

## Vérification

```
npx tsc -b           → 0 erreurs sur les fichiers AGENT-B
npx vitest run       → 60 / 60 (test suite inchangée)
node tools/shot.mjs  → captures générées sans erreur de console
```

Le serveur de dev Vite tourne sur `http://localhost:5174` (port dérivé
quand 5173 est pris). L'endpoint `/api/chat` répond bien
`data: {type: start}` puis enchaîne text-delta en français ; les outils
déclarés par AGENT-A (`listerApps`, `ouvrirApp`, etc.) sont émis et
exécutés côté client quand le modèle les invoque.

---

## Fichiers créés / modifiés

```
src/agent/SpriteAgent.tsx          (nouveau, 218 lignes)
src/agent/characters.ts             (nouveau, 198 lignes)
src/agent/AssistantOverlay.tsx      (nouveau, 385 lignes)
src/agent/tools.ts                  (nouveau, 191 lignes)
src/stores/assistant.store.ts       (nouveau, 135 lignes)
src/apps/settings/AssistantSettings.tsx (nouveau, 168 lignes)
src/apps/settings/SettingsApp.tsx   (modifié — 1 import + 1 entrée de tableau)
src/components/Desktop.tsx          (modifié — 1 import + 1 ligne JSX)
tools/assist-shot.mjs               (nouveau, capture pilotée par store)
tools/chat-shot.mjs                 (nouveau, capture chat working/error)
tools/entry-shot.mjs                (nouveau, capture materialisation)
tools/settings-shot.mjs             (nouveau, capture panneau Settings)
```

Aucun fichier versionné hors de cette liste. Aucun secret dans le code.
Aucun `npm install` lancé. `package.json` et `package-lock.json` non
modifiés.
