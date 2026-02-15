# Roadmap de implementación paso a paso

## Fase 0 — Diseño operativo (1-2 días)
- Definir roles, contratos y workflow.
- Definir política de runtime: Codex-first + Claude para planning + `gh` para estado.
- Acordar checklist de aceptación.

## Fase 1 — GitHub-first + dispatch básico (3-5 días)
- Manager crea issue padre + subtareas con `gh`.
- Asignación por rol y estado.
- Dispatcher sugiere runtime por tarea.
- PR template con secciones obligatorias (cambios, tests, riesgos).

## Fase 2 — Ejecución técnica fiable (1 semana)
- Skill packs ejecutables por rol crítico.
- Testing unit/integration.
- Browser QA para UI.

## Fase 3 — Slack loop (3-4 días)
- Notificar: task_started, blocked, qa_failed, ready_for_review.
- Canal único para aprobaciones humanas.

## Fase 4 — Linear sync (3-5 días)
- Mapeo GitHub ⇄ Linear.
- Reconciliación diaria de estados.

## Fase 5 — Optimización (continuo)
- Métricas: cycle time, failure rate, rework, lead time.
- Postmortems automáticos en fallos repetidos.
- Mejora continua de skills y reglas de dispatch.
