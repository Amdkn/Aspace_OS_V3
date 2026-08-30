# datasets — les échecs réels, pas des cas fabriqués

> GEPA « lit les traces d'exécution pour comprendre **pourquoi** les choses
> échouent » plutôt que de constater l'échec. Sans traces, pas d'évolution :
> ce dossier les porte.

## Ce qu'il y a dedans

[`echecs_instruments.jsonl`](echecs_instruments.jsonl) — **16 défauts mesurés
le 2026-08-30**, chacun avec sa mesure fausse, sa mesure vraie, sa cause, son
correctif appliqué, et **par quoi il aurait pu être détecté plus tôt**.

Ce ne sont pas des cas d'école : ce sont les instruments qui ont menti pendant
la construction de ce dossier même. E11 est la porte G2 qui validait un script
ne compilant pas ; E14, un scan de secrets qui accusait le mauvais fichier.

## Les six familles qui s'en dégagent

| Famille | Cas | Ce qui la caractérise |
|---|---:|---|
| **Sonde aveugle** | E01, E03, E04 | L'API interrogée ne voit pas ce qu'on croit qu'elle voit |
| **Motif non normalisé** | E05, E10, E16 | La sonde cherche une forme, le texte en porte une autre |
| **Total qui n'additionne pas** | E02, E06 | On somme des valeurs qui ne se somment pas |
| **Extraction trop large / stricte** | E09, E15 | Le filtre attrape du bruit, ou rate l'évident |
| **Sortie perdue** | E07 | La mesure est juste et n'arrive jamais |
| **Porte qui valide une promesse** | E08, E11 | On vérifie la présence d'un mot, pas le fait |

**La plus dangereuse est E04** — une sonde qui *confirme* l'hypothèse attendue.
Une sonde muette éveille la méfiance ; une sonde qui va dans le sens espéré la
désarme.

## Comment ce jeu s'utilise

```bash
python C:/Users/amado/ASpace_OS_V3/90-self-evolution/datasets/valider.py
```

Chaque entrée porte un champ `detectable_par` : c'est la **contre-mesure** qui
aurait suffi. Un correctif proposé par un cycle d'évolution ne vaut que s'il
fait passer les cas de la famille visée sans casser les autres — c'est la
porte de validation du dépôt Nous, appliquée à des données réelles.

## Ce que ce jeu ne permet pas encore

**Il ne mesure pas un taux de succès sur des tâches.** Les 16 entrées décrivent
des défauts d'instrument, pas des exécutions notées. Un cycle GEPA complet
demanderait des tâches avec un résultat attendu ; **elles n'existent pas ici**,
et aucune skill de ce dossier n'est issue d'une optimisation automatique.

Ce jeu sert donc à **une chose précise** : vérifier qu'un changement de sonde
ne réintroduit pas un défaut déjà payé.
