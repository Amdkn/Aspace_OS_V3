# Ordre des Couches — Local → WSL → VPS

## Règle d’or
Local conçoit → WSL structure → VPS déploie

## Interdits
- Un doc WSL ne dicte pas la conception Local
- Un doc VPS ne modifie pas la structure WSL

## Obligatoire dans chaque doc
- Layer: Local|WSL|VPS
- Rôle de la couche dans la chaîne
- Dépendances amont/aval
