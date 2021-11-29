"""
ZEROS
The zeros tool returns a new array with a given shape and type filled with 0's.

print(numpy.zeros((1,2)))  # Default type is float
#Output : [[ 0.  0.]] 

print(numpy.zeros((1,2), dtype = int))  # Type changes to int
#Output : [[0 0]]



ONES
The ones tool returns a new array with a given shape and type filled with 1's.

print(numpy.ones((1,2)))  # Default type is float
#Output : [[ 1.  1.]] 

print(numpy.ones((1,2), dtype = int))  # Type changes to int
#Output : [[1 1]]   


TASK:
You are given the shape of the array in the form of space-separated integers,
each integer representing the size of different dimensions, your task is to print an array
of the given shape and integer type using the tools numpy.zeros and numpy.ones.

Sample Input:
3 3 3

Sample Output:
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]

"""
import numpy as np


def main(args_list: list) -> None:
    
    print(np.zeros(args_list, dtype = int))
    print(np.ones(args_list, dtype = int))
    

if __name__ == '__main__':

    # input for hackerrank
    # dimensions = list(map(int, input().strip().split()))
    
    dimensions = [3, 4, 5]

    main(dimensions)
