"""
Пример ввода для программы:

3
odd 2
even 3
odd 5
"""


class EvenStream:
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


class OddStream:
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())


if __name__ == '__main__':
    queries = int(input())
    for _ in range(queries):
        stream_name, num = input().split()
        num = int(num)
        if stream_name == "even":
            print_from_stream(num)
        else:
            print_from_stream(num, OddStream())
