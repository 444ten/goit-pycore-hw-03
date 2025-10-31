from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        wish_day = birthday.replace(year=today.year)

        if wish_day < today:
            wish_day = wish_day.replace(year=today.year + 1)

        delta = (wish_day - today).days

        if 0 <= delta <= 7:
            if   wish_day.weekday() == 5:
                wish_day += timedelta(days=2)
            elif wish_day.weekday() == 6:
                wish_day += timedelta(days=1)
            
            result.append({
                "name": user["name"],
                "congratulation_date": wish_day.strftime("%Y.%m.%d")
            })

    return result


# test

# users = [
#     {"name": "John Doe", "birthday": "1985.11.1"},
#     {"name": "Jane Smith", "birthday": "1990.10.31"},
#     {"name": "Alice", "birthday": "2000.01.26"},
# ]

# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:")
# for entry in upcoming_birthdays:
#     print(f"{entry['name']}: {entry['congratulation_date']}")
