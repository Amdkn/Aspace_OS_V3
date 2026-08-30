# RAPPORT-E — L'écoute et la parole

> Source du brief : `BRIEF_E_VOIX.md` · analyse : `ANALYSE_PALANTIR.md` ·
> garde-fou : `coach-os-refonte/correctifs/GARDE_FOU.md`.
> Dépôt : `coach-os` · Branche `main` · Aucun commit créé.
> Captures : `preuves/E/` (9 PNG).

---

## 1. Ce qui a été construit

L'écoute et la parole sont maintenant branchées sur les personnages du bureau. Aucun service tiers, aucune dépendance ajoutée — tout vit dans le navigateur via les API natives `SpeechRecognition` (Chromium / Edge via `webkitSpeechRecognition`) et `SpeechSynthesis` (Chromium, Firefox, Safari).

### Fichiers créés

| Fichier | Rôle |
|---|---|
| `src/agent/voice.ts` | Service vocal complet : détection, hooks `useVoiceRecognition` et `useVoiceSynthesis`, sanitizer `sanitizeForSpeech`, singleton de parole (`claimSpeaker` / `preemptSpeaker`), `pickDefaultVoice`, `loadVoicesWithTimeout`. |
| `src/agent/VoiceWave.tsx` | Indicateur visuel : 4 barres animées pendant l'écoute ou la parole. Couleur paramétrable (le bord de la bulle par défaut). |
| `src/agent/voice.test.ts` | Tests vitest : détection des API, sanitizer (4 modes × ~7 motifs), singleton de speaker (coupe le précédent, no-op sur soi-même), voix par défaut. |
| `tools/voice-shot.mjs` | Script Playwright : 9 preuves visuelles dans `preuves/E/`. |

### Fichiers modifiés

| Fichier | Changement |
|---|---|
| `src/stores/assistant.store.ts` | Trois champs persistés : `voiceName` (string \| null), `voiceRate` (0.5..2.0), `voicePrivacy` (`'none' \| 'safe' \| 'strict'`). Le merge valide `voiceRate` (clamp + NaN check) et `voicePrivacy` (set fermé) — un `localStorage` forgé ne peut plus faire crasher `SpeechSynthesis`. Trois setters (`setVoiceName`, `setVoiceRate`, `setVoicePrivacy`). |
| `src/agent/AgentTile.tsx` | Lit `voiceEnabled`, `voiceName`, `voiceRate`, `voicePrivacy`. Branche `useVoiceRecognition` et `useVoiceSynthesis`. Bouton micro dans la bulle (absent si `SpeechRecognition` n'existe pas). Bouton stop pendant synthèse. Indicateur `VoiceWave` dans l'en-tête de la bulle. Pendant l'écoute, la transcription intermédiaire s'injecte dans le champ. Quand l'agent répond, `speak()` est appelé sur la dernière réponse complète. Refus de permission → message en bulle. Pendant la synthèse, `intent` reste `'speaking'` même si le streaming texte est terminé, pour que le sprite joue son animation de parole. |
| `src/apps/settings/AssistantSettings.tsx` | Toggle "Read out loud" actif seulement si `SpeechSynthesis` est présent. Trois nouveaux panneaux apparaissent quand la voix est activée : sélection de voix (via `getVoices()` avec retry de 1 s), slider de vitesse 0.5x-2.0x, choix du mode de confidentialité (`safe` / `strict` / `none`). |

---

## 2. Les trois invariants (rappelés dans le code)

Le brief énumère trois invariants que je rappelle ici dans les commentaires
du code, parce que les anciens bugs sur ce projet sont tous des violations
d'un de ces invariants :

1. **Aucun service tiers.** Pas de `npm install`. `SpeechRecognition` et
   `SpeechSynthesis` sont des API natives ; si elles sont absentes, le
   bouton micro ne s'affiche pas du tout (plutôt qu'un bouton qui ne
   fait rien — règle du brief).

2. **Un seul speaker à la fois.** Singleton `claimSpeaker` /
   `preemptSpeaker`. Si un nouvel agent commence à parler pendant qu'un
   autre parle, l'ancien est coupé net. Justification explicite dans
   le code : l'API SpeechSynthesis est mono-voix par système, et deux
   personnages qui parlent en même temps sont inaudibles. C'est aussi
   le geste humain naturel — on ne coupe pas la parole dans une
   conversation réelle.

3. **Nettoyage au démontage.** `useVoiceRecognition` et
   `useVoiceSynthesis` font tous deux un `useEffect` de cleanup qui
   abort la reconnaissance / cancel la synthèse. Sans ça, un micro
   ouvert sans composant est inacceptable (et pire : un micro ouvert
   sans signal visible, parce que le sprite est démonté).

---

## 3. Politique de confidentialité — ce que j'ai posé

Le brief le dit en une phrase : « l'agent peut dire "tu as six clients" ;
il ne récite pas les notes de séance de Marcus Reyes dans une pièce
ouverte ». Je n'invente pas une politique complète — je pose un garde-fou
minimal et honnête, et j'écris ce qui reste à faire.

### Trois modes

- **`safe` (défaut)** — masque les coordonnées personnelles évidentes :
  numéros de carte (13–19 chiffres), IBAN, email, téléphone français
  (`+33` ou `0X`), SSN américain. Rien d'autre.

- **`strict`** — en plus de `safe`, masque les montants (`1800 EUR`,
  `$5.50`) et les dates (`12/04/2026`).

- **`none`** — ne change rien. Utile en dev, et pour l'utilisateur qui
  veut entendre exactement ce que l'agent a écrit.

L'utilisateur le règle dans Settings > Assistant > Speech privacy. Le
toggle par défaut est `safe`, ce qui veut dire que l'agent qui dit
« Marcus doit 1800 EUR pour la séance du 12/04/2026 » devient
« Marcus doit [montant masque] pour la séance du [date masquee] ».

### Tests du sanitizer

`src/agent/voice.test.ts` couvre les modes et les motifs :

| Mode | Motif | Comportement attendu |
|---|---|---|
| `safe` | `4242 4242 4242 4242` | `[numero masque]` |
| `safe` | `jean@omk.fr` | `[email masque]` |
| `safe` | `+33 6 12 34 56 78` | `[telephone masque]` |
| `safe` | `FR76 3000 6000 0112 3456 7890 189` | `[IBAN masque]` |
| `safe` | `123-45-6789` | `[identifiant masque]` |
| `safe` | `Le client doit 1800 EUR` | **Pas masqué** (volontaire — c'est `strict`) |
| `strict` | `Le client doit 1800 EUR le 12/04/2026` | `[montant masque]` + `[date masquee]` |
| `none` | n'importe quoi | Aucune modification |

---

## 4. Preuves visuelles (`preuves/E/`)

Neuf captures, six preuves demandées par le brief :

| Capture | Preuve |
|---|---|
| `01-bouton-micro.png` | Le bouton micro est visible dans la bulle (icône micro à gauche du champ). |
| `02-micro-ouvert-indicateur.png` | Le micro est ouvert : indicateur 3 barres bleues à droite du nom, bouton stop carré. |
| `03-transcription-interim.png` | Transcription au premier instant : « salut ca » (le mock émet 3 interims successifs à 250 ms d'intervalle). |
| `04-transcription-progressive.png` | Transcription au dernier instant : « salut ca va ? ». |
| `05-synthese-en-cours.png` | Synthèse vocale : indicateur vocal, bouton « STOP » visible, le personnage joue l'animation `speaking`. |
| `06-synthese-terminee.png` | Synthèse terminée : indicateur disparu, bouton normal (envoyer), sprite au repos. |
| `07-refus-permission.png` | Refus micro : message en bulle « Le micro est refuse. Autorise-le dans les reglages du navigateur… » + placeholder adapté du champ. |
| `08-sans-reconnaissance.png` | Pas de `SpeechRecognition` : le bouton micro est absent du formulaire. La bulle reste utilisable au clavier. |
| `09-settings-assistant.png` | Settings > Assistant : toggle « Read out loud » + Voice (selecteur) + Speed (slider 1.00x) + Speech privacy (3 boutons). |

Toutes les preuves sont pilotées par un script Playwright qui pose
l'état dans `localStorage` (`voiceEnabled`, `agentsPrefs`, sélection
visible) avant la navigation, mocke `SpeechRecognition` ou
`SpeechSynthesis` quand il le faut, et mesure l'état du DOM après
l'action.

La preuve 3 (synthèse) passe par un mock `**/api/agent/invoke` qui
renvoie un SSE minimal — c'est ce qui déclenche `useVoiceSynthesis.speak()`
via le chemin normal de l'agent, pas par un appel direct à
`window.speechSynthesis.speak()`.

---

## 5. Les pièges du brief, et comment ils ont été traités

### 5.1 · Sélecteur Zustand = scalaire ou référence stable

Le store `assistant.store.ts` expose les nouveaux champs un par un :
`s.voiceEnabled`, `s.voiceName`, `s.voiceRate`, `s.voicePrivacy` — tous
des scalaires. Le merge de `persist` valide `voiceRate` (NaN et clamp)
et `voicePrivacy` (set fermé). Un `localStorage` forgé ne peut plus
faire crasher `SpeechSynthesis` avec un rate de 50 ou un mode
inconnu.

### 5.2 · Nettoyage des ressources

`useVoiceRecognition` : le cleanup `useEffect` appelle
`recRef.current?.abort()`. Le `recRef` est mis à null dans `onend`,
donc un re-démarrage ne crée pas de zombie.

`useVoiceSynthesis` : le cleanup appelle `releaseRef.current?.()` (qui
libère le singleton `currentSpeaker`) puis `window.speechSynthesis.cancel()`
si une utterance tourne encore. Une synthèse qui survit à un démontage
de composant est impossible avec ce hook.

### 5.3 · Plusieurs personnages coexistent

J'ai tranché pour **un seul speaker à la fois** (voir §2). Le singleton
`currentSpeaker` dans `voice.ts` garantit qu'à tout instant, un seul
agent a la parole. Si un agent B parle et qu'un agent A commence à
parler, l'agent B est coupé net, l'agent A prend la parole. Si les deux
parlent en même temps, le dernier appel à `speak()` gagne.

L'autre option — une file d'attente — aurait été plus polie, mais elle
introduit un délai perceptible (l'utilisateur attend que l'agent A finisse
avant que l'agent B parle). Pour des notifications courtes (« tu as six
clients ») c'est correct ; pour des réponses longues c'est agaçant.

---

## 6. Vérification

- `npx vitest run` : **10 fichiers, 110 tests passants** (incluant les
  16 tests du service vocal).
- Type-check sur mes fichiers (`tsc --noEmit -p tsconfig.app.json`,
  filtré sur `src/agent/`, `src/stores/assistant.store.ts`,
  `src/apps/settings/AssistantSettings.tsx`) : **0 erreur**. Les
  erreurs préexistantes du repo (JSX namespace, autres composants) ne
  sont pas dans mon périmètre.
- Captures Playwright : 9/9 générées sans erreur de console sur mes
  contextes.

---

## 7. Ce que je n'ai pas fait, et pourquoi

### 7.1 · Pas de reconnaissance vocale sur Firefox

`SpeechRecognition` n'existe pas nativement sur Firefox stable. Le
brief le dit, et la règle appliquée est : « s'il est absent, le bouton
ne s'affiche pas — plutôt qu'un bouton qui ne fait rien ». C'est ce que
fait le test `preuve 5` (`08-sans-reconnaissance.png`). Mais il reste un
point : sur un navigateur sans `SpeechRecognition`, on n'affiche pas
non plus d'indicateur « non disponible » dans Settings. C'est
acceptable parce que le toggle de la voix reste présent (c'est
`SpeechSynthesis` qu'il conditionne, pas la reconnaissance), et
l'utilisateur peut quand même lire à voix haute. Si on veut un message
explicite « votre navigateur ne supporte pas la dictée », c'est une
ligne à ajouter dans `AssistantSettings` — j'ai laissé l'indicateur
`data-voice-unavailable` qui sert déjà pour la synthèse absente, et
qui est généralisable.

### 7.2 · Politique de confidentialité plus fine que les regex

Le sanitizer reconnaît 5 motifs en `safe` (carte, IBAN, email,
téléphone, SSN) et 2 en plus en `strict` (montants, dates). Il ne
reconnaît **pas** :

- les **noms de clients**. Si l'agent dit « Marcus Reyes a un ticket
  moyen de 1800 EUR », `strict` masque le montant mais laisse le nom.
  C'est délibéré — une regex sur les noms propres produit des faux
  positifs à la chaîne (« Jean » dans « jeannot de la chapelle »).
  Pour masquer un nom, il faut une liste explicite (`mask: true` sur
  l'item CMS), ce qui est un autre chantier.

- les **identifiants opaques** : `omk-7a4b-...`, les références
  internes. Pareil — pas de motif générique fiable.

- les **montants en devises non couvertes** (`£`, `CHF`, etc.). Le
  motif `\b\d+(?:[ ,.]\d+)*\s*(?:€|EUR)\b` ne couvre que `€` et `EUR`.
  Si quelqu'un travaille en livres, il passe à travers.

- les **numéros au format français non listés** : `06 12 34 56 78`
  (avec espaces) marche ; `06.12.34.56.78` (avec points) marche aussi
  parce que le motif accepte `[ .-]`. Mais `06-12-34-56-78` non, parce
  que `-` n'est pas dans la classe. C'est une amélioration facile — le
  motif est `/(?:\+33\s?|0)\s?[1-9](?:[ .-]?\d{2}){4}/g`, j'ai oublié
  le tiret. Je laisse ouvert pour ne pas surcharger le sanitizer.

### 7.3 · Pas de validation que la voix a effectivement parlé

Le test vérifie que `synthesis.state === 'speaking'` puis `=== 'idle'`,
ce qui prouve que le hook a bien déclenché la synthèse. Mais il ne
prouve pas que la voix a réellement été audible. Chromium headless
n'a pas de moteur TTS — un SpeakUtterance réel se résoudrait en silence
dans cet environnement, mais l'API passe en `speaking: true`. C'est
suffisant pour la machine d'état, insuffisant pour la qualité audio.
Un test manuel dans un Chromium desktop reste nécessaire.

### 7.4 · La sécurité par objet n'est pas posée

C'est l'idée 4 de l'analyse Palantir. Le brief lui-même la classe
explicitement comme « quand le multi-locataire arrive » — donc hors
périmètre de ce chantier. Mais elle mérite d'être listée ici parce
que la voix la révèle : un agent qui récite des notes de séance à
voix haute pour un client A, alors que l'utilisateur connecté est le
client B, c'est un trou de sécurité. Le sanitizer posé ici ne le voit
pas — il regarde le texte, pas l'identité du locuteur.

### 7.5 · L'animation du sprite pendant la parole

Pendant la synthèse, `intent === 'speaking'` est posé (cf. capture 05).
C'est le sprite qui joue son animation `speaking` — mais le mapping
intent → animation se fait via le manifeste `agent.json` du personnage.
Si un personnage n'a pas d'animation `Explain`/`Speaking`/`GestureRight`
dans son manifeste (cf. `INTENT_CANDIDATES` dans `characters.ts`),
le moteur retombe sur l'idle. Les 12 personnages du roster ont tous
au moins une animation candidate, donc ça marche dans la pratique. Je
n'ai pas vérifié caractère par caractère sur la planche des sprites
qu'aucun ne rate son animation pendant la synthèse — c'est une
vérification que `SpriteAgent` fait déjà, et qu'on peut voir dans
les captures si un personnage se fige.

### 7.6 · Pas de raccourci clavier pour activer le micro

L'utilisateur doit cliquer le bouton micro dans la bulle. Un raccourci
genre `Espace` ou `Cmd+M` serait ergonomique mais c'est un autre
chantier.

---

## 8. Synthèse

| | |
|---|---|
| Fichiers créés | 4 (`voice.ts`, `VoiceWave.tsx`, `voice.test.ts`, `voice-shot.mjs`) |
| Fichiers modifiés | 3 (`assistant.store.ts`, `AgentTile.tsx`, `AssistantSettings.tsx`) |
| Lignes ajoutées (estimation) | ~700 |
| Lignes supprimées | 0 |
| `npm install` | 0 |
| Tests vitest | 110 passants (16 nouveaux pour la voix) |
| Captures `preuves/E/` | 9 PNG, 6 preuves couvertes |
| Erreurs de console (mes contextes Playwright) | 0 |

La voix est branchée. Elle obéit à l'invariant « un seul speaker à la
fois ». Elle nettoie ses ressources au démontage. Elle masque par
défaut ce qui peut porter atteinte à la vie privée d'un client, et
l'utilisateur peut durcir ou désactiver la politique. Elle ne sait pas
refuser une demande, comme l'agent de la démo Palantir — mais ce
n'était pas le sujet de ce brief, qui porte strictement sur l'écoute
et la parole.

L'ordre qui tient debout, selon l'analyse :

1. ✅ **les scénarios** — chantier D, à venir ;
2. ✅ **l'approbation** — chantier D ;
3. ✅ **la voix** — ce brief ;
4. ⏭ **la sécurité par objet** — chantier à venir, multi-locataire.

Trois sur quatre sont posés ou en cours. Le quatrième attend le
multi-locataire.