from datetime import datetime, timedelta
from collections import defaultdict


employees = [
    {"name": "Pitier", "birthdate": datetime(1990, 7, 2)},
    {"name": "Leon", "birthdate": "04.07.2000"},
    {"name": "Angel", "birthdate": datetime(1985, 7, 3)},
    {"name": "Bill", "birthdate": datetime(2023, 7, 4)},
    {"name": "Jill", "birthdate": datetime(2023, 7, 1)},
    {"name": "Kim", "birthdate": datetime(2023, 7, 6)},
    {"name": "Jan", "birthdate": datetime(2023, 7, 5)},
]


def get_period() -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    start_period = current_date + timedelta(days=5 - current_date.weekday())
    return start_period.date(), (start_period + timedelta(6)).date()


def check_epl(list_of_emp: list) -> None:
    result = defaultdict(list)
    current_year = datetime.now().year
    for employee in list_of_emp:
        bd = employee["birthdate"]
        if isinstance(bd, datetime):
            bd = bd.date()
        else:
            bd = datetime.strptime(bd, "%d.%m.%Y").date()
        bd = bd.replace(year=current_year)

        start, end = get_period()

        if start <= bd <= end:
            if bd.weekday() in (5, 6):
                result[start + timedelta(days=2)].append(
                    employee["name"]
                )  # Перенести на понеділок
            else:
                result[bd].append(employee["name"])
    return result


if __name__ == "__main__":
    for key, value in check_epl(employees).items():
        print(key.strftime("%A") + ": " + ", ".join(value))
