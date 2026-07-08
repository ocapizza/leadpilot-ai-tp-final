# Checklist de entrega

## 6. Prueba, Documenta y Entrega

- Test de estres: documentado con 6 casos en `tests/test_stress_log.txt`.
- Camino infeliz: incluido en casos T02, T03, T05 y T06.
- Video demo: `evidencias/demo_leadpilot_ai.mp4`, duracion 3 minutos.
- Credenciales/API keys: no se incluyen en el repositorio ni se muestran en el video.
- PDF arquitectura: `LeadPilot_AI_Diagrama_Arquitectura.pdf`.
- JSON n8n: `leadpilot_ai_n8n_workflow.json`.
- Link base de datos: incluido en `README.md`.
- Evidencias: carpeta `evidencias/`.

## Check de seguridad

- Filtro anti bucles infinitos: Gmail Trigger usa busqueda acotada por asunto y `newer_than:1d`.
- Comparacion de tipos: filtros IF comparan numero contra numero para datos faltantes y string contra string para decision humana.
- Prompt dinamico: `prompts/openai_prompt.md` usa variables del flujo como nombre, email, asunto, mensaje e historial.
- Resiliencia API IA: OpenAI usa `continueOnFail` y deriva a `04c Error Handling - Registrar fallo API IA`.

## Nota de ejecucion

La credencial de OpenAI queda pendiente para que el profesor conecte su propia API key durante la correccion. Gmail y Airtable quedaron configurados en n8n Cloud.
