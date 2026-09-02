# Jerry Business Pulse — v0

Pulse B1 du Business OS (A'Space OS V3, 30_Business_OS). Quatre variantes Jerry,
chacune un domaine business :

| Variante | Dossier | Domaine |
|---|---|---|
| Jerry Prime | `01_Prime/` | business classique : revenus, clients, offres |
| Jerry Bio | `02_Bio/` | bio/health : protocoles, mesures, réglementaire |
| Jerry Nexus | `03_Nexus/` | tech/plateforme : produit, utilisateurs, API |
| Jerry Solarpunk | `04_Solarpunk/` | solaire/durabilité : énergie, impact, communauté |

Registre central : `00_Registre/registre.json`.

## Verifier la structure

```bash
python C:/Users/amado/ASpace_OS_V3/30_Business_OS/00_Jerry_Business_Pulse/verifier.py
```

`PULSE_OK` + rc=0 si tout passe, sinon `PULSE_KO` + rc=1.

## Contraintes v0

- Squelette fonctionnel : aucune donnée business réelle.
- Python stdlib uniquement, aucune dépendance pip.
- Contenus en français, ASCII sans accents.
