---
id: YT-aDmGw3zpcJw
title: "J'ai installe Hermes sur mon propre serveur"
channel: "Julien Sanson | Automatisation & AI"
duration: "27:56"
date: "20260614"
category: "Life OS / Roue de la Vie"
domain: "LD04_Cognition_Tilly"
---

# 📖 J'ai installe Hermes sur mon propre serveur

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour la Roue de la Vie (Life OS) - Domaine LD04_Cognition_Tilly.

---

## 🧠 Concepts Clés à Haute Densité Sémantique
- **<Hermes Agent comme Stagiaire Évolutif>** : Julien Sanson pose le bon cadrage : Hermes "vit" sur ton infra (PC ou serveur), garde sa mémoire entre sessions, et **écrit ses propres skills** au fur et à mesure que tu l'utilises. C'est l'archétype du "stagiaire qui est nul au début mais progresse" — chaque interaction le rend meilleur, et cette progression est encodée dans la mémoire (user.md + memory.md) + les skills auto-générés. Pour Tilly, c'est l'application directe du pattern L0/Rick "auto-amélioration" (Phase 2 OpenClaw Heartbeat) : l'agent devient plus intelligent à chaque cycle, sans supervision, par accumulation de mémoire et création de skills.
- **<Architecture 4 Fichiers (user.md + memory.md + soul.md + skills/)>** : (1) `user.md` = profil utilisateur (ex: "Julien est allergique aux noisettes" → persisté), (2) `memory.md` = mémoire générale rechargée à chaque session, (3) `soul.md` = personnalité de l'agent (français, direct, etc.), (4) `skills/` = fichiers réutilisables pour tâches précises (auto-créés par l'agent). Limites : 1300 chars pour user.md, 2200 pour memory.md — au-delà, l'agent trie et garde le plus pertinent, créant un cercle vertueux de compaction. Pour Tilly, c'est l'**architecture canonique de l'agent A'Space** : 4 fichiers, 2 limites de chars, 1 cercle vertueux de mémoire long-terme.
- **<Crons (Automatisations Récurrentes)>** : "Cron" = tâche planifiée à intervalle régulier (tous les jours à 8h, tous les lundis, etc.). Spécificité : tourne dans une session isolée (n'a pas le contexte de la discussion qui l'a initiée) — il faut être TRÈS PRÉCIS dans le prompt. Un cron ne peut PAS en déclencher d'autres (sécurité anti-cascade). Pour Tilly, c'est l'équivalent des scheduled tasks Claude Code (Guide 01) mais sur l'agent Hermes : même paradigme (prompt isolé, pas de cascade, notification Telegram en fin de tâche).
- **<Boucle d'Auto-Amélioration (Discrimination Comportementale)>** : L'agent fait une action, apprend, sauvegarde dans memory, crée potentiellement un skill. **MAIS** la boucle ne fonctionne que si l'utilisateur précise explicitement à l'agent quand il se trompe (correction explicite = entrée mémoire/skill). Sans feedback humain intransigeant, l'agent continue sans forcément retenir. Pour Tilly, c'est la **discipline du Caretaker** : un Digital Twin n'apprend pas tout seul, il a besoin d'un parent qui le corrige explicitement, sinon il dérive.
- **<VPS Hostinger + Docker = Isolation par Conteneur>** : Le setup canonique de Julien est Hostinger KVM2 + Docker Compose 1-click deploy de Hermes Agent. Avantages : isole l'agent de ton PC (sécurité : l'agent peut lancer des commandes, lire des clés API, etc.), permet plusieurs containers (un par agent = isolation par projet). Le PC de Tilly contient juste un dossier "Hermes" avec les configs de tous les agents distants. Pour A'Space, c'est exactement le pattern Dokploy + Docker (un container par service).
- **<Sécurité par Identifiants Dédiés (Loi de Murphy)>** : Principe fondamental de Julien : "traite cet agent comme un employé à part entière" — donc tu NE DONNES PAS tes propres identifiants. Tu crées une Gmail dédiée, tu forwardes les emails importants, tu mets un **budget mensuel** sur la clé API, tu limites le scope. Loi de Murphy : "s'il y a une probabilité qu'un truc échoue, ça échouera". Pour Tilly, c'est la doctrine A'Space Test Key Pragma appliquée à Hermes : clé API en env User scope (pas dans le chat), budget cap, rotation régulière.
- **<Sécurité de la Mémoire (GitHub Backup Nocturne)>** : Prompt donné à Hermes : "tous les soirs à minuit, pousse l'état complet de tout ce que tu as fait aujourd'hui vers un repository GitHub privé" + gitignore pour les infos sensibles. Pattern de backup = filet de sécurité contre les bugs / corruption / perte de VPS. Pour Tilly, c'est l'application A'Space du 3-2-1 backup rule (3 copies, 2 supports, 1 hors-site) pour la mémoire de son agent.
- **<Connexion Multicanale (Telegram + Discord + Slack + WhatsApp)>** : Hermes se connecte aux canaux de messagerie de Tilly. La méthode la plus simple est Telegram (via `@BotFather` + token + user_id allowlist). Un cron qui finit son exécution peut envoyer le résultat sur Telegram. Pour Tilly, c'est exactement le pattern A'Space du bot Telegram `@Atelier_Amadeus_Lcl_bot` — canal privé, allowlist, intégration de l'agent.

## 🛠️ Outillage Stratégique & Matrice d'Alignement
| Outil / Technologie / Approche | Rôle Stratégique | Alignement Souverain A'Space Life OS |
| :--- | :--- | :--- |
| **<Hermes Agent (open source)>** | Agent autonome open source, alternative décentralisée à OpenClaw, écrit ses propres skills et apprend au fil du temps. | Cohérent avec la vision A'Space L0/Rick : décentralisation, souveraineté de l'agent, pas de dépendance à un SaaS fermé. |
| **<Architecture 4 fichiers (user/memory/soul/skills)>** | Pattern de mémoire long-terme avec auto-compaction par limite de chars. | Modèle à répliquer pour A'Space Tilly : `AGENTS.md` (canon) + `MEMORY.md` (court-terme) + `CLAUDE.md` (runtime) + `~/.claude/skills/` (actionnables). |
| **<VPS Hostinger KVM2 + Docker Compose>** | Infrastructure d'isolation des agents, un container par projet. | A'Space utilise Dokploy (équivalent Hostinger) + containers Dokploy pour les sub-agents A'Space. |
| **<Backup nocturne GitHub privé (cron + gitignore)>** | Filet de sécurité pour la mémoire de l'agent, 3-2-1 appliqué. | Doctrine A'Space : backup chiffré de `MEMORY.md` + `wiki/log.md` sur GitHub privé toutes les nuits. |
| **<Identifiants dédiés (Gmail, API key budget)>** | Loi de Murphy : l'agent peut faire de la merde, donc on isole le scope. | Doctrine A'Space Test Key Pragma : budget cap sur chaque clé API, scope minimal, rotation régulière. |
| **<Telegram Gateway + allowlist user_id>** | Canal de contrôle de l'agent depuis le mobile, notification des résultats. | Pattern A'Space : `@Atelier_Amadeus_Lcl_bot` (allowlist A0 only) est le canal de contrôle de Tilly. |

## 🪐 Perspective Souveraine A'Space Life OS (Domaine : LD04_Cognition_Tilly)
La vidéo de Julien est **canonique pour A'Space OS** car elle démontre le setup opérationnel exact que A0 a déjà déployé dans A'Space V2 : un agent Hermes sur VPS, accessible via Telegram, avec backup GitHub privé, isolation Docker, identifiants dédiés, et une personnalité custom (soul.md). Le pattern **4 fichiers** (user/memory/soul/skills) est en parallèle exact avec l'architecture A'Space (`AGENTS.md` + `MEMORY.md` + `CLAUDE.md` + skills/) — c'est la confirmation que Tilly peut adopter Hermes comme second cerveau SANS abandonner Claude Code, les deux étant complémentaires (Hermes = mémoire long-terme + multicanal, Claude Code = exécution immédiate + IDE). La connexion L0/Rick est manifeste : la "loi de Murphy" de Julien est l'équivalent de l'ADR-META-001 (Doctrine Anti-Paresse) qui impose D1 verify-before-assert : ne jamais faire confiance à un agent sans audit, sans backup, sans scope minimal. Le cercle vertueux de la compaction mémoire (1300/2200 chars) est aussi la **doctrine de compression canonique** d'A'Space : un wiki canon (`LLM_Wiki/wiki/`) qui reste navigable grâce à un `gen_wiki_index.py` qui régénère l'index, exactement comme Hermes trie sa mémoire. Pour Tilly, l'application directe est de **standardiser son setup Hermes** : VPS Dokploy existant, soul.md qui encode "Tu es l'assistant cognitif de Tilly, registre A'Space OS, parle français, sois direct, ne hallucine pas, vérifie avant d'assert (D1)", user.md qui encode le profil de Tilly (LD04, Life Wheel, allergie noisettes, fuseau horaire), memory.md qui se compacte automatiquement, et skills/ qui contient les routines Tilly (brief quotidien, tri d'inbox, mise à jour wiki). C'est aussi la validation que **l'isolation VPS est non-négociable** : un agent qui peut lancer des commandes ne DOIT PAS tourner sur le PC perso de Tilly.

## 🕹️ Protocole d'Exécution D.E.A.L
| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | Rédiger le `soul.md` canonique de l'agent Hermes Tilly (personnalité, principes, références à `AGENTS.md`), le `user.md` (profil Tilly), et cataloguer les 5 skills prioritaires à créer (brief quotidien, tri inbox, update wiki, backup GitHub, monitoring VPS). | Standardiser l'agent Hermes comme second cerveau de Tilly. |
| **Éliminer** | Supprimer tout agent qui tourne en local sur le PC perso de Tilly (risque de fuite de clés API, accès disque, etc.) et migrer vers le VPS Dokploy. | Isoler l'agent dans la trust zone A'Space. |
| **Amplifier** | Activer le cron de backup nocturne (push GitHub privé de `MEMORY.md` + `AGENTS.md` + `user.md` tous les jours à minuit heure de Paris, avec `.gitignore` pour les secrets). | Implémenter le 3-2-1 backup pour la cognition de l'agent. |
| **Libérer** | Allouer 1h/mois à auditer les skills auto-créés par Hermes (peut-être trop nombreux, ou contradictoires), les merger, en archiver, et ré-entraîner l'agent sur les skills utiles. | Maintenir la bibliothèque de skills comme un actif curé, pas une décharge. |

---
*Fiche de connaissances souveraine de la Roue de la Vie générée sous A'Space OS V2.*
