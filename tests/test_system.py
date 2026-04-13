import pytest
from unittest.mock import patch
from tools.system import abrir_app, es_comando_abrir

@patch('tools.system.subprocess.Popen')
def test_abrir_app_permitida(mock_popen):
    mock_popen.return_value = None
    result = abrir_app("chrome")
    assert result == True
    mock_popen.assert_called_with(["chrome"], shell=False)

@patch('tools.system.subprocess.Popen')
def test_abrir_app_no_permitida(mock_popen):
    result = abrir_app("badapp")
    assert result == False
    mock_popen.assert_not_called()

def test_es_comando_abrir():
    assert es_comando_abrir("abre chrome") == True
    assert es_comando_abrir("Hola") == False