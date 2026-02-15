# Runtime interoperability: Codex + Claude Code + GitHub CLI

## Objetivo
Hacer que los tres runtimes funcionen como un solo equipo, evitando lock-in a una sola herramienta.

## Contrato único
Todos los agentes y runtimes intercambian tareas con `docs/task-schema.json`.

## Reglas de ruteo
1. **Planificación y arquitectura** → Claude Code.
2. **Implementación y correcciones** → Codex.
3. **Persistencia de estado (issues/PR/reviews)** → GitHub CLI.
4. **Riesgo alto** → aprobación del manager antes de merge.

## Adaptadores
- Configuración declarativa: `.claude/orchestration/runtime-adapters.json`
- Resolución operativa de runtime: `scripts/agentmesh_dispatcher.py`

## Ejemplo de uso
```bash
python scripts/agentmesh_dispatcher.py examples/task-sample.json
```

Salida esperada (resumen):
- runtime recomendado (`codex` o `claude-code`)
- owner_role
- estado actual
- acción posterior: sincronizar con `gh`

## Integración gradual
- **Paso 1**: usar dispatcher en local para validar asignación.
- **Paso 2**: ejecutar runtime seleccionado y publicar resultado en issue.
- **Paso 3**: automatizar el ciclo con CI y comentarios automáticos en PR.
