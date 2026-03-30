import json

MEMORY_FILE = "memory.json"


# ---------------- NORMALIZACIÓN ----------------

def normalizar(texto):
    return (
        texto.lower()
        .replace("el ", "")
        .replace("la ", "")
        .replace("los ", "")
        .replace("las ", "")
        .strip()
    )


# ---------------- LOAD / SAVE ----------------

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)

            if "history" not in data:
                data["history"] = []

            if "profile" not in data:
                data["profile"] = {
                    "nombre": "A.U.R.A.",
                    "significado": "Adaptive Unit for Relational Awareness",
                    "descripcion_corta": "Estoy aquí contigo.",
                    "descripcion_larga": "Soy A.U.R.A., diseñada para asistirte con claridad y precisión."
                }

            if "facts" not in data:
                data["facts"] = []

            if "context" not in data:
                data["context"] = {}

            return data

    except:
        return {
            "history": [],
            "profile": {},
            "facts": [],
            "context": {}
        }


def save_memory(mem):
    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f, indent=2)


# ---------------- INTELIGENCIA ----------------

def evaluar_importancia(texto):
    texto = texto.lower()

    # 🔥 filtrar preguntas y operaciones primero
    indicadores_pregunta = [
        "cuanto", "cuánto", "cómo", "como", "qué", "que", "por qué",
        "cuando", "cuándo", "dónde", "donde", "quién", "quien",
        "si tengo", "si hay", "cuántos", "cuantos"
    ]
    if any(p in texto for p in indicadores_pregunta):
        return 0.1

    # 🔥 filtrar operaciones matemáticas o absurdos
    if any(op in texto for op in ["=pez", "=sapo", "+", "-", "*", "/"]):
        return 0.1

    if "me gusta" in texto or "me encanta" in texto:
        return 0.9

    if "estoy haciendo" in texto or "estoy trabajando en" in texto:
        return 0.85

    if texto.startswith("soy ") or texto.startswith("me llamo"):
        return 0.85

    if "tengo" in texto:
        return 0.5  # 🔥 bajo el umbral de guardado

    if len(texto) < 8:
        return 0.1

    return 0.3


def extraer_categoria(texto):
    texto = texto.lower()

    if "proyecto" in texto or "desarrollando" in texto:
        return "proyecto"

    if "me gusta" in texto or "me encanta" in texto:
        return "preferencia"

    if "soy " in texto or "me llamo" in texto:
        return "identidad"

    if "tengo" in texto:
        return "posesion"

    return "general"


# ---------------- APRENDIZAJE ----------------

def aprender_usuario(memory, user_input):
    texto = user_input.lower()
    profile = memory.setdefault("profile", {})

    # 🔥 gustos (SIN duplicados)
    if "me gusta" in texto or "me encanta" in texto:
        gusto = texto.replace("me encanta", "").replace("me gusta", "").strip()
        gusto_norm = normalizar(gusto)
        gustos = profile.setdefault("gustos", [])
        if not any(normalizar(g) == gusto_norm for g in gustos):
            gustos.append(gusto)

    # 🔥 eliminar gusto
    if "ya no me gusta" in texto:
        target = texto.replace("ya no me gusta", "").strip()
        target_norm = normalizar(target)
        gustos = profile.get("gustos", [])
        profile["gustos"] = [
            g for g in gustos if normalizar(g) != target_norm
        ]

    # 🔥 aversiones (nuevo)
    if "odio" in texto or "no me gusta" in texto or "detesto" in texto or "no soporto" in texto:
        aversion = (
            texto.replace("odio", "")
                 .replace("no me gusta", "")
                 .replace("detesto", "")
                 .replace("no soporto", "")
                 .strip()
        )
        aversion_norm = normalizar(aversion)
        if aversion_norm:
            aversiones = profile.setdefault("aversiones", [])
            if not any(normalizar(a) == aversion_norm for a in aversiones):
                aversiones.append(aversion)

    # 🔥 eliminar aversion
    if "ya no odio" in texto or "me empezó a gustar" in texto:
        target = texto.replace("ya no odio", "").replace("me empezó a gustar", "").strip()
        target_norm = normalizar(target)
        aversiones = profile.get("aversiones", [])
        profile["aversiones"] = [
            a for a in aversiones if normalizar(a) != target_norm
        ]

    # 🔥 proyectos
    if "estoy trabajando en" in texto or "estoy haciendo" in texto:
        proyecto = (
            texto.replace("estoy trabajando en", "")
                .replace("estoy haciendo", "")
                .strip()
        )
        profile["proyecto_actual"] = proyecto

    return memory