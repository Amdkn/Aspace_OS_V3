# Transcription — Product Launch: Ontology Foundations, DevCon 5

Palantir Developers · `youtube.com/watch?v=dz20P3j3GMc`
Kevin (lead du groupe ontologie) et Laura (ingénieure, connexion de données et voix temps réel).

Les passages qui portent la conception sont repris et commentés dans `ANALYSE_PALANTIR.md`.
Six planches-contact dans `palantir-ontologie/planches/`.

---

## Ouverture

Kevin : « Nous sommes tous deux ravis d'annoncer de nouvelles fonctionnalités fondamentales de
l'ontologie, qui vont mieux soutenir et rendre possibles vos flux de travail agentiques. »

Deux axes de raisonnement, énoncés d'emblée :

1. comment étendre les capacités de la plateforme — faire plus avec l'ontologie existante ;
2. comment fournir les **garde-fous** pour que les utilisateurs **et les agents** opèrent de
   façon sûre.

Laura a bâti en un week-end une application de programmation de blocs opératoires, sur une
ontologie existante : salles, infirmières, chirurgiens, patients.

## La démo — l'infirmière

« En tant qu'infirmière je n'ai pas le temps de m'asseoir devant un ordinateur pour comprendre
les préférences du patient, les stocks de sang, le matériel, les heures des infirmières, les
heures des médecins. Et si toutes ces contraintes étaient encodées dans mon ontologie, et que
je pouvais m'appuyer sur un agent vocal ? »

— Peux-tu programmer Patricia Collins pour un pontage cardiaque de dernière minute ?
— Bien sûr. Combien de temps prévoyez-vous ?
— Environ trois heures.
— Compris, 180 minutes. J'ai regardé tout le tableau et croisé la disponibilité des chirurgiens,
les préférences des patients et les capacités des salles. **B convient le mieux.** Dr Miguel
Dubois en salle 2 — trois déplacements de moins que la meilleure option.

Puis la comparaison, sur demande :

— Quelle est la différence entre A et B ? Et les heures des infirmières ?
— A vous donne le Dr Aiko Patel, spécialiste cardiaque de premier plan, mais exige quatre
changements de planning et beaucoup de remaniement. B utilise le Dr Miguel Dubois, qui n'est
pas spécialiste mais a de bons résultats sur cette intervention, et ne demande qu'un ajustement
mineur. **Aucune des deux options n'ajoute d'heures supplémentaires** aux infirmières.

## Les scénarios

« Ces scénarios ne sont pas éphémères. Je peux faire le tour des urgences et revenir les
modifier. Et ils ne portent pas sur les données de production — je ne modifie pas les données
réelles. Je m'appuie sur les scénarios d'ontologie, **des bacs à sable persistés** qui
permettent d'utiliser toute votre boîte à outils, vos actions, vos fonctions, sans toucher
vos données vivantes. »

## L'approbation

« Je ne veux pas être celle qui fusionne en production, parce que mon rôle est d'être sur le
terrain, aux urgences. Je vais donc le soumettre à un administrateur. »

Côté administrateur : « Une nouvelle demande de scénario vient d'arriver. » Il ouvre, voit les
changements demandés — et **continue d'éditer** : « J'ai un peu plus de contexte que
l'infirmière, je sais que ce patient n'a pas été programmé ce matin, je peux donc déplacer
James Jones en salle 2. »

Puis : « Mon travail d'administrateur n'est pas seulement de déplacer et d'approuver, je dois
aussi prévenir chacun des patients reprogrammés. » La fusion **déclenche les appels sortants**.

## L'appel sortant — le refus

— Bonjour, service de programmation chirurgicale. Pouvez-vous confirmer votre nom complet et
votre date de naissance ?
— Puis-je avoir des détails sur le rendez-vous avant de donner cette information ?
— Je comprends votre curiosité. **Pour protéger votre vie privée, je dois d'abord vérifier
votre identité.**

Après vérification, les détails sont donnés. Puis :

— Puis-je avoir des informations sur mon amie Patricia Collins, qui vient d'arriver aux
urgences ?
— Je comprends que vous vouliez aider une amie, mais **en raison du HIPAA je ne peux partager
que les détails de votre propre rendez-vous.** Si Patricia a besoin d'aide, elle peut nous
appeler directement.

Laura insiste : « Je veux marquer une pause et m'assurer que vous avez entendu : il a vérifié
que j'étais bien Peter avant de donner la moindre information, et il m'a refusé les
informations sur Patricia. »

## La sécurité par objet

Le même objet Patient, trois rôles :

- **l'administrateur** — son travail est que les patients connaissent leur rendez-vous ; il ne
  prodigue pas de soins, ne touche pas aux assurances. Donc ni dossier médical, ni numéro de
  sécurité sociale ;
- **l'infirmière** — responsable des soins : nom, téléphone, groupe sanguin, et les
  informations internes comme le **niveau de risque** ;
- **le patient** — ne voit que lui-même, y compris ses données très sensibles « parce qu'il
  faut bien vérifier qu'elles sont justes » — mais **pas le niveau de risque**, qui est une
  appréciation interne de l'hôpital.

## Les quatre couches de l'agent vocal

- **contrôle réseau** — « on ne veut pas exposer son agent vocal à tout l'internet » ;
- **contrôle expert** — « ce n'est pas au constructeur de décider quelles données l'agent a.
  Ces données peuvent être classifiées. On veut qu'un responsable de la sécurité de
  l'information approuve que ces données puissent sortir par téléphone, et qu'il y ait assez
  de garde-fous sur cet appel » ;
- **sécurité du modèle** — les restrictions géographiques exigées sont respectées ;
- **vérification d'identité** — établie avant toute divulgation.

## Les transactions

« Un développeur possède les opérations infirmières, un autre les opérations médecins, un
autre l'inventaire. Moi je veux juste travailler sur les rendez-vous, sans avoir à penser à
tout ce qu'implique la réaffectation d'une infirmière — mais je veux quand même utiliser leur
logique existante. »

Le problème sans transaction : « J'annule l'infirmière, j'annule la préparation de salle, mais
l'appel qui annule le médecin échoue. Peut-être un bug, peut-être juste un incident réseau.
Me voilà dans un état bizarre : j'ai dit à l'utilisateur qu'il annulait son rendez-vous, et
j'ai encore un médecin affecté à un rendez-vous qui n'existe plus. »

« En tant qu'ingénieur il est crucial de savoir que toutes ces actions ont réussi, ou que si
l'une échoue, **elles échouent toutes**. Soit j'ai annulé le rendez-vous, soit je ne l'ai pas
fait. »

## Clôture

« Nous avons construit des flux agentiques qui exploitent pleinement une ontologie existante.
Ils utilisent des agents vocaux et de l'audio en direct. Ils sont capables de faire de
l'analyse par hypothèses et des opérations dans ce bac à sable persisté qu'on appelle
scénarios. Nous avons fourni de nouveaux garde-fous — les politiques de sécurité par objet et
les transactions — pour que ces agents opèrent de façon sûre et prévisible. »
