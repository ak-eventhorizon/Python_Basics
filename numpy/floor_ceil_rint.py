"""
FLOOR
The tool floor returns the floor of the input element-wise.

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.floor(my_array))  # [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]



CEIL
The tool ceil returns the ceiling of the input element-wise.

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.ceil(my_array))  # [  2.   3.   4.   5.   6.   7.   8.   9.  10.]



RINT
The rint tool rounds to the nearest integer of input element-wise.

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.rint(my_array))  # [  1.   2.   3.   4.   6.   7.   8.   9.  10.]



TASK
You are given a 1-D array. Your task is to print the floor, ceil and rint of all the elements of array.

Sample Input:
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

Sample Output:
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

"""
import numpy as np


def main(a: list) -> None:
    np_arr = np.array(a)

    print(np.floor(np_arr))
    print(np.ceil(np_arr))
    print(np.rint(np_arr))


if __name__ == '__main__':

    # # input for hackerrank
    # arr = list(map(float, input().strip().split()))

    arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
    main(arr) 
