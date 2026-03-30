import requests
from core.prompt import construir_prompt


def preguntar_modelo(user_input, contexto):

    prompt = construir_prompt(contexto) + f"\nUsuario: {user_input}"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False,
        },
    )
    print("=== PROMPT ENVIADO ===")
    print(prompt)
    print("=== FIN PROMPT ===")
    
    return response.json()["response"]