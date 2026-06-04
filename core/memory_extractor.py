import json
import ollama


EXTRACTOR_PROMPT = """
Extract useful long-term memory about the user.

Return ONLY valid JSON.

Format:

{
    "category": "",
    "memory": ""
}

Valid categories:

personal
education
work
projects
preferences

Examples:

Input:
"I have a fluid mechanics exam next Tuesday"

Output:
{
    "category":"education",
    "memory":"Fluid Mechanics exam next Tuesday"
}

Input:
"My favourite colour is blue"

Output:
{
    "category":"preferences",
    "memory":"Favourite colour is blue"
}

Input:
"I work as a Senior Hose Technician"

Output:
{
    "category":"work",
    "memory":"Senior Hose Technician"
}

Only extract information about the user.

Do not extract facts about the world.

"The sky is blue"
should return:

{
    "category":"none",
    "memory":""
}

If nothing should be remembered:

{
    "category":"none",
    "memory":""
}

Respond with JSON only.
"""


def extract_memory(user_input):

    try:

        response = ollama.chat(
            model="qwen2.5:7b",
            messages=[
                {
                    "role": "system",
                    "content": EXTRACTOR_PROMPT
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

        return result

    except Exception as e:

        print(
            f"[MEMORY EXTRACTOR ERROR] {e}"
        )

        return {
            "category": "none",
            "memory": ""
        }