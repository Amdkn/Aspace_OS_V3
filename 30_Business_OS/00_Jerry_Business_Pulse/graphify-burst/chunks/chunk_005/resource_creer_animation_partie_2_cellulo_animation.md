# 🧿 Guide Geordi Resource — [FR] Créer une animation - Partie 2：Cellulo d’animation

## 🧬 Métadonnées
- **ID Vidéo** : YT-wgljjcINcus
- **Titre** : [FR] Créer une animation - Partie 2：Cellulo d’animation
- **Chaîne** : CLIP STUDIO PAINT
- **Serendipity Score** : 7/10
- **Catégorie** : AI / 2D Animation / Graphic Design / Digital Art
- **Date de Clarification** : 2026-05-24
- **Statut** : CLARIFIED_PLANE

---

## 1. Concepts Clés (Concepts Clés)

L'animation traditionnelle numérique sous **Clip Studio Paint** s'appuie sur le paradigme historique du celluloïd physique (ou "cel"). Cette section détaille les concepts mathématiques, d'organisation des données et de chronologie régissant ce processus.

### Le Paradigme du Cellulo (Animation Cel)
Le cellulo d'animation moderne dans un logiciel de dessin est la transposition numérique de la feuille de plastique transparente en acétate de cellulose utilisée jadis par les studios traditionnels (comme Disney ou Ghibli). Dans Clip Studio Paint, un cellulo ne correspond pas simplement à un calque opaque isolé, mais à une entité de dessin dynamique contenue dans un "dossier d'animation". Ce concept permet de superposer des dessins transparents (le line-art, les ombres, les couleurs) tout en les traitant comme une seule et unique frame temporelle sur la timeline.

### Spécification de Cellule et Mappage Temporel
Contrairement aux logiciels de montage vidéo où chaque calque a une existence temporelle linéaire automatique, Clip Studio Paint découple la création du dessin et son affichage sur la timeline. Ce processus est appelé la "Spécification de Cellule". Un dessin présent dans le dossier d'animation n'apparaît à l'écran que s'il est explicitement "spécifié" ou "mappé" à une frame précise de la timeline. Ce système offre une flexibilité immense : un même cellulo peut être affiché plusieurs fois à des moments différents, ou étiré pour durer plusieurs frames (animation sur "doubles" ou "triples").

### Table lumineuse numérique et Pelures d'oignon (Onion Skinning)
Pour dessiner le mouvement de manière fluide, l'animateur doit voir les dessins précédents et suivants en transparence.
- **La pelure d'oignon** : Affiche les cellulos adjacents avec des teintes colorées configurables (généralement rouge pour les frames précédentes, bleu pour les frames suivantes) et une opacité dégressive.
- **La table lumineuse (Light Table)** : Permet d'importer temporairement n'importe quel dessin du projet ou d'un fichier externe au centre de la zone de travail actuelle, de le tourner ou de le redimensionner pour servir de référence anatomique ou de perspective, sans affecter le calque final.

### Dossiers de Cellulo pour la Couleur et les Lignes
Dans un pipeline de production professionnel, un cellulo d'animation est souvent structuré sous forme de dossier contenant plusieurs calques : un calque vectoriel pour le tracé propre (Lineart), un calque raster pour les couleurs de fond (Flat Colors), et des calques en mode produit/incrustation pour les ombres et les lumières. Clip Studio Paint sait lire ce dossier complexe comme un calque unique sur la timeline, permettant à l'artiste de peindre et de modifier les ombres de manière isolée sans altérer le trait.

---

## 2. Entités & Outils (Entités & Outils)

L'exécution du workflow d'animation requiert une maîtrise des outils d'interface utilisateur et des types de structures de calques de Clip Studio Paint.

### Outils d'Interface de la Timeline
- **Dossier d'Animation (Animation Folder)** : Le conteneur parent obligatoire sur la timeline. Tous les calques insérés à l'intérieur deviennent des candidats pour devenir des cellulos d'animation.
- **Palette Timeline** : La console de contrôle centrale d'où l'on gère la cadence (framerate), la durée de l'animation, les clés d'effets visuels et le mappage des cellulos.
- **Spécifier le cellulo (Specify Cels)** : Le bouton ou raccourci clavier qui associe le cellulo actif à la frame courante de la timeline.
- **Nouveau Cellulo d'Animation** : Raccourci de création qui génère automatiquement un nouveau calque dans le dossier d'animation et l'associe instantanément à la frame sélectionnée.

### Outils de Dessin de Précision
- **Calques Vectoriels d'Animation** : Indispensables pour le tracé. Ils permettent d'utiliser la gomme vectorielle pour effacer les intersections de traits en un clic, et de redimensionner le tracé sans perte de qualité.
- **Outil Remplissage (Pot de peinture) avec détection d'écart** : Permet de colorer rapidement les cellulos en fermant virtuellement les lignes interrompues du line-art.

---

## 3. Synthèse Pratique (Synthèse Pratique)

Le cœur de ce guide repose sur la transition du dessin fixe vers l'animation séquentielle dynamique en utilisant les cellulos.

### Méthodologie de Création des Cellulos
L'artiste commence par créer une scène d'animation. Il crée ensuite un dossier d'animation dans la palette des calques. Pour dessiner le premier cellulo, il insère un nouveau calque à l'intérieur de ce dossier. Sur la timeline, il se positionne à la première frame et effectue une "spécification de cellule" pour lier ce calque. C'est à ce moment précis que le canevas devient éditable. Pour créer l'image suivante, il déplace la tête de lecture sur la timeline (par exemple de 3 frames pour animer en "3s" à 24fps), clique sur "Nouveau Cellulo", ce qui crée automatiquement un calque vierge nommé séquentiellement (ex: "2") et l'affiche sur l'écran.

### Configuration Avancée de la Pelure d'Oignon
L'activation de la fonction "Pelure d'oignon" se fait via le menu Animation > Affichage de l'animation > Paramètres de pelure d'oignon. L'animateur y configure le nombre d'images antérieures et postérieures visibles (généralement 2 ou 3) et leur opacité de départ (ex: 50%). Cela fournit le guide visuel indispensable pour interpoler les intervalles (in-betweens) entre deux poses clés (keys).

### Gestion de la Résolution et des Marges de Sécurité (Canevas d'Animation)
Lors de l'animation de cellulos, il est recommandé de travailler sur un canevas plus grand que la zone d'exportation finale. Clip Studio Paint gère cela via le cadre d'exportation (Output Frame) et le cadre de sécurité (Safe Frame). Cela permet de dessiner des éléments qui entrent ou sortent du champ de la caméra de manière fluide, et d'appliquer des mouvements de caméra numériques (panoramiques, travellings) sans jamais révéler les bords coupés des dessins raster de nos cellulos.

---

## 4. Actionnabilité (D.E.A.L) (Actionnabilité)

Comment intégrer ce workflow d'animation par cellulos pour industrialiser nos productions de contenus souverains ?

### D — Definition (Définition)
- **Objectif** : Paramétrer le cadre de production technique avant le premier tracé.
- **Actions** :
  1. Définir la cadence cible du projet : Standard cinéma (24 fps), animation web rapide (12 fps ou 15 fps) ou standard TV (25/30 fps).
  2. Établir la nomenclature de nommage automatique des calques dans les préférences de Clip Studio Paint (ex: incrémentation numérique automatique: 1, 2, 3 ou alphabétique: A, B, C).
  3. Déterminer la structure type du dossier d'animation (Lineart vectoriel + Couleur raster).

### E — Elimination (Élimination)
- **Objectif** : Supprimer le gaspillage de temps, les erreurs d'in-betweening et les calques orphelins.
- **Actions** :
  1. Éliminer les calques orphelins (calques créés dans la palette des calques mais jamais assignés à la timeline) en exécutant périodiquement la commande de nettoyage des cellulos non utilisés.
  2. Supprimer la fatigue oculaire en configurant des couleurs de pelure d'oignon à fort contraste (par exemple, vert citron pour le passé, magenta électrique pour le futur) sur un fond de canevas gris neutre à 18% de réflectance.
  3. Bannir le dessin destructif : éliminer l'usage du calque raster unique pour le trait et la couleur. Toujours séparer les calques à l'intérieur d'un dossier de cellulo pour préserver l'intégrité du trait.

### A — Automation (Automatisation)
- **Objectif** : Automatiser la navigation temporelle et la génération de structures de dessins complexes.
- **Actions** :
  1. Automatiser la création de calques composites en programmant une action rapide (Quick Action) qui crée un dossier de calques contenant "Trait (Vectoriel)" + "Couleur (Raster)" et l'enregistre comme cellulo type d'un seul raccourci clavier.
  2. Configurer des raccourcis clavier optimisés pour les fonctions fréquentes : `Numpad 0` pour activer la table lumineuse, `Numpad .` pour activer/désactiver la pelure d'oignon, et les touches directionnelles gauche/droite pour naviguer de frame en frame.
  3. Créer un script d'exportation par lots qui compile et exporte automatiquement les cellulos propres au format PNG transparent pour d'autres moteurs d'animation ou d'effets visuels.

### L — Liberation (Libération)
- **Objectif** : S'affranchir de la dépendance aux logiciels de l'écosystème Adobe (Animate/Premiere) et acquérir une indépendance absolue de création de contenu de haute facture.
- **Actions** :
  1. Exploiter la puissance du moteur de dessin naturel de Clip Studio Paint pour donner un rendu "fait main" et organique à des créations de communication d'A'Space OS, marquant une rupture avec l'esthétique standardisée et froide des illustrations vectorielles d'entreprise.
  2. Travailler sur des configurations matérielles nomades (iPad Pro, tablettes Windows légères) avec une fluidité exceptionnelle que n'offrent pas les outils lourds traditionnels.
  3. Devenir le maître d'œuvre complet de nos récits visuels en stockant nos fichiers d'animation au format ouvert de Clip Studio pour assurer la pérennité de notre patrimoine intellectuel.

---

## 5. SOP Opérationnelle de Création de Séquence de Cellulos

```text
[SOP-CSP-CELLULO-ANIM]
1. Initialisation du Document : Ouvrir Clip Studio Paint. Créer un nouveau document de type "Animation". Définir la taille du cadre de sortie à 1920x1080, la résolution à 300 dpi et la cadence à 24 fps.
2. Structure de la Timeline : Si elle n'est pas affichée, ouvrir la palette "Timeline" (Fenêtre > Timeline). Créer un nouveau dossier d'animation. Renommer le dossier "01_Lineart".
3. Création du Premier Cellulo : Cliquer sur la frame 1 de la timeline. Cliquer sur l'icône "Nouveau cellulo d'animation". Un calque nommé "1" est créé automatiquement dans le dossier et assigné à la frame 1. Dessiner la pose clé initiale.
4. Préparation de la Pose Suivante : Se déplacer à la frame 4 de la timeline (pour animer en "3s"). Cliquer à nouveau sur "Nouveau cellulo d'animation". Un calque vierge nommé "2" est créé à la frame 4.
5. Activation de la Pelure d'Oignon : Cliquer sur l'icône "Activer la pelure d'oignon" dans la palette de la timeline pour voir le dessin "1" en transparence rouge. Dessiner la pose clé finale ou la transition intermédiaire sur le calque "2".
6. Création des Intervalles (In-betweens) : Cliquer sur la frame 2 de la timeline. Créer un nouveau cellulo "3". Utiliser la pelure d'oignon pour dessiner le dessin intermédiaire exactement à mi-chemin géométrique entre le dessin "1" (rouge) et le dessin "2" (bleu).
7. Validation par boucle (Play) : Régler les balises de début et de fin de lecture sur la timeline pour englober la séquence créée. Lancer la lecture en boucle (raccourci Espace) pour valider la fluidité rythmique de l'animation.
```
