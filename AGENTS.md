# AGENTS.md — Canon A'Space OS V3 & Meta-Routeur DOX

> **Loi L0 — Rick.** *Un système qui ne sait pas se répliquer n'est pas un système,
> c'est un document.*
> 
> **Architecture Souveraine & Pyramide Déterministe à 7 Niveaux.**
> Ce fichier racine agit comme le **Meta-Routeur du War Room (Hivemind)**. Il ne centralise plus artificiellement les détails locaux mais aiguille le trafic vers les `AGENTS.md` arborescents (DOX) de chaque sous-dossier maître pour éliminer la famine de contexte et économiser le Tool Calling.

---

## 1. La Pyramide à 7 Niveaux d'A'Space OS V3

```
      ▲
     / \     [7D] HIVEMIND & WAR ROOM : 13e Docteur / Arbitrage transversal Amadou Kone
    /---\
   / 6D  \   [6D] IDENTITÉS & SOUL FILES : CLAUDE.md / GEMINI.md / Soul.md (Air Traffic Control)
  /-------\
 /   5D    \ [5D] HOOKS & VALIDATION GATES : Coupe-circuit déterministe, Veto PII, Gates SSSF
/-----------\
|    4D     | [4D] CRONS & HEARTBEATS : Télémétrie 60s Yas, Tâche hebdo Distillation 50_
|-----------|
|    3D     | [3D] SKILLS & SERVEURS MCP : Ryan ADW, Tool Calling, Antigravity SDK
|-----------|
| SUBSTRAT  | [MACRO] WEBHOOKS & BROKERS : Event Log append-only uc.db (Zero Kafka lourd)
|-----------|
|  PANTRY   | [MICRO] SILVER PLATTER & MÉMOIRE : SQLite WAL, Semantica RDF Graham, OKF 0.2
└───────────┘
```

---

## 2. Meta-Routeur DOX — Cartographie des Sub-AGENTS.md

Pour éviter d'ingérer des dizaines de documents à chaque prompt, l'agent charge **exclusivement** le `AGENTS.md` du sous-dossier concerné :

| Organe / Dossier | Rôle dans V3 & Niveau Pyramide | Fichier d'Aiguillage Dédié |
| :--- | :--- | :--- |
| **`50_Distillation/`** | **LE GATE D'ENTRÉE INVIOLABLE** [5D]. Rien n'entre sans ce sas. | [`50_Distillation/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/50_Distillation/AGENTS.md) |
| **`70_Onthologies/`** | **VÉRITÉ FORMELLE RDF** [Pantry / 6D]. Gardien : Graham (1 681+ nœuds). | [`70_Onthologies/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/70_Onthologies/AGENTS.md) |
| **`40_Memory_Wiki_OKF/`** | **MÉMOIRE LONGUE CERTIFIÉE** [Pantry / 6D]. Format OKF v0.2. | [`40_Memory_Wiki_OKF/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/40_Memory_Wiki_OKF/AGENTS.md) |
| **`90-self-evolution/`** | **SYSTÈME IMMUNITAIRE ANTI-REJEU** [5D / 6D]. Patterns P1-P6. | [`90-self-evolution/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/90-self-evolution/AGENTS.md) |
| **`60_Implementation_...`**| **CADRE & SOPS D'EXÉCUTION** [5D]. Standards de compilation. | [`60_Implementation_Méthodologiques/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/60_Implementation_M%C3%A9thodologiques/AGENTS.md) |
| **`10_Tech_OS/`** | **PLOMBERIE, KERNEL & RUNTIME** [Substrat / 3D]. Ryan & Yaz. | [`10_Tech_OS/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/10_Tech_OS/AGENTS.md) |
| **`20_Life_OS/`** | **VIE, SANTÉ, RITUELS & IKIGAI** [L1 Action]. Amy, Rory. | [`20_Life_OS/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/20_Life_OS/AGENTS.md) |
| **`30_Business_OS/`** | **CASH-FLOW & OFFRES RÉELLES** [L2 Action]. Clara, Bill. | [`30_Business_OS/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/30_Business_OS/AGENTS.md) |
| **`_INBOX/`** | **RÉCEPTION INTENTS BRUTS** [Contrôleur C]. Sas d'arbitrage. | [`_INBOX/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/_INBOX/AGENTS.md) |

---

## 3. Les Invariants Transversaux Inviolables

1. **Règle d'or 1 : Le Gate Inviolable (`50_Distillation/`)**
   - Aucun fichier brut, aucune note non triée n'entre en direct dans la mémoire ou le graphe.
2. **Règle d'or 2 : Les 4 Organes Souverains au-dessus de tout**
   - `70_Onthologies/`, `40_Memory_Wiki_OKF/`, `60_Implementation_Méthodologiques/` et `90-self-evolution/` gouvernent les 3 OS applicatifs (`10_Tech_OS`, `20_Life_OS`, `30_Business_OS`).
   - Tech OS est un serviteur silencieux : interdiction formelle de cannibaliser le système.
3. **Règle d'or 3 : Le Couplage Déterministe (Hooks & Webhooks)**
   - Les agents ne s'exécutent jamais sans intercepteurs runtime (`10_Tech_OS/kernel/hooks/`).
   - Le "Rot Rate" et les fuites de secrets (PII) sont bloqués net par veto déterministe.

---

## 4. Chaîne d'Outils & Résolution de Conway

- **La racine reste minimale :** Le présent fichier route les requêtes sans encombrer le contexte.
- **Un agent est un item qui traverse des états :** Géré via `uc.db` et les validation gates SSSF.
- **Loi d'observation dynamique (D3) :** Le disque physique est l'unique source de vérité (`python scripts/cartographier_v3.py`).

---

## 5. Mémoire de Fin de Réponse — DOX & OKF

Toute modification structurelle ou apprentissage système est :
- Inscrit dans le sous-registre `AGENTS.md` du composant concerné (Append-Only D4).
- Formalisé en OKF v0.2 dans `40_Memory_Wiki_OKF/concepts/`.
- Validé par synthèse vocale sans conflit mutex.
