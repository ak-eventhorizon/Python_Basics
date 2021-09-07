def staircase(n):
    for i in range(1, n+1):
        stair = '#'*i
        print(stair.rjust(n, ' '))


staircase(6)
