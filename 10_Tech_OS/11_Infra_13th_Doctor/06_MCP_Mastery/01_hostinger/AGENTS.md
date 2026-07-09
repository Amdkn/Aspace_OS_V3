# 01_hostinger — DOX leaf for Hostinger MCP

> Parent: `../AGENTS.md`. Framework: `../../06_MCP_Mastery_dox/AGENTS.md`.
> Canon: vault = `HOSTINGER_API_TOKEN` (Windows env User). NEVER in `.md`/`.json`/git/MCP args.

## Purpose

The Hostinger MCP is the **DNS + domain registry + VPS inventory** plane of A'Space OS.
Every sslip.io subdomain (`*.148.230.92.235.sslip.io`), every registered domain, and the VPS
list at Hostinger pass through it. No public-facing record is changed without going through this
contract.

## Ownership

- A0 Amadeus — approves any record tied to a production domain.
- A2 Claude Code — orchestrates DNS changes.
- A3 sub-agent — runs `mcp__hostinger__*` calls.

## Local Contracts

### Auth

- Env var: `HOSTINGER_API_TOKEN` (Windows env User). NEVER in `.md`/`.json`/git/MCP args.
- MCP server: `hostinger-api-mcp` binary at `/c/Users/amado/AppData/Roaming/npm/hostinger-api-mcp` (local).
- Provider: `hpanel.hostinger.com`.

### REST API fallback (canonical when MCP unavailable)

When `mcp__hostinger__*` is not configured in the session, use the REST API directly with the
same `HOSTINGER_API_TOKEN`. The MCPs on VPS `aspace-vps` (`~/.nvm/versions/node/v24.15.0/lib/node_modules/hostinger-{api,billing,dns,domains,hosting,reach,vps}-mcp`) and the REST API share the same token.

- **Base URL** : `https://developers.hostinger.com` (NOT `api.hostinger.com` — returns 530/1016).
- **Auth** : `Authorization: Bearer <HOSTINGER_API_TOKEN>`.
- **Zone read** : `GET /api/dns/v1/zones/{domain}`.
- **Zone write (canonical)** : `PUT /api/dns/v1/zones/{domain}` with the FULL zone payload. **There is no `POST /records` endpoint.** Any record missing from the PUT is deleted.
- **Reference pattern** (proven 2026-06-13 for `abc-os.kalybana.com`):
  1. `GET /api/dns/v1/zones/kalybana.com` → fetch current zone
  2. Append the new record to the array
  3. `PUT /api/dns/v1/zones/kalybana.com` with the full modified array
  4. `GET /api/dns/v1/zones/kalybana.com` → verify

See [[../../../.claude/projects/C--Users-amado/memory/project_hostinger_api|project-hostinger-api]] memory for full detail.

### Capabilities (live, 2026-06-10)

| Tool | Read | Write | Destructive |
|------|------|-------|-------------|
| listDomains | ✅ | — | — |
| getDomain | ✅ | — | — |
| listDNSRecords | ✅ | — | — |
| createDNSRecord | — | ✅ | — |
| updateDNSRecord | — | ✅ | — |
| deleteDNSRecord | — | — | ✅ HITL |
| listVPS | ✅ | — | — |
| getVPS | ✅ | — | — |
| restartVPS | — | ✅ | ✅ HITL (affects all live services) |

### Rate limit

5 requests/second observed. The MCP client retries on 429 — but always back off and stagger
batch operations (`sleep 0.25` between record creates).

## Work Guidance

### W1 — Read existing records before any change

```ts
// Before adding an A record, read the zone:
const zone = await mcp__hostinger__listDNSRecords({ domain: 'aspace.fr' });
// Check for stale records pointing to old IPs.
```

### W2 — sslip.io for subdomains

We do NOT manage DNS for `*.sslip.io` (it's a public wildcard resolver). We only manage
the apex `aspace.fr` and any sub-A-records pointing to `148.230.92.235`. The `sslip.io` part
is just a hostname trick.

### W3 — Propagation awareness

Hostinger DNS propagation is 1–5 min usually, up to 30 min for some resolvers. After
`createDNSRecord`, do **not** retry on a 409/duplicate within 30 min — it's almost always
a stale local cache, not a real conflict.

### W4 — Destructive ops

- `deleteDNSRecord` — HITL gate. Always confirm A0 wants the record gone, not just edited.
- `restartVPS` — HITL gate. This kills every container on the VPS. The right tool for a
  single container restart is `ssh aspace-vps docker restart <name>`, not Hostinger.

### W5 — Canonical pattern: PUT zone-replacement (no incremental endpoint)

The Hostinger API v1 has no `POST /zones/{domain}/records` endpoint. To add a record, the
canonical path is **PUT zone-replacement** with the full payload. Cost of getting this wrong:
the next `GET` returns a partial zone and any record you forgot to include is **silently
deleted**. Always back up the current zone first.

```bash
# 1. Back up current zone
curl -sS -H "Authorization: Bearer $HOSTINGER_API_TOKEN" \
  "https://developers.hostinger.com/api/dns/v1/zones/kalybana.com" \
  > /tmp/kalybana-zone-backup-$(date +%Y%m%d-%H%M%S).json

# 2. Read the zone, append your record, PUT it back
#    (use python/jq for the array manipulation)
python3 << 'PY'
import json, urllib.request, os
token = os.environ["HOSTINGER_API_TOKEN"]
domain = "kalybana.com"

# Read
req = urllib.request.Request(
    f"https://developers.hostinger.com/api/dns/v1/zones/{domain}",
    headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
)
zone = json.loads(urllib.request.urlopen(req).read())

# Append new record (example: CNAME for a new Vercel subdomain)
zone.append({
    "type": "CNAME",
    "name": "abc-os",
    "ttl": 300,
    "records": [{"content": "cname.vercel-dns.com", "is_disabled": False}],
})

# Write
req = urllib.request.Request(
    f"https://developers.hostinger.com/api/dns/v1/zones/{domain}",
    data=json.dumps(zone).encode(),
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    },
    method="PUT",
)
resp = urllib.request.urlopen(req)
print(f"PUT {resp.status} {resp.reason}")
PY

# 3. Verify the new record is there
curl -sS -H "Authorization: Bearer $HOSTINGER_API_TOKEN" \
  "https://developers.hostinger.com/api/dns/v1/zones/kalybana.com" | \
  python3 -c "import sys,json; z=json.load(sys.stdin); print([r for r in z if r.get('name')=='abc-os'])"
```

**Why this matters** : the first instinct is `POST /records` (REST convention). That returns
404 on Hostinger, not 405 — so a sub-agent will re-derive the PUT workaround every time
unless this section is in the contract. This is the most expensive re-derivation in the
Hostinger path (~10 min lost per occurrence).

## Verification

```bash
# Confirm the token is in env and the MCP can list domains:
ssh aspace-vps "echo $HOSTINGER_API_TOKEN" 2>/dev/null   # echo nothing in prod; just confirm not empty
mcp__hostinger__listDomains()
# Expect: status=ok, 1+ domain
```

## Child DOX Index

This leaf has no sub-domains yet. If a separate contract emerges for "DNS records" vs
"VPS inventory", split here and reference from the root.
