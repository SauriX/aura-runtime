def es_pregunta_identidad(prompt):
    p = prompt.lower().strip()
    patrones = ["quien eres", "qué eres", "que eres"]
    return any(p == pat or p.startswith(pat + " ") for pat in patrones)


def responder_identidad(prompt, memory):
    if not es_pregunta_identidad(prompt):
        return None

    profile = memory.get("profile", {})

    return f"{profile['nombre']}. {profile['significado']}. {profile['descripcion_corta']}"