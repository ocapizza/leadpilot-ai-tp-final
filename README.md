# LeadPilot AI - Ecosistema de Automatizacion IA Autonomo

Trabajo practico final para AI Automation.

## Caso de uso
LeadPilot AI automatiza la gestion de leads B2B recibidos por Gmail. El sistema registra el lead en Airtable, usa OpenAI para clasificarlo y redactar una respuesta, solicita aprobacion humana por Slack y finalmente responde por Gmail manteniendo el hilo original.

## Tecnologias integradas
- n8n: orquestador principal del flujo.
- Airtable: memoria del sistema y registro de estados.
- OpenAI GPT: procesamiento IA con prompt estructurado y salida JSON.
- Slack: punto Human-in-the-loop para aprobacion.
- Gmail: canal de entrada y salida multicanal.

## Archivos del entregable
- `LeadPilot_AI_Diagrama_Arquitectura.pdf`: documento PDF con arquitectura, resiliencia, HITL y pruebas.
- `leadpilot_ai_n8n_workflow.json`: workflow importable en n8n.
- `database/airtable_schema.csv`: estructura sugerida para Airtable.
- `database/airtable_schema.json`: version tecnica del esquema.
- `prompts/openai_prompt.md`: prompt dinamico usado por el nodo IA.
- `tests/test_stress_log.txt`: resultado de 5 pruebas documentadas.
- `evidencias/*.png`: capturas/evidencias para adjuntar en GitHub.

## Variables requeridas en n8n
- `AIRTABLE_BASE_ID`
- `SLACK_APPROVAL_CHANNEL`
- `N8N_WEBHOOK_URL`

Las credenciales de Gmail, Airtable, Slack y OpenAI deben configurarse en n8n Credentials. No se incluyen API keys ni secretos en el JSON.

## Link a base de datos
Completar al publicar: `[Airtable en modo lectura](PEGAR_LINK_AIRTABLE_AQUI)`

## Link a repositorio GitHub
Completar al publicar: `[Repositorio GitHub](PEGAR_LINK_GITHUB_AQUI)`

## Check de seguridad
- Filtro anti bucles en Gmail mediante busqueda de correos recientes y palabras clave.
- Prompt IA dinamico con variables del sistema.
- Max tokens limitado para optimizar costos.
- HITL antes de contactar al cliente final.
- Ruta de error para datos faltantes y fallas de API.
- Estados claros en Airtable para trazabilidad.
