---
session: agent-a149ba1d1a8aa4a38
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\d13e9144-d0de-4698-83b3-4f36e8e49b48\subagents\agent-a149ba1d1a8aa4a38.jsonl
debut: 2026-07-22T07:58:11.547Z
fin: 2026-07-22T08:03:01.891Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "Reprise. Phase 1 et 2 livrées. Phase 3 = **uniquement créer la page Notion**, pas de mini-site, pas de capsule…"
---

## >>> UTILISATEUR #1

Reprise. Phase 1 et 2 livrées. Phase 3 = **uniquement créer la page Notion**, pas de mini-site, pas de capsule, pas de quiz. Strict.

## Étapes

1. **Trouver le parent Notion** via `mcp__notion__API-post-search` avec query="OMK". Récupère le 1er résultat pertinent (page contenant "OMK", "AaaS", "Solaris" ou "Business OS" dans le titre). Si rien, query="AaaS". Si toujours rien, query="Solaris". Garde son `id` comme parent.

2. **Créer la page** via `mcp__notion__API-post-page` avec :
   - `parent.page_id` = l'id de la page trouvée
   - `properties.title` = title de la page : `[OMK] Prospection Coach Expert — Marketplaces Study`
   - `children` = blocs structurés (paragraphes + headings + tables simples en rich_text). **Pas de markdown dans children**, utiliser les types de blocks Notion (`heading_1`, `heading_2`, `paragraph`, `bulleted_list_item`, `table`).

## Structure de la page (à transcrire en blocks Notion)

```
# [OMK] Prospection Coach Expert — Marketplaces Study

## 🎯 Résumé exécutif
Le coach expert cible = opérateur senior ou fondateur avec expertise narrow, capable de transformer son expertise en accompagnement premium récurrent, au-delà du simple appel ponctuel type intro.co. ICP OMK primaire = Orbiter 🏗️ (Coach-as-OS Layer, scalabilité async, transformation persistée). Solaris 🎨 et Nexus ⚖️ restent jumeaux (contenu + conformité).

## 🗺️ Cartographie marketplaces
### intro.co
- Modèle : marketplace d'appels individuels avec experts sélectionnés
- Pricing : par expert/session
- ICP coach : experts publics, fondateurs, opérateurs, créateurs
- Forces : accès direct, crédibilité, réservation fluide
- Faiblesses : peu de continuité, dépendance à la notoriété, profondeur limitée

### BetterUp
- Modèle : coaching structuré B2B corporate
- Pricing : devis entreprise
- ICP coach : coachs professionnels en programmes RH
- Forces : scale enterprise, mesure, parcours structurés
- Faiblesses : moins accessible individuel, processus corporate

### CoachHub
- Modèle : réseau coaching digital B2B
- Pricing : devis entreprise
- ICP coach : coachs certifiés leadership/carrière
- Forces : réseau international, orientation organisations
- Faiblesses : forte orientation entreprise, moins pertinent niche conseil expert

## 👤 Profil coach expert CIBLE
- Opérateur senior ou fondateur
- Expertise narrow, prouvée par résultats
- Pratique premium récurrente (pas juste appel ponctuel)
- Veut scaler sans devenir agence

## 🔗 Pain → OMK mapping
| Pain | ICP OMK | Agent concret |
|---|---|---|
| Dépendance notoriété | Orbiter | Brand-to-System Pipeline |
| Pas de continuité transformationnelle | Nexus | Client Journey Memory |
| Scalabilité limitée | Orbiter | Async Cohort Engine |
| Qualité/dispo variable | Solaris | Content-to-Asset Dam |
| Épuisement contenu | Solaris | Visibility Loop |
| Conformité paiements/RGPD | Nexus | Compliance & Billing Guard |
| Refus de devenir agence | Orbiter | Coach-as-OS Layer |

ICP primaire : **Orbiter** 🏗️

## 📡 Canaux prospection

### LinkedIn
Sales Navigator queries :
- Query 1 : ("coach" OR "consultant" OR "mentor") AND ("scaling" OR "système") AND ("senior" OR "expert") AND ("B2B" OR "dirigeants") — Founder/CEO — FR/BE/CH/CA — 1K-10K followers
- Query 2 : ("coach" OR "formateur") AND ("lance" OR "nouveau programme" OR "auteur") AND ("transformation" OR "leadership") — Posts 30j — FR

Hashtags : #coachscalable #entrepreneurcoach #coachsystème

Groupes : "Coachs & Consultants en France" (~28K) · "Scale My Coaching Business" (~9K EN/FR)

### Email — 2 triggers + séquence 3-step
Trigger 1 : publication livre/programme → email J+2 angle Orbiter
Trigger 2 : post LinkedIn burnout → email J+0 angle Solaris

Séquence :
- J+0 Email 1 : question ouverture, pas de call
- J+3 Email 2 : étude de cas vidéo, pas de push meeting
- J+7 Email 3 : lien Calendly, NO-FOLLOW-UP

### Content & Partnerships
1. Intro.co × OMK : co-pub guide "The Coach's Operating System" + webinar conjoint W18 H2 2026
2. Mighty Networks / Circle : add-on "OMK Coach OS" intégré à leur marketplace, MRR partagé

## 💬 Messaging angles

### Solaris 🎨
Subject : "Vous parlez 1×, l'agent publie 12×"
Body : Vous avez 200h de lives et 5 podcasts — et pourtant vous êtes le seul à pouvoir "exécuter". Solaris capture chaque prise de parole, la décline en 12 formats (post, reel, newsletter, lead-magnet), et garde votre voix. Vous restez le stratège. Votre agent fait le reste. 90 sec pour voir : [lien]

### Nexus ⚖️
Subject : "Contrats B2B en 7 min, pas 7 jours"
Body : Un client entreprise vous demande un DPA RGPD. Votre avocat facture 1 800 € pour 4 jours. Nexus génère le contrat conforme à votre cadre, signe eIDAS, archive l'audit trail — et vous notifie à l'échéance. Vous facturez 5 000 € de plus par client B2B sans augmenter votre risque. Démo guidée : [lien]

### Orbiter 🏗️
Subject : "Scaler sans devenir une agence"
Body : Vos 20 meilleurs clients transforment. Vos 80 autres achètent et churnent en 90 jours. Orbiter installe un OS sur votre cabinet : graphe de transformation par client, alertes de décrochage, programmes async auto-portants. Vous passez de 50K à 250K€ ARR sans recruter. Diagnostic gratuit 30 min : [lien]

## 📚 Sources
- intro.co — https://intro.co/
- intro.co how-it-works — https://intro.co/how-it-works
- intro.co pricing — https://intro.co/pricing
- intro.co become-a-coach — https://intro.co/apply/become-a-coach
- Boon vs BetterUp — https://www.boon-health.com/compare/betterup
- BetterUp alternatives (Vibly) — https://vibly.io/blog/betterup-alternatives/
- Online coaching platforms (Yo-Coach) — https://www.yo-coach.com/blog/top-online-coaching-platforms/
- Leadership coaching platforms (Hallett) — https://hallettleadership.com/feeds/blog/platforms-one-on-one-executive-coaching-relationship-improvement
- Coaching platforms and marketplaces (Paperbell) — https://paperbell.com/blog/coaching-marketplace/

## 🔗 Liens canon OMK (à compléter A0)
- ADR-ICP-ORBITER-001 (canon 2026-06-24)
- ADR-ICP-SOLARIS-001 (canon 2026-06-24)
- ADR-ICP-NEXUS-001 (canon 2026-06-24)
- ADR-LLM-COST-COMPARE-001 (prix agent €/mois)
```

3. **Retourne dans ta réponse** :
- L'URL de la page Notion créée
- 200 char de résumé pour le main-agent

## Garde-fous
- Si le 1er search Notion ne donne pas de parent OMK clair, **essaie 2 requêtes supplémentaires** ("AaaS", "Solaris", "Nexus", "Business OS") avant de remonter en erreur
- Ne crée JAMAIS la page à la racine workspace si tu n'as pas trouvé de parent pertinent — retourne l'erreur au main-agent avec les pages candidates trouvées
- Pas de tools autres que `mcp__notion__*` dans cette phase

### assistant

Page Notion créée sous le parent pertinent **Deploy Solaris Instance via Vercel + Supabase Cloud** :

https://app.notion.com/p/OMK-Prospection-Coach-Expert-Marketplaces-Study-3a57e9e2658c8101a75bfa287ad59251

**Résumé main-agent — 200 caractères :**  
Page Notion OMK créée sous le parent Solaris : étude marketplaces, ICP Coach Expert centré Orbiter, mapping pains/agents, canaux LinkedIn/email, partenariats, messaging Solaris/Nexus/Orbiter et sources.
