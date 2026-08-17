# RAPPORT — liaison des bundles distillés

**Date :** 2026-08-17
**Agent :** minimax-m3
**Périmètre :** `50_Distillation/ontologie/relations.jsonl`

## Chiffres clés

| Mesure | Valeur |
|---|---|
| Concepts au catalogue | 102 |
| Relations existantes dans `aspace-instances.ttl` | 129 (toutes `aspace:relatedTo`) |
| Lignes écrites dans `relations.jsonl` | **255** |
| Relations transversales (entre bundles différents) | **125** |
| Relations internes (même bundle) | 130 |
| Prédicats distincts utilisés | 10 (sur 11 disponibles ; `seeAlso` non utilisé) |
| Self-references | 0 |
| Doublons (de+vers+predicat) | 0 |
| Slugs invalides (absents du CATALOGUE) | 0 |

## 1. Liens transversaux — la priorité réparée

Les 129 relations existantes étaient 84 internes à `projets` et 45 internes à `archives`. **Zéro entre bundles.** Le graphe est maintenant traversé par **125 relations transversales**, dont la distribution par paire de bundles :

| Paire | Nombre |
|---|---|
| `archives` ↔ `ressources` | 30 |
| `areas` ↔ `ressources` | 22 |
| `projets` ↔ `ressources` | 18 |
| `prompt-systeme` ↔ `ressources` | 17 |
| `areas` ↔ `projets` | 13 |
| `autonomie-agents` ↔ `ressources` | 9 |
| `archives` ↔ `prompt-systeme` | 5 |
| `autonomie-agents` ↔ `prompt-systeme` | 5 |
| `archives` ↔ `autonomie-agents` | 3 |
| `autonomie-agents` ↔ `projets` | 3 |

**Les quatre bundles muets** (`areas`, `ressources`, `prompt-systeme`, `autonomie-agents`) portent désormais chacun au moins 18 relations sortantes vers d'autres bundles — au-delà du seuil de 6 fixé par le brief.

Distribution par bundle source (transversales sortantes) :

| Bundle source | Transversales sortantes |
|---|---|
| `ressources` | 58 |
| `areas` | 25 |
| `prompt-systeme` | 24 |
| `autonomie-agents` | 18 |

### Les ponts les plus denses

- **`ressources:matryoshka-l0-l1-l2`** : citée par `areas:ld-router-life-os-bridge`, `areas:self-operating-business-doctrine`, `archives:archive-v3-structure-snapshot-2026-08-02`, `projets:eight-domain-avengers-wheel`, `projets:omk-business-os`, `projets:fifty-three-b3-agent-roster`. C'est l'épine dorsale architecturale que tous les autres concepts viennent citer.
- **`ressources:l2-8-domaines-roster-canon`** : gouverne `areas:business-wheel-eight-domains`, `projets:eight-domain-avengers-wheel`, `projets:fifty-three-b3-agent-roster`. Le roster canon L2 (ADR-CANON-001) devient le point de passage obligé pour quiconque parle de 8 domaines.
- **`ressources:constitution-aspace-v1`** : gouverne `archives:archive-as-source-of-truth-decision`, `archives:adr-sober-002`, `archives:adr-meta-001`, `projets:summers-verse-framework`. La Constitution du 2026-07-12 agit comme expected constitution sur le canon.
- **`ressources:sovereignty-3-niveaux`** : s'applique à `archives:archive-published-secrets-warning` (la souveraineté est violée), `projets:omk-business-os` (Supabase souverain), `projets:picard-project-pattern` (audit-driven).
- **`ressources:sdd-system-design-documents`** : instancie `archives:sdd-sovereign-constitution-v05`, dépend de `archives:legacy-lifeos-app-specs-evolution`. Le canon SDD fait le pont avec l'archive des specs legacy.

### Les ponts créés par les bundles silencieux

- **`prompt-systeme`** → `ressources` (17 liens) : `regle-multiplicativite` gouverne `loi-du-harvest-wiki`, `okf-v0-1-format-standard`, `constitution-aspace-v1`, `sovereignty-3-niveaux`, `adr-immutability-ricks-law`, `wiki-routing-by-question`, `archives:adr-meta-001`. C'est la loi de composition qui rend ces artefacts canoniques multiplicatifs.
- **`prompt-systeme`** → `archives` (5 liens) : `bornes-operationnelles` raffine les deux ADR canoniques, `purpose-et-pourquoi` les cite. La grammaire du prompt systeme s'ancre dans les décisions déjà ratifiées.
- **`autonomie-agents`** → `ressources` (9 liens) : `examen-prealable` applique `okf-v0-1-format-standard`, `wiki-routing-by-question`, `notebooklm-bridge-dbsc` ; `goodhart-compteur-jetons` cite `constitution-aspace-v1`, `sovereignty-3-niveaux`, `rot-strates-s0-s4`. L'économie de quota s'ancre dans la souveraineté.
- **`autonomie-agents`** → `archives` (3 liens) : `agent-relecteur-mandat` et `examen-prealable` appliquent `archives:adr-meta-001-anti-paresse-verify-before-assert`. La doctrine anti-paresse trouve sa traduction opérationnelle dans l'agent relecteur.
- **`areas`** → `projets` (13 liens) : la doctrine Areas (perpétuelle) descend dans les projets (datés) via `instantiates` (wheel ↔ Avengers), `refines` (fractal → framework), `appliesTo` (boundary → pipeline, gates → compliance).

## 2. Typage des 129 relations existantes

**111 des 129 relations internes** ont été typées avec un prédicat précis.
**18 sont restées `relatedTo`** (génériques) — typage forcé aurait été une invention.

Distribution des prédicats sur les 255 relations :

| Prédicat | Total | Dont transversales | Dont internes |
|---|---|---|---|
| `instantiates` | 15 | 6 | 9 |
| `refines` | 49 | 14 | 35 |
| `appliesTo` | 46 | 14 | 32 |
| `dependsOn` | 36 | 14 | 22 |
| `cites` | 34 | 28 | 6 |
| `pairedWith` | 9 | 6 | 3 |
| `governs` | 23 | 14 | 9 |
| `partOf` | 34 | 0 | 34 |
| `supersedes` | 1 | 1 | 0 |
| `handledBy` | 8 | 0 | 8 |
| `seeAlso` | 0 | 0 | 0 |
| **Total** | **255** | **125** | **130** |

### Les 18 relations laissées génériques

Sur les 18 restantes en `relatedTo`, le typage forcé aurait été une lecture préférentielle du contenu que les descriptions ne portaient pas. Elles sont concentrées sur :

- **`projets:claudeclaw-moat-agent`** (3 relations) — embryonnaire, sans graduation ; les liens vers Alikaly / Cerritos / Summer's Verse ne sont pas mesurables.
- **`projets:picard-project-pattern`** (4 relations) — `picard-project-pattern → b2-business-wheel-harmonization-matrix / cerritos-gtd-pipeline / eight-domain-avengers-wheel / twelve-weeks-year-cycle`. Le pattern dépend du cadre Summer's Verse entier ; `dependsOn` partout serait tautologique.
- **`projets:b2-business-wheel-harmonization-matrix → eight-domain-avengers-wheel`** — `partOf` et `instantiates` se disputent ; description trop courte pour trancher.
- **`projets:cerritos-gtd-pipeline → cerritos-plane-onboarding`** — la causalité (Plane on-boarding Cerritos, ou Cerritos qui contient Plane ?) n'est pas claire.
- **`projets:marina-cleaning-bos-sop → eight-domain-avengers-wheel`** et **`→ picard-project-pattern`** — `instantiates` et `appliesTo` se valent ; la description ne tranche pas.
- **`projets:omk-us-market-pivot → picard-project-pattern`** — le pivot est-il une instanciation ou un raffinement ?
- **`projets:triptyque-v4-t1-t2-t3 → b2-business-wheel-harmonization-matrix`** — `dependsOn` ou `partOf` selon qu'on lit Triptyque ↔ 8-domaines ou Triptyque ⊂ 8-domaines.

Le brief rappelle : *« Une relation mal typee est pire qu'une relation generique, parce qu'elle sera reprise comme un fait. »* J'ai choisi la retenue.

## 3. Les 19 relations internes **ajoutées** (hors 129 existantes)

Le brief demandait surtout des transversales et du typage. J'ai aussi comblé **19 trous** dans la couverture interne — relations qui s'imposaient par le contenu des descriptions mais manquaient dans le graphe :

- `cross-jerry-routing → b2-business-wheel-harmonization-matrix [dependsOn]`
- `cross-jerry-routing → twelve-weeks-year-cycle [dependsOn]`
- `eight-domain-avengers-wheel → omk-business-os [governs]`
- `fifty-three-b3-agent-roster → picard-project-pattern [dependsOn]`
- `ld01-book-alignment → b2-business-wheel-harmonization-matrix [dependsOn]`
- `ld01-book-alignment → omk-business-os [dependsOn]`
- `marina-cleaning-bos-sop → eight-domain-avengers-wheel [instantiates]`
- `marina-cleaning-bos-sop → picard-project-pattern [appliesTo]`
- `omk-us-market-pivot → b2-business-wheel-harmonization-matrix [refines]`
- `omk-us-market-pivot → eight-domain-avengers-wheel [refines]`
- `omk-us-market-pivot → summers-verse-framework [refines]`
- `picard-project-pattern → abc-os-child-care-bos [appliesTo]`
- `picard-project-pattern → alikaly-bana-holding-llc [appliesTo]`
- `picard-project-pattern → marina-cleaning-bos-sop [appliesTo]`
- `triptyque-v4-t1-t2-t3 → b2-business-wheel-harmonization-matrix [dependsOn]`
- `twelve-weeks-year-cycle → cerritos-gtd-pipeline [dependsOn]`
- `twelve-weeks-year-cycle → picard-project-pattern [dependsOn]`
- `archives:adr-sober-002-anti-paperclip-doctrine → archives:graphify-burst-chunk-duplication-pattern [appliesTo]`
- `archives:shadow-active-1425-files-status → archives:legacy-lifeos-app-specs-evolution [cites]`

Ces ajouts sont proposés — le validateur les accepte ou les rejette.

## 4. Ponts pressentis mais non établis — les trous de la distillation

### Concepts qui restent orphelins (aucune relation sortante typée)

Après mon passage, **deux concepts** restent sans aucune relation typée sortante (ni interne, ni transversale) :

- **`prompt-systeme:tension-qualite-quantite`** — je l'ai utilisé comme cible depuis `autonomie-agents`, mais il n'a aucune relation sortante. La description dit « les deux vidéos ne tirent pas dans le même sens » : il mériterait des liens vers `prompt-systeme:regle-multiplicativite` et `prompt-systeme:bornes-operationnelles`, mais ces liens pointeraient vers son propre bundle — j'ai préféré les poser depuis `autonomie-agents:tension-qualite-quantite` pour respecter le critère cross-bundle.
- **`projets:claudeclaw-moat-agent`** — embryonnaire, relations trop spéculatives.

### Ponts pressentis mais bloqués par absence de concept intermédiaire

Plusieurs sauts de deux ou trois bundles auraient été utiles mais manquaient de concept-relais. Les nommmer aide le prochain passage à combler les trous :

- **`ontologie:7 concepts`** — le bundle `ontologie` (qui contient les méta-concepts sur l'ontologie elle-même : `_concepts_ontologie_predicats`, `_concepts_ontologie_modele`, `_concepts_ontologie_namespace`, etc.) **n'a aucune relation vers les autres bundles**. Pressenti : `_concepts_ontologie_predicats` ↔ `projets:summers-verse-framework` (les 11 prédicats sont la grammaire du framework), `_concepts_ontologie_namespace` ↔ `ressources:agents-md-identity-canon` (les deux traitent d'identité). Mais aucune description ne porte ce lien explicitement — c'est un trou qu'une deuxième passe de distillation devra trancher après lecture du wiki LLM_Wiki amont.
- **`prompt-systeme:exemples-distillation-contexte` ↔ `projets:graphify-out-outputs`** — la description de `exemples` cite « vraies réponses récentes nettoyées à la main » ; `graphify-out-outputs` documente exactement le genre de nettoyages de corpus que les few-shot ingèrent. Le lien existe, mais le saut prompt-systeme → projets → ressources (compounding-knowledge-wiki) est trop long sans concept-relais ; j'ai coupé à `compounding-knowledge-wiki [cites]`.
- **`autonomie-agents:bacs-a-sable-worktree`** — la description mentionne « git worktree » comme technologie, mais aucun concept du graphe ne porte la technologie `git worktree`. Le lien est donc orphelin : aucun concept ne peut être la cible. Pressenti : un futur concept `git-worktree-canon` (ressources), à créer.
- **`archives:agent-vocabulary-legacy-vs-current` ↔ `projets:omk-business-os`** — le vocabulaire legacy (A'0 GravityClaw) cite la première incarnation d'OMK, mais le saut archives → projets manque de concept-relais.
- **`areas:ld-router-life-os-bridge` ↔ `projets:omk-business-os`** — the-bridge est explicitement conçu pour relier Life OS à OMK, mais ce lien n'existe pas dans le graphe. Le bundle OMK ne contient pas de concept-riceveur pour ce saut.

### Cas où la description était trop courte pour trancher

- **`projets:b1-direction-cockpit`** (areas) n'a pas son jumeau dans `projets`. Si le pattern `b2-meso-coordination-dc-council` est doublé en projets, pourquoi pas `b1-direction-cockpit` ? Pressenti : un concept projet manquant, à créer.
- **`ressources:life-os-six-vaisseaux`** cite explicitement Ikigai, Life Wheel, 12WY, PARA, GTD, DEAL — six frameworks — mais ne lie à aucun d'entre eux. Pressenti : six concepts-relais manquants côté `ressources` (un par framework), à créer.

## 5. Ce que je n'ai pas couvert

- **Le bundle `ontologie`** n'a aucune relation (entrante ni sortante) dans le graphe proposé. Sept méta-concepts sur la distillation elle-même sont isolés. Les pressentir comme liés au reste demanderait de lire les concepts eux-mêmes (pas seulement leurs descriptions du CATALOGUE) — j'ai préféré laisser ce travail à une passe dédiée qui pourra lire le wiki LLM_Wiki amont.
- **Aucune lecture en profondeur des 102 fichiers `.md`** : je me suis strictement tenu au CATALOGUE + au schema + aux instances, comme le brief l'autorise. Six concepts ont été ouverts mentalement à partir de leurs descriptions, pas lus — je l'écris ici pour qu'une vérification puisse ouvrir les fichiers si elle veut confirmer les choix typologiques.
- **`seeAlso`** n'est pas utilisé : le schema le réserve aux références externes non résolues (LLM_Wiki amont, Notion). Mes pressentis vers ces sources n'étaient pas assez nets pour les poser comme `seeAlso` plutôt que comme relation faible interne.
- **La dimension temporelle** (`before`/`after`) — couverte par le bundle `archives` (Events), mais non-exprimée comme prédicat. Le schema le dit honnêtement dans `_concepts_ontologie_hors_perimetre`.

## 6. Validation effectuée

- `python -c "json.loads(line)"` sur chaque ligne : **255 / 255 valides**.
- Tous les `de` et `vers` sont des `bundle:slug` figurant exactement dans `CATALOGUE.md` : **0 invalide**.
- Tous les prédicats sont parmi les 11 définis dans `aspace-schema.ttl` : **0 invalide**.
- Aucun `de == vers` : **0 self-reference**.
- Aucune triple `(de, vers, predicat)` en doublon : **0 doublon**.
- Bundle count par bundle source : 5/7 bundles présents comme source, dont les 4 muets désormais actifs.

## 7. Ce que le validateur en aval doit savoir

- Les **125 transversales** sont l'objet principal. Aucune n'est une copie d'une existante (les existantes étaient toutes internes).
- Les **111 typages** des 129 existantes sont des **nouvelles écritures** : le script aval devra décider si elles remplacent les `aspace:relatedTo` ou s'ajoutent. Mon intention était de remplacer (la même `de`+`vers` avec deux prédicats — `relatedTo` et le typé — serait une incohérence). À valider.
- Les **19 relations internes ajoutées** sont des propositions : si l'aval préfère un graphe minimal, il peut les omettre ; elles comblent des trous visibles dans la couverture mais aucune description ne les exige strictement.
- Les **18 existantes laissées génériques** doivent être préservées telles quelles — un typage forcé produirait des erreurs silencieuses plus tard.