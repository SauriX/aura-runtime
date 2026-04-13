import pytest
from brain.personality import detectar_modo, aplicar_personalidad

def test_detectar_modo_normal():
    memory = {"history": []}
    assert detectar_modo("Hola", memory) == "normal"

def test_detectar_modo_chiste():
    memory = {"history": []}
    assert detectar_modo("Cuéntame un chiste", memory) == "chiste"

def test_detectar_modo_otro_con_historial():
    memory = {"history": [{"user": "chiste"}]}
    assert detectar_modo("otro", memory) == "chiste"

def test_aplicar_personalidad_normal():
    memory = {"state": {"mood": "neutral", "energy": 0.7}}
    result = aplicar_personalidad("Hola mundo", "normal", memory)
    assert isinstance(result, str)

def test_aplicar_personalidad_energia_baja():
    memory = {"state": {"mood": "neutral", "energy": 0.3}}
    result = aplicar_personalidad("Esta es una respuesta muy larga que debería cortarse", "normal", memory)
    assert len(result) <= 120

def test_aplicar_personalidad_mood_tenso():
    memory = {"state": {"mood": "tenso", "energy": 0.7}}
    result = aplicar_personalidad("Fascinante idea", "normal", memory)
    assert "Fascinante" not in result