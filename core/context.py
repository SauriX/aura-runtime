def obtener_facts_relevantes(memory, user_input):
    facts = memory.get("facts", [])
    texto_input = user_input.lower()

    relevantes = []

    # 1. match directo
    for f in facts:
        dato = f["dato"].lower()

        for palabra in texto_input.split():
            if palabra in dato:
                relevantes.append(f)
                break

    # 2. si no hay match fuerte → usar top facts (mezcla)
    if not relevantes:
        relevantes = facts[:5]

    # 🔥 3. evitar duplicados
    vistos = set()
    filtrados = []

    for f in relevantes:
        if f["dato"] not in vistos:
            filtrados.append(f)
            vistos.add(f["dato"])

    # 🔥 4. construir texto
    texto = ""
    if filtrados:
        texto = "Preferencias del usuario (usa esto para responder):\n"
        for f in filtrados[:5]:
            texto += f"- {f['dato']}\n"
        texto += "\n"

    return texto

def construir_contexto(memory,user_input):
    contexto = ""
    # 🔥 facts primero 
    facts_text = obtener_facts_relevantes(memory, user_input)
    if facts_text:
        contexto += facts_text

    history = memory.get("history", [])[-3:]

    if history:
        ultimo = history[-1]["user"]
        contexto += f"Tema actual: {ultimo}\n\n"

    for h in history:
        contexto += f"Usuario: {h['user']}\n"
        contexto += f"A.U.R.A.: {h['aura']}\n"

    return contexto