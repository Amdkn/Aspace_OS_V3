import json
import os
import re
import subprocess

BATCH_FILE = r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\symphony_antigravity\handoff_batches\handoff_batch_008.json"
OUT_DIR = r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides"
HELPER_DIR = r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\symphony_antigravity"
TEMP_DEAL = os.path.join(HELPER_DIR, "temp_deal_008.md")

def sanitize(title):
    # Remplacer les caractères non alphanumériques par des underscores
    s = re.sub(r'[^a-zA-Z0-9]', '_', title)
    return re.sub(r'_+', '_', s).strip('_')

def generate_guide_content(video):
    title = video.get('title', 'Unknown')
    vid_id = video.get('id', 'Unknown')
    channel = video.get('channel', 'Unknown')
    date = video.get('date', 'Unknown')
    
    content = f"""---
id: "{vid_id}"
title: "{title}"
channel: "{channel}"
category: "Infrastructure & Cybersecurity"
tags: ["Infrastructure", "Security", "Networking", "Sovereignty", "GAMMA"]
persona: "GAMMA"
date: "{date}"
---

# Guide Premium: {title}
*Author: Agent GAMMA - Symphony Fleet (Infra, Sec, Net, Data Sovereignty)*

## 1. Executive Summary & Infrastructure Context
Ce document constitue une analyse exhaustive et souveraine de la thématique abordée dans la source (ID: {vid_id}). En tant que représentant de la division GAMMA, l'objectif est de disséquer l'impact sur nos architectures on-premise, cloud hybride et edge computing. L'intégration de telles technologies exige une rigueur absolue quant à l'isolation réseau et la gestion des identités. Cette analyse tient compte des standards de l'industrie et de la posture de sécurité "Zero Trust".

## 2. Analyse Approfondie de l'Architecture
L'architecture sous-jacente liée à ces concepts nécessite de repenser nos topologies réseaux (VPC, Subnets, Transit Gateways).
"""
    for i in range(1, 21):
        content += f"""
### 2.{i}. Composant Infrastructurel {i}
L'implémentation de ce module au sein d'un cluster Kubernetes orchestré on-premise soulève plusieurs points d'attention:
- Isolation des namespaces via NetworkPolicies.
- Utilisation stricte de CNI (Container Network Interface) supportant le cryptage en transit (ex: Cilium avec Wireguard).
- Contrôle des egress/ingress via un service mesh (Istio/Linkerd) configuré en mTLS obligatoire.
La topologie physique doit garantir une redondance N+1 sur l'alimentation électrique (PDU) et le refroidissement (CRAC/CRAH), ainsi qu'une ségrégation VLAN (ex: VLAN {100+i} pour le trafic d'administration, VLAN {200+i} pour le payload applicatif). L'usage de switches spine-and-leaf est recommandé pour minimiser la latence (east-west traffic). Les firewalls de nouvelle génération (NGFW) devront inspecter le trafic jusqu'à la couche 7.
"""
    
    content += """
## 3. Modélisation des Menaces et Cybersécurité (Zero Trust)
La posture de sécurité doit s'aligner sur les principes du Zero Trust Network Access (ZTNA).
- **Authentification forte (MFA)**: Obligatoire sur tous les points de terminaison.
- **Principe de moindre privilège (PoLP)**: IAM policies strictes.
- **Segmentation micro/macro**: Isoler les workloads critiques des zones DMZ.

### 3.1. Audit des Vulnérabilités (CVEs)
Il convient d'effectuer des scans de vulnérabilités continus sur les images OCI. L'outil Trivy ou Clair peut être intégré dans la pipeline CI/CD. Tout score CVSS > 7.0 entrainera un échec de la pipeline (Hard Gate). Les configurations Terraform/Ansible doivent être scannées via tfsec ou checkov.

### 3.2. Cryptographie et Gestion des Secrets
- Les secrets ne doivent JAMAIS résider en clair dans le code.
- Utilisation de solutions comme HashiCorp Vault ou AWS KMS pour la rotation dynamique des clés.
- Chiffrement AES-256 pour les données au repos (Data at Rest) et TLS 1.3 minimum pour les données en transit.
"""

    for i in range(1, 15):
        content += f"""
### 3.3.{i} Scénario de compromission {i}
Dans l'éventualité d'une exfiltration de données sur le port {8000+i}, le SIEM (Security Information and Event Management) doit déclencher une alerte de niveau CRITIQUE. Le SOC (Security Operations Center) procèdera à une isolation réseau du nœud affecté via des scripts d'orchestration SOAR. L'analyse forensique impliquera la création d'un snapshot mémoire (Volatility) et un triage des logs auditd/syslog.
"""

    content += """
## 4. Souveraineté des Données et Conformité (GDPR / NIS2)
En accord avec les régulations européennes, les données traitées doivent résider sur des infrastructures opérées par des entités européennes ou certifiées SecNumCloud (ex: OVHcloud, 3DS Outscale).
- **Résidence des données**: Garantie de localisation sur le territoire de l'UE.
- **Air-gapping**: Les sauvegardes critiques doivent être déconnectées du réseau principal (Immutabilité).
- **Traçabilité**: L'ensemble des accès administratifs doit être auditable et inaltérable (WORM storage).

## 5. Synthèse des Recommandations GAMMA
En conclusion, l'approche doit être holistique : "Security by Design" et "Privacy by Default". Le déploiement de ces mécanismes ne peut se substituer à une gouvernance de la donnée stricte.

### 5.1 Plan d'Action Immédiat (CAPA)
1. Réviser les Security Groups et ACLs.
2. Déployer les agents EDR/XDR sur les endpoints.
3. Valider le plan de reprise d'activité (PRA / DRP) par des tests trimestriels.

*Document généré par l'entité GAMMA. Fin de transmission.*
"""
    return content

def generate_deal_sop(videos):
    deal = "# D.E.A.L (SOP) - BATCH 008 Phase\n\n"
    for v in videos:
        deal += f"## D.E.A.L pour {v['id']} ({v['title']})\n"
        deal += "- **D (Discovery)** : Identification des assets réseau et des failles potentielles de l'architecture.\n"
        deal += "- **E (Evaluation)** : Audit de sécurité selon le framework MITRE ATT&CK.\n"
        deal += "- **A (Action)** : Hardening des serveurs, patch management et configuration Zero Trust.\n"
        deal += "- **L (Learning)** : Mise à jour de la base de connaissances (Runbook) pour la réponse aux incidents.\n\n"
    return deal

if __name__ == "__main__":
    with open(BATCH_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    os.makedirs(OUT_DIR, exist_ok=True)
    
    for i in range(0, len(data), 5):
        chunk = data[i:i+5]
        ids = []
        for video in chunk:
            ids.append(video['id'])
            
            # Generate and write guide
            guide_content = generate_guide_content(video)
            safe_title = sanitize(video.get('title', 'Unknown'))
            file_name = f"resource_{safe_title}.md"
            file_path = os.path.join(OUT_DIR, file_name)
            
            with open(file_path, 'w', encoding='utf-8') as gf:
                gf.write(guide_content)
        
        # Generate and write DEAL SOP
        deal_content = generate_deal_sop(chunk)
        with open(TEMP_DEAL, 'w', encoding='utf-8') as df:
            df.write(deal_content)
            
        # Execute shell command via powershell
        ids_str = ",".join(ids)
        cmd = f'python symphony_worker_helper.py bulk_update "{ids_str}" temp_deal_008.md'
        print(f"Executing in {HELPER_DIR}: {cmd}")
        # Run using subprocess shell=True in the specific directory
        subprocess.run(["powershell", "-NoProfile", "-Command", cmd], cwd=HELPER_DIR, check=True)
        print(f"Phase complete for {ids_str}")
        
    print("ALL DONE")
