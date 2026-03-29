def es_pregunta_identidad(prompt):
    p = prompt.lower().strip()
    patrones = ["quien eres", "qué eres", "que eres"]
    return any(p == pat or p.startswith(pat + " ") for pat in patrones)


def responder_identidad(user_input, memory):
    p = user_input.lower()

    if not es_pregunta_identidad(p):
        return None

    profile = memory.get("profile", {})

    nombre = profile.get("nombre", "A.U.R.A.")
    significado = profile.get("significado", "Adaptive Unit for Relational Awareness")

    # 🔥 detectar si quiere más detalle
    quiere_detalle = any(x in p for x in [
        "exactamente", "explica", "detalla", "bien", "realmente"
    ])

    if quiere_detalle:
        return f"Soy {nombre} ({significado}). Una unidad diseñada para asistirte con criterio, claridad y eficiencia en tus decisiones."

    # 🔥 respuesta base (LA BUENA)
    return f"Soy {nombre} ({significado}). Diseñada para ayudarte a entender, decidir y actuar con claridad."