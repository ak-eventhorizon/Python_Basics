from itertools import combinations_with_replacement
"""
combinations_with_replacement(iterable, r) - возвращает итератор с комбинациями элементов
последовательности iterable с длинной r элементов, позволяя повторять в комбинациях отдельные 
элементы более одного раза (в отличии от метода combinations()). Каждая комбинация заключена в
кортеж длиной r элементов.

list(combinations_with_replacement('1234', 2)
>>> [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('2', '2'), ('2', '3'), ('2', '4'), ('3', '3'), ('3', '4'), ('4', '4')]

list(combinations('1234', 2)
>>> [('1', '2'), ('1', '3'), ('1', '4'), ('2', '3'), ('2', '4'), ('3', '4')]
"""


def main(s: str, num: int) -> None:

    string = ''.join(sorted(s))  # 'ACHK'
    my_list = list(combinations_with_replacement(string, num))

    [print(''.join(i)) for i in my_list]


if __name__ == '__main__':
    user_input = input().split()  # HACK 2
    main(user_input[0], int(user_input[1]))
