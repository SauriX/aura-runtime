import json
import re


def fallback(raw):
    limpio = limpiar_basura(raw)
    return {
        "accion": "responder",
        "contenido": limpio
    }


FRASES_BASURA = [
    "Como siempre, mi objetivo es facilitar el diálogo",
    "mi objetivo es facilitar el diálogo y la reflexión",
    "para que puedas explorar tus pensamientos y sentimientos",
    "me alegra saber que han pasado cosas interesantes en tu vida",
    "¿Qué deseo expresar o explorar hoy?",
]

def limpiar_basura(texto):
    # 🔥 cortar coletillas genéricas
    for frase in FRASES_BASURA:
        idx = texto.find(frase)
        if idx != -1:
            texto = texto[:idx].strip().rstrip(".,; ")

    # 🔥 quitar líneas donde AURA se presenta sola sin que se lo pidan
    lineas = texto.split("\n")
    limpias = []
    for l in lineas:
        if "A.U.R.A." in l and "Soy" in l:
            continue
        limpias.append(l)

    return "\n".join(limpias).strip()

def parsear_respuesta(raw):
    raw = raw.strip()

    # 🔥 intentar JSON directo
    try:
        data = json.loads(raw)
    except:
        # 🔥 buscar JSON dentro del texto
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

    # 🔥 doble JSON
    if isinstance(contenido, str):
        texto = contenido.strip()
        if texto.startswith("{") and "accion" in texto:
            try:
                return json.loads(texto)
            except:
                pass

    # 🔥 fallback final
    if not contenido:
        return fallback(raw)

    data["contenido"] = contenido
    return data