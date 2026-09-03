---
type: OKF-0.2
id: "spec-rescope-cascade-verify-ruban-atomique"
layer: "L0"
created: "2026-09-02"
statut: PROPOSE
source: "_INBOX/_admis/S1_Rick/intent-rescope-cascade-20260902.md (FROZEN)"
remplace: "10_Tech_OS/12_Life_Core_11th/tapes/02_Rory_Health/Cascade_Verify_Spec.md (work 19, chaine de preuve cassee — works 30/31/32)"
---

# SPEC — Re-scopage work 19 : verification cascade A1/A2/A3, ruban atomique

## 1. Objectif

Re-scoper le work 19 (uc.db) dont la chaine de preuve est cassee : remplacer
le snapshot du 2026-09-01 par une **mesure du jour** de l'etat cascade
A1/A2/A3, en lecture seule, sans toucher a `apply_life_os_cascade.sh`.

## 2. Contrainte du bloc criteres (cause racine des works 30/31/32)

`review.py` traite CHAQUE ligne non-vide du bloc `## Critere d'acceptation`
comme un critere independant et exige une preuve (`evidence --criterion <N>`,
0-based) ou une commande executable entre accents graves PAR LIGNE. Regle
absolue : chaque critere = UNE SEULE ligne physique, commencant par `- []`,
contenant EXACTEMENT UNE commande executable entre accents graves, jamais de
continuation de ligne.

## 3. Perimetre

- Lecture seule : `multica agent/squad/project list`, `git status --porcelain`, requete SQL uc.db.
- Interdits : mutation multica, modification de `apply_life_os_cascade.sh`, ecriture directe uc.db hors `uc.py`.
- A la soumission du work, le worker remplace `<N>` dans la doc (pas dans le bloc criteres ci-dessous, qui garde la valeur litterale `0` comme placeholder) par l'id reel du work au moment de l'execution de la commande de verification de prediction.

## Critere d'acceptation

- [] `multica agent list` mesure du jour retourne les 16 agents cibles (A1-Beth, A1-Morty, A2-Orville, A2-Discovery, A2-SNW, A2-Enterprise, A2-Cerritos, A2-Protostar, A3-Pike, A3-Dal, A3-Mercer, A3-Mariner, A3-Picard, A3-Spock, A3-Geordi, A3-Data)
- [] `multica squad list` mesure du jour retourne 3 squads (Squad-A1-Beth-Morty, Squad-A2-Frameworks, Squad-A3-Officiers)
- [] `multica project list` mesure du jour retourne 3 projets actifs (A1-Vision, A2-Frameworks, A3-Officiers)
- [] `git -C C:/Users/amado/ASpace_OS_V3 status --porcelain -- 10_Tech_OS/12_Life_Core_11th/tapes/02_Rory_Health/apply_life_os_cascade.sh` retourne vide, rc 0
- [] prediction anterieure a la premiere evidence du work : `python -c "import sqlite3;c=sqlite3.connect('10_Tech_OS/kernel/uc.db');p=c.execute('SELECT predicted_at FROM prediction WHERE work_id=? ORDER BY predicted_at LIMIT 1',(0,)).fetchone();e=c.execute("SELECT MIN(at) FROM event WHERE work_id=? AND kind='evidence'",(0,)).fetchone();print(1 if p and e and p[0]<e[0] else 0)"` retourne 1 (placeholder 0 = id du work, a remplacer par l'id reel au moment de l'execution)

