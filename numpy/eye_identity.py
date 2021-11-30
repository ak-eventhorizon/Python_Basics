"""
IDENTITY
The identity tool returns an identity array. 
An identity array is a square matrix with all the main diagonal elements as 1 and the rest as 0.
The default type of elements is float.

print(numpy.identity(3))  # 3 is for dimension 3 X 3

#Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]



EYE
The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. 
The diagonal can be main, upper or lower depending on the optional parameter k. 
A positive k is for the upper diagonal, a negative k is for the lower, and a k=0 (default) is for the main diagonal.

print(numpy.eye(5, 5, k=1))  # 5 X 5 Dimensional array with first upper diagonal 1.

#Output
[[0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]
 [0. 0. 0. 0. 0.]]

"""
import numpy as np


def main(d1, d2) -> None:
    
    print(np.eye(d1,d2))
    

if __name__ == '__main__':

     # input for hackerrank
     r, c = map(int, input().strip().split())
     
     main(r,c) 
