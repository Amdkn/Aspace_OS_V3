# LINKS — wf0-spock dossier = SOMMAIRE vers la source de vérité

> Le GO Spock, ses amendments, ses ratifications vivent à **plat** dans
> `decisions/`. Ce dossier `wf0-spock/` n'est PAS un doublon — c'est un
> **SOMMAIRE** qui pointe vers la source canonique (D4 append-only).
> Le seul fichier writable ici est `STATE.json` (état de l'airlock courant).
>
> M3 lit `STATE.json` pour décider, pointe vers `source_decisions` pour le pourquoi.

## Sources canoniques (lue seule ici)

- **GO source** : `agent-os/citadel/decisions/GO_SPOCK_UNIQUE.md`
- **Decision de lancement** : `agent-os/citadel/decisions/2026-07-06_fenetre_fable_go_spock_lance.json`
- **Amendment perpétuel → 3 ans** : wargame 15 + 26, gravé dans `STATE.json`

## Gate decision (consommé par wf1_runner.ps1)

`wf1_runner.ps1` lit `decisions/enable_wf1.flag` (présent = OK, absent = kill-switch Spock).
Ce flag est posé/retiré par `/go-spock` et `/kill-wf1` (A0-Amodei arbitre, A+ ratifie).

## Cycle WF0 → WF1 → WF2 → WF3

- **WF0** = A0-Amodei (cadre, ne touche pas)
- **WF1** = Morty (exécution, ce runner)
- **WF2** = Picard (consommateur L2)
- **WF3** = MiroFish (sims prédictives)

**WF0 ne s'exécute PAS** — c'est une chaîne de POUVOIR, pas un worker. Le dossier `wf0-spock/` est la **mémoire de l'airlock**, pas un runner.

## Lien vers ADR-AIRLOCK-001

3 airlocks : Beth (capacité, ici `capacity_green`) · Cerritos/Mission Control (statuts Plane) · Morty (décision). Spock **n'est PAS une airlock** — Spock est la **cascade GO** qui active/désactive le système (le enable_wf1.flag est le seul fichier qui ouvre/ferme l'airlock à la racine).

**Tri par réversibilité (loi wargame 23) :**
- Suppression de ce README = aucune réversibilité (re-créable)
- Suppression de STATE.json = ALERTE (le runner ne sait plus l'état de l'airlock)
- Suppression de `decisions/enable_wf1.flag` = KILL-SWITCH (wf1_runner exit immédiat)

D7 : aucun de ces fichiers ne se touche sans audit-échantillon Fable.
