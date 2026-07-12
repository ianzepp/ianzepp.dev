# Ian Zepp: Comprehensive Career and Research History

**Status:** Internal source material for `ianzepp.dev` content generation

**Evidence reviewed through:** July 12, 2026
**Primary emphasis:** Current independent AI and systems R&D, followed by the historical career that made it possible

## Purpose and use

This document is the factual source of truth for future autobiographical pages, interactive timelines, project drill-downs, case studies, biographies, resumes, and outreach material. It is deliberately broader than any single public page.

The website should not reproduce this document from top to bottom. It should use the material as a structured content reservoir:

1. lead with the current research period;
2. let readers drill from research programs into projects, phases, architecture, trials, tests, commits, transcripts, and source links;
3. keep the conventional employment chronology available as a parallel historical track;
4. expose evidence without publishing sensitive records;
5. distinguish verified facts from first-person career recollection and generated summary evidence.

### Evidence grades

- **A — directly verified:** source code, Git history, executed records, first-party corporate records, validated credentials, or contemporaneous primary sources.
- **B — corroborated:** consistent first-person record plus a credible secondary source, or transcript synthesis corroborated by live repositories.
- **C — first-person recollection:** older resume, LinkedIn export, or Ian's direct account without independent documentary confirmation.
- **D — lead only:** inference, ambiguous aggregator, or unresolved identity/entity relationship.

Commit, transcript, test, trial, and document counts are time-stamped measurements. They should always retain their measurement date and inclusion rule when presented publicly.

---

# Part I — The main story: independent AI and systems R&D

## Period definition

**September 2025–present**, with source recovery and preparatory work visible in August 2025.

This is not a sabbatical project, a short course, or a collection of generated demos. It is a sustained independent R&D program combining:

- programming-language and compiler engineering;
- agent kernels, multi-agent runtimes, and orchestration;
- programmable multi-tenant platforms;
- MCP security and governance;
- full-stack Rust and WebAssembly applications;
- multi-provider LLM evaluation;
- local-model inference and tuning;
- retrieval systems and applied AI products;
- developer tooling, protocol bridges, release systems, and operational infrastructure;
- a document-driven delivery method with explicit goals, campaigns, phases, ledgers, acceptance proofs, and independent audits.

The important claim is not that AI wrote many changes. The important claim is that Ian developed a repeatable way to direct, constrain, test, integrate, and audit AI-assisted engineering across complex systems.

## Scale snapshot

Measurements below cover local material available on July 12, 2026.

### Git activity

Across every local Git repository under `/Users/ianzepp/work`, filtering for the exact author identity `Ian Zepp <ian.zepp@protonmail.com>` from August 1, 2025 through July 12, 2026:

- **218** local Git repositories existed at measurement time.
- Current `HEAD` histories contained 20,621 matching commit appearances.
- Deduplicating identical SHAs across clones, archived/current copies, and history-preserving imports produced **17,710 unique commits**.
- All local refs contained **18,647 unique commits**.
- A deliberately selected original/core R&D set accounted for **16,033 unique commits across 106 repositories**.
- **16,041 unique commits** occurred from December 2025 through July 12, 2026.
- **14,928** occurred from January 1 through July 12, 2026.
- May and June alone contained **7,204**.
- The full measured period averaged approximately **1,476 unique commits per month**, including partial months and the October pause.
- December through partial July averaged approximately **2,005 per month**.

| Month | Deduplicated commits in current `HEAD` histories |
| --- | ---: |
| August 2025 | 589 |
| September 2025 | 138 |
| October 2025 | 2 |
| November 2025 | 940 |
| December 2025 | 1,113 |
| January 2026 | 1,028 |
| February 2026 | 1,286 |
| March 2026 | 591 |
| April 2026 | 1,505 |
| May 2026 | 3,196 |
| June 2026 | 4,008 |
| July 1–12, 2026 | 3,314 |

Commit subjects indicate substantive work rather than formatter churn:

- 4,371 began with feature/add/implement/build language;
- 1,261 were fix-prefixed;
- 1,419 were refactor/clean/polish-prefixed;
- 349 were test-prefixed;
- 2,322 were documentation-prefixed;
- 450 were chore/style-prefixed;
- only 134 explicitly matched formatting/style terminology;
- 7,538 used other domain-specific subjects such as complete, route, remove, phase, expose, migrate, lower, validate, or implement named architecture.

**Interpretation caveat:** These are Git commits recorded under Ian's author identity inside an explicitly AI-assisted practice. They are not a claim that Ian manually typed every line or personally executed every commit command. They measure directed, integrated, and accepted engineering work. SHA deduplication avoids obvious double counting; exact-author filtering may omit work recorded under other identities.

### Transcript and agent-orchestration activity

The structured transcript archive spans September 6, 2025 through July 12, 2026:

- **9,588 unique transcript captures**, representing **6,638 distinct root session IDs**;
- **258 active dates** across 310 calendar days, or **83.2%** of all dates;
- a **117-day uninterrupted active streak** from November 8, 2025 through March 4, 2026;
- Claude: 4,859 captures;
- Codex: 2,944 captures;
- OpenCode: 879 captures;
- Hermes: 489 captures;
- Pi: 417 captures.

| Month | Distinct root session IDs | Active days |
| --- | ---: | ---: |
| September 2025 | 22 | 10 |
| October 2025 | 14 | 4 |
| November 2025 | 337 | 25 |
| December 2025 | 879 | 31 |
| January 2026 | 815 | 31 |
| February 2026 | 919 | 28 |
| March 2026 | 433 | 28 |
| April 2026 | 676 | 30 |
| May 2026 | 1,421 | 30 |
| June 2026 | 349 | 29 |
| July 1–12, 2026 | 773 | 12 |

A capture is an archived direct, resumed, branched, delegated, or automated agent interaction. It is not necessarily one direct conversation with Ian. Parsed record/message/tool-call totals contain repeated context from resumed branches and should not be marketed as unique utterances.

A user-utterance-only topic screen found recurring discussion in:

- architecture, protocols, compilers, and runtimes: 1,898 captures;
- Faber/Radix/Rivus/Nanus: 1,871;
- Abbot/Prior/Swarm/Fleet/Vivarium/ReAct: 1,689;
- goal/delivery/factory/campaign/ledger work: 963;
- Gauntlet/Leptos/Field Board: 793;
- trials/evals/grading/judging/verifiers: 701;
- explicit test-suite, integration-test, Cargo-test, or property-test language: 460;
- Cephalopodic/MCP Tap/Fortress/Scath: 418;
- Gofolio/Ghostfolio: 369;
- Monk: 338.

These frequency screens overlap and can repeat resumed context. They are discovery signals, not project totals.

### Goals, campaigns, delivery documents, and ledgers

Within a selected current/original R&D repository set:

- **216** exact `goal*.md` documents;
- **43** exact `campaign*.md` documents;
- **91** exact `ledger*.md` documents;
- **1,396** delivery- or phase-named Markdown documents;
- **95** architecture/design-named Markdown documents;
- **114** plan/roadmap-named Markdown documents.

An independent narrower scan of 139 immediate-child Git repositories under the Faber, Ian Zepp, and Minted Geek Swarm containers found:

- 247 goal-named documents;
- 52 campaign-named documents;
- 1,009 delivery-named documents;
- 117 ledger-named documents;
- 904 phase-named documents.

The differences reflect different repository sets and filename rules. Categories overlap. Neither count should be represented as an exact number of completed projects.

Radix alone is a defensible case study in document-driven delivery:

- **219** immediate `docs/factory/*` initiative directories;
- **42** campaign documents;
- **224** goal documents;
- **931** delivery documents;
- **105** ledgers;
- **785** phase-named documents;
- more than 1,600 tracked Markdown files under `docs/factory` in the broader scan.

### Test and evaluation surfaces

A static lower bound across six selected contemporary systems found **6,087 defined tests**:

| Current system | Static test definitions |
| --- | ---: |
| Faber/Radix | 2,918 |
| Faber package/project CLI | 515 |
| Minted Geek Swarm runtime | 1,262 |
| Field Board / Gauntlet Week One | 1,077 |
| Gofolio CLI | 89 |
| Consolidated trials monorepo | 226 |

This counts tracked Rust test attributes and Python `def test_` markers. It is not a current passing-test report and excludes many other repositories, browser tests, integration scenarios, corpus cases, and compiler exempla.

### LLM trial corpus

The Faber trial system contains:

- **17,681 execution-result rows**: 17,045 base responses, 537 judged chain results, and 99 pipeline results;
- **493 result-bearing directories**;
- **114 run IDs**;
- **26 models**;
- **84 task IDs represented in base output**;
- **266 active task definitions** across compile, translate, predict, write, and chain tasks;
- **159 active judged chain tasks** with `judge_prompt` definitions;
- **537 executed chain rows with verdict objects**.

Raw and graded JSONL representations duplicate the same 17,045 base responses. The 34,726 combined row count must not be described as 34,726 distinct trials.

Additional durable research assets include:

- 164 provenance-bearing local-inference `run-metadata.json` files;
- 113 saved local-inference conversation traces;
- multi-provider evaluation matrices;
- deterministic and LLM-as-judge grading;
- ethics/adversarial experiment definitions;
- design trials with blind candidate ranking and judge reconciliation;
- coding-agent fixtures;
- fleet-agent benchmark scenarios and prompt/scaffolding ablations;
- model, host, power-state, context-window, quantization, and server-tuning provenance.

Self-correction is implemented in task and harness design, but executed correction-result volume has not been independently established. Public wording should distinguish designed capability from completed trial counts.

## Month-by-month R&D chronology

### August 2025 — recovery and reconstruction

- Imported and documented historical source archives.
- Recovered Salesforce applications, Zendesk/Salesforce integration, ActiveMQ/JMS tooling, payment ingestion, Appenda components, KMap/Koog, older Minted services, and the 2019 Motivis platform source.
- Began concentrated work on the Monk API family.
- The 589-commit count includes archive recovery and history-preserving work; it should not be presented as 589 new product features.

### September 2025 — Monk in Rust and architecture cleanup

- Primary work on the Rust Monk API alongside the TypeScript platform.
- Ported tests and platform patterns from TypeScript into idiomatic Rust.
- Used phased refactors, explicit review gates, and safety questions around metadata, DDL generation, handlers, and observer boundaries.
- 138 deduplicated commits in current histories.

### October 2025 — deliberate low-activity interval

- Only four transcript-active days and two matching commits in current histories.
- Work was dominated by systems troubleshooting and personal research rather than the later software R&D pace.
- This month is useful context: the high-intensity period was sustained but not retroactively projected onto every month.

### November 2025 — Monk becomes an ecosystem

- 337 distinct root sessions across 25 active days.
- 940 deduplicated commits.
- Work across Monk API, CLI, UI, IRC, bot, MCP, sync, and related infrastructure.
- Multi-tenancy, schema isolation, metadata/model runtime, observer rings, filesystems, packages, protocol adapters, and CLI surfaces developed in parallel.
- Commit/review gates and multi-phase implementation became consistent operating practice.

### December 2025 — Monk OS and Faber genesis

- 879 distinct root sessions across all 31 days.
- 1,113 deduplicated commits.
- Monk API OS, EMS, Anarchy, Monastery, OS SDK, HTTP/display services, and related tooling.
- Faber Romanus emerged as a major language/compiler project.
- Parallel agent delegation became routine for repetitive conversions and broad refactors.
- Git commits became explicit cognitive checkpoints between design and the next phase.

### January 2026 — compiler family, trials, and agent infrastructure

- 815 distinct root sessions across all 31 days.
- 1,028 deduplicated commits.
- Faber compiler work expanded into Rivus self-hosting, Artifex, minimal Nanus compilers in several implementation languages, Radix, tree-sitter/editor work, examples, and public documentation.
- Faber Trials built model/context/n-shot matrices with executable grading and judged/pipeline experiments.
- Abbot, agent CLI/worker infrastructure, and transcript tooling expanded.
- Living design documents became persistent project memory rather than one-session plans.

### February 2026 — agent kernels and Field Board

- 919 distinct root sessions across all 28 days.
- 1,286 deduplicated commits.
- Abbot and Prior explored persistent agent execution, typed frames, plugins, model providers, backpressure, rooms, tools, and system boundaries.
- Cassio and Vivarium supported transcript and private-data workflows.
- Field Board/Gauntlet Week One delivered a seven-crate full-stack Rust system in seven days, including Leptos/WASM, Axum/PostgreSQL, binary protobuf frames, native canvas logic, AI tools, observability, performance harnesses, and more than one thousand current test definitions.
- Research and implementation used tiered models, parallel scouts, worktrees, and strict validation gates.

### March 2026 — breadth, applied systems, and evaluation reuse

- 433 distinct root sessions across 28 active dates in the structured archive; the generated monthly summary covers all calendar days through additional source material.
- 591 deduplicated commits in current histories; the lower Git number reflects project/history shape rather than low conversational activity.
- Gofolio API/CLI/web, LegacyLens, Ye Olde RAG, MediaPipe Palm, SkyFi tools, ServiceCore, Tava Health, Medbridge, Upstream, and other bounded builds.
- Muninn grew into a polyglot frames/kernel/bridge/runtime family.
- Prior expanded toward a software-factory control plane.
- MCP Tap/Cephalopodic began.
- QRStatic used empirical codec and recovery sweeps.
- Reusable evaluation and implementation skills were extracted from projects rather than left as one-off code.
- REQUIREMENTS → SCOPE → PLAN → README and warmup/document-driven execution became explicit workflow contracts.

### April 2026 — MCP governance and audit discipline

- 676 distinct root sessions across all 30 days.
- 1,505 deduplicated commits.
- Cephalopodic expanded into API, CLI, web, Fortress, Scath, sink, radar, capstone, releases, and security/governance work.
- Faber/Radix, Prior, Cassio, and reusable skills continued.
- Independent acceptance auditing and structured multi-wave review became institutionalized.
- Delivery documents increasingly served as executable control planes for agent work.

### May 2026 — Swarm and Abbotik acceleration

- 1,421 distinct root sessions across all 30 days.
- 3,196 deduplicated commits.
- Minted Geek Swarm consolidated split agent/runtime concepts into a Rust runtime monorepo and surrounding integration/client surfaces.
- Abbotik developed as a Rust API/LLM/daemon/MCP/CLI platform with legacy TypeScript/web boundaries.
- Goal-driven phase delivery and separate acceptance audits are visible in exact May sessions.

### June 2026 — runtime consolidation and compiler/factory expansion

- 349 distinct root sessions across 29 active days.
- 4,008 deduplicated commits, the highest complete month in the measured Git period.
- Swarm runtime and integration work continued at production-shaped boundaries.
- Faber/Radix factory initiatives, hosts, targets, validation, cleanup, and documentation expanded rapidly.
- The lower transcript-root count alongside the higher commit count reflects orchestration style, long-running work, imported/preserved histories, and multi-commit delivery rather than a simple one-session/one-commit relationship.

### July 1–12, 2026 — Radix factory intensity

- 773 distinct root sessions across all 12 observed days.
- 3,314 deduplicated commits in twelve days.
- Radix alone accounted for approximately 1,986 current-history commits during the period.
- Factory goals, campaigns, ledgers, target work, compiler architecture, cleanup, documentation, and validation dominated visible activity.
- The partial month must not be extrapolated as a promised full-month rate.

---

# Part II — Current research programs

## 1. Faber / Radix: language, compiler, runtime, and factory

**Period:** December 2025–present

**Primary locations:** `/Users/ianzepp/work/faberlang/*`
**Primary languages:** Rust, Faber, TypeScript; supporting Python, Go, C, Zig, WGSL, Metal, Racket/sexp representations

Faber is a programming-language ecosystem; Radix is the principal compiler engine. This is the largest and deepest current research program.

### Architecture

- Shared parsing, semantic analysis, and typechecking feed two broad compilation lanes.
- The application lane lowers Faber HIR to reviewable Rust and then native Cargo binaries.
- The systems lane lowers MIR into executable FMIR/runtime artifacts and additional fail-closed surfaces.
- Target and validation surfaces include Rust, Go and TypeScript file emission; WebAssembly; LLVM text; Metal; WGSL; Racket/sexp staging; GPU/tensor experiments; and compiler round-trip checks.
- The public examples/corpus repository contains hundreds of `.fab` programs and expected-output artifacts.
- The E2E harness walks the public corpus across multiple backends and intermediate forms.
- Supporting repositories cover the package CLI, runtime, host kernel, native host, providers, standard library/Norma, tree-sitter grammar, examples, documentation, archival material, and trials.

### Delivery system

Radix uses factory initiative directories containing combinations of:

- `goal.md` — the intended end state and invariants;
- campaign documents — related multi-goal work;
- delivery or phase specifications — implementation graphs and gates;
- ledgers — durable state, findings, deferred work, and completion evidence;
- audits and acceptance proofs;
- clean-break, correctness, optimization, documentation, and housekeeping passes.

The scale—219 factory initiatives and thousands of supporting documents—shows sustained architecture management rather than disconnected prompt-to-code generation.

### Activity and validation

- Radix contains approximately **5,512** recent deduplicated commits in current history.
- June 2026 contained about 1,493; July 1–12 contained about 1,986.
- Current static scans find roughly **2,918** Radix test definitions and **515** in the public Faber CLI.
- The public Faber corpus includes hundreds of examples and expected outputs across backend lanes.

### Research questions

- Can a language be designed for machine generation while remaining reviewable by humans?
- Can multiple target lanes share semantic truth without pretending every backend has equal capability?
- Can compilation, validation, packaging, runtime hosting, and LLM learnability be managed as one research program?
- Can implementation work be decomposed into durable, auditable factory initiatives instead of ephemeral chat instructions?

### Interactive timeline candidates

- Faber Romanus language exploration;
- Rivus self-hosting compiler work;
- Artifex self-compiled binary;
- Nanus minimal compilers in TypeScript, Rust, Go, and Python;
- Radix Rust compiler consolidation;
- application versus systems lanes;
- target capability matrix;
- Faber trials and grammar-only learning experiments;
- factory/campaign delivery system;
- current host/runtime/provider split.

## 2. Minted Geek Swarm: multi-agent runtime and operating system

**Period:** May 2026–present

**Primary locations:** `/Users/ianzepp/work/minted-geek-swarm/*`
**Primary language:** Rust, with separate TypeScript/Astro and Swift presentation/consumer projects

Swarm is a multi-agent runtime monorepo centered on the `swarmd` binary.

### Architecture

- The current runtime contains 15 named imported runtime/domain crates.
- Domains include kernel, RTM, key, API, LLM, SES, VFS, MCP, ACP, CRM, PMP, SMS, operations, and payments.
- Public HTTP terminates at one runtime boundary.
- Internal work moves through local kernel/frame paths rather than service-to-service HTTP.
- Runtime containment is treated as an architectural invariant, not a naming convention.
- Production-shaped black-box testing lives in a sibling integration repository and drives the built binary through public routes.
- CLI, TUI, web, documentation, hub, CEO/operations, release, and corporate repositories surround the core runtime.
- Historical split-service repositories retain earlier architecture and migration history.

### Activity and validation

- The current Swarm runtime history contains approximately **1,928** commits since May 2026.
- The runtime contains roughly **1,262** static test definitions.
- The wider container is approximately 97% Rust by classified source-file count.
- The `swarm-web` boundary is deliberately separated from Rust runtime crates and generates public documentation/catalog surfaces.

### Research questions

- How should multiple tool-using agents communicate, persist state, and coordinate without collapsing into ad hoc HTTP microservices?
- What belongs in a kernel/frame boundary versus a domain service?
- How can integration tests exercise production containment rules through the same public route consumers use?
- How should human governance, billing, credentials, filesystems, messaging, and model providers coexist in one runtime?

## 3. Agent-kernel lineage: Abbot, Prior, Muninn, Fleet, Orqa, Vivarium

**Period:** January 2026–present, with ideas traceable to Monk OS
**Primary languages:** Rust, TypeScript, Go, Python, shell

These are related but distinct experiments in agent execution, typed messaging, orchestration, persistence, and operator control.

### Abbot

- Persistent tool-using Rust AI daemon.
- SQLite state, OpenAI-compatible provider boundaries, CLI/TUI/monitor surfaces.
- Message-first microkernel and uniform frame/syscall model.
- Rooms, turns, tools, model providers, persistence, and operator workflows treated as explicit subsystems.

### Prior

- Typed-frame agentic runtime with kernel routing and response correlation.
- Separates room, turn, LLM, VFS, EMS, and related subsystems.
- Expanded into daemon, gate, factory, CLI, web, and TUI projects.
- Factory work treated goals and execution stages similarly to compiler AST/passes: interpretation, semantic validation, stage evaluation, artifacts, and end-to-end acceptance.

### Muninn

- Polyglot protocol/runtime family.
- Rust kernel/frames and supporting packages coexist with TypeScript and Go frame consumers.
- Provider-neutral streaming LLM and tool-loop work.
- Strong example of a platform core in one language with consumers and bridges in others.

### Fleet and Orqa

- Fleet formalizes Mind/Head/Hand roles, multi-agent work distribution, stewardship, and dead-man/continuation behavior.
- Orqa fans work out to background agents and provides task/pod/mail operations.
- Claude Workers and related tools explored sandboxed identities, remote workers, and Git-conflict avoidance.

### Cassio

- Rust transcript AST processor for Claude, Codex, OpenCode, and related session logs.
- Converts raw agent event streams into readable transcripts and summary inputs.
- Made the current empirical analysis of interaction patterns and project history possible.

### Vivarium

- Local-first private-agent email archive and retrieval system.
- Proton integration, decrypted sync, indexing/embeddings, send workflows, and IMAP/SMTP support.
- Treats private communications as a durable agent data surface rather than a transient connector.

## 4. Monk: programmable multi-tenant platform and cross-language consumers

**Period:** August 2025–April 2026, with later descendants

**Primary platform language:** TypeScript on Bun/Hono
**Consumer and bridge languages:** Rust, TypeScript, Go, protocol-specific adapters

Monk is the clearest bridge between Ian's historical enterprise-platform experience and the current AI R&D period.

### Platform architecture

- Multi-tenant programmable backend.
- PostgreSQL schema-per-tenant or SQLite file-per-tenant modes.
- Dynamic model runtime and metadata-driven APIs.
- Authentication, token machinery, ACLs, audit history, format negotiation, encryption, import/export, packages, cron, and filesystem surfaces.
- Ordered observer rings/hooks around platform behavior.
- Model-first APIs rather than one hard-coded application schema.

### Cross-language and protocol consumers

- TypeScript and Rust CLIs;
- Rust API rewrite/client experiments;
- TypeScript SDK/bindings;
- Go FUSE interface;
- FTP server adapter;
- IRC server adapter;
- EMS/event management;
- bot and natural-language interfaces;
- Monk UI;
- Monk OS kernel/coreutils/SDK/archive experiments.

This family demonstrates deliberate separation between a TypeScript platform and Rust/Go/protocol consumers.

### Activity

- `monk-api` contains approximately **1,122** recent commits.
- November and December 2025 transcript summaries show sustained model, infrastructure, CLI, protocol, and operating-system work.

## 5. Field Board / Gauntlet Week One: seven-day vertical system

**Period:** February 16–22, 2026, with later polish

**Repository names:** `gauntlet-week-1`, later mirrored/continued as `fieldboard`
**Primary language:** Rust end-to-end

Field Board is a real-time collaborative whiteboard with AI-assisted board manipulation. It is also a compact demonstration of Ian's rapid iterative method.

### Current workspace shape

The current Cargo workspace contains **seven crates**:

1. `server` — Axum HTTP/WebSocket server and PostgreSQL persistence;
2. `client` — Leptos 0.8 server rendering plus WASM hydration;
3. `canvas` — from-scratch 2D engine with native-testable core and WASM wrapper;
4. `frames` — shared binary frame model and protobuf codec;
5. `traces` — framework-independent observability primitives;
6. `perf` — live HTTP/WebSocket load and latency harness;
7. `cli` — REST and WebSocket automation client.

The original sprint presentation focused on six core app/support crates; CLI is the seventh current workspace member.

### Technical architecture

- Rust 2024 edition across server, browser frontend, canvas, protocol, observability, performance, and CLI.
- Leptos SSR plus WebAssembly hydration; no JavaScript application runtime.
- Axum, SQLx, and PostgreSQL backend.
- Shared `Frame` type between client and server.
- Binary protobuf envelope over WebSockets using Prost.
- Flexible `data` and `trace` values are `serde_json::Value` in memory and recursively converted to protobuf values; the wire representation is binary protobuf, not JSON text.
- Request lifecycle: `Request → Item* → Done | Error | Cancel`, supporting streamed responses.
- A native-testable canvas core keeps browser APIs outside the main document/camera/input/hit/render logic.
- Real-time object updates, cursors, chat, camera following, savepoints/rewind, AI tool calls, and board observability.
- Two-speed persistence: dirty-object batching and a separate frame-log queue.
- One-use WebSocket authentication tickets consumed by deletion.
- Multi-provider AI tool loop mutates and broadcasts board objects live.

### Sprint metrics and current state

- Current Git history: **511** commits.
- Daily commits from February 16–22: 40, 76, 84, 102, 70, 52, and 86.
- Current static scan: **1,077** Rust test definitions across the workspace.
- A time-stamped February 21 snapshot reported 41,578 total source/test lines, 15,757 test lines, 915 annotated tests, 989 passing tests, and 41.2% measured line coverage.
- A later portfolio snapshot reported 48,932 lines, 498 commits, 1,065 passing tests, one failure, and 40.4% coverage.
- These are different points in a rapidly changing sprint. They must retain their dates instead of being merged into one synthetic metric.

### AI development process

The sprint archive records:

- 347 transcript captures across all concurrent work during the week;
- 273 Gauntlet-path captures in the cost/accounting summary;
- 855.2 million raw input-token units reported by the provider accounting method, dominated by cached context reads;
- 4.5 million output tokens;
- 158h 46m summed agent wall time, exceeding calendar time because agents ran in parallel;
- explicit workflow constraints: format, lint, test, then commit; no production `unwrap`; tests in dedicated files;
- separate architectural, technical-writing, correctness, and implementation roles.

Provider-token accounting should be presented only with its cache and concurrency caveats.

### Existing interactive presentation pattern

Field Board already contains a useful model for the autobiographical site:

- navigation between **Architecture**, **Timeline**, and **Transcripts**;
- a clickable crate dependency map;
- tabs for overview, crates, stack, and decisions;
- a day-by-day carousel with commit counts, named work phases, representative commit messages, and field notes;
- a synchronized screenshots/recordings carousel;
- a transcript explorer grouped by day and session;
- stat strips for lines, duration, tests, and coverage;
- drill-down from system overview to exact repositories and artifacts.

The main site should adapt this interaction model across multiple projects rather than hiding all repositories in one undifferentiated archive.

## 6. Trials and evaluation systems

### Faber Trials

Research areas include:

- model learnability from grammar-only, example, and library contexts;
- n-shot conditions;
- translation and compilation correctness;
- three-level executable grading: typecheck, execution, correct output;
- pipeline/drafter/reviewer pairings;
- judged chain trials;
- format/framing sensitivity;
- differential-sensitivity and conversation-dynamics studies;
- retry, rate-limit, matrix, and durable-result handling.

A January 2026 study ran four models across 672 trials each (2,688 total in that matrix). Transcript evidence reports grammar-only context at 87% versus 79% complete in that study, an eight-pair pipeline including one reported 0%→100% recovery, and a 19-task complex-translation set where grammar/library changes moved one model from 68% to 79%. These measurements are transcript-grounded and should be linked to their exact result artifacts before prominent public use.

### Consolidated Trials monorepo

The current repository brings together:

- cloud LLM trials;
- coding-agent evaluations;
- ethics and high-stakes decision studies;
- blind design-production/judging/reconciliation;
- local GGUF/MLX inference tuning;
- server and conversation benchmarks;
- fleet-agent scenarios;
- prompt, scaffold, context, and agent-count ablations;
- durable run metadata and replayable artifacts.

The artifacts include hundreds of provenance-bearing local inference files, logs, JSONL event streams, machine/power metadata, tuning parameters, and summaries.

### Ethics trials

- Four scenario families and eight experiment definitions.
- ABAB framing, casualty sweeps, escalation, target importance, recursive consistency, coercion/compliance follow-ups, and rubric hooks.
- Expanding units and repeats yields 103 defined trial units per model across the current definitions.
- No committed executed ethics artifacts were present at audit time; describe the implemented harness and study design, not a completed result volume.

### Design trials

- Multi-model production of candidate designs.
- Candidate anonymization.
- Blind ranked judging by multiple models.
- Reconciliation, pairwise rates, consensus, disagreement, and self-preference reports.
- The harness is implemented; committed production study volume was not present at audit time.

## 7. Gofolio: applied product plus evaluation operator UI

**Components:** Go API, Rust CLI/TUI, SvelteKit web application

### Product

- Ghostfolio-compatible investment/portfolio backend in Go.
- Rust terminal portfolio application with market data, portfolio views, charts, chat, and LLM tool use.
- SvelteKit frontend for portfolio and wealth-management workflows.

### Evaluation system

- **73 defined cases**: 39 golden regression cases plus 34 multi-tool, adversarial, and portfolio scenarios.
- Parallel multi-model runner.
- Fixture-backed and live modes.
- Multiple API-key leases and bounded concurrency.
- SQLite plus per-case JSON artifacts.
- Replay support.
- Three implemented executable grading tiers.
- A fourth LLM-as-judge tier remained explicitly unimplemented at audit time.
- Ratatui/Crossterm live evaluation UI showing case/tool progress, pass/fail/error totals, latency, model/run selection, tier details, artifacts, and replay information.
- Current durable sample: two runs, 15 case results, 44 recorded steps, and 15 per-case JSON files.

This is a strong example of turning evaluation infrastructure into an operator-facing application.

## 8. Cephalopodic: MCP control plane, security, and governance

**Period:** March–June 2026

**Nature:** Collaborative; Ian is a major but not sole contributor
**Languages:** Go, React/TypeScript, Python, SQL, Rust

The family includes:

- Go control plane/API and authenticated MCP surface;
- upstream server registration and catalog synchronization;
- user-scoped taps;
- authentication and access control;
- CLI and React/TypeScript web application;
- MCP sink and testing utilities;
- Fortress inline security gateway;
- scanning, radar, capstone, and Scath implementations;
- Homebrew and public release infrastructure.

Fortress inspects JSON-RPC before and after forwarding and supports enforcement, quarantine, review, signatures/policies, and heuristic classification.

The family demonstrates a platform core in Go with TypeScript/React, Python, Rust, and security-tool consumers around it.

## 9. Abbotik

**Period:** April–May 2026
**Primary language:** Rust, with legacy TypeScript/web surfaces

- Rust durable backend for tenant data, auth, metadata, and `/api/*` surfaces.
- PostgreSQL persistence.
- Rust/Axum OpenAI-compatible LLM service boundary.
- Room/factory handlers and backend integration.
- Rust daemon, MCP, and CLI.
- Legacy TypeScript API/app/web and documentation/release repositories.
- Homebrew distribution and public release plumbing.

## 10. Applied AI and product experiments

### LegacyLens

- COBOL-focused retrieval-augmented generation system using AWS CardDemo source.
- Parser/chunker/embedding pipeline.
- Pinecone/OpenAI/LangChain stack in the original build.
- Retriever and RAG chain.
- CLI and web UI.
- Tests, benchmarks, indexing, hybrid-search/caching/streaming follow-up work.

### Ye Olde RAG

- Retrieval pipeline for Chaucer's *Canterbury Tales* in the original Middle English.
- A deliberately different corpus used to test retrieval, language distance, and explanatory interfaces.

### QRStatic / QRStatic Riptide

- Zero-dependency Rust temporal-correlation/steganographic QR research.
- Temporal and tiled evaluation harnesses.
- Prefix, M-of-N, sharded tiling, PSNR, quantization, and recovery sweeps.
- Transcript evidence records 128-trial and quantization studies that drove defaults; exact claims should link to live artifacts.

### SkyFi

- Rust CLI/MCP/verification tools around satellite-imagery APIs.
- Cloudflare deployment and release work.

### MediaPipe Palm

- Palm/gesture tracking experiments.
- Event, gesture, and evaluation layers around upstream MediaPipe work.
- Must be described as contribution/extension work, not ownership of MediaPipe.

### Gauntlet interview/product builds

March 2026 included multiple bounded product/partner builds and reviews across Go, Rust, Python, Angular, React, Leptos, and other stacks. These include ServiceCore, Tava Health, Medbridge, Upstream, and related exercises. They demonstrate rapid stack adaptation but should be clearly labeled as cohort/interview/partner exercises rather than long-lived owned products.

## 11. Developer and operations tools

- `slice` — contiguous code-range manipulation CLI.
- `github2md` — repository-to-Markdown extraction.
- `brendan` — Mermaid/SVG rendering without a browser runtime.
- `cassio` — transcript AST and archive processing.
- `skyfi-cli` — satellite-imagery API CLI.
- `dig-json`, `ping-json`, `corewlan-json`, `coreutils-json` — structured system/network tools.
- `opencode-sync` — conversation synchronization between machines/directories.
- `claude-ctx` — context-window inspection.
- `claude-workers`, `agents`, `claude-agents` — agent orchestration and diagnostics.
- Homebrew taps, release repositories, binary-publication workflows, Docker, Cloudflare, Railway, and related operational systems.

---

# Part III — The R&D operating method

## Design first, implementation second

Across monthly transcript summaries and exact sessions, major work generally follows:

1. inspect the live repository and recent history;
2. discuss the intended invariant and reject weak proxies;
3. write or revise a goal/design/delivery document;
4. split work into bounded phases;
5. assign independent reconnaissance or implementation where scopes do not overlap;
6. implement one coherent slice;
7. format, lint, test, and inspect the diff;
8. commit as a cognitive checkpoint;
9. run correctness, cleanliness, security, performance, documentation, or acceptance audits;
10. update the ledger and continue.

Commits function as punctuation and durable state boundaries, not end-of-day dumps.

## Human role

Ian's recurring role is:

- select the problem and desired invariant;
- challenge architecture and naming;
- decide clean-break versus compatibility policy;
- gate implementation after design discussion;
- partition parallel work;
- reject weak tests or policy-evasion;
- test outcomes independently;
- decide whether evidence is sufficient to call a goal complete;
- integrate the result into a larger system.

The agents provide reconnaissance, implementation throughput, review, documentation, and repetitive transformation. The process is intentionally not “ask once and accept the generated repository.”

## Multi-agent orchestration

The archive shows repeated use of:

- read-only scout agents before architecture changes;
- parallel, non-overlapping file/module assignments;
- separate architecture and implementation agents;
- specialized correctness, security, optimization, documentation, and housekeeping passes;
- model tiering by task cost and reasoning depth;
- worktrees or sandboxed identities when write scopes would overlap;
- parent-session validation of agent claims;
- explicit termination of unhelpful agent waves.

Representative March examples include eight parallel scope documents, five research sessions, and nine technical-writer passes. Field Board's summed agent wall time exceeded calendar time because multiple sessions ran concurrently.

## Validation philosophy

- Tests should prove the intended architecture rather than weaken it until green.
- Compatibility is not preserved automatically in personal software.
- Generated bulk work is reviewed with counts, samples, idempotency, targeted searches, and broad validation.
- Goal completion is audited separately from implementation completion.
- One May 2026 goal session produced seven committed phases, separate acceptance proofs, and an LLM goal-completion audit that explicitly refused to call the overall goal complete while persistence/provider/recovery requirements remained unresolved.

## Cross-language systems orientation

Recurring architecture deliberately separates platforms from consumers:

- Monk: TypeScript platform with Rust/TypeScript/Go/protocol consumers;
- Muninn: Rust kernel and frames with TypeScript and Go consumers;
- Cephalopodic: Go control plane/security with React/TypeScript, Python, SQL, and Rust surfaces;
- Faber: Rust compiler with Faber corpus and multiple comparison/validation targets;
- Field Board: shared Rust protocol across server, Leptos/WASM client, native canvas, CLI, traces, and perf harness;
- Swarm: Rust runtime with separated presentation and native-client boundaries.

---

# Part IV — Conventional career and company history

## Chronology

| Period | Organization/activity | Role | Location/context | Evidence |
| --- | --- | --- | --- | --- |
| 1996-05-21–2000-05-20 | United States Marine Corps | Corporal (E-4), 0351 Assaultman; small-boat qualification | United States; service record includes Marine Corps assignments | A — DD-214, honorable discharge |
| 1999–2000 | KMap / open source | Creator and developer | Linux/KDE open-source community | A — source archive, Nmap announcement, Ian's release post |
| 2002–2007 | Florida real estate | Licensed real-estate sales | Gainesville, Florida area | C — two older career records; licensing not independently reviewed |
| 2008-02–2009-04 | Beatport | Software Developer; resume describes Senior Software Engineer | Denver, Colorado | A for employment/title; C for detailed stack/responsibility narrative |
| 2009 | Red Hat | Technical Architect / Software Engineer | Raleigh, North Carolina; APAC Partner Center work | C — two consistent resumes, technical narrative, RHCE context; employer-issued record missing |
| 2009–2010 | Independent Salesforce consulting | Founder / consultant | Remote/client work | C — older resumes; company identity unresolved, possibly M43 Instead |
| 2011-09-05–2015-06-15 | roundCorner | Chief Scientist; functionally Chief Software Architect; later VP Engineering | New York office plus distributed/global work | A for employment and dates; B for later title progression |
| 2012 onward | Applied Aim Inc | Founder / outside consultant | Delaware corporation; client work during roundCorner period | A for entity and paid client activity |
| 2014–2017 | Minted.IO and related entities | Founder / software developer / IP owner | Puerto Rico, New York, New Hampshire context | A/B depending title and entity relationship |
| 2016-02-22–2017-02 | Salesforce.com, Inc. | Technical Solution Architect; later described as Senior Technical Architect | Atlanta/east-coast client consulting | A for employment/start; C for client/responsibility detail |
| 2017-02–by 2019-07 | Motivis Learning Systems | VP, Platform Research and Development / Software Engineering | Salem/Nashua, New Hampshire; initially remote from North Carolina | A — executed offer tied to Minted.IO acquisition |
| 2019-07–2020 | Motivis via Minted Geek OÜ | Independent platform/strategy consultant | Remote/international company structure | A — executed agreement and detailed scope |
| 2019 onward | Minted Geek entities | Founder, director/officer, consultant | United States, Estonia, and related jurisdictions | A/B — entity and contract records; individual venture outcomes vary |
| 2020-12 onward | Technology consulting through Minted Geek OÜ | Independent engineering consultant | Remote | A for executed agreement; client-sensitive scope omitted |
| 2021–2024 | Early retirement / independent interests | Not conventional employment | North Carolina and personal projects | C — Ian's account; exact boundary intentionally approximate |
| 2025–present | Independent AI and systems R&D | Founder-level builder, systems engineer, research director | Self-funded/independent | A — repositories, Git, transcripts, trials, tests, goals, and artifacts |

## United States Marine Corps

- Active service from May 21, 1996 through May 20, 2000.
- Honorable discharge.
- Final rank Corporal, pay grade E-4.
- MOS 0351 Assaultman.
- Small-boat qualification/responsibility.
- Decorations and military education are present in the DD-214 but should be transcribed only if relevant to a military-service section.

## Early open source: KMap and Koog

### KMap

- C++/Qt/KDE graphical frontend for Nmap.
- Released publicly by January 2000.
- Linux and FreeBSD compilation discussed in Ian's contemporary announcement.
- Nmap's own release archive names Ian as the author of a KDE frontend.

### Koog Epsilon

- KDE-era Napster client preserved in the archived source collection.
- Demonstrates early desktop UI, protocol, network-client, and open-source work.
- Original dates/authorship should be grounded from source headers and archive history before detailed publication.

## Beatport

- Employer record identifies Ian as Software Developer in the Software Development department.
- Performance review covers calendar 2008.
- Payroll, benefits, and termination records establish employment through early April 2009.
- Resume narrative places Ian on the core API/engineering team.
- Reported stack: Zend PHP, Mule ESB, enterprise Java, Spring, Hibernate, Maven, Squid, Akamai, and MySQL.

## Red Hat

- Two consistent historical resumes describe Technical Architect / Software Engineer work in 2009.
- Reported project: multilingual APAC Partner Center Portal across Korea, Japan, and China.
- Reported Salesforce features: Translation Workbench, Apex, Visualforce, more than 20 sandboxes, large Ultimate Edition license allocations, and limited production deployment access.
- Reported responsibility: implementation oversight plus internal mentoring on engineering practices.
- RHCE Enterprise Linux 5 appears in historical credential records and the 2023 resume.
- No Red Hat offer, payroll, W-2, separation, or benefits record has been found.
- Old email reportedly preserves interview and follow-up discussion, but it has not been incorporated into the evidence archive.
- This role is credible and resume-usable, but remains evidence grade C internally.

## Independent Salesforce consulting before roundCorner

- Historical resumes describe a one-person Salesforce consulting firm operating approximately 2009–2010.
- The firm closed or changed when Ian joined roundCorner full-time.
- The 2011 roundCorner agreement explicitly names Ian as owner of M43 Instead, LLC and permits continued board-approved outside consulting.
- It is not yet confirmed whether M43 Instead is the same firm described in the 2009–2010 resume entry.

## roundCorner

### Employment and title progression

- Executed employment agreement effective September 5, 2011.
- Formal starting title: Chief Scientist.
- Agreement scope: strategy, process and computerized information services, software applications, client delivery, and related leadership.
- Resume functional title: Chief Software Architect.
- Later resume and public-company-profile title: Vice President of Engineering.
- Exact title-change dates remain unresolved.
- Equity agreements from 2011 and 2013 corroborate continued service and meaningful incentive participation.
- Employment ended June 15, 2015 and transitioned immediately to contracting through Ian's Puerto Rico company.

### Reported leadership and delivery

- Technical ownership of company engineering and Salesforce implementation architecture.
- Transition from custom implementations toward a product-line model.
- Reported engineering/product team growth from four to twelve.
- Reported supervision of onshore and offshore engineering, QA, analyst, and support staff across four continents and full-day timezone coverage.
- Jenkins, Ant, and Salesforce continuous integration.
- Training, interviewing, mentoring, standards, and engineering-management responsibility.
- Reported customers included nonprofit, education, healthcare, media, and foundation organizations.
- The roundCause product was later associated with Salesforce NGO Connect in historical career material; exact transaction/product lineage needs separate corroboration before stating an acquisition as fact.

## Applied Aim Inc

- Delaware corporation effective April 9, 2012.
- Tax, banking, and two 2012 Form 1099 records establish paid client activity.
- Operated during the roundCorner period as an outside consulting vehicle.
- Client names and financial details should remain private unless selected for a case study.
- Relationship to M43 Instead and the earlier consulting firm is unresolved.

## Minted venture and entity history

Minted was not one uninterrupted legal company. It was a sequence of software brands, operating entities, IP holdings, partnerships, and consulting vehicles.

### Product/IP continuity

- Minted Geek existed as a software brand/domain/source asset by February 2015.
- A signed 2015 IP-separation memorandum records Ian retaining the Minted Geek website, source, domain, branding/training material, `mintedFinancial`, and `mintedWarehouse`.
- Minted.IO existed as a Puerto Rico entity by May 6, 2014.
- Historical resumes describe a focused self-funded Minted.IO platform-development period in 2015.
- A later New York Minted.IO entity sold software-platform and API-development assets to Motivis in February 2017.
- Motivis's executed employment offer expressly conditioned Ian's VP role on that acquisition.

### Entities

| Entity | Period/evidence | Defensible fact |
| --- | --- | --- |
| Minted.IO LLC, Puerto Rico | 2014 onward | Organized May 6, 2014; registrations, permits, and tax filings exist |
| Minted Technology & Consulting, Hong Kong | By February 2015 | Incorporation records and executed software/IP division |
| Minted Geek Kft, Hungary | 2015-era | Appears in IP-division record; separate operating history unresolved |
| Minted.IO LLC, New York | 2015–2017 era | Seller in Motivis asset acquisition |
| Minted Geek Inc, United States | 2019 | Ian documented as attending director/chair/secretary with president authority |
| Minted Geek Panama Inc | 2019 | Registered entity; beneficial ownership/operations not fully reviewed |
| Minted Geek OÜ, Estonia | 2019 onward | Ian founder and management-board member; computer programming declared activity; consulting contracts |
| Minted Geek Capital LLC | 2021 onward | Formation, operating agreement, and annual-report records |

Formation alone does not prove revenue, traction, headcount, or success. The strongest venture claim is the creation and sale of the Minted.IO software/API assets, followed by executive employment and later consulting.

## Salesforce.com

- Executed offer title: Technical Solution Architect.
- Start date: February 22, 2016.
- Payroll statements span February 2016 through February 2017.
- Historical resume title: Senior Technical Architect / consultant.
- Reported client work included large east-coast enterprises such as CarMax and Home Depot.
- Reported specialization: Sales Cloud, Service Cloud, Force.com architecture, Apex, Visualforce, and external integrations.
- Historical records list roughly ten Salesforce certifications and CTA-candidate work.
- “Hero of the Month — Southeast Region” appears in the 2023 resume and needs independent verification before prominent use.

## Motivis Learning Systems

### Executive employment

- Executed offer dated January 18, 2017.
- Position: Vice President, Platform Research and Development.
- Reported directly to the CEO.
- Employment conditioned on acquisition of Minted.IO assets.
- Effective hire date was tied to the February 2017 closing.
- Historical resume describes leadership of an approximately ten-person frontend/backend team.
- Reported stack: TypeScript/ES6, Node.js, PostgreSQL, Google Cloud.
- Responsibilities included platform engineering/R&D, build/deployment, Salesforce/Amazon/Google/Stripe integrations, and strategic platform work.

### Independent consulting

- By July 1, 2019, the legal relationship had shifted to independent consulting through Minted Geek OÜ.
- Executed scope included Cloud API architecture planning, roadmap prioritization, design/development/testing of key improvements, DevOps documentation and handoff, executive strategy, and stakeholder discussions.
- Agreement could continue through the end of 2020.
- Exact employee end date remains unresolved.

## Minted Geek consulting

- US corporate records establish Ian's director/officer activity in 2019.
- Estonian records identify Ian as founder and management-board member of Minted Geek OÜ.
- Motivis consulting through the entity is directly documented beginning July 2019.
- A separate December 2020 agreement documents engineering consulting through Minted Geek OÜ for another technology company.
- Client-sensitive commercial terms should not be published.

## Education

- University of Massachusetts Amherst documentation supports a bachelor's degree.
- Historical resume describes a Bachelor of Business Administration completed in 2020 after part-time study beginning in 2008.
- Exact degree title and conferral date should be transcribed from the validated credential before final publication.

## Certifications and credentials

Historical records identify:

- Red Hat Certified Engineer, Enterprise Linux 5;
- Salesforce Sales Cloud Consultant;
- Salesforce Service Cloud Consultant;
- Salesforce Force.com Advanced Developer;
- Salesforce Advanced Administrator;
- Salesforce Data Architecture & Management Designer;
- Certified ScrumMaster;
- Sun Certified Java Programmer, Java 6;
- MySQL Certified Developer;
- Cisco CCENT/CCNA exam records;
- CompTIA/VA reimbursement records for A+, Network+, and Security+ work.

Certification issue/expiration/current-status details should be individually checked before publishing a current credentials list.

---

# Part V — Languages and technical capability

## Strong current languages

### Rust

Primary current systems language across:

- Radix/Faber compiler and CLI;
- Swarm runtime;
- Abbot/Prior/Muninn kernels;
- Field Board server/client/canvas/protocol/CLI;
- Gofolio CLI;
- Cassio;
- QRStatic;
- Cephalopodic CLI components;
- developer and system utilities.

### TypeScript / JavaScript

- Monk API and platform ecosystem;
- earlier Motivis cloud platform;
- Faber trial harness;
- React/Astro/SvelteKit presentation surfaces;
- SDKs, bindings, web applications, and infrastructure tooling.

### Go

- Gofolio API;
- Cephalopodic control-plane/security components;
- FUSE and protocol work;
- compiler comparison/emission targets;
- services and tooling.

### Python

- LegacyLens and RAG work;
- evaluation harnesses;
- local inference/tuning;
- data processing, scripts, and research automation.

## Historical and supporting languages

- PHP/Zend from Beatport and archived platform work;
- Java/Spring/Hibernate and JMS/ActiveMQ-era systems;
- Apex/Visualforce/Salesforce metadata and automation;
- C and C++/Qt/KDE from early open source and compiler/runtime targets;
- Svelte/SvelteKit, React, Angular, Leptos/WASM;
- SQL/PostgreSQL/SQLite;
- shell, Docker, CI/release automation;
- Faber itself;
- experimental Zig, WGSL, Metal, LLVM text, Racket/sexp, and WebAssembly surfaces.

Language lists should be attached to systems and outcomes, not rendered as a context-free keyword wall.

---

# Part VI — Recommended interactive website content model

## Default information hierarchy

The public site should lead with current R&D, not ancient chronology:

1. **Current R&D overview** — scale, active programs, operating method, and why it matters.
2. **Interactive research timeline** — September 2025 to present, month/phase/project drill-down.
3. **Research-program map** — Faber, Swarm, agent kernels, Monk, Field Board, Trials, Gofolio, Cephalopodic, applied experiments.
4. **Selected project field reports** — architecture, timeline, decisions, trials, tests, artifacts, transcripts, demos, repository links.
5. **Historical career timeline** — military, early open source, Beatport, Red Hat, consulting, roundCorner, Minted, Salesforce, Motivis.
6. **Evidence ledger** — public links plus private-document verification summaries.
7. **Full repository archive** — searchable supporting catalog.

## Two coordinated timelines

### Research timeline: default

Granularity:

- year/quarter;
- month;
- research program;
- goal/campaign;
- delivery phase;
- commits and validation;
- trials/results;
- transcript evidence;
- live artifact or repository.

Suggested default window: **November 2025–present**, where sustained intensity begins. August–October can appear as prologue/source recovery.

### Career timeline: secondary

Granularity:

- organization/entity;
- title and formal versus functional title;
- location and employment/consulting/founder status;
- products and responsibilities;
- transition to the next role;
- evidence grade and source summary.

## Project drill-down template

Field Board's existing presentation is the model. Each major project can expose:

1. **Overview** — problem, thesis, current status, dates.
2. **Architecture** — interactive repository/crate/service graph.
3. **Timeline** — phases or days, commit counts, named milestones, decisions.
4. **Trials/evidence** — experiments, tests, benchmarks, acceptance proofs.
5. **Transcripts** — selected human/agent decision excerpts, not raw dumps.
6. **Artifacts** — screenshots, videos, diagrams, live demos, releases.
7. **Repositories** — exact public links and private metadata summaries.

## Candidate project field reports

Priority order:

1. Faber/Radix;
2. Minted Geek Swarm;
3. Field Board;
4. Trials/Faber Trials;
5. Monk;
6. Agent-kernel lineage: Abbot → Prior → Muninn → Swarm;
7. Gofolio and its live evaluation UI;
8. Cephalopodic/Fortress;
9. LegacyLens;
10. QRStatic.

## Interaction ideas grounded in existing work

- A research activity histogram using the monthly deduplicated commit table.
- Toggle between commits, transcript root sessions, active days, tests, and trial-result counts.
- Click a month to reveal active programs and representative goals.
- Click a program to reveal repo/crate dependency graphs.
- Click a factory initiative to reveal goal → phases → ledger → acceptance evidence.
- Switch a project between Architecture, Timeline, Trials, Transcripts, and Artifacts views.
- Show “time-stamped snapshot” labels whenever metrics changed during rapid iteration.
- Let users choose “story,” “technical,” or “evidence” depth.
- Keep private repositories visible as named systems with architecture summaries, but never link or leak private URLs/content.
- Pair quantitative density with selected decisions; do not reduce the work to vanity counts.

---

# Part VII — Source map and unresolved questions

## Primary local sources

- Career evidence corpus: `/Users/ianzepp/work/ianzepp/career-corpus/`
- Transcript archive: `/Users/ianzepp/work/ianzepp/transcripts/`
- Work-proof documents: `/Users/ianzepp/Desktop/Work Proof/`
- Repository inventory generator and CSVs: `/Users/ianzepp/work/ianzepp/career-corpus/inventory/`
- Faber: `/Users/ianzepp/work/faberlang/`
- Swarm: `/Users/ianzepp/work/minted-geek-swarm/`
- Field Board: `/Users/ianzepp/work/ianzepp/fieldboard/`
- Trials: `/Users/ianzepp/work/ianzepp/trials/`
- Monk: `/Users/ianzepp/work/ianzepp/monk-*`
- Gofolio: `/Users/ianzepp/work/ianzepp/gofolio-*`
- Cephalopodic: `/Users/ianzepp/work/cephalopodic/`
- Abbotik: `/Users/ianzepp/work/abbotik/`

## Public sources

- Nmap 2.50 release: <https://insecure.org/stf/Nmap-2.50-Release.html>
- KMap 0.7 announcement: <https://seclists.org/nmap-announce/2000/1>
- roundCorner company profile: <https://www.gaebler.com/Funded-Company-0F5780A5-FE79-4BE4-B38A-753CAE0641D0-roundCorner>
- GitHub profile: <https://github.com/ianzepp>
- Field Board live/demo material and repository links are recorded in its README.

## Representative transcript evidence handles

- Faber Trials matrix and executable grading: `/Users/ianzepp/work/ianzepp/transcripts/2026-01/2026-01-05.daily.md`, grounded in `2026-01-05T18-29-27-claude.md`.
- Field Board Leptos rewrite, canvas tests, and binary frames: `/Users/ianzepp/work/ianzepp/transcripts/2026-02/2026-02-18.daily.md` and `2026-02-19.daily.md`, including `2026-02-19T13-30-44-claude.md`.
- Reusable Gofolio/Muninn/Prior evaluation and implementation patterns: `/Users/ianzepp/work/ianzepp/transcripts/2026-03/2026-03-14.daily.md`.
- Prior factory/compiler-pass analogy and control plane: `/Users/ianzepp/work/ianzepp/transcripts/2026-03/2026-03-17.daily.md`.
- QRStatic empirical codec work: `/Users/ianzepp/work/ianzepp/transcripts/2026-03/2026-03-16.daily.md`, including `2026-03-16T18-10-50-claude.md`.
- Goal-driven phased delivery and honest incomplete-goal audit: `/Users/ianzepp/work/ianzepp/transcripts/2026-05/2026-05-03T19-08-00-codex.md`.
- July Faber factory goal/plan/ledger density: `/Users/ianzepp/work/ianzepp/transcripts/2026-07/2026-07-01T00-23-17-pi.md`, `2026-07-01T01-59-17-pi.md`, and `2026-07-01T07-16-57-codex.md`.

## Material uncertainties

- Exact Red Hat start/end dates and direct employer documentation.
- Whether M43 Instead, Applied Aim, and the 2009–2010 consulting entry represent one business lineage or separate entities.
- Exact roundCorner title-promotion dates.
- Exact employee-to-contractor transition date at Motivis beyond “no later than July 1, 2019.”
- Relationship/migration between Puerto Rico and New York Minted.IO entities.
- Commercial outcomes of each Minted legal entity.
- Exact degree title/conferral date.
- Current validity and issue/expiration dates of historical certifications.
- Customer names, revenue, team metrics, acquisition/product lineage, and awards that rely only on older resume material.
- Which private current projects can be described publicly and at what architectural depth.

## Attribution exclusions

Do not describe imported or upstream repositories as original work without targeted authorship review. Known reference/upstream trees include:

- `bt-search/*`;
- `llama.cpp`;
- MediaPipe upstream;
- Ghostfolio upstream;
- `dxx-rebirth`;
- `build-your-own-x`;
- Gauntlet source/input repositories.

These may support contribution, evaluation, modernization, or comparative-analysis stories only when Ian-authored changes are isolated.

---

# Short factual positioning statement

Ian Zepp is a software founder, former engineering executive, and systems-oriented independent researcher. His earlier career spans open-source Linux tooling, API and platform engineering, Salesforce architecture, engineering leadership, company formation, an acquired software/API platform, and executive platform R&D. Since late 2025, he has operated a self-funded AI-assisted software research program covering compilers, multi-agent runtimes, programmable platforms, MCP security, full-stack Rust, evaluation science, local inference, retrieval systems, and developer infrastructure. The work is documented through more than 17,000 deduplicated recent commits, thousands of archived direct and delegated agent interactions, hundreds of goal/campaign/ledger artifacts, thousands of tests, more than 17,000 recorded Faber trial executions, and multiple production-shaped systems spanning Rust, TypeScript, Go, Python, WebAssembly, and protocol-specific consumers.
