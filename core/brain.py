import ollama

from core.personality import load_personality
from core.memory import get_all_memories


def ask_jarvis(user_input):

    personality = load_personality()

    memories = get_all_memories()

    memory_text = ""

    for category, items in memories.items():

        memory_text += f"\n{category.upper()}:\n"

        for item in items:
            memory_text += f"- {item}\n"

    system_prompt = f"""
{personality}

Known information about the user:

{memory_text}

Use this information when relevant.

Keep responses concise.
"""

    response = ollama.chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return response["message"]["content"]