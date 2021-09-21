class Player:
    """Player for a minion game

    side: \n
    'c' - consonants (согласные) \n
    'v' - vowels (гласные) \n

    Подход: количество подстрок, начинающихся с определенной буквы в строке равно
    длине подстроки от этой буквы до конца строки. Например, берем подстроку "ANANA"
    в стоке "BANANA". Количество подстрок в ней = 5:
    ANANA
    ANAN
    ANA
    AN
    A
    """

    def __init__(self, string, side):
        self.string = string
        self.side = side  # 'c' - consonants (согласные) or 'v' - vowels (гласные)
        self.score = 0
        self.calculate_score()

    def calculate_score(self):
        for i in range(len(self.string)):
            if self.side == 'v' and self.string[i] in 'AEIOU':
                self.score += len(self.string[i:])
            elif self.side == 'c' and self.string[i] not in 'AEIOU':
                self.score += len(self.string[i:])


def minion_game(string: str) -> None:

    kevin = Player(string, 'v')
    stuart = Player(string, 'c')

    if kevin.score > stuart.score:
        print('Kevin', kevin.score)
    elif kevin.score < stuart.score:
        print('Stuart', stuart.score)
    else:
        print('Draw')


if __name__ == '__main__':
    minion_game('BANANA')  # -> Stuart 12
    minion_game('BAAA')  # -> Kevin 6
    minion_game('CRUSIFICTIONATION')  # -> Stuart 89
    minion_game('ABBA')  # -> Draw
