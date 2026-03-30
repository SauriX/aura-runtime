def decidir(user_input, memory):
    texto = user_input.lower()

    # ---------------- ACCIONES ----------------
    if any(p in texto for p in ["abre", "abrir", "ejecuta", "inicia"]):
        return {
            "tipo": "accion"
        }

    # ---------------- BÚSQUEDA ----------------
    if any(p in texto for p in [
        "clima", "hora", "noticias", "precio", "cuanto cuesta"
    ]):
        return {
            "tipo": "buscar"
        }

    # ---------------- DEFAULT ----------------
    return {
        "tipo": "responder"
    }