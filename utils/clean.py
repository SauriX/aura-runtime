def limpiar_respuesta(texto):
    if not texto:
        return texto

    basura = [
        "Soy una inteligencia artificial",
        "Soy una IA",
        "Como inteligencia artificial"
    ]

    for b in basura:
        texto = texto.replace(b, "")

    return texto.strip()