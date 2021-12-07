"""
INNER
The inner tool returns the inner product of two arrays.

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print(numpy.inner(A, B))     #Output : 4


OUTER
The outer tool returns the outer product of two arrays.

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print(numpy.outer(A, B))     #Output : [[0 0]
                             #          [3 4]]

TASK
You are given two arrays: A and B.
Your task is to compute their inner and outer product.

Input Format
The first line contains the space separated elements of array A.
The second line contains the space separated elements of array B.

Output Format
First, print the inner product.
Second, print the outer product.

Sample Input:
0 1
2 3

Sample Output:
3
[[0 0]
 [2 3]]


"""
import numpy as np


def main(a: list, b: list) -> None:
    np_arr_a = np.array(a)
    np_arr_b = np.array(b)

    print(np.inner(np_arr_a, np_arr_b))
    print(np.outer(np_arr_a, np_arr_b))


if __name__ == '__main__':

    # # input for hackerrank
    # arr_a = list(map(int, input().strip().split()))
    # arr_b = list(map(int, input().strip().split()))

    arr_a = [0, 1]
    arr_b = [2, 3]
    
    main(arr_a, arr_b) 
