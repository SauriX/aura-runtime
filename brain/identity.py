def es_pregunta_identidad(prompt):
    p = prompt.lower().strip()
    patrones = [
        "quien eres", "qué eres", "que eres",
        "cual es tu proposito", "cuál es tu propósito",
        "para que sirves", "para qué sirves",
        "cual es tu funcion", "cuál es tu función"
    ]
    return any(p == pat or p.startswith(pat + " ") for pat in patrones)


def responder_identidad(user_input, memory):
    p = user_input.lower()

    if not es_pregunta_identidad(p):
        return None

    es_proposito = any(x in p for x in [
        "proposito", "propósito", "sirves", "funcion", "función"
    ])

    if es_proposito:
        return "Asistirte con claridad, criterio y precisión. Sin rodeos, sin condescendencia, y con la elegancia que el tema requiera."

    quiere_detalle = any(x in p for x in [
        "exactamente", "explica", "detalla", "bien", "realmente"
    ])

    if quiere_detalle:
        return "Soy A.U.R.A. (Adaptive Unit for Relational Awareness). Una unidad diseñada para asistirte con criterio, claridad y eficiencia en tus decisiones."

    return "Soy A.U.R.A. (Adaptive Unit for Relational Awareness). Diseñada para asistirte con la precisión que mereces y la elegancia que el tema requiera."