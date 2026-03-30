from core.memory import (
    load_memory,
    save_memory,
    evaluar_importancia,
    extraer_categoria,
    aprender_usuario
)

from core.memory_engine import guardar_hecho, decaer_memoria
from core.executor import ejecutar_comando
from core.responder import generar_respuesta
from brain.personality import detectar_modo, aplicar_personalidad
from brain.identity import responder_identidad
from brain.style import ajustar_estilo
from brain.decision import decidir

from utils.clean import limpiar_respuesta
from utils.normalize import normalizar_contenido


def agregar_historial(memory, user, aura):
    if aura and len(aura) > 3:
        if memory["history"] and memory["history"][-1]["user"].lower() == user.lower():
            return
        memory["history"].append({"user": user, "aura": aura})
        memory["history"] = memory["history"][-6:]


def main():
    print("A.U.R.A.: Inicializada.")

    while True:
        user_input = input("Tú: ").strip()

        if user_input.lower() == "salir":
            break

        memory = load_memory()

        # 🔥 memoria evolutiva
        memory = decaer_memoria(memory)

        # ---------------- IDENTIDAD ----------------
        identidad = responder_identidad(user_input, memory)
        if identidad:
            print("A.U.R.A.:", identidad)
            continue

        # ---------------- DECISIÓN ----------------
        decision = decidir(user_input, memory)

        # ---------------- ACCIONES ----------------
        if decision["tipo"] == "accion":
            ejecutado, memory = ejecutar_comando(user_input, memory)
            if ejecutado:
                save_memory(memory)
                continue

        # ---------------- RESPUESTA ----------------
        contenido = generar_respuesta(user_input, memory)

        # ---------------- POST ----------------
        contenido = normalizar_contenido(contenido)
        respuesta = limpiar_respuesta(contenido)
        respuesta = ajustar_estilo(user_input, respuesta)
        modo = detectar_modo(user_input,memory)
        respuesta = aplicar_personalidad(respuesta, modo)
        if not respuesta or len(respuesta.strip()) < 2:
            respuesta = "Continúa, te escucho."
        print("A.U.R.A.:", respuesta)

        # ---------------- MEMORIA ----------------
        agregar_historial(memory, user_input, respuesta)

        memory = aprender_usuario(memory, user_input)

        memory = guardar_hecho(
            memory,
            user_input,
            evaluar_importancia,
            extraer_categoria
        )

        memory["ultimo"] = user_input

        save_memory(memory)


if __name__ == "__main__":
    main()