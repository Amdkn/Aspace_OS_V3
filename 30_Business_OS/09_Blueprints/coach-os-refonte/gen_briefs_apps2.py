# -*- coding: utf-8 -*-
"""Vague 2 des briefs d'enrichissement d'apps. Contenu tire de CARTE.md section 3."""
import pathlib, re
P = pathlib.Path(__file__).parent

# On reutilise le tronc commun du premier generateur, avec l'interdiction
# des workflows BMAD ajoutee (un agent s'y est bloque sur « [A] Approve »).
src = (P / "gen_briefs_apps.py").read_text(encoding="utf-8")
COMMUN = re.search(r'COMMUN = """(.*?)"""', src, re.S).group(1)
COMMUN = COMMUN.replace("## Interdits\n\n1.", """## Interdits

0. **N'invoque AUCUN workflow BMAD** (`bmad-spec`, `bmad-build-auto`,
   `bmad-advanced-elicitation`, `bmad-party-mode`...). Le depot en contient 46 ;
   ils ouvrent une porte d'approbation « [A] Approve / [E] Edit » que personne ne
   peut franchir ici — la session est non interactive. Tu **implementes
   directement** : tu edites les fichiers, tu verifies, tu rends. N'ecris aucun
   document de specification ; ecris du code.

1.""", 1)

REPO = ("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/"
        "05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os")

APPS = {
"growth": dict(
  fichier="src/apps/growth/GrowthApp.tsx", accent="#16a34a",
  actuel="(lire le fichier pour l'etat exact)",
  cible="""
Ajoute ces **quatre** sections, en gardant toutes les existantes :

- **Acquisition** — chaque canal note sur quatre criteres : viralite, taux de
  conversion, cout, facilite de mise en oeuvre. Une note globale s'en deduit.
  Le detail montre ce qui marche et ce qui a echoue sur ce canal.

- **Strategie** — le phasage d'une offre : lancement, montee en charge,
  optimisation. Chaque phase porte ses objectifs, sa duree et son critere de
  passage a la suivante.

- **Partenariats** — les partenaires potentiels ou actifs : ce qu'ils apportent,
  ce qu'ils attendent, l'etat de la relation (`prospect / en discussion /
  actif / dormant`).

- **AEO** — la visibilite dans les reponses des modeles de langage : quelles
  requetes citent la marque, lesquelles citent un concurrent, et depuis quand.
  C'est le referencement de l'ere des agents ; traite-le comme une metrique
  suivie dans le temps.
"""),

"finance": dict(
  fichier="src/apps/finance/FinanceApp.tsx", accent="#0d9488",
  actuel="(lire le fichier pour l'etat exact)",
  cible="""
Ajoute ces **quatre** sections, en gardant toutes les existantes :

- **Plancher de marge** — pas une marge cible, un PLANCHER : le seuil sous lequel
  une prestation ne se vend pas. Chaque offre : son cout reel, son plancher, son
  prix pratique, et l'ecart. Rends visible ce qui passe sous le plancher.

- **Courbe de demande** — des scenarios de prix et leur volume estime. Montre au
  moins trois points par offre pour qu'on voie la pente, pas un chiffre isole.

- **Budget de tokens** — la depense en modeles, comparee au cout des personnes
  qu'elle evite d'embaucher. C'est la metrique qui justifie l'automatisation :
  presente-la comme un rapport, pas comme une facture.

- **Formes de prix** — les differentes manieres de facturer une meme prestation :
  frais d'installation, abonnement, a l'evenement, gratuit en accroche. Chaque
  forme avec ce qu'elle implique en tresorerie et en engagement client.
"""),

"product": dict(
  fichier="src/apps/product/ProductApp.tsx", accent="#ea580c",
  actuel="(lire le fichier pour l'etat exact)",
  cible="""
Ajoute ces **quatre** sections, en gardant toutes les existantes :

- **Classement** — les idees de produit rangees en paliers S / A / B / F, avec le
  critere qui justifie chaque placement. Un classement sans justification ne vaut
  rien : la justification est obligatoire sur chaque entree.

- **Lancement** — les cinq etapes canoniques : valider, pre-vendre, lancer,
  construire l'audience, produitiser. Chaque etape porte son etat et sa preuve
  d'achevement.

- **MVP** — la discipline du plus petit livrable : une fonctionnalite, un client,
  un probleme. Chaque entree nomme les trois, et signale quand l'une des trois
  deborde.

- **Ideation** — les idees a l'etat brut, evaluees sur quatre angles : tendance
  porteuse, opportunite, demande observee, taille economique.
"""),

"tasks": dict(
  fichier="src/apps/tasks/TasksApp.tsx", accent="#059669",
  actuel="(lire le fichier pour l'etat exact)",
  cible="""
Ajoute ces **trois** sections, en gardant toutes les existantes :

- **Definition of Done** — un champ OBLIGATOIRE par tache : a quoi on reconnait
  qu'elle est finie. Rends visibles les taches qui n'en ont pas : ce sont les
  plus dangereuses.

- **Comparateur** — la verification d'un livrable contre une reference :
  comparaison d'image, fichier temoin, parite de comportement. Chaque entree dit
  ce qui est compare, contre quoi, et le verdict.

- **Actions exposees** — le compte hebdomadaire des actions rendues publiques
  (livraison, publication, envoi). C'est une mesure de rythme, pas de volume :
  presente-la comme une serie dans le temps.
"""),

"audit": dict(
  fichier="src/apps/audit/AuditApp.tsx", accent="#dc2626",
  actuel="6 grilles prevues, 1 seule ecrite — les 5 autres sont des ebauches vides",
  cible="""
Cette app a **six grilles d'audit prevues, une seule ecrite**. Les cinq autres
sont des ebauches vides (cherche-les dans le fichier, autour des lignes 269-308).

**Ecris les cinq grilles manquantes.** Chacune est une liste de criteres
evaluables, avec pour chaque critere : son libelle, ce qu'on observe pour le
juger, et une echelle a trois niveaux.

Les cinq :

- **Arbitrage** — ce qui doit rester une decision humaine, et pourquoi.
- **Contexte** — ce que l'agent doit savoir du metier pour agir juste.
- **Donnees** — la qualite, la fraicheur et la provenance de ce qu'il consomme.
- **Automatisabilite** — ce qui peut passer a la machine, ce qui resiste.
- **Retour sur arbitrage** — ce que coute une decision humaine, ce qu'elle evite.

Prends modele sur la grille deja ecrite : meme structure, meme rendu, meme
niveau de detail. Ne la modifie pas.
"""),
}

for app, a in APPS.items():
    txt = ("# BRIEF — enrichir l'app `%s`\n\n"
           "Tu es un developpeur front. Tu ajoutes des sections a UNE app existante,\n"
           "avec du contenu structure et une page de detail par element.\n\n"
           "**Ton fichier principal** : `%s`\n"
           "**Etat actuel** : %s\n"
           "**Accent de l'app** : `%s`\n"
           % (app, a["fichier"], a["actuel"], a["accent"])
           + COMMUN.replace("{REPO}", REPO)
           + "\n## Les sections a ajouter\n" + a["cible"])
    (P / ("BRIEF_APP_%s.md" % app)).write_text(txt, encoding="utf-8")
    print("BRIEF_APP_%-12s %6d car." % (app + ".md", len(txt)))
