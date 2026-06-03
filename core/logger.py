from datetime import datetime

def log_conversation(
    user_input,
    response
):

    with open(
        "conversations/log.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"\n[{datetime.now()}]\n"
        )

        file.write(
            f"USER: {user_input}\n"
        )

        file.write(
            f"JARVIS: {response}\n"
        )