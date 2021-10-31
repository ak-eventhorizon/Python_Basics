import re


def telephone_validate(s: str) -> str:
    """
    Функция получает строку и проверяет - является ли она валидным номером телефона,
    такой номер содержит 10 цифр и начинается с 7,8,9

    :param s:
    :return: bool
    """

    pattern = r'^[789]\d{9}$'

    if re.match(pattern, s):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    # YES section
    print(telephone_validate('9587456281'))
    print(telephone_validate('7123211122'))

    # NO section
    print(telephone_validate('1252478965'))
    print(telephone_validate('81252478965'))
    print(telephone_validate('78965'))