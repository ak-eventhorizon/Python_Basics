import re


def roman_validate(s: str) -> bool:
    """
    Функция получает строку и проверяет - является ли она валидным римским числом

    :param s:
    :return: bool
    """

    pattern = r'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

    if re.match(pattern, s):
        return True
    else:
        return False


if __name__ == '__main__':
    # True section
    print(roman_validate('I'))
    print(roman_validate('XI'))
    print(roman_validate('CDXXI'))
    print(roman_validate('MMXVIII'))
    print(roman_validate('MMMCMXCIX'))

    # False section
    print(roman_validate('IIX'))
    print(roman_validate('IXC'))
    print(roman_validate('CCCDXXI'))
    print(roman_validate('IM'))
    print(roman_validate('MXMMMMCMXCIX'))

    # user_input = input()
    # print(roman_validate(user_input))
