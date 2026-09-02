---
title: ADR-GTD-001 - canon 5 stages Cerritos
layer: L1
date: 2026-09-02
source: 20_Life_OS/25_GTD_Cerritos/01_Inbox_Mariner/inbox.md item 1
---

# Note - ADR-GTD-001 (canon 5 stages Cerritos, gap #10 du plan fancy-hugging-bengio)

L'inbox Mariner (`20_Life_OS/25_GTD_Cerritos/01_Inbox_Mariner/inbox.md`, item 1)
porte la capture : creer ADR-GTD-001 pour figer le canon 5 stages Cerritos
(capture/clarify/organize/review/engage avec les twins Mariner/Boimler/Rutherford/
Tendi/Freeman), gap #10 du plan fancy-hugging-bengio. Le README du framework
(`20_Life_OS/25_GTD_Cerritos/README.md`) decrit la matrice canon mais aucun
Architecture Decision Record ne l'a formellement acte.

## Objectif

Ecrire un ADR unique qui acte la decision de canon 5 stages Cerritos :

1. `ADR-GTD-001.md` dans `20_Life_OS/25_GTD_Cerritos/02_Clarify_Boimler/`
   (decision sortie du stage Clarify de Boimler), structure ADR standard :
   frontmatter (`status: accepted`, `date: 2026-09-02`, `deciders`), sections
   `## Context`, `## Decision`, `## Consequences`.
2. La `## Decision` acte la matrice canon 5 stages x 5 A3 twins telle que
   decrite dans `20_Life_OS/25_GTD_Cerritos/README.md` (Mariner=Capture,
   Boimler=Clarify, Rutherford=Organize, Tendi=Review, Freeman=Engage) et les
   5 etapes canon (capture, clarify, organize, review, engage).
3. La `## Context` cite les sources reelles : `20_Life_OS/25_GTD_Cerritos/README.md`,
   `20_Life_OS/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md`, et l'inbox item 1.
4. La `## Consequences` liste au moins 3 consequences executables (qui ecrit
   ou, qui clarifie, escalades Beth/Enterprise/SNW).

## Périmètre

- Ecrire : `20_Life_OS/25_GTD_Cerritos/02_Clarify_Boimler/ADR-GTD-001.md`
- Lire (sources) : `20_Life_OS/25_GTD_Cerritos/README.md`,
  `20_Life_OS/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md`,
  `20_Life_OS/25_GTD_Cerritos/01_Inbox_Mariner/inbox.md`
- Ne pas modifier : les specs existantes de Cerritos, l'inbox Mariner (le
  cochage de l'item 1 appartient a Boimler en Clarify, hors de ce ruban), les
  autres frameworks 20_Life_OS, le schema `10_Tech_OS/kernel/schema.sql`.
- Ne pas creer de tache Plane distante (statut NEEDS_CONTEXT7).
- Respecter l'interdit de `25_GTD_Cerritos/AGENTS.md` : aucun fichier a la
  racine du framework ; tout fichier cree va dans `02_Clarify_Boimler/`.

## Critère d'acceptation

- N1 : le fichier `20_Life_OS/25_GTD_Cerritos/02_Clarify_Boimler/ADR-GTD-001.md`
  existe et contient `status: accepted` en frontmatter. Verification (exit 0) :
  `python -c "s=open(r'C:/Users/amado/ASpace_OS_V3/20_Life_OS/25_GTD_Cerritos/02_Clarify_Boimler/ADR-GTD-001.md',encoding='utf-8').read();assert 'status: accepted' in s;print('N1 OK')"`
- N2 : l'ADR documente les 5 stages et les 5 twins canon. Verification (imprime
  True) : `python -c "s=open(r'C:/Users/amado/ASpace_OS_V3/20_Life_OS/25_GTD_Cerritos/02_Clarify_Boimler/ADR-GTD-001.md',encoding='utf-8').read();print(all(w in s for w in ['Mariner','Boimler','Rutherford','Tendi','Freeman','capture','clarify','organize','review','engage']))"`
- N3 : l'ADR contient les sections `## Context`, `## Decision`,
  `## Consequences`. Verification (imprime True) :
  `python -c "s=open(r'C:/Users/amado/ASpace_OS_V3/20_Life_OS/25_GTD_Cerritos/02_Clarify_Boimler/ADR-GTD-001.md',encoding='utf-8').read();print(all(m in s for m in ['## Context','## Decision','## Consequences']))"`

## Interdits

- Prononcer `done` : seul le 11e Docteur detache, depuis `review`.
- Modifier une spec existante de Cerritos ou l'inbox Mariner.
- Ecrire hors de `02_Clarify_Boimler/` (sauf lecture).
- Cumuler Build et Review.
- Creer une tache distante Plane (NEEDS_CONTEXT7).
