from typing import Dict, Any, Optional

def detectar_modo(user_input: str, memory: Dict[str, Any]) -> str:
    """
    Detecta el modo de respuesta basado en la entrada del usuario y el historial.

    Args:
        user_input: La entrada del usuario.
        memory: El diccionario de memoria del sistema.

    Returns:
        El modo detectado: "chiste" o "normal".
    """
    texto = user_input.lower().strip()

    if texto in ["otro", "otra", "mas", "más", "dale", "sigue"]:
        if memory.get("history"):
            ultimos = [h["user"].lower() for h in memory["history"][-3:]]
            if any("chiste" in u for u in ultimos):
                return "chiste"

    if "chiste" in texto:
        return "chiste"

    return "normal"


def aplicar_personalidad(respuesta: str, modo: str, memory: Optional[Dict[str, Any]] = None) -> str:
    """
    Aplica ajustes de personalidad a la respuesta basada en el estado de ánimo, energía y modo.

    Args:
        respuesta: La respuesta original a modificar.
        modo: El modo de respuesta ("chiste", "normal", etc.).
        memory: El diccionario de memoria (opcional).

    Returns:
        La respuesta modificada con personalidad aplicada.
    """
    if not isinstance(respuesta, str):
        return respuesta

    state = memory.get("state", {}) if memory else {}

    mood = state.get("mood", "neutral")
    energy = state.get("energy", 0.7)

    texto = respuesta.strip()

    # ---------------- LONGITUD (CLAVE) ----------------
    # energía baja → cortar respuesta
    if energy < 0.4:
        texto = texto[:120]
    # ---------------- FILTRO DE ARROGANCIA ----------------
    frases_problematicas = [
        "no es necesario",
        "no hace falta",
        "no es relevante"
    ]

    for f in frases_problematicas:
        if f in texto.lower():
            texto = texto.replace(texto, "Continúa. Te escucho.")

    # ---------------- MOOD ----------------
    if mood == "tenso":
        # menos sarcasmo, más directo
        texto = texto.replace("Fascinante", "")
        texto = texto.replace("Curioso", "")
        texto = texto.strip()

    elif mood == "positivo":
        # ligero refuerzo positivo
        if not texto.endswith("🙂"):
            texto += ""

    # ---------------- MODO CHISTE ----------------
    if modo == "chiste":
        return texto  # no tocar humor

    return texto.strip()