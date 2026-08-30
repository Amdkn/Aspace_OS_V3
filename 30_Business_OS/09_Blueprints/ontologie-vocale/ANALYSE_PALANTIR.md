# Ce que dit Palantir — Ontology Foundations, DevCon 5

Source : `youtube.com/watch?v=dz20P3j3GMc` · Kevin (lead groupe ontologie) et Laura
(ingénieure, connexion de données et voix temps réel). Transcription intégrale à côté :
`transcription-palantir.md`. Planches-contact dans `palantir-ontologie/planches/`.

---

## La démo, en une phrase

Une infirmière aux urgences demande **à la voix** de programmer une opération. L'agent lit
l'ontologie, propose trois scénarios, en discute, puis l'infirmière **soumet à un
administrateur** qui arbitre et fusionne — et la fusion déclenche des **appels sortants** aux
patients déplacés.

Ce n'est pas une démo de chatbot. C'est une démo de **gouvernance d'agent**.

## Quatre idées, et ce qu'elles valent pour Coach OS

### 1 · Les scénarios — un bac à sable persistant

> « Ces scénarios ne sont pas éphémères. Je peux faire le tour des urgences et revenir les
> modifier. Et ils ne touchent pas les données de production. »

L'agent travaille dans un **bac à sable qui a toute la boîte à outils** — les mêmes actions,
les mêmes fonctions — mais qui n'écrit pas dans les données réelles. On itère, on compare, et
seule la fusion est un acte.

**Pour nous, c'est le manque le plus criant.** Aujourd'hui les cinq outils de Coach OS
agissent immédiatement : `changerTheme` change le thème, point. Un agent qui se trompe a déjà
agi. Et l'audit P3 vient de montrer qu'un contenu peut lui donner des ordres — un agent
détourné qui agit dans un bac à sable ne casse rien.

### 2 · L'approbation — celui qui propose n'est pas celui qui engage

> « Je ne veux pas être celle qui fusionne en production, parce que mon rôle est d'être sur le
> terrain. »

Le rôle qui a le contexte propose ; le rôle qui a l'autorité arbitre. Et l'administrateur
**continue d'éditer le scénario** avant de fusionner — il n'approuve pas en bloc.

Chez Mark, c'est le même geste : *« Yes or no on the queue. Ship or kill. Move on. »* La page
People / Agents de Coach OS l'annonce déjà — « You approve in 10 min ». Elle le raconte, elle
ne le fait pas.

### 3 · Les transactions — tout ou rien

> « J'annule l'infirmière, j'annule la préparation de salle, mais l'appel qui annule le
> médecin échoue. Maintenant j'ai un médecin affecté à un rendez-vous qui n'existe plus. »

Une action d'agent enchaîne plusieurs écritures. Sans transaction, un échec au milieu laisse
un état incohérent que personne n'a voulu.

Coach OS a exactement ce défaut en germe : `allerASection` ouvre l'app **puis** clique la
section. Si le clic échoue, l'app reste ouverte sur autre chose et l'outil rend une erreur —
l'utilisateur voit une fenêtre qu'il n'a pas demandée.

### 4 · La sécurité par objet — le même objet, trois vues

Le même objet Patient est vu différemment par trois rôles : l'administrateur voit les
coordonnées mais pas le dossier médical ni le numéro de sécurité sociale ; l'infirmière voit
le groupe sanguin et le niveau de risque ; le patient voit tout de lui-même, **sauf** le
niveau de risque, qui est une appréciation interne de l'hôpital.

C'est exactement la question que le pentest a laissée ouverte pour le multi-locataire. Et la
réponse de Palantir n'est pas « une base par client » : c'est **une politique par type
d'objet, par propriété, par ligne**.

## Les quatre couches autour de l'agent vocal

Elles sont énumérées explicitement, et elles sont transposables telles quelles :

| couche | ce que ça veut dire |
|---|---|
| **contrôle réseau** | « on ne veut pas exposer son agent vocal à tout l'internet » |
| **contrôle expert** | ce n'est pas au constructeur de décider quelles données l'agent peut dire ; un responsable sécurité approuve |
| **sécurité du modèle** | les restrictions géographiques du modèle sont respectées |
| **vérification d'identité** | l'agent a exigé nom et date de naissance **avant** de parler du rendez-vous |

Le moment le plus instructif de la démo est un **refus** : *« Puis-je avoir des informations
sur mon amie Patricia Collins ? »* — *« Je comprends, mais en raison du HIPAA je ne peux
partager que vos propres informations. »*

Un agent vocal qui ne sait pas refuser n'est pas déployable chez un avocat ou un comptable.

## Ce que je retiens pour la suite

L'écoute et la parole que tu demandes ne sont pas une fonctionnalité isolée. Dans cette démo,
la voix est **le moyen**, et l'ontologie plus la gouvernance sont **la substance**. Un agent
vocal branché sur des outils qui agissent immédiatement, sans scénario ni approbation, serait
plus dangereux qu'utile — surtout après ce que le pentest vient de trouver.

L'ordre qui tient debout :

1. **les scénarios** — l'agent propose, il n'agit plus directement ;
2. **l'approbation** — la file où l'on tranche en dix minutes, réellement ;
3. **la voix** — écoute et parole, une fois qu'il y a quelque chose de sûr à commander ;
4. **la sécurité par objet** — quand le multi-locataire arrive.
