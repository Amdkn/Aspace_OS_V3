---
adr_id: ADR-REF-PERSONAS-001
title: Différenciation stricte entre personas — Landings OMK Nexus
status: RATIFIED
created: 2026-07-06
ratified: 2026-07-06
owner: B1 Summers Nexus OMK BOS
gatekeeper_doctrine: E-Myth B1 — travail ON la marque, pas IN une marque uniforme
strates_couvertes: A (Editorial Ledger) · B (Terminal Stratégique) · C (Atelier Industriel)
personas_canon: 3 prioritaires (Marcus / Harrison / David)
personas_à_étendre: 2 listés PRD-NEXUS §4 (Amara · Christian) · 1 cité (Clara)
sources_canons:
  - PRD-NEXUS-EVOLUTION-IA-001 §3 §4 — 3 strates × 10 ICPs × 6 candidates × 5 personas (3 prioritaires : Marcus/Harrison/David)
  - ADR-ICP-NEXUS-001 (RATIFIED 2026-06-21) — Persona Expert méthodique · mantra "L'illusion de la complexité" · 3 piliers Nexus
  - ADR-LANDING-PERSONAS-001 (DRAFT V1, 2026-07-06) — 3 landings distinctes spec
  - ADR-LANDING-AESTHETIC-001 (DRAFT, 2026-07-06) — doctrine esthétique en miroir d'ANTI-TEMPLATE
  - ADR-LANDING-COPY-001 (DRAFT, 2026-07-06) — doctrine copywriting + vocabulary canonique signé
  - ADR-DESIGN-SYSTEM-001 (DRAFT, 2026-07-06) — tokens canoniques (palette/font/space)
  - ADR-ANTI-TEMPLATE-001 (RATIFIED) — patterns bannis génériques
  - ADR-AAAS-PRICING-001 (RATIFIED 2026-06-24) — $1000/mois × 100 (sister canon pricing, NON différencié par persona)
  - ADR-ANTI-PAPERCLIP-001 (RATIFIED 2026-06-21) — anti-paperclip · doctrine sobriété
  - ADR-ICP-NEXUS-001 (RATIFIED) — ICP source du persona "Expert méthodique"
empirical_v2_d1:
  - C:\Users\amado\omk-nexus-landing-3-personas\v2\marcus\index.html — Editorial Ledger empirique
  - C:\Users\amado\omk-nexus-landing-3-personas\v2\harrison\index.html — Terminal Stratégique empirique
  - C:\Users\amado\omk-nexus-landing-3-personas\v2\david\index.html — Atelier Industriel empirique
references_inspirations_v2:
  - _references\apartamentomagazine.com-fetch.md — Editorial Ledger mood
  - _references\linear.app-fetch.md — Terminal Stratégique mood
  - _references\teenage.engineering-fetch.md — Atelier Industriel mood
extends:
  - ADR-ICP-NEXUS-001
  - ADR-ANTI-TEMPLATE-001
supersedes: null
doctrine_lock: append-only · D4 no-amnesia · D7 cost-of-escalation
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-2"
  context: "Ratification Tier 2 DDD Landing Pages — 3 ADR multi-page & personas ratifiés en bloc."
---

# ADR-REF-PERSONAS-001 — Différenciation stricte entre personas (Landings OMK Nexus)

> **Gatekeeper doctrine** : B1 E-Myth travaille **ON** la marque (les personas sont des produits distincts) — pas **IN** une marque uniforme (template générique swappé en couleur). Sister-ships, pas uniformité.

## 1. Purpose & Contexte

Le PRD-NEXUS-EVOLUTION-IA-001 §3 §4 mandate la production de **3 landings distinctes** adressant chacune une strate prioritaire :

| Strate | Persona | Métier | H1 horizon |
|---|---|---|---|
| **A** | **Marcus** | Managing Partner coaching C-Suite | aujourd'hui |
| **B** | **Harrison** | CEO agence BDR (Business Development Representative) | 30 jours |
| **C** | **David** | fractional COO ×15 PME | 90 jours |

L'ADR-LANDING-PERSONAS-001 (V1 DRAFT) acte que les 3 landings doivent être **spécifiées distinctement**. Le présent ADR grave la **doctrine de différenciation stricte** qui empêche la dérive "template uniforme swappé en couleur" (anti-pattern V1) et fixe les **règles d'extension** pour les 5 personas canon (Marcus/Harrison/David + Amara/Christian/Clara listés PRD §4).

**Pourquoi cet ADR existe** : sans verrouillage canonique, un A3 livré sans supervision va naturellement dériver vers "page générique reusable cross-persona" (gain de temps court terme, perte de marque à 1an+). La doctrine est gravée **une fois** ici pour que les 3 livraisons V2 restent radicalement différenciées.

**Sister canon — ne pas dupliquer** :
- **ICP source** : ADR-ICP-NEXUS-001 (RATIFIED) — persona "Expert méthodique" + mantra + 3 piliers
- **Aesthetic général** : ADR-LANDING-AESTHETIC-001 (DRAFT) — doctrine en miroir d'ANTI-TEMPLATE-001
- **Tokens** : ADR-DESIGN-SYSTEM-001 (DRAFT) — palette/font/space canoniques
- **Copy** : ADR-LANDING-COPY-001 (DRAFT) — vocabulary + signature par persona
- **Spec 3 landings** : ADR-LANDING-PERSONAS-001 (DRAFT V1)
- **Pricing** : ADR-AAAS-PRICING-001 (RATIFIED) — $1000/mois ×100 identique partout
- **Anti-patterns** : ADR-ANTI-TEMPLATE-001 (RATIFIED)
- **Empirical V2 D1** : `C:\Users\amado\omk-nexus-landing-3-personas\v2\` — 3 livrables radicaux

## 2. Decision : 3 postures éditoriales distinctes (DOGME)

**Décision canonique** : chaque persona prioritaire reçoit **une posture éditoriale propriétaire** radicalement différenciée sur **4 axes obligatoires** :

1. **Palette dominante** (background + couleur accent) — 0 chevauchement
2. **Display font italic** (la signature typographique de la marque) — 0 chevauchement
3. **Élément signature visuel** (le motif récurrent qui rend la page reconnaissable) — 0 chevauchement
4. **Section naming convention** (la grammaire des titres de section) — 0 chevauchement

> **Dogme** : si une page peut être confondue avec une autre par couleur OU typo OU élément signature, la différenciation a échoué. Reprendre la posture jusqu'à ce que les 4 axes soient **uniques et immédiatement identifiables**.

**Vocabulaire de posture** (sister-canon) : on parle de **posture éditoriale** (et non de "template" / "skin" / "thème"). La posture est une **identité éditoriale** au sens E-Myth B1 : c'est ce que le client voit en 0,5 seconde et qui décide s'il **reconnaît son monde** ou s'il "scroll".

## 3. Persona → Aesthetic Mapping (CANONIQUE)

### 3.1 Marcus (Strate A · Managing Partner coaching C-Suite) → **Editorial Ledger**

Posture inspirée de `apartamentomagazine.com` (cahier de tendances, marginalia, photographie documentaire). Le C-Suite qui scroll doit sentir **le papier**.

| Axe | Valeur canonique |
|---|---|
| **Palette dominante** | paper `#F4EFE6` (background) + oxblood `#7C1F23` (accent) |
| **Display font italic signature** | **Fraunces italic** (titres h1/h2) |
| **Body + secondary** | Source Serif 4 (corps) + JetBrains Mono (numerique/codes) |
| **Élément signature** | **Marginalia handwritten** — notes manuscrites en marge (gauche/droite) qui commentent le corps, comme un coach de cabinet annote un dossier client |
| **Section naming** | `§N.M` (style Legal Brief) — ex : `§1.2 Le Chef de Cabinet IA` |
| **Éléments d'autorité** | numérotation serrée, lettres capitales discrètes, interlignage généreux, photographie argentique |
| **Vocabulary canonique** | "Le Chef de Cabinet IA" · "Audit + Wargame de vos process de synthèse" |
| **CTA mailto** | `audits@marcus-coach.nexus.omk.services` |
| **Manifeste empirique V2** | `C:\Users\amado\omk-nexus-landing-3-personas\v2\marcus\index.html` |

**Pourquoi Editorial Ledger pour Marcus** : le Managing Partner de coaching C-Suite lit des **dossiers confidentiels** (board papers, mémos, audits) — l'Editorial Ledger le transporte dans son **monde lexical**. La marginalia handwritten est le clin d'œil : le coach **annote**, il ne slide pas.

### 3.2 Harrison (Strate B · CEO agence BDR) → **Terminal Stratégique**

Posture inspirée de `linear.app` (issue tracker design tool, monochromatic dark, type crisp, chiffres-first). Le CEO BDR qui scroll doit sentir **le cockpit**.

| Axe | Valeur canonique |
|---|---|
| **Palette dominante** | deep ink `#0A0E16` (background) + teal `#2DD4BF` (accent) |
| **Display font signature** | **Outfit** (titres, sans-serif géométrique) + Manrope (body) |
| **Mono signature** | **Geist Mono** (numérique, codes, tickers) |
| **Élément signature** | **Ticker pseudo-code** — bandeau défilant ou bloc statique de lignes type `[M0X] PROCESSING pipeline.value` qui prouve que "ça travaille" sans montrer le code |
| **Section naming** | `[M0X]` (style Issue Tracker / Module Index) — ex : `[M01] L'Arbitrage Jevons` |
| **Éléments d'autorité** | compteurs temps-réel, M0X/M01/M02 numérotation, dashboards compressés, micro-interactions imperceptibles |
| **Vocabulary canonique** | "L'Arbitrage Jevons" · "Plan fixe + Gstack" |
| **CTA mailto** | `arbitrage@harrison-bdr.nexus.omk.services` |
| **Manifeste empirique V2** | `C:\Users\amado\omk-nexus-landing-3-personas\v2\harrison\index.html` |

**Pourquoi Terminal Stratégique pour Harrison** : un CEO d'agence BDR vit dans **Linear, Notion, HubSpot, dashboards**. Le Terminal Stratégique est son **native habitat**. Le ticker `[M0X]` est la signature : "ce système travaille pour vous, voici ses modules".

### 3.3 David (Strate C · fractional COO ×15 PME) → **Atelier Industriel**

Posture inspirée de `teenage.engineering` (produits physiques documentés, OP-1, assemblage photographique, étiquetage au pochoir). Le COO qui scroll doit sentir **l'atelier**.

| Axe | Valeur canonique |
|---|---|
| **Palette dominante** | warm noir `#1C1917` (background) + amber `#D97706` (accent) |
| **Display font signature** | **Source Serif italic** (titres) — pour la chaleur de la mention manuelle |
| **Body + secondary** | IBM Plex Sans (corps) + IBM Plex Mono (numérique/SOPs) |
| **Élément signature** | **SOP-to-Skill before/after** — bloc comparatif qui montre une SOP client **transformée en skill exécutable** (état avant = paragraphe flou ; état après = checklist exécutable visible) |
| **Section naming** | `WORKBENCH 0X` (style établi / établi-grade) — ex : `WORKBENCH 01 — SOPs → Skills exécutables` |
| **Éléments d'autorité** | pochoirs (stencil), numéros de série fictifs, photographies d'atelier, nomenclature OP-1, paper texture légère |
| **Vocabulary canonique** | "SOPs → Skills exécutables" · "W× par client" |
| **CTA mailto** | `atelier@david-coo.nexus.omk.services` |
| **Manifeste empirique V2** | `C:\Users\amado\omk-nexus-landing-3-personas\v2\david\index.html` |

**Pourquoi Atelier Industriel pour David** : un fractional COO passe sa vie dans des **processus, runbooks, SOPs**. L'Atelier Industriel est son **mode opératoire**. Le SOP-to-Skill before/after est la signature : "voilà ce que je fais, voilà le livrable".

## 4. Cross-Différenciation Rules (DOGME — 0 tolérance)

| Axe | Marcus (Editorial) | Harrison (Terminal) | David (Atelier) | Règle |
|---|---|---|---|---|
| **Background** | paper `#F4EFE6` | deep ink `#0A0E16` | warm noir `#1C1917` | **3 valeurs uniques** |
| **Accent** | oxblood `#7C1F23` | teal `#2DD4BF` | amber `#D97706` | **3 valeurs uniques** |
| **Display italic** | Fraunces italic | (Outfit — pas d'italic display) | Source Serif italic | **2 italic différents OU aucun — jamais 2 identiques** |
| **Mono** | JetBrains Mono | Geist Mono | IBM Plex Mono | **3 familles différentes** |
| **Élément signature** | Marginalia handwritten | Ticker pseudo-code `[M0X]` | SOP-to-Skill before/after | **3 éléments uniques, jamais répétés** |
| **Section naming** | `§N.M` | `[M0X]` | `WORKBENCH 0X` | **3 grammaires distinctes** |
| **Vocabulary signé** | "Le Chef de Cabinet IA" | "L'Arbitrage Jevons" | "SOPs → Skills exécutables" | **3 mantras uniques** |
| **CTA mailto** | `audits@marcus-coach.nexus.omk.services` | `arbitrage@harrison-bdr.nexus.omk.services` | `atelier@david-coo.nexus.omk.services` | **3 sous-domaines distincts** |

**Test de différenciation (gate de validation A0)** : si on place 3 captures côte à côte avec 1 seconde de scroll, **chaque page doit être identifiée par son monde lexical** (papier · cockpit · atelier). Si 2 sont interchangeables, la différenciation a échoué.

## 5. Vocabulary canonique signé + Pricing (cohérence canon)

**Vocabulary canonique par persona** (sister-canon ADR-LANDING-COPY-001) :

| Persona | Mantra (titre) | Signature (sous-titre / value-prop) |
|---|---|---|
| **Marcus** | "Le Chef de Cabinet IA" | "Audit + Wargame de vos process de synthèse" |
| **Harrison** | "L'Arbitrage Jevons" | "Plan fixe + Gstack" |
| **David** | "SOPs → Skills exécutables" | "W× par client" |

> **Règle de signature** : chaque persona a **un mantra + une signature**. Pas d'alternative. Pas de variation A/B sauvage. Sister-canon strict.

**Pricing** : **$1000/mois × 100 clients** identique sur les 3 landings. Pas de pricing différencié par persona. Sister-canon ADR-AAAS-PRICING-001 + ADR-ANTI-PAPERCLIP-001.

> **Anti-pattern gravé** : un pricing différent par persona (ex : $2000 pour Marcus, $500 pour David) viole la doctrine E-Myth B1 (cohérence canonique) et la sobriété anti-paperclip. Refusé.

## 6. CTA mailto-canon par persona

| Persona | Sous-domaine canonique | Usage |
|---|---|---|
| **Marcus** | `audits@marcus-coach.nexus.omk.services` | email entrant pour demande d'audit C-Suite |
| **Harrison** | `arbitrage@harrison-bdr.nexus.omk.services` | email entrant pour demande d'arbitrage Jevons |
| **David** | `atelier@david-coo.nexus.omk.services` | email entrant pour atelier SOPs → Skills |

> **Règle** : le sous-domaine `<mot-clé>@<persona-role>.nexus.omk.services` est figé pour 1an+. Pas de renommage sans amendement canonique. Sister-canon anti-paperclip : chaque sous-domaine est routé vers A0 inbox canonique (gate HITL), pas vers une boîte noire.

## 7. Workflow d'extension (4ᵉ persona et au-delà)

**Pour ajouter un 4ᵉ persona (ex : Amara growth native-IA listé PRD-NEXUS §4)** :

### Étape 1 — Sister-canon d'abord (PRÉ-REQUIS)

Produire **dans cet ordre** :
1. **ADR-ICP-NEXUS-001 amendé** (ou nouvel ADR `ADR-ICP-NEXUS-00X-<persona>`) — acte le persona dans l'ICP canonique
2. **Référence inspiration fetchée D1** dans `_references/<source>-fetch.md` (cf. pattern Apartamento/Linear/Teenage Engineering)
3. **Validation A0** (HITL gate) — pas d'auto-promotion B1 (D7 cost-of-escalation)

### Étape 2 — Posture éditoriale (CHOIX)

**Choix A (préférable, ROI)** : **réutiliser une posture existante** (Editorial Ledger / Terminal / Atelier) en changeant **uniquement vocabulary + signature + CTA mailto**. Pas de nouvelle posture. C'est le chemin canonique pour la plupart des extensions.

**Choix B (rare, 1an+)** : créer une **4ᵉ posture éditoriale distincte** — UNIQUEMENT si :
- Le persona est **suffisamment radical** pour qu'aucune des 3 postures existantes ne porte son monde lexical (D6 root cause)
- La nouvelle posture respecte les **4 axes obligatoires** (palette / display italic / élément signature / section naming) avec **0 chevauchement** avec les 3 existantes
- Sister-canon `_references/` + ADR-LANDING-AESTHETIC-001 amendé + ADR-LANDING-PERSONAS-001 amendé

> **Anti-pattern gravé** : créer une 4ᵉ posture "pour varier" / "parce que c'est joli" viole la doctrine E-Myth B1. La variation décorative n'est pas une raison. Sister-ship = préférence ; uniformité forcée = refus.

### Étape 3 — Landing built + V2 empirique

- Code livré dans `C:\Users\amado\omk-nexus-landing-3-personas\v3\<persona>\index.html` (extension V3)
- Gate A0 ratification finale avant promotion production

### Étape 4 — Amendement du présent ADR

- Mise à jour `personas_canon` (D4 append-only) : ancien persona reste en historique, nouveau ajouté
- Mise à jour de la **matrice §4 cross-différenciation rules** avec les 4 axes
- Refus d'invention : **ne JAMAIS inventer** le mapping d'un 5ᵉ/6ᵉ/7ᵉ/8ᵉ persona non documenté dans PRD-NEXUS §4 ou dans un ADR-ICP-NEXUS amendé

## 8. Anti-patterns gravés (D7 cost-of-escalation)

❌ **Page "générique" réutilisable cross-persona** (template uniforme avec couleur swappée) — **REFUSÉ**. Coût caché 1an+ : aucune marque reconnaissable, aucune conversion ICP-spécifique. V1 a dérivé ici, c'est précisément ce que cet ADR corrige.

❌ **Persona sans posture éditoriale distincte** — REFUSÉ. Si un persona ne peut pas être distingué des 3 autres en 1 seconde, la posture a échoué.

❌ **Chevauchement volontairement gardé pour "cohérence de marque"** — REFUSÉ. Anti-pattern "cohérence" = confusion avec **uniformité**. La cohérence de marque canonique A'Space = **sister-ships** (3 postures sœurs, pas 1 template), PAS uniformité. ADR-ICP-NEXUS-001 §3 piliers Nexus + ADR-L2-AAAS-001 AaaS 3 variants sont déjà des sister-ships : même pattern appliqué aux 3 landings.

❌ **Pricing différencié par persona** — REFUSÉ. Sister-canon ADR-AAAS-PRICING-001 + ADR-ANTI-PAPERCLIP-001. Pricing uniforme $1000/mois partout.

❌ **Élément signature partagé entre 2 personas** — REFUSÉ. La marginalia handwritten, le ticker pseudo-code et le SOP-to-Skill before/after sont **uniques par construction**. Tout copier-coller d'un élément signature = violation directe de la §4 matrice.

❌ **Display italic identique entre 2 personas** — REFUSÉ. Fraunces italic est réservé à Marcus. Source Serif italic est réservé à David. Harrison n'utilise pas d'italic display (Outfit géométrique). Si un 4ᵉ persona veut un italic display, il doit être **un 3ᵉ font** (pas Fraunces, pas Source Serif).

❌ **Section naming `§N.M` / `[M0X]` / `WORKBENCH 0X` collapsé** — REFUSÉ. Chaque grammaire est un signal sémiotique du monde lexical. Les 3 grammaires sont **3 langues**.

❌ **Mapping persona 4-8 inventé** — REFUSÉ. Cet ADR ne spécifie que les **3 personas prioritaires** (Marcus/Harrison/David). Pour Amara/Christian/Clara cités PRD-NEXUS §4, suivre le workflow §7. Pour un hypothétique 5ᵉ/6ᵉ/7ᵉ/8ᵉ persona, **refus d'invention** : attendre un ADR-ICP-NEXUS amendé ou nouveau.

❌ **Mention "local-first" / "2027"** — REFUSÉ. Cet ADR n'engage pas de roadmap temporelle, ni de positionnement infra local-first. Sister-canon : si ces termes doivent apparaître, c'est dans un ADR-ICP-NEXUS amendé ou un ADR-LANDING-COPY-001 amendé, **pas ici**.

## 9. References & Sister-canon

### Sister-canon RATIFIED (à respecter absolument)

- **ADR-ICP-NEXUS-001** (RATIFIED 2026-06-21) — persona "Expert méthodique" + mantra + 3 piliers Nexus
- **ADR-AAAS-PRICING-001** (RATIFIED 2026-06-24) — $1000/mois ×100, identique partout
- **ADR-ANTI-PAPERCLIP-001** (RATIFIED 2026-06-21) — sobriété, anti-paperclip
- **ADR-ANTI-TEMPLATE-001** (RATIFIED) — patterns bannis génériques
- **ADR-L2-AAAS-001** (RATIFIED) — AaaS 3 variants = sister-ships doctrine

### Sister-canon DRAFT (à ratifier en parallèle)

- **ADR-LANDING-PERSONAS-001** — 3 landings distinctes spec (V1 DRAFT)
- **ADR-LANDING-AESTHETIC-001** — doctrine esthétique en miroir d'ANTI-TEMPLATE
- **ADR-LANDING-COPY-001** — doctrine copywriting + vocabulary canonique signé
- **ADR-DESIGN-SYSTEM-001** — tokens canoniques (palette/font/space)

### Empirical V2 D1 receipts (3 livrables radicaux)

- `C:\Users\amado\omk-nexus-landing-3-personas\v2\marcus\index.html` — Editorial Ledger empirique
- `C:\Users\amado\omk-nexus-landing-3-personas\v2\harrison\index.html` — Terminal Stratégique empirique
- `C:\Users\amado\omk-nexus-landing-3-personas\v2\david\index.html` — Atelier Industriel empirique

### References inspirations V2 (fetch-vérifiées live)

- `_references\apartamentomagazine.com-fetch.md` — mood Editorial Ledger
- `_references\linear.app-fetch.md` — mood Terminal Stratégique
- `_references\teenage.engineering-fetch.md` — mood Atelier Industriel

### PRD source

- **PRD-NEXUS-EVOLUTION-IA-001 §3 §4** — 3 strates × 10 ICPs × 6 candidates × 5 personas (3 prioritaires : Marcus/Harrison/David)

### Workflow d'amendement

- D4 append-only : ne JAMAIS réécrire cet ADR
- Tout amendement = nouvelle section datée + bump version
- Sister-canon `ADR-REF-PERSONAS-001` doit rester l'ancre des **règles de différenciation** ; les **3 personas canon** sont l'épitomé actuel. Un 4ᵉ persona amendé cet ADR, ne le crée pas ailleurs.

---

**Sign-off gate** : A0 ratification requise avant promotion DRAFT → RATIFIED. Gate HITL : reviewer ≠ auteur, sœur canon check (3 empiriques V2 + 3 références + sister-canon DRAFT aligné).
