import time

def cargar_estado(memory):
    if "state" not in memory:
        memory["state"] = {
            "mood": "neutral",        # neutral | positivo | tenso
            "energy": 0.7,            # 0.0 – 1.0
            "focus": "user",          # user | task | idle
            "last_interaction": time.time()
        }
    return memory


def actualizar_estado(memory, user_input, respuesta):
    state = memory.get("state", {})

    texto = user_input.lower()

    # ---------------- MOOD ----------------
    if any(p in texto for p in ["gracias", "bien", "genial"]):
        state["mood"] = "positivo"

    elif any(p in texto for p in ["mal", "odio", "cansado", "estresado"]):
        state["mood"] = "tenso"

    else:
        state["mood"] = "neutral"

    # ---------------- ENERGY ----------------
    if len(user_input) > 120:
        state["energy"] -= 0.05
    else:
        state["energy"] += 0.02

    state["energy"] = max(0.1, min(1.0, state["energy"]))

    # ---------------- TIME ----------------
    state["last_interaction"] = time.time()

    memory["state"] = state
    return memory