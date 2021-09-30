import calendar


def day_checker(year: str, month: str, day: str) -> None:
    """
    По дате вычисляется какой это день недели
    """

    days = [name.upper() for name in calendar.day_name]
    weekday_num = calendar.weekday(int(year), int(month), int(day))

    print(days[weekday_num])


if __name__ == '__main__':
    m, d, y = input("MM DD YYYY: ").split()
    day_checker(y, m, d)
