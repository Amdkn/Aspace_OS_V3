# La cadence et l'escalade, en diagrammes

Ces trois schémas sont la **même vérité que `schema/01_cadence.sql`**, sous
une forme qui se lit d'un coup d'œil. S'ils divergent du SQL, c'est le SQL
qui fait foi — lui seul peut refuser une donnée.

## 1. L'emboîtement — de la plus petite unité à l'année

La vague de Scrum est la seule unité réelle. Tout le reste est un agrégat,
et chaque agrégat porte sa règle de compte.

```mermaid
flowchart LR
  subgraph L2["L2 · Business OS — comprimé"]
    direction LR
    S["Scrum<br/><small>B3 · quotidien</small>"]
    SP["Sprint<br/><small>B2 · hebdomadaire</small>"]
    R["Rock<br/><small>B1 · mensuel</small>"]
    S -- "×5" --> SP
    SP -- "×4" --> R
  end
  subgraph L1["L1 · Life OS — NON comprimé"]
    direction LR
    C["Cycle 12WY<br/><small>A3 · trimestriel</small>"]
    A["Année civile<br/><small>A2 · garde annuelle</small>"]
    C -- "×4" --> A
  end
  R -- "×3" --> C
```

**La frontière entre les deux sous-graphes est la frontière de compression.**
Business OS accélère ; Life OS garde le temps réel, délibérément, pour que
l'arbitrage humain reste observable.

## 2. L'escalade de revue — et la sortie d'A0

```mermaid
flowchart TD
  V["Vague livrée"] --> A3
  A3["A3 · conseils<br/><small>accepte le cycle ou renvoie le Rock</small>"]
  A2["A2 · vaisseaux<br/><small>garde l'alignement de l'année</small>"]
  A1["A1 · Morty<br/><small>gatekeeper de complexité</small>"]
  H["human:amdkn<br/><small>seul à pouvoir apposer le verdict</small>"]
  A0["A0 · Amadeus"]

  A3 -- "escalade" --> A2
  A2 -- "escalade" --> A1
  A1 -- "escalade" --> H
  A3 -. "renvoi" .-> V
  A2 -. "renvoi" .-> V
  A1 -. "renvoi" .-> V
  A0 -. "SORT de la boucle" .-x A3

  style A0 stroke-dasharray: 5 5
  style H stroke-width:3px
```

A0 n'a **aucune arête entrante**. Sa sortie de la boucle n'est pas une
consigne écrite en marge : c'est la forme du graphe. La table
`palier_revue` du SQL le fait respecter de la même façon — A0 n'y figure pas.

## 3. Le flux d'une vague, de la production au verdict

```mermaid
sequenceDiagram
  participant B3 as B3 · escouade
  participant DB as 90_Back-Office
  participant FO as 80_Front-Office
  participant A3 as A3 · conseil
  participant H as human:amdkn

  B3->>B3: produit les concepts OKF
  B3->>B3: écrit constats.json<br/>(dettes · avancées · apprentissages)
  B3->>DB: enregistre la vague + durée machine
  Note over DB: v_compression tranche :<br/>commodité atteinte ou non
  DB->>FO: generer.py rend la page autonome
  FO->>A3: une page, trois secondes
  A3->>A3: accepte / renvoie / escalade
  A3->>H: escalade si le palier ne tranche pas
  H->>DB: tampon_verdict.py<br/>machine → humain
  Note over H: le seul geste<br/>qu'aucun agent ne peut poser
```

## Ce que ces schémas ne disent pas

Ils décrivent la cadence **cible**. Ils ne disent pas où l'on en est.

À la date du 2026-08-20 : **37 concepts sur 424 portent un verdict humain**,
et aucune vague n'a encore été enregistrée dans la base. Les diagrammes
décrivent une machine dont une seule pièce tourne.
