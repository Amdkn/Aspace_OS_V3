---
ldxx: LD04_Cognition
domain: 03_IT
canonical_name: System Design 101 — APIs, Databases, Caching, CDNs, Load Balancing, Production Infra
type: guide-premium
maturity: solid
source_video_id: oYxTTirKY8M
source_url: https://youtu.be/oYxTTirKY8M
channel: Hayk Simonyan
duration_min: 180
fetched_at: 2026-06-25
transcript_chars: 152321
author_role: A3 Tilly (LD04 Cognition H30)
ldxx_mirror: ld04_cognition/system_design_101.md
ld: LD07_Creativity_Reno
b2_owner: cyborg-it
sister_b1: jerry-prime
---

# System Design 101 — Le Manuel de Production pour Ingénieurs IA-Native

> **Résumé exécutif** : Dans un monde où l'IA écrit l'implémentation ligne-à-ligne, la valeur migre vers la **capacité de designer le système entier** — APIs, bases de données, caching, CDN, load balancing, observabilité. Cette vidéo de 3 heures de Hayk Simonyan est le manuel condensé qu'un Senior+ doit internaliser pour rester pertinent dans l'ère agentic.

## 1. Vision Globale — Pourquoi le System Design est Le Skill #1 Post-IA

Hayk Simonyan ouvre sur un constat brutal : **chaque ingénieur utilise désormais l'IA pour écrire du code**. Les entreprises savent. Les entretiens tech ont pivoté. La question n'est plus "sais-tu coder cette fonction ?" mais "**comprends-tu comment les composants dialoguent à haut niveau, et peux-tu designer le système from scratch ?**".

C'est exactement la doctrine **Solarpunk / Agentic Governance** posée par les ADR-ICP-SOLARIS-001 / NEXUS-001 / ORBITER-001 ratifiés 2026-06-24 : l'IA accélère l'exécution, l'humain doit détenir l'**architecture de gouvernance**. Ce guide est le pendant **03_IT** (infrastructure) de cette doctrine.

**Trois lois cadres** que toute la vidéo installe :
1. **No single point of failure** — chaque composant critique doit avoir son failover.
2. **Horizontal > Vertical** — scale out (ajouter des nœuds) plutôt que scale up (grossir un nœud).
3. **Caching everywhere it's safe** — la latence la moins chère est celle qu'on évite.

## 2. APIs — Le Contrat Qui Survit à Tout

Hayk distingue **4 styles d'API** avec leurs tradeoffs systémiques :

| Style | Cas d'usage | Latence | Couplage | Verdict A0 |
|---|---|---|---|---|
| **REST** | CRUD public, documentation large | Moyenne | Fort (schéma) | ✅ Défaut raisonnable |
| **GraphQL** | Front-ends flexibles (mobile multi-vue) | Moyenne | Faible côté client | ✅ Mobile first (Orbiter ICP) |
| **gRPC** | Service-to-service, schemas stricts | Très faible | Fort (protobuf) | ✅ Backend Solaris ICP |
| **WebSocket / SSE** | Real-time push | Très faible (stateful) | Moyen | ⚠️ Complexité opérationnelle |

**Idempotency keys** : non-négociable pour tout endpoint de mutation exposé à un client qui retry (mobile, agent LLM). Sans cela, un retry réseau = double paiement, double post.

**Versioning** : préfixer l'URL (`/v1/`, `/v2/`) plutôt que header. L'URL est l'API visible ; le header est négociable. La règle Hayk : **ne jamais casser un contrat client sans 6 mois deprecation window**.

**Rate limiting** : Token Bucket > Leaky Bucket pour 95% des cas (burst-friendly). Réponse standard : `429 Too Many Requests` + header `Retry-After`.

## 3. Databases — Le Cœur Qui Pompe Ou Qui Étrangle

**SQL vs NoSQL** n'est pas un débat idéologique — c'est un tradeff de **cohérence vs latence vs scalabilité** :

- **PostgreSQL** (SQL relationnel) → **golden path** par défaut. ACID, JSON columns pour flexibilité, extensions (PostGIS, pgvector, TimescaleDB). Cas Hayk : 90% des SaaS early-stage. Cas A0 : Life-OS-2026 stack canon.
- **MongoDB** (document) → schémas évolutifs rapides, mais perte de garanties fortes. À éviter si les relations sont nombreuses.
- **Cassandra / ScyllaDB** (wide-column) → write-heavy, multi-DC, eventual consistency. Stack Netflix / Instagram scale.
- **Redis** (in-memory KV) → caching + pub/sub + leaderboard. **Pas une base primaire.**
- **DynamoDB** (managed KV) → serverless scale-to-zero. Vendor lock-in AWS.

**Replication topologies** :
- **Single leader + read replicas** → défaut. Write sur leader, read distribué. Lag acceptable pour lecture.
- **Multi-leader** → fusion complexe, last-write-wins perd des données. Rarement justifié sauf offline-first mobile.
- **Leaderless (Dynamo-style quorum)** → haute dispo, eventual consistency. Coût opérationnel élevé.

**Sharding** : choisir sa **shard key** comme un mariage — divorce impossible sans downtime. Hayk insiste : **toujours inclure le tenant_id dans la clé** pour multi-tenancy.

**Connection pooling** : PgBouncer en transaction-pooling mode. Ne **jamais** ouvrir une connexion par requête en serverless — c'est le chemin le plus court vers le timeout.

## 4. Caching — L'Art de Ne Pas Répondre

**Hiérarchie L1 → L5** :

1. **L1 in-process** (Map locale, LRU bounded) — sous-microseconde, mais **non partagé entre instances**.
2. **L2 Redis cluster** — ~1ms, partagé, eviction LRU/LFU. **Standard production.**
3. **L3 CDN edge cache** — ~10ms, géographique, **stale-while-revalidate**.
4. **L4 DB query cache** (Materialized views, pg_views) — niveau SQL, refresh incrémental.
5. **L5 Browser cache + Service Worker** — côté client, ETag + `Cache-Control: max-age`.

**Cache invalidation** : le **2e problème le plus dur** en CS (après naming). Patterns Hayk :

- **TTL seul** → simple, mais fenêtre d'incohérence.
- **Write-through** → DB + cache synchrones, latence d'écriture x2.
- **Write-behind** → cache d'abord, async DB. Risque perte si cache crashe.
- **Cache-aside (lazy)** → lecture : check cache → miss → DB → set cache. **Défaut pragmatique.**

**Cache stampede** : 1000 requêtes miss simultanées sur la même clé = 1000 hits DB. Mitigation : **single-flight** (mutex distribué), **probabilistic early expiration** (rafraîchir avant TTL avec probabilité croissante).

## 5. CDN — La Peau Géographique Du Système

Un CDN n'est pas qu'un cache statique. Hayk distingue :

- **Static CDN** (Cloudflare, CloudFront, Fastly) — images, JS, CSS, fonts.
- **Dynamic CDN** (Cloudflare Workers, Fastly Compute@Edge) — **exécuter du code au edge**, personalization, A/B test, geofencing.

**Cache key** : par défaut `(host, path)`. Personnalisation = fragmenter le cache (rarement justifié au-delà de la langue).

**Purge** : invalidation rapide via API (< 30s idéal). Préférer **surrogate-key tagging** plutôt que purge URL-by-URL.

**Origin shield** :中间层 CDN ↔ origin pour absorber les misses en burst. Évite que l'origin se fasse DDoS-er par son propre CDN.

## 6. Load Balancing — Le Bureau D'orientation Du Trafic

**L4 vs L7** :
- **L4 (TCP/UDP)** → bas niveau, ultra-rapide, hashing par IP:port. AWS NLB.
- **L7 (HTTP)** → routage par path/host/header/cookie, TLS termination, retry policies. AWS ALB, HAProxy, Envoy.

**Algorithmes** :
- **Round-robin** → équilibre uniforme,假设 nœuds homogènes (rarement vrai).
- **Weighted round-robin** → 容错 matériel hétérogène.
- **Least connections** → meilleur pour connexions longues (WebSocket).
- **Consistent hashing** → sticky session sans état serveur (memcached, Cassandra).

**Health checks** : actif (HTTP probe) + passif (suivre le taux d'erreur réel). **Actif seul** détecte un serveur vivant qui répond 500. **Passif seul** détecte tard.

**Circuit breaker** : après N échecs, ouvrir le circuit (fail fast) pendant T secondes. Patterns : half-open pour试探 recovery. **Indispensable** pour cascades de failures (services qui dépendent d'autres services).

## 7. Observability — Les Trois Piliers

Hayk insiste : **logs ≠ metrics ≠ traces**. Les trois sont nécessaires.

- **Metrics** (Prometheus, Datadog) — numériques, time-series, alerting. Cardinalité bornée.
- **Logs** (structured JSON, ELK / Loki) — événements discrets, debugging. **Jamais** logger en plain text en prod.
- **Traces** (OpenTelemetry, Jaeger, Tempo) — causalité inter-services. **W3C Trace Context** standard.

**SLI / SLO / Error Budget** :
- **SLI** = mesure (ex: p99 latency < 200ms).
- **SLO** = objectif (99.9% des requêtes).
- **Error budget** = 0.1% = 43min/mois. Quand le budget est épuisé → **freeze des features, focus reliability**.

**RED method** (Rate / Errors / Duration) pour services. **USE method** (Utilization / Saturation / Errors) pour infra.

## 8. Capstone — Le Design Doc Que Tu Dois Écrire Avant De Coder

La vidéo conclut sur le **deliverable** : un design doc de 2-5 pages contenant :

1. **Requirements** — fonctionnels (user stories) + non-fonctionnels (latence, throughput, dispo cible).
2. **Capacity estimation** — back-of-envelope : QPS, storage, bandwidth. Hayk donne un cadre : 10x headroom sur la charge attendue.
3. **High-level diagram** — boxes + arrows. **Pas un diagramme UML complet**, juste les composants et leurs interfaces.
4. **Data model** — schéma des tables/collections principales + index critiques.
5. **API contracts** — endpoints + request/response shapes (exemples JSON).
6. **Tradeoffs** — 3-5 décisions architecturales avec rationale. **C'est la partie senior.**
7. **Failure modes** — que se passe-t-il si X tombe ? Quelle dégradation acceptable ?
8. **Rollout plan** — feature flags, canary %, monitoring pre/post.

**Anti-patterns à éviter dans ton design** :
- "On verra à l'échelle" → capacity estimation **maintenant**.
- "Kafka partout" → ajouter un broker quand le besoin est prouvé (YAGNI).
- "Microservices from day 1" → **monolith first**, extract quand la douleur est mesurée.
- "NoSQL parce que scale" → 95% des cas Postgres suffit.

---

## 📚 Ressources Pour Aller Plus Loin

- **Designing Data-Intensive Applications** (Martin Kleppmann) — la bible.
- **System Design Interview Vol 1 & 2** (Alex Xu) — patterns canoniques.
- **ByteByteGo** (YouTube + blog) — companion visuel de la vidéo.
- **High Scalability** blog — post-mortems réels.

## 🎯 Action Item Pour Cette Semaine

Si tu es junior → faire **3 design docs** sur des systèmes réels (Twitter feed, Uber dispatch, Stripe payments) avec la structure ci-dessus. Soumettre à senior review.

Si tu es senior → coacher **2 juniors** sur leur premier design doc. Le senior-ing n'est pas une promotion, c'est une posture.

Si tu es staff/principal → rédiger **le design doc canon** d'un service que toute l'équipe utilise. Poser le standard.

---

*Geordi-curated • Antigravity Premium Standard 8 sections • LD04 Cognition 03_IT bridge • H30 30-day learning arc*
