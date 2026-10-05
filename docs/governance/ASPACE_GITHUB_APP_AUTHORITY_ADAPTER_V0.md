# A'Space GitHub App Authority Adapter v0

Status: DESIGN / REGISTRATION CANARY

Répartition cible et promotions proposées le 2026-10-05 : [Capacités permanentes et promotions organisées v1](ASPACE_GITHUB_APP_CAPACITY_AND_PROMOTION_V1.md). Le profil initial ci-dessous est historique ; il ne définit pas un plafond institutionnel définitif. La v1 n'est pas encore appliquée aux Apps.
Parent: #555
Gateway parent: #544 / #542

## 1. Why a GitHub App

A'Space must not treat one personal OAuth token as a universal GitHub identity.

The Gateway needs explicit authority planes:

```
GitHub
├─ repository resources
│  └─ GitHub App installation token
├─ user-owned resources
│  └─ GitHub App user-to-server token when supported/authorized
└─ control-plane events
   └─ signed GitHub App webhooks
```

This lets A'Space separate:
- institutional holon identity;
- runtime/provider identity;
- GitHub App identity;
- human user authority;
- repository installation authority.

## 2. Token model

### App JWT

Used only to authenticate the GitHub App itself and mint installation access
tokens.

Properties:
- signed from the App private key;
- very short lived;
- never used as a general repository token;
- private key never enters git.

### Installation access token

Primary machine-to-GitHub authority for repository-native effects.

Use for:
- Issues;
- Pull Requests;
- Checks;
- repository Contents;
- Discussions where supported by granted permissions;
- Actions/readback;
- other explicitly granted repository resources.

Properties:
- repository-bounded by the installation;
- permissions cannot exceed the App installation;
- short lived;
- should be minted on demand and discarded.

### User access token

Only for effects that genuinely belong to the human/user authority plane.

Use only after explicit user authorization and only where GitHub exposes the
required account-level resource to the GitHub App.

This is the candidate authority for Amdkn personal Projects V2 #9 and #12.
The canary must prove the actual GitHub behavior; do not infer parity from
repository installation permissions.

## 3. Least-privilege registration profile

Initial repository permissions:

| Permission | Initial level | Reason |
|---|---|---|
| Metadata | Read | Required repository identity |
| Issues | Read/Write | executable cells + return_to |
| Pull requests | Read/Write | mutation/evidence |
| Checks | Read/Write | deterministic gate projection |
| Actions | Read | workflow truth/readback |
| Contents | Read | canon/evidence readback |
| Discussions | Read/Write | RFC/exploration bridge |
| Workflows | None initially | enable only if Gateway must mutate workflows |
| Administration | None | forbidden until a concrete endpoint proves need |

Do not grant broad permissions for convenience.

## 4. Webhook ingress

Minimum subscribed event families:

- `issues`
- `issue_comment`
- `pull_request`
- `pull_request_review`
- `check_run`
- `check_suite`
- `workflow_run`
- `discussion`
- `discussion_comment`
- `installation`
- `installation_repositories`

Webhook envelope:

```
X-GitHub-Delivery
X-GitHub-Event
X-Hub-Signature-256
       ↓
SignatureVerifier
       ↓
DeliveryDedupe
       ↓
GitHubIngressNormalizer
       ↓
InterFabricEnvelope.v1
       ↓
Nardole / Capability Fabric / HostPolicy
```

Rules:
- verify HMAC before parsing intent;
- delivery ID is the first dedupe key;
- preserve repository / installation / sender / event type as evidence;
- downstream UNKNOWN is never converted to blind retry;
- every effect carries `return_to`.

## 5. Runtime neutrality

The GitHub App is not an agent.

It is an authority + event adapter of A'Space Gateway.

A GitHub event resolves:

```
event
→ capability_need
→ institutional holon
→ authority
→ admissible runtime
→ execution
→ evidence
→ GitHub egress
```

Hermes, Codex, Antigravity, Jules, Claude or a future runtime may execute the
work. The GitHub App must not encode provider identity into the mission.

## 6. Secret handling

Never commit:
- App private key;
- webhook secret;
- installation token;
- user access token;
- refresh token.

Target secret homes:
- local development: OS credential store / dedicated secret manager;
- GitHub Actions: repository/environment secret only when repository-scoped
  execution genuinely needs it;
- sovereign Gateway: runtime secret store behind HostPolicy.

A private key is root material. Derived installation tokens are disposable.

## 7. Registration canary

1. Register private App: **A'Space Gateway**.
2. Install it only on `Amdkn/Aspace_OS_V3`.
3. Start with minimal repository permissions.
4. Generate one private key and store it outside git.
5. Mint App JWT.
6. Resolve installation ID.
7. Mint installation token.
8. Read repository metadata.
9. Write one bounded test comment/check through the App.
10. Receive one signed webhook and prove HMAC + delivery dedupe.
11. Test personal Projects #9/#12 with the correct GitHub App authority type.
12. Persist receipt in #555.
13. Delete/revoke transient test material.

## 8. Project V2 authority experiment

Current proven truth:
- authenticated `gh` user authority can mutate Projects #9/#12;
- repository `GITHUB_TOKEN` cannot.

The GitHub App canary must distinguish three cases:

1. installation token can mutate the user project;
2. user-to-server token can mutate the user project;
3. GitHub does not expose equivalent authority for that personal-project path.

Case 3 is not a failure of the Gateway. It is an explicit authority boundary.

## 9. Acceptance

PASS requires:
- App registered privately;
- installed on selected repository only;
- no personal PAT required for repository-native automation;
- private key absent from git;
- installation token TTL + repository scope proven;
- signed webhook accepted;
- duplicate delivery rejected/idempotently absorbed;
- one App-authored bounded mutation succeeds;
- personal Project V2 behavior empirically classified;
- evidence attached to #555 and returned to #544.

## 10. Non-goals

- GitHub App is not WorkGraph.
- GitHub App is not Nardole.
- GitHub App is not the Capability Fabric.
- GitHub App is not the institutional identity of A'Space.
- GitHub App does not receive blanket administration rights.
