def load_personality():

    with open(
        "config/personality.txt",
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()