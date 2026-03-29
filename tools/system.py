import subprocess

def abrir_app(app):
    try:
        subprocess.Popen(app, shell=True)
        return True
    except Exception as e:
        print("Error:", e)
        return False


def es_comando_abrir(prompt):
    palabras = ["abre", "abrir", "ejecuta", "inicia"]
    return any(p in prompt.lower() for p in palabras)