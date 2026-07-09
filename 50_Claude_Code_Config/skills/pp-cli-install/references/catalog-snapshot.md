# Printing Press Library Catalog — Snapshot 2026-05-17

Pre-built CLIs available at `https://github.com/mvanhorn/printing-press-library`.
For each service, the release tag is `<service>-current` and the Windows binary asset is `<service>-pp-cli-windows-amd64.exe`.

When the user requests `/pp-cli-install <X>`, check if `<X>` appears in the table below. If yes → the install script will auto-download (no flags needed). If no → consult `known-spec-urls.md` or use `-DocsUrl`.

**This snapshot drifts.** Run `gh api repos/mvanhorn/printing-press-library/releases` to get the live state, or re-list `library/<category>/` directories.

## By category

### ai
- elevenlabs (embedded in cli-printing-press main catalog)

### auth
- stytch

### cloud
- cf-domain
- cloud-run-admin
- digitalocean
- render

### commerce
- amazon-seller
- craigslist
- ebay
- fedex
- gumroad
- instacart
- shopify
- slickdeals
- squarespace
- tiktok-shop
- yahoo-finance

### developer-tools
- agent-capture
- airframe
- company-goat
- docker-hub
- domain-goat
- firecrawl
- **github**
- namecheap
- nse-india
- nvd
- openfda
- postman-explore
- pypi
- scrape-creators
- sec-edgar
- **supabase**
- trigger-dev
- uspto-tsdr

### media-and-entertainment
- youtube

### monitoring
- **sentry**

### payments
- mercury
- plaid
- **stripe**

### productivity
- cal-com
- fathom
- figma
- fireflies
- freshservice
- granola
- marianatek
- myfitnesspal
- **notion** ⭐ (full Notion REST API)
- opensnow
- outlook-calendar
- outlook-email
- resend
- roam
- **slack**
- techmeme

### project-management
- **jira**
- **linear**

### sales-and-crm
- contact-goat
- servicetitan-pricebook

### social-and-messaging
- **discord**
- front
- **telegram**
- **twilio**

### travel
- google-flights
- kayak

## A'Space relevance map

| A'Space need | Service in catalog? | Path |
|---|---|---|
| Notion (knowledge base) | ✅ notion | priority 1 (upstream) |
| ClickUp (tasks) | ❌ | use known-spec-urls.md → OpenAPI YAML |
| Airtable (bases) | ❌ | docs scrape (LLM quota) |
| Apollo.io (CRM) | ❌ | Postman conversion |
| Hostinger (VPS) | ❌ | Postman conversion |
| Stripe (payments) | ✅ stripe | priority 1 |
| GitHub | ✅ github | priority 1 (but `gh` CLI already officiel) |
| Supabase | ✅ supabase | priority 1 (but `supabase` CLI déjà officiel) |
| Telegram | ✅ telegram | priority 1 |
| Discord | ✅ discord | priority 1 |
| Slack | ✅ slack | priority 1 |
| Linear | ✅ linear | priority 1 |
| Jira | ✅ jira | priority 1 |

## Refresh procedure

```bash
# List release tags
gh api repos/mvanhorn/printing-press-library/releases --paginate | grep '"tag_name"'

# List a category
gh api repos/mvanhorn/printing-press-library/contents/library/productivity | jq '.[].name'
```

When adding a service here, also update `known-spec-urls.md` if a direct OpenAPI exists upstream (some library entries auto-refresh from a public spec — capture that URL for fallback).
