# BRIEF C2-PRODUCT_OFFE_1 — Produit, offres et flux de travail (1/2)

Tu es un technicien d'analyse. Tu lis des transcrits de conferences et tu en
extrais de quoi refondre l'architecture d'information d'un produit.

## Le produit

**Coach OS** est un shell type OS de bureau dans le navigateur : fenetres
deplacables, dock, et **19 apps metier** montees dans ces fenetres. React 19,
TypeScript, Tailwind v4, Zustand. Chaque app a une barre laterale de sections ;
chaque section ouvre une page de detail.

Les 19 apps : `dashboard` · `product` · `growth` · `sales` · `operations` ·
`finance` · `legal` · `people` · `it-rd` · `clients` · `tasks` · `marketplace` ·
`settings` · `onboarding` · `welcome` · `audit` · `cognition` · `design` ·
`_ui` (composants partages).

Aujourd'hui la plupart sont des **coquilles generiques** : trois ou quatre
sections au nom vague, sans modele derriere. C'est ce qu'on refond.

Le produit s'appelle **OMK Nexus**. Il vise aujourd'hui la niche des **coachs**,
et doit pouvoir servir d'autres niches demain. Une primitive qui ne marche que
pour des coachs est donc moins interessante qu'une primitive qui marche pour
n'importe quel metier de service — dis-le quand c'est le cas.

## Ce qu'un travail parallele a deja etabli

Six agents ont analyse un premier corpus de 18 conferences. Leurs conclusions,
que tu peux confirmer ou contredire mais que tu ne dois pas re-decouvrir :

- **Il manque une couche transversale** au produit : un *graphe de contexte*, un
  depot versionne des entites, relations et regles du domaine du client, lu par
  tous les agents et cure par des humains. Coach OS manipule Person, Squad,
  Agent, Runbook, Incident dans 19 apps sans les avoir jamais nommes.
- **Le metier de Forward Deployed Engineer se decompose en gestes.** Cinq sont
  automatisables (construire l'ontologie, verrouiller le plan, specialiser les
  agents, evaluer, cabler les systemes). Quatre resistent : le mandat
  hierarchique, le consentement a reveler l'exception non ecrite, la
  responsabilite juridique, et la promotion d'un constat en primitive de
  plateforme.
- **Un bon test de primitive** : une vraie primitive rend les sections existantes
  *plus pauvres en isolation*. Si l'ajouter ne devalorise rien de ce qui existe,
  c'est une rubrique decorative.

## Ta grappe n'est pas une frontiere

Le nom de ta grappe dit **d'ou viennent** ces videos, pas **ou vont** leurs
enseignements. Une conference rangee sous « vente » peut porter la meilleure idee
sur la structure des offres, ou sur l'ontologie. Ne t'auto-censure pas : si une
primitive sert `finance` ou `legal`, dis-le, meme si ta grappe s'appelle
autrement.

Inversement, une primitive peut n'appartenir a **aucune app** — elle peut relever
de la couche transversale (le graphe de contexte), ou du modele economique. Ce
sont des reponses valides et souvent les plus utiles.

## Ce qu'on cherche — deux choses, pas une

**1. Des primitives produit.** Un concept nomme, defini en une phrase, qu'on peut
transformer en section de barre laterale, en bloc de page de detail, ou en objet
du modele de donnees.

**2. Du materiau de domaine.** C'est ce qui manquait au premier corpus. Comment
un travail excellent est-il *structure* dans ce metier ? Que contient reellement
un pipeline de vente bien tenu, une offre bien construite, un tableau de bord de
dirigeant utile ? Ce n'est pas de la theorie d'agent, c'est de la structure
d'objet metier — et c'est ce dont on a besoin pour dessiner des pages de detail
qui ne soient pas creuses.

Si une video ne porte que du premier type, dis-le. Si elle ne porte que du
second, c'est tres bien aussi.

## Tes transcrits (8)

- `transcripts2/product-offers-workflows/de8Dp2EWo0g.md` — J'ai analysé 85 Agences IA, voici ce qui marche en 2026
- `transcripts2/product-offers-workflows/Y3PcRp5RFzk.md` — I Built 500 AI Workflows, These 5 Actually Sell in 2026
- `transcripts2/product-offers-workflows/OQdE5uTtScE.md` — The NEW Rules of Selling AI (2026)
- `transcripts2/product-offers-workflows/gYzlgK5Dw1s.md` — Claude Code + Hermes Agent = $10,000 AI Agents
- `transcripts2/product-offers-workflows/vFepZE_wrfg.md` — How to Build $10,000 Agentic Workflows (Claude Code Tutorial)
- `transcripts2/product-offers-workflows/8n-hjkw1bMs.md` — How to build Agentic Workflows with Openclaw
- `transcripts2/product-offers-workflows/vYRUpnnePmA.md` — 6 AI Agency Offers That Actually Make Money in 2026
- `transcripts2/product-offers-workflows/M-BuvknrDYc.md` — 7 Ways I'm Using AI Agents to Make Money in 2026 (Real Examples)

## Livrable — `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/analyses/C2_PRODUCT_OFFE_1.md`

### 1. Par video

- **Ce que la video defend**, en trois phrases maximum.
- **3 a 8 primitives**, chacune avec : un nom court en francais, une definition
  d'une phrase, et une citation VERBATIM de **moins de 15 mots** qui l'ancre.
- **Ce qui ne s'applique PAS**, et pourquoi. Section obligatoire, jamais vide :
  une video dont tout serait applicable signale que tu as arrete de reflechir.

### 2. Traduction produit

| primitive | app visee (ou `couche transversale` / `aucune`) | section | bloc de page de detail | rend quoi plus pauvre en isolation ? |

La derniere colonne applique le test : si tu ne peux rien y ecrire, la primitive
est decorative — retire-la du tableau et dis pourquoi tu l'as ecartee.

### 3. Materiau de domaine

Ce que ces videos t'apprennent sur **la structure du travail** dans leur metier :
les objets manipules, leurs etats, les rythmes, ce qu'on regarde et quand.
Ecris-le comme si tu decrivais un metier a quelqu'un qui doit en dessiner
l'outil.

### 4. Les trois meilleures idees

Classees, chacune justifiee **contre les deux autres**. Un classement sans
comparaison ne vaut rien.

### 5. Ce que ca dit de la these FDE

Ta grappe confirme-t-elle, nuance-t-elle ou contredit-elle les conclusions
rappelees plus haut ? Si elle n'en dit rien, ecris-le — c'est une reponse.

## Interdits

1. Tu ecris **un seul fichier**, a ce chemin ABSOLU exactement : `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/analyses/C2_PRODUCT_OFFE_1.md`.
   N'ecris nulle part ailleurs, et surtout pas dans un dossier `analyses/`
   relatif — un agent precedent a ainsi pollue un depot en lecture seule.
2. **Pas plus de 15 mots d'affilee** cites d'un transcript (droit d'auteur).
3. Ne lis QUE les transcripts de ta liste. Pas de web, pas d'installation.
4. **N'invente aucune citation.** Si tu ne retrouves pas le passage, ecris la
   primitive sans citation en le signalant.
5. Si un transcript est vide ou inutilisable, dis-le et passe au suivant.

## Si tu dois t'arreter

Ecris le rapport avec ce que tu as etabli et une section « **reste a couvrir** »
nommant les videos non traitees. Les sections 1 et 3 priment : si le temps
manque, livre-les completes et tronque le reste.
