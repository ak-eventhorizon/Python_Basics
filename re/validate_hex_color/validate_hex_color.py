import re


def hex_colors_in_string(s: str) -> list:
    """
    Specifications of HEX Color Code:
    - It must start with a '#' symbol.
    - It can have 3 or 6 digits.
    - Each digit is in the range of 0 to F (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F).
    - letters can be higher or lower case

    Valid Hex Color Codes:
    #FFF
    #025
    #F0A1FB

    Invalid Hex Color Codes:
    #fffabg
    #abcf
    #12365erff

    CSS Code Pattern:
    Selector
    {
        Property: Value;
    }

    :param s: входная строка
    :return: список из валидных hex кодов в строке
    """

    pattern = r'(?<!^)(#(?:[0-9a-fA-F]{3}){1,2})'
    result = re.findall(pattern, s)
    return result


if __name__ == '__main__':

    # Блок с формированием входных данных из файла
    with open('validate_hex_color.txt', 'r') as f:
        lines = f.read().splitlines()

    results = list()

    for line in lines:
        if hex_colors_in_string(line):
            results += hex_colors_in_string(line)

    [print(result) for result in results]
