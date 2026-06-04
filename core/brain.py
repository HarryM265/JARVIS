import time
import ollama

from core.personality import (
    load_personality,
    load_engineering_personality
)

from core.memory import (
    get_all_memories,
    load_context,
    save_context
)


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

    # Load recent conversation history
    conversation = load_context()

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    messages.extend(conversation)

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    start = time.time()

    response = ollama.chat(
        model="qwen2.5:7b",
        messages=messages,
        options={
            "temperature": 0.3,
            "num_predict": 40
        }
    )

    elapsed = time.time() - start

    print(
        f"Response time: {elapsed:.2f}s"
    )

    response_text = response["message"]["content"]

    # Save conversation
    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    conversation.append(
        {
            "role": "assistant",
            "content": response_text
        }
    )

    # Keep only last 20 messages
    conversation = conversation[-20:]

    save_context(
        conversation
    )

    return response_text