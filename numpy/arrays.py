"""
A NumPy array is a grid of values. 
They are similar to lists, except that every element of an array must be the same type.

You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.

Input:
1 2 3 4 -8 -10

Output:
[-10.  -8.   4.   3.   2.   1.]  -- reverse numpy array with float type
"""
import numpy as np


def arrays(a: list) -> list:

    a.reverse()
    np_arr = np.array(a, float)
    return np_arr


if __name__ == '__main__':

    arr = [1, 2, 3, 4, -8, -10]
    print(arrays(arr))
