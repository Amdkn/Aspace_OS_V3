import os
import sys
import asyncio
import edge_tts
import win32com.client

BRAIN_DIR = r"C:\Users\amado\.gemini\antigravity\brain\ca47e94f-1b0e-44f5-b619-0600db15150d"
MP3_FILE = os.path.join(BRAIN_DIR, "matrice_alignement_tech_os.mp3")

SPEECH_SCRIPT = """
Matrice d'Alignement et Architecture du Cycle d'Ingénierie Tech OS.

Première partie : Analyse de l'Alignement. Votre Vision contre l'Exécution Récente.
Le constat d'Amadou Kone est chirurgical : les agents de fond ont confondu déclarer un état et produire de la valeur industrielle.
Ce qui a été fait par la flotte : les soixante-six travaux ont créé des vérificateurs, initialisé des registres comme registre para et pulse, audité des files mortes, et monté des interfaces statiques. C'est l'étape zéro : la stabilisation du plancher.
Ce qui manquait : l'Ingénierie des Systèmes. Les agents se sont comportés comme des scribes documentaires plutôt que comme des ingénieurs d'un runtime souverain. Ils ont documenté l'existence de V2, de Life OS et de Business OS sans activer les pipelines dynamiques de transformation : les trois Gates réelles, le compilateur Prompt as Code, et l'orchestration fractale des trois Docteurs.

Deuxième partie : Le Cycle d'Ingénierie Agentique Unifié.
Pour que Tech OS ne dépende plus de prompts manuels ni de boucles d'introspection verbeuses de soixante itérations, le cycle de développement d'un agent s'articule autour de sept disciplines d'ingénierie intégrées :
Numéro un : L'Ontology Engineering. Structuration formelle du domaine. Zéro texte ambigu : entités, relations, invariants, graphes de connaissances et schémas immuables. Sous la responsabilité du treizième Docteur et de Graham.
Numéro deux : Le Context Engineering. Élimination de l'append-only. Remplacement du chat continu par un espace d'état condensé Skill point state. Avec le bus state point dji-zonn et la sonde passive de Bill. Sous la responsabilité du onzième Docteur, de Rory et de Bill.
Numéro trois : Le Prompt Engineering avec Prompt as Code. Les prompts ne sont plus saisis à la main : ils sont compilés dynamiquement à la volée via des blueprints Jinja deux, avec un plafond strict sous deux mille quarante-huit tokens et la clause arrêt budget. Sous la responsabilité du douzième Docteur et de Nardole.
Numéro quatre : Le Harness Engineering. La cage déterministe qui contrôle le modèle probabiliste, avec gate point paille, un hard cap à vingt-cinq itérations maximum, et un coupe-circuit budgétaire sous vingt-cinq dollars par jour. Sous la responsabilité du treizième Docteur, de Ryan et Yaz.
Numéro cinq : Le Loop Graph Engineering. Conception de machines d'états finis en trois temps : Spécifier, Construire, Valider, avec sortie binaire et bascule automatique vers Donna en Dead Letter Queue en cas de trois échecs consécutifs. Sous la responsabilité de River et Donna.
Numéro six : L'Answer Engineering. Formatage contractuel de la réponse sous forme de patch d'état, avec preuve mécanique d'exécution à code retour zéro.
Numéro sept : L'Orchestration Engineering. Répartition fractale des charges entre Cœurs, Domaines et Techniciens, avec injection granulaire d'outils Composio par Clara, et S1 Rick en arbitre suprême des flux.

Troisième partie : Application Pratique aux trois Cœurs de l'Écosystème.
L0 Bedrock Core sur Tech OS Local et Agent OS Desktop au port cinquante-cinq cinquante-cinq : Ryan compile et build, Yaz surveille les métriques et baux, Graham fige les états, Donna capture les échecs.
L1 Life Core sur Vercel et Supabase : Amy capte les rituels et intentions, Rory structure PARA et GTD, River cadence le sprint douze semaines et publie l'état des huit jauges Zora au vert.
L2 Buzz Core sur Business OS et The OMK Office : machine déterministe visant dix mille dollars par mois net. Bill sonde la disponibilité métabolique, Clara monte les outils Composio nécessaires, et Nardole dispatche les tâches aux techniciens Marvel sans surcharger le contexte.

Quatrième partie : Sélection de Prompts d'Action Prêts à l'Emploi.
Option un : Harness et Loop Graph Engineering au pôle L0 pour verrouiller le cap à vingt-cinq itérations et le tuple formel.
Option deux : Prompt as Code et Context Engineering au pôle L2 pour le compilateur dynamique Nardole et Clara.
Option trois : Ontology et Answer Engineering au pôle L2 pour le pipeline des cent clients par mois à trois cents dollars l'an pour The OMK Office.
Option quatre : Orchestration et Replay Engineering au pôle S1 et L0 pour équiper Graham de la sauvegarde et restauration SQLite WAL.

Sur quel pilier d'ingénierie active-t-on le prochain mandat d'exécution ?
""".strip()

async def generate():
    print(f"Génération audio HD via edge-tts (fr-FR-DeniseNeural)...")
    comm = edge_tts.Communicate(SPEECH_SCRIPT, "fr-FR-DeniseNeural", rate="+3%")
    await comm.save(MP3_FILE)
    print(f"Fichier généré avec succès : {MP3_FILE} ({os.path.getsize(MP3_FILE)} octets)")

def play():
    print("Démarrage de la lecture vocale Windows...")
    wmp = win32com.client.Dispatch("WMPlayer.OCX")
    media = wmp.newMedia(MP3_FILE)
    wmp.currentMedia = media
    wmp.controls.play()

if __name__ == "__main__":
    asyncio.run(generate())
    if "--no-play" not in sys.argv:
        play()
