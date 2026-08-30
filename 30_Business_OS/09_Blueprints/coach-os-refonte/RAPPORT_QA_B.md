# Rapport QA B — Coach OS

**Périmètre** : `people`, `operations`, `it-rd`, `clients`, `tasks`
**Thèmes testés** : `warm-paper` (clair) et `dark-oled` (sombre)
**Captures** : `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/qa/B/`

**Note méthodologique** : le sélecteur `--section` du `tools/shot.mjs` matche le
bouton désactivé du fil d'Ariane et échoue à cliquer la section active. Pour
passer outre sans modifier le dépôt, j'ai posé le thème dans le localStorage,
puis cliqué le bouton de la sidebar via `aside button` filtré sur le libellé
exact. Le bouton désactivé reste dans le fil d'Ariane (capture intacte, juste
un clic mort).

---

## Défauts trouvés

Triés du plus grave au plus bénin. Chaque ligne porte sa preuve image.

| app | section | theme | gravite | ce qui ne va pas | capture |
|-----|---------|-------|---------|------------------|---------|
| clients | IP Vault | warm-paper | bloquant | Les 4 fiches affichent `undefined` comme titre (à la place du titre de la note de session). Données manquantes côté seed ou binding cassé. | `qa/B/clients/warm-paper/05_ip-vault.png` |
| clients | IP Vault | dark-oled | bloquant | Même défaut — `undefined` sur les 4 fiches, persisté quel que soit le thème. | `qa/B/clients/dark-oled/05_ip-vault.png` |
| it-rd | Kernel | warm-paper | visible | Titre `IT Software Kernel` quasi invisible : texte gris foncé sur fond gris foncé. La fenêtre IT/R&D impose son thème "Cyberpunk" (sombre) qui ne suit pas le thème global clair — incohérence avec les autres apps voisines. | `qa/B/it-rd/warm-paper/01_kernel.png` |
| it-rd | Experiments | warm-paper | visible | Titre `Experiments` quasi invisible, même cause (thème Cyberpunk local imposé, ignore `warm-paper`). | `qa/B/it-rd/warm-paper/02_experiments.png` |
| it-rd | Deploys | warm-paper | visible | Titre `Deploys` quasi invisible — `Cyberpunk` local ignore le thème global. | `qa/B/it-rd/warm-paper/03_deploys.png` |
| it-rd | Journal | warm-paper | visible | Titre `Journal` quasi invisible. | `qa/B/it-rd/warm-paper/04_journal.png` |
| it-rd | Boucles | warm-paper | visible | Titre `Boucles` quasi invisible. | `qa/B/it-rd/warm-paper/05_boucles.png` |
| it-rd | Drift | warm-paper | visible | Titre `Drift` quasi invisible. | `qa/B/it-rd/warm-paper/06_drift.png` |
| it-rd | Evals | warm-paper | visible | Titre `Evals` quasi invisible. | `qa/B/it-rd/warm-paper/07_evals.png` |
| it-rd | Kernel | dark-oled | visible | Même famille de titres illisibles (sombre sur sombre). Le thème global `dark-oled` est censé être sombre mais ici c'est juste "encore plus sombre" — l'en-tête de section se confond avec le fond. | `qa/B/it-rd/dark-oled/01_kernel.png` |
| it-rd | Experiments | dark-oled | visible | Titre `Experiments` quasi invisible. | `qa/B/it-rd/dark-oled/02_experiments.png` |
| it-rd | Deploys | dark-oled | visible | Titre `Deploys` quasi invisible. | `qa/B/it-rd/dark-oled/03_deploys.png` |
| it-rd | Journal | dark-oled | visible | Titre `Journal` quasi invisible. | `qa/B/it-rd/dark-oled/04_journal.png` |
| it-rd | Boucles | dark-oled | visible | Titre `Boucles` quasi invisible. | `qa/B/it-rd/dark-oled/05_boucles.png` |
| it-rd | Drift | dark-oled | visible | Titre `Drift` quasi invisible. | `qa/B/it-rd/dark-oled/06_drift.png` |
| it-rd | Evals | dark-oled | visible | Titre `Evals` quasi invisible. | `qa/B/it-rd/dark-oled/07_evals.png` |
| operations | Knowledge Base | warm-paper | visible | Sous chaque fiche : `citations undefined this month`. Champ non lié (probablement `citations` absent du seed). | `qa/B/operations/warm-paper/02_knowledge.png` |
| operations | Knowledge Base | dark-oled | visible | Même défaut — `citations undefined`. | `qa/B/operations/dark-oled/02_knowledge.png` |
| operations | Runbooks | warm-paper | visible | 4 fiches sur 4 ont un titre tronqué : `Client onb…`, `Monthly cl…`. La card coupe avant la fin et le lecteur ne sait pas ce qu'il y a dans la fiche sans cliquer. | `qa/B/operations/warm-paper/01_runbooks.png` |
| operations | Runbooks | dark-oled | visible | Mêmes 4 titres tronqués. | `qa/B/operations/dark-oled/01_runbooks.png` |
| operations | Incidents | warm-paper | visible | 3 titres tronqués : `Egress attemp…`, `Stripe webhook …`, `Backup verified - …`. | `qa/B/operations/warm-paper/03_incidents.png` |
| operations | Incidents | dark-oled | visible | Mêmes 3 titres tronqués. | `qa/B/operations/dark-oled/03_incidents.png` |
| operations | Processus | warm-paper | visible | 6 titres tronqués : `Client onbardi…`, `Monthly close …`, `Session transc…`, `Incident triage - …`, `Calendar sync - …`. Et le champ `outputs:` se résume à `outputs: …` pour toutes les fiches — troncature plus sévère encore. | `qa/B/operations/warm-paper/04_processus.png` |
| operations | Processus | dark-oled | visible | Mêmes troncatures (titres + outputs). | `qa/B/operations/dark-oled/04_processus.png` |
| operations | Benchmarks | warm-paper | visible | 5 titres tronqués sur 6 : `Quiz scoring accur…`, `Multi-tenant RLS is…`, `Stripe webhook ide…`, `Compliance export …`, `Edge function cold s…`. | `qa/B/operations/warm-paper/05_benchmarks.png` |
| operations | Benchmarks | dark-oled | visible | Mêmes 5 titres tronqués. | `qa/B/operations/dark-oled/05_benchmarks.png` |
| operations | Changements | warm-paper | visible | 6 titres tronqués sur 6 : `Add tag-based se…`, `Move Calendly sy…`, `Roll back voice-cl…`, `Auto-promote fla…`, `Disable QuizResu…`, `Bundle Notion Ex…`. | `qa/B/operations/warm-paper/06_changements.png` |
| operations | Changements | dark-oled | visible | Mêmes 6 titres tronqués. | `qa/B/operations/dark-oled/06_changements.png` |
| operations | Alertes | warm-paper | visible | 6 titres tronqués sur 6 : `Edge function col…`, `Stripe webhook r…`, `Unknown user-agent …`, `Memory threshold…`, `Failed to send session …`, `Voice-clone fideli…`. | `qa/B/operations/warm-paper/07_alertes.png` |
| operations | Alertes | dark-oled | visible | Mêmes 6 titres tronqués. | `qa/B/operations/dark-oled/07_alertes.png` |
| clients | Directory | warm-paper | visible | 1 titre tronqué sur 6 : `Atelier Bric…` (= "Atelier Bricolage"). | `qa/B/clients/warm-paper/04_directory.png` |
| clients | Directory | dark-oled | visible | Même troncature `Atelier Bric…`. | `qa/B/clients/dark-oled/04_directory.png` |
| tasks | Definition of Done | warm-paper | visible | 6 titres tronqués sur 6 : `Onboarding to…`, `Stripe webho…`, `Compliance e…`, `Newsletter #2…`, `Voice-clone v…`, `Quarterly rene…`. | `qa/B/tasks/warm-paper/04_definition-of-done.png` |
| tasks | Definition of Done | dark-oled | visible | Mêmes 6 titres tronqués. | `qa/B/tasks/dark-oled/04_definition-of-done.png` |
| tasks | Comparateur | warm-paper | visible | 5 titres tronqués sur 6 : `Onboarding to…`, `Voice-clone v2…`, `Compliance ex…`, `Newsletter #21…`, `RLS isolation …`. | `qa/B/tasks/warm-paper/05_comparateur.png` |
| tasks | Comparateur | dark-oled | visible | Mêmes 5 titres tronqués. | `qa/B/tasks/dark-oled/05_comparateur.png` |
| tasks | Actions exposees | warm-paper | visible | 4 titres tronqués sur 4 : `Newsletter #21…`, `Product chan…`, `Coach Spotligh…`, `Newsletter #22…`. | `qa/B/tasks/warm-paper/06_actions-exposees.png` |
| tasks | Actions exposees | dark-oled | visible | Mêmes 4 titres tronqués. | `qa/B/tasks/dark-oled/06_actions-exposees.png` |

---

## Sections capturées et jugées saines

Ces captures ont été ouvertes et inspectées ; pas de défaut constaté (ou
uniquement des choix de design assumés).

**people** (warm-paper + dark-oled) :
- `01_overview.png`, `02_team.png`, `03_agents.png`, `04_squads.png`,
  `05_content.png`, `06_cadence.png`, `07_culture.png`, `08_personas.png`,
  `09_memoire.png`, `10_codex.png` — toutes OK sur les deux thèmes.

**operations** (warm-paper + dark-oled) :
- `08_context-layer.png` — OK (5 entités : SOP, Runbook, Skill, Routine, Incident).

**it-rd** :
- `08_ontology.png` (warm-paper + dark-oled) — OK, titre rouge lisible sur fond
  sombre, 9 entités visibles.

**clients** (warm-paper + dark-oled) :
- `01_active.png`, `02_onboarding.png`, `03_churn-risk.png` — OK.

**tasks** (warm-paper + dark-oled) :
- `01_today.png`, `02_upcoming.png`, `03_done.png` — OK (vide assumé sur
  `done` : "No completed tasks yet.").

---

## Ce que je n'ai pas pu tester, et pourquoi

- **Capture default (Overview / Today / etc.)** : le sélecteur du `tools/shot.mjs`
  matche le bouton désactivé du fil d'Ariane (où le segment actif est rendu
  avec `disabled`) au lieu du bouton de la sidebar. Pour l'Overview, qui est la
  section par défaut, j'ai laissé `--section` vide et la capture montre bien la
  première section. Pour les sections suivantes, j'ai contourné via un wrapper
  Playwright (`/tmp/qa-shot.mjs`) qui clique le bouton de la `aside` filtré sur
  le libellé exact. Je n'ai pas modifié le dépôt.

- **Fenetre redimensionnée** : les captures sont en 1440×900. Les troncatures
  observées (cartes operations/clients/tasks) varient probablement avec la
  largeur ; je n'ai pas exploré les fenêtres étroites où les coupures sont
  pires.

- **Erreurs de console** : aucune erreur de console n'a été signalée par
  `tools/shot.mjs` (qui ne sort que les 10 premières) ni par mon wrapper. Je
  n'ai pas non plus constaté de tour bloqué ou d'écran blanc au chargement —
  les 74 captures ont toutes abouti.

- **Interactions mortes** : je n'ai pas cliqué manuellement sur les cartes
  (drill-down, onClick). C'est un audit statique de rendu, pas un test
  fonctionnel. Une carte qui semble cliquable et qui ne l'est pas serait un
  défaut non-détecté ici.

- **Statut per-app des thèmes** : pour `it-rd` j'ai noté que la fenêtre reste
  en thème "Cyberpunk" (sombre) sous `warm-paper` ET sous `dark-oled`. Je ne
  sais pas si c'est un bug ou un choix ("IT/R&D toujours sombre, peut-importe
  le thème global"). Le brief me dit de signaler les incohérences, pas
  l'intention. Je signale.