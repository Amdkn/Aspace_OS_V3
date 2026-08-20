---
type: Concept
title: B1 — coup d'autorite et frontieres (ce qui se decide, ce qui ne s'y decide pas)
description: La frontiere d'autorite de l'etage B1 : il decide du North Star, des cycles 12WY, des decision rights, de la handoff queue, des specs DoD/JTBD, de la gouvernance. Il ne decide pas de l'execution tactique, ne re-derive pas la doctrine perpetuelle, ne remplace pas le Council B2.
tags: [b1, direction, decision-rights, autorite, frontiere, cockpit]
generated: { by: minimax-m3, at: 2026-08-19T01:35:00Z }
verified:
  - { by: process:lecture-fractal-b1b2b3, at: 2026-08-19T01:35:00Z }
  - { by: process:synthese-pulse-b1-tour-1, at: 2026-08-19T01:35:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: fractal-arch
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md"
    title: L2 Business — The B1 / B2 / B3 Fractal Architecture
    last_modified: 2026-06-02
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md"
    title: B2 Business Wheel Harmonization Matrix
    last_modified: 2026-05-27
okf_version: "0.2"
---

# B1 — coup d'autorite et frontieres

Mnemonic canonique : **B1 = WHY/WHERE, B2 = WHAT/gate, B3 = HOW/proof.** Cette page fixe la frontiere.

## Ce que B1 decide (le coup d'autorite)

Tire du fractal B1/B2/B3, B1 possede six objets :

1. **North Star** — la cible de long terme, ce qui ne change pas entre deux 12WY.
2. **12WY cycles** — la cadence d'Entrepreneur (3 rocks / 12WY, 1 rock / mois).
3. **Decision rights** — qui decide quoi, entre B1 et gatekeepers (Rick/Morty) et A0 Amadeus.
4. **Handoff queue** — le registre des mandates emis vers B2 (voir concept adjacent).
5. **DoD/JTBD packet specs** — la grammaire des paquets que B2 doit remplir (B1 tient le gabarit, B2 le remplit).
6. **Gouvernance** — les stop conditions et l'escalier d'escalade.

Un etage qui decide de tout ne decide de rien. La frontiere est donc aussi importante que le contenu.

## Ce que B1 ne decide PAS

Trois interdits non-negociables :

- **Pas d'execution tactique.** B1 n'ecrit pas de code, ne lance pas de campagne, n'envoie pas de facture. Il mandate, il ne fait pas.
- **Pas de re-derivation de la doctrine.** La doctrine perpetuelle vit dans l'Area (macro) et les Projects la calibrent (micro), pas l'inverse. B1 cite la doctrine, il ne la repense pas dans un mandate.
- **Pas de remplacement du Council B2.** L'arbitrage meso (les 8 hero-managers) traite les conflits cross-domaines. B1 n'intervient que quand **le Council ne peut pas preserver la wheel 8-domain** tout en restant dans North Star, cycle, autorite et appetit pour le risque courants.

## La triple frontiere (qui decide, et quand)

| Sujet | Decide | Conditions |
|---|---|---|
| North Star / repositionnement marche | B1 (avec A0) | Drift observe, cycle 12WY termine, ou evidence terrain > 1 trimestre |
| 12WY courant et rocks B1 | B1 | A chaque rollover de cycle |
| Mandat B1→B2 (intent + contraintes + success signal) | B1 | Quand wheel imbalance scannee detecte un signal |
| Definition DoD et JTBD | **B2** | Traduit le mandat B1 — B1 n'ecrit pas le DoD |
| Execution JTBD et preuve | **B3** | JTBD recu d'un B2 owner — B3 n'agit jamais sans source DoD/JTBD |
| Arbitrage cross-domaines (pair checks) | **B2 Council** | 3 modes : parallel, handoff, negotiation |
| Escalade vers B1 | B2 Council | Seulement si wheel 8-domain menacee |
| Escalade vers A0 Amadeus | B1 gatekeepers (Rick/Morty) | Emergency triggers, doctrines verrouillees menacees |

## Anti-pieges — ce qui ferait deraper B1

- **B1 qui descend dans le DoD.** Un mandat B1 qui dit *« DoD : livrer la feature X avant le 15 »* a ecrit le travail de B2. La forme correcte : *« success signal : adoption monetaire de la feature X par ≥ 10 % du segment cible d'ici fin de 12WY »*. B1 fixe le succes, pas la livraison.
- **B1 qui arbitre un conflit cross-domaines** que le Council peut resoudre. Court-circuiter le Council creuse une dette d'autorite : le Council apprend qu'il n'est pas l'instance d'arbitrage, et la prochaine fois il escalade par defaut.
- **B1 qui re-derive la doctrine Area dans un mandat Project.** L'Area est perpetuelle ; le Project calibre. Confondre les deux casse le DRY du fractal.

## Sources de l'autorite

- `00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` — la table des rangs A/B et la liste *possede / ne fait jamais*.
- `B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md` §« B2 Council » — la condition d'escalade vers B1 (Council ne peut preserver la wheel).
- `B1_Area_Direction/03_DECISION_CHARTER.md` (reference, non lu dans cette passe) — qui decide quoi, documente comme charte.

## Liens

- [[b1-mandate-packet-spec]] — ce que B1 transmet vers le bas, sous quelle forme
- [[b1-wheel-imbalance-six-signes]] — le scan qui decide quand emettre un mandat
- [[b1-stop-conditions-escalier]] — quand B1 arrete le systeme
- [[fractal-b1b2b3-architecture]] — la table source

## Note de confiance

**Confirme par machine.** Frontiere tiree verbatim de la table des rangs A/B dans le fractal. L'interdit *« pas d'execution tactique »* est explicite dans la colonne *« Ne fait jamais »* de la table.