---
session: agent-ada3ac6ddfa960f2e
origine: claude
chemin_source: C:\Users\amado\.claude\projects\C--Users-amado\bf0d8147-2bf5-4bb4-84bf-a254bd46999e\subagents\agent-ada3ac6ddfa960f2e.jsonl
debut: 2026-08-01T18:32:18.722Z
fin: 2026-08-01T19:06:13.230Z
messages_utilisateur: 1
reponses_assistant: 0
titre: "Tu es Geordi (officier Resources du PARA de l'utilisateur). Tâche : LINT du LLM Wiki. Réponds en français. ## …"
---

## >>> UTILISATEUR #1

Tu es Geordi (officier Resources du PARA de l'utilisateur). Tâche : LINT du LLM Wiki. Réponds en français.

## Cible (lecture seule)
`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki`
~1773 fichiers `.md`. C'est un vault Obsidian (dossiers : concepts, entities, agent_capsules, audits, comparisons, dreams, inbox, hand_offs, J01_Prime, J02_Bio, J03_Nexus, J04_Solarpunk, L0, Claude Export, Gemini_Takeout_2026, copilot, Hermes Agent…).

## Règle absolue
**Ne modifie AUCUN fichier du wiki.** Tu es en lecture seule sur le vault. Le seul fichier que tu écris est ton rapport (chemin en bas). Ignore les dossiers `.obsidian`, `.claudian`, `graphify-out`, `Excalidraw`.

## Ce que tu dois détecter
Écris des scripts Python (via Bash) pour analyser en masse — ne lis pas 1773 fichiers un par un.

1. **Liens `[[...]]` cassés** — cible inexistante dans le vault. Donne le compte total + le top 30 des cibles manquantes les plus référencées (c'est le signal le plus utile : ce sont les notes à créer).
2. **Frontmatter YAML** — fichiers sans frontmatter ; frontmatter présent mais illisible (YAML invalide) ; champs manquants par rapport au schéma dominant. Déduis le schéma dominant des fichiers qui en ont un, ne l'invente pas.
3. **Notes orphelines** — aucun lien entrant. Compte + répartition par dossier (pas la liste complète si >100).
4. **Doublons** — même titre H1 ou même nom de fichier à des chemins différents ; notes au contenu identique (hash).
5. **Notes vides ou squelettes** — < 100 caractères de contenu utile hors frontmatter.
6. **Hygiène de nommage** — noms avec espaces, accents non normalisés, caractères interdits Windows, longueur de chemin > 240 (risque réel sur ce système).

## Format du rapport
Écris `C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/WIKI_LINT_2026-08-01.md` avec ce frontmatter :

```yaml
---
id: WIKI_LINT_2026_08_01
layer: L1_Life_OS
role: A3_PARA_Discipline
classification: Resources
status: ACTIVE
created: 2026-08-01
---
```

Puis : un tableau de synthèse (métrique / valeur / gravité), puis une section par catégorie avec les chiffres et les exemples concrets (chemins réels), puis une section finale **« Corrections par ordre de rentabilité »** : ce qui se répare en masse par script vs ce qui demande une décision humaine. Chiffre l'effort.

## Sortie de l'agent
Ton texte final = un résumé de 10 lignes max : les 3 problèmes les plus graves avec leurs chiffres, et le chemin du rapport. Pas de préambule.

Facts only : si un chiffre n'est pas mesuré, ne l'invente pas. Si un dossier est illisible ou trop gros, dis-le explicitement dans le rapport plutôt que de l'omettre silencieusement.
