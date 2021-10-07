from collections import deque
"""
deque - двусторонняя последовательность. Можно добавлять, удалять и сдвигать 
элементы с обеих сторон.

d = deque()
d.append(1)         -> deque([1])
d.appendleft(2)     -> deque([2, 1])
d.clear()           -> deque([])
d.extend('12')      -> deque(['1', '2'])
d.extendleft('345') -> deque(['5', '4', '3', '1', '2'])
d.count('1')        -> 1
d.index('1')        -> 3
d.pop()             -> '2'  -> deque(['5', '4', '3', '1'])
d.popleft()         -> '5'  -> deque(['4', '3', '1'])
d.extend('789')     -> deque(['4', '3', '1', '7', '8', '9'])
d.remove('3')       -> deque(['4', '1', '7', '8', '9'])
d.reverse()         -> deque(['9', '8', '7', '1', '4'])
d.rotate(2)         -> deque(['1', '4', '9', '8', '7'])   (смещение вправо)
d.rotate(-2)        -> deque(['9', '8', '7', '1', '4'])   (смещение влево)
"""


def main():
    d = deque()

    num = int(input())

    for i in range(num):
        user_input = input().split()
        command = user_input[0]
        value = user_input[1] if len(user_input) > 1 else None

        if command == 'append':
            d.append(value)
        elif command == 'appendleft':
            d.appendleft(value)
        elif command == 'pop':
            d.pop()
        elif command == 'popleft':
            d.popleft()

    print(' '.join(d))


if __name__ == '__main__':
    main()
