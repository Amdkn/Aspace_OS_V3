---
titre: Spec GTD Cerritos - initialisation inbox GTD fonctionnel
spec: amy_spec_l1
date: 2026-09-02
work: L1
parent_a2: A2_HoloDeck_Cerritos_GTD
---

# Ruban - GTD Cerritos : initialiser un inbox GTD fonctionnel

## Verifie reellement (etat du repo au 2026-09-01)

Mesure directe de `C:/Users/amado/ASpace_OS_V3/20_Life_OS/25_GTD_Cerritos/` :
les 5 dossiers de stage existent (`01_Inbox_Mariner` a `05_Engage_Freeman`),
chacun porte des specs (`A3_*_Spec.md`, `AGENT.md`, `README.md`, `SOUL.md`),
mais **aucun `inbox.md` fonctionnel n'existe** : `01_Inbox_Mariner/` ne contient
que des specs de capture (Mariner, frontmatter `stage: Capture`,
`A3_L1_GTD_MARINER_CAPTURE`). Le README du framework (`25_GTD_Cerritos/README.md`)
decrit le workflow capture/clarify/organize/review/engage et la matrice canon
5 stages x 5 A3 twins (canon actif : Mariner=Capture, Boimler=Clarify,
Rutherford=Organize, Tendi=Review, Freeman=Engage) mais ne fournit pas
d'artefact de capture executable. Le ruban n'est donc pas redondant.

## Objectif

Creer dans `25_GTD_Cerritos/01_Inbox_Mariner/` un inbox GTD fonctionnel :

1. `inbox.md` - la liste de capture Mariner, peuplee de 5 items reels
   (items ci-dessous, tous issus de modules existants du repo, sources citees).
2. `README_workflow.md` - le workflow capture/clarify/organize applique a cet
   inbox, conforme a la matrice canon de `25_GTD_Cerritos/README.md`.

## Les 5 items reels a peupler (sources verifiees)

| # | Item brut | Source (chemin reel) | Prochain clarifier |
|---|---|---|---|
| 1 | Creer ADR-GTD-001 (canon 5 stages Cerritos, gap #10 du plan fancy-hugging-bengio) | `20_Life_OS/25_GTD_Cerritos/README.md` section Alignement Plan | Boimler |
| 2 | Implementer le state.json bus (schema state-bus.v1, writer `state_writer.py`, plan §9.1) | `20_Life_OS/25_GTD_Cerritos/README.md` section Alignement Plan | Boimler |
| 3 | Verifier le scope API Plane avant toute mutation distante (statut actuel : NEEDS_CONTEXT7) | `20_Life_OS/25_GTD_Cerritos/README.md` Handoff Rules | Boimler |
| 4 | Migrer META_ONTOLOGIE.md de `30_MEMORY_CORE/` vers OpenWiki (dossier candidat archivage) | `00_Amadeus/AGENTS.md` Local rule 1 | Boimler |
| 5 | Peupler `Beth_Alignment_Log/` (dossier vide, seul README present) | `20_Life_OS/00_Gatekeepers_Beth_Morty/Beth_Alignment_Log/` | Beth |

## Livrables et format

### inbox.md

```markdown
# Inbox - Mariner (Capture)

> Source des items : modules A_Space OS V3 reels (sources citees par item).
> Regle : Mariner capture, ne clarifie pas. Prochain owner : Boimler (ou Beth).

## Items (open)

- [ ] [2026-09-02] <item 1> | src: <chemin> | next: A3:Boimler
- [ ] [2026-09-02] <item 2> | src: <chemin> | next: A3:Boimler
- [ ] [2026-09-02] <item 3> | src: <chemin> | next: A3:Boimler
- [ ] [2026-09-02] <item 4> | src: <chemin> | next: A3:Boimler
- [ ] [2026-09-02] <item 5> | src: <chemin> | next: A1:Beth

## Regles de capture (Mariner)

- 1 ligne = 1 raw input, source citee sinon `hypothesis`.
- Pas de secret copie dans ce fichier.
- Clarify = Boimler (bucket PARA + tag @next/@waiting/@someday/@archive).
- Item > 1 session ou > 1 semaine : escalade Enterprise (PARA) ou SNW (12WY).
```

Le worker complete les `<item N>` et `<chemin>` avec le contenu exact du
tableau ci-dessus (verbatim, sans invention).

### README_workflow.md

Doit decrire, en s'appuyant sur `25_GTD_Cerritos/README.md` (matrice canon
5 stages x 5 A3 twins) et `A3_Mariner_Capture_Spec.md` :

1. Capture (Mariner) : ajouter une ligne `- [ ] [date] <raw> | src: <chemin> | next: A3:Boimler`.
2. Clarify (Boimler) : assigner bucket PARA + tag, cocher et deplacer l'item.
3. Organize (Rutherford) : l'item clarifie part dans 24_PARA_Enterprise
   (bucket) ou 23_12WY_SNW (rock), jamais en vrac dans l'inbox.
4. Review (Tendi) : vidange hebdomadaire, inbox vide = vert.
5. Engage (Freeman) : next action dispatchee vers A1 Morty.
6. Escalades : Beth (overload/veto A1), Enterprise (projet), SNW (rock).

## Perimetre

- Ecrire : `20_Life_OS/25_GTD_Cerritos/01_Inbox_Mariner/inbox.md`
- Ecrire : `20_Life_OS/25_GTD_Cerritos/01_Inbox_Mariner/README_workflow.md`
- Ne pas modifier : les specs existantes (`A3_Mariner_Capture_Spec.md`,
  `AGENT.md`, `SOUL.md`, `README.md` du framework), les autres stages, le
  schema `kernel/schema.sql`.
- Ne pas creer de tache Plane distante (NEEDS_CONTEXT7).
- Respecter l'interdit du `25_GTD_Cerritos/AGENTS.md` : aucun fichier a la
  racine du framework, tout fichier cree va dans `01_Inbox_Mariner/`.

## Critere d'acceptation

- N1 : `inbox.md` existe et contient exactement 5 items ouverts, chacun avec une ligne `| src: ` citant un chemin reel existant. Verification : `python -c "import re,os;s=open(r'C:/Users/amado/ASpace_OS_V3/20_Life_OS/25_GTD_Cerritos/01_Inbox_Mariner/inbox.md',encoding='utf-8').read();print(s.count('- [ ]'))"` -> 5
- N2 : chaque chemin cite dans `inbox.md` existe sur disque. Verification (exit 0) : `python -c "import re,os;s=open(r'C:/Users/amado/ASpace_OS_V3/20_Life_OS/25_GTD_Cerritos/01_Inbox_Mariner/inbox.md',encoding='utf-8').read();paths=[p.strip() for p in re.findall(r'src: (\S+)',s)];assert len(paths)==5;print([os.path.exists(os.path.join(r'C:/Users/amado/ASpace_OS_V3',p)) for p in paths])"` -> les 5 chemins impriment True
- N3 : `README_workflow.md` existe et documente les 5 stages canon avec les bons twins (Mariner/Boimler/Rutherford/Tendi/Freeman). Verification : `python -c "s=open(r'C:/Users/amado/ASpace_OS_V3/20_Life_OS/25_GTD_Cerritos/01_Inbox_Mariner/README_workflow.md',encoding='utf-8').read();print(all(n in s for n in ['Mariner','Boimler','Rutherford','Tendi','Freeman']))"` -> True

## Interdits

- Prononcer `done` : seul le 11e Docteur detache, depuis `review`.
- Modifier une spec existante de Cerritos.
- Ecrire hors de `01_Inbox_Mariner/` (sauf lecture).
- Inventer un item sans chemin source reel (tout item non sourcant = `hypothesis`, refuse).
- Cumuler Build et Review.
