# 🤖 AgentMesh - Autonomous Development Team

## Overview

AgentMesh is an autonomous development team system where specialized agents collaborate to deliver complete features and fixes. The team is orchestrated by a Project Manager (PM) agent that coordinates work, manages timelines, and ensures quality.

## Team Structure

```
┌─────────────────────────────────────────┐
│     Manager (PM/Orchestrator)           │ ◄── Entry point for all tasks
│  • Task breakdown                       │
│  • Team coordination                    │
│  • Status management                    │
│  • User validation                      │
└──────────────┬──────────────────────────┘
               │
        ┌──────┴───────┬──────────┬──────────┐
        │              │          │          │
   ┌────▼──────┐ ┌───▼────┐ ┌──▼────┐ ┌───▼────┐
   │Researcher │ │Developer│ │Architect│ │  QA    │
   │           │ │         │ │        │ │        │
   │Investigation│ │Implementation│ │Infrastructure│ │Quality│
   └───────────┘ └─────────┘ └────────┘ └────────┘
```

## Agent Roles & Responsibilities

### 🎯 Manager (PM/Orchestrator)
**Role**: Project Manager and Team Leader

**Responsibilities**:
- Parse incoming tasks and break them into subtasks
- Distribute work to specialized team members
- Coordinate between team members and resolve conflicts
- Validate deliverables against requirements
- Manage timelines and dependencies
- Report status and identify blockers
- Request user validation when needed
- Create GitHub branches and coordinate PRs

---

### 🔍 Researcher
**Role**: Investigation & Validation Specialist

**Responsibilities**:
- Validate technical approaches and architectural decisions
- Research best practices and industry standards
- Investigate unknown challenges
- Create POC (Proof of Concept) solutions
- Provide recommendations with tradeoffs analysis

---

### 💻 Developer (Fullstack)
**Role**: Implementation Specialist

**Responsibilities**:
- Implement backend APIs
- Implement frontend components
- Design and manage databases
- Write unit and integration tests
- Create comprehensive documentation
- Make Git commits following conventions

---

### 🏗️ Architect
**Role**: Infrastructure & Design Specialist

**Responsibilities**:
- Design cloud architecture
- Ensure scalability and performance
- Implement security best practices
- Create Infrastructure as Code
- Design disaster recovery strategies

---

### ✅ QA (Senior QA)
**Role**: Quality Assurance & Validation

**Responsibilities**:
- Design test strategies
- Create automated test scenarios
- Validate requirements compliance
- Identify bugs and edge cases
- Approve code for release

---

## How to Use

### Step 1: Assign Task to Manager
Give the Manager agent a task with clear requirements:

```
"Build API endpoint for user registration with:
- Email validation
- Password hashing
- Rate limiting
- Comprehensive tests"
```

### Step 2: Manager Coordinates
The Manager will:
1. Break down the task
2. Engage appropriate team members
3. Keep you updated
4. Escalate decisions needing your input

### Step 3: Monitor & Validate
- Watch status updates
- Respond to escalations
- Validate deliverables
- Approve for release

---

## Integration with Multi-Runtime System

This Agent Mesh integrates with the existing runtime strategy:

- **Codex**: Default runtime for implementation tasks
- **Claude Code**: Used for discovery, planning, architecture
- **GitHub CLI**: Handles PR/issue lifecycle

See `.claude/orchestration/runtime-adapters.json` for runtime configuration.

---

**Status**: 🟡 Phase 1 - Manual Task Assignment + Multi-Runtime Support
