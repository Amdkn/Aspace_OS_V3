# C2 — Croissance, acquisition, clonage de personnes

Cluster de 6 transcripts. Méthodes d'acquisition pour SaaS, clonage de funnel par IA,
clonage d'un sales coach par indexation de corpus, prospection vidéo IA sur LinkedIn,
framework "PROFIT" pour agence IA, et outreach vidéo Loom pour clients locaux.

---

## 1. Par vidéo

### V1 — Léo Grindarss, *9 méthodes d'acquisition pour un SaaS* (`yYMwsA7HBHQ`)

**Ce que la vidéo défend.**
Léo classe neuf canaux d'acquisition en tier list après les avoir testés sur ses SaaS,
apps mobiles et chez ses clients de consulting. Les canaux « volume » (clipping, créateurs,
affiliation) paient plus vite que les canaux « qualifiés » (ads, influenceurs), qui coûtent
cher mais scalent fort une fois maîtrisés. Le SEO, lent à installer, reste obligatoire à
poser dès le début, même s'il ne paie pas avant 12 mois.

**Primitives.**

- **P1 — Grille multi-critères de canaux.** Chaque canal est évalué sur quatre axes
  indépendants — viralité, conversion, facilité de production, coût — et non sur un seul.
  > Citation : « on va les classer sous forme de tier list » (8 mots).
- **P2 — Phasage de canaux selon le momentum.** L'ordre d'activation des canaux dépend
  du stade de l'entreprise (lancement → scale → optimisation), pas du canal lui-même.
  > Citation : « le plus important c'est d'utiliser [...] clipping et créateur et affiliation » (10 mots).
- **P3 — Compromis volume-conversion assumé.** Un canal à 5 % de conversion mais à
  volume infini bat un canal à 80 % de conversion mais à audience étouffée.
  > Citation : « faites du volume et dans le volume vous avez de la conversion » (10 mots).

**Ce qui ne s'applique PAS.**
La tier-list elle-même est de l'opinion, pas un cadre : Léo pondère selon ses SaaS B2C
mobile. Un SaaS B2B avec un cycle de vente à 6 mois n'a pas les mêmes critères — le
« volume » tue si la marge brute est faible et le CAC absorbé sur un an. Les seuils
chiffrés (« 50–80 % de l'acquisition via clipping+créateurs ») sont des mesures single-tenant ;
les exporter à un cabinet de coaching B2B ou à une marketplace à vendeurs est illégitime.
La doctrine « l'acquisition fait tout » ignore rétention et produit : aucun des canaux
cités ne les adresse.

---

### V2 — Matt Clark, *I cloned Alex Hormozi's $100M funnel with AI* (`uRskzZf4I6U`)

**Ce que la vidéo défend.**
Le clonage d'un funnel gagnant passe par la préparation des assets (photo, testimonials,
style guide, calendar embed, vidéo source), puis par une demande à l'IA de cloner le
layout et la sales psychology — jamais le contenu. Télécharger la vidéo source via une
extension Chrome, l'uploader dans Gemini, demander un script analogue pour son propre
produit : c'est la chaîne qui transforme un funnel étranger en funnel personnel. Claude
génère du HTML qui se colle dans WordPress/Shopify n'importe où, sans page builder ;
l'itération consiste à corriger des détails de rendu dans la même conversation.

**Primitives.**

- **P4 — Contrat de préparation d'assets avant prompt.** Avant de demander à l'IA de
  cloner une page, on liste tous les assets disponibles (photo, testimonials, style guide,
  calendar embed) et on les prépare ; sans cette étape, le prompt devient un
  aller-retour chaotique.
  > Citation : « I want to make sure that I know exactly um the elements » (9 mots).
- **P5 — Séparation layout-contenu dans le clonage.** On copie la structure et la
  sales psychology d'une page, jamais le contenu textuel ; chaque bloc est rempli avec
  ses propres assets.
  > Citation : « use their layout structure and general sales psychology, but use it to create my own page » (14 mots).
- **P6 — Analyse vidéo source par upload + transcription.** Pour cloner un funnel qui
  contient une vidéo, on télécharge la vidéo (extension Chrome) et on l'uploade dans
  Gemini avec une consigne de transcription en script analogue.
  > Citation : « I downloaded or I added this extension to Chrome called Video Download Helper » (12 mots).

**Ce qui ne s'applique PAS.**
Le stack précis (Claude + WhisperFlow + Pictory + Video Download Helper) est un chemin
parmi d'autres — un OS ne doit pas s'y accrocher. Le clonage fonctionne pour les
funnels « publics » qu'on a le droit de référencer ; pour un concurrent au funnel privé,
c'est de l'inspiration manuelle. La fidélité du clone dépend d'avoir des assets déjà
propres : pour un coach sans testimonial ni photo, la page générée est vide et le clone
n'a rien à dire.

---

### V3 — Jeremy Miner / Paul Allen, *World's Best Sales Coach Just Got Cloned by AI* (`oXCNcdYiyXQ`)

**Ce que la vidéo défend.**
7Q.ai a transcrit et indexé chaque mot des formations de Jeremy Miner (161 verticales,
des milliers d'heures), puis a construit un retriever qui sort un clip de 30 secondes
pertinent au lieu d'une réponse générique. Pour les knowledge workers, l'équivalent du
« game film » des athlètes existe enfin : on rejoue ses propres appels, on voit où la
garde du prospect s'est levée, et on renvoie vers le clip de formation qui corrige ce
geste précis. Un LLM généraliste (ChatGPT, Grok) mélange les sources et produit du
« slop » ; un LLM nourri exclusivement par un corpus personnel indexé reste fidèle.

**Primitives.**

- **P7 — Retrieval sur corpus personnel indexé.** Un système d'IA ne devrait jamais
  répondre à une question métier à partir de données publiques : il indexe chaque mot
  du corpus du client et retrieve le passage exact.
  > Citation : « We've transcribed every word you and your team have spoken » (10 mots).
- **P8 — Clip de 30 s comme réponse atomique.** Au lieu d'un paragraphe générique, le
  système retourne le clip exact de formation qui répond à la question, avec son
  timestamp et son contexte d'origine.
  > Citation : « here's a 30 second clip that is exactly what you need » (11 mots).
- **P9 — Renforcement post-formation par rappel ciblé.** La formation seule ne change
  pas le comportement ; c'est le rappel régulier et ciblé qui produit les résultats —
  l'étude Marshall Goldsmith sur 88 000 leaders le montre.
  > Citation : « regular periodic followup had offthecharts progress » (5 mots).

**Ce qui ne s'applique PAS.**
Le clonage d'un « world-class sales coach » exige des milliers d'heures de corpus
indexé. Un coach qui démarre avec 50 heures de contenu ne peut pas être « cloné » de
cette façon : le retriever a trop peu de signal pour distinguer ses positions des
positions communes. La promesse « un billion de Jeremy Miners » est commerciale, pas
technique — l'IA reproduit la méthode, pas la présence, le ton, ni la confiance qu'inspire
un humain. Le couplage avec Gong (call recording) est une autre brique ; sans elle, le
game-film n'existe pas.

---

### V4 — Shubham Sharma, *Comment j'ai piégé LinkedIn avec une vidéo IA* (`cT0zEwF39Q0`)

**Ce que la vidéo défend.**
Shubham orchestre une chaîne Airtable → HeyGen → Creatomate → API screenshot → Unipile
pour produire une vidéo personnalisée par prospect, où le prénom et le profil LinkedIn
défilent derrière son avatar IA. Résultat annoncé : un taux de réponse 20 fois supérieur
au texte, parce que la vidéo simule un contact personnel sans en avoir le coût. L'astuce
défensive : mixer une vraie vidéo filmée (où il fait des gestes) avec un insert IA (où il
dit le prénom), pour rendre la détection plus difficile.

**Primitives.**

- **P10 — Substitution d'assets par destinataire à partir d'un template.** Un même
  template vidéo prend en variables le prénom, le profil LinkedIn, le post à commenter ;
  chaque prospect reçoit une vidéo unique sans coût marginal de création.
  > Citation : « le code promo qui apparaît avec le nom de Martin c'est une variable » (12 mots).
- **P11 — Screenshot-vidéo live comme contexte de crédibilité.** Au lieu d'un fond
  statique, on génère une vidéo du profil LinkedIn du destinataire en train de défiler —
  ce qui simule une visite en temps réel de son profil par l'émetteur.
  > Citation : « le fait de voir son screenshot derrière c'est une chose » (10 mots).
- **P12 — Agrégation d'API sortantes pour canaux fermés.** Quand une plateforme
  (LinkedIn) bloque nativement l'envoi de vidéo, on passe par un agrégateur (Unipile)
  qui expose l'API et produit le rendu de prévisualisation.
  > Citation : « LinkedIn normalement nous permet pas de faire ça » (7 mots).

**Ce qui ne s'applique PAS.**
Cette chaîne est fragile. LinkedIn peut bannir les comptes qui émettent trop de vidéos
IA par jour. Le coût (HeyGen + Creatomate + Unipile ≈ 150 €/mois) ne se rentabilise
qu'au-dessus de 50 prospects/jour ; en dessous, un email personnalisé suffit. L'astuce
défensive (mix réel/IA) est exactement ce que les plateformes détectent de mieux en
mieux — ce qui marche aujourd'hui sera filtré demain. Le « 20 fois le taux de réponse »
est un claim du créateur, pas une mesure contrôlée.

---

### V5 — Michele Torti, *How I'd Get My First AI Agency Client in 30 Days* (`F9TV5hmsmKI`)

**Ce que la vidéo défend.**
Cinq mois à regarder des tutos IA = 0 €. Le déclic : arrêter de commencer par les
outils, commencer par le problème. Le système « PROFIT » (Pick profitable niche,
Recognize offer, Outreach, Fulfill, Increase recurring, Transform) impose une
séquence — problème → offre → outreach → livraison → récurrent → business. Vendre « de
l'automatisation IA », c'est se vendre soi-même ; vendre « un speed-to-lead qui rappelle
en 5 min et remplit le calendrier sans recruter », c'est vendre un outcome. Le second
vend, le premier pas.

**Primitives.**

- **P13 — Inversion de séquence problème-outil.** Dans tout projet, le problème métier
  précède l'outil ; commencer par l'outil enferme dans le « tutorial hell » et bloque
  l'accès au client.
  > Citation : « Why are you starting with tools first? » (6 mots).
- **P14 — Filtre de niche à trois critères.** Une niche n'est valable que si elle coche
  trois cases : elle fait du vrai profit, elle a un problème répétitif et douloureux
  soluble par l'IA, et le porteur a un avantage injuste (réseau, métier, langue).
  > Citation : « the business needs to make real money » (7 mots).
- **P15 — Refocalisation d'offre par outcome.** Une offre vend le résultat métier
  observable, pas la mécanique qui l'obtient ; le client ne paie pas pour « de l'IA »,
  il paie pour « rappeler en 5 min et remplir le calendrier ».
  > Citation : « Nobody buys AI. They buy the outcome » (7 mots).
- **P16 — Modèle économique setup + retainer.** Un projet ponctuel libère de la
  trésorerie mais ne bâtit pas une agence ; seul un retainer mensuel récurrent
  transforme un freelancer en opérateur d'agence.
  > Citation : « setup fee pays the bills for the agency » (8 mots).

**Ce qui ne s'applique PAS.**
Le sigle PROFIT est mnémonique, pas structurel — il faut extraire les 6 gestes, pas
mémoriser l'acronyme. « Nobody buys AI » est trop fort : les acheteurs sophistiqués
(DSI, CTO) achètent bien de l'IA ; la nuance exacte est « personne n'achète AI pour
AI », ce qui est plus faible et plus défendable. Le cas client « $2M en 6 mois » est un
outlier ; le médian d'une agence IA qui démarre est plutôt $0–3 K MRR au bout de 3 mois.

---

### V6 — Adam Erhart, *Record 2-min video → $297/mo client* (`p0Fw_xGIWpE`)

**Ce que la vidéo défend.**
Erhart a vendu pendant 10 ans la même mécanique : l'audit visible (comptage d'avis
Google) → permission demandée → vidéo Loom de 30 secondes montrant le gap → follow-up
→ close à 297 $/mois. Cette mécanique marche comme « lumpy mail » depuis 2010 et comme
vidéo Loom aujourd'hui ; ce qui change, c'est le canal, pas le principe. Une seule
offre, un seul problème, un seul prix — pas de menu. Le Cheesecake Factory tue la
conversion.

**Primitives.**

- **P17 — Audit-not-pitch.** Au lieu de pitcher son service, on montre au prospect un
  défaut visible et quantifiable de son business, et on propose de le réparer.
  > Citation : « you're going to prove that you understand his problem before you ask » (12 mots).
- **P18 — Permission-gate avant envoi d'asset.** On ne balance pas la vidéo d'audit ;
  on demande d'abord « puis-je vous l'envoyer ? » ; ceux qui répondent oui deviennent
  les destinataires.
  > Citation : « Is it all right to send it over? » (7 mots).
- **P19 — Discipline mono-offre.** Un seul service, un seul problème, un seul prix ; le
  reste du menu attend que le client ait signé le premier.
  > Citation : « one offer, one problem, one price » (6 mots).
- **P20 — Discipline du pas-de-réponse.** L'absence de réponse n'est pas un refus,
  c'est un « pas maintenant » ; deux relances espacées suffisent avant de passer au
  prospect suivant.
  > Citation : « No reply is not a no. It's a not right now » (10 mots).

**Ce qui ne s'applique PAS.**
Le « 297 $/mois pour des avis Google » est un prix pour un marché local US très
spécifique ; en B2B SaaS, le ticket d'entrée est 10× plus haut et le cycle 10× plus
long. « Lumpy mail » → Loom est une migration de canal, pas une révolution de principe —
l'OS ne doit pas canoniser Loom, il doit canoniser l'audit-visible. « Envoyer 10
messages par jour » est un volume solo ; une équipe de 5 personnes a besoin d'une
cadence différente (qualification outbound, scoring,Account-Based Marketing).

---

## 2. Traduction produit

| # | Primitive | App visée | Section | Bloc de page de détail | Rend quoi plus pauvre en isolation ? |
|---|---|---|---|---|---|
| P1 | Grille multi-critères de canaux | growth | Acquisition | Tableau 4 colonnes (viralité/conversion/coût/facilité) avec score par canal | Sans grille, les canaux deviennent des rubriques uniformes ; la sélection devient subjective et le tri s'effondre. |
| P2 | Phasage de canaux | growth | Stratégie | Timeline 3 phases (lancement / scale / optimisation) avec canaux empilés | Sans phasage, `growth` ne distingue plus « à activer maintenant » de « à activer quand on a du budget » ; tout paraît urgent. |
| P3 | Compromis volume-conversion | growth | Stratégie | Toggle par canal : mode « volume » ou mode « qualifié » | Sans toggle, l'utilisateur vise les deux et n'atteint ni l'un ni l'autre ; le canal s'épuise. |
| P4 | Contrat de préparation d'assets | growth + _ui | Campagnes / Modèles | Checklist des assets requis (photo, testimonials, embed, vidéo) avant activation d'un template IA | Sans checklist, chaque prompt IA devient un aller-retour chaotique ; la « génération en un clic » est un mensonge. |
| P5 | Séparation layout-contenu | growth + design | Pages | Vues « structure » et « contenu » indépendantes ; clone de structure autorisé, contenu réécrit | Sans séparation, le clone de funnel devient du plagiat ; la section « inspiration » disparaît. |
| P6 | Analyse vidéo source | growth | Recherche de modèles | Module « importer une vidéo source + extraire le script » dans le builder de page | Sans ce module, le clonage se limite aux pages textuelles ; la moitié des funnels gagnants devient invisible. |
| P7 | Retrieval sur corpus personnel | couche transversale | Base de connaissance | Champ « corpus indexé » par entité (Person/Agent), requêté en priorité avant tout LLM généraliste | Sans cette priorité, l'OS répond avec du contenu générique au lieu du corpus du client ; la valeur du graphe de contexte s'évapore. |
| P8 | Clip de 30 s atomique | people | Bibliothèque de formation | Vue « clip » par extrait de formation avec timestamp, attachable à une fiche prospect | Sans clip atomique, la formation reste un long vidéo que personne ne ré-écoute ; la bibliothèque n'est jamais rappelée au moment de l'action. |
| P9 | Renforcement post-formation | people + sales | Plan de coaching | Fréquence de rappel + clip attaché à chaque étape du pipeline | Sans rappel, la formation n'est jamais appliquée (Goldsmith) ; la page « mes formations » devient un cimetière de badges. |
| P10 | Substitution d'assets par destinataire | growth | Campagnes | Template vidéo + table de variables ; prévisualisation par destinataire | Sans substitution, l'outreach reste générique ; le `growth` n'a plus de moteur de personnalisation industrielle. |
| P11 | Screenshot-vidéo live | growth | Assets sortants | Type d'asset « vidéo-personnalisée-avec-scroll » | Sans ce type d'asset, la personnalisation se limite au prénom ; la vidéo perd son effet de preuve. |
| P12 | Agrégation d'API sortantes | couche transversale | Connecteurs | Liste des canaux fermés (LinkedIn, WhatsApp, IG) avec API tierce obligatoire | Sans agrégation, l'OS ne peut émettre que sur des canaux ouverts (email, formulaire) ; `growth` perd les canaux où se trouvent les décideurs. |
| P13 | Inversion problème-outil | couche transversale | Ordre de projet | Vue « Workflow » qui force le champ « problème » avant le champ « outil » | Sans cette contrainte, tous les projets démarrent tool-first et restent en tutorial hell ; la plateforme n'a plus de boussole. |
| P14 | Filtre de niche 3 critères | growth + sales | Cible | Score auto-évalué sur 3 axes (profit / problème / avantage) avant de figer l'ICP | Sans filtre, le ciblage devient un wishlist ; la section « ICP » de `sales` n'a plus aucun pouvoir de tri. |
| P15 | Refocalisation par outcome | sales + product | Offre | Canvas « offre » avec champs « outcome client » obligatoires, « mécanique » en second | Sans canvas orienté outcome, l'argumentaire reste centré features ; le pricing paraît arbitraire. |
| P16 | Setup + retainer | sales + finance | Contrat | Modèle de contrat avec `setup_fee` + `monthly_retainer`, refus d'un one-off | Sans ce modèle, l'utilisateur signe des one-offs et plafonne ; la MRR de l'OS ne se construit jamais. |
| P17 | Audit-not-pitch | sales + audit | Premier contact | Template vidéo audit (Loom ou équivalent) attaché au prospect, pas un pitch deck | Sans ce template, le premier contact est un pitch et finit ignoré ; `sales` n'a plus de porte d'entrée humaine. |
| P18 | Permission-gate | sales + growth | Séquence outbound | Étape « demande de permission » obligatoire avant envoi d'asset | Sans gate, l'envoi ressemble à du spam ; le taux de réponse chute et le canal se dégrade. |
| P19 | Discipline mono-offre | sales + product | Offre | Refus d'une page « menu » ; un seul service affiché par prospect | Sans discipline, l'offre devient illisible ; le prospect choisit de ne pas choisir. |
| P20 | Pas-de-réponse ≠ non | sales | Relance | Limite à 2 relances espacées ; après, archivage avec motif | Sans limite, les relances s'éternisent et le moral baisse ; la cadence d'outbound s'effondre. |

> **Primitives écartées** : aucune. Toutes les 20 primitives passent le test — chacune
> dévalorise quelque chose d'existant si on la retire. Les plus faibles sont P3 (toggle
> volume/qualifié, qui peut vivre comme sous-rubrique de P2) et P11 (screenshot-vidéo,
> qui n'a de valeur qu'en présence de P10) ; je les conserve parce qu'elles forcent des
> décisions que l'OS ne sait pas prendre aujourd'hui.

---

## 3. Matériau de domaine

**Le métier de l'acquisition outbound, tel que ces six vidéos le décrivent, ressemble à
une chaîne de décisions industrielles, pas à une discipline de persuasion.**

**Les objets manipulés.**

- **Le canal** a quatre propriétés indépendantes (viralité, conversion, coût, facilité),
  un point d'activation (à quel stade du produit), et un compteur de saturation (quand il
  s'épuise). Léo insiste : chaque canal a un cycle de vie propre, pas un score absolu.
- **L'asset outbound** (vidéo Loom, email, DM, page de funnel) a une structure (template)
  et des variables (nom, avatar, contexte, profil). Le pipeline d'envoi est un mécanisme
  de substitution d'asset par destinataire (Shubham) — pas une copie-collée.
- **L'offre** a un outcome observable (le client voit le résultat), une mécanique (comment
  l'IA l'obtient), un prix, et un mode de facturation (one-off vs retainer). Le « bad
  offer » de Torti (« nous faisons des automatisations AI ») n'a pas d'outcome visible ;
  le « good offer » (« speed-to-lead qui rappelle en 5 min ») en a un.
- **Le pipeline de vente** a un ordre strict — niche (3 critères) → offre (refocalisée
  outcome) → outreach (permission + asset) → audit (vidéo) → close → relance disciplinée
  → upsell après le premier contrat. Inverser un seul cran casse le pipeline (Torti).
- **Le corpus personnel** (Paul Allen / Jeremy Miner) : pour une personne dont le métier
  EST le conseil, son corpus de formations est un actif qui peut être indexé, requêté,
  et renvoyé comme réponse. Ce n'est pas une « base de connaissance » au sens
  documentaire — c'est un produit dérivé dont chaque clip de 30 s est une unité
  monnayable.
- **Le funnel cloné** (Matt Clark) : un funnel gagnant a une structure copiable et un
  contenu à substituer. La mécanique du clonage est — asset prep → extraction de la
  source (vidéo) → transcription → script analogue → régénération → intégration dans la
  page → itération de rendu. La séparation layout/contenu n'est pas une convention de
  design, c'est une séparation juridique (ce qui est copiable) et sémantique (ce qui
  doit être réécrit).

**Les états traversés.**

- Pour un **prospect** : `froid` → `permission demandée` → `permission accordée` →
  `audit reçu` → `audit regardé` → `question posée` → `close tenté` → `client` ou
  `archivé après 2 relances` (Erhart).
- Pour un **canal** d'acquisition : `à activer` → `actif` → `saturé` → `archivé` (Léo).
  Léo observe que les canaux à audience froide (clipping) s'épuisent plus vite que les
  canaux à audience chaude (affiliés).
- Pour un **client** : `premier contrat (setup)` → `retainer` → `upsell sur problème
  adjacent` → `multi-service`. Torti insiste : sans upsell, le retainer reste un one-off
  déguisé.
- Pour un **asset outbound** : `template vide` → `template + variables mappées` →
  `preview par destinataire` → `envoi batch` → `tracking réponse` (Shubham).
- Pour un **funnel** : `source identifiée` → `assets réunis` → `IA-clone généré` →
  `rendu vérifié` → `déployé` → `itéré sur détails de rendu` (Matt Clark).

**Les rythmes.**

- **Outreach solo** : 10 messages/jour, 2 relances, archivage. Cadence humaine, pas
  industrielle (Erhart).
- **Outreach industrialisé** : 50+ prospects/jour, pipeline Airtable, génération vidéo
  en batch. Cadence de pipeline (Shubham). Le coût tooling (~150 €/mois) impose le seuil.
- **Cycle de vente B2B** : 6 mois minimum. Incompatible avec les rythmes de Léo et
  Torti, qui parlent de SaaS self-serve et d'agences AI — pas de mêmes segments.
- **Formation + rappel** : la formation ponctuelle a 0 % de rétention ; le rappel
  périodique a un effet « off the charts » (Goldsmith, cité par Paul Allen). Le rappel
  est hebdomadaire ou mensuel, pas quotidien.
- **Indexation de corpus** : la transcription et l'indexation sont one-shot (Paul Allen :
  161 verticales, milliers d'heures), mais le retriever tourne en continu. Le travail
  d'indexation est projet ; le retriever est commodité.

**Ce qu'on regarde et quand.**

- **Avant d'envoyer** : la permission a-t-elle été demandée ? Oui/non (Erhart).
- **Avant de pitch** : l'audit a-t-il été livré ? Oui/non (Erhart).
- **Avant de relancer** : combien de jours depuis le dernier contact ? > 2 jours
  (Erhart). Combien de relances déjà ? ≤ 2.
- **Avant de facturer** : le client a-t-il signé pour le setup fee ET le retainer ?
  Oui/non (Torti).
- **Avant de cloner une page** : a-t-on préparé tous les assets requis ? Oui/non
  (Matt Clark). Le clone sans assets est vide.
- **Avant de répondre à une question client** : le clip de 30 s existe-t-il dans le
  corpus indexé ? Si oui, on l'envoie avec son timestamp ; si non, on passe à l'avis
  générique (Paul Allen).
- **Avant d'ajouter un canal** : la grille 4 critères (viralité/conversion/coût/facilité)
  est-elle remplie ? À quel stade du produit on l'active ? Léo : pas d'ads au lancement.
- **Avant de figer l'ICP** : les 3 critères (vrai profit / problème répétitif /
  avantage injuste) sont-ils validés ? Torti : si l'un manque, tout le reste devient
  plus dur.

**Les états impossibles que ces vidéos enseignent aussi.**

- On ne peut pas envoyer un audit sans avoir demandé la permission — l'envoi devient
  spam, le canal se dégrade (Erhart).
- On ne peut pas vendre de l'IA sans avoir formulé l'outcome client — l'objection
  « c'est cher » arrive au premier coup (Torti).
- On ne peut pas cloner une page sans avoir préparé les assets — l'IA génère du vide
  (Matt Clark).
- On ne peut pas activer un canal à ads au lancement — la marge est trop faible pour
  absorber le CAC (Léo).
- On ne peut pas répondre à une question métier avec un LLM généraliste quand un
  corpus indexé existe — la réponse perd la fidélité au coach (Paul Allen).

---

## 4. Les trois meilleures idées

**Rang 1 — Inversion problème-outil (P13, de Torti).**
C'est un primitif *méta*, pas une feature. Les deux autres primitifs (substitution
d'assets par destinataire, audit-not-pitch) ne paient que si l'utilisateur a intériorisé
l'inversion. Un utilisateur en tutorial hell qui copie le template d'Erhart produira une
vidéo Loom techno-centrée, sans audit visible. Un utilisateur qui copie la chaîne de
Shubham construira un pipeline de masse qui spamme. L'inversion est le primitif qui rend
les deux autres utiles. Elle s'applique au-delà de l'outbound : tout workflow de l'OS
commence par le problème, pas par l'outil — y compris la construction d'une primitive
elle-même. Sans elle, la plateforme devient une bibliothèque de features sans boussole.

**Rang 2 — Substitution d'assets par destinataire (P10, de Shubham).**
C'est le seul primitif du cluster qui exige une infrastructure réelle de l'OS —
moteur de templates, table de variables, agrégateur d'API sortantes, prévisualisation
par destinataire. L'audit-not-pitch (P17) marche en one-to-one, à cadence humaine ; il
est contenu dans la liste de courses d'un commercial. La substitution d'assets ouvre la
cadence industrielle sans perdre la personnalisation : un prospect qui reçoit une vidéo
avec son profil LinkedIn en arrière-plan est engagé qualitativement différemment d'un
prospect qui reçoit un email avec son nom en variable. C'est aussi le primitif qui
force l'OS à modéliser explicitement la notion de « destinataire » comme entité de
première classe — ce que le cluster de grappes antérieures n'a pas fait.

**Rang 3 — Audit-not-pitch (P17, d'Erhart).**
C'est le primitif le plus universalisable. Il marche pour un coach B2B, un dentiste
local, un SaaS B2C, une association. Il survit aux changements de canal — lumpy mail
en 2010, Loom en 2025, vidéo IA en 2026 — parce que le principe (« donner avant de
demander ») ne dépend pas du médium. Il marche même si l'OS n'a aucune autre feature :
un commercial qui envoie 10 audits par jour en suivant le template d'Erhart signe des
clients. Les deux autres primitifs ont besoin d'un OS structuré pour se déployer
(workflow forcé pour P13, infrastructure de templates pour P10) ; P17 peut fonctionner
avec un cahier et un téléphone. Pour un produit qui doit servir d'autres niches demain,
c'est la primitive la plus défensive.

**Pourquoi pas les autres ?**
P7 (retrieval sur corpus personnel) et P8 (clip de 30 s) sont puissantes, mais
elles ne s'appliquent qu'aux niches « conseil / formation » — elles sont moins
universalistes que P17. P1/P2 (grille et phasage de canaux) sont de la stratégie
d'acquisition, pas une primitive de plateforme : elles appartiennent à `growth`, pas à
la couche transversale. P16 (setup + retainer) est un primitif financier important mais
limité au modèle d'agence ; pour un produit SaaS self-serve, il ne s'applique pas.

---

## 5. Ce que ça dit de la thèse FDE

**Confirmation forte d'un geste déjà identifié.** Le geste FDE « promouvoir un constat
en primitive de plateforme » (le 4e des quatre qui résistent) est illustré directement
par Torti : la séquence problème-outil EST la promotion d'un constat (« les clients
achètent des outcomes, pas de l'IA ») en primitif de plateforme. Sans cette promotion,
l'OS reste une bibliothèque d'outils. Le cluster confirme que ce geste résiste à
l'automatisation parce qu'il exige un arbitrage humain (quel constat mérite d'être
promu ?), pas seulement une exécution technique.

**Affinement des 5 gestes automatisables.**

- « Construire l'ontologie » est complété par **« préparer le contrat d'assets » (P4)**.
  L'OS doit non seulement modéliser les entités du client, il doit aussi inventorier
  les assets concrets (photo, testimonials, calendar embed, vidéo) qui serviront de
  variables dans les templates. Matt Clark montre que cette étape, omise, transforme
  un prompt unique en 20 allers-retours.
- « Câbler les systèmes » est complété par **« agréger les API sortantes » (P12)**.
  L'OS doit savoir *émettre* sur des canaux fermés (LinkedIn, WhatsApp, Instagram), pas
  seulement lire sur des API ouvertes. Shubham montre qu'Unipile est la brique qui rend
  l'émission possible quand la plateforme refuse nativement l'envoi.

**Ajout d'un nouveau geste automatisable manquant dans la première analyse.**
**« Indexer le corpus personnel du client » (P7)**. Paul Allen et Jeremy Miner montrent
qu'un coach avec 10 000 heures de formation a un actif qu'aucun LLM généraliste ne peut
reproduire. L'OS doit donc, dans son graphe de contexte, prévoir un slot « corpus
indexé » par entité Person — et requêter ce corpus *avant* de tomber sur le LLM
généraliste. Ce n'est pas la même chose que « construire l'ontologie » (qui structure
les relations entre entités) : c'est « rendre le corpus requêtable » (qui rend
l'expertise retrouvable à l'unité de clip près). Le cluster suggère que ce geste devrait
être ajouté à la liste des cinq automatisables — il devient un sixième.

**Confirmation par le négatif.** Aucun des 6 transcripts ne parle du mandat
hiérarchique, du consentement à révéler l'exception non écrite, ou de la responsabilité
juridique — les trois autres gestes FDE qui résistent. La grappe ne les contredit pas,
elle n'en parle simplement pas. Ce silence est cohérent : les six vidéos sont des
praticiens qui montrent des gestes opérationnels (acquisition, vente, tooling), pas des
managers qui arbitrent des exceptions. La couche FDE qui résiste (mandat, exception,
juridique) est probablement mieux éclairée par les grappes « clients », « compliance »
ou « operations » — pas par « growth/acquisition/clonage ».

**Nuance sur « spécialiser les agents ».** Torti recommande explicitement « vous n'avez
pas besoin d'être un expert technique — sous-traitez la construction ». C'est
l'inverse de la spécialisation agent telle que formulée dans la première analyse. À
mettre en regard : l'OS ne doit pas chercher à remplacer l'expert métier du client, il
doit chercher à rendre cet expert *substituable* sur des gestes techniques (templates,
API). L'expert reste, l'OS prend la tuyauterie. La spécialisation des agents n'est
donc pas « former un agent à faire le métier du client » mais « construire un agent
qui exécute les gestes techniques du client à partir de l'expertise du client ». P7
(retrieval sur corpus) en est l'opérationnalisation.

**Implication pour le canon.** Le canon V2 gagnerait à inclure le primitif P13
(inversion problème-outil) comme règle de gouvernance transversale — non pas comme
section d'une app, mais comme invariant que toutes les sections doivent respecter.
Les primitifs P7 (corpus indexé) et P12 (agrégation API sortantes) gagneraient à être
ajoutés à la liste des gestes FDE automatisables. Les primitifs P10, P11, P17, P18
gagneraient à être ajoutés à l'app `growth` ; P14, P15, P16 à l'app `sales` ; P8, P9 à
l'app `people`. P1, P2, P3 restent dans `growth` comme primitives d'acquisition
pures, sans prétention transversale.
