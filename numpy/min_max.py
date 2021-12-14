"""
MIN
The tool min returns the minimum value along a given axis.
By default, the axis value is None. Therefore, it finds the minimum over all the dimensions of the input array.

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print(numpy.min(my_array, axis = 0))         #Output : [1 0]
print(numpy.min(my_array, axis = 1))         #Output : [2 3 1 0]
print(numpy.min(my_array, axis = None))      #Output : 0
print(numpy.min(my_array))                   #Output : 0


MAX
The tool max returns the maximum value along a given axis.
By default, the axis value is None. Therefore, it finds the maximum over all the dimensions of the input array.

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print(numpy.max(my_array, axis = 0))         #Output : [4 7]
print(numpy.max(my_array, axis = 1))         #Output : [5 7 3 4]
print(numpy.max(my_array, axis = None))      #Output : 7
print(numpy.max(my_array))                   #Output : 7


TASK
You are given a 2-D array with dimensions NxM.
Your task is to perform the min function over axis 1 and then find the max of that.

Input Format
The first line of input contains space separated values of N and M.
The next N lines contains M space separated integers.

Output Format
Compute the min along axis 1 and then print the max of that result.

Sample Input:
4 2
2 5
3 7
1 3
4 0

Sample Output:
3


"""
import numpy as np


def main(a: list) -> None:
    np_arr = np.array(a)

    min_along_axis_1 = np.min(np_arr, axis=1)
    print(np.max(min_along_axis_1))


if __name__ == '__main__':

    # # input for hackerrank
    # n, m = list(map(int, input().strip().split()))
    # arr = list()
    # for _ in range(n):
    #     arr.append(list(map(int, input().strip().split())))

    arr = [[2, 5], [3, 7], [1, 3], [4, 0]]
    
    main(arr) 
