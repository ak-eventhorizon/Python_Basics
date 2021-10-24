"""
any() - возвращает True если хотя бы один элемент из итерируемого аргумента является истинным
any([1 == 0, 1 > 5, 1 > 0])  --> True
any([])  --> False

all() - возвращает True если все элементы из итерируемого аргумента являются истинными
all([0 == 0, 5 > 1, 1 > 0])  --> True
all([])  --> True
"""


def is_palindromic(string: str) -> bool:
    return string == string[::-1]


def main():
    integers = list(map(int, input().split()))

    condition_1 = all([elem > 0 for elem in integers])  # все числа положительные
    condition_2 = any([is_palindromic(str(elem)) for elem in integers])  # есть хоть один палиндром

    print(condition_1 and condition_2)


if __name__ == '__main__':
    n = int(input())  # не требуется для решения, требуется только по условиям задачи
    main()
