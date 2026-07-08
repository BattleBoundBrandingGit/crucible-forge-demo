# Claude Application Visual Package

Polished Mermaid diagrams and a one-pager for **Anthropic Claude Max for Builders** and related opportunity applications.

> **Early public showcase.** These visuals communicate product vision and documented architecture at a high level. They do not represent shipped production software or proprietary implementation.

> **This public package intentionally summarizes private architecture at a conceptual level. Production implementation specs remain private.**

---

## Contents

| File                                                               | Purpose                                                              | Best for                                     |
| ------------------------------------------------------------------ | -------------------------------------------------------------------- | -------------------------------------------- |
| [crucible-ecosystem-diagram.md](crucible-ecosystem-diagram.md)     | AKOS platform map — products, Core engine, intelligence architecture | "What is The Crucible?" slide or doc section |
| [core-brain-engine-pipeline.md](core-brain-engine-pipeline.md)     | Core Brain Engine API pipeline (conceptual summary)                  | Technical credibility — engine design        |
| [knowledge-flow-diagram.md](knowledge-flow-diagram.md)             | How work becomes reusable intelligence + token reduction loop        | Value proposition — why it matters           |
| [claude-application-one-pager.md](claude-application-one-pager.md) | Single-page reviewer summary                                         | Application form, cover doc, or PDF export   |

---

## Source Documents

### In this public showcase repo

| Document                                 | Used by                                        |
| ---------------------------------------- | ---------------------------------------------- |
| [vision.md](../../vision.md)             | All visuals, one-pager                         |
| [architecture.md](../../architecture.md) | Ecosystem, pipeline, knowledge flow, one-pager |
| [diagrams.md](../../diagrams.md)         | Ecosystem, knowledge flow (companion diagrams) |
| [diagrams/](../../diagrams/)               | Standalone `.mermaid` source files           |
| [product/](../../product/)                 | Product overview PDF package                 |
| [roadmap.md](../../roadmap.md)           | One-pager, product evolution context           |
| [ip-boundary.md](../../ip-boundary.md)   | Scope and public/private delineation           |

### Private production references _(not included in this public showcase)_

These files live in the private production repository. They are **not linked** here because they are not part of this repo.

| Private reference                            | Summarized in                                                  |
| -------------------------------------------- | -------------------------------------------------------------- |
| `spec-011-core-brain-engine-api-contract.md` | [core-brain-engine-pipeline.md](core-brain-engine-pipeline.md) |
| `knowledge-model.md`                         | [knowledge-flow-diagram.md](knowledge-flow-diagram.md)         |
| `system-map.md`                              | [crucible-ecosystem-diagram.md](crucible-ecosystem-diagram.md) |
| `architecture/README.md` (production index)  | Ecosystem and pipeline visuals at a high level                 |

---

## Recommended Screenshots to Export

Use this checklist when preparing application materials. Export diagrams as **PNG** (slides, forms) or **SVG** (print, Figma).

- [ ] **Ecosystem diagram** — full platform map with Core intelligence layer
- [ ] **Core Brain Engine pipeline** — MVP vs Phase 2 / Future boundaries visible
- [ ] **Knowledge flow** — capture → engine → reuse → Claude → feedback loop
- [x] **Product overview PDF** — [`docs/product/The-Crucible-Product-Overview.pdf`](../../product/The-Crucible-Product-Overview.pdf)
- [ ] **One-pager** — export `claude-application-one-pager.md` to PDF
- [x] **Concept demo** — [`assets/screenshots/`](../../../assets/screenshots/) (Brain Map, Knowledge Flow, Signal View)
- [ ] **README hero** — architecture diagram section from root [README.md](../../../README.md)

**Suggested filenames** (after export):

| Asset | Location |
|-------|----------|
| `crucible-ecosystem.png` | [`assets/diagrams/`](../../../assets/diagrams/) |
| `core-brain-engine-pipeline.png` | [`assets/diagrams/`](../../../assets/diagrams/) |
| `knowledge-flow.png` | [`assets/diagrams/`](../../../assets/diagrams/) |
| `forge-brain-brain-map.png` | [`assets/screenshots/`](../../../assets/screenshots/) |

See [`assets/README.md`](../../../assets/README.md) for naming conventions. Mermaid sources: [`docs/diagrams/`](../../diagrams/).

---

## Exporting Diagrams as Images

No export tooling is bundled in this repository. Use one of these lightweight options:

### Option A — Mermaid Live Editor (recommended)

1. Open [mermaid.live](https://mermaid.live)
2. Copy the ` ```mermaid ` block from any diagram file
3. Export as PNG or SVG
4. Save to [`assets/diagrams/`](../../../assets/diagrams/)

### Option B — VS Code / Cursor

1. Install the **Markdown Preview Mermaid Support** extension
2. Open the diagram `.md` file and preview
3. Screenshot or use extension export if available

### Option C — GitHub render

1. Push to GitHub — Mermaid renders inline in `.md` files
2. Screenshot the rendered diagram from the browser
3. Crop to diagram bounds

### Option D — CLI (optional, not required)

```bash
npx -p @mermaid-js/mermaid-cli mmdc \
  -i docs/diagrams/ecosystem.mermaid \
  -o assets/diagrams/crucible-ecosystem.png
```

To use CLI, first save the mermaid block to a standalone `.mmd` file. No CLI dependency is added to this repo by default.

---

## Branding

Logo assets are not yet in this repository. When available, place them in [`assets/logos/`](../../../assets/logos/). See [`assets/README.md`](../../../assets/README.md).

---

## IP Reminder

These visuals are **public-safe**. They do not expose orchestration internals, retrieval ranking, embedding strategy, prompt compiler implementation, or production memory logic. See [ip-boundary.md](../../ip-boundary.md).
