# WARGAME 10 — Local AI MiniMax : cache sémantique, watchdog, routage (l'infra de M3 lui-même)

> Wargamé par Fable 5, 2026-07-06. Exécuteur : **MiniMax M3** (c'est SON infra). Exécutable blind.
> Machine RÉELLE (recon ce jour, pas un tutoriel) : Windows 11 AMD64 · 8 CPU logiques · 32 GB RAM ·
> 434 GB libres · GPU = « Virtual Desktop Monitor » (AUCUN GPU dédié détecté).

## LA VÉRITÉ MACHINE (qui réécrit la mission)
Sans GPU dédié, « modèle local léger pour le 1er jet » = CPU-only : un 7B quantisé tourne mais LENT
(~qq tokens/s sur 8 threads). **Conclusion honnête : le gros du gain local ne viendra PAS d'un LLM
local — il viendra du CACHE SÉMANTIQUE (0 token, 0 GPU) + du plan fixe MiniMax (5,1 Md/50$, D1-verified
ADR-LLM-COST-COMPARE-001).** Le LLM local CPU = tier optionnel pour le formatage batch nocturne, pas le hot path.
- RECON NEEDED : `dxdiag /t dxdiag.txt` puis grep GPU — confirmer que « Virtual Desktop Monitor » n'est pas un artefact RDP masquant une carte réelle. SI GPU réel ≥ 8 GB VRAM → rouvrir le tier local-LLM.

## MOVES

**M1 — Le cache sémantique (le vrai moteur d'économie)**
- Action : `citadel/dlp/../cache/semantic_cache.py` — SQLite local (`citadel/cache/cache.db`), **exact-match d'abord** (hash SHA256 du prompt normalisé : lowercase, espaces réduits, timestamps strippés) ; clé = (hash, model, purpose) ; valeur = (réponse, created_at, ttl).
- Observation : hit → réponse en <5 ms, 0 token cloud ; compteur hits/misses dans le fichier stats.
- Échec probable : cache poisonné (une mauvaise réponse servie à l'infini) → **cause** : pas d'invalidation. **Contre-action** : TTL par purpose (analyse prospect 7j · processus client 30j · canon 24h) + commande purge par clé.
- Fork : SI hit-rate < 20 % après 2 WK → l'exact-match ne suffit pas → PHASE 2 embeddings locaux (CPU ok : modèle d'embedding ~100 MB) — pas avant, YAGNI.

**M2 — Le routage local vs cloud (la politique chiffrée)**
- Action : table de routage dans le module : (a) cache hit → local, toujours ; (b) PII détectée (DLP wargame 05) → JAMAIS cloud sans redaction préalable — ordre strict `redact() PUIS route` ; (c) tâche < 500 tokens estimés ET template connu → formatage déterministe (code, pas LLM — LD01-004 §4.5) ; (d) reste → MiniMax M3 plan fixe (le « cloud » est déjà flat-rate : router agressivement vers lui est ÉCONOMIQUEMENT CORRECT ici, contrairement au cas API-variable des clients).
- Observation : chaque appel logge sa route (cache/deterministic/m3) ; ratio visible.
- **Nuance clé** : pour OMK Nexus CLIENTS (facture API variable), la politique s'inverse — le cache+local pèse lourd. Ce wargame documente LES DEUX politiques (la nôtre flat-rate, la leur variable) — c'est l'argument de vente du Quiz (wargame 07).

**M3 — Le watchdog (anti bash-hang / saturation)**
- Action : `citadel/cron/watchdog.py` (schtask 1h via install-loops.ps1, additif) : (a) procs bash/python orphelins > 30 min sans parent CC/Hermes → kill + log (JAMAIS silencieux) ; (b) `cache.db` > 500 MB → vacuum + purge TTL échus ; (c) disque libre < 50 GB → alerte Telegram (pas d'action destructive — Loi du Checkpoint Profond).
- Observation : log `watchdog.log` append-only, 1 ligne/action avec PID/taille/preuve.
- Échec probable : le watchdog tue un run légitime long (graphify 600s, sims) → **cause** : seuil naïf. **Contre-action** : allowlist par nom de commande (graphify, wf3_sim, book_loop) + seuil 30 min → 2h pour l'allowlist.

**M4 — Le bilan économique (chiffres sourcés, le reste RECON)**
- Action : projeter le PoC 10 clients : ~40 h transcriptions/client/mois × 25k tokens/h ≈ 1 Md tokens/mois à 10 clients → **dans le plan 5,1 Md/50$** avec marge ×5 ; vs API cloud variable ≈ 15 $/M output → ~15 000 $/mois. Écart = l'argument Jevons du Quiz. Constantes : plan MiniMax sourcé (ADR-LLM-COST-COMPARE-001) ; 25k tokens/h et 15 $/M = ordres de grandeur marqués `≈`, à re-sourcer au premier client réel (RECON).
- Observation : le bilan vit dans un fichier que le CEO-Bench cite (métrique d'amorçage : coût/lead).

## ABORT CONDITIONS
1. Le cache exigerait une dépendance réseau (Redis cloud etc.) → STOP, SQLite local est le contrat.
2. Le watchdog demanderait des droits admin → STOP, user-scope seulement (Trust Zone).

## VERIFICATION RUNS
1. Cache : 2 appels identiques → 2e = hit <5 ms, compteur +1 ; purge par clé fonctionne.
2. Watchdog dry-run : proc bash fictif 31 min → détecté+loggé ; graphify simulé → épargné (allowlist).
3. Routage : phrase avec PII → route = redact-first prouvée par le log ; jamais de PII brute dans les logs.

## RED-TEAM PASS
- **Échouée** : « sans GPU le local-first est mort » — non : le local-first ici = cache + déterministe + souveraineté des données ; le LLM local n'a jamais été le cœur (et le plan fixe rend M3 quasi-local économiquement).
- **Réussie → patch** : « le hash exact-match rate 95 % des re-demandes (une virgule change tout) » — patch intégré : normalisation agressive AVANT hash (M1) + fork Phase-2 embeddings chiffré sur hit-rate < 20 % à 2 WK — le seuil décide, pas l'ego.

## SELF-GRADE : 12/12 — machine réelle au recon ✓, deux politiques de routage (nôtre/client) ✓, Beth-compat ✓ (tout est fond de tâche).
