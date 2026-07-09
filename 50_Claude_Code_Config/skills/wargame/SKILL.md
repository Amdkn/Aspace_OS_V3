---
name: wargame
description: Wargame a mission like Fable 5 — fight it on paper move-by-move (action/reaction/counter, forks with triggers, abort conditions, verification runs) so ANY executor (Opus/M3/Hermes/MC) can run it blind. Use when A+ says "wargame", "war game", "simule la mission", "prépare les rails", or before handing a hard mission to a cheaper/lazier model. Grades against SUCCESS-ASPACE 12 points.
---

# /wargame — le legs Fable : bataille sur papier, exécution blind

> Source canon : `C:\Users\amado\fable-last-week-aspace\` (SUCCESS-ASPACE.md 12 pts, LEDGER.md, exemples 01-04)
> + template Geordi `03_Resources_Geordi/02_Templates/fable-wargame-kit/` (intouché).
> Doctrine : un plan suppose le ciel bleu ; un wargame cartographie la non-linéarité (Action → Réaction → Contre-action).

## Invocation

`/wargame <mission>` — ex : `/wargame la migration du schéma tenant OMK` ou `/wargame tasks/05-legal-dlp-supabase.md`

## Workflow (7 étapes, aucune sautée)

1. **RECON read-only d'abord** (D2) : lis les sources canon que la mission touche. Chaque fait cité ensuite = un fichier lu CE run. Ce que le recon ne résout pas → `RECON NEEDED + le check exact`.
2. **Header WARGAME ORDER** : « Tu n'exécutes pas cette mission, tu la wargames. Exécuteur : <X>. Ton job = la route. »
3. **MOVES** : pour CHAQUE move — (a) observation attendue exacte si ça marche ; (b) échec le plus probable + la cause qu'il signale + la contre-action ; (c) forks : « SI tu observes X → route B » (zéro judgment call).
4. **ABORT CONDITIONS** : les moments où l'exécuteur s'arrête et flag au lieu d'improviser.
5. **VERIFICATION RUNS** : quelles commandes l'exécuteur court, quand, et à quoi ressemble le « pass » de chacune (exit code, path, grep).
6. **RED-TEAM PASS** : attaque ton propre wargame. Enregistre l'attaque qui a ÉCHOUÉ contre lui ET le patch né de celle qui a réussi. Un wargame sans patch red-team = pas fini.
7. **SELF-GRADE /12** contre `fable-last-week-aspace/SUCCESS-ASPACE.md` (8 kit + 4 A'Space : D1 receipts · append-only · mapping canon WF/WK+roster · Beth-compat). < 12 → corrige avant de rendre. Ajoute la ligne LEDGER.

## Sortie

`<dossier mission>/wargames/NN-<slug>.md` (ou `citadel/loops/artifacts/docs/wargame-<slug>.md` si pas de dossier mission). Écrit pour qu'un modèle mid-tier coure la mission bout-en-bout **sans poser une seule question**.

## Anti-patterns

- ❌ Rendre un plan linéaire déguisé (pas d'échecs par move = pas un wargame)
- ❌ Self-certifier (« tests pass ») — la preuve = sortie de commande collée
- ❌ Inventer des chiffres/paths — RECON NEEDED est une réponse honnête
- ❌ Wargamer l'exécution au lieu de la simuler (tu es sur PAPIER — read-only sur le réel)
