from itertools import groupby


def main(s: str) -> None:

    result = list()

    for key, group_item in groupby(s):
        counter = 0
        for i in group_item:
            counter += 1

        result.append((counter, key))

    [print(i, end=' ') for i in result]


if __name__ == '__main__':
    # main('1222311')  # (1, '1') (3, '2') (1, '3') (2, '1')
    main('aaabbbbccdeeeee')  # (3, 'a') (4, 'b') (2, 'c') (1, 'd') (5, 'e')
