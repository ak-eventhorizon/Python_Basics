def infinite_sequence(start: int):
    """
    Генератор бесконечной последовательности, начиная с числа start
    На практике такой подход не используется, поскольку в стандартной
    библиотеке есть itertools.count()
    """
    num = start
    while True:
        yield num
        num += 1


def finite_sequence():
    yield 'first'
    yield 'second'
    yield 'last'


if __name__ == '__main__':
    counter_from_5 = infinite_sequence(5)
    print(next(counter_from_5))  # 5
    print(next(counter_from_5))  # 6
    print(next(counter_from_5))  # 7

    # используем генератор для бесконечного цикла по нему (принудительно ограничиваем 50 итераций)
    for i in infinite_sequence(0):
        print(i, end=' ')
        if i == 50:
            break

    # использование генератора с ограниченным количеством использований, на четверный раз
    # вернется ошибка, поскольку в функции только три yield-а
    print()
    gen = finite_sequence()
    print(next(gen))  # 'first'
    print(next(gen))  # 'second'
    print(next(gen))  # 'last'
    print(next(gen))  # будет ошибка StopIteration
