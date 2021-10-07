from itertools import combinations
"""
combinations(iter, r) - возвращает все комбинации длиной r из iter (в виде кортежей)
без повторяющихся элементов

print(list(combinations('1234', 2)))
>>> [('1', '2'), ('1', '3'), ('1', '4'), ('2', '3'), ('2', '4'), ('3', '4')]
"""


def show_combinations(s: str, k: int) -> None:

    sorted_str = sorted(s)

    for i in range(k):
        combs = combinations(sorted_str, i + 1)
        for comb in combs:
            print(''.join(comb))


if __name__ == '__main__':
    string, num = input().split()  # Пример ввода: HACK 2
    show_combinations(string, int(num))
