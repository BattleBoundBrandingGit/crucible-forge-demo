# Diagram Sources

Reusable **Mermaid source files** for The Crucible public showcase. Use these in [Mermaid Live Editor](https://mermaid.live), documentation, slides, or export pipelines.

> **Conceptual only** — not production topology, not proprietary orchestration internals.

---

## Files

| File | Describes |
|------|-----------|
| [ecosystem.mermaid](ecosystem.mermaid) | AKOS product ecosystem — Forge, Barrage, Siege, Aether, Core, Forge Brain |
| [platform-architecture.mermaid](platform-architecture.mermaid) | Layered platform stack and major subsystems |
| [knowledge-flow.mermaid](knowledge-flow.mermaid) | How context composes, reaches a model, and compounds back |
| [brain-hierarchy.mermaid](brain-hierarchy.mermaid) | Big Brain · Mini Brains · Baby Brains hierarchy |
| [roadmap.mermaid](roadmap.mermaid) | Product evolution phases |

---

## Relationship to other diagram docs

| Location | Role |
|----------|------|
| **`docs/diagrams/`** (this folder) | Standalone `.mermaid` sources for export and reuse |
| [`docs/diagrams.md`](../diagrams.md) | Canonical **embedded** Mermaid in Markdown (README pulls from here) |
| [`docs/visuals/claude-application/`](../visuals/claude-application/) | Builder-program diagram package with annotations |
| [`assets/diagrams/`](../../assets/diagrams/) | **Exported PNG/SVG** renders (when created) |

Do not delete any layer — they serve different publishing workflows.

---

## Exporting to PNG or SVG

### Mermaid Live (recommended)

1. Open [mermaid.live](https://mermaid.live)
2. Paste the contents of any `.mermaid` file
3. Export PNG or SVG
4. Save to [`assets/diagrams/`](../../assets/diagrams/) using descriptive names, e.g. `crucible-ecosystem.png`

### CLI (optional)

```bash
npx -p @mermaid-js/mermaid-cli mmdc \
  -i docs/diagrams/ecosystem.mermaid \
  -o assets/diagrams/crucible-ecosystem.png
```

---

## IP reminder

These diagrams are **public-safe**. They do not document retrieval ranking, embedding strategy, prompt compiler implementation, or production memory logic. See [IP Boundary](../ip-boundary.md).
