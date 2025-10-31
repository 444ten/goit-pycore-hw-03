from datetime import datetime

def get_days_from_today(date) -> int:
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()

        return (today - target_date).days
    except ValueError:
        return "Invalid date format. Use 'YYYY-MM-DD'."


# test

# d1 = '2024-10-31'
# print(get_days_from_today(d1))
# d2 = '2026-10-31'
# print(get_days_from_today(d2))
# d3 = '2024-10.31'
# print(get_days_from_today(d3))
