---
type: Bundle index
title: operations — playbooks et gestes de remise en route
description: Sous-bundle en attente de sa première page. Il portera les procédures répétables : redémarrages, migrations, vérifications.
tags: [okf, operations, index]
generated: { by: claude-opus-5, at: 2026-08-17T15:10:00Z }
okf_version: "0.2"
---

Ce sous-bundle porte les **procédures répétables** : redémarrer un service,
appliquer une migration, vérifier qu'un jeton est encore vivant.

Un playbook utile dit aussi **comment on sait que ça a marché**. Une procédure
qui se termine sans critère de succès se rejoue à l'aveugle, et c'est ainsi
qu'un `exit 0` trompeur passe pour une réussite.

# Files

- [Le prototype de franchise reproductible](franchise-ownerbooks-runbooks.md) - Comment `01-omk-business-os` sert de gabarit aux 4 autres projets Picard. La seule variable sourcee est le `Mode` (Nexus/Orbiter), lu dans des litteraux PowerShell non interpoles des North Star. Les recus D1 du prototype ne se recopient pas : 30 documents ecrits, dont 24 en `A SOURCER` assume.
- [Rendre WSL persistant et auto-réparant](wsl-gardien-persistance.md) - La distro tombe en `0x8007274c` — affichée `Running`, injoignable — et tue la session Ori en cours. Un gardien détaché par le planificateur de tâches la relève seul en 45 secondes, mesuré. Contient les deux pièges payés : un daemon lancé depuis un agent meurt avec l'arbre de processus de l'outil, et un `.ps1` contenant un tiret cadratin casse le parseur PowerShell 5.1 des dizaines de lignes plus bas.
- [Vérifier l'intégrité du corpus OKF](verifier-integrite-corpus-okf.md) - Un script mesure ce que le canon confiait à la vigilance : 78 liens morts sur 2728, 14 frontmatter incomplets, et la répartition réelle de la confiance (46 revus par un humain, 582 par machine). Le corpus lie par **préfixe** de slug, pas par slug exact — un test d'égalité stricte déclarait 90 morts dont la plupart résolvaient. Contient les quatre pièges d'instrument payés pour que le rapport ne mente pas.
- [Vague de revue Sonnet 5 — 7 domaines, 230 concepts](vague-revue-sonnet-7-domaines.md) - Couverture intégrale sur les sept, 53 accepter / 164 réserver / 13 rejeter, 7 points de forfait pour 98 concepts. Quatre affirmations restituées par la synthèse externe comme des faits ne tiennent pas : le barème d'affiliation 50/150/250 $ n'existe nulle part dans le corpus, `NON_FORCED` est reconstruit, les trajectoires Green Lantern sont l'œuvre d'un seul auteur, Thunderbolts n'a aucune preuve d'exécution.
- [NotebookLM en assistance de revue humaine](notebooklm-revue-humaine.md) - Quand la production n'est plus le goulot : 423 fichiers produits en une nuit, aucun relu. Regroupement en 26 sources chargeables, et la règle qui ne se délègue pas — rien ne passe de `machine` à `humain` sans le propriétaire du produit.
- [Fenêtres qui clignotent — onze hooks Orca morts](hooks-orca-morts-fenetres-clignotantes.md) - Quatre hooks en `matcher: "*"` lançaient `powershell.exe` puis `cmd.exe` à chaque appel d'outil, ouvrant un onglet Windows Terminal à chaque fois, pour un script qui sortait à sa première condition — toutes les variables Orca étaient vides. Le chemin est caché dans un `-EncodedCommand` base64, donc invisible à une recherche de texte. Contient aussi le piège `Path.home()` qui ignore `HOME` sous Windows et a fait éditer le vrai fichier à un test censé être isolé.
- [Une 404 de Vercel n'est pas une 404 de l'app](vercel-repli-spa-404.md) - Sans règle de repli dans `vercel.json`, tout chemin profond d'une SPA rend le 404 de la plateforme avant que le code ne s'exécute. C'est ce qui bloquait la connexion Google de Coach OS, après que le `redirect_uri_mismatch` de Google eut été corrigé. Contient le geste de vérification à trois chemins.
- [Relance spec-loop — diagnostic et remise en route](relance-spec-loop-2026-08-30.md) - Cinq causes imbriquées de l'arrêt de la cadence 1 m : abonnement MiniMax expiré (429 sans alerte), clé déplacée vers `_secrets_local` que les scripts ne suivaient pas, CLI 2.1.250 qui refuse tout modèle personnalisé côté client, dépôt coach-os éventré, aucun superviseur de superviseur. Correctifs : canal `claude-glm.cmd` avec les deux drapeaux MCP obligatoires, exports MiniMax supprimés (contamination des sous-processus), cadence 1 repointée vers V3, skill réinstallée via `npx skills add -y -g`. Vérifié par PONG + premier tour Beth (exit 0, `agents_en_derive = 0`).
