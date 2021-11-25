"""
SHAPE
The shape tool returns a tuple of array dimensions and can be used to change the dimensions of an array.

my_1D_arr = numpy.array([1, 2, 3, 4, 5])
my_1D_arr.shape  # -> (5,) -> 1 row and 5 columns

my_2D_arr = numpy.array([[1, 2],[3, 4],[6,5]])
my_2D_arr.shape  # -> (3,2) -> 3 rows and 2 columns 

my_arr = numpy.array([1, 2, 3, 4, 5, 6])
my_arr.shape = (3,2)
print(my_arr)  #    [[1 2]
                    [3 4]
                    [5 6]]

RESHAPE
The reshape tool gives a new shape to an array without changing its data. 
It creates a new array and does not modify the original array itself.

my_2D_arr = numpy.array([[1, 2],[3, 4],[5, 6]])
new_arr = my_2D_arr.reshape(3,2)
print(new_arr)  #   [[1 2 3]
                    [4 5 6]]


TASK:
You are given a space separated list of nine integers. 
Your task is to convert this list into a 3X3 NumPy array.
"""
import numpy as np


def main(arr: list, row: int, col: int):
    np_arr = np.array(arr)
    return np_arr.reshape(row, col)


if __name__ == '__main__':
    user_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(main(user_arr, 3, 3))
