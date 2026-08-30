import json

v1 = json.load(open('02_Areas_Spock.json', encoding='utf-8'))
v2 = json.load(open('02_Areas_Spock_v2.json', encoding='utf-8'))

# Heritage: v1+v2 types, relations, codes, contradictions
# v3 adds new types discovered in this wave

# New types from wave 3 (VPP rule, MUSE Quota Stage, Weekly Gate Check, Founder Load Ceiling,
# Beth HALT escalation matrix, AaaS Seed SQL Protocol, n8n Workflow, JTBD Packet, Meso Decision,
# Meso Issue, B1 Output Packet, Cerritos routing, etc.)

new_types_v3 = [
    {
        "nom": "VPP Hard Rule (Vitality Protection Protocol)",
        "attributs": ["signal", "GREEN", "ORANGE", "RED", "trigger_action"],
        "chemins": [
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/SUMMERS_VERSE_TEMPLATE.md",
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/B3_Area_Warp_Core/Lead_Lag_Logs/README.md"
        ]
    },
    {
        "nom": "Beth HALT Decision Tree",
        "attributs": ["ld03_state", "ld04_state", "trigger", "jerry_action", "beth_notification", "expansion_permission"],
        "chemins": [
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/SUMMERS_VERSE_TEMPLATE.md",
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/B1_Area_Direction/README.md"
        ]
    },
    {
        "nom": "Founder Load Ceiling",
        "attributs": ["ceiling_type", "green_state", "orange_state", "red_state"],
        "chemins": [
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/SUMMERS_VERSE_TEMPLATE.md"
        ]
    },
    {
        "nom": "Seasonal Biology Adjustment (J02)",
        "attributs": ["season (Winter/Spring/Summer-Autumn)", "domain", "winter_target", "spring_target", "summer_target"],
        "chemins": [
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/12WY_Area_Cadence/W01_W04_Foundation/README.md",
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/12WY_Area_Cadence/W05_W08_Scaling/README.md",
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/12WY_Area_Cadence/W09_W12_Optimization/README.md"
        ]
    },
    {
        "nom": "12WY Block",
        "attributs": ["block_number", "weeks", "primary_goal", "secondary_goal", "non_negotiable"],
        "chemins": [
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/12WY_Area_Cadence/W01_W04_Foundation/README.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/12WY_Area_Cadence/W05_W08_Scaling/README.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/12WY_Area_Cadence/W05.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/12WY_Area_Cadence/W08.md"
        ]
    },
    {
        "nom": "6-Account Banking Structure",
        "attributs": ["account (BUFFER/REINVEST/INDEPENDENCE/PROTECT/PLAY/GIVE)", "purpose", "allocation_pct"],
        "chemins": [
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/01_Capital_Architecture/README.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/02_Cash_Flow_Architecture/README.md"
        ]
    },
    {
        "nom": "Wealth Tier",
        "attributs": ["tier (T1 Safety / T2 Compound / T3 Business Equity / T4 Opportunistic)", "purpose", "income_share_pct", "deployment_condition"],
        "chemins": [
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/05_Investment_Accumulation/README.md"
        ]
    },
    {
        "nom": "Runway Gate",
        "attributs": ["color (RED/ORANGE/YELLOW/SURGE)", "months", "decision_authority"],
        "chemins": [
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/12WY_Area_Cadence/W01.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/01_Capital_Architecture/README.md"
        ]
    },
    {
        "nom": "Coverage Gate",
        "attributs": ["color", "coverage_pct", "decision_authority"],
        "chemins": [
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/02_Cash_Flow_Architecture/README.md"
        ]
    },
    {
        "nom": "Family Load Gate",
        "attributs": ["color", "score", "decision_authority"],
        "chemins": [
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/SUMMERS_VERSE_TEMPLATE.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/08_Family_Financial_Governance/README.md"
        ]
    },
    {
        "nom": "Risk Category",
        "attributs": ["category (Income Volatility/Market Investment/Liability/Family Load)", "description", "mitigation"],
        "chemins": [
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/03_Risk_Management/README.md"
        ]
    },
    {
        "nom": "Insurance Category",
        "attributs": ["category (Health/Disability/Liability/Life)", "coverage_target", "review_cadence"],
        "chemins": [
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/07_Insurance_Protection/README.md"
        ]
    },
    {
        "nom": "MUSE-eligibility Test",
        "attributs": ["qualifying_rules_count (7)", "disqualifiers_count (5)", "gate"],
        "chemins": [
            "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md",
            "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/B2_Area_Domains/06_MUSE_Eligible_Criteria_LD08/README.md"
        ]
    },
    {
        "nom": "Relational Capital Move (Voss/Grant/Cialdini)",
        "attributs": ["move (calibrated_question/label/mirror/giver/reciprocity)", "purpose", "principle_ref"],
        "chemins": [
            "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md",
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/12WY_Area_Cadence/README.md"
        ]
    },
    {
        "nom": "Flow Component (Csikszentmihalyi)",
        "attributs": ["component (clear_goals/immediate_feedback/challenge_skill_balance/deep_involvement/control/loss_self_consciousness/transformation_of_time)", "design_rule"],
        "chemins": [
            "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md"
        ]
    },
    {
        "nom": "Anti-Fun Audit (Creativity Gate 1)",
        "attributs": ["question", "answer_test", "if_failed_action"],
        "chemins": [
            "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md"
        ]
    },
    {
        "nom": "Creativity Crisis Mode",
        "attributs": ["mode (acute/chronic/recovery/building/stable)", "creative_output_rule"],
        "chemins": [
            "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/SUMMERS_VERSE_TEMPLATE.md"
        ]
    },
    {
        "nom": "Card Stack Component (B0 self-operating business)",
        "attributs": ["register (role_map/sop_map/training_map/metrics_map/exception_map)", "owner", "proof"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/01_E_MYTH_FRANCHISE_PROTOTYPE.md"
        ]
    },
    {
        "nom": "Delegation Slot (Who Not How)",
        "attributs": ["question", "assigned_layer", "output"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/03_WHO_NOT_HOW_DELEGATION_MATRIX.md"
        ]
    },
    {
        "nom": "Offer Packet Field (Hormozi)",
        "attributs": ["field (ICP/Pain/Dream_Outcome/Time_Delay/Effort/Risk_Reversal/Proof/Price_Logic)", "definition"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/04_OFFER_AND_BRAND_ENGINE.md"
        ]
    },
    {
        "nom": "Brand Packet Field (Billion Dollar Brand Club)",
        "attributs": ["field (Category/Enemy/Signature_Mechanism/First_Channel/Story_Asset)", "definition"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/04_OFFER_AND_BRAND_ENGINE.md"
        ]
    },
    {
        "nom": "Project Graduation Gate Ladder",
        "attributs": ["gate (0..7)", "name", "required_evidence", "decision_owner"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/10_PROJECT_GRADUATION_GATES.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/05_PROJECT_GRADUATION_GATES.md"
        ]
    },
    {
        "nom": "Status Ladder (Project Maturity)",
        "attributs": ["status (RAW_IDEA/MARKET_HYPOTHESIS/VALIDATION_SPRINT/PRODUCT_ONLY_PROTOTYPE/SOB_INCUBATION/OPERATING_BUSINESS_CANDIDATE/BUSINESS_DONE)", "meaning", "required_proof"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/05_PROJECT_GRADUATION_GATES.md"
        ]
    },
    {
        "nom": "Domain Pair Check (B2 Wheel Harmonization)",
        "attributs": ["pair", "question", "escalation_if_unresolved"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md"
        ]
    },
    {
        "nom": "Red Flag Combination (Wheel Health)",
        "attributs": ["combination", "rule"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md"
        ]
    },
    {
        "nom": "Council Mode (B2)",
        "attributs": ["mode (parallel/handoff/negotiation)", "rule"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/B2_DC_DIRECTION_COUNCIL_WORKFLOW.md"
        ]
    },
    {
        "nom": "B2 Meso Decision Packet",
        "attributs": ["meso_decision_id", "source_mandate", "mode", "impacted_domains", "tradeoff", "decision", "proof_expected"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/B2_DC_DIRECTION_COUNCIL_WORKFLOW.md"
        ]
    },
    {
        "nom": "B2 Peer Escalation Packet (meso)",
        "attributs": ["meso_issue_id", "requesting_domain", "peer_domain", "conflict", "options", "recommended_tradeoff", "b1_escalation_needed"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/B2_MESO_VP_SWARM_COORDINATION.md"
        ]
    },
    {
        "nom": "B1 North Star Statement",
        "attributs": ["horizon (1Y/3Y/10Y)", "statement", "minimum_outcome"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/01_NORTH_STAR_1Y_3Y_10Y.md"
        ]
    },
    {
        "nom": "Direction Invariant (B1)",
        "attributs": ["invariant", "owner"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/01_NORTH_STAR_1Y_3Y_10Y.md"
        ]
    },
    {
        "nom": "Validation Sprint Step",
        "attributs": ["step", "owner", "proof"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/09_MARKET_VALIDATION_SPRINT.md"
        ]
    },
    {
        "nom": "Weekly Area Management (WAM)",
        "attributs": ["step", "duration", "purpose"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/12WY_Area_Cadence/WEEKLY_EXECUTION_TEMPLATE.md"
        ]
    },
    {
        "nom": "Execution Score Zone",
        "attributs": ["zone", "execution_score_pct", "action"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/12WY_Area_Cadence/WEEKLY_EXECUTION_TEMPLATE.md"
        ]
    },
    {
        "nom": "Growth AARRR Stage",
        "attributs": ["stage (Acquisition/Activation/Retention/Revenue/Referral)", "principle_ref", "guardian_owner"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/01_Growth_Superman_Guardians/03_SUPERMAN_GROWTH_PRINCIPLES.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/01_Growth_Superman_Guardians/01_B3_AGENT_ROSTER.md"
        ]
    },
    {
        "nom": "Hero Identity Card (Squad Member)",
        "attributs": ["hero_name", "lore_role", "business_role", "principles", "aarrr_stage"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/01_Growth_Superman_Guardians/01_B3_AGENT_ROSTER.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/02_Sales_MartianManhunter_Illuminati/01_B3_AGENT_ROSTER.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/03_Product_Flash_Avengers/01_B3_AGENT_ROSTER.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/04_Ops_Batman_Fantastic4/01_B3_AGENT_ROSTER.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/05_IT_Cyborg_KangDynasty/01_B3_AGENT_ROSTER.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/06_Finance_WonderWoman_Thunderbolts/01_B3_AGENT_ROSTER.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/07_People_GreenLantern_XMen/01_B3_AGENT_ROSTER.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/08_Legal_Aquaman_Eternals/01_B3_AGENT_ROSTER.md"
        ]
    },
    {
        "nom": "B3 Squad (swarm)",
        "attributs": ["squad_name", "domain", "b2_owner", "lead_character", "members", "build_gates", "anti_patterns", "escalation_rule", "notion_source_url"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/01_Growth_Superman_Guardians/00_B3_SWARM_CONFIG.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/02_Sales_MartianManhunter_Illuminati/00_B3_SWARM_CONFIG.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/03_Product_Flash_Avengers/00_B3_SWARM_CONFIG.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/04_Ops_Batman_Fantastic4/00_B3_SWARM_CONFIG.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/05_IT_Cyborg_KangDynasty/00_B3_SWARM_CONFIG.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/06_Finance_WonderWoman_Thunderbolts/00_B3_SWARM_CONFIG.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/07_People_GreenLantern_XMen/00_B3_SWARM_CONFIG.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/08_Legal_Aquaman_Eternals/00_B3_SWARM_CONFIG.md"
        ]
    },
    {
        "nom": "Sales Principle Cluster",
        "attributs": ["cluster (A Offer / B Pricing / C Model / D Acquisition / E Discovery / F Persuasion / G Field craft)", "principles_count", "principles_count_total_v3"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/02_Sales_MartianManhunter_Illuminati/03_JOHNJONES_SALES_PRINCIPLES.md"
        ]
    },
    {
        "nom": "Growth Principle",
        "attributs": ["principle_number", "name", "aarrr_stage", "guardian_owner", "anti_pattern", "kr_ref"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/01_Growth_Superman_Guardians/03_SUPERMAN_GROWTH_PRINCIPLES.md"
        ]
    },
    {
        "nom": "Mode (Solaris/Nexus/Orbiter)",
        "attributs": ["name", "revenue_band", "capability_profile", "owner"],
        "chemins": [
            "02_Areas_Spock/Business_Pulse/README.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/01_NORTH_STAR_1Y_3Y_10Y.md"
        ]
    },
    {
        "nom": "B2 Domain (J01 Business)",
        "attributs": ["numero (01..08)", "hero (DC)", "squad (Marvel)", "krs", "principles_doc", "build_gates"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/01_Growth_Superman_Guardians/README.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/02_Sales_MartianManhunter_Illuminati/README.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/03_Product_Flash_Avengers/README.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/04_Ops_Batman_Fantastic4/README.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/05_IT_Cyborg_KangDynasty/README.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/README.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/07_People_GreenLantern_XMen/README.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/08_Legal_Aquaman_Eternals/README.md"
        ]
    },
    {
        "nom": "B2 Domain (J03 Finance)",
        "attributs": ["numero (01..08)", "name", "function", "key_metric", "framework_refs"],
        "chemins": [
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/README.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/01_Capital_Architecture/README.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/02_Cash_Flow_Architecture/README.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/03_Risk_Management/README.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/04_Tax_Optimization/README.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/05_Investment_Accumulation/README.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/06_Succession_Planning/README.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/07_Insurance_Protection/README.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/08_Family_Financial_Governance/README.md"
        ]
    },
    {
        "nom": "B2 Domain (J02 Biological Stack)",
        "attributs": ["numero (01..08)", "name", "ld_layer", "primary_source", "what_it_protects"],
        "chemins": [
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/B2_Area_Domains/README.md",
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/B2_Area_Domains/01_Sleep_Recovery/README.md"
        ]
    },
    {
        "nom": "B2 Domain (J04 Contribution)",
        "attributs": ["numero (01..08)", "name", "ld_layer", "contribution_type", "sovereign (LD08?)"],
        "chemins": [
            "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/B2_Area_Domains/README.md",
            "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/B2_Area_Domains/05_Solarpunk_Doctrine_LD08/README.md",
            "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/B2_Area_Domains/06_MUSE_Eligible_Criteria_LD08/README.md",
            "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/B2_Area_Domains/08_Contribution_Architecture_Integrated/README.md"
        ]
    },
    {
        "nom": "JTBD Canonical Packet (Area-level)",
        "attributs": ["jtbd_id", "source_rock", "domain", "b2_owner", "squad_lead", "supports", "principles_ref", "evidence_grade", "status"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/01_Growth_Superman_Guardians/JTBD-GROWTH-001_GUARDIANS_AAAS_GTM_PACKET.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/02_Sales_MartianManhunter_Illuminati/JTBD-SALES-001_ILLUMINATI_OFFER_QUALIFY_PACKET.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/03_Product_Flash_Avengers/JTBD-PRODUCT-001_AVENGERS_PRD_ACTIVATION_PACKET.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/04_Ops_Batman_Fantastic4/JTBD-OPS-001_FANTASTIC4_DEAL_SOP_PACKET.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/05_IT_Cyborg_KangDynasty/JTBD-IT-001_KANGDYNASTY_SOVEREIGN_PROVISION_PACKET.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/06_Finance_WonderWoman_Thunderbolts/JTBD-FINANCE-001_THUNDERBOLTS_MRR_MARGIN_RUNWAY_PACKET.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/07_People_GreenLantern_XMen/JTBD-PEOPLE-001_XMEN_CAPSULE_ONBOARD_ETHICS_PACKET.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/08_Legal_Aquaman_Eternals/JTBD-LEGAL-001_ETERNALS_CONTRACT_COMPLIANCE_PACKET.md"
        ]
    },
    {
        "nom": "B3 Handoff Contract (intra-squad)",
        "attributs": ["handoff_id", "from_agent", "to_agent", "reason", "context_variables"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/01_Growth_Superman_Guardians/02_PEER_UNBLOCKING_AND_HANDOFFS.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/02_Sales_MartianManhunter_Illuminati/02_PEER_UNBLOCKING_AND_HANDOFFS.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/03_Product_Flash_Avengers/02_PEER_UNBLOCKING_AND_HANDOFFS.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/04_Ops_Batman_Fantastic4/02_PEER_UNBLOCKING_AND_HANDOFFS.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/05_IT_Cyborg_KangDynasty/02_PEER_UNBLOCKING_AND_HANDOFFS.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/06_Finance_WonderWoman_Thunderbolts/02_PEER_UNBLOCKING_AND_HANDOFFS.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/07_People_GreenLantern_XMen/02_PEER_UNBLOCKING_AND_HANDOFFS.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/08_Legal_Aquaman_Eternals/02_PEER_UNBLOCKING_AND_HANDOFFS.md"
        ]
    },
    {
        "nom": "Shared Context And Proof Log",
        "attributs": ["source_b2_rock", "source_jtbd", "current_goal", "active_member", "peer_reviewed_by", "artifact_paths", "proof_paths", "lead_indicator", "lag_indicator", "status", "next_authority_needed"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/01_Growth_Superman_Guardians/03_SHARED_CONTEXT_AND_PROOF_LOG.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/02_Sales_MartianManhunter_Illuminati/03_SHARED_CONTEXT_AND_PROOF_LOG.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/03_Product_Flash_Avengers/03_SHARED_CONTEXT_AND_PROOF_LOG.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/04_Ops_Batman_Fantastic4/03_SHARED_CONTEXT_AND_PROOF_LOG.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/05_IT_Cyborg_KangDynasty/03_SHARED_CONTEXT_AND_PROOF_LOG.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/06_Finance_WonderWoman_Thunderbolts/03_SHARED_CONTEXT_AND_PROOF_LOG.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/07_People_GreenLantern_XMen/03_SHARED_CONTEXT_AND_PROOF_LOG.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/08_Legal_Aquaman_Eternals/03_SHARED_CONTEXT_AND_PROOF_LOG.md"
        ]
    },
    {
        "nom": "n8n Workflow Blueprint (DEAL Phase 4)",
        "attributs": ["workflow_name (Cash-In/Inbound/Sunday Uplink)", "trigger", "nodes_sequence", "rollback", "outputs"],
        "chemins": [
            "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/10_N8N_CashIn_Flow.md",
            "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/11_N8N_Inbound_Flow.md",
            "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/12_N8N_Sunday_Uplink.md",
            "02_Areas_Spock/Business_Pulse/docs/documentation/n8n_workflows.md"
        ]
    },
    {
        "nom": "DEAL Seed Protocol (Storefront/Engine/Pulse/Vitality/Shield)",
        "attributs": ["protocol_name", "phase", "guard", "sql_injection_pattern"],
        "chemins": [
            "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/05_Seed_Product_Offerings.md",
            "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/06_Seed_Growth_Leads.md",
            "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/07_Seed_Finance_Invoices.md",
            "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/08_Seed_People_Capacity.md",
            "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/09_Seed_Legal_Documents.md"
        ]
    },
    {
        "nom": "Webhook Event (Stripe)",
        "attributs": ["event_name", "metadata_required", "downstream_actions"],
        "chemins": [
            "02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/10_N8N_CashIn_Flow.md"
        ]
    },
    {
        "nom": "Composer Track Milestone (V0.1.x)",
        "attributs": ["version", "status", "tag_baseline", "feature_packed"],
        "chemins": [
            "02_Areas_Spock/the-bridge-__-life-os/conductor-track.md"
        ]
    },
    {
        "nom": "Warp Core Domain (B3 quarterly JD)",
        "attributs": ["domain", "principle_principles_owner", "b3_squad", "build_gates"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/Lead_Lag_Logs/README.md",
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/B3_Area_Warp_Core/Lead_Lag_Logs/README.md",
            "02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B3_Area_Warp_Core/Lead_Lag_Logs/README.md",
            "02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/B3_Area_Warp_Core/Lead_Lag_Logs/README.md"
        ]
    },
    {
        "nom": "Biological Domain KR (LD03/LD04)",
        "attributs": ["kr_id", "metric", "green", "orange", "red", "frequency"],
        "chemins": [
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/SUMMERS_VERSE_TEMPLATE.md",
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/B3_Area_Warp_Core/Lead_Lag_Logs/README.md",
            "02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/B2_Area_Domains/01_Sleep_Recovery/README.md"
        ]
    },
    {
        "nom": "Foundation Doctrine (SOB)",
        "attributs": ["doctrine_name (E-Myth/Who-Not-How/Offer-Brand-Engine/Graduation)", "owner", "status"],
        "chemins": [
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/00_SOB_INDEX.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/01_E_MYTH_FRANCHISE_PROTOTYPE.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/03_WHO_NOT_HOW_DELEGATION_MATRIX.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/04_OFFER_AND_BRAND_ENGINE.md",
            "02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/05_PROJECT_GRADUATION_GATES.md"
        ]
    }
]
print('New types count:', len(new_types_v3))

# Combine with v1+v2 types (preserving order)
all_types = list(v1['types']) + list(v2.get('types_added_in_v2', [])) + list(new_types_v3)

# Actually, v2 inherits v1 types (the JSON just lists them again with same structure).
# To avoid duplicating paths we should dedup by type name.
seen = set()
unique_types = []
for t in v1['types'] + new_types_v3:
    if t['nom'] not in seen:
        seen.add(t['nom'])
        unique_types.append(t)
# Now also add any types from v2 not in v1 (some v2 may have re-listed v1 types — skip those).
# Since v2['types'] mirrors v1['types'] exactly (same noms), we don't need to add them again.
print('Unique types:', len(unique_types))

# Save a first draft to inspect
draft = {
    'types': unique_types,
    'types_count': len(unique_types),
}
with open('_v3_types_draft.json', 'w', encoding='utf-8') as f:
    json.dump(draft, f, ensure_ascii=False, indent=2)
print('Wrote _v3_types_draft.json')
