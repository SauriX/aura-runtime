A.U.R.A Runtime

========================
Requisitos
========================

- Python 3.10+
- Ollama instalado y ejecutándose en local
- Modelo recomendado:
  - llama3
- Endpoint local:
  - http://localhost:11434


========================
Instalación 
========================

pip install -r requirements.txt

Nota:
Puedes omitir git clone y cd si ya tienes el proyecto descargado o lo manejas localmente.


========================
Roadmap
========================

[Memoria]
- Clasificación de memoria relevante (no heurística)
- Resumen automático de contexto
- Olvido inteligente
- Perfil del usuario persistente

[Acciones]
- Acciones compuestas (multi-step)
- Ejecución condicional (if / else)
- Integración con sistema (archivos, comandos)
- Plugins externos

[Inteligencia]
- Mejor detección de intención
- Planificación de tareas
- Razonamiento multi-paso
- Reducción de alucinaciones

[Personalidad]
- Personalidad adaptativa
- Modos de interacción (técnico, casual, minimalista)
- Ajuste dinámico de tono

[Interfaz]
- UI básica (web o desktop)
- Integración con voz
- Visualización de memoria

[Arquitectura]
- Sistema de eventos
- Logging estructurado
- Configuración dinámica
- Testing del sistema

========================

A.U.R.A Runtime - Guía de instalación (Ollama y dependencias)

========================
1. Instalar Ollama
========================

Descargar desde:
https://ollama.com/download

O en terminal (Linux/macOS):

curl -fsSL https://ollama.com/install.sh | sh


========================
2. Iniciar Ollama
========================

ollama serve

Esto levanta el servidor en:
http://localhost:11434


========================
3. Descargar modelo
========================

ollama pull llama3


========================
4. Probar modelo (opcional)
========================

ollama run llama3


========================
5. Instalar dependencias
========================

pip install -r requirements.txt

Contenido de requirements.txt:

requests
ddgs


========================
6. Ejecutar A.U.R.A.
========================

python main.py


========================
Notas importantes
========================

- Asegúrate de que Ollama esté corriendo antes de iniciar A.U.R.A.
- Si A.U.R.A. no responde, verifica:
  - Ollama activo (ollama serve)
  - Modelo descargado (llama3)
  - Dependencias instaladas
