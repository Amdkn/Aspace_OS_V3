# [A-SPEC][UDM-001] Unified Domain Model, Bounded Contexts & State Ownership

**Objective:** Define the canonical business objects, their meaning, and which bounded context owns their mutation.

Databases, APIs and UIs project this model.
- Not a Supabase schema dump.
- Not a React type inventory.
- Not one universal database.
- Office, Business OS, Mobile and Factory agree on object identity.

---

## Bounded Contexts

1. **Identity & Tenancy**: Manages institutional boundaries, access control, and workspace isolation.
2. **Catalog & Marketing**: Manages market positioning, products, offers, and audience segments.
3. **CRM & Sales**: Manages customer journeys, from lead generation to customer status.
4. **Operations & Fulfillment**: Manages service delivery, bookings, cases, and document workflows.
5. **Billing & Entitlements**: Manages revenue, subscriptions, access rights, and payments.
6. **Orchestration & Fabric**: Manages executable capabilities, workflows, and their cryptographic receipts.

---

## 1. Identity & Tenancy Context

### Tenant
- **Canonical Identifier**: `tenant_id`
- **Aggregate/Bounded Context**: Identity & Tenancy
- **Write Authority**: Tenancy Service / Root Administrator
- **Read Projections**: Global API, Auth Tokens, Local Database Caches
- **Lifecycle/State Owner**: Identity Provider (IdP) / Tenancy Ledger
- **Invariants**: Must have at least one active Workspace and one Root Administrator. Cannot be deleted if active Subscriptions exist.
- **Cross-Context References**: Referenced universally as the isolation boundary.
- **Migration/Version Rules**: Immutable identity. Upgrades via state migration of nested workspaces.

### Workspace
- **Canonical Identifier**: `workspace_id`
- **Aggregate/Bounded Context**: Identity & Tenancy
- **Write Authority**: Tenant Administrator
- **Read Projections**: App State, Session Context
- **Lifecycle/State Owner**: Tenancy Ledger
- **Invariants**: Belongs to exactly one Tenant. Must have a valid name.
- **Cross-Context References**: `tenant_id`
- **Migration/Version Rules**: Soft-delete only. Workspaces can merge via data transfer, not ID aliasing.

### Organization
- **Canonical Identifier**: `organization_id`
- **Aggregate/Bounded Context**: Identity & Tenancy
- **Write Authority**: Identity & Tenancy Context / Root Administrator
- **Read Projections**: Business OS, Marketing, CRM
- **Lifecycle/State Owner**: Identity & Tenancy Context
- **Invariants**: Represents the legal/business entity. Can map to 1-to-N Tenants.
- **Cross-Context References**: `tenant_id`
- **Migration/Version Rules**: Corporate restructuring creates new organizations, maintaining historical ledgers.

### Membership
- **Canonical Identifier**: `membership_id`
- **Aggregate/Bounded Context**: Identity & Tenancy
- **Write Authority**: Workspace Administrator
- **Read Projections**: Access Control Lists (ACLs), UI Menus
- **Lifecycle/State Owner**: Identity Provider / Auth Service
- **Invariants**: Links exactly one User (Identity) to one Workspace with exactly one Role.
- **Cross-Context References**: `workspace_id`, `role_id`, `user_id`
- **Migration/Version Rules**: Ephemeral and append-only state transitions (Revoked/Granted).

### Role
- **Canonical Identifier**: `role_id`
- **Aggregate/Bounded Context**: Identity & Tenancy
- **Write Authority**: IAM (Identity & Access Management) Core
- **Read Projections**: ACLs, Gateway Policies
- **Lifecycle/State Owner**: IAM Core
- **Invariants**: Roles contain an immutable set of capabilities (Entitlements) or permissions.
- **Cross-Context References**: `workspace_id` (if custom), `tenant_id`
- **Migration/Version Rules**: Standard roles are versioned globally. Custom roles are versioned per tenant.

---

## 2. Catalog & Marketing Context

### Brand
- **Canonical Identifier**: `brand_id`
- **Aggregate/Bounded Context**: Catalog & Marketing
- **Write Authority**: Marketing Department / Catalog Service
- **Read Projections**: Public Websites, Product Catalogs
- **Lifecycle/State Owner**: Catalog Service
- **Invariants**: Unique canonical name per Organization.
- **Cross-Context References**: `organization_id`
- **Migration/Version Rules**: Brands are merged via alias maps to the canonical ID.

### Product
- **Canonical Identifier**: `product_id`
- **Aggregate/Bounded Context**: Catalog & Marketing
- **Write Authority**: Product Management System
- **Read Projections**: E-commerce storefronts, Billing systems
- **Lifecycle/State Owner**: Product Catalog Core
- **Invariants**: Belongs to a Brand. Must have a baseline SKU and definition.
- **Cross-Context References**: `brand_id`
- **Migration/Version Rules**: New versions create new Product IDs with lineage to deprecated IDs.

### Offer
- **Canonical Identifier**: `offer_id`
- **Aggregate/Bounded Context**: Catalog & Marketing
- **Write Authority**: Pricing & Promotion Engine
- **Read Projections**: Sales Portals, Checkout Sessions
- **Lifecycle/State Owner**: Promotion Engine
- **Invariants**: Must bind exactly one or more Products to a Price/Currency within a validity window.
- **Cross-Context References**: `product_id`, `audience_id`
- **Migration/Version Rules**: Immutable once published. Revisions require a new Offer ID.

### Audience
- **Canonical Identifier**: `audience_id`
- **Aggregate/Bounded Context**: Catalog & Marketing
- **Write Authority**: Marketing / Segmentation Engine
- **Read Projections**: CRM, Analytics, Ad Platforms
- **Lifecycle/State Owner**: Segmentation Engine
- **Invariants**: Defined by deterministic inclusion rules or explicit member sets.
- **Cross-Context References**: `tenant_id`
- **Migration/Version Rules**: Audience definitions are versioned; members are computed dynamically.

---

## 3. CRM & Sales Context

### Lead
- **Canonical Identifier**: `lead_id`
- **Aggregate/Bounded Context**: CRM & Sales
- **Write Authority**: CRM Intake / Lead Scoring Engine
- **Read Projections**: Sales Funnel, Marketing Automation
- **Lifecycle/State Owner**: CRM Core
- **Invariants**: Represents intent. Cannot have an active Subscription natively (must convert to Customer).
- **Cross-Context References**: `audience_id`, `offer_id`
- **Migration/Version Rules**: Merged leads maintain aliases to the surviving `lead_id`.

### Customer
- **Canonical Identifier**: `customer_id`
- **Aggregate/Bounded Context**: CRM & Sales
- **Write Authority**: CRM Core / Account Management
- **Read Projections**: Billing, Support, Analytics
- **Lifecycle/State Owner**: CRM Core
- **Invariants**: A Customer represents a transacting entity. Must have valid contact details and an associated Tenant.
- **Cross-Context References**: `tenant_id`, `lead_id` (origin)
- **Migration/Version Rules**: Customer records are immutable in history; updates append to a change ledger.

---

## 4. Operations & Fulfillment Context

### Booking
- **Canonical Identifier**: `booking_id`
- **Aggregate/Bounded Context**: Operations & Fulfillment
- **Write Authority**: Scheduling / Logistics Service
- **Read Projections**: Calendars, Customer Portal
- **Lifecycle/State Owner**: Scheduling Service
- **Invariants**: Binds a Time, a Resource, and a Customer. Cannot double-book non-shareable resources.
- **Cross-Context References**: `customer_id`, `product_id` (service)
- **Migration/Version Rules**: Changes to bookings (reschedules) are recorded as a state transition on the same ID.

### Case
- **Canonical Identifier**: `case_id`
- **Aggregate/Bounded Context**: Operations & Fulfillment
- **Write Authority**: Support / ITSM Core
- **Read Projections**: Support Dashboard, Customer Portal
- **Lifecycle/State Owner**: Support Core
- **Invariants**: Must be associated with a Customer or Workspace. Requires a status (Open, Closed, etc.).
- **Cross-Context References**: `customer_id`, `workspace_id`
- **Migration/Version Rules**: History is append-only.

### DocumentRequest
- **Canonical Identifier**: `document_request_id`
- **Aggregate/Bounded Context**: Operations & Fulfillment
- **Write Authority**: Workflow Automation / Compliance Service
- **Read Projections**: Task Lists, User Portals
- **Lifecycle/State Owner**: Compliance Service
- **Invariants**: Must point to an expected Document schema. Requires a status and due date.
- **Cross-Context References**: `case_id`, `customer_id`
- **Migration/Version Rules**: Re-requests generate new `document_request_id` to preserve audit trails.

---

## 5. Billing & Entitlements Context

### Payment
- **Canonical Identifier**: `payment_id`
- **Aggregate/Bounded Context**: Billing & Entitlements
- **Write Authority**: Payment Gateway / Financial Ledger
- **Read Projections**: Invoices, CRM, Analytics
- **Lifecycle/State Owner**: Financial Ledger
- **Invariants**: Immutable record of transaction. Tied to a specific Currency and Amount.
- **Cross-Context References**: `customer_id`, `subscription_id`
- **Migration/Version Rules**: Cannot be modified. Corrections require compensatory payments/refunds.

### Subscription
- **Canonical Identifier**: `subscription_id`
- **Aggregate/Bounded Context**: Billing & Entitlements
- **Write Authority**: Billing Engine
- **Read Projections**: Access Control, CRM, Customer Portal
- **Lifecycle/State Owner**: Billing Engine
- **Invariants**: Connects a Customer to an Offer. Must have a defined term and payment state.
- **Cross-Context References**: `customer_id`, `offer_id`
- **Migration/Version Rules**: Upgrades/Downgrades append a new term to the same `subscription_id` or generate a new one based on contract type.

### Entitlement
- **Canonical Identifier**: `entitlement_id`
- **Aggregate/Bounded Context**: Billing & Entitlements
- **Write Authority**: Subscription & Provisioning Engine
- **Read Projections**: IAM, Capabilities Router, Product Surfaces
- **Lifecycle/State Owner**: Provisioning Engine
- **Invariants**: Grants a specific right or quota based on an active Subscription. If the Subscription ends, Entitlement state must transition to inactive.
- **Cross-Context References**: `subscription_id`, `workspace_id`
- **Migration/Version Rules**: Ephemeral projection of the Subscription contract.

---

## 6. Orchestration & Fabric Context

### Workflow
- **Canonical Identifier**: `workflow_id`
- **Aggregate/Bounded Context**: Orchestration & Fabric
- **Write Authority**: Workflow Orchestrator
- **Read Projections**: Automation Logs, Task Monitors
- **Lifecycle/State Owner**: Workflow Orchestrator
- **Invariants**: Must consist of defined states and capabilities. Execution cannot violate Tenant isolation.
- **Cross-Context References**: `tenant_id`, `capability_id`
- **Migration/Version Rules**: Schema is versioned (`workflow_id_v2`). In-flight executions complete on the version they started with.

### Capability
- **Canonical Identifier**: `capability_id`
- **Aggregate/Bounded Context**: Orchestration & Fabric
- **Write Authority**: Capability Fabric / System Registry
- **Read Projections**: API Gateways, Agent Planners
- **Lifecycle/State Owner**: System Registry
- **Invariants**: Represents an executable function. Must expose required Entitlements to be invoked.
- **Cross-Context References**: `entitlement_id`
- **Migration/Version Rules**: Semver versioning. Breaking changes require a new `capability_id`.

### EffectReceipt
- **Canonical Identifier**: `receipt_id`
- **Aggregate/Bounded Context**: Orchestration & Fabric
- **Write Authority**: Execution Kernel
- **Read Projections**: Audit Logs, Data Lineage
- **Lifecycle/State Owner**: Execution Kernel
- **Invariants**: Cryptographically verifiable proof of execution. Immutable upon creation.
- **Cross-Context References**: `capability_id`, `workspace_id`
- **Migration/Version Rules**: Never migrated. Purely append-only permanent audit log.
