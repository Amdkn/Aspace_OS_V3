# SUCCESS-ASPACE.md · définition du « proprement wargamé » (12 points)

Un wargame passe seulement si les DOUZE tiennent.

## Les 8 du kit (Fable Wargame Kit, Geordi 02_Templates)

1. Chaque move énonce son observation attendue — exactement ce qu'on doit voir si ça a marché.
2. Chaque move porte son échec le plus probable, la cause que cet échec signale, et la contre-action.
3. Chaque fork a un trigger. « Si tu observes X, prends la route B. » Zéro judgment call laissé à l'exécuteur.
4. Toute assomption non résolue par le recon est marquée RECON NEEDED avec le check exact qui la résout.
5. Les abort conditions existent — les moments où on s'arrête et on flag au lieu d'improviser.
6. La vérification est épelée : quels runs l'exécuteur fait, quand, et à quoi ressemble le « pass » de chacun.
7. Il a survécu à une passe red-team. Le doc enregistre l'attaque qui a échoué contre lui, et le patch né de celle qui n'a pas échoué.
8. Il est exécutable à l'aveugle. Un modèle mid-tier court la mission bout-en-bout sans poser une seule question.

## Les 4 A'Space (ADR-META-001 + canon)

9. **D1 receipts** : chaque claim du wargame sur l'état du système pointe un fichier/commande vérifiable. Pas de « je suppose que le canon dit ».
10. **Append-only** : aucun move ne réécrit un ADR RATIFIED, un intouchable (A3_Book_LD01_Spec, BIBLIOGRAPHY, README), ni ne hard-delete (→ _TRASH).
11. **Mapping canon exact** : WF0/1/2 = strates, WK01-13 = semaines 12WY. Les 8 domaines Business ≠ tags LDxx (tous sous LD01). Roster ADR-CANON-001, jamais de nom inventé.
12. **Beth-compat** : aucun move ne touche vie/santé A+ (seul veto, ADR-WARMODE-002). Un wargame qui exige des nuits blanches d'A+ = FAIL au point 12.
