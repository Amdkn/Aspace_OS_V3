# Client Onboarding Kit v1 — Solaris Nexus Agency

**Date :** 2026-05-27
**Statut :** Template canonique — déclenche les 8 SOPs Active du mesh
**Ancré sur :** ADR-MESH-L2-001 · ADR-ID-001 · ADR-CK-FREE-001 · OPS-001 (Onboard New Nexus Client)

---

## Pré-requis (à remplir avant kickoff)

| Champ | Type | Source |
|-------|------|--------|
| Nom de l'agence cliente | string | Mail / discovery call |
| Nom commercial (Display_Name) | string | Idem |
| `CLIENT_ID` slug | string ≤24c, lowercase, kebab | Généré (cf. ADR-ID-001 D2) |
| URL site web | url | Discovery |
| Email principal contact | email | Discovery |
| LinkedIn fondateur | url | Discovery / Apollo |
| Pays / Secteur d'activité | strings | Discovery |
| Quota livrables mensuel négocié | int | Devis signé |
| Date de lancement | date | Devis signé |

## Étape 1 — Créer le record Airtable 🌞 Clients & Workspaces

**Squad** : Fantastic4 (Ops) déclenche, mais création par Jerry/A0
**SOP source** : OPS-001 dans Notion

Champs minimum à remplir dans Airtable (base `appmWf5Xm7w9Ae0ky`, table `tbluaIHfq2HPUDh1M`) :

```
- Nom de l'Agence Cliente        : {Display_Name}
- Deal Lié                        : {DL-CLIENT_ID-01}
- Statut du Compte               : "Onboarding"
- Date de Lancement              : {date kickoff}
- Quota de Livrables Mensuel     : {int}
- Dossier Racine S3              : (à provisionner par IT-001)
- Portail Client Space Agent     : (à provisionner)
- Taux de Complétion Onboarding  : 0%
```

À sa création, le record reçoit un Airtable record ID. Le **CLIENT_ID slug** doit être noté dans le champ texte dédié (à ajouter si pas encore présent — checklist Phase 1 ADR-ID-001).

## Étape 2 — Provisionner l'infra (KangDynasty / IT-001)

**Tasks ClickUp à créer dans S3-8 Infrastructure Médias** :

```
Titre : [SOP-L2-IT-001] CL-{slug} — Provision VPS Nexus instance
Tags  : cl:{slug} · dom:it · p1
Description : Cf. SOP Notion OPS-001 page 36c7e9e2-658c-81b6-8540-c45e4a56a97f
```

Sous-tâches automatiques :
- [ ] Créer bucket S3 dédié `s3://aspace-nexus-{slug}/`
- [ ] Déployer instance Solaris via Dokploy (cf. SOP IT-002)
- [ ] Provisionner schema Supabase `tenant_{slug}` (cf. config Supabase self-host)
- [ ] Configurer domaine `{slug}.aspace.solaris.app` (Caddy/Traefik)
- [ ] Tester healthcheck

## Étape 3 — Configurer Knowledge & Brand Books (XMen / PEOPLE-001)

**Tasks ClickUp dans S2-3 Onboarding & RAG** :
- Vectorisation Brand Books (Prof. X) : ingérer PDF brand book → Supabase vector store
- Création Context Pack : extraire ton de voix, mots interdits, codes HEX
- Filtres Mots Interdits (Jean Grey) : configurer liste anti-cliché spécifique

**Record Airtable 🏮 Knowledge & Brand Books** :
- Upload PDF Brand Book
- Saisir 3 exemples textes représentatifs du ton
- Saisir mots strictement interdits
- Lier au record 🌞 Clients & Workspaces

## Étape 4 — Lancer le pipeline Sales (Illuminati / SALES-001)

**Si lead inbound** :
- Task ClickUp S2-2 list "Audits Margin Bleed" : `[SOP-L2-SALES-001] CL-{slug} — Qualifier lead inbound + audit margin bleed`
- Record Airtable 🦸 Leads & Audits : `LD-{slug}-{YYYYMM}` avec score Lighthouse
- Si qualified : créer record Airtable 💸 Sales Pipeline `DL-CL-{slug}-01`

## Étape 5 — Generate proposal & contract (Eternals / LEGAL-001)

**Task ClickUp S4-9** :
- `[SOP-L2-LEGAL-001] CL-{slug} — Préparer contrat client + DPA`

**Record Airtable 🔱 Compliance & Contrats** :
- `LG-CL-{slug}-MSA-01` (Master Service Agreement)
- `LG-CL-{slug}-DPA-01` (Data Processing Agreement)
- IP Cleared checkbox + watermark policy

## Étape 6 — Émission première facture (Thunderbolts / FINANCE-001)

**Task ClickUp S4-10 list "Émission Factures Stripe"** :
- `[SOP-L2-FINANCE-001] CL-{slug} — Émettre invoice Stripe setup fee + M1`

**Record Airtable 🛡️ Finance & Compute** :
- `INV-CL-{slug}-{YYYYMM}` Setup fee + MRR M1
- Lien d'abonnement Stripe
- Coûts API mensuels prévisionnels
- Marge nette prévisionnelle

## Étape 7 — Activer la machine Growth (Guardians)

**Task ClickUp S2-1 list "Publish LinkedIn Personal Brand Post"** :
- `[SOP-L2-GROWTH-001] CL-{slug} — Publier post personnal branding fondateur agence`

## Étape 8 — Activer la Factory (Avengers / Forge Textuelle + Visuelle)

**Si premier brief reçu** :
- Record Airtable 🦇 Briefs & Opérations : `BR-CL-{slug}-{YYYYMMDD}-01`
- Build Gate validation : checkbox "Objectif clair" + "Charte respectée"
- Si validé : Task ClickUp S2-4 → cascade vers S3-5 (texte) ou S3-6 (visuel)

## Étape 9 — Activer Bug Triage (Avengers / PRODUCT-003)

**SOP-L2-PRODUCT-003** : si un bug est rapporté pendant l'onboarding, task ClickUp dans la list dédiée avec sévérité P0/P1/P2/P3.

## Checklist 100% onboarding

- [ ] Record 🌞 Clients & Workspaces créé, CLIENT_ID assigné
- [ ] Infra provisionnée (S3 + Solaris instance + Supabase schema + domaine)
- [ ] Brand Book vectorisé + Context Pack créé
- [ ] Contrats MSA + DPA signés
- [ ] Première facture émise + paiement reçu
- [ ] Premier brief Build-Gate validé
- [ ] Premier livrable Factory produit
- [ ] Portail Space Agent accessible au client
- [ ] `Taux de Complétion Onboarding` = 100%
- [ ] `Statut du Compte` passé de "Onboarding" à "Active"

## Sortie attendue end-to-end (les 8 SOPs Active testées en réel)

À la fin de cet onboarding, **les 8 SOPs Active** ont été exercées au moins 1 fois en réel. C'est le **vrai Build_Gate** doctrinal. Mettre à jour Notion `Build_Gate` field avec : `"Tested via onboarding {CLIENT_ID} on {date} — see Airtable CL-{slug}"`.

## Notes opérationnelles

- Durée moyenne attendue : **5-10 jours ouvrés** entre signature et premier livrable
- Bloquants typiques : DPA en attente client, brand book pas fourni, accès Stripe en attente
- Escalation : tout retard >3 jours sur une étape → ping A0 + arbitrage A1 (Rick)

## Références

- ADR-MESH-L2-001 — Doctrine tri-plateforme
- ADR-ID-001 — Identifiants universels
- ADR-CK-FREE-001 — Contraintes ClickUp Free
- ADR-NOTION-001 — Back-office Solaris template
- Notion Solaris HQ : `36c7e9e2-658c-8185-bd87-e76c9f5360b6`
- ClickUp workspace : `90141225938`
- Airtable base : `appmWf5Xm7w9Ae0ky`
