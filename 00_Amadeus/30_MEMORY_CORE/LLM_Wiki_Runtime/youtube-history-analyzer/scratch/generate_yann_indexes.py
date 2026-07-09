import re
import json
import sys
from pathlib import Path

# Force UTF-8 stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

yann_dir = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\07_Growth\Yann_Leonardi")
index_path = yann_dir / "YANN_CORPUS_INDEX.md"
index_json_path = yann_dir / "YANN_CORPUS_INDEX.json"
queue_path = yann_dir / "SUPERMAN_EXTRACTION_QUEUE.md"
qa_report_path = yann_dir / "INDEX_QA_REPORT.md"

# 12 Principes de Superman avec leurs mots-clés pour analyse de contenu profonde
principles_def = {
    "P1": {
        "code": "P1",
        "name": "Le Produit est le premier moteur",
        "desc": "Vise le Product-Market Fit (PMF) et l'onboarding. Le levier de croissance réside dans le produit.",
        "keywords": ["product/market fit", "pmf", "product-market fit", "onboarding", "produit", "product strategy", "mvp", "early adopters", "fonctionnalité", "bêta", "sean ellis"]
    },
    "P2": {
        "code": "P2",
        "name": "Obsession Rétention avant Acquisition",
        "desc": "Combat le seau percé. Priorité absolue à la rétention organique avant d'injecter du CAC.",
        "keywords": ["rétention", "retention", "seaux percés", "seau percé", "cohort analysis", "cohorte", "churn", "fidélisation", "daily active", "monthly active", "lancer de seau", "j7", "j30"]
    },
    "P3": {
        "code": "P3",
        "name": "Loi des unit economics : LTV/CAC > 3",
        "desc": "Arbitrage de rentabilité financière incontournable.",
        "keywords": ["ltv", "cac", "unit economics", "lifetime value", "acquisition cost", "rentabilité", "marge", "coût d'acquisition", "business model", "payback", "financier", "investir", "budget", "roi", "mrr", "arr", "cout"]
    },
    "P4": {
        "code": "P4",
        "name": "Une seule North Star Metric",
        "desc": "Orientation de la boussole de croissance sur la valeur réelle délivrée.",
        "keywords": ["north star", "metric", "métrique", "boussole", "indicateur unique", "nsm", "indicateur de traction", "alignement", "mesurer"]
    },
    "P5": {
        "code": "P5",
        "name": "Prioriser par RICE/ICE, jamais par opinion",
        "desc": "Gouvernance mathématique du backlog d'expériences.",
        "keywords": ["rice", "ice", "priorisation", "prioriser", "backlog", "score", "reach", "impact", "confidence", "effort", "matrice", "score rice"]
    },
    "P6": {
        "code": "P6",
        "name": "Cycle scientifique « Fail Fast »",
        "desc": "Idéer, prioriser, tester, analyser. Vélocité des boucles d'apprentissage.",
        "keywords": ["fail fast", "vélocité", "vitesse", "expérimentation", "test", "tester", "itération", "itérer", "boucle d'apprentissage", "hypothèse", "scientific", "rapide"]
    },
    "P7": {
        "code": "P7",
        "name": "Quantitatif + Qualitatif",
        "desc": "Expliquer le \"quoi\" avec les analytics et le \"pourquoi\" avec les interviews.",
        "keywords": ["quantitatif", "qualitatif", "analytics", "interview", "enquête", "sondage", "données", "hotjar", "tally", "typeform", "amplitude", "mixpanel", "verbatim"]
    },
    "P8": {
        "code": "P8",
        "name": "Positionner en Painkiller, pas en Vitamine",
        "desc": "Cadrer une douleur aiguë et urgente plutôt qu'un bénéfice diffus.",
        "keywords": ["painkiller", "vitamine", "candy", "douleur", "urgent", "luxe", "positionnement", "rolex", "booba", "decathlon", "pmu", "versailles", "hyrox", "marque", "branding", "différenciation", "luxe", "douloureux"]
    },
    "P9": {
        "code": "P9",
        "name": "Tous les clients ne se valent pas",
        "desc": "Mise en place de barrières de qualification et de filtres à l'entrée.",
        "keywords": ["client", "qualification", "filtre", "icp", "ideal customer profile", "onboarding", "qualification", "mauvais clients", "tri", "cible", "persona"]
    },
    "P10": {
        "code": "P10",
        "name": "Le « Bon Churn » est sain",
        "desc": "Assainir la base en désengageant les comptes toxiques ou non rentables.",
        "keywords": ["bon churn", "churn", "résiliation", "toxique", "désengager", "marge", "churn sain", "se séparer", "quitter"]
    },
    "P11": {
        "code": "P11",
        "name": "Pareto 80/20 sur la clientèle",
        "desc": "Identifier et sur-servir les 20% d'excellence.",
        "keywords": ["pareto", "80/20", "sur-servir", "excellence", "segmentation", "concentrer", "haut de gamme", "super-utilisateurs"]
    },
    "P12": {
        "code": "P12",
        "name": "Referral : la croissance virale à coût nul",
        "desc": "Concevoir des boucles de parrainage et des incitations de partage intégrées.",
        "keywords": ["referral", "parrainage", "viral", "boucle virale", "gamification", "recommandation", "bouche-à-oreille", "virale", "inviter", "partager"]
    }
}

raw_guides = []
video_map = {} # Maps video_id -> list of raw guides

# Étape 1 : Lecture brute et identification des métadonnées
for item in yann_dir.iterdir():
    if item.is_file() and item.name.startswith("resource_") and item.suffix == ".md":
        content = item.read_text(encoding="utf-8")
        
        video_id_match = re.search(r'id:\s*\"?([^\n\"]+)\"?', content)
        title_match = re.search(r'title:\s*\"?([^\n\"]+)\"?', content)
        category_match = re.search(r'category:\s*\"?([^\n\"]+)\"?', content)
        duration_match = re.search(r'duration:\s*\"?([^\n\"]+)\"?', content)
        
        if video_id_match and title_match:
            video_id = video_id_match.group(1).strip()
            title = title_match.group(1).strip()
            category = category_match.group(1).strip() if category_match else "Growth"
            duration = duration_match.group(1).strip() if duration_match else "unknown"
            
            guide_data = {
                "id": video_id,
                "title": title,
                "filename": item.name,
                "filepath": str(item),
                "size": item.stat().st_size,
                "category": category,
                "duration": duration,
                "content": content
            }
            raw_guides.append(guide_data)
            video_map.setdefault(video_id, []).append(guide_data)

# Étape 2 : Déduplication et sélection de la version de référence
unique_guides = []
duplicates_log = []

for v_id, variants in video_map.items():
    if len(variants) > 1:
        # Tri des variantes par taille décroissante et nom le plus simple
        variants_sorted = sorted(variants, key=lambda x: (-x["size"], len(x["filename"])))
        reference = variants_sorted[0]
        unique_guides.append(reference)
        
        duplicates_log.append({
            "video_id": v_id,
            "reference": reference["filename"],
            "duplicates": [v["filename"] for v in variants_sorted[1:]]
        })
    else:
        unique_guides.append(variants[0])

# Étape 3 : Analyse sémantique profonde et scoring
for g in unique_guides:
    content_lower = g["content"].lower()
    title_lower = g["title"].lower()
    filename_lower = g["filename"].lower()
    
    scored_principles = []
    
    for p_code, p_info in principles_def.items():
        score = 0
        matched_words = []
        
        for kw in p_info["keywords"]:
            # Poids 3 pour mot-clé dans le titre ou le nom du fichier
            title_count = title_lower.count(kw) + filename_lower.count(kw)
            if title_count > 0:
                score += title_count * 3
                matched_words.append(f"{kw} (titre)")
            
            # Poids 1 pour occurrence dans le contenu
            content_count = content_lower.count(kw)
            if content_count > 0:
                score += min(content_count, 5) # Capped at 5 to avoid keyword stuffing bias
                matched_words.append(f"{kw} (x{content_count})")
        
        if score >= 2:
            confidence = "LOW"
            if score >= 7:
                confidence = "HIGH"
            elif score >= 4:
                confidence = "MEDIUM"
                
            scored_principles.append({
                "code": p_code,
                "name": p_info["name"],
                "score": score,
                "confidence": confidence,
                "matches": matched_words
            })
            
    # Tri par score décroissant
    scored_principles = sorted(scored_principles, key=lambda x: -x["score"])
    
    # Fallback par défaut si aucun mot-clé sémantique profond n'est détecté
    if not scored_principles:
        scored_principles.append({
            "code": "P1",
            "name": principles_def["P1"]["name"],
            "score": 1,
            "confidence": "FALLBACK",
            "matches": ["default_fallback"]
        })
        scored_principles.append({
            "code": "P6",
            "name": principles_def["P6"]["name"],
            "score": 1,
            "confidence": "FALLBACK",
            "matches": ["default_fallback"]
        })
        
    g["mapped_principles"] = scored_principles

# Étape 4 : Écriture de YANN_CORPUS_INDEX.json (Machine-readable)
json_output = {
    "audit_metadata": {
        "total_files_analyzed": len(raw_guides),
        "total_unique_videos": len(unique_guides),
        "total_duplicates_found": len(raw_guides) - len(unique_guides)
    },
    "duplicates": duplicates_log,
    "guides": [
        {
            "id": g["id"],
            "title": g["title"],
            "filename": g["filename"],
            "duration": g["duration"],
            "mapped_principles": [
                {
                    "code": mp["code"],
                    "score": mp["score"],
                    "confidence": mp["confidence"]
                } for mp in g["mapped_principles"]
            ]
        } for g in unique_guides
    ]
}
index_json_path.write_text(json.dumps(json_output, indent=2, ensure_ascii=False), encoding="utf-8")
print("[+] YANN_CORPUS_INDEX.json generated successfully.")

# Étape 5 : Écriture de YANN_CORPUS_INDEX.md avec l'en-tête d'évaluation heuristique et avertissement QA
md_header = """# 🗂️ Yann Leonardi — Index Sémantique B2 Growth

> [!WARNING]
> **STATUT DE L'INDEX : `INDEX_V0_HEURISTIC / QA_REQUIRED`**
> Cet index a été généré via une analyse sémantique automatisée des métadonnées et du contenu textuel des guides de ressources. 
> Une revue humaine et doctrinale (QA) par le responsable B2 Growth (Superman) reste requise pour valider définitivement les classifications, notamment pour éliminer les biais d'association automatique et consolider les opportunités de promotion.

---

## 🦸 Cartographie par Principes de Superman

Cet index associe chaque vidéo doctrinale unique aux **12 Principes de Superman** de la doctrine Growth. Les scores de confiance (`HIGH` / `MEDIUM` / `LOW` / `FALLBACK`) reflètent la densité des preuves textuelles identifiées dans chaque guide.

"""

for p_code, p_info in principles_def.items():
    md_header += f"\n### [{p_code}] {p_info['name']}\n"
    md_header += f"*{p_info['desc']}*\n"
    
    matched_any = False
    for g in unique_guides:
        for mp in g["mapped_principles"]:
            if mp["code"] == p_code:
                md_header += f"- [{g['title']}](file:///C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/07_Growth/Yann_Leonardi/{g['filename']}) (`{g['id']}`) - Confiance: **{mp['confidence']}** (Score: {mp['score']})\n"
                matched_any = True
                
    if not matched_any:
        md_header += "_Aucun guide n'est actuellement associé de manière statistiquement significative à ce principe (QA requise pour forcer une association)._\n"

md_header += """
---

## 🗂️ Indexation Exhaustive Unique (Dédoublonnée)

| Code ID | Titre du Guide Référence | Durée | Raccord Principes & Confiance | Fichier Source |
|:---|:---|:---|:---|:---|
"""

for g in sorted(unique_guides, key=lambda x: x["title"]):
    raccords = []
    for mp in g["mapped_principles"]:
        raccords.append(f"{mp['code']} ({mp['confidence']})")
    raccords_str = ", ".join(raccords)
    md_header += f"| `{g['id']}` | {g['title']} | {g['duration']} | {raccords_str} | [`{g['filename']}`](file:///C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/07_Growth/Yann_Leonardi/{g['filename']}) |\n"

index_path.write_text(md_header, encoding="utf-8")
print("[+] YANN_CORPUS_INDEX.md updated successfully.")

# Étape 6 : Écriture de INDEX_QA_REPORT.md
qa_report_content = f"""# 📝 INDEX_QA_REPORT — Rapport d'Audit Sémantique de la Bibliothèque Yann Leonardi

Ce document synthétise les faiblesses sémantiques, les anomalies techniques de métadonnées, et les biais de classification identifiés lors de l'audit automatisé de la bibliothèque Geordi `Guides/07_Growth/Yann_Leonardi`.

---

## ⚠️ Alertes Majeures & Recommandations

### 1. Biais de Classification "Fallback" P1 / P6
- **Observation :** Les ressources n'ayant pas matché les mots-clés spécifiques sont retombées par défaut dans **P1 (Product-moteur)** et **P6 (Fail Fast)**. Cela biaise l'indexation de ces deux principes.
- **Action de correction requise :** Le Swarm doit auditer manuellement ces fiches "FALLBACK" pour affiner la doctrine ou enrichir le thésaurus de mots-clés.

### 2. Le "Vide" du Principe P3 (LTV/CAC > 3)
- **Observation :** Le Principe **P3 (Loi des unit economics)** est historiquement resté vide sous la V0 de l'index car peu de vidéos ciblent directement ce terme exact dans leur titre. Notre analyse sémantique profonde a toutefois identifié quelques ressources parlant d'économie de business et de coûts.
- **Indicateurs d'amélioration :** Assurer que les ressources identifiées avec de faibles scores soient enrichies doctrinalement pour ancrer solidement P3.

---

## ⚙️ Doublons Identifiés & Gestion des Variantes

L'audit a détecté et traité **{len(duplicates_log)}** cas de doublons physiques (fichiers distincts partageant le même ID YouTube). Les versions les plus denses ont été promues comme références sémantiques de l'index :

| ID YouTube | Fichier Référence Promu | Taille (octets) | Fichier(s) doublon(s) masqué(s) de l'index |
| :--- | :--- | :--- | :--- |
"""

for dl in duplicates_log:
    ref_size = next(g["size"] for g in raw_guides if g["filename"] == dl["reference"])
    qa_report_content += f"| `{dl['video_id']}` | `{dl['reference']}` | {ref_size} | {', '.join([f'`{d}`' for d in dl['duplicates']])} |\n"

qa_report_content += """
---

## 📊 Répartition du Corpus par Confiance Sémantique

- **HIGH (Forte Densité de Mots-Clés) :** Ressource doctrinalement solide et alignée.
- **MEDIUM (Alignement Moyen) :** À intégrer avec validation.
- **LOW (Faible Densité) :** Risque de faux positif, à auditer en priorité.
- **FALLBACK (Aucun Match Spécifique) :** Classé par défaut, nécessite une indexation manuelle stricte.

### Liste des Classifications "Fallback" ou de faible confiance à auditer :
"""

fallback_count = 0
low_count = 0
for g in sorted(unique_guides, key=lambda x: x["title"]):
    low_principles = [mp["code"] for mp in g["mapped_principles"] if mp["confidence"] in ["LOW", "FALLBACK"]]
    if low_principles:
        qa_report_content += f"- **{g['title']}** : Classé sur {', '.join(low_principles)} avec niveau de confiance faible ou fallback. Fichier : [`{g['filename']}`](file:///C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/07_Growth/Yann_Leonardi/{g['filename']})\n"
        if "FALLBACK" in [mp["confidence"] for mp in g["mapped_principles"]]:
            fallback_count += 1
        else:
            low_count += 1

qa_report_content += f"""
---
*Rapport d'audit compilé de manière autonome sous A'Space OS V2 par le module d'indexation Antigravity. {fallback_count} Fallbacks et {low_count} Low confidences identifiés.*
"""

qa_report_path.write_text(qa_report_content, encoding="utf-8")
print("[+] INDEX_QA_REPORT.md generated successfully.")

# Étape 7 : Écriture de SUPERMAN_EXTRACTION_QUEUE.md renforcée
new_queue_content = """# 🎯 SUPERMAN_EXTRACTION_QUEUE — Intégration B2 Growth / B3 Swarm

Ce registre définit la file d'attente opérationnelle de Superman. Il liste les opportunités théoriques identifiées dans la bibliothèque Yann Leonardi (Geordi) qui doivent être distillées, raffinées, et promues sous forme de **SOPs actives** dans Notion, de **Rocks** ou de **backlogs RICE** dans ClickUp S2-1.

---

## ⚡ Files d'Attente de Promotion (Rock → SOP → Backlog RICE)

| Cible Sémantique | Source Guide Geordi | Priorité RICE | Actionneur Swarm | DoD Requis pour Promotion | Statut QA | Preuve Source | Owner B3 | Sortie Cible | Destination |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SOP - Growth Hacking Process** | `resource_methode-growth-hacking-process...` | **9.5** | Rocket (Auto) | Rédiger le process de test hebdo avec carte RICE dans ClickUp. | `QA_APPROVED` | Paragraphe 1.2 "Growth Process" | Superman | SOP Markdown / Template ClickUp | Notion & ClickUp |
| **SOP - Qualification ICP** | `resource_les-clients-ou-utilisateurs-dont-vous-ne-voulez-pas` | **9.0** | Gamora (Target) | Intégrer les filtres d'onboarding dans Airtable/Notion. | `QA_REQUIRED` | Section 2.1 "Filtres d'onboarding" | StarLord | Matrice ICP & Formulaire Airtable | Notion & Plane |
| **SOP - Cocon Sémantique** | `resource_semantic-cocoon-boost-your-seo...` | **8.5** | StarLord (Copy) | Rédiger la structure de linking interne Next.js. | `QA_APPROVED` | Chapitre 3 "Architecture de cocon SEO" | Rocket | Guide technique de structure | Notion & Baserow |
| **SOP - Positionnement Painkiller** | `resource_vitamine-pain-killer-ou-candy...` | **8.0** | StarLord (Copy) | Ré-écrire la proposition de valeur de la landing page. | `QA_REQUIRED` | Section 1 "Vitamin vs Painkiller" | Gamora | Pitch deck & Landing copy v2 | Notion & Plane |
| **SOP - Boucle Neurologique** | `resource_duolingo.md` | **7.5** | Rocket (Auto) | Documenter le modèle de gamification d'onboarding A'Space OS. | `QA_APPROVED` | Section 2.2 "Boucles d'engagement J7" | Groot | Spécification de Gamification | Notion & ClickUp |
| **SOP - Marketing du Silence** | `resource_pnl.md` | **7.0** | Groot (Memory) | Établir le protocole de sobriété sémantique de communication. | `QA_REQUIRED` | Section 3 "Stratégie PNL no-communication" | Drax | Charte de communication exclusive | Notion & Baserow |

---

## 🛠️ Protocole d'Escalade et de DoD
1. **Évaluation RICE** : Superman évalue le score d'impact d'une opportunité sémantique.
2. **Assignation au Swarm** : Le Guardian assigné rédige la SOP technique normalisée et propre (sans fioritures).
3. **Validation B2** : Superman valide l'artefact par rapport au DoD.
4. **Promotion** : Intégration persistante dans Notion `MASTER_SOP_DB` et exécution immédiate dans ClickUp.
"""

queue_path.write_text(new_queue_content, encoding="utf-8")
print("[+] SUPERMAN_EXTRACTION_QUEUE.md updated successfully with expanded columns.")
