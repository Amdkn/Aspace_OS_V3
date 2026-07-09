# WARGAME 05 — DLP Legal Supabase (fork A de NEXUS-NICHE-001)

> Wargamé par Fable 5, 2026-07-06. Exécuteur : **Hermes** (+ ingénieur Abdaty). Exécutable blind.
> Le DLP est LA porte qui rend le reste sûr-à-ouvrir (niche = Data First/Conformité).

## RECON (fait — D1)
- Prototype regex EXISTANT : `citadel/cron/telegram_warmode_push.py` → `exfil_scan()` (sk-ant, gh[pousr]_, xox[baprs]-, AKIA, sbp_, token Telegram, JWT → [REDACTED]). NE PAS réécrire — extraire en module partagé.
- `ADR-OMK-005_tenant-isolation-guard.md` (RLS par tenant) ; quarantaine convention posée : `loops/artifacts/tickets/_quarantine/` + signal `dlp-hit`.
- Contrainte canon : DÉTERMINISTE (même input → même redaction ; AUCUN LLM dans la boucle DLP).

## MOVES
**M1 — Extraire le module partagé `citadel/dlp/redact.py`**
- Action : déplacer les patterns d'exfil_scan + ajouter PII : email, téléphone (formats US/FR), IBAN, SSN/NIR, adresse (numéro+rue heuristique conservatrice). Chaque pattern : nom, regex, remplacement `[REDACTED:<type>]`, test positif + négatif.
- Observation : `redact(text) -> (clean, hits[])` ; telegram_warmode_push importe le module (1 source de vérité).
- Échec probable : faux positifs massifs (les IDs projet ressemblent à des tokens) → **cause** : regex trop larges. **Contre-action** : allowlist explicite (prj_, mvs_, wf_, job ids connus) testée AVANT le pattern secret.
- Fork : SI un pattern exige du contexte (nom de personne) → NE PAS le faire en regex ; marquer `RECON NEEDED: NER local (spaCy?) — phase 2`, ne pas bloquer la phase 1.

**M2 — Le point d'insertion (où le proxy vit)**
- Action : DEUX insertions, pas une : (a) **pré-réseau local** — toute fonction qui POST vers un LLM cloud passe par `redact()` d'abord (wrapper unique) ; (b) **pré-écriture tickets** — `loops/artifacts/tickets/` n'accepte que du texte redacté.
- Observation : grep du codebase : aucun `requests.post` vers api.minimax/anthropic sans passer par le wrapper.
- Échec probable : un chemin contourne le wrapper (script legacy) → **cause** : adoption non forcée. **Contre-action** : hook PostToolUse existant + revue Spock échantillonnée ; à terme un lint grep en CI locale.

**M3 — Niveau 2 : le secret DU client de ton client**
- Action : scénario canon (transcription Gong contient une clé AWS du client final) : `redact()` attrape AKIA → hit niveau 2 → ticket ENTIER en `_quarantine/` (pas juste masqué) + signal `dlp-hit` status open → airlock B3 passe RED (compteur cycles verts → 0).
- Observation : le hit niveau 2 est distinguable (type=cloud-credential) et déclenche quarantaine, pas simple masquage.

**M4 — Audit trail SOC2/EU-AI-Act**
- Action : chaque run append `citadel/dlp/audit.jsonl` : `{ts, tenant, hits_count, types[]}` — JAMAIS le contenu. Compteur par tenant pour la preuve de conformité.
- Observation : audit.jsonl grandit, zéro PII dedans (vérifiable par redact(audit) == audit).

**M5 — Test harness**
- Action : `citadel/dlp/test_redact.py` : corpus piégé (≥20 phrases : secrets réels-format, PII, faux-amis allowlist) → exigence : 100% des patterns connus attrapés, 0 faux négatif ; faux positifs < 5%.
- Observation : pytest exit 0 ; le corpus VIT avec le module (chaque incident réel ajoute une phrase).

## ABORT CONDITIONS
1. Un pattern demande une lib réseau/cloud pour détecter → STOP (le DLP doit tourner offline).
2. redact() modifie la sémantique métier du texte (chiffres business masqués par erreur) → STOP, resserrer, re-tester.

## VERIFICATION RUNS
1. `python -m pytest citadel/dlp/test_redact.py` → exit 0.
2. `python -c "from redact import redact; print(redact('clé sk-ant-abc123 tel 06 12 34 56 78'))"` → 2 hits, texte propre.
3. telegram_warmode_push fonctionne toujours (import du module, push OK: sent).

## RED-TEAM PASS
- **Échouée** : « le DLP ralentit tout » — non : regex compilées une fois, µs par message.
- **Réussie → patch** : « le secret coupé en deux par un saut de ligne échappe au regex » — patch : normaliser (join des lignes courtes contiguës) AVANT scan ; ajouter le cas au corpus.

## SELF-GRADE : 12/12
