import time
import ollama

from core.personality import (
    load_personality,
    load_engineering_personality
)
from core.memory import get_all_memories


def ask_jarvis(
    user_input,
    engineering_mode=False
):

    if engineering_mode:
        personality = load_engineering_personality()
    else:
        personality = load_personality()

    memories = get_all_memories()

    memory_text = ""

    for category, items in memories.items():

        if not items:
            continue

        memory_text += f"\n{category.upper()}:\n"

        for item in items:
            memory_text += f"- {item}\n"

    system_prompt = f"""
{personality}

Known information about the user:

{memory_text}

Rules:
- Default to one sentence answers.
- Maximum three sentences unless asked for detail.
- Be direct and concise.
- Do not explain your reasoning.
- Do not repeat information unnecessarily.
"""

    start = time.time()

    response = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        options={
            "temperature": 0.3,
            "num_predict": 40
        },
        think = False
    )

    elapsed = time.time() - start

    print(
        f"Response time: {elapsed:.2f}s"
    )

    return response["message"]["content"]