﻿"""
MATHEMATICS

a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print(a + b)                     #[  6.   8.  10.  12.]
print(numpy.add(a, b))           #[  6.   8.  10.  12.]

print(a - b)                     #[-4. -4. -4. -4.]
print(numpy.subtract(a, b))      #[-4. -4. -4. -4.]

print(a * b)                     #[  5.  12.  21.  32.]
print(numpy.multiply(a, b))      #[  5.  12.  21.  32.]

print(a / b)                     #[ 0.2   0.33333333   0.42857143   0.5 ]
print(numpy.divide(a, b))        #[ 0.2   0.33333333   0.42857143   0.5 ]

print(a % b)                     #[ 1.  2.  3.  4.]
print(numpy.mod(a, b))           #[ 1.  2.  3.  4.]

print(a**b)                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print(numpy.power(a, b))         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]



TASK
You are given two integer arrays, A and B of dimensions MxN.
Your task is to perform the following operations:

Add (A + B)
Subtract (A - B)
Multiply (A * B)
Integer Division (A // B)
Mod (A % B)
Power (A ** B)


Input Format:
The first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array A.
The following N lines contains M space separated integers of array B.

Sample Input:
1 4
1 2 3 4
5 6 7 8

Sample Output:
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 

"""
import numpy as np


def main(arr1: list, arr2: list) -> None:
    
    a1 = np.array(arr1, int)
    a2 = np.array(arr2, int)
    
    print(a1 + a2)
    print(a1 - a2)
    print(a1 * a2)
    print(a1 // a2)
    print(a1 % a2)
    print(a1 ** a2)


if __name__ == '__main__':

    # input for hackerrank
    n, m = map(int, input().strip().split())
    arr1 = list()
    arr2 = list()
    
    for _ in range(n):
        arr1 += list(map(int, input().strip().split()))
    for _ in range(n):
        arr2 += list(map(int, input().strip().split()))
        
    main(arr1, arr2) 
