from core.memory import load_memory, save_memory, guardar_hecho
from core.model import preguntar_modelo
from core.parser import parsear_respuesta
from core.context import construir_contexto

from brain.identity import responder_identidad
from brain.intent import forzar_busqueda
from brain.style import ajustar_estilo

from tools.web import buscar_web
from tools.system import abrir_app, es_comando_abrir

from utils.clean import limpiar_respuesta
from utils.normalize import normalizar_contenido


def agregar_historial(memory, user, aura):
    if aura and len(aura) > 3:
        memory["history"].append({
            "user": user,
            "aura": aura
        })
        memory["history"] = memory["history"][-6:]


def main():
    print("A.U.R.A.: Inicializada.")

    while True:
        user_input = input("Tú: ").strip()

        if user_input.lower() == "salir":
            break

        memory = load_memory()

        # ---------------- PRIORIDAD DE DECISIONES ----------------

        # 1. IDENTIDAD
        identidad = responder_identidad(user_input, memory)
        print("DEBUG identidad:", identidad)
        if identidad:
            print("A.U.R.A.:", identidad)
            continue

        # 2. COMANDOS DEL SISTEMA
        if es_comando_abrir(user_input):
            print("A.U.R.A.: Ejecutando...")

            apps = user_input.lower()
            apps = apps.replace("abre", "").replace("abrir", "").replace("ejecuta", "").replace("inicia", "")
            apps = apps.strip().split("y")

            ejecutadas = []

            for app in apps:
                app = app.strip()
                if app:
                    if abrir_app(app):
                        ejecutadas.append(app)

            memory["ultima_accion"] = ", ".join(ejecutadas)
            save_memory(memory)

            print("A.U.R.A.: Listo.")
            continue

        # 3. BÚSQUEDA
        if forzar_busqueda(user_input):
            print("A.U.R.A.: Buscando...")

            resultados = buscar_web(user_input)
            resumen = str(resultados)

            contexto = construir_contexto(memory,user_input)

            raw = preguntar_modelo(
                    f"Información:\n{resumen}\n\nPregunta: {user_input}",
                    contexto
                )

            decision = parsear_respuesta(raw)
            contenido = decision.get("contenido")

        else:
            # 4. MODELO NORMAL
            contexto = construir_contexto(memory,user_input)

            raw = preguntar_modelo(user_input, contexto)
            print("RAW:\n", raw)
            decision = parsear_respuesta(raw)
            contenido = decision.get("contenido")

        # ---------------- POST-PROCESADO ----------------

        contenido = normalizar_contenido(contenido)
        respuesta = limpiar_respuesta(contenido)
        respuesta = ajustar_estilo(user_input, respuesta)

        print("A.U.R.A.:", respuesta)

        # ---------------- MEMORIA ----------------

        agregar_historial(memory, user_input, respuesta)
        memory = guardar_hecho(memory, user_input)

        memory["ultimo"] = user_input
        save_memory(memory)


if __name__ == "__main__":
    main()