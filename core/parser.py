import json
import re

def fallback(raw):
    limpio = limpiar_basura(raw)
    return {
        "accion": "responder",
        "contenido": limpio
    }
def limpiar_basura(texto):
    lineas = texto.split("\n")
    limpias = []

    for l in lineas:
        if "A.U.R.A." in l and "Soy" in l:
            continue
        limpias.append(l)

    return "\n".join(limpias).strip()
def parsear_respuesta(raw):
    try:
        data = json.loads(raw)
    except:
        match = re.search(r'\{.*?\}', raw, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group(0))
            except:
                return fallback(raw)
        else:
            return fallback(raw)

    contenido = data.get("contenido")
# 🔥 soporte alterno
    if not contenido and "respuesta" in data:
        contenido = data["respuesta"]
    # doble JSON
    if isinstance(contenido, str):
        texto = contenido.strip()
        if texto.startswith("{") and "accion" in texto:
            try:
                return json.loads(texto)
            except:
                pass
    if not contenido:
        return fallback(raw)

    data["contenido"] = contenido            
    return data