import pytest
from unittest.mock import patch, MagicMock
from tools.web import buscar_web

@patch('tools.web.DDGS')
def test_buscar_web(mock_ddgs):
    mock_instance = MagicMock()
    mock_instance.text.return_value = [{"title": "Result 1", "body": "Content 1"}]
    mock_ddgs.return_value.__enter__.return_value = mock_instance
    
    result = buscar_web("test query")
    assert len(result) == 1
    assert result[0]["title"] == "Result 1"