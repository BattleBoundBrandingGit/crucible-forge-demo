# Core Brain Engine Pipeline

> **Application visual** · Public showcase context: [architecture.md](../../architecture.md), [diagrams.md](../../diagrams.md)  
> **Private source reference** _(not in this repo)_: `spec-011-core-brain-engine-api-contract.md`  
> **Showcase note:** Contract names and stage boundaries are shown at the API level. Implementation internals remain in the private production repository.

## Diagram

```mermaid
flowchart TB
    subgraph input["Input"]
        src["ImportedSource"]
    end

    subgraph mvp["MVP Pipeline — Core Brain Engine Contract"]
        direction TB
        s1["createImportedSource()"]
        s2["runReaders()"]
        s3["runExtractors()"]
        s4["runRuleEngine()"]
        s5["runRelationshipMapper()"]
        s6["resolveKnowledge()"]
        s7["generateBrainStoreWriteBatch()"]
        s8["runBrainEngine()"]
        s9["validateBrainEngineResult()"]

        s1 --> s2 --> s3 --> s4 --> s5 --> s6 --> s7
        s8 -.->|"orchestrates all stages"| s2
        s7 --> s8
        s8 --> s9
    end

    subgraph contracts["Output Contracts"]
        direction LR
        c1["ReaderResult"]
        c2["ExtractionResult"]
        c3["RuleEngineResult"]
        c4["RelationshipResult"]
        c5["KnowledgeResolutionResult"]
        c6["BrainStoreWriteBatch"]
        c7["BrainEngineResult"]
    end

    subgraph phase2["Phase 2 — Broader Coverage"]
        direction LR
        p2a["PDF & richer source types"]
        p2b["Review queues · transport wrappers"]
    end

    subgraph future["Future — Extensions"]
        direction LR
        f1["OCR · LLM-assisted layers"]
        f2["Vector / semantic search"]
        f3["Remote persistence adapters"]
    end

    subgraph store["Persistence Boundary"]
        bs["Brain Store<br/><i>MVP: dry_run only</i>"]
    end

    src --> s1
    s2 -.-> c1
    s3 -.-> c2
    s4 -.-> c3
    s5 -.-> c4
    s6 -.-> c5
    s7 -.-> c6
    s9 -.-> c7

    s7 --> bs
    s9 --> bs

    mvp -.-> phase2
    mvp -.-> future

    style mvp fill:#0f172a,stroke:#22d3ee,stroke-width:2px,color:#e2e8f0
    style phase2 fill:#1e1b4b,stroke:#a78bfa,stroke-width:1px,stroke-dasharray:5 5,color:#e2e8f0
    style future fill:#1c1917,stroke:#78716c,stroke-width:1px,stroke-dasharray:5 5,color:#a8a29e
    style contracts fill:#0c1222,stroke:#64748b,color:#94a3b8
    style input fill:#0c1222,stroke:#fbbf24,color:#fef3c7
    style store fill:#0c1222,stroke:#34d399,color:#d1fae5
```

## Stage Boundaries (per spec-011)

| Stage       | Scope                                                                                                                      | Notes                                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **MVP**     | Full operation set: `createImportedSource` through `validateBrainEngineResult`                                             | Includes readers, extractors, **rule engine**, **relationship mapper**, knowledge resolution, and **dry-run** write-batch generation |
| **Phase 2** | Broader source types (e.g. PDF), richer relationship families, review-queue metadata, CLI/Local API/MCP transport wrappers | Builds on the same contract — does not replace MVP stages                                                                            |
| **Future**  | OCR, research importers, LLM-assisted suggestions, vector/semantic search, Supabase/remote persistence                     | Explicit extensions outside MVP contract                                                                                             |

## Pipeline Steps (Plain English)

| Step                               | What it does                                                                        |
| ---------------------------------- | ----------------------------------------------------------------------------------- |
| **ImportedSource**                 | Accepted source entering the engine — file, paste, or import bundle with provenance |
| **createImportedSource()**         | Normalizes input into canonical source with stable identity and privacy scope       |
| **runReaders()**                   | Parses source into structured segments → **ReaderResult**                           |
| **runExtractors()**                | Pulls candidate entities, tasks, decisions, requirements → **ExtractionResult**     |
| **runRuleEngine()**                | Applies deterministic classification and threshold rules → **RuleEngineResult**     |
| **runRelationshipMapper()**        | Derives graph-shaped candidate relationships → **RelationshipResult**               |
| **resolveKnowledge()**             | Compares candidates against existing knowledge → **KnowledgeResolutionResult**      |
| **generateBrainStoreWriteBatch()** | Produces dry-run write plan → **BrainStoreWriteBatch** (MVP: `dry_run` only)        |
| **runBrainEngine()**               | Orchestrates full pipeline into one result → **BrainEngineResult**                  |
| **validateBrainEngineResult()**    | Verifies contract invariants before consumers act on the result                     |

## Output Contracts

| Contract                      | Produced by                      | Contains (abstract)                                  |
| ----------------------------- | -------------------------------- | ---------------------------------------------------- |
| **ReaderResult**              | `runReaders()`                   | Normalized text, segments, warnings, source linkage  |
| **ExtractionResult**          | `runExtractors()`                | Candidate entities, tasks, decisions, evidence       |
| **RuleEngineResult**          | `runRuleEngine()`                | Rule matches, classifications, threshold summaries   |
| **RelationshipResult**        | `runRelationshipMapper()`        | Candidate nodes, edges, relationship evidence        |
| **KnowledgeResolutionResult** | `resolveKnowledge()`             | Outcomes, matches, conflicts, review recommendations |
| **BrainStoreWriteBatch**      | `generateBrainStoreWriteBatch()` | Atomic dry-run operations for Brain Store            |
| **BrainEngineResult**         | `runBrainEngine()`               | All stage outputs, summaries, warnings, validation   |

## What This Diagram Does Not Show

Per public IP boundaries, this visual does **not** include:

- Internal orchestration code or service topology
- Embedding, indexing, or retrieval ranking algorithms
- Prompt compiler or token optimization internals
- Authentication, deployment, or database schemas

See [ip-boundary.md](../../ip-boundary.md).

## Export

See [README.md](README.md#exporting-diagrams-as-images) for PNG/SVG export instructions.
