import pytest
from unittest.mock import patch, MagicMock
from core.model import preguntar_modelo

@patch('core.model.requests.post')
def test_preguntar_modelo(mock_post):
    mock_response = MagicMock()
    mock_response.json.return_value = {"response": "Respuesta del modelo"}
    mock_post.return_value = mock_response
    
    with patch('core.model.construir_prompt', return_value="Prompt"):
        result = preguntar_modelo("Hola", {})
        assert result == "Respuesta del modelo"
        mock_post.assert_called_once()
        args = mock_post.call_args
        assert args[1]["json"]["prompt"] == "Prompt\nUsuario: Hola"