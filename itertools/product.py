from itertools import product


def make_cartesian_product(first: str, second: str) -> None:

    first_list = [int(x) for x in first.split()]
    second_list = [int(x) for x in second.split()]

    result = product(first_list, second_list)

    for elem in result:
        print(elem, end=' ')


if __name__ == '__main__':
    a = input('A: ')  # space separated integers with no duplicates - 1 2 6
    b = input('B: ')  # space separated integers with no duplicates - 11 22 33
    make_cartesian_product(a, b)
