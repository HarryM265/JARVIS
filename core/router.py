from core.commands import handle_command
from core.brain import ask_jarvis

def is_engineering_question(text):

    engineering_keywords = [

        "equation",
        "theorem",
        "integral",
        "differentiate",
        "derivative",
        "laplace",
        "matrix",
        "eigenvalue",
        "complex",
        "phasor",
        "circuit",
        "voltage",
        "current",
        "resistance",
        "stress",
        "strain",
        "moment",
        "torque",
        "fluid",
        "mechanics",
        "thermodynamics",
        "physics",
        "calculus",
        "math",
        "mathematics",
        "solve",
        "find the",
        "prove",
        "control system",
        "pid",
        "transfer function"

    ]

    text = text.lower()

    return any(
        keyword in text
        for keyword in engineering_keywords
    )

def route(user_input):

    is_command, response = handle_command(
        user_input
    )

    if is_command:
        return response

    if is_engineering_question(
        user_input
    ):

        print(
            "[ENGINEERING MODE]"
        )

        return ask_jarvis(
            user_input,
            engineering_mode=True
        )

    return ask_jarvis(
        user_input
    )