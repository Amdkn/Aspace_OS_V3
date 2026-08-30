# BRIEF — Agent OS : fond d'ecran, icones de bureau, redimensionnement

**Perimetre exclusif : `C:/Users/amado/agent-os/desktop/`.** Tu ne touches a rien
d'autre. En particulier `C:/Users/amado/agent-os/observatoire/` n'est pas a toi.

L'application existe, compile a **0 erreur TypeScript**, et a ete verifiee en
pilotant l'interface : dock peuple, fenetres qui s'ouvrent, multi-instances,
persistance au rechargement, export d'instantane. **Ne recommence rien.** Tu
ajoutes trois choses.

Le serveur de dev tourne sur `http://localhost:5199`. Ne le relance pas.

---

# 1 · Le fond d'ecran

L'image est deja en place : `public/wallpapers/solarpunk-3.jpg` (110 Ko).

Le bureau affiche aujourd'hui un degrade sombre. Il doit afficher cette image.

Trois choses a ne pas rater :

- **La lisibilite avant l'image.** Une photo derriere une barre de menus et des
  icones rend le texte illisible. Il faut un voile — un calque sombre entre le
  fond et le contenu, ou un flou local sous la barre. **Verifie le resultat en
  capture**, ne suppose pas que ca passe.
- **Le cadrage** : l'image doit couvrir sans se deformer.
- **Un fond reste choisissable.** Ne code pas le chemin en dur dans le composant
  du bureau. Une petite liste de fonds disponibles, l'actuel selectionne, le
  choix persiste comme le reste. Coach OS vient de faire la meme chose ; tu peux
  lire `src/lib/wallpaper.ts` dans son depot pour voir un motif, sans le copier.

---

# 2 · Les icones de bureau

Aujourd'hui les apps ne sont accessibles que par le dock. Le bureau est vide.

Ajoute des **icones sur le bureau**, une par app du registre — Observateurs,
Memoires, Cadre externe — et **elles doivent venir du registre**, pas d'une liste
ecrite a cote. Ajouter une app doit faire apparaitre son icone sans toucher au
bureau : c'est tout l'interet du registre ouvert.

Comportement attendu :

- **Double-clic** pour ouvrir. C'est la convention d'un bureau.
- **Un clic** selectionne, et la selection se voit.
- Les icones sont **deplacables**, et leur position **persiste**. Un bureau dont
  les icones reviennent en haut a gauche a chaque rechargement n'est pas un
  bureau.

Le registre porte deja un `icon` par app, aujourd'hui un caractere — `◉`, `✎`,
`▣`. Tu peux faire mieux, mais **n'ajoute aucune dependance d'icones** : trois
dependances aujourd'hui (react, react-dom, zustand), garde cette sobriete.

---

# 3 · Le redimensionnement

`resizeWindow` existe dans le magasin et n'est appele qu'a un seul endroit. Les
fenetres ne se redimensionnent pas a la souris.

- **Poignees sur les quatre bords et les quatre coins.** Pas seulement le coin
  bas-droit : c'est le minimum syndical, et on s'en apercoit tout de suite.
- **Tailles minimales** pour qu'une fenetre ne devienne pas inutilisable.
- **La taille persiste**, comme la position.
- Pendant le glissement, la fenetre suit le curseur sans decalage cumulatif.
  Le piege classique : recalculer a partir de la position de depart du curseur,
  pas a partir du dernier evenement.

---

## Interdits

0. **Aucun workflow BMAD** : ils ouvrent une porte « [A] Approve » infranchissable
   en session non interactive.
1. **Aucune dependance nouvelle.**
2. **Ne defais pas la correction de `shell/store.ts`.** `selectOrderedWindows`
   construisait un nouveau tableau a chaque appel : `useSyncExternalStore` compare
   par identite, d'ou « getSnapshot should be cached » puis « Maximum update depth
   exceeded », et la page ne s'affichait jamais. Il a ete remplace par le hook
   `useOrderedWindows()`. **Aucun selecteur ne doit construire un objet ou un
   tableau.** Le commentaire dans le fichier explique le piege ; laisse-le.
3. Pas de `git commit`, pas de `git push`.
4. Chemins absolus hors depot.

## Verification

```
npx tsc --noEmit -p tsconfig.app.json     # doit rester a 0
npx vite build
```

**Puis pilote l'interface et regarde.** Le typage vert ne prouve rien sur ce qui
s'affiche : la version precedente compilait parfaitement et ne s'affichait pas.

Un script de verification existe et fonctionne :
`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/verifie_agent_os.mjs`
Lis-le — il montre comment piloter cette application avec Playwright (installe
dans `~/gauntlet-eyes`), et son commentaire d'en-tete signale un piege : ses
premiers selecteurs cherchaient `footer button` alors que le dock est un `div`,
et il declarait a tort l'application cassee.

Ce que tu dois prouver, capture a l'appui :
1. le fond s'affiche **et le texte reste lisible par-dessus** ;
2. un double-clic sur une icone ouvre l'app ;
3. une icone deplacee reste en place apres rechargement ;
4. une fenetre redimensionnee par un bord **et** par un coin garde sa taille
   apres rechargement.

## Rapport

`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/RAPPORT_AGENT_OS_V3.md`

Les quatre preuves ci-dessus avec le chemin de leur capture, ce que tu as change,
et **tout point non fait avec sa raison**. Un point non fait et signale vaut mieux
qu'un point bacle en silence.

Si tu dois t'arreter avant la fin, ecris quand meme ce rapport.
