from .converter import convert_line_message_to_google_chat
from .models import LineMessage

def main():
    """Main entry point of the script"""
    line_message = LineMessage(text="Hello\nWorld!")
    google_chat_message = convert_line_message_to_google_chat(line_message)
    print(google_chat_message.text)  # Output: Hello<br>World!

if __name__ == "__main__":
    main()