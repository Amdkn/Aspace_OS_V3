---
session: agent-a20fc1ac23e010e32
projet: subagents
debut: 2026-08-04T21:12:10.919Z
fin: 2026-08-04T21:17:14.251Z
messages_utilisateur: 1
reponses_assistant: 2
---

## >>> UTILISATEUR #1

Tu compares une copie vendorée de canvas-ui à son dépôt amont. LECTURE SEULE — ne modifie aucun fichier du dépôt Coach OS, ne clone rien, n'installe rien.

Amont : https://github.com/DavidHDev/canvas-ui
Copie locale : C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os/src/components/canvasui/v30/

Faits établis, ne les redécouvre pas : la copie locale contient 33 composants, chacun en `<Name>/<Name>.tsx` (wrapper React) + `<Name>Vanilla.ts` (moteur WebGL). Un `index.ts` sert de barrel.

Un autre agent audite déjà l'INTÉGRATION dans l'app (cycle de vie, thèmes, AppFrame). Ne fais pas ça. Toi tu travailles sur la CONFORMITÉ À L'AMONT.

Utilise `WebFetch` ou `curl` pour lire le README, la documentation et les sources de l'amont sur GitHub (raw.githubusercontent.com). Tu peux aussi utiliser les outils MCP GitHub disponibles.

Réponds à :

1. **Quelle est l'API d'intégration officielle ?** Comment l'amont recommande-t-il de monter un effet ? Props attendues, conteneur requis, contraintes de dimensionnement, gestion du `devicePixelRatio`.

2. **Quel est le contrat de nettoyage documenté ?** Que doit appeler un consommateur au démontage ? L'amont fournit-il un `destroy()` / `dispose()` ? Est-il appelé dans la copie locale ?

3. **Combien d'instances simultanées l'amont supporte-t-il ?** Partage-t-il un renderer entre effets, ou un par effet ? Documente-t-il la limite de contextes WebGL du navigateur ?

4. **Divergences.** Liste ce que la copie locale a modifié par rapport à l'amont : composants renommés, props ajoutées, moteurs réécrits, fichiers absents de l'amont. Concentre-toi sur les divergences qui touchent la performance ou le cycle de vie, pas les détails cosmétiques.

5. **Y a-t-il une version plus récente** de l'amont que celle copiée ? Sur quoi te bases-tu pour le dire ?

Rends un rapport dense, chaque affirmation sourcée (URL ou fichier:ligne). Si une information n'est pas trouvable dans la documentation amont, écris "non documenté" plutôt que de supposer.

### assistant

I'll start by exploring the local copy and fetching upstream sources in parallel.

### assistant

## Rapport de conformité à l'amont — canvas-ui v30

Méthode : comparaison exhaustive des 66 fichiers (33 `<Name>.tsx` + 33 `<Name>Vanilla.ts`) contre `DavidHDev/canvas-ui@main` (raw.githubusercontent), après normalisation CRLF/LF. Arbre amont récupéré via l'API git/trees (518 chemins, non tronqué).

---

### 0. Cadrage : la copie est quasi bit-à-bit conforme

Les 33 noms de composants locaux correspondent **exactement** aux 33 répertoires `src/lib/<Name>/` de l'amont — aucun renommage, aucun composant manquant, aucun composant inventé. L'amont y ajoute seulement les wrappers `.vue`/`.svelte`/`.solid.tsx`/`.preact.tsx` (non copiés, sans impact).

Sur 66 fichiers, il n'existe que **deux classes de divergence** (détail §4). Aucun moteur n'a été réécrit, aucune prop n'a été ajoutée aux composants eux-mêmes.

---

### 1. API d'intégration officielle

**Montage recommandé** (`README.md`, section « Quick start » ; docs Installation, `src/app/(shell)/docs/installation/page.tsx`) : on **enveloppe** le sous-arbre à décorer.

```tsx
import { Liquid } from "@/components/canvasui/Liquid";
<Liquid><YourEntirePage /></Liquid>
```

**Props attendues** (`src/lib/Liquid/Liquid.tsx:18-22`) : `LiquidProps extends LiquidOptions` + `children: ReactNode`, `className?: string`, `style?: React.CSSProperties`. **Aucune autre prop d'intégration** — pas de `width`/`height`, pas de `paused`, pas de `dpr`, pas de `quality` global (le `quality` existe sur certains moteurs seulement, ex. `FrostVanilla.ts`).

**Conteneur requis** — imposé par le wrapper, non par le consommateur (`Liquid.tsx:74-116`) : le composant crée lui-même un `<div style={{position:"relative", ...style}}>` contenant trois nœuds : un `<canvas layoutsubtree="true">` (source html-in-canvas), le `content` (`<div>` du sous-arbre), et un `<canvas aria-hidden>` de sortie en `position:absolute; inset:0; pointerEvents:none`. Le contrat vanilla correspondant est `LiquidElements { source, content, output }` (`LiquidVanilla.ts:32-42`).

**Contraintes de dimensionnement** : le moteur lit `output.clientWidth/clientHeight` (`LiquidVanilla.ts:529-531`). Le conteneur externe doit donc avoir une hauteur résolue par CSS — **l'amont ne le documente nulle part explicitement** ; c'est une contrainte déduite du code (`Math.max(1, …)` empêche seulement le crash, pas le rendu vide). Un `ResizeObserver` sur `output` (`LiquidVanilla.ts:845-849`) et une méthode publique `resize()` couvrent les redimensionnements.

**devicePixelRatio** : géré entièrement en interne, **plafonné à 2**.
- Famille wrapper : `const dpr = Math.min(window.devicePixelRatio || 1, 2)` puis `output.width = clientWidth*dpr` et, en mode html-in-canvas, `source.width = cssWidth*dpr` (`LiquidVanilla.ts:529-546`). Ce dimensionnement du buffer source vient du commit `c2494ea1` (2026-07-27, « Fix HTML blurriness for high-DPR screens ») — **présent dans la copie locale**.
- Famille Object (three.js) : `renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2))` (`AsciiObjectVanilla.ts:1314-1315`).

Aucune prop ne permet de surcharger le DPR. **Non documenté** côté site : le plafond de 2 n'apparaît dans aucune page de docs.

---

### 2. Contrat de nettoyage

**Oui, l'amont fournit un `destroy()` explicite et le documente.**

- Type public : `LiquidInstance.destroy: () => void`, commenté « Stop the loop and release all GPU resources » (`LiquidVanilla.ts:44-50`).
- Documenté dans l'exemple vanilla officiel : `liquid.destroy();` (installation/page.tsx, bloc `USAGE[vanilla]`).
- FAQ amont : « Each component initializes only when mounted, pauses when off-screen, and cleans up fully on unmount » (`src/components/landing/faq.tsx:24`).

**Ce que `destroy()` fait réellement** (`LiquidVanilla.ts:880-900`) : `destroyed = true`, `cancelAnimationFrame`, `observer.disconnect()` (ResizeObserver), `intersection.disconnect()` (IntersectionObserver), retrait du listener `prefers-reduced-motion`, `releaseAll()` (FBOs), `deleteTexture`/`deleteProgram`/`deleteShader`/`deleteBuffer`, `paintable.onpaint = null`, retrait des listeners pointer.
Famille Object (`AsciiObjectVanilla.ts:1431-1452`) : `stopLoop`, observers, `controls.dispose()`, `clearModel()`, `pmrem/draco/targets/materials/textures.dispose()`, `renderer.dispose()`.

**Limite importante, à signaler** : ni `Liquid` ni les moteurs three.js n'appellent `WEBGL_lose_context.forceContextLoss()` — vérifié à 0 occurrence sur `Liquid`, `GlassObject`, `LiquidObject`, `ParticleObject`, `DitheredObject`. Le contexte WebGL sous-jacent n'est donc libéré qu'au GC du canvas, pas de façon déterministe. Il n'existe **aucun** `dispose()` public (le nom du contrat est bien `destroy`).

**Est-il appelé dans la copie locale ?** Oui. Le cleanup du `useEffect` (`instanceRef.current?.destroy(); instanceRef.current = null;`) est présent et **byte-identique à l'amont** dans les 33 wrappers locaux — p. ex. `…/v30/Liquid/Liquid.tsx` et `…/v30/AsciiObject/AsciiObject.tsx`. Aucun composant local n'a perdu son `destroy()`.

---

### 3. Instances simultanées

- **Nombre supporté : non documenté.** Aucune page de docs, aucun README, aucun `llms.txt`, aucune entrée FAQ ne mentionne un nombre maximal d'effets simultanés.
- **Limite de contextes WebGL du navigateur : non documentée.** Recherche « context limit / WebGL context / multiple / per page » sur `docs/page.tsx`, `docs/installation/page.tsx`, `landing/faq.tsx`, `public/llms.txt` : zéro occurrence.
- **Renderer partagé : non.** Chaque instance crée son propre contexte : `output.getContext("webgl2", …)` par instance (`LiquidVanilla.ts:323-330`) ; famille Object : `renderer = new THREE.WebGLRenderer({…})` par instance (`AsciiObjectVanilla.ts:905`). **Un contexte GL par effet monté**, sans pool ni singleton.
- **Ce que l'amont fait de facto** (preuve indirecte, la seule disponible) : la page /components affiche les 33 composants via `<PreviewVideo src={component.video}>` (`src/app/(shell)/components/page.tsx:32-33`) — des `.webm` pré-enregistrés, pas 
