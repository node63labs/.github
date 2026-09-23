# NODE63 Labs

**Building secure cloud platforms, operational systems, and vertical software.**

NODE63 Labs is a technology company focused on **platform engineering, cloud infrastructure, secure automation, developer tooling, and operational software**.

We build independent products on top of a governed engineering foundation, with clear boundaries between reusable technical capabilities and product-specific domain authority.

> **Clear boundaries. Reproducible systems. Evidence-backed engineering.**

---

## Products

### Lariba Cloud

**Lariba Cloud** is an operational control plane for cloud and operational systems.

It is designed to help teams understand activity, coordinate systems, automate bounded actions, and retain evidence of what happened.

**Govern · Orchestrate · Prove**

Lariba Cloud also provides reusable platform capabilities that can support other NODE63 products without absorbing their domain authority.

#### Public developer resources

| Repository | Purpose |
| --- | --- |
| [`lariba-spec`](https://github.com/node63labs/lariba-spec) | Public API specifications, schemas, and contracts |
| [`lariba-sdk-js`](https://github.com/node63labs/lariba-sdk-js) | JavaScript / TypeScript SDK for Lariba Cloud integrations |
| [`lariba-docs-site`](https://github.com/node63labs/lariba-docs-site) | Developer documentation and integration guidance |

Additional SDKs, tooling, examples, and developer resources may be published as the ecosystem evolves.

### MedicamentOS

**MedicamentOS** is operational software for modern pharmacy workflows.

It is being designed around reliable day-to-day operations, inventory and stock workflows, pharmacy-domain control, and a clear separation between shared technical infrastructure and pharmacy business authority.

---

## Platform Engineering

Across NODE63 Labs, reusable technical capabilities are developed behind explicit contracts and ownership boundaries.

Current platform areas include:

- identity and authentication primitives
- service and environment identity
- permission and authorization foundations
- secrets isolation
- event contracts, ingestion, and routing
- observability and operational evidence
- release and execution provenance
- SDKs, APIs, and integration tooling

Reusable infrastructure may be shared across products. **Product-specific business rules and domain authority remain inside the product that owns them.**

---

## Open Developer Ecosystem

NODE63 Labs publishes selected developer-facing components so developers can integrate with our products without exposing proprietary production internals.

Public resources may include:

- API specifications and schemas
- SDKs and client libraries
- developer documentation
- integration examples and starter projects
- selected engineering tools
- explicitly licensed open-source projects

Our **production applications, control planes, operational infrastructure, security-sensitive systems, proprietary automation, and internal implementation details remain private**.

> **Public interfaces. Private implementation. Explicit contracts.**

---

## How We Engineer

Across NODE63 Labs, we optimize for:

- **Architecture before structural implementation** — significant system changes begin with explicit boundaries and design intent.
- **Explicit authority** — identity, permissions, policy, environment, and execution boundaries should be clear.
- **Evidence before acceptance** — code existing or CI passing is not, by itself, proof that a capability is accepted.
- **Reproducible engineering** — builds, environments, tests, and delivery paths should be independently repeatable.
- **Stable public contracts** — developer-facing interfaces should evolve deliberately and compatibly.
- **Security by design** — sensitive implementation and production authority remain tightly controlled.

---

## Repository Visibility Model

| Public | Private |
| --- | --- |
| Specifications and schemas | Product core implementations |
| SDKs and client libraries | Production applications |
| Developer documentation | Deployment and operational infrastructure |
| Examples and starter projects | Security-sensitive implementation |
| Selected tools and libraries | Internal automation and orchestration logic |
| Explicitly licensed open-source projects | Proprietary platform capabilities |

A repository being public does **not** automatically mean it is open source. Reuse and redistribution rights are defined by the license in each repository.

---

## Contributing

Contribution policies vary by repository.

Before opening an issue or pull request, review the repository's `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, and `LICENSE` when available.

Keep bug reports, feature requests, and integration discussions scoped to the relevant public repository.

---

## Security

Do **not** disclose suspected vulnerabilities, credentials, secrets, or security-sensitive information in public issues or discussions.

Use the security reporting instructions published in the relevant repository whenever available.

---

## Licensing

Each public repository defines its own licensing terms.

**Public visibility does not grant permission to copy, modify, redistribute, or commercially reuse code unless the repository's license explicitly allows it.**

---

## NODE63 Labs

We are building a multi-product engineering company where reusable platform capabilities make product development faster without weakening ownership, security, or domain boundaries.

**Building what's next.**
