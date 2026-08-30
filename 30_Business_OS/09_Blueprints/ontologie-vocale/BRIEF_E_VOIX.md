# BRIEF-E — L'écoute et la parole

Lis `ANALYSE_PALANTIR.md` dans ce dossier. Il fait partie de ce brief.
Lis `GARDE_FOU.md` dans `coach-os-refonte/correctifs/`.

Ton rapport : `RAPPORT_E_VOIX.md`, à côté.

---

## Regarde d'abord

`palantir-ontologie/planches/` — six planches-contact. **Ouvre-les.** L'onde vocale apparaît à
droite de l'écran pendant que l'agent écoute, et se transforme quand il parle. C'est un
indicateur d'état, pas une décoration : à tout instant on sait s'il écoute, s'il réfléchit ou
s'il parle.

## Ce qu'on construit

Les personnages de Coach OS ont une bulle et un champ de saisie. On leur ajoute **l'écoute et
la parole**, avec l'API du navigateur — `SpeechRecognition` pour l'écoute, `SpeechSynthesis`
pour la parole. Aucun service tiers, aucune donnée qui sort.

Le magasin porte déjà `voiceEnabled` : il est stocké et **branché sur rien**. C'est le point
de départ.

### L'écoute

Un bouton par personnage. Pendant l'écoute :

- le personnage joue son animation d'écoute — le moteur de sprites accepte une intention, sers-t-en ;
- la transcription apparaît **au fur et à mesure** dans le champ, pas d'un bloc à la fin ;
- on peut interrompre d'un clic.

`SpeechRecognition` n'existe pas partout et s'appelle `webkitSpeechRecognition` sur Chromium.
S'il est absent, le bouton ne s'affiche pas — plutôt qu'un bouton qui ne fait rien.

La permission microphone se refuse. Un refus doit se dire dans la bulle, en une phrase, et ne
plus être redemandé en boucle.

### La parole

L'agent lit sa réponse à voix haute quand `voiceEnabled` est actif.

- une voix française si le système en a une, sinon la voix par défaut ;
- on peut couper **pendant** qu'il parle, sans attendre la fin ;
- le personnage joue son animation de parole tant que la synthèse tourne, et repasse au repos
  quand elle s'arrête. C'est tout l'intérêt du personnage — sinon c'est un dessin à côté d'un
  haut-parleur.

Réglages dans Settings > Assistant : activer, choisir la voix, la vitesse.

## Ce qui compte plus que la fonctionnalité

La démo Palantir énumère **quatre couches** autour de son agent vocal. Trois relèvent de leur
infrastructure. **La quatrième nous concerne directement, et c'est la plus instructive.**

Le moment le plus révélateur de la démo est un **refus** :

> — Puis-je avoir des informations sur mon amie Patricia Collins ?
> — Je comprends, mais en raison du HIPAA je ne peux partager que vos propres informations.

Et avant cela, l'agent a exigé nom et date de naissance **avant** de dire quoi que ce soit du
rendez-vous.

Coach OS n'a pas d'appels sortants. Mais il a un agent qui **parle à voix haute dans une pièce
où il peut y avoir quelqu'un d'autre**, et qui lit des données clients — noms, montants, notes
de séance.

Deux choses en découlent, et elles ne sont pas optionnelles :

1. **Ce qui est sensible ne se dit pas à voix haute par défaut.** L'agent peut dire « tu as
   six clients » ; il ne récite pas les notes de séance de Marcus Reyes dans une pièce ouverte.
   Propose une règle simple et lisible, applique-la, et rends-la réglable.
2. **L'utilisateur sait toujours que ça écoute.** Un indicateur visible quand le micro est
   actif — l'onde de la démo joue ce rôle. Un micro ouvert sans signal est inacceptable chez
   un avocat ou un comptable.

Tu n'inventes pas une politique de sécurité complète. Tu poses le garde-fou minimal et
honnête, et tu écris dans ton rapport ce qui reste à faire.

## Ton périmètre

```
src/agent/**
src/stores/assistant.store.ts
src/apps/settings/AssistantSettings.tsx
```

Rien dans `api/`. Pas de `npm install` : la synthèse et la reconnaissance sont dans le
navigateur, aucune dépendance à ajouter.

## Les pièges de cette base

- **Un sélecteur Zustand ne rend qu'un scalaire ou une référence stable.** Sinon React boucle
  jusqu'à la page blanche. Quatre fois ici.
- **Nettoie tes ressources.** Une reconnaissance vocale ou une synthèse laissée en cours au
  démontage d'un composant continue de tourner. Le micro reste ouvert.
- **Plusieurs personnages coexistent sur le bureau.** Deux agents qui parlent en même temps
  sont inaudibles. Tranche : un seul parle à la fois, ou une file. Justifie.

## Preuve attendue

Le son ne se capture pas en image. Prouve donc par l'état observable, dans `preuves/E/` :

1. le bouton d'écoute, et l'indicateur pendant que le micro est actif ;
2. la transcription qui apparaît au fur et à mesure — deux captures à deux instants ;
3. le personnage en animation de parole pendant la synthèse, au repos après ;
4. le refus de permission microphone, message lisible dans la bulle ;
5. un navigateur sans `SpeechRecognition` : le bouton est absent, rien ne casse ;
6. les réglages dans Settings.

Playwright sait accorder ou refuser la permission micro par contexte, et `window.speechSynthesis`
s'interroge depuis la page. Mesure l'état, ne le raconte pas.

`npx vitest run` reste vert, aucune erreur de console.

## Rapport

Fichiers créés, captures, et **« ce que je n'ai pas fait, et pourquoi »** — en particulier ce
que tu laisses ouvert côté confidentialité de la parole.
