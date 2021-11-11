"""
Decorator usage example.

You are given list of mobile numbers.
Sort them in ascending order then print them in the standard format shown below:

+91 xxxxx xxxxx

The given mobile numbers may have +91, 91 or 0 written before the actual 10-digit number.
Alternatively, there may not be any prefix at all.
"""


def numbers_formatter(func):
    def inner(*args):
        # обрезание элементов - оставляем последние 10 цифр
        sliced_to_10_digits = [i[-10:] for i in args[0]]

        # форматирование элементов по шаблону +91 xxxxx xxxxx
        formatted = [f'+91 {i[0:5]} {i[5:]}' for i in sliced_to_10_digits]

        func(formatted)

    return inner


@numbers_formatter
def sort_phone(lst):
    print(*sorted(lst), sep='\n')


if __name__ == '__main__':
    inputs = ['07895462130', '919875641230', '9195969878', '+911234567890']

    sort_phone(inputs)
