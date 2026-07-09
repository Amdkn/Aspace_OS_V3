---
type: prompts-pack
id: PROMPTS_AAARR_GROWTH_SIGNAL
title: "AAARR Growth Signal Pack - 11 prompts (Acquisition/Activation/Retention/Recommandation/Revenu)"
status: RATIFIED
date: 2026-07-05T09:45:00-04:00
author: HA (A3 Picard in PARA)
refines: prompts/01..11_*.txt (Build-It Prompt Pack canon, 11 fichiers .txt intouchables)
sister: ADR-LD01-011 D1 / spec/agent_spec_omk_nexus.md
append_only: true
tier: T1 (Haiku primarily, Sonnet for high-stakes)
dlp_light: REQUIRED (7 patterns subset, see specs/security_spec_omk_nexus.md)
---

# AAARR Growth Signal Pack - 11 Prompts

> Pack de 11 prompts pour le signal acquisition OMK Nexus BOS (Tier T1 coaching B2B). Pattern AAARR (Acquisition / Activation / Retention / Recommandation / Revenu) per Gemini Deep Research Tier 2 Growth Domain. **Tous les outputs DOIVENT passer par `dlp_light_filter.py` AVANT insertion en DB**.

## Convention d'usage

Chaque prompt est invoque par un agent Bedrock Haiku (Tier 1, ~10x moins cher que Sonnet). L'output est :
1. Filtre par `dlp_light_filter.py` (7 patterns subset)
2. Score selon AAARR (0-1)
3. Si score >= 0.7 : persist + trigger next stage
4. Si score < 0.7 : discard + log "low_quality_signal"

Les prompts sont concus pour etre **idempotents** (meme input -> meme output, modulo le timestamp) et **scoped** (chaque prompt a une responsabilite unique, pas de surcharge).

---

## ACQUISITION (2 prompts)

### Prompt #1 - Apollo Signal Scraper

**Role** : Scraper Apollo.io pour identifier les embauches de directeurs commerciaux / VP Sales dans les 30 derniers jours (signal chaud d'intention d'achat d'outils sales).

**Input schema** :
```json
{
  "apollo_query": {
    "job_titles": ["VP Sales", "Head of Sales", "Chief Revenue Officer", "Sales Director"],
    "industries": ["Business Consulting", "Professional Training", "Executive Coaching"],
    "company_size": ["11-50", "51-200", "201-500"],
    "posted_within_days": 30,
    "geo": ["France", "Belgium", "Switzerland", "Canada"]
  }
}
```

**Output schema** :
```json
{
  "signals": [
    {
      "company_name": "string",
      "company_domain": "string",
      "hiring_manager_name": "string",
      "hiring_manager_email": "string (if available)",
      "job_title": "string",
      "posted_date": "ISO 8601",
      "company_size": "string",
      "annual_revenue_estimate": "string",
      "apollo_score": "0-1",
      "aaarr_acquisition_score": "0-1",
      "rationale": "string (1-2 sentences why this is a hot signal)"
    }
  ],
  "total_signals_found": "int",
  "execution_timestamp": "ISO 8601"
}
```

**Tier** : Haiku. **Cost** : ~$0.02/query.

---

### Prompt #2 - Reddit Pain Point Scraper

**Role** : Scraper Reddit (subreddits r/sales, r/entrepreneur, r/coaching, r/salesforce) pour identifier les discussions recentes (90 derniers jours) mentionnant des frustrations operationnelles liees a notre niche.

**Input schema** :
```json
{
  "subreddits": ["sales", "entrepreneur", "coaching", "smallbusiness"],
  "keywords": ["otter.ai alternative", "lemlist too expensive", "hubspot too complex", "ai for coaching", "automate sales calls"],
  "time_filter": "month",
  "min_upvotes": 5
}
```

**Output schema** :
```json
{
  "discussions": [
    {
      "post_id": "string",
      "post_title": "string",
      "post_url": "string",
      "author_username": "string",
      "subreddit": "string",
      "score": "int (upvotes)",
      "num_comments": "int",
      "created_utc": "ISO 8601",
      "pain_point_summary": "string (1-2 sentences)",
      "aaarr_acquisition_score": "0-1",
      "match_with_omk_niche": "0-1",
      "recommended_response": "string (draft Reddit comment or DM template)"
    }
  ],
  "total_discussions_found": "int"
}
```

**Tier** : Haiku. **Cost** : ~$0.03/query.

---

## ACTIVATION (3 prompts)

### Prompt #3 - Signal Qualification Scorer

**Role** : Prendre un signal brut (Apollo ou Reddit) et le scorer selon 6 dimensions : Fit (notre niche), Pain (urgence), Budget (capacite $1k/mois), Authority (decideur), Timeline (rapidite), Engagement (interaction).

**Input schema** :
```json
{
  "signal": {
    "source": "apollo|reddit",
    "raw_data": "object (per Prompt #1 or #2 output)",
    "company_context": "optional object (Crunchbase enrichment)"
  }
}
```

**Output schema** :
```json
{
  "qualification": {
    "fit_score": "0-1",
    "pain_score": "0-1",
    "budget_score": "0-1",
    "authority_score": "0-1",
    "timeline_score": "0-1",
    "engagement_score": "0-1",
    "global_score": "0-1 (weighted average)",
    "qualified": "boolean (true if global >= 0.7)",
    "next_action": "string (e.g., 'send_outreach_email', 'schedule_call', 'discard')",
    "rationale": "string (2-3 sentences)"
  }
}
```

**Tier** : Haiku. **Cost** : ~$0.01/signal.

---

### Prompt #4 - Outreach Email Drafter

**Role** : Prendre un signal qualifie (score >= 0.7) et rediger un email d'approche hyper-specifique (3-5 phrases, ton direct, pas de spam).

**Input schema** :
```json
{
  "qualified_signal": "object (from Prompt #3)",
  "sender_context": {
    "sender_name": "A0 (Amadeus)",
    "sender_role": "Founder OMK Nexus",
    "previous_touchpoints": "array (emails sent before, if any)"
  },
  "email_template": "first_touch|second_touch|referral_intro"
}
```

**Output schema** :
```json
{
  "email": {
    "subject": "string (5-8 words, no spam triggers)",
    "body": "string (3-5 sentences, 50-100 words)",
    "personalization_anchors": "array (specific data points referenced)",
    "call_to_action": "string (one specific ask)",
    "send_recommendation": "today|tomorrow|wait_for_trigger",
    "follow_up_if_no_reply_days": "int (typically 3-5)"
  }
}
```

**Tier** : Sonnet (high-stakes, first impression). **Cost** : ~$0.05/email.

---

### Prompt #5 - LinkedIn Connection Request Drafter

**Role** : Rediger une demande de connexion LinkedIn (300 char max) pour les prospects qualifies, en s'appuyant sur leur activite recente (post, commentaire).

**Input schema** :
```json
{
  "linkedin_profile": {
    "name": "string",
    "headline": "string",
    "recent_activity": "array (last 3 posts/comments)"
  },
  "context": "object (from Prompt #3)"
}
```

**Output schema** :
```json
{
  "connection_request": {
    "message": "string (<= 300 chars)",
    "tone": "professional|friendly|direct",
    "personalization_hook": "string",
    "send_recommendation": "boolean"
  }
}
```

**Tier** : Haiku. **Cost** : ~$0.01/request.

---

## RETENTION (2 prompts)

### Prompt #6 - Nurture Email Sequencer

**Role** : Pour un prospect pas encore qualified (score < 0.7) ou en attente de decision, generer une sequence de 5 emails valeur (1/semaine) pour rester top-of-mind.

**Input schema** :
```json
{
  "prospect": {
    "name": "string",
    "company": "string",
    "industry": "string",
    "pain_points": "array (from Quiz d'Acquisition or AAARR signals)"
  },
  "sequence_duration_weeks": 5
}
```

**Output schema** :
```json
{
  "sequence": [
    {
      "week": "int (1-5)",
      "subject": "string",
      "body": "string (200-300 words, valeur pure, pas de pitch)",
      "value_topic": "string (e.g., 'How we reduced Otter.ai costs by 80%')",
      "cta": "string (soft, e.g., 'reply if interested')"
    }
  ]
}
```

**Tier** : Haiku. **Cost** : ~$0.08/sequence (5 emails).

---

### Prompt #7 - Engagement Re-igniter

**Role** : Pour un prospect qui a stoppe de repondre (no reply 30+ jours), rediger un email de re-engagement (ton leger, valeur haute).

**Input schema** :
```json
{
  "prospect": "object",
  "last_interaction": {
    "date": "ISO 8601",
    "channel": "email|linkedin|telegram",
    "their_last_message": "string (optional)"
  },
  "new_value_trigger": "string (optional, e.g., 'new customer case study')"
}
```

**Output schema** :
```json
{
  "reignite_email": {
    "subject": "string (curiosity-driven, no spam)",
    "body": "string (100-150 words, personal + value)",
    "send_recommendation": "boolean",
    "expected_reactivation_probability": "0-1"
  }
}
```

**Tier** : Haiku. **Cost** : ~$0.02/email.

---

## RECOMMANDATION (2 prompts)

### Prompt #8 - Referral Request Drafter

**Role** : Pour un client satisfait (> 3 mois retainer), rediger une demande de referral (1-2 peers du meme secteur).

**Input schema** :
```json
{
  "satisfied_client": {
    "name": "string",
    "company": "string",
    "satisfaction_score": "0-1",
    "tenure_months": "int"
  },
  "ideal_referral_profile": "string (e.g., 'VP Sales at 50-200 person coaching agency in France')"
}
```

**Output schema** :
```json
{
  "referral_request": {
    "channel": "email|telegram|linkedin_dm",
    "message": "string (150-250 words)",
    "value_offer_to_referral": "string (e.g., 'free Quiz d'Acquisition audit')",
    "incentive_structure": "string (e.g., '1 month free if referral signs')"
  }
}
```

**Tier** : Sonnet (delicate ask). **Cost** : ~$0.04/request.

---

### Prompt #9 - Peer Introduction Broker

**Role** : Pour 2 clients satisfaits du meme secteur, rediger un email d'introduction croisee (peer-to-peer, valeur mutuelle).

**Input schema** :
```json
{
  "client_a": "object",
  "client_b": "object",
  "shared_context": "string (why they should know each other)"
}
```

**Output schema** :
```json
{
  "intro_email": {
    "to_a": "string (introducing B)",
    "to_b": "string (introducing A)",
    "context_bridge": "string",
    "suggested_next_step": "string (e.g., 'schedule a 30-min call')"
  }
}
```

**Tier** : Sonnet (delicate). **Cost** : ~$0.06/intro.

---

## REVENU (2 prompts)

### Prompt #10 - Quiz d'Acquisition Result Drafter

**Role** : Prendre les inputs du Quiz d'Acquisition et generer la cartographie de pertes structuree (4 axes : outils, RH maintenance, acquisition, total).

**Input schema** :
```json
{
  "quiz_inputs": "object (from frontend Quiz)",
  "industry_benchmarks": "object (avg costs per industry)"
}
```

**Output schema** :
```json
{
  "cartographie": {
    "cout_actuel": {
      "outils_mensuels": "number (USD)",
      "rh_maintenance": "number (USD)",
      "cout_acquisition": "number (USD)",
      "total": "number (USD)"
    },
    "projection_omk": {
      "outils_mensuels": "number",
      "rh_maintenance": "number",
      "cout_acquisition": "number",
      "total": "number"
    },
    "economie_mensuelle": "number",
    "roi_annuel": "number",
    "payback_period_months": "number",
    "scoring": {
      "fit": "0-1",
      "pain_severity": "low|medium|high",
      "urgency": "1-3 mois|3-6 mois|6+ mois|exploration",
      "budget_capacity": "confirmed|likely|unlikely"
    },
    "next_action": "string"
  }
}
```

**Tier** : Sonnet (high-stakes, client-facing). **Cost** : ~$0.10/report.

---

### Prompt #11 - Closing Sequence Drafter

**Role** : Pour un prospect qui a complete le Quiz avec score >= 0.7 et a demande un follow-up, rediger une sequence de closing (3 emails sur 7 jours, ton assumé, preuve ROI en tete).

**Input schema** :
```json
{
  "quiz_report": "object (from Prompt #10)",
  "prospect": "object",
  "closing_path": "beta_coach_early_access|wait_phase_3|referral"
}
```

**Output schema** :
```json
{
  "closing_sequence": [
    {
      "day": "int (1, 3, 7)",
      "subject": "string",
      "body": "string (200-400 words, assumé, preuve ROI)",
      "objection_handler": "string (anticipated objection + response)",
      "cta": "string (specific ask: schedule call, sign, refer)"
    }
  ],
  "expected_conversion_probability": "0-1",
  "alternative_paths_if_no_reply": "array of strings"
}
```

**Tier** : Sonnet (closing = high-stakes). **Cost** : ~$0.15/sequence.

---

## Couts agreges (Haiku primarily, Sonnet for high-stakes)

Pour 100 clients prospects :
- 100 x Acquisition (2 prompts) = $5
- 100 x Activation (3 prompts) = $7
- 100 x Retention (2 prompts) = $10
- 50 x Recommandation (2 prompts, 50% des clients satisfont) = $5
- 100 x Revenue (2 prompts) = $25
- **TOTAL : ~$52/mois** (consistent avec cost_spec_omk_nexus.md Projection MiniMax)

## Anti-patterns

- Ne JAMAIS executer un prompt sans DLP-light filter actif
- Ne JAMAIS scorer un signal sans contexte (toujours cross-checker Crunchbase/Apollo)
- Ne JAMAIS envoyer un email sans review humain pour les closes (Sonnet a un taux d'erreur ~5%)
- Ne JAMAIS promettre un ROI chiffre dans un email (utiliser projections, pas garanties)
- Ne JAMAIS scraper un site qui l'interdit explicitement dans robots.txt
- Ne JAMAIS spammer un prospect qui a demande a ne plus etre contacte
