WARGAME ORDER. Tu n'exécutes pas cette mission, tu la wargames. Exécuteur : **Hermes** (avec l'ingénieur Abdaty). Ton job = la route.

Recon read-only : `ADR-NEXUS-NICHE-001` §Legal (proxy DLP déterministe), `citadel/cron/telegram_warmode_push.py` (exfil_scan existant = le prototype regex), MCP `supabase-omk` (tables existantes — list only), `ADR-OMK-005_tenant-isolation-guard.md`.

Combats sur papier → `wargames/05-legal-dlp.md`. SUCCESS-ASPACE 9-12. Secrets : jamais en .md/.json/git (Test Key Pragma : env User scope only).

=== MISSION BRIEF ===

**Fork A de NEXUS-NICHE-001** : les scripts de redaction **DLP** pour le Duo Legal — expurger de manière déterministe PII et secrets industriels AVANT toute interaction réseau/cloud, sur l'infra Supabase OMK.

Livrables : (a) l'architecture du proxy : où il s'insère (edge function ? middleware local avant l'appel M3 cloud ? les deux ?) ; (b) le catalogue de patterns : PII (noms, emails, téléphones, adresses), secrets (clés API — réutiliser/étendre l'exfil_scan du telegram push), secrets industriels client (comment les détecter : NER local ? dictionnaire par tenant ?) ; (c) le mode déterministe : même input → même redaction (pas de LLM dans la boucle DLP elle-même) ; (d) l'audit trail : chaque redaction loggée (compteur par tenant, jamais le contenu) pour la preuve SOC2/EU-AI-Act ; (e) le test harness : corpus de phrases piégées → 100% caught, 0 faux négatif toléré sur les patterns connus.

Wargame en particulier : le scénario « transcription Gong d'un client contient la clé AWS de SON client » (PII de niveau 2) — route de détection + quarantaine.

Vérifie avant de rapporter. Le plus simple qui marche — le DLP est la porte qui rend le reste sûr-à-ouvrir.
