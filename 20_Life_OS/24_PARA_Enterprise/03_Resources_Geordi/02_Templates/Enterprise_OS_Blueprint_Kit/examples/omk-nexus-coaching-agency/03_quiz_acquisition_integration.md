---
type: example-quiz-acquisition-integration
id: OMK_NEXUS_QUIZ_ACQUISITION_INTEGRATION
title: "OMK Nexus BOS - Quiz d'Acquisition Medvi integre a l'Agentic Dashboard"
status: RATIFIED
date: 2026-07-05T09:45:00-04:00
author: HA
sister: examples/omk-nexus-coaching-agency/02_first_session_runbook.md
append_only: true
---

# 03 - Quiz d'Acquisition Medvi integre a l'Agentic Dashboard

> Documentation technique de l'integration du Quiz d'Acquisition Medvi (audit context) dans l'Agentic Dashboard (Tier T1 OMK Nexus BOS).

## Pourquoi ce quiz ?

Le Quiz d'Acquisition Medvi est ne comme **pattern de vente par preuve de ROI** : le prospect entre ses volumes d'activite, le systeme fait tourner une simulation en arriere-plan, et delivre en ~30 secondes une cartographie de pertes financieres structuree.

**Dans le contexte Medvi** : le quiz etait utilise pour vendre des programmes de perte de poids (niche medicale, chute FDA).

**Dans le contexte OMK Nexus BOS** : le meme pattern est reutilise pour vendre de l'architecture agentique B2B (niche coaching, EU AI Act aware). Meme structure (Quiz -> Simulation -> Cartographie), domaine different.

L'integration avec l'Agentic Dashboard permet :
- Self-serve 24/7 (le prospect fait le quiz quand il veut)
- Scoring automatique (lead qualified si score >= 0.7)
- Handoff vers Telegram bot pour closing humain
- Audit trail complet (chaque reponse tracee pour compliance)

## Architecture du Quiz

### Frontend (Agentic Dashboard, simulation web)

```
[Hero section]
  Titre : "Decouvrez combien vous depensez en operations inutiles"
  Sous-titre : "Quiz 90 secondes - Sans engagement - Resultat immediat"
  CTA : "Commencer le Quiz"

[Step 1/5] Identification
  - Nom / Prenom (optionnel)
  - Email professionnel (requis pour recevoir le rapport)
  - Nom de l'entreprise
  - Secteur (dropdown : Coaching B2B / Agence BD / SaaS / Autre)

[Step 2/5] Volumes d'activite
  - Nombre d'appels de vente / semaine : [slider 0-200]
  - Nombre de transcripts analyses / mois : [slider 0-1000]
  - Nombre de prospects contacts / semaine : [slider 0-500]
  - Nombre d'onboardings clients / mois : [slider 0-50]
  - Taille de l'equipe (sales + ops) : [slider 0-100]

[Step 3/5] Stack actuelle
  - Outils payants coches (multiselect) :
    [ ] Otter.ai / Gong (~$30-300/mois)
    [ ] Lemlist / Instantly (~$50-200/mois)
    [ ] HubSpot / Salesforce CRM (~$50-500/mois)
    [ ] Notion (~$10-50/mois)
    [ ] Calendly (~$10-30/mois)
    [ ] Zapier (~$30-300/mois)
    [ ] Autre : [text]
  - Couts mensuels totaux estimes : [auto-calcule]

[Step 4/5] Frustrations
  - "Quelle est votre plus grande frustration operationnelle ?" [textarea]
  - "Avez-vous tente l'automatisation IA ? Si oui, qu'est-ce qui a foire ?" [textarea]

[Step 5/5] Engagement
  - "Etes-vous pret a investir $1k/mois pour automatiser ?" [Oui / Non / Peut-etre]
  - "Timeline de decision ?" [Immediat / 1-3 mois / 3-6 mois / Exploration]

[Submission]
  -> POST /api/quiz/submit (JSON payload)
  -> Trigger simulation background (Sonnet tier)
  -> Show "Analyse en cours..." (~30 sec)
  -> Redirect to /quiz/report/{session_id}
```

### Backend (Fargate orchestrator, Phase 2 - pour l'instant c'est simule)

```python
# Pseudo-code du handler
@app.post("/api/quiz/submit")
async def submit_quiz(payload: QuizSubmission):
    # 1. Persist raw submission in DynamoDB
    item = await ddb.put_item("quiz_submissions", payload.dict())

    # 2. Trigger background simulation (Sonnet tier)
    task = await fargate.run_task(
        image="omk-nexus-quiz-sim:v1",
        env={"submission_id": item.id, "model": "sonnet"}
    )

    # 3. Return submission_id immediately (progressive UX)
    return {"submission_id": item.id, "status": "processing"}

@app.get("/quiz/report/{session_id}")
async def get_report(session_id: str):
    # Check if simulation complete
    report = await ddb.get_item("quiz_reports", session_id)
    if report.status == "complete":
        return report
    elif report.status == "processing":
        return {"status": "processing", "poll_after_ms": 2000}
    else:
        return {"status": "error", "message": report.error}
```

### Simulation Sonnet (Tier 2 du Triptyque)

Le systeme prend les inputs et genere une cartographie structuree :

```yaml
cartographie:
  cout_actuel:
    outils_mensuels: $X (liste detaillee)
    rh_maintenance: $Y (heures admin x taux horaire)
    cout_acquisition: $Z (Lemlist + temps prospection)
    total: $X + $Y + $Z = $TOTAL_ACTUEL

  projection_omk:
    outils_mensuels: $X * 0.2 (remplaces par OMK Triptyque 1)
    rh_maintenance: $Y * 0.1 (automatise par LD01 Ops)
    cout_acquisition: $Z * 0.3 (AAARR signal > email blast)
    total: $PROJECTION_OMK

  economie_mensuelle: $TOTAL_ACTUEL - $PROJECTION_OMK
  roi_annuel: economie_mensuelle * 12
  payback_period: $1000 / economie_mensuelle (en mois)

  scoring:
    fit_score: 0.85 # 0-1 base sur les inputs
    pain_severity: high # low/medium/high
    urgency: 1-3 mois # timeline
    budget_capacity: $1000+/mois confirme ou pas

  next_action:
    - "GO pour beta-coach early access (Phase 2)"
    - "Wait for Phase 3 official launch (09/07+)"
    - "Refer to a peer coach (recommandation loop AAARR)"
```

## DLP-light filter sur les outputs

Tous les outputs du Quiz passent par `dlp_light_filter.py` AVANT d'etre persistes ou retournes au prospect. 7 patterns scannes (per `specs/security_spec_omk_nexus.md`) :

- AWS keys, GitHub PATs, Slack tokens, PEM keys = BLOCK
- Credit cards, SSNs = BLOCK
- Email + phone (PII basique) = WARN + masking

Le filtre est applique au niveau du Fargate handler avant le write DynamoDB ET avant la response au frontend.

## Integration avec les 11 prompts AAARR

Apres le Quiz, le prospect est score 0-1. Si score >= 0.7 :
1. **AAARR Acquisition prompt #1** : scrape Apollo pour des prospects similaires (meme secteur, meme taille)
2. **AAARR Activation prompt #2** : pre-redige une sequence d'approche pour le prospect lui-meme (referral loop)
3. **AAARR Retention prompt #1** : inscrit le prospect dans la nurture sequence (emails valeur)
4. **AAARR Recommandation prompt #1** : demande au prospect de referer 1-2 pairs (loop ouvert)

Si score < 0.7 :
- Nurture sequence passive seulement
- Pas d'AAARR Acquisition actif (pas qualified)
- Re-essai du Quiz dans 90 jours avec nouveau contexte

## Audit trail

Chaque Quiz submission genere 3 entrees dans le write-once audit log (S3 Object Lock, 7-year hold) :
1. `quiz_submission_{id}` (input raw + timestamp + IP hash)
2. `quiz_simulation_{id}` (Sonnet output + tokens used + cost estimate)
3. `quiz_report_view_{id}` (quand le prospect a vu le rapport + duration + scroll depth)

Ces 3 entrees sont liees par `submission_id` pour permettre une analyse forensique en cas de dispute.

## Phase 2 deliverables

- Implementation reelle du Fargate orchestrator
- Migration du Quiz de la simulation vers le runtime reel
- DLP-light middleware deploye en production
- AAARR prompts valides sur 100+ signaux reels
- 3 beta-coachs en early access utilisent le Quiz live
- 10+ prospects qualifies avec conversion > 5%

## Phase 3 deliverables

- 100 clients actifs utilisent le Quiz self-serve
- DLP complet Blueprint section 6 (9 patterns)
- EU AI Act compliance documentee
- ROI reel valide sur 100+ cas

## Anti-patterns

- Ne JAMAIS exposer le quiz sans DLP-light actif
- Ne JAMAIS promettre un ROI chiffre dans le quiz (projections, pas garanties)
- Ne JAMAIS envoyer les reponses a un outside vendor (Bedrock in-account obligatoire)
- Ne JAMAIS garder les PII au-dela de 90 jours dans le cache semantique
- Ne JAMAIS utiliser le quiz comme outil de spam (chaque reponse = engagement reel)
