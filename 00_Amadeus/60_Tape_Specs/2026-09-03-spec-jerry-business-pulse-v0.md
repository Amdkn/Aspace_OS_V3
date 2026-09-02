# Spec — Jerry Business Pulse v0 : initialiser 00_Jerry_Business_Pulse fonctionnel

- Rôle : Spec (ruban φ), L2 Buzz Core — pour 30_Business_OS (B1).
- Date : 2026-09-03 · Statut : executable, aucune question requise par le constructeur.
- Portée : création du dossier B1 `C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/` (actuellement VIDE — vérifier avant de commencer) et de ses 4 variantes Jerry.

## Contexte

Jerry Business Pulse est le pulse B1 du Business OS. Quatre variantes Jerry :
Prime (business classique), Bio (bio/health), Nexus (tech/plateforme),
Solarpunk (solaire/durabilité). v0 = squelette fonctionnel minimal : structure
de dossiers, README par variante, registre central, et un script de vérification
exécutable. Aucune dépendance externe, Python stdlib uniquement.

## Quoi batir — OU (chemins exacts)

Base : `C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/`

1. `README.md` — présentation du pulse B1, les 4 variantes, comment lancer la vérification.
2. `00_Registre/registre.json` — registre central :
   - `version: "v0"`, `date_init: "2026-09-03"`
   - `variantes`: liste ordonnée des 4 ids `prime`, `bio`, `nexus`, `solarpunk`
   - chaque variante: `{"id": ..., "nom": "Jerry <Nom>", "dossier": "01_Prime|02_Bio|03_Nexus|04_Solarpunk", "cree": "2026-09-03"}`
3. Par variante, dossier + fichiers (mêmes 4 fichiers, contenu adapté au domaine) :
   - `01_Prime/README.md` (business classique : revenus, clients, offres)
   - `02_Bio/README.md` (bio/health : protocoles, mesures, réglementaire)
   - `03_Nexus/README.md` (tech/plateforme : produit, utilisateurs, API)
   - `04_Solarpunk/README.md` (solaire/durabilité : énergie, impact, communauté)
   - Chaque README variante contient au minimum : titre `# Jerry <Nom>`, section `## Etat` avec `statut: v0-initialise`, section `## Prochaines etapes` (3 puces minimum).
4. `verifier.py` — script stdlib qui vérifie TOUTE la structure ci-dessus
   (dossiers, registre.json valide, 4 variantes présentes, README non vides,
   `statut: v0-initialise` présent dans chaque README) et affiche
   `PULSE_OK` + rc=0 si tout passe, sinon `PULSE_KO` + rc=1.

## Critere d'acceptation

- [ ] `ls C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/` liste exactement : `00_Registre/`, `01_Prime/`, `02_Bio/`, `03_Nexus/`, `04_Solarpunk/`, `README.md`, `verifier.py`
- [ ] `python -c "import json;d=json.load(open(r'C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/00_Registre/registre.json'));assert [v['id'] for v in d['variantes']]==['prime','bio','nexus','solarpunk']"` retourne rc=0
- [ ] `for d in 01_Prime 02_Bio 03_Nexus 04_Solarpunk; do test -s "C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/$d/README.md" || exit 1; done` retourne rc=0
- [ ] `grep -c "statut: v0-initialise" C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/0*/README.md` retourne 4 lignes de valeur >= 1
- [ ] `python C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/verifier.py` affiche `PULSE_OK` et retourne rc=0
- [ ] `ls C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/00_Registre/` contient `registre.json` et rien d'autre

## Contraintes

- Ne pas modifier `10_Tech_OS/kernel/uc.db`.
- Ne rien écrire hors `00_Jerry_Business_Pulse/`.
- v0 = squelette : aucune donnée business réelle, aucune dépendance pip.
- Tous les contenus en français, ASCII sans accents dans les noms de fichiers.
