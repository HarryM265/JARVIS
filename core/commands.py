def handle_command(text):

    text = text.lower()

    if text == "jarvis status":

        return (
            True,
            "All systems operational, sir."
        )

    return (
        False,
        None
    )