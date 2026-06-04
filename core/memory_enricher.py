from datetime import datetime
from datetime import timedelta


def enrich_memory(memory):

    memory_lower = memory.lower()

    today = datetime.today()

    weekdays = {

        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6

    }

    for day_name, day_number in weekdays.items():

        phrase = f"next {day_name}"

        if phrase in memory_lower:

            days_ahead = (
                day_number -
                today.weekday()
            )

            if days_ahead <= 0:

                days_ahead += 7

            target_date = (
                today +
                timedelta(
                    days=days_ahead
                )
            )

            date_string = target_date.strftime(
                "%Y-%m-%d"
            )

            memory = memory.replace(
                phrase,
                date_string
            )

            memory = memory.replace(
                phrase.title(),
                date_string
            )

    return memory