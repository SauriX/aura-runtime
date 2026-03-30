def detectar_modo(user_input, memory):
    texto = user_input.lower().strip()

    if texto in ["otro", "otra", "mas", "más", "dale", "sigue"]:
        if memory.get("history"):
            ultimos = [h["user"].lower() for h in memory["history"][-3:]]
            if any("chiste" in u for u in ultimos):
                return "chiste"

    if "chiste" in texto:
        return "chiste"

    return "normal"


def aplicar_personalidad(respuesta, modo):
    # La personalidad ya viene definida desde el prompt del modelo.
    # Este paso no altera nada para no pisar el tono británico.
    return respuesta