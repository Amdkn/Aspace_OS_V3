#!/usr/bin/env python3
import os
import sys
import argparse
import yaml
import json
import glob
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

# Définition des chemins canoniques de la forge
FORGE_ROOT = r"C:\Users\amado\ASpace_OS_V2"
AGENT_OS_DIR = os.path.join(FORGE_ROOT, ".agent-os")
NOTEBOOKLM_BRIDGE_SCRIPT = r"C:\Users\amado\.agent\skills\notebooklm-bridge\notebooklm_rpc.py"
PYTHON_EXE = r"C:\Python314\python.exe"

def init_env():
    """Initialise l'environnement et s'assure que les dossiers requis existent."""
    os.makedirs(os.path.join(AGENT_OS_DIR, "standards"), exist_ok=True)
    os.makedirs(os.path.join(AGENT_OS_DIR, "specs"), exist_ok=True)
    os.makedirs(os.path.join(AGENT_OS_DIR, "product"), exist_ok=True)
    os.makedirs(os.path.join(AGENT_OS_DIR, "dashboard"), exist_ok=True)
    
    # Créer un index.yml par défaut s'il n'existe pas
    index_path = os.path.join(AGENT_OS_DIR, "standards", "index.yml")
    if not os.path.exists(index_path):
        default_index = {
            "standards": [
                {
                    "id": "global/naming",
                    "description": "File naming, variable naming conventions and architecture structure",
                    "path": "global/naming.md"
                },
                {
                    "id": "api/response-format",
                    "description": "API response envelope structure, status codes and error formats",
                    "path": "api/response-format.md"
                }
            ]
        }
        with open(index_path, 'w', encoding='utf-8') as f:
            yaml.dump(default_index, f, default_flow_style=False)
        
        # Créer les fichiers markdown par défaut associés
        for std in default_index["standards"]:
            std_file = os.path.join(AGENT_OS_DIR, "standards", std["path"].replace("/", os.sep))
            os.makedirs(os.path.dirname(std_file), exist_ok=True)
            with open(std_file, 'w', encoding='utf-8') as sf:
                sf.write(f"# Standard {std['id']}\n\nDéfinissez vos règles ici pour la Sovereign Stack.")

def write_shape_spec():
    spec_template = """# Spec: [Nom de la Fonctionnalité]

## 1. Objectif & Portée
*Qu'est-ce que nous construisons ? Décrivez le changement ou la fonctionnalité.*

## 2. Visuels & Références
*Mockups, wireframes ou exemples d'implémentations existantes à référencer.*

## 3. Standards Appliqués
*Liste des standards injectés à respecter.*

## 4. Spécifications Techniques
*Détails techniques de l'implémentation (modèles de données, API, isolation).*
"""
    spec_file = os.path.join(AGENT_OS_DIR, "specs", "new_feature_spec.md")
    with open(spec_file, 'w', encoding='utf-8') as f:
        f.write(spec_template)
    return spec_file

class DashboardRequestHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def do_POST(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/api/save-content':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            payload = json.loads(post_data.decode('utf-8'))
            
            file_type = payload.get('type')
            file_id = payload.get('id')
            content = payload.get('content')
            
            file_id_norm = file_id.replace("/", os.sep)
            
            if file_type == 'standard':
                target_file = os.path.join(AGENT_OS_DIR, "standards", f"{file_id_norm}.md")
            elif file_type == 'spec':
                target_file = os.path.join(AGENT_OS_DIR, "specs", file_id_norm)
            else:
                self.send_response(400)
                self.end_headers()
                return
                
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(content)
                
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Fichier sauvegardé avec succès !"}).encode('utf-8'))
            return

    def do_GET(self):
        parsed_path = urlparse(self.path)
        
        # API : Lister les standards
        if parsed_path.path == '/api/standards':
            index_path = os.path.join(AGENT_OS_DIR, "standards", "index.yml")
            with open(index_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {"standards": []}
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data.get("standards", [])).encode('utf-8'))
            return
            
        # API : Lister les specs
        if parsed_path.path == '/api/specs':
            specs_dir = os.path.join(AGENT_OS_DIR, "specs")
            specs = []
            if os.path.exists(specs_dir):
                for filepath in glob.glob(os.path.join(specs_dir, "*.md")):
                    specs.append({
                        "name": os.path.basename(filepath),
                        "path": filepath
                    })
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(specs).encode('utf-8'))
            return

        # API : Récupérer le contenu d'un fichier
        if parsed_path.path == '/api/get-content':
            query = parse_qs(parsed_path.query)
            file_type = query.get('type', [None])[0]
            file_id = query.get('id', [None])[0]
            
            file_id_norm = file_id.replace("/", os.sep)
            
            if file_type == 'standard':
                target_file = os.path.join(AGENT_OS_DIR, "standards", f"{file_id_norm}.md")
            elif file_type == 'spec':
                target_file = os.path.join(AGENT_OS_DIR, "specs", file_id_norm)
            else:
                self.send_response(400)
                self.end_headers()
                return
                
            if os.path.exists(target_file):
                with open(target_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"content": content}).encode('utf-8'))
            else:
                if file_type == 'standard':
                    os.makedirs(os.path.dirname(target_file), exist_ok=True)
                    with open(target_file, 'w', encoding='utf-8') as sf:
                        sf.write(f"# Standard {file_id}\n\nDéfinissez vos règles ici.")
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"content": f"# Standard {file_id}\n\nDéfinissez vos règles ici."}).encode('utf-8'))
                else:
                    self.send_response(404)
                    self.end_headers()
            return
        
        # API : Ingestion / Liste des Notebooks via bridge
        if parsed_path.path == '/api/notebooklm/list':
            try:
                # Exécution synchrone courte du bridge Playwright
                result = subprocess.run([PYTHON_EXE, NOTEBOOKLM_BRIDGE_SCRIPT, 'list'], capture_output=True, text=True, encoding='utf-8', timeout=15)
                # Extraire le JSON de la sortie standard (la dernière ligne contient généralement le JSON [])
                lines = result.stdout.strip().split('\n')
                json_str = "[]"
                for line in reversed(lines):
                    if line.startswith('[') and line.endswith(']'):
                        json_str = line
                        break
                notebooks = json.loads(json_str)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "notebooks": notebooks}).encode('utf-8'))
            except Exception as e:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "expired", "notebooks": [], "error": str(e)}).encode('utf-8'))
            return

        # API : Connexion interactive NotebookLM
        if parsed_path.path == '/api/notebooklm/login':
            # Lance le script de login en arrière-plan sans bloquer le serveur web
            subprocess.Popen([PYTHON_EXE, NOTEBOOKLM_BRIDGE_SCRIPT, 'login'])
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Navigateur de connexion Google ouvert. Connectez-vous, puis fermez le navigateur pour persister la session."}).encode('utf-8'))
            return

        # API : Injecter un nouveau standard
        if parsed_path.path == '/api/inject':
            query = parse_qs(parsed_path.query)
            std_id = query.get('id', [None])[0]
            if std_id:
                index_path = os.path.join(AGENT_OS_DIR, "standards", "index.yml")
                with open(index_path, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f) or {"standards": []}
                
                standards = data.get("standards", [])
                found = False
                for std in standards:
                    if std['id'] == std_id:
                        found = True
                        break
                if not found:
                    standards.append({
                        "id": std_id,
                        "description": f"Standard auto-créé pour {std_id}",
                        "path": f"{std_id}.md"
                    })
                    data["standards"] = standards
                    with open(index_path, 'w', encoding='utf-8') as f:
                        yaml.dump(data, f, default_flow_style=False)
                    
                    std_file = os.path.join(AGENT_OS_DIR, "standards", std_id.replace("/", os.sep) + ".md")
                    os.makedirs(os.path.dirname(std_file), exist_ok=True)
                    with open(std_file, 'w', encoding='utf-8') as sf:
                        sf.write(f"# Standard {std_id}\n\nDéfinissez vos règles ici pour la Sovereign Stack.")
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"message": f"Standard {std_id} injecté avec succès !"}).encode('utf-8'))
            else:
                self.send_response(400)
                self.end_headers()
            return

        # API : Shape-spec
        if parsed_path.path == '/api/shape':
            write_shape_spec()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Shape-spec initié et template new_feature_spec.md créé !"}).encode('utf-8'))
            return

        # Servir index.html
        if parsed_path.path in ('/', '/index.html'):
            html_path = os.path.join(AGENT_OS_DIR, "dashboard", "index.html")
            if os.path.exists(html_path):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                with open(html_path, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.end_headers()
            return

        self.send_response(404)
        self.end_headers()

def start_server(port=6677):
    init_env()
    server = HTTPServer(('localhost', port), DashboardRequestHandler)
    print(f"=== [Agent OS Dashboard] ===")
    print(f"Interface graphique lancée avec succès.")
    print(f"URL locale : http://localhost:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServeur arrêté.")

def cmd_shape_spec():
    print("=== [Agent OS / Antigravity] - SHAPE SPEC ===")
    spec_file = write_shape_spec()
    print(f"Modèle de spécification créé avec succès dans : {spec_file}")

def main():
    init_env()
    parser = argparse.ArgumentParser(description="Agent OS & Antigravity Sovereign Bridge")
    subparsers = parser.add_subparsers(dest="command", help="Commandes disponibles")
    subparsers.add_parser("shape-spec", help="Initier le shaping de spécification")
    subparsers.add_parser("serve", help="Lancer le front-end sur localhost:6677")
    
    args = parser.parse_args()
    if args.command == "shape-spec":
        cmd_shape_spec()
    elif args.command == "serve":
        start_server(6677)
    else:
        start_server(6677)

if __name__ == "__main__":
    main()
