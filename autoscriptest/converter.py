from .models import LineMessage, GoogleChatMessage

def convert_line_message_to_google_chat(line_message: LineMessage) -> GoogleChatMessage:
    """Converts a Line message to a Google Chat message"""
    google_chat_text = line_message.text.replace("\n", "<br>")
    return GoogleChatMessage(text=google_chat_text)