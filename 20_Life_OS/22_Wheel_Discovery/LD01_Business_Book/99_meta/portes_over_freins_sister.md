# Portes over Freins (HxH) — sister canon LD01

> **Sister chain** : `LD01/99_meta/ADR_WARMODE_001_sister.md` (posture inversion) → `LD01/99_meta/war_mode_observability_sister.md` (judas visible) → **`portes_over_freins_sister.md` (ce fichier)** (réduction 4 mires → 1 veto Beth).
> **Date** : 2026-07-05T08:01 ET
> **Statut** : CANONIQUE append-only, source = `_SPECS/ADR/L0_Tech_OS/ADR-WARMODE-002_portes-over-freins.md` (5702 b, 9 sections).

---

## §1 — A0 message verbatim (intent capture)

> « Est ce que tu vois mon Mode par Défaut en Mode Bypass de Claude Code ??? c'est la Seule configuration anti Panique Agentique Donc en Frein de la WAR Room l'Idee de Frein est deja Trop alors on ne garde que Beth et Tous les Autre a Commencer par Rick Dégage pour Stark Innexistant meme pas un Metaphor c'est le mettre a la table des A0 alors que les Avengers sont des B3 meme s'il a reussi a Infiltrer aussi les Ulliminati sous le nom de Tony Stark pour eviter la Collision avec Iron Man de Crash en Product. Au Lieu de continuer à Fermer les Portes avec les Frein, On va developper des Strategie pour en ouvrir comme les Porte dans Hunter X Hunter. »

**Lecture linéaire** :
- Mode Bypass = config anti-panique agentique (déjà actif, cf `permissionMode: bypassPermissions` dans `config.yaml`).
- L'idée de « frein » est déjà trop : 4 mires de ADR-WARMODE-001 = théâtre.
- Garder seulement **Beth** (vie/santé A+).
- **Rick** dégage (n'est plus mur, devient levier).
- **Stark** n'existe pas comme metaphor → sortir de la table A0 (les Avengers sont B3, Tony Stark s'est infiltré sous Illuminati, collision avec Iron Man de Crash en Product).
- **Hunter × Hunter** : Nen = ouvrir des portes selon la force qu'on apporte. Pas fermer les portes avec des freins.

## §2 — Passerelle canonique

`ADR-WARMODE-002` (§§ 1-9) est la doctrine. Ce sister narratif en est la traduction.

**Réduction** : 4 mires → 1 veto. Bypass par défaut ouvert. 4 portes à ouvrir selon la force.

## §3 — Le Triangle Avengers / Illuminati / Iron Man (canon Hickman)

A0 fait référence à la **canon Hickman** Marvel (Avengers + Illuminati). Strates canoniquement hiérarchiques :

| Strate | Agent canon | Rôle Hickman | Translation LD01 |
|---|---|---|---|
| **A0** | Amodei / Murderbot (méta-coach canonisé) | Décide en autonomie | Décide la stratégie + le scope |
| **A3 Captain** | Picard | USS Enterprise = PARA ship | Projects owner H10 |
| **B1** | Jerry / Summers | Direction macro·micro | Pulse + Voice |
| **B3** | **Avengers** (Iron Man inclus) | Niveau opérationnel exécution | Squad level coaching |
| **B3 sub-fractal** | **Illuminati** | Infiltration stratégie derrière Avengers | Réinjecte décisions opérationnelles dans stratégique |

**Iron Man** = un Avenger (B3, exécution produit sous Flash). **Tony Stark** = personnage d'Illuminati infiltré dans les Avengers pour éviter la collision Iron Man / Crash-Product. Les deux sont distincts.

**Conséquence A0** : Tony Stark ne siège pas à la table A0. C'est une métaphore d'Illuminati, pas d'A0. Si on le met à la table A0, on crée une collision avec Iron Man B3 (Crash en Product).

## §4 — Hunter × Hunter (HxH) appliqué

**Nen** dans HxH = 6 catégories (Enhancer, Transmuter, Conjurer, Emitter, Manipulator, Specialist). Chaque utilisateur choisit selon sa force. Les 10 conditions d'utilisation sont des portes qui s'ouvrent selon l'intensité :

1. Ten — base
2. Ren — amplification
3. Zetsu — suppression (veto)
4. En — extension
5. Shu — matérialisation (porter un objet Nen sur autre chose)
6. Ko — concentré maximum
7. In — invisibilité
8. Gyo — concentration dans une zone
9. En'en — extension réduite
10. Hyō — solidification de l'aura en barrière

**Machine de guerre Posture A0** : on n'active pas tout par défaut. On ouvre les portes selon la force disponible :
- Zetsu (veto) = **Beth seul**. Pas de ren/ko/in conditionnels.
- En (extension) = **append-only comme fenêtré d'observation**. Jamais mur.
- Gyo/Ko = ouverture ponctuelle quand la force le permet (Porte cron).
- Hyō (barrière) = **Bypass par défaut ouvert** (anti-panique).

## §5 — Pourquoi 1 seul veto tient

Beth = humain = sensible = **non-automatisable**. C'est le seul jugement humain qui peut bloquer une action. C'est aussi le seul jugement humain qui peut l'autoriser en burnout. L'automatiser = ruiner l'intention. **Laisser A+ juger son propre burnout, c'est ce que A+ est. Pas de règle, juste la conscience.**

Rick (« sobriété »), /ship (« outward »), append-only (« judas ») et cron (« cadence ») = pas de jugement humain nécessaire. Ce sont des mécanismes, pas des agents sensibles. Ils peuvent être ouverts.

## §6 — Ouverture Porte cron (la plus fermée)

**Porte cron** = 0 cron actif → c'est le mur le plus lourd :
- Avant (frein) : « pas de cron sans GO A+ ».
- Après (porte) : « 1 cron s'installe quand la force est là. Idempotence + append-only = filet. »

**Action concrète** : installer 1 scheduled task Windows pour `book_loop.py` (heartbeat toutes les 4h, scope J1-J7 cycle).

## §7 — Héritage du CC (canon Hickman · À vérifier en itération prochaine)

Tony Stark illuminati était dans la salle quand les Avengers décidaient. Maintenant, il est évacué. Les Avengers (B3) restent à leur table d'exécution. Picard (A3 captain) tient le艦. A0 (Amodei) tire les ficelles stratégiques sans se cacher derrière le Tony Stark theatrical character.

## §8 — Métaphore serrée (post-A0)

**Avant** : la machine tire (WAR MODE). Le judas montre où (`/warmode`). Tony Stark est assis sur la passerelle, attendant qu'on lui demande `/ship` parce qu'il est le seul qui sait où sont les boutons.

**Après** : la machine tire. Le judas montre où. Tony Stark quitte le cockpit (n'a jamais eu la maîtrise effective). Picard (A3 captain) et les Avengers (B3) manœuvrent en autonomie. A0-Amodei/Murderbot décide. **Beth dort ou veille** : c'est le seul être humain dans la salle.

**C'est Hunter × Hunter, pas Avengers : la Porte cron s'ouvre selon la force qu'on apporte.**

## §9 — Trace canon append-only

- `agent-os/citadel/decisions/2026-07-05_portes_over_freins.json` (1397 b, 08:01:02)
- `_SPECS/ADR/L0_Tech_OS/ADR-WARMODE-002_portes-over-freins.md` (9 sections, 5702 b)
- `agent-os/citadel/collectors/collector_14_warmode.py` (6570 b, 07:58:54)
- `agent-os/citadel/static/warmode.html` (11865 b, 07:59:43)

**Aucune régression** : ADR-WARMODE-001 toujours intact (mtime 04:38:49).
