from tools.system import abrir_app, es_comando_abrir

def ejecutar_comando(user_input, memory):
    if not es_comando_abrir(user_input):
        return False, memory

    print("A.U.R.A.: Ejecutando...")

    apps = user_input.lower()
    apps = apps.replace("abre", "").replace("abrir", "").replace("ejecuta", "").replace("inicia", "")
    apps = apps.strip().split("y")

    ejecutadas = []

    for app in apps:
        app = app.strip()
        if app:
            if abrir_app(app):
                ejecutadas.append(app)

    memory["ultima_accion"] = ", ".join(ejecutadas)

    print("A.U.R.A.: Listo.")

    return True, memory