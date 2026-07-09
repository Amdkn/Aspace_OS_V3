# WARGAME 06 — Growth AARRR : les 11 prompts de signal (fork B de NEXUS-NICHE-001)

> Wargamé par Fable 5, 2026-07-06. Exécuteur : **Hermes** (B2 Superman/Guardians). Exécutable blind.
> Cible : 10 premiers Executive Coaches → pipeline des 100×1000$.

## RECON (fait — D1)
- 3 signaux canon (ADR-NEXUS-NICHE-001) : **Alpha** recrutement tech · **Bêta** expansion +15%/6mo · **Gamma** compliance (contrat Fortune 500/régulé).
- 10 catégories en 3 strates (transcripts Gemini) : A coaching exécutif ×3 · B agences growth/BDR ×3 · C conseil opérationnel ×4.
- 2 séquences template existent (email Alpha « Jevons », LinkedIn Gamma « compliance »). MCP Apollo dispo (tools apollo_*) mais auth à vérifier au run → RECON NEEDED : `apollo_users_api_profile` répond ?
- D6 précédent : IP résidentielle blacklistable (leçon YouTube IpBlocked #10).

## MOVES
**M1 — La matrice 11 prompts** (signal × strate, pas 11 inventions)
- Action : générer `loops/artifacts/docs/aaarr-11-prompts.md` : Alpha×{A,B,C} =3 · Bêta×{A,B,C} =3 · Gamma×{A,B,C} =3 · +2 transverses (référence sortante : « votre concurrent X a réduit ses coûts de » ; réactivation : lead froid 30j). Chaque prompt : input (données du signal), template FR+EN, variable-slots, CTA unique (le Quiz, wargame 07).
- Observation : 11 prompts numérotés, chacun ≤ 150 mots, zéro claim médical, zéro deepfake (anti-Medvi).
- Échec probable : prompts génériques interchangeables → **cause** : le signal n'est pas dans le texte. **Contre-action** : règle : la 1re phrase DOIT citer le fait observé (l'offre d'emploi, le contrat annoncé) — sinon rejet.

**M2 — Le pipeline signal→séquence (pré-rédigé, JAMAIS auto-envoyé)**
- Action : flux : scraper/Apollo → `loops/artifacts/signals/lead-<slug>.md` (fait observé + source + strate) → tri AARRR → séquence pré-rédigée stockée `artifacts/docs/outreach/<tenant>/` → **envoi = ship OUTBOARD** (gated `enable_ship_outboard.flag`, gagné à 3 cycles verts — pas ce GO).
- Observation : zéro appel d'envoi dans le code du pipeline ; la sortie est un fichier.
- Fork : SI Apollo 401/rate-limit → bascule source locale (annuaires publics scrapés lentement, 1 req/10s) + signal `apollo-blocked` ; ne JAMAIS burn l'IP (D6 #10).

**M3 — Qualification AARRR**
- Action : scoring simple par lead : Acquisition (signal fort=2/faible=1) + Activation (taille équipe coach ≥5 = +1) + Revenue (secteur régulé = +2, budget implicite) ; seuil contact ≥ 3. Stocké dans le fichier lead.
- Observation : chaque lead a un score reproductible (mêmes inputs → même score).

**M4 — Métriques d'amorçage (branchées wargame 03)**
- Action : compteurs pour le CEO-Bench : leads qualifiés/WK, séquences prêtes/WK, (post-outboard : réponses, calls, closes). Book lit ces compteurs tant que MRR=0.
- Observation : le tick WF2 cite ces chiffres avec source fichier.

## ABORT CONDITIONS
1. Toute donnée scrapée contenant PII non-publique → route DLP (wargame 05) AVANT stockage ; DLP absent → STOP le scraping.
2. Apollo exige un scope payant non provisionné → flag ledger, continuer sur source locale.

## VERIFICATION RUNS
1. `aaarr-11-prompts.md` : grep compte 11 sections `## P[0-9]+` ; chaque P contient `{{FAIT_OBSERVE}}`.
2. Un lead test (fictif, marqué TEST) traverse le pipeline → fichier lead + score + séquence, ZÉRO requête d'envoi loggée.
3. grep du pipeline : aucun `send|sendmail|messages.send` hors bloc gated outboard.

## RED-TEAM PASS
- **Échouée** : « 11 prompts = spam à échelle » — non : chaque envoi reste outboard-gated + 1re phrase = fait observé (impossible à masser sans le signal).
- **Réussie → patch** : « le scoring sur-pondère Gamma (régulé=+2) et le pipeline ne produit QUE des leads compliance » — patch : quota par signal (max 50% d'un même type dans le top-10 hebdo) ; l'équilibre du pipeline est une métrique CEO-Bench.

## SELF-GRADE : 12/12
