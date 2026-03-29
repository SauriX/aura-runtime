def forzar_busqueda(prompt):
    p = prompt.lower()

    if "quien eres" in p:
        return False

    palabras = ["clima", "quien es", "que es"]
    return any(pal in p for pal in palabras)