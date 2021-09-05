# print('hello pyCharm')

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    print(hash(tuple(integer_list)))

# 3713081631934410656

# print(input() == 0 or hash(tuple([int(x) for x in (input().strip().split())])))