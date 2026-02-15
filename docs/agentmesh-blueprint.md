# AgentMesh Blueprint (Codex + Claude Code + GitHub CLI)

## 1. Objetivo
Construir una fábrica multi-agente que entregue tareas de principio a fin con validación incremental contigo.

## 2. Principios operativos
1. **Codex-first execution** para trabajo de implementación.
2. **Claude for planning depth** en discovery/arquitectura/riesgos.
3. **GitHub como sistema de registro** para estado y evidencias.
4. **Contratos estructurados** en vez de prompts libres para handoffs.
5. **Quality gates + checkpoints humanos** antes de cerrar tareas.

## 3. Modelo de interoperabilidad
- Todos los runtimes consumen y producen el mismo contrato (`docs/task-schema.json`).
- El manager decide owner_role; el dispatcher decide runtime recomendado.
- Tras cada ejecución, el estado se sincroniza con `gh`.

## 4. Flujo E2E mínimo viable
1. Intake (objetivo + restricciones + acceptance criteria).
2. Planning (descomposición, riesgos, dependencias).
3. Dispatch (selección de runtime por rol/estado).
4. Implementación y pruebas.
5. QA funcional/técnico.
6. PR con evidencia.
7. Aprobación humana.
8. Cierre + retro para mejorar skills.

## 5. Roles sugeridos
- Engineering Manager, Product Manager, Tech Lead
- Backend/Frontend/Platform
- QA Automation (browser + regresión)

## 6. Integración por fases
- **Fase 1**: GitHub CLI obligatorio.
- **Fase 2**: Slack para notificaciones y aprobación rápida.
- **Fase 3**: Linear para sincronización bidireccional.

## 7. DoD
Una tarea está terminada solo si:
- Cumple ACs
- Tiene tests/evidencia
- Tiene PR y reporte QA
- Tiene estado final sincronizado en GitHub
