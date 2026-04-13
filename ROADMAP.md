# Roadmap de Mejoras para A.U.R.A Core

Este documento detalla las mejoras de prioridad media y baja para el proyecto A.U.R.A. Las de alta prioridad ya han sido implementadas (seguridad, pruebas básicas, refactorización inicial).

## Prioridad Media

### Rendimiento y Escalabilidad
- **Base de datos para memoria**: Migrar de `memory.json` a SQLite o TinyDB para mejor manejo de datos grandes.
- **Optimización de decaimiento**: Implementar decaimiento exponencial basado en tiempo real.
- **Caché de respuestas**: Agregar caché LRU para respuestas similares.
- **Procesamiento asíncrono**: Usar asyncio para búsquedas web y comandos.

### Funcionalidades (del Roadmap Original)
- **Clasificación inteligente de memoria**: Usar embeddings para relevancia.
- **Resumen automático**: Integrar modelo de resumen vía Ollama.
- **Acciones compuestas**: Permitir secuencias multi-step.
- **Detección de intención mejorada**: Clasificador ML con scikit-learn.

### Experiencia de Usuario
- **Interfaz gráfica**: UI simple con Tkinter o Flask.
- **Soporte multilingüe**: Extender a inglés/francés.
- **Modos de personalidad**: Implementar modos técnico/casual.

## Prioridad Baja

### Integraciones y Compatibilidad
- **Más modelos LLM**: Soporte para Mistral, CodeLlama, etc.
- **Búsqueda web avanzada**: APIs como SerpAPI para resultados ricos.
- **Compatibilidad OS**: Soporte nativo para Linux/Mac.

### Monitoreo y Mantenimiento
- **Logging estructurado**: Usar loguru para debug.
- **Versionado de memoria**: Backups automáticos.
- **Benchmarking**: Scripts de medición de rendimiento.

### Otras Funcionalidades
- **Plugins externos**: Sistema de plugins con importlib.
- **Notificaciones**: Integración con sistema para alertas.
- **Personalidad adaptativa**: Aprendizaje del feedback del usuario.

## Notas de Implementación
- Cada mejora debe incluir tests unitarios.
- Actualizar este roadmap a medida que se implementen.
- Priorizar basándose en feedback de usuarios.