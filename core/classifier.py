import ollama
import json


CLASSIFIER_PROMPT = """
You are an intent classifier.

The classification MUST be exactly one of:

COMMAND
PERSONAL_INFO
PERSONAL_QUESTION
GENERAL_QUESTION
MATH_QUESTION
DIFFICULT_QUESTION

Do not invent new categories.

Return ONLY valid JSON:

{
    "classification": "",
    "confidence": 0
}

Confidence must be between 0 and 100.

MATH_QUESTION
=
Mathematical expressions or related mathematical questions.

Examples:
Solve y'' - 6y' + 9y = 18x
Integrate x^2 sin(x) dx
Derive the formula for the area of a circle"
What is De Moivre's theorem?
What is Hooke's Law?
Explain Kirchhoff's Laws.

COMMAND
=
User wants Jarvis to perform an action immediately.

Examples:
open chrome
shutdown computer
remember this

NOT:
I want you to remember...
design
explain
analyse
create
plan
solve

PERSONAL_QUESTION
=
Questions about the user.

Examples:

"What is my favourite colour?"
"What do I study?"
"What is my cat's name?"
"What do you know about me?"

Typical examples of questions that a user might ask:

Input:
"My favourite colour is blue"

Output:
{
    "classification":"PERSONAL_INFO",
    "confidence":95
}

Input:
"Solve y'' - 6y' + 9y = 18x"

Output:
{
    "classification":"MATH_QUESTION",
    "confidence":99
}
"""


def classify_input(user_input):

    try:

        response = ollama.chat(
            model="qwen2.5:7b",
            messages=[
                {
                    "role": "system",
                    "content": CLASSIFIER_PROMPT
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            options={
                "temperature": 0
            }
        )

        result = json.loads(
            response["message"]["content"]
        )
        classification = (
            result["classification"]
            .upper()
            .replace("-", "_")
            .replace(" ", "_")
        )

        result["classification"] = classification

        return result

    except Exception as e:

        print(
            f"[CLASSIFIER ERROR] {e}"
        )

        return {
            "classification":
                "GENERAL_QUESTION",
            "confidence":
                0
        }