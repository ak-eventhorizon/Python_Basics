"""
CONCATENATE
Two or more arrays can be concatenated together using the concatenate 
function with a tuple of the arrays to be joined:

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print(numpy.concatenate((array_1, array_2, array_3)))    

#Output
[1 2 3 4 5 6 7 8 9]



If an array has more than one dimension, it is possible to specify the axis 
along which multiple arrays are concatenated. By default, it is along the first dimension:

array_1 = numpy.array([[1,2,3],[4,5,6]])
array_2 = numpy.array([[7,8,9],[10,11,12]])

print(numpy.concatenate((array_1, array_2), axis = 1))   

#Output
[[1 2 3 7 8 9]
 [4 5 6 10 11 12]]    



TASK:
You are given two integer arrays of size NxP and MxP (N & M are rows, and P is the column).
Your task is to concatenate the arrays along axis 0.

Input Format:
The first line contains space separated integers N, M and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

Output Format:
Print the concatenated array of size (N+M)xP.

Sample Input:
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 

Sample Output:
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
"""
import numpy as np


def main(arr1: list, arr2: list) -> None:
    
    a1 = np.array(arr1)
    a2 = np.array(arr2)

    print(np.concatenate((a1, a2), axis = 0)) 


if __name__ == '__main__':

    # input for hackerrank
    #n, m, p = map(int, input().strip().split())
    #user_arr1 = list()
    #user_arr2 = list()

    #for _ in range(n):
    #    user_arr1.append(list(map(int, input().strip().split())))

    #for _ in range(m):
    #    user_arr2.append(list(map(int, input().strip().split())))


    user_arr1 = [[1, 2], [1, 2], [1, 2], [1, 2]]
    user_arr2 = [[3, 4], [3, 4], [3, 4]]

    main(user_arr1, user_arr2) 
