import pytest
from utils.clean import limpiar_respuesta

def test_limpiar_respuesta_vacia():
    assert limpiar_respuesta("") == ""

def test_limpiar_respuesta_basura():
    texto = "Hola, soy una inteligencia artificial. ¿Cómo estás?"
    result = limpiar_respuesta(texto)
    assert "inteligencia artificial" not in result
    assert result == "Hola, . ¿Cómo estás?"

def test_limpiar_respuesta_sin_basura():
    texto = "Hola, ¿cómo estás?"
    result = limpiar_respuesta(texto)
    assert result == texto