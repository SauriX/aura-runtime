import pytest
from core.parser import limpiar_basura, parsear_respuesta, fallback

def test_limpiar_basura():
    texto = "Hola, me alegra saber que han pasado cosas interesantes en tu vida. ¿Qué más?"
    result = limpiar_basura(texto)
    assert "me alegra saber" not in result
    assert result == "Hola"

def test_limpiar_basura_aura():
    texto = "Respuesta\nA.U.R.A. Soy tu asistente.\nMás texto"
    result = limpiar_basura(texto)
    assert "A.U.R.A. Soy" not in result

def test_parsear_respuesta_json_valido():
    raw = '{"accion": "responder", "contenido": "Hola"}'
    result = parsear_respuesta(raw)
    assert result["accion"] == "responder"
    assert result["contenido"] == "Hola"

def test_parsear_respuesta_json_embedded():
    raw = 'Texto {"accion": "responder", "contenido": "Hola"} más texto'
    result = parsear_respuesta(raw)
    assert result["accion"] == "responder"

def test_parsear_respuesta_fallback():
    raw = "Texto sin JSON"
    result = parsear_respuesta(raw)
    assert result["accion"] == "responder"
    assert "Texto sin JSON" in result["contenido"]

def test_parsear_respuesta_doble_json():
    raw = '{"contenido": "{\\"accion\\": \\"responder\\", \\"contenido\\": \\"Hola\\"}"}'
    result = parsear_respuesta(raw)
    assert result["accion"] == "responder"

def test_fallback():
    result = fallback("Texto")
    assert result["accion"] == "responder"
    assert result["contenido"] == "Texto"