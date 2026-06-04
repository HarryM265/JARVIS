from core.classifier import classify_input

while True:

    text = input(
        "\nInput: "
    )

    result = classify_input(
        text
    )

    print(
        f"\n[{result}]"
    )