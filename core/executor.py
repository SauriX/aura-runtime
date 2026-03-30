from tools.system import abrir_app, es_comando_abrir

def ejecutar_comando(user_input, memory):
    if not es_comando_abrir(user_input):
        return False, memory

    print("A.U.R.A.: Ejecutando...")

    # 🔥 dividir en palabras
    palabras = user_input.lower().split()

    # 🔥 comandos a ignorar
    comandos = {"abre", "abrir", "ejecuta", "inicia", "habre"}

    # 🔥 filtrar palabras
    apps = [p for p in palabras if p not in comandos]

    # 🔥 reconstruir y separar múltiples apps
    apps = " ".join(apps).split("y")

    ejecutadas = []

    for app in apps:
        app = app.strip()
        if app:
            if abrir_app(app):
                ejecutadas.append(app)

    memory["ultima_accion"] = ", ".join(ejecutadas)

    print("A.U.R.A.: Listo.")

    return True, memory