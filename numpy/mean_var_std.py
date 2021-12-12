"""
MEAN
The mean tool computes the arithmetic mean along the specified axis.
By default, the axis is None. Therefore, it computes the mean of the flattened array.

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.mean(my_array, axis = 0))        #Output : [ 2.  3.]
print(numpy.mean(my_array, axis = 1))        #Output : [ 1.5  3.5]
print(numpy.mean(my_array, axis = None))     #Output : 2.5
print(numpy.mean(my_array))                  #Output : 2.5


VAR
The var tool computes the arithmetic variance along the specified axis.
By default, the axis is None. Therefore, it computes the variance of the flattened array.

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.var(my_array, axis = 0))         #Output : [ 1.  1.]
print(numpy.var(my_array, axis = 1))         #Output : [ 0.25  0.25]
print(numpy.var(my_array, axis = None))      #Output : 1.25
print(numpy.var(my_array))                   #Output : 1.25


STD
The std tool computes the arithmetic standard deviation along the specified axis.
By default, the axis is None. Therefore, it computes the standard deviation of the flattened array.

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.std(my_array, axis = 0))         #Output : [ 1.  1.]
print(numpy.std(my_array, axis = 1))         #Output : [ 0.5  0.5]
print(numpy.std(my_array, axis = None))      #Output : 1.11803398875
print(numpy.std(my_array))                   #Output : 1.11803398875


TASK
You are given a 2-D array of size NxM.
Your task is to find:
1 - The mean along axis 1
2 - The var along axis 0
3 - The std along axis None

Input Format
The first line of input contains space separated values of N and M.
The next N lines contains M space separated integers.

Output Format
First, print the mean.
Second, print the var.
Third, print the std.

Sample Input:
2 2
1 2
3 4

Sample Output:
[ 1.5  3.5]
[ 1.  1.]
1.11803398875


"""
import numpy as np


def main(a: list) -> None:
    np_arr = np.array(a)

    print(np.mean(np_arr, axis=1))
    print(np.var(np_arr, axis=0))
    print(np.std(np_arr, axis=None))


if __name__ == '__main__':

    # # input for hackerrank
    # n, m = list(map(int, input().strip().split()))
    # arr = list()
    # for _ in range(n):
    #     arr.append(list(map(int, input().strip().split())))

    arr = [[1, 2], [3, 4]]
    
    main(arr) 
