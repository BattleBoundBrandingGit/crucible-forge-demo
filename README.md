# Forge Brain

**Visual intelligence layer for The Crucible**

Forge Brain is the **early visual layer** inside [Forge](docs/vision.md) — the desktop workspace for **The Crucible**, an AI Knowledge Operating System (AKOS) built around **local-first intelligence**, **composable context**, and **disciplined API usage**.

This repository is an **early public showcase** for builder program review. It contains documentation, **conceptual Mermaid diagrams**, and a **static front-end concept demo** — not production code, not a finished product UI, and not the private engine that powers the platform.

---

## Accuracy Note

| | |
|---|---|
| **What this repo is** | Early public showcase — vision, architecture diagrams, and a static Forge Brain concept demo |
| **What this repo is not** | Production repo, shipped product, or proprietary implementation |

The production Crucible platform remains **private and under active development**. Diagrams and the concept demo are **directional** — they communicate intent, not deployed systems. See [IP Boundary](docs/ip-boundary.md).

---

## Interactive Concept Demo

A **premium static HTML brain map** — cinematic, screenshot-ready, and open locally with no install.

**[Open `demo/index.html`](demo/index.html)**

| Feature | Description |
|---------|-------------|
| **Radial brain map** | Large central Crucible Brain with first and second orbit modules |
| **Curved neural edges** | Glowing SVG relationship lines that highlight on selection |
| **Display modes** | Ecosystem View · Brain View · Knowledge Flow (visual-only toggles) |
| **Sidebar brief** | Category badges, explanations, clickable connection pills |
| **Atmosphere** | Particle field, pulse rings, dark cinematic gradients |

**First orbit:** Big Brain · Knowledge Graph · Experience Engine · Aether · Forge  
**Second orbit:** Mini Brains · Baby Brains · Skills · Memory · Prompt Compiler · Token Optimization · Brain Gardener · Core · Siege · Barrage

Mock conceptual data only — **no backend, no proprietary orchestration, not production.**

*The full Forge Brain entity graph canvas (zoom, pan, project nodes) remains in development.*

---

## The Problem

Builders repeat the same expensive AI setup every session: re-explaining context, re-finding files, re-configuring agents, re-pasting prompts, and re-paying token and API costs. There is no map of what exists or how it connects.

**The Crucible** exists to fix that — as a platform, not a chat window.

---

## System Architecture

The Crucible is an **AI Knowledge Operating System**: ecosystem products above a shared engine, with intelligence concepts and platform services at a high level.

```mermaid
graph TB
    subgraph akos["The Crucible — AI Knowledge Operating System"]
        direction TB

        subgraph products["Ecosystem Products"]
            direction LR
            forge["Forge<br/><i>Desktop Workspace</i>"]
            aether["Aether<br/><i>Intelligence Layer</i>"]
            siege["Siege<br/><i>Integration Platform</i><br/>(planned)"]
            barrage["Barrage<br/><i>Cloud / Team Platform</i><br/>(planned)"]
        end

        subgraph forgeLayer["Forge — Visual Layer"]
            fb["Forge Brain<br/><i>Graph Surface</i><br/>(showcase focus)"]
        end

        subgraph core["Core — Shared Engine / Runtime"]
            direction TB

            subgraph intelligence["Intelligence Architecture <i>(conceptual)</i>"]
                direction LR
                bb["Big Brain<br/><i>Central orchestration</i>"]
                mb["Mini Brains<br/><i>Scoped specialists</i>"]
                baby["Baby Brains<br/><i>Task-level units</i>"]
                sl["Skills Library"]
                ee["Experience Engine<br/><i>Learning loop</i>"]
                bg["Brain Gardener<br/><i>Knowledge curation</i>"]
            end

            subgraph services["Platform Services <i>(abstract)</i>"]
                direction LR
                kg["Knowledge Graph"]
                mem["Memory"]
                pc["Prompt Compiler"]
                to["Token Optimization"]
                auto["Automation"]
            end
        end
    end

    forge --> fb
    fb --> bb
    bb --> mb
    bb --> baby
    mb --> sl
    baby --> sl
    bb --> kg
    kg --> mem
    bb --> pc
    pc --> to
    ee --> bb
    bg --> kg
    bg --> mem
    aether --> bb
    aether --> kg
    auto --> bb
    siege -.-> core
    barrage -.-> core
    forge --> core
```

*Conceptual diagram — not production topology. Full annotations: [docs/diagrams.md](docs/diagrams.md#1-system-architecture)*

---

## Knowledge Flow

How context composes, reaches a model, and compounds back into the brain layer.

```mermaid
flowchart LR
    user(["Builder"])
    forge["Forge<br/><i>Desktop Workspace</i>"]
    bb["Big Brain<br/><i>Orchestration</i>"]
    kg["Knowledge Graph"]
    skills["Skills Library /<br/>Mini Brains"]
    model["Claude or<br/>Other AI Model"]
    response["Better Response<br/><i>Scoped · Provenance-aware</i>"]
    ee["Experience Engine"]
    brain["Brain Layer<br/><i>Memory + Graph update</i>"]

    user -->|"intent + focus"| forge
    forge -->|"composed request"| bb
    bb -->|"resolve context"| kg
    kg -->|"relevant assets"| skills
    skills -->|"scoped prompt + context"| model
    model -->|"model output"| response
    response -->|"outcome signal"| ee
    ee -->|"learn + refine"| brain
    brain -->|"enriched knowledge"| kg
    brain -.->|"updated context"| bb
    response -->|"deliver"| forge
    forge -->|"present"| user
```

*Logical flow — not proprietary orchestration code. Details: [docs/diagrams.md](docs/diagrams.md#2-knowledge-flow)*

---

## Product Roadmap

```mermaid
flowchart LR
    mvp["Forge MVP<br/><i>Desktop workspace ·<br/>Forge Brain graph</i>"]
    local["Local AI<br/><i>Local-first intelligence ·<br/>on-device context</i>"]
    team["Team Collaboration<br/><i>Barrage · shared graphs</i>"]
    market["Marketplace<br/><i>Skills · templates ·<br/>shared knowledge</i>"]
    ent["Enterprise /<br/>Ecosystem<br/><i>Siege integrations ·<br/>full AKOS scale</i>"]

    mvp -->|"now → near-term"| local
    local -->|"mid-term"| team
    team -->|"long-term"| market
    market -->|"horizon"| ent
```

**Current stage:** Forge MVP / early showcase. Full platform not launched. Details: [docs/roadmap.md](docs/roadmap.md) · [docs/diagrams.md](docs/diagrams.md#3-product-roadmap)

---

## Platform Principles

| Principle | What it means |
|-----------|---------------|
| **Local-first intelligence** | Context and knowledge live close to the builder — owned, not trapped in a vendor cloud |
| **Composable context** | Prompts, files, memories, and skills assemble into reusable bundles |
| **Disciplined API usage** | Model calls are scoped, intentional, and traceable — less token and API waste |

---

## Ecosystem at a Glance

| Product | Role | Status |
|---------|------|--------|
| **The Crucible** | AI Knowledge Operating System — the platform | In development |
| **Core** | Shared engine and runtime | Private — not in this repo |
| **Forge** | Desktop workspace | In development |
| **Forge Brain** | Graph surface inside Forge — **this showcase** | Early public showcase |
| **Aether** | Intelligence layer | In development |
| **Siege** | Integration platform | Planned |
| **Barrage** | Cloud / team platform | Planned |

---

## What Forge Brain Visualizes

Forge Brain maps relationships across a builder's practice — projects, prompts, files, agents, memories, skills, models, workflows, clients, and knowledge.

```mermaid
graph TD
    client["Client"] -->|owns| project["Project"]
    project -->|contains| prompt["Prompt"]
    project -->|contains| agent["Agent"]
    project -->|contains| memory["Memory"]
    agent -->|uses| prompt
    agent -->|powered_by| model["Model"]
    agent -->|equipped_with| skill["Skill"]
    agent -->|references| file["File"]
    workflow["Workflow"] -->|chains| agent
    memory -->|draws_from| knowledge["Knowledge"]
    file -->|sources| knowledge
    skill -->|supports| knowledge
```

*Conceptual canvas view — not a screenshot. Interactive prototype planned.*

---

## Why Forge Brain Exists

- **Reduce repeated setup** — See what exists before rebuilding context
- **Reuse composable context** — Skills, memories, and bundles travel with the work
- **Reduce token and API waste** — Scope what reaches the model
- **Preserve provenance** — Trace sources and references across the graph
- **Make large knowledge feel small** — Focus on the subgraph that matters now
- **Organize AI work visually** — See the whole practice, not just the latest chat

---

## Target Prototype Capabilities

The **[concept demo](demo/index.html)** visualizes the AKOS brain network. A full **Forge Brain graph canvas** (zoom, pan, entity nodes, timeline/focus modes) is still planned:

| Capability | Status |
|------------|--------|
| Static brain network visualization | **Available** — `demo/index.html` |
| Interactive entity graph canvas | Planned |
| Zoom, pan, drag, minimap | Planned |
| Focus · Timeline · Cluster modes | Planned |
| Aether mode preview | Planned |

---

## Development Status

| Area | Status |
|------|--------|
| Architecture diagrams (Mermaid) | **Available** — conceptual only |
| Static concept demo (`demo/`) | **Available** — front-end only, mock data |
| Forge Brain graph canvas prototype | **Planned** |
| Screenshots / GIFs | **Not created** |
| Core engine / Forge desktop | **In development** — private repo |
| Full platform launch | **Not yet** |

**Maintainer:** Austin Brower

---

## Documentation

| Document | Description |
|----------|-------------|
| [Diagrams](docs/diagrams.md) | **Canonical source** for all Mermaid architecture visuals |
| [Vision](docs/vision.md) | AKOS thesis and design principles |
| [Architecture](docs/architecture.md) | High-level system design |
| [Roadmap](docs/roadmap.md) | Alpha, Beta, and Future phases |
| [IP Boundary](docs/ip-boundary.md) | Public vs. private delineation |
| [Application Visuals](docs/visuals/claude-application/) | Diagrams and one-pager for builder program review |

---

## Getting Started

```bash
git clone https://github.com/BattleBoundBrandingGit/crucible-forge-demo.git
cd crucible-forge-demo
open demo/index.html   # macOS — or open demo/index.html in any browser
```

1. **Try the concept demo** — [`demo/index.html`](demo/index.html)
2. **Read the diagrams** — [docs/diagrams.md](docs/diagrams.md)
3. **Read the vision** — [docs/vision.md](docs/vision.md)

---

<p align="center">
  <strong>Forge Brain</strong> — See how your AI work connects. Build with clarity.
</p>
