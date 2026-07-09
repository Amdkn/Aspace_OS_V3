# 🧿 Guide Geordi Resource — Enve. 2d animation. Importez une image raster par calque (français)

## 🧬 Métadonnées
- **ID Vidéo** : YT-0vgZUybSGuY
- **Titre** : Enve. 2d animation. Importez une image raster par calque (français)
- **Chaîne** : Alexander Kiryanov
- **Serendipity Score** : 7/10
- **Catégorie** : AI / 2D Animation / Graphic Design / Open Source Software
- **Date de Clarification** : 2026-05-24
- **Statut** : CLARIFIED_PLANE

---

## 1. Concepts Clés (Concepts Clés)

L'importation et la manipulation d'images rasters (ou matricielles) au sein d'un environnement d'animation vectorielle open-source comme **Enve** constituent une technique pivot pour les animateurs 2D. Cette méthode combine la richesse texturale des médias matriciels avec la souplesse d'animation et de déformation du vectoriel.

### Pipeline d'Animation Hybride Raster-Vectoriel
Le pipeline hybride est le processus par lequel des éléments graphiques peints de manière traditionnelle ou générés par IA générative (médias matriciels au format PNG avec canal alpha) sont intégrés dans un logiciel d'animation vectorielle pour y subir des transformations géométriques. Contrairement au vectoriel pur, le matriciel conserve une richesse de texture, de grain et d'ombrage pictural complexe qui serait extrêmement lourde à calculer en courbes de Bézier. Le défi réside dans la préservation de la qualité de ces textures lors des rotations, zooms et déformations.

### Gestion Non-Destructive des Calques Raster
Lorsqu'une image raster est importée dans Enve, le logiciel crée un calque de référence pointant vers le fichier source externe. Les transformations appliquées dans Enve (redimensionnement, rotation, opacité) sont enregistrées de manière métadonnée sous forme d'équations géométriques de rendu. Cela garantit que l'image source n'est jamais altérée et que le moteur de rendu réévalue la pixellisation en temps réel à chaque frame, optimisant l'anticrénelage (anti-aliasing) selon le facteur d'échelle actuel de la caméra virtuelle.

### Cinématique Directe (FK) et Hiérarchie de Parenté
Pour animer une marionnette 2D (rigging de personnage) composée de multiples calques d'images raster (bras, avant-bras, main), Enve utilise un système de parenté. Un calque "enfant" hérite de toutes les transformations spatiales de son calque "parent". Comprendre la mise en place de cette hiérarchie est crucial pour éviter de devoir replacer manuellement chaque partie du corps à chaque image clé. Le mouvement se propage naturellement le long de la chaîne articulaire.

### Point d'Ancrage et Pivot d'Articulation
Chaque calque raster possède son propre centre de transformation local, communément appelé "point de pivot" ou "ancrage". Par défaut, le pivot est placé au centre géométrique de l'image. Pour animer un membre de manière réaliste (par exemple, faire pivoter un bras à partir de l'épaule plutôt que du milieu de l'humérus), l'animateur doit repositionner manuellement le pivot à l'articulation exacte avant de générer des clés d'animation.

---

## 2. Entités & Outils (Entités & Outils)

Le workflow repose sur un ensemble précis de logiciels libres et de formats de fichiers industriels pour garantir l'interopérabilité et la performance.

### Logiciels & Moteurs de Rendu
- **Enve 2D** : Logiciel d'animation open-source multiplateforme écrit en C++ et exploitant Qt5 pour l'interface utilisateur. Son architecture modulaire permet de combiner calques vectoriels, images rasters, séquences d'images et scripts d'effets visuels.
- **Krita & GIMP** : Logiciels de peinture numérique et de retouche d'images open-source utilisés en amont pour découper le personnage en calques séparés et exporter chaque membre dans un format supportant la transparence.
- **Moteur OpenToonz / MyPaint integration** : Les brosses et shaders internes à Enve qui permettent de retoucher ou d'ombrer des calques directement au sein de la timeline de production.

### Spécifications de Formats et Protocoles
- **PNG (Portable Network Graphics) avec canal Alpha (32-bit RGBA)** : Le format standard d'exportation. Il assure une compression sans perte et préserve le canal alpha indispensable pour superposer proprement les membres du personnage sans blocs blancs rectangulaires.
- **TGA / TIFF (optionnels)** : Formats d'échange professionnels pour les cas exigeant des profondeurs de couleur supérieures (16-bit par canal) afin d'éviter le banding dans les dégradés d'ombres portées.

---

## 3. Synthèse Pratique (Synthèse Pratique)

L'importation correcte d'une image raster dans Enve pour chaque calque et sa préparation à l'animation suivent un protocole technique rigoureux afin d'éviter les surcharges mémoire et les artefacts visuels.

### Processus d'Importation pas à pas
Le processus débute par l'importation individuelle de chaque fichier PNG correspondant à une partie de la marionnette. Dans l'interface d'Enve, l'action consiste à passer par le menu d'importation d'actifs ou à glisser-déposer les fichiers directement dans le panneau des ressources ou sur la timeline. Enve crée instantanément un calque distinct pour chaque image, étiquetant le calque avec le nom du fichier.

### Configuration Critique des Articulations et Pivots
Une fois les calques rasters importés et positionnés grossièrement pour assembler la marionnette, l'étape la plus critique consiste à utiliser l'outil d'édition de pivot. En déplaçant le pivot de chaque calque raster (l'épaule pour le bras, le coude pour l'avant-bras, le poignet pour la main), l'animateur établit la base physique des rotations. Si cette étape est omise ou mal réalisée, toute tentative d'animation brisera la cohérence structurelle du personnage, provoquant des déconnexions de membres inesthétiques.

### Optimisation des Ressources CPU/GPU et Gestion du Cache
L'animation de calques raster multiples consomme beaucoup plus de mémoire vive (RAM) et de bande passante GPU que l'animation vectorielle pure, car le processeur graphique doit charger et stocker des textures en haute résolution. Pour maintenir une prévisualisation fluide en temps réel (playback à 24 ou 30 fps) :
1. **Résolution ciblée** : Limiter la résolution des images raster importées aux dimensions réelles nécessaires à l'écran. Importer un fichier 4K pour un calque représentant un petit accessoire de 200 pixels de large est une faute technique grave.
2. **Utilisation du cache de rendu** : Activer les options de mise en cache interne dans Enve pour éviter de recalculer les dalles matricielles statiques à chaque frame.

---

## 4. Actionnabilité (D.E.A.L) (Actionnabilité)

Comment maximiser notre efficacité opérationnelle et notre souveraineté créative avec Enve 2D et le pipeline d'importation raster ?

### D — Definition (Définition)
- **Objectif** : Cadrer et standardiser la phase de préparation des actifs rasters.
- **Actions** :
  1. Définir une nomenclature stricte pour l'exportation des fichiers rasters (ex: `charName_arm_L_upper.png`, `charName_arm_L_lower.png`).
  2. Valider la résolution finale du projet d'animation (ex: HD 1080p ou 4K) pour adapter la résolution d'exportation des calques rasters à exactement 100% de leur taille maximale affichée à l'écran.
  3. Établir une charte de profondeur de couleur (recommander le format PNG 8-bit RGBA pour le web, ou TIFF 16-bit pour la production cinéma).

### E — Elimination (Élimination)
- **Objectif** : Éliminer les sources de lourdeur système, de plantage d'Enve et de ralentissement du rendu.
- **Actions** :
  1. Éliminer toutes les marges transparentes inutiles autour de chaque image raster exportée via Krita/GIMP (recadrage automatique aux pixels non transparents) pour réduire le poids des textures chargées dans le GPU.
  2. Écarter l'utilisation d'images raster compressées avec perte (JPEG) qui détruisent les bords par compression par blocs et ne supportent pas la transparence native.
  3. Bannir le rigging sans structure : interdire l'animation directe de calques raster enfants avant d'avoir vérifié visuellement l'ancrage correct et la parenté du groupe.

### A — Automation (Automatisation)
- **Objectif** : Rendre le processus d'importation et de configuration des calques instantané et répétable.
- **Actions** :
  1. Automatiser l'exportation multi-calques depuis Krita ou GIMP à l'aide de scripts d'exportation de calques en fichiers individuels (Krita standardise cela avec l'outil d'export de calques d'animation).
  2. Structurer des dossiers de surveillance (watch folders) : concevoir un script simple de rechargement des liaisons (re-link) dans Enve pour mettre à jour instantanément tous les calques rasters si les fichiers sources sont repeints à l'extérieur.
  3. Définir des modèles (templates) de projets Enve avec la hiérarchie squelettique de base pré-configurée, prête à accueillir les nouvelles versions d'images rasters par simple écriture sur fichier.

### L — Liberation (Libération)
- **Objectif** : Acquérir une indépendance absolue vis-à-vis des écosystèmes propriétaires d'animation (Adobe Animate, Toon Boom Harmony) très coûteux.
- **Actions** :
  1. Utiliser un outil 100% open-source, portable et respectueux de la vie privée (Enve + Krita), garantissant la souveraineté totale de notre chaîne de production numérique.
  2. Permettre à nos équipes créatives de travailler sur n'importe quel système d'exploitation léger, y compris des stations de travail Linux souveraines à faibles ressources.
  3. Libérer le potentiel esthétique en mariant la liberté artistique du dessin traditionnel à la main (peinture numérique riche dans Krita) avec l'efficacité industrielle de l'animation interpolée vectorielle sous Enve.

---

## 5. SOP Opérationnelle d'Import et d'Animation Raster sous Enve

```text
[SOP-ENVE-RASTER-IMPORT]
1. Préparation dans le Logiciel Source (Krita/GIMP) : Isoler chaque élément anatomique ou graphique sur son propre calque. Recadrer chaque élément au plus près de ses bords utiles. Exporter au format PNG-32 (RGBA) dans un sous-dossier "/assets" dédié du projet.
2. Lancement du Projet Enve : Créer un nouveau projet dans Enve aux dimensions cibles (ex: 1920x1080 à 24fps). Sauvegarder le fichier projet ".enve" dans le répertoire parent de "/assets".
3. Importation Structurée : Ouvrir le gestionnaire d'actifs d'Enve, importer l'ensemble des fichiers PNG du dossier "/assets". Glisser-déposer chaque ressource sur la timeline sous forme de calques distincts.
4. Rigging de Pivot : Sélectionner un calque (ex: avant-bras). Activer l'outil "Edit Anchor". Glisser le symbole de pivot rouge au centre physique de l'articulation avec le bras (le coude). Répéter rigoureusement pour chaque calque.
5. Établissement de la Parenté : Dans le panneau de hiérarchie des calques, glisser-déposer le calque de l'avant-bras sous le calque du bras pour le définir comme enfant. Tester la rotation du bras parent pour valider que l'avant-bras suit le mouvement de manière fluide et transparente.
6. Animation de Test : Se positionner à la frame 1, insérer une image clé sur la rotation. Aller à la frame 12, appliquer une rotation de 45 degrés pour vérifier l'interpolation et la qualité du rendu matriciel.
```
