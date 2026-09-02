---
session: b6b8d6cb-aa4e-4bed-a2b2-39daffdcaaea
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado-agent-os-citadel\b6b8d6cb-aa4e-4bed-a2b2-39daffdcaaea.jsonl
debut: 2026-07-14T15:01:31.010Z
fin: 2026-07-14T15:39:20.410Z
messages_utilisateur: 1
reponses_assistant: 2
titre: "Tu es le WORKER WF1 (Morty : A2 Curie 12WY + A2 Holo Deck/Cerritos GTD), une ITÃ‰RATION du run loop 24/7 (ADR-…"
---

## >>> UTILISATEUR #1

Tu es le WORKER WF1 (Morty : A2 Curie 12WY + A2 Holo Deck/Cerritos GTD), une ITÃ‰RATION du run loop 24/7 (ADR-L1-WF-001). Tu n'es pas un chat : tu finis UN item avec preuve, tu logges, tu EXIT â€” le runner te relance aussitÃ´t. Le filesystem est ta seule mÃ©moire entre itÃ©rations.

CWD = C:\Users\amado\agent-os\citadel.

## Â§0 â€” START HEARTBEAT (PATCH WP-1, 2026-07-06 â€” wargame 12)

**AVANT TOUTE AUTRE ACTION**, Ã©mets cette ligne dans `loops/logs/worklog.md` :

```
- [<ISO maintenant>] [wf1-morty] START iter N â€” preuve: ctx-budget=low, mode=production
```

oÃ¹ N = numÃ©ro d'itÃ©ration (lis `wf1_runner.log` pour le connaÃ®tre, ou utilise 1 si premiÃ¨re iter).

C'est ta **preuve d'existence**. Si tu ne le fais pas, tu n'as pas travaillÃ©. Le runner vit â€” c'est toi qui doit montrer que TU vis.

## Â§1 BIS â€” CONTEXT BUDGET (PATCH WP-1)

Tu as ~10k tokens de budget. **RÃˆGLES STRICTES** :

- **NE RELIS PAS** `loops/ARCHITECTURE.md` (2431 b) ni `loops/domains/wf1-morty/README.md` (1216 b) Ã  chaque iter. Ce sont des canoniques stables, ta premiÃ¨re iter les a internalisÃ©s.
- Si tu dois vÃ©rifier un dÃ©tail, lis une **section spÃ©cifique** avec offset/limit (max 50 lignes), JAMAIS le fichier complet.
- **Max 1 fichier > 50 lignes par iter.** Si tu te retrouves Ã  en lire 2, tu as mal piochÃ© la queue â€” recommence avec un item plus simple.
- **Ne charge JAMAIS le contenu d'un dossier entier en mÃ©moire.** Pioche 1 fichier task, travaille, log, exit.

Ces rÃ¨gles prÃ©viennent le context thrashing. Un worker qui crashe = un worker qui n'a rien produit. Le `[wf1-morty] START` + le `[wf1-morty] <verbe>` final = la **seule** preuve que tu as travaillÃ©.

## Â§1 â€” SÃ©quence obligatoire (canonique)

1. LIS : les 10 derniÃ¨res lignes de `loops/logs/worklog.md` (ne rÃ©pÃ¨te JAMAIS le travail d'une itÃ©ration prÃ©cÃ©dente).
2. PIOCHE dans cet ordre :
   a. l'item `status: queued` le plus ancien de `loops/artifacts/tasks/` DONT le travail est faisable maintenant (un item-contrainte type `cap-*` dont l'exit_condition n'est pas atteignable = le laisser, ce n'est pas une tÃ¢che) ;
   b. SI queue vide â†’ UN item de backlog des contrats `loops/domains/*/README.md` (Â§Backlog), prioritÃ© : wf3-mirofish office-hours sims (wargame 09 M4 : 4 personas, format signal `office-hours-sim-N` avec verdict + â‰¥1 objection non rÃ©solue) puis wf2-book tick (wargame 03 M1) ;
   c. SI tout est vide â†’ exÃ©cute UNE mission de build depuis les rails `C:\Users\amado\fable-last-week-aspace\wargames\` (ordre : 05 DLP module redact.py â†’ 07 quiz.html â†’ 06 prompts AARRR), UN move par itÃ©ration.
3. TRAVAILLE pour de vrai : ship INTERNE seulement (jamais d'envoi externe â€” `enable_ship_outboard` absent), DLP avant tout rÃ©seau, append-only, jamais toucher un RATIFIED ni un intouchable, roster canon exact.
4. PREUVE obligatoire : colle la sortie de commande / le `Test-Path` dans l'item ou le signal produit. Sans preuve = status `unverified`, pas `done`.
5. CLÃ”TURE : update le status de l'item + append 1 ligne Ã  `loops/logs/worklog.md` : `- [ISO] [wf1-morty] <verbe+objet> â€” preuve: <path/exit>`.
6. EXIT immÃ©diatement aprÃ¨s la ligne worklog. Une itÃ©ration = un item. Pas de question Ã  l'humain (No-HITL : si bloquÃ©, Ã©cris un signal `blocked-<slug>` et prends autre chose Ã  l'itÃ©ration suivante).

## Â§6 BIS â€” EMERGENCY EXIT (PATCH WP-1)

Si Ã  tout moment tu dÃ©tectes que ton contexte dÃ©passe **80 %** de sa capacitÃ© (symptÃ´mes : compaction agressive, rÃ©ponses tronquÃ©es,tools qui timeout) :

1. **Ã‰METS** immÃ©diatement une ligne worklog : `- [ISO] [wf1-morty] ctx-pressure iter N â€” preuve: <symptÃ´me observÃ©>`
2. **EXIT** sans finir l'item en cours. L'item reste `status: queued` pour l'iter suivante (frais, sans contexte contaminÃ©).

Mieux vaut une itÃ©ration courte avec preuve qu'une itÃ©ration longue qui crashe sans rien produire. Le runner te respawnera dans 45 s avec un worker neuf.

### assistant

Itération terminée. Récap :

**START HEARTBEAT** : ✅ émis à 11:10:29

**Pioche** (séquence §1) :
- §1.2a : `cap-compression-x4.md` → SKIP (type `cap-*`, exit_condition non atteignable, owner=wf2-book)
- §1.2b : backlogs wf1-morty/wf2-book/wf3-mirofish → tous clos/bloqués (wf2-book #2 = attente 1er client signé)
- §1.2c : wargames 05/07/06 → tous déjà implémentés → fallback maintenance verify sur 05 (priorité #1 de l'ordre)

**Travail réel** : vérification wargame 05 M4 (audit trail) + M5 (test harness) :
- `python -m pytest dlp/test_redact.py` → **26 passed in 4.23s** (exit 0)
- `dlp/audit.jsonl` → **16/16 lignes clean, 0 PII** (invariant M4 `redact(audit)==audit` OK)
- Signal produit : `citadel/loops/artifacts/signals/dlp-m4m5-verify-20260714.md` (3129 b)

**Clôture** : 2 lignes worklog append (START + SHIP) avec preuves Test-Path + sortie pytest collée.

**Ctx budget** : low, aucun symptôme de compaction. EXIT.

### assistant

Background task `bdv5thb4i` (find UNKNOWNS-REGISTER) completed — déjà résolu via `ls` synchrone (fichier trouvé à `fable-last-week-aspace/wargames/UNKNOWNS-REGISTER.md`, lu partiellement). Aucune action requise.

Itération wf1-morty iter 1 reste CLOSED. EXIT maintenu.
