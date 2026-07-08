# LeadPilot AI - Ecosistema de Automatizacion IA Autonomo

Trabajo practico final para AI Automation.

## Caso de uso
LeadPilot AI automatiza la gestion de leads B2B recibidos por Gmail. El sistema registra el lead en Airtable, usa OpenAI para clasificarlo y redactar una respuesta, solicita aprobacion humana por Gmail y finalmente responde manteniendo el hilo original.

## Tecnologias integradas
- n8n: orquestador principal del flujo.
- Airtable: memoria del sistema y registro de estados.
- OpenAI GPT: procesamiento IA con prompt estructurado y salida JSON.
- Gmail: canal de entrada, salida y punto Human-in-the-loop para aprobacion.

## Archivos del entregable
- `LeadPilot_AI_Diagrama_Arquitectura.pdf`: documento PDF con arquitectura, resiliencia, HITL y pruebas.
- `leadpilot_ai_n8n_workflow.json`: workflow importable en n8n.
- `database/airtable_schema.csv`: estructura sugerida para Airtable.
- `database/airtable_schema.json`: version tecnica del esquema.
- `prompts/openai_prompt.md`: prompt dinamico usado por el nodo IA.
- `tests/test_stress_log.txt`: resultado de 5 pruebas documentadas.
- `evidencias/*.png`: capturas/evidencias para adjuntar en GitHub.
- `evidencias/demo_leadpilot_ai.mp4`: video demo corto para la correccion.
- `CHECKLIST_ENTREGA.md`: verificacion punto por punto contra la consigna.

## Variables requeridas en n8n
- `AIRTABLE_BASE_ID`
- `APPROVER_EMAIL`
- `N8N_WEBHOOK_URL`

Las credenciales de Gmail, Airtable y OpenAI deben configurarse en n8n Credentials. No se incluyen API keys ni secretos en el JSON. La credencial de OpenAI queda pendiente para que el profesor use su propia API key al corregir.

## Link a base de datos
[Airtable - tabla Leads](https://airtable.com/appRAWorY6yPb4QJn/tblEx4UKF4j0bkVvr/viwd1TlkGIsdGkjva)

## Link a workflow n8n
[Workflow n8n Cloud](https://delroy2026.app.n8n.cloud/workflow/qSfCEYFOYzLFvlGc?projectId=KJrQfW9cIoac0mkH)

## Link a repositorio GitHub
[Repositorio GitHub](https://github.com/ocapizza/leadpilot-ai-tp-final)

## Check de seguridad
- Filtro anti bucles en Gmail mediante busqueda de correos recientes y palabras clave.
- Prompt IA dinamico con variables del sistema.
- Max tokens limitado para optimizar costos.
- HITL antes de contactar al cliente final.
- Ruta de error para datos faltantes y fallas de API.
- Estados claros en Airtable para trazabilidad.
