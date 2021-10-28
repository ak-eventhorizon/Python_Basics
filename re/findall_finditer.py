"""
re.findall()
Возвращает все совпадения с паттерном в строке или списке строк
re.findall(r't', 'http://:')  --> ['t', 't']
re.findall(r'\w', 'http://:')  --> ['h', 't', 't', 'p']

re.finditer()
Возвращает итератор, выдающий все совпадения с паттерном в строке или списке строк
list(map(lambda x: x.group(), re.finditer(r'\w', 'http://:')))  --> ['h', 't', 't', 'p']

"""

import re


def main(s: str) -> None:
    """
    Возвращает все вхождения последовательных гласных (две и более подряд),
    если они с обеих сторон окружены согласными.

    :param s:
    :return:
    """
    v = 'AEIOUaeiou'
    c = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'

    # using positive lookbehind (?<=) and positive lookahead (?=) patterns
    pattern = r'(?<=[' + c + '])([' + v + ']{2,})(?=[' + c + '])'

    occurs = re.findall(pattern, s)
    if occurs:
        [print(occur) for occur in occurs]
    else:
        print('-1')


if __name__ == '__main__':
    # user_string = input()

    user_string1 = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
    main(user_string1)

    user_string2 = 'dooo-'
    main(user_string2)
