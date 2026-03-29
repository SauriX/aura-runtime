import json

MEMORY_FILE = "memory.json"


def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)

            # estructura base
            if "history" not in data:
                data["history"] = []

            if "profile" not in data:
                data["profile"] = {
                    "nombre": "A.U.R.A.",
                    "significado": "Adaptive Unit for Relational Awareness",
                    "descripcion_corta": "Estoy aquí contigo.",
                    "descripcion_larga": "Soy A.U.R.A., diseñada para asistirte con claridad y precisión."
                }

            if "facts" not in data:
                data["facts"] = []

            if "context" not in data:
                data["context"] = {}

            return data

    except:
        return {
            "history": [],
            "profile": {},
            "facts": [],
            "context": {}
        }


def save_memory(mem):
    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f, indent=2)


# ---------------- INTELIGENCIA ----------------

def evaluar_importancia(texto):
    texto = texto.lower()

    # patrones fuertes
    if "me gusta" in texto or "me encanta" in texto:
        return 0.9

    if "estoy haciendo" in texto or "estoy trabajando en" in texto:
        return 0.85

    if "soy" in texto or "tengo" in texto:
        return 0.8

    # ruido
    if len(texto) < 8:
        return 0.1

    return 0.3


def extraer_categoria(texto):
    texto = texto.lower()

    if "proyecto" in texto or "desarrollando" in texto:
        return "proyecto"

    if "me gusta" in texto:
        return "preferencia"

    if "soy" in texto:
        return "identidad"

    return "general"


def guardar_hecho(memory, user_input):
    importancia = evaluar_importancia(user_input)

    if importancia < 0.7:
        return memory

    categoria = extraer_categoria(user_input)

    nuevo = {
        "dato": user_input,
        "peso": importancia,
        "categoria": categoria
    }

    memory["facts"].append(nuevo)

    # limitar tamaño
    memory["facts"] = sorted(
        memory["facts"],
        key=lambda x: x["peso"],
        reverse=True
    )[:20]
    return memory

def aprender_usuario(memory, user_input):
    texto = user_input.lower()

    # gustos
    if "me gusta" in texto:
        gusto = texto.replace("me gusta", "").strip()
        memory["profile"].setdefault("gustos", []).append(gusto)

    # proyectos
    if "estoy trabajando en" in texto or "estoy haciendo" in texto:
        proyecto = texto.replace("estoy trabajando en", "").replace("estoy haciendo", "").strip()
        memory["profile"]["proyecto_actual"] = proyecto

    return memory