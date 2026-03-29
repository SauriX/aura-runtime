import json
import re

def fallback(raw):
    return {
        "accion": "responder",
        "contenido": raw.strip()
    }

def parsear_respuesta(raw):
    try:
        data = json.loads(raw)
    except:
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group(0))
            except:
                return fallback(raw)
        else:
            return fallback(raw)

    contenido = data.get("contenido")

    # doble JSON
    if isinstance(contenido, str):
        texto = contenido.strip()
        if texto.startswith("{") and "accion" in texto:
            try:
                return json.loads(texto)
            except:
                pass

    return data