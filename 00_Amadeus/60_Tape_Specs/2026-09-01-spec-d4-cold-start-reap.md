# Spec — réplication du ruban (test D4 : démarrage à froid + reap)

## Problème mesuré

Le CERTIFICAT_VIVANCE-20260901.md prouve un cycle complet mais pas les deux
conditions D4 restantes : démarrage à froid, reprise d'un worker tué.

## Fichier cible

`10_Tech_OS/kernel/uc.db` (état machine, pas de fichier construit).

## Règle

1. **Démarrage à froid** : `python uc.py submit` sur un ruban neuf, depuis un
   shell vierge, puis cycle complet `claim → predict → review → done` par le
   mécanisme seul (aucun état en mémoire du worker).
2. **Reap** : `claim` avec bail court (60 s), tuer le process sans `review`,
   attendre expiration, `uc.py reap` doit rendre le travail à la file
   (status → pending, claim supprimé, event `reap` horodaté).
3. Re-claim après reap : le work est réclamable, `attempts` incrémenté.

## Mesure de succès

- `uc.py reap` rc 0 ; work retourné en `pending` ; claim = 0 ligne.
- Le work réapparu est re-claimable avec rc 0.
- Les deux cycles portent des events horodatés distincts dans la table `event`.

## Portée

Test de mécanisme uniquement. Aucun artefact applicatif construit.
