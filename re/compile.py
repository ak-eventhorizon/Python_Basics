import re
"""
re.compile - превращает паттерн (в строковом представлении) в regular expression object, 
который в дальнейшем можно использовать для методов match(), search(), findall() и др.

если передается не валидный паттерн - выбрасывается исключение re.error
"""


def regexp_validate(string: str) -> bool:
    try:
        re.compile(string)
        re_is_valid = True
    except re.error:
        re_is_valid = False

    return re_is_valid


if __name__ == '__main__':
    num_cases = int(input())
    patterns = [input() for i in range(num_cases)]

    for pattern in patterns:
        print(regexp_validate(pattern))

# .*\+    -> True
# .*+     -> False
