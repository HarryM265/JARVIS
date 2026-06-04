import json

MEMORY_FILE = "memory/user_memory.json"

def load_memory():
    with open(MEMORY_FILE, "r") as file:
        return json.load(file)

def save_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_memory(category, text):

    data = load_memory()

    if category not in data:
        data[category] = []

    data[category].append(text)

    save_memory(data)

def get_memories(category):

    data = load_memory()

    return data.get(category, [])

def get_all_memories():

    return load_memory()

def save_all_memories(memories):

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            memories,
            file,
            indent=4
        )


def save_memory(
    category,
    memory
):

    memories = get_all_memories()

    if category not in memories:

        memories[category] = []

    if memory not in memories[category]:

        memories[category].append(
            memory
        )

        save_all_memories(
            memories
        )

        return True

    return False

CONTEXT_FILE = "memory/conversation_context.json"

def load_context():

    try:

        with open(
            CONTEXT_FILE,
            "r"
        ) as file:

            return json.load(file)

    except:

        return []


def save_context(context):

    with open(
        CONTEXT_FILE,
        "w"
    ) as file:

        json.dump(
            context,
            file,
            indent=4
        )
