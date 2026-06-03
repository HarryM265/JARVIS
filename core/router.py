from core.commands import handle_command
from core.brain import ask_jarvis

def route(user_input):

    is_command, response = handle_command(
        user_input
    )

    if is_command:
        return response

    return ask_jarvis(user_input)