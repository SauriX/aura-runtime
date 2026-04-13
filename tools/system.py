import subprocess
import shlex

# Lista blanca de aplicaciones permitidas (nombres comunes)
ALLOWED_APPS = {
    "chrome", "firefox", "edge", "notepad", "calc", "explorer", "cmd", "powershell",
    "word", "excel", "powerpoint", "outlook", "spotify", "vlc", "discord", "steam",
    "vscode", "code", "sublime", "atom", "pycharm", "webstorm"
}

def abrir_app(app):
    # Sanitizar entrada básica
    app = app.strip().lower()
    if not app or len(app) > 50:  # Límite de longitud
        return False
    
    # Verificar si es una app permitida (o contiene una)
    if not any(allowed in app for allowed in ALLOWED_APPS):
        print(f"A.U.R.A.: Aplicación '{app}' no permitida por seguridad.")
        return False
    
    try:
        # Usar shell=False para mayor seguridad, pasar como lista
        subprocess.Popen([app], shell=False)
        return True
    except FileNotFoundError:
        # Si falla, intentar con shell=True pero sanitizado
        try:
            safe_app = shlex.quote(app)  # Para Unix-like, pero ayuda
            subprocess.Popen(safe_app, shell=True)
            return True
        except Exception as e:
            print(f"A.U.R.A.: Error al abrir '{app}': {e}")
            return False
    except Exception as e:
        print(f"A.U.R.A.: Error al abrir '{app}': {e}")
        return False


def es_comando_abrir(prompt):
    palabras = ["abre", "abrir", "ejecuta", "inicia"]
    return any(p in prompt.lower() for p in palabras)