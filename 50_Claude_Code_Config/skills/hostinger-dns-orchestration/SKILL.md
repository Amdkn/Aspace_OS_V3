---
name: hostinger-dns-orchestration
description: Orchestrate Hostinger DNS zone management via the official `hostinger-dns-mcp` MCP (part of `hostinger-api-mcp` v0.2.14+ family). Use this skill when the user says "add a DNS record", "point a domain to Vercel", "list my domains", "check DNS propagation", "create an A record", "create a CNAME", "delegate a subdomain", or any DNS operation on a Hostinger-registered domain. Triggers on "hostinger", "DNS", "A record", "CNAME", "TXT", "MX", "domain delegation", "DNS propagation". Auth = `HOSTINGER_API_TOKEN` (Bearer token from https://hpanel.hostinger.com → API tokens), set via Test Key Pragma. We use the DNS-SPECIALIZED MCP (`hostinger-dns-mcp`, not the full `hostinger-api-mcp`) to stay under the 100-tool IDE limit.
---

# /hostinger-dns-orchestration — DNS via Hostinger specialized MCP

## Why DNS-only MCP not the full Hostinger suite
- Full `hostinger-api-mcp` package exposes **118 tools** across 8 subdomains (VPS, DNS, billing, domains, e-commerce, horizons, hosting, reach). This **crashes the 100-tool IDE limit** in Claude Code (per `Hostinger_God_Mode.md` §1).
- The same package ships focused bins: `hostinger-dns-mcp`, `hostinger-vps-mcp`, `hostinger-domains-mcp`, etc. Each is ~25-35 tools.
- For DNS work (our primary use case), `hostinger-dns-mcp` is the right choice. Add `hostinger-vps-mcp` later when we touch VPS APIs.

## MCP wiring (verified 2026-06-16)
- Server: `hostinger-dns-mcp@latest` (npm, MIT, official Hostinger team `devs@hostinger.com`)
- Wired in `.mcp.json` as `"hostinger-dns"` (NEW 2026-06-16)
- Auth: `HOSTINGER_API_TOKEN` env var User scope (Bearer token, rotate per Test Key Pragma)
- Transport: stdio via `npx -y hostinger-dns-mcp@latest`

## Preconditions (verify first)

| Check | Command | Pass criterion |
|---|---|---|
| Token valid | Call `mcp__hostinger-dns__list_dns_zones` (or equivalent) | returns ≥ 1 zone (your registered domains) |
| Domain registered on Hostinger | Inspect zones list | domain present |
| DNS not delegated away | Check NS records | if NS points to another registrar, you can READ but not WRITE here |

> If the token is wrong, calls return 401 with `"message": "Unauthenticated"`. Rotate via Test Key Pragma.

## Tool catalogue (hostinger-dns-mcp, ~25-35 tools)

### Zone discovery
- `list_dns_zones` — all zones (domains) the token can manage
- `get_dns_zone` — single zone details (name, records count, status, expiry)
- `get_dns_zone_records` — all records in a zone, paginated
- `get_dns_record` — single record details

### Record CRUD
- `create_dns_record` — A / AAAA / CNAME / MX / TXT / NS / SRV / CAA (HITL for high-impact: apex A, MX, NS)
- `update_dns_record` — modify an existing record
- `delete_dns_record` — DESTRUCTIVE (HITL double-convocation)
- `bulk_update_dns_records` — apply N changes in one call (for migrations)

### Validation
- `validate_dns_record` — pre-flight check (is the value a valid IP? a valid hostname?)
- `check_dns_propagation` — query public resolvers (Cloudflare, Google, Quad9) and report propagation %

## Common workflows

### Point a domain to Vercel (apex + www)

```
1. list_dns_zones  # find the zone for <your-domain>
2. For apex (root):
   - update_dns_record({ zone, id: <A-record-id>, value: "76.76.21.21", type: "A" })
3. For www subdomain:
   - create_dns_record({ zone, name: "www", type: "CNAME", value: "cname.vercel-dns.com" })
4. validate_dns_record({ zone, name: "www", type: "CNAME", value: "cname.vercel-dns.com" })
5. check_dns_propagation({ zone, type: "A", name: "@" })
   # → expect 100% within 60s (Vercel's TTL is 60s)
```

> Vercel's recommended apex A record: `76.76.21.21`. Vercel handles `www` redirect automatically if you set the domain in the Vercel dashboard first.

### Add a TXT record (SPF, DKIM, DMARC, domain verification)

```
create_dns_record({
  zone: "<your-domain>",
  name: "@",  # root
  type: "TXT",
  value: "v=spf1 include:_spf.google.com ~all"
})
```

### Verify a domain for a third-party service (Notion, Supabase, Vercel)

Most services give you a TXT value like `notion-verification=abc123` or `supabase-domain-verification=xyz789`:

```
create_dns_record({ zone, name: "@", type: "TXT", value: "<the-verification-value>" })
# then check the service's UI to confirm
```

## Gotchas (D6 paid for)

| Symptom | Root cause | Fix |
|---|---|---|
| `create_dns_record` returns 422 | Invalid record format (e.g. value is not a valid IP for A record) | Use `validate_dns_record` first, fix the value |
| `update_dns_record` returns 404 | Wrong `id` — Hostinger IDs are NOT sequential | Re-fetch via `get_dns_zone_records` first |
| TTL is forced to 3600 | Some TLDs (e.g. `.fr`) require minimum 3600s TTL | Accept the lag or migrate to a more flexible TLD |
| DNS shows "managed elsewhere" | Domain's NS records point to another registrar | Change NS at the current registrar first, OR transfer the zone to Hostinger (separate workflow) |
| `check_dns_propagation` shows < 50% after 5 min | Cached resolvers (some ISPs cache for 1h) | Wait or use a different resolver manually: `dig @1.1.1.1 <your-domain>` |

## Record-type quick reference

| Type | Use case | Value format | HITL required? |
|---|---|---|---|
| A | IPv4 address | `76.76.21.21` | YES for apex A (changes the site) |
| AAAA | IPv6 address | `2606:4700:4700::1111` | YES for apex AAAA |
| CNAME | Alias to another hostname | `cname.vercel-dns.com` | NO (subdomain only, cannot conflict with apex) |
| MX | Mail server | `10 mail.example.com.` | YES (breaks email if wrong) |
| TXT | Verification / SPF / DKIM | `"v=spf1 ..."` (with quotes) | NO |
| NS | Authoritative nameservers | `ns1.example.com.` | YES (breaks DNS resolution if wrong) |
| SRV | Service locator | `0 5 5060 sip.example.com.` | NO |
| CAA | Restrict which CAs can issue certs | `0 issue "letsencrypt.org"` | NO |

## Auth & token rotation

- `HOSTINGER_API_TOKEN` from https://hpanel.hostinger.com → Account → API tokens
- Required scope: **VPS Management** + **DNS** (check both — tokens created via "New Token" button often lack DNS scope implicitly per `Hostinger_God_Mode.md` §1)
- To rotate: A0 generates new token (with correct scope) → pastes in chat → agent sets env var User scope → A0 revokes old
- **NEVER** inline the token in `.mcp.json` (use env var, Test Key Pragma doctrine)

## What this skill does NOT do

- ❌ Register a new domain (UI-only on hpanel.hostinger.com)
- ❌ Transfer a domain between registrars (UI workflow)
- ❌ DNS-level rate limiting / DDoS protection (use Cloudflare in front, or Hostinger's CDN)
- ❌ DNSSEC signing (not exposed via the API)
- ❌ Wildcard records (`*.example.com`) — supported but not via this MCP; use hpanel UI

## Related

- Skill `Hostinger_God_Mode` (legacy) — VPS-focused (snapshots, firewall, Monarx); see `~/.skills/Hostinger_God_Mode.md`
- ADR-SECNET-001 — DNS architecture (kalybana.com, supabase.kalybana.com, Caddy reverse proxy)
- `wiki/hand_offs/handoff_business_os_resumption_2026-06-16.md` — architecture pivot (Vercel + Supabase Cloud + Coolify on Hostinger VPS)
