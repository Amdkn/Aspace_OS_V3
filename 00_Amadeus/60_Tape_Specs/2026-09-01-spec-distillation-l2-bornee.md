---
id: "l2-spec-002"
layer: "L2"
classification: "Distillation"
status: "READY"
created: "2026-09-01"
okf_version: "0.2"
description: "Distillation L2 bornee : extraire les apprentissages des sessions Business OS vers un brief + un extract JSON"
spec_parent: "C:/Users/amado/ASpace_OS_V3/_INBOX/B1_Jerry_Summers/spec_l2_distill.md"
---

# Spec — distillation L2 bornée (work compagnons)

## Objectif
Produire une première distillation bornée du corpus Business OS : un brief
markdown lisible + un extract JSON structuré, à partir d'une lecture ciblée
des sources rédigées (PAS des 4 647 vidages de sessions).

## Sources (exclusives, dans cet ordre)
1. `C:/Users/amado/ASpace_OS_V3/30_Business_OS/` — lire AGENTS.md local puis
   au plus 10 fichiers `.md` de blueprints/notes rédigées.
2. `C:/Users/amado/ASpace_OS_V3/50_Distillation/RAPPORT_INTENTIONS_V3.md` —
   sections Business/PARA uniquement.

## Artefacts à produire
1. `C:/Users/amado/ASpace_OS_V3/50_Distillation/distill_l2_sessions-20260901.md`
   — au moins 4 sections `## ` (une par thème extrait), chaque section cite
   au moins un chemin de source mesuré.
2. `C:/Users/amado/ASpace_OS_V3/50_Distillation/distill_l2_sessions-20260901.json`
   — JSON UTF-8 valide : liste d'objets `{"domaine", "apprentissage", "source"}`,
   au moins 5 entrées.

## Critère d'acceptation
- [ ] `python -c "import os;p=r'C:/Users/amado/ASpace_OS_V3/50_Distillation/distill_l2_sessions-20260901.md';assert os.path.getsize(p)>1500,'trop court'"`
- [ ] `python -c "import json;d=json.load(open(r'C:/Users/amado/ASpace_OS_V3/50_Distillation/distill_l2_sessions-20260901.json',encoding='utf-8'));assert isinstance(d,list) and len(d)>=5 and all(set(('domaine','apprentissage','source'))<=set(e) for e in d),'json incomplet'"`
- [ ] `python -c "t=open(r'C:/Users/amado/ASpace_OS_V3/50_Distillation/distill_l2_sessions-20260901.md',encoding='utf-8').read();import re;s=re.findall(r'^## ',t,re.M);assert len(s)>=4,'sections insuffisantes: %d'%len(s)"`

## Périmètre
Dedans : les deux artefacts ci-dessus + lecture des sources listées.
Dehors : toute écriture dans `30_Business_OS/`, `70_Onthologies/`, uc.db
(sauf le cycle kernel qui le porte), toute modification de source.

## Interdits
Ne pas modifier les sources. Ne pas lire `sessions_md/` (matière brute, 71 %
du corpus). Ne pas toucher au schéma du kernel.
