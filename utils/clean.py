import re

def limpiar_respuesta(texto):
    if not texto:
        return texto

    basura = [
        "Soy una inteligencia artificial",
        "Soy una IA",
        "Como inteligencia artificial"
    ]

    for b in basura:
        texto = re.sub(re.escape(b), '', texto, flags=re.IGNORECASE)

    return texto.strip()