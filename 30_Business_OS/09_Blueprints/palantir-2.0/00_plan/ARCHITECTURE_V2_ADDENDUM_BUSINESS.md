# Architecture V2 — Addendum Business : Cartographie Multi-Tenant & Moteur d'Affiliation

**Emplacement :** `C:\Users\amado\ASpace_OS_V3\30_Business_OS\09_Blueprints\palantir-2.0\00_plan\ARCHITECTURE_V2_ADDENDUM_BUSINESS.md`

**Rôle :** Spécification de la Modélisation Métier, de la Taxonomie Multi-Tenant (Niveaux 0 à 3) et du Moteur d'Affiliation Financière.

**Ancrage :** Addendum applicatif au noyau technique `ARCHITECTURE_V2.md` (Rang 6 — Émulateur Palantir 2.0). Consomme l'infrastructure via FastMCP / REST. **Aucun risque de régression** sur le noyau technique.

**Statut :** OPTION B (Gemini 8) — séparé du plan V2 pour ne pas polluer le contexte du moteur technique. Contient les corrections Gemini 9 (SHACL-SPARQL valide, deadline persistante).

---

## 1. Vision & Séparation des Couches

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              COUCHE BUSINESS & COMMERCIAL (CE ADDENDUM)                     │
│    Modèle d'Affiliation, Niveaux de Clientèle 0-3, Paliers SaaS & OSP       │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ (Consomme via FastMCP / REST)
                                       v
┌─────────────────────────────────────────────────────────────────────────────┐
│              NOYAU TECHNIQUE PALANTIR 2.0 (ARCHITECTURE_V2.md)              │
│    Ontology Engine, PySHACL, Branching Sandbox, AI FDE, LangGraph, SQLite   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Taxonomie des Niveaux de Clientèle (Tiering 0 à 3)

| Niveau | Rôle Métier | Prix SaaS / Mois | Modèle d'Affiliation & Seuil de Rentabilité | Périmètre d'Action & OSP |
| --- | --- | --- | --- | --- |
| **Level 0** | **Amadeus / A'Space OS** *(Client Racine / Architecte)* | **$0** *(Propriétaire)* | **Auto-Réplication (Loi L0)**. Encaissement global des flux SaaS et distribution des crédits d'affiliation. | **System Root Admin** : Contrôle du métamodèle, accès complet au graphe d'ontologie, réplication du système et gestion des tenants. |
| **Level 1** | **Coaches & Consultants** *(Conseillers de CEOs)* | **$1,500 / mois** | **+$500 / mois** par CEO affilié. **3 CEOs = $0/mois** (Gratuité totale). **4+ CEOs = +$500/mois de profit net**. | **Multi-Tenant Coach View** : Dashboard d'audit des Ontologies des CEOs conseillés. Création de scénarios d'optimisation d'entreprise. |
| **Level 2** | **CEOs & Dirigeants** *(Opérateurs d'Entreprise)* | **$1,000 / mois** | **+$250 / mois** par membre d'équipe affilié. Déduction directe sur la facture du CEO. | **Enterprise Cockpit** : Contrôle de l'Ontologie d'Entreprise, des pipelines de données, validation et fusion (`Approve & Merge`) des scénarios. |
| **Level 3** | **Membres d'Équipe** *(Exécuteurs Opérationnels)* | **$750 / mois** | **Remises cumulées** et crédits d'utilisation à partir du 5e membre affilié dans le même tenant. | **Task Bounded Scope** : Accès strictement limité aux objets métiers attribués. Modification du schéma globale interdite. |

---

## 3. Spécification Ontologique Protégé (`Aspace_Core.owl`) — Classes Métier

* `aspace:ClientTier` *(Super-classe)*
* `aspace:Level0_Architect`
* `aspace:Level1_Coach`
* `aspace:Level2_CEO`
* `aspace:Level3_TeamMember`
* `aspace:AffiliationContract` *(traçabilité des parrainages)*
* `aspace:SaaSInvoice` *(états de facturation et crédits)*

### Data & Object Properties

* `aspace:hasSaaSPlan` (`domain`: `ClientTier`, `range`: `xsd:decimal`)
* `aspace:affiliatedBy` (`domain`: `ClientTier`, `range`: `ClientTier`)
* `aspace:referralCredit` (`domain`: `ClientTier`, `range`: `xsd:decimal`)
* `aspace:activeAffiliatesCount` (`domain`: `ClientTier`, `range`: `xsd:integer`)
* `aspace:effectiveSaaSFee` (`domain`: `ClientTier`, `range`: `xsd:decimal`)
* `aspace:clarificationDeadline` *(Gemini 9 — correction)* — timestamp ISO 8601 stocké dans `ont_scenarios` pour persister le timer 15-min à travers les redémarrages du serveur

---

## 4. Règles SHACL — Correction Gemini 9 (syntaxe valide)

> **Erreur Gemini 9 :** les chaînes `"IF ... THEN ..."` ne sont pas du SHACL valide. PySHACL ne sait pas les interpréter.
>
> **Correctif :** utiliser `sh:select` (SPARQL natif) pour les contraintes de structure, et calculer l'arithmétique d'affiliation **dans `defineTool.py`** (Python natif), pas en SHACL.

### 4.1. SHACL-SPARQL pour contraintes de structure

```turtle
# Contrainte : tout ClientTier doit avoir un hasSaaSPlan >= 0
aspace:ClientTierPlanShape a sh:NodeShape ;
    sh:targetClass aspace:ClientTier ;
    sh:property [
        sh:path aspace:hasSaaSPlan ;
        sh:datatype xsd:decimal ;
        sh:minInclusive 0 ;
        sh:message "hasSaaSPlan doit être >= 0" ;
    ] .

# Contrainte : activeAffiliatesCount >= 0
aspace:AffiliatesCountShape a sh:NodeShape ;
    sh:targetClass aspace:ClientTier ;
    sh:property [
        sh:path aspace:activeAffiliatesCount ;
        sh:datatype xsd:integer ;
        sh:minInclusive 0 ;
        sh:message "activeAffiliatesCount doit être >= 0" ;
    ] .

# Règle SPARQL : Level 1 (Coach) ne peut avoir QUE des Level 2 (CEO) affiliés
aspace:CoachAffiliationShape a sh:NodeShape ;
    sh:targetClass aspace:Level1_Coach ;
    sh:sparql [
        a sh:SPARQLConstraint ;
        sh:message "Un Coach ne peut affilier QUE des CEOs (Level 2)" ;
        sh:select """
            SELECT $this ?affiliate WHERE {
                $this aspace:affiliatedBy ?aff .
                ?aff rdf:type ?affType .
                FILTER (?affType != aspace:Level2_CEO)
            }
        """ ;
    ] .
```

### 4.2. Arithmétique d'affiliation — Python natif (`defineTool.py`)

**PAS** en SHACL. Calculs dans `affiliation.calculate_statement()` :

```python
# 30_emulateur/defineTool.py — Rang 7 (futur)

def calculate_statement(client_id: str, active_affiliates_count: int, tier: int) -> dict:
    """Calcule effectiveSaaSFee et payoutAmount selon le tier."""
    if tier == 1:  # Coach
        if active_affiliates_count >= 3:
            effective_fee = 0.0
            payout = (active_affiliates_count - 3) * 500.0
        else:
            effective_fee = 1500.0 - (active_affiliates_count * 500.0)
            payout = 0.0
    elif tier == 2:  # CEO
        # effectif_level3_count passé en paramètre
        effective_fee = max(0.0, 1000.0 - (active_level3_count * 250.0))
        payout = 0.0
    else:  # Level 0 ou Level 3
        effective_fee = 0.0
        payout = 0.0
    return {"effectiveSaaSFee": effective_fee, "payoutAmount": payout}
```

---

## 5. Matrice AI FDE Level-Aware (`ai_fde/loop.py`)

| Niveau | Portée des Scénarios | Mode de Validation |
| --- | --- | --- |
| **Level 0** | Métamodèle, Réplication OS, Logistique & Multi-Tenant | Direct Commit ou Auto-Approval |
| **Level 1** | Audit Multi-Entreprises, Scénarios Conseils CEOs | Validation Requise par le Coach avant soumission au CEO |
| **Level 2** | Ontologie d'Entreprise, Pipelines, Re-organisation | Validation Humaine Obligatoire via `Approve & Merge` (Level 2) |
| **Level 3** | Exécution de Tâches, Mises à jour d'Instances | Restreint aux Workflows Locaux. Interdiction de modifier le Schéma |

---

## 6. Assumption-Based Branching (Mode 0-Humain) — Correction Gemini 9 (deadline persistante)

> **Erreur Gemini 9 :** timer 15 minutes en RAM volatile. Si serveur redémarré, branche jamais créée.
>
> **Correctif :** `clarification_deadline` (timestamp ISO 8601) stocké dans `ont_scenarios` au moment où la clarification est demandée. Cron Python (ou boucle coordinateur) vérifie la table et déclenche le branching si `now() > clarification_deadline`.

### 6.1. Schéma SQLite (Rang 7 futur)

```sql
-- Ajout à ont_scenarios dans emulator.db (Rang 6 base + Rang 7 colonnes)
ALTER TABLE ont_scenarios ADD COLUMN clarification_deadline TEXT;  -- ISO 8601
ALTER TABLE ont_scenarios ADD COLUMN clarification_context TEXT;  -- JSON: contexte pour hypothèses
ALTER TABLE ont_scenarios ADD COLUMN branch_status TEXT DEFAULT 'pending';  -- pending | branched | merged | rejected
```

### 6.2. Logique du cron coordinateur

```python
# 30_emulateur/cron/clarification_watchdog.py — Rang 7

import sqlite3
import json
from datetime import datetime, timezone

def check_clarification_deadlines(db_path: str = "emulator.db") -> list:
    """Appelé toutes les 60s par cron. Crée les branches d'hypothèse pour les scénarios expirés."""
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL")
    cur = conn.cursor()
    now = datetime.now(timezone.utc).isoformat()
    cur.execute("""
        SELECT id, clarification_context
        FROM ont_scenarios
        WHERE branch_status = 'pending'
          AND clarification_deadline IS NOT NULL
          AND clarification_deadline < ?
    """, (now,))
    expired = cur.fetchall()
    for scenario_id, context_json in expired:
        context = json.loads(context_json)
        # Crée N branches avec hypothèses
        for i, hypothesis in enumerate(context.get("hypotheses", []), start=1):
            branch_id = f"{scenario_id}_branch_{i}"
            cur.execute("""
                INSERT INTO ont_scenarios (id, parent_id, branch_status, clarification_context, created_at)
                VALUES (?, ?, 'branched', ?, ?)
            """, (branch_id, scenario_id, json.dumps({"hypothesis": hypothesis}), now))
    conn.commit()
    conn.close()
    return expired
```

### 6.3. Trigger de branching

Si clarification requise par `clarifying_agent.py` (Level 1/2) sans réponse en **15 minutes** :
1. L'AI FDE stocke `clarification_deadline = now() + 15min` dans `ont_scenarios`.
2. Le cron `clarification_watchdog.py` (toutes les 60s) détecte l'expiration et génère $N$ branches (`Branch_1`, `Branch_2`) avec les hypothèses les plus probables.
3. Il consigne les hypothèses dans `ont_scenarios` (`clarification_context`) et `kernel/uc.db` (audit).
4. L'exécution se poursuit en bac à sable persistant sans bloquer la chaîne de traitement.

---

## 7. Pont Mining AST → Protégé — Correction Gemini 9 (`json_to_owl.py`)

> **Erreur Gemini 9 :** `STRUCTURES.json` (Sprint 0) → architecte recrée manuellement dans Protégé. Mining AST inutile.
>
> **Correctif :** `json_to_owl.py` convertit `STRUCTURES.json` en RDF/Turtle (`palantir_mined.owl`) que l'architecte ouvre dans Protégé pour enrichir visuellement (au lieu de page blanche).

### 7.1. Script (Rang 6 Sprint 0)

```python
# 30_emulateur/ontology/json_to_owl.py

from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal
from rdflib.namespace import XSD
import json

AS = Namespace("http://aspace.local/ontology#")
PAL = Namespace("http://palantir.com/ontology#")

def mined_to_owl(structures_json_path: str, output_owl_path: str):
    """Convertit STRUCTURES.json (mining AST) en RDF/Turtle importable dans Protégé."""
    g = Graph()
    g.bind("as", AS)
    g.bind("pal", PAL)
    g.bind("owl", OWL)

    with open(structures_json_path) as f:
        structures = json.load(f)

    for cls in structures.get("classes", []):
        name = cls["name"]
        # Crée la classe dans le namespace aspace
        g.add((AS[name], RDF.type, OWL.Class))
        if "docstring" in cls:
            g.add((AS[name], RDFS.comment, Literal(cls["docstring"])))
        for prop in cls.get("properties", []):
            g.add((AS[prop["name"]], RDF.type, OWL.DatatypeProperty))
            g.add((AS[prop["name"]], RDFS.domain, AS[name]))

    g.serialize(destination=output_owl_path, format="turtle")
    return output_owl_path

# Usage:
# python -m ontology.json_to_owl \
#   --input palantir-mcp/.mined/STRUCTURES.json \
#   --output 30_emulateur/ontology/palantir_mined.owl
```

### 7.2. Workflow dans Protégé

1. L'architecte ouvre Protégé.
2. **File → Open** → `30_emulateur/ontology/palantir_mined.owl` (RDF/Turtle).
3. Les classes/propriétés minées apparaissent dans l'onglet **Classes**.
4. L'architecte **enrichit visuellement** : ajoute contraintes SHACL, contraintes OWL, restreint domain/range.
5. Sauvegarde dans `Aspace_Core.owl` (le fichier principal).

---

## 8. Endpoints FastMCP `defineTool.py`

* `affiliation.register_referral(referrer_id, referee_id, tier)` — Enregistre le parrainage et met à jour les comptages.
* `affiliation.calculate_statement(client_id)` — Calcule solde, remise, montant du virement (utilise `calculate_statement()` Python du §4.2).
* `affiliation.get_tier_discount(tenant_id)` — Remise de groupe pour Level 3 (≥5 membres).
* `clarification.request_human_input(scenario_id, question, hypotheses_json, timeout_min=15)` — Enregistre deadline + hypothèses dans `ont_scenarios.clarification_deadline`.
* `clarification.force_branch_if_expired(scenario_id)` — Appelée par le cron quand deadline expirée.

---

## 9. REST & Webhook FastAPI

* `GET /api/v2/billing/statement/{client_id}` — Solde d'affiliation + facture nette (widget Coach OS).
* `POST /api/v2/billing/webhook/stripe` — Événements de paiement pour débloquer/suspendre les accès.
* `GET /api/v2/clarification/{scenario_id}` — État de la clarification (pending / branched / merged).

---

## 10. Intégration dans la Feuille de Route

```
[ ARCHITECTURE_V2.md ] (Noyau Émulateur Technique — Sprints 0 à 4)
├── Sprint 0  : Moisson YouTube + 4 sous-agents + json_to_owl.py
├── Sprint 1A : Ingestor Protégé + SQLite WAL + Branching Sandbox
├── Sprint 1B : AIP Python + Bridge Kernel
├── Sprint 2  : CLI Python typer + widgets Coach OS + Pipeline n8n REST
├── Sprint 3  : Slate + AI FDE Eval-Driven + clarifying_agent (avec deadline persistante)
└── Sprint 4  : PySHACL + AI Engine + signaux + auto-MCP
        │
        │  (Consommé par la couche applicative)
        v
[ ARCHITECTURE_V2_ADDENDUM_BUSINESS.md ] (CE FICHIER — Futur)
├── Sprint 5  : Ingestion Aspace_Core.owl (Classes ClientTier 0-3) + SHACL-SPARQL
├── Sprint 6  : Moteur Affiliation Python (`defineTool.py`) + endpoints REST
└── Sprint 7  : AI FDE Level-Aware + Spatial Widgets Coach OS (Billing Deck)
                + cron `clarification_watchdog.py`
```

---

## 11. Directives d'Exécution pour M3 & Opus (Rang 7 futur)

1. **Opus (Orchestrateur)** : Grille de revue pour vérifier que les développements Rang 7 respectent la séparation noyau / business.
2. **M3 (Ouvrier 5B Tokens)** : Implémentation UNIQUEMENT à partir du **Sprint 2** du Rang 6, une fois le noyau ontologique Rang 6 stable dans `emulator.db`.

### Conditions de création / déclenchement

**NE PAS** commencer le Rang 7 tant que :
- Le Sprint 1A du Rang 6 n'est pas validé par Opus
- L'utilisateur n'a pas explicitement demandé le déclenchement du Rang 7
- Les 33 corrections Gemini (1+2+3+4+5+6+9) ne sont pas stabilisées en exécution

**Ce fichier est créé dès maintenant** pour préserver le contenu hors du plan V2, mais son exécution reste post-Sprint 1A.
