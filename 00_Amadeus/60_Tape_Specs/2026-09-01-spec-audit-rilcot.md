---
id: "l2-spec-003"
layer: "L2"
classification: "Audit"
status: "READY"
created: "2026-09-01"
okf_version: "0.2"
description: "Audit de coherence du domaine RILCOT dans l'ontologie V3 : gates, JTBD, labels/manifests. Produit un rapport d'audit executable avec corrections proposees."
kernel_work: "work 3 (uc.db) — audit RILCOT, layer L2, sans ruban au moment de la redaction"
---

# Spec — audit RILCOT (coherence ontologie V3)

## Objectif
Verifier la coherence du domaine RILCOT (`03_RILCOT_Members_Space_OS`) dans
l'ontologie V3 : gates transverses complets (Legal / Finance / Ops / Sales /
Product / IT / People / Growth), JTBD cibles (JTBD-001..005), labels et
manifests coherents entre les fichiers TTL sources — puis produire un rapport
d'audit executable listant les incoherences mesurees et, pour chacune, une
correction proposee (chemin + patch exact).

## Fichiers d'entree (exclusifs, chemins absolus verifies)
1. `C:/Users/amado/ASpace_OS_V3/70_Onthologies/sujets/01_Projects_Picard.ttl`
   — domaine RILCOT : JTBD-001..005 Nexus, gates transverses RILCOT JTBD-002
   (l.2494-3052), `03_RILCOT_Members_Space_OS Domain Development Map`
   (l.3094), `B2 Offer Brand Revenue Engine - 03_RILCOT` (l.3124), `B2
   Business Domains — 03 RILCOT Members Space & OS` (l.3130).
2. `C:/Users/amado/ASpace_OS_V3/70_Onthologies/sujets/30_Business_OS.ttl` —
   `Manifest — RILCOT Members Space & OS` (l.63).
3. `C:/Users/amado/ASpace_OS_V3/70_Onthologies/sujets/05_From_V2_Domains.ttl`
   — `Manifest — RILCOT Members Space & OS` (l.63).
4. `C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/aspace-os.ttl` —
   lignes ~670-770 : `LD01 Book Alignment mappe 6 livres vers 8 B2 domains`
   (l.743), `RILCOT refine le LD01 Book Alignment avec 9 livres (ajout Expert
   Secrets + Group Genius)` (l.746), `Le Picard Project Pattern a été appliqué
   à l'audit RILCOT Master Interface (2026-05-20)` (l.763-764).

## Reference croisee (lecture seule, sans statut de source d'audit)
- `C:/Users/amado/ASpace_OS_V3/30_Business_OS/AGENTS.md` — regle des 8 domains
  B2 / 8 squads B3 (Growth / Sales / Product / Ops / IT / Finance / People /
  Legal) servant de reference des gates attendus.

## Verifications a executer (l'audit les fait toutes, zero question)
1. **Gates complets** : dans `01_Projects_Picard.ttl`, compter les labels
   `JTBD-002 RILCOT Transverse * Gate`. Attendu : exactement 8, couvrant
   Legal, People, Finance, IT, Ops, Product, Sales, Growth. Listing de chaque
   gate trouve avec sa ligne.
2. **JTBD cibles** : pour chaque gate, verifier la presence d'un JTBD-001
   RILCOT de projet correspondant (Claims Data IP Boundary / Owner and Agent
   Handoff Map / Price Margin Model / Runtime And Data Boundary / DELIVERY SOP
   / MVP Demo Boundary / Diagnostic To Proposal) — JTBD-001..005 cibles
   (Nexus VOC Packet, Member-ICP Filter, Painkiller Message Variants,
   Non-Paid Experiment + RICE, Growth Signal Gate).
3. **Labels/manifests coherents** : `30_Business_OS.ttl` et
   `05_From_V2_Domains.ttl` portent tous deux `Manifest — RILCOT Members
   Space & OS` a la ligne 63 — comparer les attributs complets des deux
   noeuds (labels, buckets, dates `dct:modified`) et signaler toute
   divergence ligne par ligne.
4. **Triplets LD01** : verifier la chaine
   `ld01-book-alignment` → (refines par) `rilcot` et la coherence 6 vs 9
   livres (`aspace-os.ttl` l.743-746) — le rapport doit confirmer ou
   contredire les chiffres 6 et 9 par lecture des lignes citees.
5. **Picard audit** : confirmer le triplet `picard-audit appliesTo rilcot`
   (l.763-764) et sa ligne de source.

## Fichier de sortie (unique)
`C:/Users/amado/ASpace_OS_V3/50_Distillation/audit-rilcot-2026-09-01.md`
Structure obligatoire du rapport :
- section `## Methodologie` (outils et commandes reellement executes, rc) ;
- section `## Verifications` — une sous-section `### ` par verification 1-5
  ci-dessus, avec preuve (ligne, valeur comptee, commande) ;
- section `## Incoherences` — liste numerique ; si aucune : le mot exact
  `AUCUNE INCOHERENCE MESUREE` ;
- section `## Corrections proposees` — pour chaque incoherence : chemin du
  fichier, ancien extrait, nouvel extrait propose (patch textuel exact), sans
  appliquer le patch ;
- section `## Verdict` — `COHERENT` ou `INCOHERENT` + nombre d'incoherences.

## Critere d'acceptation
1. Le fichier `C:/Users/amado/ASpace_OS_V3/50_Distillation/audit-rilcot-2026-09-01.md` existe et fait plus de 1500 octets : `python -c "import os;assert os.path.getsize(r'C:/Users/amado/ASpace_OS_V3/50_Distillation/audit-rilcot-2026-09-01.md')>1500,'trop court'"`
2. Le rapport contient les cinq sections obligatoires : `python -c "t=open(r'C:/Users/amado/ASpace_OS_V3/50_Distillation/audit-rilcot-2026-09-01.md',encoding='utf-8').read();[assert_() for assert_ in [lambda:None]];import sys;miss=[s for s in ['## Methodologie','## Verifications','## Incoherences','## Corrections proposees','## Verdict'] if s not in t];sys.exit('manques: %s'%miss if miss else 0)"`
3. Le rapport contient une sous-section par verification (5 sous-titres `### ` sous `## Verifications`) : `python -c "t=open(r'C:/Users/amado/ASpace_OS_V3/50_Distillation/audit-rilcot-2026-09-01.md',encoding='utf-8').read().split('## Verifications')[1].split('## Incoherences')[0];import sys;n=t.count(chr(10)+'### ');sys.exit(0 if n>=5 else 'sous-sections: %d'%n)"`
4. Le rapport cite les trois chemins d'entree TTL exacts et le triplet LD01 (9 livres) : `python -c "t=open(r'C:/Users/amado/ASpace_OS_V3/50_Distillation/audit-rilcot-2026-09-01.md',encoding='utf-8').read();import sys;need=['01_Projects_Picard.ttl','30_Business_OS.ttl','05_From_V2_Domains.ttl','aspace-os.ttl','9 livres'];m=[s for s in need if s not in t];sys.exit('citations manquantes: %s'%m if m else 0)"`
5. Chaque incoherence listee sous `## Incoherences` possede une entree correspondante sous `## Corrections proposees` (meme nombre de corrections que d'incoherences, ou verdict `COHERENT` avec zero correction) : verifiable par lecture du rapport — le nombre d'entrees numerique des deux sections est egal et le `## Verdict` annonce ce meme nombre.

## Périmètre
Dedans : lecture des 4 fichiers d'entree listes + `30_Business_OS/AGENTS.md`,
ecriture du fichier de sortie unique, compte et comparaison de lignes TTL.
Dehors : toute modification de `70_Onthologies/` (les corrections proposees
restent des patches textuels dans le rapport, jamais appliques), ecriture
dans `30_Business_OS/`, modification de uc.db ou du schema kernel, lecture de
`00_Amadeus/30_MEMORY_CORE/sessions_md/` (matiere brute).

## Interdits
Appliquer une correction sans travail distinct separe (audit = lecture seule
sur les sources). Inventer une valeur non mesuree — toute affirmation porte
le numero de ligne ou `A SOURCER`. Toucher au schema du kernel.
