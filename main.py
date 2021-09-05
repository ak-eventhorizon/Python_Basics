# print('hello pyCharm')

if __name__ == '__main__':
    N = int(input())
    my_list = list()

    for i in range(N):
        user_input = input().split(' ')
        command = user_input[0]
        args = user_input[1:]
        args = [int(elem) for elem in args]

        if command == 'insert':
            my_list.insert(args[0], args[1])
        elif command == 'print':
            print(my_list)
        elif command == 'remove':
            my_list.remove(args[0])
        elif command == 'append':
            my_list.append(args[0])
        elif command == 'sort':
            my_list.sort()
        elif command == 'pop':
            my_list.pop()
        elif command == 'reverse':
            my_list.reverse()
