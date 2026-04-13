import pytest
from core.memory_engine import normalizar, decaer_memoria, encontrar_fact, detectar_cambio, guardar_hecho

def test_normalizar():
    assert normalizar("El café es bueno") == "café es bueno"
    assert normalizar("LA casa") == "casa"

def test_decaer_memoria():
    memory = {"facts": [{"peso": 1.0}, {"peso": 0.8}]}
    result = decaer_memoria(memory)
    assert result["facts"][0]["peso"] == 0.95
    assert result["facts"][1]["peso"] == 0.76

def test_encontrar_fact():
    memory = {"facts": [{"dato": "Me gusta el café", "peso": 0.9}]}
    fact = encontrar_fact(memory, "café")
    assert fact is not None
    assert fact["dato"] == "Me gusta el café"

def test_detectar_cambio():
    memory = {"facts": [{"dato": "Me gusta el café", "peso": 1.0}]}
    detectar_cambio(memory, "ya no me gusta el café")
    assert memory["facts"][0]["peso"] == 0.1

def test_guardar_hecho():
    def mock_eval(text): return 0.9
    def mock_cat(text): return "gustos"
    
    memory = {"facts": []}
    result = guardar_hecho(memory, "Me gusta el chocolate", mock_eval, mock_cat)
    assert len(result["facts"]) == 1
    assert result["facts"][0]["dato"] == "Me gusta el chocolate"