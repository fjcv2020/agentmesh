# AgentMesh Project

## Project Vision

AgentMesh is a multi-runtime delivery system designed to execute software work end-to-end as a realistic team (manager + specialists), with strong quality gates and a single system of record.

## Runtime Strategy (Codex-first, interoperable)

- **Codex (default runtime)**: implementation, refactoring, test fixing, technical execution.
- **Claude Code**: discovery, planning, architecture, risk analysis.
- **GitHub CLI (`gh`)**: issue/PR lifecycle and status persistence.

Runtime adapters are declared in `.claude/orchestration/runtime-adapters.json`.

## Team Topology

### Management & Product
- **Engineering Manager** (`management/engineering-manager`)
- **Product Manager** (`product/product-manager`)

### Engineering
- **Fullstack Developer** (`development-team/fullstack-developer`)
- **Cloud Architect** (`devops-infrastructure/cloud-architect`)
- **Platform Engineer** (`devops-infrastructure/platform-engineer`)

### Quality
- **QA Automation** (`quality/qa-automation`)

## Core Skills

### Orchestration
- **Work Orchestration** (`management/work-orchestration`)
- **GitHub CLI Ops** (`orchestration/github-cli-ops`)

### Development
- **Codex Execution** (`development/codex-execution`)
- **Agent Development** (`development/agent-development`)
- **MCP Builder** (`development/mcp-builder`)
- **GCP Cloud Run** (`development/gcp-cloud-run`)

### Quality
- **Senior QA** (`development/senior-qa`)
- **Browser QA** (`quality/browser-qa`)

## Delivery Workflow (MVP)

1. Product Manager refines request and acceptance criteria.
2. Engineering Manager decomposes tasks and assigns owner roles.
3. Dispatcher maps each task to a runtime (`scripts/agentmesh_dispatcher.py`).
4. Specialists execute work in Codex/Claude Code.
5. GitHub CLI persists artifacts and state transitions.
6. QA validates behavior and manager requests human approval when needed.

## Operating Contracts

- Task handoffs follow `docs/task-schema.json`.
- Stage ownership and gates are defined in `.claude/orchestration/pipeline.json`.
- Runtime mapping is defined in `.claude/orchestration/runtime-adapters.json`.
- Additional operating references:
  - `docs/agentmesh-blueprint.md`
  - `docs/phased-roadmap.md`
  - `docs/runtime-interoperability.md`

## Agent Mesh Team System 🤖

An **autonomous team of 5 specialist agents** that coordinates to deliver work end-to-end:

- **Manager** - Orchestrates all work, breaks down tasks, coordinates team
- **Researcher** - Investigates unknowns, validates approaches, creates POCs
- **Developer** - Implements features end-to-end (backend, frontend, tests)
- **Architect** - Designs infrastructure and ensures scalability/security
- **QA** - Tests, validates quality, performs security/performance checks

See `.claude/agents/AGENT_MESH.md` for complete team documentation and usage examples.

### Quick Example

```
User: "Build user authentication with OAuth2 + GitHub"
     ↓
Manager: Breaks down into subtasks for Researcher, Developer, Architect, QA
     ↓
Researcher: Validates OAuth2 best practices
Developer: Implements backend + frontend
Architect: Designs session storage & security
QA: Creates test suite
     ↓
Manager: Coordinates review, requests user validation
     ↓
Deploy via GitHub
```

## Next Milestones

1. ✅ **Agent Mesh Team Created** - Manager + 4 specialists configured
2. Wire dispatcher output to automatic `gh issue comment` updates.
3. Add Slack notifications for blocked/ready-for-review transitions.
4. Add Linear synchronization once GitHub-first flow is stable.
5. Integrate Manager agent into dispatcher workflow for automatic orchestration.
