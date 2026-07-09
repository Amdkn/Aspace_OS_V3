# Aggregate 6 swarm JSON into 2 ADR canon-batch canon (D6 #80 anti-loop : string FIXE)
import json, os

JSON_DIR = r"C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\canon_batch_v4_2026-06-25"
os.makedirs(JSON_DIR, exist_ok=True)

# IT-EXT swarm 3 sub-agents (6 guides IT)
it_ext_json = {
    "guides": [
        {
            "slug": "google-ai-coding-masterclass-summary-zbmuiaPuiNM",
            "pilier_titre_canon": "AI Coding : Outils Sans Devenir Dev",
            "insight_verbatim": "L'IA va remplacer les programmeurs. Mais elle ne va pas remplacer celui qui sait quoi programmer. Ce qui compte c'est de savoir structurer un probleme, pas d'ecrire la syntaxe.",
            "concept_cles": ["Vibe coding", "Spec-first prompting", "Agent loop autonomy", "Context window economy"],
            "sisters": ["ADR-AAAS-IT-CANON-001", "ADR-META-001", "ADR-SOBER-002"]
        },
        {
            "slug": "reading-ais-mind-probes-passengers-vs-drivers-N-yVh0bKsIk",
            "pilier_titre_canon": "Probes Passagers vs Drivers : Lire l'IA",
            "insight_verbatim": "La vraie question n'est pas ce que le modele sait, mais ce que le modele ignore qu'il ignore. Les probes bien construites revelent les angles morts, les drivers les exploitent.",
            "concept_cles": ["Interpretability probes", "Latent space mapping", "Activation steering", "Driver vs passenger split"],
            "sisters": ["ADR-AAAS-IT-CANON-001", "ADR-SOBER-002", "ADR-META-001"]
        },
        {
            "slug": "system-design-101-apis-databases-caching-cdns-load-balancing-production-infra-oYxTTirKY8M",
            "pilier_titre_canon": "Architecture Production Infra Resiliente",
            "insight_verbatim": "Caching is a complex topic, but the fundamental thing to know is that there are two main strategies: cache aside and write through. Both have tradeoffs in terms of complexity, performance, and consistency that you need to understand deeply before picking one.",
            "concept_cles": ["cache-aside", "write-through", "load-balancing", "CDN", "production-resilience"],
            "sisters": ["ADR-AAAS-IT-CANON-001", "ADR-META-001"]
        },
        {
            "slug": "ant-simulator-collision-resolution-MD4hH1ObrYg",
            "pilier_titre_canon": "Algorithmie Espaces Discrets Bornes",
            "insight_verbatim": "Grid based collision detection works by dividing the world into cells, only checking collisions between entities in the same or adjacent cells, dramatically reducing the number of pairwise checks from O(n2) to roughly O(n) for uniformly distributed entities.",
            "concept_cles": ["spatial-hashing", "grid-partitioning", "O(n)-lookup", "bounded-arena", "discretization"],
            "sisters": ["ADR-AAAS-IT-CANON-001", "ADR-META-001", "ADR-SOBER-002"]
        },
        {
            "slug": "every-folder-on-my-computer-full-reveal-tiago-forte-A0pdL3MS_7E",
            "pilier_titre_canon": "Code comme Competence Cognitive Second Cerveau",
            "insight_verbatim": "c'est pas juste pour les creatifs ou les hackers les codeurs deviennent une competence cognitive fondamentale pour pouvoir vraiment changer le monde vous allez avoir besoin de coder",
            "concept_cles": ["code", "competence cognitive", "second cerveau", "PARA", "productivite"],
            "sisters": ["ADR-AAAS-IT-CANON-001", "ADR-META-001", "ADR-MEM-002"]
        },
        {
            "slug": "retry-urban-vpn-WgmseucKcCA",
            "pilier_titre_canon": "Anti-Pause HitL Strategie Maintenance VPN",
            "insight_verbatim": "note it's basically what we're doing but we've uh we we've made it a lot more elegant we have a system in place where um every couple of weeks I get a notification from Claude",
            "concept_cles": ["anti-pause", "HITL", "UrbanVPN", "notification", "rotation"],
            "sisters": ["ADR-AAAS-IT-CANON-001", "ADR-META-001", "ADR-META-006"]
        }
    ]
}

# CONTENT swarm 3 sub-agents (5 guides mixed)
content_json = {
    "guides": [
        {
            "slug": "design-skills-that-actually-work-Ot582-E61ac",
            "domaine": "01_Product",
            "pilier_titre_canon": "Skill Design That Actually Works",
            "insight_verbatim": "Skills should be designed for agent discoverability and predictability, not human readability. The skill's description is the trigger surface - if the model can't pattern-match it to a user request, the skill effectively doesn't exist.",
            "concept_cles": ["discoverability", "trigger surface", "description-as-API", "progressive disclosure"],
            "sisters": ["ADR-AAAS-OPERATIONS-CANON-001", "ADR-AAAS-PRICING-001", "ADR-META-001"]
        },
        {
            "slug": "ops-framework-yP4p3reZUcU",
            "domaine": "02_Ops",
            "pilier_titre_canon": "Operational Framework Discipline",
            "insight_verbatim": "Operational frameworks succeed when they encode irreversibility gates at the right cadence: daily actions reversible, weekly commitments reviewable, quarterly pivots expensive. The framework's value is making cost-of-change explicit at each layer.",
            "concept_cles": ["irreversibility gates", "cadence layering", "cost-of-change", "review loops"],
            "sisters": ["ADR-AAAS-OPERATIONS-CANON-001", "ADR-META-001", "ADR-SOBER-002"]
        },
        {
            "slug": "13-business-finance-lessons-after-losing-money-FvtskCSwbxc",
            "domaine": "04_Finance",
            "pilier_titre_canon": "Le capital survit aux erreurs",
            "insight_verbatim": "La chose la plus importante dans les affaires c'est pas d'etre intelligent c'est d'avoir du cash. Tu peux etre tres mauvais dans tes decisions mais tant que t'as du cash tu survis.",
            "concept_cles": ["runway-cash", "survie-primer", "anti-burnout", "decision-reversible"],
            "sisters": ["ADR-AAAS-FINANCE-CANON-001", "ADR-AAAS-PRICING-001", "ADR-SOBER-002"]
        },
        {
            "slug": "21-business-lessons-i-wish-i-learned-10-years-earlier-bPmhfM1HRWI",
            "domaine": "04_Finance",
            "pilier_titre_canon": "Loueurs ou proprietaires mindset",
            "insight_verbatim": "Dans la vie t'as deux choix soit tu es locataire soit tu es proprietaire. Si tu es locataire de ta sante de tes finances de tes relations tu paies toujours quelqu'un d'autre paie a ta place.",
            "concept_cles": ["mindset-proprietaire", "ownership-actif", "anti-dependance", "valeur-locative"],
            "sisters": ["ADR-AAAS-FINANCE-CANON-001", "ADR-AAAS-PRICING-001", "ADR-AAAS-OPERATIONS-CANON-001"]
        },
        {
            "slug": "boring-businesses-highest-survival-rates-5fS-lD1nFxM",
            "domaine": "07_Growth",
            "pilier_titre_canon": "Boring Businesses Highest Survival Rates",
            "insight_verbatim": "Boring businesses survive because they solve essential, recurring needs. Predictable demand, low competition from disruptors, and steady cash flow make them resilient through economic cycles.",
            "concept_cles": ["recurring demand", "low disruption", "steady cashflow", "economic resilience", "essential services"],
            "sisters": ["ADR-AAAS-ACQUISITION-DOCTRINE-001", "ADR-AAAS-PRICING-001", "ADR-SOBER-002"]
        }
    ]
}

# Save JSON canon
with open(os.path.join(JSON_DIR, "it_ext_swarm.json"), "w", encoding="utf-8") as f:
    json.dump(it_ext_json, f, indent=2, ensure_ascii=False)
with open(os.path.join(JSON_DIR, "content_swarm.json"), "w", encoding="utf-8") as f:
    json.dump(content_json, f, indent=2, ensure_ascii=False)

print("[OK] JSON canon saved:")
print("     it_ext_swarm.json: " + str(len(it_ext_json["guides"])) + " guides")
print("     content_swarm.json: " + str(len(content_json["guides"])) + " guides")
print("     Total: " + str(len(it_ext_json["guides"]) + len(content_json["guides"])) + " guides for 2 ADR canon-batch")