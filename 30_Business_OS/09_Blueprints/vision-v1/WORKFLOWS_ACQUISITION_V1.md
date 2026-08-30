---
id: WORKFLOWS_ACQUISITION_V1
blueprint: vision-v1
suppose: ARCHITECTURE_V1.md (analyse) · VISION.md (ordre des rangs)
statut: CONCEPTION — aucun code, aucune installation. Rien ici ne se construit avant le rang 0.
date: 2026-08-13
---

# Les workflows d'acquisition — conception

## Le point qui redessine la chaîne

Shubham écrit **le script de chaque prospect à la main**. L'analyse le note comme un
coût — *« ~5 min par prospect, 80 h pour mille »* — et propose qu'un agent le rédige.

C'est vrai, mais ce n'est pas tout ce que fait ce geste.

**En écrivant chaque script à la main, Shubham regarde chaque cible.** Il ne peut pas
envoyer à quelqu'un qu'il n'a pas lu. Sa chaîne n'a pas de garde-fou parce qu'elle n'en
a pas besoin : le goulot humain *est* le garde-fou. Il est involontaire, mais il tient.

Automatiser la rédaction retire ce goulot. Si on se contente de remplacer « l'humain
écrit » par « l'agent écrit », on ne gagne pas 80 heures : **on supprime la seule
vérification qui existait**, et on branche une machine sur de vraies personnes.

D'où le principe qui gouverne tout ce document :

> **Un point d'arrêt humain se place là où l'étape suivante est irréversible.**
> Deux choses sont irréversibles dans cette chaîne : **dépenser** et **contacter**.
> Donc deux arrêts, pas un.

L'analyse n'en prévoyait qu'un (à l'envoi). Le second — avant la génération vidéo —
n'est pas de la prudence en plus : c'est le goulot de Shubham, remis à sa place.

---

## La chaîne, recoupée

Shubham a cinq cercles dans l'ordre : liste → vidéo → capture → montage → envoi.
Cet ordre est celui d'un exécutant. Le nôtre est celui d'un décideur, et il diffère sur
un point : **on observe avant de rédiger, et on rédige avant de dépenser.**

| # | Nœud | Nature | Coût | Irréversible ? |
|---|---|---|---|---|
| 1 | `cible.qualifier` | **agent** | jetons | non |
| 2 | `cible.observer` | workflow (MCP Playwright) | temps machine | non |
| 3 | `message.rediger` | **agent** | jetons | non |
| — | **ARRÊT 1 — le script** | **humain** | — | *porte de la dépense* |
| 4 | `video.generer` | workflow (HeyGen) | **€** | oui — dépense |
| 5 | `video.monter` | workflow (Creatomate) | **€** | oui — dépense |
| — | **ARRÊT 2 — l'envoi** | **humain + code à 6 chiffres** | — | *porte du contact* |
| 6 | `message.envoyer` | workflow (Unipile) | € | **oui — touche une personne** |

Deux agents. Quatre workflows. Deux arrêts.

### Ce que chaque nœud fait, et pourquoi il est de sa nature

**1 · `cible.qualifier` — agent.** Lit la fiche prospect dans le CMS, rend un score et
**une raison écrite**. Sous le seuil, la chaîne s'arrête ici : zéro euro dépensé, une
ligne au journal. C'est le nœud que Make ne sait pas faire et que l'analyse identifie
comme notre vrai gain — *« l'agent peut décider d'arrêter après l'étape 2 »*. On le
déplace en tête : arrêter après avoir payé n'est pas arrêter.

**2 · `cible.observer` — workflow.** Capture le profil LinkedIn et le site. Chez
Shubham, une API maison **qui tourne sur son ordinateur** — l'analyse la nomme SPOF, à
juste titre : *« si l'ordi dort, la chaîne s'arrête »*. Chez nous, un MCP Playwright
côté serveur. Rien à décider ici : c'est déterministe, donc c'est un workflow.

**3 · `message.rediger` — agent.** Rédige à partir de la fiche **et de l'observation**.
C'est l'inversion par rapport à Shubham, qui génère la vidéo avant de capturer le
profil. Un script écrit sans avoir regardé la cible est un publipostage avec un prénom
dedans.

**4 et 5 · `video.generer`, `video.monter` — workflows.** HeyGen puis Creatomate.
Template et variables : du déterministe pur. L'analyse le dit — *« la partie composition
est du déterministe pur, pas un job d'agent »*.

**6 · `message.envoyer` — workflow.** Unipile. Déclenché **uniquement** par la levée de
l'arrêt 2.

---

## Les deux arrêts

### Arrêt 1 — la porte de la dépense

**Ce que l'humain voit** : la fiche, le score et la raison du nœud 1, la capture du nœud
2, le script du nœud 3. Sur un écran.

**Ce qu'il peut faire** : approuver · corriger le script · rejeter la cible.

**Pourquoi ici** : c'est le dernier instant où arrêter ne coûte rien. Après, HeyGen
facture. Et c'est le goulot de Shubham remis à sa place — sauf qu'il relit au lieu
d'écrire, ce qui prend trente secondes au lieu de cinq minutes. **Le gain de 80 heures
survit ; la vérification aussi.**

**Il se relâche** : quand un opérateur a validé N scripts d'affilée sans correction, le
lot suivant peut passer en approbation groupée. Le relâchement se mérite sur des
mesures, il ne se décrète pas au départ.

### Arrêt 2 — la porte du contact

**Ce que l'humain voit** : la vidéo montée, le destinataire, le compte émetteur.

**Ce qu'il fait** : saisit un **code de confirmation à 6 chiffres** — le mécanisme que
l'architecture reprend de Lumail pour les outils à effet de bord externe.

**Pourquoi un code et pas un bouton** : un bouton s'actionne par réflexe. Le rang 1 de
l'architecture le pose comme exigence, pas comme option.

**Pourquoi ici malgré l'arrêt 1** : entre les deux, deux services tiers ont écrit. Le
risque 1 de l'architecture est explicite — *« un outil renvoie une URL forgée, l'agent la
passe à Creatomate, qui la passe à Unipile, qui l'envoie »*. **L'arrêt 1 valide une
intention. L'arrêt 2 valide un artefact.** Ce ne sont pas les mêmes objets, donc ce
n'est pas le même contrôle.

---

## Ce que porte le graphe

Le graphe d'état (rang 2) tient un état par cible, qui survit aux deux arrêts. Sans
persistance, une approbation le lendemain matin rejouerait toute la chaîne — et
repaierait HeyGen.

```
{ cible_id, statut, score, raison,
  captures[], script, script_approuve_par, script_approuve_le,
  video_brute_url, video_montee_url,
  envoi_approuve_par, code_confirme_le, envoi_id, cout_cumule }
```

`cout_cumule` n'est pas décoratif : c'est ce qui rend le risque 3 de l'architecture
(coût marginal par prospect) mesurable au lieu d'être une inquiétude.

Deux `interrupt()`, aux deux arrêts. La reprise repart du nœud suivant, **jamais du
début**.

---

## La surface MCP

n8n retenu — souveraineté, MCP officiel mature, workflows scriptables en JSON
(ARCHITECTURE_V1 §5). Il expose **quatre** workflows, pas un de plus :

| outil MCP | entrée | sortie | € |
|---|---|---|---|
| `observer_cible` | url_linkedin, url_site | captures[] | non |
| `generer_video` | script, avatar_id | video_brute_url | **oui** |
| `monter_video` | video_brute_url, captures[], variables | video_montee_url | **oui** |
| `envoyer_message` | destinataire, video_url, jeton_confirmation | envoi_id | **oui** |

**`envoyer_message` exige un `jeton_confirmation`** émis par la levée de l'arrêt 2. Sans
jeton valide, le workflow refuse. La garde n'est pas dans le prompt de l'agent — elle est
dans le workflow. Un agent qu'on persuade ne peut pas fabriquer le jeton.

C'est la seule ligne de ce document qui compte vraiment sur le plan sécurité : **le
contrôle vit du côté qui ne se laisse pas convaincre.**

---

## Ce qui n'est pas décidé

- **Quel avatar, quelle voix.** HeyGen suppose un enregistrement initial. C'est une
  décision de marque, comme l'objet 3D d'hier.
- **Le seuil de qualification.** Il se règle sur des cibles réelles, pas à la table.
- **Le canal.** Unipile couvre LinkedIn, Instagram, WhatsApp. Un seul pour commencer.
- **Qui approuve.** Toi seul au départ ; à terme un rôle.

## Ce qui ne se construit pas encore

Rien ici. L'ordre de l'architecture est strict et je le confirme : **rang 0 — la surface
d'écriture — d'abord**. Le CMS n'a ni `createItem` ni `deleteItem` ; une chaîne
d'acquisition qui ne sait pas écrire une ligne dans le CRM produit des vidéos que
personne ne retrouve.

Ce document sert à ça : quand le rang 0 et le rang 1 seront posés, la chaîne est déjà
dessinée, et sa construction se délègue par brief au lieu de se réinventer.

**Le prochain livrable exécutable est un brief M3 sur le rang 0**, pas une installation
n8n.
