def decaer_memoria(memory):
    for fact in memory["facts"]:
        fact["peso"] *= 0.95
    return memory


def encontrar_fact(memory, texto):
    texto = texto.lower()

    for fact in memory["facts"]:
        if texto in fact["dato"].lower():
            return fact

    return None


def detectar_cambio(memory, texto):
    texto = texto.lower()

    if "ya no me gusta" in texto:
        target = texto.replace("ya no me gusta", "").strip()

        for fact in memory["facts"]:
            if target in fact["dato"].lower():
                fact["peso"] *= 0.2


def guardar_hecho(memory, user_input, evaluar_importancia, extraer_categoria):
    texto = user_input.lower()

    # detectar cambios
    detectar_cambio(memory, texto)

    importancia = evaluar_importancia(user_input)

    if importancia < 0.7:
        return memory

    existente = encontrar_fact(memory, texto)

    if existente:
        existente["peso"] += 0.2
        return memory

    categoria = extraer_categoria(user_input)

    nuevo = {
        "dato": user_input,
        "peso": importancia,
        "categoria": categoria
    }

    memory["facts"].append(nuevo)

    memory["facts"] = sorted(
        memory["facts"],
        key=lambda x: x["peso"],
        reverse=True
    )[:20]

    return memory