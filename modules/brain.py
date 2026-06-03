from modules.memory import (
    add_memory,
    get_memories
)

def ask_jarvis(user_input):

    text = user_input.lower()

    if "remember that" in text:

        memory = user_input.replace(
            "remember that",
            ""
        ).strip()

        add_memory(
            "personal",
            memory
        )

        return "Certainly sir. I've stored that information."

    if "what do you remember" in text:

        memories = get_memories(
            "personal"
        )

        if not memories:
            return "I currently have no memories stored."

        return "\n".join(memories)

    return (
        "My primary language model "
        "is still downloading, sir."
    )