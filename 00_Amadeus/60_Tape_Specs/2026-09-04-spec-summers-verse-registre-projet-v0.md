---
id: spec-summers-verse-registre-projet-v0
date: 2026-09-04
layer: L1
status: active
type: ruban-phi
target: 30_Business_OS/00_Summers_Verse/projects/coach-os-app
framework: Summers Verse — registre projet + verifier
pattern_source:
  - 30_Business_OS/00_Summers_Verse/00_Registre/verifier.py
  - 20_Life_OS/25_GTD_Cerritos/verifier.py
version: v0
---

# Ruban φ — Summers Verse : registre projet coach-os-app + verifier étendu

## Objectif

Dans `30_Business_OS/00_Summers_Verse/projects/coach-os-app/`, créer :

1. `registre.json` — enregistrement du projet :
   - `id` : identifiant projet (non vide) — `coach-os-app`
   - `nom` : nom lisible — `Coach OS App`
   - `statut` : `actif` | `pause` | `clos` — valeur initiale `actif`
   - `owners` : liste des propriétaires
   - `liens` : chemins relatifs vers `gtd/` (et README.md)
2. `verify_projet.py` — verifier étendu qui :
   1. charge `registre.json` (situé à côté du script) ;
   2. exige `id` non vide (chaîne, stripped non vide) ;
   3. exige `statut` ∈ {`actif`, `pause`, `clos`} ;
   4. affiche `PROJET_OK` et sort rc=0 si tout est bon, `PROJET_KO` et rc=1 sinon (fichier absent, JSON invalide, champs manquants/invalides).

## Spec autonome

Aucune clarification humaine requise. Valeurs par défaut posées par le ruban (id=`coach-os-app`, statut initial=`actif`).

## Tests d'acceptation

- Test positif : `python verify_projet.py` → stdout contient `PROJET_OK`, rc=0.
- Test négatif : `registre.json` renommé en `registre.json.bak` → stdout contient `PROJET_KO`, rc=1. (Restaurer ensuite.)

## Défaire

Supprimer `registre.json` et `verify_projet.py` dans le dossier cible.
