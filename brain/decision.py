def decidir(user_input, memory):
    texto = user_input.lower()
    state = memory.get("state", {})
    energy = state.get("energy", 0.7)
    mood = state.get("mood", "neutral")
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
        "tipo": "responder",
        "modo": "breve" if energy < 0.3 else "normal"
    }