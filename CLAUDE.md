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

## Next Milestones

1. Wire dispatcher output to automatic `gh issue comment` updates.
2. Add Slack notifications for blocked/ready-for-review transitions.
3. Add Linear synchronization once GitHub-first flow is stable.
