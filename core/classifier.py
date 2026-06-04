import ollama
import json


CLASSIFIER_PROMPT = """
You are an intent classifier.

The classification MUST be exactly one of:

COMMAND
PERSONAL_INFO
GENERAL_INFO
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

Examples:

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