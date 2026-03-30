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


# ---------------- DECAIMIENTO ----------------

def decaer_memoria(memory):
    for fact in memory["facts"]:
        fact["peso"] *= 0.95
    return memory


# ---------------- BÚSQUEDA INTELIGENTE ----------------

def encontrar_fact(memory, texto):
    texto = normalizar(texto)

    for fact in memory["facts"]:
        dato = normalizar(fact["dato"])

        if texto in dato or dato in texto:
            return fact

    return None


# ---------------- DETECTAR CAMBIO ----------------

def detectar_cambio(memory, texto):
    texto = texto.lower()

    if "ya no me gusta" in texto:
        target = normalizar(texto.replace("ya no me gusta", "").strip())

        for fact in memory["facts"]:
            if target in normalizar(fact["dato"]):
                # 🔥 reducción fuerte
                fact["peso"] *= 0.1


# ---------------- GUARDAR HECHO ----------------

def guardar_hecho(memory, user_input, evaluar_importancia, extraer_categoria):
    texto = user_input.lower()

    # 🔥 detectar cambios primero
    detectar_cambio(memory, texto)

    importancia = evaluar_importancia(user_input)

    if importancia < 0.7:
        return memory

    existente = encontrar_fact(memory, texto)

    # 🔥 refuerzo inteligente
    if existente:
        existente["peso"] += 0.3
        existente["dato"] = user_input  # actualizar versión más reciente
        return memory

    categoria = extraer_categoria(user_input)

    nuevo = {
        "dato": user_input,
        "peso": importancia,
        "categoria": categoria
    }

    memory["facts"].append(nuevo)

    # 🔥 ordenar por importancia
    memory["facts"] = sorted(
        memory["facts"],
        key=lambda x: x["peso"],
        reverse=True
    )

    # 🔥 limpiar basura (peso bajo)
    memory["facts"] = [
        f for f in memory["facts"] if f["peso"] > 0.2
    ][:20]

    return memory