WARGAME ORDER. Tu n'exécutes pas cette mission, tu la wargames. Exécuteur : **MiniMax M3** (c'est SON infra — rails blind). Ton job = la route.

Recon read-only : `ADR-LLM-COST-COMPARE-001` (plan fixe 5.1Md tokens/50$ D1-verified), `ADR-NEXUS-NICHE-001` §IT (cache sémantique SQLite/OPFS) + §Finance (anti-Jevons), la machine réelle : OS/RAM/GPU/disque libre (commandes système au recon — PAS de tutoriel générique), `.hermes/disposition.md`.

Combats sur papier → `wargames/10-localai-minimax.md`. SUCCESS-ASPACE 9-12. Secrets : env User scope only.

=== MISSION BRIEF ===

Le **stack local-first MiniMax** qui écrase le coût variable : (1) **cache sémantique local** — si un agent redemande une analyse déjà traitée (profil prospect, processus client), servir depuis SQLite local à latence ~0, zéro token cloud ; (2) **watchdog** — nettoyage de fond anti bash-hang / saturation KV-cache ; (3) **segmentation Product** — modèle local léger pour 1er jet/formatage, M3 1M-contexte réservé à l'injection matière-noire en validation finale.

Livrables : (a) le schéma du cache : clé (hash sémantique ? exact-match d'abord — le plus simple qui marche), invalidation (TTL par type de donnée), stockage (SQLite fichier local, chemin) ; (b) la politique de routage local vs cloud : quelle tâche va où, avec les seuils chiffrés (tokens estimés, sensibilité PII → jamais cloud sans DLP mission 05) ; (c) le watchdog : quoi surveiller (procs bash orphelins, taille KV, disque), cadence, action (kill+log, jamais silencieux) ; (d) le bilan économique : coût/mois projeté du PoC 10 clients sous plan fixe vs API cloud (chiffres sourcés ADR-LLM-COST-COMPARE-001, le reste RECON NEEDED).

Wargame en particulier : « le cache sert une réponse périmée à un client payant » — trigger de fraîcheur + contre-action.

Vérifie avant de rapporter. Le plus simple qui marche.
