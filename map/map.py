"""
map() - применяет функцию (первый параметр) к каждому элементу итерируемого объекта (второй
параметр) и возвращает результат

print(list(map(len, ['Tina', 'Raj', 'Tom']))) --> [4, 3, 3]

print(list(map(lambda i: i*2, [1, 2, 3, 4]))) --> [2, 4, 6, 8]
"""


def fib(len_f: int):
    """
    Генератор для последовательности Фибоначчи длинной len_f
    """
    a, b = 0, 1
    for i in range(len_f):
        yield a
        a, b = b, a + b


def main(num: int) -> list:
    first_n_of_fibonacci = list(fib(num))
    return list(map(lambda x: x**3, first_n_of_fibonacci))


if __name__ == '__main__':
    n = int(input())
    print(main(n))
