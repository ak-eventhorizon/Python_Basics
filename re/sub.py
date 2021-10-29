"""
re.sub()
Проверяет строку на соответствие указанному паттерну и для каждого найденного совпадения
вызывает указанный метод (или lambda-функцию).
Возвращает модифицированную строку.

ПРИМЕР-1:
def square(match):
    number = int(match.group())  # group - возвращает фрагмент соответствующий рег. выражению
    return str(number**2)

print(re.sub(r'\d', square, '1 2 3 4 5'))  --> '1 4 9 16 25'

ПРИМЕР-2:
html = '''
<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
'''
print re.sub("(<!--.*?-->)", "", html)  # удаление комментариев в html

"""

import re


def main(s: str) -> str:
    """
    Функция получает строку и заменяет в ней символы:
    ' && ' --> ' and '
    ' || ' --> ' or '
    && и || должны иметь пробемы с обеих сторон

    :param s:
    :return:
    """
    current_string = s

    current_string = re.sub(r' && ', ' and ', current_string)
    current_string = re.sub(r' \|\| ', ' or ', current_string)
    # двойной прогон - на случай такого кейса 'n && && && && && &&n'
    # с одинарным получится так -> 'n and && and && and &&n'
    current_string = re.sub(r' && ', ' and ', current_string)
    current_string = re.sub(r' \|\| ', ' or ', current_string)

    return current_string


if __name__ == '__main__':

    input_strings = [
        'a = 1;',
        'b = input();',
        '',
        'if a + b > 0 && a - b < 0:',
        '    start()',
        'elif a * b > 10 || a / b < 1:',
        '    stop()',
        'print',
        'set(list(a)) | set(list(b))',
        '# Note do not change &&& or ||| or & or |',
        '# Only change those "&&" which have space on both sides.',
        '# Only change those "|| which have space on both sides.',
        'n && && && && && &&n'
    ]

    for string in input_strings:
        print(main(string))
