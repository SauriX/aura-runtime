import json
import re

def normalizar_contenido(contenido):
    if not isinstance(contenido, str):
        return contenido

    texto = contenido.strip()

    # JSON válido
    if texto.startswith("{") and "contenido" in texto:
        try:
            data = json.loads(texto)
            return data.get("contenido", texto)
        except:
            pass

    # JSON roto
    match = re.search(r'"contenido"\s*:\s*"(.+)', texto)
    if match:
        posible = match.group(1)
        posible = posible.split('"}')[0]
        return posible.strip()

    return texto