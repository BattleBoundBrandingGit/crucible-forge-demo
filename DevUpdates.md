# DevUpdates

Development log for the crucible-forge-demo public showcase repository.

---

## 2026-07-07 · 6:45 PM (UTC-5)

**AI model/tool used:** Cursor · Auto

**Prompt/task summary:** Create polished visual proof assets for The Crucible Claude/Anthropic opportunity application — Mermaid diagrams (ecosystem, Core Brain Engine pipeline, knowledge flow), one-pager, and package README in `docs/visuals/claude-application/`.

**Files/folders created or changed:**

- `docs/visuals/claude-application/README.md` (created)
- `docs/visuals/claude-application/crucible-ecosystem-diagram.md` (created)
- `docs/visuals/claude-application/core-brain-engine-pipeline.md` (created)
- `docs/visuals/claude-application/knowledge-flow-diagram.md` (created)
- `docs/visuals/claude-application/claude-application-one-pager.md` (created)
- `docs/architecture.md` (updated — link to application visuals)
- `README.md` (updated — documentation table link)
- `DevUpdates.md` (created)

**What was completed:**

- Added ecosystem Mermaid diagram with The Crucible platform, Core, Forge, Barrage, Siege, Aether, and intelligence architecture (Big Brain, Mini Brains, Baby Brains, Skills, Experience Engine, Brain Gardener)
- Added Core Brain Engine pipeline diagram with canonical steps from spec-011 task definition, output contracts, and MVP vs Phase 2 visual boundaries
- Added knowledge flow diagram emphasizing token reduction, reuse, and Experience Engine feedback loop
- Added Claude application one-pager with credible scope and honest development status
- Added package README with export checklist and lightweight Mermaid-to-image instructions
- Linked application visuals from root README and `docs/architecture.md`

**Verification status:**

- `npx prettier --check docs/visuals/claude-application/**/*.md` — **passed** after `--write` formatting
- Mermaid PNG/SVG export — not added; export documented via Mermaid Live Editor and optional CLI (no heavy dependencies added)
- No app code changes; architecture spec files unchanged

**Assumptions made:**

- Source architecture files (`docs/architecture/spec-011-*.md`, `knowledge-model.md`, `system-map.md`, `architecture/README.md`) were **not present** in this showcase repo at task time; pipeline steps and contracts follow the task specification and existing public docs (`docs/architecture.md`, `docs/vision.md`, `docs/diagrams.md`)
- `runRuleEngine()` and `runRelationshipMapper()` grouped as **Phase 2** enrichment between extraction and knowledge resolution (MVP path runs extract → resolve directly when Phase 2 is not active)
- No branding/logo assets exist in repo; package README notes this
- One-pager “6 months unlock” section is directional ambition, not a committed timeline

**Recommended next step:**

- Export diagrams to PNG via [mermaid.live](https://mermaid.live) for application submission; screenshot `demo/index.html` for visual proof
- Copy architecture spec files into `docs/architecture/` in this repo (or sync from private repo) so diagram source links resolve on GitHub

---

## 2026-07-07 · 6:50 PM (UTC-5)

**AI model/tool used:** Cursor · Auto

**Prompt/task summary:** Follow-up from background filesystem search — located `spec-011-core-brain-engine-api-contract.md` in `The Crucible Clean` and corrected pipeline diagram MVP boundaries.

**Files/folders created or changed:**

- `docs/visuals/claude-application/core-brain-engine-pipeline.md` (updated)

**What was completed:**

- Background `find` located spec at `/Volumes/Extra Memory/Claude_External/The Crucible Clean/docs/architecture/spec-011-core-brain-engine-api-contract.md`
- Corrected pipeline diagram: `runRuleEngine()` and `runRelationshipMapper()` are **MVP** (not Phase 2) per spec-011 §5.1 and §11.1
- Added missing **RuleEngineResult** contract to diagram and tables
- Reclassified Phase 2 as broader source coverage, review queues, transport wrappers; Future as OCR, LLM layers, vector search, persistence (per spec-011 §11.2–11.3)
- Noted MVP dry-run-only persistence boundary for Brain Store writes

**Verification status:**

- Diagram content cross-checked against spec-011 sections 2.1, 5.1, 4.x contracts, and 11.x deferred work
- Prettier not re-run (single-file content update)

**Assumptions made:**

- Spec in `The Crucible Clean` is the authoritative source; not copied into showcase repo per IP boundary instructions

**Recommended next step:**

- Sync public-safe architecture docs from `The Crucible Clean/docs/architecture/` into showcase `docs/architecture/` so GitHub source links resolve

---

## 2026-07-07 · 6:41 PM (UTC-5)

**AI model/tool used:** Cursor · Auto

**Prompt/task summary:** Review Claude application visual package — fix broken links to missing `docs/architecture/` specs; make showcase repo self-contained and reviewer-safe.

**Files/folders created or changed:**

- `docs/visuals/claude-application/README.md` (updated)
- `docs/visuals/claude-application/crucible-ecosystem-diagram.md` (updated)
- `docs/visuals/claude-application/core-brain-engine-pipeline.md` (updated)
- `docs/visuals/claude-application/knowledge-flow-diagram.md` (updated)
- `docs/visuals/claude-application/claude-application-one-pager.md` (updated)
- `docs/ip-boundary.md` (updated — link to application visuals)
- `DevUpdates.md` (appended)

**What was completed:**

- Replaced broken links to `docs/architecture/spec-011-*.md`, `knowledge-model.md`, `system-map.md`, and `architecture/README.md` with plain-text private source references
- Pointed all in-repo citations to existing public docs: `vision.md`, `architecture.md`, `diagrams.md`, `roadmap.md`, `ip-boundary.md`
- Added required README note: public package summarizes private architecture; production specs remain private
- Split source table into “in this repo” vs “private production references (not linked)”
- Clarified one-pager honest boundary without implying private specs exist in showcase repo
- Verified root `README.md` links target files that exist in this repo

**Verification status:**

- `npx prettier --check docs/visuals/claude-application/**/*.md` — run at task completion
- Grep: no remaining `../../architecture/` markdown links in visual package

**Assumptions made:**

- Private production spec filenames are cited as plain text only — no URLs or copies into showcase repo
- GitHub directory link `docs/visuals/claude-application/` resolves to package README (standard behavior)

**Recommended next step:**

- Commit and push; export diagram PNGs via mermaid.live for application submission

---

## 2026-07-07 · 6:42 PM (UTC-5)

**AI model/tool used:** Cursor · Auto

**Prompt/task summary:** Polish static interactive Forge Brain HTML demo — full Crucible Brain network with ecosystem, intelligence, and services modules; aligned with docs/visuals package.

**Files/folders created or changed:**

- `demo/index.html` (updated)
- `demo/styles.css` (updated)
- `demo/script.js` (updated)
- `README.md` (updated — demo node list)
- `DevUpdates.md` (appended)

**What was completed:**

- Rebuilt demo with 17 nodes: central Crucible Brain, 5 ecosystem products, 6 intelligence concepts, 5 platform services (including **Automation**)
- Three-ring layout (Ecosystem · Intelligence · Services) with SVG ring guides
- Hover tooltips, click-to-select, direct + soft relationship edge highlighting, side panel with layer tags
- Accessible node buttons, Escape to deselect, responsive layout
- Dark polished visual style with hub pulse and float animations
- Link to application visuals package from demo header; README demo table updated

**Verification status:**

- Static files only — open `demo/index.html` in browser to verify
- No backend, no private logic, mock conceptual data only

**Assumptions made:**

- Siege and Barrage remain marked planned; all copy is public-safe per ip-boundary.md
- Docs link works when viewing from local filesystem or GitHub

**Recommended next step:**

- Screenshot demo with a node selected for Claude application materials; commit and push

---

## 2026-07-07 · 6:44 PM (UTC-5)

**AI model/tool used:** Cursor · Auto

**Prompt/task summary:** Premium cinematic redesign of static Forge Brain demo — radial brain map, curved glowing edges, display modes, particles, polished sidebar.

**Files/folders created or changed:**

- `demo/index.html` (redesigned)
- `demo/styles.css` (redesigned)
- `demo/script.js` (redesigned)
- `README.md` (updated — stronger Interactive Concept Demo section)
- `DevUpdates.md` (appended)

**What was completed:**

- Structured radial map: center Crucible Brain, first orbit (5 nodes), second orbit (10 nodes) per spec
- Curved SVG spokes and relationship paths with glow filter and selection highlighting
- Animated pulse rings and canvas particle background
- Hero header, notice bar, mode toggles (Ecosystem / Brain / Knowledge Flow)
- Larger node cards with initials, category colors, hover scale and glow
- Premium sidebar with badges, pills, public/private boundary note
- Responsive layout for tablet and mobile
- Static only — mock conceptual data, no backend

**Verification status:**

- Manual: open `demo/index.html` in browser
- No automated tests; static front-end only

**Assumptions made:**

- Display modes are visual-only highlights (no layout rearrangement) to keep logic public-safe and simple
- Siege and Barrage remain planned; all copy matches ip-boundary.md

**Recommended next step:**

- Capture screenshots in each display mode for Claude Max for Builders application; commit and push

---

## 2026-07-07 · 6:48 PM (UTC-5)

**AI model/tool used:** Cursor · Auto

**Prompt/task summary:** Upgrade Forge Brain demo to ultra-dense living knowledge graph — Canvas rendering, 300–1500 nodes, traveling edge pulses, cluster modes.

**Files/folders created or changed:**

- `demo/index.html` (rewritten)
- `demo/styles.css` (rewritten)
- `demo/script.js` (rewritten — Canvas graph engine)
- `README.md` (updated — Interactive Concept Demo section)
- `DevUpdates.md` (appended)

**What was completed:**

- Procedural mock graph: 15 domain clusters + hub + ecosystem anchors (Forge, Core, Aether, Claude)
- Density controls: Low (~300), Medium (~700), High (~1400) nodes with 1000+ edges at medium/high
- Canvas renderer with glowing edges, anchor nodes, cluster halos (Cluster View)
- Click anchor → wave pulses travel along edges via requestAnimationFrame; nodes flash on arrival
- Modes: Brain Map, Knowledge Flow, Cluster View, Signal View (continuous faint pulses)
- Pan/zoom, pulse speed slider, reset view, sidebar with pills and boundary note
- Static only — mock conceptual data, no backend

**Verification status:**

- Manual: open `demo/index.html`, test Medium density and anchor click wave
- No automated tests

**Assumptions made:**

- Satellite nodes use generic conceptual labels (not real client data)
- Performance capped at dpr 2 and ~1400 nodes for browser safety

**Recommended next step:**

- Screenshot Signal View with wave on Big Brain anchor for application; commit and push

---

## 2026-07-07 · 6:53 PM (UTC-5)

**AI model/tool used:** Cursor · Auto

**Prompt/task summary:** Final polish pass on Forge Brain demo — larger graph framing, screenshot readiness, Export PNG, README screenshot guide.

**Files/folders created or changed:**

- `demo/index.html` (Export PNG button)
- `demo/styles.css` (export button styling; hub label moved to canvas)
- `demo/script.js` (larger layout, vignette background, 2× PNG export, default zoom)
- `README.md` (screenshot how-to section)
- `DevUpdates.md` (appended)

**What was completed:**

- Medium density confirmed as default (`DEFAULT_DENSITY`)
- Graph scaled larger: `WORLD_RADIUS_FACTOR` 0.47, wider clusters, default zoom 1.12
- Canvas vignette background and brighter default edges for screenshot readability
- Hub and anchor labels rendered on canvas (“Crucible Brain”, full anchor names)
- **Export PNG** — offscreen 2× render via shared `paint()`; downloads graph canvas only
- README **Screenshots** section with mode and export workflow
- Static only — mock data, no backend

**Verification status:**

- `node --check demo/script.js` — pass
- Manual: open demo, Reset view, Export PNG

**Assumptions made:**

- Graph-only export is sufficient; full-page capture left to browser screenshot tools
- HTML hub label hidden because canvas now draws the hub title

**Recommended next step:**

- Export PNGs for Brain Map, Knowledge Flow, and Signal View; commit and push

---

## 2026-07-07 · 6:57 PM (UTC-5)

**AI model/tool used:** Cursor · Auto

**Prompt/task summary:** Polish repository for public showcase — organize assets, rename screenshots, professional README landing page, fix links.

**Files/folders created or changed:**

- `assets/README.md` (created)
- `assets/diagrams/.gitkeep` (created)
- `assets/logos/.gitkeep` (created)
- `assets/screenshots/*.png` (renamed — removed date suffixes)
- `README.md` (rewritten — hero, Screenshots gallery, section reorder)
- `docs/ip-boundary.md` (updated asset paths and demo status)
- `docs/diagrams.md` (screenshot cross-reference)
- `docs/visuals/claude-application/README.md` (points to `assets/`)
- `demo/script.js` (export filename matches canonical naming)
- `DevUpdates.md` (appended)

**What was completed:**

- `assets/` structure: `screenshots/`, `diagrams/`, `logos/`
- Screenshots renamed: `forge-brain-{mode}-{density}.png` (no timestamps)
- README opens with hero + embedded screenshot gallery (Brain Map, Knowledge Flow, Signal View)
- `assets/README.md` documents naming, folders, and future videos/GIFs/logos
- Visual package and IP boundary updated to new asset locations
- Export PNG download uses canonical filename pattern
- Link verification: all 5 README image paths resolve; ip-boundary relative paths fixed

**Verification status:**

- Python link checker: 5/5 README images OK; anchor-only “broken” links are false positives
- All screenshot PNGs present in `assets/screenshots/`
- No references to old `docs/visuals/forge-brain-*.png` paths

**Assumptions made:**

- `forge-brain-brain-medium-2026-07-07-2.png` renamed to `forge-brain-brain-high.png` (second Brain Map capture)
- Full-page browser screenshots remain optional; committed assets are canvas exports only

**Recommended next step:**

- Export Mermaid diagrams to `assets/diagrams/`; add `.gitignore` for `.DS_Store`; commit and push

---

## 2026-07-07 · 7:00 PM (UTC-5)

**AI model/tool used:** Cursor · Auto

**Prompt/task summary:** Organize Claude-generated product overview package — docs/product, docs/diagrams sources, tools/build_pdf, screenshot canonical names, README showcase polish.

**Files/folders created or changed:**

- `docs/product/` — `The-Crucible-Product-Overview.pdf`, `.md`, `README.md`
- `docs/diagrams/` — five `.mermaid` files + `README.md`
- `tools/build_pdf.py` (moved from root; output path updated)
- `assets/screenshots/` — renamed showcase PNGs; extras in `archive/`
- `README.md`, `assets/README.md`, `docs/diagrams.md`, `docs/ip-boundary.md`
- `docs/visuals/claude-application/README.md`, `demo/script.js`
- `DevUpdates.md` (appended)

**What was completed:**

- Product overview PDF and Markdown moved to `docs/product/`
- Mermaid sources moved from root `diagrams/` to `docs/diagrams/`
- `build_pdf.py` moved to `tools/`; writes `docs/product/The-Crucible-Product-Overview.pdf`
- Showcase screenshots: `forge-brain-brain-map`, `knowledge-flow`, `signal-view`; alternates archived
- README restructured: hero → screenshots → demo → product PDF → diagrams → IP boundary
- `docs/product/README.md` and `docs/diagrams/README.md` added
- Export PNG uses showcase filenames (`forge-brain-brain-map.png`, etc.)
- Cross-links updated across visual package and IP boundary

**Verification status:**

- `node --check demo/script.js` — pass
- Markdown link checker: 3/3 README images resolve; product PDF path resolves
- No links to old root paths (`diagrams/`, `build_pdf.py`, timestamped PNG names)

**Assumptions made:**

- `forge-brain-brain-medium.png` renamed to `forge-brain-brain-map.png` as canonical Brain Map
- Low/high density alternates kept in `assets/screenshots/archive/` not deleted
- `docs/diagrams.md` (embedded Mermaid) coexists with `docs/diagrams/` (source files)

**Recommended next step:**

- Commit and push; export Mermaid PNGs to `assets/diagrams/`; add `.gitignore` for `.DS_Store` and `Archive.zip`
