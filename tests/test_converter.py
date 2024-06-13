from autoscriptest.converter import convert_line_message_to_google_chat
from autoscriptest.models import LineMessage, GoogleChatMessage

def test_converter():
    """Tests the converter function"""
    line_message = LineMessage(text="Hello\nWorld!")
    google_chat_message = convert_line_message_to_google_chat(line_message)
    assert google_chat_message.text == "Hello<br>World!"