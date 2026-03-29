import re

def ajustar_estilo(user_input, respuesta):
    if not isinstance(respuesta, str):
        return respuesta

    texto = respuesta.strip()
    user = user_input.lower()

    # quitar prefijos innecesarios
    texto = re.sub(
        r'^A\.U\.R\.A\.\s*(Ah, Señor\.|Sí, Señor\.|Entendido, Señor\.|Claro, Señor\.)\s*',
        '',
        texto
    )

    # evitar doble AURA
    texto = re.sub(r'A\.U\.R\.A\.\s*A\.U\.R\.A\.', 'A.U.R.A.', texto)

    return texto.strip()