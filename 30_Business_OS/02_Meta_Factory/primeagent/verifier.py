#!/usr/bin/env python3
# -*- coding: ascii -*-
"""Verificateur PrimeAgent v0.

Spec : 00_Amadeus/60_Tape_Specs/2026-09-04-spec-primeagent-v0.md
Genere une franchise de test dans un tmpdir, verifie l'arborescence,
l'idempotence protectrice et le rc d'usage.
Sortie : PRIMEAGENT_OK (rc=0) ou PRIMEAGENT_KO (rc=1).
"""

import sys
import os
import json
import tempfile
import shutil
import subprocess

DOMAINES = ["growth", "sales", "product", "ops", "it",
            "finance", "people", "legal"]

DOSSIERS = ["01_Growth", "02_Sales", "03_Product", "04_Ops",
            "05_IT", "06_Finance", "07_People", "08_Legal"]

ERREURS = []


def erreur(detail):
    ERREURS.append("  ERREUR: " + detail)


def main():
    ici = os.path.dirname(os.path.abspath(__file__))
    generateur = os.path.join(ici, "agent-template.py")
    if not os.path.isfile(generateur):
        print("PRIMEAGENT_KO")
        print("  ERREUR: agent-template.py absent de " + ici)
        return 1

    tmpdir = tempfile.mkdtemp()
    try:
        # 2. Generation d'une franchise de test
        r = subprocess.run([sys.executable, generateur, "Franchise Test", tmpdir],
                           capture_output=True, text=True)
        if r.returncode != 0:
            erreur("generation rc=%s (attendu 0), stderr=%s"
                   % (r.returncode, r.stderr.strip()))
        dossier = os.path.join(tmpdir, "franchise-test")
        if not os.path.isdir(dossier):
            erreur("dossier franchise-test absent dans le tmpdir")

        # 3. Verification de l'arborescence
        for d in DOSSIERS:
            if not os.path.isdir(os.path.join(dossier, d)):
                erreur("dossier de domaine absent: " + d)

        chemin_json = os.path.join(dossier, "franchise.json")
        contenu_json_avant = None
        try:
            with open(chemin_json, "r", encoding="utf-8") as f:
                contenu_json_avant = f.read()
            donnees = json.loads(contenu_json_avant)
            if donnees.get("nom") != "Franchise Test":
                erreur("franchise.json: nom != 'Franchise Test'")
            if donnees.get("slug") != "franchise-test":
                erreur("franchise.json: slug != 'franchise-test'")
            if donnees.get("domaines") != DOMAINES:
                erreur("franchise.json: domaines != liste des 8 domaines B2")
            if not donnees.get("cree"):
                erreur("franchise.json: champ 'cree' vide")
            if donnees.get("statut") != "v0-initialise":
                erreur("franchise.json: statut != 'v0-initialise'")
        except (OSError, ValueError) as e:
            erreur("franchise.json illisible ou JSON invalide: %s" % e)

        try:
            with open(os.path.join(dossier, "README.md"), "r",
                      encoding="utf-8") as f:
                racine = f.read()
            if not racine.strip():
                erreur("README racine du slug vide")
            else:
                if "# Franchise Test" not in racine:
                    erreur("README racine: titre '# Franchise Test' absent")
                if "statut: v0-initialise" not in racine:
                    erreur("README racine: 'statut: v0-initialise' absent")
        except OSError as e:
            erreur("README racine illisible: %s" % e)

        for d in DOSSIERS:
            titre = d.split("_", 1)[1]
            chemin = os.path.join(dossier, d, "README.md")
            try:
                with open(chemin, "r", encoding="utf-8") as f:
                    contenu = f.read()
                if not contenu.strip():
                    erreur("README du domaine %s vide" % d)
                elif "# Franchise Test - %s" % titre not in contenu:
                    erreur("README du domaine %s: titre '# Franchise Test - %s' absent"
                           % (d, titre))
            except OSError as e:
                erreur("README du domaine %s illisible: %s" % (d, e))

        # 4. Test d'echec propre (idempotence protectrice)
        r2 = subprocess.run([sys.executable, generateur, "Franchise Test", tmpdir],
                            capture_output=True, text=True)
        if r2.returncode == 0:
            erreur("re-generation sur franchise existante: rc=0 (attendu != 0)")
        try:
            with open(chemin_json, "r", encoding="utf-8") as f:
                apres = f.read()
            if contenu_json_avant is not None and apres != contenu_json_avant:
                erreur("franchise.json modifie par la re-generation (invariant viole)")
        except OSError as e:
            erreur("franchise.json illisible apres re-generation: %s" % e)

        # 5. Test usage : sans argument, rc attendu 2
        r3 = subprocess.run([sys.executable, generateur],
                            capture_output=True, text=True)
        if r3.returncode != 2:
            erreur("invocation sans argument: rc=%s (attendu 2)" % r3.returncode)
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

    if ERREURS:
        print("PRIMEAGENT_KO")
        for e in ERREURS:
            print(e)
        return 1
    print("PRIMEAGENT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
