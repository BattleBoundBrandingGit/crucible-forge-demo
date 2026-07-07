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
