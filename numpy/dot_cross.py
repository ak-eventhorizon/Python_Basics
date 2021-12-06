"""
DOT
The dot tool returns the dot product of two arrays.

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print(numpy.dot(A, B))       #Output : 11


CROSS
The cross tool returns the cross product of two arrays.


A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print(numpy.cross(A, B))     #Output : -2


TASK
You are given two arrays A and B. Both have dimensions of NxN.
Your task is to compute their matrix product.

Input Format
The first line contains the integer N.
The next N lines contains N space separated integers of array A.
The following N lines contains N space separated integers of array B.

Output Format
Print the matrix multiplication of A and B.

Sample Input:
2
1 2
3 4
1 2
3 4

Sample Output:
[[ 7 10]
 [15 22]]


"""
import numpy as np


def main(a: list, b: list) -> None:
    np_arr_a = np.array(a)
    np_arr_b = np.array(b)

    print(np.dot(np_arr_a, np_arr_b))


if __name__ == '__main__':

    # # input for hackerrank
    # n = int(input().strip())
    # arr_a = list()
    # arr_b = list()
    # for _ in range(n):
    #     arr_a.append(list(map(int, input().strip().split())))
    # for _ in range(n):
    #     arr_b.append(list(map(int, input().strip().split())))

    arr_a = [[1, 2], [3, 4]]
    arr_b = [[1, 2], [3, 4]]
    
    main(arr_a, arr_b) 
