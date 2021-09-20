class Player:
    """Player for a minion game

    side: \n
    'c' - consonants (согласные) \n
    'v' - vowels (гласные)
    """

    def __init__(self, string, side):
        self.string = string
        self.all_substrings = list()
        self.player_substrings = set()
        self.side = side  # 'c' - consonants (согласные) or 'v' - vowels (гласные)
        self.score = 0

        self.set_all_substrings()
        self.set_player_substrings()
        self.calculate_score()

    def set_all_substrings(self):
        self.all_substrings = [
            self.string[i:j]
            for i in range(len(self.string))
            for j in range(i + 1, len(self.string) + 1)
        ]

    def set_player_substrings(self):
        for substring in self.all_substrings:
            if self.side == 'v' and substring[0] in 'AEIOU':
                self.player_substrings.add(substring)
            elif self.side == 'c' and substring[0] not in 'AEIOU':
                self.player_substrings.add(substring)

    def calculate_score(self):
        for substring in self.player_substrings:
            self.score += self.all_substrings.count(substring)


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
    minion_game('ABBA')  # -> DRAW!
