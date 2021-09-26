from itertools import permutations


def show_permutations():
    string, length = input('Input "STRING <space> num": ').split()
    result = permutations(string, int(length))

    for elem in result:
        print(''.join(elem))


if __name__ == '__main__':
    show_permutations()

# Input:
# HACK 2

# Output:
# HA
# HC
# HK
# AH
# AC
# AK
# CH
# CA
# CK
# KH
# KA
# KC
