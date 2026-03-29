import json

MEMORY_FILE = "memory.json"

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
            return data
    except:
        return {"history": [], "profile": {}}

def save_memory(mem):
    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f, indent=2)