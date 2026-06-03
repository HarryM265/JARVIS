def load_personality():

    with open(
        "config/personality.txt",
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def load_engineering_personality():

    with open(
        "config/engineering_personality.txt",
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()