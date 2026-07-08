# IP Boundary

This document defines what **this public showcase repository** includes and what remains in **private production systems**. The boundary exists to share product vision and demo capability — without exposing proprietary implementation, client data, or competitive advantage.

---

## Accuracy Note

**This repository is an early public showcase and documentation surface for Forge Brain.** The production Crucible platform — including Core (the shared engine/runtime), Forge (the desktop workspace), and Aether (the intelligence layer) — remains private and under active development. Nothing here should be interpreted as a launched product, interactive demo, or complete system.

---

## What This Repository Includes

### Public by Design

| Category | What's Included |
|----------|-----------------|
| **Product vision** | The Crucible as a platform — local-first intelligence, composable context, disciplined API usage |
| **Ecosystem overview** | High-level roles of The Crucible, Core, Forge, Forge Brain, Aether, Siege, and Barrage |
| **Product overview** | PDF + Markdown package — [`product/The-Crucible-Product-Overview.pdf`](product/The-Crucible-Product-Overview.pdf) |
| **Forge Brain concept demo** | Interactive static graph demo — [`demo/index.html`](../demo/index.html) |
| **High-level architecture** | Layered system diagram, entity-relationship model (abstract), data flow (simplified) |
| **Conceptual diagrams** | Mermaid system architecture, knowledge flow, roadmap, entity graph, and [claude-application visuals](visuals/claude-application/) |
| **Roadmap** | Alpha, Beta, and Future phases with honest development status |
| **Visual assets** | Forge Brain screenshots in [`assets/screenshots/`](../assets/screenshots/); diagram exports planned in [`assets/diagrams/`](../assets/diagrams/) |
| **Documentation** | README, vision, architecture, roadmap, diagrams, and this IP boundary document |

### Acceptable Level of Detail

- Platform principles: local-first intelligence, composable context, disciplined API usage
- Product names, roles, boundaries, and development status
- Entity types and relationship concepts (abstract)
- Forge Brain UI capabilities (canvas, modes, interactions) as prototype features
- General design principles (layered separation, entity-relationship model, progressive disclosure)
- Directional roadmap — clearly marked as planned or in development

---

## What This Repository Does NOT Include

### Private / Proprietary

| Category | What Stays Private |
|----------|-------------------|
| **Core engine / runtime** | The shared engine beneath all products — entity management, runtime services, platform primitives |
| **Backend orchestration** | Internal service coordination, job queues, event processing pipelines |
| **Prompt compiler** | How prompts are assembled, versioned, and resolved at runtime |
| **Memory system** | Persistence strategies, retrieval logic, decay policies, and consolidation rules |
| **Embeddings & indexing** | Vector strategies, chunking approaches, index schemas, and refresh cadences |
| **Retrieval & ranking** | Relevance scoring, Aether context selection, and prioritization logic |
| **Token optimization** | Context window management, compression, deduplication, and cost controls |
| **Aether intelligence internals** | How the intelligence layer selects and composes context |
| **Forge desktop application** | The production desktop workspace codebase |
| **Authentication & authorization** | Identity providers, permission models, and access control implementation |
| **Client data** | Real client names, project details, configurations, or usage patterns |
| **API keys & secrets** | Credentials, environment configurations, and service account details |
| **Deployment infrastructure** | Cloud topology, CI/CD pipelines, monitoring, and scaling configuration |
| **Siege & Barrage implementation** | Integration platform and cloud/team platform codebases |

### Explicitly Out of Scope

- Source code from the private production repository
- Database schemas, migration files, or data models
- Internal API specifications beyond high-level contracts
- Performance benchmarks, cost models, or unit economics
- Employee or contractor documentation
- Legal agreements, NDAs, or client contracts

---

## Product Boundary Reference

| Product | In this repo? | What is shown |
|---------|---------------|---------------|
| **The Crucible** (platform) | Vision & positioning only | Principles, ecosystem map, long-term direction |
| **Core** (engine/runtime) | Architecture diagram only | Abstract role — no implementation |
| **Forge** (desktop workspace) | Referenced, not included | Described as the host for Forge Brain |
| **Forge Brain** (graph surface) | **Documentation + diagrams only** | Mermaid visuals; interactive prototype planned |
| **Aether** (intelligence layer) | Aether mode UI preview only | Conceptual overlay — no intelligence internals |
| **Siege** (integration platform) | Roadmap reference only | Planned — no code or specs |
| **Barrage** (cloud/team platform) | Roadmap reference only | Planned — no code or specs |

---

## Why This Boundary Exists

1. **Protect the engine** — Core, Aether, and orchestration layers are core IP
2. **Protect clients** — No real client data, configurations, or identifiable information
3. **Enable open showcase** — Evaluators can understand the product without production access
4. **Set honest expectations** — This is an early documentation showcase, not a shipped product or demo

---

## How to Evaluate This Showcase

| Evaluable From This Repo | Requires Private Access |
|--------------------------|------------------------|
| Platform vision and design principles | Core engine performance and behavior |
| Ecosystem product boundaries | Memory system and persistence |
| Forge Brain UX concepts (diagrams, docs) | Working interactive prototype |
| Graph navigation mode concepts | Aether intelligence layer accuracy |
| Entity-relationship modeling approach | Real client deployments |
| Documentation quality and honesty | Full API specifications |
| Conceptual mermaid diagrams | Screenshots, GIFs, and demo recordings |
| Development status transparency | Forge desktop application and infrastructure |

---

## Licensing & Usage

- **This repository** — Public showcase materials for evaluation, demonstration, and program application
- **Private production systems** — All rights reserved; not licensed through this repository
- **Demo code** — When released, prototype application code will carry an explicit open-source license
- **Visual assets** — Screenshots and GIFs will be added when the prototype is ready; none exist in the repo today

---

## Questions

For questions about public/private boundaries or early access to private systems, contact the repository maintainer. This document will be updated as products mature and the boundary shifts.
