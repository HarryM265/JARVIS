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