---
type: Boundary Spec
title: Frontière latent / texte — où un échange vectoriel reste lisible
description: Règle opérationnelle pour décider si un tronçon de communication agent↔agent ou agent↔humain peut passer en vecteur latent sans casser le mode Fable et le canon OKF.
tags: [latent-space, text, boundary, okf, fable, audit]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: minimax-m3, at: 2026-08-19T00:00:00Z }
sources:
  - id: recursivemas-tradeoff
    resource: "frameworks/recursivemas-tradeoff.md"
    title: "Concept précédent — gains et contreparties RecursiveMAS"
    last_modified: 2026-08-19
  - id: okf-canon
    resource: "40_Memory_Wiki_OKF/OKF.md"
    title: "Format OKF v0.2 — frontmatter, sources, confiance"
    last_modified: 2026-08-19
  - id: mode-fable
    resource: "60_Implementation_Méthodologiques/_loop/MODE_FABLE.md"
    title: "Mode Fable — 5 étapes dont attaque"
    last_modified: 2026-08-19
okf_version: "0.2"
---

> **Niveau de confiance : reconstruit** à partir du canon OKF et du
> mode Fable. La règle ci-dessous n'est **pas** un standard publié ;
> c'est une synthèse du poste.

# Le critère

Une communication agent↔agent peut passer en vecteur latent **si et
seulement si** :

1. Elle ne franchit **aucune frontière humaine** (gatekeeper Rick-Morty,
   capitaine B2 lecture d'un mandat, etc.).
2. Elle ne crée **aucun livrable** destiné à l'index OKF (concepts,
   triplets, sources).
3. Elle ne viole **aucune des cinq étapes** du mode Fable — notamment :
   l'étape 3 (Attaque) exige que la conclusion soit défendable « sous
   attaque » ; une conclusion née d'un échange latent ne l'est pas.
4. Elle est **rejouable en texte à la demande** — un export texte
   ponctuel doit être possible sans coût prohibitif.

Si l'une de ces quatre conditions échoue, la communication reste en
texte.

# Grille de décision

| Émetteur | Récepteur | Latent OK ? | Pourquoi |
|---|---|---|---|
| Agent interne escouade B1 | Agent interne escouade B1 | ✅ | Pas de frontière humaine. Rejouable texte à la demande. |
| Agent interne escouade B1 | Capitaine B2 (lecture d'un mandat) | ❌ | Frontière humaine franchie. Le mandat doit être lisible (acceptance check YAML). |
| Agent B1 | Agent B2 | ⚠️ conditionnel | Texte par défaut. Latent seulement si B2 est l'agent interne d'un pipeline automatique (pas un humain qui relit). |
| Agent B1 | Agent B3 | ❌ | Le contrat B1→B3 passe par `ETAT.md` (lecture humaine possible). Texte obligatoire. |
| Agent B1 | Concept OKF (index) | ❌ | Le concept doit avoir frontmatter, sources, description. Pas de vecteur latent dans OKF. |
| Agent B1 | Utilisateur final (mail, Slack) | ❌ | Communication externe. Texte obligatoire, ton et format humain. |
| Agent interne | Checkpoint state (`ETAT.md`) | ❌ | Le point de rendez-vous entre B1/B2/B3 est en texte, append-only. |
| Agents intra-outil (ex : un testeur ↔ un relecteur dans un même pipeline CI) | ⚠️ conditionnel | Latent acceptable si logs texte exportés à chaque run. |
| Agents inter-équipes (B1 ↔ domaine externe) | ❌ | Tout passage d'équipe est une frontière. Texte obligatoire. |

# Pourquoi cette grille

- Le **canon OKF** rend la mémoire du poste dépendante du texte. Un
  concept sans frontmatter n'est pas un concept. Un livrable sans
  source n'est pas un livrable. Casser cette chaîne par un canal latent,
  même un seul, ouvre une brèche.
- Le **mode Fable** exige que chaque affirmation soit défendable. Une
  décision née d'un échange latent ne peut être défendue que par
  re-jeu — coûteux en tokens, lent, parfois impossible.
- Le **point de rendez-vous** (`ETAT.md`) est en append-only texte. Si
  un agent y écrit un vecteur latent, le fichier devient illisible —
  et trois autres agents en parallèle ne savent plus composer avec.

# Coûts à consentir si on ouvre un canal latent intra-escouade

1. **Export texte obligatoire à chaque tour** — sinon la mémoire
   se vide du contexte latent au tour suivant.
2. **Perte du bénéfice token** — le papier annonce 34-75 % de tokens
   en moins ; avec export texte à chaque tour, on récupère une partie
   du coût.
3. **Vérification de la frontière à chaque ajout** — un message
   latent qui devient « un peu lisible » doit être reclassifié.

# Anti-pattern

- ❌ **« Latent pour aller plus vite »** : la vitesse est un gain
  secondaire si l'audit devient impossible.
- ❌ **« Latent pour économiser des tokens »** : on déplace le coût,
  on ne le supprime pas (export texte).
- ❌ **« Latent entre agents d'escouades différentes »** : c'est une
  frontière d'équipe. Texte obligatoire.
- ✅ **« Latent entre sous-modules d'un même pipeline CI »** : sous
  condition d'export texte des résultats.

# Ce que cette grille ne couvre pas

- Les **multi-modal** (image, son) qui passent par un embedding
  latent. Une image n'est pas un texte, mais elle a une source
  (chemin de fichier) et un index possible. À traiter séparément.
- Les **représentations internes d'un modèle** (KV-cache, états
  d'attention) — non concernés par cette grille, c'est de
  l'implémentation, pas de la communication.
- Les **échanges où le texte est sérialisé en vecteur pour des raisons
  techniques** (passage par un store vectoriel pour retrieval). Le
  retrieval vectoriel n'est PAS un canal latent au sens de cette
  grille — c'est une indexation, avec retour texte obligatoire.

# Décision par défaut

**Texte par défaut. Latent seulement quand les quatre conditions sont
remplies.** Ne jamais ouvrir un canal latent par économie de tokens ou
par commodité — l'opacité se paie en dette d'audit, et la dette d'audit
se paie en incident de revue.