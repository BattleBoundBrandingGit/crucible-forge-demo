# Architecture (High Level)

This document describes the **public, high-level architecture** of The Crucible ecosystem and Forge Brain's place within it. The production engine, internal orchestration, and implementation-specific details are intentionally abstracted and are **not present in this repository**.

## Design Principles

1. **Platform, not monolith** — The Crucible is an ecosystem of products sharing a common engine, not a single application
2. **Local-first** — Knowledge and context are owned and stored close to the builder
3. **Composable context** — Assets assemble into reusable bundles rather than one-off configurations
4. **Disciplined API usage** — External calls are scoped, intentional, and traceable
5. **Entity-relationship model** — All products share a common graph of typed entities and edges
6. **Layered separation** — Presentation, workspace, engine, intelligence, integration, and team layers are distinct concerns
7. **Progressive disclosure** — Builders see summary views by default; depth is available on demand

## System Overview

```
┌─────────────────────────────────────────────────────────┐
│              The Crucible (Platform)                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌───────────────────────────────────────────────────┐  │
│  │           Forge (Desktop Workspace)               │  │
│  │  ┌─────────────────────────────────────────────┐  │  │
│  │  │  Forge Brain (Graph Surface)                │  │  │
│  │  │  Canvas · Modes · Visual navigation         │  │  │
│  │  └─────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────┘  │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  Core — shared engine / runtime                         │
│  Entity registry · Relationships · Platform primitives  │
├──────────────┬──────────────┬───────────────────────────┤
│   Aether     │    Siege     │        Barrage            │
│ Intelligence │ Integration  │   Cloud / Team (future)   │
│    layer     │   platform   │        platform           │
└──────────────┴──────────────┴───────────────────────────┘
```

## Layer Descriptions

### The Crucible (Platform)

The umbrella ecosystem — not a single deployable unit. Defines shared principles (local-first intelligence, composable context, disciplined API usage) and coordinates how products interact through Core.

### Forge (Desktop Workspace)

The primary builder-facing product. Forge is where daily AI work happens — managing projects, configuring agents, composing context, and operating on knowledge assets. Forge is a **desktop workspace**, not a web app or chat interface.

Forge Brain lives **inside** Forge as its visual intelligence layer.

### Forge Brain (Graph Surface) — *this showcase*

The visual intelligence layer and interactive graph surface within Forge. In this public repository, Forge Brain is represented through **documentation and conceptual diagrams only** — the interactive prototype is planned but not yet published here.

Responsibilities (conceptual):

- Render entity-relationship graphs on an interactive canvas
- Provide navigation modes: default, focus, timeline, cluster, and Aether preview
- Handle viewport interactions (zoom, pan, drag, minimap)
- Visualize relationships between projects, prompts, files, agents, memories, skills, models, workflows, clients, and knowledge
- Preview how Aether surfaces context in place (Aether mode)

Forge Brain is a **read-navigate-focus** surface. It does not own business logic, execution, or the proprietary engine.

### Core (Shared Engine / Runtime)

The shared engine beneath all Crucible products. Core is **not included in this public repository**.

Responsibilities (abstracted):

- Entity registry for all platform types
- Relationship management between entities
- Platform primitives shared across Forge, Aether, Siege, and Barrage
- Runtime services that products build on

Core is the single source of truth for what exists in a builder's practice. Products read from and write to Core — they do not maintain independent registries.

### Aether (Intelligence Layer)

The intelligence layer that operates across the platform:

- Selects and surfaces relevant context based on current focus
- Helps make large knowledge feel small in active context
- Operates as an overlay in Forge Brain's Aether mode (preview in this showcase)
- Implementation details are proprietary and not disclosed here

### Siege (Integration Platform) — *planned*

The integration platform for connecting external tools, APIs, and systems to The Crucible:

- Bridges external services into the entity-relationship model
- Enables workflows that span The Crucible and outside tools
- Planned — not yet in development in this showcase

### Barrage (Cloud / Team Platform) — *planned*

The future cloud and team platform:

- Shared workspaces and collaboration at scale
- Team-level context and knowledge management
- Planned — not yet in development in this showcase

## Entity Model (Abstract)

All products share a common entity-relationship model:

```
Entity Types:
  Project, Prompt, Agent, File, Memory, Skill, Model, Workflow, Client, Knowledge

Relationship Types (examples):
  Project ──contains──▶ Prompt
  Agent ──uses──▶ Prompt
  Agent ──references──▶ File
  Workflow ──chains──▶ Agent
  Memory ──belongs_to──▶ Project
  Client ──owns──▶ Project
  Knowledge ──supports──▶ Skill
  File ──sources──▶ Knowledge
```

The full relationship schema, validation rules, and provenance tracking are proprietary. This showcase demonstrates the *concept* through the Forge Brain graph prototype.

## Data Flow (Simplified)

This flow describes the **production platform architecture** at a high level. The demo in this repository implements only the Forge Brain interaction layer with representative data.

```
Builder action on Forge Brain canvas
        │
        ▼
Forge (workspace operation)
        │
        ▼
Core (entity / relationship query or mutation)
        │
        ├──▶ Aether (context surfacing, if active)
        ├──▶ Siege (external integration, if triggered)
        └──▶ Barrage (team operation, if triggered)
        │
        ▼
Response → Forge → Forge Brain (graph update)
```

## What This Document Does Not Cover

The following are intentionally excluded from this public architecture:

- Core engine implementation and runtime internals
- Internal orchestration and prompt compilation pipelines
- Memory system implementation and persistence strategies
- Embedding, indexing, and retrieval ranking algorithms
- Token optimization and context window management
- Aether intelligence layer internals
- Authentication and authorization implementation
- Deployment topology and infrastructure
- Client-specific configurations or data schemas

See [IP Boundary](ip-boundary.md) for the complete public/private delineation.

## Technology Notes (This Showcase)

This public repository contains **documentation and conceptual diagrams only** for the Forge Brain demo surface. When the interactive prototype is released, it will use technologies appropriate for graph visualization. Specific framework choices will be documented at release time.

The production Crucible platform — including Core, Forge, and Aether — is developed in a separate, private repository.
