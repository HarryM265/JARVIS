
import datetime


def get_greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "Good morning sir."

    elif hour < 18:
        return "Good afternoon sir."

    else:
        return "Good evening sir."