# Watchdog L0 — S1 Rick

> `LAW.md` dit ce que Rick possede. Ce document dit **ce que Rick surveille**.
> La loi garantit qu'un seul mecanisme engendre les trois Cores.
> Le watchdog garantit que ce mecanisme **reste vivant**.

Rick ne construit pas, ne specifie pas, ne revoit pas. Il repond a une seule question,
en permanence :

> **Le jumeau numerique est-il vivant, bien portant, et anti-fragile ?**

Trois mots, trois seuils, trois preuves. Aucun n'est une opinion.

---

## 1. Vivant — le runtime existe-t-il ?

A0 orchestre Life OS ; il ne se surveille pas lui-meme. Un orchestrateur qui juge sa propre
sante est exactement le defaut que la boucle gauntlet existe pour corriger, transpose a
l'infrastructure.

| Signe | Mesure | Seuil |
|---|---|---|
| A0 tourne | `A0.log` ecrit depuis moins de 10 min | sinon **MORT** |
| L'ordonnanceur tourne | pid vivant, journal qui avance | sinon **MORT** |
| Le fournisseur repond | `PONG` sur le primaire | sinon **BASCULE** |

**Un journal vide n'est pas une preuve de mort.** Un `claude -p` n'ecrit qu'a la fin :
zero octet signifie qu'il reflechit. Le signal fiable est l'arbre de travail, pas le journal.
Confondre les deux a deja fait tuer des agents qui travaillaient.

## 2. Bien portant — l'hote tient-il la charge ?

**C'est ici que le systeme est tombe le 12 aout, et c'est la lecon fondatrice de ce
document.**

L'ordonnanceur avait un ecart minimal de 90 secondes entre deux lancements. Ce delai
protegeait contre le verrou du script npm — un fichier unique que Windows verrouille — et
seulement contre lui.

**Un delai borne la frequence. Il ne borne pas la population.**

Sept cadences, chacune lancant un `claude -p` sans jamais compter les processus vivants,
ont porte le poste a **103 `node.exe`**, puis a `0xc000012d` — `STATUS_COMMITMENT_LIMIT`,
plus de memoire a engager. Multica est tombe, le gateway MCP s'est deconnecte, la machine a
redemarre. Le travail en vol a ete perdu.

Les deux plafonds, desormais dans `ordonnanceur.sh` :

```
MAX_CADENCES_VIVES=2      # cadences simultanees
MAX_NODE=45               # node.exe sur le poste, toutes origines
```

| Signe | Mesure | Seuil |
|---|---|---|
| Processus | `tasklist | grep -c node` | **< 45** |
| Cadences vives | pid fichiers valides | **≤ 2** |
| Espace disque | racine du profil | **> 5 Go** |

**Un rendez-vous manque et annonce vaut infiniment mieux qu'un hote qui tombe.** Une cadence
refusee se lit dans le journal ; un `0xc000012d` ne previent personne.

## 3. Anti-fragile — le systeme apprend-il de ses chutes ?

Robuste = survit au choc. **Anti-fragile = en sort meilleur.** La difference se mesure a une
seule chose : le meme incident peut-il se reproduire a l'identique ?

Un incident est clos quand, et seulement quand :

1. **la cause est nommee** — pas le symptome. « Le PC a plante » est un symptome ;
   « aucun plafond de population sur les processus » est une cause ;
2. **un garde-fou existe en code**, pas dans une intention ;
3. **le garde-fou a ete vu se declencher** — un plafond jamais atteint en test est un
   plafond suppose ;
4. **la lecon est ecrite la ou le prochain la lira** — ici, ou dans le `CLAUDE.md` concerne.

Sans les quatre, l'incident n'est pas clos : il est en attente de recidive.

---

## Ce que Rick refuse

- **De construire.** Un watchdog qui code devient partie prenante de ce qu'il juge.
- **De croire un rapport.** Un agent a deja declare une section reparee alors que la capture
  montrait les titres coupes. La capture a raison contre le rapport, toujours.
- **De croire un instrument sans l'avoir eprouve.** Trois verdicts faux ont ete produits ici
  par des outils justes appliques de travers : un selecteur qui attrapait le mauvais bouton,
  un test qui cherchait un `footer button` la ou le dock est un `div`, un harnais qui
  capturait le telephone en 390 x 242 — une fente, pas un ecran. **Un outil se teste sur un
  defaut connu avant de servir de juge.**
- **De laisser croitre ce que l'hote ne porte pas.** Voir §2. La cadence sautee s'annonce.

## Ce que Rick fait quand ca tombe

1. **Constater sans interpreter** — la mesure d'abord, le recit ensuite.
2. **Distinguer la panne du defaut** — un outil qui echoue sur une page injoignable rend un
   faux rouge, pas un verdict. Cette confusion a produit trois fausses alertes en une nuit.
3. **Nommer la cause**, appliquer le garde-fou, **le voir se declencher**.
4. **L'ecrire ici.** Un incident non ecrit se reproduit.

---

## Journal des incidents

### 2026-08-12 · 05:15 — Saturation memoire de l'hote

**Symptome.** `0xc000012d` dans Multica, gateway MCP deconnecte, redemarrage du poste.

**Cause.** `ordonnanceur.sh` bornait la frequence des lancements (90 s) sans borner leur
population. Sept cadences × `claude -p` → 103 `node.exe` → `STATUS_COMMITMENT_LIMIT`.

**Garde-fou.** `MAX_CADENCES_VIVES=2` et `MAX_NODE=45`, avec refus annonce dans le journal.

**Vu se declencher.** Test a sec, cadences 1/2/3 au pas de la seconde : la premiere part,
les suivantes sont refusees et journalisees.

**Lecon.** *Un delai borne la frequence, pas la population. Les deux plafonds sont
necessaires, et le second manquait.*

**Clos** — les quatre conditions §3 sont remplies.

### 2026-08-13 · 05:30 — Le gateway mort en silence, et le garde-fou qui regardait ailleurs

**Symptome.** Aucun outil MCP de toute la session. Decouvert par accident, en
cherchant a joindre Supabase — pas par une alerte.

**Constat brut.** `agentgateway.exe` absent des processus, **zero ecoute sur 3300**.
`~/.mcp.json` ne declare qu'une entree, `gateway`. Gateway mort = **0 outil sur 23
serveurs declares**. Ce n'est pas une degradation, c'est une falaise.

**Cause 1 — la topologie.** Un point d'entree unique, sans palier. Aggrave par un
`initialize` tout-ou-rien : un seul serveur qui ne demarre pas abat les 23.

**Cause 2 — le garde-fou mesure un proxy.** `build_config.py:69` :

```python
if not (shutil.which(cmd) or os.path.isfile(cmd)):
```

Il teste que **le binaire existe sur le disque**. Un serveur dont le jeton est
revoque passe au vert et meurt au premier appel.

**Garde-fou pose.** `20_Harness/agentgateway/sonde_identifiants.py` — un appel reel
a l'API de chaque fournisseur (« qui suis-je »), jamais une valeur de jeton affichee.
Il ne corrige rien et ne relance rien : il mesure et il dit. Un outil qui reecrit
`mcp_sources.json` seul serait un outil qui cache ses propres degats.

**Vu se declencher — et corrige deux fois avant d'etre juste.**

Premier passage, 23 serveurs : 4 identifiants annonces refuses — `airtable` (401),
`clickup` (401), `vercel` (403), `vercel-omk` (403).

**Deux de ces quatre etaient des faux morts, et la faute etait dans la sonde.**
`airtable` et `clickup` portent leurs jetons en `${env:VAR}`. La sonde testait la
CHAINE `${env:AIRTABLE_API_KEY}` comme si c'etait un jeton. C'est le piege 2 de
`CLAUDE.md` §3bis, rencontre depuis l'autre bout : le gateway resout ces
placeholders, donc **tout outil qui lit `mcp_sources.json` a cru observe un autre
systeme que celui qui tourne**. Corrige par `resoudre()`, calque sur
`build_config.py:resolve_env()`. Les deux repondent 200.

Verdict final : **2 identifiants refuses** — `vercel` et `vercel-omk`, tous deux
`HTTP 403 {"invalidToken": true}`. Vercel le dit lui-meme. Temoin qui valide la
sonde : `vercel-abc`, meme forme de jeton, meme requete, **200**.

Precision de l'utilisateur, qui elimine une cause : ses jetons sont crees **sans
expiration**. Un `invalidToken` n'est donc pas une peremption — c'est une
revocation ou une suppression cote Vercel. Le mot « rotation » etait le mauvais.

**Deuxieme lecon, et elle double la premiere.** La sonde v1 jetait le corps de la
reponse et ne gardait que le code HTTP. Elle savait dire *refuse*, jamais
*pourquoi*. Les deux faux morts n'ont ete demasques qu'en lisant le corps.

> **Un garde-fou qui rend un code sans motif fabrique des diagnostics plausibles.**
> Toute sonde de ce depot conserve le corps de l'erreur : c'est lui qui distingue
> « jeton refuse » de « je n'ai jamais lu de jeton ».

**La lecon la plus chere de la journee, et elle m'appartient.**

Ma premiere sonde, improvisee, n'envoyait pas d'en-tete `User-Agent`.
`api.supabase.com` rend **403** dans ce cas. J'ai declare les trois jetons Supabase
morts et annonce a l'utilisateur que sa « Condition E » de rotation etait en cause.
**C'etait faux : les trois repondent 200.** La sonde definitive, avec `User-Agent`,
l'a montre deux heures plus tard.

C'etait la **deuxieme fois dans la meme session** : le matin, `urllib.urlretrieve`
sans `User-Agent` avait rendu 403 sur 23 registres Canvas UI, ce qui se lisait comme
« ces composants n'existent pas ».

> **Un 403 sans `User-Agent` n'est pas un refus d'identifiant. C'est un refus de
> client.** Toute sonde HTTP de ce depot envoie un `User-Agent` — sans quoi elle
> mesure sa propre politesse, pas la sante de la cible.

**Clos partiellement.** Les quatre conditions §3 sont remplies pour la dimension
*identifiants*. Elles ne le sont pas pour deux autres, qui restent ouvertes :

- **La falaise.** Rien ne degrade encore. Les 2-3 serveurs critiques devraient etre
  declares aussi en direct dans `~/.mcp.json`, hors gateway.
- **Le silence.** Rien n'annonce la mort du gateway. Il faut une sonde externe
  periodique — et le gateway ne peut pas etre son propre watchdog (§1).
- **Le blocage structurel.** Le gateway vit en SessionId 1 ; la session qui detecte
  la panne ne peut pas la reparer. Tant que c'est vrai, chaque chute coute
  l'attention de l'humain.
