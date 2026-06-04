from core.commands import handle_command
from core.brain import ask_jarvis
from core.classifier import classify_input
from core.memory_extractor import extract_memory
from core.memory_enricher import enrich_memory
from core.memory import save_memory

from config.settings import DEBUG


def route(user_input):

    is_command, response = handle_command(
        user_input
    )

    if is_command:
        return response

    result = classify_input(
        user_input
    )

    classification = (
        result["classification"]
    )

    confidence = (
        result["confidence"]
    )

    if DEBUG:

        print(
            f"[{classification}] ({confidence}%)"
        )

        if confidence < 60:

            print(
                "[LOW CONFIDENCE]"
            )
    if classification == "PERSONAL_INFO":

        memory = extract_memory(
            user_input
        )

        if DEBUG:

            print(
                f"[MEMORY] {memory}"
            )

        category = memory.get(
            "category",
            "none"
        )

        memory_text = memory.get(
            "memory",
            ""
        )

        if category != "none":

            memory_text = enrich_memory(
                memory_text
            )

            saved = save_memory(
                category,
                memory_text
            )

            if DEBUG:

                print(
                    f"[MEMORY SAVED] {saved}"
                )

            return (
                "I'll remember that, sir."
            )

        return (
            "Understood, sir."
        )

    if classification == "MATH_QUESTION":

        if DEBUG:

            print(
                "[ENGINEERING MODE]"
            )

        return ask_jarvis(
            user_input,
            engineering_mode=True
        )

    if classification == "DIFFICULT_QUESTION":

        return (
            "Sir, this appears to be a complex question. "
            "Would you like me to use advanced reasoning mode? "
            "(This may take longer.)"
        )

    return ask_jarvis(
        user_input
    )