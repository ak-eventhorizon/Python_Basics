def minion_game(string: str) -> None:
    """Игра определяющая у кого из двух игроков больше комбинаций из заданной строки

    Игрок 1 (Stuart) - получает очко за каждое вхождение в строку комбинации,
    начинающейся с согласной

    Игрок 2 (Kevin) - получает очко за каждое вхождение в строку комбинации,
    начинающейся с гласной

    Подход: количество подстрок, начинающихся с определенной буквы в строке равно
    длине подстроки от этой буквы до конца строки. Например, берем подстроку "ANANA"
    в стоке "BANANA". Количество подстрок в ней = 5:
    ANANA
    ANAN
    ANA
    AN
    A

    :param string: Строка (только большие буквы)"""

    score_kevin = 0  # гласные
    score_stuart = 0  # согласные

    for i in range(len(string)):
        if string[i] in 'AEIOU':
            score_kevin += len(string[i:])
        else:
            score_stuart += len(string[i:])

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
    minion_game('ABBA')  # -> Draw
