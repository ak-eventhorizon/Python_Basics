"""
re.start() и re.end()
Возвращает индексы начала и окончания найденного совпадения по указанному паттерну.

m = re.search(r'\d+', '1234')
m.start()  --> 0
m.end()  --> 4
"""

import re


def main(string: str, substring: str) -> None:
    """
    Возвращает индексы начала и конца всех вхождений подстроки в строку.
    Совпадения перекрывающие, т.е. часть очередного совпадения может включать часть предыдущего:
    'aaa' --> два совпадения 'aa' 'aa'

    :param string:
    :param substring:
    :return:
    """
    pattern = re.compile(substring)
    occurs = pattern.search(string)

    if not occurs:
        print((-1, -1))

    while occurs:
        print(f'({occurs.start()}, {occurs.end() - 1})')
        occurs = pattern.search(string, occurs.start() + 1)


if __name__ == '__main__':
    # user_string = input()
    # user_substring = input()
    # main(user_string, user_substring)

    user_string1 = 'aaadaa'
    user_substring1 = 'aa'
    main(user_string1, user_substring1)

    print('')

    user_string2 = 'abbabbabbabba'
    user_substring2 = 'abba'
    main(user_string2, user_substring2)
