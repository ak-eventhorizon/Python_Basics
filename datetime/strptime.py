from datetime import datetime


def time_delta(t1: str, t2: str) -> None:
    """
    Выводит разницу между двумя датами (в секундах).

    Используется метод strptime() - преобразует строку в объект timedate.

    Разбор строки производится по указанному формату:
    https://www.journaldev.com/23365/python-string-to-datetime-strptime

    :param t1: 'Sat 02 May 2015 19:54:36 +0530'
    :param t2: 'Fri 01 May 2015 13:54:36 -0000'
    :return:
    """

    t1_datetime_obj = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2_datetime_obj = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

    delta = t1_datetime_obj.timestamp() - t2_datetime_obj.timestamp()  # timestamp преобразует дату в количество секунд

    print(abs(int(delta)))  # разница выводится по абсолютному значению (без отрицательных)


if __name__ == '__main__':
    time_delta('Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000')  # 25200
    time_delta('Sat 02 May 2015 19:54:36 +0530', 'Fri 01 May 2015 13:54:36 -0000')  # 88200
