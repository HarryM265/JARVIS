from core.memory_extractor import (
    extract_memory
)

while True:

    text = input(
        "\nInput: "
    )

    result = extract_memory(
        text
    )

    print(
        f"\n{result}"
    )