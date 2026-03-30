from core.model import preguntar_modelo
from core.parser import parsear_respuesta
from core.context import construir_contexto

from brain.intent import forzar_busqueda
from tools.web import buscar_web


def generar_respuesta(user_input, memory):
    if forzar_busqueda(user_input):
        print("A.U.R.A.: Buscando...")

        resultados = buscar_web(user_input)
        resumen = str(resultados)

        contexto = construir_contexto(memory, user_input)

        raw = preguntar_modelo(
            f"Información:\n{resumen}\n\nPregunta: {user_input}",
            contexto
        )
    else:
        contexto = construir_contexto(memory, user_input)

        raw = preguntar_modelo(user_input, contexto)
        """ print("RAW:\n", raw) """

    decision = parsear_respuesta(raw)
    contenido = decision.get("contenido")

    return contenido