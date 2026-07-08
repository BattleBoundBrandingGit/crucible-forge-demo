# Assets

Public media for the **Forge Brain** showcase repository — screenshots, exported diagrams, and future brand assets.

> All visuals use **mock conceptual data** only. No production graph, client data, or proprietary internals.

---

## Folder structure

| Folder | Purpose | Status |
|--------|---------|--------|
| [`screenshots/`](screenshots/) | Forge Brain concept demo captures (showcase set) | **Available** |
| [`screenshots/archive/`](screenshots/archive/) | Alternate density exports (not in README) | Archive |
| [`diagrams/`](diagrams/) | PNG/SVG exports of Mermaid diagrams | Placeholder — sources in [`docs/diagrams/`](../docs/diagrams/) |
| [`logos/`](logos/) | Brand marks, wordmarks, app icons | **Future** |

---

## Showcase screenshots (`screenshots/`)

Canonical files embedded in the root [README](../README.md):

| File | Demo mode | Description |
|------|-----------|-------------|
| `forge-brain-brain-map.png` | Brain Map | Dense interconnected knowledge graph (Medium density) |
| `forge-brain-knowledge-flow.png` | Knowledge Flow | User → Forge → Brain → Claude → Experience Engine |
| `forge-brain-signal-view.png` | Signal View | Continuous pulses across the network |

**To capture new screenshots:** open [`demo/index.html`](../demo/index.html) → set mode → **Reset view** → **Export PNG** → rename to match the table above.

Alternate density exports belong in [`screenshots/archive/`](screenshots/archive/) unless promoted to the showcase set.

---

## Diagram exports (`diagrams/`)

Reserved for static exports from [`docs/diagrams/`](../docs/diagrams/) and the [claude-application package](../docs/visuals/claude-application/).

Suggested filenames:

```
crucible-ecosystem.png
platform-architecture.png
knowledge-flow.png
brain-hierarchy.png
roadmap.png
```

---

## Future assets

| Type | Folder | Notes |
|------|--------|-------|
| **Logos** | `logos/` | Wordmark, icon, dark/light variants |
| **Demo videos** | TBD — consider `assets/videos/` | Short screen recordings |
| **GIFs** | TBD — consider `assets/gifs/` | Looping Signal View captures |

---

## Usage

- **README** embeds the three showcase screenshots
- **Product overview PDF** — [`docs/product/`](../docs/product/)
- Do not treat these assets as production UI or real customer data
