# -*- coding: utf-8 -*-
"""Vagues 2 et 3 du chantier Dashboard. Le tronc commun est repris du brief 1
pour que la doctrine (theme, chiffres durs, interdits) ne diverge pas."""
import pathlib

P = pathlib.Path(__file__).parent
tronc = (P / "BRIEF_DASHBOARD_V1.md").read_text(encoding="utf-8")
COMMUN = tronc[tronc.index("## Le theme"):tronc.index("## Rapport attendu")]

VAGUES = {
 "V2": dict(
  titre="les 7 pages de securite",
  dossier="security",
  groupe="SECURITY",
  images="`14-kill-switches.png`, `15-panic.png`, `16-compliance.png`, plus les images `z-*` de la seconde moitie de la video",
  sections="""
1. **Kill Switches** — la grille d'interrupteurs, **42 exactement**, groupes par
   famille (controle des couts, securite et garde-fous, agents, outils). Chaque
   interrupteur : son libelle, ce qu'il coupe en une phrase, son etat. Un
   interrupteur arme doit se voir au premier coup d'oeil.

2. **DLP & Exfil** — les **9 motifs**, et ils ne sont pas negociables. Sept
   **bloquants** : cles d'acces AWS, en-tetes de cle d'API, cles privees PEM,
   jetons Slack, PAT GitHub, cartes bancaires, numeros SSN. Deux en
   **avertissement** : chaines en forme de cle secrete AWS, JWT. Distingue
   nettement bloquant et avertissement — c'est toute la nuance de la page.

3. **Panic** — le bouton qui arrete tout, et ce qu'il implique. Une page qui doit
   inspirer la prudence : ce qui s'arrete, ce qui survit, ce qui est reversible.
   Confirmation obligatoire, et l'action est tracee.

4. **Rate Limits** — les limites de debit par agent et par surface, leur
   consommation actuelle, et ce qui se passe au depassement.

5. **Security Posture** — l'etat de preparation, critere par critere, avec trois
   niveaux : conforme, partiel, non conforme. Le total ne suffit pas : c'est la
   liste des manques qui sert.

6. **Compliance** — la lecture SOC 2 / HIPAA. Un score, la liste des controles,
   et surtout le **brief de remediation** : pour chaque ecart, le texte qu'on
   envoie a un modele pour le combler. C'est la partie que Mark met en avant.

7. **Alerting** — les alertes configurees, leur seuil, leur destinataire et leur
   dernier declenchement.

Rappelle, sur `Kill Switches` ou `Security Posture`, l'ordre du goulot
d'etranglement, exactement celui-ci :
`limite de debit -> chargement de l'agent -> coupe-circuit modele -> plafond de
cout (echoue ferme) -> commutateur d'outil -> garde-fou -> boucle de conversation
-> repartition des outils -> analyse DLP -> journal`.

Le plafond de cout **echoue ferme** : s'il ne peut pas calculer la depense du
jour, il arrete tout plutot que de laisser filer. Ce comportement doit se voir,
pas seulement exister dans le code.
"""),

 "V3": dict(
  titre="les 4 pages de plateforme",
  dossier="platform",
  groupe="PLATFORM",
  images="`17-integrations.png`, plus les images `z-*` de la seconde moitie de la video",
  sections="""
1. **Integrations** — la grille des connecteurs, comme dans
   `17-integrations.png` : une tuile par outil, son etat (`connecte / disponible
   / indisponible`), et ce a quoi il donne acces. Coach OS en a de vrais : les
   MCP passent tous par un gateway unique. Appuie-toi sur ce qui existe plutot
   que d'inventer un catalogue.

2. **Knowledge** — le depot de documents et leur cycle : depose, extrait,
   decoupe, vectorise, interrogeable. Chaque entree porte son etat dans ce cycle.
   On doit pouvoir poser une question a un document, voir la reponse **et sa
   source**.

3. **Memories** — la memoire longue et son hygiene. Chaque souvenir : le fait
   retenu, sa provenance, sa date, son statut (`confirme / contredit / a
   verifier`) et son poids. Une couche partagee entre agents — la ruche — et une
   couche propre a chaque agent. La memoire brute est un depotoir ; ce qui compte
   est ce qui a ete verifie.

4. **Members** — l'equipe et ses roles. **Cinq roles, du plus faible au plus
   fort : viewer, analyst, operator, admin, owner.** Chaque personne : son role,
   ce qu'il lui ouvre, sa derniere activite. Le principe a rendre visible :
   l'interface ne fait que masquer des onglets, **l'autorite est au serveur**.
   Chaque changement de privilege est attribue a une personne reelle.
"""),
}

EN_TETE = """# BRIEF — app Dashboard, vague %(v)s : %(titre)s

Tu es developpeur front. Tu ecris **un module de sections autonome** pour l'app
`dashboard` de Coach OS, d'apres l'Enterprise OS de Mark Kashef.

## Cloisonnement — lis ceci en premier

Trois agents travaillent sur cette app **en meme temps**. Pour qu'ils ne se
marchent pas dessus, chacun ecrit dans son dossier et **aucun ne touche a
`DashboardApp.tsx`** : le raccordement est fait ensuite, par l'orchestrateur.

**Ton perimetre exclusif : `src/apps/dashboard/%(dossier)s/`**

Tu y crees un `index.ts` qui exporte :

```ts
export const %(groupe)s_SECTIONS: AppSection[] = [ ... ];
```

Le type `AppSection` vient de `src/components/AppFrame.tsx` — importe-le, ne le
redefinis pas. Regarde comment `DashboardApp.tsx` construit son tableau de
sections aujourd'hui et produis exactement la meme forme : `{ id, label, icon,
render }`. Tes donnees de demonstration vont dans
`src/apps/dashboard/%(dossier)s/seed.ts`.

**Si tu edites `DashboardApp.tsx`, tu casses le travail de deux autres agents.**

## Le depot

`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`

React 19 - TypeScript - Tailwind v4 - Zustand - Vite.
**Reference TS : 75 erreurs preexistantes. Ne la depasse pas.** `npm test` : 60 verts.

## La barre — regarde-la, ne l'imagine pas

`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/barre-jarvis/pages/`

26 images pleine resolution extraites de la video de Mark. Pour toi : %(images)s.
`06-chat-sidebar-complete.png` montre la barre laterale entiere et lisible.

**Ouvre ces images.** Un agent qui juge sur une description approuve tout — c'est
le mode d'echec numero un de cette methode, dit tel quel par ses auteurs.

## Le fond — les chiffres sont donnes, ne les invente pas

`C:/Users/amado/Downloads/Enterprise_OS_Blueprint_Kit (1)/BLUEPRINT.md`

Document de Mark. Il fixe : **42 coupe-circuits**, **9 motifs DLP** (7 bloquants,
2 avertissements), **~31 tables**, **6 seaux**, **3 cles**, **15 piles**,
**5 roles**, **4 paliers**.

**Adaptation obligatoire.** Coach OS ne tourne pas sur AWS. Tu transposes :
Bedrock vers les modeles reellement utilises ici (Claude Opus/Sonnet/Haiku,
MiniMax-M3, modeles ouverts) ; DynamoDB et S3 vers Supabase ; IAM vers les 5
roles. Les donnees affichees sont de demonstration, credibles pour un cabinet de
coaching. La **structure** est celle de Mark.

## Tes sections
%(sections)s
"""

VERIF = """
## Verification obligatoire

```
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
npm test
grep -rEo "\\b(bg|text|border)-(white|black|stone|slate|zinc|gray|neutral)(-[0-9]+)?\\b" src/apps/dashboard/%(dossier)s --include=*.tsx | wc -l
```

Attendu : **au plus 75**, tests verts, **0 classe de palette**.

Tes sections ne sont pas encore raccordees a l'app — c'est voulu, le raccordement
vient apres. Tu ne peux donc pas les photographier toi-meme. Rends un code qui
compile et dont chaque section affiche quelque chose de structure.

## Rapport attendu

Ecris-le dans
`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/RAPPORT_DASHBOARD_%(v)s.md`.

Il contient : les sections livrees avec leur `id`, les fichiers crees, le nom
exact de la constante exportee, les chiffres de verification, les couleurs
semantiques laissees volontairement avec leur raison, et **tout point non fait
avec sa raison**. Un point non fait et signale vaut mieux qu'un point bacle en
silence.

Si tu dois t'arreter avant la fin, ecris quand meme ce rapport avec l'etat exact.
"""

for v, a in VAGUES.items():
    d = dict(a, v=v)
    txt = (EN_TETE % d) + COMMUN + (VERIF % d)
    txt = txt.replace(
        "1. Tu ne touches qu'a `src/apps/dashboard/`.",
        "1. Tu ne touches qu'a `src/apps/dashboard/%s/`. **Ni `DashboardApp.tsx`**, "
        "ni le dossier d'une autre vague." % a["dossier"])
    f = P / ("BRIEF_DASHBOARD_%s.md" % v)
    f.write_text(txt, encoding="utf-8")
    print("%-28s %6d caracteres" % (f.name, len(txt)))
