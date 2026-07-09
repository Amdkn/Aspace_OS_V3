---
name: diagnose-proxy-boolean
description: Hunt and cure proxy-boolean health flags — any health/status boolean computed from a proxy (grep of a trace, file presence, count-ever) instead of the source of truth. This is STRUCTURAL evaluation gaming - the system reports green while its own governor screams red. Use when auditing a loop/collector/dashboard, when a Picard variant (C1..I1) kicks off a domain, when a metric "looks always green", or when A+ says "angle-mort", "proxy", "faux vert", "diagnose les booléens". Battle-tested twice in prod 2026-07-06 (mirofish_attached + cadence_alive).
---

# /diagnose-proxy-boolean — le détecteur d'evaluation gaming structurel

> Pattern (wargame 08, vécu) : **(gouverneur qui parle) + (consommateur sourd) + (boundary qui dit
> « accélère » vers le mur annoncé)**. L'angle-mort n'est jamais LE booléen — c'est la CLASSE :
> tout flag de santé calculé par proxy au lieu de la source de vérité.

## Les 4 phases (aucune sautée)

**1. IDENTIFIER** — lister les booléens de santé du système audité : `grep -n "alive\|attached\|healthy\|ok\|= True\|_fresh\|_ready" <loop/collector>.py` + les badges verts des dashboards. Chaque flag → une ligne d'inventaire.

**2. TRACER LA SOURCE** — pour chaque flag, remonter à sa fonction. Verdicts :
- lit la **source de vérité** (le signal, la donnée fraîche, le résultat de commande) → sain ;
- **grep d'une trace / présence de fichier / count-depuis-toujours** → PROXY (faux-vert garanti dans le temps) ;
- la fonction **n'existe pas** (le flag est décoratif, ou le consumer entier est absent) → pire que proxy.
Signatures connues (chassées en prod) : `grep 'X' dans un log/calendar` (mirofish_attached) · `count >= 1` sans fraîcheur (cadence_alive) · consumer absent (L2 Gstack).

**3. VÉRIFIER LE CONSOMMATEUR RÉEL** — la question tueuse : *« quand le gouverneur dit RISQUE, qui l'entend ? »* `grep -c "<dossier signals/source>" <consumer>.py` = 0 → sourd. Vérifier aussi la boundary rule : si elle peut dire « accélère » pendant un RED non-lu → l'angle-mort est armé.

**4. CURER — ADDITIF avec exit_condition chiffrée** (jamais suppressif) :
- ajouter la fonction d'écoute (lecture seule de la source de vérité) + un champ NOUVEAU (garder l'ancien pour compat/ownership) + un risk_flag + la boundary conditionnelle ;
- **absorber par la queue** (LOOP-002) : le RED devient une task avec `exit_condition` CHIFFRÉE (ex : `capacité ≥96/WK ×2WK → re-simuler`). Une absorption sans exit_condition chiffrée = éteindre l'alarme sans agir → INVALIDE ;
- vérifier la boucle complète : dry-run AVANT (flag True, rule cappée) → absorption → run réel APRÈS (flag False, décision en queue).

## Preuves canon (répliquer ce niveau de preuve)
`mirofish_attached` : dry-run `risque_unabsorbed: True` + rule « CAP ×4 » → task cap-compression-x4 → run réel `False`, 7/7 invariants. `cadence_alive` : champ `cadence_fresh` <48h ajouté, dry-run `true`. Rails complets : `fable-last-week-aspace/wargames/08-picard-mirofish.md`.

## Anti-patterns
❌ Supprimer/renommer l'ancien flag (casse l'ownership et les consommateurs existants) · ❌ curer par un 2e proxy (un grep qui greppe mieux reste un grep) · ❌ absorber sans condition de sortie · ❌ patcher le producteur d'autrui autrement qu'en additif strict.
