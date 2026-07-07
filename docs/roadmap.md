# Roadmap

This roadmap describes the public development trajectory for Forge Brain and its place in The Crucible ecosystem. Timelines are directional, not commitments. **The full Crucible platform is not launched** — individual products are at different stages of development.

---

## Alpha — Current Phase

**Goal:** Establish this repository as a credible early public showcase — clear product positioning, ecosystem boundaries, and conceptual diagrams. Interactive prototype work happens separately.

### Deliverables

| Item | Status | Notes |
|------|--------|-------|
| Public showcase documentation | **Done** | Vision, architecture, roadmap, IP boundary |
| Product positioning & accuracy note | **Done** | Platform boundaries, no overclaiming |
| Conceptual diagrams (mermaid) | **Done** | Ecosystem and knowledge graph in README |
| Interactive graph canvas | **Planned** | First prototype not yet in this repo |
| Navigation modes | **Planned** | Focus, timeline, cluster, Aether preview |
| Minimap & viewport controls | **Planned** | Part of first prototype |
| Visual assets (screenshots, GIFs) | **Planned** | Not created yet — paths documented as placeholders |
| Sample graph dataset | **Planned** | Representative nodes across entity types |
| Local demo instructions | **Planned** | Clone-and-run when prototype ships |

### Alpha Success Criteria

- A reviewer can understand The Crucible ecosystem and Forge Brain's role within 60 seconds
- Product boundaries are clear: platform vs. products, public vs. private
- Conceptual diagrams communicate the graph and ecosystem vision without implying shipped UI
- Documentation does not overclaim production readiness or existing visual assets
- Repository is suitable as an early public showcase for builder programs

---

## Beta — Next Phase

**Goal:** Mature the Forge Brain demo with richer interactions and representative data that reflects real builder workflows.

### Planned Capabilities

| Area | Description |
|------|-------------|
| **Representative graph data** | Sample projects with realistic entity relationships across all types |
| **Entity detail views** | Inspect prompts, agents, files, and memories from the canvas |
| **Relationship exploration** | Click edges to understand connection types and provenance |
| **Focus mode depth** | Isolate subgraphs with contextual summary of what's in scope |
| **Aether mode preview** | Demonstrate how context surfacing would appear on the canvas |
| **Timeline interactions** | Scrub through relationship history on sample data |
| **Demo packaging** | Clone-and-run instructions with no external dependencies |

### Beta Success Criteria

- Demo runs locally without access to private systems
- Sample graph tells a coherent story about a builder's AI practice
- Focus and Aether modes communicate the platform vision clearly
- Performance acceptable for graphs with 100+ nodes in the demo

*Note: Beta does not require live Core integration. Connecting to the production engine is a Future phase goal.*

---

## Future — Horizon

**Goal:** Forge Brain integrates with the production Crucible platform as the ecosystem matures.

### Exploration Areas

| Area | Vision | Dependency |
|------|--------|------------|
| **Core integration** | Live entity and relationship data from the production engine | Core runtime |
| **Forge desktop wiring** | Forge Brain as a native panel inside the Forge workspace | Forge desktop app |
| **Aether live overlays** | Real context surfacing driven by the intelligence layer | Aether |
| **Siege connectors** | External tools appear as nodes in the graph | Siege platform |
| **Barrage team views** | Shared graphs and collaborative context for teams | Barrage platform |
| **Provenance tracing** | Follow source references across the graph visually | Core + Aether |
| **Cross-project maps** | Relationship views spanning multiple projects and clients | Core |
| **Export & sharing** | Share graph views and context bundles | Forge + Core |

### Future Success Criteria

- Forge Brain renders live project graphs from Core
- Measurable reduction in repeated setup for active builders
- Composable context reuse demonstrably reduces unnecessary token and API calls
- Ecosystem products are navigable from the Forge Brain graph surface

---

## Platform Development (Private)

The following are tracked in the private production repository, not here:

| Product | Stage |
|---------|-------|
| Core engine / runtime | In development |
| Forge desktop workspace | In development |
| Aether intelligence layer | In development |
| Siege integration platform | Planned |
| Barrage cloud / team platform | Planned |

---

## How to Follow Progress

- **This repository** — Demo releases, documentation updates, and asset additions
- **Release tags** — Versioned demo snapshots as the prototype matures
- **Changelog** — Added with the first public prototype release

---

## Contributing

This is a public showcase repository. Contribution guidelines will be published when the interactive demo is open for community input.
