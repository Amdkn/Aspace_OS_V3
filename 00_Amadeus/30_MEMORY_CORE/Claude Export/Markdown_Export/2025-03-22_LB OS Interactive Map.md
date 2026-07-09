# LB OS Interactive Map

**Created:** 2025-03-22 06:34:53

---

## Human

<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LB OS - Interactive Map</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f9f9fb;
    }

    h1 {
      text-align: center;
      padding: 20px;
    }

    #map {
      position: relative;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
    }

    .node {
      position: absolute;
      padding: 10px 20px;
      border-radius: 10px;
      background-color: #fff;
      border: 2px solid #ddd;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      transition: transform 0.2s ease;
      cursor: pointer;
    }

    .node:hover {
      transform: scale(1.05);
      z-index: 10;
    }

    .tooltip {
      display: none;
      position: absolute;
      background: #333;
      color: white;
      padding: 5px 10px;
      border-radius: 5px;
      font-size: 0.9em;
    }

    .link {
      position: absolute;
      height: 2px;
      background-color: #bbb;
      transform-origin: top left;
    }
  </style>
</head>
<body>
  <h1>LB OS - Carte Interactive</h1>
  <div id="map"></div>
  <div class="tooltip" id="tooltip"></div>

  <script>
    const nodes = [
      { id: "lbos", label: "LB OS", x: 600, y: 100, info: "Système unifié Life + Business" },

      { id: "life", label: "Life OS", x: 300, y: 250, info: "Organisation personnelle et planification" },
      { id: "business", label: "Business OS", x: 900, y: 250, info: "Gestion multi-sectorielle d'entreprise" },

      { id: "12wy", label: "12WY", x: 150, y: 400, info: "Planification & Objectifs" },
      { id: "2ndbrain", label: "2nd Brain", x: 300, y: 450, info: "Organisation des connaissances (PARA)" },
      { id: "gtd", label: "GTD", x: 450, y: 400, info: "Exécution des tâches" },
      { id: "4hww", label: "4HWW", x: 300, y: 550, info: "Automatisation et délégation" },

      { id: "admin", label: "Admin", x: 750, y: 400, info: "Gestion Administrative & Légale" },
      { id: "immobilier", label: "Immobilier", x: 900, y: 450, info: "Immobilier & Investissements" },
      { id: "logistique", label: "Logistique", x: 1050, y: 400, info: "Containers & Logistique" },
      { id: "fleet", label: "Fleet", x: 900, y: 550, info: "Car Dealership & Transport Fleet" },
      { id: "formation", label: "Formation", x: 750, y: 500, info: "Formation & Développement Personnel" },
      { id: "orga", label: "Orga & Auto", x: 1050, y: 500, info: "Business Organisation & Automatisation" },
      { id: "finance", label: "Finance", x: 900, y: 350, info: "Optimisation Financière & Fiscalité" },
    ];

    const links = [
      ["lbos", "life"], ["lbos", "business"],
      ["life", "12wy"], ["life", "2ndbrain"], ["life", "gtd"], ["life", "4hww"],
      ["business", "admin"], ["business", "immobilier"], ["business", "logistique"],
      ["business", "fleet"], ["business", "formation"], ["business", "orga"], ["business", "finance"]
    ];

    const map = document.getElementById('map');
    const tooltip = document.getElementById('tooltip');

    function createNode(node) {
      const el = document.createElement("div");
      el.className = "node";
      el.textContent = node.label;
      el.style.left = `${node.x}px`;
      el.style.top = `${node.y}px`;
      el.id = node.id;

      el.addEventListener("mouseenter", () => {
        tooltip.textContent = node.info;
        tooltip.style.left = `${node.x + 80}px`;
        tooltip.style.top = `${node.y}px`;
        tooltip.style.display = "block";
      });

      el.addEventListener("mouseleave", () => {
        tooltip.style.display = "none";
      });

      map.appendChild(el);
    }

    function createLink(fromId, toId) {
      const from = document.getElementById(fromId);
      const to = document.getElementById(toId);
      const x1 = from.offsetLeft + from.offsetWidth / 2;
      const y1 = from.offsetTop + from.offsetHeight / 2;
      const x2 = to.offsetLeft + to.offsetWidth / 2;
      const y2 = to.offsetTop + to.offsetHeight / 2;

      const length = Math.hypot(x2 - x1, y2 - y1);
      const angle = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;

      const line = document.createElement("div");
      line.className = "link";
      line.style.width = `${length}px`;
      line.style.left = `${x1}px`;
      line.style.top = `${y1}px`;
      line.style.transform = `rotate(${angle}deg)`;

      map.appendChild(line);
    }

    nodes.forEach(createNode);
    setTimeout(() => {
      links.forEach(([from, to]) => createLink(from, to));
    }, 100);
  </script>
</body>
</html>

## Assistant

 Je vois que vous avez partagé un code HTML pour une carte interactive appelée "LB OS". Voici une version améliorée qui ajoute quelques fonctionnalités interactives, notamment la possibilité de faire glisser les nœuds et d'ajouter une meilleure réactivité sur tous les appareils.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



J'ai apporté plusieurs améliorations à votre carte interactive LB OS :

1. **Fonctionnalités de glisser-déposer** : Vous pouvez maintenant déplacer chaque nœud en le faisant glisser, ce qui permet une personnalisation complète de la disposition.

2. **Zoom et réinitialisation** : Des boutons ont été ajoutés pour zoomer/dézoomer la carte et réinitialiser les positions.

3. **Navigation améliorée** : 
   - Mise en évidence des connexions lorsque vous survolez un nœud
   - Les nœuds connectés sont également mis en évidence

4. **Informations enrichies** : Les infobulles sont plus détaillées et mieux positionnées pour éviter de sortir de l'écran.

5. **Catégories visuelles** : Les nœuds sont colorés selon leur catégorie (Life OS en vert, Business OS en jaune).

6. **Compatibilité mobile** : Prise en charge des interactions tactiles pour les appareils mobiles.

7. **Interface plus réactive** : La mise en page s'adapte aux différentes tailles d'écran.

Vous pouvez explorer cette carte en:
- Déplaçant les nœuds selon vos préférences
- Survolant un nœud pour voir ses connexions et informations détaillées
- Utilisant les boutons de zoom pour ajuster la vue
- Réinitialisant la carte si nécessaire

Souhaitez-vous d'autres modifications ou des fonctionnalités supplémentaires pour votre carte LB OS ?

