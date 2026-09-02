---
title: "landing prouvée — site statique OMK 3 personas (correction du ruban 2026-08-02)"
work_id: 5
layer: L2
created: 2026-09-01
remplace: "00_Amadeus/60_Tape_Specs/2026-08-02-landing-omk-trois-personas-en-ligne.md (non modifié, append-only — l'ancien ruban exigeait 'npm run build retourne 0' sur un repo sans npm, cause des 4 échecs de work 5)"
---

## Objectif

Prouver, par des preuves d'environnement exécutables, que la landing statique OMK
« 3 personas » est servie localement et performante. Aucune construction n'est requise :
le repo est du HTML pur, sans npm ni package.json.

Repo du périmètre (vérifié 2026-09-01 par listing de répertoire) :

```
C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/omk-nexus-landing-3-personas
```

Contenu constaté : `index.html`, `david-fractional-coo.html`, `harrison-bdr-agency.html`,
`marcus-coach-c-suite.html` + dossiers `v2/` et `v3/` (mêmes 4 pages en v2 ;
`amara-growth-multi-tenant.html` en v3). Aucun `package.json`, aucun npm — tout critère
exigeant npm est ici invalide par construction.

## Critère d’acceptation

- [ ] CA1 — Serveur local : `python -m http.server` lancé à la racine du repo sert les 4 pages racine ET les 4 pages v2 (index, david-fractional-coo, harrison-bdr-agency, marcus-coach-c-suite) ; chaque URL répond HTTP 200. Preuve : sortie curl (code + URL) des 8 requêtes collée dans le rapport d'exécution.
- [ ] CA2 — Page v3 servie : `v3/amara-growth-multi-tenant.html` répond HTTP 200 sur le même serveur. Preuve : sortie curl.
- [ ] CA3 — Performance : score Lighthouse performance > 90 sur `http://localhost:<port>/index.html` servi localement, mesuré via `npx lighthouse <url> --output=json --output-path=<chemin_preuve>.json --chrome-flags="--headless"` ou équivalent. Preuve : le fichier JSON sauvegardé + la valeur `categories.performance.score` (x100 > 90) extraite et citée dans le rapport.

## Périmètre

Dedans — uniquement le repo listé ci-dessus, en lecture/exécution :

- servir localement les pages HTML (racine, v2/, v3/) ;
- mesurer Lighthouse sur la page index servie localement ;
- produire les preuves (sorties curl, JSON Lighthouse) dans le rapport d'exécution.

Dehors (non requis pour ce work) :

- le quiz, toute interaction utilisateur sur les pages ;
- le DNS, les noms de domaine, la publication en ligne ;
- le déploiement production (Vercel ou autre) ;
- toute modification du contenu ou du design des pages.

## Interdits

- Ne pas toucher aux variables d'environnement de production (aucun `.env` de prod lu ou modifié).
- Ne pas modifier le DNS.
- Ne pas réécrire les HTML existants : le repo est en lecture seule. Exception unique : une correction bloquante (page qui ne charge pas du tout) est permise si elle est justifiée explicitement dans le rapport d'exécution, avec le diff minimal avant/après.
- Ne pas ajouter npm, package.json ou build step au repo — le statut statique est la donnée, pas un défaut.
- Ne pas modifier l'ancien ruban `2026-08-02-landing-omk-trois-personas-en-ligne.md` (append-only).
