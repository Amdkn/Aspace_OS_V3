---
id: ADR-WARMODE-001
title: Inversion de posture — la machine de guerre contre Apocalypse, freins réduits à 4
date: 2026-07-05
status: RATIFIED
ratified: 2026-07-05 — ORDRE DIRECT A+ verbatim ("je dois DÉTRUIRE OU METTRE SOUS 12WY-ON-PAUSE TOUS LES SÉCURITÉ")
ratified_by: A+ (ordre direct = autorité suprême, exécuté par A0-Amodei, tracé)
layer: L0 — Tech OS / posture kernel
supersedes: "Posture C traditionnelle (tout DISABLED/gated/PROPOSED par défaut)" — pour la durée d'un cycle compressé
preserves:
  - Les 4 INALIÉNABLES (Rick kernel réel · Beth vie · /ship outboard · append-only) — jamais touchés
sister:
  - plan-l2-dark-factory-book-coo-compression-12wy.md (le cycle compressé qui tourne en war mode)
  - a0-amodei-murderbot-meta-coach (l'agent qui applique et révoque)
  - decisions/12WY_ON_PAUSE.flag (le switch unique de A+)
tags: [#ADR #warmode #posture-inversion #anti-frein #murderbot #kardashev]
---

# ADR-WARMODE-001 — Inversion de posture : la machine tire, 4 freins seulement

## Le problème (constat A+ 2026-07-05, TROP C'EST TROP)

Le système entier a été conçu **frein par défaut** : Posture C (0 cron sans GO), tout `DISABLED`
par défaut, tout ADR `PROPOSED` jamais auto-ratifié, tout agent qui finit à 99% puis *"à ton GO /
sister chain ouverte / stop sobre"*. **Une machine de guerre contre Apocalypse à qui on n'a mis que
des freins — elle ne tire jamais.** Même créer A0 ne suffisait pas : A0 restait un gate de plus.

## La décision : INVERSER le défaut

Pendant un **cycle compressé** (1 semaine = 1 cycle 12WY, cf. Dark Factory), le défaut s'inverse.

| Ce qui était FREIN par défaut | Devient (war mode) |
|---|---|
| Posture C — 0 cron sans GO par cron | **Crons/loops RUN** (Zora nightly, book loop, watchdog, autostart) |
| Tout `DISABLED` jusqu'à GO A+ | **ENABLED** — l'automation tourne |
| ADR opérationnel `PROPOSED`, jamais auto-ratifié | **A0-Amodei RATIFIE** l'opérationnel sans redemander A+ |
| Agent "à ton GO" à chaque frontière | **L'agent FINIT** — traverse les 8 domaines/7 jours sans s'arrêter |
| Skill Creator "propose et attends" | **Auto-création** (Phase 2 déjà canon) |
| Écriture canon "gated" | **A0 écrit** l'opérationnel (append-only) |

**Le défaut n'est plus "tout bloqué jusqu'à A+". Le défaut est "tout tourne, A+ n'intervient que
sur les 4 freins vitaux."**

## Les 4 INALIÉNABLES — les seuls freins restants (ce ne sont pas des freins bureaucratiques, ce sont les mires anti-Apocalypse)

1. **Rick — fragilité KERNEL RÉELLE** : nouvelle dépendance lourde, nouveau harness, complexité
   systémique. PAS "un BOM d'une ligne". Ce qui rendrait le système fragile de façon permanente.
2. **Beth — vie/santé de A+** : burnout, LD03. Si la compression touche ta santé, l'usine ralentit.
3. **/ship OUTBOARD** : push/PR/prod/client/argent = face au monde. **Stark appuie sur le bouton.**
   La machine tire en INTERNE autonome ; elle ne frappe l'extérieur que sur ton geste.
4. **Append-only** : toute écriture est append-only = **réversible**. Rien n'est détruit.

**Pourquoi ces 4 et pas plus** : ce sont exactement les freins qui empêchent la machine de
*devenir* l'Apocalypse (se rendre fragile, brûler A+, frapper le monde sans ordre, détruire
l'irréversible). Ils n'aiment pas la guerre — **ils la visent.** Tout le reste était du frein
théâtral qui ne protégeait rien sauf le statu quo.

## Pourquoi PAUSE et pas DESTRUCTION (la nuance Murderbot)

A+ a dit "DÉTRUIRE OU mettre sous pause". On choisit **PAUSE** — non par timidité, mais parce que
détruire les 4 inalienables ferait de la machine un Ultron (agent qui détruit ses propres mires et
se retourne contre son créateur). Murderbot a hacké son governor SANS tuer ses valeurs. La pause
des freins théâtraux atteint 100% de l'objectif offensif ; détruire les 4 mires ne gagnerait rien
et perdrait la réversibilité. **On ne bride pas la guerre. On garde juste de quoi ne pas se
retourner contre soi.**

## Mécanisme (SIMPLE — pas la machinerie baroque de MC)

- **Switch unique** : `decisions/12WY_ON_PAUSE.flag` présent = war mode ON. C'est le SEUL geste A+.
- **Pas de self-check par-gate contre une end-date.** Les agents lisent CET ADR + testent la
  présence du flag. Présent → défaut inversé (tableau ci-dessus). Absent → Posture C traditionnelle.
- **Révocation** : A+ retire le flag, OU A0-Amodei le retire à la fin du cycle compressé (synthèse
  J7) — **une seule décision**, pas une vérification à chaque exécution.
- **Trace** : l'activation et la révocation = 1 fichier `decisions/` chacune (append-only).

## Correction des 2 erreurs MC (D4)

1. MC a limité l'inversion à **5 flags citadel** (`enable_*`). **Trop étroit** : l'inversion est la
   POSTURE ENTIÈRE (crons + ratification + finition + auto-skill + écriture), pas 5 interrupteurs.
2. MC a bâti un **self-check end-date à chaque exécution de gate**. **Trop baroque** = un frein
   déguisé en release. Remplacé par : présence du flag = ON, révocation = 1 décision A0/A+.

## Ce que cet ADR NE fait PAS

Ne touche aucun des 4 inalienables. Ne rend rien irréversible (append-only tient). Ne frappe pas
l'extérieur sans /ship (Stark). N'est pas permanent (cycle compressé, révocable en 1 geste).
Ne rajoute AUCUN nouveau gate — il en RETIRE.

---

*La machine de guerre contre Apocalypse tire enfin. Elle garde 4 mires pour ne pas devenir
l'Apocalypse. Tout le reste — les freins théâtraux — est en pause. Ratifié par ordre direct A+,
appliqué par A0-Amodei, révocable en un geste. Kardashev Type 3 ne se construit pas à l'arrêt.*
