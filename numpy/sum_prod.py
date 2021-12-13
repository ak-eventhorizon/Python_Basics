﻿"""
SUM
The sum tool returns the sum of array elements over a given axis.
By default, the axis value is None. Therefore, it performs a sum over all the dimensions of the input array.

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.sum(my_array, axis = 0))         #Output : [4 6]
print(numpy.sum(my_array, axis = 1))         #Output : [3 7]
print(numpy.sum(my_array, axis = None))      #Output : 10
print(numpy.sum(my_array))                   #Output : 10


PROD
The prod tool returns the product of array elements over a given axis.
By default, the axis value is None. Therefore, it performs the product over all the dimensions of the input array.

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.prod(my_array, axis = 0))            #Output : [3 8]
print(numpy.prod(my_array, axis = 1))            #Output : [ 2 12]
print(numpy.prod(my_array, axis = None))         #Output : 24
print(numpy.prod(my_array))                      #Output : 24

TASK
You are given a 2-D array with dimensions NxM.
Your task is to perform the sum tool over axis 0 and then find the product of that result.

Input Format
The first line of input contains space separated values of N and M.
The next N lines contains M space separated integers.

Output Format
Compute the sum along axis 0. Then, print the product of that sum.

Sample Input:
2 2
1 2
3 4

Sample Output:
24


"""
import numpy as np


def main(a: list) -> None:
    np_arr = np.array(a)

    sum_along_axis_0 = np.sum(np_arr, axis=0)
    print(np.prod(sum_along_axis_0))


if __name__ == '__main__':

    # # input for hackerrank
    # n, m = list(map(int, input().strip().split()))
    # arr = list()
    # for _ in range(n):
    #     arr.append(list(map(int, input().strip().split())))

    arr = [[1, 2], [3, 4]]
    
    main(arr) 