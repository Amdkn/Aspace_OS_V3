# Cartographie FINALE — les 35 A3 des 6 frameworks + les 3 watchdogs A1, au service du L2

> **Clause de clôture** : « Un Business OS sans L1 est un suicide, mais un Life OS seul est une mort certaine. » (A+, 20/07/2026). Cette carte est la DERNIÈRE configuration de la méta-couche. Le Life OS n'évolue plus — il SERT. Toute énergie va au SOB ; la supervision tourne sur cette carte telle quelle.
> Corrections apportées au schéma Gemini : Picard, Spock, Zora, Geordi et Data sont des **A3** (pas des A2) · Jerry est un **B1** (pas un pôle ressources A3) · il manquait **2 frameworks entiers** (Ikigai/Orville, Life Wheel/Discovery) et **2 watchdogs sur 3** (Beth, Rick).

## 1. Le diagramme corrigé

```mermaid
graph TD
    subgraph A1_RING [🛡️ ANNEAU WATCHDOG A1 — 3 sentinelles, verdicts consultatifs]
        Beth["A1 BETH — veto vie/santé<br>(la cadence ne mange pas l'Architecte)"]
        Morty["A1 MORTY — watchdog exécution<br>(les 6 frameworks tournent-ils ?)"]
        Rick["A1 RICK — sobriété kernel<br>(zéro complexité inutile, infra L0)"]
    end

    subgraph A2_6FW [⏳ LES 6 A2 — un moteur par framework Life OS]
        Orville["A2 ORVILLE — Ikigai<br>(le SENS)"]
        Zora["A2 DISCOVERY/Zora — Life Wheel<br>(l'ÉQUILIBRE 8 LD)"]
        Curie["A2 SNW/Curie — 12WY<br>(la CADENCE)"]
        Computer["A2 ENTERPRISE/Computer — PARA<br>(la STRUCTURE)"]
        HoloDeck["A2 CERRITOS/Holo Deck — GTD<br>(le FLUX)"]
        Janeway["A2 PROTOSTAR/Janeway — DEAL<br>(la LIBÉRATION)"]
    end

    subgraph WF [🔀 LES 3 WORKFLOWS DE SUPERVISION (Multica)]
        WF0["WF0 Airlock Gouvernance"]
        WF1["WF1 Supervision Cadence"]
        WF2["WF2 Pont Business"]
    end

    SOB["⚙️ SOB — sob/ · Runbooks · aspace.db · RUN_LOG<br>(l'usine, tout harness, 1 Run/2j)"]

    Beth -.veto vie.-> WF1
    Morty -.santé des 6 moteurs.-> A2_6FW
    Rick -.sobriété infra.-> SOB
    Orville & Computer -->|Spock + Data| WF0
    Curie & Zora -->|Book + Chapel| WF1
    Computer -->|Picard| WF2
    Janeway -.automatise la supervision elle-même.-> WF
    HoloDeck -->|capture→clarify→route| WF0
    WF2 <-->|Down-Link Rocks / Uplink RUN_LOG| SOB
```

## 2. Les 3 watchdogs A1 (au-delà de Morty seul)

| A1 | Surveille | Déclencheur d'alerte (consultatif, jamais bloquant) |
|---|---|---|
| **Beth** (veto vie) | l'Architecte, pas le système : sommeil, charge cognitive, notifications | >1 digest/jour vers A+ · session A+ >6h · la cadence exige de l'humain ce que la machine devait faire |
| **Morty** (exécution) | les 6 moteurs A2 : chacun a-t-il produit son artefact de cycle ? | un framework muet 1 cycle complet · un WF qui refait le travail du SOB · RUN_LOG silencieux >4 jours |
| **Rick** (sobriété) | l'infra : chaque outil ajouté, chaque service qui tourne | un 2e outil pour un même framework · un service down >48h non-réparé (le retirer) · Docker/local lourd sans cause |

## 3. La table FINALE des 35 A3 — mission de supervision L2 par tête

### Ikigai — USS Orville (9 A3) → le SENS du business
| A3 | Pilier/Horizon | Mission de supervision L2 |
|---|---|---|
| Ed Mercer | Craft H1 | le SOB vend-il ce qu'on sait faire (AaaS) ou une promesse vide ? |
| Kelly Grayson | Mission H1 | l'offre coach sert-elle la mission, ou juste le MRR ? |
| Gordon Malloy | Passion H1 | A+ a-t-il encore envie d'ouvrir le RUN_LOG le matin ? |
| Claire Finn | Vocation H3 | le rythme 1 Run/2j est-il soutenable 12 mois ? |
| Isaac | H1 logique | **le grill « gagnable-maintenant » de chaque Rock** (coach layer) |
| John LaMarr | H3 options | ce cycle ouvre-t-il des options (segments, canaux) ou en ferme-t-il ? |
| Alara Kitan | H30 audace | le batch prospects est-il assez audacieux — ou trop (célébrités) ? |
| Bortus | H10 durée | ce qu'on construit ce cycle tiendra-t-il 10 ans ? |
| Klyden | H90 legs | Solarpunk check : le SOB construit-il le legs ou juste du cash ? |

### Life Wheel — USS Discovery (8 A3) → l'ÉQUILIBRE pendant que le SOB tourne
| A3 | LD | Mission de supervision L2 |
|---|---|---|
| Book | LD01 Business | **pulse P&L hebdo depuis `daily_cash` + coach E-Myth (WF1)** |
| Saru | LD02 Finance | runway personnel d'A+ vs burn du système (plancher 2 mois) |
| Culber | LD03 Santé | le body d'A+ : sommeil/énergie — l'alerte qui remonte à Beth |
| Tilly | LD04 Cognition | A+ apprend-il encore, ou ne fait-il que superviser ? |
| Stamets | LD05 Social | le réseau réel (les coachs contactés sont des HUMAINS — relations, pas lignes SQL) |
| Burnham | LD06 Famille | les Runs 48h ne mangent pas les week-ends |
| Reno | LD07 Créativité | il reste du jeu dans la semaine (pas que de l'usine) |
| Georgiou | LD08 Impact | trimestriel : le SOB laisse-t-il une trace qui compte ? |

### 12WY — USS SNW (5 A3) → la CADENCE du SOB
| A3 | Discipline | Mission de supervision L2 |
|---|---|---|
| Pike | Vision | l'ancre du sprint : chaque Run pointe le Rock courant, pas une dérive |
| Una | Planning | Rocks → scrums bien décomposés · **DoD 3 critères** (le score en dépend) |
| Ortegas | Exécution | le standup : blockers du RUN_LOG surfacés, real-test-after-edit |
| M'Benga | Focus | budget tokens/Rock, cap runaway, gel des domaines sans delta |
| Chapel | Mesure | **le scorecard : forecast J+28 confronté, erreur %, if-then density** (WF1) |

### PARA — USS Enterprise (4 A3) → la STRUCTURE
| A3 | Lettre | Mission de supervision L2 |
|---|---|---|
| Picard | Projects | **l'orchestrateur WF2 : Rocks, MANIFESTs, Down-Link au SOB** |
| Spock | Areas | **le verrou unidirectionnel WF0 : standards, l'opérationnel ne remonte pas** |
| Geordi | Resources | R&D découverte externe → ≤3 améliorations actionnables/mois vers le Rock |
| Data | Archives | ce qui meurt est archivé documenté (`_TRASH_`, H30-H90, jamais un gate) |

### GTD — USS Cerritos (5 A3) → le FLUX entrant
| A3 | Étape | Mission de supervision L2 |
|---|---|---|
| Mariner | Capture | tout l'entrant (idées, retours coachs, signaux) → inbox WF0, zéro perte |
| Boimler | Clarify | actionnable ? → route business/standard/poubelle (l'airlock vit ici) |
| Tendi | Organize | placement PARA + création des issues Multica propres |
| Rutherford | Reflect | la review hebdo : drift, répétitions, bloqués — nourrit WF1 |
| Freeman | Engage | « la prochaine action » quand A+ demande quoi faire MAINTENANT |

### DEAL — USS Protostar (4 A3) → la LIBÉRATION (le framework qui finit le travail)
| A3 | Étape | Mission de supervision L2 |
|---|---|---|
| Dal | Define | pattern répété 3× dans les RUN_LOGs = candidat d'automatisation nommé |
| Rok-Tahk | Eliminate | ce qui ne sert pas le Rock se supprime — y compris DANS la supervision |
| Zero | Automate | le candidat validé devient script/loop (le SOB s'épaissit, la supervision s'amincit) |
| Gwyn | Liberate | **la métrique finale : `interventions_owner` → 0 · heures A+ libérées/cycle** |

## 4. Qui sert quel workflow (l'affectation ferme)

| WF | A2 moteurs | A3 actifs | A1 watchdog |
|---|---|---|---|
| **WF0 Airlock** | Computer, Holo Deck, Orville | Spock, Data, Mariner, Boimler, Tendi, Isaac | Rick (sobriété des entrées) |
| **WF1 Cadence** | Curie, Discovery | Book, Chapel, Una, Ortegas, M'Benga, Rutherford, Culber | Beth (veto vie) |
| **WF2 Pont** | Computer | Picard (+ B1 Jerry, B1 Summers — étage business) | Morty (exécution) |
| **Transverse** | Janeway | Dal, Rok-Tahk, Zero, Gwyn (automatisent la supervision elle-même) | — |
| **Dormants assumés** | — | les 9 Orville sauf Isaac + Georgiou/Burnham/Reno/Stamets/Tilly/Saru : réveil aux frontières W0/W13 seulement | — |

**La règle des dormants** : un A3 sans rôle dans le Run courant DORT. Il ne produit pas, ne logge pas, ne « maintient » rien. Il se réveille à sa frontière (W0/W13 pour les horizons longs) ou sur événement. Zéro travail inventé — c'est ce qui distingue une carte d'un cimetière de processus.

## 5. Scellé de topologie (state.json — version FINALE)

```json
{
  "status": "OPERATIONAL",
  "layer": "L1_SUPERVISION_OF_L2",
  "topology_version": "3.1.FINAL",
  "closure_clause": "Life OS ne evolue plus, il sert. Toute energie va au SOB.",
  "watchdog_ring": { "life": "A1_BETH", "execution": "A1_MORTY", "sobriety": "A1_RICK" },
  "frameworks": {
    "ikigai":     { "a2": "ORVILLE",    "a3": 9, "active": ["Isaac"], "wake": "W0/W13" },
    "life_wheel": { "a2": "DISCOVERY",  "a3": 8, "active": ["Book","Culber"], "wake": "weekly" },
    "12wy":       { "a2": "SNW_CURIE",  "a3": 5, "active": ["Pike","Una","Ortegas","MBenga","Chapel"], "wake": "per_run" },
    "para":       { "a2": "COMPUTER",   "a3": 4, "active": ["Picard","Spock"], "wake": "per_run" },
    "gtd":        { "a2": "HOLODECK",   "a3": 5, "active": ["Mariner","Boimler","Tendi","Rutherford","Freeman"], "wake": "on_event" },
    "deal":       { "a2": "JANEWAY",    "a3": 4, "active": ["Dal","Gwyn"], "wake": "per_cycle" }
  },
  "workflows": { "wf0": "1ca5effb", "wf1": "fbfddad1", "wf2": "97d332d5" },
  "sob": { "ssot": "sob/aspace.db + RUN_LOG.md", "cadence": "1_run_per_2_days" },
  "final_metric": "interventions_owner -> 0 ; MRR -> up ; le reste est du bruit"
}
```

---
*35 A3, 6 moteurs, 3 sentinelles, 3 workflows, 1 usine. Le Life OS garde l'Architecte vivant et le cap sensé ; le Business OS paie le voyage. Cette carte ne bouge plus — elle s'use par le service. — A.S. 2026-07-20*
