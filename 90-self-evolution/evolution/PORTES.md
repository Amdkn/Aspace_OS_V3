# Les portes — ce qu'une skill doit franchir pour entrer

> Reprend les contraintes de
> [`hermes-agent-self-evolution`](https://github.com/NousResearch/hermes-agent-self-evolution) :
> « Candidates pass multiple gatekeeping constraints: full test suite passage,
> size limits (skills ≤15KB), caching compatibility, semantic preservation,
> and human PR review before acceptance. »
>
> Et le verrou d'Hermes : `skills.write_approval: true` met les écritures en
> attente sous `~/.hermes/pending/skills/`. **Human review gates all changes —
> never direct commits occur.**

## Les six portes

| | Porte | Comment on la vérifie |
|---|---|---|
| **G1** | **Ancrage mesuré** | Le frontmatter porte `metadata.hermes.ancrage` avec au moins un repère `P`/`B`/`D`/`I`, une `mesure` chiffrée, et une `source` qui existe |
| **G2** | **Vérification exécutable** | `scripts/` contient un `--auto-test` qui **peut échouer**. Un test qui ne peut pas échouer ne teste rien |
| **G3** | **Taille** | `SKILL.md` ≤ 15 Ko. Au-delà, la skill est survolée au lieu d'être suivie |
| **G4** | **Structure** | Les quatre sections : *Quand l'utiliser*, *Pourquoi elle existe*, *Procédure*, *Pièges*, *Vérification* |
| **G5** | **Soustraction nommée** | La skill dit ce qu'elle **remplace**. (B4 — 700 intentions d'orchestration, aucune pour retirer quelque chose) |
| **G6** | **Revue humaine** | Aucune skill ne passe en `confiance: humain` sans le propriétaire |

**G1 à G5 sont scriptées** — `python evolution/portes.py`. **G6 ne l'est pas,
et ne le sera jamais** : c'est le seul verrou qu'aucun script ne peut poser à
la place de quelqu'un.

## La boucle, et où elle s'arrête aujourd'hui

Le dépôt Nous décrit :

```
Lire la skill ──► Générer un jeu d'éval ──► GEPA ──► Variantes
                        ──► Évaluer ──► Portes ──► Revue humaine
```

GEPA « lit les traces d'exécution pour comprendre *pourquoi* les choses
échouent » plutôt que de constater l'échec.

**État réel ici :** `datasets/` est **vide**. Sans jeu d'évaluation, il n'y a
rien à optimiser — **les six skills de ce dossier sont écrites à la main**,
aucune n'est issue d'un cycle GEPA. Annoncer le contraire serait exactement la
confusion mesuré/supposé que **D2** interdit.

Ce qui existe : les portes G1–G5, exécutables, qui valent pour une skill
écrite à la main comme pour une variante générée.

## Ce que Prime Agent ajoute

La récursion `rlm` — un sous-agent est créé, rend une poignée stable, et le
parent continue pendant qu'il tourne. Deux choses en sont reprises :

1. **Le *Continual Harness*** : ce qui doit survivre à l'invocation vit dans un
   fichier relu au démarrage, pas dans le contexte. C'est
   [`p2-mandat-persistant`](../skills/p2-mandat-persistant/SKILL.md).
2. **La borne d'exécution** : « turn, token, and wall-clock limits stop
   execution ». Sur ce poste : `MAX_CADENCES_VIVES=2`, une seule boucle à la
   fois, `pgrep -fc` avant de relancer.

**Ce qui n'est pas repris :** les 95,5 % sur ARC-AGI-3. Ce chiffre mesure le
harnais Prime Agent, pas ce dossier. Le citer comme une promesse serait
malhonnête.

## Ce que ce dossier remplace

Rien n'est ajouté sans soustraction (B4) :

- Les briefs `GARDE-FOU` (96×), `LES SEPT CADENCES` (69×) et `MODE FABLE`
  (60×) **ne doivent plus être réémis** : leur contenu d'autorisation va dans
  le mandat persistant, leur contenu de cadence dans une skill.
- La vérification par jugement d'agent est remplacée par
  `scripts/*.py --auto-test`. Un avis n'est pas une mesure.
