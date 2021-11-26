"""
TRANSPOSE
We can generate the transposition of an array using the tool transpose.
It will not affect the original array, but it will create a new array.

my_array = numpy.array([[1, 2, 3], [4, 5, 6]])
print numpy.transpose(my_array)

#Output
[[1 4]
 [2 5]
 [3 6]]


FLATTEN
The tool flatten creates a copy of the input array flattened to one dimension.

my_array = numpy.array([[1, 2, 3], [4, 5, 6]])
print my_array.flatten()

#Output
[1 2 3 4 5 6]


TASK:
You are given a N X M integer array matrix with space separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.

Input:
The first line contains the space separated values of N and M.
The next N lines contains the space separated elements of M columns.

Sample Input
2 2
1 2
3 4

Sample Output
[[1 3]
 [2 4]]
[1 2 3 4]
"""
import numpy as np


def main(arr: list) -> None:
    
    my_arr = np.array(arr)
    transposed_arr = np.transpose(my_arr)
    flatten_arr = my_arr.flatten()

    print(transposed_arr)
    print(flatten_arr)


if __name__ == '__main__':

    # # input for hackerrank
    # n, m = map(int, input().strip().split())
    # user_arr = list()

    # for _ in range(n):
    #     user_arr.append(list(map(int, input().strip().split())))

    user_arr = [[1, 2], [3, 4]]

    main(user_arr)
