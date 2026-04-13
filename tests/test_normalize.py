import pytest
from utils.normalize import normalizar_contenido

def test_normalizar_contenido_no_str():
    assert normalizar_contenido(123) == 123

def test_normalizar_contenido_json_valido():
    texto = '{"contenido": "Hola"}'
    result = normalizar_contenido(texto)
    assert result == "Hola"

def test_normalizar_contenido_json_roto():
    texto = 'Texto "contenido": "Hola mundo"} más'
    result = normalizar_contenido(texto)
    assert result == "Hola mundo"

def test_normalizar_contenido_sin_json():
    texto = "Texto normal"
    result = normalizar_contenido(texto)
    assert result == "Texto normal"