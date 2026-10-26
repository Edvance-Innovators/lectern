"""Generator tests use a fake OpenAI client - no network calls."""
from unittest.mock import patch, MagicMock
from backend import generator


@patch.object(generator, "client")
def test_generate_overlay_returns_string(mock_client):
    mock_resp = MagicMock()
    mock_resp.choices = [MagicMock()]
    mock_resp.choices[0].message.content = "# Test\n\n- point"
    mock_client.chat.completions.create.return_value = mock_resp

    out = generator.generate_overlay("some text", "university", "standard")
    assert isinstance(out, str)
    assert out.startswith("#")
