import pytest
from unittest.mock import patch
from core.executor import ejecutar_comando

@patch('core.executor.abrir_app')
@patch('core.executor.es_comando_abrir')
def test_ejecutar_comando_no_comando(mock_es, mock_abrir):
    mock_es.return_value = False
    memory = {}
    result, mem = ejecutar_comando("Hola", memory)
    assert result == False

@patch('core.executor.abrir_app')
@patch('core.executor.es_comando_abrir')
def test_ejecutar_comando_abrir_app(mock_es, mock_abrir):
    mock_es.return_value = True
    mock_abrir.return_value = True
    memory = {}
    result, mem = ejecutar_comando("abre chrome", memory)
    assert result == True
    assert mem["ultima_accion"] == "chrome"
    mock_abrir.assert_called_with("chrome")

@patch('core.executor.abrir_app')
@patch('core.executor.es_comando_abrir')
def test_ejecutar_comando_multiples_apps(mock_es, mock_abrir):
    mock_es.return_value = True
    mock_abrir.return_value = True
    memory = {}
    result, mem = ejecutar_comando("abre chrome y spotify", memory)
    assert result == True
    assert len(mem["ultima_accion"].split(", ")) == 2