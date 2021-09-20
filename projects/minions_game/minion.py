def minion_game(string: str) -> None:
    """Игра определяющая у кого из двух игроков больше комбинаций из заданной строки

    Игрок 1 (Stuart) - получает очко за каждое вхождение в строку комбинации,
    начинающейся с согласной

    Игрок 2 (Kevin) - получает очко за каждое вхождение в строку комбинации,
    начинающейся с гласной

    :param string: Строка (только большие буквы)"""

    score_kevin = 0
    score_stuart = 0
    kevin_substrings = set()
    stuart_substrings = set()

    #  все возможные подстроки в строке
    all_substrings = [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]

    for substring in all_substrings:
        if substring[0] in 'AEIOU':
            kevin_substrings.add(substring)
        else:
            stuart_substrings.add(substring)

    for substring in kevin_substrings:
        score_kevin += all_substrings.count(substring)

    for substring in stuart_substrings:
        score_stuart += all_substrings.count(substring)

    if score_kevin == score_stuart:
        print('Draw')
    elif score_kevin > score_stuart:
        print('Kevin', score_kevin)
    else:
        print('Stuart', score_stuart)


if __name__ == '__main__':
    minion_game('BANANA')  # -> Stuart 12
    minion_game('BAAA')  # -> Kevin 6
    minion_game('CRUSIFICTIONATION')  # -> Stuart 89
    minion_game('ABBA')  # -> DRAW!
