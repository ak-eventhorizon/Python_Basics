import re


def main():
    user_input = input()
    result = re.split(r'[,.]', user_input)
    [print(elem) for elem in result]


if __name__ == '__main__':
    main()

# INPUT:
# 100,05,4.30.56,5

# OUTPUT:
# 100
# 05
# 4
# 30
# 56
# 5
