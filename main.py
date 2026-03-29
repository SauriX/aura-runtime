from core.memory import load_memory, save_memory
from brain.identity import responder_identidad
from brain.intent import forzar_busqueda
from tools.web import buscar_web
from core.model import preguntar_modelo

while True:
    user_input = input("Tú: ")
    memory = load_memory()

    # identidad
    identidad = responder_identidad(user_input, memory)
    if identidad:
        print("A.U.R.A.:", identidad)
        continue

    # búsqueda
    if forzar_busqueda(user_input):
        print("A.U.R.A.: Buscando...")
        print(buscar_web(user_input))
        continue

    # modelo
    respuesta = preguntar_modelo(user_input)
    print("A.U.R.A.:", respuesta)