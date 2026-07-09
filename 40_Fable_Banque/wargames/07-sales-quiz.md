# WARGAME 07 — Quiz Simulateur d'Inférence (Sales, pattern Medvi assaini)

> Wargamé par Fable 5, 2026-07-06. Exécuteur : **Hermes** (B2 JohnJones/Illuminati). Exécutable blind.
> Closing par preuve mathématique du ROI — pas d'appel à froid.

## RECON (fait — D1)
- Landing EN existante : single-file statique `omk-nexus-landing-en` (Vercel 200 OK, dark `#0A0E16`+`#C8A55C`) → **le Quiz suit le même pattern** (HTML/JS single-file, zéro framework, zéro build).
- 3 Personas (transcripts Gemini) : Marcus Vance (C-Suite/compliance) · Clara Sterling (BDR/Jevons) · David Kross (Fractional COO/SOPs).
- Constantes sourcées : plan MiniMax 5,1Md tokens/50$/mo (ADR-LLM-COST-COMPARE-001, D1-verified) ; prix cloud ~15$/M tokens output (ordre de grandeur public) → marquer `≈` ; pénalités EU AI Act → RECON NEEDED (fourchette officielle à citer, pas inventer).

## MOVES
**M1 — L'arbre du quiz (6 questions, 1 friction par persona)**
- Action : Q1 rôle (coach exécutif / agence BDR / COO fractionné / autre) → branche persona ; Q2 nb coachs/SDRs ; Q3 heures de calls enregistrés/mois ; Q4 stack IA actuelle (ChatGPT/Claude persos · API cloud · rien) ; Q5 secteur régulé o/n ; Q6 heures admin/semaine/personne.
- Observation : 6 questions, chaque réponse = valeur numérique ou branche ; aucun texte libre (déterminisme du calcul).
- Échec probable : abandon avant la fin → **cause** : trop long/abstrait. **Contre-action** : barre de progression + résultat partiel teasé dès Q3 (« déjà ~$X détectés »).

**M2 — Le moteur de calcul (transparent, chaque constante sourcée)**
- Action : pertes = (a) taxe admin : Q6 × 52 × taux horaire chargé (défaut 85$/h, éditable) × Q2 ; (b) tokens : Q3 × ~25k tokens/h transcrite × ≈15$/M cloud VS amorti plan fixe (~0,01$/M à 5,1Md/50$) ; (c) risque compliance : SI Q5=oui ET Q4=comptes persos → ligne rouge « exposition EU AI Act » SANS chiffre inventé (lien source officielle, RECON NEEDED).
- Observation : le détail du calcul est AFFICHÉ (pas une boîte noire) — c'est la crédibilité du closing.
- Fork : SI l'utilisateur met des valeurs absurdes (0 partout) → verdict honnête « structure déjà sobre » + CTA doux (newsletter), pas de pertes gonflées. L'anti-Medvi, c'est ça.

**M3 — Les 3 sorties types**
- Action : verdict par persona — Marcus : « Chef de Cabinet Souverain : $X admin + exposition compliance → plan de libération » ; Clara : « Paradoxe de Jevons : facture $Y→$Z, marge récupérable » ; David : « SOPs dormants : N h de conduite du changement → skills exécutables ». Chaque verdict cite SES inputs.
- Observation : 3 wordings écrits, CTA unique : call 20 min (pas d'achat direct — forfait 1000$ se close en call).

**M4 — Implémentation single-file + anti-Medvi**
- Action : `quiz.html` autonome (même palette que la landing), calcul 100% client-side (ZÉRO donnée envoyée — cohérence souveraineté : le prospect DOIT constater que rien ne part), disclaimers : estimations, pas de conseil médical/légal, sources visibles.
- Observation : ouvrir le fichier local = quiz fonctionnel offline ; onglet réseau vide pendant tout le parcours.
- Échec probable : « client-side = pas de lead capturé » → **cause** : tension capture vs preuve de souveraineté. **Contre-action** : la capture est APRÈS le verdict, opt-in explicite (email pour recevoir le rapport PDF) — le verdict reste gratuit sans email.

## ABORT CONDITIONS
1. Une constante business introuvable en source → elle devient un slot éditable affiché, jamais un chiffre affirmé.
2. Le déploiement exigerait un backend → STOP (single-file est le contrat).

## VERIFICATION RUNS
1. Ouvrir quiz.html local : 6 questions traversées, verdict s'affiche, onglet réseau = 0 requête.
2. Les 3 branches persona testées avec inputs types → 3 verdicts distincts, chiffres reproductibles.
3. grep quiz.html : `fetch(|XMLHttpRequest` absent hors bloc opt-in email.

## RED-TEAM PASS
- **Échouée** : « le pattern Medvi est toxique en soi » — non : ce qui a tué Medvi = deepfakes + claims médicaux + affiliés sauvages ; ici zéro des trois, et le calcul est transparent.
- **Réussie → patch** : « Marcus refuse le Docker local (peur technique) et le quiz le perd » — patch : le verdict Marcus propose DEUX routes : self-hosted (souverain) OU **managé par OMK** (on opère pour vous) — la peur technique devient l'argument du forfait.

## SELF-GRADE : 12/12
