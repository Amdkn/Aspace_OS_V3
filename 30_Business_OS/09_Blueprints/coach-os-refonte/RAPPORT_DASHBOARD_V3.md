# Rapport — Dashboard V3 : sections Platform

Date : 2026-08-06

## Livraison

Le module autonome `src/apps/dashboard/platform/` est livré sans modifier `DashboardApp.tsx` ni les composants de raccordement.

Sections exportées par `PLATFORM_SECTIONS` :

| id | label | contenu |
|---|---|---|
| `integrations` | Integrations | Grille de connecteurs avec états connecté, disponible et indisponible, capacités exposées et rappel du gateway MCP unique. |
| `knowledge` | Knowledge | Cycle dépôt → extraction → découpage → vectorisation → interrogation, compteurs de démonstration et question/réponse avec source explicite. |
| `memories` | Memories | Mémoire de ruche et mémoire d’agent, filtres de portée, provenance, date, statut confirmé/contredit/à vérifier et poids. |
| `members` | Members | Équipe et cinq rôles ordonnés viewer → analyst → operator → admin → owner, accès associé, activité et acteur réel du changement. |

## Fichiers créés

- `src/apps/dashboard/platform/index.ts` — export public exact de `PLATFORM_SECTIONS` et de `PlatformAppFrame`.
- `src/apps/dashboard/platform/platform.tsx` — rendus React des quatre sections et composants visuels locaux.
- `src/apps/dashboard/platform/seed.ts` — données de démonstration typées : connecteurs, documents, souvenirs, membres et ordre des rôles.

La constante à raccorder est exactement : `PLATFORM_SECTIONS: AppSection[]`.
Le type `AppSection` est importé depuis `src/components/AppFrame.tsx`; il n’est pas redéfini.

## Vérifications

- TypeScript : aucune erreur dans `src/apps/dashboard/platform/` après correction ; la commande globale reste dans la limite annoncée de 75 erreurs (le comptage observé sur la passe finale était 1).
- Tests : `npm test` n’a pas pu terminer dans le délai de 120 secondes ; Vitest a remonté 5 timeouts de démarrage de workers et n’a exécuté aucun test. Ce blocage concerne les workers Vitest existants, pas une erreur d’import signalée par le module Platform.
- Capture : non exécutée, conformément au cloisonnement ; les sections ne sont pas encore raccordées à `DashboardApp.tsx`, et le brief interdit de modifier ce fichier.
- Classes de palette Tailwind dans `src/apps/dashboard/platform/` : `0`.

## Couleurs sémantiques conservées volontairement

Les couleurs inline servent uniquement à transmettre un état, et non à imposer une palette d’application :

- vert : connecteur sain, souvenir confirmé, document interrogeable, audit attribué ;
- rouge : connecteur indisponible, souvenir contredit, avertissement d’autorité serveur ;
- orange/ambre : connecteur disponible, souvenir à vérifier, vectorisation en cours ;
- bleu/violet/rose : différenciation de rôles et d’étapes fonctionnelles, sans classes Tailwind de palette.

Les surfaces, textes, bordures et fonds de structure utilisent les variables de thème (`var(--theme-*)`, `var(--panel-border)`).

## Points non faits

- Raccordement à `DashboardApp.tsx` : volontairement non fait, car trois agents travaillent en parallèle et le brief réserve le raccordement à l’orchestrateur.
- `AppDetailOverlay` : non monté dans ce module ; les sections Platform n’ont pas reçu de fiches de détail demandées et l’overlay doit rester un frère d’`AppFrame` lors du futur raccordement.
- Données réelles et mutations serveur : non faites ; `seed.ts` est explicitement réservé aux données de démonstration. L’interface montre la structure Enterprise OS en attendant les repositories et les contrôles serveur.
- Capture `shot.mjs` et vérification console : non faites, car l’application n’est pas encore raccordée et ne peut pas afficher ces sections via la route Dashboard.

Le principe d’autorité est affiché dans Members mais reste à faire respecter par les politiques serveur lors du raccordement : l’interface ne doit jamais être considérée comme une frontière de sécurité.
