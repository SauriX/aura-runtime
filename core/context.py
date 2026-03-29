from core.memory import load_memory, save_memory
from core.model import preguntar_modelo
from core.parser import parsear_respuesta
from core.context import construir_contexto

from brain.identity import responder_identidad
from brain.intent import forzar_busqueda
from brain.style import ajustar_estilo

from tools.web import buscar_web
from tools.system import abrir_app, es_comando_abrir, detectar_apps

from utils.clean import limpiar_respuesta
from utils.normalize import normalizar_contenido


# ---------------- HISTORIAL ----------------

def agregar_historial(memory, user, aura):
    if aura and len(aura) > 3:
        memory["history"].append({
            "user": user,
            "aura": aura
        })
        memory["history"] = memory["history"][-6:]


# ---------------- MAIN ----------------

def main():
    print("A.U.R.A.: Inicializada.")

    while True:
        user_input = input("Tú: ").strip()

        if user_input.lower() == "salir":
            break

        memory = load_memory()

        # ---------------- PRIORIDAD ----------------

        # 1. IDENTIDAD
        identidad = responder_identidad(user_input, memory)
        if identidad:
            print("A.U.R.A.:", identidad)
            continue

        # 2. COMANDOS DIRECTOS (fallback rápido)
        if es_comando_abrir(user_input):
            print("A.U.R.A.: Ejecutando...")

            apps = detectar_apps(user_input)
            ejecutadas = []

            for app in apps:
                if abrir_app(app):
                    ejecutadas.append(app)

            memory["ultima_accion"] = ", ".join(ejecutadas)
            save_memory(memory)

            if ejecutadas:
                print(f"A.U.R.A.: Abrí {', '.join(ejecutadas)}.")
            else:
                print("A.U.R.A.: No pude ejecutar la solicitud.")

            continue

        # ---------------- CONTEXTO ----------------

        contexto = construir_contexto(memory)

        # ---------------- MODELO ----------------

        raw = preguntar_modelo(
            f"Pregunta actual: {user_input}",
            contexto
        )

        decision = parsear_respuesta(raw)

        accion = decision.get("accion")
        contenido = decision.get("contenido")

        # ---------------- ACCIONES DEL MODELO ----------------

        if accion == "abrir":
            print("A.U.R.A.: Ejecutando...")

            apps = [a.strip() for a in contenido.split(",")]
            ejecutadas = []

            for app in apps:
                if abrir_app(app):
                    ejecutadas.append(app)

            memory["ultima_accion"] = ", ".join(ejecutadas)
            save_memory(memory)

            if ejecutadas:
                print(f"A.U.R.A.: Abrí {', '.join(ejecutadas)}.")
            else:
                print("A.U.R.A.: No pude ejecutar la solicitud.")

            continue

        elif accion == "buscar":
            print("A.U.R.A.: Buscando...")

            resultados = buscar_web(contenido)
            resumen = str(resultados)

            raw = preguntar_modelo(
                f"Información:\n{resumen}\n\nPregunta actual: {user_input}",
                contexto
            )

            decision = parsear_respuesta(raw)
            contenido = decision.get("contenido")

        # ---------------- POST-PROCESADO ----------------

        contenido = normalizar_contenido(contenido)
        respuesta = limpiar_respuesta(contenido)
        respuesta = ajustar_estilo(user_input, respuesta)

        print("A.U.R.A.:", respuesta)

        # ---------------- MEMORIA ----------------

        agregar_historial(memory, user_input, respuesta)
        memory["ultimo"] = user_input
        save_memory(memory)


if __name__ == "__main__":
    main()